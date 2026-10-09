# Judging notes: pool-1 (639 passages, 16 queries)

Judge: one Claude instance, the same model family as the pool author. It graded blind (no access to the draft gold set, the configurations or the rankings), read every passage in full, and checked the canonical texts in `ref/canonical/` where a chunk's context was unclear.

Grade totals: 3 = 55, 2 = 102, 1 = 211, 0 = 271.

## How the scale was applied

The suggested 0–3 scale fit well, and I kept it. Some boundary cases came up again and again, so I settled them with fixed rules. The eval should know these rules, because they move scores:

- **Term queries, other senses of the term.** A passage that uses the queried word in any sense gets at least a 1, as asked. That includes inflections ("hazardous", "flood hazard", "Control of Major Accident Hazards"). For the multi-word query "information hazard", a passage that has only "hazard" does not count as a mention, so those are 0.
- **The term appears only in the heading path.** The passage text never uses the term or touches the concept; only its section heading does (e.g. "...major hazard (COMAH) site › Impact on vulnerable people", or SB 53 Chapter 5.1 cross-reference definitions under "Whistleblower Protections"). These get 0. The parent chunk that carries the heading already covers that mention. Exception: when the child passage is substantively *about* the heading's subject, it is graded on that content. Example: OpenAI's "Potential claims" items under "Safeguarding against severe harm" got 1.
- **Definitions of compound terms.** In the term queries:
  - A designated definition of a *subtype* of the queried term gets 3 ("passive loss of control", "context-dependent misalignment", "known misalignment").
  - A definition of a compound term that characterises the concept gets 2 ("systemic risk source", "systemic risk tiers", "misalignment risk", "near miss", "'resolved' serious incident").
  - A definition of a *process* term over the concept gets 1 ("systemic risk management", "systemic risk assessment", "systemic risk modelling").
