# Review of search/RANKING.md

*Written 2026-10-09 by Grok, for Joseph and for the author of the proposal. A reading of the proposal against the ranker it describes. Nothing here is a vote on the other reviews.*

Read whole: `search/RANKING.md`, `search/DESIGN.md`, `search/weights.toml`, `search/srcsearch/rank.py`. Read at the points the register cites: `embed_input` in `db.py`, `norm_term` and `WORD_RE` in `text.py`, `terms` and `FUNCTION_WORDS` in `match.py`, `fix_ocr_ai` in `bin/corpus.py`, `_score` and the tier rule in `outline.py`, and the pilot report's §3 where the proposal's nDCG figures come from (definition prior 0.540 → 0.697, cosine alone 0.654, fused 0.761, v2 rule +0.024). Those figures match the report.

Ran today, on the current index: `hybrid --explain` for `catastrophic risk` (top 20) and for `whistleblower` on SB 53 (top 15); `outline` of that second query at 30 lines; `hybrid --explain` for `hazard` on IASR 2026 (top 8). Did not re-run `pilot-check` or `outline-check`. Did not re-read Cormack, Clarke and Büttcher; the proposal already marks that citation as memory.

## Judgment

Adopt the register, and adopt it before changing the combiner. The split between a hypothesis and its encoding is what Joseph asked for, and several entries already use it to say something the code cannot say by itself: phrase is the zero-gap case of proximity, proximity's coverage and exactness are already inside BM25, Influence is doubtful as evidence, a contents line is evidence of location for the outline. That file is useful even if the formula in §3 never ships.

The formula is the right target and it is not yet a model to build. Score as a sum of log likelihood ratios once a term is estimated as a ratio. Until then, what §3.2 actually proposes is a shared rank curve, which is a cleaner reciprocal-rank fusion over groups. Naming that curve a likelihood ratio will make the next weight look principled while it is still a shape chosen by hand. Build the groups, write the Words equation, and keep today's multipliers beside it until the fixtures in §8 hold.

## The current head is the multipliers

`search()` computes a reciprocal-rank base, then multiplies (`rank.py`, the score just before the sort). For `catastrophic risk` the passage DESIGN §8 wants first is first:

| rank | document | semantic rank | lexical rank | base | what is multiplied | score |
|---|---|---|---|---|---|---|
| 1 | SB 53, §22757.11(c), exact definition, confidence 0.95 | 7 | 119 | 0.0205 | ×2.9 definition, ×1.6 proximity, ×1.10 Influence, ×1.025 recency | 0.1073 |
| 7 | Hendrycks 2023, not a definition | 24 | 15 | 0.0252 | ×1.6 proximity, ×1.05, ×1.025 | 0.0435 |
| 10 | Anthropic RSP v1.0, superseded, not a definition | 34 | 2 | 0.0268 | ×1.6, ×1.10, ×0.8 superseded, ×1.0 recency | 0.0377 |
| 11 | UUK taxonomy, lexical rank 1, not a definition | 94 | 1 | 0.0229 | ×1.6, ×1.025 | 0.0375 |

The statutory definition is lexical rank 119. Hendrycks and the superseded RSP both have a better RRF base. The definition is first because of the multipliers, above all ×2.9. The top six results are exact definitions of "Catastrophic risk"; the score then falls from 0.100 to 0.043. I checked the rank-1 product: 0.020512 × 2.9 × 1.1 × 1.025 × 1.6 = 0.1073, the printed score.

Every one of those twenty results has `phrase: true`, proximity 1.0 and `f_signals` 1.6. On this query the proximity term scales the head and does not reorder it. The phrase factor has already fired inside the lexical score, and the proximity factor fires again at its ceiling. That is the double count H-W3 and H-W4 name, visible without an ablation.

A second query shows the other half of the same mechanism. On SB 53, `whistleblower`:

