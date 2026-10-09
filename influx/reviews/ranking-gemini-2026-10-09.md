# Review of `search/RANKING.md`: The Log-Odds Ranking Proposal

*Drafted 2026-10-09 by Gemini for Joseph and Claude (Opus 5.5). This review audits the proposal in `search/RANKING.md` against the repository's search implementation (`search/srcsearch/rank.py`), configuration (`search/weights.toml`), the search pilot findings (`influx/search-pilot-2026-10-09/REPORT.md`), and the outline consumer (`search/srcsearch/outline.py`). Two other reviewers are working concurrently.*

---

## Executive Summary

The proposal in `search/RANKING.md` is an exceptional diagnostic of why `hybrid` search is at risk of heuristic rot. The impulse to replace an accretion of ad-hoc multipliers ($\times 2.0$, $\times 1.2$, $\times (1 + 0.6\pi)$, $\times 0.3$) with a principled Bayesian evidence framework—where every signal represents a log-likelihood ratio and combination is strictly additive—is conceptually sound and aligns with modern probabilistic IR.

However, the proposal in its current draft contains **three severe mathematical and engineering traps** that would cause immediate search quality regressions if implemented naively:

1. **The Multiplier-to-Log-Odds Deflation Trap:** Translating current multipliers directly into log-odds (e.g., definition boost of $3 \to \log(3) \approx 1.1$; TOC penalty of $0.3 \to \log(0.3) \approx -1.2$) drastically deflates their actual ranking power. In bounded RRF, $3\times$ functioned as an insurmountable priority tier; in an additive log-odds sum, $+1.1$ is easily overridden by minor lexical or semantic score variations, destroying the definitions-first ordering that is the repository's single strongest ranking lever (+0.157 nDCG@10).
2. **The Incoherence of Rank-Based Likelihood Ratios (Decision 1):** The proposal leans toward deriving evidence from *ranks* via a shared curve $\lambda(r)$. But rank is a query-dependent ordinal, not an evidence metric. Summing $\log \lambda(r)$ across groups produces a multiplicative rank product, not RRF. It introduces intractable boundary conditions: what evidence does a group contribute to candidates outside its retrieval pool (e.g., past rank 400 in cosine, or having zero lexical matches)? Assigning $\log \Lambda = 0$ ("neutral") violates the law of total probability and privileges sparse queries over dense ones.
3. **The Hidden Spaghetti Inside the "Words" Group:** The proposal claims "composition is addition" across groups, but sweeps six messy, interacting factors (BM25 exact, stem BM25, phrase boost, proximity, density, and headings) into the "Words" group without providing an internal composition rule. The heuristic multiplier soup Joseph complained about is merely moved inside the group boundary.

Below is a detailed analysis of these findings, an audit of the individual hypotheses, recommendations on the four decisions for Joseph, and a concrete path forward.

---

## 1. Core Strengths of the Proposal

1. **The Hypothesis Register is the Right Abstraction:**
   Requiring every ranking signal to specify *Feature*, *Hypothesis*, *Impetus*, *Encoding*, *Fixture*, and *Status* permanently halts unprincipled tinkering. Making refuted hypotheses permanent register entries prevents repeating past failures (e.g., H-W5 Density, which hurt single-word queries).
2. **Clean Separation of Pre-Evidence Massaging (§4 Query and Text):**
   Classifying tokenization, OCR repair, case folding, and normalisation as "Query and text" rules rather than ranking evidence is a vital conceptual clarification. It exposes bugs that previously lurked in the plumbing (such as the hyphenation mismatch between `text.WORD_RE` and `match.py`, and the case sensitivity discrepancy between BM25 and the concordance).
3. **Unification of Phrase and Proximity:**
   Recognizing that H-W3 (phrase match) is simply the boundary condition ($\text{gap} = 0$) of H-W4 (proximity) resolves an active double-counting bug in `hybrid` today, where phrase matches receive both a $2\times$ lexical boost and a $1.6\times$ proximity boost.
4. **Disentangling Relevance from Scope and Governance (H-D1 to H-D3):**
   Recognizing that catalog Influence is prestige/reach (not relevance) and that superseded status is a scope/history concern rather than a topical penalty brings overdue rigor to the document-level factors.
5. **Decoupled Unit Fixtures via Pure Functions (§5.1, §7):**
   Requiring ranking functions to operate purely on in-memory text and corpus statistics—allowing unit tests in `search/fixtures/` without touching Postgres or Ollama—will drastically accelerate development and prevent regression.

