"""Cleaning a canonical text for indexing, without losing where each character came from.

The index searches *indexed text*: the canonical text without image links, link
targets and their tooltips, HTML tags and markdown emphasis (DESIGN §5.2). IASR
2026's web edition repeats each footnote's whole reference in a link tooltip, so
indexing the raw text would match reference lists inside body paragraphs.

Results, though, quote and page the canonical text's own characters. So cleaning
keeps a map: `Mapped.pos[i]` is the offset in the canonical file of indexed
character i. A sentence found in indexed text maps back to an exact span of the
file, so its page comes from the file's markers and `bin/check-quote` can confirm
it. The pilot cut long blocks without this map and had to locate the pieces by
their first words (influx/search-pilot-2026-10-09/chunk.py, `_split_piece`).
"""
import html, re, unicodedata


class Mapped:
    """A string, and for each of its characters the offset it came from."""
    __slots__ = ('s', 'pos')

    def __init__(self, s, pos):
        self.s, self.pos = s, pos

    @classmethod
    def of(cls, raw, start=0, end=None):
        end = len(raw) if end is None else end
        return cls(raw[start:end], list(range(start, end)))

    def __len__(self):
        return len(self.s)

    def sub(self, rx, repl):
        """Like rx.sub over self.s. repl(m) returns a str, whose characters all map
        to the match's start, or a tuple of group numbers, whose text is kept with
        its own offsets (a link keeps its text and drops its target)."""
        s, P = self.s, self.pos
        out, pos, last = [], [], 0
        for m in rx.finditer(s):
            a, b = m.span()
            out.append(s[last:a]); pos.extend(P[last:a])
            r = repl(m)
            if isinstance(r, str):
                anchor = P[a] if a < len(P) else (P[-1] + 1 if P else 0)
                out.append(r); pos.extend([anchor] * len(r))
            else:
                for g in r:
                    if m.group(g) is None:
                        continue
                    ga, gb = m.span(g)
                    out.append(s[ga:gb]); pos.extend(P[ga:gb])
            last = b
        out.append(s[last:]); pos.extend(P[last:])
        return Mapped(''.join(out), pos)

    def slice(self, a, b):
        return Mapped(self.s[a:b], self.pos[a:b])

    def strip(self):
        a, b = 0, len(self.s)
        while a < b and self.s[a].isspace():
            a += 1
        while b > a and self.s[b - 1].isspace():
            b -= 1
        return self.slice(a, b)

    def span(self, a=0, b=None):
        """The canonical file's [start, end) for indexed characters [a, b)."""
        b = len(self.s) if b is None else b
        if b <= a:
            p = self.pos[a] if a < len(self.pos) else (self.pos[-1] + 1 if self.pos else 0)
            return p, p
        return self.pos[a], self.pos[b - 1] + 1


# -------------------------------------------------------------------- cleaning
# A link target: a URL (balanced parentheses allowed) and an optional quoted
# title, as in bin/canonicalize, whose older pattern let titles with nested
# parentheses through (fixed 2026-10-09, 2962ae3).
URL = (r'(?:\((?:[^()\n\s]|\([^()\n\s]*\))*\s+"[^"\n]*"\)'
       r'|\((?:[^()\n]|\([^()\n]*\))*\))')
COMMENT_RE = re.compile(r'<!--.*?-->', re.S)
MARK_LINE_RE = re.compile(r'^----------\[(?:pdf-page \d+(?:, printed "[^"\n]*")?|not in pdf)\]----------$', re.M)  # corpus.MARK_RE's lines
IMG_RE = re.compile(r'!\[[^\]\n]*\]' + URL)
LINK_RE = re.compile(r'\[((?:[^\[\]\n]|\[[^\[\]\n]*\])*)\]' + URL)
CITE_TEXT_RE = re.compile(r'[\d,\s–\-\\()\[\]]*')          # [34)] and the like: a citation number
AUTOLINK_RE = re.compile(r'<(?:https?://|www\.|mailto:)[^>\s]*>')
BARE_URL_RE = re.compile(r'\b(?:https?://|www\.)[^\s<>()\[\]]*[^\s<>()\[\].,;:!?\'"”’]')
BR_RE = re.compile(r'<br\s*/?>', re.I)
SUP_NUM_RE = re.compile(r'<sup>[\s\d,–\-*†‡]*</sup>', re.I)
TAG_RE = re.compile(r'</?[A-Za-z][^>\n]{0,300}>')
ENTITY_RE = re.compile(r'&(?:#\d{1,6}|#x[0-9A-Fa-f]{1,6}|[A-Za-z]{2,8});')
ESCAPE_RE = re.compile(r'\\([\\`*_{}\[\]()#+\-.!$|<>~"\'])')
STRONG_RE = re.compile(r'\*\*|(?<![\w_])__|__(?![\w_])')
EM_RE = re.compile(r'(?<![\w*])\*(?=\S)([^*\n]+?)(?<=\S)\*(?![\w*])')
RULE_ROW_RE = re.compile(r'^[ \t]*\|?[ \t]*:?-{3,}:?[ \t]*(?:\|[ \t]*:?-{3,}:?[ \t]*)*\|?[ \t]*$', re.M)
BULLET_RE = re.compile(r'^[ \t]*[-*+•][ \t]+', re.M)
LEADER_RE = re.compile(r'[\ufffd.·…_]{4,}')        # a contents page's dot leaders (IASR's came through as U+FFFD)
SPACES_RE = re.compile(r'[ \t  -​ ]+')
LINE_EDGE_RE = re.compile(r' ?\n ?')
BLANKS_RE = re.compile(r'\n{3,}')


