# Review of `search/RANKING.md` (as of b7fbfb0)

*2026-10-09, by Claude (Fable 5.1), for Joseph and the proposal's author. Two other reviewers wrote at the same time; I haven't seen their files. What I read whole: `search/RANKING.md`, `search/weights.toml`, `search/srcsearch/rank.py`, `search/DESIGN.md`. What I read in part: the pilot's `REPORT.md` (its first two sections) and `search/eval/pilot-check` (its docstring and scorer). I ran nothing. Findings are listed most consequential first; the small ones are at the end.*

## In short

The register is the valuable part and should be kept whatever happens to §3. Writing each factor as a hypothesis apart from its encoding has already surfaced things the code hid (the three tokenizers of H-Q5, the two case rules of H-Q4, the double-counting inside H-W4's $\pi$), and §2 is an accurate description of `rank.py`: I checked each factor and the H-W4 formula against the code, and they agree.

The log-odds model is the right frame, but the proposal under-describes it in three places that change the decisions in §8:

1. **The rank curve is not a neutral choice beside the weights; it *is* the weight of every evidence group.** Under the proposed model, the curve's scale fixes how much a group's whole ranking can say, and so how it compares to the priors. With an RRF-shaped curve the top ten of a group span 0.14 nats, less than today's Influence factor (0.10 nats). "Equal weights" is undefined until the curve is fixed, so §8's decision 1 has to come first, and decision 2 partly falls out of it.
2. **"From ranks" and "from calibrated scores" are not two methods; they are two feature choices for one model, logistic regression**, which is what "log odds, linear in the groups' evidence" already is. Naming it gives the proposal a standard fitting method, a standard way to hold out data, and a precise meaning for "equal opportunity" (a prior on the coefficients). It also shows that a rank curve *can* be calibrated from judged data, which dissolves the dichotomy in §3.2.
3. **Rank evidence changes meaning with scope, and cannot give what the outline and the answerability cue need: an absolute score.** A passage at lexical rank 1 inside one 200-passage document and at rank 1 over 48,000 passages get the same evidence. And the top rank always gets the top evidence, so "nothing in scope answers this" is unsayable from ranks. DESIGN §11 step 8 records this exact gap ("an absolute cosine floor isn't supported by measurement … This is a question for `hybrid` too") and a calibrated log-odds from scores is the thing that would fill it. That argues against the lean in §8.1, and the proposal doesn't weigh it.

Then two things the model needs and doesn't say: what a passage *absent* from a group contributes, and that today's multipliers cannot be carried over as likelihood ratios without re-measuring.

## What I checked, and found right

- §2 against `rank.py` `search()`, `lexical()`, `proximity_density()`, `definition_matches()`, `_recency()`: the candidate rule, the two BM25 legs, the phrase and heading multipliers on the lexical score, the RRF base with $k = 60$, the seven multipliers and their values. One omission: proximity is computed only for the top 500 passages of the lexical ranking (`signal_pool`), and everything outside that head gets $f = 1$. Since $f \ge 1$, being outside the head is never a penalty, but §2 should say the cap exists, because it is a hypothesis of its own (that nothing past lexical rank 500 is rescued by proximity).
- H-W4's formulas against `proximity_density`: $\gamma$ is the code's `gap`, $\sigma$ and $\rho$ its sentence and paragraph sets, $o$ its order test, $\kappa$ its `best`, $\pi$ its return value. They match.
- H-F1's arithmetic ($70/61 \approx 1.15$) is right.
- BM25's $N$, $\overline{|p|}$ and document frequencies are taken over the whole corpus even when a scope is given (`_bm25`, `_stats`). So the lexical *score* is scope-invariant and the lexical *rank* is not. That fact bears on finding 3 below.
- The register's encodings are honest about where values came from. H-R1's "fitted to judged misses, so they are optimistic" and H-R2's "set after one bad result" are exactly the marks that keep this from becoming the spaghetti Joseph described.

## Findings

### 1. The curve is the weight

In the proposed model a group contributes $\log \Lambda_g$. If the evidence comes from rank through a shared curve $\lambda(r)$, then the most a group can ever say, between its rank 1 and rank $r$, is $\log \lambda(1) - \log \lambda(r)$. That span is set by the curve alone. Some values, so the point is concrete:

| Term | Size in nats |
|---|---|
| RRF curve, rank 1 against rank 10: $\ln(70/61)$ | 0.14 |
| RRF curve, rank 1 against rank 400: $\ln(460/61)$ | 2.0 |
| Influence, anchor: $\ln 1.10$ | 0.10 |
| Definition, exact, confidence 1: $\ln 3$ | 1.10 |
| Section kind, toc: $\ln 0.3$ | −1.2 |
| Proximity at its maximum: $\ln 1.6$ | 0.47 |

With the RRF curve, an exact definition outweighs the whole top 100 of the semantic ranking ($\ln(160/61) = 0.96$), and Influence can reorder a group's top ten on its own. With a steep curve ($\lambda(r) = 1/r$, say) the same priors become tie-breakers. So "every group enters with weight 1" has no content until the curve is chosen, and the §3.3 rule "a weight other than 1 needs a measurement" is silently preceded by a choice no measurement has been proposed for. Two consequences:

- §8's decision 1 should be made first and stated as "choose the curve, which sets the scale all priors are measured against." The present text treats it as one open choice among four.
- The flatness of RRF that H-F1 reads as a defect ("may undervalue the top") is also the property that made RRF robust in the pilot: no one list can decide the fusion. Under a steep curve one group's error becomes decisive. The hypothesis should carry both directions, so the ablation can say which wins here.

### 2. This is logistic regression; say so

$\log O(R \mid e) = \log O(R) + \sum_g \log \Lambda_g(e_g)$ with each $\log \Lambda_g$ a function of a feature is a generalised additive model on the log-odds scale; with each one linear in its feature it is logistic regression. I say this not for the name but for what it buys:

- **The two options in §3.2 are one model with different features.** "From ranks" is logistic regression on $\log \lambda(r_g)$ with tied coefficients. "From calibrated scores" is the same with the raw score (or a monotone transform of it) as the feature. Either can be fitted, so **a rank curve can be calibrated**: among judged passages, the fraction relevant at each rank band in each group estimates $P(R \mid r)$, and a one- or two-parameter curve (log-linear in $\log r$, say) fitted to that *is* $\lambda$. The proposal's "ranks first, calibrate later, group by group" becomes "fit the curve's one parameter now; fit per-group coefficients later if the data support them."
- **"Equal opportunity" has a standard form:** a prior on the coefficients centred on 1 (ridge toward equal weights). The strength of that prior is what "until a measurement justifies otherwise" means numerically, and the held-out test in §5.3 is the ordinary one.
- **Calibration is testable in its own right.** If the score claims to be a log-odds, a reliability check on the judged data (do passages scored at odds 3:1 turn out relevant about 75% of the time?) is a second evaluation beside nDCG@10, and it is the one that licenses the uses in finding 3. The proposal claims a probability and then evaluates only an order; it should evaluate the probability too.
- The sizes are workable. With roughly five group coefficients, one curve parameter and an intercept, 160 graded results plus 469 judged stretches is not rich but is not "fitting the noise" either, provided the fit is held out as §5.3 says.

Two cautions that come with the name. First, a logistic model with correlated features (Words and Meaning) shares the weight between them rather than double-counting, which is the fix §3.1 wants, but a fitted model will then *not* have equal weights, and the register needs a status for "fitted below 1 because correlated with group X," distinct from "measured to hurt." Second, with $\Lambda$ fitted, the "neutral is built in" claim ($\Lambda = 1$ means nothing) holds only at the feature value the fit centres on; it needs the intercept to absorb the rest.

### 3. Rank evidence is scope-relative and has no floor

Two uses already in the repository need an absolute score, and the proposal's lean cannot give one.

- **Scope.** `hybrid` takes a scope, and the outline scores "every passage in scope." Under `--in california-2025-sb53` a passage at lexical rank 1 is the best of about 200; over the corpus it is the best of 48,000. With rank evidence these get the same $\log \Lambda$, so the score's meaning shifts with every scope, and a top-2% tier in one document means something different from the same tier in another. BM25 and cosine distance, by contrast, are computed against whole-corpus statistics (checked, above), so score-based evidence keeps one meaning across scopes.
- **The floor.** The answerability cue (`weights.toml [answerable]`) and the outline's "'zzqqxx' gets a top 2%" problem both need to say when nothing in scope is relevant. From ranks this is impossible: rank 1 exists for every query. A calibrated log-odds from scores, with the prior as its intercept, gives exactly the statement "the best passage here has posterior odds of 1:50," which is the floor DESIGN §11 step 8 could not find from cosine distance alone. (The cue's current threshold, 0.50, was set by separating on-topic from far-off-topic queries; a calibrated score would let it degrade gracefully for near-topic ones, which weights.toml notes are untested.)

