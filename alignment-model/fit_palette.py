#!/usr/bin/env python3
"""Fit the colour families in palette.css (CIECAM02 / CAM02-UCS), and write them back.

    python3 fit_palette.py --dry-run          # print the token block + a summary, change nothing
    python3 fit_palette.py                    # rewrite the family tokens in palette.css
    python3 fit_palette.py --deeper 11 --red-trim 0.85 --rotate 5    # try variations
    python3 build.py --palette && python3 contrast.py                 # then look and measure

Standard library only (reuses the CIECAM02 model in contrast.py). With no options it
reproduces the current palette.

HOW EACH FAMILY IS BUILT (all distances are CAM02-UCS ΔE', measured from the paper colour
in palette.css, sRGB reference viewing conditions):

  deeper   A point at hue h with a fixed colourfulness M' (--m-deeper; × --red-trim for the
           --red families), darkened until it sits --deeper from the paper. Darkening is capped
           at --cap (ΔJ'): a family whose hue is close to the paper's own (≈ 120°) can only get
           far from the paper by getting darker, which turns yellow-greens olive and sands
           muddy; the cap keeps those pastel and lets them sit a little closer to the paper.
  deep     deeper moved --lift-deep of the way back toward the paper (default ⅓).
  normal   deeper moved --lift-normal of the way toward the paper (default ⅔).
           Moving by constant fractions makes every step the same size and keeps every
           family the same distance from the paper at each step; differences between
           families shrink by the same fractions.
  bd       Border: colourfulness --m-border (red-trimmed too), darkened to --border from the
           paper (no cap).
  edge     Line colour: fixed J' / M' (--edge J M) at the family's hue.
  ink      Accent text: fixed J' / M' (--ink J M) at the family's hue. M' 18 is about the most
           J' 36 allows before jade and teal leave the sRGB gamut (watch for the warning).

  stone is the neutral family: hue --stone-hue, colourfulness --stone-m, same targets but
  no darkening cap (lightness is all it has); its edge and ink are the fixed colours in
  --stone-edge / --stone-ink.

HUES (CIECAM02 h, one per chromatic family, in the order of NAMES below):
  --hues      nine angles (default: the current palette)
  --rotate    add this many degrees to all of them
  --even      replace them with nine equal steps of 40°, starting at the first hue
  Nine families on one hue circle can't be much more than ~40° apart; keeping them evenly
  spread is what keeps the closest pair of families as far apart as possible.

WHAT TO WATCH after changing anything:
  contrast.py's summary — normal/deep/deeper ↔ paper (the balance), the two steps, the
  smallest family ↔ family distance at each step, and WCAG. This script prints the same
  headline numbers, and warns if a colour falls outside the sRGB gamut (it gets clipped).
  Rough reading of ΔE': ~1 just noticeable side by side · 2–5 clearly visible · > 10 distinct.
  Reds (rose, clay, mauve) look more vivid than the model predicts (Helmholtz–Kohlrausch),
  which is what --red-trim compensates for.
"""
import argparse
import importlib.util
import itertools
import math
import re
import sys
sys.dont_write_bytecode = True   # keep the folder free of __pycache__
from pathlib import Path

HERE = Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location("contrast", HERE / "contrast.py")
cam = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(cam)

NAMES = ["rose", "clay", "sand", "sage", "jade", "teal", "slate", "iris", "mauve"]
HUES = [16, 55, 95, 136, 177, 217, 256, 296, 336]
ORDER = ["stone"] + NAMES
BEGIN = "  /* families: normal / deep / deeper fills, border, line, accent ink */"


# ------------------------------------------------------------------ inverse CIECAM02

def inv3(m):
    (a, b, c), (d, e, f), (g, h, i) = m
    det = a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)
    return [[(e * i - f * h) / det, (c * h - b * i) / det, (b * f - c * e) / det],
            [(f * g - d * i) / det, (a * i - c * g) / det, (c * d - a * f) / det],
            [(d * h - e * g) / det, (b * g - a * h) / det, (a * e - b * d) / det]]


MHPE_INV = inv3(cam.MHPE)
M02_INV = inv3(cam.M02)
XYZ_TO_RGB = inv3([[0.4124564, 0.3575761, 0.1804375],     # exact inverse of the
                   [0.2126729, 0.7151522, 0.0721750],     # sRGB matrix contrast.py
                   [0.0193339, 0.1191920, 0.9503041]])    # uses, so round trips agree