def clean(raw, start=0, end=None, emphasis=False, refs=False):
    """Indexed text of raw[start:end], as a Mapped. With emphasis=True, markdown
    bold and italics are kept: definition detection reads `**Term:**` and `*term*`.
    With refs=True, footnote markers and citation link texts are kept ("including<sup>7</sup>
    the" gives "including7 the"; "[2024\\)](#page-63-7)" gives "2024)"): they aren't
    words for ranking, but they are in the text a quote must match (bin/check-quote
    matches letters and digits, so "including the" is a near miss)."""
    m = Mapped.of(raw, start, end)
    m = m.sub(COMMENT_RE, lambda _: ' ')
    m = m.sub(MARK_LINE_RE, lambda _: ' ')
    m = m.sub(IMG_RE, lambda _: ' ')
    m = m.sub(LINK_RE, lambda x: ' ' if CITE_TEXT_RE.fullmatch(x.group(1)) and not refs else (1,))
    m = m.sub(AUTOLINK_RE, lambda _: ' ')
    m = m.sub(BARE_URL_RE, lambda _: ' ')
    m = m.sub(BR_RE, lambda _: ' ')
    if not refs:
        m = m.sub(SUP_NUM_RE, lambda _: ' ')
    m = m.sub(TAG_RE, lambda _: '')
    m = m.sub(ENTITY_RE, lambda x: html.unescape(x.group(0)))
    m = m.sub(ESCAPE_RE, lambda _: (1,))
    if not emphasis:
        m = m.sub(STRONG_RE, lambda _: '')
        m = m.sub(EM_RE, lambda _: (1,))
    m = m.sub(RULE_ROW_RE, lambda _: '')
    m = m.sub(BULLET_RE, lambda _: '')
    m = m.sub(LEADER_RE, lambda _: ' ')
    m = m.sub(SPACES_RE, lambda _: ' ')
    m = m.sub(LINE_EDGE_RE, lambda _: '\n')
    m = m.sub(BLANKS_RE, lambda _: '\n\n')
    return m.strip()


def clean_heading(raw):
    return ' '.join(clean(raw).s.split()).strip(' :')


# ------------------------------------------------------------------- sentences
_ABBREV = re.compile(r'(?:\b(?:e\.g|i\.e|etc|cf|vs|al|Art|Arts|No|Nos|Fig|Figs|Sec|Secs|para|paras|Ch|Vol|pp|p|ed|eds|Dr|Mr|Ms|Mrs|St|Inc|Ltd|Co|Corp|Jr|Sr|approx|incl|resp|U\.S|U\.K|E\.U)|\b[A-Z])\.$')
_BOUNDARY = re.compile(r'(?<=[.;!?])(["”’)\]]*)\s+(?=[A-Z0-9(“"‘\'•\-–])|\n+')


def sentences(text):
    """[(start, end)] of the sentences in text, by punctuation and line breaks.
    A period after a common abbreviation or an initial doesn't end one."""
    out, a = [], 0
    for m in _BOUNDARY.finditer(text):
        b = m.start() + len(m.group(1) or '')      # a closing quote or bracket stays with its sentence
        if m.group(0)[0] != '\n' and text[m.start() - 1] == '.' and _ABBREV.search(text[max(a, m.start() - 12):m.start()]):
            continue
        if text[a:b].strip():
            out.append((a, b))
        a = m.end()
    if text[a:].strip():
        out.append((a, len(text)))
    return out


# --------------------------------------------------------------- normalising
def fold(s):
    """Casefolded, unaccented, with typographic dashes and quotes made plain."""
    s = unicodedata.normalize('NFKD', s)
    s = ''.join(c for c in s if not unicodedata.combining(c))
    s = s.casefold()
    return (s.replace('‐', '-').replace('‑', '-').replace('–', '-').replace('—', '-')
             .replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"'))


WORD_RE = re.compile(r'[^\W_]+(?:[-\'][^\W_]+)*')


def words(s):
    """Word tokens of folded text; hyphenated and apostrophe'd words stay whole."""
    return WORD_RE.findall(fold(s))


def norm_term(t):
    """A defined term's normal form: folded, without quotes, emphasis or a
    parenthetical abbreviation ("Floating point operations (FLOP)"), its last word
    singular. Two definitions of the same term normalise alike."""
    t = fold(clean(t).s)
    t = re.sub(r'[\'"*_`]', '', t)
    t = re.sub(r'\([^)]*\)', ' ', t)
    t = re.sub(r'[^\w\s-]', ' ', t)
    ws = t.split()
    if ws:
        w = ws[-1]
        if len(w) > 3 and w.endswith('ies') and not w.endswith(('eies', 'aies')):
            ws[-1] = w[:-3] + 'y'
        elif len(w) > 3 and w.endswith('s') and not w.endswith(('ss', 'us', 'is', 'ics')):
            ws[-1] = w[:-1]
    return ' '.join(ws)


def norm_passage(s):
    """For duplicate detection: letters and digits only, folded. Two passages
    that differ only in markup, spacing or punctuation hash alike."""
    return ' '.join(words(s))
