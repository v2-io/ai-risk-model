from dn import *
SC, S, E = load_scores()
OJ = {q: T[q]['stretches'] for q in QUERIES}
qs = [q for q in QUERIES if not q.startswith('chemical')]
b, pa = flagged_against(SC['today'], OJ, queries=qs)
for n in ('tags_b1', 'exp_a2', 'exptags'):
    v, pb = flagged_against(SC[n], OJ, queries=qs); lo, hi = boot_pq(pa, pb)
    print(f'without the bio query: today {b:.3f}  {n} {v:.3f} ({v - b:+.3f}, {lo:+.3f} to {hi:+.3f})')
# leave-one-query-out sensitivity of the tags gain
d = []
for q in QUERIES:
    qq = [x for x in QUERIES if x != q]
    a, _ = flagged_against(SC['today'], OJ, queries=qq); c, _ = flagged_against(SC['tags_b1'], OJ, queries=qq)
    d.append((round(c - a, 3), q[:30]))
print('tags gain, leaving one query out (min, max):', min(d), max(d))