def ucs_to_hex(vc, Jp, ap, bp):
    """CAM02-UCS (J', a', b') -> '#RRGGBB', plus whether it was inside the sRGB gamut."""
    J = Jp / (1.7 - 0.007 * Jp)
    M = (math.exp(0.0228 * math.hypot(ap, bp)) - 1) / 0.0228
    h = math.atan2(bp, ap)
    C = M / vc.F_L ** 0.25
    t = (C / (math.sqrt(J / 100) * (1.64 - 0.29 ** vc.n) ** 0.73)) ** (1 / 0.9) if J > 0 else 0
    e_t = 0.25 * (math.cos(h + 2) + 3.8)
    A = vc.A_w * (J / 100) ** (1 / (vc.c * vc.z))
    p2 = A / vc.N_bb + 0.305
    p3 = 21 / 20
    if t == 0:
        a = b = 0.0
    else:
        p1 = (50000 / 13 * vc.N_c * vc.N_cb * e_t) / t
        s, co = math.sin(h), math.cos(h)
        if abs(s) >= abs(co):
            p4 = p1 / s
            b = p2 * (2 + p3) * (460 / 1403) / (p4 + (2 + p3) * (220 / 1403) * (co / s) - 27 / 1403 + p3 * (6300 / 1403))
            a = b * co / s
        else:
            p5 = p1 / co
            a = p2 * (2 + p3) * (460 / 1403) / (p5 + (2 + p3) * (220 / 1403) - (27 / 1403 - p3 * (6300 / 1403)) * (s / co))
            b = a * s / co
    Ra = 460 / 1403 * p2 + 451 / 1403 * a + 288 / 1403 * b
    Ga = 460 / 1403 * p2 - 891 / 1403 * a - 261 / 1403 * b
    Ba = 460 / 1403 * p2 - 220 / 1403 * a - 6300 / 1403 * b
    unc = lambda x: math.copysign(100 / vc.F_L * ((27.13 * abs(x - 0.1)) / (400 - abs(x - 0.1))) ** (1 / 0.42), x - 0.1)
    RGBc = cam.mul(cam.M02, cam.mul(MHPE_INV, [unc(Ra), unc(Ga), unc(Ba)]))
    RGB = [v / (cam.WHITE[1] * vc.D / w + 1 - vc.D) for v, w in zip(RGBc, vc.RGB_w)]
    XYZ = [x / 100 for x in cam.mul(M02_INV, RGB)]
    lin = cam.mul(XYZ_TO_RGB, XYZ)
    ok = all(-0.003 <= x <= 1.003 for x in lin)
    enc = lambda x: 12.92 * x if x <= 0.0031308 else 1.055 * x ** (1 / 2.4) - 0.055
    return "#%02X%02X%02X" % tuple(round(min(1, max(0, enc(x))) * 255) for x in lin), ok


# ------------------------------------------------------------------ construction

def point(Jp, m, h):
    r = math.radians(h)
    return (Jp, m * math.cos(r), m * math.sin(r))


def dist(p, q):
    return math.dist(p, q)


def darken_to(paper, m, h, target):
    """J' such that the point (J', m, h) sits `target` from the paper (bisection on darkening)."""
    lo, hi = 0.0, 60.0
    for _ in range(50):
        d = (lo + hi) / 2
        if dist(point(paper[0] - d, m, h), paper) < target:
            lo = d
        else:
            hi = d
    return paper[0] - d


def lift(p, paper, k):
    return tuple(x + (y - x) * k for x, y in zip(p, paper))


def family(vc, paper, h, m, mb, a, edge=None, ink=None, cap=True):
    Jd = darken_to(paper, m, h, a.deeper)
    if cap:
        Jd = max(Jd, paper[0] - a.cap)
    D = point(Jd, m, h)
    pts = {"": lift(D, paper, a.lift_normal), "deep": lift(D, paper, a.lift_deep), "deeper": D,
           "bd": point(darken_to(paper, mb, h, a.border), mb, h)}
    out, bad = {}, []
    for k, p in pts.items():
        out[k], ok = ucs_to_hex(vc, *p)
        if not ok:
            bad.append(k or "normal")
    for k, given, (J, M) in (("edge", edge, a.edge), ("ink", ink, a.ink)):
        out[k], ok = (given, True) if given else ucs_to_hex(vc, *point(J, M, h))
        if not ok:
            bad.append(k)
    return out, bad


def fit(a):
    css = (HERE / "palette.css").read_text(encoding="utf-8")
    paper_hex = re.search(r"--paper:\s*(#[0-9A-Fa-f]{6})", css).group(1)
    vc = cam.Viewing()
    paper = vc.ucs(paper_hex)
    hues = [float(x) for x in a.hues]
    if len(hues) != len(NAMES):
        sys.exit("--hues needs %d angles (%s)" % (len(NAMES), " ".join(NAMES)))
    if a.even:
        hues = [hues[0] + 40 * i for i in range(len(NAMES))]
    hues = [(x + a.rotate) % 360 for x in hues]
    red = set(a.red.split(","))
    fams, warn = {}, []
    fams["stone"], bad = family(vc, paper, a.stone_hue, a.stone_m, a.stone_m * 1.1, a,
                                edge=a.stone_edge, ink=a.stone_ink, cap=False)
    warn += [("stone", b) for b in bad]
    for n, h in zip(NAMES, hues):
        k = a.red_trim if n in red else 1.0
        fams[n], bad = family(vc, paper, h, a.m_deeper * k, a.m_border * k, a)
        warn += [(n, b) for b in bad]
    return css, paper_hex, hues, fams, warn


