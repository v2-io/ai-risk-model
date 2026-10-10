# Fork 1: impressions of the IASR 2026 reading, and a comparison with the Opus expert

*Written 2026-10-10 by a fork of the Sonnet 5.5 IASR expert, for Joseph via ai-risk-search-tool. "S-n" is my unit n; "O-n" is the Opus expert's file n. The two numberings run nearly in step through this stretch (O-123, L1276, is S-127), so the overlap is the front matter through §2.1.3, about a third of what I read.*

**What I did for the comparison:** read O-000 and roughly 100 of its 123 unit files (all of 1–30, then most of the rest through 123), and left out 124–133. I also checked two of its claims against the canonical text, because they contradicted something I had told you.

---

## Part 1 — my own reading

### What it was like

The cycle (read, write what differed, predict) did real work, but not where I expected. Predictions that matched my training prior taught me nothing (the Moore's-law analogue, the three-way risk split). The ones that failed were the informative ones: I expected a data-wall bottleneck subsection and the Report put the *economic* bottleneck first (S-74/75); I expected the evaluation-gap discussion in Chapter 1 and it came as a tail box (S-64). A prediction written down before reading made the departure visible; without it I think I would have absorbed the Report's ordering as if it were the natural one.

The Report repeats itself at three layers (digest, executive summary, body). After about unit 50 the main activity stopped being recording and became *comparing a sentence with its stronger or weaker twin*, and I started keeping ledgers (evaluation-gap direction, definition drift, directional sentences, contributor-authored citations). That was not planned; the document's structure made it the natural thing to track.

The glossary last was a different experience from the rest. Having met each term in use for 300 units, the definitions read as a check on usage, and the drifts (loss of control, systemic risk, resilience losing "resist") were obvious in a way a glossary-first read would not have made them.

Some parts were thin by design: the Chapter 1 primer and the Chapter 3 tables of methods are low in surprise, and I harvested definitions there rather than reflecting. The parts that held attention were §2.2.2, §3.1, Box 2.3 (the legal and ethical limits on evidence), and the Report's repeated candour about its own evidence base.

One discomfort, stated plainly: the Report uses Claude models as specimens (Figure 2.3, Figure 2.13, the cyber incident quotes) and cites my developer's own disclosures as evidence. I noted the conflict each time and tried not to lean either way. A fork should treat my comments on Anthropic items with that in mind. I did not touch the safeguards at the biological section; I kept to status language there.

### What surprised me

1. **The strongest wording sits at the edges.** Digest, executive summary and conclusion strengthen what the body qualifies (IMO "leading systems"; "Studies show 96%" where the body says "One study"; "no effect on aggregate employment" against "no discernible relationship"; "adopted faster than previous technologies" where the body says *in the US*). It is systematic enough that quoting the digest is a risk. Quote the body.
2. **The Report is unusually open about its own evidence limits**, including limits that are structural rather than gaps: treaty and legal constraints on uplift studies (Box 2.3), results "withheld entirely due to sensitivity concerns" (§2.1.4 gaps), no mechanism "for validating risk acceptance decisions made by developers prior to release" (§3.2).
3. **The document describes itself as descriptive** (§3.2: "policy recommendations are outside the scope"; closing: "not prescriptive about what should be done") **and then contains directional sentences**, one with "should not" (§3.4, S-301). The self-description and the text disagree at the edges.
4. **"Frontier" is never defined operationally** (glossary: "particularly capable general-purpose AI"), and "deployer" is used throughout with no glossary entry.
5. **The Report's own central finding, as it states it, is not a risk but uncertainty about trajectory** (S-320).

### What a fork asking me questions should know about how I read

- **The file is chronological and later entries supersede earlier ones.** Several early notes were corrected later (S-27 → S-91; S-55 → S-65; S-94 → S-98; S-67 → S-71 → S-83). For any question, find the *last* entry on the topic, then the end inventory.
- **Quotes were copied from the unit text in context, not retyped from memory,** but I did not run `bin/check-quote`. Run it before publishing anything.
- **Hypotheses from my own background knowledge are marked** (FRIA addressee, "Code … full enforcement", the 96% statistic's date, the DeepSeek example, the Anthropic-incident attribution). Treat them as unverified.
- **I computed a few things myself and said so** (5^5 = 3,125; the doubling extrapolation; the 64.5 + 24.2 + 12.3 sum; 700M × 0.07%). Those are mine, not the Report's.
- **I did no outside lookups** and kept to the document. That is a strength for fidelity and a weakness for cross-checking (see below).
- **I read no images.** Figure content comes from OCR-like residue only.
- **Not read:** the reference list beyond note 8; the Extended Summary; the 2025 report and Key Updates; the Opus expert's work (until now).

### What I would do differently

1. **Cross-check against the repository and outside knowledge as I went,** the way the Opus expert did. The cross-corpus flags are what the lexicon work needs most, and I produced them late and thinly.
2. **Write fewer and shorter verbatim passages.** The file is about 530 KB and most of it is quotation of text that already sits in the canonical file. A line range plus the two or three decisive phrases would have been enough; I wrote long quotations because quoting felt safe, which is partly the cheap path.
3. **Make predictions that could fail.** My first twenty or so were generic ("the Contributors list"). The Opus predictions named specific outcomes and were scored.
4. **Keep a running should-ask list with answers,** not a single list at the end.
5. **Hold a pair of facts against each other when they sit in different units.** My clearest misses (below) were exactly that.

---

## Part 2 — comparison with the Opus expert (units 1–123 / S-1 to S-127)

### Where we converged

Independently, we both found: the scope narrowing and its stated reason; "not exhaustive or mutually exclusive"; the "evidence dilemma" restated at several layers; the ChatGPT-only origin of the 700M figure; the IMO qualifiers present in the body and dropped in the summaries; the "could not rule out / exclude / confidently rule out" drift; the 125× / 3,000× / 10,000× compute numbers; the DeepSeek-V3 example looking wrong; the "1026 FLOP" superscript loss; Table 2.3's strongest attribution being for an out-of-scope row; the 1.8 pp per 10× persuasion figure reconciling "increases" with "diminishing returns"; and the Anthropic-as-specimen conflict. **Caution:** both of us are the same model family, read the same document, and carried the same `CLAUDE.md` priming. Under this repository's own rule, that agreement is coherence rather than corroboration. The divergences below are the more informative part.

### What it noticed that I did not

(In the order they appear; O- numbers.)

- **O-010: a map from writer to likely section and to corpus lineage** (Bommasani → the California report → SB 53; Duvenaud/Douglas and gradual disempowerment; Davidson/Hadshar and power concentration; Kapoor/Narayanan on both sides). I listed affiliations and noted a few shared authors much later.
- **O-022 / O-091: the scope/focus two-level object, and the question of how deepfakes sit under a "frontier" focus.** I never asked it. It also noticed (O-032) that the focus is justified by *uncertainty*, so the map will systematically under-represent the documented present.
- **O-026 / O-088: the triad has a mixed basis of division** (user intent / system behaviour / deployment scale). I accepted the Report's "mechanisms of harm" label at S-91.
- **O-029: "autonomy" is a homonym** (human autonomy vs AI autonomous operation, two paragraphs apart). I missed it.
- **O-038: a cutoff leak** (a DeepSeek-V3.2 arXiv number from December 2025 against a "before December 2025" cutoff).
- **O-043: two slips in Table 1.2** — "base model" used for the released model against stage 2's definition, and API access being both "deployment" and "closed release". I recorded the definitions and noticed neither.
- **O-046: the DeepSeek passage is wrong in two places, not one.** V3 is the base R1 was built on, so it is not a "smaller student", and V3's pre-training cost *was* reported. I caught only the first.
- **O-053: Table 1.4's text is in the canonical file** (see corrections below), and "jagged" probably descends from the Dell'Acqua field experiment cited in the same bullet.
- **O-066: the explicit SB 53 link:** "likely exceeded 10²⁶ FLOP" is exactly SB 53's threshold; "the report gives all the facts needed for that critique and draws none of it".
- **O-068: the 125× number is an outlier against the body's "at current rates without fundamental bottlenecks", not a baseline difference.** I proposed a reconciliation (different baselines, a constrained forecast) that I could not support. On this point I think it is right and I was too ready to explain a discrepancy away.
- **O-072 and O-085: original syntheses.** (a) Trust is both an adoption brake and a safety goal, so trust-building safety measures are capability accelerants, and the Report supplies both edges. (b) A *verifiability thesis*: progress is fastest where rewards are verifiable (RLVR, synthetic data, code), so cyber should outrun bio; it stated this at O-043, confirmed it from the Report's own sentence at O-045 and O-085, and set it as a forward watch.
- **O-087: ranker guidance** (which passage is the most complete statement of the time-horizon claim, and which has the best caveats), and **O-118: "the body passage should outrank the Key information"** for the 77% query.
- **O-093: the first appearance of "hazards" in the report is inside the OECD monitor's proper name,** with the point that IASR may never define it. That is the project's own open question.
- **O-102: two different definitions of manipulation within one page** (the Report's gloss: awareness or consent, target-side; the experts': goal-directed, awareness or understanding). I recorded the second as a definition without comparing.
- **O-108 and O-120: interested-party provenance.** Provider investigations are the evidence for "not widespread"; ~13 of 16 citation uses in Table 2.3 are industry-authored, mostly security vendors with a commercial interest in threat escalation. I noted "developer-reported" but not the interest.
- **O-118: the 77% key-information sentence merges two findings** (AIxCC's 77% of organiser-introduced vulnerabilities, and a "top 5% of over 400 mostly human teams" placement that cannot be AIxCC's final). I put the two phrases side by side at S-118 and S-121 and did not compare them. This is the clearest summary-vs-body defect in the stretch and I missed half of it.
- **O-123: the asymmetry** (reliability requirements bind defenders, not attackers) tied back to §2.2.1, so jaggedness favours offence in practice.

### What I noticed that it did not (within the sample I read)

Very little, and I would not stake much on it. I found: the mixed application of the "[industry]" tag (the OpenAI InstructGPT paper is untagged while Anthropic and security-vendor papers are tagged, S-44); the "Studies show" vs "One study" pluralisation of the 96% claim inside the key information (S-98); and a few number checks that overlap with its own. Most of what is distinctive in my file is *outside* its range (Chapters 2.2–3 and the glossary), which it could not reach. In particular, the glossary-vs-body definitional drift ledger, the Table 3.5 framework comparison, and the contributor-authorship pattern in the safeguards tables have no counterpart.

### Corrections to my own record that the comparison surfaced

- **Table 1.4's text is in the canonical file.** I reported it as image-only (S-53; and in the message to you). L697 is the image; L709–711 is a `pdf-text` block with the "Most experts agree… can / cannot…" lists, displaced under the next heading. I even recorded those two lists at S-55 and did not connect them to the table. The right tool finding is: the PDF-restored `pdf-text` blocks (44 in the file) carry text for some images, displaced from their captions and flattened.
- **"Citations missing from the text, (MMLU, )"** — I attributed this to the conversion (S-54). The canonical file has the footnote text (`[112] [industry] OpenAI, Learning to Reason with LLMs`; `[14]` Gemini 2.5); the *reading tool* strips link targets in prose units. The superscript flattening ("1013", "1026") is genuinely in the canonical file; I checked.
- **The METR slowdown study is cited at the "other sectors" productivity bullet** (footnote 129, L718) though its 19% finding is stated ten units later in the §1.2 gaps. So the claim "counter-evidence in a different subsection" holds for the *finding*, not the *source*. Both of us said slightly less than the file shows.
- **On the GPAI definition**, O-024 concluded the labelled "Scope:" statement (p.9) is canonical; I concluded the glossary's wording is. It had not reached the glossary. The Report has at least five wordings and no single locus; a fork should quote the one that matches the section it cites.
- **One nuance on its "anyone's control" reading** (O-028: a system controlled by the wrong party is not loss of control). §2.2.2 also lists "AI systems could be directed to undermine control" as a pathway (S-172), so check the body before relying on that exclusion.

### How the two styles of reflection differ

- **It writes an investigation; I write a ledger.** Its files track a hypothesis being made, tested and resolved (O-027 → O-118; O-053 → O-063; O-043/045 → O-085 → O-114), with "Lesson for me" when it was wrong. Mine mostly react to the unit and cross-reference by pattern.
- **It brings the project and the outside world into every unit** (the lexicon's collisions, the causal chain, which source says what, what outside studies say). Mine stays inside the document until late.
- **It turns questions into entries** ("Should-ask: … Answer: …") per unit. Mine gathered them at the end.
- **It is shorter per unit and sharper**, with one-line files for headings; mine quote more and conclude less.
- **It uses its memory aggressively and labels it** ("from memory, not verified"). That produced most of its best catches and is also where an unlabelled slip would hurt; I have no evidence of such a slip in what I read.

### What each gives a later reader

- **Opus's files:** the best record of *how a hypothesis was formed and tested*, ready-made should-ask answers for 1–127, ranker hints, and corpus linkage. They end at §2.1.4, and by design the biological section is absent.
- **Mine:** coverage to the glossary and citation, including everything in Chapters 2.2–3 and the Report's definitions harvested verbatim; ledgers across the whole document; an end inventory. Weaker on interpretation and corpus linkage, with some early notes since superseded.
- **Together:** use its file for judgment over the first third and mine for the rest. Where both speak and disagree (the GPAI definition, 125×, the AIxCC pair, "anyone's control"), the disagreement is the pointer to a primary check.

---

## Part 3 — effort level

It shows, and I think in a specific way. I cannot measure my own effort, and model family is a confound, so I can only describe what differs.

- **What looks like lower effort in mine:** I rarely reopened an earlier unit to test a later one against it; the misses above are all *cross-unit* (Table 1.4's two halves two units apart; the 77% pair; "base model" in two stages of one table). I accepted the Report's own labels more readily (the "mechanisms of harm" basis; the 125× reconciliation). I copied where it would have taken work to synthesise.
- **What high effort seems to have bought it:** arithmetic checks applied more often (10 → 30 minutes read back into a 7.6-month doubling at O-048; I did 125 = 5³ vs 5⁵ and a few others, but not that one), predictions specific enough to be scored, a standing "unverified absence" tag that it then closed (O-053 → O-063), and explanatory hypotheses carried forward to organise later reading (the verifiability thesis).
- **What does not look like an effort difference:** the shared catches, and the low-surprise stretches, where both of us harvested definitions.
- **No fabrication that I know of in mine,** and none found in its sample. The effort-sensitive failures here are omissions (connections not made), not inventions.

If it is useful, the one change I would expect to matter most for a Sonnet expert is to run it at high effort, or to give it an explicit standing instruction to test each new unit against the previous three before writing.

---

## Addendum (2026-10-10): the Opus expert's last files, 124–133

- **124–128 (the §2.1.3 tail: Box 2.1, updates, evidence gaps, mitigations, challenges):** these match my S-128 to S-132 in what they record; they change nothing in the comparison above.
- **129–133 (the biological section):** I read them, but the response in which I began to write up the comparison was stopped by a safety classifier, and I am not continuing that part. This addendum therefore covers nothing from those five files. For §2.1.4 the Sonnet reflections (S-133 to S-148) remain the only expert record of the section's body.