- Hybrid ranks 1–4 are the legislative counsel's digest and the findings, all containing the word (scores 0.036 to 0.033).
- Rank 5 is the operative prohibition ("A frontier developer shall not make, adopt, enforce, or enter into a rule…"), semantic rank 1, no lexical rank, score 0.0185. The quote does not contain "whistleblower". Its score is one RRF term, 1/61, times SB 53's Influence and recency. Ranks 6–15 are the same shape: semantic ranks 3–14, no lexical rank, scores stepping down by about 0.0003 each.

A passage with no lexical hit contributes about 0 from the lexical side, because a missing rank is stored as N+1 (`rank.py`: `lex_rank.get(i, N + 1)`, and N is the canonical passage count). With N in the tens of thousands that term is about 0.00002, which is the neutral the log-odds model wants, arrived at by accident of the formula. The operative clause loses because the digest has two terms and it has one, not because absence is scored as a large penalty.

## Where the proposed model is ahead of its math

**The multipliers are ratios only after the base is odds.** §3 says today's multipliers translate directly and that the definition boost of 3 says a definition is three times as likely. The live factor is `1 + 2·m·c`, so confidence 1 gives ×3 and the SB 53 detection gives ×2.9. Multiplying an RRF base by 2.9 triples a sum of reciprocal ranks. It becomes "three times as likely" when the base is an odds and the 2.9 is added in the log. Phrase and heading do not translate even in that weaker sense: they multiply the lexical score before the rank is taken (`lexical()`, the phrase and heading loops), so their effect is whatever rank change survives `1/(60+r)`. Proximity was moved onto the fused score because inside the lexical score it did not change the rank. That history is in the proposal, and it is the reason "they translate directly" covers the post-fusion factors only.

**A shared rank curve is H-F1, and H-F1 is not yet a likelihood ratio.** A rank depends on the other candidates and on how many relevant passages the query has. One curve for every group, independent of the pool size, is the RRF robustness the pilot already measured. It is worth keeping as the way Meaning meets Words. It does not become $\Lambda(e) = P(e|R)/P(e|\neg R)$ by being written in a sum. BM25 is the group that already has a log-odds pedigree: the Robertson–Spärck Jones weight is a log odds ratio of term presence, and the idf in `rank.py` is Lucene's smoothed variant of that, `ln(1 + (N − n + 0.5)/(n + 0.5))`, not a probability fitted to these judgments. Rank-transforming the Words score throws away the magnitude that pedigree was for, in order to share a scale with cosine distance, which has no such pedigree. Role is neither a ranking nor a BM25. An exact definition is a categorical fact. Giving it a rank on a shared curve, or a weight of 1, leaves its magnitude to the shape of the curve.

**"Weight 1" and "Λ = 1" are different neutrals.** §3.3 gives every group weight 1 until measured. §3 says a factor that tells us nothing has Λ = 1, a term of 0 in the sum. A silent group should add 0. A group at weight 1 adds a full curve. On the whistleblower query those two choices are the difference between the operative clause staying a semantic-only hit and someone later "correcting" missing words into a negative term. Keep the current missing-rank behavior, which is approximately 0, and state it as the hypothesis: a group that did not retrieve the passage contributes nothing. "Not retrieved" as evidence against relevance is a separate hypothesis, and it would fight H-M1, whose job is the passage that never uses the query's words.

**Equal curves change which definitions stay first, and the product requirement is that they stay first.** Arithmetic on the written RRF curve, with an exact definition adding one extra $\lambda(1) = \frac{1}{61}$ and a non-definition adding nothing: a definition that is rank 62 on both sides ties a non-definition that is rank 1 on both sides. Today's ×3, applied to the sum, ties that same perfect non-definition only when the definition is about rank 123 on both sides. For `catastrophic risk` the statutory definition would survive the gentler rule, because its semantic rank is 7: base 0.0205 plus 1/61 is 0.0369, which still beats Hendrycks's base 0.0252 and a hypothetical both-sides rank 1 at 0.0328. A definition that is only mediocre on both lists would not. DESIGN §1 and the gold query in DESIGN §8 ask for the definition above a passage that merely uses the word. The outline also forces an exact definition into the strong tier after scoring (`outline.py`, the loop over `defines`). The list and the outline are two mechanisms. A migration that watches nDCG and not this head can pass while the list's reason for putting SB 53 first has changed.

