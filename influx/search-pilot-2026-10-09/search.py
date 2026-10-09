"""Pilot ranker over the embedded pilot passages (search pilot, 2026-10-09).

In memory (numpy), not Postgres: the point is to compare rankings, not to build
the index. Lexical scoring is BM25 (exact word forms, plus Postgres's own
english_stem for the stemmed side, fetched once through psql-18), with phrase
and memorata's proximity/density folded into one lexical score, as in
memorata's mix mode. Semantic is cosine over one model's vectors.

    python3 search.py 'hazard' [--model bge-m3] [--mode mix+p] [-n 10] [--explain]

Every result carries the anchor the plan asks for (§3.5): relata key, physical
PDF page, printed page, and an exact quote in the canonical file's characters.
"""
import json, math, os, re, subprocess, sys, unicodedata
sys.dont_write_bytecode = True
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import chunk, embed  # noqa: E402

SCRATCH = embed.SCRATCH
STOP = set('a an and are as at be by for from has have in is it its of on or that the this to was were will with which we our'.split())

# ------------------------------------------------------------ tokenizing
def fold(s):
    s = unicodedata.normalize('NFKC', s).lower()
    return s.replace('‑', '-').replace('‐', '-').replace('’', "'")

WORD = re.compile(r'[a-z0-9]+')

def words(s):
    return WORD.findall(fold(s))

_STEMS = {}
def stems(vocab):
    """english_stem for each word, from Postgres itself (the design's stemmed side), cached on disk."""
    path = os.path.join(SCRATCH, 'stems.json')
    if not _STEMS and os.path.exists(path):
        _STEMS.update(json.load(open(path)))
    missing = sorted(set(vocab) - set(_STEMS))
    for i in range(0, len(missing), 5000):
        part = missing[i:i + 5000]
        arr = '{' + ','.join(part) + '}'
        out = subprocess.run(['psql-18', '-d', 'postgres', '-Atc',
                              "select w, coalesce(array_to_string(ts_lexize('english_stem', w), ','), '') "
                              "from unnest(%s::text[]) w" % ("'" + arr + "'")],
                             capture_output=True, text=True, check=True).stdout
        for line in out.splitlines():
            w, _, s = line.partition('|')
            _STEMS[w] = s or w
    if missing:
        json.dump(_STEMS, open(path, 'w'))
    return _STEMS

