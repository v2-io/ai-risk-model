# Source atlas — UK government (beyond AISI), Five Eyes, ETSI

Line numbers refer to `…/scratchpad/src-text/<key>.txt` (pdftotext `-layout`). "p" is the physical PDF page, counted by form-feeds (`\f`), so p1 is the first page of the PDF whatever the printed folio says. Ranges are inclusive. One-line notes are signposts only. They say what drew me to a passage, not what it means.

A reading tip for the tabular documents (the DSIT implementation guide, the NRR, the CRA, the DSIT capabilities annex): `-layout` keeps columns side by side, so open them in a window 200+ characters wide. Squeezing whitespace breaks the columns apart.

Documents are grouped roughly by genre, not alphabetically. Every key in the set is here. Search for `### key` to jump to one.

---

## A. NCSC Assessment products (PHIA probabilistic register)

### ncsc-2024-near-term — "The near-term impact of AI on the cyber threat" (NCSC, 24 Jan 2024) — 314 lines, 8 pp

- **TOC:** none.
- **Glossary:** 261–292 (p7–8). Six terms. Notably *Transformative AI*, glossed via "artificial general intelligence, the hypothetical concept of autonomous systems that learn to surpass human capabilities in most intellectual tasks" (276–279).
- **Extraction note:** the PHIA probability yardstick is a graphic and did not extract. At 55–63 (p2) the text says the terms "correspond to the likelihood ranges below", and nothing follows. The words ("realistic possibility", "highly likely", "almost certainly") appear throughout, but their numeric ranges are not in this text. `/` characters are page-edge artefacts.
- **Passages:**
  1. **31–95 (p1–3).** Self-description of NCSC-A as "the authoritative voice on the cyber threat to the UK", followed by the key judgements. This is the core genre: every sentence is a forecast carrying a calibrated likelihood word.
  2. **100–117 (p3–4).** The scope exclusions and the explicit load-bearing *assumption*: "no significant breakthrough in transformative AI in this time period. This assumption should be kept under review". This is a claim conditional on an assumption, stated out loud. The list of assertion types doesn't cover it well.
  3. **122–176 (p4–5).** Table 1: capability uplift by actor class (three columns) × attack stage, on an ordinal scale ("MINIMAL UPLIFT → … → SIGNIFICANT UPLIFT", 176). A classification crossed with an ordinal judgement. The table extracted legibly.
  4. **179–256 (p5–7).** Numbered judgements 3–11. Causal chains, each carrying a probability word ("It is therefore likely that cyber criminal use … will contribute to the global ransomware threat", 197–199). Note the "data" mechanism (247–251).

### ncsc-2025-impact — "Impact of AI on cyber threat from now to 2027" (NCSC, 7 May 2025) — 277 lines, 7 pp

- **TOC:** none.
- **Glossary:** 223–255 (p6–7). *AI*, *Frontier AI* ("AI systems that can provide a wide variety of tasks that match or exceed the capabilities present in today's most advanced systems"), *AI system* (a notably infrastructural definition: "host infrastructure, management systems, access control systems and programming interface"), *AI design*, *Vulnerability* (including zero-day vs n-day).
- **Extraction note:** the yardstick graphic is missing again (27–36, p1).
- **Passages:**
  1. **38–71 (p2–3).** Key judgements, then context. "Technical surprise is likely" (71) is a meta-judgement about the assessment's own reliability.
  2. **109–153 (p4–5).** The VRED (vulnerability research and exploit development) judgement. "there is a remote chance of universal access to AI for cyber security defence by 2027, [so] there will almost certainly be a digital divide" (127–130): a probability judgement used as the premise of another. "fully automated, end-to-end advanced cyber attacks is unlikely to 2027" (146–147).
  3. **168–208 (p5–6).** AI systems as attack surface, and a causal claim about *developer incentives*: "In the rush to provide a market-leading AI model … developers will prioritise an accelerated release schedule over security considerations" (187–190).
- Cross-document: the sentence "Keeping pace with frontier AI cyber developments will almost certainly be critical to cyber resilience for the decade to come" (49–50, 132–133) reappears almost verbatim, with its PHIA word, in the 2026 blog `ncsc-2026-ten-questions` (93–94), prefixed "The NCSC's view is that". Assessment language migrates into advisory prose and keeps its probability word.

### hmg-2023-safety — "Safety and Security Risks of Generative Artificial Intelligence to 2025" (HM Government, 2023; no month given in the text) — 225 lines, 6 pp

- **TOC:** none.
- **Glossary:** a sidebar, "Our definitions and scope", at 12–45 (p2), **interleaved line by line with the summary column** (a two-column garble). Read it slowly. It defines *Safety and Security* ("The protection, wellbeing and autonomy of civil society and the population"), *AI* ("Machine-driven capability to achieve a goal by performing cognitive tasks"), *Frontier AI*, *GenAI*, *LLM*, *Risk* ("A situation involving exposure to detrimental impacts"), and *Threat* ("A malicious risk involving an actor with intent"). The scope exclusion is at 44–45: military risks are not considered.
- **Passages:**
  1. **11–61 (p2).** The whole summary plus the definitions sidebar. Very dense: PHIA-register forecasts, and a risk/threat distinction set up in the margin.
  2. **117–131 (p4).** Threat actors. "potentially anyone to pose a threat through malicious use, misuse or mishap" (117–118) is a three-way cause taxonomy in one clause.
  3. **138–198 (p5–6).** An explicit domain taxonomy (digital / political-societal / physical, "at least three overlapping domains"), a compounding claim ("they are likely to compound and influence other risks", 153), then the "most significant risks" typology, with coined terms given in scare quotes (data poisoning, prompt injection, model inversion, perturbation, deepfakes, hallucinations).
  4. **201–220 (p6).** Conclusions. Distinctive: a claim about the limits of *government's own knowledge* ("Governments will highly likely not have full insight into private sector progress", 210) and a recorded expert disagreement ("experts disagree on whether generative AI is a stepping stone to … Artificial General Intelligence", 215–216).

---

## B. NCSC blogs (short, bylined, advisory; mostly 2025–26)

Short enough to read whole. Each is a few pages of web print with its "WRITTEN BY / PUBLISHED / WRITTEN FOR" footer. I give the whole length plus pointers.

