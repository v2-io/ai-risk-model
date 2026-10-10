"""De novo checks: shared loader. Reads the spike's code and pickles; writes only to this scratch dir."""
import os, sys, pickle, json
sys.dont_write_bytecode = True
SP = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
ME = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(SP, 'code'))
import numpy as np
import common as CM
import rescore as RS
T = RS.T
QUERIES = CM.QUERIES

def ro_conn():
    c = CM.connect()
    c.execute('set session characteristics as transaction read only')
    c.commit()
    return c

def load_scores():
    E = pickle.load(open(os.path.join(SP, 'runs', 'expansion-scores.pkl'), 'rb'))
    S = pickle.load(open(os.path.join(SP, 'runs', 'tags-scores.pkl'), 'rb'))
    out = dict(today=RS.today(), exp_a2=E['R+N|2.0'], exp_a1=E['R+N|1.0'], tags_b1=S['tags-both|1.0'],
               exptags=S['exp+tags+exp-on-tags b1.0|1.0'], exptags_noeot=S['exp+tags b1.0|1.0'])
    return out, S, E

def stretches_from(dirpath, conn, only_keys=None):
    grades, keys = CM.OC.judged_grades(dirpath)
    C = CM.OC.Corpus(conn, keys)
    out = {}
    nf = 0
    for q, items in grades.items():
        for it in items:
            if only_keys and it['key'] not in only_keys: continue
            s = C.resolve(it)
            if not s or not s['ps']:
                nf += 1; continue
            out.setdefault(q, []).append(dict(key=it['key'], grade=it['grade'], gain=2 ** it['grade'] - 1,
                                              must=it['grade'] >= 2, ps=sorted(s['ps']), lines=it['lines'],
                                              quote=it.get('quote', ''), how=s['how']))
    return out, keys, nf

def flagged_against(scores, ST, cut=188, must_only=False, queries=None, keys=None):
    """flagged over stretches ST {q: [stretch]} with scores {q: {pid: s}} ranking all Au5 passages."""
    num = den = 0; pq = {}
    for q in (queries or ST):
        if q not in scores or q not in ST: continue
        rows = T[q]['rows'] if q in T else None
        s = scores[q]
        rk = {i: n + 1 for n, i in enumerate(sorted(s, key=lambda i: -s[i]))}
        ko = {(CM_P[i]['key'], CM_P[i]['ord']): i for i in s}
        a = b = 0
        for st in ST[q]:
            if must_only and not st['must']: continue
            if keys and st['key'] not in keys: continue
            best = min(rk[ko[k]] for k in st['ps'])
            a += st['gain'] * (best <= cut); b += st['gain']
        num += a; den += b; pq[q] = (a, b)
    return (num / den if den else float('nan')), pq

def boot_pq(pqa, pqb, n=4000, seed=0):
    rng = np.random.default_rng(seed); qs = [q for q in pqa if pqa[q][1]]
    d = []
    for _ in range(n):
        smp = rng.choice(qs, len(qs))
        na = sum(pqa[q][0] for q in smp); da = sum(pqa[q][1] for q in smp)
        nb = sum(pqb[q][0] for q in smp); db = sum(pqb[q][1] for q in smp)
        d.append(nb / db - na / da)
    return np.percentile(d, 2.5), np.percentile(d, 97.5)

CM_P = pickle.load(open(os.path.join(SP, 'runs', 'table.pkl'), 'rb'))['P']