# ------------------------------------------------------------- the index
class Index:
    def __init__(self, target=1200):
        self.target = target
        self.ps = embed.passages_for(target)
        self.toks = [words(p['text']) for p in self.ps]
        vocab = {w for t in self.toks for w in t}
        self.stem = stems(vocab)
        self.N = len(self.ps)
        self.len = np.array([len(t) for t in self.toks], dtype=np.float32)
        self.avg = float(self.len.mean())
        self.df_w, self.df_s = {}, {}
        self.tf_w, self.tf_s = [], []
        for t in self.toks:
            cw, cs = {}, {}
            for w in t:
                cw[w] = cw.get(w, 0) + 1
                s = self.stem.get(w, w)
                cs[s] = cs.get(s, 0) + 1
            self.tf_w.append(cw)
            self.tf_s.append(cs)
            for w in cw:
                self.df_w[w] = self.df_w.get(w, 0) + 1
            for s in cs:
                self.df_s[s] = self.df_s.get(s, 0) + 1
        self.vecs = {}

    def vec(self, model, inp='ctx'):
        k = (model, inp)
        if k not in self.vecs:
            name = re.sub(r'[^\w.-]', '_', model)
            self.vecs[k] = np.load(os.path.join(SCRATCH, 'emb', f'{name}__t{self.target}__{inp}.npy'))
        return self.vecs[k]

    # ---------------------------------------------------------- lexical
    def bm25(self, qterms, tf, df, k1=1.2, b=0.75):
        sc = np.zeros(self.N, dtype=np.float32)
        for q in qterms:
            n = df.get(q, 0)
            if not n:
                continue
            idf = math.log(1 + (self.N - n + .5) / (n + .5))
            for i, c in enumerate(tf):
                f = c.get(q)
                if f:
                    sc[i] += idf * f * (k1 + 1) / (f + k1 * (1 - b + b * self.len[i] / self.avg))
        return sc

    def lexical(self, query):
        qw = [w for w in words(query) if w not in STOP] or words(query)
        qs = [self.stem.get(w) or stems([w])[w] for w in qw]
        exact = self.bm25(qw, self.tf_w, self.df_w)
        stemmed = self.bm25(qs, self.tf_s, self.df_s)
        score = exact + 0.5 * stemmed           # exact form counts for more than a stemmed match
        phrase = np.zeros(self.N, dtype=np.float32)
        if len(qw) > 1:
            pat = ' '.join(words(query))
            for i, t in enumerate(self.toks):
                if score[i] > 0 and pat in ' '.join(t):
                    phrase[i] = 1
            score = score * (1 + phrase)
        return score, phrase

    # --------------------------------------------------------- priors
    def def_match(self, p, query):
        """How strongly the passage defines the queried term.

        v1 (the first runs): 1.0 for the term itself, 0.6 for a term containing the query
        or contained in it. The judged pool showed the second half was wrong: the bare
        'risk' definitions were boosted for 'catastrophic risk', 'Hazard' for 'information
        hazard'. A *narrower* term ('loss of control scenario', 'passive loss of control')
        is a definition someone surveying the query wants; a *broader* one isn't.
        v2 (DEF_RULE = 'v2'): exact 1.0; a term containing the query 0.5; contained 0."""
        if DEF_RULE == 'v2':
            # "definition of X", "what is X", "meaning of X", "define X": the term is X
            query = re.sub(r'^\s*(?:(?:the\s+)?(?:definitions?|meaning) of|what (?:is|are)(?: an?)?|define)\s+', '', query, flags=re.I)
        qn = chunk.norm_term(query)
        best = 0.0
        defs = p['defs'] + (self.extra_defs(p) if DEF_RULE == 'v2' else [])
        for d in defs:
            n = d.get('norm') or chunk.norm_term(d['term'])
            if n == qn:
                m = 1.0
            elif re.search(r'\b' + re.escape(qn) + r'\b', n):
                m = 0.6 if DEF_RULE == 'v1' else NARROWER
            elif DEF_RULE == 'v1' and len(n) > 3 and re.search(r'\b' + re.escape(n) + r'\b', qn):
                m = 0.6
            else:
                continue
            best = max(best, m * d['conf'])
        return best

    _XD = {}
    def extra_defs(self, p):
        """Definitions in running prose that the chunker's patterns missed (found from the
        judged pool's misses): 'the notion of X' (AI Act recitals), and a repeated head
        noun, 'X scenarios are scenarios in which', 'systemic risks are risks that'."""
        if p['id'] in self._XD:
            return self._XD[p['id']]
        out = []
        t = p['text']
        for m in re.finditer(r"\bthe notion of ['‘\"]([^'’\"]{2,50})['’\"]", t, re.I):
            out.append(dict(term=m.group(1), kind='notion-of', conf=0.8))
        for m in re.finditer(r"(?:^|[.:;]\s+|\n|,\s+)(?:-\s*)?([A-Za-z][\w-]*(?:\s+[\w-]+){0,4}?)\s+(\w+?s?)\s+(?:is|are)\s+(?:an?\s+)?\2\b\s+(?:that|which|in which|where|when|of)\b", t):
            term = (m.group(1) + ' ' + m.group(2)).strip()
            term = re.sub(r'^(?:in this \w+\s+)', '', term, flags=re.I)
            out.append(dict(term=term, kind='repeated-head', conf=0.7))
        for d in out:
            d['norm'] = chunk.norm_term(d['term'])
        self._XD[p['id']] = out
        return out

    def prior(self, p, query, weights):
        m = 1.0
        dm = self.def_match(p, query)
        if dm:
            m *= 1 + weights['defines'] * dm
        m *= weights['section'].get(p['section'], 1.0)
        return m, dm

    # ------------------------------------------------------- ranking
    def rank(self, query, model='bge-m3', mode='mix+p', inp='ctx', weights=None, qvec=None, keys=None):
        weights = weights or DEFAULT_WEIGHTS
        lex, phrase = self.lexical(query)
        idx = np.arange(self.N)
        if keys:
            mask = np.array([p['key'] in keys for p in self.ps])
        else:
            mask = np.ones(self.N, bool)
        sem = None
        if not mode.startswith('lex'):
            if qvec is None:
                qvec = embed.embed_queries(model, [query])[0]
            sem = self.vec(model, inp) @ qvec
        if mode.startswith('lex'):
            base = lex.copy()
            base[lex <= 0] = -1
        elif mode.split('+')[0] == 'sem':
            base = sem.copy()
        else:
            sem_rank = np.empty(self.N)
            sem_rank[np.argsort(-sem)] = np.arange(1, self.N + 1)
            lex_rank = np.empty(self.N)
            order = np.lexsort((-sem, -lex))      # ties in lex (incl. all zeros) broken by sem
            lex_rank[order] = np.arange(1, self.N + 1)
            lex_rank[lex <= 0] = self.N + 1
            if mode.startswith('rrf'):
                base = 1 / (60 + sem_rank) + 1 / (60 + lex_rank)
            else:
                base = 1 / np.sqrt(sem_rank * lex_rank)
        dms = np.zeros(self.N)
        self._last_defs = dms
        if '+p' in mode:
            pri = np.ones(self.N)
            for i, p in enumerate(self.ps):
                pri[i], dms[i] = self.prior(p, query, weights)
            base = base * pri if not mode.startswith('lex') else np.where(base > 0, base * pri, base)
        base = np.where(mask, base, -np.inf)
        order = np.argsort(-base)
        if mode.endswith('+d'):
            order = self.diversify(order, base, weights.get('per_doc_decay', 0.7))
        return order, dict(base=base, lex=lex, sem=sem, phrase=phrase, defs=dms)

    def diversify(self, order, base, decay, head=300):
        """Each further passage from a document already shown is scaled by decay**n, so a
        term-survey query shows each source's best passage before one source's tenth.
        Definitions are exempt: two definitions in one source (SB 53's two 'catastrophic
        risk's) are both wanted."""
        seen, adj = {}, []
        for i in order[:head]:
            k = self.ps[i]['key']
            n = seen.get(k, 0)
            is_def = bool(self.ps[i]['defs']) and base[i] > 0 and self._last_defs is not None and self._last_defs[i] > 0
            adj.append((base[i] * (1 if is_def else decay ** n), i))
            if not is_def:
                seen[k] = n + 1
        adj.sort(key=lambda x: -x[0])
        return np.array([i for _, i in adj] + list(order[head:]))

