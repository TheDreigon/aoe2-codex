"""Prepare local working files from the game data in this repository.

Usage (from the repository root):
    python -I codex/tools/prepare_data.py [--history]

Writes to codex/.local/data/ (ignored by git):
  - civ_bonuses.md      the bonus text of every civ
  - civ_trees.md        each civ's gaps compared with the majority of civs, plus its rare items
  - all_items.md        every unit, tech and building, with its description and the civs that have it
  - regions/<region>.md one file per region (regions.json) combining all of the above, plus the
                        original history text when it exists in codex/.local/original-history/
With --history, first downloads the game's history texts (from the fandom wiki) into
codex/.local/original-history/. Those texts belong to Microsoft: they stay local only.
"""
import json
import re
import sys
import time
import urllib.parse
import urllib.request
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TOOLS = Path(__file__).resolve().parent
OUT = ROOT / 'codex' / '.local' / 'data'
HIST = ROOT / 'codex' / '.local' / 'original-history'

# Wiki page holding each civ's "History" section.
WIKI_PAGES = {
    'Armenians': 'Armenians', 'Aztecs': 'Aztecs (Age of Empires II)', 'Bengalis': 'Bengalis',
    'Berbers': 'Berbers (Age of Empires II)', 'Bohemians': 'Bohemians', 'Britons': 'Britons',
    'Bulgarians': 'Bulgarians', 'Burgundians': 'Burgundians', 'Burmese': 'Burmese',
    'Byzantines': 'Byzantines (Age of Empires II)', 'Celts': 'Celts', 'Chinese': 'Chinese (Age of Empires II)',
    'Cumans': 'Cumans', 'Danes': 'Danes (Age of Empires II)', 'Dravidians': 'Dravidians',
    'Ethiopians': 'Ethiopians (Age of Empires II)', 'Franks': 'Franks', 'Georgians': 'Georgians',
    'Goths': 'Goths', 'Gurjaras': 'Gurjaras', 'Hindustanis': 'Hindustanis', 'Huns': 'Huns',
    'Incas': 'Inca (Age of Empires II)', 'Italians': 'Italians (Age of Empires II)',
    'Japanese': 'Japanese (Age of Empires II)', 'Jurchens': 'Jurchens', 'Khitans': 'Khitans', 'Khmer': 'Khmer',
    'Koreans': 'Koreans', 'Lithuanians': 'Lithuanians', 'Magyars': 'Magyars', 'Malay': 'Malay',
    'Malians': 'Malians (Age of Empires II)', 'Mapuche': 'Mapuche (Age of Empires II)',
    'Mayans': 'Maya (Age of Empires II)', 'Mongols': 'Mongols (Age of Empires II)', 'Muisca': 'Muisca',
    'Persians': 'Persians (Age of Empires II)', 'Poles': 'Poles (Age of Empires II)',
    'Portuguese': 'Portuguese (Age of Empires II)', 'Romans': 'Romans (Age of Empires II)',
    'Saracens': 'Saracens', 'Saxons': 'Saxons', 'Shu': 'Shu', 'Sicilians': 'Sicilians', 'Slavs': 'Slavs',
    'Spanish': 'Spanish (Age of Empires II)', 'Tatars': 'Tatars (Age of Empires II)', 'Teutons': 'Teutons',
    'Tupi': 'Tupi (Age of Empires II)', 'Turks': 'Turks', 'Varangians': 'Varangians', 'Vietnamese': 'Vietnamese',
    'Vikings': 'Vikings (Age of Empires II)', 'Wei': 'Wei', 'Wu': 'Wu',
}


def clean(t):
    t = re.sub(r'<br>', '\n', t)
    t = re.sub(r'<[^>]+>', '', t)
    return re.sub(r'\n\s*\n+', '\n', t).strip()


