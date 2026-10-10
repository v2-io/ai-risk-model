"""Held-out queries: the source experts' own questions (not among the 12), which neither the tagger
briefs, the beta choice nor the spike's classification ever saw. Today's hybrid vs tags-both beta 1,
scored by the spike's flagged measure (pooled Au5, cut 188) against the experts' blind stage-1 judgments.
Query vectors cached here, not in search/eval/.cache."""
import json, os
from dn import *
import tags_eval as TE
from srcsearch import rank, embed
conn = ro_conn()
ED = '/Users/josephwecker-v2/src/ai-risk-model/search/eval/expert-judgments'
ST, keys, _ = stretches_from(ED, conn)
keys = [k for k in keys if k != 'bengio-2026-international']
ST = {q: [s for s in v if s['key'] in keys] for q, v in ST.items()}
NEW = [q for q in ST if q not in QUERIES and ST[q]]
print(len(NEW), 'held-out queries')
os.makedirs(os.path.join(ME, 'cache'), exist_ok=True)
QC = os.path.join(ME, 'cache', 'qvec.json')
try: qc = json.load(open(QC))
except Exception: qc = {}
def qv(s):
    if s not in qc:
        qc[s] = embed.embed_query('bge-m3', s); json.dump(qc, open(QC, 'w'))
    v = np.array(qc[s], dtype=np.float32); return v / np.linalg.norm(v)
P = CM_P
ids = sorted(P)
# build rows for each new query exactly as build_table does (only the fields rescore.multipliers needs)
z = np.load(os.path.join(SP, 'cache', 'bge-m3-full.npz')); Vids = [int(i) for i in z['ids']]; V = z['V']
for q in NEW:
    v = qv(q)
    res, pq = rank.search(conn, q, n=10 ** 9, keys=CM.AU5, qvec=list(map(float, v)))
    out, by_sha = {}, {}
    for r, s, ex in res:
        out[r[0]] = (s, ex); by_sha.setdefault(r[11], (s, ex))
    for i, p in P.items():
        if i not in out and p['norm_sha'] in by_sha:
            out[i] = by_sha[p['norm_sha']]
    rows = {}
    for i in ids:
        s, ex = out.get(i, (None, {}))
        rows[i] = dict(key=P[i]['key'], ord=P[i]['ord'], section=P[i]['section'], cand=i in out, score=s,
                       base=ex.get('base'), f_def=ex.get('f_def', 1.0), f_section=ex.get('f_section', 1.0),
                       proximity=ex.get('proximity'))
    RS.T[q] = dict(rows=rows, stretches=[], pq=pq, N=len(P))
tags = TE.load_tags()
bm = TE.BM25({i: tags.get(i, []) for i in P})
TVz = np.load(os.path.join(SP, 'cache', 'bge-m3-tags.npz'), allow_pickle=True)
TV = dict(zip(TVz['ids'].tolist(), TVz['V'])); TVm = np.stack([TV[i] for i in ids])
base, tagged, tlex_only, tsem_only = {}, {}, {}, {}
for q in NEW:
    rows = RS.T[q]['rows']
    M = RS.multipliers(q)
    h = {i: (rows[i]['score'] or 0.0) for i in ids}
    tl = TE.ranks(bm.score(q)); ts = TE.ranks(dict(zip(ids, (TVm @ qv(q)).tolist())), 400)
    base[q] = h
    tagged[q] = {i: h[i] + M[i] * (1 / (60 + tl.get(i, RS.NBIG)) + 1 / (60 + ts.get(i, RS.NBIG))) for i in ids}
    tlex_only[q] = {i: h[i] + M[i] * (1 / (60 + tl.get(i, RS.NBIG))) for i in ids}
    tsem_only[q] = {i: h[i] + M[i] * (1 / (60 + ts.get(i, RS.NBIG))) for i in ids}
b, pqa = flagged_against(base, ST, queries=NEW)
bm_, _ = flagged_against(base, ST, queries=NEW, must_only=True)
print(f'today        flagged {b:.3f} must {bm_:.3f}')
for name, S in (('tags-both b1', tagged), ('tags-lex b1', tlex_only), ('tags-sem b1', tsem_only)):
    v, pqb = flagged_against(S, ST, queries=NEW)
    m, _ = flagged_against(S, ST, queries=NEW, must_only=True)
    lo, hi = boot_pq(pqa, pqb)
    print(f'{name:12} flagged {v:.3f} ({v - b:+.3f}, {lo:+.3f} to {hi:+.3f}) must {m:.3f}')
_, pqb = flagged_against(tagged, ST, queries=NEW)
for q in NEW:
    a, d = pqa[q]; c, _ = pqb[q]
    print(f'  {q[:70]:70} gain {d:3}  today {a / d:.2f} -> tags {c / d:.2f}')
# also at a per-document scope (cut = 10% of that doc's passages), since these questions name one source
print('\nper-document scope (rank within the named document only, cut 10% of its passages):')
tot = {'base': [0, 0], 'tags': [0, 0]}
for q in NEW:
    for k in keys:
        sts = [s for s in ST[q] if s['key'] == k]
        if not sts: continue
        dids = [i for i in ids if P[i]['key'] == k]; cut = round(0.1 * len(dids))
        ko = {(P[i]['key'], P[i]['ord']): i for i in dids}
        for nm, S in (('base', base), ('tags', tagged)):
            rk = {i: n + 1 for n, i in enumerate(sorted(dids, key=lambda i: -S[q][i]))}
            for s in sts:
                tot[nm][0] += s['gain'] * (min(rk[ko[x]] for x in s['ps']) <= cut); tot[nm][1] += s['gain']
print({k: round(v[0] / v[1], 3) for k, v in tot.items()})