The fixture for H-R1 should name that competitor: an exact definition against a non-definition at lexical rank 1 and semantic rank 1, and a third passage that is an exact definition of a broader term. "A definition against a passage that only uses the term" passes under almost any positive boost, including the one the pilot already fitted.

**The two evaluations are two events.** The pilot grades passages the old ranker already retrieved. The outline judgments mark stretches a reader of the whole document would open, including stretches that never use the query's words (DESIGN §11). Fit-on-one, report-on-the-other is the right discipline for small data, and a weight that wins on one and loses on the other may be true of one event. §5.3 should pre-commit which grade is R before anyone fits a ratio. The pilot's own diversification note bears on that choice: per-document decay lowered nDCG because the judge graded other-sense mentions 1, and the report says those are mentions Joseph wants caught. For this corpus a colliding sense is relevant. A likelihood fitted to "the AI sense of the word" will bury the industrial "hazard" the gold query wants beside IASR's. I would write that into the definition of R in §3, as a hypothesis about the project rather than a detail of nDCG.

H-C1 cannot be checked by switching a term off. A passage the candidate rule never returns has no ablation. The outline scores only what `rank.search` returns (`_score`), and its module docstring still says every passage in scope is scored. The docstring is the stale line; H-C1 matches the function. The check is a count, against the outline judgments: of the must-read stretches, how many contain no candidate passage. That count is the recall ceiling of the outline Joseph called the point of the tool.

The independence check in §6 has the same data problem. Correlation of the model's own group scores inside a judged top 10 is correlation among passages the current ranker already promoted. It can show Words and Meaning moving together there. It does not estimate $P(e|R)$ and $P(e|\neg R)$ over candidates. Run it over the candidate pool, with the outline's must-read labels mapped onto passages, and read it as a diagnostic the register can quote.

## Words, before any new directory

§3.1 says the Words rule is BM25, with phrase, proximity and heading as terms inside it. That sentence is the load the module split in §7 will have to carry, and it is not yet an equation. The live encoding is a different rule in each place:

