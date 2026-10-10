# Ranking: the hypotheses, and the model that combines them

*Drafted 2026-10-09 by Claude (Opus 5.5) at Joseph's request, then revised the same day after reviews by Fable, Gemini and Grok (`influx/reviews/ranking-*-2026-10-09.md`). Nothing here is built yet. It describes how `hybrid` ranks today (§2), the model to replace it (§3–§5), and the rules that keep the model re-examined (§6). The decisions are in §8: Claude's, supported by Joseph, each with what should cause it to be revisited.*

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
   - proximity: $1 + 0.6\,\pi(p)$, with $\pi$ the proximity score of H-W4, computed only for the top 500 passages of the lexical ranking (others get 1, so being outside that head is never a penalty, and nothing past it is rescued by proximity);
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

### 3.2 It is a logistic regression

Fable's review (`influx/reviews/ranking-fable-2026-10-09.md`) named what §3's model is: a logistic regression. Gemini's review (`ranking-gemini-2026-10-09.md`) reached the same place by another road, that BM25 already approximates a log-odds and cosine similarity can be calibrated to one. Joseph, 2026-10-09: "It's interesting how often properly framing the problem in the first place helps clarify. It's also interesting how many otherwise adhoc heuristic-evolving 'solutions' turn out to have forgotten to treat it as a regression / prediction problem."

So the model predicts the probability that a passage is relevant from a vector of features $\mathbf{x}(p, q)$:

$$P(R \mid \mathbf{x}) = \sigma\Bigl(\beta_0 + \sum_{j} \beta_j \, x_j(p, q)\Bigr), \qquad \sigma(z) = \frac{1}{1 + e^{-z}}$$

Its log-odds is §3's sum, with each group's $\log \Lambda_g$ linear in that group's features. What the framing settles:
- **"Ranks or scores" stops being a dichotomy.** A feature can be a rank or a score; either way its coefficient is fitted. The earlier draft of this section leaned towards a fixed rank curve (H-F1). Both reviews argued against that, for a reason it had not weighed: rank evidence is relative to the scope and has no floor, so it can't say that nothing in scope is relevant. The outline and the answerability cue need exactly that.
- **"Equal weights" gets a meaning.** It was undefined while the features' scales differed. Fable's example: under an RRF-shaped curve a group's whole top ten spans $\ln(70/61) \approx 0.14$ nats, about the same as the Influence multiplier's $\ln 1.10 \approx 0.10$, so Influence alone could reorder it. With every feature standardised over the candidates, equal opportunity is a prior on the coefficients, pulling them towards each other until the data say otherwise.
- **The probability is testable.** The model claims a probability, not just an order, so its calibration can be checked: of passages it puts at $P = 0.7$, about 70% should be judged relevant.
- **What counts as relevant is fixed before fitting** (Grok). A grade-1 or grade-2 stretch is relevant, including a mention in a colliding sense: the pilot's judge graded the NRR's industrial "hazard" relevant, and those are mentions Joseph wants caught. That is a hypothesis about the project, not a detail of the evaluation, and a model fitted to "the AI sense only" would bury them.
- **Absence is a value, not a gap.** Every candidate gets every feature. Cosine is computed for all candidates, not just the 400 nearest, which is an exact scan and cheap. A passage with no query word has BM25 0, a real value whose coefficient is fitted. A non-candidate is the one remaining absence (H-C1). The reviewers disagree on what absence should mean. Fable: it is evidence like any other value. Grok: a group that didn't retrieve a passage should contribute nothing, because missing words treated as evidence against relevance would fight H-M1, whose whole job is the passage that never uses the query's words. Today's code gives a missing lexical rank about zero, by accident of $1/(60 + N)$. The fit decides it, and Grok's whistleblower criterion (§8.4) guards against the paraphrase being buried.
- **Today's multipliers are measured again, not translated.** They were measured on RRF's scale, so their register statuses drop back to *proposed* when the combiner changes, with the old measurements kept as impetus. The definition factor $1 + 2\,m\,c$ is the exception in form: it is exactly a mixture over whether the detection is right, so its shape survives and only its size is refitted.