---

## 2. Critical Mathematical & Architectural Issues

### 2.1 The Multiplier Translation Fallacy (Definition Deflation)

In §3, the proposal states:
> *"Today's multipliers already are likelihood ratios in disguise. The definition boost of 3 says a definition is three times as likely to be relevant. They translate directly into this model."*

**This claim is mathematically and empirically false.**

In the current implementation (`rank.py` lines 428–442), base scores come from RRF:
$$s_{\mathrm{RRF}}(p) = \frac{1}{60 + r_{\mathrm{sem}}(p)} + \frac{1}{60 + r_{\mathrm{lex}}(p)}$$
The theoretical maximum base score for a candidate ranking #1 in both legs is $\frac{1}{61} + \frac{1}{61} \approx 0.0328$. A candidate ranking #5 in lexical and #10 in semantic receives $\approx 0.0154 + 0.0143 = 0.0297$.
When a definition match occurs, `hybrid` multiplies this base score by $3.0$:
$$0.0297 \times 3.0 = 0.0891$$
Because no non-definition passage can ever exceed $0.0328$, the $3.0\times$ multiplier acts as an **absolute hierarchical partition**. It guarantees that an exact definition appears above all non-definitions, regardless of how high the non-definitions score.

Now consider the proposed additive log-odds translation:
$$\text{Score} = \log O(R) + \log \Lambda_{\mathrm{words}} + \log \Lambda_{\mathrm{meaning}} + \log \Lambda_{\mathrm{role}} + \dots$$
If the definition boost of 3 is translated to $\log \Lambda_{\mathrm{role}} = \ln(3) \approx +1.10$:
- Consider Passage A (an exact glossary definition): $\log \Lambda_{\mathrm{words}} = +2.5$, $\log \Lambda_{\mathrm{meaning}} = +2.0$, $\log \Lambda_{\mathrm{role}} = +1.10$. Total score = **$+5.60$**.
- Consider Passage B (a dense chapter with 8 mentions of the term and high semantic overlap, but not a definition): $\log \Lambda_{\mathrm{words}} = +4.2$, $\log \Lambda_{\mathrm{meaning}} = +3.5$, $\log \Lambda_{\mathrm{role}} = 0.0$. Total score = **$+7.70$**.

Passage B easily crushes Passage A by more than 2 full log-odds points. The glossary definition drops from #1 to #5 or lower.

**Why did this happen?** Because in Bayesian reality, when a user queries a technical term, the likelihood ratio of a definition being relevant is **not** 3:1. If $P(\text{def} \mid R) \approx 0.30$ and $P(\text{def} \mid \neg R) \approx 0.005$, the true likelihood ratio $\Lambda_{\mathrm{def}} \approx 60$, which corresponds to $\log \Lambda_{\mathrm{def}} \approx +4.1$.
A multiplier of 3 only worked in `hybrid` because it operated on a bounded reciprocal denominator. In an additive log-odds model, the log-likelihood ratio for definitions must be calibrated to match the dynamic range of the Words and Meaning groups (typically $+3.0$ to $+5.0$).

The exact same problem in reverse affects negative multipliers:
- Section kind TOC penalty: today is $\times 0.3$. In log-odds, $\ln(0.3) \approx -1.2$. A TOC entry whose heading and lines match all query words can easily achieve $\log \Lambda_{\mathrm{words}} = +5.0$. Adding $-1.2$ leaves it at $+3.8$, easily allowing TOC lines to pollute the top 10. A TOC match should have $\log \Lambda \le -4.0$.

### 2.2 The Flaw in Rank-Based Evidence (Decision 1)

In §3.2 and §8 (Decision 1), the proposal leans toward deriving evidence from *ranks* rather than *scores*:
> *"From ranks, which is what RRF does. Each group ranks the candidates, and a passage's rank becomes evidence through one declared curve shared by all groups... My lean is to start from ranks, with one shared curve and equal weights."*

This recommendation contradicts the foundation of the proposed Bayesian model:

1. **RRF does not sum log-odds:**
   RRF sums reciprocal ranks directly: $\sum_g \frac{1}{k + r_g}$.
   In log-odds, evidence is additive in the log domain: $\sum_g \log \Lambda_g$.
   If $\Lambda_g(r) = \frac{1}{k + r}$, then $\log \Lambda_g(r) = -\ln(k + r)$.
   Summing these across groups yields:
   $$\sum_g \log \Lambda_g = -\sum_g \ln(k + r_g) = -\ln \prod_g (k + r_g)$$
   Maximizing this is equivalent to **minimizing the rank product** $\prod_g (k + r_g)$, which behaves completely differently from RRF! A rank product brutally penalizes any candidate that ranks poorly in just one leg (e.g., rank 1 in lexical and rank 800 in semantic gives $61 \times 860 = 52,460$, which loses to rank 50 in both: $110 \times 110 = 12,100$). RRF was chosen specifically because it was robust to one leg failing.