DEF_RULE = os.environ.get('PILOT_DEF_RULE', 'v1')
NARROWER = float(os.environ.get('PILOT_NARROWER', '0.25'))   # v2's boost for a definition of a narrower term
DEFAULT_WEIGHTS = dict(defines=2.0, section={'toc': 0.3, 'references': 0.3, 'abbreviations': 0.5})

# --------------------------------------------------------------- anchors
_RAW = {}
def raw_of(key):
    if key not in _RAW:
        _RAW[key] = open(os.path.join(chunk.CANON, key + '.md'), encoding='utf-8').read()
    return _RAW[key]

_PAGES = {}
def pages_of(key):
    if key not in _PAGES:
        _, marks, _ = chunk.parse(key)
        _PAGES[key] = chunk.Pages(marks)
    return _PAGES[key]

_CUR = {}
def current(p):
    """The same passage re-chunked from the canonical text as it is now. The embedded
    passages were cut before the 2026-10-09 rebuild (OCR "Al" -> "AI", plus a header
    line that shifted every offset in the corrected files); quotes and pages must come
    from today's text. The chunking is identical (checked), so ids line up."""
    k = p['key']
    if k not in _CUR:
        ps, _ = chunk.passages(k, 1200)
        _CUR[k] = {q['id']: q for q in ps}
    q = _CUR[k].get(p['id'])
    return q if q and q['text'].replace('Al', 'AI') == p['text'].replace('Al', 'AI') else p

