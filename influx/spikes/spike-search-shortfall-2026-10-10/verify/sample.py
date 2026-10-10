from dn import *
import random
CUT = 188
items = []
for q in QUERIES:
    if q.startswith('chemical'): continue
    rows = T[q]['rows']; ko = {(r['key'], r['ord']): i for i, r in rows.items()}
    for st in T[q]['stretches']:
        ids = [ko[k] for k in st['ps']]
        h = [rows[i]['hrank'] for i in ids if rows[i]['hrank']]
        if h and min(h) <= CUT: continue
        items.append((q, st, ids))
print(len(items), 'non-bio unflagged')
random.seed(20261010)
smp = random.sample(items, 45)
os.makedirs(os.path.join(ME, 'cache'), exist_ok=True)
with open(os.path.join(ME, 'cache', 'sample.txt'), 'w') as f:
    for n, (q, st, ids) in enumerate(smp):
        p0 = CM_P[sorted(ids, key=lambda i: CM_P[i]['ord'])[0]]
        txt = ' '.join(CM_P[i]['text'] for i in sorted(ids, key=lambda i: CM_P[i]['ord']))
        f.write(f"#{n} sid={st['sid']} | Q: {q} | doc {st['key']} | grade {st['grade']} | {len(ids)} passages | path: {' › '.join(p0['path'])[-150:]}\n")
        f.write(f"   judge note: {st['note'][:300]}\n   text: {txt[:700]}\n\n")
