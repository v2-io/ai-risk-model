#!/usr/bin/env python3
"""Document-side tags (DESIGN §12's idea), written blind to the queries by Sonnet taggers
(tagging/tags-N.json), measured against the judgments.

Variants, each one ranking at the fixed cut 188:
  tags-lex   BM25 over each passage's tags (Au5 as the collection), its rank fused into today's RRF at weight beta
  tags-sem   bge-m3 cosine between the query and the passage's tags joined, fused likewise
  tags-both  both legs
  doc2query  the passage re-embedded as title + path + text + "Topics: tags", replacing today's semantic leg
  + expansion: the blind expansion phrases (R+N) matched against tags as well (lexical and semantic)
"""
import glob, json, math, os, pickle, re, sys, collections
import numpy as np
sys.path.insert(0, os.path.dirname(__file__))
import rescore
from rescore import *
from common import qvec, connect, passages
from srcsearch import embed, rank
from srcsearch.db import embed_input

k = 60
TAGDIR = os.path.join(SPIKE, 'tagging')
CACHE = os.path.join(SPIKE, 'cache')


def load_tags():
    tags = {}
    for f in sorted(glob.glob(os.path.join(TAGDIR, 'tags-*.json'))):
        for i, ts in json.load(open(f))['tags'].items():
            tags[int(i)] = [t for t in ts if isinstance(t, str)]
    return tags


TOK = re.compile(r"[a-z0-9]+")


def toks(s):
    out = []
    for w in TOK.findall(s.lower()):
        if len(w) > 3 and w.endswith('s') and not w.endswith('ss'):
            w = w[:-1]
        out.append(w)
    return out


class BM25:
    def __init__(self, docs):
        self.d = {i: collections.Counter(toks(' ; '.join(ts))) for i, ts in docs.items()}
        self.len = {i: sum(c.values()) for i, c in self.d.items()}
        self.avg = np.mean(list(self.len.values())) or 1
        self.df = collections.Counter(w for c in self.d.values() for w in c)
        self.N = len(self.d)

    def score(self, q, stop=rank.STOP):
        ws = [w for w in dict.fromkeys(toks(q)) if w not in stop] or toks(q)
        out = {}
        for i, c in self.d.items():
            s = 0.0
            for w in ws:
                f = c.get(w, 0)
                if f:
                    idf = math.log(1 + (self.N - self.df[w] + 0.5) / (self.df[w] + 0.5))
                    s += idf * f * 2.2 / (f + 1.2 * (0.25 + 0.75 * self.len[i] / self.avg))
            if s:
                out[i] = s
        return out


def ranks(d, pool=None):
    r = {i: n + 1 for n, i in enumerate(sorted(d, key=lambda i: -d[i]))}
    return {i: v for i, v in r.items() if pool is None or v <= pool}


def embed_many(texts, path):
    if os.path.exists(path):
        z = np.load(path, allow_pickle=True)
        return dict(zip(z['ids'].tolist(), z['V']))
    ids = sorted(texts)
    vecs = []
    for j in range(0, len(ids), 16):
        vecs += embed._call('bge-m3', [texts[i] for i in ids[j:j + 16]])
    V = np.array(vecs, dtype=np.float32)
    V /= np.linalg.norm(V, axis=1, keepdims=True)
    np.savez(path, ids=np.array(ids), V=V)
    return dict(zip(ids, V))


