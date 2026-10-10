# Debrief: where the outline's shortfall comes from

*To Joseph and ai-risk-model-61, from the Claude (Opus 5.5) session that ran this spike, 2026-10-10. Every number is reproducible from `code/` (see `README.md`); the run outputs are in `runs/`. Tiers: **measured** (a computation over the judgments, with a paired bootstrap over the 12 queries where it says "interval"), **estimated** (my reading or an inference from measurements), **guessed** (said as such).*

## The short answer

The quarter of judged material the outline doesn't flag is mostly not a weighting problem, not an embedding problem, and not, for the most part, paraphrase. The judges marked what an agent needs in order to *answer* each question. Much of that is linked to the query only by domain knowledge: self-exfiltration and power-seeking for "loss of control", SB 53's deception incident for "misalignment", the glossary entry for "Alignment". No ranking built only on how similar a passage is to the query, in words or in embedding space, gets much of it: every such variant I tried moved the measure by about ±0.02.

What moved it was knowledge supplied from outside the similarity computation:
- **On the query side:** expansions a fresh agent wrote without seeing the documents: +0.025 to +0.050.
- **On the document side:** concept tags Sonnet wrote for every passage without seeing the queries: +0.068.
- **Both, with the expansions matched against the tags too:** +0.118, which takes flagged from 0.752 to 0.870, and must-read from 0.849 to 0.959.

That is the project's own plan seen from the search side: a lexicon of terms, their source wordings, and their relations, applied to both queries and documents. It argues for building those legs before fitting a combiner.

## 1. The measure, and what it can and can't say

