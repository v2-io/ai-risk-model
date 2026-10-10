"""Out-of-sample: score the spike's saved rankings against the source experts' blind stage-1 judgments
(search/eval/expert-judgments), which did not exist when the spike chose its configurations."""
from dn import *
conn = ro_conn()
ED = '/Users/josephwecker-v2/src/ai-risk-model/search/eval/expert-judgments'
SC, S, E = load_scores()
ST, keys, nf = stretches_from(ED, conn)
keys = [k for k in keys if k != "bengio-2026-international"]
ST = {q: [s for s in v if s["key"] in keys] for q, v in ST.items()}
print('expert docs', keys, 'unresolved', nf)
hows = {}
for q in ST:
    for st in ST[q]: hows[st['how']] = hows.get(st['how'], 0) + 1
print('resolved by', hows)
q12 = [q for q in QUERIES if q in ST]
# Same for the original judges restricted to the same 4 docs, for comparability
OJ, okeys, _ = stretches_from(CM.JUDG, conn)
for label, J in (('original judges, same 4 docs', OJ), ('experts (blind stage 1)', ST)):
    print(f'\n== {label}')
    base, pqa = flagged_against(SC['today'], J, queries=q12, keys=keys)
    mb, _ = flagged_against(SC['today'], J, queries=q12, keys=keys, must_only=True)
    print(f'  today      flagged {base:.3f}  must {mb:.3f}')
    for name in ('exp_a1', 'exp_a2', 'tags_b1', 'exptags_noeot', 'exptags'):
        v, pqb = flagged_against(SC[name], J, queries=q12, keys=keys)
        m, _ = flagged_against(SC[name], J, queries=q12, keys=keys, must_only=True)
        lo, hi = boot_pq(pqa, pqb)
        print(f'  {name:14} flagged {v:.3f} ({v - base:+.3f}, {lo:+.3f} to {hi:+.3f})  must {m:.3f}')
    # tags controls
    for name in ('tags-lex|1.0', 'tags-sem|1.0'):
        v, pqb = flagged_against(S[name], J, queries=q12, keys=keys)
        print(f'  {name:14} flagged {v:.3f} ({v - base:+.3f})')
    # per doc
    for k in keys:
        b0, _ = flagged_against(SC['today'], J, queries=q12, keys=[k])
        b1, _ = flagged_against(SC['tags_b1'], J, queries=q12, keys=[k])
        b2, _ = flagged_against(SC['exptags'], J, queries=q12, keys=[k])
        print(f'    {k:34} today {b0:.2f} tags {b1:.2f} exp+tags {b2:.2f}')