### ncsc-2026-retaining-advantage — "Retaining defensive advantage in the age of frontier AI cyber capabilities" (Richard Horne, CEO; FT letter, 15 Apr 2026) — 66 lines, 2 pp

- **TOC / glossary:** none.
- **Read it whole (1–66).** A leader's letter: a hopeful long-term claim ("can ultimately be a good thing", 14), a near-term exposure claim (21–25), then an appeal to fundamentals and to Cyber Essentials. "Cyber risk is business risk" (34) is a slogan that recurs across the set.

### ncsc-2026-patch-wave — "Preparing for a 'vulnerability patch wave'" (Ollie Whitehouse, CTO, 1 May 2026) — 104 lines, 2 pp

- **TOC / glossary:** none. It defines *technical debt* inline (6–8).
- **Read it whole.** The distinctive move is at 10–16 (p1): an institutional **expectation of a coming event**, coined and named ("the NCSC expects there will be a 'forced correction' … a 'patch wave'"). It predicts a market-wide correction rather than a threat. Recommendations follow in graded conditionals (42–60): where X is available, do Y; where neither, Z.

### ncsc-2026-ten-questions — "10 questions to ask when using AI models to find vulnerabilities" (Ruth C, Head of Vulnerability Management, 11 May 2026) — 147 lines, 3 pp

- **TOC / glossary:** none.
- **Read it whole.** The voice is conversational ("HOLD ON!", 14). Two things stand out. A measurement deployed as argument: "over 40,000 vulnerabilities assigned CVEs in 2025 … only about 400 new vulnerabilities were tracked as exploited, and only around 40 of those were zero-days" (46–48, p1). And the PHIA sentence carried over from `ncsc-2025-impact` (93–94, p2). The guidance takes the form of questions the reader should ask, not directives.

### ncsc-2026-thinking-agentic — "Thinking carefully before adopting agentic AI" (Martin R, Dr Kate S, 15 May 2026) — 155 lines, 4 pp

- **TOC / glossary:** none. It gives an inline definition of *agentic AI* at 15–19 (p2): "the next step for the most advanced generative AI (also known as 'frontier AI')", which equates frontier with generative.
- **Read it whole.** A blog summary of `asd-2026-careful-agentic`. Points of interest:
  - 24–43 (p2): a four-item "additional risks" list (broader access, unpredictable behaviour, harder to spot, challenging to explain).
  - 72–84 (p3): "A system may take an action, but humans remain accountable for…", an accountability allocation.
  - 112 (p3): "loss of control" appears as an incident category to plan for ("agentic AI failures, misuse and loss of control"). It is used, not defined.

### ncsc-2026-managing-agentic — "Managing the cyber risk of agentic AI" (Toby W, Principal Security Architect, 20 Aug 2026) — 395 lines, 6 pp

- **TOC:** an in-page "In this blog" list, 18–39 (p1).
- **Glossary:** none. An inline trichotomy defines human-in / on / out-of-the-loop at 169–176 (p3).
- **Passages:**
  1. **7–116 (p1–2).** Framing. It gestures at "several incidents involving AI models and agentic AI systems carrying out unsanctioned or unintended activity" (14–16) but *does not describe any*. It says it is interim advice to be superseded by formal guidance (49–53). Autonomy is proportional to controls. Built-in model safeguards "should not be treated as holistic" (94–101).
  2. **200–311 (p3–5).** Sandboxing, with **two four-level maturity models** (network, 253–259; compute isolation, 282–292). These are ordinal classifications of *controls*, not of risks. Note 269–271: "When prompted or trained on the underlying model to do so, AI agents may be able to discover and exploit configuration issues, or potentially even vulnerabilities … a sandbox escape." Also "blast radius" (236, 300).
  3. **313–358 (p5–6).** Observability. It lists "chain of thought traces and transcripts" as telemetry (319) and says to treat agent activity "as a form of user activity" (332). Then attribution (watermarking outbound traffic) and "pull the plug" (352–358).

### ncsc-2026-defend-agentically — "One does not simply defend agentically" (Dave Chismon, CTO for Architecture, 21 Sep 2026) — 220 lines, 4 pp

- **TOC / glossary:** none.
- **Passages:**
  1. **7–59 (p1).** An *argument*, built from a quoted maxim (Halvar Flake: "All offensive problems are technical problems, and all defensive problems are political problems") through a purpose-of-the-actor analysis to an "inconvenient truth" conclusion (57–59). It is a structural asymmetry claim reached by reasoning, not evidence.
  2. **86–157 (p2–3).** Three "core principles" of current defence, then a **five-dimension × five-level (0–4) framework for the "riskiness" of an automated defensive action**: Potency, Scope, Criticality, Rollout confidence, Recoverability. **Garbled:** each dimension's one-line description is split and interleaved with its level rows (e.g. 104–105, 136–138, 148–149). Read it with the PDF open if you can.
  3. **177–193 (p3).** A named government programme (Cyber Shield, NCSC and DCMS) and a stated research need: "how we deterministically prove that 'low risk' actions really are low risk" (183–184).

### ncsc-2026-frontier-defenders — "Why cyber defenders need to be ready for frontier AI" (Paul J, NCSC, and Alan Steer, AISI; 30 Mar 2026) — 307 lines, 5 pp

- **TOC:** none.
- **Glossary:** "Glossary of terms used", 34–67 (p1–2), extracted from a web accordion, so the "Show" / "Show All" tokens are artefacts. *AI* (= GenAI unless stated), *Frontier AI models* ("the most capable models available at any given time", plus a claim about distillation), and *AI systems* ("combine models with tools, workflows and human oversight"; "Many of the benefits and risks … are delivered by AI systems rather than raw model capability alone").
- **Passages:**
  1. **72–112 (p2).** The measurement passage: AISI's multi-step cyber-range results, with a named model (Claude Opus 4.6) and step counts (15.6 / 9.8 / best 22 of 32), a human-time equivalence (≈6 of 14 hours), and a cost ("around £65"). A second-hand measurement, cited from AISI.
  2. **115–165 (p2–3).** Two "reinforcing trends", then the limitations. Hedges run in *both* directions: models fall short, and "these results likely underrepresent what current models are capable of" (147–150). There is also a boxed near-term detectability claim (155–158).
  3. **245–281 (p4–5).** "Shape the battlefield": a defender-advantage argument, with a boxed caveat that the advantage "is not guaranteed" (261–262).

