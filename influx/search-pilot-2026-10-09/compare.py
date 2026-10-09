"""Paired comparison of two eval rows over the same queries (search pilot, 2026-10-09).

    python3 compare.py RESULTS.json 'modelA|mode|target|input' 'modelB|mode|target|input'

Prints the mean nDCG@10 difference, per-query wins/losses/ties, and a bootstrap
95% interval over queries. With 16 queries, an interval that spans zero means
the pilot cannot tell the two apart.
"""
import json, sys
import numpy as np

def row(rows, spec):
    m, mode, t, inp = spec.split('|')
    hits = [r for r in rows if r['model'] == m and r['mode'] == mode and str(r['target']) == t and r['input'] == inp]
    if not hits:
        sys.exit(f'no row {spec}')
    return hits[-1]

def compare(rows, a, b, n=10000, seed=0):
    ra, rb = row(rows, a), row(rows, b)
    qs = sorted(set(ra['per_query']) & set(rb['per_query']))
    d = np.array([ra['per_query'][q]['ndcg'] - rb['per_query'][q]['ndcg'] for q in qs])
    rng = np.random.default_rng(seed)
    boots = d[rng.integers(0, len(d), (n, len(d)))].mean(axis=1)
    lo, hi = np.percentile(boots, [2.5, 97.5])
    return dict(mean=d.mean(), lo=lo, hi=hi, wins=int((d > 0.005).sum()), losses=int((d < -0.005).sum()),
                ties=int((abs(d) <= 0.005).sum()), n=len(d))

if __name__ == '__main__':
    rows = json.load(open(sys.argv[1]))
    c = compare(rows, sys.argv[2], sys.argv[3])
    print(f'{sys.argv[2]}  minus  {sys.argv[3]}: {c["mean"]:+.3f}  95% [{c["lo"]:+.3f}, {c["hi"]:+.3f}]  '
          f'wins {c["wins"]} losses {c["losses"]} ties {c["ties"]} of {c["n"]}')
