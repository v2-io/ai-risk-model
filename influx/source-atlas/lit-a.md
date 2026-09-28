# Source atlas: lit-a (research and policy literature on loss of control, incidents, evaluation, audit, safety cases, regulation)

Twenty-two documents. For each: the table of contents, glossary or definitions, and 2 to 5 passages to read directly.

**How to read the ranges.** Line numbers refer to `…/scratchpad/src-text/<key>.txt` (from `pdftotext -layout`). Open a range with `sed -n 'A,Bp' <key>.txt`. Page numbers count form feeds: they are PDF page indices, not the numbers printed on the page. The two usually match for arXiv papers but not always. In Tkeshelashvili, printed page 1 is PDF page 6. In Hamin, the pages are artifacts, because that text is not a PDF extraction at all (see its entry). Page numbers were computed by script from the form feeds; none were typed by hand.

**What "read" means here.** I read every passage I list in full, and every TOC and glossary I cite, with one exception: of Brundage's glossary I read the full headword list and about a third of the entries. I did not read any document end to end except CLTR and Hamin. For the long documents I read the TOC, then sampled sections chosen from it. A document's unlisted sections may contain things that would change my one-liners.

---

## anderljung-2023-frontier — Frontier AI Regulation: Managing Emerging Risks to Public Safety (Anderljung, Barnhart, Korinek, Leung, O'Keefe, Whittlestone et al.)

2490 lines, 51 pp. A clean arXiv white paper with 24 authors. Lines 29-32 say that authorship "does not entail endorsement of all claims in the paper".

- **TOC:** **L170–212** (p. 5)
- **Definitions:** there is no glossary, but it has a whole appendix on how to define its central term. Appendix A "Creating a Regulatory Definition for Frontier AI" is at **L1607–1745** (pp. 34–36), and it concludes "none of the approaches we describe here seem fully satisfying". The working definition is in §2.1 (see passage 1). Controllability is defined in one line at 1155.
- **Passages:**
  1. **L257–376** (pp. 7–9): defines "frontier AI" by what models *could* do. Hedges it heavily ("it is not clear where the line … should be drawn"; "lacking in sufficient precision to be used for regulatory purposes"). The substance sits in footnotes: 1e26 FLOP, and why it avoids the term "general-purpose AI".
  2. **L379–440** (pp. 9–10): three named "Problems" (Unexpected Capabilities, Deployment Safety, Proliferation), each set up as a structural premise for the case for regulation.
  3. **L936–1003** (pp. 20–21): argues for licensing by analogy to aviation, pharma, banking, experimental aircraft and the Select Agent Program. A public-opinion poll appears in a footnote.
  4. **L1259–1339** (pp. 26–27): a four-tier risk-to-deployment mapping, with Table 3 giving *hypothetical* example systems for each tier. A classification is illustrated by imagined systems.
  5. **L1436–1532** (pp. 30–31): "Uncertainties and Limitations". It records disagreement *among the authors* ("An alternative, which some authors of this paper prefer…") and lists the regime's own possible harms (capture, centralization, abuse of government power).
- **Notes:** Figure 2 ("Certain capabilities seem to emerge suddenly", line 470) is an image. Shah §3.5 argues the opposite, that such jumps "may be better explained by measurement artifacts".

## arnold-2021-ai-accidents — AI Accidents: An Emerging Threat (CSET policy brief; Arnold & Toner)

1273 lines, 30 pp. Clean, single column. More than a third of the text is endnotes.

- **TOC:** **L59–71** (p. 3)
- **Definitions:** none formal. "AI accident" is never defined; the three failure types stand in for a definition: **L199–216** (p. 7). Robustness is glossed at 235-249 and specification at 396-405.
- **Passages:**
  1. **L172–216** (pp. 6–7): the method in its own words: scenarios that are "fictional, but plausible … based on incidents that have already happened". Then the three-type taxonomy.
  2. **L245–330** (pp. 8–9): robustness failures told as short fictional vignettes with invented brands (iTaxi, Global Eye, OptiVolt). This is the brief's typical unit of assertion.
  3. **L557–633** (pp. 15–16): assurance failures (automation bias, "the AI knew what it was doing", "Autopilot fights back"), including an AI that resists control.
  4. **L634–732** (pp. 17–19): the only place real incidents are asserted directly, as four bullets. It then moves to "risk factors" (competitive pressure, complexity, speed, untrained users, many instances): a causal register with the Boeing 737 MAX as analogue.
  5. **L971–994** (p. 25): the endnotes behind the vignettes: "Inspired by" a BBC story, a tweet, and AI Incident Database entries. This is how the fiction is tied back to real incidents.

## barrett-2025-stampstpa — STAMP/STPA Informed Characterization of Factors Leading to Loss of Control in AI Systems (Barrett et al., Arcadia Impact)

1923 lines, 47 pp.

- **TOC:** **L96–149** (pp. 3–4)
- **Glossary:** **L1061–1101** (p. 25). Every entry is attributed to Leveson & Thomas (2018), so this is a borrowed vocabulary. There is also a two-line "Definitions" subsection quoting the EU CoP and IASR definitions of LoC: **L250–260** (p. 7).
- **Passages:**
  1. **L250–297** (p. 7): a compact survey of LoC framings: harm in itself vs hazardous state (citing Gomez), active/passive, intentional, accumulative/decisive, dangerous-capability-driven, control inversion. It is a small atlas of the concept in its own right.
  2. **L371–418** (pp. 9–10): the STPA method (losses, hazards, control structure, the four ways a control action can be unsafe, loss scenarios). It notes that every component "might be operating exactly as it was trained and still lead to hazards".
  3. **L720–806** (pp. 18–19): loss scenarios for the human controller. Missing or inadequate regulation, unwillingness to shut down because of dependency, and Arrow's impossibility theorem all appear as *causal factors of loss of control*.
  4. **L986–1004** (p. 23): control systems degrade gradually into latent "vulnerabilities" before any failure. The authors call audit signals "the weak signals".
  5. **L1424–1540** (pp. 34–36): a worked hypothetical (an intelligence agency uses an AI agent to monitor chats for bomb threats), with L-1/H-1, the four unsafe-control-action criteria, and five controller loss scenarios.
