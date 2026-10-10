"""Stage 2: what hybrid and outline returned for anthropic-2026-risk-report-aug, reordered.

Adapted from california-2025-sb53.inputs/build_reorder.py. Inputs: the stage-1 file,
ideal.json (the passages, by src.passages ord, in the order they should have come, with
grades) and notes.json (per query and tool). Raw runs and the passage table were kept in
the job's scratch directory (G); the passages came from
  psql-18 -d airisk_sources -c "select ord,start_off,end_off from src.passages
    where doc_key='anthropic-2026-risk-report-aug' and layer='canonical' order by ord"
Run from the worktree root.
"""
import json, re, os
R = os.getcwd()
G = '/Users/josephwecker-v2/.claude/jobs/81669188/tmp/rr-gold'
KEY = 'anthropic-2026-risk-report-aug'
W = R + '/search/eval/expert-judgments'
I_ = W + f'/{KEY}.inputs'
t = open(R + f'/ref/canonical/{KEY}.md', encoding='utf-8').read()
L = lambda o: t.count('\n', 0, int(o)) + 1
P = {}
for r in open(G + '/passages.txt'):
    o, s, e = r.strip().split('|'); s, e = int(s), int(e)
    txt = re.sub(r'<span[^>]*></span>|\*\*|<br>|\]\([^)]*\)|\[|\|', ' ', t[s:s + 160])
    P[int(o)] = dict(lines=[L(s), L(e - 1)], quote=' '.join(txt.split())[:70])
J = json.load(open(W + f'/{KEY}.json'))
qs = list(J['queries'])
ideal = json.load(open(I_ + '/ideal.json'))
notes = json.load(open(I_ + '/notes.json'))
repo_sha = open(G + '/repo_sha.txt').read().strip()


def overl(a, b):
    return not (a[1] < b[0] or a[0] > b[1])


out = []
for i, q in enumerate(qs):
    stretches = J['queries'][q]
    def g1(p):  # stage-1 grade of a passage: highest grade of any judged stretch it overlaps
        return max([s['grade'] for s in stretches if overl(P[p]['lines'], s['lines'])] or [0])
    I = [(int(p), g) for p, g in ideal[q]['items']]
    ids = {p for p, _ in I}
    ok = sorted(p for p in P if p not in ids and g1(p) > 0)  # inside a judged stretch, not singled out
    allowed = ids | set(ok)
    hy = json.load(open(f'{G}/{i:02d}.hybrid.json'))['results']
    rank = {int(x['passage'].split('#')[1]): x['rank'] for x in hy}

    def item(p, g):
        d = dict(passage=p, lines=P[p]['lines'], quote=P[p]['quote'], grade=g)
        if g1(p) == 0:
            d['added_in_stage2'] = True
        return d
    items = [dict(item(p, g), shown_rank=rank.get(p)) for p, g in I]
    noise = [r for p, r in sorted(rank.items(), key=lambda x: x[1]) if p not in allowed]
    e = dict(query=q, tool='hybrid', items=items, acceptable=ok, noise=noise)
    if notes.get(q, {}).get('hybrid'): e['note'] = notes[q]['hybrid']
    out.append(e)
    txt = open(f'{G}/{i:02d}.outline-text.txt').read()
    opened = [(int(a), int(b)) for a, b in re.findall(r'▸ L(\d+)–(\d+)', txt)]
    cov = lambda lr: any(overl(lr, x) for x in opened)
    oitems = [dict(item(p, g), opened=cov(P[p]['lines'])) for p, g in I]
    good = [P[p]['lines'] for p in allowed]
    onoise = [f'L{a}–{b}' for a, b in opened if not any(overl((a, b), l) for l in good)]
    oj = json.load(open(f'{G}/{i:02d}.outline.json'))
    e = dict(query=q, tool='outline', items=oitems, noise=onoise,
             no_query_words_warning=txt.split('\n')[1].startswith('No passage in scope holds'),
             likely_unanswered=oj['answerability']['likely_unanswered'],
             passages_with_query_words=oj['passages_with_query_words'],
             source_lines_in_opened_ranges=sum(b - a + 1 for a, b in opened))
    if notes.get(q, {}).get('outline'): e['note'] = notes[q]['outline']
    out.append(e)

meta = dict(
    key=KEY, canonical_sha256=J['canonical_sha256'], repo_sha=repo_sha,
    repo_sha_note='HEAD of expert/anthropic-2026-risk-report-aug-gold when the searches ran: main e0e7025 plus the stage-1 commit (no code changes)',
    judge=J['judge'], date='2026-10-10',
    commands=[f"bin/source-search hybrid -n 20 QUERY {KEY}",
              f"bin/source-search outline QUERY {KEY} --lines 60 (--text read; JSON kept)"],
    how=("Items are the tool's own passages (src.passages, ord), in the order they should have come, with "
         "the grade I gave at stage 2 (normally the stage-1 grade of the stretch holding the passage; "
         "'added_in_stage2' marks a passage no stage-1 stretch covered). shown_rank is the hybrid rank, null "
         "if not in the top 20. For the outline, 'opened' says whether any opened range overlaps the passage. "
         "'acceptable' lists passages inside a judged stretch that I didn't single out; they aren't noise. "
         "'noise' lists hybrid ranks, or outline ranges, holding no graded or acceptable passage."),
    omitted={'chemical and biological weapons uplift': "left out at the coordinator's request"},
    passages={str(k): v['lines'] for k, v in P.items()})
json.dump(dict(meta=meta, entries=out), open(W + f'/{KEY}.reorder.json', 'w'), indent=1, ensure_ascii=False)
for e in out:
    if e['tool'] == 'hybrid':
        found = [x['passage'] for x in e['items'] if x['shown_rank']]
        print(f"{e['query'][:34]:34} hy: {len(found)}/{len(e['items'])} ideal in top20; noise {len(e['noise'])}/20; g2 missed {[x['passage'] for x in e['items'] if x['grade']==2 and not x['shown_rank']]}")
    else:
        print(f"{'':34} ol: {sum(x['opened'] for x in e['items'])}/{len(e['items'])} opened; noise ranges {len(e['noise'])}; g2 missed {[x['passage'] for x in e['items'] if x['grade']==2 and not x['opened']]}; warn={e['no_query_words_warning']}")
