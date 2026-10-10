"""Is the gain real relevance or spread? Passage-level precision@188 (label>0), gain-weighted precision,
distinct heading paths in the top 188, and mean rank of must-read stretches' best passage."""
from dn import *
SC, S, E = load_scores()
P = CM_P
def stats(sc):
    prec = must_prec = paths = 0; ranks = []
    for q in QUERIES:
        rows = T[q]['rows']; s = sc[q]
        top = sorted(rows, key=lambda i: -s[i])[:188]
        prec += sum(rows[i]['label'] > 0 for i in top) / 188
        must_prec += sum(rows[i]['label'] == 2 for i in top) / 188
        paths += len({(P[i]['key'], tuple(P[i]['path'])) for i in top})
        rk = {i: n + 1 for n, i in enumerate(sorted(rows, key=lambda i: -s[i]))}
        ko = {(r['key'], r['ord']): i for i, r in rows.items()}
        for st in T[q]['stretches']:
            ranks.append(min(rk[ko[k]] for k in st['ps']))
    n = len(QUERIES)
    return prec / n, must_prec / n, paths / n, np.median(ranks), np.mean(np.log(ranks))
print(f'{"":16} {"P@188":>6} {"mustP":>6} {"paths":>6} {"medRk":>6} {"meanLogRk":>9}')
for name in ('today', 'exp_a1', 'exp_a2', 'tags_b1', 'exptags_noeot', 'exptags'):
    print(f'{name:16} ' + ' '.join(f'{x:6.3f}' if k < 2 else f'{x:6.1f}' for k, x in enumerate(stats(SC[name]))))
# random-perturbation control: add two RRF legs that are random permutations, at beta 1
rng = np.random.default_rng(3)
vals = []
for t in range(5):
    R = {}
    for q in QUERIES:
        rows = T[q]['rows']; M = RS.multipliers(q); ids = list(rows)
        r1 = rng.permutation(len(ids)); r2 = rng.permutation(len(ids))
        R[q] = {i: SC['today'][q][i] + M[i] * (1 / (60 + r1[j] + 1) + 1 / (60 + r2[j] + 1)) for j, i in enumerate(ids)}
    vals.append(RS.flagged(R))
print('two random legs at beta 1: flagged', np.round(vals, 3))
