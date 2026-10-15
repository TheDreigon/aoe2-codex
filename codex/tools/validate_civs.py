"""Validate the civ design files in codex/civs/*.toml.

Usage (from the repository root):
    python -I codex/tools/validate_civs.py [FILE ...]      validate the given files (default: all)
    python -I codex/tools/validate_civs.py --tree CIV      print the current tree of a civ (internal name)
    python -I codex/tools/validate_civs.py --find NAME     list the civs that currently have an item
    python -I codex/tools/validate_civs.py --names         list every unit, tech and building name

Checks the structure described in codex/civs/README.md and codex/RULES.md (sections 6 and 8):
composition (4-6 bonuses with at least one economic and one military, one team bonus, two unique
techs for Castle and Imperial Age, at least one unique unit), required fields, level-1 constraints
that can be checked mechanically (item names exist in the game, architecture set exists) and
whether every original bonus, unique unit and unique tech is accounted for.
Errors make the exit code 1; warnings do not.
"""
import json
import re
import sys
import tomllib
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CIVS_DIR = ROOT / 'codex' / 'civs'
OUT_OF_SCOPE = {'Shu', 'Wei', 'Wu', 'Romans'}
# Items whose help text has no bold name: internal name -> displayed name.
ALIASES = {
    'RATHA': 'Ratha', 'RATHA2': 'Ratha', 'ERATHA': 'Elite Ratha', 'ERATHA2': 'Elite Ratha',
    'KONNIK_INF': 'Konnik', 'EKONNIK_INF': 'Elite Konnik', 'TREBU': 'Trebuchet', 'WARCHAR': 'War Chariot',
}
ARCHITECTURE_SETS = {
    'African', 'Central American', 'Central Asian', 'Central European', 'East Asian', 'Eastern European',
    'Mediterranean', 'Middle Eastern', 'Northern European', 'South American', 'South Asian',
    'Southeast Asian', 'Western European',
}
KINDS = {'economic', 'military', 'other'}
CHANGES = {'kept', 'changed', 'new'}
DROPPED_KINDS = {'bonus', 'team_bonus', 'unique_unit', 'unique_tech', 'unique_building', 'tree', 'other'}


def load_game():
    d = json.loads((ROOT / 'data' / 'data.json').read_text(encoding='utf-8'))
    s = json.loads((ROOT / 'data' / 'locales' / 'en' / 'strings.json').read_text(encoding='utf-8'))
    names = {}
    for kind in ('Unit', 'Tech', 'Building'):
        for i, x in d['data'][kind].items():
            help_text = s.get(str(x['LanguageNameId'] + 21000)) or ''
            m = re.search(r'<b>(.+?)</b>', help_text)
            internal = x.get('internal_name', str(i))
            names[(kind, int(i))] = m.group(1) if m else ALIASES.get(internal, internal)
    trees = {}
    for civ, c in d['civs'].items():
        trees[civ] = {names[(k, i)]: k for k in ('Unit', 'Tech', 'Building') for i in c[k] if (k, i) in names}
    help_texts = {civ: s.get(str(c['help_string_id']), '') for civ, c in d['civs'].items()}
    all_names = defaultdict(set)
    for (k, _), n in names.items():
        all_names[n].add(k)
    return trees, help_texts, all_names


def original_elements(help_text):
    """Split a civ help text into bonuses, unique units, unique techs and team bonus."""
    t = re.sub(r'<br>', '\n', help_text)
    t = re.sub(r'<[^>]+>', '', t)
    lines = [x.strip() for x in t.splitlines() if x.strip()]
    out = {'bonus': [], 'unique_unit': [], 'unique_tech': [], 'team_bonus': []}
    section = 'bonus'
    for line in lines[1:]:
        low = line.lower()
        if low.startswith('unique unit'):
            section = 'unique_unit'
            continue
        if low.startswith('unique tech'):
            section = 'unique_tech'
            continue
        if low.startswith('team bonus'):
            section = 'team_bonus'
            continue
        bullet = line.startswith('•')
        line = line.lstrip('•').strip()
        if section in ('bonus', 'team_bonus') and not bullet and out[section]:
            out[section][-1] += ' ' + line  # a bonus wrapped over two lines
            continue
        if section == 'unique_unit':
            out[section] += [re.sub(r'\s*\(.*?\)\s*$', '', u).strip() for u in re.split(r',\s*(?![^()]*\))', line)]
        elif section == 'unique_tech':
            out[section].append(re.sub(r'\s*\(.*\)\s*$', '', line).strip())
        else:
            out[section].append(line)
    return out


def norm(x):
    x = re.sub(r'[^a-z0-9%/+-]+', ' ', x.lower())
    return re.sub(r'\s*/\s*', '/', x).strip()