### 3.3 Equal opportunity, fitting and testing

Features are standardised over each query's candidates. Coefficients start from a shared prior (ridge regression towards their common mean), so no feature gets more say than another until the judged data justify it. Joseph's principle, and memorata's "co-equal common factors" (Joseph, 2026-07-09), is that rule.

The two judged sets differ in kind (Fable's point):
- **The pilot's grades** cover only passages some ranking surfaced. They can't teach the model anything about what the ranker missed.
- **The whole-document judgments** cover everything their judges read, which is what fitting needs.

So the model is fitted on the whole-document judgments, by leave-one-document-out: five fits, each tested on the document it didn't see. The pilot's grades are the out-of-sample test. A feature that matters must hold its sign across the five fits. One whose coefficient changes sign is reported as unsupported, not tuned.

Any coefficient that ends up away from the shared prior needs its register entry, a fixture and a recorded fit, as in §5.

## 4. The hypothesis register

Each entry has:
- **Feature:** what is observed, in notation like Joseph's.
- **Hypothesis:** the claimed relation to relevance, with its direction and shape.
- **Impetus:** why it was proposed, and by whom.
- **Encoding:** how the math says it, kept apart so the hypothesis can be challenged on its own.
- **Fixture:** the synthetic case that would show it working.
- **Evidence and status.**

Statuses: *proposed* (no test), *fixture-checked*, *measured* (an ablation on the evaluations, with its result), *calibrated* (weight fitted to data), *refuted* (this encoding made the evaluations worse; kept in the register with the measurement, so it isn't proposed again unknowingly). An encoding that did nothing on these queries stays *measured*, with the queries named, since the queries may simply not test it (Grok). When an encoding changes, the Encoding line is the live one and the old one moves to a dated Evidence line.

Notation: $q$ is the query, with content words $w_1, \dots, w_n$; $p$ is a passage, of $|p|$ words; $d$ is its document; $f(w, p)$ is the number of times $w$ occurs in $p$; $N$ is the number of passages, and $n_w$ the number holding $w$.

### Query and text: what counts as a match

These come before any evidence is scored. They decide what the query is and what text a passage presents, so an error here reaches every group below. Joseph, 2026-10-09: "our lexical massaging is essentially hypotheses on the search-term -> result-relevance". They were implicit in the code until this entry; all are *proposed* unless marked.

**H-Q1 Content words.**
- Feature: q's words minus a stop list ("a", "of", "the" … and "what", "how", "does", "which", "we", "our"; `rank.STOP`).
- Hypothesis: function words carry no evidence of relevance.
- Encoding: dropped from BM25 and proximity, but kept by the phrase factor and the concordance, where "loss of control" needs its "of".
- Open: that's two rules for one question. "What" and "how" are on the list because questions use them, which is a separate claim (H-Q2's kind). And the two lists are opposites in places (Grok): `rank.STOP` drops "we", "our", "what", "how", "does" and "do" and keeps "not", "no" and "nor", while `match.FUNCTION_WORDS` does the reverse. One hypothesis should have one list, with the phrase keeping its function words by an explicit exception.

**H-Q2 Definition intent.**
- Feature: q begins "definition of", "what is", "define", "meaning of" (`rank.DEF_INTENT`).
- Hypothesis: such a query asks about the term after it, and a definition of that term is what's wanted.
- Encoding: the term is parsed out and drives H-R1.
- Status: measured with the v2 definition rule in the pilot.

**H-Q3 OCR repair.**
- Feature: "Al" in q where "AI" was meant (`corpus.fix_ocr_ai`).
- Hypothesis: a query typed from an uncorrected copy means "AI". The code is more careful than that: it leaves listed surnames and name-shaped references alone (Grok), and the hypothesis should say so, as well as the choice to run a document corrector on queries.

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

**H-Q8 Expansion through the lexicon** (proposed 2026-10-10).
- Feature: the query's terms resolved through the lexicon's per-source term mappings to each source's own wording ("loss of control" → the EU Code's "reliably direct, modify, or shut down"; "developer" → the AI Act's "provider").
- Hypothesis: a passage that states a mapped equivalent of the query's term, in its source's own words, is evidence of relevance much as the query's own words are, weighted by how close the mapping is.
- Impetus: the paraphrase gap. A quarter of what the whole-document judges marked never shares the query's words (DESIGN §11 step 8), and on 2026-10-10 the EU Code's loss-of-control definition ranked 105th by cosine for "humans can no longer shut down or correct the AI system". Embedding the text without its title or path didn't change that (0.493 against 0.567 for a generic "AI systems can…" passage), so the embedder itself is matching surface words.
- Decided against, 2026-10-10: fine-tuning the embedder on lexicon mappings. That would hide our translation decisions in the vectors, where they can't be seen, attributed or switched off, and freeze first-pass mappings. Joseph raised fine-tuning, Claude argued for explicit expansion instead, and Joseph agreed: "a potential new hybrid factor or flag that does lexicon-based permutations-- we'll stay model-agnostic still for now."
- Encoding: none yet. It needs the lexicon's mapping records (plan G4). `--explain` should name each mapping used, so every expansion is visible and can be checked.
- Open: a factor in the default ranking or an opt-in flag; how a closed ambiguity (`{a | b}`) expands; whether expansion also widens the candidate pool (H-C1), which it would have to in order to help at all.

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
- Open (Grok): the encoding and the hypothesis disagree. An exact match also matches its stem, so an exact hit gets the exact term *plus* half the stem term, while a stem-only hit gets the half. The hypothesis wants a stem-only match as its own, weaker term, present only when the exact form is absent.
- Status: measured. Replacing stems with longer word forms scored −0.011, because the query word is often the derived form itself ("misalignment" needs "misaligned"). That variant is *refuted* (H-W2b).

**H-W3 Phrase.**
- Feature: $w_1 w_2 \dots w_n$ adjacent and in order, with any separators between them.
- Hypothesis: the query as a phrase is much stronger evidence than its words scattered.
- Impetus: pilot.
- Encoding: $\ell(p) \times 2$, the phrase found by the literal matcher. Before 2026-10-09 it never fired for "loss of control" (a bug).
- Status: measured, +0.001 fused and +0.045 by the lexical side alone.
- Note: H-W3 is nearly the zero-gap case of H-W4, and the model shouldn't count both. Not exactly, though (Fable): proximity runs on the content words, so for "loss of control" its window is "loss … control" with "of" as a one-word gap, while the phrase runs on the full term. A passage reading "loss control" gets full proximity and no phrase factor. Which word list each uses is an H-Q1 decision showing up in two places.

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
- Status: measured for toc and references (pilot); proposed for the rest. `figure` was set after one bad result, and it doesn't reach the result's neighbour (Grok, 2026-10-09): for "hazard" on IASR, rank 2 is a figure *caption*, which the chunker files as body, so the figure weight never touches it. The hypothesis covers captions that only name a term; the encoding covers six section kinds. Either the feature is made to match the hypothesis, or captions get a hypothesis of their own (a caption can be the sentence that says what a figure is for). Retuning 0.3 is not the answer.
- Note: this is evidence about the passage's role, not a prior about it. A contents line holding "loss of control" is evidence of where the section is, which the outline uses.

**H-R3 Boilerplate.**
- Feature: site navigation, running headers, vote lines.
- Hypothesis: carries no information about any query.
- Status: proposed, not built. It is the other candidate cause of the SB 53 navigation result.

**H-R4 A summary inside the source** (proposed by the SB 53 expert, 2026-10-09).
- Feature: a passage that summarises the source it sits in: a legislative digest, an executive summary, a key-findings box.
- Hypothesis: such a passage is keyword-dense, so it ranks above the operative text, yet it can drop the qualifiers that decide a question. It is weaker evidence than the text it summarises, on the questions the summary gets wrong.
- Impetus: SB 53's Legislative Counsel's Digest drops "comply with" from the framework duty, the large-developer limit on the penalty, and "reasonable" in the internal-process duty, and once writes "internet use" for "internal use".
- Status: proposed. A whole-document reader is what finds this, since the summary and the operative text agree on the words.

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
- Status: proposed, and doubtful. The catalog says outright that reach "is not relevance". Grok's arithmetic: anchor against context is a factor of 1.16. With both sides at rank 1, that is 0.0361 against 0.0311, while one side falling from rank 1 to rank 10 moves the score only from 0.0328 to 0.0307. So "mild" is true beside a ×2.9 definition boost and false inside the top ten. Decided: out of ranking (§8).

**H-D3 Recency.**
- Feature: d's position among its organisation's documents by year.
- Hypothesis: newer is more often wanted.
- Impetus: Joseph: "Freshness of document, freshness within a source (company, institute)".
- Encoding: $\times (1 + 0.05\,y)$, with $y \in [0, 1]$ the document's position by year.
- Status: proposed. Like H-D1, it may be preference rather than relevance. A bug in the encoding (Grok): a missing year is read as year 0, the organisation's oldest (`year or 0` in `_recency`). The neutral 0.5 applies only when the key is missing altogether.

### Fusion and candidates

**H-F1 The rank curve.**
- Feature: a passage's rank $r$ within a group.
- Hypothesis: the evidence $\lambda(r)$, taken as a log likelihood ratio, falls with rank. RRF's $\lambda(r) = 1/(60 + r)$ says it falls slowly: $\lambda(1)/\lambda(10) = 70/61 \approx 1.15$. Read as a likelihood ratio, its top ten span $\ln(70/61) \approx 0.14$ nats, close to the Influence multiplier's $\ln 1.10 \approx 0.10$ (Fable's comparison). Read as a log likelihood ratio itself, they span only $1/61 - 1/70 \approx 0.002$. Either way the curve's scale, not any weight, decides how much a group can say.
- Status: *superseded* by §3.2. Rank evidence is relative to the scope and has no floor, so the model uses features with fitted coefficients instead. A rank can still be a feature if the fit supports it.

**H-C1 The candidate pool.**
- Feature: p is a candidate if it holds any query word, is among the 400 nearest, or defines the term.
- Hypothesis: every relevant passage is a candidate.
- Status: untested. The outline treats non-candidates as having no hits, so a miss here is silent. It can't be ablated, since there's nothing to switch off. The check is a count (Grok): of the judges' must-read stretches, how many hold no candidate passage. That count is the recall ceiling of the outline.

**Not ranking, kept apart:**
- the collapsing of verbatim copies, which is presentation;
- the answerability cue, a label on the results, never a factor (`rank.answerability`).

## 5. Checking each hypothesis

### 5.1 Fixtures

The fixtures are a small synthetic corpus in `search/fixtures/`. Each case isolates one hypothesis and states the order it predicts:
- **H-W4:** two passages, identical except for the gap between $w_1$ and $w_2$ (one word; one sentence; one paragraph). Predicted order: smaller gap first, and a sentence boundary costing more than a few words.
- **H-R1:** a definition of the term against a passage that only uses it. Predicted: the definition first, and a broader term's definition not boosted.
- **H-R2:** a contents line holding the phrase against a body sentence holding it.

Fixtures test each hypothesis's encoding in isolation. They need each signal to be computable from text and corpus statistics without the database, so signals become pure functions, with the database only fetching inputs (§7). Two requirements from Grok:
- **The fixture corpus states its background statistics** ($N$, $n_w$, $\overline{|p|}$), or a BM25 order is an artifact of statistics nobody wrote down.
- **Each case carries the negative its hypothesis also claims:** proximity abstains on one word; a broader term's definition isn't boosted; a missing year is neutral; a phrase match doesn't also get a full proximity term. H-R1's case names the strong competitor: an exact definition against a non-definition at rank 1 on both lists, plus a definition of a broader term. "A definition against a passage that only uses the term" would pass under almost any positive boost.

A fixture that fails means the encoding doesn't say what its hypothesis says. That's a bug, found before any evaluation is run.

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
- **The independence assumption (§3.1)** is checked directly, over the whole candidate pool with the whole-document labels mapped onto passages, not inside a judged top ten, which holds only passages today's ranker already promoted (Grok). Across the judged data, compare how the groups' evidence correlates among relevant passages and among irrelevant ones. Strong correlation within one class means two groups are counting the same thing, and they should merge.

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

## 8. Decisions

*Joseph, 2026-10-09: "I'm happy to go with your lean on anything-- I'm not going to be able to choose a better curve or priors or anything than you here. Mark your decisions as yours and supported by me and, if possible, what should cause someone to revisit it." So each decision below is Claude's, supported by Joseph. Each says what should cause someone to revisit it. They were made after Fable's and Gemini's reviews; Grok's review arrived after; decisions 3, 4 and 5 were revisited in its light the same day, and the sequence in 6 was changed.*

1. **The model is a logistic regression on standardised features** (§3.2), not a fixed rank curve. Words gets BM25 on exact forms and on stems, headings as a BM25F field, and phrase and proximity as additive features (Gemini's point that the Words group was still multipliers inside). Meaning gets cosine, computed for every candidate. Role gets the definition match times its confidence, and section-kind indicators.
   - Revisit if coefficients change sign across the leave-one-document-out fits, which means too little data for that many features: drop to fewer.
   - Revisit if the predicted probabilities are poorly calibrated, which means the independence or linearity assumption is wrong: consider monotone non-linear terms per feature, or interactions.
   - Revisit if the judged data roughly double, or the embedder or chunker changes.
2. **Fit on the whole-document judgments by leave-one-document-out; test on the pilot's grades** (§3.3).
   - Revisit when more judged data exist, or if the two sets disagree on a feature's direction. That would mean one of them is biased in a way not yet understood.
3. **Influence is out of ranking entirely, ties included** (changed after Grok's arithmetic, H-D2); reach belongs in `--by source` and the result's fields. Superseded versions become scope, as DESIGN §6.3 already specified: by default only the active version is scored, with a note that older ones exist, and `--history` brings them in. Recency is out of the default score; a sort option can come later if someone asks, and the missing-year bug (H-D3) is fixed whenever it returns.
   - Revisit Influence or recency if a study of what agents actually look for (the hallucination test's logs, DESIGN §11 step 8) shows them preferring anchor or newer documents beyond what relevance explains.
   - Revisit superseded if an agent misses content that exists only in an older version, for example text a later version dropped. That would call for a "dropped later" note rather than ranking.
4. **Built beside today's model as `--fusion evidence`; it becomes the default only if it passes**, and the old path is then deleted. To pass:
   - pilot-check no worse than 0.802 beyond its interval;
   - definitions still first on term queries;
   - outline-check no worse at 60, 120 and 200 lines;
   - `--explain`'s terms summing exactly to the score;
   - the predicted probabilities calibrated;
   - "catastrophic risk" still leads with the exact definitions;
   - "whistleblower" on SB 53 still surfaces the operative prohibition, which is semantic rank 1 and holds no query word.

   The first four criteria are Gemini's, the fifth Fable's, the last two Grok's. A 16-query nDCG can hold while either of those two moves.
   - Revisit if it fails: record where and why before deciding anything.
5. **Fixtures are ours to write**, in `search/fixtures/`, one case per hypothesis to start. Each states an order the hypothesis predicts (for H-W4, adjacent before a sentence apart, a sentence apart before a paragraph apart) and tests the pure function directly.
   - Revisit when a hypothesis is added or its encoding changes; its fixture comes with it.
6. **The order of work** (Grok's sequencing): first write the Words group's equation and its fixtures in the current module. That means one BM25 on exact forms, a stem-only term, one positional term whose best case is the phrase, and heading as its own small term. Only then split the code into the modules of §7, since a split freezes whatever composition is implicit that day. Moving the concordance, definitions and answerability functions out of `rank.py` is independent and can happen any time.
7. **The first measurement is Fable's, before any restructuring:** fit the logistic model to the features today's `--explain` already prints, over the judged data, and read the coefficients. That measures what the earlier draft could only lean on.
   - Revisit this plan if that fit shows the features as they stand already separate relevant from irrelevant well. Then the restructuring is about clarity, not quality, and can go at its own pace.
