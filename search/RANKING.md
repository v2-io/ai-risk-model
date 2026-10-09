# Ranking: the hypotheses, and the model that combines them

*A proposal, drafted 2026-10-09 by Claude (Opus 5.5) at Joseph's request. Nothing here is built yet. It describes how `hybrid` ranks today (§2), proposes a model to replace it (§3–§5), and sets rules so the model keeps being re-examined (§6). The decisions for Joseph are in §8.*

## 1. Why

Joseph, 2026-10-09: "it's really easy to keep churning on the hybrid model and adding more edge-cases and heuristics and adjustments and it becomes spaghetti really quickly-- pretty much every time you see a result way out of place and recognize intuitively that something is clearly wrong." He asked for factors that are "very well principled, individually checked, simulated even with fixtures and mock results"; for a foundation, "something bayesian or even the principle of giving weights equal opportunity until something specific justifies a non-uniform weighing of the factors", with the justifications recorded; and for code whose organisation "mirrors a clean and well-organized defensible mental model of the algorithm".

He added the form the factors should take: each written as a hypothesis, apart from its math, so that "the underlying assumptions can be challenged or composed together independent of the math". He sketched one, for proximity, and then said of the sketch: "my notation was deficient, and I was using a very oversimplified model of proximity, I know". It is kept as H-W4's impetus; the formal statements in the register are mine.

