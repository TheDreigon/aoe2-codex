"""Build the site's historical mode (historical/) from the codex civ designs.

Usage (from the repository root):
    python -I codex/tools/build_site.py

Reads the original site data (data/data.json, data/locales/*/strings.json, data/trees/*.json),
the civ designs (codex/civs/*.toml), the out-of-scope list (codex/out-of-scope.md) and the
Scenario Editor unit stats (codex/tools/scenario-units-stats.json), and writes a complete data
set for the historical mode to historical/data/. The original data is never modified.

What each design changes on the site:
  - the civ's displayed name and its bonus panel (label, time window, original name, bonuses,
    unique units and techs, team bonus, a link to the design file), each line with its reason;
  - its tree: unique units and techs, items added and removed, per-civ renames.
A unit that only one designed civ has is shown as a unique unit (RULES 6.1). Every change and its
reason also goes to historical/data/codex.json, which historical/codex.js shows on the tree.
Generated texts are English in every locale. Prints a report of anything it could not place.
"""
import copy
import hashlib
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
FIRST_UNIT_ID = 95000      # synthetic ids for level-2 units with adapted stats
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
CHANGE_LABELS = {'kept': 'Kept from the game', 'new': 'New in the codex', 'changed': 'Changed by the codex'}
WHY_LIMIT = 900  # characters of a reason shown in the bonus panel's tooltips
UNIQUE_UNIT_CAP = 2  # RULES 6.1: 1 or 2 unique units per civ
UNIQUE_UNIT_EXCEPTIONS = {'Chinese': 3}  # owner's decision, 18 October 2026 (RULES 6.1)
SINGLE_CIV_WHY = 'Only this civ has this unit in the codex, so it counts as a unique unit (RULES 6.1).'
# Scenario Editor unit icons come from the game (codex/tools/extract_scenario_icons.py writes
# scenario-units-icons.json); a unit without one there takes the closest existing unit icon.
FALLBACK_PICTURES = {
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


ARMOUR_CLASSES = {'infantry': 1, 'cavalry': 8}  # the game's armour classes for a change of unit class


def stats_segment(text, tier):
    """The part of a design's free-text `stats` about one tier: the base tier comes before '. Elite';
    the Elite tier is the sentence after it, without its upgrade's own cost in brackets and without
    the closing 'Fully upgraded' totals."""
    if tier == 'base':
        return re.split(r'\.\s+Elite\b', text, maxsplit=1)[0]
    m = re.search(r'\.\s+Elite\b(.*)', text, re.S)
    if not m:
        return ''
    seg = re.split(r'\.\s+Fully upgraded\b', m.group(1), maxsplit=1)[0]
    head, sep, tail = seg.partition('):')
    return tail if sep else seg


def class_change(text):
    """(old armour class, new armour class) when the stats make the unit change class, else None."""
    m = re.search(r'\b(?:is|becomes) an? (cavalry|infantry) unit instead of an? (cavalry|infantry) unit', text, re.I)
    return (ARMOUR_CLASSES[m.group(2).lower()], ARMOUR_CLASSES[m.group(1).lower()]) if m else None


def parse_stats(text, tier='base'):
    """Numbers for one tier from a design's free-text `stats`."""
    seg = stats_segment(text, tier)
    out = {}
    for key, pattern in (('HP', r'(\d+)\s*HP'), ('Attack', r'(\d+)\s*attack'),
                         ('Speed', r'speed\s*(\d+(?:\.\d+)?)'), ('ReloadTime', r'reload\s*(\d+(?:\.\d+)?)\s*s'),
                         ('TrainTime', r'train(?:ing)? time\s*(\d+)'), ('Range', r'range\s*(\d+(?:\.\d+)?)')):
        m = re.search(pattern, seg, re.I)
        if m:
            out[key] = float(m.group(1)) if '.' in m.group(1) else int(m.group(1))
    m = re.search(r'(\d+)\s*/\s*(\d+)\s*armou?r', seg, re.I)
    if m:
        out['MeleeArmor'], out['PierceArmor'] = int(m.group(1)), int(m.group(2))
    cost = {res.capitalize(): int(n) for n, res in re.findall(r'(\d+)\s*(food|wood|gold|stone)\b', seg, re.I)}
    if cost:
        out['Cost'] = cost
    return out


def esc(text):
    return (text or '').replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def esc_attr(text):
    return esc(text).replace('"', '&quot;')


def shorten(text, limit):
    text = re.sub(r'\s+', ' ', text or '').strip()
    return text if len(text) <= limit else text[:limit].rsplit(' ', 1)[0] + '…'


def why_text(item):
    """The reason for a design element: how it relates to the game, then its basis."""
    head = CHANGE_LABELS.get(item.get('change'), '')
    if head and item.get('level'):
        head += f' (level {item["level"]})'
    if item.get('replaces'):
        head += f'; replaces {item["replaces"]}' if head else f'Replaces {item["replaces"]}'
    parts = [head + '.'] if head else []
    if item.get('basis'):
        parts.append(item['basis'])
    return ' '.join(parts)


def add_to_description(text, note):
    """Append a note to a unit's description: the part of its help text before the italic upgrade
    line, which main.js's getHelpText takes as the first <i>…</i>."""
    i = text.find('<br>\n<i>')
    if i < 0:
        return text.replace('<br>\n', f'<br>\n{note} ', 1)
    return text[:i] + f'<br>\n{note}' + text[i:]


def with_why(html, why):
    return f'<span class="codex-why" data-codex-why="{esc_attr(shorten(why, WHY_LIMIT))}">{html}</span>' if why else html


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


def age_rows(age_id):
    """The two grid rows of an age: main.js draws two rows per age, the Dark Age first."""
    return [2 * (age_id - 1), 2 * (age_id - 1) + 1]


def fit_column(grid, col, ages, preferred=None, top=0):
    """Rows for a line of items (a unit and its upgrades, or one item) in column `col`, each in a row of
    its own age and below the previous one, or None. main.js draws an item's line to the first item
    above it in its column (its parent) or, with nothing above, to its building; so the column must be
    empty from `top` (the row under the parent, or the top) to the bottom, or a line would be cut."""
    if any(grid[r][col] is not None for r in range(top, len(grid))):
        return None
    for prefs in ((preferred or []), []):  # the preferred rows first, then the first row of each age
        rows, lowest = [], top
        for i, age in enumerate(ages):
            band = [r for r in age_rows(age) if lowest <= r < len(grid)]
            if not band:
                break
            r = prefs[i] if i < len(prefs) and prefs[i] in band else band[0]
            rows.append(r)
            lowest = r + 1
        if len(rows) == len(ages):
            return rows
    return None


def layout_problems(tree):
    """Layout problems as main.js draws a tree: an item outside the rows of its age; an item with a link
    whose first item above (its column's parent) is not the linked one; an item without a link (drawn
    from its building) with an item above it. Each: (kind, building, node_id, name, row, column)."""
    index = {n['id']: n for n in tree['units_techs']}
    out = []
    for b in tree['buildings']:
        grid = b['grid'] or []
        for r, row in enumerate(grid):
            for c, cell in enumerate(row):
                n = index.get(cell)
                if n is None:
                    continue
                if r // 2 + 1 != n['age_id']:
                    out.append(('outside the rows of its age', b['name'], n['node_id'], n['name'], r, c))
                above = index.get(next((grid[rr][c] for rr in range(r - 1, -1, -1) if grid[rr][c]), None))
                if n.get('link_id') not in (None, -1):
                    if not above or above['node_id'] != n['link_id'] or above['node_type'] != n['link_node_type']:
                        out.append(('not under the item it upgrades', b['name'], n['node_id'], n['name'], r, c))
                elif above:
                    out.append(('cut off from its building', b['name'], n['node_id'], n['name'], r, c))
    return out


def retype(tree, node, node_type):
    """Change an item's node type; the items linked to it follow, so main.js keeps drawing their line."""
    old = node['node_type']
    if old == node_type:
        return
    node['node_type'] = node_type
    for n in tree['units_techs']:
        if n is not node and n.get('link_id') == node['node_id'] and n.get('link_node_type') == old:
            n['link_node_type'] = node_type


def template_anchor(tree, node):
    """The node_id of the item that `node` hangs under in its own tree (the first item above it in its
    column, when that is the item it links to), or None when it hangs from its building."""
    b, r, c = grid_position(tree, node['id'])
    if b is None or node.get('link_id') in (None, -1):
        return None
    index = {n['id']: n for n in tree['units_techs']}
    above = next((b['grid'][rr][c] for rr in range(r - 1, -1, -1) if b['grid'][rr][c]), None)
    parent = index.get(above)
    return parent['node_id'] if parent and parent['node_id'] == node['link_id'] else None


def remove_from_grid(tree, node_id):
    """Remove an item; the items that hung under it hang under its own parent instead (or its building)."""
    b, r, c = grid_position(tree, node_id)
    if b is not None:
        b['grid'][r][c] = None
    removed = next((n for n in tree['units_techs'] if n['id'] == node_id), None)
    tree['units_techs'] = [n for n in tree['units_techs'] if n['id'] != node_id]
    if removed is not None:
        for n in tree['units_techs']:
            if n.get('link_id') == removed['node_id'] and n.get('link_node_type') == removed['node_type']:
                n['link_id'], n['link_node_type'] = removed.get('link_id'), removed.get('link_node_type')


class Builder:
    def __init__(self):
        self.data = load(ROOT / 'data' / 'data.json')
        self.strings_en = load(ROOT / 'data' / 'locales' / 'en' / 'strings.json')
        self.trees = {p.stem: load(p) for p in (ROOT / 'data' / 'trees').glob('*.json')}
        self.scenario = load(CODEX / 'tools' / 'scenario-units-stats.json')
        icons = CODEX / 'tools' / 'scenario-units-icons.json'
        self.icons = load(icons) if icons.exists() else {}
        self.notes = {}  # civ -> [(node or building, kind, reason)], resolved to node ids at the end
        self.design_units = set()  # id() of the nodes that are a design's unique units
        self.s = Strings()
        self.next_tech = FIRST_TECH_ID
        self.next_unit = FIRST_UNIT_ID
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
        key = str(node['help_string_id'] - 79000)
        return self.strings_en.get(key) or self.s.extra.get(key, '')

    def note(self, node, kind, why):
        """Record a change on the tree: added, removed, renamed, new (unique item) or kept (unique item)."""
        self.notes.setdefault(self.civ, []).append((node, kind, why or ''))

    def renamed_strings(self, node, old, new, note=None):
        node['name'] = new
        node['name_string_id'] = self.s.add(new)
        text = self.help_text(node).replace(f'<b>{old}</b>', f'<b>{new}</b>', 1)
        if note:
            text = text.replace('<br>\n', f' {note}<br>\n', 1)
        node['help_string_id'] = self.s.add(text) + 79000

    def place_line(self, tree, building_name, nodes, anchor_id=None, prefer_col=None, prefer_rows=None):
        """Place a line of new items (a unit and its upgrades, or one item) in one column of a building,
        each in a row of its own age, without cutting another item's line (see fit_column): under the
        item with node_id `anchor_id` when the line upgrades it, else hanging from the building, in the
        preferred column if it fits, else in the first column that fits, else in a new column."""
        building = find_building(tree, building_name)
        if building is None:
            self.report.append(f'{self.civ}: no {building_name} in the tree for {nodes[0]["name"]}')
            return False
        grid = building['grid']
        ages = [n['age_id'] for n in nodes]
        if anchor_id is not None:
            anchor = next((n for n in tree['units_techs'] if n['node_id'] == anchor_id
                           and grid_position(tree, n['id'])[0] is building), None)
            if anchor is not None:
                _, ar, ac = grid_position(tree, anchor['id'])
                rows = fit_column(grid, ac, ages, prefer_rows, ar + 1)
                if rows:
                    return self.put(tree, building, nodes, ac, rows)
                self.report.append(f'{self.civ}: {nodes[0]["name"]} has no room under {anchor["name"]}; it hangs from the {building_name}')
        nodes[0]['link_id'], nodes[0]['link_node_type'] = None, 'BuildingTech'  # main.js then draws its line to the building
        width = len(grid[0])
        columns = ([prefer_col] if prefer_col is not None and prefer_col < width else []) + [c for c in range(width) if c != prefer_col]
        for c in columns:
            rows = fit_column(grid, c, ages, prefer_rows)
            if rows:
                return self.put(tree, building, nodes, c, rows)
        for row in grid:
            row.append(None)
        rows = fit_column(grid, width, ages, prefer_rows)
        if rows is None:
            self.report.append(f'{self.civ}: no rows for the line {", ".join(n["name"] for n in nodes)} in the {building_name}')
            return False
        return self.put(tree, building, nodes, width, rows)

    def put(self, tree, building, nodes, col, rows):
        for n, r in zip(nodes, rows):
            building['grid'][r][col] = n['id']
            n['row'] = r
            n['building_id'] = building['building_id']
            tree['units_techs'].append(n)
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
        if model in self.icons:
            picture, icon_note = self.icons[model], ''
        else:
            fallback = self.template(FALLBACK_PICTURES.get(model, 'Knight'))
            picture, icon_note = (fallback[1]['picture_index'] if fallback else 0), '; icon is a stand-in'
        self.data['data']['Unit'][str(uid)] = {
            'internal_name': st['internal_name'], 'ID': uid, 'HP': st['hp'], 'Cost': st['cost'],
            'Attack': st['attack'] or 0, 'Range': st['range'] or 0, 'MeleeArmor': st['melee_armour'] or 0,
            'PierceArmor': st['pierce_armour'] or 0, 'LineOfSight': st['line_of_sight'], 'Speed': st['speed'],
            'ReloadTime': st['reload_time'], 'TrainTime': st['train_time'],
            'Attacks': [{'Amount': a['amount'], 'Class': a['class']} for a in st['attacks']],
            'Armours': [{'Amount': st['melee_armour'] or 0, 'Class': 4}, {'Amount': st['pierce_armour'] or 0, 'Class': 3}],
        }
        text = (f'Create <b>{name}</b> (‹cost›)<br>\nUnique unit of the codex, built on the Scenario Editor unit '
                f'{model} (existing game content{icon_note}).<br>\n<i>Upgrades: as the game\'s {model}.</i>'
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
        # A unique unit that keeps the name of one of the civ's own unique units and takes a Scenario
        # Editor unit as its model is the game's unit with that unit's look (RULES section 5): its line,
        # data and Elite upgrade stay, with the design's adapted stats.
        looks = {u['name'] for u in wanted if u['name'] in lines
                 and TREE_NAMES.get(u['model'], u['model']) not in self.catalog
                 and TREE_NAMES.get(u['model'], u['model']) in self.scenario}
        freed = []  # (building name, row, col) of removed castle unique-unit cells
        for base, nodes in lines.items():
            if base not in models and base not in looks:
                for n in nodes:
                    self.removed_units.add(n['name'])
                    b, r, c = grid_position(tree, n['id'])
                    if b is not None:
                        freed.append((b['name'], r, c, n['name'].startswith('Elite ')))
                    remove_from_grid(tree, n['id'])
        renamed_elites = {r['from'] for r in design.get('rename', [])}
        for u in wanted:
            model, name, building = TREE_NAMES.get(u['model'], u['model']), u['name'], u.get('building', 'Castle')
            if name in looks:
                self.apply_look(tree, u, lines[name], model)
                continue
            present = [n for n in tree['units_techs'] if n['name'] in (model, f'Elite {model}')]
            if not present:
                tmpl = self.template(model, building)
                age = AGE_IDS.get(u.get('age'))  # the design's age, else the model's own
                slot = next((f for f in freed if f[0] == building and not f[3]), None)
                eslot = next((f for f in freed if f[0] == building and f[3]), None)
                for s in (slot, eslot):
                    if s:
                        freed.remove(s)
                prefer_col = slot[2] if slot else None
                base_row = slot[1] if slot else AGE_ROWS[u.get('age', 'Castle')][0]
                if tmpl:
                    b_obj = find_building(tree, building)
                    if b_obj is None:
                        self.report.append(f'{self.civ}: no {building} for {name}')
                        continue
                    base_node = self.clone(tmpl[1], b_obj['building_id'])
                    base_node['node_type'] = 'UniqueUnit'
                    if age:
                        base_node['age_id'] = age
                    line = [base_node]
                    elite = self.template(f'Elite {model}', tmpl[2])
                    if elite:
                        elite_node = self.clone(elite[1], b_obj['building_id'])
                        elite_node['node_type'] = 'UniqueUnit'
                        elite_node['age_id'] = max(elite_node['age_id'], base_node['age_id'])
                        if elite_node.get('link_id') == base_node['node_id']:  # keep the line to its base
                            elite_node['link_node_type'] = base_node['node_type']
                        line.append(elite_node)
                    self.place_line(tree, building, line, prefer_col=prefer_col,
                                    prefer_rows=[base_row, eslot[1] if eslot else None])
                    present = line
                elif model in self.scenario:
                    b_obj = find_building(tree, building)
                    node = self.scenario_node(model, name, b_obj['building_id'] if b_obj else 82)
                    if node:
                        if age:
                            node['age_id'] = age
                        self.place_line(tree, building, [node], prefer_col=prefer_col, prefer_rows=[base_row])
                        if u.get('stats'):
                            self.adapt_stats(tree, node, u['stats'])
                        self.note(node, 'kept' if u.get('change') == 'kept' else 'new', why_text(u))
                        self.design_units.add(id(node))
                    continue
                else:
                    self.report.append(f'{self.civ}: no template for unique unit model {model}')
                    continue
            base_node = next((n for n in present if n['name'] == model), None)
            if base_node is not None and u.get('stats'):
                self.adapt_stats(tree, base_node, u['stats'])
            elite_node = next((n for n in present if n['name'] == f'Elite {model}'), None)
            if elite_node is not None and u.get('stats') and parse_stats(u['stats'], 'elite'):
                self.adapt_stats(tree, elite_node, u['stats'], 'elite')
            for n in present:
                retype(tree, n, 'UniqueUnit')
                self.design_units.add(id(n))
                self.note(n, 'kept' if u.get('change') == 'kept' else 'new', why_text(u))
                if n['name'] == model and name != model:
                    self.renamed_strings(n, model, name, f'(Codex: the game\'s {model}.)')
                elif n['name'] == f'Elite {model}' and name != model and f'Elite {model}' not in renamed_elites:
                    self.renamed_strings(n, f'Elite {model}', f'Elite {name}')

    def apply_look(self, tree, u, nodes, model):
        """The game's unique unit line with a Scenario Editor unit's look and the design's adapted stats."""
        picture = self.icons.get(model)
        for n in sorted(nodes, key=lambda n: n['name'].startswith('Elite ')):  # the base tier first
            retype(tree, n, 'UniqueUnit')
            if picture is not None:
                n['picture_index'] = picture
            look = f'The game\'s {esc(n["name"])} with the look of the Scenario Editor unit {esc(model)} (codex).'
            if u.get('stats'):  # the game's description and upgrade line no longer fit; the stats say what changed
                text = (f'Create <b>{esc(n["name"])}</b> (‹cost›)<br>\n{look}<br>\n<i>Upgrades: as the codex stats say.</i>'
                        f'<br>\n‹hp› ‹attack› ‹armor› ‹piercearmor› ‹range›')
            else:
                text = add_to_description(self.help_text(n), look)
            n['help_string_id'] = self.s.add(text) + 79000
            if u.get('stats'):
                tier = 'elite' if n['name'].startswith('Elite ') else 'base'
                if tier == 'base' or parse_stats(u['stats'], 'elite'):
                    self.adapt_stats(tree, n, u['stats'], tier)
            self.design_units.add(id(n))
            self.note(n, 'kept' if u.get('change') == 'kept' else 'new', why_text(u))

    def adapt_stats(self, tree, node, stats_text, tier='base'):
        """Give a level-2 unit its own data entry with the design's adapted stats (other civs keep the model)."""
        overrides = parse_stats(stats_text, tier)
        old_node_id = node['node_id']
        base = self.data['data']['Unit'].get(str(old_node_id))
        if base is None or not overrides:
            self.report.append(f'{self.civ}: could not apply adapted stats to {node["name"]}')
            return
        uid = self.next_unit
        self.next_unit += 1
        entry = copy.deepcopy(base)
        entry.update(overrides)
        entry['ID'] = uid
        if 'Attack' in overrides:  # the base melee or pierce attack in the attack list follows the new value
            for a in entry.get('Attacks', []):
                if a['Class'] in (3, 4) and a['Amount'] == base.get('Attack'):
                    a['Amount'] = overrides['Attack']
        if 'MeleeArmor' in overrides or 'PierceArmor' in overrides:
            entry['Armours'] = [a for a in entry.get('Armours', []) if a['Class'] not in (3, 4)] + [
                {'Amount': entry['MeleeArmor'], 'Class': 4}, {'Amount': entry['PierceArmor'], 'Class': 3}]
        change = class_change(stats_text)
        if change:
            entry['Armours'] = [dict(a, Class=change[1]) if a['Class'] == change[0] else a for a in entry.get('Armours', [])]
            if not any(a['Class'] == change[1] for a in entry['Armours']):
                entry['Armours'].append({'Amount': 0, 'Class': change[1]})
        self.data['data']['Unit'][str(uid)] = entry
        upgrades = self.data['data'].get('unit_upgrades', {})
        if str(old_node_id) in upgrades:  # an Elite tier keeps its upgrade's cost and time
            upgrades[str(uid)] = copy.deepcopy(upgrades[str(old_node_id)])
        old_id = node['id']
        node['node_id'] = uid
        node['id'] = f"Unit_{uid}_{node['building_id']}"
        b, r, c = grid_position(tree, old_id)
        if b is not None:
            b['grid'][r][c] = node['id']
        for other in tree['units_techs']:  # keep the line to the next tier (an Elite links to its base by id)
            if other is not node and other.get('link_id') == old_node_id and other.get('link_node_type') == node['node_type']:
                other['link_id'] = uid
        text = add_to_description(self.help_text(node), f'Codex stats (level 2): {esc(stats_text)}')
        node['help_string_id'] = self.s.add(text) + 79000

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
            if slot:
                old_cells.remove(slot)
            self.place_line(tree, building, [node], prefer_col=slot[2] if slot else None,
                            prefer_rows=[slot[1] if slot else AGE_ROWS[age][0]])
            self.note(node, 'kept' if ut.get('change') == 'kept' else 'new', why_text(ut))

    # ---- tree and renames ---------------------------------------------------------------------
    def nodes_named(self, tree, name):
        name = TREE_NAMES.get(name, name)
        return ([n for n in tree['units_techs'] if n['name'] == name]
                + [b for b in tree['buildings'] if b['name'] == name])

    def apply_tree(self, tree, design):
        t = design.get('tree', {})
        reasons = t.get('basis', {})
        for name in t.get('remove', []):
            nodes = self.nodes_named(tree, name)
            if not nodes and TREE_NAMES.get(name, name) in self.tree_names and name not in self.removed_units:
                self.report.append(f'{self.civ}: remove {name}: not in the tree')
            for n in nodes:
                if n.get('node_status') != 'NotAvailable':
                    self.note(n, 'removed', reasons.get(name))
                n['node_status'] = 'NotAvailable'
        pending = []  # added items that need a place in the tree
        for name in t.get('add', []):
            nodes = self.nodes_named(tree, name)
            if nodes:
                for n in nodes:
                    if n.get('node_status') == 'NotAvailable':
                        self.note(n, 'added', reasons.get(name))
                    n['node_status'] = 'ResearchedCompleted'
                continue
            tname = TREE_NAMES.get(name, name)
            if tname in self.building_catalog:
                building = copy.deepcopy(self.building_catalog[tname][1])
                building['node_status'] = 'ResearchedCompleted'
                if building['grid']:
                    building['grid'] = [[None for _ in row] for row in building['grid']]
                tree['buildings'].append(building)
                self.note(building, 'added', reasons.get(name))
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
            pending.append({'name': name, 'node': node, 'building': bname, 'row': r, 'col': c,
                            'anchor': template_anchor(self.trees[civ], tnode)})
        # Added items that upgrade one another (a unit and its Elite) go in one column, in their order.
        by_id = {p['node']['node_id']: p for p in pending}
        children = {p['anchor']: p for p in pending if p['anchor'] in by_id and by_id[p['anchor']]['building'] == p['building']}
        for root in [p for p in pending if p not in children.values()]:
            line = [root]
            while line[-1]['node']['node_id'] in children:
                line.append(children[line[-1]['node']['node_id']])
            if self.place_line(tree, root['building'], [p['node'] for p in line], anchor_id=root['anchor'],
                               prefer_col=root['col'], prefer_rows=[p['row'] for p in line]):
                for p in line:
                    self.note(p['node'], 'added', reasons.get(p['name']))

    def apply_renames(self, tree, design):
        for rn in design.get('rename', []):
            nodes = self.nodes_named(tree, rn['from'])
            if not nodes:
                if not self.nodes_named(tree, rn['to']) and TREE_NAMES.get(rn['from'], rn['from']) in self.tree_names:
                    self.report.append(f'{self.civ}: rename {rn["from"]}: not in the tree')
                continue
            for n in nodes:
                self.renamed_strings(n, n['name'], rn['to'])
                if rn.get('model') in self.icons and n.get('use_type') == 'Unit':
                    n['picture_index'] = self.icons[rn['model']]
                self.note(n, 'renamed', f'Renamed from {rn["from"]}' + (f', with the look of the {rn["model"]}' if rn.get('model') else '')
                          + '. ' + rn.get('basis', ''))

    # ---- civ panel ----------------------------------------------------------------------------
    def civ_text(self, design, file_stem, extra_units=()):
        p = design['profile']
        lines = [esc(design['label'])]
        meta = f'Time window: <b>{esc(p["window"])}</b>.'
        if design.get('original_name'):
            meta += f' Called <b>{esc(design["original_name"])}</b> in the game.'
        lines.append(f'<i>{meta}</i>')
        lines.append('')
        for b in design.get('bonus', []):
            lines.append('• ' + with_why(esc(b['text']), why_text(b)))
        lines.append('')
        lines.append('<b>Unique Units:</b>')
        units = [with_why(f'{esc(u["name"])} ({esc(u.get("building", "Castle"))})', why_text(u)) for u in design.get('unique_unit', [])]
        units += [with_why(f'{esc(name)} ({esc(building)})', SINGLE_CIV_WHY) for name, building in extra_units]
        lines.append(', '.join(units))
        lines.append('')
        lines.append('<b>Unique Techs:</b>')
        for ut in design.get('unique_tech', []):
            lines.append('• ' + with_why(f'{esc(ut["name"])} [{esc(ut["building"])}, {esc(ut["age"])}] ({esc(ut["effect"])})', why_text(ut)))
        lines.append('')
        lines.append('<b>Team Bonus:</b>')
        lines.append(with_why(esc(design['team_bonus']['text']), why_text(design['team_bonus'])))
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
        panels = []  # civ panels are written after the single-civ pass, which can add unique units
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
                panels.append((civ_key, civ_entry, design, stem))
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
        single = self.single_civ_units(out_trees, [k for k in self.data['civs'] if k in designs])
        # Report layout problems that the game's own trees do not have (the game's data has some of its
        # own, such as items stacked under an item they do not link to by type; those are left as they are).
        game_layout = {key: {p[:3] for p in layout_problems(t)} for key, t in self.trees.items()}
        everywhere = {p for probs in game_layout.values() for p in probs if p[0] == 'not under the item it upgrades'}
        for civ_key in designs:
            key = civ_key.upper()
            for p in layout_problems(out_trees[key]):
                if p[:3] not in game_layout.get(key, set()) | everywhere:
                    self.report.append(f'{civ_key}: layout: {p[3]} is {p[0]} ({p[1]}, row {p[4]}, column {p[5]})')
        for civ_key, civ_entry, design, stem in panels:
            civ_entry['help_string_id'] = self.s.add(self.civ_text(design, stem, single.get(civ_key, [])))
        changes = {}
        for civ_key, notes in self.notes.items():
            nodes = changes.setdefault(civ_key, {})
            for obj, kind, why in notes:
                entry = nodes.setdefault(obj['id'], {'kinds': [], 'why': []})
                if kind not in entry['kinds']:
                    entry['kinds'].append(kind)
                if why and why not in entry['why']:
                    entry['why'].append(why)
        for key, tree in out_trees.items():
            save(OUT / 'trees' / f'{key}.json', tree)
        save(OUT / 'data.json', self.data)
        save(OUT / 'codex.json', {'civs': changes})
        for loc_dir in sorted((ROOT / 'data' / 'locales').iterdir()):
            strings = load(loc_dir / 'strings.json')
            strings.update(self.s.extra)
            strings['1'] = 'Codex'
            save(OUT / 'locales' / loc_dir.name / 'strings.json', strings)
        # Cache busting: the generated files refer to each other by string ids that change between
        # builds, so a browser must never mix files of two builds. version.js runs before main.js
        # (which requests data.json as soon as it runs) and adds this build to every request for a
        # data file.
        build = hashlib.sha1(json.dumps([self.data, self.s.extra, changes, out_trees], sort_keys=True).encode('utf-8')).hexdigest()[:12]
        js = ('// Generated by codex/tools/build_site.py: load the data files of this build, never a cached older one.\n'
              '(function () {\n'
              '    const open = XMLHttpRequest.prototype.open;\n'
              '    XMLHttpRequest.prototype.open = function (method, url) {\n'
              '        const args = Array.prototype.slice.call(arguments);\n'
              "        if (typeof url === 'string' && url.indexOf('data/') === 0) {\n"
              f"            args[1] = url + (url.indexOf('?') < 0 ? '?' : '&') + 'v={build}';\n"
              '        }\n'
              '        return open.apply(this, args);\n'
              '    };\n'
              '})();\n')
        (OUT.parent / 'version.js').write_text(js, encoding='utf-8', newline='\n')
        # The page's own scripts and styles carry the build too, so a cached older version.js,
        # codex.js or codex.css is never used with this build's data.
        assets = hashlib.sha1(b''.join((OUT.parent / f).read_bytes() for f in ('codex.js', 'codex.css', 'compare.js'))).hexdigest()[:8]
        for page in ('index.html', 'compare.html'):
            path = OUT.parent / page
            html = path.read_text(encoding='utf-8')
            html = re.sub(r'src="version\.js(\?v=[0-9a-f]+)?"', f'src="version.js?v={hashlib.sha1(js.encode()).hexdigest()[:12]}"', html)
            html = re.sub(r'(src|href)="(codex\.js|codex\.css|compare\.js)(\?v=[0-9a-f]+)?"', rf'\1="\2?v={assets}"', html)
            path.write_text(html, encoding='utf-8', newline='\n')
        print(f'built {len(out_trees)} civs ({len(designs)} designs), {len(self.s.extra)} custom strings, build {build}')
        for line in self.report:
            print('note:', line)

    def unit_identity(self, node):
        """The game's name of a unit, so that renamed copies and per-civ variants count as the same unit."""
        if not hasattr(self, 'game_unit_names'):
            self.game_unit_names = {n['node_id']: n['name'] for tree in self.trees.values()
                                    for n in tree['units_techs'] if n['use_type'] == 'Unit'}
        return self.game_unit_names.get(node['node_id'], node['name'])

    def single_civ_units(self, trees, civs):
        """RULES 6.1: a unit that only one designed civ has is a unique unit, wherever it is trained;
        a unit that two or more share is regional unless a design makes it its unique unit."""
        holders = {}
        single = {}  # civ -> [(unit line, building)] made unique by the rule
        for civ_key in civs:
            for n in trees[civ_key.upper()]['units_techs']:
                if n['use_type'] == 'Unit' and n['node_status'] != 'NotAvailable':
                    holders.setdefault(self.unit_identity(n), set()).add(civ_key)
        for civ_key in civs:
            self.civ = civ_key
            for n in trees[civ_key.upper()]['units_techs']:
                if n['use_type'] != 'Unit' or n['node_status'] == 'NotAvailable':
                    continue
                shared = len(holders.get(self.unit_identity(n), ())) > 1
                if n['node_type'] in ('Unit', 'RegionalUnit', 'UnitUpgrade') and not shared:
                    retype(trees[civ_key.upper()], n, 'UniqueUnit')
                    self.note(n, 'new', SINGLE_CIV_WHY)
                    b, _, _ = grid_position(trees[civ_key.upper()], n['id'])
                    line = (n['name'][6:] if n['name'].startswith('Elite ') else n['name'], b['name'] if b else '?')
                    if line not in single.setdefault(civ_key, []):
                        single[civ_key].append(line)
                    self.report.append(f'{civ_key}: {n["name"]} is held by no other civ and is shown as a unique unit')
                elif n['node_type'] == 'UniqueUnit' and shared and id(n) not in self.design_units:
                    retype(trees[civ_key.upper()], n, 'RegionalUnit')
                    self.report.append(f'{civ_key}: {n["name"]} is shared with other civs and is shown as a regional unit')
        for civ_key in civs:
            lines = {n['name'][6:] if n['name'].startswith('Elite ') else n['name']
                     for n in trees[civ_key.upper()]['units_techs']
                     if n['node_type'] == 'UniqueUnit' and n['node_status'] != 'NotAvailable' and n['use_type'] == 'Unit'}
            if len(lines) > UNIQUE_UNIT_EXCEPTIONS.get(civ_key, UNIQUE_UNIT_CAP):
                self.report.append(f'{civ_key}: {len(lines)} unique unit lines ({", ".join(sorted(lines))}), over the 1 or 2 of RULES 6.1')
        return single

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