This doesn't settle §8.1 toward scores; the stated costs are real (BM25's scale moves with the query length and term rarity, and the data are small). But those costs are addressable (normalise BM25 by the query's maximum attainable score, or by its idf sum, before calibrating; the curve for cosine distance is already scope-free), while the rank option's costs are structural. If ranks are chosen first anyway, the proposal should say that the outline and answerability stay on a separate, absolute signal, and why that is acceptable.

### 4. What a missing group contributes is unstated, and it matters

A passage can be absent from the semantic group (not among the 400 nearest), from the Words group (no query word), or from both and still be a candidate (a definition). Today's code gives an absent group rank $N + 1$, so RRF adds $1/(k + N + 1) \approx 0$. The proposal says a factor that tells nothing has $\Lambda = 1$, and then never says whether absence is "nothing" or is evidence. It is evidence: being outside the 400 nearest means being farther than the 400th, and holding none of the query's words is BM25's strongest statement. Under rank evidence the natural encoding is $\lambda(\text{pool size} + 1)$, which with the RRF curve is nearly the same as rank 400 and so says little; under score evidence it is the score's actual value (a cosine distance you can compute for any passage; a BM25 of 0). Three things follow:

- The pool size (H-C1) stops being a candidate filter and becomes part of the evidence encoding; a change to it changes scores, not just recall. The register should say so.
- The outline could stop treating non-candidates as "no hits" and score them as prior plus absence evidence, which would make the "+9 sections not shown (5 near)" counts commensurable with the opened ones.
- H-C1's own hypothesis, "every relevant passage is a candidate," can only be tested from the whole-document judgments, since the pilot's grades are pooled from ranked lists and so can never contain a non-candidate. That is the next finding.

### 5. The two judged sets are not alike, and the difference decides what each can calibrate

§5.3 adds them together ("160 graded results; 469 stretches"). They answer different questions. The pilot's grades are pooled from the rankings' own top tens, so they say nothing about what the rankings missed, and anything calibrated on them (the rank curve's tail, the absence evidence, H-C1) inherits that blindness. The whole-document judgments were made by readers who read in order without seeing any ranking, so they are the only data here that can say what a relevant passage looks like *when the ranker didn't find it*. For fitting a curve's tail, for H-C1, and for the independence check in §6, prefer them; for nDCG at the top, the pilot's grades are fine. The proposal should name this, because "fit on one set, report on the other" is only sound when the sets are drawn alike, and these aren't.

### 6. Today's multipliers don't translate; they re-measure

§3 says the multipliers "translate directly into this model": the definition boost of 3 "says a definition is three times as likely to be relevant." As a reading of the number that is right, but the number was measured as a multiplier on an RRF sum, and its effect there depends on the sum's scale. $\times 0.3$ on $1/(60 + 1)$ moves a passage from rank 1 to about rank 143; $\times 0.3$ on odds moves it by 1.2 nats, whose rank effect depends entirely on the curve (finding 1). So the fitted values (H-R1's 1/0.25/0, H-R2's 0.3–0.7, proximity's 0.6) are starting points under the new model, not carried-over measurements, and their register status should drop back to *proposed* when the model changes, with the old measurement kept as impetus. The proposal's own rule in §6 ("re-run the ablations when a hypothesis is added, since composition can change what the others contribute") already implies this; it should apply it to the change of combiner, which changes composition most of all.

One multiplier survives translation exactly, and it is worth saying because it is a small vindication of the current encoding: the definition factor $1 + 2mc$ is the Bayesian mixture $c \cdot \Lambda + (1 - c) \cdot 1$ for $\Lambda = 3$, which is the right way to use a detector's confidence. So H-R1's *form* is already what the model wants; only its value needs re-measuring.

### 7. Within-group composition is where the spaghetti lived, and the model leaves it there

"Composition is addition" holds across groups. Within Words, §3.1 says the rule is "BM25, with phrase, proximity and heading as terms inside it," and today those are multipliers on BM25 ($\times 2$, $\times 1.2$, $\times (1 + 0.6\pi)$), which is addition only in the log. That is fine, but it should be stated as the group's rule in its own register entry, with the same discipline as the top level: each inner term is a log-likelihood ratio, conditionally independent of BM25 given relevance, or else absorbed. H-W4's own note shows the problem the model exists to solve, reproduced one level down: $\pi$ carries coverage and exactness that BM25 and the stem leg already count. The cure the proposal gives (strip $\pi$ to closeness alone) is right, and the group entry is where to record the rule that makes it necessary. The fixture for Words should then test the group's composition, not only each term alone.

Related: H-W3 is not quite "the zero-gap case of H-W4." Proximity runs on content words (`pq['words']`, stop words removed), so for "loss of control" its window is over "loss … control" and "of" is a one-word gap; the phrase matcher runs on the full term with function words. A passage with "loss control" adjacent would get maximal proximity and no phrase factor. Either is defensible; the register should say which word list each uses, since that is an H-Q1 decision leaking into two places.

## Smaller notes

- **H-W1's status** cites 0.79, which is the fused score with priors. BM25 alone is the pilot's 0.540 (without the definition prior) or `pilot-check`'s 0.702 (lexical with priors). The entry should cite the lexical-alone number, since that is what its hypothesis claims.
- **H-M2 against H-R3.** The site-navigation failure is listed under both. The proposal's own method (§6: read `--explain`, find the mis-specified term) can decide it: if the navigation passage's semantic rank is high *and* a title-free re-embedding drops it, it is H-M2; if its semantic rank is unremarkable and it rises on something else, H-R3. Worth running before building either fix, since one is a re-embed of the corpus and the other is a detector.
- **H-D1 (superseded) as scope rather than relevance:** agreed, and the code already has `active_key` on every document row, so folding is cheap. If it is kept in ranking at all, note that a superseded document and its successor often hold near-identical passages, so the factor mostly orders copies, which `_collapse` only handles for verbatim text.
- **H-D3's encoding** ranks among *distinct years* within the organisation (`years.index(y) / (len(years) - 1)`), and a lone document gets 0.5. Two documents from one year tie. Fine, but the register's "position among its organisation's documents by year" reads as a per-document position.
- **H-T1's overlap** means a definition sentence can sit in two passages and both receive the definition evidence, which yields near-duplicates in a top ten that `_collapse` (exact text hash) will not fold. Not new, but the log-odds model makes it visible, because both will carry the same large term.
- **§6's independence check** needs judged data in which relevant passages are not already selected by the signals being correlated; see finding 5 (use the whole-document judgments).
- **§2's "13 factors with 27 tunable values"**: I count 31 named values in `weights.toml` including the non-numeric ones and the answerability threshold. Not worth precision, but "about thirty" is safer than an exact count that a reader will recount.
- **RRF's provenance.** My memory matches the proposal's (Cormack, Clarke and Büttcher, SIGIR 2009, $k = 60$ tuned), and like the author I have not re-read it. Two unverified memories agreeing is not verification; the citation check that `influx/reviews/citation-check-2026-10-07.md` did for the plan would settle it in a minute.

## On the decisions in §8

1. **Ranks or scores.** Not either; one logistic model, and the first question is which feature per group. My lean, lower confidence than the author's on the opposite: scores for Meaning (cosine distance is already scope-free and bounded) and a normalised BM25 for Words, with a one-parameter curve each, fitted on the whole-document judgments and reported on the pilot's grades. If ranks are chosen anyway, fit the curve rather than inheriting $1/(60 + r)$, and keep an absolute signal for the outline and answerability.
2. **Status, Influence, recency.** Agree with the author on all three leans. Add: under any curve flatter than $1/r$, Influence at its present values is below the resolution of the model anyway (finding 1), so "out of ranking, used for ties" is also what the arithmetic says.
3. **Migration.** Agree, with one addition that costs an afternoon and should come before any code: fit the logistic model on the *existing* `--explain` output over the judged data (the per-passage ranks, scores and factor values are all already printed) and look at the coefficients. That says, before building, whether equal weights is near the optimum, which groups carry signal, and roughly what the curve wants to be. It is the cheapest test of §3 there is, and it turns §8.1 from a lean into a measurement.
4. **Fixtures.** Agree. Add one for within-group composition (finding 7) and one for absence (finding 4): a candidate present in only one group, with a predicted score relative to one present in both.

## What this review did not do

I did not run the ablations, the fixtures (which don't exist yet), or `pilot-check`; the arithmetic in finding 1 is mine from the stated values and is easy to recheck. I did not read `outline.py`, `match.py` or the pilot's judging notes, so where I speak of the outline I rely on DESIGN §11 and §12. I did not look at memorata's `proximity_score` to confirm the port; I compared the register to `rank.py` only. Treat the findings as the content; silence on a section is not endorsement.
