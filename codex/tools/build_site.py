"""Build the site's historical mode (historical/) from the codex civ designs.

Usage (from the repository root):
    python -I codex/tools/build_site.py

Reads the original site data (data/data.json, data/locales/*/strings.json, data/trees/*.json),
the civ designs (codex/civs/*.toml), the out-of-scope list (codex/out-of-scope.md) and the
Scenario Editor unit stats (codex/tools/scenario-units-stats.json), and writes a complete data
set for the historical mode to historical/data/. The original data is never modified.

What each design changes on the site:
  - the civ's displayed name and its bonus panel (label, time window, original name, bonuses,
    unique units and techs, team bonus, a link to the design file);
  - its tree: unique units and techs, items added and removed, per-civ renames.
Generated texts are English in every locale. Prints a report of anything it could not place.
"""
import copy
import json
import re
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CODEX = ROOT / 'codex'
OUT = ROOT / 'historical' / 'data'
REPO_URL = 'https://github.com/TheDreigon/aoe2-codex/blob/master/codex/civs/'

FIRST_STRING_ID = 990000   # custom strings; help strings are looked up as help_string_id - 79000
FIRST_TECH_ID = 9000       # synthetic ids for level-2 techs
DEFAULT_TECH_COST = {'Food': 300, 'Gold': 250}
DEFAULT_RESEARCH_TIME = 60
AGE_ROWS = {'Dark': [1], 'Feudal': [3, 2], 'Castle': [5, 4], 'Imperial': [6, 7]}
AGE_IDS = {'Dark': 1, 'Feudal': 2, 'Castle': 3, 'Imperial': 4}
# Unique-tech icons by age, whatever the building: the game's silver (Castle) and gold (Imperial)
# crowns, and a bronze crown for the Feudal Age made from the silver one (img/Tech/codex-ut-feudal.png).
UNIQUE_TECH_PICTURES = {'Feudal': 'codex-ut-feudal', 'Castle': 33, 'Imperial': 107}
TREE_NAMES = {  # design name -> name used in the site's tree files
    'Trebuchet': 'Trebuchet (Packed)', 'Blackwood Archers': 'Blackwood Archer',
    'Elite Blackwood Archers': 'Elite Blackwood Archer',
}
FALLBACK_PICTURES = {  # scenario units without an icon in img/: closest existing unit icon
    'Crusader Knight': 'Knight', 'Heavy Pikeman': 'Pikeman', 'Heavy Swordsman': 'Long Swordsman',
    'Heavy Crossbowman': 'Arbalester', 'Eastern Swordsman': 'Long Swordsman', 'Norse Warrior': 'Berserk',
    'Mounted Samurai': 'Samurai', 'Khan': 'Mangudai', 'Sogdian Cataphract': 'Cataphract',
    'Pagan Priest': 'Monk', 'Priest': 'Monk', 'Canoe': 'Galley', 'Iroquois Warrior': 'Eagle Scout',
    'Flamethrower': 'Scorpion', 'Imperial Centurion': 'Centurion', 'Imperial Legionary': 'Legionary',
    'Royal Janissary': 'Janissary', 'Qizilbash Warrior': 'Savar', 'Amazon Archer': 'Archer',
    'Amazon Warrior': 'Long Swordsman',
}


class Strings:
    def __init__(self):
        self.extra = {}
        self.next_id = FIRST_STRING_ID

    def add(self, text):
        sid = self.next_id
        self.next_id += 1
        self.extra[str(sid)] = text
        return sid


def load(path):
    return json.loads(Path(path).read_text(encoding='utf-8'))


def save(path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False, separators=(',', ':')), encoding='utf-8', newline='\n')


def first_sentence(text, limit=240):
    text = re.sub(r'\s+', ' ', text or '').strip()
    m = re.match(r'(.+?[.;])(\s|$)', text)
    s = m.group(1) if m else text
    return s if len(s) <= limit else s[:limit].rsplit(' ', 1)[0] + '…'


def esc(text):
    return (text or '').replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def grid_position(tree, node_id):
    for b in tree['buildings']:
        for r, row in enumerate(b['grid'] or []):
            for c, cell in enumerate(row):
                if cell == node_id:
                    return b, r, c
    return None, None, None


def find_building(tree, name):
    candidates = [b for b in tree['buildings'] if b['name'] == name and b['grid']]
    candidates.sort(key=lambda b: -sum(1 for row in b['grid'] for cell in row if cell))
    return candidates[0] if candidates else None


