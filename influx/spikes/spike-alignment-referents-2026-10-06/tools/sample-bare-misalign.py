"""Draw the stratified sample in data/misalign-sample-50.txt.

Lines containing "misaligned"/"misalignment" NOT followed immediately by with/to,
excluding lines that look like references (arxiv/http/doi/"(20xx)"/"et al. 20xx"/
Proceedings/preprint). At most 2 per document, shuffled with seed 20261006, first 50.
Context = the line before, the line, the line after, whitespace-normalised.

Usage: cd DIR_OF_EXTRACTIONS && python3 -I sample-bare-misalign.py > out.txt
"""
import glob, random, re
random.seed(20261006)
items = []
for f in sorted(glob.glob("*.txt")):
    lines = open(f, errors="ignore").read().split("\n")
    for i, l in enumerate(lines):
        if re.search(r"\bmisalign(ed|ment)\b", l, re.I) and not re.search(
                r"arxiv|http|doi|\(20\d\d\)|et al\.,? \(?20|Proceedings|preprint", l, re.I):
            m = re.search(r"\bmisalign(ed|ment)\b(.{0,40})", l, re.I)
            if re.match(r"\s*(with|to)\b", m.group(2), re.I):
                continue
            ctx = " ".join(x.strip() for x in lines[max(0, i - 1):i + 2])
            items.append((f[:-4], i + 1, re.sub(r"\s+", " ", ctx)))
bydoc = {}
for it in items:
    bydoc.setdefault(it[0], []).append(it)
pool = []
for k, v in bydoc.items():
    random.shuffle(v)
    pool += v[:2]
random.shuffle(pool)
for n, (k, l, c) in enumerate(pool[:50], 1):
    print(f"{n}. {k} L{l}: {c[:420]}\n")