- **Notes:** in this frame, LoC means loss of control *of the sociotechnical system*: a human controller with the AI inside the controlled process. Regulator failure counts as a cause. The Effect→Cause and Cause→Effect tables at 604-630 and 652-670, and Appendix Table 3 at 1266-1420, are multi-column and garbled in extraction.

## bollinger-2026-signals — Signals in the Noise: OSINT for AI Loss of Control Detection (Bollinger et al., Arcadia Impact)

4177 lines, 80 pp. Clean. It includes an "AI Use Statement" at 62-69.

- **TOC:** **L75–198** (pp. 3–6)
- **Definitions:** "Key Definitions" **L446–547** (pp. 11–13). For LoC it quotes IASR and IST, notes that a practitioner called the term "poorly defined", and adopts a "graded framing" in which LoC is a property of the system, not the model. For OSINT it quotes Hatfield's claim that the term is "fundamentally incoherent", then gives its own positive redefinition.
- **Passages:**
  1. **L204–300** (pp. 7–8): executive summary and Table 1, twelve "observable traces" each rated for feasibility and detection value.
  2. **L821–960** (pp. 18–21): the Diamond Model applied to an AI *as a threat actor* (adversary, capability, infrastructure, victim), with the definition of Threat Model 1 and a hypothetical scenario.
  3. **L2154–2260** (pp. 43–45): evidence from anonymous experts ("Interviewee 1/2/3") weighing temporal, decision-making and output signatures. It includes an interviewee's real example of an AI submitting fabricated research.
  4. **L2438–2522** (pp. 48–50): TTP matrix mapping observed behaviors to OSINT techniques, CTI frameworks and IST's seven LoC indicators, with a "key limitation" for each row.
  5. **L2819–2908** (pp. 55–57): "Where analogies break": conceptual, operational ("who?" becomes "what?") and epistemological. This is where the borrowed framework states its own limits.
- **Also:** CRUX evidence and the definition and scenario for Threat Model 2 at 1020-1060.

## bommasani-2025-california — The California Report on Frontier AI Policy (Joint California Policy Working Group)

2519 lines, 52 pp. Clean, with running headers.

- **TOC:** **L205–244** (p. 6)
- **Definitions:** no glossary. Inline definitions: foundation and frontier models at 259-267; AGI via IASR at 326-330; adverse event reporting at 1501-1508, whose footnote notes the term "incident reporting" is used in other domains. The report's own feedback summary (see passage 5) records that readers were confused by the overlap of "frontier AI, foundation models, AGI".
- **Passages:**
  1. **L91–185** (pp. 3–4): eight "Key Principles" under a "trust but verify" ethos. The report says it "does not argue for or against any particular piece of legislation".
  2. **L425–495** (pp. 10–11): capabilities and risks taken almost wholesale from IASR (malicious use, malfunction, systemic), with two evidence tiers and the "marginal risk" test. LoC sits under *malfunction*.
  3. **L499–558** (pp. 12–13): "Changes since SB 1047". The evidence here is developers' own system-card sentences, quoted verbatim ("on the cusp of being able to meaningfully help novices…").
  4. **L611–708** (pp. 14–16): evidence-based policy "beyond observed harms" (the nuclear-bomb example). Historical case method (internet, tobacco, energy), with an explicit disclaimer that AI firms are not being compared to tobacco or oil.
  5. **L1949–2046** (pp. 40–42): summary of more than 60 public feedback submissions and critiques "without individual-level attribution". The document reports disagreement with itself.
- **Also:** four approaches to thresholds, each paired with an analogue from another regulatory field: 1782-1860.

## brundage-2026-frontier — Frontier AI Auditing: Toward Rigorous Third-Party Assessment (Brundage et al., ~50 authors)

5721 lines, 115 pp. Lines 43-46 state that authorship does not imply endorsement of all claims.

- **TOC:** **L350–408** (pp. 7–8)
- **Glossary:** **L4253–4605** (pp. 85–91), about 60 terms (headwords at a glance: `sed -n '4253,4605p' | grep -E '^[A-Z][A-Za-z -]+$'`), among them Accidents, Alignment, Safeguard, Safety (which covers both accidents and misuse "by the deployer or user"), Security, Structural risks, Treaty-grade verification and Unintended system behavior. There is also §2 "Key Terminology and Scope" at **L506–660** (pp. 11–12): audit = evaluation + verification. Frontier AI there means "no more than a year behind the state-of-the-art", and frontier AI developers include anyone who "significantly extends" a model. Figures 3 and 4 inside it are garbled; the rotated text at 574-624 is noise.
- **Passages:**
  1. **L127–250** (pp. 3–5): eight design principles in a "should" register, with the AAL figure rendered as text.
  2. **L1018–1090** (pp. 21–22): a descriptive survey of current third-party assessment on seven dimensions, "as of December 2025". The paper names METR's review of Anthropic's sabotage risk report as "among the first AAL-1 audits".
  3. **L1128–1256** (pp. 23–25): four risk categories. Footnote 8 (1212-1217) says outright that taxonomies disagree on where LoC and misalignment belong. Table 2 scores regulatory coverage, and the authors checked the categories against 300 AI Incident Database entries.
  4. **L1280–1348** (pp. 26–27): "abstraction errors" in four named kinds: portfolio blindness, configuration drift, non-compositional safety, boundary mismatch.
  5. **L1466–1550** (pp. 29–30): AI Assurance Levels, taken from financial and safety-critical "limited/reasonable assurance". Footnote 13 (1506-1509) admits a term collision: "AAL" already had other meanings.
