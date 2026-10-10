"""Builds aisi-2025-frontier.reorder.json from the expert's stage-1 judgments, the tool's own
passages, and the saved runs of bin/source-search (hybrid and outline, 21 queries).

    python3 -I build_reorder.py RUNS_DIR

RUNS_DIR holds NN.hybrid.json and NN.outline.txt, NN in the order of the stage-1 file's
queries. The tool's passages (src.passages) were read with
    psql -d airisk_sources -At -F'|' -c "select ord, start_off, end_off, page, page_last, length(text)
       from src.passages where doc_key='aisi-2025-frontier' and layer='canonical' order by ord"
and are kept beside this file as passages.txt. Offsets are characters of the canonical file.
"""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
RUNS = sys.argv[1]
CANON = os.environ.get('CANON', '/Users/josephwecker-v2/src/ai-risk-model/ref/canonical/aisi-2025-frontier.md')
J = json.load(open(os.path.join(HERE, '..', 'aisi-2025-frontier.json')))
OV = json.load(open(os.path.join(HERE, 'overrides.json')))
NOTES = json.load(open(os.path.join(HERE, 'notes.json')))
t = open(CANON, encoding='utf-8').read()
L = lambda o: t.count('\n', 0, int(o)) + 1
P = {}
for r in open(os.path.join(HERE, 'passages.txt')):
    o, s, e, pg, pl, n = r.strip().split('|')
    s, e = int(s), int(e)
    P[int(o)] = dict(lines=[L(s), L(e - 1)], quote=' '.join(t[s:s + 90].split())[:70])
overlap = lambda a, b: not (a[1] < b[0] or a[0] > b[1])
qs = list(J['queries'])
out, ideal = [], {}
for i, q in enumerate(qs):
    g, first = {}, {}
    for k, it in enumerate(J['queries'][q]):
        for o, p in P.items():
            if overlap(p['lines'], it['lines']):
                g[o] = max(g.get(o, 0), it['grade'])
                first.setdefault(o, k)
    ov = OV.get(q, {})
    for o in ov.get('drop', []):
        g.pop(o, None)
    pref = [o for o in ov.get('order', []) if o in g]
    rest = sorted((o for o in g if o not in pref), key=lambda o: (-g[o], first[o]))
    order = pref + rest
    ok = set(ov.get('ok', []))
    ideal[q] = dict(items=[[o, g[o]] for o in order], ok=sorted(ok))
    hy = json.load(open(f'{RUNS}/{i:02d}.hybrid.json'))['results']
    rank = {int(x['passage'].split('#')[1]): x['rank'] for x in hy}
    items = [dict(passage=o, lines=P[o]['lines'], quote=P[o]['quote'], grade=g[o], shown_rank=rank.get(o)) for o in order]
    ids = set(order) | ok
    noise = [r for o, r in sorted(rank.items(), key=lambda x: x[1]) if o not in ids]
    e = dict(query=q, tool='hybrid', items=items, noise=noise, top20=[o for o, _ in sorted(rank.items(), key=lambda x: x[1])])
    if NOTES.get(q, {}).get('hybrid'):
        e['note'] = NOTES[q]['hybrid']
    out.append(e)
    txt = open(f'{RUNS}/{i:02d}.outline.txt').read()
    opened = [(int(a), int(b)) for a, b in re.findall(r'▸ L(\d+)–(\d+)', txt)]
    cov = lambda lr: any(overlap(lr, x) for x in opened)
    oitems = [dict(passage=o, lines=P[o]['lines'], quote=P[o]['quote'], grade=g[o], opened=cov(P[o]['lines'])) for o in order]
    good = [P[o]['lines'] for o in ids]
    onoise = [f'L{a}–{b}' for a, b in opened if not any(overlap(l, (a, b)) for l in good)]
    lines2 = txt.split('\n')
    banner = None
    if len(lines2) > 1 and lines2[1].startswith(('Nothing in scope', 'No passage in scope')):
        banner = lines2[1][:120]
    e = dict(query=q, tool='outline', items=oitems, noise=onoise, opened_ranges=[list(x) for x in opened],
             source_lines_in_opened_ranges=sum(b - a + 1 for a, b in opened), banner=banner)
    if NOTES.get(q, {}).get('outline'):
        e['note'] = NOTES[q]['outline']
    out.append(e)
meta = dict(
    key='aisi-2025-frontier',
    canonical_sha256=J['canonical_sha256'],
    repo_sha='e0e702550a81994afd9ab7878fea57c71d5cf5a5',
    judge=J['judge'],
    date='2026-10-10',
    commands=['bin/source-search hybrid -n 20 QUERY aisi-2025-frontier',
              'bin/source-search outline QUERY aisi-2025-frontier --lines 60 (--text read; JSON kept)',
              'bin/source-search lexical TERM aisi-2025-frontier --text (the term queries only, as a check)'],
    how=("Items are the tool's own passages (src.passages, ord), in the order they should have come, with the grade from stage 1 "
         "(the highest grade of any judged stretch that overlaps the passage). The order is: the 'order' override where I gave one, "
         "then grade, then the order I listed the stretches in stage 1 (roughly importance, not strictly). shown_rank is the hybrid "
         "rank, null if not in the top 20. For the outline, 'opened' says whether any opened (▸) range overlaps the passage. "
         "'noise' lists hybrid ranks, or outline ranges, holding no graded passage; passages that are relevant but weren't graded "
         "(listed per query in overrides.json as ok) aren't counted as noise. 'banner' is the outline's own line about whether "
         "anything answers the query. A passage inside a graded section counts as graded even when it is not worth reading on its "
         "own (a figure's 'Source:' line, say); I dropped the two clearest cases, per overrides.json."),
    passages={str(k): v['lines'] for k, v in P.items()})
json.dump(dict(meta=meta, entries=out), open(os.path.join(HERE, '..', 'aisi-2025-frontier.reorder.json'), 'w'), indent=1, ensure_ascii=False)
json.dump(ideal, open(os.path.join(HERE, 'ideal.json'), 'w'), indent=1, ensure_ascii=False)
for e in out:
    if e['tool'] == 'hybrid':
        n2 = [x for x in e['items'] if x['grade'] == 2]
        n1 = [x for x in e['items'] if x['grade'] == 1]
        f = lambda xs: sum(1 for x in xs if x['shown_rank'])
        print(f"{e['query'][:44]:44} | hybrid g2 {f(n2)}/{len(n2)} g1 {f(n1)}/{len(n1)} noise {len(e['noise'])}", end=' ')
    else:
        n2 = [x for x in e['items'] if x['grade'] == 2]
        n1 = [x for x in e['items'] if x['grade'] == 1]
        f = lambda xs: sum(1 for x in xs if x['opened'])
        print(f"| outline g2 {f(n2)}/{len(n2)} g1 {f(n1)}/{len(n1)} noise ranges {len(e['noise'])} lines {e['source_lines_in_opened_ranges']} banner={'Y' if e['banner'] else '-'}")
