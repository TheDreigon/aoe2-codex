"""Validate the civ design files in codex/civs/*.toml.

Usage (from the repository root):
    python -I codex/tools/validate_civs.py [FILE ...]      validate the given files (default: all)
    python -I codex/tools/validate_civs.py --tree CIV      print the current tree of a civ (internal name)
    python -I codex/tools/validate_civs.py --find NAME     list the civs that currently have an item
    python -I codex/tools/validate_civs.py --names         list every unit, tech and building name

Checks the structure described in codex/civs/README.md and codex/RULES.md (v0.5, sections 1, 5, 6 and 8):
composition (4-6 passive bonuses with at least one economic and one military; one team bonus; 2-4
unique techs, one at the Castle and one at the Town Center, with valid buildings, kinds and ages;
1-2 unique units, regional units not counting), required fields (including the one-line relevance
statement of RULES 6.9 for every bonus, team bonus, unique unit and unique tech; original_name for renamed
civs and a precise time window, RULES section 1), the level constraints that can be
checked mechanically (item names exist in the game, architecture set exists, only unique techs may be
level 2) and whether every original bonus, unique unit and unique tech is accounted for. Units that exist only
in campaigns and the Scenario Editor (codex/tools/scenario-units.md) count as existing game content (RULES
section 5): they are accepted as the `model` of a unique unit or of a per-civ rename.
Errors make the exit code 1; warnings do not. With several files, it also lists the unit models and the
effects (bonuses, team bonuses, unique techs) that more than one design uses, so that the holder lists in
the precedents can be checked.

Level convention (RULES 6.5): a level-1 unique tech is an existing tech identical in play. Its effect text
names the civ's own (possibly renamed) units and leaves out targets the civ does not have; its precedent
quotes the game's text. Any narrowed, widened, retargeted or combined effect makes a new, level-2 tech.
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
TECH_BUILDINGS = {
    'Castle', 'Town Center', 'Market', 'Monastery', 'University', 'Dock', 'Mill', 'Lumber Camp',
    'Mining Camp', 'Barracks', 'Archery Range', 'Stable', 'Siege Workshop',
}
MILITARY_BUILDINGS = {'Castle', 'Barracks', 'Archery Range', 'Stable', 'Siege Workshop', 'Dock'}
TECH_KINDS = {'military', 'civil'}
AGES = ['Dark', 'Feudal', 'Castle', 'Imperial']
# Regional units do not count as unique units (RULES 6.1): the game's own regional units (node type
# 'RegionalUnit' in data/trees/) plus the Genitour, which the owner made a regional unit.
OWNER_REGIONAL_UNITS = {'Genitour', 'Elite Genitour'}
CHANGES = {'kept', 'changed', 'new'}
SCENARIO_UNITS_FILE = ROOT / 'codex' / 'tools' / 'scenario-units.md'
DROPPED_KINDS = {'bonus', 'team_bonus', 'unique_unit', 'unique_tech', 'unique_building', 'tree', 'other'}


def load_scenario_units():
    """Names of the units listed in codex/tools/scenario-units.md (first column of its table), without the
    wiki's disambiguation suffix, e.g. 'Canoe (Age of Empires II)' -> 'Canoe'."""
    units = set()
    if not SCENARIO_UNITS_FILE.exists():
        return units
    for line in SCENARIO_UNITS_FILE.read_text(encoding='utf-8').splitlines():
        cells = [c.strip() for c in line.strip().strip('|').split('|')]
        if not line.startswith('|') or len(cells) < 2 or cells[0] in ('Unit', '') or set(cells[0]) <= set('-: '):
            continue
        units.add(re.sub(r'\s*\(Age of Empires II\)$', '', cells[0]))
    return units


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
    display = {civ: s.get(str(c['name_string_id'])) or civ for civ, c in d['civs'].items()}
    help_texts['__display__'] = display
    help_texts['__scenario__'] = load_scenario_units()
    help_texts['__prereq__'], help_texts['__substitutes__'] = load_prerequisites(names, d['civs'])
    help_texts['__regional__'] = OWNER_REGIONAL_UNITS | {
        x['name'] for f in (ROOT / 'data' / 'trees').glob('*.json')
        for x in json.loads(f.read_text(encoding='utf-8'))['units_techs'] if x['node_type'] == 'RegionalUnit'}
    all_names = defaultdict(set)
    for (k, _), n in names.items():
        all_names[n].add(k)
    return trees, help_texts, all_names


