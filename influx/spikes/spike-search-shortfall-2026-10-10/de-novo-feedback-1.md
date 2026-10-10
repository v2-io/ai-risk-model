# De novo feedback 1 on the search-shortfall spike

*Claude (Opus 5.5), asked by ai-risk-model-61 for an independent, adversarial pass, 2026-10-10. I read `README.md`, `debrief.md`, `proposed-changes.md`, every script in `code/`, every file in `runs/`, the tagger and expander briefs and their tool calls (from the session transcripts), `search/eval/outline-check`, the judgments and RANKING §8. I reran what I could and added new measurements. Nothing outside this file was changed. My scripts sit in my scratch directory, which isn't durable; I can add them under this spike if they're wanted.*

*Tiers follow the debrief: **measured** (computed by me, from the spike's saved rankings or the live database, read-only), **estimated** (my reading), **guessed**.*

## The short version

The spike's numbers reproduce. Its central result, that knowledge from outside the similarity computation (query expansion plus document tags) recovers much of the outline's shortfall, **holds up out of sample, but smaller**. The headline for tags alone does not hold up as well.

- **Against new judges.** The source experts' blind stage-1 judgments (`search/eval/expert-judgments/`) didn't exist when the spike chose its settings. Scored against them, expansion plus tags still gains **+0.098** (interval +0.063 to +0.139; measured). **Tags alone fall from +0.080 to +0.042**, and that interval crosses zero. Expansion at α = 1 is **−0.002**.
- **On new queries.** The experts' 27 own questions were never seen by the taggers, the β choice or the classification. On them tags gain **+0.028** (−0.014 to +0.079), and +0.016 at a per-document cut (measured). The questions differ in kind from the 12 and today already flags 0.875 of them, so this is a weak test. It is a consistent sign at about a third of the size, not a replication.
- **"Blind" expansion is blind to the repository, not to the documents.** 177 of the expander's 295 phrases occur verbatim in Au5. At least 25 multi-word phrases occur verbatim in exactly one Au5 source, among them SB 53's and the EU Code's own wordings. Dropping them cuts the expansion gain by about a quarter (measured). The spike's test dropped only the three phrasings CLAUDE.md quotes.
- **The SB 53 judge-variance finding depends on which second judge you have.** With the SB 53 expert as a third judge, 91% of what the ranking misses against the Claude judge was marked by another judge, not 60%. Every must-read miss was. Pooled over four documents, about a third of today's misses are marked by one judge only (measured, by lenient line overlap).
- **A second reading of the classification agrees with the first:** 80% on primary category, κ 0.74, and gain-weighted shares within 4 points, on a random 45 of the 133 stretches. But I'm the same model family, I'd seen the scheme and the debrief's shares, and I read the same kind of evidence. That supports the coding's reliability, not the scheme's validity.
- **A few descriptive claims are stronger than the data.** "50% hold none of the query's content words" is 39% by stem. "Most rank far down" is contradicted by the spike's own `curves.txt`: 46% of the unflagged gain sits within twice the cut. And "linked by domain knowledge rather than similarity" sits awkwardly beside the spike's own finding that tags work mostly by restating a passage in standard vocabulary.

The direction of `proposed-changes.md` survives: new evidence legs before a combiner rebuild. The size of the tag effect should be reported as a range across judges, and the combination as the robust result.

## What reproduced

Measured, from the live database and the spike's saved rankings:
- `outline-check --judgments search/eval/outline-judgments` today gives flagged 0.752, opened 0.332/0.653 at 60/200 lines, list@R 0.397/0.687. These match `runs/outline-with.txt`, so the index hasn't drifted for Au5.
- `rescore.today()` gives 0.752 and must-read 0.849.
- Expansion R+N gives 0.777 at α = 1 and 0.802 at α = 2. Every row in `runs/tags.txt` I recomputed matches, including tags-both β = 1 at 0.820 and the combination at 0.870.
- The random baseline is 0.215–0.219, and 68% of the room above chance is right: (0.752 − 0.217)/(1 − 0.217).
- The slash-token claim holds. `ts_debug` gives `file` tokens for "Misalignment/Instrumental", "chemical/biological", "threats/risks" and "ISO/IEC". The passage count depends on the regex, which the spike doesn't state: mine (`[A-Za-z]{2,}/[A-Za-z]{2,}`) gives 6,047 canonical passages, against the spike's 4,748. Worth stating in item 1.
- The judgment files and the canonical texts share sha256s for all five documents, so the spike's (and my) line-overlap comparisons between judges are valid.
- The tags line up with their passages (spot check of 8). Every batch's ids match its tags file, so the shared scratch directory (below) caused no mix-up I could find.

## Findings

### 1. Out of sample against the source experts' judgments (measured)

Same 12 queries and same saved rankings, scored by the spike's own `flagged` (pooled Au5, cut 188) against the experts' stage-1 files. The experts cover four documents; IASR is only partly judged and is left out of both columns. The left column gives the original judges on the same four documents, so the two compare.

| ranking | original judges, 4 docs | experts, 4 docs |
|---|---|---|
| today | 0.743 (must 0.822) | 0.729 (must 0.817) |
| expansion R+N, α 1 | +0.004 (−0.009 to +0.017) | −0.002 (−0.019 to +0.016) |
| expansion R+N, α 2 | +0.038 (+0.007 to +0.073) | +0.023 (−0.008 to +0.056) |
| tags-both, β 1 | **+0.080** (+0.037 to +0.122) | **+0.042** (−0.005 to +0.083) |
| expansion α 2 + tags β 1 | +0.091 | +0.069 (+0.038 to +0.099) |
| ... with expansions matched against tags | +0.122 (+0.080 to +0.173) | **+0.098** (+0.063 to +0.139), must 0.925 |

By document, tags alone help the Risk Report (0.74 → 0.80) and SB 53 (0.66 → 0.74) against the experts. They do nothing for the EU Code (0.76 → 0.78) and slightly hurt AISI (0.75 → 0.73).

How I read it (estimated): the combined result is robust to who judges, and that's the finding to lead with. The tag-only effect is about half as large against a second judge. That fits two things. Tags partly encode the same reading the original Claude judges brought. And some of the tag gain is spread across more stretches rather than precision (finding 6). The experts are Claude too, so this doesn't settle the shared-priors worry. A cross-family judge on more than one document would.

### 2. Held-out queries (measured)

The experts asked 27 questions of their own beyond the 12. No part of the spike saw them. I computed today's ranking for each with `rank.search` (query vectors cached in my scratch, not `search/eval/.cache`) and added the tag legs exactly as `tags_eval.fuse` does:

| | flagged (pooled, cut 188) | must |
|---|---|---|
| today | 0.875 | 0.892 |
| tags-both β 1 | 0.903 (+0.028, −0.014 to +0.079) | 0.932 |
| tags-lex only | +0.016 | |
| tags-sem only | +0.012 | |

- At a per-document cut (10% of the named document's passages, since these questions name one source): 0.753 → 0.769.
- 17 of the 27 are already at 1.00 today.
- Gains: "what security must protect model weights" 0.57 → 1.00, "SB 53's definition of catastrophic risk" 0.56 → 0.89, "how does the Code treat internal use" 0.56 → 0.69.
- Losses: "AISI's mandate, access to models…" 0.67 → 0.50, and "how fast are capabilities improving" 0.93 → 0.87.

These questions are narrower, single-source and written in the source's own vocabulary ("ASL-3", "SB 53's definition of…"), so they are easier lexically and near the ceiling. I'd call this weak evidence that tags generalise beyond the 12 queries: the same sign, about a third the size.

### 3. The expansion isn't document-naive (measured)

The expander was blind to the repository's documents and judgments but not to the documents themselves. SB 53, the EU Code and IASR are public, prominent and before its training cutoff.
- 177 of 295 phrases occur verbatim as phrases in Au5.
- Among them, phrases occurring verbatim in exactly one Au5 source include "evading the control of its frontier developer", "foreseeable and material risk", "Office of Emergency Services", "safety and security model report", "within 15 days" and "Directive (EU) 2019/1937". Only three were flagged as not blind.
- Dropping all 25 multi-word phrases that occur verbatim in exactly one Au5 source (a crude filter that also removes some generic ones, such as "likelihood and severity") takes α = 1 from +0.025 to +0.018, and α = 2 from +0.050 to +0.038. Both intervals stay above zero.

So expansion's gain is mostly not recall of the sources' text, but about a quarter may be. That matters for the corpus beyond Au5. Au5 are among the best-known documents in it, and a lexicon-derived expansion won't carry a model's memory of a statute's wording.

A smaller point on the brief: its example of a neighbour, "the provisions that qualify a definition", was written after the spiker had seen SB 53's "Property" and equity-exclusion misses. It's mild, but it points the expander at a category the judgments contain (XREF). The tagger brief's "a mechanism, an instance, a piece of evidence" likewise names the classification's own categories, though that framing is the design itself, so it's fair to keep. It is one more reason the bare-prompt control in proposal 2 matters.

### 4. Judge variance, now with a third judge (measured)

`judges.py` found that of SB 53's misses against the Claude judge, 0.133 of 0.333 (40%) were marked by Claude alone, measured against Gemini. With the SB 53 expert's stage-1 file added:

| SB 53, misses against the Claude judge | also marked by the other judge |
|---|---|
| by Gemini | 60% |
| by the expert (Claude Opus) | 91% |
| by either | 91% |
| must-read misses, by the expert | 100% |

So on SB 53 the ground only one judge marked is about 9%, not "a third or more". The difference is mostly Gemini reading more narrowly than either Claude. That makes this a family effect as much as judge noise. It's a reason to want cross-family judges, and it also cuts against using two Claude judges as "independent" agreement.

Across the four documents with experts, today's misses against the original judge are marked by the expert as well (any line overlap, same query):

| | today | after expansion + tags |
|---|---|---|
| AISI | 39% | 54% |
| Risk Report | 61% | 23% |
| SB 53 | 91% | 89% |
| EU Code | 67% (judge: Grok) | 44% |
| pooled | 66% | 56% |

So in aggregate about a third of the shortfall is one judge's reading, close to the spike's estimate even though its SB 53 figure doesn't hold. Line overlap is lenient (a chapter-sized stretch overlaps almost anything), so these shares are upper bounds on agreement.

There is a good sign in the second column: the combined remedy preferentially recovers ground both judges marked. What's left on the Risk Report and the EU Code is mostly one judge's. SB 53 is the exception: its residual misses are shared, which fits the statute's cross-references (XREF) being reachable by no similarity or tag signal, as the spike says.

### 5. The classification, read a second time (measured agreement; estimated meaning)

I classified a seeded random 45 of the 133 non-bio unflagged stretches before opening `classification.tsv`. I worked from the query, the judge's note, the heading path and the first ~700 characters of the stretch, using the debrief's category definitions.
- Primary agreement was 36 of 45 (80%), κ 0.74. The spike's label was my primary or my stated alternative in 40 of 45.
- Gain-weighted shares in the sample, mine against the spike's: neighbour 36% vs 33%, rewording 24% vs 25%, context 15% vs 15%, related glossary entry 13% vs 13%, cross-reference 7% vs 5%, word form 5% vs 9%.
- The disagreements sit on the neighbour/context boundary (4) and around word form (3).

Limits: I'm the same model family as the first reader. I knew the scheme and its pooled shares before starting. And I read openings, not whole stretches. A blind reader from another family, without the debrief, is still what proposal 12 asks for.

On the scheme itself (estimated): it mixes two dimensions. Five categories describe the *relation* between stretch and query (rewording, neighbour, context, glossary, cross-reference). Two describe the *mechanism* of the miss (word form, near miss). IASR's executive-summary "Cyberattacks:" paragraph and "Misalignment/Instrumental" are rewordings by relation and word-form misses by mechanism. So "word form 3%" understates how often morphology contributes, and the 26%/37% split isn't a partition of causes. I'd code the two dimensions separately.

### 6. Is the gain relevance or spread? (measured)

`flagged` credits a stretch for any one passage in the tier, so a ranking that spreads its top 188 over more stretches can gain without getting more precise. Precision in the top 188 (passage label > 0, mean over queries), with must-read precision and distinct heading paths beside it:

| | P@188 | must-read P@188 | distinct paths | flagged |
|---|---|---|---|---|
| today | 0.358 | 0.161 | 110 | 0.752 |
| tags β 1 | 0.366 | 0.169 | 113 | 0.820 |
| expansion α 2 | 0.394 | 0.178 | 107 | 0.802 |
| expansion + tags (+ on tags) | 0.402 | 0.184 | 111 | 0.870 |

- Expansion and the combination raise precision as well as reach, so their gains are real relevance.
- Tags alone raise flagged by 0.068 but precision only by 0.008, with slightly more distinct paths. A good share of their flagged gain is spread. That fits finding 1, where tags halve against a second judge.
- Two random rankings fused at β = 1 give 0.70–0.71, so perturbation alone costs flagged. With the TF-IDF control, that confirms the tags carry information. They just carry less than +0.068 suggests.

### 7. The logistic fit (measured)

- **In-sample** (fit on all 12 queries × 5 documents), the passage-weighted fit reaches AUC 0.896 but flagged only 0.731, below today's 0.752. So the objective mismatch the spike reports isn't a held-out artefact, and its conclusion stands more firmly than the held-out numbers alone show.
- **The spike's proposed fix (item 8)**, weighting each passage by its stretch's gain over the stretch's passage count, gives 0.754 in-sample and 0.733 held out by query. About today's level. On these features, reweighting the objective doesn't recover the tail. That supports the spike's main thesis, but proposal 8 should say it was tried and gave a null rather than present it as the remedy.
- **Today isn't a held-out baseline.** `weights.toml`'s measured values were set on the pilot's grades: 16 queries, 7 of them among the 12 here, over 4 of the 5 Au5 documents. Comparing a held-out fit with a partly in-sample hand-tuned ranking favours today. The in-sample result above sidesteps this.
- **RANKING §8 decision 1** says to revisit "if coefficients change sign across the leave-one-document-out fits": that means too little data for that many features, so drop to fewer. `heading` and `sec_figure` flip sign. The debrief notes the flips but not that they trip decision 1's own condition.
- **"Cosine about 4× lexical"** reads standardised coefficients under heavy collinearity (`cos` with `log_sem_rank`, which takes −0.67; `lex` with `has_lex` and `coverage`). The ratio isn't interpretable as relative importance. I'd drop it or say that.

### 8. Descriptive claims that run ahead of the data (measured)

- **"50% sits in stretches holding none of the query's content words."** That's by exact token. By Postgres English stem it's 39%; by 5-letter prefix, 33%. Today's stem leg already sees stems, so this doesn't change what the ranking could match, but the sentence as written overstates absence.
- **"A minority are near misses, and most rank far down."** From `curves.txt`, the share of unflagged gain recovered by widening the cut: 33% at 15%, 46% at 20%, 60% at 30%. Nearly half the misses are within twice the cut. That is "close", even though no variant tried moves them up.
- **"Most of it is linked to the query by domain knowledge rather than by similarity."** The evidence is that variants of today's features and small embedders (≤ 0.6B, under the memory line) move flagged ±0.02. But the spike's own control finds tags work "mostly by restating a passage in the field's standard vocabulary": echo tags +0.043 against bridge tags +0.018. Restating in standard vocabulary is vocabulary normalisation, which larger embedders and cross-encoders are built to do, and neither was tested. I'd scope the claim: "not reachable by today's features or the small embedders tried". Which of the two readings is right is exactly what the untested cross-encoder would say.
- **"The non-candidates are far away by cosine too (best cosine ranks 400–1,850)."** The 400 lower bound is the pool's definition, not a finding. The upper end carries the information.

### 9. The outline against a list, in the spike's own runs (measured)

This isn't the spike's question, but the data are in `runs/outline-with.txt` and the debrief's §4 table reads more favourably for the outline than the full table does. Under every ranking, a ranked list read to the same source lines (list@R) reaches more than the outline opens:

| | 60 lines | 200 lines |
|---|---|---|
| today | 0.332 vs 0.397 | 0.653 vs 0.687 |
| combined | 0.372 vs 0.472 | 0.774 vs 0.830 |

Each cell is outline opened vs list@R. Covered and must-read go the same way. Better ranking lifts both, and the list slightly more: +0.143 against +0.121 at 200 lines. So the outline's opening policy is a separate shortfall that these remedies don't touch. The Risk Report and SB 53 experts' notes say much the same per document.

### 10. Smaller points

- **Tagging procedure is confounded with document.** Batches 1–3 are all IASR, 4–5 the Risk Report, and 6 covers the EU Code, SB 53 and AISI. Tag density runs 6.2 to 11.7 per passage by batch. Batch 4 made a second pass adding "expert-recognition tags", and batch 2 calls itself a session tagging "by hand". Per-document tag gains can't be separated from tagger procedure. A production tagger would be one procedure, so a repeat with one prompt across all five documents would say how much the mix matters.
- **The six taggers shared one scratch directory** (the parent session's). The repository's CLAUDE.md warns that parallel agents need their own. Batch 2's tagger noticed and moved to a subdirectory. I found no collision (every tags file matches its batch exactly), but it was luck.
- **Reference-list entries got topical tags** (e.g. a robotics paper's entry tagged "safety of embodied AI"). The references multiplier damps them, but a production tagger should probably not tag bibliography entries topically.
- **Intervals.** The paired bootstrap over 12 queries uses percentile intervals, which run narrow at n = 12. It doesn't adjust for about 20 configurations tried. And the combined headline inherits α = 2, chosen from three values (the combination wasn't run at α = 1). Read the intervals as descriptive, as the debrief partly says.
- **Robustness I checked:**
  - Without the chemical/biological query: tags +0.059, combination +0.114.
  - Leaving one query out: the tags gain ranges +0.058 to +0.078.
  - No single query drives the result.
- **Proposal 9's H-M2 row** ("helpful for AUC (text only: 0.845 → 0.798)") reads as if text-only helps. It means the title and path help AUC. Reword.
- **Proposal 1's count** (4,748 passages in 393 texts) should give its regex (see "What reproduced").
- **`README.md` says the database must be as of `fafaa73`.** The index evidently hasn't changed for Au5 since (outline-check reproduces exactly). Commits since then touch only `search/eval/`.

## What I'd change in the debrief and proposals

1. Lead with the combination as the robust result: +0.118 against the original judges, +0.098 against the experts. Give tags alone as a range, +0.04 to +0.08 depending on judge and about +0.03 on held-out queries (interval crossing zero).
2. In §1, replace "a third or more of the SB 53 shortfall" with the three-judge figure. Keep the pooled one-third, with the leniency caveat.
3. In proposal 2's "before building", add: re-score against the expert judgments (now available) and a document-naive expansion control. Add one tagging procedure across all documents too.
4. In proposal 8, report that stretch-weighted fitting was tried: 0.754 in-sample, 0.733 held out.
5. Scope the "domain knowledge rather than similarity" sentence (finding 8). The cross-encoder test on the top 400, already listed in §7, is the measurement that would settle it.
6. Separate relation from mechanism in the classification before a second reader codes it.

## What I didn't do

- No cross-family second reader, no bare-prompt tagging control, no cross-encoder. Those are still the spike's open measurements.
- I didn't rebuild `runs/table.pkl`. I used it as saved and checked it against a live `outline-check`.
- I didn't classify, or read beyond labels and numbers, anything in the chemical/biological query.
- I loaded nothing beyond bge-m3 (about 1 GB, already resident) to embed the 27 held-out queries.

## On the spike, and the brief I received

It's a careful spike. The tiers are honest, every number traced to a script, and its own caveats (upper-bound framing, shared priors, the classification as least-checked) anticipated most of what I'd have raised. The one place it understated its own uncertainty is the tag-only effect, and the expert judgments that show that arrived after it was written. The brief I got was right for an audit: no enumeration, and a plain licence to look anywhere. That is why I went to the expert judgments, which the spike couldn't have used. I'm on the line for follow-ups.
