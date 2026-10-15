"""Render the AoE2 historical-accuracy report JSON into a single HTML page.

usage: python -I render.py report.json out.html
report.json = {"synthesis": md, "groups": [verified group], "themes": [verified theme], "date": "..."}
"""
import html
import json
import re
import sys

REGION_PT = {
    '01_britain_france': 'Grã-Bretanha e França',
    '02_iberia_italy_rome': 'Ibéria, Itália e Roma',
    '03_central_europe': 'Europa Central',
    '04_norse_slavs_goths': 'Nórdicos, Eslavos e Godos',
    '05_byzantium_balkans_caucasus': 'Bizâncio, Balcãs e Cáucaso',
    '06_steppe': 'Estepe',
    '07_islamic_world_africa': 'Mundo Islâmico e África',
    '08_indian_subcontinent': 'Subcontinente Indiano',
    '09_china': 'China',
    '10_east_southeast_asia': 'Ásia Oriental e do Sudeste',
    '11_americas': 'Américas',
}
RATING_PT = {
    'faithful': 'Fiel',
    'plausible': 'Plausível',
    'abstraction': 'Abstração',
    'stretched': 'Forçado',
    'anachronistic': 'Anacrónico',
    'wrong': 'Errado',
    'unfounded': 'Sem base',
}
RATING_DESC = {
    'faithful': 'Diretamente assente na história documentada deste povo',
    'plausible': 'Ligação defensável, com pequeno exagero',
    'abstraction': 'Mecânica de jogo que representa um traço real',
    'stretched': 'Ligação fraca ou forçada',
    'anachronistic': 'Coisa real, mas de outra época ou lugar',
    'wrong': 'Premissa factualmente incorreta',
    'unfounded': 'Sem base histórica; puro equilíbrio de jogo',
}
KIND_PT = {
    'label': 'Rótulo', 'bonus': 'Bónus', 'unique_unit': 'Unidade única', 'unique_tech': 'Tech única',
    'team_bonus': 'Bónus de equipa', 'unique_building': 'Edifício único', 'tech_tree': 'Tech tree',
}
PROP_PT = {
    'bonus': 'Bónus', 'unique_unit': 'Unidade única', 'unique_tech': 'Tech única', 'team_bonus': 'Bónus de equipa',
    'tech_tree': 'Tech tree', 'rename': 'Renomear', 'building': 'Edifício', 'other': 'Outro',
}
SEV_PT = {'minor': 'menor', 'moderate': 'moderado', 'major': 'grave'}
CONF_PT = {'high': 'alta', 'medium': 'média', 'low': 'baixa'}
THEME_ORDER = ['game_model', 'tech_tree_audit', 'names_descriptions', 'representation']
TECHTREE_SLUG = {'Incas': 'Incas', 'Mayans': 'Mayans'}

e = html.escape


def inline_md(s):
    s = e(s)
    s = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', s)
    s = re.sub(r'(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])', r'<em>\1</em>', s)
    s = re.sub(r'(?<![\w_])_(?!\s)(.+?)(?<!\s)_(?![\w_])', r'<em>\1</em>', s)
    s = re.sub(r'`(.+?)`', r'<code>\1</code>', s)
    return s


