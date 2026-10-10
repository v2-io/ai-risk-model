import re, collections
from dn import *
SPC = dict(l.rstrip('\n').split('\t')[:2] for l in open(os.path.join(SP, 'runs', 'classification.tsv')) if not l.startswith(('#', 'sid')))
sids = {}
for l in open(os.path.join(ME, 'cache', 'sample.txt')):
    m = re.match(r'#(\d+) sid=(.*?) \| Q:.*grade (\d)', l)
    if m: sids[int(m.group(1))] = (m.group(2), int(m.group(3)))
mine = {int(a): (b, c) for a, b, c, _ in (l.rstrip('\n').split('\t') for l in open(os.path.join(ME, 'mine.tsv')) if not l.startswith('#'))}
agree = agree_alt = 0; M = collections.Counter(); gm = collections.Counter(); gs = collections.Counter()
rows = []
for n, (sid, g) in sids.items():
    s = SPC.get(sid, '?'); p, alt = mine[n]
    gain = 2 ** g - 1
    agree += p == s; agree_alt += s in (p, alt)
    M[(p, s)] += 1; gm[p] += gain; gs[s] += gain
    rows.append((n, sid, g, p, alt, s))
N = len(sids)
print(f'n={N}; primary agreement {agree}/{N} = {agree / N:.0%}; spiker label among my primary or alternate {agree_alt}/{N}')
cats = sorted(set(gm) | set(gs))
po = agree / N
pm = collections.Counter(mine[n][0] for n in sids); ps = collections.Counter(SPC.get(sids[n][0]) for n in sids)
pe = sum(pm[c] * ps[c] for c in cats) / N / N
print(f"Cohen's kappa {(po - pe) / (1 - pe):.2f}")
tg = sum(gm.values())
print('gain-weighted shares in this sample, mine vs spiker:')
for c in cats: print(f'  {c:7} {gm[c] / tg:.0%}  {gs[c] / tg:.0%}')
print('disagreements (n sid grade mine/alt spiker):')
for r in rows:
    if r[3] != r[5]: print('  ', r)