def free_cell(building, rows):
    grid = building['grid']
    for r in rows:
        if r < len(grid):
            for c, cell in enumerate(grid[r]):
                if cell is None:
                    return r, c
    width = len(grid[0])
    for row in grid:
        row.append(None)
    return rows[0], width


def remove_from_grid(tree, node_id):
    b, r, c = grid_position(tree, node_id)
    if b is not None:
        b['grid'][r][c] = None
    tree['units_techs'] = [n for n in tree['units_techs'] if n['id'] != node_id]


class Builder:
    def __init__(self):
        self.data = load(ROOT / 'data' / 'data.json')
        self.strings_en = load(ROOT / 'data' / 'locales' / 'en' / 'strings.json')
        self.trees = {p.stem: load(p) for p in (ROOT / 'data' / 'trees').glob('*.json')}
        self.scenario = load(CODEX / 'tools' / 'scenario-units-stats.json')
        self.s = Strings()
        self.next_tech = FIRST_TECH_ID
        self.report = []
        self.catalog = {}
        self.building_catalog = {}
        for civ, tree in self.trees.items():
            for node in tree['units_techs']:
                b, r, c = grid_position(tree, node['id'])
                self.catalog.setdefault(node['name'], []).append((civ, node, b['name'] if b else None, r, c))
            for b in tree['buildings']:
                self.building_catalog.setdefault(b['name'], (civ, b))
        self.tree_names = set(self.catalog) | set(self.building_catalog)

    # ---- helpers -------------------------------------------------------------------------
    def template(self, name, building=None):
        options = self.catalog.get(name, [])
        if building:
            preferred = [o for o in options if o[2] == building]
            options = preferred or options
        return options[0] if options else None

    def help_text(self, node):
        return self.strings_en.get(str(node['help_string_id'] - 79000), '')

    def renamed_strings(self, node, old, new, note=None):
        node['name'] = new
        node['name_string_id'] = self.s.add(new)
        text = self.help_text(node).replace(f'<b>{old}</b>', f'<b>{new}</b>', 1)
        if note:
            text = text.replace('<br>\n', f' {note}<br>\n', 1)
        node['help_string_id'] = self.s.add(text) + 79000

    def place(self, tree, node, building_name, rows, prefer=None):
        building = find_building(tree, building_name)
        if building is None:
            self.report.append(f'{self.civ}: no {building_name} in the tree for {node["name"]}')
            return False
        if prefer is not None and prefer[0] < len(building['grid']) and prefer[1] < len(building['grid'][0]) \
                and building['grid'][prefer[0]][prefer[1]] is None:
            r, c = prefer
        else:
            r, c = free_cell(building, rows)
        building['grid'][r][c] = node['id']
        node['row'] = r
        node['building_id'] = building['building_id']
        tree['units_techs'].append(node)
        return True

    def clone(self, tmpl_node, building_id):
        node = copy.deepcopy(tmpl_node)
        node['id'] = f"{node['use_type']}_{node['node_id']}_{building_id}"
        node['building_id'] = building_id
        node['node_status'] = 'ResearchedCompleted'
        return node

    # ---- unique units -----------------------------------------------------------------------
    def scenario_node(self, model, name, building):
        rows = self.scenario.get(model) or []
        if not rows:
            self.report.append(f'{self.civ}: unknown model {model}')
            return None
        st = rows[0]
        uid = st['id']
        fallback = self.template(FALLBACK_PICTURES.get(model, 'Knight'))
        picture = fallback[1]['picture_index'] if fallback else 0
        self.data['data']['Unit'][str(uid)] = {
            'internal_name': st['internal_name'], 'ID': uid, 'HP': st['hp'], 'Cost': st['cost'],
            'Attack': st['attack'] or 0, 'Range': st['range'] or 0, 'MeleeArmor': st['melee_armour'] or 0,
            'PierceArmor': st['pierce_armour'] or 0, 'LineOfSight': st['line_of_sight'], 'Speed': st['speed'],
            'ReloadTime': st['reload_time'], 'TrainTime': st['train_time'],
            'Attacks': [{'Amount': a['amount'], 'Class': a['class']} for a in st['attacks']],
            'Armours': [{'Amount': st['melee_armour'] or 0, 'Class': 4}, {'Amount': st['pierce_armour'] or 0, 'Class': 3}],
        }
        text = (f'Create <b>{name}</b> (‹cost›)<br>\nUnique unit of the codex, built on the Scenario Editor unit '
                f'{model} (existing game content; icon is a stand-in).<br>\n<i>Upgrades: as the game\'s {model}.</i>'
                f'<br>\n‹hp› ‹attack› ‹armor› ‹piercearmor› ‹range›')
        return {
            'age_id': 3, 'building_id': None, 'building_in_new_column': None, 'building_upgraded_from_id': None,
            'grid': None, 'help_string_id': self.s.add(text) + 79000, 'id': f'Unit_{uid}_{building}',
            'link_id': None, 'link_node_type': 'BuildingTech', 'name': name, 'name_string_id': self.s.add(name),
            'node_id': uid, 'node_status': 'ResearchedCompleted', 'node_type': 'UniqueUnit',
            'picture_index': picture, 'row': 5, 'use_type': 'Unit',
        }

    def apply_unique_units(self, tree, design):
        current = [n for n in tree['units_techs'] if n['node_type'] == 'UniqueUnit']
        lines = {}
        for n in current:
            base = n['name'][6:] if n['name'].startswith('Elite ') else n['name']
            lines.setdefault(base, []).append(n)
        wanted = design.get('unique_unit', [])
        models = [TREE_NAMES.get(u['model'], u['model']) for u in wanted]
        freed = []  # (building name, row, col) of removed castle unique-unit cells
        for base, nodes in lines.items():
            if base not in models:
                for n in nodes:
                    self.removed_units.add(n['name'])
                    b, r, c = grid_position(tree, n['id'])
                    if b is not None:
                        freed.append((b['name'], r, c, n['name'].startswith('Elite ')))
                    remove_from_grid(tree, n['id'])
        renamed_elites = {r['from'] for r in design.get('rename', [])}
        for u in wanted:
            model, name, building = TREE_NAMES.get(u['model'], u['model']), u['name'], u.get('building', 'Castle')
            present = [n for n in tree['units_techs'] if n['name'] in (model, f'Elite {model}')]
            if not present:
                tmpl = self.template(model, building)
                if tmpl:
                    b_obj = find_building(tree, building)
                    if b_obj is None:
                        self.report.append(f'{self.civ}: no {building} for {name}')
                        continue
                    base_node = self.clone(tmpl[1], b_obj['building_id'])
                    base_node['node_type'] = 'UniqueUnit'
                    slot = next((f for f in freed if f[0] == building and not f[3]), None)
                    self.place(tree, base_node, building, AGE_ROWS[u.get('age', 'Castle')],
                               prefer=(slot[1], slot[2]) if slot else None)
                    if slot:
                        freed.remove(slot)
                    elite = self.template(f'Elite {model}', tmpl[2])
                    if elite:
                        elite_node = self.clone(elite[1], b_obj['building_id'])
                        elite_node['node_type'] = 'UniqueUnit'
                        eslot = next((f for f in freed if f[0] == building and f[3]), None)
                        self.place(tree, elite_node, building, AGE_ROWS['Imperial'],
                                   prefer=(eslot[1], eslot[2]) if eslot else (base_node['row'] + 1, grid_position(tree, base_node['id'])[2]))
                        if eslot:
                            freed.remove(eslot)
                        present = [base_node, elite_node]
                    else:
                        present = [base_node]
                elif model in self.scenario:
                    b_obj = find_building(tree, building)
                    node = self.scenario_node(model, name, b_obj['building_id'] if b_obj else 82)
                    if node:
                        slot = next((f for f in freed if f[0] == building and not f[3]), None)
                        self.place(tree, node, building, AGE_ROWS[u.get('age', 'Castle')],
                                   prefer=(slot[1], slot[2]) if slot else None)
                        if slot:
                            freed.remove(slot)
                    continue
                else:
                    self.report.append(f'{self.civ}: no template for unique unit model {model}')
                    continue
            for n in present:
                n['node_type'] = 'UniqueUnit'
                if n['name'] == model and name != model:
                    self.renamed_strings(n, model, name, f'(Codex: the game\'s {model}.)')
                elif n['name'] == f'Elite {model}' and name != model and f'Elite {model}' not in renamed_elites:
                    self.renamed_strings(n, f'Elite {model}', f'Elite {name}')

    # ---- unique techs -----------------------------------------------------------------------
    def precedent_tech(self, ut):
        prec = ut.get('precedent', '')
        name = prec.split(' (')[0].strip()
        tmpl = self.template(name) if name else None
        if tmpl and tmpl[1]['use_type'] == 'Tech':
            return tmpl[1]
        return None

    def apply_unique_techs(self, tree, design):
        old = [n for n in tree['units_techs'] if n['node_type'] == 'UniqueTech']
        old_cells = []
        for n in old:
            b, r, c = grid_position(tree, n['id'])
            if b is not None:
                old_cells.append((b['name'], r, c, n['age_id']))
            remove_from_grid(tree, n['id'])
        for ut in design.get('unique_tech', []):
            building = ut['building']
            age = ut['age']
            prec = self.precedent_tech(ut)
            picture = UNIQUE_TECH_PICTURES.get(age, 33)
            if ut.get('level') == 1 and prec is not None:
                tid = prec['node_id']
            else:
                tid = self.next_tech
                self.next_tech += 1
                cost = dict(self.data['data']['Tech'].get(str(prec['node_id']), {}).get('Cost', DEFAULT_TECH_COST)) if prec else dict(DEFAULT_TECH_COST)
                rt = self.data['data']['Tech'].get(str(prec['node_id']), {}).get('ResearchTime', DEFAULT_RESEARCH_TIME) if prec else DEFAULT_RESEARCH_TIME
                self.data['data']['Tech'][str(tid)] = {'Cost': cost, 'ID': tid, 'ResearchTime': rt, 'internal_name': ut['name']}
            b_obj = find_building(tree, building)
            if b_obj is None:
                self.report.append(f'{self.civ}: no {building} for tech {ut["name"]}')
                continue
            why = first_sentence(ut.get('basis', ''))
            text = (f'Research <b>{esc(ut["name"])}</b> (‹cost›)<br>\n{esc(ut["effect"])} '
                    f'<i>({building}, {age} Age{", level 2" if ut.get("level") == 2 else ""}.) {esc(why)}</i>')
            node = {
                'age_id': AGE_IDS.get(age, 3), 'building_id': b_obj['building_id'], 'building_in_new_column': None,
                'building_upgraded_from_id': None, 'grid': None, 'help_string_id': self.s.add(text) + 79000,
                'id': f'Tech_{tid}_{b_obj["building_id"]}', 'link_id': None, 'link_node_type': 'BuildingTech',
                'name': ut['name'], 'name_string_id': self.s.add(ut['name']), 'node_id': tid,
                'node_status': 'ResearchedCompleted', 'node_type': 'UniqueTech', 'picture_index': picture,
                'row': AGE_ROWS[age][0], 'use_type': 'Tech',
            }
            slot = next((c for c in old_cells if c[0] == building and c[3] == AGE_IDS.get(age)), None)
            self.place(tree, node, building, AGE_ROWS[age], prefer=(slot[1], slot[2]) if slot else None)
            if slot:
                old_cells.remove(slot)

    # ---- tree and renames ---------------------------------------------------------------------
    def nodes_named(self, tree, name):
        name = TREE_NAMES.get(name, name)
        return ([n for n in tree['units_techs'] if n['name'] == name]
                + [b for b in tree['buildings'] if b['name'] == name])

    def apply_tree(self, tree, design):
        t = design.get('tree', {})
        for name in t.get('remove', []):
            nodes = self.nodes_named(tree, name)
            if not nodes and TREE_NAMES.get(name, name) in self.tree_names and name not in self.removed_units:
                self.report.append(f'{self.civ}: remove {name}: not in the tree')
            for n in nodes:
                n['node_status'] = 'NotAvailable'
        for name in t.get('add', []):
            nodes = self.nodes_named(tree, name)
            if nodes:
                for n in nodes:
                    n['node_status'] = 'ResearchedCompleted'
                continue
            tname = TREE_NAMES.get(name, name)
            if tname in self.building_catalog:
                building = copy.deepcopy(self.building_catalog[tname][1])
                building['node_status'] = 'ResearchedCompleted'
                if building['grid']:
                    building['grid'] = [[None for _ in row] for row in building['grid']]
                tree['buildings'].append(building)
                continue
            tmpl = self.template(tname)
            if not tmpl:
                if tname in self.tree_names:
                    self.report.append(f'{self.civ}: add {name}: no template')
                continue
            civ, tnode, bname, r, c = tmpl
            b_obj = find_building(tree, bname) if bname else None
            if b_obj is None:
                self.report.append(f'{self.civ}: add {name}: no {bname} in the tree')
                continue
            node = self.clone(tnode, b_obj['building_id'])
            self.place(tree, node, bname, [r] + [x for x in range(8) if x != r], prefer=(r, c))

    def apply_renames(self, tree, design):
        for rn in design.get('rename', []):
            nodes = self.nodes_named(tree, rn['from'])
            if not nodes:
                if not self.nodes_named(tree, rn['to']) and TREE_NAMES.get(rn['from'], rn['from']) in self.tree_names:
                    self.report.append(f'{self.civ}: rename {rn["from"]}: not in the tree')
                continue
            for n in nodes:
                self.renamed_strings(n, n['name'], rn['to'])

    # ---- civ panel ----------------------------------------------------------------------------
    def civ_text(self, design, file_stem):
        p = design['profile']
        lines = [esc(design['label'])]
        meta = f'Time window: <b>{esc(p["window"])}</b>.'
        if design.get('original_name'):
            meta += f' Called <b>{esc(design["original_name"])}</b> in the game.'
        lines.append(f'<i>{meta}</i>')
        lines.append('')
        for b in design.get('bonus', []):
            lines.append(f'• {esc(b["text"])}')
        lines.append('')
        lines.append('<b>Unique Units:</b>')
        lines.append(', '.join(f'{esc(u["name"])} ({esc(u.get("building", "Castle"))})' for u in design.get('unique_unit', [])))
        lines.append('')
        lines.append('<b>Unique Techs:</b>')
        for ut in design.get('unique_tech', []):
            lines.append(f'• {esc(ut["name"])} [{esc(ut["building"])}, {esc(ut["age"])}] ({esc(ut["effect"])})')
        lines.append('')
        lines.append('<b>Team Bonus:</b>')
        lines.append(esc(design['team_bonus']['text']))
        lines.append('')
        lines.append(f'<a href="{REPO_URL}{file_stem}.toml" target="_blank">Design notes and sources</a>')
        return '<br>\n'.join(lines)

    # ---- main -----------------------------------------------------------------------------------
    def build(self):
        designs = {}
        for path in sorted((CODEX / 'civs').glob('*.toml')):
            d = tomllib.loads(path.read_text(encoding='utf-8'))
            designs[d['civ']] = (d, path.stem)
        out_trees = {}
        for civ_key, civ_entry in self.data['civs'].items():
            tree_key = civ_key.upper()
            tree = copy.deepcopy(self.trees[tree_key])
            self.civ = civ_key
            self.removed_units = set()
            if civ_key in designs:
                design, stem = designs[civ_key]
                self.apply_unique_units(tree, design)
                self.apply_unique_techs(tree, design)
                self.apply_tree(tree, design)
                self.apply_renames(tree, design)
                civ_entry['name_string_id'] = self.s.add(design['name'])
                civ_entry['help_string_id'] = self.s.add(self.civ_text(design, stem))
                lists = {'Unit': set(), 'Tech': set(), 'Building': set(b['node_id'] for b in tree['buildings'] if b.get('node_status') != 'NotAvailable')}
                for n in tree['units_techs']:
                    if n['node_status'] != 'NotAvailable' and n['use_type'] in lists:
                        lists[n['use_type']].add(n['node_id'])
                for k, v in lists.items():
                    civ_entry[k] = sorted(v)
            else:
                name = self.strings_en.get(str(civ_entry['name_string_id']), civ_key)
                reason = self.out_of_scope.get(civ_key, 'Not in the codex roster.')
                civ_entry['name_string_id'] = self.s.add(f'{name} (out of scope)')
                original = self.strings_en.get(str(civ_entry['help_string_id']), '')
                civ_entry['help_string_id'] = self.s.add(
                    f'<b>Out of scope for the codex.</b> {esc(reason)} The original design is shown unchanged.<br>\n<br>\n{original}')
            out_trees[tree_key] = tree
        for key, tree in out_trees.items():
            save(OUT / 'trees' / f'{key}.json', tree)
        save(OUT / 'data.json', self.data)
        for loc_dir in sorted((ROOT / 'data' / 'locales').iterdir()):
            strings = load(loc_dir / 'strings.json')
            strings.update(self.s.extra)
            strings['1'] = 'Codex'
            save(OUT / 'locales' / loc_dir.name / 'strings.json', strings)
        print(f'built {len(out_trees)} civs ({len(designs)} designs), {len(self.s.extra)} custom strings')
        for line in self.report:
            print('note:', line)

    @property
    def out_of_scope(self):
        reasons = {}
        text = (CODEX / 'out-of-scope.md').read_text(encoding='utf-8')
        for m in re.finditer(r'^\| \*\*([^*]+)\*\*[^|]*\| ([^|]+) \|', text, re.M):
            key = m.group(1).split()[0]
            reasons[key] = re.sub(r'\s+', ' ', m.group(2)).strip()
        return reasons


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    Builder().build()