### ncsc-2025-bugs-to-bypasses — "From bugs to bypasses: adapting vulnerability disclosure for AI safeguards" (Dr Kate S, NCSC, and Dr Robert Kirk, DSIT/AISI Safeguards; 2 Sep 2025) — 228 lines, 4 pp

- **TOC / glossary:** none. It defines *safeguards* inline at 29–33 (p1): "techniques developers use to prevent AI systems from producing policy-violating outputs or actions", which includes refusal training, unlearning and classifiers. It also names SBBP and SBDP (52–55).
- **Passages:**
  1. **29–60 (p1–2).** The definition, then a claim marked as belief ("We think applying these foundations will probably help", 44–45).
  2. **104–134 (p2–3).** Numbered best-practice principles. The example contrasts a vague scope with "a detailed model spec" (109–113). A disclaimer: a bounty programme "does not automatically mean the model or system is safe or secure" (132–134).
  3. **139–183 (p3).** The distinctive part: **asserted ignorance and open questions**. "We're assuming that lessons from decades of cyber security apply to AI systems, but there are probably also important differences" (143–144). "Unlike in cyber, established principles for judging the severity of safeguard attacks don't yet exist" (165–166). Then Anthropic's proposed jailbreak-severity criteria (166–172). The document holds a research agenda as content.

### ncsc-2025-prompt-injection — "Prompt injection is not SQL injection (it may be worse)" (David C, Technical Director for Platforms Research, 8 Dec 2025) — 237 lines, 6 pp

- **TOC / glossary:** none. It defines *prompt injection* at 8–12 (p1) and *indirect prompt injection* at 59–61 (p2).
- **Extraction note:** narrow-column web print. The `/` lines are page-edge artefacts. Otherwise clean.
- **Passages (or read it whole):**
  1. **1–31 (p1).** The coinage history and a definition that locates the flaw in *developer practice* ("developers concatenate their own instructions with untrusted content … and then treat the model's response as if there were a robust boundary"). It states the thesis as an argument ("This blog argues…").
  2. **66–122 (p2–4).** A mechanistic claim about LLMs ("there is only ever 'next token'", 83–84), leading to a possibility claim ("may never be totally mitigated", 87–88) and a reframe as an "inherently confusable deputy" (107–122). A reclassification argued from mechanism.
  3. **197–211 (p5–6).** A historical analogy used as a forecast: the SQL-injection decade, so "a similar wave of breaches may follow".

---

## C. Joint multinational guidance and statements

### fiveeyes-2026-ai-shift — "The AI shift in cyber risk: why leaders must act now" (Five Eyes cyber agency heads, 22 Jun 2026) — 141 lines, 3 pp

- **TOC / glossary:** none.
- **Read it whole.** A signed collective statement (six signatories at 105–136). It has the most compressed forecast in the set, with no evidence or hedge attached: "Frontier AI models are anticipated to exceed current industry expectations … The timeline is not years, it is months" (15–17, p1). Imperative leadership calls follow (19–23, 48–71). The register is exhortation.

### ncsc-2023-guidelines-secure-ai — "Guidelines for secure AI system development" (NCSC and CISA with 21 partner agencies, Nov 2023) — 848 lines, 20 pp

- **TOC:** 72–85 (p4).
- **Glossary:** none as such. Inline definitions: *ML applications* (193–199, p6), *adversarial machine learning* (201–212, p6), and *provider* / *user* (235–245, p7). Footnote 1 (797–801, p19) defines "provider" in EU-AI-Act-like terms ("places that system on the market or puts it into service under its own name or trademark"). Footnote markers 4 and 5 have no visible anchor in the body text.
- **Extraction note:** cover-page logo text at 3–4. Contributor list at 31–52 (Anthropic, OpenAI, Google DeepMind and others).
- **Passages:**
  1. **193–262 (p6–7).** "Why is AI security different?" and "Who is responsible", an allocation of responsibility along the supply chain ("providers of AI components should take responsibility for the security outcomes of users further down the supply chain", 249–250). There is also a criticality trigger (260–262).
  2. **295–386 (p9–10).** The distinctive voice: **guidelines written as present-tense statements of a desired state**, not as imperatives: "System owners and senior leaders understand threats…", "You are confident that the task at hand is most appropriately addressed using AI" (305, 331). A norm dressed as description. Your list of assertion types doesn't have a slot for it.
  3. **543–609 (p14–15).** Protect the model, incident management ("The inevitability of security incidents…", 571), responsible release (red teaming; "safety or fairness" named as out of scope, 590–591).

*(The other joint guidance, `asd-2026-careful-agentic`, and the NPSA booklet are in section E, after the codes of practice.)*

---

## D. Codes of practice and the ETSI standard (one text lineage, plus its parent governance code)

These three documents are one text at different stages. `dsit-2025-ai-cyber-cop` (Jan 2025) became ETSI TS 104 223 (Apr 2025) and then `etsi-2025-en304223` (Dec 2025). `dsit-2025-ai-cyber-cop-guide` is its implementation guide. **I checked mechanically:** across the 13 principles the provisions are word-for-word identical. The only changes are renumbering, US spelling, "your" → "the", "may" → "can", two added clause cross-references, one grammar repair (5.5.1-1), and reference lists converted to [i.N] form. So a quote from one is a quote from the other. They differ in the definitions and the stakeholder table (see the ETSI entry).

### dsit-2025-ai-cyber-cop — "Code of Practice for the Cyber Security of AI" (DSIT, 31 Jan 2025) — 725 lines, 18 pp

- **Not source text: lines 1–7** are a PROVENANCE block added by the agent that rendered the web page to PDF. Its own advice: the page numbers of this PDF are rendering artefacts, so cite by section. The page's footnotes (markers 1–8 in the body) are **absent** from the rendering.
- **TOC:** 22–29 (p2); principle list 239–266 (p7–8).
- **Glossary:** Annex A, 667–724 (p17–18). Stakeholder definitions (Developers, System Operators, Data Custodians, End-users, Affected entities) with an organisation-type mapping table, 130–217 (p5–7). A shall / should / may table, 220–234 (p7).
- **Passages:**
  1. **47–128 (p3–5).** The rationale ("AI has distinct differences to software"), a consultation measurement used as legitimacy ("endorsed by 80% of respondents … Support for each principle … ranged from 83% to 90%", 65–69), and scope ("AI security … considered a subset of cyber security", 81–82).
  2. **130–234 (p5–7).** The role taxonomy. Note the *Affected entities* definition, "individuals and technologies … that are **not directly affected** by AI systems" (170–172). As written it contradicts its own label, and it survives unchanged into ETSI (504–508). Then the modal-verb semantics.
  3. **390–413 (p11).** Principle 4, "Enable human responsibility", in full: five provisions mixing *should* and *shall*.
  4. **507–568 (p13–15).** Documentation and testing (8.x, 9.x). A causal premise sits inside a requirement: "As discovery of poisoned data is likely to occur after training (if at all), Developers shall document…" (527–531).