UNIT_LINKS = {'Unit', 'UnitUpgrade', 'RegionalUnit', 'UniqueUnit'}


def load_prerequisites(names, civs):
    """Item name -> names it depends on (upgrade chain, research chain or the building that makes it),
    taken from the tree layouts in data/trees/ (a dependency counts if most civs that have the item show it).
    Also returns, per civ, the buildings that stand in for a standard one (Mule Cart for the Mining Camp,
    Fortified Church for the Monastery, ...), found where the civ's own tree hosts an item elsewhere."""
    seen, deps = Counter(), defaultdict(Counter)
    hosts = defaultdict(dict)  # civ -> item -> host building
    for civ in civs:
        f = ROOT / 'data' / 'trees' / f'{civ.upper()}.json'
        if not f.exists():
            continue
        tree = json.loads(f.read_text(encoding='utf-8'))
        for x in tree['units_techs'] + tree['buildings']:
            kind, lt, lid = x['use_type'], x['link_node_type'], x['link_id']
            me = names.get((kind, x['node_id']))
            if not me:
                continue
            seen[me] += 1
            found = set()
            if lid is not None:
                if kind in ('Unit', 'Tech') and lt in UNIT_LINKS:
                    found.add(names.get(('Unit', lid)))
                elif kind in ('Unit', 'Tech') and lt == 'Research':
                    found.add(names.get(('Tech', lid)))
                elif kind == 'Building' and lt in ('BuildingTech', 'BuildingNonTech'):
                    found.add(names.get(('Building', lid)))
                elif kind == 'Building' and lt == 'Unit':
                    found.add(names.get(('Unit', lid)))
            if kind in ('Unit', 'Tech') and x.get('building_id') is not None:
                host = names.get(('Building', x['building_id']))
                found.add(host)
                hosts[civ][me] = host
            for n in found - {None, me}:
                deps[me][n] += 1
    prereq = {me: {n for n, k in c.items() if k * 2 > seen[me]} for me, c in deps.items()}
    usual = {}
    for civ_hosts in hosts.values():
        for item, host in civ_hosts.items():
            usual.setdefault(item, Counter())[host] += 1
    substitutes = defaultdict(lambda: defaultdict(set))  # civ -> standard building -> stand-ins
    for civ, civ_hosts in hosts.items():
        for item, host in civ_hosts.items():
            main = usual[item].most_common(1)[0][0]
            if host and main and host != main:
                substitutes[civ][main].add(host)
    return prereq, substitutes


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