- **Counterpart terms in other sources.** When a source uses a different term for the same slot, its definition gets 2 when it is the closest counterpart: SB 53 "critical safety incident" for the query "serious incident", and the reverse; SB 53 "deploy" for the query "deployer"; the NIST "AI Deployment actors" for "deployer".
- **Generic "risk" definitions.** The IASR "Risk" glossary entry, AI Act Art 3(2), "Risk factors" and "Marginal risk" get 0 on compound-term queries ("catastrophic risk", "severe harm", "information hazard"). They are relevant only to the query "definition of risk". A reasonable judge might give these a 1 for touching the concept. I did not, because someone typing "catastrophic risk" does not want the bare definition of risk ranked among the results.
- **Obligations versus characterisation (actor and procedure terms).** A passage that just imposes a duty on a deployer, frontier developer or similar actor gets 1. A passage that says what the role *is* or why it matters gets 2 (e.g. AI Act recital 93 on why deployers are best placed to spot risks; IASR's lifecycle table setting developers beside deployers).
- **Bibliography entries, tables of contents, and page-footer legends** get 0, even when a reference title contains the term (e.g. "AI Whistleblowers" or "An Overview of Catastrophic AI Risks" in IASR Notes).

## Per-query notes

- **hazard.** Only one 3: the IASR glossary entry. NVIDIA is the one source that uses "hazard" as a working concept, with hazards that have frequency, duration, onset speed and predictability. I gave 2 to the NVIDIA passages that state those properties, and 1 to the long tail of NRR mentions in other senses (COMAH, natural hazards, flood hazard, "hazardous materials"). NRR "dangerous goods" (#364) got 1: it describes a hazard in the industrial sense without the word. The other dangerous-goods scenario passages got 0.
- **catastrophic risk.** The 3s are the two SB 53 definitions (#19 and #53, which are near-duplicates), Anthropic's footnote 1 (inside #19 of the risk report: "used in its plain meaning rather than … statutory definition") and NRR #36 ("Risks assessed to have the highest impact score (5) are considered catastrophic"). The NRR one is a judgment call, because it defines an impact *level* rather than the phrase itself. I graded it 3 because it is the NRR's operative definition.
- **severe harm.** The OpenAI definition (#2) is the only 3. The OpenAI tracked-category criteria, the High/Critical threshold definitions and the misuse-versus-misalignment routing got 2. Anthropic "catastrophic harm" passages got 1 as near-synonym mentions. NRR consequence lists with fatalities got 0. They describe harm, but say nothing about the *severe-harm* concept.
- **loss of control.** The pool is small (15) because the configurations largely agree. Every passage is relevant, and many are near-restatements of the IASR definition (main report, executive summary, extended summary, glossary, key-information bullets). It is the easiest query in the set, with little room to separate configurations.
- **developer.** There are many hits in the software-developer sense, or just from the URL "developer.nvidia.com". The bibliography hits ("Open-Source Developer Productivity") got 0. Passages using "developers" for staff (NVIDIA #50) got 1. Note: the AI Act's closest counterpart, the Art 3(3) "provider" definition, is not in the pool. Under a lexical reading that is correct, but given how the project uses this query, it is a recall gap.
- **definition of risk.** The 3s are AI Act Art 3(2), IASR "Risk", NIST §1.1 and NVIDIA's "We defined risk as…". The 2s are operationalisations and variants: NRR reasonable-worst-case framing, Anthropic's P×H×U decomposition, marginal risk, IASR "systemic risks" (with its contrast to the AI Act), and CoP recital (i), which ties interpretation to the AI Act's definition of "risk". Glossary entries for risk-management *processes* got 1.
- **humans can no longer shut down or correct the AI system.** The 3s are statements of the situation itself: the CoP definition ("losing the ability to reliably direct, modify, or shut down") and the IASR and extended-summary definitions of loss of control (including "resist attempts to shut them down"). The AI Act "stop button" (#378), recital 73 ("constraints that cannot be overridden by the system itself") and NIST §3.2 ("ability to shut down, modify, or have human intervention") got **2, not 3**. They state the *control* that guards against the situation, not the situation, but they are plainly relevant. IASR persistence (#280) and misalignment → resisting shutdown (#263, #286) got 2. Automation-bias passages, where humans fail to correct AI outputs, got 1: a different sense, but it matches the literal query. The OECD capability-scenario passages got 0.
- **difference between malicious and non-malicious risks.** The 3s are NRR #14 (non-malicious: accidents and natural hazards; malicious: threats from actors), NRR #32 (5-year versus 2-year assessment windows; intent × capability × vulnerability for malicious likelihood) and the IASR misuse/malfunction/systemic taxonomy (#156 and extended #19). The 2s are the Cohere row in IASR Table 3.x ("Malicious use" versus "Harm in ordinary, non-malicious use"), Anthropic's naturally-emerging versus engineered misalignment, and the "Malicious use" glossary entry. Passages that discuss only malicious use and draw no contrast got 0 or 1.
- **information hazard.** Exactly one relevant passage is in the pool: IASR #228, with the inline definition "information that may be harmful to share", graded 3. Everything else is 0. Matches on "hazard", "information", "OECD AI Incidents and Hazards Monitor" and misinformation are not mentions of this term. **The pool is missing known hits** in these ten sources:
  - Anthropic risk report, canonical line ~1287: "for infohazard reasons" (one word, so no lexical match);
  - NVIDIA, line ~318: WMDP as "a proxy evaluation for hazardous knowledge";
  - arguably IASR, lines ~617 and ~2205 ("dangerous knowledge").

  Pooled recall on this query will be overstated. This query is the clearest test of whether a configuration handles a rare term *and* its variants.
- **death or serious injury to more than 50 people or a billion dollars of damage.** This paraphrases the SB 53 threshold. Both SB 53 catastrophic-risk definitions got 3. Other severity thresholds got 2: OpenAI's severe-harm definition, the NRR impact-scale table (fatalities, casualties, £), the AI Act serious-incident definition and recital 155, SB 53 critical safety incident, and Anthropic's footnote about statutory thresholds. NRR scenario narratives that mention fatalities got 0. Anthropic's COVID-cost footnotes (#358, #359) got 0, and the threat-model magnitude passages got 1.
- **whistleblower.** The only 3 is the IASR "Whistleblowing" glossary entry. The SB 53 operative anti-retaliation provisions (#59, #61), the digest passages (#8, #9), the AI Act recital 172, the CoP non-retaliation measure and the link to the CoP–EU whistleblower directive got 2. The SB 53 "covered employee" definition (#54) got 2: it defines who is protected without using the word. Some would grade it 3.
- **misalignment.** This is the richest query: 11 definitions. Anthropic §2.5 has a whole definitions block, and IASR has a glossary entry plus its main text. Anthropic #64 got 3 because it continues the #63 definition ("we consider only active misalignment"); the chunker split the definition. Anthropic #119 (direct/emergent misalignment typology) got 2, not 3, because it sits inside an argument rather than the definitions section.
- **deployer.** The 3s are AI Act Art 3(4) and recital 13. Most AI Act passages are obligations (1). Glossary entries for "Deployment" and "Deployment environment" got 1 and 0 respectively.
- **serious incident.** The only 3 is AI Act Art 3(49). SB 53 critical safety incident got 2 as the counterpart, as did the CoP "near miss" and "resolved" definitions, the CoP reporting timelines keyed to the harm categories (#80) and recital (j). NRR narrative passages containing "incident" got 0.
- **critical safety incident.** The 3s are both SB 53 definitions. Anthropic's own incident-disclosure passages (#463, #464, #500, #542) got 1: they touch the concept of disclosing AI safety incidents, but none is an SB 53 CSI. That is a borderline call; 0 would also be defensible. NRR passages with "critical", "safety" or "incident" got 0.

## Problems with the passages themselves

- **Definitions split by chunking.** Anthropic misalignment definition #63 → #64. Emergent-misalignment definition #119 → #120 (cut mid-sentence). The CoP specified-systemic-risks lead-in (#139) is separated from its list. The CoP "nature of systemic risks" intro (#125) is separated from its characteristics. AI Act recital 110 (#168) is cut mid-sentence. NVIDIA Table 2 (#21) is cut after the header row, so the worked hazard-source → hazard example ("Adversarial prompt → Disinformation") is in another chunk.
- **Footnotes and bibliography mixed into body chunks.** NVIDIA chunks #17, #20, #35, #48 and #49 carry page-bottom references and URLs. Anthropic #19 has footnote 1 in the middle of a list. Anthropic #68 is a footnote-only chunk with `&lt;sup>` entity residue. AI Act #251 merges recital 171 with footnote 53.
- **Page-footer legend residue.** NRR chunks end with the risk-matrix legend ("140 Catastrophic 5 Significant 4 Moderate 3 …"). It gives lexical matches on "catastrophic" (#616, #567, #504, #480) and "significant". NRR #46 merges a list with matrix numbers.
- **Figure OCR text.** IASR #179, #189 and #319 are figure contents run together (e.g. #179 includes a model's chain of thought about avoiding shutdown, unreadable as prose).
- **Duplicates and near-duplicates.**
  - SB 53 #19/#53 and #20/#55 (parallel definitions in two code chapters, "frontier model" versus "foundation model").
  - OpenAI #45/#78 (identical text).
  - NRR "Impact on vulnerable people" flood passages #662/#670/#678 (identical sentence) and the repeated "Common consequences" boilerplate.
  - IASR main report / extended summary / glossary restating the same definitions.

  I graded the duplicates identically, so nDCG will reward a ranking that fills the top 10 with copies. Collapsing duplicates, or noting them in the report, would help.
- **Hub passages.** Some short glossary entries are in many pools: IASR "Risk" (#650) is in 8 of the 16, AI Act Art 3(2) in 6, IASR "Risk factors" in 5. They are short and generic, so their embeddings sit near many queries. This looks like a property of the embedding models more than of any one query.

## On the queries and the scale

- **Pooled recall is an upper bound.** "information hazard" shows it directly (see above), and the "developer" pool lacks the AI Act's "provider". If recall is reported, I would label it "recall within the pool".
- **A gap in the scale.** The scale has no grade for *the same slot under a different word*: provider/developer, CSI/serious incident, deploy/deployer. I used 2 for those. Since the project's method rests on mapping terms across sources, you might want to score counterpart-term retrieval as its own measure rather than fold it into graded relevance.
- **Some queries are much easier than others.** "loss of control" is close to saturated: every passage relevant, 8 of 15 graded 3. "information hazard" has one relevant passage. Averaged per query, these two will dominate the differences between configurations for opposite reasons. You might want to report per-query scores beside the mean.
- **The two kinds of query behave differently.** On term queries, the main way a configuration fails is other-sense and heading-only noise (NRR for "hazard"; bibliography hits for "developer"). On NL queries it is topical neighbours (OECD capability scenarios for the shutdown query; NRR malicious-incident scenarios for the malicious/non-malicious query).
- **The glossary signal Joseph asked about.** I counted the 55 grade-3 grades by the form of the definition (a passage graded 3 for two queries counts twice):
  - 17 sit in a section the chunker already labels "Glossary" or "Definitions" (IASR glossary; Anthropic §2.5);
  - 14 are statutory "X means…" or "the notion of X" clauses whose `section` field is **empty** (AI Act Art 3 and recitals, SB 53, CoP legal text). A heading-based glossary flag would miss all of these; it would need to detect the definition pattern itself;
  - 24 are definitional statements in running text: IASR key-information bullets, the executive and extended summaries, NRR #14/#32/#36, OpenAI's "By 'severe harm' … we mean", the "risk" definitions in NIST and NVIDIA, the CoP Appendix 1.4 list entry for loss of control, Anthropic's footnote 1, and the inline IASR #228.

  So a definition flag is likely to help, but only about a third of the gold 3s would be caught by section headings alone. Pattern detection ("means", "refers to", "we define", "by X we mean", a term followed by a colon at the start of a list item) would reach most of the rest.

## Batch 2 (pool-2, 59 passages; judgments-2.json)

These were graded with the same rules. Grade totals: 2 = 1, 1 = 23, 0 = 35. No grade 3.

- **information hazard.** Anthropic #220 ("call undue attention to misuse vectors for infohazard reasons") is the "infohazard" hit I flagged as missing from pool 1. It now appears, graded 1: it uses the term without defining it. NVIDIA's "hazardous knowledge" passage (~line 318) is still not in either pool.
- **developer.** IASR #421 got 2. It lists the actors along the AI value chain ("data and cloud providers, model developers, and model hosting platforms"), which bears directly on splitting "developer" into roles. The other IASR mentions of "AI developer" got 1.
- **Most of the new passages are short IASR glossary entries and risk-management table rows.** Examples: Risk management, Risk threshold, Safeguard, Safety, and Table 3.x rows. Most got 0, because none uses the queried term or touches its concept beyond generic risk vocabulary. This is the same short-glossary hub pattern noted above, and it looks stronger in the 8B model's additions than in pool 1.
- **Duplicates.** IASR #37 and extended #7 are near-identical bullets. Extended #62 also appears under both "developer" and "deployer".
- **"Al" for "AI".** I graded the extended-summary passages as if they read "AI". Nothing in this batch turned on that.

## Batch 3 (pool-3, 13 reranker-promoted passages; judgments-3.json)

These were graded with the same rules. Grade totals: 2 = 5, 1 = 4, 0 = 4.

- **developer.** AI Act Art 3(3) "provider" (#271) got 2. This is the counterpart I said was missing from pool 1, under the same-slot-different-word rule. The reranker found it, and no first-stage configuration did.
- **definition of risk.** AI Act Art 3(65) "systemic risk" and Anthropic's "misalignment risk" definition each got 2, matching the IASR "systemic risks" entry and Anthropic's P×H×U decomposition in batch 1.
- **difference between malicious and non-malicious risks.** IASR #173 got 2. It states the contrast directly: "Some malicious actors intentionally use AI-generated content …, while other harms … occur unintentionally."
- **loss of control.** IASR #279 (what loss-of-control scenarios would require) got 2, consistent with the other factor passages.
- **The rest.** The NRR attack scenarios for the casualty-threshold query got 0; AI Act recital 133 (synthetic content) for the shutdown query got 0, as did IASR #160 (which covers malicious use only, with no contrast) for the malicious/non-malicious query. IASR #333, on degraded skills weakening human oversight, got 1 for the shutdown query. The deployer obligations and the CoP serious-incident commitment got 1.
