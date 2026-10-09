"""The concordance verbs: lexical, exact-phrase, exact-words, exact-bytes (DESIGN §7).

Every match of the query in the indexed text of the passages (and headings) in
scope, found by match.py, located by its offset in the canonical text, counted by
form, and ordered by proximity.

Passages overlap by a sentence, so a match is identified by where it starts in the
canonical file and counted once.

Ordering (§7.1, Joseph 2026-10-09: "say 'within chunk' but use our earlier logic for
ranking -- including proximity etc."): tightest first. A match's proximity uses
memorata's weights (`memorata3/search.py` proximity_score): 1 − 0.03 per word
between the query's words − 0.25 per sentence boundary − 0.6 per paragraph boundary,
floored at 0. Every match is in the query's order, so its order factor is 1. Ties go
to the document with more matches, then to body text over references, then to
position. This is the in-order core of proximity; porting memorata's whole
proximity and density into hybrid's ranking is §11 step 5.
"""
import re

from . import anchor, match
from .text import clean, sentences

INFLUENCE_RANK = dict(anchor=0, major=1, supporting=2, context=3, corpus=4)


def proximity(span_text, n_terms):
    if n_terms < 2:
        return 1.0
    gap = match.gap_words(span_text, n_terms)
    paras = span_text.count('\n\n')
    sents = max(0, len(sentences(span_text)) - 1)
    return round(max(0.0, 1 - 0.03 * gap - 0.25 * sents - 0.6 * paras), 4)


def _candidates(conn, query, mode, keys):
    pats = match.prefilter(query, mode)
    where = ' and '.join(['p.text ~* %s'] * len(pats))
    return conn.execute(
        f"""select p.id, p.doc_key, p.section, p.start_off, p.end_off from src.passages p
            where p.layer = 'canonical' and {where} and (%s::text[] is null or p.doc_key = any(%s))
            order by p.doc_key, p.start_off""", (*pats, keys, keys)).fetchall()


def _heading_candidates(conn, query, mode, keys):
    pats = match.prefilter(query, mode)
    where = ' and '.join(["(h.text || ' ' || coalesce(h.title, '')) ~* %s"] * len(pats))
    return conn.execute(
        f"""select h.doc_key, h.start_off, h.text, h.title, h.page, h.printed from src.headings h
            where {where} and (%s::text[] is null or h.doc_key = any(%s))
            order by h.doc_key, h.start_off""", (*pats, keys, keys)).fetchall()


def find(conn, query, mode, keys=None):
    """(occurrences, heading hits). An occurrence: key, section, text, form, the
    query word it matched (exact-words), its offsets in the canonical file, its
    passage's span, and its proximity."""
    n_terms = len(match.terms(query, mode)) if mode != 'bytes' else 1
    kc = query != query.lower()
    rx_words = match.pattern(query, mode) if mode in ('words', 'words-loose') else None
    seen, occ = set(), []
    for _pid, key, section, start, end in _candidates(conn, query, mode, keys):
        m = clean(anchor.raw_of(key), start, end)
        for a, b in match.finditer(query, mode, m.s):
            off = m.pos[a]
            if (key, off) in seen:
                continue
            seen.add((key, off))
            text = m.s[a:b]
            o = dict(key=key, section=section, text=text, form=match.form(text, mode, kc), offset=off,
                     end_offset=m.pos[b - 1] + 1, start=start, end=end, proximity=proximity(text, n_terms))
            if rx_words:
                mm = rx_words.fullmatch(text)
                o['word'] = next((match.terms(query, mode)[i].core for i, g in enumerate(mm.groups()) if g), None) if mm else None
            occ.append(o)
    heads = []
    for key, start, text, title, page, printed in _heading_candidates(conn, query, mode, keys):
        s = text + (' ' + title if title else '')
        for a, b in match.finditer(query, mode, s):
            heads.append(dict(key=key, form=match.form(s[a:b], mode, kc), text=s[a:b], page=page, printed=printed,
                              heading=text, offset=start, at=a))
    return occ, heads


def counts(occ, heads):
    """{form: [body, references, headings]}, and {key: dict(body, references, headings)}."""
    forms, docs = {}, {}
    for o in occ:
        part = 1 if o['section'] == 'references' else 0
        forms.setdefault(o['form'], [0, 0, 0])[part] += 1
        docs.setdefault(o['key'], [0, 0, 0])[part] += 1
    for h in heads:
        forms.setdefault(h['form'], [0, 0, 0])[2] += 1
        docs.setdefault(h['key'], [0, 0, 0])[2] += 1
    return forms, docs


def order(occ, docs):
    return sorted(occ, key=lambda o: (-o['proximity'], o['section'] == 'references', -docs[o['key']][0],
                                      o['key'], o['offset']))


def not_counted(conn, query, mode, keys, occ, heads):
    """What the next looser search would add: its matches that start where none of
    this search's do, by form. dict(verb, mode, query, total, forms)."""
    wmode, wquery = match.widen(query, mode)
    if wmode == mode and wquery == query:
        return None
    w_occ, w_heads = find(conn, wquery, wmode, keys)
    have = {(o['key'], o['offset']) for o in occ}
    add = {}

    def tally(o):
        # what bytes missed is the case, or a line break or hyphen between the words: shown as it is
        f = re.sub(r'\s*\n\s*', '⏎', o['text']) if mode == 'bytes' else o['form']
        add[f] = add.get(f, 0) + 1
    for o in w_occ:
        if (o['key'], o['offset']) not in have:
            tally(o)
    have_h = {(h['key'], h['offset'], h['at']) for h in heads}
    for h in w_heads:
        if (h['key'], h['offset'], h['at']) not in have_h:
            tally(h)
    verb = {v: k for k, v in VERB_MODE.items()}.get(wmode, 'lexical, word by word' if wmode == 'words-loose' else wmode)
    return dict(verb=verb, mode=wmode, query=wquery, total=sum(add.values()),
                forms=dict(sorted(add.items(), key=lambda x: -x[1])))


VERB_MODE = {'lexical': 'loose', 'exact-phrase': 'phrase', 'exact-words': 'words', 'exact-bytes': 'bytes'}


def attach_anchors(occ, info):
    """Each occurrence's anchor: the sentence at its start, from anchor.make."""
    for o in occ:
        fid, ptc = info.get(o['key'], (None, None))
        qw = re.findall(r"[^\W_]+", o['form'].lower())[:1]
        o['anchor'] = anchor.make(o['key'], o['start'], o['end'], qw, at=o['offset'], fidelity=fid, pages_to_check=ptc)