"Flagged" (`outline-check`'s flagged/reached) credits a judged stretch when any passage overlapping it is ranked in the top 10% of the scope: 188 of Au5's 1,872 passages. Gain is 3 for must-read and 1 for helps. Today's value is **0.752**, and must-read alone is 0.849 (measured). I reproduced both exactly from the scorer's own code.

Three facts about the measure that bear on everything below (measured):
- **A random ranking scores 0.215–0.219.** Big stretches are easy to hit by chance. Today's ranking captures 68% of the room above chance.
- **Crediting a whole section** (a stretch counts if any passage with its heading path is flagged) raises today to 0.803, but raises random to 0.435. Relative to chance it's the same, so I kept the passage measure.
- **The shortfall is mostly grade 1.** Must-read stretches are flagged at 0.849, helps-only stretches much less.

**Judge variance is a real share of it** (measured on SB 53, the one document with two blind judges). Of what the ranking misses against Claude's judgments, 0.133 of 0.333 was marked by Claude alone. Against Gemini's, 0.074 of 0.232 was marked by Gemini alone. So a third or more of the SB 53 shortfall is ground the judges themselves don't share. I can't measure that on the other four documents.

## 2. Decomposition

Measured, pooled over Au5 at the 188 cut (`runs/decompose-188.txt`, `runs/curves.txt`):

| | share of judged gain |
|---|---|
| flagged today | 0.752 |
| unflagged, no passage in it is a candidate at all (Grok's H-C1 count) | 0.057 |
| unflagged, a candidate but ranked past the cut | 0.191 |
| ceiling of today's candidate pool (every candidate flagged) | 0.943 |

Of the unflagged gain:
- 15% would make the cut on full-scan cosine alone;
- 12% would make it on lexical alone;
- 50% sits in stretches holding none of the query's content words.

Where the misses rank: today's hybrid reaches 0.833 at a 15% cut and 0.867 at 20%. So a minority are near misses, and most rank far down.

Term queries do better than questions: 0.814 against 0.716 (must-read 0.904 against 0.819). The worst is "humans can no longer shut down or correct the AI system", at 0.40.

**What kind of thing is missed** (estimated: my classification of all 133 non-bio unflagged stretches from their opening words and the judges' notes, one reader; `runs/classification.tsv` has every call). The 12 stretches of the chemical/biological query weren't inspected:

| Category | Share of unflagged gain | Share of unflagged must-read gain | Example |
|---|---|---|---|
| Conceptual neighbour: an instance, mechanism or evidence of the query's concept | 37% | 27% | the Risk Report's "Pathway 5: Self-exfiltration" for loss of control |
| Rewording of the query's own concept, including another source's term for it | 26% | 50% | EU Code "Measure 1.4 Framework notifications" for what a developer must report |
| Peripheral context, linked by the judge's wide reading | 11% | 0% | the EU Code's SME exemption recital |
| Bio query, not inspected | 8% | 9% | — |
| Glossary entry for a related term | 7% | 5% | IASR "Alignment:", "Control:", "Cyberattack:" |
| The document's own cross-references: a definition used inside a relevant one, an exclusion, a statute's repeat | 5% | 5% | SB 53 (l) "Property"; §22757.16 equity exclusion; Labor Code repeats |
| Word form the matcher misses | 3% | 0% | "cyber" vs "Cyberattacks"; "shut down" vs "shutdown"; a tokenizer bug (below) |
| Near miss holding the query's words | 3% | 5% | "Pathway 1: Broad/diffuse sandbagging" |

So DESIGN §11 step 8's reading, "a paraphrase problem", covers about a quarter of the shortfall, though half of its must-read part. The larger share is relations between concepts, which no amount of better paraphrase matching reaches.

## 3. What didn't work, and why

All measured, as the change in flagged against today, with the paired bootstrap interval over queries.

- **Fable's logistic fit (RANKING §8.7) on today's `--explain` features** (`runs/fit-lr.txt`). Held out, it raises passage AUC from 0.866 to 0.882 (by document) or 0.894 (by query). But flagged falls to 0.740 or 0.703.
  - The fit improves the bulk ordering, which big stretches with hundreds of passages dominate, and not the tail the outline is judged on. The fitting objective has to be the measure the tool is for, or it will optimise the wrong thing.
  - The coefficients, standardised: cosine is about 4× lexical (+2.2 against +0.56); references −2.2 and toc −0.77 hold their sign. Definition +0.27 to +0.64, phrase +0.19, proximity +0.05. Heading and figure flip sign across folds, and query-word coverage comes out negative (collinear with lexical).
  - RANKING §8.7's revisit condition is met in the sense it names: restructuring today's features is about clarity, not about this shortfall.
- **Query parsing** (`runs/parsing.txt`).
  - Adding can/could/no/not/must/should/may/before/after/longer/whether/decided to the stop list: −0.001.
  - Dropping words in more than 10% or 5% of passages: −0.012 each.
  - BM25's IDF already discounts these words.
  - The prediction in the brief that parsing would matter more than the fit doesn't hold for stop words. It does hold for query *expansion*, which is parsing in the wider sense (§4).
- **Candidate pool:** scoring every passage by cosine, not the nearest 400: +0.005 (−0.007 to +0.017). The non-candidates are far away by cosine too (their best cosine ranks run 400–1,850 of 1,872).
- **Embedding input** (all 1,872 passages re-embedded; `runs/emb-variants-bge-m3.txt`). Path and text without the title: −0.005. Text alone: +0.008, but cosine-alone AUC drops from 0.845 to 0.798, so the context helps the bulk ordering. The single-passage finding in the brief holds at scale: H-M2 isn't the cause.
- **Other small embedders,** each replacing bge-m3 in the hybrid (`runs/emb-models.txt`): snowflake-arctic-embed2 +0.007, qwen3-embedding:0.6b −0.014, embeddinggemma:300m +0.018. Every interval spans zero. They reshuffle rather than improve: about 30–37 gain points won against 23 lost (`runs/by-category.txt`).
- **All of today's multipliers together** are worth +0.017 (+0.006 to +0.028).
- **Doc2query-style embedding** (the passage's text and its tags embedded together, replacing today's vector): +0.020 (−0.003 to +0.042). Tags help far more as their own legs than folded into one vector.

## 4. What did work

**Query expansion** (`runs/expansion.txt`). A fresh Opus agent wrote rephrasings and neighbours for 11 queries without opening the documents or judgments (`runs/blind-expansions.json`; it left out the bio query on my request). Each phrase gets its own lexical and semantic rankings, fused into one RRF with weight α for all the expansions together, at the same fixed cut:

| | α = 1 | α = 2 |
|---|---|---|
| Rephrasings | +0.026 (+0.006 to +0.049) | +0.034 |
| Neighbours | +0.028 (+0.010 to +0.048) | +0.042 (+0.019 to +0.071) |
| Both | +0.025 (+0.009 to +0.044) | +0.050 (+0.015 to +0.094), must-read 0.897 |

- Dropping the three phrasings the expander flagged as possibly learned from CLAUDE.md changes nothing.
- α was chosen from three values, so the α = 2 row is slightly optimistic.

**Document-side concept tags** (`runs/tags.txt`, `runs/tags-controls.txt`). These are DESIGN §12's idea, measured. Six Sonnet agents tagged every Au5 passage (about 9 tags each) without access to the queries or judgments. The tags are indexed by BM25 over the tags and by bge-m3 over the joined tags, and fused into today's RRF at weight β:

| | flagged | change, interval | must-read |
|---|---|---|---|
| tags, β = 1 | 0.820 | +0.068 (+0.030 to +0.107) | 0.918 |
| control: each passage's own top TF-IDF words, same number per passage | 0.754 | +0.003 | |
| only tags sharing no word with their passage ("bridge") | 0.770 | +0.018 | |
| only tags sharing a word with it | 0.795 | +0.043 | |

- The control says the gain is the tagger's knowledge, not an extra lexical leg.
- The tags work mostly by restating a passage in the field's standard vocabulary, which is the vocabulary queries are written in, and partly by naming what isn't there.

**Both together:**

| | flagged | change, interval | must-read |
|---|---|---|---|
| expansion + tags | 0.842 | +0.091 (+0.058 to +0.124) | 0.938 |
| ... with the expansion phrases also matched against the tags | 0.870 | +0.118 (+0.077 to +0.169) | 0.959 |

What each recovers (`runs/by-category-tags.txt`, against my classification):
- Tags alone recover rewordings most: 22 of 50 gain points.
- Query-side neighbours matched against document-side tags recover the most neighbours: 27 of 69.
- The two sides meet in a shared vocabulary.

Per query, combined: the shutdown question goes 0.40 → 0.71, loss of control 0.73 → 0.90, cyber 0.76 → 0.93, misalignment 0.63 → 0.76, bio 0.77 → 0.93 (tags only, since it had no expansion). Hazard and whistleblower are unchanged at β = 1, though a β = 2 variant cost hazard 0.94 → 0.76 (`runs/tags-per-query.txt`).

**It reaches what the outline opens,** not just the tier (`runs/outline-with.txt`: `outline-check`'s own scoring, with the new scores substituted for `rank.search` in my process only):

| Lines | Opened reached, today → combined | Covered, today → combined |
|---|---|---|
| 60 | 0.332 → 0.372 | 0.288 → 0.334 |
| 120 | 0.541 → 0.614 | |
| 200 | 0.653 → 0.774 | 0.566 → 0.694 |

**Across judges** (measured, `runs/per-doc.txt`, `runs/sb53-gemini.txt`):
- The EU Code, judged by Grok rather than Claude, improves like the others: 0.84 → 0.89 with tags, 0.92 combined.
- SB 53 against Gemini's judgments: 0.77 → 0.82 with tags.
- That eases, without removing, the worry that Claude taggers and Claude judges share priors.

**Why to hold the tag numbers loosely** (estimated):
- **My brief told the taggers what the tags were for** (bridging to related concepts), so this is an upper bound on what a plain "what is this about" prompt would give. A control batch under a bare prompt would measure the difference. Batch 6's tagger pointed this out.
- **They tagged in document order,** so orphan fragments (chart text, table rows) got context a passage-at-a-time tagger wouldn't have.
- **About 20 configurations were tried on 12 queries.** I report β = 1 as the primary for that reason.
- **Four of five documents** have Claude judges, and the taggers are Claude.
- **Cost:** the six taggers used about 1.5 million tokens for 1,872 passages. The whole corpus (61,559 passages) would be about 50 million that way (estimated, linear); per-passage batch calls would cost much less.

## 5. Smaller findings

- **A tokenizer bug** (measured). Postgres's parser reads slash-joined words as one `file` token. "Misalignment/Instrumental" in IASR's Table 3.5 is therefore invisible to BM25 for "misalignment", and the same goes for "chemical/biological" (32 occurrences), "threats/risks" (53) and others. 4,748 passages in 393 texts hold slash-joined words; Au5 has 520 such tokens. It's H-Q5's territory and touches `tsv_exact`, `tsv_stem` and the definitions' lookups alike.
- **Word forms** (measured on examples). Query "cyber" doesn't match "cyberattack(s)" (stem `cyberattack`), and "shut down" doesn't match "shutdown". Compounds are outside both the stem leg and `lexical`'s four-letter cap.
- **Near-copies** don't carry their original's rank: SB 53's Labor Code sections repeat §22757.11's definitions nearly verbatim. Only 2% of the unflagged gain has a near-copy (cosine ≥ 0.92) in the tier, so it's small.
- **Cross-references within a statute** (SB 53's "Property" and equity exclusion, which qualify "catastrophic risk") are a structural relation. A judge followed them; no similarity signal will. Small (5%), but some are must-reads.
- **Chunker faults the taggers reported** (estimated from their notes, not verified by me; worth a chunker pass):
  - Risk Report tables come through column-interleaved (passages 130271–130277, 130313–130324, 130479–130487).
  - Heading paths go stale inside the Risk Report (130046–130055 under "Claim 3.1.2" hold Claims 3.1.3–3.3.1).
  - IASR passages end with glued trailing headings (124508, 124520, 124525, 124536).
  - IASR's "Key information"/"Mitigations" boxes share one path across subsections (2.1's cyber and bio boxes are indistinguishable by path).
  - AISI 134366 is under the wrong heading.
  - The AISI appendix, references and glossary nest under "Conclusion".
  - EU Code sentence lead-ins are promoted to headings (125611 "The safety margin will").
  - EU Code legal numerals are lost ("Articles and 56(5)", 125584).
  - SB 53's 123676 "internet use" for "internal use" (the digest error the SB 53 expert found).

## 6. What this means for RANKING §8

- **§8.7 has its answer.** On the outline's measure, the fit is about clarity and calibration, not quality. If the combiner is rebuilt as a logistic model, fit it to a stretch-level objective (or weight passages by gain over stretch size), not to passage likelihood. Passage AUC rose while flagged fell.
- **Turning experts into fitting data** matters less than I think the plan assumed: the features they would fit can't reach most of the shortfall. The experts may serve better as the document-side taggers. They've read their sources experientially, which is what a tag needs and what the Sonnet taggers here had only in batches.
- **H-Q8 should cover relations, not only equivalences.** Rewordings and source wordings are a quarter of the shortfall; neighbours are more than a third. Both expansion lists helped about equally.
- **The order I'd suggest** is in `proposed-changes.md`, with reasons.

## 7. What I didn't do

- No cross-encoder. DESIGN §6.4 measured one at 2.7–2.9 GB on CPU, near the memory line the brief drew, and it would rerank only a head the misses mostly aren't in. A test on the top 400 per query would settle it.
- No second blind expander or tagger from another model family, and no bare-prompt tagging control. Both are the obvious next measurements for the tag result.
- No classification of the bio query's misses, by the brief's constraint.
- No hallucination-test runs (DESIGN §11 step 8). Everything here measures pointing, not what agents then do with it.

## On the brief

It was a good one to receive. It gave the measurements already proposed as context rather than a plan, it said what you had checked first-hand and what you hadn't, and it labelled your prediction as a prediction. That labelling is why I tested the parsing half of it rather than inheriting it. The one thing I'd add for whoever does the verification: the classification in §2 is the least checked thing here, and a second reader classifying the same 133 stretches blind to mine would say how much of "37% neighbours" is my reading.