### etsi-2025-en304223 — ETSI EN 304 223 V2.1.1 "Securing AI; Baseline Cyber Security Requirements for AI Models and Systems" (Dec 2025) — 891 lines, 16 pp

- **TOC:** 83–116 (p3).
- **Glossary:** §3.1 Terms, 336–411 (p7–8). §3.3 Abbreviations, 418–422 (p8). Table 4-1 Stakeholders, 432–508 (p9–10). The modal-verbs clause is at 168–173 (p4): "'must' and 'must not' are NOT allowed in ETSI deliverables".
- **Passages:**
  1. **183–231 (p5–6).** Introduction and scope. The DSIT rationale text, now with a mapping to ISO/IEC 22989 lifecycle stages (200–210).
  2. **336–411 (p7–8).** Definitions, useful set against DSIT's Annex A. ETSI **drops** DSIT's definition of *Artificial Intelligence* and gives an ISO-style *AI system* instead ("engineered system that generates outputs … for a given set of human-defined objectives", 344–345). It drops *Adversarial AI*, *Explainability* and *Inference Attack*. It adds ISO-style *inference*, *prediction* (with NOTEs), *ML model* and *training data*.
  3. **432–508 (p9–10).** The stakeholder table, now **mapped to EU AI Act roles** ("Developers can be AI providers under the EU AI Act", 459–461; "System operators can be deployers … and can also be AI providers if they make changes to the system", 471–473). A fossil survives: "because the voluntary Code has placed expectations on Developers…" (491–494), even though the EN is not a voluntary code.
  4. **584–642 (p11–12).** Principles 3–4 in "Provision 5.1.x-y" form, if you want the typical texture of the normative body.

### dsit-2025-ai-cyber-cop-guide — "Implementation Guide for the AI Cyber Security Code of Practice" (DSIT-commissioned; author John Sotiropoulos, Kainos; 2025) — 2036 lines, 50 pp

- **TOC:** none.
- **Glossary:** Abbreviations 60–97 (p2–3). "Terms Used" 99–164 (p3–5). The terms *extend* the Code's glossary with *Agentic Systems*, *Excessive Agency*, *Hallucination*, *Prompt Injection*, *Evasion Attack*, *Model Extraction* and others. It also defines "regularly" operationally (241–242, p8).
- **Layout:** sections 4.x are **four-column tables** (Provision | Related threats/risks | Example measures | References). They are legible in the raw file at about 230 columns. The scenario names drift: the scenario is introduced as "LLM Provider" (200) but called "LLM Platform" in every table row.
- **Passages:**
  1. **166–246 (p5–8).** How to use it, and the **four worked scenarios** (Chatbot App, ML Fraud Detection, LLM Provider, Open-Access LLM). The fraud scenario is carefully drafted to sit outside EU AI Act Art 5(1)(c) (193–199). The key relational claim is at 218–233: "AI Security underpins all aspects of AI Safety and safeguards Responsible AI", with misuse declared "out of scope" but partly addressed anyway.
  2. **677–726 (p19–20).** Provisions 3.1.2–3.1.3. Scenario-conditional risk ratings ("Indirect Prompt Injections and Bias are rated as High when the app is used for recruitment but Low when used for summarisation", 720–721). Risk level is made a property of the deployment context, not of the model.
  3. **785–921 (p21–24).** Principle 4, human oversight, the full table. It shows the typical example pattern across the four scenarios, the UK GDPR Art 22 anchoring, and prohibited-use monitoring.
  4. **1615–1663 (p40–41).** Provisions 9.4 / 9.4.1 (output leakage; "unintended influence"). Jailbreak simulation appears as an example control.

### dsit-2025-cyber-governance — "Cyber Governance Code of Practice" (DSIT with NCSC, policy paper, 8 Apr 2025) — 469 lines, 12 pp

- Not part of the AI lineage above, but it is its parent. DSIT calls it "the foundational code in DSIT's modular approach", and says organisations implementing the AI Cyber Security Code "should also follow" it (135–149, p5). The DSIT AI code in turn calls itself "an addendum to the Software Code of Practice" (dsit-2025-ai-cyber-cop 73–76). **AI appears only incidentally** here (123, 147).
- GOV.UK web page printed to PDF: browser header and footer lines ("14/05/2025, 14:04 …", URL "n/12") on every page.
- **TOC:** 20–24 (p1).
- **Glossary:** 288–346 (p8–9). *Cyber security* is defined to include "harm caused intentionally by the operator of the system, or accidentally, as a result of failing to follow security procedures or being manipulated into doing so" (303–315). *Gain assurance* is defined (330–333), and it is the verb nearly every action uses. Extraction glitch: *Risk owner* is fused into the *Risk appetite* row (339–341).
- **Read it whole, or:**
  1. **55–149 (p3–5).** Audience and rationale. A survey statistic is used as the reason to act ("50% of businesses and 66% of high-income charities … 70% … 74%", 109–113), followed by "Cyber risk is a material risk for almost all organisations" (117–118).
  2. **154–283 (p5–8).** The 22 numbered **actions** in five groups (A Risk management … E Assurance and oversight). They are directives to board members, mostly "Gain assurance that…", and they cross-reference each other ("aligned with the agreed cyber risk appetite (Action A3)"). Obligations addressed to a governance role, not to a system.

---

## E. Other joint and protective-security guidance

### asd-2026-careful-agentic — "Careful adoption of agentic AI services" (ASD's ACSC lead; CISA, NSA, Cyber Centre, NCSC-NZ, NCSC-UK; 2026) — 1115 lines, 29 pp

