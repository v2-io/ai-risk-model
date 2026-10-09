"""Is ollama's packaging of a model the problem, or the model? (search pilot, 2026-10-09)

Embeds the same passages and queries with the Hugging Face release of a model
through sentence-transformers, saved under the name hf-<model>, so eval.py can
score it beside the ollama build.

    HF_HUB_OFFLINE=1 python3 hf_check.py Qwen/Qwen3-Embedding-0.6B hf-qwen3-0.6b [--device mps]
"""
import json, os, re, sys, time
sys.dont_write_bytecode = True
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import embed  # noqa: E402

def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument('repo')
    ap.add_argument('name')
    ap.add_argument('--device', default='mps')
    ap.add_argument('--query-prompt', default=embed.PROMPTS['qwen3-embedding:0.6b'][0])
    a = ap.parse_args()
    from sentence_transformers import SentenceTransformer
    m = SentenceTransformer(a.repo, device=a.device)
    m.max_seq_length = 1024
    ps = embed.passages_for(1200)
    docs = [embed.doc_input('bge-m3', p, 'ctx') for p in ps]     # 'bge-m3' template = no document prefix
    t0 = time.time()
    v = m.encode(docs, batch_size=16, normalize_embeddings=True, show_progress_bar=False, convert_to_numpy=True)
    secs = time.time() - t0
    out = os.path.join(embed.SCRATCH, 'emb', f'{a.name}__t1200__ctx')
    np.save(out + '.npy', v.astype(np.float32))
    json.dump(dict(model=a.repo, n=len(ps), seconds=round(secs, 1), device=a.device), open(out + '.json', 'w'))
    qs = [q['q'] for q in json.load(open(os.path.join(HERE, 'gold-draft.json')))['queries']]
    qv = m.encode([a.query_prompt + q for q in qs], normalize_embeddings=True, convert_to_numpy=True)
    json.dump({q: qv[i].tolist() for i, q in enumerate(qs)},
              open(os.path.join(embed.SCRATCH, 'emb', f'{a.name}__queries.json'), 'w'))
    print(f'{a.repo}: {len(ps)} passages in {secs:.0f}s on {a.device}')

if __name__ == '__main__':
    main()
