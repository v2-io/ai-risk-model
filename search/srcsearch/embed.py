"""Embeddings, through a local ollama, cached by model and input (DESIGN §4, §5.4).

The cache is keyed by sha256 of the exact text embedded, so only passages whose
embedding input is new are sent to the model; a rebuild, or a re-chunk that leaves
a passage unchanged, costs nothing. Batches are committed as they finish, so an
interrupted run resumes where it stopped.

Each model gets the query and document prefixes its authors specify (from the
pilot's embed.py). bge-m3 needs none. Its 8,192-token window is real only when
num_ctx and num_batch are raised: by default ollama cuts it at 2,048 tokens and
says nothing (pilot REPORT §2).
"""
import hashlib, json, time, urllib.request

from .db import embed_input

OLLAMA = 'http://localhost:11434/api/embed'
DEFAULT_MODEL = 'bge-m3'
# model: (query prefix, document prefix template, context window in tokens, dimensions)
MODELS = {
    'bge-m3': ('', '{body}', 8192, 1024),
    'snowflake-arctic-embed2': ('query: ', '{body}', 8192, 1024),
    'nomic-embed-text-v2-moe': ('search_query: ', 'search_document: {body}', 512, 768),
    'embeddinggemma:300m': ('task: search result | query: ', 'title: none | text: {body}', 2048, 768),
}


def _call(model, inputs, keep_alive='5m'):
    ctx = MODELS[model][2]
    body = dict(model=model, input=inputs, truncate=True, keep_alive=keep_alive,
                options=dict(num_ctx=ctx, num_batch=ctx))
    req = urllib.request.Request(OLLAMA, data=json.dumps(body).encode(), headers={'Content-Type': 'application/json'})
    return json.load(urllib.request.urlopen(req, timeout=3600))['embeddings']


def unload(model):
    try:
        _call(model, ['x'], keep_alive=0)
    except Exception:
        pass


def embed_query(model, query):
    return _call(model, [MODELS[model][0] + query])[0]


def _vec(v):
    return '[' + ','.join(f'{x:.6g}' for x in v) + ']'


def missing(conn, model):
    """[(embed_sha, input text)] for passages with no cached vector for model."""
    rows = conn.execute(
        'select distinct on (p.embed_sha) p.embed_sha, d.key, d.title, p.path, p.section, p.text '
        'from src.passages p join src.documents d on d.key = p.doc_key '
        'where not exists (select 1 from cache.embeddings e where e.model = %s and e.input_sha = p.embed_sha) '
        'order by p.embed_sha', (model,)).fetchall()
    out = []
    for sha, key, title, path, section, text in rows:
        inp = embed_input(dict(key=key, title=title), dict(path=path, section=section, text=text))
        if hashlib.sha256(inp.encode()).hexdigest() != sha:
            raise RuntimeError(f'{key}: a passage\'s embedding input no longer hashes to its embed_sha; '
                               f'run bin/source-index --rebuild')
        out.append((sha, inp))
    return out


def embed_missing(conn, model=DEFAULT_MODEL, batch=16, log=print):
    todo = missing(conn, model)
    # end the read's transaction: otherwise each batch's transaction below is only a
    # savepoint inside it, nothing commits until the end, and the open transaction
    # holds locks that block a concurrent --rebuild (it happened, 2026-10-09)
    conn.commit()
    if not todo:
        return 0
    prefix, tmpl, _, dims = MODELS[model]
    log(f'embedding {len(todo)} passages with {model} (cached vectors are reused; Ctrl-C is safe, a rerun resumes)')
    t0, done = time.time(), 0
    try:
        for i in range(0, len(todo), batch):
            part = todo[i:i + batch]
            vecs = _call(model, [tmpl.format(body=inp, title='none') for _, inp in part])
            with conn.transaction():
                with conn.cursor() as cur:
                    cur.executemany(
                        'insert into cache.embeddings (model, input_sha, dims, vec) values (%s, %s, %s, %s::halfvec) '
                        'on conflict do nothing',
                        [(model, sha, len(v), _vec(v)) for (sha, _), v in zip(part, vecs)])
            done += len(part)
            if (i // batch) % 100 == 0 or done == len(todo):
                el = time.time() - t0
                log(f'  {done}/{len(todo)}  {el:.0f}s  (about {el / done * (len(todo) - done):.0f}s left)')
    finally:
        unload(model)
    return done


def gc(conn):
    """Delete cached vectors no passage uses. Keeping them makes a revert free."""
    with conn.transaction():
        cur = conn.execute('delete from cache.embeddings e where not exists '
                           '(select 1 from src.passages p where p.embed_sha = e.input_sha)')
        return cur.rowcount
