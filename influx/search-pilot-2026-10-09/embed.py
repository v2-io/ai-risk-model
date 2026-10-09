"""Embed the pilot passages with one ollama model (search pilot, 2026-10-09).

    python3 embed.py MODEL [--target 1200] [--input ctx|raw]

Writes <scratch>/emb/<model>__t<target>__<input>.npy (unit-normalised float32,
row order = passages.json for that target) and a .json sidecar with timings.
One model at a time; the model is unloaded afterwards (keep_alive 0) because
Joseph's laptop is shared.

Prompts: each model gets the query/document prefixes its authors specify.
Leaving them off is a common way to under-rate asymmetric models.
"""
import json, os, re, sys, time, urllib.request
sys.dont_write_bytecode = True
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import chunk  # noqa: E402

SCRATCH = os.environ.get('PILOT_SCRATCH', '/private/tmp/claude-505/-Users-josephwecker-v2-src-ai-risk-model/'
                         'd8b6db06-39a9-4093-aa85-b8d0915a85d8/scratchpad/pilot')

KEYS = ['california-2025-sb53', 'openai-2025-preparedness-framework-v2', 'eu-cop-2025-safety-security',
        'nvidia-2025-frontier', 'nist-2023-ai-rmf', 'cabinetoffice-2026-nrr', 'eu-2024-ai-act',
        'bengio-2026-international', 'anthropic-2026-risk-report-aug', 'bengio-2026-international-extended']
TITLES = {
    'california-2025-sb53': 'California SB 53, Transparency in Frontier Artificial Intelligence Act (2025)',
    'openai-2025-preparedness-framework-v2': 'OpenAI, Preparedness Framework, Version 2 (2025)',
    'eu-cop-2025-safety-security': 'EU General-Purpose AI Code of Practice: Safety and Security Chapter (2025)',
    'nvidia-2025-frontier': 'NVIDIA, Frontier AI Risk Assessment (2025)',
    'nist-2023-ai-rmf': 'NIST, Artificial Intelligence Risk Management Framework (AI RMF 1.0) (2023)',
    'cabinetoffice-2026-nrr': 'UK Cabinet Office, National Risk Register 2026',
    'eu-2024-ai-act': 'EU Artificial Intelligence Act, Regulation (EU) 2024/1689',
    'bengio-2026-international': 'International AI Safety Report 2026',
    'anthropic-2026-risk-report-aug': 'Anthropic, Risk Report: August 2026',
    'bengio-2026-international-extended': 'International AI Safety Report 2026: Extended Summary for Policymakers',
}

# (query prefix, document prefix template, max tokens the model was trained for)
PROMPTS = {
    'bge-m3': ('', '{body}', 8192),
    'bge-large': ('Represent this sentence for searching relevant passages: ', '{body}', 512),
    'mxbai-embed-large': ('Represent this sentence for searching relevant passages: ', '{body}', 512),
    'snowflake-arctic-embed2': ('query: ', '{body}', 8192),
    'snowflake-arctic-embed': ('Represent this sentence for searching relevant passages: ', '{body}', 512),
    'nomic-embed-text-v2-moe': ('search_query: ', 'search_document: {body}', 512),
    'embeddinggemma:300m': ('task: search result | query: ', 'title: {title} | text: {body}', 2048),
    'granite-embedding:30m': ('', '{body}', 512),
    'qwen3-embedding:0.6b': ('Instruct: Given a search query about AI risk, safety or governance, retrieve passages '
                             'from source documents that define or discuss it\nQuery: ', '{body}', 8192),
    'qwen3-embedding': ('Instruct: Given a search query about AI risk, safety or governance, retrieve passages '
                        'from source documents that define or discuss it\nQuery: ', '{body}', 8192),
}

def passages_for(target):
    path = os.path.join(SCRATCH, f'passages_t{target}.json')
    if os.path.exists(path):
        return json.load(open(path))
    out = []
    for k in KEYS:
        ps, _ = chunk.passages(k, target)
        out.extend(ps)
    os.makedirs(SCRATCH, exist_ok=True)
    json.dump(out, open(path, 'w'))
    return out

