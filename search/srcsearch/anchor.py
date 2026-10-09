"""Anchors: relata key, physical PDF page, printed page, and an exact quote (plan §3.5).

Every result carries one. Joseph, 2026-10-09: "the search results should always
come back with your preferred reference format -- key + pdf-page etc. etc." A
quote taken from a result can be cited as it stands and checked with
`bin/check-quote --batch`.

What the pilot learned building them (REPORT §7), and how this follows it:
- quotes are taken from indexed text (text.clean), so they hold no link targets
  or tooltips (IASR's tooltips hold whole references, which check-quote then finds
  on the endnote pages), and they are in check-quote's normalisation: no tags,
  table pipes or emphasis;
- the page is the quoted sentence's, not the passage's start (350 of the pilot's
  3,714 passages span pages, and 7 run backwards), found exactly through the
  offset map;
- a quote is widened until it is unique on its page, where check-quote counts it
  (an NRR boilerplate sentence recurs on 20 pages);
- for a source whose fidelity record says to check the PDF (check-all, or one of
  its pages_to_check), the anchor says so: bin/check-quote settles the page there.
"""
import bisect, re

from . import CANON
from .chunk import Pages
from .text import clean, fold, sentences, words

MAX_QUOTE = 240
# What bin/check-quote reads as a gap in a quote ("…", "...", "[the developer]"). A
# quote holding one from the source itself (SaferAI quotes OpenAI with "[. . . ]")
# would be matched in pieces, so quotes stay clear of them.
GAP_RE = re.compile(r'…|\.\s?\.\s?\.|\[[^\]]*\]')


def _clip_gaps(s, a, b, keep):
    """[a, b) narrowed to the stretch between gap markers that holds position keep
    (or the longest stretch, if keep falls in a marker)."""
    cuts = [(m.start() + a, m.end() + a) for m in GAP_RE.finditer(s[a:b])]
    if not cuts:
        return a, b
    spans, x = [], a
    for c0, c1 in cuts:
        spans.append((x, c0))
        x = c1
    spans.append((x, b))
    hit = [sp for sp in spans if sp[0] <= keep < sp[1]]
    return hit[0] if hit else max(spans, key=lambda sp: sp[1] - sp[0])
_RAW, _PAGES = {}, {}


def raw_of(key):
    if key not in _RAW:
        _RAW[key] = open(f'{CANON}/{key}.md', encoding='utf-8').read()
        _PAGES[key] = Pages(_RAW[key])
    return _RAW[key]


def pages_of(key):
    raw_of(key)
    return _PAGES[key]


_PIPE = re.compile(r'\s*\|\s*')
_LEAD = re.compile(r'^[\s|]+')


def _indexed(key, start, end):
    m = clean(raw_of(key), start, end, refs=True)
    m = m.sub(_PIPE, lambda _: ' ')
    return m


def _page_bounds(key, off):
    pg = pages_of(key)
    k = bisect.bisect_right(pg.offs, off) - 1
    a = pg.offs[k] if k >= 0 else 0
    b = pg.offs[k + 1] if k + 1 < len(pg.offs) else len(raw_of(key))
    return a, b


def _letters(s):
    return ''.join(c for c in fold(s) if c.isalnum())


def _count_on_page(key, off, quote):
    """How often the quote occurs on its page, matched as bin/check-quote matches:
    letters and digits only, run together, so word boundaries don't count. SB 53's
    '(e) "Frontier developer" has the meaning …' also matches inside '(f) "Large
    frontier developer" has the meaning …' (largE-FRONTIER…)."""
    a, b = _page_bounds(key, off)
    needle = _letters(quote)
    if not needle:
        return 0
    hay, n, i = _letters(_indexed(key, a, b).s), 0, -1
    while True:
        i = hay.find(needle, i + 1)
        if i == -1:
            return n
        n += 1