2. **The Boundary / Absence Problem:**
   What is the rank of a passage that has *zero* lexical hits? In `rank.py`, semantic search pulls 400 passages. Many contain none of the query words.
   What is $r_{\mathrm{words}}(p)$ for such a passage?
   - If $r = \infty$ and $\log \Lambda(\infty) = -\infty$, the passage is immediately discarded, destroying semantic search's ability to find paraphrases or translated terminology (e.g., connecting "developer" to "provider" in the EU AI Act).
   - If unranked passages are assigned $\log \Lambda = 0$ ("neutral"), then a passage with rank 400 in lexical search is either *better* than zero hits ($\log \Lambda(400) > 0$) or *worse* than zero hits ($\log \Lambda(400) < 0$). If rank 400 is $> 0$, then rank 400 is treated better than having no evidence, but rank 401 (outside the pool) gets 0. If rank 400 is $< 0$, then having an irrelevant match is worse than having no match at all.
3. **BM25 is Already a Log-Odds Model:**
   The proposal overlooks the theoretical history of Information Retrieval. BM25 is not an arbitrary heuristic that needs to be ranked and re-mapped; Stephen Robertson and Karen Spärck Jones derived BM25 specifically as a monotone approximation of the 2-Poisson log-likelihood ratio:
   $$\text{BM25}(q, p) \approx \log \frac{P(\mathbf{w} \mid R)}{P(\mathbf{w} \mid \neg R)}$$
   BM25 *already is* on a log-odds scale!
   Similarly, embedding cosine similarity $s = \cos(\mathbf{e}_q, \mathbf{e}_p)$ can be mapped to log-odds via standard logistic calibration (Platt scaling):
   $$\log \Lambda_{\mathrm{meaning}}(s) = \beta (s - s_0)$$
   where $s_0$ is the neutral cosine threshold (empirically around $0.45$–$0.50$, as confirmed by `weights.toml` `answerable.distance = 0.50`) and $\beta$ is a scaling factor.
   - When $s > s_0$, $\log \Lambda > 0$ (positive evidence).
   - When $s = s_0$, $\log \Lambda = 0$ (neutral).
   - When $s < s_0$, $\log \Lambda < 0$ (negative evidence).
   This avoids arbitrary rank truncation and preserves true score magnitude.

### 2.3 The "Equal Opportunity" Scale Normalization Fallacy

In §3.3, the proposal states:
> *"Every group enters with weight 1 on the same scale, until a measurement justifies something else."*

"Weight 1" is only meaningful if the *variance and dynamic range* of the signals are comparable.
If the Words group outputs log-odds in the range $[-5.0, +10.0]$ and the Meaning group outputs log-odds in the range $[-1.5, +2.0]$, assigning both a weight of $1.0$ is **not** equal opportunity—it allows the Words group to completely dominate the ranking.
Before weights can be set to 1, each group's output must be calibrated to a standardized evidentiary scale.

### 2.4 Unresolved Composition Within the Words Group

Section 3.1 states:
> *"Within a group, hypotheses compose by the group's own rule, stated in the group's register entry. For Words that rule is BM25, with phrase, proximity and heading as terms inside it."*

However, looking at §4:
- H-W2 encodes stems as $+ 0.5 \times \text{stem BM25}$.
- H-W3 encodes phrase as $\ell(p) \times 2.0$.
- H-W4 encodes proximity as $\times (1 + 0.6\pi)$.
- H-W6 encodes heading as $\ell(p) \times 1.2$.

These are the exact same heuristic multipliers from `rank.py`. BM25 does not natively support multiplying by headings or proximity.
If the project wants a principled Words group, it should use established probabilistic formulations:
- **BM25F (Fielded BM25):** Combine heading matches and body matches *before* non-linear saturation:
  $$\tilde{\text{tf}}(w, p) = \text{tf}_{\mathrm{body}}(w, p) + w_{\mathrm{head}} \cdot \text{tf}_{\mathrm{head}}(w, p)$$