def doc_input(model, p, mode):
    if mode == 'ctx':
        head = TITLES[p['key']]
        path = ' › '.join(p['path'][1:]) if len(p['path']) > 1 else ''
        body = head + ('\n' + path if path else '') + '\n\n' + p['text']
        title = TITLES[p['key']]
    else:
        body, title = p['text'], 'none'
    return PROMPTS[model][1].format(body=body, title=title)

def call(model, inputs, ctx, keep_alive='5m'):
    body = dict(model=model, input=inputs, truncate=True, keep_alive=keep_alive,
                options=dict(num_ctx=ctx, num_batch=ctx))
    req = urllib.request.Request('http://localhost:11434/api/embed', data=json.dumps(body).encode(),
                                 headers={'Content-Type': 'application/json'})
    return json.load(urllib.request.urlopen(req, timeout=3600))

def embed_queries(model, queries):
    pre, _, mx = PROMPTS[model]
    d = call(model, [pre + q for q in queries], min(mx, 2048))
    v = np.array(d['embeddings'], dtype=np.float32)
    return v / np.linalg.norm(v, axis=1, keepdims=True)

EXTRA_QUERIES = os.path.join(HERE, 'queries-extra.json')

def save_queries(model):
    """Embed the gold queries (and any extras) with this model while it is loaded."""
    qs = [q['q'] for q in json.load(open(os.path.join(HERE, 'gold-draft.json')))['queries']]
    if os.path.exists(EXTRA_QUERIES):
        qs += json.load(open(EXTRA_QUERIES))
    name = re.sub(r'[^\w.-]', '_', model)
    path = os.path.join(SCRATCH, 'emb', f'{name}__queries.json')
    have = json.load(open(path)) if os.path.exists(path) else {}
    todo = [q for q in dict.fromkeys(qs) if q not in have]
    if todo:
        v = embed_queries(model, todo)
        have.update({q: v[i].tolist() for i, q in enumerate(todo)})
        json.dump(have, open(path, 'w'))
    return have

def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument('model')
    ap.add_argument('--target', type=int, default=1200)
    ap.add_argument('--input', default='ctx', choices=['ctx', 'raw'])
    ap.add_argument('--batch', type=int, default=16)
    a = ap.parse_args()
    ps = passages_for(a.target)
    name = re.sub(r'[^\w.-]', '_', a.model)
    out = os.path.join(SCRATCH, 'emb', f'{name}__t{a.target}__{a.input}')
    os.makedirs(os.path.dirname(out), exist_ok=True)
    if os.path.exists(out + '.npy'):
        print('exists', out)
        return
    mx = PROMPTS[a.model][2]
    ctx = min(mx, 8192)
    inputs = [doc_input(a.model, p, a.input) for p in ps]
    vecs, toks, t0 = [], 0, time.time()
    for i in range(0, len(inputs), a.batch):
        d = call(a.model, inputs[i:i + a.batch], ctx)
        vecs.extend(d['embeddings'])
        toks += d.get('prompt_eval_count', 0)
        if (i // a.batch) % 20 == 0:
            print(f'{a.model} {i + len(inputs[i:i + a.batch])}/{len(inputs)} {time.time() - t0:.0f}s', flush=True)
    secs = time.time() - t0
    v = np.array(vecs, dtype=np.float32)
    v /= np.linalg.norm(v, axis=1, keepdims=True)
    np.save(out + '.npy', v)
    # truncation check: how many inputs exceed the model's window (chars/4 is rough; count exactly on a sample)
    json.dump(dict(model=a.model, target=a.target, input=a.input, n=len(ps), seconds=round(secs, 1),
                   tokens=toks, dims=v.shape[1], ctx=ctx), open(out + '.json', 'w'))
    save_queries(a.model)
    call(a.model, ['x'], ctx, keep_alive=0)   # unload
    print(f'done {a.model}: {len(ps)} passages, {secs:.0f}s, {toks} tokens, dim {v.shape[1]}')

if __name__ == '__main__':
    main()
