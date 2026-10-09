"""The literal matcher behind the concordance verbs (search/DESIGN.md §7.1).

One matcher, at four strictnesses. Each verb is a "mode" here:
- bytes:  the query's characters exactly, spaces included, case included;
- phrase: the query's words in order and adjacent, as whole words exactly as typed;
          any run of non-alphanumerics between them ("loss-of-control", a line break);
- words:  each word exactly as typed, as a whole word, counted on its own;
- loose:  the query's words in order anywhere within one passage, each with a left
          word boundary and a right side that may run on (below).

Case, in every mode but bytes (Joseph's convention, 2026-10-09): a lowercase letter
matches either case, and an uppercase letter only itself. 'ai' finds "AI" and "ai";
'AI' finds only "AI". It is letter by letter, unlike rg's smart-case.

A '*' at either end of a word removes the boundary on that side: 'hazard*' finds
every longer word, '*hazard' finds "infohazard".

The right side of a loose word (§7.1): one of its spelling variants, then up to four
more letters, then a plural or possessive ending that doesn't count toward the four.
- a final e may drop before i or e: 'use' finds "using", not "us" or "usual";
- a final y after a consonant may become ie: 'policy' finds "policies", not "police";
- the cap is Joseph's (2026-10-09), counted from the end of the full word: it keeps
  "assessments" and drops "policymakers" and "definition";
- a word typed with a trailing '*' keeps the spelling variants and has no cap;
- function words ('of', 'the', 'to' …) stay whole words, so 'loss of control'
  doesn't match "loss often … control".

Patterns are Python regexes over indexed text (text.clean). `prefilter` gives a
case-insensitive Postgres pattern that every match also matches, to narrow the
passages before the exact match runs in Python.
"""
import re

MODES = ('bytes', 'phrase', 'words', 'loose')
# Two more, used inside the tool: 'loose-phrase', the words adjacent as in a phrase
# but each with a loose word's right side (semantic --without-phrase); and
# 'words-loose', each word on its own with a loose right side (what exact-words
# reports a looser search would add).
LOOSER = dict(bytes='phrase', phrase='loose', words='words-loose')   # the next rung up, for "would add"
WORD_MODE = dict(bytes=None, phrase='phrase', words='phrase', loose='loose')
WORD_MODE.update({'loose-phrase': 'loose', 'words-loose': 'loose'})
CAP = 4
WORD_CH = r'[^\W_]'                 # a letter or digit
NOT_WORD = r'[\W_]'
SEP = r'[\W_]+'                     # between the words of a phrase
GAP = r'[\s\S]*?'                   # between the words of a loose match, within one passage
POSSESSIVE = r"(?:'s|s'|s)?"
# In a loose match these stay whole words: 'of' would otherwise find "often" and
# "offer" inside 'loss of control'. Acronyms ('AI') aren't among them, so they keep
# their plurals.
FUNCTION_WORDS = set('a an and are as at be by for from has have in is it its of on or that the this to was were '
                     'will with which not no nor'.split())


class Term:
    """One word of a query: its letters, and whether a '*' opens either side."""
    __slots__ = ('core', 'open_left', 'open_right')

    def __init__(self, tok):
        self.open_left, self.open_right = tok.startswith('*'), tok.endswith('*') and len(tok) > 1
        self.core = tok.strip('*')

    def __repr__(self):
        return ('*' if self.open_left else '') + self.core + ('*' if self.open_right else '')


def terms(query, mode):
    """The query's words. A phrase's words are separated by anything that isn't a
    letter, digit, '*' or apostrophe, so 'loss-of-control' is three words."""
    toks = re.split(r"[^\w*']+|_", query)
    return [Term(t) for t in toks if t.strip("*'")]


def case(s):
    """Joseph's case rule as a regex: lowercase letters match either case."""
    out = []
    for c in s:
        u = c.upper()
        if c.islower() and len(u) == 1 and u != c:
            out.append(f'[{c}{u}]')
        else:
            out.append(re.escape(c))
    return ''.join(out)


def _ending(core):
    """The core's last letter, with its spelling variants (§7.1): (stem regex)."""
    if len(core) > 2 and core[-1] in 'eE':
        e, ie = ('[eE]', '[iIeE]') if core[-1] == 'e' else ('E', '[IE]')
        return case(core[:-1]) + f'(?:{e}|(?={ie}))'
    if len(core) > 2 and core[-1] in 'yY' and core[-2].lower() not in 'aeiouy' and core[-2].isalpha():
        alt = '(?:[yY]|[iI][eE])' if core[-1] == 'y' else '(?:Y|IE)'
        return case(core[:-1]) + alt
    return case(core)