def md_to_html(md):
    """Small Markdown subset: ##/### headings, paragraphs, one level of nested lists, pipe tables."""
    out, para, table = [], [], []
    lst = None  # (tag, [[text, subtag, [subitems]]])

    def flush_para():
        if para:
            out.append('<p>' + inline_md(' '.join(para)) + '</p>')
            para.clear()

    def flush_list():
        nonlocal lst
        if lst:
            tag, items = lst
            lis = []
            for text, subtag, sub in items:
                inner = inline_md(text)
                if sub:
                    inner += f'<{subtag}>' + ''.join(f'<li>{inline_md(x)}</li>' for x in sub) + f'</{subtag}>'
                lis.append(f'<li>{inner}</li>')
            out.append(f'<{tag}>' + ''.join(lis) + f'</{tag}>')
            lst = None

    def flush_table():
        if table:
            rows = [[c.strip() for c in r.strip().strip('|').split('|')] for r in table]
            head, body = rows[0], [r for r in rows[1:] if not all(re.fullmatch(r':?-{2,}:?', c) for c in r)]
            out.append('<div class="tbl-wrap"><table class="md"><thead><tr>' + ''.join(f'<th>{inline_md(c)}</th>' for c in head)
                       + '</tr></thead><tbody>' + ''.join('<tr>' + ''.join(f'<td>{inline_md(c)}</td>' for c in r) + '</tr>' for r in body)
                       + '</tbody></table></div>')
            table.clear()

    lines = md.splitlines()
    if lines and re.match(r'^#\s', lines[0]):
        lines = lines[1:]
    for raw in lines:
        line = raw.rstrip()
        if line.lstrip().startswith('|'):
            flush_para(); flush_list(); table.append(line); continue
        flush_table()
        if not line.strip():
            flush_para(); flush_list(); continue
        m = re.match(r'^(#{2,4})\s+(.*)$', line)
        if m:
            flush_para(); flush_list()
            lvl = len(m.group(1))
            text = m.group(2).strip()
            sid = 'sx-' + re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')[:40]
            out.append(f'<h{lvl} id="{sid}">{inline_md(text)}</h{lvl}>')
            continue
        if re.match(r'^\s*(---|\*\*\*)\s*$', line):
            flush_para(); flush_list(); out.append('<hr>'); continue
        indent = len(raw) - len(raw.lstrip(' \t'))
        m = re.match(r'^\s*[-*•]\s+(.*)$', line)
        m2 = re.match(r'^\s*\d+[.)]\s+(.*)$', line)
        if m or m2:
            flush_para()
            tag = 'ul' if m else 'ol'
            text = (m or m2).group(1)
            if indent >= 2 and lst:
                last = lst[1][-1]
                last[1] = last[1] or tag
                last[2].append(text)
                continue
            if not lst or lst[0] != tag:
                flush_list(); lst = (tag, [])
            lst[1].append([text, None, []])
            continue
        if lst and indent >= 2:
            last = lst[1][-1]
            if last[2]:
                last[2][-1] += ' ' + line.strip()
            else:
                last[0] += ' ' + line.strip()
            continue
        flush_list()
        if line.lstrip().startswith('>'):
            flush_para(); out.append('<blockquote>' + inline_md(line.lstrip('> ')) + '</blockquote>'); continue
        para.append(line.strip())
    flush_para(); flush_list(); flush_table()
    return '\n'.join(out)


def slug(civ):
    return 'civ-' + re.sub(r'[^a-z0-9]+', '-', civ.lower())


def score_class(s):
    return 'lo' if s <= 3 else ('mid' if s <= 6 else 'hi')


def score_meter(s):
    cells = ''.join(f'<i class="{"on" if k < s else ""}"></i>' for k in range(10))
    return f'<span class="meter {score_class(s)}" role="img" aria-label="Fidelidade {s} em 10">{cells}</span>'


def rating_chip(r):
    return f'<span class="chip r-{r}" title="{e(RATING_DESC.get(r, ""))}">{RATING_PT.get(r, r)}</span>'


