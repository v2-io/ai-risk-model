"""Extends judges.py: for each document with a second blind judge (the source expert), how much of what
today's ranking misses against the original judge was marked by the other judge at all (line overlap,
same query). For SB 53, also with Gemini, and with either."""
from dn import *
import glob
R = '/Users/josephwecker-v2/src/ai-risk-model/search/eval/'
def load(path):
    d = json.load(open(path)); return d['key'], d['queries']
def lines(it): return set(range(it['lines'][0], it['lines'][1] + 1))
ST = {q: T[q]['stretches'] for q in QUERIES}
SC, _, _ = load_scores()
def miss_split(key, others, sc, label):
    s = sc
    mx = un = shared = 0; mx_m = un_m = shared_m = 0
    for q in QUERIES:
        rows = T[q]['rows']; rk = {i: n + 1 for n, i in enumerate(sorted(rows, key=lambda i: -s[q][i]))}
        ko = {(r['key'], r['ord']): i for i, r in rows.items()}
        for st in ST[q]:
            if st['key'] != key: continue
            g = st['gain']; mx += g
            if min(rk[ko[k]] for k in st['ps']) <= 188: continue
            un += g
            # judged-but-empty vs not judged: only count queries every other judge judged
            judged = all(q in o for o in others)
            if any(lines({'lines': st['lines']}) & lines(it) for o in others for it in o.get(q, [])):
                shared += g
            if st['must']:
                un_m += g
                if any(lines({'lines': st['lines']}) & lines(it) for o in others for it in o.get(q, [])): shared_m += g
    return mx, un, shared, un_m, shared_m
for f in sorted(glob.glob(R + 'expert-judgments/*.json')):
    if 'reorder' in f: continue
    key, ex = load(f)
    others = [ex]
    names = 'expert'
    for name, sc in (('today', SC['today']), ('exp+tags', SC['exptags'])):
        mx, un, sh, um, shm = miss_split(key, others, sc, name)
        print(f'{key:32} {name:9} vs {names:14}: unflagged {un / mx:.3f} of judged gain; of it, also marked by {names} {sh / un if un else 0:.0%}'
              f' (must-read unflagged {um}, of it shared {shm / um if um else 0:.0%})')
    if key == 'california-2025-sb53':
        _, gm = load(R + 'outline-judgments-gemini/california-2025-sb53.json')
        for oth, nm in (([gm], 'gemini'), ([gm, ex], 'gemini|expert')):
            mx, un, sh, um, shm = miss_split(key, oth, SC['today'], 'today')
            print(f'{key:32} today     vs {nm:14}: unflagged {un / mx:.3f}; of it, also marked by {nm} {sh / un:.0%}')
tot = {}
for nm in ('today', 'exptags'):
    U = Sh = 0
    for f in sorted(glob.glob(R + 'expert-judgments/*.json')):
        if 'reorder' in f: continue
        key, ex = load(f)
        mx, un, sh, um, shm = miss_split(key, [ex], SC[nm], nm)
        U += un; Sh += sh
    print(f'pooled over 4 docs, {nm}: unflagged gain {U}, of it marked by the expert too {Sh / U:.0%}')