def make(key, start, end, qwords=(), at=None, fidelity=None, pages_to_check=()):
    """An anchor for the passage at raw[start:end]: a quote of the first sentence
    holding a query word (or the sentence at offset `at`, for a definition), cut
    around the word if long, widened until unique on its page."""
    # the text runs on past the passage, to its page's end, so a quote can widen into
    # the next passage (a one-line definition that recurs nearly verbatim needs it)
    ext = max(end, min(_page_bounds(key, max(start, end - 1))[1], end + 1500))
    m = _indexed(key, start, ext)
    ss_all = [(a, b) for a, b in sentences(m.s) if len(words(m.s[a:b])) >= 3] or [(0, len(m.s))]
    ss = [x for x in ss_all if m.pos[x[0]] < end] or ss_all[:1]
    qw = set(qwords)
    pick = None
    if at is not None:
        pick = next((i for i, (a, b) in enumerate(ss) if m.pos[min(b, len(m.pos)) - 1] >= at), None)
    if pick is None and qw:
        pick = next((i for i, (a, b) in enumerate(ss) if qw & set(words(m.s[a:b]))), None)
    if pick is None and qw:                     # a word form containing a query word ("infohazard")
        pick = next((i for i, (a, b) in enumerate(ss) if any(q in w for w in words(m.s[a:b]) for q in qw)), None)
    pick = pick or 0
    a, b = ss[pick]
    if b - a > MAX_QUOTE:                       # a long sentence: a window around the first query word
        seg = m.s[a:b]
        hit = None
        for q in qw:
            mm = re.search(r'\b' + re.escape(q), seg, re.I)
            if mm and (hit is None or mm.start() < hit):
                hit = mm.start()
        c = max(0, (hit or 0) - MAX_QUOTE // 3)
        if c:
            c = seg.find(' ', c) + 1 or c
        e = min(len(seg), c + MAX_QUOTE)
        if e < len(seg):
            e = seg.rfind(' ', c, e) if seg.rfind(' ', c, e) > c else e
        a, b = a + c, a + e
    hit = min((mm.start() for q in qw for mm in [re.search(r'\b' + re.escape(q), m.s[a:b], re.I)] if mm), default=None)
    a, b = _clip_gaps(m.s, a, b, a + hit if hit is not None else -1)
    # widen until unique on its page: the next sentence, then the one before
    i0 = i1 = pick
    for _ in range(4):
        q = m.s[a:b]
        if _count_on_page(key, m.pos[a], q) <= 1:
            break
        if i1 + 1 < len(ss_all) and not GAP_RE.search(m.s[b:ss_all[i1 + 1][1]]):
            i1 += 1
            b = ss_all[i1][1]
        elif i0 > 0 and not GAP_RE.search(m.s[ss_all[i0 - 1][0]:a]):
            i0 -= 1
            a = ss_all[i0][0]
        else:
            break
    quote = ' '.join(m.s[a:b].split())
    quote = _LEAD.sub('', quote)
    raw_off = m.pos[a] if a < len(m.pos) else start
    page, printed, nip = pages_of(key).at(raw_off)
    check = fidelity == 'check-all' or (page in (pages_to_check or ()))
    unique = _count_on_page(key, raw_off, quote) <= 1
    return dict(key=key, page=page, printed=printed, quote=quote, not_in_pdf=nip,
                check_pdf=bool(check), unique_on_page=unique, offset=raw_off)


OPEN, CLOSE = '«⟨', '⟩»'
# A verbatim quote is shown between these in text output (Joseph, 2026-10-09: "«⟨   ⟩»
# let's do this- a little clunky maybe but looks great in the terminal (fwiw) and no
# ambiguity or confusion"). The pair occurs in none of the canonical texts, so a quote
# can hold any quotation marks of its own. JSON keeps the quote as a plain string.


def show_quote(q):
    return f'{OPEN}{q}{CLOSE}'


def fmt(a):
    pr = f', printed "{a["printed"]}"' if a.get('printed') else ''
    flags = []
    if a.get('page_label'):
        flags.append(a['page_label'])
    elif a.get('not_in_pdf'):
        flags.append('not in the PDF')
    elif a.get('check_pdf'):
        flags.append('page not yet confirmed')
    if a.get('unique_on_page') is False and not (a.get('page_check') or {}).get('status') == 'ambiguous':
        flags.append('quote occurs more than once on the page')
    return f'{a["key"]} p.{a["page"]}{pr}: {show_quote(a["quote"])}' + (f'  [{"; ".join(flags)}]' if flags else '')


# ------------------------------------------------------------- settling pages
# An anchor's page comes from the canonical text's page markers. Where the source's
# fidelity record says not to trust them there (check-all, or one of its
# pages_to_check), bin/check-quote settles the page against the PDF's own text
# (DESIGN §5.1). It runs once per anchor: its verdict is cached in
# cache.quote_checks, keyed by the canonical text's and the checker's sha256 (see
# search/cache.sql). The reader then gets the settled page, and a label only where
# the page truly can't be confirmed, never an instruction to go and read the PDF.
LABELS = {
    'ok': None,
    'unconfirmed': 'page not confirmed against the PDF',
    'not-in-pdf': 'not in the PDF: from the web edition only',
    'ambiguous': 'quote occurs more than once on the page',
    'page-mismatch': 'page not confirmed',
    'near-miss': 'quote not confirmed',
    'not-found': 'quote not confirmed',
    'no-text': 'page not confirmed',
}
_CANON_SHA, _CHECKER_SHA = {}, []


def _canon_sha(key):
    if key not in _CANON_SHA:
        import hashlib
        _CANON_SHA[key] = hashlib.sha256(raw_of(key).encode('utf-8')).hexdigest()
    return _CANON_SHA[key]


def _checker_sha():
    if not _CHECKER_SHA:
        import hashlib
        from . import REPO
        h = hashlib.sha256()
        for f in ('check-quote', 'canonicalize'):
            h.update(open(f'{REPO}/bin/{f}', 'rb').read())
        _CHECKER_SHA.append(h.hexdigest())
    return _CHECKER_SHA[0]


def needs_check(a):
    return bool(a.get('check_pdf') or a.get('not_in_pdf'))


def _apply(a, rec):
    status = rec.get('status')
    a['page_check'] = dict(status=status, page_from=rec.get('page_from'), cited=a['page'])
    if rec.get('page') is not None and status in ('ok', 'unconfirmed', 'ambiguous'):
        a['page'] = rec['page']
        if rec.get('printed'):
            a['printed'] = rec['printed']
    a['check_pdf'] = False
    a['page_label'] = LABELS.get(status, f'check-quote: {status}')
    if status == 'not-in-pdf':
        a['not_in_pdf'] = True


def settle(conn, anchors, every=False):
    """Settle the page of each anchor that needs the PDF (or of every anchor, with
    every=True: --verify), from the cache or by one run of bin/check-quote over all
    the misses. Returns how many were checked afresh."""
    import hashlib, json, os, subprocess, sys
    from . import REPO, db
    todo = [a for a in anchors if every or needs_check(a)]
    if not todo:
        return 0
    if not getattr(settle, '_ready', False):
        db.ensure_cache(conn)
        settle._ready = True
    ck = _checker_sha()
    keyed = [(a, a['key'], hashlib.sha256(a['quote'].encode('utf-8')).hexdigest(), int(a['page']), _canon_sha(a['key']))
             for a in todo]
    have = {}
    for k in {x[1] for x in keyed}:
        rows = conn.execute(
            """select quote_sha, page_cited, record from cache.quote_checks
               where doc_key = %s and canon_sha = %s and checker_sha = %s and quote_sha = any(%s)""",
            (k, _canon_sha(k), ck, [x[2] for x in keyed if x[1] == k])).fetchall()
        for qs, pc, rec in rows:
            have[(k, qs, pc)] = rec
    miss, seen = [], set()
    for a, k, qs, pc, cs in keyed:
        rec = have.get((k, qs, pc))
        if rec is not None:
            _apply(a, rec)
        elif (k, qs, pc) not in seen:
            seen.add((k, qs, pc))
            miss.append((k, qs, pc, cs, a['quote']))
    if miss:
        batch = [dict(id=str(i), key=k, anchors=[dict(quote=q, page=pc)]) for i, (k, qs, pc, cs, q) in enumerate(miss)]
        out = subprocess.run([os.path.join(REPO, 'bin', 'check-quote'), '--batch', '-', '--jsonl'],
                             input='\n'.join(json.dumps(b) for b in batch), capture_output=True, text=True)
        recs = [json.loads(l) for l in out.stdout.splitlines() if l.strip()]
        if out.returncode == 2 or len(recs) != len(miss):
            print(f'bin/check-quote failed: {out.stderr.strip()[:300]}', file=sys.stderr)
        got = {}
        with conn.transaction():
            for r in recs:
                k, qs, pc, cs, q = miss[int(r['id'])]
                x = (r.get('anchors') or [{}])[0]
                got[(k, qs, pc)] = x
                conn.execute(
                    """insert into cache.quote_checks (doc_key, quote_sha, page_cited, canon_sha, checker_sha, quote,
                                                       status, page, page_from, printed, record)
                       values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) on conflict do nothing""",
                    (k, qs, pc, cs, ck, q, x.get('status') or 'unknown', x.get('page'), x.get('page_from'),
                     x.get('printed'), json.dumps(x)))
        for a, k, qs, pc, cs in keyed:
            if (k, qs, pc) in got:
                _apply(a, got[(k, qs, pc)])
    return len(miss)