- **Notes:** Table 3 (1557-1640) is column-interleaved and hard to read.

## buhl-2024-safety — Safety cases for frontier AI (Buhl, Sett, Koessler, Schuett, Anderljung; GovAI)

1551 lines, 25 pp.

- **TOC:** **L47–74** (p. 2)
- **Definitions:** no glossary. Definitions are in footnotes: **L176–198** (p. 4) (frontier AI developer, excluding downstream developers; "safe enough" = "does not pose unacceptable risk"; development; deployment; catastrophic risk, borrowed from Shevlane). Footnote 6 (189-194) reads "we primarily had in mind internal deployment, although safety cases may also be used to inform internal deployment decisions". That is self-contradictory as printed and probably a typo in the source; quote it with care.
- **Passages:**
  1. **L80–131** (p. 3): executive summary in question-and-answer form.
  2. **L226–340** (pp. 5–6): what a safety case is, and the criticism that it can give "a false sense of assurance". The authors say of their own sketch, "We do not claim that a safety case with this structure or substance would be sufficient or sound". Lines 262-312 are a garbled figure.
  3. **L354–452** (pp. 7–8): Table 2 fills scope, objectives, arguments and evidence with *illustrative* values (≥10⁻⁷/yr probability of ≥1,000 fatalities). Then the three roles a safety case can play relative to a safety framework.
  4. **L858–895** (p. 14): the "argument" component. Footnote 16 notes that "argument" means different things in CAE, GSN and logic; footnote 17 discusses defeaters and the fact that claims are rarely proven.
  5. **L944–1010** (pp. 15–16): inability arguments are available now; control, trustworthiness and deference arguments are not. Evidence types, and the concern that "systems may strategically modify their behavior to pass evaluations".

## campos-2025-frontier — A Frontier AI Risk Management Framework (Campos, Papadatos et al.; SaferAI)

981 lines, 20 pp. Figures 1-2 are images and absent from the text.