- **Markov Random Field (MRF) / BM25-TP:** Integrate phrase and proximity as unigram, sequential dependence (adjacent phrase), and full dependence (unordered proximity window) potentials, whose log-probabilities sum linearly.

---

## 3. Findings on Specific Hypotheses

| ID | Hypothesis | Review Finding | Recommendation |
|---|---|---|---|
| **H-Q1** | Stop words | Dropping stop words from BM25 while keeping them in phrases creates inconsistencies. Questions ("what is X") trigger H-Q2 anyway. | Keep stop words in literal phrases; retain BM25 stop list. |
| **H-Q4** | Case rule | Postgres's `simple` dictionary and `bge-m3` lowercase everything, making Joseph's uppercase convention inoperative in ranking. | Keep case sensitivity in exact phrase/concordance only; do not attempt case-sensitive BM25 unless token collisions justify it. |
| **H-Q5** | Tokens | Hyphenated tokens ("loss-of-control") are split by the literal matcher but kept by `text.WORD_RE`. | **Bug.** Standardize on splitting hyphens into tokens with an implicit zero-gap phrase constraint. |
| **H-Q6** | Term identity | Singularising the last word ("Capabilities" $\to$ "capability") merges distinct terms in safety governance. | Restrict singularisation to known plural inflections; do not singularise if the plural is registered as an autonomous term. |
| **H-T3 / H-M2** | Context in embedding | Prepending document title and heading path causes short passages (navigation, footers) to score high on cosine. | **Indexing bug, not a ranking bug.** Weight heading/title context inversely to passage length, or truncate context for short snippets. |
| **H-W3 / H-W4** | Phrase vs Proximity | Double-counts phrase hits in `hybrid` today. | Merge: H-W3 is proximity with window size equal to term length and order preserved. Remove standalone `phrase_factor = 2.0`. |
| **H-W5** | Density | Correctly refuted. Density is redundant with BM25 term frequency saturation. | Keep status *refuted*. |
| **H-R1** | Definition boost | The $+2.0$ boost in `weights.toml` cannot translate to $\ln(3) \approx 1.10$. | Set log-odds evidence for exact definition to $+4.5$, narrower to $+1.5$. |
| **H-R2** | Section kind | $\times 0.3$ penalty cannot translate to $\ln(0.3) \approx -1.2$. | Set TOC/references log-odds penalty to $-4.0$. |
| **H-D1** | Superseded | Penalizing superseded versions with $\times 0.8$ clutters top results with historical drafts. | **Move to Scope.** Default to active versions only; require `--history` to search superseded docs. |
| **H-D2** | Influence | Influence represents corpus curation reach, not query relevance. | **Remove from ranking.** Restrict to a tie-breaker when log-odds scores are within $\epsilon = 0.05$. |
| **H-D3** | Recency | A $5\%$ recency boost biases against foundational definitions in older anchor documents. | Demote to tie-breaker or eliminate. |

---

## 4. The Downstream Contract with `outline.py`

`RANKING.md` currently does not address how the proposed ranking model interfaces with `search/srcsearch/outline.py`. This is an oversight, as the outline is the primary user-facing consumer of ranking scores.

In `outline.py`:
- Line 50 notes:
  > `HEAT = ((0.01, '█'), (0.02, '▓'), (0.05, '▒'), (0.10, '░'))`
  > *"Ranks rather than scores, because RRF compresses scores differently for a one-word query and for a question."*
- Line 22:
  > *"top is the best 2% (at least 10), near the next, to 10%... The tiers are ranks, not a judgment of relevance: a query nothing in scope answers still has a top 2%."*

`outline.py` was forced to use relative rank percentiles precisely because RRF scores have no absolute semantic meaning. An off-topic query still unfolded sections because the top 2% of passages were opened even when their true relevance was zero.

**The log-odds model completely solves this problem for `outline.py`:**
- A score of $\log O(R \mid e) = 0$ corresponds to $P(R \mid e) = 0.5$.
- A score $> 0$ indicates a passage is more likely relevant than not.
- A score $< -2.0$ indicates clear irrelevance ($P < 0.12$).
- The outline can replace arbitrary percentiles (top 2%) with absolute probabilistic thresholds (e.g., only open sections with $\log O > +1.5$). If an off-topic query is run, the entire outline remains folded, naturally signaling that the query has no hits.

---

## 5. Adjudication of the Four Decisions for Joseph (§8)