- **TOC:** 3–32 (p3).
- **Glossary:** none. Inline definitions: *agentic AI* and its "key attributes" (80–101, p5), agentic vs generative AI (112–117, p5), *privilege compromise* (220–226, p8), *specification gaming* (301–305, p10), *confused deputy* (212–213, 231–233, p8).
- **Passages:**
  1. **36–117 (p4–5).** Purpose, scope and the definition of agentic AI. Note the blanket recommendation "organisations should only use agentic AI for low-risk and non-sensitive tasks" (60–61), and the list of agent attributes (goals, "statistical models", privileges, metrics).
  2. **192–345 (p7–10).** The **risk taxonomy** (privilege / design and configuration / behaviour / structural / accountability), each with a boxed **hypothetical "Scenario example"**: a constructed incident narrative, neither real nor forecast. The behaviour-risk subsection (301–340) is the notable part. A cyber-agency document states **alignment-literature claims without citation**: "AI agents may pursue their objectives in ways developers did not anticipate … This behaviour is known as specification gaming" (302–305); "Some AI systems have demonstrated capacity for strategic deception … misrepresents its actions to avoid shut down" (316–319); evaluation awareness (313–315); and, earlier, "may even bypass system-level instructions to achieve their objectives" (162–163, p7).
  3. **346–487 (p11–13).** Structural risks (orchestration, tool use, third parties, "rogue agents", communication) and accountability risks (attribution, accuracy, visibility). A good sample of risk description by mechanism.
  4. **841–895 (p22–23).** Controls that assume the agent may be an adversary: "Assess agents' ability to evade security measures", "Conduct regular assessments of an agent's ability to bypass safeguards" (869–872), and cryptographic attestation "where agents must prove that they are running expected and unmodified code" (892–893).
  5. **901–987 (p24–25).** Research asks (agent-specific evaluations, STPA / STPA-Sec / CAST) and a conclusion that ends in an explicit **planning assumption**: "organisations should assume that agentic AI systems may behave unexpectedly" (984–987).

### npsa-2024-secure-innovation — "Secure Innovation: Security Advice for Emerging Technology Companies" (NPSA and NCSC, 2024) — 644 lines, 21 pp

- **Not what the set might suggest:** it contains **no AI content** (grep for AI / artificial / machine learning / frontier: nothing). It is general protective-security advice for start-ups: state-actor IP theft, insider risk, export controls, investment screening.
- **Badly garbled:** booklet spreads (two printed pages per PDF page) plus sidebars interleave throughout. The contents page (30–49, p3) is scrambled.
- **TOC:** 30–49 (p3), garbled. **Glossary:** none.
- **Passages:**
  1. **82–103 (p5).** A threat-actor typology with *motives* attached: state actors (three motives), competitors, criminals.
  2. **The five numbered "CASE STUDY" boxes**, each an incident account with a press citation. They are the most distinctive form here: 01 at 145–157 (p6); 02 at 215–230 (p8, the Tesla insider-recruitment attempt); 03 at 380–396 (p13, interleaved with an NSI Act sidebar); 04 at 498–513 (p17); 05 at 594–621 (p19, interleaved with the further-information list).
- Oddity: the footer at 639–642 (p20) says "This information is supplied in confidence to the named reader … exempt from disclosure under the Freedom of Information Act", on a public booklet.

---

## F. The 2023 AI Safety Summit papers (DSIT, GO-Science)

`dsit-2023-capabilities` names `goscience-2023-future` and `hmg-2023-safety` as its "Annex A" and "Annex B (attached)" (1351–1353). They are not included in its PDF, but both are in this set. `dsit-2023-capabilities` line 223 says Annex A gives "more detail on AI capabilities in content creation, computer vision, theory of mind, memory, mathematics…", which matches GO-Science's "Current Frontier AI Capabilities (detail)" section (goscience 1384ff). All three share the Summit definition of *frontier AI*.

### dsit-2023-capabilities — "Capabilities and risks from frontier AI: A discussion paper on the need for further research into AI risk" (DSIT, Oct 2023) — 2366 lines, 45 pp

- **TOC:** 23–57 (p3).
- **Glossary:** 1259–1343 (p29–30). Among the entries, directly relevant to your schema: ***Risk factors*** "Elements or conditions that can increase downstream risks. For example, weak guardrails (risk factor) could enable an actor to misuse an AI system to perform a cyber attack (downstream risk)" (1338–1340). Also *Alignment* ("the process of ensuring…", 1270–1271), *Capabilities*, *Evaluations*, *Scaffold*, *Misgeneralisation*, *Open ended domains*.
- **Endnotes:** 1357–2366 (p31–45). About 280 numbered endnotes, and some carry **substantive claims** that never appear in the body (e.g. 2309–2311 on bad actors removing safeguards; 2343–2346 citing FTC romance-scam losses; 1955–1959 quoting the OpenAI Charter).
- **Passages:**
  1. **62–135 (p4–5).** The frame: "The UK Government believes more research into AI risk is needed" and "This report focuses on evidence for risks". The Summit definition of frontier AI (96–102). A distinctive claim about which risk is primary: "the overarching risk is a loss of trust in and trustworthiness of this technology" (91–94).
  2. **260–341 (p8–10).** "Frontier AI could be more capable than evaluations indicate" (elicitation via prompts, tools, scaffolds, fine-tuning), then the limitations debate, stated as competing evidence (general reasoning vs memorisation).
  3. **546–746 (p15–19).** The risk architecture: "cross-cutting risk factors" (technical and societal *conditions*) as distinct from risks, which fall under "societal harms, misuse and loss of control" (550–552). Then specification problem, evaluation, tracking deployment, standards, incentives ("race to the bottom", 724–730), and market concentration.
  4. **1081–1221 (p25–28).** Loss of control. Two contributing factors (hand-over vs active reduction, 1090–1097). **Expert disagreement is asserted as a finding in itself** ("This threat model is controversial", 1130). A necessary-conditions analysis follows: disposition plus capability (1133–1135). The capabilities appear as "early signs" (manipulation, cyber offence, autonomous replication).
- Also typical: each misuse risk uses a **Current capabilities / Projected capabilities / Potential Risks and Impacts** template (dual-use science 905–956, p22–23; cyber 958–1043, p23–25).

### dsit-2023-emerging-processes — "Emerging Processes for Frontier AI Safety" (DSIT, Oct 2023) — 2173 lines, 45 pp

