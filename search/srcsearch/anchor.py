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


def fmt(a):
    pr = f', printed "{a["printed"]}"' if a.get('printed') else ''
    flags = []
    if a.get('not_in_pdf'):
        flags.append('not in the PDF')
    if a.get('check_pdf'):
        flags.append('check the page against the PDF')
    if a.get('unique_on_page') is False:
        flags.append('quote occurs more than once on the page')
    if a.get('verified'):
        flags.append(a['verified'])
    return f'{a["key"]} p.{a["page"]}{pr}: "{a["quote"]}"' + (f'  [{"; ".join(flags)}]' if flags else '')