def fetch_history():
    HIST.mkdir(parents=True, exist_ok=True)
    for civ, page in WIKI_PAGES.items():
        url = 'https://ageofempires.fandom.com/api.php?' + urllib.parse.urlencode(
            {'action': 'parse', 'page': page, 'prop': 'wikitext', 'format': 'json', 'redirects': 1})
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        try:
            w = json.load(urllib.request.urlopen(req, timeout=30))['parse']['wikitext']['*']
        except Exception as exc:  # noqa: BLE001 - report and continue with the other civs
            print(civ, 'ERROR', exc)
            continue
        m = re.search(r'(?ms)^==\s*History\s*==\s*\n(.*?)(?=^==[^=])', w)
        h = m.group(1) if m else ''
        h = re.sub(r'<ref[^>]*?/>|<ref[^>]*>.*?</ref>', '', h, flags=re.S)
        h = re.sub(r'\[\[(?:[^|\]]*\|)?([^\]]*)\]\]', r'\1', h)
        h = re.sub(r"'''?", '', h)
        h = re.sub(r'</?(?:section|onlyinclude|noinclude)[^>]*>', '', h)
        (HIST / f'{civ}.md').write_text(
            f'# {civ}: original in-game history text (ageofempires.fandom.com, page "{page}")\n\n' + h.strip() + '\n',
            encoding='utf-8')
        print(civ, len(h))
        time.sleep(0.3)


def main():
    if '--history' in sys.argv:
        fetch_history()
    d = json.loads((ROOT / 'data' / 'data.json').read_text(encoding='utf-8'))
    s = json.loads((ROOT / 'data' / 'locales' / 'en' / 'strings.json').read_text(encoding='utf-8'))
    dd, civs = d['data'], d['civs']
    n = len(civs)

    def name_help(kind, i):
        x = dd[kind].get(str(i))
        if not x:
            return str(i), ''
        t = s.get(str(x['LanguageNameId'] + 21000)) or ''
        m = re.search(r'<b>(.+?)</b>', t)
        return (m.group(1) if m else x.get('internal_name')), clean(t)

    cnt = {k: Counter(i for c in civs.values() for i in c[k]) for k in ['Unit', 'Tech', 'Building']}
    OUT.mkdir(parents=True, exist_ok=True)

    bonuses = []
    for name, c in civs.items():
        bonuses.append(f'### {name}\n' + clean(s.get(str(c['help_string_id']), '')) + '\n')
    (OUT / 'civ_bonuses.md').write_text('\n'.join(bonuses), encoding='utf-8')

    def gaps(name):
        c = civs[name]
        lines = []
        for k in ['Unit', 'Tech', 'Building']:
            have = set(c[k])
            common = [i for i, v in cnt[k].items() if v >= n * 0.5]
            miss = sorted({name_help(k, i)[0] for i in common if i not in have})
            lines.append(f'- {k} MISSING (held by >=50% of civs): ' + (', '.join(miss) or 'none'))
        lines.append('- Rare/unique items (held by <=3 civs):')
        for k in ['Unit', 'Tech', 'Building']:
            for i in sorted(set(c[k])):
                if cnt[k][i] <= 3:
                    nm, h = name_help(k, i)
                    lines.append(f'  - [{k}] {nm} ({cnt[k][i]} civ(s)): ' + h.replace('\n', ' ')[:600])
        return '\n'.join(lines)

    (OUT / 'civ_trees.md').write_text(
        '\n\n'.join(f'## {name}\n' + gaps(name) for name in civs), encoding='utf-8')

    items = ['# All units, techs and buildings, with description and how many civs have each']
    for k in ['Unit', 'Tech', 'Building']:
        items.append(f'\n## {k}')
        for i, v in sorted(cnt[k].items(), key=lambda x: -x[1]):
            nm, h = name_help(k, i)
            holders = '' if v >= n - 12 else ' | civs: ' + ', '.join(cn for cn, c in civs.items() if i in c[k])
            items.append(f'- {nm} [{v}/{n}]{holders}: ' + h.replace('\n', ' ')[:400])
    (OUT / 'all_items.md').write_text('\n'.join(items), encoding='utf-8')

    regions = json.loads((TOOLS / 'regions.json').read_text(encoding='utf-8'))
    (OUT / 'regions').mkdir(exist_ok=True)
    for g, cl in regions.items():
        blocks = []
        for name in cl:
            hist_file = HIST / f'{name}.md'
            hist = hist_file.read_text(encoding='utf-8') if hist_file.exists() else '(history text not downloaded: run with --history)'
            blocks.append(f'## {name}\n### Bonus text\n' + clean(s.get(str(civs[name]['help_string_id']), ''))
                          + '\n### Tech tree\n' + gaps(name) + '\n### Original history text\n' + hist)
        (OUT / 'regions' / f'{g}.md').write_text(f'# Region: {g}\n\n' + '\n\n'.join(blocks), encoding='utf-8')
    print('ok:', OUT)


if __name__ == '__main__':
    main()