- **TOC:** 217–263 (p6–7).
- **Glossary:** "Key terms", 274–294 (p8). Seven terms. *Dangerous capabilities* ("abilities of an AI system to cause significant harm due to intentional misuse or accident"), *Safety* ("the prevention and mitigation of harms from AI"), *Relevant government authority*, *Frontier AI organisation*. A **footnote** at 689 (p16): "Controllability is also sometimes referred to as 'alignment' or 'steerability'". The text defines controllability issues as "propensities to apply their capabilities in ways that neither the models' users nor the models' developers want" (661–664).
- **Passages:**
  1. **13–110 (p2–3).** The document classifies *itself*: a "potential list", "not … government policy that must be enacted", "a potential menu for a very small number of AI organisations", "the world's first overview" (28–35, 69–96). The epistemic status of every practice that follows is set here.
  2. **305–556 (p9–13).** Responsible Capability Scaling. The most commitment-shaped text in the set: pre-specified "risk thresholds", "operationalise … such that multiple observers with access to the same information would agree" (417–419), buffer thresholds against "overshooting" (440–443), ALARP (470–471), "prepare to pause" (516–521).
  3. **589–689 (p15–16).** Evaluations. The four-way split of what to evaluate (dangerous capabilities / controllability / societal harms / system security) and the alignment-synonym footnote.
  4. **1722–1914 (p37–40).** Misuse prevention. Practices in bolded-imperative-plus-rationale form, with trade-offs stated inside the practice (privacy vs log retention, 1797–1800; "the distinction between misuse and legitimate use can be ambiguous", 1780–1782).

### goscience-2023-future — "Future Risks of Frontier AI" (GO-Science, Oct 2023) — 2197 lines, 44 pp

- Every page carries the banner "NOT A STATEMENT OF GOVERNMENT POLICY". It is a running-header artefact, but it is also the document's declared status.
- **TOC:** 72–82 (p3).
- **Glossary:** 1340–1375 (p31). *Agency*, *Agentic*, *AGI* (with synonyms "General AI, Strong AI, Broad AI"), *Autonomy*, *Capability*, etc. Also footnoted definitions in the risk section: *existential risk* "we consider this to mean a risk of human extinction or societal collapse" (1142), and *misaligned* (1143–1146), both on p25.
- **Passages:**
  1. **18–62 (p2).** Executive summary. The voice is **reported expert opinion** ("experts repeatedly highlighted", "many experts see this as highly unlikely"), plus a double-negative evidential claim: "there is insufficient evidence to rule out that future Frontier AI, if misaligned, misused or inadequately controlled, could pose an existential threat" (54–57). It also claims risk derives from capability-in-use, not from generality (43–47).
  2. **424–520 (p11–12).** "Other Critical Uncertainties": risk as a function of context, ownership and access. It names companies and predicts market entrants (503–507).
  3. **671–777 (p17–18).** The scenario method ("Scenarios are not predictions", 679; built by "General Morphological Analysis", 711–716; benign scenarios deliberately excluded, 690–695) and **Scenario 1**, a past-tense narrative from 2030. The five uncertainty labels sit in a left column that interleaves with the narrative. The other four scenarios run 780–1017 (p19–22).
  4. **1073–1196 (p24–26).** The richest passage in my set for a schema. An **eight-way taxonomy of how future harm arises** (1080–1092). Then **necessary conditions** for existential risk ("To pose an existential risk, a model must be given or gain some control over systems with significant impacts", 1111–1117). Three named **pathways** (misalignment / single point of failure / overreliance, 1118–1130). A list of risk-raising capabilities (1131–1139). "Emergence is less tractable to traditional prohibitive regulations … than design" (1152–1153). Mitigations whose "technical feasibility … is uncertain, with experts holding opposing views" (1172–1178).

---

## G. Cabinet Office risk registers (national risk-assessment genre)

Both use landscape multi-column layouts. The extraction interleaves the columns, so **open the raw file wide**. It is much more legible than it sounds.

### cabinetoffice-2025-cra — "Chronic Risks Analysis" (Cabinet Office and GO-Science, 2025) — 4566 lines, 132 pp

- **TOC:** 3–32 (p3). Two columns, interleaved.
- **Glossary:** none. The document names 26 chronic risks but assesses 25 (end-to-end encryption is listed with "Analysis … under review", 286–287, 355–358). Each of the 25 assessments opens with a field labelled **"Definition"**, but it usually holds a *characterisation* of the risk ("Cyber attacks, such as ransomware, continue to pose a significant and ongoing threat…", 877–879) rather than a definition of a term. The AI one starts with a real definition and then turns into risk framing (1343–1356).
- **Passages:**
  1. **110–170 (p6–7).** What a "chronic risk" is (erodes the economy, community, way of life and/or national security; raises the likelihood of acute risks), and a **methodological disclaimer**: "their systemic and enduring nature make traditional, probabilistic impact assessments less effective" (145–147). The method is evidence gathering plus futures workshops plus "impact mapping". It is also typical of the interleaving.
  2. **848–1022 (p27–31).** The technology theme intro, then the full **per-risk template** for "Changes in the nature of cyber security threats": Definition / Current evidence (statistics: "43% of UK businesses", 889, 917) / Example vulnerabilities / Example mitigations / "Examples of additional benefits from taking action" / "What the future might hold", split into **Short-term trajectories** and **Longer-term uncertainties** / a connections diagram. It cites the NCSC 2024 PHIA judgement second-hand (910–915).
  3. **1333–1486 (p40–43).** The AI chronic risk ("Impacts from use and capability of artificial intelligence"). A sidebar statistic ("The computational resources used to train AI models doubles every 3 – 4 months", 1350–1352). The mitigations name AISI (1415–1419). The final page is a **connections diagram** whose edges are labelled with causal sentences ("Frontier AI may be used to design bioweapons" → CBRN attack, 1456–1464). It extracted as scattered text but is recoverable.
  4. **4419–4549 (p127–131).** Cross-cutting analysis: a **network measurement of the document's own risk graph** ("State threats has the largest total number of direct impacts … 11 in total", 4436–4438; "each is only impacted by two chronic risks", 4456–4457). It also gives edge polarity: **"Reinforcing" vs "Diminishing"** (4490–4498). This is the closest thing in my set to a causal-loop schema, and it is the document's own.
