#!/usr/bin/env python3
"""Re-embed every Au5 passage in input variants, into cache/ (git-ignored), never the database.

  full   title + path + text, exactly as db.embed_input builds it (a check: should match cache.embeddings)
  path   path + text, no title
  text   the passage text alone

usage: reembed.py MODEL [variant ...]
"""
import json, os, sys, time, urllib.request
import numpy as np
sys.path.insert(0, os.path.dirname(__file__))
from common import SPIKE, connect, passages
from srcsearch.db import embed_input

OLLAMA = 'http://localhost:11434/api/embed'
# (query prefix, document template, ctx): as search/srcsearch/embed.py for the models it knows
MODELS = {
    'bge-m3': ('', '{body}', 8192),
    'snowflake-arctic-embed2': ('query: ', '{body}', 8192),
    'nomic-embed-text-v2-moe': ('search_query: ', 'search_document: {body}', 512),
    'embeddinggemma:300m': ('task: search result | query: ', 'title: none | text: {body}', 2048),
    'qwen3-embedding:0.6b': ('Instruct: Given a search query, retrieve passages of AI-risk documents that answer it\nQuery: ',
                             '{body}', 8192),
    'mxbai-embed-large': ('Represent this sentence for searching relevant passages: ', '{body}', 512),
}


def call(model, inputs, keep='5m'):
    ctx = MODELS[model][2]
    body = dict(model=model, input=inputs, truncate=True, keep_alive=keep, options=dict(num_ctx=ctx, num_batch=ctx))
    req = urllib.request.Request(OLLAMA, data=json.dumps(body).encode(), headers={'Content-Type': 'application/json'})
    return json.load(urllib.request.urlopen(req, timeout=3600))['embeddings']


def inputs(conn, P, variant):
    titles = dict(conn.execute("select key, title from src.documents where key = any(%s)", (sorted({p['key'] for p in P.values()}),)).fetchall())
    out = {}
    for i, p in P.items():
        if variant == 'full':
            out[i] = embed_input(dict(key=p['key'], title=titles[p['key']]), p)
        elif variant == 'path':
            out[i] = (' › '.join(p['path']) + '\n\n' if p['path'] else '') + p['text']
        else:
            out[i] = p['text']
    return out


def main():
    model = sys.argv[1]
    variants = sys.argv[2:] or ['full', 'path', 'text']
    conn = connect()
    P = passages(conn)
    os.makedirs(os.path.join(SPIKE, 'cache'), exist_ok=True)
    tmpl = MODELS[model][1]
    try:
        for v in variants:
            path = os.path.join(SPIKE, 'cache', f'{model.replace(":", "_")}-{v}.npz')
            if os.path.exists(path):
                print('have', path)
                continue
            inp = inputs(conn, P, v)
            ids = sorted(inp)
            vecs, t0 = [], time.time()
            for k in range(0, len(ids), 16):
                vecs += call(model, [tmpl.format(body=inp[i]) for i in ids[k:k + 16]])
            V = np.array(vecs, dtype=np.float32)
            V /= np.linalg.norm(V, axis=1, keepdims=True)
            np.savez(path, ids=np.array(ids), V=V)
            print(f'{model} {v}: {len(ids)} passages in {time.time() - t0:.0f}s -> {path}', flush=True)
    finally:
        try:
            call(model, ['x'], keep=0)
        except Exception:
            pass


if __name__ == '__main__':
    main()
