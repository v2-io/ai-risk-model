"""Builds eu-cop-2025-safety-security.reorder.json from the saved runs, ideal.json and notes.json.
Adapted from california-2025-sb53.inputs/build_reorder.py. The runs (hybrid JSON, outline text and
JSON) were kept in the job's scratch directory; the passage list came from src.passages."""
import json, re
R = '/Users/josephwecker-v2/src/ai-risk-model'
G = '/Users/josephwecker-v2/.claude/jobs/7354940e/tmp/gold'
W = R + '/.claude/worktrees/expert-eu-cop-gold/search/eval/expert-judgments'
K = 'eu-cop-2025-safety-security'
t = open(R + f'/ref/canonical/{K}.md', encoding='utf-8').read()
L = lambda o: t.count('\n', 0, int(o)) + 1
P = {}
for r in open(G + '/passages.txt', encoding='utf-8'):
    o, s, e, h = r.rstrip('\n').split('|', 3)
    s, e = int(s), int(e)
    P[int(o)] = dict(lines=[L(s), L(e - 1)], quote=' '.join(re.sub(r'\]\([^)]*\)', ']', t[s:s + 120]).split())[:70])
J = json.load(open(W + f'/{K}.json'))
qs = list(J['queries'])
ideal = json.load(open(W + f'/{K}.inputs/ideal.json'))
notes = json.load(open(W + f'/{K}.inputs/notes.json'))
ov = lambda a, b: not (a[1] < b[0] or a[0] > b[1])
out = []
for i, q in enumerate(qs):
    I = [(int(p), g) for p, g in ideal[q]['items']]
    A = set(ideal[q].get('ok', []))
    hy = json.load(open(f'{G}/runs/{i:02d}.hybrid.json'))['results']
    rank = {int(x['passage'].split('#')[1]): x['rank'] for x in hy}
    items = [dict(passage=p, lines=P[p]['lines'], quote=P[p]['quote'], grade=g, shown_rank=rank.get(p)) for p, g in I]
    ids = {p for p, _ in I} | A
    noise = [r for p, r in sorted(rank.items(), key=lambda x: x[1]) if p not in ids]
    e = dict(query=q, tool='hybrid', items=items, acceptable=sorted(A), noise=noise)
    if notes.get(q, {}).get('hybrid'):
        e['note'] = notes[q]['hybrid']
    out.append(e)
    txt = open(f'{G}/runs/{i:02d}.outline.txt', encoding='utf-8').read()
    opened = [(int(a), int(b)) for a, b in re.findall(r'▸ L(\d+)–(\d+)', txt)]
    cov = lambda lr: any(ov(lr, r) for r in opened)
    oitems = [dict(passage=p, lines=P[p]['lines'], quote=P[p]['quote'], grade=g, opened=cov(P[p]['lines'])) for p, g in I]
    good = [P[p]['lines'] for p in ids]
    onoise = [f'L{a}–{b}' for a, b in opened if not any(ov(l, (a, b)) for l in good)]
    head = txt.split('\n')[1]
    e = dict(query=q, tool='outline', items=oitems, noise=onoise,
             flagged_unanswered=head.startswith('Nothing in scope'),
             ranges_opened=len(opened), source_lines_in_opened_ranges=sum(b - a + 1 for a, b in opened))
    if notes.get(q, {}).get('outline'):
        e['note'] = notes[q]['outline']
    out.append(e)
meta = dict(key=K, canonical_sha256=J['canonical_sha256'], repo_sha='e0e702550a81994afd9ab7878fea57c71d5cf5a5',
    judge=J['judge'], date='2026-10-10',
    commands=[f"bin/source-search hybrid -n 20 QUERY {K}", f"bin/source-search outline QUERY {K} --lines 60 (--text read; JSON kept)"],
    how="Items are the tool's own passages (src.passages, ord), in the order they should have come, with a grade. Grades come from stage 1: the highest grade of any judged stretch overlapping the passage, adjusted where a stage-1 stretch was coarser than the passage grain (e.g. the empty 'ADDITIONAL LEGAL TEXT: Recital 110' heading, #125, is dropped). shown_rank is the hybrid rank, null if not in the top 20. 'acceptable' lists relevant passages that weren't graded; they aren't counted as noise. For the outline, 'opened' says whether any opened range (▸) overlaps the passage, since the outline has no ranks. 'noise' lists hybrid ranks, or outline ranges, holding no graded or acceptable passage. The chemical-and-biological query carries anchors and grades only, by request.",
    passages={str(k): v['lines'] for k, v in P.items()})
json.dump(dict(meta=meta, entries=out), open(W + f'/{K}.reorder.json', 'w'), indent=1, ensure_ascii=False)
for e in out:
    if e['tool'] == 'hybrid':
        print(e['query'][:44], '| missed', [x['passage'] for x in e['items'] if x['shown_rank'] is None], '| noise ranks', e['noise'])
    else:
        print('   outline missed', [x['passage'] for x in e['items'] if not x['opened']], '| noise ranges', len(e['noise']), 'of', e['ranges_opened'], '| unans', e['flagged_unanswered'], e['source_lines_in_opened_ranges'])
