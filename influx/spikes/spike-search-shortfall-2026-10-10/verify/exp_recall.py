"""expansion.py's R+N rows, rerun without the phrases that look recalled from one Au5 source's text:
phrases of 3+ words that occur verbatim in exactly one Au5 document. Also: exp+tags (b1, exp on tags) with the same drop."""
from dn import *
import tags_eval as TE
from srcsearch import rank
conn = ro_conn()
EXP = json.load(open(os.path.join(SP, 'runs', 'blind-expansions.json')))['queries']
phc = json.load(open(os.path.join(SP, 'cache', 'phrase-qvec-bge-m3.json')))
z = np.load(os.path.join(SP, 'cache', 'bge-m3-full.npz')); ids = z['ids']; V = z['V']
W = rank.weights()['lexical']
drop = set()
for q, v in EXP.items():
    for p in v['rephrasings'] + v['neighbours']:
        if len(p.split()) < 3: continue
        docs = conn.execute("select count(distinct doc_key) from src.passages where doc_key = any(%s) and layer='canonical' "
                            "and tsv_exact @@ phraseto_tsquery('simple', %s)", (CM.AU5, p)).fetchone()[0]
        if docs == 1: drop.add(p)
print(len(drop), 'dropped:', sorted(drop))
semc, lexc = {}, {}
for p in {p for d in EXP.values() for p in d['rephrasings'] + d['neighbours']}:
    v = np.array(phc[p], dtype=np.float32); v /= np.linalg.norm(v)
    order = np.argsort(-(V @ v))[:400]
    semc[p] = {int(ids[j]): n + 1 for n, j in enumerate(order)}
    lx, *_ = rank.lexical(conn, rank.parse(p), W, CM.AU5)
    lexc[p] = {i: n + 1 for n, i in enumerate(sorted((i for i in lx if lx[i] > 0), key=lambda i: -lx[i]))}
def run(alpha, dropset):
    S = {}
    for q in QUERIES:
        h = RS.hybrid(q)
        E = [] if q not in EXP else [p for L in ('rephrasings', 'neighbours') for p in EXP[q][L] if p not in dropset]
        if not E: S[q] = h; continue
        M = RS._M[q]
        S[q] = {i: h[i] + M[i] * (alpha / len(E)) * sum(1 / (60 + semc[e].get(i, RS.NBIG)) + 1 / (60 + lexc[e].get(i, RS.NBIG)) for e in E) for i in h}
    return S
base = RS.today()
for a in (1.0, 2.0):
    for nm, ds in (('all', set()), ('minus recalled', drop)):
        S = run(a, ds); d = RS.boot(base, S)
        print(f'R+N alpha {a} {nm:15} flagged {RS.flagged(S):.3f} ({d[0]:+.3f}, {d[1]:+.3f} to {d[2]:+.3f})')