class Report:
    def __init__(self, path):
        self.path = path
        self.errors, self.warnings = [], []

    def err(self, msg):
        self.errors.append(msg)

    def warn(self, msg):
        self.warnings.append(msg)


def need(r, table, keys, where):
    for k in keys:
        v = table.get(k)
        if v is None or (isinstance(v, (str, list)) and not v):
            r.err(f'{where}: missing or empty "{k}"')


def check_level(r, table, where):
    if table.get('level') != 1:
        r.err(f'{where}: level must be 1 in a level-1 design (got {table.get("level")!r})')


def validate(path, game):
    trees, help_texts, all_names = game
    r = Report(path)
    try:
        doc = tomllib.loads(path.read_text(encoding='utf-8'))
    except tomllib.TOMLDecodeError as exc:
        r.err(f'TOML parse error: {exc}')
        return r, None
    need(r, doc, ['civ', 'name', 'status', 'label', 'summary'], 'top level')
    civ = doc.get('civ', '')
    if civ not in trees:
        r.err(f'civ "{civ}" is not an internal civ name in data/data.json')
        return r, doc
    if civ in OUT_OF_SCOPE:
        r.err(f'civ "{civ}" is out of scope')
    if doc.get('status') not in ('draft', 'reviewed', 'approved'):
        r.err('status must be draft, reviewed or approved')
    expected_file = re.sub(r'[^A-Za-z0-9]+', '', doc.get('name', '')) + '.toml'
    if path.name != expected_file:
        r.warn(f'file name should be {expected_file} (the displayed name without spaces or punctuation)')
    for key in ('ideas', 'contested', 'open_questions'):
        v = doc.get(key, [])
        if not isinstance(v, list) or not all(isinstance(x, str) and x.strip() for x in v):
            r.err(f'"{key}" must be a list of non-empty strings')
    for idea in doc.get('ideas', []):
        if not re.match(r'^N[23]\b', idea):
            r.err(f'idea must start with its level (N2 or N3): {idea[:60]!r}')

    prof = doc.get('profile', {})
    need(r, prof, ['entity', 'region', 'window', 'sources'], '[profile]')
    if not isinstance(prof.get('sources', []), list):
        r.err('[profile] sources must be a list')

    bonuses = doc.get('bonus', [])
    if not 4 <= len(bonuses) <= 6:
        r.err(f'{len(bonuses)} bonuses; RULES 6.1 asks for 4 to 6')
    kinds = Counter(b.get('kind') for b in bonuses)
    if not kinds['economic']:
        r.err('no economic bonus (RULES 6.1)')
    if not kinds['military']:
        r.err('no military bonus (RULES 6.1)')
    for n, b in enumerate(bonuses, 1):
        w = f'[[bonus]] #{n}'
        need(r, b, ['text', 'kind', 'change', 'precedent', 'basis'], w)
        check_level(r, b, w)
        if b.get('kind') not in KINDS:
            r.err(f'{w}: kind must be one of {sorted(KINDS)}')
        if b.get('change') not in CHANGES:
            r.err(f'{w}: change must be one of {sorted(CHANGES)}')

    tb = doc.get('team_bonus')
    if not isinstance(tb, dict):
        r.err('exactly one [team_bonus] table is required')
    else:
        need(r, tb, ['text', 'change', 'precedent', 'basis'], '[team_bonus]')
        check_level(r, tb, '[team_bonus]')
        if tb.get('change') not in CHANGES:
            r.err('[team_bonus]: change must be one of kept, changed, new')

    uus = doc.get('unique_unit', [])
    if not uus:
        r.err('at least one [[unique_unit]] is required')
    for n, u in enumerate(uus, 1):
        w = f'[[unique_unit]] {u.get("name", n)}'
        need(r, u, ['name', 'model', 'change', 'basis'], w)
        check_level(r, u, w)
        if u.get('change') not in CHANGES:
            r.err(f'{w}: change must be one of kept, changed, new')
        if u.get('model') and u['model'] not in all_names:
            r.err(f'{w}: model "{u["model"]}" is not an existing unit or building name')

    uts = doc.get('unique_tech', [])
    if len(uts) != 2:
        r.err(f'{len(uts)} unique techs; RULES 6.1 asks for exactly 2')
    if sorted(t.get('age', '') for t in uts) != ['Castle', 'Imperial']:
        r.err('unique techs must be one Castle Age and one Imperial Age tech (age = "Castle" / "Imperial")')
    for n, t in enumerate(uts, 1):
        w = f'[[unique_tech]] {t.get("name", n)}'
        need(r, t, ['name', 'age', 'effect', 'change', 'precedent', 'basis'], w)
        check_level(r, t, w)
        if t.get('change') not in CHANGES:
            r.err(f'{w}: change must be one of kept, changed, new')

    tree = doc.get('tree', {})
    have = trees[civ]
    basis = tree.get('basis', {})
    for item in tree.get('add', []):
        if item not in all_names:
            r.err(f'[tree] add: "{item}" is not an existing unit, tech or building name')
        elif item in have:
            r.warn(f'[tree] add: "{item}" is already in the {civ} tree')
        if item not in basis:
            r.err(f'[tree.basis]: no basis for added "{item}" (RULES 6.4)')
    for item in tree.get('remove', []):
        if item not in all_names:
            r.err(f'[tree] remove: "{item}" is not an existing unit, tech or building name')
        elif item not in have:
            r.warn(f'[tree] remove: "{item}" is not in the {civ} tree')
        if item not in basis:
            r.err(f'[tree.basis]: no basis for removed "{item}" (RULES 6.4)')
    for item in basis:
        if item not in tree.get('add', []) and item not in tree.get('remove', []):
            r.warn(f'[tree.basis]: "{item}" is neither added nor removed')

    for n, rn in enumerate(doc.get('rename', []), 1):
        w = f'[[rename]] {rn.get("from", n)}'
        need(r, rn, ['from', 'to', 'basis'], w)
        check_level(r, rn, w)
        if rn.get('from') and rn['from'] not in all_names:
            r.err(f'{w}: "{rn["from"]}" is not an existing unit, tech or building name')

    arch = doc.get('architecture', {})
    need(r, arch, ['set', 'basis'], '[architecture]')
    if arch.get('set') and arch['set'] not in ARCHITECTURE_SETS:
        r.err(f'[architecture]: "{arch["set"]}" is not one of the 13 existing sets')

    for n, dr in enumerate(doc.get('dropped', []), 1):
        w = f'[[dropped]] #{n}'
        need(r, dr, ['item', 'kind', 'reason'], w)
        if dr.get('kind') not in DROPPED_KINDS:
            r.err(f'{w}: kind must be one of {sorted(DROPPED_KINDS)}')

    # Every original element must be kept, replaced or dropped somewhere in the file.
    text = norm(path.read_text(encoding='utf-8'))
    orig = original_elements(help_texts[civ])
    for kind, items in orig.items():
        for item in items:
            if norm(item) and norm(item) not in text:
                r.warn(f'original {kind} not accounted for (keep it, name it in "replaces" or add a [[dropped]] entry): {item!r}')
    return r, doc