### Decision 1: Rank-based evidence or calibrated scores?
- **Claude's lean:** Start with ranks, one shared curve, equal weights. (*Confidence: moderate*)
- **Gemini's verdict: Reject Claude's lean; use calibrated scores.**
  *Rationale:*
  As demonstrated in §2.2, rank-based evidence in a log-odds framework creates a rank product that destroys RRF's tolerance for single-leg retrieval. It creates undefined boundary conditions for candidates outside top pools and makes "equal opportunity" impossible.
  BM25 is *already* an established log-odds formula. Embedding cosine similarity is cleanly mapped to log-odds via logistic Platt scaling: $\log \Lambda_{\mathrm{meaning}} = \beta(\cos - 0.50)$. Calibrated scores preserve magnitude, behave gracefully at candidate pool boundaries, and fulfill Joseph's request for a defensible mental model.

### Decision 2: Status, Influence, and Recency (H-D1 to H-D3)
- **Claude's lean:** Influence out of ranking (ties only); Superseded to scope (`--history`); Recency stays weak prior. (*Confidence: moderate-low*)
- **Gemini's verdict: Adopt Claude's lean on Influence and Superseded; eliminate Recency from relevance.**
  *Rationale:*
  - **Influence:** Reach is not relevance. Using it in scoring distorts specialized queries. Keep it strictly as a secondary tie-breaker.
  - **Superseded:** Historical drafts should not be mixed with active standards. Fulfilling this via scope (`--history`) is clean and avoids polluting search results.
  - **Recency:** In safety governance, foundational documents (e.g., older NIST or early frontier lab commitments) frequently define terminology better than newer incremental updates. A recency multiplier arbitrarily penalizes canonical definitions. Drop recency from relevance scoring entirely; allow an explicit `--sort recent` flag if a user requests chronological ordering.

### Decision 3: The Migration Path
- **Claude's lean:** Build the new model beside today's as `--fusion evidence`, run evaluations and ablations. If no worse, switch default. (*Confidence: high*)
- **Gemini's verdict: Strongly Endorse.**
  *Acceptance Criteria:*
  1. Mean nDCG@10 on `search/eval/pilot-check` must not drop below the existing baseline (**0.802** across the 16 pilot queries).
  2. Definitions-first ordering must not regress on term queries (e.g., "hazard", "catastrophic risk").
  3. `search/eval/outline-check` must show equal or improved section opening efficiency at budgets 60, 120, and 200 lines.
  4. `--explain` must print strictly additive terms that sum exactly to the final score.

### Decision 4: Synthetic Corpus for Fixtures
- **Claude's lean:** Write synthetic corpus in `search/fixtures/`, starting with one case per hypothesis.
- **Gemini's verdict: Strongly Endorse.**
  *Implementation detail:* Ensure the fixtures test pure functions without database dependencies. Each fixture should assert an ordinal invariant: e.g., for H-W4, `score(p_adjacent) > score(p_sent_break) > score(p_para_break)`.

---

## 6. Recommended Action Plan

1. **Phase 1: Plumbing and Bug Fixes (Low Risk, Immediate Gain)**
   - Unify tokenization between `match.py` and `text.py` for hyphens (H-Q5).
   - Merge H-W3 (phrase) into H-W4 (proximity) to eliminate double counting.
   - Move `superseded` from a ranking multiplier to a scope filter (`--history`).
   - Move `influence` from a ranking multiplier to tie-breaking.
2. **Phase 2: Build the Calibrated Log-Odds Combiner (`--fusion evidence`)**
   - Implement `search/srcsearch/rank/combine.py` using calibrated log-odds:
     $$\text{Score} = \text{BM25F}_{\mathrm{exact+stem+head}} + \text{Proximity}_{\mathrm{mrf}} + \beta(\cos - 0.50) + \log \Lambda_{\mathrm{role}}$$
   - Calibrate $\log \Lambda_{\mathrm{role}}$: set exact definitions to $+4.5$, narrower to $+1.5$, TOC/references to $-4.0$.
3. **Phase 3: Verification Against Baselines**
   - Run `search/eval/pilot-check --fusion evidence` and verify against the $0.802$ baseline.
   - Run `search/eval/outline-check` to confirm outline section coverage does not regress.
   - Run `search/eval/hypotheses` ablations to confirm each active hypothesis contributes positive gain outside its bootstrap interval.
4. **Phase 4: Deprecate `hybrid` and Connect to `outline.py`**
   - Switch `--fusion evidence` to the default.
   - Update `outline.py` to use calibrated log-odds score thresholds instead of rank percentiles.

---
*End of Review.*