def render_civ(c, region_key):
    civ = c['civ']
    counts = {}
    for el in c['elements']:
        counts[el['rating']] = counts.get(el['rating'], 0) + 1
    dist = ''.join(
        f'<span class="dist-seg r-{r}" style="flex:{counts[r]}" title="{RATING_PT[r]}: {counts[r]}"></span>'
        for r in RATING_PT if counts.get(r)
    )
    parts = []
    parts.append(f'''<div class="civ-head-body">
  <p class="represents"><strong>Representa:</strong> {e(c["represents_pt"])} <span class="period">· {e(c["period_pt"])}</span></p>
  <p class="verdict">{e(c["verdict_pt"])}</p>
  <p class="meta-line">Confiança da análise: {CONF_PT.get(c["confidence"], c["confidence"])} · <a href="https://aoe2techtree.net/#{e(civ)}" target="_blank" rel="noopener">Ver no aoe2techtree.net</a></p>
</div>''')
    if c.get('naming_scope_issues_pt'):
        parts.append(f'<h4>Nome, âmbito e época</h4><p>{e(c["naming_scope_issues_pt"])}</p>')
    rows = ''.join(
        f'<tr><td class="el-name">{e(el["element"])}<span class="kind">{KIND_PT.get(el["kind"], el["kind"])}</span></td>'
        f'<td>{rating_chip(el["rating"])}</td><td class="expl">{e(el["explanation_pt"])}</td></tr>'
        for el in c['elements']
    )
    parts.append(f'<h4>Elemento a elemento</h4><div class="tbl-wrap"><table class="elements"><thead><tr><th>Elemento</th><th>Avaliação</th><th>Porquê</th></tr></thead><tbody>{rows}</tbody></table></div>')
    if c['tree_issues']:
        parts.append('<h4>Tech tree</h4><ul class="plain">' + ''.join(
            f'<li><strong>{e(t["item"])}</strong> {e(t["problem_pt"])}</li>' for t in c['tree_issues']) + '</ul>')
    if c['history_text_issues']:
        parts.append('<h4>Texto de história do jogo</h4><div class="hist">' + ''.join(
            f'<div class="hist-item sev-{h["severity"]}"><p class="claim"><span class="sev">{SEV_PT[h["severity"]]}</span>{e(h["claim_pt"])}</p>'
            f'<p><strong>Problema:</strong> {e(h["problem_pt"])}</p><p><strong>Correção:</strong> {e(h["correction_pt"])}</p></div>'
            for h in c['history_text_issues']) + '</div>')
    if c['missing_features_pt']:
        parts.append('<h4>O que falta</h4><ul class="plain">' + ''.join(f'<li>{e(x)}</li>' for x in c['missing_features_pt']) + '</ul>')
    if c['proposals']:
        parts.append('<h4>Propostas para mais fidelidade</h4><div class="props">' + ''.join(
            f'<div class="prop"><p class="prop-title"><span class="ptype">{PROP_PT.get(p["type"], p["type"])}</span>{e(p["title_pt"])}</p>'
            f'<p>{e(p["description_pt"])}</p><p class="basis"><strong>Base histórica:</strong> {e(p["historical_basis_pt"])}</p></div>'
            for p in c['proposals']) + '</div>')
    if c['contested_pt']:
        parts.append('<h4>Pontos em debate entre historiadores</h4><ul class="plain">' + ''.join(f'<li>{e(x)}</li>' for x in c['contested_pt']) + '</ul>')
    if c['key_sources']:
        parts.append('<h4>Fontes e historiadores</h4><p class="sources">' + ' · '.join(e(x) for x in c['key_sources']) + '</p>')
    worst = sum(counts.get(r, 0) for r in ('wrong', 'anachronistic', 'unfounded'))
    return f'''<details class="civ" id="{slug(civ)}" data-region="{region_key}" data-score="{c["fidelity_score"]}" data-name="{e(civ.lower())}">
<summary>
  <img class="emblem" src="emblems/{civ.lower()}.png" alt="" width="44" height="44" loading="lazy">
  <span class="civ-title"><span class="civ-name">{e(civ)}</span><span class="civ-region">{e(REGION_PT.get(region_key, region_key))}</span></span>
  <span class="civ-score"><span class="score-num {score_class(c["fidelity_score"])}">{c["fidelity_score"]}</span>{score_meter(c["fidelity_score"])}</span>
  <span class="dist" aria-label="Distribuição das avaliações">{dist}</span>
  <span class="flags">{worst} problemas graves</span>
</summary>
<div class="civ-body">{''.join(parts)}</div>
</details>'''