def main(argv):
    game = load_game()
    trees, _, all_names = game
    if argv[:1] == ['--tree']:
        for kind in ('Unit', 'Tech', 'Building'):
            print(f'{kind}: ' + ', '.join(sorted(n for n, k in trees[argv[1]].items() if k == kind)))
        return 0
    if argv[:1] == ['--find']:
        civs = sorted(c for c, t in trees.items() if argv[1] in t)
        print(f'{argv[1]} [{len(civs)}/{len(trees)}]: ' + ', '.join(civs))
        return 0
    if argv[:1] == ['--names']:
        for n in sorted(all_names):
            print(f'{n} ({"/".join(sorted(all_names[n]))})')
        return 0
    files = [Path(a) for a in argv] or sorted(CIVS_DIR.glob('*.toml'))
    failed = 0
    docs = {}
    for f in files:
        r, doc = validate(f, game)
        if doc:
            docs[f.name] = doc
        status = 'FAIL' if r.errors else 'ok'
        print(f'{status}  {f.name}' + (f'  ({len(r.warnings)} warning(s))' if r.warnings else ''))
        for m in r.errors:
            print(f'    error: {m}')
        for m in r.warnings:
            print(f'    warning: {m}')
        failed += bool(r.errors)
    if len(files) > 1:
        civs = Counter(d.get('civ') for d in docs.values())
        for civ, n in civs.items():
            if n > 1:
                print(f'error: civ "{civ}" is designed in {n} files')
                failed += 1
        uts = Counter(t.get('name') for d in docs.values() for t in d.get('unique_tech', []))
        for name, n in uts.items():
            if n > 1:
                print(f'warning: unique tech "{name}" appears in {n} civs')
        uus = defaultdict(list)
        for d in docs.values():
            for u in d.get('unique_unit', []):
                uus[u.get('name')].append(d.get('name'))
        for name, holders in uus.items():
            if len(holders) > 1:
                print(f'note: unique unit "{name}" is shared by ' + ', '.join(holders))
        print(f'{len(files)} file(s), {failed} with errors')
    return 1 if failed else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
