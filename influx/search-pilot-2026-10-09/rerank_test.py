"""Would a cross-encoder have helped? (search pilot, 2026-10-09)

Reranks the head of a first-stage ranking with bge-reranker-v2-m3 on CPU only
(memorata measured 18-21 GB on Metal, ~4.8 GB on CPU), and scores three orders
of that head against gold-draft.json: first stage alone, reranker alone, and the
reranker folded in as one multiplicative factor (memorata's way).

    HF_HUB_OFFLINE=1 python3 rerank_test.py --model qwen3-embedding:0.6b --mode rrf+p --head 30
"""
import json, math, os, resource, sys, time
sys.dont_write_bytecode = True
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import embed, eval as ev, search  # noqa: E402

def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument('--model', default='bge-m3')
    ap.add_argument('--mode', default='mix+p')
    ap.add_argument('--head', type=int, default=30)
    ap.add_argument('--boost', type=float, default=1.0)
    ap.add_argument('--qrels')
    a = ap.parse_args()
    from sentence_transformers import CrossEncoder
    t0 = time.time()
    ce = CrossEncoder('BAAI/bge-reranker-v2-m3', device='cpu', max_length=512)
    load_s = time.time() - t0
    gold = ev.load_gold()
    ix = search.Index(1200)
    if a.qrels:
        qr = {}
        for f in a.qrels.split(','):
            for q, d in json.load(open(f)).items():
                qr.setdefault(q, {}).update(d)
        pid = {p['id']: i for i, p in enumerate(ix.ps)}
        for g in gold:
            g['expect'] = [dict(grade=int(v), pid=k) for k, v in qr.get(g['q'], {}).items() if int(v) > 0]
        hold = [[{pid[e['pid']]} for e in g['expect']] for g in gold]
    else:
        hold = ev.matches(ix, gold)
    qv = ev.qvecs(a.model)
    tot = {'first': [], 'rerank': [], 'fold': []}
    secs = 0
    for g, hs in zip(gold, hold):
        order, sig = ix.rank(g['q'], a.model, a.mode, qvec=qv[g['q']])
        head = [int(i) for i in order[:a.head]]
        pairs = [(g['q'], embed.doc_input('bge-m3', ix.ps[i], 'ctx')) for i in head]
        t = time.time()
        s = ce.predict(pairs, batch_size=8)
        secs += time.time() - t
        rel = 1 / (1 + np.exp(-np.array(s) / 4.0))        # memorata's temperature
        rr = [head[j] for j in np.argsort(-np.array(s))]
        fold = [head[j] for j in np.argsort(-(sig['base'][head] * (1 + a.boost * rel)))]
        for name, o in (('first', head), ('rerank', rr), ('fold', fold)):
            o2 = np.array(o + [int(i) for i in order[a.head:]])
            sc = ev.score(o2, g['expect'], hs)
            tot[name].append(sc['ndcg'])
            if name != 'first':
                pass
        print(f'{g["q"][:44]:<44} first {tot["first"][-1]:.2f}  rerank {tot["rerank"][-1]:.2f}  fold {tot["fold"][-1]:.2f}', flush=True)
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e9   # bytes on macOS
    print(f'mean nDCG@10  first {np.mean(tot["first"]):.3f}  rerank {np.mean(tot["rerank"]):.3f}  fold {np.mean(tot["fold"]):.3f}')
    print(f'load {load_s:.1f}s; rerank {secs:.1f}s for {len(gold)} queries x {a.head}; peak RSS {rss:.1f} GB')

if __name__ == '__main__':
    main()