def main():
    tags = load_tags()
    conn = connect()
    P = passages(conn)
    missing = [i for i in P if i not in tags]
    print(f'tags for {len(tags)} of {len(P)} passages; {sum(len(v) for v in tags.values()) / max(1, len(tags)):.1f} tags each; '
          f'{len(missing)} passages untagged')
    for i in missing:
        tags[i] = []
    titles = dict(conn.execute('select key, title from src.documents').fetchall())
    TV = embed_many({i: '; '.join(tags[i]) or '(none)' for i in P}, os.path.join(CACHE, 'bge-m3-tags.npz'))
    DV = embed_many({i: embed_input(dict(key=P[i]['key'], title=titles[P[i]['key']]), P[i]) +
                     ('\n\nTopics: ' + '; '.join(tags[i]) if tags[i] else '') for i in P},
                    os.path.join(CACHE, 'bge-m3-doc2query.npz'))
    bm = BM25({i: tags[i] for i in P})
    EXP = json.load(open(os.path.join(SPIKE, 'runs', 'blind-expansions.json')))['queries']
    ids = sorted(P)
    TVm = np.stack([TV[i] for i in ids]); DVm = np.stack([DV[i] for i in ids])
    phc = json.load(open(os.path.join(CACHE, 'phrase-qvec-bge-m3.json')))

    def qv(s):
        v = np.array(phc[s] if s in phc else qvec(s), dtype=np.float32)
        return v / np.linalg.norm(v)

    legs = {}
    for q in QUERIES:
        v = qv(q)
        legs[q] = dict(tlex=ranks(bm.score(q)), tsem=ranks(dict(zip(ids, (TVm @ v).tolist())), 400),
                       d2q=dict(zip(ids, (DVm @ v).tolist())))
        E = (EXP.get(q, {}).get('rephrasings', []) + EXP.get(q, {}).get('neighbours', []))
        legs[q]['E'] = [(ranks(bm.score(e)), ranks(dict(zip(ids, (TVm @ qv(e)).tolist())), 400)) for e in E]
    base = today()
    Eexp = pickle.load(open(os.path.join(SPIKE, 'runs', 'expansion-scores.pkl'), 'rb'))

    def fuse(start, beta, use=('tlex', 'tsem'), with_exp=False, alpha=2.0):
        S = {}
        for q in QUERIES:
            M = rescore._M.setdefault(q, rescore.multipliers(q))
            h = start[q]
            L = legs[q]
            S[q] = {}
            for i in h:
                add = sum(beta / (k + L[u].get(i, NBIG)) for u in use)
                if with_exp and L['E']:
                    add += (alpha * beta / len(L['E'])) * sum(1 / (k + a.get(i, NBIG)) + 1 / (k + b.get(i, NBIG)) for a, b in L['E'])
                S[q][i] = h[i] + M[i] * add
        return S

    print(f'today: flagged {flagged(base):.3f} must {flagged(base, must_only=True):.3f}')
    out = []
    for beta in (0.5, 1.0, 2.0):
        for name, use in (('tags-lex', ('tlex',)), ('tags-sem', ('tsem',)), ('tags-both', ('tlex', 'tsem'))):
            S = fuse(base, beta, use)
            d = boot(base, S)
            out.append((name, beta, S))
            print(f'{name:10} beta {beta:<3}: flagged {flagged(S):.3f} ({d[0]:+.3f}, {d[1]:+.3f} to {d[2]:+.3f}) must {flagged(S, must_only=True):.3f}')
    D2Q = {q: hybrid(q, sem=legs[q]['d2q']) for q in QUERIES}
    d = boot(base, D2Q)
    print(f'doc2query (text+tags embedded, replacing today\'s vector): flagged {flagged(D2Q):.3f} ({d[0]:+.3f}, {d[1]:+.3f} to {d[2]:+.3f}) must {flagged(D2Q, must_only=True):.3f}')
    for beta in (1.0, 2.0):
        S = fuse(Eexp['R+N|2.0'], beta)
        d = boot(base, S)
        print(f'query expansion R+N (alpha 2) + tags-both beta {beta}: flagged {flagged(S):.3f} ({d[0]:+.3f}, {d[1]:+.3f} to {d[2]:+.3f}) must {flagged(S, must_only=True):.3f}')
        S2 = fuse(Eexp['R+N|2.0'], beta, with_exp=True)
        d = boot(base, S2)
        print(f'  ... and expansion phrases matched against tags too:      flagged {flagged(S2):.3f} ({d[0]:+.3f}, {d[1]:+.3f} to {d[2]:+.3f}) must {flagged(S2, must_only=True):.3f}')
        out.append((f'exp+tags b{beta}', beta, S))
        out.append((f'exp+tags+exp-on-tags b{beta}', beta, S2))
    _, pq0 = flagged(base, per_query=True)
    best = max(out, key=lambda o: flagged(o[2]))
    _, pqb = flagged(best[2], per_query=True)
    print(f'\nper query, today -> best ({best[0]} beta {best[1]}):')
    for q in QUERIES:
        print(f'  {q[:48]:48} {pq0[q]:.2f} -> {pqb[q]:.2f}')
    pickle.dump({f'{n}|{b}': S for n, b, S in out} | {'doc2query': D2Q}, open(os.path.join(SPIKE, 'runs', 'tags-scores.pkl'), 'wb'))


if __name__ == '__main__':
    main()