`hybrid` is already drifting the way he describes. Every weight in `search/weights.toml` has a recorded reason, and most have a measurement, but the factors don't form one model. Two symptoms from the same day:
- Proximity did nothing when folded into the lexical score, because the fusion keeps only the lexical *rank*. So it was moved to multiply the fused score, where it had an effect. That was locally sensible, but no model said where proximity belonged.
- `figure = 0.3` was set after one result looked wrong (IASR's chart data ranked first for "hazard"), with the reason "set like a contents page" and no measurement.

## 2. What `hybrid` does today

As read from `search/srcsearch/rank.py` (`search`, `lexical`, `proximity_density`, `definition_matches`) and `search/weights.toml`, 2026-10-09:

1. **Candidates:** every passage holding any query content word, the 400 passages nearest by cosine, and every passage defining the query's term. Nothing else is scored, and the outline treats the rest as having no hits.
2. **A lexical score:** BM25 on exact word forms, plus BM25 on Postgres's English stems at weight 0.5. It is then multiplied by 2.0 if the query occurs as a phrase, and by 1.2 if every query word is in the passage's heading path.
3. **A semantic distance:** cosine distance between the query's embedding and the passage's. A passage's embedding input is the document's title, the heading path and the passage text.
4. **Fusion:** reciprocal rank fusion, where $r_{\mathrm{sem}}(p)$ and $r_{\mathrm{lex}}(p)$ are the passage's semantic and lexical ranks and $k = 60$:

   $$s_{\mathrm{RRF}}(p) = \frac{1}{k + r_{\mathrm{sem}}(p)} + \frac{1}{k + r_{\mathrm{lex}}(p)}$$

5. **Then seven multipliers on the fused score**, so that

   $$s(p) = s_{\mathrm{RRF}}(p) \prod_{j} f_j(p)$$

   with these $f_j$:
   - defines the term: $1 + 2\,m\,c$, where the match $m$ is 1 for the exact term and 0.25 for a narrower one, and $c$ is the detection's confidence;
   - section kind: $0.3$ for toc, references, index and figure; $0.5$ for abbreviations; $0.7$ for restored text;
   - superseded: $0.8$;
   - Influence: $1.10$ for anchor, $1.05$ for major, $0.95$ for context;
   - recency within the organisation: $1 + 0.05\,y$, where $y \in [0, 1]$ is the document's position among its organisation's documents by year;
   - proximity: $1 + 0.6\,\pi(p)$, with $\pi$ the proximity score of H-W4;
   - density: off (weight 0).

That makes 13 factors with 27 tunable values, in three different places: inside the lexical score, inside the fusion, and multiplied on top. The fused score has no meaning of its own: a sum of reciprocal ranks, times priors stated on another scale.

RRF itself, as I remember its source (Cormack, Clarke and Büttcher, SIGIR 2009; not re-read for this), is an empirical finding: summing $1/(k + r)$ beat fancier fusion methods, and $k = 60$ was a tuned constant. What it gives is robustness, since it needs no calibrated scores. It has no theory of evidence, so nothing in it says how a prior multiplier should relate to the fused rank.

## 3. The proposed model

**Score = the log odds that a passage is relevant to the query.** Let $R$ be the event that passage $p$ is relevant to query $q$, and $e_g$ the evidence of group $g$. If the groups' evidence is roughly independent given $R$ and given $\neg R$, Bayes' rule gives

$$\log O(R \mid e) = \log O(R) + \sum_{g} \log \Lambda_g(e_g), \qquad \Lambda_g(e_g) = \frac{P(e_g \mid R)}{P(e_g \mid \neg R)}$$

where $O(R)$ is the prior odds that the passage is relevant, and the likelihood ratio $\Lambda_g$ says how much more likely a relevant passage is than an irrelevant one to show the evidence $e_g$.

What this buys:
- **Every factor has one meaning:** a likelihood ratio, or a prior. A factor that tells us nothing has $\Lambda = 1$, a term of $0$, so "neutral" is built in.
- **Composition is addition.** A factor can't sit in the wrong place, because there is only one place.
- **`--explain` becomes exact:** the terms printed add up to the score.
- **Today's multipliers already are likelihood ratios in disguise.** The definition boost of 3 says a definition is three times as likely to be relevant. They translate directly into this model. What doesn't translate is the RRF base, which is why it is replaced (§3.2).

### 3.1 Groups, because the signals aren't independent

Summing is only right for evidence that is roughly independent given relevance, and several of today's signals measure the same thing. BM25, stems, phrase, proximity, density and heading all measure overlap between the query's words and the passage's. Summing them as separate likelihood ratios would count the same evidence several times. So the hypotheses (§4) are grouped, and only groups are summed:

| Group | What it measures | Hypotheses |
|---|---|---|
| **Query and text** | not evidence: what the query is and what text a passage presents, before any group sees them | H-Q1 to H-Q7, H-T1 to H-T3 |
| **Words** | the query's own words in the passage: which, how rare, how close together, where | H-W1 to H-W6 |
| **Meaning** | the passage says something like the query, in any words | H-M1, H-M2 |
| **Role** | what the passage is in its document: a definition, a contents line, a figure label | H-R1 to H-R3 |
| **Document** | which document it is in: its status, its reach, its age | H-D1 to H-D3 |

Within a group, hypotheses compose by the group's own rule, stated in the group's register entry. For Words that rule is BM25, with phrase, proximity and heading as terms inside it. Across groups, the log-odds terms add.

The groups aren't fully independent either: a passage that uses the query's words also tends to be close in meaning. This is the main assumption the model rests on, and §6 says how it is checked.

### 3.2 Each group's evidence on one scale

To add, each group's raw signal must become a log likelihood ratio. There are two ways, and the choice is open (§8):

- **From ranks**, which is what RRF does. Each group ranks the candidates, and a passage's rank becomes evidence through one declared curve shared by all groups: the top of a ranking is strong evidence, and the evidence falls away with rank. This keeps RRF's robustness, since raw scores are never compared across groups. It makes the shape of the curve a stated hypothesis (H-F1), not a constant.
- **From calibrated scores.** Each group's raw score (a BM25 value, a cosine distance) is mapped to a log likelihood ratio by a monotone curve fitted to judged data. This uses more information, since a much better match counts for more than a slightly better one. But BM25's scale moves with the query, and the judged data are small (§5.3).

My lean is to start from ranks, with one shared curve and equal weights, and to try calibrated scores later, group by group, where the data allow. *Confidence: moderate.*

### 3.3 Equal opportunity

Every group enters with weight 1 on the same scale, until a measurement justifies something else. Joseph's principle, and memorata's "co-equal common factors" (Joseph, 2026-07-09), is the same rule. A weight other than 1 needs:
- an entry in the register saying why;
- a fixture showing the factor does what its hypothesis says;
- an ablation on both evaluations, recorded with its interval.

Weights fitted to the judged data are marked as fitted, with the data they were fitted on (§5.3).

## 4. The hypothesis register

Each entry has:
- **Feature:** what is observed, in notation like Joseph's.
- **Hypothesis:** the claimed relation to relevance, with its direction and shape.
- **Impetus:** why it was proposed, and by whom.
- **Encoding:** how the math says it, kept apart so the hypothesis can be challenged on its own.
- **Fixture:** the synthetic case that would show it working.
- **Evidence and status.**

Statuses: *proposed* (no test), *fixture-checked*, *measured* (an ablation on the evaluations, with its result), *calibrated* (weight fitted to data), *refuted* (measured, and it hurt or did nothing; kept in the register with the measurement, so it isn't proposed again unknowingly).

Notation: $q$ is the query, with content words $w_1, \dots, w_n$; $p$ is a passage, of $|p|$ words; $d$ is its document; $f(w, p)$ is the number of times $w$ occurs in $p$; $N$ is the number of passages, and $n_w$ the number holding $w$.

### Query and text: what counts as a match

These come before any evidence is scored. They decide what the query is and what text a passage presents, so an error here reaches every group below. Joseph, 2026-10-09: "our lexical massaging is essentially hypotheses on the search-term -> result-relevance". They were implicit in the code until this entry; all are *proposed* unless marked.

**H-Q1 Content words.**
- Feature: q's words minus a stop list ("a", "of", "the" … and "what", "how", "does", "which", "we", "our"; `rank.STOP`).
- Hypothesis: function words carry no evidence of relevance.
- Encoding: dropped from BM25 and proximity, but kept by the phrase factor and the concordance, where "loss of control" needs its "of".
- Open: that's two rules for one question. "What" and "how" are on the list because questions use them, which is a separate claim (H-Q2's kind).

**H-Q2 Definition intent.**
- Feature: q begins "definition of", "what is", "define", "meaning of" (`rank.DEF_INTENT`).
- Hypothesis: such a query asks about the term after it, and a definition of that term is what's wanted.
- Encoding: the term is parsed out and drives H-R1.
- Status: measured with the v2 definition rule in the pilot.

**H-Q3 OCR repair.**
- Feature: "Al" in q where "AI" was meant (`corpus.fix_ocr_ai`).
- Hypothesis: a query typed from an uncorrected copy means "AI".

**H-Q4 Case.**
- Feature: capitals in q.
- Hypothesis, Joseph's convention: a capital means the user wants that case ("AI", not "ai"), and lowercase means either.
- Encoding: used by the concordance verbs and by `hybrid`'s phrase factor only. BM25 lowercases everything, and so, in effect, does the embedding. So in `hybrid` a capital mostly doesn't count.
- Open: whether that's right for ranking, or an accident of where Postgres's index sits.

**H-Q5 Tokens.**
- Feature: how q and p are cut into words.
- Hypothesis: the unit of matching is the word, with apostrophes inside a word kept.
- Encoding: inconsistent, found 2026-10-09. `hybrid`'s query words keep a hyphenated word whole ("loss-of-control" is one token, `text.WORD_RE`), while the literal matcher splits it into three. Postgres's parser does something else again. One of these is an unstated assumption; which should win isn't decided.

**H-Q6 Term identity for definitions.**
- Feature: a defined term and the query's term, each normalised: folded, unaccented, quotes, emphasis and a parenthetical abbreviation removed, the last word made singular (`text.norm_term`).
- Hypothesis: two terms that normalise alike are the same term ("Risks" = "risk"; "Floating point operations (FLOP)" = "floating point operations").
- Open: singularising the last word merges terms the project might keep apart. "Capabilities" as a defined term may not be "capability".

**H-Q7 Word forms.**
- Feature: what extends a word: the two spelling rules, up to four more letters, a free plural or possessive, function words kept whole (DESIGN §7.1); in BM25, Postgres's stems (H-W2).
- Hypothesis: these extensions are the same word, or close enough to count.
- Encoding: in `lexical` and in the phrase factor, the run-on; in BM25, stems.
- Status: the cap and spelling rules were measured on 18 key terms (DESIGN §7.1); stems against run-on as a ranking leg, measured (H-W2b).
- Open: the two encodings disagree by design, and that disagreement is itself unexamined.

**H-T1 The unit of relevance.**
- Feature: the passage: about 800–1,500 characters, never across a heading, one glossary entry or definition per passage, split at paragraphs then sentences, with one sentence of overlap (DESIGN §5.2).
- Hypothesis: relevance can be judged a passage at a time. The outline then aggregates passages to sections.
- Open: the overlap means one sentence can count in two passages.

**H-T2 What text counts.**
- Feature: indexed text drops link targets, link tooltips, image links and HTML (DESIGN §5.2), and OCR's "Al" is corrected.
- Hypothesis: these carry no evidence. IASR's tooltips repeat a full reference at every citation, which inflated counts from about 730 to 993.
- Status: measured for that count.

**H-T3 Query and passage embedded differently.**
- Feature: the query is embedded as typed, with no prefix (bge-m3 specifies none). A passage is embedded with its document's title and heading path before its text (H-M2).
- Hypothesis: a bare query should sit close to a passage carrying its context.
- Open: the asymmetry may be what lets the title dominate short passages (H-M2's known failure).

### Words

**H-W1 Term presence.**
- Feature: whether $w_i \in p$, with $f(w_i, p)$, $n_{w_i}$ and $|p|$.
- Hypothesis: a passage holding the query's words is more likely relevant. A rare word is stronger evidence than a common one, repeats count for less and less, and a long passage's matches count for less.
- Impetus: standard; BM25.
- Encoding: BM25, with $k_1 = 1.2$ and $b = 0.75$, and $\overline{|p|}$ the mean passage length:

  $$\mathrm{BM25}(q, p) = \sum_{w \in q} \mathrm{idf}(w) \, \frac{f(w, p)\,(k_1 + 1)}{f(w, p) + k_1 \left(1 - b + b\,\frac{|p|}{\overline{|p|}}\right)}, \qquad \mathrm{idf}(w) = \ln\left(1 + \frac{N - n_w + 0.5}{n_w + 0.5}\right)$$
- Status: measured. In the pilot, lexical search with the priors is "as good as anything" on term queries (0.79).

**H-W2 Exact form over stem.**
- Feature: $w_i$ matched exactly, or only through its stem ("developer" and "development").
- Hypothesis: a stem-only match is weaker evidence, because stems merge words this project keeps apart.
- Impetus: DESIGN §6.1, from the corpus's term collisions.
- Encoding: the lexical score is $\ell(p) = \mathrm{BM25}_{\mathrm{exact}}(q, p) + 0.5\,\mathrm{BM25}_{\mathrm{stem}}(q, p)$.
- Status: measured. Replacing stems with longer word forms scored −0.011, because the query word is often the derived form itself ("misalignment" needs "misaligned"). That variant is *refuted* (H-W2b).

**H-W3 Phrase.**
- Feature: $w_1 w_2 \dots w_n$ adjacent and in order, with any separators between them.
- Hypothesis: the query as a phrase is much stronger evidence than its words scattered.
- Impetus: pilot.
- Encoding: $\ell(p) \times 2$, the phrase found by the literal matcher. Before 2026-10-09 it never fired for "loss of control" (a bug).
- Status: measured, +0.001 fused and +0.045 by the lexical side alone.
- Note: H-W3 is the zero-gap case of H-W4. The model should say so, not count both.

**H-W4 Proximity.**
- Feature: for a passage holding at least two of the query's words, a window $W$ of $p$ that covers one occurrence of each word present. Its cost is
  - $\gamma(W)$, the words inside it beyond the query's own;
  - $\sigma(W)$, the sentences it spans;
  - $\rho(W)$, the paragraphs it spans;
  - $o(W) \in \{0, 1\}$, whether the words appear out of the query's order.

  These combine into one distance, and the window that matters is the cheapest:

  $$c(W) = \alpha\,\gamma(W) + \beta\,(\sigma(W) - 1) + \delta\,(\rho(W) - 1), \qquad c^{*}(p) = \min_{W} c(W)$$

- Hypothesis: the evidence of relevance falls as $c^{*}$ grows, with $0 < \alpha \ll \beta < \delta$: an extra word costs little, a sentence break more, a paragraph break most. Words out of order are weaker evidence than the same words in order.
- Impetus: memorata (Joseph, 2026-07-09); and Joseph's sketch on 2026-10-09 of relevance falling with the text between two query words.
- Encoding: memorata's `proximity_score`, with $\alpha = 0.03$, $\beta = 0.25$, $\delta = 0.6$. It doesn't search every window. It tries one per occurrence of the rarest word present, taking the nearest occurrence of each other word, and keeps the best closeness $\kappa$ among those windows $\mathcal{W}$. With $P$ the query words present, $|P|/n$ their share of the query, and $\bar{x}$ their mean exactness (an inflection counts $0.55$):

  $$\kappa(p) = \max_{W \in \mathcal{W}} \; \max\{0,\, 1 - c(W)\} \cdot 0.75^{\,o(W)}, \qquad \pi(p) = \frac{|P|}{n} \, \bar{x} \, \bigl(0.4 + 0.6\,\kappa(p)\bigr)$$

  It is applied as $\times (1 + 0.6\,\pi)$ on the fused score, a placement chosen by measurement, not by model.
- Status: measured, $+0.026$ (interval $-0.002$ to $+0.073$), most of it one query.
- Open:
  - The constants $\alpha$, $\beta$, $\delta$, $0.75$, $0.55$ and the floor $0.4$ are memorata's, not measured here. Each is a sub-hypothesis that a fixture can check.
  - $\pi$ mixes three claims (coverage, exactness, closeness) that belong to H-W1, H-Q7 and this entry respectively. Coverage and exactness are already counted by BM25 and the stem leg, so they are counted twice.
  - The unit of $\gamma$ (words, characters, tokens) is a choice. Joseph's sketch counted characters.
  - Linear decay clamped at $c^{*} = 1$ is one shape among several: exponential, $1/(1 + c^{*})$. The shape is part of the hypothesis.

**H-W5 Density.**
- Feature: count and rate of the query's words in p.
- Hypothesis: a passage that keeps returning to the words is more about them.
- Impetus: memorata.
- Status: *refuted* here. It cost one-word queries ("whistleblower" −0.084), where it is the only signal. Off.
- Note: it overlaps H-W1's term frequency, which may be why.

**H-W6 Heading.**
- Feature: $\{w_1, \dots, w_n\} \subseteq$ the words of the passage's heading path.
- Hypothesis: a passage under a heading naming the query is about it.
- Impetus: pilot (6 of the NRR's 79 "hazard" forms were in headings only).
- Encoding: $\ell(p) \times 1.2$.
- Status: proposed, untested.

### Meaning

**H-M1 Semantic similarity.**
- Feature: $\cos(\mathbf{e}(q), \mathbf{e}(p))$, where $\mathbf{e}$ is bge-m3's embedding.
- Hypothesis: closer in embedding space means more likely relevant, including for passages that never use the query's words.
- Impetus: standard. The pilot found fusion with lexical beats either alone, and the whole-document judges found much of what matters doesn't use the query's words (DESIGN §11 step 8).
- Status: measured as a group (in the pilot, cosine alone 0.654, against 0.761 fused with the priors).

**H-M2 Context in the embedding.**
- Feature: e(p) embeds the title, the heading path and p together.
- Hypothesis: context makes a bare clause findable as its document's ("(c) 'Catastrophic risk' means…").
- Impetus: DESIGN §5.4.
- Status: proposed.
- Known failure: a short passage's embedding is dominated by the title, so site navigation ranks first for "whistleblower" on SB 53. Either the hypothesis needs a bound (context weighted by the passage's length), or the failure belongs to H-R3.

### Role

**H-R1 Definition.**
- Feature: $p$ defines a term $t$, detected with confidence $c$, where $t$ is the query's term (exact), contains it (narrower), or is contained in it (broader).
- Hypothesis: a definition of the exact term is strong evidence; of a narrower term, weak; of a broader one, none.
- Impetus: Joseph, 2026-10-09: "Whether a chunk is part of something specifically designated as a glossary or definition or something might be very high factor."
- Encoding: $\times (1 + 2\,m\,c)$, with the match $m$ = $1$, $0.25$ and $0$ for exact, narrower and broader.
- Status: measured, the strongest single lever (lexical alone 0.540 → 0.697). The match values were fitted to judged misses, so they are optimistic.

**H-R2 Section kind.**
- Feature: p's section kind: toc, references, index, abbreviations, figure, restored.
- Hypothesis: these mention terms without saying anything about them, so a match there is weaker evidence.
- Encoding: $\times 0.3$ to $\times 0.7$ (§2).
- Status: measured for toc and references (pilot); proposed for the rest. `figure` was set after one bad result.
- Note: this is evidence about the passage's role, not a prior about it. A contents line holding "loss of control" is evidence of where the section is, which the outline uses.

**H-R3 Boilerplate.**
- Feature: site navigation, running headers, vote lines.
- Hypothesis: carries no information about any query.
- Status: proposed, not built. It is the other candidate cause of the SB 53 navigation result.

### Document

**H-D1 Superseded.**
- Feature: d is superseded by a later version.
- Hypothesis: an agent usually wants the current version.
- Encoding: $\times 0.8$.
- Status: proposed. Open: this is arguably scope (`--history` unfolds versions), not relevance.

**H-D2 Influence.**
- Feature: d's catalog Influence.
- Hypothesis: a document others copy from is more often the one wanted.
- Encoding: $\times 0.95$ to $\times 1.10$.
- Status: proposed, and doubtful. The catalog says outright that reach "is not relevance". It may belong to the ordering of ties, or to presentation, not to evidence.

**H-D3 Recency.**
- Feature: d's position among its organisation's documents by year.
- Hypothesis: newer is more often wanted.
- Impetus: Joseph: "Freshness of document, freshness within a source (company, institute)".
- Encoding: $\times (1 + 0.05\,y)$, with $y \in [0, 1]$ the document's position by year.
- Status: proposed. Like H-D1, it may be preference rather than relevance.

### Fusion and candidates

**H-F1 The rank curve.**
- Feature: a passage's rank $r$ within a group.
- Hypothesis: the evidence $\lambda(r)$ falls with rank. RRF's $\lambda(r) = 1/(60 + r)$ says it falls slowly: $\lambda(1)/\lambda(10) = 70/61 \approx 1.15$, so ranks 1 and 10 differ by 15%. That may undervalue the top of a ranking. Since RRF sums $\lambda$ rather than its logarithm, it also isn't a log likelihood ratio.
- Status: proposed; its shape is the main open choice (§3.2).

**H-C1 The candidate pool.**
- Feature: p is a candidate if it holds any query word, is among the 400 nearest, or defines the term.
- Hypothesis: every relevant passage is a candidate.
- Status: untested. The outline treats non-candidates as having no hits, so a miss here is silent.

**Not ranking, kept apart:**
- the collapsing of verbatim copies, which is presentation;
- the answerability cue, a label on the results, never a factor (`rank.answerability`).

## 5. Checking each hypothesis

### 5.1 Fixtures

The fixtures are a small synthetic corpus in `search/fixtures/`. Each case isolates one hypothesis and states the order it predicts:
- **H-W4:** two passages, identical except for the gap between $w_1$ and $w_2$ (one word; one sentence; one paragraph). Predicted order: smaller gap first, and a sentence boundary costing more than a few words.
- **H-R1:** a definition of the term against a passage that only uses it. Predicted: the definition first, and a broader term's definition not boosted.
- **H-R2:** a contents line holding the phrase against a body sentence holding it.

Fixtures test each hypothesis's encoding in isolation. They need each signal to be computable from text and corpus statistics without the database, so signals become pure functions, with the database only fetching inputs (§7). A fixture that fails means the encoding doesn't say what its hypothesis says. That's a bug, found before any evaluation is run.

### 5.2 Ablation

`search/eval/hypotheses` (proposed) runs both evaluations with each hypothesis switched off in turn, and prints each one's contribution with a bootstrap interval:
- `pilot-check`: 16 queries, pooled blind grades;
- `outline-check`: 12 queries × 5 documents, whole-document judgments.

A hypothesis whose contribution sits in the noise on both is marked for review. Not removal: a hypothesis can be right and simply untested by these queries. Its fixture still holds it to its claim. The printout is what the register's Evidence entries are updated from.

### 5.3 Calibration, and the data it may use

The judged data are small: the pilot's 16 queries, 160 graded results; and 12 queries × 5 documents of whole-document judgments, 469 stretches. Fitting many weights to them would fit the noise.

So calibration fits few parameters, one per group at most, and keeps fitting and testing apart. Fit on one set, report on the other, and say which. Equal weights stay the default wherever a fitted weight doesn't beat them outside its interval on the held-out set.

## 6. Keeping it re-examined

The register lives in this file, and nothing ranks without an entry in it. Concretely:
- **In the code:** every function that computes a factor opens its docstring with its hypothesis ID and one line stating the hypothesis, not just a pointer. The combiner lists the IDs it combines. `search/eval/hypotheses` fails if the combiner uses a factor with no register entry, or a register entry marked *refuted* is still switched on.
- **In `weights.toml`:** every value names its hypothesis ID. The existing rule stays: "Change a weight only with an eval run before and after, recorded in the commit message."
- **When a result looks wrong:** read `--explain`, find which hypothesis's term is mis-specified, check that hypothesis with a fixture, and change its encoding or its status. A new factor or a special case is the last resort, and enters the register as *proposed* with a fixture like anything else.
- **When to re-run the ablations** (each recorded in the register's dated Evidence):
  - when the corpus changes substantially (a reindex that moves many passages, as on 2026-10-09);
  - when judged data are added;
  - when the embedder or the chunker changes;
  - when a hypothesis is added, since composition can change what the others contribute.
- **The independence assumption (§3.1)** is checked directly. Across the judged data, compare how the groups' evidence correlates among relevant passages and among irrelevant ones. Strong correlation within one class means two groups are counting the same thing, and they should merge.

## 7. Code that mirrors the model

```
search/srcsearch/rank/
  candidates.py   H-C1: which passages are scored
  words.py        H-W1–W6: one Words evidence term
  meaning.py      H-M1–M2: one Meaning evidence term
  role.py         H-R1–R3: one Role term
  document.py     H-D1–D3: one Document term
  combine.py      §3: each group's evidence to the log-odds scale, summed; the one formula
  explain.py      the terms that sum to the score, each with its hypothesis IDs
```

Each module's pure functions take text and corpus statistics, and its fixture tests import them directly. The database code fetches inputs and nothing else. `rank.py`'s concordance, definitions and answerability functions aren't ranking and would move out of it.

## 8. Decisions for Joseph

1. **Rank-based evidence or calibrated scores** (§3.2). My lean: ranks first, with one shared curve, equal weights. *Confidence: moderate.*
2. **Whether status, Influence and recency are relevance at all** (H-D1–D3), or preferences that belong to scope, ties or presentation. My lean: Influence out of ranking, used only to order ties. Superseded becomes scope (`--history` unfolds versions; by default only the active version is scored, with a note that older versions exist). Recency stays as a weak prior until measured. *Confidence: moderate-low.*
3. **The migration.** My lean: build the new model beside today's as `--fusion evidence`, and run both evaluations and the ablations. If it is no worse beyond noise, switch the default and delete the old path. If it is worse, record where before deciding. *Confidence: high on the method.*
4. **The fixtures' corpus is ours to write**, and could also serve the outline. My lean: yes, and it starts with one case per hypothesis.