- Also distinctive: 206–270 (p9–10) instructs readers to *generate their own* scenarios (random risk selection, futures wheel, "+1 Y … 5-20 Y" rings, Mitigate / Adapt / Exploit / Continue / Terminate). The method is handed to the reader as content.

### cabinetoffice-2026-nrr — "National Risk Register 2026" (Cabinet Office, 2026) — 7618 lines, 223 pp

- **Page numbering:** in this file the printed folio is one ahead of the PDF page (the footer "National Risk Register 2026 19" is on PDF p18). The pages below are PDF pages.
- **TOC:** 4–110 (p2–4). Two columns, interleaved.
- **Glossary:** none. Definitions are inline in chapters 1–2: *reasonable worst-case scenario* ("not a prediction of what is most likely to happen … the worst plausible manifestation of that particular risk (once highly unlikely variations have been discounted)", 204–208, restated 376–380), *acute* vs *chronic* risk (226–230, 648–666), and the likelihood and impact scales.
- **AI's place:** there is **no AI risk** among the 95. AI is explicitly a chronic risk handled by the CRA (651–657, p20). It enters the acute risks as a **templated sentence** repeated across about a dozen summaries: "AI can automate the process of launching cyber-attacks … [the sector] will continue to monitor how current and emerging AI influences this risk". Instances are at 1689, 1838, 2043, 2217, 2362, 2429, 2497, 2571, 3721 and 7392, with variant wordings at 2296, 3644 and 5199 (the last names "DSIT and the AI Security Institute").
- **Extraction note:** each risk's plotted likelihood/impact dot is a graphic. Only the axes survive, so **individual scores are not in the text**. The full matrix at 559–603 (p18) lists risk numbers by cell, but the column alignment is fragile. Cyber and conventional-attack scores are published only as group averages (e.g. 2181–2184).
- **Passages:**
  1. **187–275 (p7–9).** What the NRR is: the external version of the classified NSRA, "transparent by default", RWCS, acute vs chronic, and what changed in this edition.
  2. **397–558 (p14–17).** Methodology, the most explicit **measurement semantics** in the set. The likelihood window is 5 years (non-malicious) or 2 years (malicious). Malicious likelihood combines intent × capability × vulnerability (416–421). Scores 1–5 map to percentages, with **Table 2 aligning them to the PHIA yardstick with numeric ranges** (402–426). This is the yardstick the two NCSC assessments lost in extraction. The extraction scrambles the rows, so here they are as checked against PDF p14: score 5 (>25%) = Almost certain (95-100%), Highly likely (80-90%), likely or probable (55-75%), Realistic possibility (40-50%) and Unlikely (25-35%); score 4 (5-25%) = Highly unlikely (5-25%); score 3 (1-5%) = Remote chance (0-5%); scores 2 (0.2-1%) and 1 (<0.2%) have no PHIA word. The whole upper half of the PHIA vocabulary falls into one NRR score. There are seven impact dimensions (443–470), example impact thresholds (Table 3, 481–496), logarithmic scales ("a score 3 risk is approximately 5 times more likely … than a score 2 risk", 527–530), and confidence ratings (532–549).
  3. **643–678 (p20).** Chronic risks and AI, and the statement that risk owners "must also evidence how chronic risks … manifest in, interact with and exacerbate acute events" (673–678).
  4. **2139–2210 (p65–67).** "Cyber attack: health and social care system", one full **risk-summary template**: recent incidents (named: DXS, Cl0p/Barts) / context / Scenario (RWCS) / Key assumptions / Variations / Response capability requirements by three actor classes / Recovery / Impact on vulnerable people / Common consequences / score. Its AI paragraph is the fullest in the NRR (2152–2163), including emerging "agentic AI", "where autonomy, access, and unclear ownership can significantly amplify the impact of failure".
- Also noteworthy: assertions about **withheld** content, e.g. "A separate scenario involving a nuclear attack on the UK mainland … is held internally at a higher classification" (7566, p221).

---

## Across the set: how these documents make claims

This is my reading, with line references so you can check it. Where I say "verified" I compared the texts directly.

**1. The same assertion travels between documents, and sometimes changes on the way.** This is the pattern with the most consequence for the schema.
- DSIT code → ETSI EN: provisions verbatim (mechanically verified, see §D), including DSIT's self-description as a "voluntary Code" surviving inside a European Norm (etsi 491–494).
- NCSC-A 2025 → NCSC blog 2026: a PHIA key judgement reused with its probability word intact (`ncsc-2025-impact` 132–133 → `ncsc-2026-ten-questions` 93–94).
- NCSC-A 2024 → CRA: cited second-hand (`cabinetoffice-2025-cra` 910–915).
- HMG 2023 → DSIT capabilities 2023 (verified): HMG says "**Generative AI** will almost certainly continue to lower the barriers to entry for less sophisticated threat actors" (hmg 118–119). DSIT repeats the sentence, citing HMG (endnote 192, line 2078), as "**Frontier AI** will almost certainly continue to lower the barriers…" (dsit-2023-capabilities 901–902). The probability word and the predicate survived. The subject noun changed to a narrower, differently defined class.

If the schema gives each assertion one home in one document, these chains will either duplicate silently or collapse wrongly. It looks to me like the schema needs a way to say "this is the same judgement as that one, reissued by X, with this change".