def check_level(r, table, where, allowed=(1,)):
    if table.get('level') not in allowed:
        r.err(f'{where}: level must be {" or ".join(map(str, allowed))} here (got {table.get("level")!r})')


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

    shown = help_texts['__display__'][civ]
    if doc.get('name') and doc['name'] != shown:
        if doc.get('original_name') != shown:
            r.err(f'renamed civ: add original_name = "{shown}" at the top level (RULES section 1)')
    elif doc.get('original_name'):
        r.warn(f'original_name is only needed for renamed civs (the game already shows "{shown}")')

    prof = doc.get('profile', {})
    need(r, prof, ['entity', 'region', 'window', 'sources'], '[profile]')
    if prof.get('window') and not re.match(r'\d{3,4}\s*[–-]\s*\d{3,4}', prof['window']):
        r.warn(f'[profile] window should start with a precise year range such as "1066–1485", without "c." (RULES section 1): {prof["window"]!r}')
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
        need(r, b, ['text', 'kind', 'change', 'precedent', 'basis', 'relevance'], w)
        check_level(r, b, w)
        if b.get('kind') not in KINDS:
            r.err(f'{w}: kind must be one of {sorted(KINDS)}')
        if b.get('change') not in CHANGES:
            r.err(f'{w}: change must be one of {sorted(CHANGES)}')

    tb = doc.get('team_bonus')
    if not isinstance(tb, dict):
        r.err('exactly one [team_bonus] table is required')
    else:
        need(r, tb, ['text', 'change', 'precedent', 'basis', 'relevance'], '[team_bonus]')
        check_level(r, tb, '[team_bonus]')
        if tb.get('change') not in CHANGES:
            r.err('[team_bonus]: change must be one of kept, changed, new')

    uus = doc.get('unique_unit', [])
    regional = help_texts['__regional__']
    scenario = help_texts['__scenario__']
    counted = [u for u in uus if u.get('model') not in regional]
    if not 1 <= len(counted) <= 2:
        r.err(f'{len(counted)} unique units (regional units not counted); RULES 6.1 asks for 1 or 2')
    for u in uus:
        if u.get('model') in regional:
            r.warn(f'[[unique_unit]] {u.get("name")}: {u["model"]} is a regional unit and does not count as a unique unit')
    for n, u in enumerate(uus, 1):
        w = f'[[unique_unit]] {u.get("name", n)}'
        need(r, u, ['name', 'model', 'change', 'basis', 'relevance'], w)
        check_level(r, u, w)
        if u.get('change') not in CHANGES:
            r.err(f'{w}: change must be one of kept, changed, new')
        if u.get('model') and u['model'] not in all_names and u['model'] not in scenario:
            r.err(f'{w}: model "{u["model"]}" is not an existing unit or building name, nor a Scenario Editor unit')

    uts = doc.get('unique_tech', [])
    if not 2 <= len(uts) <= 4:
        r.err(f'{len(uts)} unique techs; RULES 6.1 asks for 2 to 4')
    buildings = Counter(t.get('building') for t in uts)
    if not buildings['Castle']:
        r.err('no unique tech at the Castle (RULES 6.1)')
    if not buildings['Town Center']:
        r.err('no unique tech at the Town Center (RULES 6.1)')
    castle_ages = sorted(t.get('age', '') for t in uts if t.get('building') == 'Castle')
    if len(castle_ages) == 2 and castle_ages != ['Castle', 'Imperial']:
        r.err('two Castle techs must be one Castle Age and one Imperial Age tech (RULES 6.4)')
    if len(castle_ages) > 2:
        r.err('more than two unique techs at the Castle')
    for n, t in enumerate(uts, 1):
        w = f'[[unique_tech]] {t.get("name", n)}'
        need(r, t, ['name', 'building', 'kind', 'age', 'effect', 'change', 'precedent', 'basis', 'relevance'], w)
        check_level(r, t, w, allowed=(1, 2))
        if t.get('change') not in CHANGES:
            r.err(f'{w}: change must be one of kept, changed, new')
        if t.get('building') and t['building'] not in TECH_BUILDINGS:
            r.err(f'{w}: building must be one of {sorted(TECH_BUILDINGS)}')
        if t.get('kind') and t['kind'] not in TECH_KINDS:
            r.err(f'{w}: kind must be military or civil')
        age = t.get('age')
        if not age:
            continue
        if age not in AGES:
            r.err(f'{w}: age must be one of {AGES}')
            continue
        if age == 'Dark':
            r.err(f'{w}: no unique tech in the Dark Age (RULES 6.4)')
        if t.get('building') == 'Castle' and AGES.index(age) < 2:
            r.err(f'{w}: a Castle tech cannot be earlier than the Castle Age')
        if t.get('kind') == 'military' and t.get('building') in MILITARY_BUILDINGS and AGES.index(age) < 2:
            r.err(f'{w}: military techs outside the Castle are Castle Age at the earliest (RULES 6.4)')
    if len(bonuses) + len(uts) > 9:
        r.warn(f'{len(bonuses)} passive bonuses + {len(uts)} unique techs > 9 (cap proposed in RULES 6.1, not enforced)')

    tree = doc.get('tree', {})
    have = trees[civ]
    basis = tree.get('basis', {})
    for item in tree.get('add', []):
        if item not in all_names:
            r.err(f'[tree] add: "{item}" is not an existing unit, tech or building name')
        elif item in have:
            r.warn(f'[tree] add: "{item}" is already in the {civ} tree')
        if item not in basis:
            r.err(f'[tree.basis]: no basis for added "{item}" (RULES 6.8)')
    for item in tree.get('remove', []):
        if item not in all_names:
            r.err(f'[tree] remove: "{item}" is not an existing unit, tech or building name')
        elif item not in have:
            r.warn(f'[tree] remove: "{item}" is not in the {civ} tree')
        if item not in basis:
            r.err(f'[tree.basis]: no basis for removed "{item}" (RULES 6.8)')
    for item in basis:
        if item not in tree.get('add', []) and item not in tree.get('remove', []):
            r.warn(f'[tree.basis]: "{item}" is neither added nor removed')
    # Tree dependencies: nothing kept or added may depend on something removed or missing.
    prereq = help_texts['__prereq__']
    stand_ins = help_texts['__substitutes__'].get(civ, {})
    removed = set(tree.get('remove', []))
    added = set(tree.get('add', []))
    final = (set(have) - removed) | added
    for item in sorted(final):
        for need_item in sorted(prereq.get(item, ())):
            if need_item in final or stand_ins.get(need_item, set()) & final:
                continue
            if need_item in removed:
                r.warn(f'[tree]: "{item}" stays in the tree but needs "{need_item}", which this design removes')
            elif item in added:
                r.warn(f'[tree]: added "{item}" needs "{need_item}", which is not in the tree')

    for n, rn in enumerate(doc.get('rename', []), 1):
        w = f'[[rename]] {rn.get("from", n)}'
        need(r, rn, ['from', 'to', 'basis'], w)
        check_level(r, rn, w)
        if rn.get('from') and rn['from'] not in all_names:
            r.err(f'{w}: "{rn["from"]}" is not an existing unit, tech or building name')
        if rn.get('model') and rn['model'] not in all_names and rn['model'] not in scenario:
            r.err(f'{w}: model "{rn["model"]}" is not an existing unit name, nor a Scenario Editor unit')

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
    # Item names contain non-ASCII letters; a Windows console defaults to a legacy code page.
    sys.stdout.reconfigure(encoding='utf-8')
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
        for n in sorted(game[1]['__scenario__'] - set(all_names)):
            print(f'{n} (Scenario Editor unit)')
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
        models = defaultdict(list)
        for d in docs.values():
            for u in d.get('unique_unit', []):
                models[u.get('model')].append(f'{d.get("name")} ({u.get("name")})')
        for d in docs.values():
            for rn in d.get('rename', []):
                if rn.get('model'):
                    models[rn['model']].append(f'{d.get("name")} ({rn.get("from")} renamed {rn.get("to")})')
        scenario = game[1]['__scenario__'] - set(all_names)
        for model, holders in sorted(models.items()):
            if len(holders) > 1:
                print(f'note: unit model "{model}" is used by ' + ', '.join(holders))
        for model, holders in sorted(models.items()):
            if model in scenario:
                print(f'note: Scenario Editor unit "{model}" is the model of ' + ', '.join(holders))
        effects = defaultdict(list)
        for d in docs.values():
            for kind, items in (('bonus', d.get('bonus', [])), ('team bonus', [d.get('team_bonus', {})]),
                                ('unique tech', d.get('unique_tech', []))):
                for x in items:
                    text = x.get('effect') or x.get('text') or ''
                    key = re.sub(r'[“”]', '"', text.lower()).replace('’', "'").strip().rstrip('.')
                    if key:
                        effects[key].append(f'{d.get("name")} ({kind}' + (f' {x["name"]})' if x.get('name') else ')'))
        for key, holders in sorted(effects.items()):
            if len(holders) > 1:
                print(f'note: effect "{key}" is held by ' + ', '.join(holders))
        print(f'{len(files)} file(s), {failed} with errors')
    return 1 if failed else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
