"""Pool the top results of every configuration for blind relevance judging (search pilot, 2026-10-09).

    python3 pool.py --depth 10 > pool.json

The gold draft lists what I expected before running anything; it cannot credit a
relevant passage I didn't think of (the AI Act's 'stop' button for the
shut-down paraphrase, say). Pooling, as TREC does, collects the union of every
configuration's top results per query; a judge who doesn't know which
configuration found what grades each one. Passages are shuffled per query.
"""
import json, os, random, sys
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import embed, eval as ev, search  # noqa: E402

def configs():
    emb = os.path.join(embed.SCRATCH, 'emb')
    models = sorted({f.split('__')[0] for f in os.listdir(emb) if f.endswith('__t1200__ctx.npy')})
    name2model = {m.replace('_', ':') if m.startswith(('embeddinggemma', 'granite', 'qwen3-embedding_0')) else m: m for m in models}
    out = [('-', 'lex+p')]
    for m in name2model:
        out += [(m, 'sem'), (m, 'rrf+p'), (m, 'mix+p')]
    return out

def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument('--depth', type=int, default=10)
    a = ap.parse_args()
    gold = ev.load_gold()
    ix = search.Index(1200)
    rng = random.Random(20261009)
    pool = []
    cfgs = configs()
    qv = {}
    for g in gold:
        ids = set()
        for m, mode in cfgs:
            if mode.startswith('lex'):
                order, _ = ix.rank(g['q'], 'bge-m3', mode)
            else:
                if m not in qv:
                    qv[m] = ev.qvecs(m)
                order, _ = ix.rank(g['q'], m, mode, qvec=qv[m][g['q']])
            ids.update(int(i) for i in order[:a.depth])
        ids = sorted(ids)
        rng.shuffle(ids)
        items = []
        for i in ids:
            p = ix.ps[i]
            items.append(dict(pid=p['id'], source=embed.TITLES[p['key']], section=' › '.join(p['path'][1:]),
                              text=p['text']))
        pool.append(dict(q=g['q'], kind=g['kind'], why=g.get('why', ''), items=items))
        print(f'{g["q"][:50]:<50} {len(items)} passages', file=sys.stderr)
    print(f'configurations pooled: {cfgs}', file=sys.stderr)
    json.dump(pool, sys.stdout, indent=1, ensure_ascii=False)

if __name__ == '__main__':
    main()