**2. Assertion forms your working list doesn't obviously hold.**
- *Claims conditional on a stated assumption.* "The assessment assumes no significant breakthrough in transformative AI" (ncsc-2024 109–112). "Assuming a lag, or no change to cyber security mitigations, there is a realistic possibility…" (ncsc-2025 47–49).
- *Claims about the state of expert opinion* rather than the world: "controversial", "many experts … some argue", "experts holding opposing views" (dsit-capabilities 1099–1102, 1130–1131; goscience 1107–1110, 1172–1173). In these passages the disagreement itself is what is being asserted.
- *Evidential-absence claims.* "insufficient evidence to rule out … an existential threat" (goscience 54–55, 1104–1106).
- *Necessary-condition analyses.* What would have to be true for loss of control or existential harm (goscience 1111–1117; dsit-capabilities 1133–1135, 1219–1221).
- *Hypotheticals that read like incident accounts but are not.* The NRR's reasonable worst-case scenarios ("not a prediction", nrr 204–206), GO-Science's 2030 narratives ("Scenarios are not predictions", 679) and ASD's "Scenario example" boxes. Only NPSA's case studies and the NRR's opening paragraphs report real events. A schema slot for "incident account" would swallow these unless incidents and scenarios are kept apart.
- *Planning assumptions*, where the reader is told to believe something for planning purposes. "defenders should assume that at least some attackers already have access to capable AI tools" (frontier-defenders 19). "assume breaches will occur" (fiveeyes 71). "organisations should assume that agentic AI systems may behave unexpectedly" (asd 985–986).
- *Norms written as descriptions.* "You are confident that the task at hand is most appropriately addressed using AI" (ncsc-2023 331).
- *Document-level status declarations* that scope every sentence inside: "NOT A STATEMENT OF GOVERNMENT POLICY" (every GO-Science page), "does not represent a policy position of HMG" (dsit-capabilities 16–18), "a potential menu" (emerging-processes 71), "interim practical advice" to be superseded (managing-agentic 49–53), "not about predicting the future" (cra 131). Every assertion in these documents seems to inherit a status from them.
- *Assertions about withheld content.* Classified scenarios, and scores published only as group averages (nrr 7566, 2181–2184).
- *Open questions as content* (bugs-to-bypasses 139–183; defend-agentically 183–186).
- *A document measuring its own causal graph* (cra 4436–4457, with reinforcing/diminishing polarity at 4490–4498).

**3. Vocabulary collisions I actually saw in this set** (not a survey):
- *frontier AI*: indexed to "today's most advanced models" and to *models* (hmg 19–23; dsit-capabilities 96–99; goscience 1364–1366). Or to *systems* that "provide a wide variety of tasks" (ncsc-2025 233–235). Or relative: "the most capable models available at any given time" (frontier-defenders 52). Or a synonym for "the most advanced generative AI" (thinking-agentic 16).
- *AI system*: ISO-style "engineered system that generates outputs … for a given set of human-defined objectives" (etsi 344–345). Infrastructure: "host infrastructure, management systems, access control systems…" (ncsc-2025 237–240). Model plus tools plus workflows plus human oversight (frontier-defenders 62–67). By reference to the White Paper's "adaptable" and "autonomous" (emerging-processes 278–279).
- *alignment*: a process (dsit-capabilities glossary 1270–1271). A synonym of "controllability" and "steerability" (emerging-processes 689). Defined negatively via "misaligned" as pursuing objectives "not in line with limitations embedded during development, and more broadly moral or ethical norms" (goscience 1143–1146). As conformance to guidelines, inside the definition of *guardrails* (etsi 353–354).
- *loss of control*: a top-level risk family with two causal factors (dsit-capabilities 1081–1097). An entry in a harm-mechanism list (goscience 1089–1090). An incident type for response plans (thinking-agentic 112). And, in the same DSIT paper as the first sense, "loss of control over personal data" as a cyber harm (dsit-capabilities 1032).
- *safeguard*: developer techniques that prevent policy-violating outputs (bugs-to-bypasses 30–31). Model-, inference- and harness-level controls, extensible to "deterministic provers" (managing-agentic 88–113). A property of ownership rules in engineering biology ("an additional safeguard against acquisition", cra 3720).
- *developer*: a supply-chain *role* anyone can hold, including an adapter or fine-tuner, and mapped to the EU "provider" (dsit-ai-cop 132–139; etsi 449–461). An *organisation* type (dsit-capabilities 1266–1267). "Frontier AI organisation" (emerging-processes 287). NCSC 2023 says "provider" instead (ncsc-2023 238–239, 799–801).
- *safety vs security*: "Safety and Security: The protection, wellbeing and autonomy of civil society and the population" (hmg 13–15). "Safety: the prevention and mitigation of harms from AI" (emerging-processes 292). "AI security … a subset of cyber security" (dsit-ai-cop 81–82). "AI Security underpins all aspects of AI Safety" (guide 218–219). "Cyber security is a necessary precondition for the safety … of AI systems" (ncsc-2023 164–165).

**4. A trend I'd flag, as reading rather than finding.** In 2023 the alignment-flavoured risks (misalignment, deception, loss of control) sit in the Summit papers, carefully hedged and footnoted. By 2026 similar claims appear *inside cyber-agency operational guidance*, stated flatly and without citation. Examples: "Some AI systems have demonstrated capacity for strategic deception" (asd 316), "may even bypass system-level instructions" (asd 162–163), agents discovering and exploiting sandbox vulnerabilities (managing-agentic 269–271), chain-of-thought traces as telemetry (managing-agentic 319). The epistemic register changed between the two genres. A schema that records the claim but not the register would erase that.

## Scope of my reading, and notes on the brief

- **Read whole:** all NCSC blogs and assessments, fiveeyes, hmg, ncsc-2023, the governance code, the DSIT AI code, ETSI, ASD, NPSA.
- **Read in part, the rest mapped by headings:** dsit-2023-capabilities (body 1–1360, except 760–898 societal harms; endnotes sampled); dsit-2023-emerging-processes (1–690, 1722–1914); goscience (1–220, 424–520, 671–800, 1022–1420; scenarios 2–5 and the capability detail not read closely); the implementation guide (1–260 and the tables cited); the CRA (method, cyber, AI, cross-cutting; the other 23 assessed chronic risks not read); the NRR (chapters 1–2, one full summary, and every AI mention by grep; about 90 other summaries not read).
- So the atlas's silence about a section is not a judgement that it's unrepresentative.
- **Pages:** every "(pN)" in this file was checked mechanically against the form-feed positions after writing (140 ranges, 0 mismatches). Line numbers are only as stable as this extraction. The NRR's printed folios run one ahead of the PDF page.
- **Two documents are barely about AI** (npsa-2024-secure-innovation: none; dsit-2025-cyber-governance: incidental). You may want to decide whether they belong in the corpus.
- **Source-file oddities:** `dsit-2025-ai-cyber-cop` is an agent's print-to-PDF of the GOV.UK page, with a provenance header (lines 1–7) and its footnotes lost. The ETSI EN is the more stable citable text for the same provisions. In relata metadata, two author fields look mis-split on "and": `dsit-2023-emerging-processes` reads `{Department for Science, Innovation; Technology}` and `asd-2026-careful-agentic` reads `{Cybersecurity; Infrastructure Security Agency}`. I didn't touch them.