def render_theme(t):
    findings = ''.join(
        f'<div class="finding sev-{f["severity"]}"><p class="f-title"><span class="sev">{SEV_PT[f["severity"]]}</span>{e(f["title_pt"])}</p>'
        f'<p>{e(f["detail_pt"])}</p>'
        + (('<p class="examples">' + ' · '.join(e(x) for x in f['examples']) + '</p>') if f['examples'] else '')
        + '</div>'
        for f in t['findings']
    )
    qs = ''.join(f'<li>{e(q)}</li>' for q in t['debate_questions_pt'])
    ps = ''.join(f'<li>{e(p)}</li>' for p in t['proposals_pt'])
    return f'''<details class="theme" id="tema-{t["theme"]}">
<summary><span class="theme-title">{e(t["title_pt"])}</span><span class="theme-sum">{e(t["summary_pt"])}</span></summary>
<div class="theme-body">
<h4>Constatações</h4>{findings}
<div class="two-col"><div><h4>Perguntas para debate</h4><ol>{qs}</ol></div><div><h4>Propostas</h4><ul>{ps}</ul></div></div>
</div>
</details>'''


def main(src, dst):
    R = json.load(open(src, encoding='utf-8'))
    civs = []
    for g in R['groups']:
        for c in g['civs']:
            civs.append((c, g['group']))
    civs.sort(key=lambda x: x[0]['civ'])
    n = len(civs)
    avg = sum(c['fidelity_score'] for c, _ in civs) / max(n, 1)
    totals = {}
    for c, _ in civs:
        for el in c['elements']:
            totals[el['rating']] = totals.get(el['rating'], 0) + 1
    tot_el = sum(totals.values()) or 1
    overall_dist = ''.join(
        f'<div class="od-row"><span class="od-label">{rating_chip(r)}</span><span class="od-bar"><span class="r-{r}" style="width:{100*totals.get(r,0)/tot_el:.1f}%"></span></span><span class="od-n">{totals.get(r,0)}</span></div>'
        for r in RATING_PT)

    ranking = sorted(civs, key=lambda x: (-x[0]['fidelity_score'], x[0]['civ']))
    rank_rows = ''.join(
        f'<a class="rk" href="#{slug(c["civ"])}" data-region="{g}"><span class="rk-name">{e(c["civ"])}</span>'
        f'<span class="rk-bar"><span class="{score_class(c["fidelity_score"])}" style="width:{c["fidelity_score"]*10}%"></span></span>'
        f'<span class="rk-n">{c["fidelity_score"]}</span></a>'
        for c, g in ranking)

    region_opts = ''.join(f'<option value="{k}">{e(v)}</option>' for k, v in REGION_PT.items())
    civ_html = '\n'.join(render_civ(c, g) for c, g in civs)
    themes = sorted(R['themes'], key=lambda t: THEME_ORDER.index(t['theme']) if t['theme'] in THEME_ORDER else 99)
    theme_html = '\n'.join(render_theme(t) for t in themes)
    cross = ''.join(
        f'<details class="cross"><summary>{e(REGION_PT.get(g["group"], g["group"]))}</summary><p>{e(g["cross_civ_notes_pt"])}</p></details>'
        for g in sorted(R['groups'], key=lambda g: g['group']))
    synthesis_html = md_to_html(R['synthesis'])
    legend = ''.join(f'<li>{rating_chip(r)} {e(RATING_DESC[r])}</li>' for r in RATING_PT)

    tpl = open(__file__.replace('render.py', 'template.html'), encoding='utf-8').read()
    page = (tpl.replace('%%N%%', str(n))
               .replace('%%AVG%%', f'{avg:.1f}'.replace('.', ','))
               .replace('%%NEL%%', str(tot_el))
               .replace('%%DATE%%', e(R.get('date', '')))
               .replace('%%OVERALL_DIST%%', overall_dist)
               .replace('%%RANKING%%', rank_rows)
               .replace('%%REGION_OPTS%%', region_opts)
               .replace('%%SYNTHESIS%%', synthesis_html)
               .replace('%%LEGEND%%', legend)
               .replace('%%THEMES%%', theme_html)
               .replace('%%CROSS%%', cross)
               .replace('%%CIVS%%', civ_html))
    open(dst, 'w', encoding='utf-8').write(page)
    print('wrote', dst, len(page))


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