def anchor(p, query):
    """An anchor: key, physical page, printed page, and a quote of one sentence (or less)
    that bin/check-quote can find, preferring the first sentence holding a query word.
    Sentences are found with links, tags and images masked, and a quote never spans a
    link (the tooltip's letters sit in the canonical text). For a check-all source the
    page here is the canonical marker's; bin/check-quote's PDF-settled page is the one
    to cite."""
    raw = raw_of(p['key'])
    p = current(p)
    seg_start = p['start']
    # Mask link targets, tooltips, images and tags with spaces (same length, so offsets
    # still map to pages). Sentences are then found in what a reader sees: an IASR
    # tooltip holds a full reference, and a quote taken from it lands on the endnote page.
    def pad(m, keep=''):
        return keep + ' ' * (len(m.group(0)) - len(keep))
    seg = raw[p['start']:p['end']]
    seg = chunk.IMG_RE.sub(pad, seg)
    seg = chunk.LINK_RE.sub(lambda m: pad(m, '' if re.fullmatch(r'[\d,\s–-]*', m.group(1)) else m.group(1)), seg)
    seg = re.sub(r'<[^>\n]{0,200}>', pad, seg)
    qw = [w for w in words(query) if w not in STOP]
    # sentence spans in the raw segment, never crossing a marker line
    spans = []
    for para in re.finditer(r'[^\n]+', seg):
        line = para.group(0)
        if chunk.corpus.MARK_RE.match(line) or line.startswith('```') or re.fullmatch(r'\s*\|?[\s|:-]+\|?\s*', line):
            continue
        for s in re.finditer(r'[^.;!?]+(?:[.;!?]+|$)', line):
            spans.append((para.start() + s.start(), para.start() + s.end()))
    def ok(a, b):
        return len(words(seg[a:b])) >= 4
    pick = None
    for a, b in spans:
        if ok(a, b) and any(w in words(seg[a:b]) for w in qw):
            pick = (a, b)
            break
    if pick is None:
        pick = next(((a, b) for a, b in spans if ok(a, b)), spans[0] if spans else (0, len(seg)))
    a, b = pick
    # a masked link (a long run of spaces) inside the sentence: the canonical text has the
    # tooltip's letters there, so a quote across it would not match. Quote up to it, or
    # from after it when too little precedes it.
    while True:
        gap = re.search(r' {8,}', seg[a:b].strip())
        if not gap:
            break
        lead = len(seg[a:b]) - len(seg[a:b].lstrip())
        g0, g1 = a + lead + gap.start(), a + lead + gap.end()
        if len(words(seg[a:g0])) >= 4:
            b = g0
        elif len(words(seg[g1:b])) >= 4:
            a = g1
        else:
            break
    q = seg[a:b]
    # drop tags, <br>, table pipes and emphasis, which bin/check-quote ignores (it matches
    # on letters and digits, and reports such a quote as matching but not 'exact')
    q = chunk.clean(q).replace('|', ' ')
    q = re.sub(r'\s+', ' ', q)
    q = re.sub(r'^\s*(?:-\s*)?(?:\(\w{1,4}\)\s*)*', '', q)
    q = q.replace('**', '').strip().strip('*').strip()
    if len(q) > 220:
        q = q[:220].rsplit(' ', 1)[0]
    off = seg_start + a + (len(seg[a:b]) - len(seg[a:b].lstrip()))
    page, printed, nip = pages_of(p['key']).at(off)
    return dict(key=p['key'], page=page, printed=printed, not_in_pdf=nip, quote=q)

def fmt_anchor(a):
    pr = f', printed "{a["printed"]}"' if a['printed'] else ''
    nip = ' [not in pdf]' if a['not_in_pdf'] else ''
    return f'{a["key"]} p.{a["page"]}{pr}{nip}: "{a["quote"]}"'

def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument('query')
    ap.add_argument('--model', default='bge-m3')
    ap.add_argument('--mode', default='mix+p')
    ap.add_argument('--target', type=int, default=1200)
    ap.add_argument('-n', type=int, default=10)
    ap.add_argument('--explain', action='store_true')
    a = ap.parse_args()
    ix = Index(a.target)
    order, sig = ix.rank(a.query, a.model, a.mode)
    for r, i in enumerate(order[:a.n], 1):
        p = ix.ps[i]
        an = anchor(p, a.query)
        print(f'{r:>2}. {fmt_anchor(an)}')
        print(f'    {p["section"]} · {" › ".join(p["path"][1:])[-90:]}')
        if a.explain:
            print(f'    base {sig["base"][i]:.4f} lex {sig["lex"][i]:.2f} sem {sig["sem"][i] if sig["sem"] is not None else 0:.3f} '
                  f'defs {sig["defs"][i]:.2f} ' + '; '.join(f'{d["kind"]}:{d["term"]}' for d in p['defs'][:3]))

if __name__ == '__main__':
    main()
