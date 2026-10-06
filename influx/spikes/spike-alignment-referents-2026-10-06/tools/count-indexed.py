"""Count bare vs. indexed uses of aligned / alignment / misaligned / misalignment.

"Indexed" = followed immediately (whitespace-normalised) by with / to / between,
or "of X with/to". Everything else is "bare", which includes activity senses
("alignment training"), reference-list titles, uses whose referent was fixed
earlier in the document, and complements placed elsewhere ("against the intent
of …"). So "bare" over-counts unindexed uses; treat the ratio as a rough
indicator only.

Usage: python3 -I count-indexed.py DIR   (DIR holds bin/extract-text outputs)
"""
import collections, glob, os, re, sys

d = sys.argv[1]
tot = collections.Counter()
pat = re.compile(r"\b(mis)?align(ed|ment)\b(.{0,60})", re.I | re.S)
for f in glob.glob(os.path.join(d, "*.txt")):
    t = re.sub(r"\s+", " ", open(f, errors="ignore").read())
    for m in pat.finditer(t):
        word = ("mis" if m.group(1) else "") + "align" + m.group(2).lower()
        rel = re.match(r"\s*(with|to|between|of [a-z]+ (with|to))\b", m.group(3), re.I)
        tot[(word, "indexed" if rel else "bare")] += 1
for (w, k), v in sorted(tot.items()):
    print(f"{w:14} {k:8} {v}")