def word_rx(t, mode):
    """A regex for one word."""
    left = WORD_CH + '*' if t.open_left else f'(?<!{WORD_CH})'
    if mode == 'loose' and not (t.core.lower() in FUNCTION_WORDS and not t.open_right):
        if t.open_right:
            body = _ending(t.core) + WORD_CH + '*'
        else:
            body = _ending(t.core) + r'[^\W\d_]{0,%d}' % CAP + POSSESSIVE
        return left + body + f'(?!{WORD_CH})'
    right = WORD_CH + '*' if t.open_right else f'(?!{WORD_CH})'
    return left + case(t.core) + right


def pattern(query, mode):
    """The query as a compiled regex, by mode. For 'words', an alternation whose
    group n is the query's word n."""
    if mode == 'bytes':
        return re.compile(re.escape(query))
    ts = terms(query, mode)
    if not ts:
        raise ValueError(f'no words in {query!r}')
    wm = WORD_MODE[mode]
    if mode in ('words', 'words-loose'):
        return re.compile('|'.join(f'({word_rx(t, wm)})' for t in ts))
    joiner = GAP if mode == 'loose' else SEP
    return re.compile(joiner.join(word_rx(t, wm) for t in ts))


def loose_spans(rx, s, first):
    """The loose matches in s: for each place the first word matches, the shortest
    span completing the query from there; then, of spans sharing an end, the
    shortest; then no two overlapping (DESIGN §7.1: "the shortest span from a
    starting word, so overlapping spans aren't counted twice")."""
    best = {}
    for m in first.finditer(s):
        mm = rx.match(s, m.start())
        if mm and (mm.end() not in best or mm.start() > best[mm.end()][0]):
            best[mm.end()] = (mm.start(), mm.end())
    out, last = [], -1
    for a, b in sorted(best.values()):
        if a >= last:
            out.append((a, b))
            last = b
    return out


def finditer(query, mode, s, _cache={}):
    """[(start, end)] of the matches of query in s."""
    k = (query, mode)
    if k not in _cache:
        rx = pattern(query, mode)
        first = re.compile(word_rx(terms(query, mode)[0], 'loose')) if mode == 'loose' else None
        _cache[k] = (rx, first)
    rx, first = _cache[k]
    if mode == 'loose' and len(terms(query, mode)) > 1:
        return loose_spans(rx, s, first)
    return [m.span() for m in rx.finditer(s)]


def prefilter(query, mode):
    """Postgres patterns (for ~*) that a passage holding a match must all match:
    each word's letters, minus a final e or y the spelling rules may change."""
    if mode == 'bytes':
        return [re.sub(r'([\\.^$|?*+()\[\]{}])', r'\\\1', query)]
    out = []
    for t in terms(query, mode):
        c = t.core[:-1] if WORD_MODE[mode] == 'loose' and len(t.core) > 2 and t.core[-1] in 'eEyY' else t.core
        out.append(re.sub(r'([\\.^$|?*+()\[\]{}])', r'\\\1', c))
    if mode in ('words', 'words-loose'):          # any of the words, not all
        return ['(' + '|'.join(out) + ')']
    return out


def form(s, mode, keep_case=False):
    """How a match is counted in the forms (or spans) table: its words, one space
    between them, lowercased unless the query has a capital (then 'AI' keeps "AISI"
    apart from "aisi"). bytes keeps its characters."""
    if mode == 'bytes':
        return s
    ws = re.findall(r"[^\W_]+(?:'[^\W_]+)*", s)
    return ' '.join(ws if keep_case else (w.lower() for w in ws))


def widen(query, mode):
    """The looser search to report against: the next rung up, or, at the top, a '*'
    on each bounded side. (mode, query)."""
    if mode in LOOSER:
        return LOOSER[mode], query
    ts = terms(query, mode)
    q = ' '.join(('*' + t.core + '*') for t in ts)
    return 'loose', q


def gap_words(span_text, n_terms):
    return max(0, len(re.findall(r"[^\W_]+", span_text)) - n_terms)