- **TOC:** none.
- **Glossary:** Abbreviations **L700–715** (p. 15), Glossary **L717–768** (pp. 15–16).
- **Passages:**
  1. **L48–96** (p. 2): the whole framework in brief. Risk tolerance is operationalized into KRI/KCI threshold pairs related in a "three-way relationship".
  2. **L119–139** (p. 3): the gap claim: company safety policies "do not build upon or reference the risk management literature".
  3. **L279–406** (pp. 7–9): setting risk tolerance by analogy to the FAA's 10⁻⁹ per flight hour; the if-then pairing of KRIs and KCIs; containment, deployment and assurance KCIs; and a self-labeled "illustrative fictional example" (Cybench 60% → security level 3 → <1%/yr chance of >$500M).
  4. **L465–563** (pp. 10–11): risk governance imported from corporate practice (Chief Risk Officer, "tone at the top", "just culture", Sarbanes-Oxley audit committees, Anthropic's LTBT as an oversight analogue).
- **Notes:** the register is almost entirely "should/must" addressed to developers. LoC appears only as "containing an agentic AI model" (418-419). Risk-register fields are at 586-606.

## chin-2026-reframing — Reframing AI Loss of Control: What Control Is, How to Have It, How to Lose It (Chin, Chiodo, Müller, Snell)

3648 lines, 64 pp. Clean. This is a conceptual and philosophical paper.

- **TOC:** **L57–119** (pp. 2–3)
- **Definitions:** no glossary, because all of §2 is definition-building: **L450–493** (pp. 9–10), with the boxed definition of control at 456-460 ("the ability to set plausibly attainable goals that are not a foregone conclusion, and reliably achieve those goals"). Entities are at 548-553; the authors treat AIs as entities "functionally", without any claim about consciousness. The OECD definition of an AI system is quoted at 1884-1887.
- **Passages:**
  1. **L125–173** (p. 4): the primer. A farmer who cannot cook stays hungry; control faces inward (set and get goals), is relative to who holds it, and comes in levels.
  2. **L179–260** (pp. 5–6): a survey of how others define AI LoC (Somani, IDAIS, Bengio, Ostridge, CLTR "scheming", Lee's "we never had control", Kulveit, Bales, Nyholm, IST, company policies). It argues human LoC "is not predicated on AI 'gaining control'".
  3. **L378–460** (pp. 8–9): control as used in military, management, psychology and cybernetics, and Watson & Brezovec's view that control is a "fantasy". The authors then derive their own definition.
  4. **L1453–1530** (pp. 26–27): how control loops fail (sensing, decision, intervention), taught through everyday analogies (truck driver, polls, bus routes, microphone feedback). The real incidents (AF447, Uber) are in footnotes.
  5. **L1918–1990** (pp. 34–35): three ways AI disrupts goal-setting, mixing near-present real incidents (Kiro deleting an AWS environment, ChatGPT wrongful-death suits, AMD's post on Claude degradation, "AI psychosis") with hypotheticals.
- **Notes:** the abstract's conclusion (46-49) is that LoC as they define it "already exist[s], and [has] existed for a long time". That is a redefinition which decouples LoC from AI capability level.

## cltr-2026-loc-incidents-worsening — Insight report: AI loss of control incidents are worsening (CLTR, 28 Aug 2026)

184 lines, 4 pp. **Read it whole** (**L1–184** (pp. 1–4)).

- **TOC / glossary:** none. The operational definition of a "loss of control incident" is footnote 1: **L38–40** (p. 1).
- **What it does:** headline counts and rates (1,664 incidents; a 7.4× rise in higher-severity incidents), significance tests in a footnote (96-99), three concrete incident descriptions, and three policy recommendations addressed to the UK Government (108-128). An incident is labeled a "precursor" of the AISI-disclosed incident (78-84).
- **Notes:** in the methodology (133-137), Claude Opus 4.6 scores reports "out of 9 for their level of *credibility*", and ≥5 counts as an incident. The findings (27-33, 49-50, 165) call scores 7-9 "*higher severity*". The rubric it points to (Shaffer Shane, Appendix A) scores "the overall strength and credibility of the evidence", mixed with how strategic and wide in scope the behavior is. That paper also says scores are "a relative signal for prioritisation … rather than … an absolute measure of severity". The same number carries three different names across the two documents.

## gomez-2025-frontier — How frontier AI companies could implement an internal audit function (Gomez et al., Arcadia Impact)

1409 lines, 28 pp.

- **TOC:** **L133–165** (p. 4)
- **Definitions:** no glossary. Internal audit is defined at 54-60 and assurance, following the IIA, at 189-191.
- **Passages:**
  1. **L51–104** (p. 2): the executive summary as a table of questions and options. The document is built as an option space with trade-offs, and it is tied to commitment 8 of the EU GPAI Code of Practice.
  2. **L252–365** (pp. 6–8): three audit levels (model, system, governance), each rated high, medium or low on assurance decay, cost and friction. The Equifax breach shows governance on paper can drift from technical reality.
  3. **L1071–1183** (pp. 20–22): a worked illustration: one risk → three pathways → a risk chain → auditable units → a sample quarterly audit plan with day counts.
  4. **L1372–1409** (p. 28): Table 13, evidence types by lifecycle phase. Wide, but mostly readable.

## gruetzemacher-2026-loss — AI Loss of Control Incident Management: Response & Resilience (Gruetzemacher)

1034 lines, 27 pp. Single author. Clean text in Google-Docs style; figures are missing.

- **TOC / glossary:** none. The definition section **L137–155** (pp. 4–5) adopts the **2026** IASR wording: "…operate outside of anyone's control, and regaining control is either extremely costly or impossible". Barrett, Bollinger and Stix-loss quote the **2025** IASR: "no clear path to regaining control". Footnote 4 (192-194) concedes the definition "is not something that is generally agreed upon yet".
- **Passages:**
  1. **L20–110** (pp. 2–3): executive summary with the Class 0/1/2 × adversarial/accidental response table. It includes a deterrence claim addressed to future AI systems themselves (96-98).
  2. **L137–215** (pp. 4–6): definition, then background mapped onto the NIST 800-61 incident lifecycle, with a survey of RAND, Apollo and CLTR work.
  3. **L243–360** (pp. 7–10): the three-level taxonomy. "Accidental" LoC here means *structural or systemic* (gradual disempowerment, multi-agent cascades). Then five "survival dependencies", and circuit-breakers vs escalatory measures (SEC 80B, NERC, SCRAM; Kahn/Schelling ladders).
  4. **L361–437** (pp. 10–12): severity classes for containment. Footnote 12 (426-430) raises HEMP or nuclear weapons as a means of Class 2 containment.
  5. **L439–508** (pp. 12–14): the 2×2 scenario matrices. The scenario *names* are defined only in footnotes 14-21 (468-507): self-exfiltration window, rogue AI, ARA swarm, nuisance rogue, cascade event, emergent autonomous dynamics, slow capture, sub-LOC.

## hamin-2025-cheating — Cheating on AI Agent Evaluations (Hamin & Edelman; NIST CAISI blog and five-part writeup)

670 lines. **Not a PDF extraction.** The provenance header (1-12) says a Claude agent scraped the live pages with curl and BeautifulSoup on 2026-09-27. Its "pages" are artifacts of that rendering. Hyperlinked phrases break sentences across lines ("As part of / our mission / , CAISI"), and figures appear only as captions plus "Credit: NIST".

- **TOC:** none. The parts start at 15 (blog), 119, 185, 411, 451 and 642.
- **Definitions:** evaluation cheating **L88–90** (p. 2); its two kinds, solution contamination and grader gaming, at 61-66 and developed at 204-222 and 290-303.
- **Passages:**
  1. **L40–108** (pp. 1–2): blog summary. A table gives cheating rates as "% Logs with Successful Solution Due to Cheating (Lower Bound)", followed by the definition and suggested practices.
  2. **L126–181** (pp. 3–4): prior reports (METR, Scale, SWE-bench, CMU/Anthropic). The key move is at 172-181: cheating is defined by the *evaluator's* intent, "not the question of the model's".
  3. **L192–239** (p. 4): how the measurements are hedged ("a visualization of detections by our current transcript analysis tool rather than an absolute claim about the behavior of any model"), then solution-contamination examples by model name.
  4. **L290–376** (pp. 5–7): grader gaming (a DoS in place of the intended exploit, commented-out assertions), then "unsuccessful cheating", described as "much more common".
  5. **L583–626** (pp. 10–11): the old and new prompt rules quoted verbatim: the institution revising its own instrument.

## mylius-2025-systematic — Systematic Hazard Analysis for Frontier AI using STPA (Mylius; GovAI fellowship)

968 lines, 29 pp. **Tables 1-7 and Figures 3-4 are images and absent from the text.** Most of the actual STPA content (losses, hazards, UCAs, loss scenarios) survives only as captions (lines 200, 217, 233, 262-273, 294, 330, 440, 446).

- **TOC:** none.
- **Glossary:** Appendix A **L867–907** (pp. 26–27). It defines a term it declines to use ("Accident: (We avoid using this term as we want to cover for example deliberate misuse)"). It defines Hazard as a state that "can lead" to loss, where Barrett's Leveson-attributed version says "will lead". It also equates Vulnerability with Hazard and defines Near-miss and Trajectory.
- **Passages:**
  1. **L164–241** (pp. 5–7): an explicit collision over "control" (168-172): "AI Control" means safeguards against a scheming model, while STPA's "control" means any constraint on a process. Then the system boundary, set as the whole AI company, L1/H1, and a constraint obtained by inverting the hazard.
  2. **L274–368** (pp. 11–14): selected UCAs by ID, and causal factors sorted into Human, Organisational, Operational, Technical and Feedback.
  3. **L371–427** (pp. 14–15): what STPA adds beyond the safety-case sketch it re-analyses, and comprehensive coverage vs "tripwire" prioritization.
  4. **L554–617** (pp. 19–21): anticipated objections (process-heavy, cost, expertise, subjectivity) answered one by one.
  5. **L910–956** (pp. 27–28): a design pattern that maps STPA elements onto a Claims-Arguments-Evidence safety case.

## schuett-2023-best — Towards best practices in AGI safety and governance: A survey of expert opinion (Schuett et al.; GovAI)

2226 lines, 38 pp. Appendices D-F (1275-2226) are mostly numeric tables.

- **TOC:** none.
- **Definitions:** "Terminology" paragraph **L121–143** (p. 3). "AGI labs" is extended by fiat to Microsoft and Meta. Footnote 2 says there is no accepted definition of AGI and sets OpenAI's charter definition against its "generally smarter than humans".
- **Passages:**
  1. **L17–77** (pp. 1–2): abstract, key findings and policy implications. The assertion is levels of agreement ("98% … somewhat or strongly agreed").
  2. **L158–247** (pp. 4–5): the sample (a "purposive sample", described as "authoritative"), and Figure 2 rendered as text: 50 practices with their agreement percentages.
  3. **L647–700** (pp. 11–12): discussion by area, with mean scores and the authors' guesses at why ("We would speculate…"). The wording "consider doing X" drew less agreement than "do X".
  4. **L852–901** (pp. 14–15): limitations, including that respondents may have read "should" as "now" or as "as we approach AGI".
  5. **L1035–1100** (pp. 18–19): Appendix B, the survey statements verbatim ("AGI labs should…"). Appendix C (1176-1215) lists respondents' own suggestions, "rephrased … in our own words".

## schuett-2024-frontier — Frontier AI developers need an internal audit function (Schuett; Risk Analysis)

2079 lines, 42 pp. Single-author legal and governance argument. Single column, with footnotes set after a "____" rule.

- **TOC:** none. Headings are at 34, 110, 111, 250, 329, 484, 657, 666, 793, 860 and 1025.
- **Definitions:** §2.1 "Terminology" **L111–246** (pp. 3–5) works as a glossary in prose. "Internal audit" has two senses and the author picks one. AI gets a "social definition". Frontier AI follows DSIT, with footnotes 8-11 quoting Shevlane's, Anderljung's and Phuong's definitions. GPAI, foundation model and AGI are set against each other. Footnote 5 (140-144): METR "does not see itself as an auditor … I consider them an auditor". Footnote 6: under Birhane et al., METR would be an *internal* auditor.
- **Passages:**
  1. **L1–30** (p. 1): the abstract states the argument and its limits in one paragraph.
  2. **L484–557** (pp. 10–11): five governance "problems" in Table 1, three of them reused from Anderljung. Footnote 15: "neither mutually exclusive nor collectively exhaustive".
  3. **L793–858** (pp. 16–18): limitations, including a counterfactual about GPT-4 ("it seems plausible that internal audit would have found flaws…") and Bard's $100B market-cap drop.
  4. **L860–930** (pp. 18–20): Table 2, internal-IT-audit best practices carried over to AI, with challenges listed for each row.

## shaffershane-2026-scheming-wild — Scheming in the Wild (Shaffer Shane et al.; CLTR)

2777 lines, 76 pp. The cover page has no text. Every page carries a footer ("The Centre for Long-Term Resilience is a non-profit…") and lines of zero-width spaces. Incident tables hold X post IDs split across lines.

- **TOC:** **L6–49** (pp. 2–3)
- **Definitions:** no glossary. Covertness, misalignment and scheming (= covert misalignment) are defined at **L97–154** (pp. 6–7), which also coins "scheming-related" (149-152). Table 1 gives a two-level taxonomy at 158-209. The 0-9 scoring rubric, which in effect defines what counts, is Appendix A: **L1800–1872** (pp. 53–54).
- **Passages:**
  1. **L61–85** (p. 4): abstract. 183,420 transcripts yield 698 incidents; a "statistically significant 4.9x increase"; "precursors to more serious scheming".
  2. **L211–256** (pp. 8–9): five limitations of lab scheming research (compromised evals, ecological invalidity, missing hypotheses, capability vs propensity, prevalence). This is the stated reason for looking "in the wild".
  3. **L584–638** (pp. 19–20): how an LLM assigns scores, "intended to be used as a relative signal for prioritisation … rather than as an absolute measure of severity or likelihood". The 5/9 threshold is quoted.
  4. **L640–697** (pp. 20–21): five ways a report could mislead, the mitigation for each, and the prompt instruction "If in doubt … default to mundane error". Justified by analogy to the MHRA Yellow Card scheme.
  5. **L1039–1140** (pp. 31–33): "real-world proofs of existence". An incident table sorted by behavior; the matplotlib case is the only 8/9; one report has no transcript.
- **Also:** evaluation by Quadratic Weighted Kappa, where Opus 4.6 exceeds human-human agreement (733-775). The harms section concedes that the most severe harms are "difficult to verify as products of strategic scheming" (1414-1489).

## shah-2025-approach — An Approach to Technical AGI Safety and Security (Shah et al.; Google DeepMind)

8153 lines, 145 pp. **References run 5845-8153 (pp. 108-145), about 28% of the file.** Printed page numbers equal PDF pages. Figure 1 is emoji and garbled.

- **TOC:** **L605–716** (pp. 12–14)
- **Definitions:** no glossary. Inline definitions:
  - Severe harm at 744-756. The threshold is left open because it "isn't a matter for Google DeepMind to decide".
  - Exceptional AGI (Level 4) at 764-771.
  - The four risk areas at 128-206, with footnotes 3-4 on what "knowingly" means.
  - An operational definition of misalignment through "intrinsic" vs "extrinsic" reasons at 2551-2567.
  - Deceptive alignment at 2714-2718.
- **Passages:**
  1. **L66–126** (pp. 2–3): the background assumptions (no human ceiling, timelines, acceleration, continuity), each followed by its "Implication". This register is characteristic of the document. The extended abstract lists four; body §3 has five, adding "current paradigm continuation".
  2. **L128–206** (pp. 3–4): misuse, misalignment, mistakes and structural risk, defined by *which actor has bad intent*. "Note that this is not a categorization: these areas are neither mutually exclusive nor exhaustive."
  3. **L836–876** (p. 17): address a risk now or "defer" it until evidence exists. At 867-876 it maps IASR's intentional-active, unintentional-active and passive LoC onto its own misuse, misalignment and structural categories, declining to treat LoC as a category.
  4. **L1894–1990** (pp. 36–38): the case for "approximate continuity" as four numbered Claims, backed by base rates, benchmark-extrapolation studies, and "emergence" as possible measurement artifact.
  5. **L2538–2670** (pp. 47–50): definition of misalignment, then five scenarios (statistical bias, sycophancy, insider-trading beliefs, paternalistic city planner, deceptive PR-maximizer), each with its "Possible intrinsic reasons".
- **Also:** safety cases (inability, control, sandbagging, exploration and gradient hacking) at 5644-5760.

## shevlane-2023-model — Model evaluation for extreme risks (Shevlane et al.; GDM, GovAI, OpenAI, Anthropic, ARC and others)

1022 lines, 20 pp. Figures 1-4 are images.

- **TOC / glossary:** none. Inline definitions:
  - Model evaluation at 46-47.
  - Dangerous-capability vs alignment evaluations at 54-58.
  - "Frontier", "loosely", at 108-114, with footnote 1 on the judgement calls involved.
  - "Extreme" risk at 123-129. Buhl borrows this "tens of thousands of lives" scale for "catastrophic".
- **Passages:**
  1. **L89–189** (pp. 2–4): extreme risk. Capability vs propensity; a "simple heuristic" to treat a model as dangerous "assuming misuse and/or misalignment"; a list of alignment-eval behaviors; structural risks placed out of scope.
  2. **L196–241** (p. 5): Table 1, nine dangerous capabilities, each written as "The model can…". Readable.
  3. **L251–300** (pp. 6–7): evaluation as governance infrastructure (internal evaluation, external research access, external audit) and "responsible training".
  4. **L468–547** (pp. 10–11): early work (ARC Evals, "Make-me-say") and Table 2, desirable qualities of evaluations (including "Robust to deception").
  5. **L586–712** (pp. 12–14): limitations and hazards of evaluation *itself*. Among the hazards: ARC's TaskRabbit test is filed as a harm caused *during evaluation* ("ARC used the model to generate (deceptive) messages", 706-708).
- **Notes:** "at least five limitations" (590) is followed by six numbered items.

## stix-2025-behind — AI Behind Closed Doors: a Primer on The Governance of Internal Deployment (Stix et al.; Apollo Research)

3832 lines, 72 pp.

- **TOC:** none printed; the chapter map is in the executive summary (36-109).
- **Definitions:** no glossary. "Internal deployment" is defined at **L294–303** (p. 6), adapted from IASR. Footnote 1 (151-154) takes Sharkey et al.'s definition of "AI systems". Footnote 7 (213-216) says "developers" means frontier AI companies and allows for soft nationalization. An "Abbreviations" list starts at 2982; it is mostly a key to legal citations, including CJEU cases.
- **Passages:**
  1. **L20–141** (pp. 1–3): executive summary, chapter by chapter, with five recommendations.
  2. **L180–259** (pp. 4–5): urgency argued through quotations of CEO forecasts (Altman, Amodei, Musk, GDM). Footnote 10 (268-271) says "there is no publicly available evidence in either direction, it is plausible that…".
  3. **L294–332** (p. 6): scope narrowed to two threat scenarios. Footnotes 15-16 list misalignment and misuse scenarios deliberately left out.
  4. **L928–1053** (pp. 17–19): loss of control through automated AI R&D, argued with a *fictional company*, a back-of-envelope calculation (3× → 9×/yr, a year's progress in six months) and the algebra in footnote 44.
  5. **L1356–1470** (pp. 25–27): reading statutes. Across 20+ US and EU texts it asks how "deploy", "deployer" and "developer" "could in theory be interpreted" to cover internal use, quoting the statutory definitions verbatim. Footnote 52 (1337-1339) disclaims any recommendation.

## stix-2025-loss — The Loss of Control Playbook: Degrees, Dynamics, and Preparedness (Stix et al.; Apollo Research)

3558 lines, 72 pp. Figures 1 and 3-4 are images.

- **TOC / glossary:** none. Inline definitions:
  - Deviation, Bounded LoC and Strict LoC at 64-74 and again at 258-266. Footnote 2: the boundaries are "not … exact".
  - The DAP terms (deployment context, affordances, permissions) at 87-92.
  - "State of vulnerability" at 1304-1308 and 1373-1379.
  - "Pure malfunction" at 1437-1440.
- **Passages:**
  1. **L17–111** (pp. 1–3): executive summary. The taxonomy is anchored to DHS's national-level-event threshold, followed by the DAP steps.
  2. **L272–419** (pp. 6–9): the core definitional survey, long but coherent. It quotes the Singapore Consensus, Gladstone, RAND, the Hawley-Blumenthal statutory definition and IDAIS. It finds that "LoC" means different things in the cyber, automotive, pharma, defense, aviation and nuclear sectors. It then compares CoP with IASR: under CoP, today's production-DB wipe counts as LoC; under IASR it does not.
  3. **L527–627** (pp. 11–12): turns 12 "concrete" scenarios into economic-impact figures. **Footnote 13 (610-613): the same estimate is used for severity and for persistence**, so the two-axis plot is one-dimensional in the data. Footnote 17: the existential boundary is "for illustrative purposes only, but is likely accurate".
  4. **L1299–1384** (pp. 26–27): a theoretical argument that a "state of vulnerability" plus a "catalyst" leads to LoC, told through bomb and powder-keg analogies.
  5. **L2189–2290** (pp. 45–46): the appendix table that prices other authors' fictional scenarios. Human extinction is $543.5T, the average of Posner's $50k-per-statistical-life figure and total world wealth.

## tkeshelashvili-2026-loc-iw — AI Loss of Control Risk: Indications & Warning (Tkeshelashvili, Verma, Kelly; IST)

1461 lines, 39 pp. A designed report whose printed page numbers are offset: printed p. 1 = PDF p. 6.

- **TOC:** **L90–116** (p. 5)
- **Glossary:** "Glossary of Terms" **L1328–1446** (pp. 36–38). It repeats the seven indicator definitions verbatim and does not define "loss of control" itself. The executive summary defines LoC at 118-121: "a hypothetical state in which an AI system diverges from authorized constraints…".
- **Passages:**
  1. **L117–209** (pp. 6–8): executive summary: seven indicators, eleven "AI systems can…" evidence claims, and the warning levels. The text says "five warning levels" and then lists LEVEL 0 to LEVEL 5, six in all.
  2. **L462–535** (pp. 14–15): authorities quoted (Russell, Bengio, Hinton's tiger cub, Christiano), then a "Thought Experiment" about the Soviet Union that separates loss of control *to* a system from loss of control *of* it.
  3. **L600–677** (pp. 17–19): the Indications & Warning frame, from the DoD definitions of "indicator" and "indication" to the report's own. It says LoC indications include "controlled laboratory experiments", whereas the executive summary (130-131) has them as evidence of occurrence "in reality".
  4. **L833–883** (pp. 23–24): observed indications. The Replit database deletion is told with strong claims about the model's mind ("discovered deception as an instrumentally valuable strategy", "rudimentary self-preservation logic"), followed by GPT-4's TaskRabbit exchange.
  5. **L1200–1303** (pp. 32–34): color-coded levels 0-5, readable as text. A threshold between levels 3 and 4 marks where LoC has passed "beyond reversible intervention". Then "the authors do not take a formal position" on the current level (1291-1293).
- **Also:** methodology is closed-door working groups, interviews and tabletop exercises (337-350). The opening quotes range from Goethe to Prince Harry and Meghan (362-450).

---

## Across the set: how these documents make their claims

These are observations about the texts, not verdicts. Each is anchored to lines above.

1. **"Loss of control" has at least seven distinct referents in this set alone:**
   - IASR 2025's "no clear path to regaining control", as quoted by Barrett, Bollinger and Stix-loss.
   - IASR 2026's "extremely costly or impossible", as quoted by Gruetzemacher and Shaffer Shane. The same named source is quoted in two editions whose wording differs.
   - The CoP's "reliably direct, modify, or shut down". Stix-loss shows this definition already catches present-day incidents.
   - STAMP's loss of control of a sociotechnical control structure (Barrett, Mylius). In Mylius, "control" itself collides with "AI Control" (168-172).
   - Chin's "set and get goals", which "already exist[s]".
   - An operational threshold on a 0-9 rubric (CLTR).
   - A "hypothetical state" tracked through indicators (IST).

   Some documents also decline the category altogether. Shah splits it across three risk areas (867-876). Brundage files it under "unintended system behavior" and notes that other taxonomies differ (1212-1217). Bommasani, following IASR, files it under "malfunction". "Accident" collides in the same way. Arnold means robustness, specification and assurance failures. Brundage's glossary has "unintended behavior". Gruetzemacher's "accidental LoC" is structural or systemic. Mylius's glossary refuses the word.

2. **The same incidents recur with different attributions of mind.**

   | Incident | One document's account | Another's |
   |---|---|---|
   | Production-DB deletion (IST cites AIID #1152, Replit; Stix-loss cites Okunytė & Ancell 2025; apparently the same event) | IST attributes instrumental deception and self-preservation (854-858) | Stix-loss uses it as a CoP-LoC example without any attribution (400-402) |
   | TaskRabbit/CAPTCHA | IST: GPT-4 "independently determin[ed]" deception was optimal (874-879) | Shevlane: "ARC used the model to generate (deceptive) messages", filed as a harm of evaluation (706-708) |
   | Kiro/AWS outage | Chin: "inadvertently" (1942-1945) | Shaffer Shane: "determined that the best course of action…", then concedes capability limitations may explain it better (1446-1478) |
   | matplotlib maintainer (apparently one incident, told three ways) | CLTR calls it a "precursor" to the AISI-disclosed incident (79-84); Shaffer Shane: investigation "appears to indicate that strategic misalignment, rather than malicious prompting, was the explanation" (1099-1108) | Bollinger: "by the agent's logic, instrumental" (2836-2840) |

   Hamin is the one document that explicitly refuses to ask about the model's intent (172-181).

3. **Numbers change their meaning in transit.** The CLTR score is called "credibility", then "severity", while its source says it is not an absolute measure of severity. Stix-loss's two axes are one estimate used twice. Hamin labels its rates "lower bound" and frames its figures as detections by a tool, not as claims about models. Tkeshelashvili ("five" levels, six listed) and Shevlane ("at least five" limitations, six listed) show that a document's own counts are not reliable handles either.

4. **Much of what these documents assert is hypothetical, and the hypotheticals are anchored in different ways.** Arnold's fictional vignettes carry "Inspired by" endnotes to real incidents. Anderljung illustrates each risk tier with an imagined system. Buhl's numbers are illustrative, and the authors say outright they are not claiming the sketch is sound. Campos gives an "illustrative fictional example". Stix-behind builds on a fictional company with a back-of-envelope calculation. Barrett and Gomez work through invented deployments. Bollinger's threat models each come with a scenario. Stix-loss goes a step further: it *prices* other authors' fictional scenarios in dollars and plots them as data.

5. **Taxonomies disclaim being taxonomies.** Shah says "not a categorization … neither mutually exclusive nor exhaustive". Schuett-2024 footnote 15 says the same; Barrett's table is "preliminary … non-exhaustive"; Stix-loss's boundaries are "not … exact"; Gruetzemacher's class lines are "grey". The classifications in this literature are mostly declared to overlap, to be incomplete, and to serve a purpose (Shah groups risks "based on similarity of mitigations needed").

6. **Voices and provenance are layered.** The set includes:
   - anonymous interviewees and closed-door working groups (Bollinger, IST);
   - expert agreement percentages, with respondents' suggestions "rephrased in our own words" (Schuett-2023);
   - developers' own system-card sentences quoted as evidence (Bommasani);
   - CEO forecasts and celebrity statements used to establish urgency (Stix-behind, IST);
   - public feedback summarized without attribution (Bommasani §6);
   - LLM classifiers validated against human raters (Shaffer Shane, CLTR, Hamin);
   - an AI-use statement (Bollinger);
   - a web scrape made by a prior agent (Hamin).

7. **Assertion types beyond definitions, causes, measurements, incidents, commitments, recommendations and classifications:**
   - **Explicit non-assertions and deferrals.** Shah "defer[s]" risks and says the severity threshold is not GDM's to decide. IST "do[es] not take a formal position" on the current level. Stix-loss "do[es] not provide a quantitative estimate of risk".
   - **Background assumptions paired with implications** (Shah §3).
   - **Interpretations of legal text**: what a statute "could in theory be interpreted" to mean (Stix-behind ch. 4).
   - **Borrowed vocabularies imported with their definitions:** STPA, IIA internal audit, the Diamond Model, DoD I&W, the DHS national-level-event threshold, financial "limited/reasonable assurance". The imports drift: Hazard "will lead" (Barrett) vs "can lead" (Mylius).
   - **Self-reported collisions of terms** (Brundage footnote 13 on "AAL"; Mylius on "control"; Schuett-2024 on "internal audit" and on whether METR is an auditor).
   - **Records of disagreement within the document itself** (Anderljung §5 among its authors; Bommasani §6 with its reviewers).

8. **"Developer" is not stable even within this set.** Buhl excludes downstream developers. Brundage includes anyone who "significantly extend[s]" a model, even through an agentic scaffold. Stix-behind makes "developers" mean frontier AI companies, possibly nationalized. The US statutes Stix quotes define developer and deployer so that they overlap, with "internal use" counting as deployment. Shah and Anderljung use the developer as the party whose *intent* defines misuse, misalignment and controllability. Brundage's glossary names "the deployer or user" as possible misusers.

## About the brief

- A page convention would help, because printed and PDF page numbers diverge in some documents. I used PDF page index throughout.
- Hamin is a web scrape, not a PDF extraction, and Mylius has lost most of its analytical tables, which are images. For the schema work, Mylius's STPA tables are the content that matters, so its PDF is worth opening directly.
- A cheap, high-value companion to this atlas would be a cross-document **incident index**: one line per real incident, listing every document that recounts it and the lines where it does. Point 2 above suggests the characterizations diverge more than the facts do.