def token_block(fams):
    return "\n".join(
        "  --{n}: {f[]};  --{n}-deep: {f[deep]};  --{n}-deeper: {f[deeper]};  --{n}-bd: {f[bd]};  "
        "--{n}-edge: {f[edge]};  --{n}-ink: {f[ink]};".replace("{f[]}", fams[n][""]).format(n=n, f=fams[n])
        for n in ORDER)


def summary(paper_hex, hues, fams, warn):
    vc = cam.Viewing()
    tone = {"normal": "", "deep": "deep", "deeper": "deeper"}
    print("hues: " + "  ".join("%s %.0f" % (n, h) for n, h in zip(NAMES, hues)))
    rng = lambda xs: "%.1f–%.1f" % (min(xs), max(xs))
    for t, k in tone.items():
        print("  %-7s ↔ paper %s   closest two families %.1f" % (
            t, rng([vc.dE(fams[n][k], paper_hex) for n in ORDER]),
            min(vc.dE(fams[x][k], fams[y][k]) for x, y in itertools.combinations(ORDER, 2))))
    print("  steps   normal↔deep %s   deep↔deeper %s   border ↔ paper %s" % (
        rng([vc.dE(fams[n][""], fams[n]["deep"]) for n in ORDER]),
        rng([vc.dE(fams[n]["deep"], fams[n]["deeper"]) for n in ORDER]),
        rng([vc.dE(fams[n]["bd"], paper_hex) for n in ORDER])))
    if warn:
        print("  out of sRGB gamut (clipped): " + ", ".join("%s %s" % w for w in warn))


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0],
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    ap.add_argument("--dry-run", action="store_true", help="print, don't write palette.css")
    ap.add_argument("--deeper", type=float, default=10.0, help="ΔE' of deeper fills from the paper")
    ap.add_argument("--lift-deep", type=float, default=1 / 3, help="deep = deeper moved this far toward the paper")
    ap.add_argument("--lift-normal", type=float, default=2 / 3, help="normal = deeper moved this far toward the paper")
    ap.add_argument("--m-deeper", type=float, default=7.2, help="colourfulness M' of deeper fills")
    ap.add_argument("--cap", type=float, default=7.0, help="most a deeper fill may darken (ΔJ')")
    ap.add_argument("--border", type=float, default=18.0, help="ΔE' of borders from the paper")
    ap.add_argument("--m-border", type=float, default=9.0, help="colourfulness M' of borders")
    ap.add_argument("--red", default="rose,clay,mauve", help="families that get --red-trim")
    ap.add_argument("--red-trim", type=float, default=0.9, help="colourfulness factor for --red")
    ap.add_argument("--edge", type=float, nargs=2, default=[48, 19], metavar=("J", "M"), help="line colour J' M'")
    ap.add_argument("--ink", type=float, nargs=2, default=[36, 18], metavar=("J", "M"), help="accent ink J' M'")
    ap.add_argument("--hues", nargs=9, default=HUES, metavar="H", help="hue angles for " + " ".join(NAMES))
    ap.add_argument("--rotate", type=float, default=0.0, help="add to every hue (degrees)")
    ap.add_argument("--even", action="store_true", help="space the hues exactly 40° apart from the first")
    ap.add_argument("--stone-hue", type=float, default=99.47246784196842, help="stone's hue")
    ap.add_argument("--stone-m", type=float, default=2.306531201822184, help="stone's colourfulness M'")
    ap.add_argument("--stone-edge", default="#6F6C62", help="stone's line colour")
    ap.add_argument("--stone-ink", default="#525046", help="stone's accent ink")
    a = ap.parse_args()

    css, paper_hex, hues, fams, warn = fit(a)
    block = token_block(fams)
    summary(paper_hex, hues, fams, warn)
    if a.dry_run:
        print("\n" + block)
        sys.exit(0)
    i = css.index(BEGIN) + len(BEGIN) + 1
    j = css.index("\n}", i)
    (HERE / "palette.css").write_text(css[:i] + block + css[j:], encoding="utf-8")
    print("wrote palette.css — note its header still describes the default settings; "
          "update it if you keep the change")