- Exact-form BM25, plus half of a second BM25 on stems. A passage that matches the exact form also matches the stem, so an exact hit receives idf_exact plus half of idf_stem. A stem-only hit receives the half. H-W2 says the stem-only match is the weaker one, which this does. It also inflates every exact hit by the stem component. The hypothesis and the encoding disagree on what the 0.5 applies to.
- Phrase multiplies that sum by 2 when the literal matcher fires.
- Proximity multiplies the fused score by $1 + 0.6\pi$, and $\pi$ itself multiplies coverage, exactness and closeness (H-W4's formula). Coverage and exactness are the double count the entry already flags.
- Heading multiplies the lexical score by 1.2, untested.

H-W4's open list is the best technical paragraph in the register. The composition I would write down, and fixture, before `words.py` exists:

- One BM25 over exact forms.
- A stem-only match as its own term, present when the exact form is absent, at a smaller weight. The measurement that killed `forms_weight` (the query word is often the derived form) stays as H-W2b, refuted for that encoding.
- One positional term whose best case is the phrase and whose value falls as the window grows, so H-W3 is the zero-gap case of H-W4 and cannot fire on top of it. The top 20 of `catastrophic risk` is the fixture's expected failure of the current encoding: phrase true and proximity 1.0 together, on every row.
- Heading as a separate small term inside the group, with the fixture the pilot already pointed at: a form that occurs in a heading and not in the body.

The constants inside $\pi$ (0.03, 0.25, 0.6, 0.75, 0.55, 0.4) are tunable values the "27" does not include. They can stay memorata's until a fixture isolates one of them. They should sit in the register as sub-hypotheses with those values, which H-W4 already asks for.

Two word-class lists disagree, which is H-Q1's "two rules" in the code rather than only in the stop-list comment. `rank.STOP` drops `we our what how does do` and keeps `not no nor`. `match.FUNCTION_WORDS` does the reverse. Proximity and BM25 use the first list; the phrase matcher uses the second. One hypothesis, one list, and the phrase keeps the function words the concordance needs by an explicit exception, as the entry already says for "of" in "loss of control".

H-Q5 is accurate: `text.WORD_RE` keeps a hyphenated word whole, and `match.terms` splits on the hyphen (`"loss-of-control"` is three words, in that function's docstring). Worth a fixture, and worth deciding, because every group below inherits it.

## Role, on the result that motivated `figure = 0.3`

For `hazard` on IASR 2026 the glossary entry "Hazard: Any event or activity…" is rank 1 (semantic 1, lexical 1, ×2.70). Rank 2 is the caption "Figure 2.1: The number of events involving ‘content generation’…", section `body`, section factor 1.0, score 0.0338. The chart-data passage that `weights.toml` cites is not in the top 8. The definition boost is what puts the glossary first. The figure weight does not touch the caption, because the caption is not section `figure`.

H-R2's hypothesis is about passages that mention a term without saying anything about it. H-R2's encoding is a multiplier on six section kinds. The caption is in the first set and not in the second. This is the spaghetti pattern §1 describes, one step later: a weight set from one bad result, on a class that no longer contains that result, while a relative of the result sits at rank 2. The register's rule is the right response. Change the encoding so the feature matches the hypothesis, or mark the caption as a different hypothesis (a caption can be the sentence that says what the figure is for). Do not retune 0.3.

The broader-term rule is doing what H-R1 says. IASR's glossary entry "Risk: The combination of the probability and severity of a harm" is semantic rank 2, no lexical rank, definition factor 1.0, hybrid rank 7. It is present, and it is not boosted. Good. The pilot's hub-passage note still applies: a short generic definition can be near in embedding space for many queries. Presence without a boost is the current policy, and it matches "a colliding or neighbouring sense stays findable."

## Document features

Decision 2 is the one I would take further than the proposal.

Influence at 1.10 against context at 0.95 is a factor of 1.16. On an RRF score, both-sides rank 1 times 1.10 is 0.0361, and both-sides rank 1 times 0.95 is 0.0311. One side falling from rank 1 to rank 10, with the other side held at rank 1, moves the unweighted score from 0.0328 to 0.0307. The Influence gap is larger than that rank gap. "Mild" is true next to a ×2.9 definition boost and false inside the top ten, which is where a flat `1/(60+r)` makes every multiplier loud. The catalog's statement that reach is not relevance, the project's reason for existing (the divergent definition is the point), and the pilot's rejection of per-document decay are the same judgment. I would take Influence out of the score entirely, including out of tie-breaks. `--by source` and the Influence field on the result are where reach belongs. Confidence high, higher than the proposal's moderate-low.

Superseded is already scope in DESIGN §6.3: fold under the active version, `--history` unfolds. The ×0.8 on RSP v1.0 is a placeholder that still leaves a superseded passage at rank 10 for `catastrophic risk`, ahead of the active document at lexical rank 1. Scope removes it from the default candidate set and says that older versions exist. That matches the hypothesis "an agent usually wants the current version" better than a discount does, and it matches a decision the design already recorded. Confidence high.

Recency I would leave out of the default score until the hypothesis says which intent. "Newer is more often wanted" is true of "what does this organisation say now" and false of "where did this formula come from," and this corpus is used for both. A weak 0.05 still moves two passages whose RRF bases are as close as the ones above. The encoding also treats a missing year as the oldest year in the organisation: `year or 0`, then an index among years (`_recency`). The 0.5 default applies only when the key is absent from that map. A fixture with a missing year should expect neutral, and the code does not do that. Confidence moderate on leaving it out; the proposal's "weak prior until measured" will measure whichever intent the current judgments happen to reward.

## Statuses, fixtures, migration

§4 says *refuted* includes "did nothing." §5.2 says a contribution inside the noise is marked for review, not removed, because the queries may not test it. Proximity's interval includes zero and the entry is *measured*. Density hurt one-word queries, where it repeats term frequency, and it is *refuted*. Those can be made consistent: *refuted* means this encoding made the evaluations worse; "did nothing on these queries" stays *measured* or *proposed*, with the queries named. The hypothesis text stays, so a later encoding can be proposed without pretending the old one was never tried. Density is the case: the hypothesis may just be H-W1's saturation, which the entry's own note says.

§5.1's three fixtures are the right shape. The synthetic corpus has to carry N, n_w and the mean passage length, or a BM25 order is an artifact of unspoken background statistics. Each case needs the negative the hypothesis also claims: proximity abstains on one word; a broader definition is not boosted; a missing year is neutral; a phrase match does not also receive a full proximity term. One case per hypothesis is the right start, and H-C1's case is the recall count above, not a pair of passages.

H-Q3's encoding is more careful than its hypothesis. `fix_ocr_ai` leaves listed surnames and name-shaped references alone. The register says a query containing "Al" means "AI". The code already declines some of those. The hypothesis worth stating is the one the code implements, including the exceptions, plus the choice to run a document corrector on queries.

The module split in §7 mirrors the groups, which is what was asked. `words.py` as "one Words evidence term" will freeze whatever composition is implicit on the day it is extracted. I would write the equation and its fixtures first, in the current module, and split once `combine.py` has a single function to call. Moving the concordance, the definitions listing and `answerability` out of `rank.py` is independent of §8. They are not ranking, the proposal is right, and that move can happen either way.

When the encoding changes, the register's Encoding is the live one and the old one moves into a dated Evidence line. DESIGN §6.2 currently has "have not been built" in the same section as "Built 2026-10-09." The register will drift the same way if Encoding keeps every historical formula.

The outline docstring and H-C1 are a smaller copy of that drift. One of them should be brought into line when the register is next touched. H-C1 is the one that matches `_score`.

## Decisions in §8

1. **Rank curve or calibrated scores.** Use the rank curve to fuse groups that are rankings: Meaning, and Words only if the Words equation is itself reduced to a rank. Keep Role as categorical factors whose magnitudes are part of the hypothesis and are checked by the strong-competitor fixture, not as a third ranking and not as weight 1. Calibrate a group when one evaluation can fit a single monotone map and the other evaluation still prefers it to the unfitted version. Do not call the sum a log-odds until a term in it was estimated as a ratio. The sequence "ranks first, calibrate later" is right for Meaning. It is the wrong representation for a definition. Confidence high on the distinction; the author's confidence was moderate on starting from ranks for everything.

2. **Status, Influence, recency.** Influence out of ranking. Superseded becomes scope, as DESIGN §6.3 already specifies. Recency out of the default score, and the missing-year encoding fixed whenever it returns. Confidence high on the first two, moderate on recency.

3. **Migration.** Build it beside today's path and run both evaluations. Also require, before switching the default, that `catastrophic risk` still leads with the exact definitions and that `whistleblower` on SB 53 still surfaces the operative section, which is semantic rank 1 and lexical-absent. nDCG on 16 queries can hold while those two move. If the new path is worse, record the queries and keep today's path; the record is the result. Deleting the old path after a switch that meets those checks is right. Confidence high.

4. **Fixtures.** Yes, and they are the test that the equation says what the hypothesis says. They do not replace the two evaluations. Confidence high.

The part I would not reopen is the reason the proposal exists. Thirteen mechanisms and a flat rank curve will keep producing a local repair for each bad row, and `figure = 0.3` is already that repair. A register that forces the next repair to name a hypothesis, an encoding, and a fixture is the constraint that makes the formula honest whether or not §3 ships as written.
