#!/usr/bin/env python3
"""
Rebuild report and highlights with source links.

Edit results/source_links.json to add/fix URLs, then run:
    python rebuild_links.py

This regenerates:
    - results/report.typ (entities section with #link() syntax)
    - results/highlights.html (DATA JSON with <a> tags)
    - results/report.pdf (recompiled, if typst is installed)
"""

import json
import re
import subprocess
import shutil

# ─── Load data ───

with open('results/source_links.json') as f:
    URLS = json.load(f)

with open('results/entity_research.json') as f:
    research = json.load(f)
research_by_name = {r['name']: r for r in research}

with open('results/consensus_entities.json') as f:
    entities = json.load(f)['entities']

GROUPS = [
    (1, 'Energy & Infrastructure'),
    (2, 'Manufacturing & Matter'),
    (3, 'Truth & Epistemic Infrastructure'),
    (4, 'Governance & Collective Intelligence'),
    (5, 'Markets & Incentive Systems'),
    (6, 'Ethics & Moral Expansion'),
    (7, 'AI & Human Agency'),
    (8, 'Interfaces & Augmentation'),
    (9, 'Science & Discovery'),
]


def _add_links(text, make_link):
    """Replace first occurrence of each known reference with a link.
    make_link(url, display_text) -> replacement string."""
    sorted_refs = sorted(URLS.items(), key=lambda x: -len(x[0]))
    for ref_text, url in sorted_refs:
        pattern = re.escape(ref_text)
        match = re.search(pattern, text)
        if match:
            before = text[:match.start()]
            # Skip if already inside a link
            if ('<a ' in before and before.count('<a ') > before.count('</a>')) or \
               ('{{LINK:' in before and before.count('{{LINK:') > before.count('}}')):
                continue
            original = match.group(0)
            text = text[:match.start()] + make_link(url, original) + text[match.end():]
    return text


def add_html_links(text):
    return _add_links(text, lambda url, t: f'<a href="{url}" target="_blank" rel="noopener">{t}</a>')


def add_typst_links(text):
    return _add_links(text, lambda url, t: f'{{{{LINK:{url}|{t}}}}}')


def escape_typst(text):
    """Escape Typst special chars, converting link placeholders to #link()."""
    placeholders = {}
    counter = [0]

    def save(m):
        key = f'__PH{counter[0]}__'
        counter[0] += 1
        placeholders[key] = m.group(0)
        return key

    text = re.sub(r'\{\{LINK:[^}]+\}\}', save, text)
    text = text.replace('$', '\\$')
    text = text.replace('#', '\\#')
    text = text.replace('@', '\\@')

    for key, ph in placeholders.items():
        m = re.match(r'\{\{LINK:(.+?)\|(.+?)\}\}', ph)
        if m:
            url, display = m.groups()
            display = display.replace('$', '\\$').replace('@', '\\@')
            text = text.replace(key, f'#link("{url}")[{display}]')
    return text


def get_scores(e):
    dacc = e.get('stage3_dacc', {})
    dacc_str = f"{dacc.get('total')}/20" if isinstance(dacc, dict) and dacc.get('total') is not None else "N/A"
    tech = e.get('stage2_total')
    tech_str = f"{tech}/70" if tech else "N/A"
    return dacc_str, tech_str


def sort_key(e):
    dacc = e.get('stage3_dacc', {})
    return -(dacc.get('total', 0) or 0) if isinstance(dacc, dict) else 0


# ═══════════════════════════════════════════
# Rebuild report.typ
# ═══════════════════════════════════════════

def rebuild_report():
    with open('results/report.typ', 'r') as f:
        full = f.read()

    # Find the entities section start
    ent_start = full.find('// ═══════════════════════════════════════════\n= Consensus Entities')
    if ent_start == -1:
        print("ERROR: Could not find entities section in report.typ")
        return
    header = full[:ent_start]

    # Build entities section
    lines = []
    lines.append('// ═══════════════════════════════════════════')
    lines.append('= Consensus Entities <entities>')
    lines.append('')
    lines.append('The 39 consensus entities are organized into nine thematic groups. For each entity, we provide its description, d/acc and technology scores, a summary of the current state of the art, and an assessment of viable next steps and key challenges.')
    lines.append('')

    for i, (cid, cname) in enumerate(GROUPS):
        group_ents = sorted([e for e in entities if e.get('cluster_id') == cid], key=sort_key)
        lines.append(f'== {cname}')
        lines.append('')
        for e in group_ents:
            name = e['name']
            desc = escape_typst(add_typst_links(e.get('description', '')))
            dacc_str, tech_str = get_scores(e)
            lines.append(f'=== {escape_typst(name)}')
            lines.append('')
            lines.append(f'{desc} \\')
            lines.append(f'#text(size: 9pt, fill: luma(100))[d/acc: {dacc_str} #h(1em) Tech: {tech_str}]')
            lines.append('')
            r = research_by_name.get(name)
            if r:
                lines.append(f'*State of the Art.* {escape_typst(add_typst_links(r["sota"]))}')
                lines.append('')
                lines.append(f'*Next Steps & Challenges.* {escape_typst(add_typst_links(r["next_steps"]))}')
            lines.append('')
        if i < len(GROUPS) - 1:
            lines.append('#pagebreak()')
            lines.append('')

    # Conclusion
    lines.append('')
    lines.append('#pagebreak()')
    lines.append('')

    # Find and keep the existing conclusion
    conc_marker = '// ═══════════════════════════════════════════\n= Conclusion'
    conc_start = full.find(conc_marker)
    if conc_start != -1:
        conclusion = full[conc_start:]
    else:
        conclusion = '= Conclusion\n\n_Conclusion not found._\n'

    with open('results/report.typ', 'w') as f:
        f.write(header + '\n'.join(lines) + conclusion)

    link_count = '\n'.join(lines).count('#link(')
    print(f"report.typ: {link_count} links")

    # Compile PDF if typst is available
    if shutil.which('typst'):
        result = subprocess.run(['typst', 'compile', 'results/report.typ', 'results/report.pdf'],
                                capture_output=True, text=True)
        if result.returncode == 0:
            print("report.pdf: compiled")
        else:
            print(f"report.pdf: COMPILE ERROR\n{result.stderr}")


# ═══════════════════════════════════════════
# Rebuild highlights.html
# ═══════════════════════════════════════════

def rebuild_highlights():
    with open('results/highlights.html', 'r') as f:
        html = f.read()

    match = re.search(r'const DATA = (\[.*?\]);\s*\n', html, re.DOTALL)
    if not match:
        print("ERROR: Could not find DATA in highlights.html")
        return

    data = json.loads(match.group(1))
    link_count = 0
    for group in data:
        for entity in group['entities']:
            name = entity['name']
            r = research_by_name.get(name)
            if r:
                entity['sota'] = add_html_links(r['sota'])
                entity['next_steps'] = add_html_links(r['next_steps'])
                link_count += entity['sota'].count('<a href=')
                link_count += entity['next_steps'].count('<a href=')

    new_json = json.dumps(data, ensure_ascii=False)
    html = html[:match.start()] + f'const DATA = {new_json};\n' + html[match.end():]

    with open('results/highlights.html', 'w') as f:
        f.write(html)

    print(f"highlights.html: {link_count} links")


# ═══════════════════════════════════════════

if __name__ == '__main__':
    print(f"Loaded {len(URLS)} URL mappings from results/source_links.json\n")
    rebuild_report()
    rebuild_highlights()
    print("\nDone! Review changes, then commit.")
