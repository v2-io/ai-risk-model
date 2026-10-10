# Before the first unit

*Expert for `california-2025-sb53`. An Opus 5.5 session, started 2026-10-09. These files are my raw first-encounter reflections, one per unit read, kept as written.*

## Unit size and form

I chose one paragraph per unit (no `--min-words`), which makes 224 units. A statute draws its distinctions at the grain of a clause; a subdivision like "(c)(1)(A)" is often a single clause. Larger units would merge the separable concepts this project cares about.

Each `NNN.md` file records what I noticed after reading unit NNN:

- what differed from my prediction;
- wandering thoughts;
- sometimes notes on the text itself, such as conversion or OCR problems.

Each file ends with my predictions for unit NNN+1. Two running files sit alongside:

- `outline.md` is my developing picture of the statute, revised about every ten units.
- `questions.md` lists questions people will probably ask a source expert, and questions they *should* ask but might not.

(These files live on the branch `expert/california-2025-sb53`. The harness blocks edits in the shared checkout from this background session.)

## What I already carry (priming, declared)

From the repo's CLAUDE.md, which I read before seeing the source:

- SB 53's "catastrophic risk" definition "carries at least seven separable concepts, in one sentence plus a paragraph of exclusions". The seven are:
  - a knowledge standard;
  - a materiality standard;
  - a causal standard;
  - the conduct it attaches to;
  - casualty and dollar thresholds;
  - a counting rule;
  - a counterfactual baseline.

  The definition also "reaches into two other provisions".
- The ">50 people or $1B" bar, which four later documents reuse under two names. Two of them relabel it "systemic risk" and drop serious injury, so SB 53's own version must include serious injury.
- SB 53 is "liberally construed to effectuate its purposes".
- A California "frontier developer" is "defined by a training act and a compute threshold".

From training (soft, unverified, and probably partly wrong in detail):

- This is Senator Wiener's 2025 bill, the successor to the vetoed SB 1047. Newsom signed it in late September 2025.
- It requires large frontier developers to publish a frontier AI framework.
- It requires transparency reports at deployment of a new frontier model.
- It creates reporting of critical safety incidents to the Office of Emergency Services.
- It adds whistleblower protections.
- It sets up a consortium for "CalCompute", a public computing cluster.
- I believe the compute threshold is 10^26 FLOPs, and that "large" means more than $500M in revenue. These numbers are exactly what the priming warning is about. I'll check them, not assume them.

**The red flag I'm watching for in myself:** "I know what this says." My priming is strongest at the catastrophic-risk definition, the thresholds and the construction clause. That's where I'll be most tempted to skim, so that's where I'll read hardest.

## Predictions for unit 1

- ≈55%: bill metadata ("Senate Bill No. 53, Chapter ___", approval and filing dates), then a Legislative Counsel's Digest. The Digest would be its own small bounded context: a second author describing the bill, not law.
- ≈30%: it opens on "The people of the State of California do enact as follows:" and then "SECTION 1." with legislative findings.
- The remainder: a web or PDF edition with header junk (leginfo navigation, a "Bill Text" banner, dates).
- If unit 1 is a heading plus a paragraph, it's probably the bill number plus the title clause: "An act to add Chapter 25.1 (commencing with Section 22757.10) to Division 8 of the Business and Professions Code … relating to artificial intelligence." I'm unsure of the numbers.
