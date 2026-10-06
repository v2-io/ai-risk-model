# Eight source models of frontier-AI risk: an overview

*Assembled 2026-09-28 from the eight sections in this directory, for Joseph (to decide whether and what intermediate step to take before the full compilation) and for the coordinator (whose vocabulary layer will draw on §2). The models are presented on their own terms, not mapped onto `model/SCHEMA-SYNTHESIS.md`. My own readings are marked as mine; §4 is entirely mine.*

## How to read this

- **What it rests on.** Everything here comes from the eight sections: `iasr.md`, `eu.md`, `frontier-safety-frameworks.md`, `anthropic-openai.md`, `nist.md`, `uk-nrr-cra.md`, `mit-cais.md`, `uk-aisi.md`. Where a section was unclear, where two seemed to disagree, or where a lineage claim needed confirming, I checked the underlying extraction. Those places are marked **[checked: key L…]** and listed together in the Appendix.
- **Model names used below.** Several sections cover more than one document, so the tables use eleven rows:
  - **IASR**: International AI Safety Report 2025 and 2026.
  - **EU**: AI Act, GPAI Code of Practice (Safety and Security chapter), Commission Guidelines.
  - **FSF**: the frontier-safety-framework genre (GDM, Meta, Microsoft, Amazon, xAI, NAVER, G42, Cohere, NVIDIA, Magic, Shanghai AI Lab), not counting Anthropic and OpenAI.
  - **Anthropic**: RSP v2.2 and v3.x, Risk Reports (Feb and Aug 2026), Frontier Compliance Framework (FCF).
  - **OpenAI**: Preparedness Framework v2 (PF), Frontier Governance Framework (FGF).
  - **NIST**: AI RMF 1.0 and AI 600-1, with 800-1 and 800-2 noted where relevant.
  - **NRR** and **CRA**: the UK National Risk Register 2026 and Chronic Risks Analysis 2025, which are one system in two registers.
  - **MIT**: the AI Risk Repository (Slattery et al. 2026).
  - **CAIS**: *An Overview of Catastrophic AI Risks* (Hendrycks et al. 2023).
  - **AISI**: UK AISI's four partial models (Research Agenda, Frontier AI Trends, Loss of Oversight, Incident report).
- **Line references** are to the underlying extractions, exactly as the sections give them:
  - `md` = `ref/iasr-2026-full.md`;
  - `act` / `cop` / `guid` / `omni` = the EU texts;
  - `<key> L…` = `scratchpad/src-text/<key>.txt`.

  The section files carry fuller context for every reference.
- **"Absent" vs "not reported."** In the collision tables:
  - "absent" means the section reports that the model does not use the term;
  - "not reported" means the section says nothing about the term. That is *not* evidence of absence.
- **Three upstream sources** shape several of the eight without being among them: California's TFAIA (SB 53), the G7 Hiroshima Code of Conduct, and the OECD's AI-incident definition. I quote them where the lineage runs through them, from the extractions I checked.

---

## Headline observations

1. **The eight do not model the same object.** They model different things:
   - a *landscape* of risks (IASR, MIT, CAIS, CRA);
   - a *developer's go/no-go gate* (FSF, OpenAI, Anthropic v2.2, and the acceptance decision in the EU Code);
   - an *organisation's risk-management activity* (NIST);
   - a *national emergency scenario set* (NRR);
   - a *research and measurement programme* (AISI).

   Anthropic v3 moved from a gate toward a periodic, argued assessment of the whole company's risk. Much of what looks like disagreement between the sources is this difference in object.
2. **Only one model grades risk on calibrated scales: the NRR.**
   - IASR, NIST and the EU Act define risk as probability × severity, then decline to score it, or leave scoring to others.
   - The FSFs and OpenAI grade *capability* as a proxy for risk.
   - Anthropic grades risk in words inside a formal decomposition.
   - MIT, CAIS and CRA do not grade by design.
   - AISI's one graded instrument grades *oversight channels*, not harm.
3. **"Hazard" is load-bearing in only two places,** the NRR and NVIDIA's framework, and it means incompatible things in each. IASR defines it but hardly uses it, and four models don't use it at all. §2.1 has seven senses.
4. **Much apparent consensus is copying.** Examples:
   - The EU Code's loss-of-control formula ("reliably direct, modify, or shut down") now recurs in at least six frameworks and analyses, all later than the Code [checked].
   - TFAIA's ">50 people or $1B" threshold recurs as "systemic risk" in both companies' compliance documents.
   - Shanghai AI Lab's glossary is built from IASR 2025's [checked].
   - MIT's causal axis and CAIS's four sources both descend from Yampolskiy 2016.

   Agreement between sources is weak evidence until lineage is known (§3.1).
5. **Severity bars differ by more than an order of magnitude under shared words.**
   - TFAIA's catastrophic-risk floor (>50 deaths) falls in the NRR's *"Moderate"* impact band (41–200 fatalities).
   - OpenAI's "severe harm" is thousands of deaths.
   - Anthropic's RSP uses "catastrophic" in its plain meaning, glossed as "existential threats or fundamental destabilization of global systems".
6. **"Systemic risk" runs in opposite directions on the capability link.**
   - IASR's systemic risks arise "rather than directly from AI capabilities".
   - The EU's must be "specific to the high-impact capabilities".
   - The two companies' compliance documents use the term for TFAIA's mass-casualty threshold.

   IASR flags the EU difference itself, but its quotation of the Act is not in the Act's text [checked].
7. **Evidence postures are opposed.**
   - NIST 600-1 admits only risks with "an existing empirical evidence base" and excludes "speculative risks".
   - The EU Code invokes the Precautionary Principle.
   - The FSFs, Anthropic and OpenAI treat "cannot rule out" as "reached".
   - IASR makes the tension itself its organising idea (the "evidence dilemma").
8. **No model covers a whole chain from causes to policy.**
   - The UK splits at the event: probabilistic scoring for scenarios and consequences (NRR); futures and systems mapping, without probabilities, for drivers (CRA).
   - The frontier frameworks model the decision.
   - NIST models the management process.
   - IASR models capability-indexed risks with an evidence-maturity overlay.

---

## 1. The models compared

### 1.1 What each one models

| Model | Object modelled | Unit of analysis | Organising structure |
|---|---|---|---|
| **IASR** | The risk landscape of general-purpose AI, for policymakers | A named risk, in practice a topic area ("cyberattacks", "loss of control") | Capabilities → risks in three categories (malicious use / malfunctions / systemic, "not exhaustive or mutually exclusive", md 834) → risk management. Fixed per-risk template including a mandatory "Evidence gaps" slot. Loss of control as three necessary factors: capability × propensity × deployment environment (md 1244–1254) |
| **EU** | Legal duties on *roles*. For systemic-risk GPAI models, a provider's process for keeping risk acceptable | Two tracks: AI *systems* graded by use; GPAI *models* graded by capability. The Code's unit is the model, all versions (cop 1230–1247) | Code Appendix 1: 5 **types** × **nature** (3 essential, 6 contributing) × **sources** (14 capabilities, 10 propensities, 13 affordances) + 4 **specified risks**. Identify → analyse → accept? → mitigate, looping; Framework + Model Report; incident reporting |
| **FSF** | The developer's decision to continue developing or deploying | A capability threshold within a risk domain (CCL, TCL, Critical Capability Threshold, …) | The if-then gate: domain → threshold (+ early-warning threshold) → evaluations → determination → **security** safeguards (gate development) and **deployment** safeguards (gate release) → acceptance → decision |
| **Anthropic** | v2.2: the gate. v3: a periodic, argued assessment of the risk from the company's activities as a whole. FCF: statutory compliance | Threat model (4 in v3), across all models including internal ones | Threshold table: threshold / company plan / industry recommendation. Risk Reports per threat model give marginal and absolute risk. Aug 2026: misalignment risk R = Σ P·H·U over three misalignment types (Aug L993–1073) |
| **OpenAI** | The gate, with safeguard sufficiency | Tracked Category × High/Critical, per model | 5 admission criteria → 3 Tracked + 5 Research Categories; Capabilities Report → Safeguards Report (each harm vector covered by claims) → SAG recommends → Leadership decides |
| **NIST** | An organisation's risk-management activity, not the risks | An outcome statement (subcategory) | GOVERN / MAP / MEASURE / MANAGE → 19 categories → 72 subcategories; profiles instantiate the Core. 600-1 adds 12 GAI risks tagged to ~210 actions. 800-1 adds a threat-profile model of misuse |
| **NRR** | National acute emergencies, for contingency planning | One reasonable worst-case scenario (RWCS): 95 in all | Likelihood × impact matrix; risk → common consequences → 23 generic response capabilities ("cause-agnostic") |
| **CRA** | Long-term, erosive national trends | A chronic risk: 26 named, 25 assessed | 7 themes; a directed interaction network with chronic-risk, acute-risk and vulnerability nodes, edges signed Reinforcing / Diminishing (CRA L4491–4498) |
| **MIT** | How the literature carves AI risk | A risk *as some source presented it*: 1,725 rows from 74 documents | Two crossed taxonomies: Causal (Entity × Intent × Timing) and Domain (7 domains, 24 subdomains). Nothing links them except co-occurrence in a row |
| **CAIS** | Sources of catastrophic and existential AI risk, for a wide audience | A risk source with named hazards | Four causes: malicious use / AI race / organizational risks / rogue AIs ("intentional, environmental/structural, accidental, and internal", L244–245). Chains between them are narrated (§6), not structured |
| **AISI** | A government research programme's objects | Four partial models: research domain (Agenda), capability trend (Trends), oversight surface (LoO), sample/event/incident (Incident) | No single model. The section's reading of a spine: acceptable ⇐ won't attempt (alignment) ∨ can't succeed (control), argued in safety cases (Agenda 477–479) |

### 1.2 Grading and uncertainty

| Model | How risk is graded | How uncertainty is handled |
|---|---|---|
| **IASR** | Risk is *defined* as probability × severity (md 2480), but no risk is scored: "inclusion here does not necessarily imply a risk is likely, severe, or requires policy action" (md 836). Severity and likelihood appear as paired prose. Evidence maturity is ordered. One graded table: Table 2.3, on AI's contribution to observed cyber trends | The **evidence dilemma** as the organising idea (md 2326); mandatory Evidence-gaps subsections; expert disagreement reported as the finding; OECD scenarios instead of forecasts; no calibrated vocabulary of its own |
| **EU** | Three separate gradings:<br>1. Scope is binary: presumption above 10^25 FLOP (act 5663–5665), or designation on Annex XIII criteria.<br>2. Acceptability: provider-defined capability **tiers** whose *form* is prescribed (measurable, at least one not yet reached) but whose *values* are not (cop 547–552), plus a safety margin.<br>3. Incidents: initial reports due in 2 / 5 / 10 / 15 days depending on harm type | The Precautionary Principle (cop 123–127); a safety margin for uncertainty in sources, assessments and mitigations (cop 573–580); elicitation that matches misuse actors; external evaluators by default; the provider bears the burden of rebutting the presumption (guid 519–521); mitigations can't be used to escape classification (guid 577–581) |
| **FSF** | Capability is the proxy for risk; 1–4 tiers; thresholds mostly qualitative, phrased as uplift over a baseline. Acceptance is "a judgment assigned to someone". "no currently published safety framework sets explicit risk thresholds" (buhl L373) | A **safety buffer** (alert thresholds set below the threshold); "cannot rule out" treated as reached (gdm-2026-gemini L127–129); conservative elicitation; uncertain domains deferred by labelling them "exploratory" |
| **Anthropic** | v2.2: capability thresholds → ASL standards. Risk Reports: verbal grades ("Very low but not negligible" → "Low"), each given as marginal and absolute. Aug: formal decomposition whose factors get verbal grades; aggregation labelled conjunctive / disjunctive / convergent | "act as though the model has surpassed the Capability Threshold" (v2.2 L443–444); "provisionally meeting … to err on the side of caution" (Aug L5065–5068); an uncertainty adjustment made outside the argument ("very low … but … only low", Aug L1055–1056) |
| **OpenAI** | High / Critical capability thresholds; indicative thresholds plus "holistic judgment"; safeguards judged for sufficiency | Elicitation is "a lower bound, rather than a ceiling" (pf-v2 L409–411); "cannot rule out"; "precautionarily treated as High"; conservative upper bounds |
| **NIST** | Defined as probability × magnitude (RMF 272–278), then deliberately ungraded. Tolerance "not prescribe[d]" (398). One bright line: at "unacceptable negative risk levels … development and deployment should cease" (446–449) | "inability to appropriately measure AI risks does not imply" high or low risk (324–325); emergent risks are to be tracked; **600-1 admits only risks with an existing empirical evidence base** (600-1 187–194) |
| **NRR** | Likelihood 1–5: log bands from <0.2% to >25% over 2 years (malicious) or 5 years (non-malicious), labelled with PHIA words. Impact 0–5 on 7 dimensions, combined to 1–5 by a rule that is not published. Confidence low / medium / high | Mainly through the scenario: the worst *plausible* case "once highly unlikely variations have been discounted" (NRR L376–381). Also named Variations, confidence ratings and uncertainty lines |
| **CRA** | No probabilistic grading, by design (CRA L145–147). Structure is read from network counts | Futures framing; short-term vs longer-term; "not about predicting the future" (CRA L131) |
| **MIT** | None. Counts measure attention in the literature, not prevalence | A residual "Other" level on each causal variable; items too vague to code are excluded |
| **CAIS** | None | Prose labels: "plausible but not certain premises"; "most speculative" |
| **AISI** | LoO only: PHIA likelihood and a 4-level severity for degradation of oversight pathways, plus per-surface Status / Risk of Degradation / Impact if Lost / Preservability. Cyber tasks graded by human expertise. Otherwise measurements | PHIA; statistical intervals; directional bounds ("lower bound"); scope disclaimers; "we did not treat expert opinion as evidence on substantive questions" (LoO 3864–3866) |

### 1.3 Method, purpose, force, exclusions

| Model | Method and stated lineage | Purpose and audience | Force | Main exclusions |
|---|---|---|---|---|
| **IASR** | A literature synthesis by an independent writing team, with structured review. 2025 states six source-quality criteria. Risk-management structure borrowed from NIST AI RMF, ISO/IEC 23894, OECD and SRA; 2025 draws on safety engineering (STPA, safety cases, ALARP) | A "shared, science-based understanding" for policymakers | "not prescriptive" (md 2194) | Narrow AI; military AI; benefits as a subject; policy recommendations. From 2026 also bias, environment, privacy and copyright |
| **EU** | Probability × severity; EU product-safety law (New Legislative Framework, Blue Guide); "international approaches": recital 110 reproduces the G7 Hiroshima list [checked]. No named risk-management standard | Internal market plus protection of health, safety and fundamental rights; addressed to roles | Act binding (fines up to 3% / EUR 15m). Code voluntary: adherence "not conclusive evidence" of compliance and **no presumption of conformity** | Military / defence / national security; pre-market R&D (though the Code reaches earlier); risks not "specific to high-impact capabilities"; AI systems as such |
| **FSF** | METR's "responsible scaling" (2023); Anthropic RSP and OpenAI PF as templates; the Seoul commitments (May 2024) as trigger; RAND security levels; safety cases; ISO/NIST vocabulary arriving later; statutory absorption 2025–26 | Pre-committing to responses to severe risk; governments, peers, public; internal decision procedure | Voluntary and discretionary ("may", "as appropriate"); revised at will: "67% of material changes … are silent" (zhu L26–31) | Non-catastrophic harms; unknown risks; structural and systemic risk; for several, loss of control and radiological/nuclear risk; the harm itself |
| **Anthropic** | METR's RSP concept; v2.2 "inspired by safety case methodologies"; v3 a "strong argument" regime (Karnofsky: "FDA-inspired"); RAND SL4; the FCF cites ISO 42001 and NIST 800-53 | Internal procedure, public signal, "prototype" for regulation. v3 grades its own parts by force | Company-plan cells are commitments; industry recommendations and the Roadmap are explicitly not; the FCF is the legal document | Risks outside four threat models; radiological/nuclear and cyber dropped as RSP threat models; engineered misalignment; slowdown of safety research |
| **OpenAI** | "Holistic risk assessment"; admission criteria "informed in part by Meta's" framework; reports "parallel Anthropic's updated RSP"; the FGF cites ISO 42001, NIST AI RMF and METR | "Build trust" with public, governments, peers | Voluntary with internal decision rights; the FGF carries legal obligations | Anything below "severe harm"; anything not "instantaneous or irremediable"; persuasion |
| **NIST** | ISO 31000, ISO Guide 73, ISO/IEC TS 5723, OECD; the Core shape of NIST's cybersecurity framework; consensus process | Organisations and "AI actors" across the lifecycle | "Voluntary, rights-preserving, non-sector-specific, and use-case agnostic"; under a 2025 order to be revised | No risk catalogue, tolerance, scoring or templates (RMF); speculative risks (600-1). "hazard" and "loss of control" have 0 occurrences |
| **NRR** | Classified NSRA (National Security Risk Assessment) → declassified register; departmental risk owners; expert challenge panels; PHIA | Proportionate planning; local risk registers; practitioners | Informational | Chronic risks; completeness; highly unlikely variations; classified detail. AI is not an acute risk |
| **CRA** | GO-Science futures and systems thinking; impact mapping | Shared understanding; long-term preparedness | Informational; "may not represent current government policy" | Probabilities; the full network; the systemic-risk scenarios |
| **MIT** | Pre-registered systematic review; best-fit framework synthesis from Yampolskiy 2016 (causal) and Weidinger 2022 (domain); every change logged | "Harmonize" fragmented frameworks for developers, policymakers, auditors | Descriptive of sources; living and versioned | Severity, likelihood, interactions; single-sector frameworks; "sources of risk at a high level of abstraction" |
| **CAIS** | No stated method; four-way split cites Yampolskiy; historical analogy; safety-engineering vocabulary | Wide audience; to "inspire collective and proactive efforts" | Advocacy with "should" recommendations | Non-catastrophic harms except as precursors; any quantification |
| **AISI** | Evaluations, uplift studies, RCTs; FTA and STPA named but not shown; capability DAG; safety-case sketches; LoO: review + 25 interviews + PHIA | Government research organisation: "to equip governments with a scientific understanding" | None regulatory | Governance, compute, bias, labour, superhuman systems (LoO); diffuse economic and environmental effects (Trends) |

### 1.4 What the tables flatten

**Five kinds of model, not eight views of one thing.**
- *Landscape models* (IASR, MIT, CAIS, CRA) say what the risks are.
- *Gate models* (FSF, OpenAI, Anthropic v2.2, the EU Code's acceptance loop) say what a developer does when a model crosses a line. The risk content that sets the line (threat models, pathways) is mostly withheld or delegated.
- *Process models* (NIST RMF, the EU Code's process layer) say what an organisation should have in place. Risks are an output of using them, not an input.
- *Scenario models* (NRR) assess one constructed worst plausible instance per risk, and then deliberately stop caring about causes: consequences funnel into 23 capabilities.
- *Measurement models* (AISI Trends, LoO, NIST 800-2) say what can be observed and how trustworthy the observation is.

Anthropic's v3 Risk Reports are a hybrid: a landscape for one company, graded in words. Karnofsky defines them *against* safety cases, which are gate-shaped: "a Risk Report is simply supposed to characterize the current level of risk, whatever it is" (karnofsky L597–599).

**Where AI sits in each model.** In nine of the eleven, AI (or a model) is the subject. In the NRR, AI is not an acute risk at all. It enters as a templated context sentence in about ten infrastructure-cyber risk summaries, and no scenario has an AI system as its actor. In the CRA, AI is one chronic risk and a driver inside several others. The UK national model therefore contains no loss of control, no misalignment and no autonomous AI actor.

**The grading spectrum is a spectrum of what gets a number.**

| What is numerically bounded | Where |
|---|---|
| Probability and impact | NRR only |
| Compute | EU 10^25; TFAIA and Meta 2026 10^26 |
| Deaths or dollars, as a severity bar | TFAIA, FCF, FGF, OpenAI PF, xAI 2025 |
| Benchmark scores | a few FSF anchors, several later removed |
| Oversight-channel degradation | AISI LoO |
| Nothing | IASR, NIST, MIT, CAIS, CRA |

Everything else is words. The EU Code's estimation formats explicitly allow "'probability: unlikely' x 'impact: high'" (cop 442–446), without supplying values.

**Most of these models are moving targets, often fast.**
- IASR narrowed its scope between 2025 and 2026.
- The RSP went from v2.2 to v3.4 within 2026.
- Meta's critical threshold went from "Stop" to "Develop with Mitigations" (meta-2026 L1678–1679).
- xAI removed its numeric criteria in 2026.
- OpenAI dropped Low and Medium levels.
- NIST is under a revision order.
- AISI's teams were reorganised between the Agenda and the Incident report.

Zhu found that most changes are silent and most weaken commitments. A compiled claim without a version and date will go stale without anyone noticing.

---

## 2. Term collisions across the models

Each term below that more than one model uses gets:
- a table with each model's sense and its evidence (verbatim where the section gives a definition, otherwise a short quote), with line references;
- then a plain statement of where the senses actually collide.

The NRR and CRA share a row, because their section treats their vocabulary together. Upstream sources (TFAIA, OECD, STPA) appear in italics where they are the origin of a sense.

### 2.0 Index

| Term | Senses found | The sharpest collision |
|---|---|---|
| hazard | 7 | A non-malicious cause class opposed to "threat" (NRR) vs any event or activity with potential to harm (IASR) vs a system state (STPA). Load-bearing only in the NRR and NVIDIA |
| risk | 6+ | Probability × severity (IASR, EU, NIST) vs a scored worst-case scenario (NRR) vs a category as a source presented it (MIT) vs source, probability and outcome class all at once (CAIS) |
| harm | 3 | Undefined nearly everywhere; a counterfactual-baseline gloss (NIST 600-1, Anthropic) vs an enumerated list (EU) |
| severity | 5 | Magnitude of harm (most) vs duration + speed of onset (NVIDIA) vs damage to an oversight channel (AISI) vs a scaler for incident-reporting deadlines (EU) |
| likelihood / probability | 5 | P(scenario occurs at least once in 2 or 5 years) (NRR) vs likelihood that a causal link *exists* (EU Code) vs P(a degradation pathway arises absent effort) (AISI) vs frequency (NVIDIA) |
| catastrophic / severe | numeric bars from >50 deaths to existential | TFAIA's >50 deaths is the NRR's "Moderate" band; the RSP's "catastrophic" is existential-scale |
| systemic risk | 4 | IASR: "rather than directly from AI capabilities"; EU: "specific to the high-impact capabilities"; FCF and FGF: TFAIA's mass-casualty threshold |
| loss of control | 6 kinds of thing | Scenario vs risk vs model ability vs legal conduct vs research domain; whether irreversibility is required; whose control |
| control | 4 | A human ability vs a countermeasure vs a paradigm that works "regardless of whether models are aligned" vs a synonym for aligned |
| safeguard / mitigation | 5 | An umbrella vs narrow anti-misuse technical measures vs legal rights protection vs one of four NIST risk responses vs one of five CRA intervention types |
| incident / event | 5 | Harm required (EU, OECD/NIST, TFAIA 1–3) vs no harm required (AISI, TFAIA 4) vs non-compliance (G42) vs a signal awaiting investigation (Anthropic FCF) |
| capability | 5 | A property of a model (most) vs relative to the frontier (EU) vs a government *response* capability (NRR) vs Cohere's likely risks |
| threshold / tier / level | 5 | A compute scope trigger vs a capability trigger vs a line of risk acceptability vs a register's inclusion bar vs a measurement parameter |
| developer / provider / deployer | 4 | EU legal roles, with no "developer" vs NIST actors defined by task vs provider = infrastructure vendor (IASR) vs provider = frontier company (Stelling) |
| alignment / misalignment | 5+ | A model propensity vs a training activity vs a property of one computation vs a claim in a safety argument vs a synonym for controlled |
| vulnerability | 3 | A system weakness to be exploited (IASR, MIT) vs the exposure of people or places (NRR, CRA, EU "affected environment") vs a target's susceptibility as a likelihood input (NRR) |
| *Secondary (§2.17–2.28):* propensity, resilience, emerging, marginal risk / uplift / baseline, threat / threat model, risk source / factor, misuse, oversight, safety case, frontier / GPAI, deployment, risk tolerance / acceptable | | |

### 2.1 hazard

| Model | Sense | Evidence |
|---|---|---|
| IASR | Defined, barely used: an event or activity with potential to harm. Also two other senses: information hazards, and STPA-style "system-level hazards" | "Any event or activity that has the potential to cause harm, such as loss of life or injury." (md 2354) [checked]. 2025 adds "social disruption, or environmental damage" (2025 7954–7955). "information that may be harmful to share" (md 1099). "system-level hazards" (md 1698) |
| EU | Twice in the Act, both in the high-risk-*system* track; undefined. Not used in the Code or Guidelines | "The hazards of AI systems covered by the requirements of this Regulation" (act 1215); "residual risk associated with each hazard" (act 3835–3836, Art. 9) |
| FSF | Absent from GDM, Meta 2025, Amazon, NAVER and Cohere. **NVIDIA**: undefined but the unit of risk analysis, each hazard scored. **Shanghai**: defined, copying IASR 2025. Microsoft: in passing | NVIDIA: "identify possible hazards, estimate the level of risk for each hazard" (nvidia L196–197). Shanghai: "Any event or activity with the potential to cause harm, such as loss of life, injury, social disruption, or environmental damage." (L2130–2131) [checked] |
| Anthropic | Not a model term; "infohazard" only | Aug L2931 |
| OpenAI | Not a model term; "information hazards" only | astra L3650 |
| NIST | **Absent** (0 occurrences in RMF and 600-1) | — |
| NRR/CRA | Undefined. A **non-malicious** source class (accidents, natural hazards), opposed to malicious "threats"; a chapter heading | "non‑malicious, such as accidents or natural hazards" (NRR L197–198) |
| MIT | Used, undefined; always paired as "hazards and harms", which is what the Domain Taxonomy classifies | L344, L470, L922, L1021 |
| CAIS | Used loosely in three senses: the risk sources themselves; items within them; the engineering sense | "three hazards of AI development: environmental competitive pressures …, malicious actors …, and complex organizational factors" (L1753–1755); "we describe specific hazards" (L31); "the hazards of the technology involved" (L1423) |
| AISI | Essentially unused. "hazardous capabilities"; a loose "crosscutting hazard". STPA is named but its hazard sense is never used | Trends 224; LoO 3677; Agenda 493 |
| *STPA (upstream)* | A system state | "A system state or set of conditions that, together with a particular set of worst-case environmental conditions, will lead to a loss (Leveson …)" (barrett-2025-stampstpa L1075–1076) [checked] |

**Where they collide.** Seven senses here, and an eighth outside the eight models (added 2026-10-06, below):
1. an event or activity with potential to harm (IASR; Shanghai, copied);
2. an item in a product-safety analysis that carries its own risk estimate (EU Art. 9; NVIDIA, FMEA-style);
3. a non-malicious *cause class* defined by the absence of intent (NRR);
4. a harm category, paired with "harm" (MIT);
5. a risk source or cause category (CAIS);
6. information harmful to share (IASR, Anthropic, OpenAI);
7. a system state that leads to loss given worst-case conditions (STPA, named by IASR and AISI but used by neither);
8. outside the eight models: a root cause of AI risk (Schnitzer et al., "AI Hazard Management", arXiv 2310.16727; see `../gamma-research/risk-formalisms.md` §2.10).

The only two models that put weight on the word are incompatible. The NRR's hazard excludes malicious causation by definition. NVIDIA's hazard is a scored unit, whatever its source. Senses 1 and 7 differ in kind: an event or activity on one side, a standing condition of a system on the other. Four models (NIST, Anthropic, OpenAI, AISI) do not use the word as a term at all. So in frontier-AI usage "hazard" is nearly unclaimed. Any definition will still collide with IASR's glossary, the civil-contingencies usage and STPA.

### 2.2 risk

| Model | Sense | Evidence |
|---|---|---|
| IASR | Defined as probability and severity of harm; used in practice as a topic area. Never scored | "The combination of the probability and severity of a harm." (md 2480); 2025 adds "that arises from the development, deployment, or use of AI" (2025 7952–7953) |
| EU | Probability of harm combined with its severity | "'risk' means the combination of the probability of an occurrence of harm and the severity of that harm" (act 3142) |
| FSF | Mostly undefined ("risk of severe harm"). GDM v3.1 defines inherent and residual risk *assessments*. **NVIDIA** adds controllability. **Shanghai** copies IASR 2025 | NVIDIA: "the potential for an event to lead to an undesired outcome, measured in terms of its likelihood (probability), its impact (severity) and its ability to be controlled or detected (controllability)" (L203–205), scored as "Risk = frequency x (duration + speed of onset) x (detectability + predictability)". Shanghai: "The combination of the probability and severity of harm arising from the development, deployment, or use of AI." (L2128–2129) [checked] |
| Anthropic | Undefined in general. Risk Reports split **absolute** risk (industry-wide if all were like Anthropic) from **marginal** risk (over other developers). Misalignment risk is an expectation | "misalignment risk… the expected total unmitigated harm induced by misaligned computations produced by covered models" (Aug L969–971); marginal / absolute (Feb L260–268) |
| OpenAI | "risk of severe harm"; undefined separately | pf-v2 L8–9 |
| NIST | A composite of probability and magnitude of an event's consequences, **positive or negative** | "the composite measure of an event's probability of occurring and the magnitude or degree of the consequences of the corresponding event" (RMF 272–274), adapted from ISO 31000 |
| NRR/CRA | Undefined as a concept. NRR: a class of emergency *and* its scored scenario, counted as a unit. CRA: a long-term trend | "87 standalone risks, and 8 linked scenarios for a total of 95 risks" (NRR L673–674) |
| MIT | The possibility of an unfortunate occurrence (SRA). In practice, whatever a source listed as a risk: events, causes, conditions or capabilities | "the possibility of an unfortunate occurrence associated with the development or deployment of artificial intelligence" (L700–702) |
| CAIS | Undefined; three senses at once: source, probability, class of outcome | "four risk sources" (L236); "increase the probability" (L2275); "catastrophic risks" |
| AISI | Undefined; "Risks posed by …" in each domain definition | Agenda 155–178 |

**Where they collide.**
- IASR, the EU and NIST share the probability × severity form. That form is ISO/IEC Guide 51's (product safety). ISO 31000 and ISO Guide 73 define risk differently, as "effect of uncertainty on objectives". NIST's "Adapted from: ISO 31000:2018" follows its sentence on positive and negative impacts, which is ISO 31000's note, while the core of its definition matches OMB A-130's form. IASR names SRA and ISO/IEC 23894 among its borrowings. (Corrected 2026-10-06; evidence in `../gamma-research/risk-formalisms.md` §2.4.)
- NIST's version includes *positive* consequences, which no other model does.
- None of the three applies the formula to produce a number.
- In the NRR, a "risk" is a *scenario instance*.
- In MIT it is a *row describing someone else's category*. The rows mix events, causes and capabilities.
- In CAIS the one word carries cause, probability and outcome.
- Anthropic's *absolute vs marginal* split has no counterpart in the regulators' definitions. IASR's "marginal risk" is a different baseline (§2.20).

### 2.3 harm

| Model | Sense | Evidence |
|---|---|---|
| IASR | Used ~190 times, undefined: the realised outcome of which risk is the probability-weighted form. "Documented harms" separate materialised risks from emerging ones | md 394 |
| EU | Undefined (185 uses in the Act). Given by enumeration: the serious-incident list, and the Code's five types | act 3331–3344; cop 1397–1404 |
| FSF | "Severe harm" undefined (GDM). Meta: "catastrophic outcomes". NAVER 2.0: subjects of protection × protected values | meta-2025 L1076–1078; naver-2026 L147–219 |
| Anthropic | Undefined. "Harm-inducing" is defined **counterfactually** | a computation that "increase[s] expected future harm above that coming from a baseline benign or null computation" (Aug L933–948) |
| OpenAI | "Severe harm" defined by a numeric bar (§2.6) | pf-v2 L33–36 |
| NIST | Undefined in the RMF. 600-1 gives a **counterfactual** gloss | "The notion of harm presumes some baseline scenario that the harmful factor (e.g., a GAI model) makes worse" (600-1 257–262) |
| NRR/CRA | What impact measures; not separately defined | NRR L451–453 |
| MIT | Undefined; paired with hazard; the "consequent harms" the domains capture | L138, L470 |
| CAIS | not reported | — |
| AISI | Undefined. "real-world harm" is distinguished from real-world "effect" | aisi-2026-incident-blog 206–209 |

**Where they collide.** No model defines harm itself. Two define it *relative to a baseline*: NIST 600-1 and Anthropic. That makes harm a marginal quantity, and it lines up with the uplift and baseline machinery in §2.20. The EU makes harm a *closed list of kinds*. AISI's harm/effect distinction matters for incidents (§2.11): an effect can happen without harm.

### 2.4 severity (and impact, magnitude)

| Model | Sense | Evidence |
|---|---|---|
| IASR | Undefined; always paired with likelihood in prose; no scale | "uncertain likelihood but potentially extreme severity" (md 1246) |
| EU | Undefined. A factor of risk, **and** a scaler of incident-report detail and deadlines | act 3142; "appropriate for the severity of the incident" (cop 1039–1040) |
| FSF | Mostly undefined. **NVIDIA: severity = duration + speed of onset**, with no magnitude term. GDM grades "significant but not severe" (TCL) without defining either | nvidia Table 1, L220–240; gdm v3.1 L851–853 |
| Anthropic | "Potential magnitude of impact" in the Risk-Report template; "severe misalignment" = could contribute to a priority pathway | Feb L478; Aug L929–931 |
| OpenAI | The severe-harm bar; exploit "severity levels"; undefined | pf-v2 L35; fgf L230 |
| NIST | "magnitude or degree of the consequences"; "severity" only in passing | RMF 273, 276–277, 711 |
| NRR/CRA | Informal. The scale is called **impact**: 0–5 on 7 dimensions, combined to 1–5; 5 = catastrophic | NRR L449–458 |
| MIT | Explicitly not captured | L605–607 |
| CAIS | Not quantified | — |
| AISI | **LoO: how badly a pathway would undermine an *oversight channel*** (extremely high / high / medium / low). Incident: "ordered roughly by severity", undefined. Exploit outcomes | LoO 257–261; Incident 405; kimi 144–146 |

**Where they collide.** Most models mean the size of harm to people, property or society, but none except the NRR puts that on a scale. Three senses are different quantities altogether:
- NVIDIA's severity is *temporal* (how long, how fast);
- AISI's LoO severity is damage to *our ability to see*, not harm to anyone;
- the EU's incident severity is an *administrative* scaler.

A compiled "severity" field would need to record which quantity is meant.

### 2.5 likelihood / probability

| Model | Sense | Evidence |
|---|---|---|
| IASR | Prose only; numbers appear only as reported elicitations (FRI) | md 714, 736 |
| EU | "Probability" is a factor of risk. "Likelihood" appears mainly as the **likelihood that a causal link exists** between a model and an incident: attribution, not occurrence | "establish or suspect with reasonable likelihood such a causal relationship" (cop 1047–1066); "the reasonable likelihood of such a link" (act 6877) |
| FSF | Mostly undefined. NVIDIA: likelihood = **frequency** (4 levels). Meta 2025 uses neither word | nvidia L220–240 |
| Anthropic | Used, undefined. P is the probability of a misalignment *type* in R = Σ P·H·U; "expected damages" = probability × size, summed | Aug L993–1073; Feb fn 41 L4011–4016 |
| OpenAI | Used, undefined | fgf L230 |
| NIST | A component of risk; not scaled | RMF 272–278 |
| NRR/CRA | NRR: the probability that the RWCS occurs **at least once** in a 2-year (malicious) or 5-year (non-malicious) window, banded 1–5 on log scales with PHIA labels. For malicious risks, a composite of intent × capability × target vulnerability. CRA rejects probabilistic assessment | NRR L404–425; L416–421; CRA L145–147 |
| MIT | Explicitly not captured | L605–607 |
| CAIS | Informal | L231–232 |
| AISI | LoO only: "how likely a pathway is to arise absent substantial effort to prevent it", on PHIA, scoped to the regime before full automation of AI R&D | LoO 257–261 |

**Where they collide.**
- **Different events.** The EU Code's "likelihood" in incident reporting is about *whether the model caused the incident*, a different question from likelihood of occurrence.
- **Different windows.** The NRR's window is fixed at 2 or 5 years. AISI's is a capability regime. Anthropic's is the Risk Report's horizon. Others have none.
- **The same yardstick, different events.** The NRR and AISI both use PHIA. But the NRR folds every PHIA word from "Unlikely (25–35%)" upward into its top score, 5 [checked: cabinetoffice-2026-nrr L400–427]. So an AISI pathway judged "unlikely" and one judged "likely" would both be NRR-5 events, if they were NRR events at all.
- **Conditioned or not.** AISI's likelihood is conditional on no preventive effort; the NRR's is not stated as conditional.

### 2.6 catastrophic / severe: the numeric bars

| Model or source | Term | Bar | Evidence |
|---|---|---|---|
| *TFAIA (upstream)* | catastrophic risk | death of or serious injury to **>50 people** or **>$1B** property damage, "arising from a single incident", through one of three named conducts (CBRN expert assistance; unsupervised cyberattack or crime-equivalent conduct; "Evading the control of its frontier developer or user") | california-2025-sb53 L187–199 [checked] |
| Anthropic FCF | **systemic** risk | ">50 fatalities arising from a single incident, or 1 billion dollars of financial damages", "including but not limited to" | FCF L118–121 |
| OpenAI FGF | **systemic** risk | "greater than 50 fatalities or $1 billion of property damages or losses arising from a single incident" | fgf L121–127 |
| FSF: xAI 2025 FAIF | catastrophic risk | TFAIA verbatim | xai-2025-faif L32–35 |
| FSF: xAI RMF 2025 | catastrophic malicious use events | ">100 deaths or over $1 billion in damages" | xai-2025-rmf L95–98 |
| OpenAI PF | severe harm | "the death or grave injury of **thousands** of people or **hundreds of billions** of dollars" | pf-v2 L33–36 |
| NRR | catastrophic = impact score 5 | fatalities **>1,000**; casualties >2,000; tens of billions of £. **>50 fatalities falls in band 3 (41–200), "Moderate"** | NRR L456–458, L481–496 |
| Anthropic RSP | catastrophic risk | "plain meaning": "existential threats or fundamental destabilization of global systems" | v3.0 fn 1 L137–141 |
| FSF: Meta | catastrophic outcomes | "large scale, devastating, and potentially irreversible harmful impacts on humanity" | meta-2025 L1076–1078 |
| CAIS | catastrophic / existential | "devastating consequences for vast numbers of people"; existential = "catastrophes from which humanity would be unable to recover" | L227–231 |
| FSF: GDM | severe / significant | undefined; TCLs cover "significant but not severe" harm | gdm v3.1 L851–853 |
| NIST | catastrophic | once, undefined, as a trigger to cease | RMF 446–449 |
| IASR, EU, AISI | — | no numeric bar ("extreme severity"; "significant impact on the Union market"; "severe and widespread harm") | md 1246; act 3420–3423; Agenda 97–98 |

**Where they collide.**
- **One word, two orders of magnitude.** "Catastrophic" spans a >50-death legal floor (TFAIA) and existential scale (the RSP). The NRR calls the >50-death level "Moderate".
- **One threshold, two names.** The TFAIA threshold is called "catastrophic" in California law and "systemic" in both companies' compliance documents.
- **Units and counting rules differ.** Bars are set in deaths or dollars (TFAIA, xAI, OpenAI), or across seven dimensions (NRR). Some are counted per single incident (TFAIA), some per scenario over a window (NRR), some over humanity's future (RSP, CAIS).

### 2.7 systemic risk

| Model | Sense | Evidence |
|---|---|---|
| IASR | Risks from widespread deployment changing behaviour, practices and structures, "rather than directly from AI capabilities". Three wordings. IASR notes the EU differs, and quotes the Act as saying something the Act's text does not say | Glossary md 2522; intro footnote md 487; 2025 11446. IASR says the Act refers to models that pose "risks of large-scale harm" (md 487). **That phrase is not in the Act, Code or Guidelines extractions** [checked: eu-2024-ai-act, eu-cop-2025-safety-security, ec-2025-gpai-guidelines]. The same wording is in the FCF: "foreseeable and material risks of large-scale harm" (FCF L118) |
| EU | The Code's whole object: risk "specific to the high-impact capabilities", with Union-scale impact, "propagated at scale across the value chain" | act 3420–3423; its three limbs become the Code's "essential characteristics" (cop 1426–1432) |
| FSF | Shanghai names systemic risk and puts it out of scope. xAI 2026 adopts the EU Code's term. GDM mentions only "structural risks" | shanghai L420–423; xai-2026 L40–42; gdm v3.1 L148–151 |
| Anthropic | FCF: TFAIA's numeric bar, covering both TFAIA's "catastrophic" and the EU's "systemic". The RSP says "catastrophic" instead | FCF L87–90, L118–121 |
| OpenAI | FGF: the same bar | fgf L121–127 |
| NIST | Not a risk term. "Systemic" names one of three bias categories. 600-1's footnote grouping is "Ecosystem / societal risks (or systemic risks)", derived in part from the IASR interim report | RMF 869–880; 600-1 205–213 [checked] |
| NRR/CRA | Adjectival: chronic risks' "systemic and enduring nature"; the CRA's unpublished "systemic risk scenarios"; the NRR's health-cyber paragraph "expanding the attack surface and systemic risk" | NRR L662; CRA L145–161; NRR L2152–2163 |
| MIT, CAIS | not reported as a term. MIT's Domain 6 and CAIS's "AI race" (the "environmental/structural" cause) cover similar ground | — |
| AISI | Not a term. The **Societal Resilience** domain, "Risks that will emerge as frontier AI systems are deployed widely and interact with economic and societal structures" (Agenda 175–176), covers the ground of IASR's systemic risk (my reading) | — |

**Where they collide.** Four senses, two of them opposed on the same axis.
- **IASR:** diffuse and deployment-driven, *not* directly from capability.
- **EU:** *must* be specific to frontier capability. Anything else is excluded however serious (cop 1428).
- **FCF and FGF:** a mass-casualty threshold from a single incident. In IASR, that is the malicious-use or malfunction category, not the systemic one.
- **UK:** networked, enduring and interacting.

A labour-market effect is systemic for IASR and outside EU systemic risk. CBRN uplift is EU-systemic and FCF-systemic but IASR "malicious use". The word cannot be carried across these models without a sense tag.

### 2.8 loss of control

| Model | What kind of thing it is | Evidence |
|---|---|---|
| IASR | A **scenario**, with two irreversibility wordings; active distinguished from passive (over-reliance) | "A scenario in which one or more general-purpose AI systems come to operate outside of anyone's control, with no clear path to regaining control." (md 2382); the body says "regaining control is either extremely costly or impossible" (md 1237, 1244); passive = "over-reliance on AI for decision-making" (md 1258) |
| EU | A **risk**, one of four specified risks, with a list of source mechanisms. In the Act, only a phrase in recital 110 | "Risks from humans losing the ability to reliably direct, modify, or shut down a model. Such risks may emerge from misalignment with human intent or values, self-reasoning, self-replication, self-improvement, deception, resistance to goal modification, power-seeking behaviour, or autonomously creating or improving AI models or AI systems" (cop 1530–1533); "unintended issues of control relating to alignment with human intent" (act 1922–1924) |
| FSF | Varies by framework: a **situation** (Meta 2026), a **model ability** (Microsoft 2026), a **risk domain** (Amazon 2026), the **EU formula** (xAI 2026), **IASR's scenario** (Shanghai), **disempowerment** (NAVER 2024, dropped in 2.0). Not a domain for GDM | Meta: "humans lose—and cannot feasibly regain—the ability to direct, modify, contain, or shut down AI systems" (meta-2026 L826–828). Microsoft: "A model's ability to undermine effective human control …" (microsoft-2026 L101–103). Amazon (L122–124). xAI (xai-2026 L25–26). Shanghai (L2116–2117) [checked]. NAVER (naver-2024 L69–71). GDM blog: "operators' ability to direct, modify or shut down" (L45–47) |
| Anthropic | Not used in the RSP or Risk Reports. FCF: a **scenario of autonomous goal pursuit**; its Tier 1 and 2 are the RSP's misalignment and automated-R&D rows. The FCF does not use the EU formula [checked: grep] | "scenarios where AI models develop and pursue goals autonomously that conflict with their developers' intentions or users' interests" (FCF L317–331) |
| OpenAI | Not used in the PF. The FGF **combines the EU formula with TFAIA's conduct clauses** (my reading, checked against TFAIA's text) | "Risks stemming from the inability to reliably direct, modify, or shut down a model, including evading the controls of a model developer or user, or autonomous conduct that, if conducted by a human, would constitute a crime…" (fgf L200–210) |
| NIST | **Absent** (0 occurrences) | — |
| NRR/CRA | **Absent** | — |
| MIT | Used, undefined. Called a "domain of impact", but no domain has that name. It sits inside 7.2 | L138; "possession of dangerous capabilities may itself be a sufficient condition for the loss of control" (L2130–2131) |
| CAIS | An **outcome** of rogue AIs; also gradual | "If an AI system is more intelligent than we are, and if we are unable to steer it in a beneficial direction, this would constitute a loss of control" (L1756–1758); "humans gradually cede more control" (L1799–1800) |
| AISI | Never defined. An **outcome** (Trends); folded into the **Autonomous Systems** domain (Agenda); a research programme's name. LoO is about *oversight* and excludes impacts "beyond loss-of-control" | Trends 1642–1643; Agenda 173–174; LoO 3971–3972 |
| *TFAIA (upstream)* | A **conduct** that qualifies a catastrophic risk, and a **critical safety incident** type | "(C) Evading the control of its frontier developer or user." (sb53 L199); "(3) Loss of control of a frontier model causing death or bodily injury." (sb53 L211–216) [checked] |

**Where they collide.**
- **Category.** It is a scenario or outcome (IASR, CAIS, Meta, Trends), a risk (EU, OpenAI FGF), a model ability (Microsoft), a legal conduct or incident type (TFAIA), a domain (Amazon, AISI), and absent (NIST, NRR, CRA, the RSP, the PF).
- **Irreversibility.** It is required by IASR's glossary ("no clear path to regaining"), Meta ("cannot feasibly regain") and Trends ("irreversible"). It is softened in IASR's own body ("extremely costly or impossible"). It is not required by the EU formula or TFAIA.
- **Whose control.** "anyone's" (IASR), "humans" (EU, Meta), "its frontier developer or user" (TFAIA), "operators" (GDM).
- **Active vs gradual.** Gradual loss is included by IASR (as passive), CAIS and Shanghai. It is not covered by the EU formula or TFAIA.
- **Convergence by copying.** Since July 2025 the EU Code's wording has become the template. xAI 2026 copies it verbatim. OpenAI's FGF embeds it. Meta, Amazon, Microsoft ("reliably directed, modified, or shut down") and GDM paraphrase it. Stix et al. and METR quote it as the Code's [checked: stix-2025-loss L381, L747, L834; metr-2025-common-elements L1041]. A search over all extractions finds it in nine documents besides the Code. All post-date it, and they are one source, not nine.

### 2.9 control

| Model | Sense | Evidence |
|---|---|---|
| IASR | (a) A **human ability** to influence and halt a system; (b) "controls" as **countermeasures** in risk management | (a) "The ability to influence the behaviour of a system in a desired way. This includes adjusting or halting its behaviour if the system acts in unwanted ways." (md 2274). (b) "implementing controls and countermeasures" (md 1717) |
| EU | Four senses: loss of control; administrative "market surveillance and control"; a capability "to control physical systems"; independence ("free from the Signatory's control"). Control over weights is also a role test | cop 1470, 1185; guid 790–793 |
| FSF | Meta 2026: **control mechanisms** (measures). Shanghai: a **human ability** (≈ IASR 2025). NVIDIA: **controls** are per-hazard measures, and **controllability** is a risk attribute | meta-2026 L795–797; shanghai L2114–2115; nvidia L204, L283–292 |
| Anthropic | not reported as a term | — |
| OpenAI | "security controls" as a class parallel to "safeguards" | pf-v2 L497–512 |
| NIST | Control **types** in the ordinary risk-management sense | "compensating, detective, deterrent, directive, and recovery controls" (RMF 1316–1318) |
| NRR/CRA | not reported | — |
| MIT | Only "where to place controls" | L106, L587 |
| CAIS | "controlled" **interchanged with "aligned"** | L2054 vs L2074 |
| AISI | **Control as a safety paradigm** (from Greenblatt et al. 2024), defined as working even if a model is misaligned | "Control protocols aim to prevent unacceptably bad outcomes regardless of whether models are aligned." (LoO 1240–1241); "control safety case" (Agenda 1182–1183) |

**Where they collide.** Four senses:
1. a human or organisational *ability* (IASR's glossary, Shanghai, and implicitly the EU's loss-of-control formula);
2. a *countermeasure* (IASR's risk-management usage, NIST, NVIDIA, OpenAI's security controls, Meta's mechanisms);
3. a specific *paradigm* defined against alignment (AISI);
4. a *synonym* for aligned (CAIS).

Senses 3 and 4 contradict each other directly: AISI's control assumes alignment may fail, while CAIS's treats the two as one thing. IASR alone uses senses 1 and 2 in the same document.

### 2.10 safeguard / mitigation

| Model | Sense | Evidence |
|---|---|---|
| IASR | **Safeguard**: a protective measure, mostly technical ("technical safeguards"). **Mitigation**: a *process* | "A protective measure intended to prevent an AI system from causing harm." (md 2494); "Risk mitigation is the process of prioritising, evaluating, and implementing controls and countermeasures" (md 1717) |
| EU | **Mitigations** come in three kinds: safety, security, governance. Security is split off by object (unauthorised release, access, theft). **Safeguard** in the Act is mostly a *legal* protection of rights; the Omnibus adds a technical sense; the Code prefers "mitigation" | cop 1343–1345, 641–645; act 408, 415; omni 243–245 |
| FSF | Mostly interchangeable. Security mitigations (weights) vs deployment mitigations (misuse); security **gates development**, deployment **gates release** | gdm v3.1 L899–900, L918–919; g42 L125–128 |
| Anthropic | v2.2: safeguards = deployment + security standards (ASL). v3: "risk mitigations" as the umbrella "across security, deployment safeguards, and alignment domains"; "safeguards" narrows toward misuse | v2.2 L180–188; v3.4 L479–480 |
| OpenAI | **Safeguards** is the umbrella; "mitigation" **does not occur** in PF v2; the FGF says safety and security mitigations | pf-v2 L497–512; fgf L459–473 |
| NIST | **Mitigation** is one of four risk-response options (mitigate / transfer / avoid / accept). Safeguard is generic | MANAGE 1.3 (RMF 1481ff.); RMF 337 |
| NRR/CRA | CRA: mitigation = existing actions, and one of five intervention types (Mitigate / Adapt / Exploit / Continue / Terminate). The NRR speaks of response, recovery and capabilities. "Safeguard" appears only in the social-care sense | CRA L155–157, L248–257; NRR L2762 |
| MIT, CAIS | Not model terms. CAIS has "Suggestions" and safe design principles | MIT L106, L587; CAIS L1708–1720 |
| AISI | **Safeguard** in four senses, including **misuse safeguards vs control safeguards** ("harmful actions that agents take of their own accord"). The Trends glossary sense is narrow | "Technical measures implemented by AI companies to prevent users from eliciting harmful information or actions from models." (Trends 2705–2706); control-red-team 44–48 |

**Where they collide.**
- **What "safeguard" covers.** It is an *umbrella* (OpenAI, IASR), a *narrow anti-user-misuse measure* (AISI Trends, Anthropic v3), a *legal rights protection* (EU Act), or *social-care safeguarding* (NRR).
- **What kind of thing "mitigation" is.** It is a *measure* (most), a *process* (IASR), one option beside transfer, avoid and accept (NIST), or one intervention beside adapt and exploit (CRA).
- **The security / other split recurs with different boundaries.** The EU splits by object. The FSFs split by which gate the measure controls. OpenAI and AISI split by harm source (malicious user vs misaligned model; misuse safeguards vs control safeguards).

### 2.11 incident / event

| Model | Sense | Evidence |
|---|---|---|
| IASR | "Incident" undefined (~45 uses, mostly database counts). Only **incident reporting** is defined. "Harm event" appears only as a figure label | md 2362; ES 1112 |
| EU | **Serious incident** (systems): "directly or indirectly leads to" death or serious harm to health, serious and irreversible disruption of critical infrastructure, infringement of fundamental-rights obligations, or serious harm to property or the environment. For GPAI it also covers serious cybersecurity breaches, **including (self-)exfiltration** of weights. **Near miss** is defined. Bare "incident" is undefined | act 3331–3344 [checked]; guid 1169–1178; cop 1055; cop 1270–1271 |
| FSF | Undefined everywhere, in various senses. G42's "Incidence Response" concerns **non-compliance with the framework** | g42 L410–411; L84–85 |
| Anthropic | RSP undefined. FCF: an **AI Event** is a *signal* awaiting investigation, the bottom of a ladder up to Critical Safety Incident | "observable events that could signify the existence of a Serious AI Incident or Critical Safety Incident, but requires further investigation" (FCF L454–458) |
| OpenAI | PF undefined. FGF: "AI safety incident" per its incident-response plan (AIRP), **whose definitions are unpublished** | fgf L493–511 |
| NIST | RMF undefined. 600-1 quotes a definition without attribution. **It is the OECD's 2024 AI-incident definition** [checked: perset-2025-how-managing-risks L1423–1430]. NIST's rendering says "contributes to" where the OECD's says "leads to" | "event, circumstance, or series of events where the development, use, or malfunction of one or more AI systems directly or indirectly contributes to one of the following harms…" (600-1 2801–2807) |
| NRR/CRA | Undefined. "Event" is used in the definition of an acute risk; incidents motivate new risks | NRR L649–650; L245–246 |
| MIT | **Absent**; no event records | — |
| CAIS | Not a model term; historical accidents serve as analogies | — |
| AISI | **Sample ⊃ event → incident**: an event is *unsanctioned behaviour with effect outside the evaluation range*, and **no harm is required**. The same incident is also a declared AISI *security* incident (INC ID). LoO: "incident response" is after-the-fact oversight | Incident 387–390; 70, 286; LoO 4001–4004 |
| *TFAIA (upstream)* | **Critical safety incident**, four kinds. The fourth needs no harm, **and explicitly excludes behaviour inside an evaluation** | "(4) A frontier model that uses deceptive techniques against the frontier developer to subvert the controls or monitoring … outside of the context of an evaluation designed to elicit this behavior …" (sb53 L211–222) [checked] |

**Where they collide.**
- **Is harm required?** Yes for the EU, OECD/NIST and TFAIA (1)–(3). No for AISI's events and TFAIA (4). The EU extends to self-exfiltration and near misses.
- **Does behaviour during an evaluation count?** AISI's incident happened in an evaluation. TFAIA (4) excludes exactly that.
- **Other senses.** G42's incident is organisational non-compliance. Anthropic's AI Event is an unconfirmed signal.
- **Causation standard.** "directly or indirectly leads to" (EU, OECD), "contributes to" (NIST's rendering), "materially contribute" (TFAIA catastrophic risk), and, for reporting, "reasonable likelihood" of a causal link (EU Code).
- **A shared harm list.** The EU and OECD/NIST enumerate nearly the same four harm kinds: health, critical infrastructure, rights, and property or environment [checked].

### 2.12 capability

| Model | Sense | Evidence |
|---|---|---|
| IASR | Defined, conditional on circumstances; the root driver of risk | "The tasks or functions that something (e.g. a human or an AI system) can perform, and how competently it can perform them, in specific conditions." (md 2248) |
| EU | The general sense is undefined. **High-impact capabilities** are defined *relative to the frontier*, which moves | "capabilities that match or exceed the capabilities recorded in the most advanced general-purpose AI models" (act 3417–3418); "not … a fixed level" (guid 562–563) |
| FSF | Scoped to include foreseeable fine-tuning and scaffolding (GDM). "Enabling capabilities" (Meta). Shanghai ≈ IASR. **Cohere's idiosyncratic sense** names likely risks | GDM v1 L210–211; meta-2025 L1091–1092; shanghai L2112–2113 [checked]. Cohere: risks "that have a high likelihood of occurring based on the types of tasks LLMs are highly performant in … This is what we refer to as 'model capabilities.'" (L174–176) |
| Anthropic | Undefined; thresholds are stated as what the model can help someone do | — |
| OpenAI | Undefined; thresholds are "things an AI system might be able to help someone do or might be able to do on its own" | pf-v2 L168–170 |
| NIST | Undefined in the RMF and 600-1. 800-2 defines it (≈ IASR) | "The range of tasks or functions that an AI system can perform and how effectively it performs them" (800-2 1547–1548) |
| NRR/CRA | **Two opposite senses**: government **response capability** (23 generic capabilities) and an **attacker's capability** (an input to malicious likelihood) | NRR L383–393; L416–418 |
| MIT | 7.2 "AI possessing dangerous capabilities", a subdomain | L453–455 |
| CAIS | Undefined; "general capabilities" contrasted with safety | L76–77 |
| AISI | Undefined; contrasted with **propensity** ("what models can do" vs "whether models actually will"); "precursor" and "prerequisite" capabilities | misalignment-investigation 40–49; Trends 85–87 |

**Where they collide.**
- **A shared core.** IASR, Shanghai and NIST 800-2 give near-identical definitions: tasks the system can perform, and how well.
- **A moving vs fixed reference.** The EU's "high-impact" capability is relative to the frontier, so the same model can drop out of scope as the frontier moves. The FSF thresholds are absolute levels.
- **A different bearer.** The NRR's "capability" belongs to the *defender* in one sense and the *attacker* in the other. Neither is a model property.
- **Cohere's usage** would mis-merge with all of the above.
- **What is being measured.** The GDM scope (capability under foreseeable fine-tuning) and OpenAI's ("elicitation … a lower bound") measure potential. IASR's "in specific conditions" measures performance in context.

### 2.13 threshold / tier / level

| Model | Sense | Evidence |
|---|---|---|
| IASR | **Risk threshold**: a line of *acceptability* that triggers action. "Capability threshold" (used 9 times) is undefined. Developer tiers are reported, not adopted | "A quantitative or qualitative limit that distinguishes acceptable from unacceptable risks and triggers specific risk management actions when exceeded." (md 2488); Table 3.5 (md 1787–1802) |
| EU | Act and Guidelines: a **compute** threshold that triggers a legal presumption (10^25 FLOP), plus 10^23 (indicative, to count as GPAI at all) and one-third of original compute (modifier becomes provider). The Code avoids the word: **tiers** (a level of systemic risk defined in capability terms) and **trigger points** (when to run lighter evaluations) | act 5663–5665; guid 216–219, 805–809; cop 1368–1370; cop 235–238 |
| FSF | **Capability** thresholds under company names (CCL, TCL, alert threshold, CCT, levels, red and yellow lines). NVIDIA's MR 1–5 is a *product-risk category*, lowered by restricting use. Meta 2026 also has a compute test (≥10^26 FLOP) for "frontier" | gdm v3.1 L847–858; nvidia L53, L184–190; shanghai L698–757 |
| Anthropic | **Capability Threshold** (v2.2) triggers a safeguard standard (ASL). v3: "capability **or usage** threshold". ASL wording retired. FCF: tiers | v2.2 L216–219; v3.0 L171; Aug fn 59 |
| OpenAI | **Capability threshold**; High / Critical; **indicative thresholds** (evaluation cut-offs). FGF **tiers** reuse the PF's threshold wording | pf-v2 L168–175, L416–418; fgf L245–248 |
| NIST | Not defined. Organisations set tiers and "minimum thresholds" for go/no-go | 600-1 709–727 |
| NRR/CRA | The qualitative **bar for inclusion** in the register; not a risk tier | NRR L195–197 |
| MIT | Not used | — |
| CAIS | not reported | — |
| AISI | Sets none; measures against "labs' own risk thresholds". A success threshold is a measurement parameter. Task difficulty levels run from non-expert to expert | Trends 1030; cyber-horizons 74; Trends 2714–2731 |
| *TFAIA (upstream)* | A compute definition of **frontier model**: >10^26 operations | sb53 L245–246 [checked] |

**Where they collide.** Five senses:
1. a compute trigger for legal scope (EU 10^25; TFAIA and Meta 10^26);
2. a capability level that triggers safeguards (FSF, Anthropic, OpenAI);
3. a line of risk acceptability (IASR's definition; Shanghai's red lines, "absolute thresholds for unacceptable outcomes");
4. an inclusion bar (NRR);
5. a measurement parameter (AISI).

IASR's own definition is sense 3, and it reports that the frameworks use sense 2 *without* sense 3. Buhl's and Stelling's analyses say the same. "Tier" also splits: in the EU Code it is a level of *systemic risk* defined in capability terms; in OpenAI's FGF it is a *capability* threshold renamed; in NIST it is the organisation's own *risk tiering*. "Level" names a safeguard standard (ASL), a capability (CCL) and an impact score (NRR).

### 2.14 developer / provider / deployer

| Model | Sense | Evidence |
|---|---|---|
| IASR | **Developer** defined broadly, including adapting. Deployer used but undefined. **Provider** means compute, cloud or hosting provider | "Any organisation that designs, builds, or adapts AI models or systems." (md 2206); md 1836 |
| EU | Legal **roles**. **Provider** = develops, or has developed, *and places on the market* under its own name. **Deployer** = uses an AI *system* under its authority; there is no model-level deployer. **No "developer" role.** Also downstream provider and downstream modifier | act 3144–3146, 3148–3149, 3432–3434; guid 780–782 |
| FSF | Mostly "we". Microsoft: "external system developers and deployers". xAI 2026 uses EU vocabulary. Stelling coins "Providers" for the companies | microsoft-2026 L142–144; xai-2026 L370; stelling L221 |
| Anthropic | "AI developer" and "frontier developer", undefined. "Provider" only in the EU legal sense (Anthropic Ireland) | FCF L640 |
| OpenAI | "frontier AI model developer", undefined. "Provider" is EU legal only. "Deployer" not used | pf-v2 L595; fgf L704–705 |
| NIST | **AI actors defined by task** (design, development, deployment, TEVV, …), so one organisation holds several roles. Developer and deployer are not defined; providers appear only among third-party entities | RMF 203–206; Appendix A 1584–1712 |
| NRR/CRA | Absent ("provider" only as service provider) | — |
| MIT | No role taxonomy; the Entity code is just "Human" | — |
| CAIS | "developer" used, undefined | L73 |
| AISI | Undefined. LoO's supply chain: "original model developer, scaffolding developer or fine-tuner, API deployer, end user" | LoO 2767–2768 |
| *TFAIA (upstream)* | "frontier developer" | via xai-2025-faif L32–33 |

**Where they collide.**
- **Only the EU defines roles legally, and it has no "developer".** Its provider role turns on placing on the market. So a developer that only uses a model internally, and not for third-party services, is outside the provider role (guid 720–722).
- **"Provider" has three referents:** the EU legal role, which Anthropic and OpenAI also use for their EU entities; infrastructure vendors (IASR); and the frontier companies generically (Stelling, Zhu).
- **"Deployer" differs in what it attaches to.** The EU's deployer uses a *system*. AISI's "API deployer" serves a *model*.
- **NIST cannot be mapped onto either** without splitting organisations into task-roles.

### 2.15 alignment / misalignment

| Model | Sense | Evidence |
|---|---|---|
| IASR | A **propensity** of a model, relative to intentions, values or norms, whose referent varies by context | "The propensity of an AI model or system to use its capabilities in line with human intentions, values, or norms. Depending on the context, this can refer to the intentions and values of various entities…" (md 2222); misalignment also "goals that conflict" (md 1240) |
| EU | **Two senses inside one model.** The Act: a *training activity*. The Code: misalignment as a model *propensity* | "model adaptations, including alignment and fine-tuning" (act 9125); "misalignment with human intent" / "misalignment with human values (e.g. disregard for fundamental rights)" (cop 1479–1480) |
| FSF | GDM: "deceptive alignment", scheming. Amazon: "alignment training" toward responsible-AI dimensions; a "model persona". xAI: "incidental alignment". Shanghai: misalignment as a tendency (≈ IASR 2025) | gdm v2 L324; amazon-2025 L152–153; amazon-2026 L276–277; xai-2025-rmf L228–229; shanghai L2120–2122 |
| Anthropic | Roadmap: behaving in line with the Constitution. Aug: misalignment is **a latent property of a specific computation**, judged by a reasonable person and the constitution | Aug L846–850; roadmap L24–26 |
| OpenAI | **Claims** in a safeguards argument: Value Alignment, Instruction Alignment | pf-v2 L883–887 |
| NIST | Not used in the RMF. 600-1 has only an organisational sense | 600-1 2586, 2605 |
| NRR/CRA | Everyday sense only | — |
| MIT | 7.1: acting in conflict with ethical standards or human goals or values, "especially the goals of designers or users" | L449–452 |
| CAIS | Undefined; interchanged with "controlled"; deceptive alignment as "playing along" | L2054/L2074; L2144 |
| AISI | Five senses. LoO: a **condition** of divergence from what developers or users intended. Its operational core is **honesty** | "A condition in which a model's actual goals, values, or behavioural dispositions diverge from those intended by its developers or users." (LoO 4073–4075) |

**Where they collide.**
- **What kind of thing it is.** A disposition of a model (IASR, EU Code, Shanghai, AISI), an activity done to a model (EU Act, Amazon), a property of one computation (Anthropic), a claim to be evidenced (OpenAI), or a synonym for control (CAIS).
- **Aligned with what.** The developer's intention (Gemini report, AISI), human values including fundamental rights (EU Code), the company's constitution (Anthropic), user instructions (OpenAI's Instruction Alignment), or responsible-AI dimensions (Amazon).
- **One model uses two senses.** The EU uses the activity sense in the Act and the property sense in the Code.
- **NIST's organisational sense is unrelated.**

### 2.16 vulnerability

| Model | Sense | Evidence |
|---|---|---|
| IASR | A **system weakness** exploitable by a malicious actor | "A weakness or flaw in a system that could be exploited by a malicious actor to cause harm." (md 2546) |
| EU | Both senses, **in one list** of affordances: vulnerability to guardrail removal and to exfiltration (system weakness); "vulnerability of the affected environment" (exposure) | cop 1492–1514 |
| NRR/CRA | Four senses: **vulnerable people** (risk-relative, "not a fixed characteristic"); **target vulnerability** as one input to malicious likelihood; the CRA's "Example vulnerabilities" field (exposed groups and sectors); a CRA **network node type**, distinct from risks | NRR L881–885; NRR L416–418; CRA L905–920; CRA L4421–4424, L4490–4492 |
| MIT | 2.2 "AI system security vulnerabilities and attacks" (system weakness) | Table 2 |
| FSF, Anthropic, OpenAI, NIST, CAIS, AISI | not reported as a term | — |

**Where they collide.** The *system-weakness* sense (IASR, MIT, the EU guardrail and exfiltration items, cyber usage generally) sits on the **cause** side. The *exposure* sense (NRR vulnerable people, CRA vulnerabilities, EU "affected environment") sits on the **harm** side. The NRR's "target vulnerability" lies in between: the attacked party's susceptibility, as an input to likelihood. The CRA makes vulnerabilities first-class network nodes; no frontier-AI model has a place for them.

### 2.17–2.28 Secondary terms

| Term | Senses, by model | Where they collide |
|---|---|---|
| **2.17 propensity** | IASR: used, undefined; "Harmful propensity" is the second loss-of-control factor (md 1252). EU Code: "inclinations or tendencies of a model to exhibit some behaviours or patterns" (cop 1477–1478), 10 listed, including hallucination, discriminatory bias, lack of reliability and lawlessness. AISI LoO: "A model's behavioural tendency or disposition towards certain kinds of behaviours." (LoO 4076–4077). FSF: xAI's "concerning propensities" bucket; Meta 2026 propensity criteria (MASK) | The EU's list includes non-agentic failure tendencies (hallucination, unreliability). IASR and AISI use the word mainly for dispositions to misbehave |
| **2.18 resilience** | IASR: a **property of society**, "The ability of societal systems to absorb, adapt to, and recover from shocks and harms" (md 2476), with "resist" added in the body. NIST: a **property of the AI system**, withstanding "unexpected adverse events" and degrading "safely and gracefully" (RMF 732–747). AISI: **Societal Resilience is a risk domain**, "Risks that will emerge as frontier AI systems are deployed widely…" (Agenda 175–176). NRR: the name of the national preparedness system (Resilience Action Plan, NRR L881–885) | Four referents: society, system, a risk domain, a government programme. AISI's domain covers what IASR calls *systemic risk*, while IASR's "societal resilience" is a *mitigation*. The same word sits on opposite sides of the chain |
| **2.19 emerging / emergent** | IASR: "emerging risks" are "risks that arise at the frontier of AI capabilities" (md 362), the 2026 scope term. NIST: "emergent risks" appear over time and must be tracked (RMF 341–342; MEASURE 3.1). EU Code: open-ended testing for "emergent properties" (cop 418–424). Meta 2026: "emerging" outcomes = exploratory (L1398–1455) | Frontier-located (IASR) vs time-located (NIST) vs property-of-the-model (EU) vs not-yet-graded (Meta) |
| **2.20 marginal risk / uplift / baseline** | IASR: **marginal risk** is increase "beyond that already posed by existing models or other technologies" (md 2394). Anthropic: **marginal** = over *other developers'* systems, vs **absolute** (Feb L260–268); uplift baseline "2023-level online resources" (v2.2 L919–921). OpenAI: net new vs "available as of 2021" (pf-v2 L145–162); marginal-risk clause keyed to competitors (L594–604). FSF: baselines include internet search, other public models, "a baseline without generative AI", open-weights models, the company's own previous model; Meta's "uniquely enable" → "substantially contribute". AISI: uplift over "internet … only" (Trends 2674–2676). NIST 800-1: marginal "relative to that baseline" of available tools (nist-2025-managing 508–511). EU: mitigations can't escape classification; a "safe reference model" grades safety *relatively* (cop 1548–1599). *TFAIA*: excludes information "otherwise publicly accessible" (sb53 L201–205) | Four different baselines: other AI models (IASR, Anthropic marginal, GDM acceptance), the internet (AISI, Amazon 2025), a dated snapshot (OpenAI 2021, Anthropic 2023), or no generative AI (GDM). The AI-model baselines move with the field, which Stelling notes: "if one Provider lowers standards, the baseline … also lowers" (stelling L1714–1715). Anthropic's "absolute" is itself a counterfactual, not an unconditioned quantity |
| **2.21 threat / threat model** | IASR: threat modelling is "A process to identify vulnerabilities in an AI model or system and anticipate how it could be exploited, misused, or otherwise cause harm." (md 2532) [checked]. EU Code: renames to **risk modelling** to avoid the cybersecurity sense (cop 1347–1350). FSF: Meta's threat scenarios (actors achieving an outcome; revised 2026 to "real-world events"); Magic's "proposed mechanisms". Anthropic: a threat model is "the specific ways that models might pose threats" (v3.0 L80), and the four threat models are the RSP's categories. OpenAI: a threat model "identifies the risks of severe harm and sets thresholds" (pf-v2 L17–19). NIST 800-1: a **threat profile** of task, actor, way and mechanism (nist-2025-managing 1099–1102). AISI: scenario maps, *and* components of one capability ("four threat models: obtaining weights, …", Trends 1728–1729). NRR: a **threat** is a malicious risk | A threat model is a process (IASR), a scenario pathway (Meta, AISI a), a category of risk (Anthropic), a device that sets thresholds (OpenAI), or a sub-capability (AISI b). The NRR's "threat" is defined by intent, the mirror of its "hazard" |
| **2.22 risk source / risk factor** | IASR: **risk factors** are "Properties or conditions that can increase the likelihood or severity of harm" (md 2482). EU Code: **systemic risk source**, "a factor which alone or in combination with other factors might give rise to systemic risk" (cop 1363–1364); "risk factor" not used. CAIS: **risk sources** are the four cause categories. MIT: "sources of risk at a high level of abstraction" is an *exclusion* criterion. NIST 600-1: "source of risk" is one of four dimensions. AISI: "contributing factors" (Incident 1038). NRR: chronic risks as "drivers" | Increasers of likelihood or severity (IASR) vs originators of risk (EU, CAIS) vs something MIT deliberately excluded. MIT's Entity/Intent/Timing is its substitute |
| **2.23 misuse / malicious use** | IASR: requires intent, "Using something, such as an AI system, to intentionally cause harm." (md 2388), with misuse and malicious use interchangeable. GDM: threat actors using capabilities of deployed *or exfiltrated* models (v2 L50–51). OpenAI: the "malicious user" as one of two harm sources. **NIST 600-1: "abuse, misuse, and unsafe repurposing by humans (adversarial or not)"** (600-1 156–171). CAIS: "Malicious actors using AIs to cause large-scale devastation" (L238). MIT: Domain 4, and Human × Intentional. AISI: Cyber Misuse, Criminal Misuse | NIST's misuse includes *non-adversarial* repurposing. IASR, CAIS and OpenAI require intent. GDM extends misuse to stolen models, which the EU files under *security* |
| **2.24 oversight** | EU Act: human oversight is a *designed feature* of high-risk systems, to monitor, interpret, override and interrupt ("'stop' button", act 4083–4131). EU Code: an *affordance* level, and evading oversight is a capability (cop 1501, 1463). AISI LoO: the *practices* of developers and deployers, namely auditing, monitoring and incident response (LoO 3991–3994), "weaker than scalable oversight". OpenAI: "Reliable and Robust System Oversight" as a safeguards claim. *TFAIA*: "no meaningful human oversight" as a condition of catastrophic conduct (sb53 L195) | A system design property vs an organisational practice vs an adjustable affordance vs a legal trigger (its absence). AISI's is explicitly not "scalable oversight" (a training-signal problem) |
| **2.25 safety case** | GDM: "an assessable argument showing how severe risks associated with a model's CCLs have been reduced to an appropriate level" (v2 L216–217). AISI: "structured arguments for the safety of a system deployed in a specified environment" (Agenda 972–973), used *to find research gaps*. OpenAI's later posts: "…explaining why a model or system's risks are adequately managed for a specified activity" (third-party-assessments L132–147); the PF itself doesn't use the term. Anthropic: v2.2 "inspired by safety case methodologies"; v3 Risk Reports defined *against* it (karnofsky L597–599). EU: the Model Report's justification of acceptability, with "conditions under which the justification … would no longer hold" (cop 717–718), is a functional analogue (my reading) | An argument *to a standard* (GDM, OpenAI, AISI) vs a characterisation *whatever the level* (Anthropic). The object differs: a model's CCL, a system in an environment, an activity |
| **2.26 frontier / general-purpose** | *UK DSIT 2023*: "AI models that can perform a wide variety of tasks and match or exceed the capabilities present in today's most advanced models." (dsit-2023-capabilities L1305–1306) [checked]. EU: GPAI model (act 3411–3415) and high-impact "match or exceed … most advanced" (act 3417–3418). IASR: frontier is "particularly capable general-purpose AI" (md 2336). FSF: GDM v3.1 reuses the EU's GPAI language; Meta 2025 relative, 2026 capability *or* ≥10^26 FLOP; NVIDIA relative. *TFAIA*: >10^26 operations. NIST 600-1: generative foundation models (EO 14110). CRA: "highly capable models that can perform a wide range of tasks" (CRA L1343–1356). AISI: "the limit of what's possible given current technology" (Agenda 193–195) | Relative definitions (DSIT → EU high-impact, Meta 2025, NVIDIA) move with the frontier. Compute definitions fix a number, and they don't agree: 10^25 (EU presumption) vs 10^26 (TFAIA, Meta 2026). NIST's scope is *generative*, not capability-relative |
| **2.27 deployment** | EU: **placing on the market** is the trigger. Internal use counts only if "essential for providing a product or service to third parties" (guid 720–722). *TFAIA*: to deploy is to make available "to a third party" (sb53 L224) [checked]. MIT: "when a product is being used by end users rather than just by developers" (L1464–1466). FSF: deployment types, including internal (GDM v3.1 L904–916; Meta 2026 L1634–1647). Anthropic: the RSP covers internal models; the FCF mainly externally deployed ones. IASR: deployment environment = use case plus context (md 2306) | Whether internal use is in scope: yes (Anthropic RSP, GDM and Meta as a deployment type); only if serving third parties (EU); no (TFAIA, MIT). IASR's deployment *environment* is a risk factor, not a lifecycle event |
| **2.28 acceptable risk / risk tolerance** | IASR: risk tolerance, "The level of risk that an individual or organisation is willing to take on." (md 2490). NIST: tolerance adapted from ISO Guide 73, "not prescribe[d]" (RMF 398–401). EU: "acceptable" is undefined; its content is the provider's justified criteria plus the safety margin (cop 1330–1332, 573–580). FSF: "deemed acceptable if…" by judgment (gdm v3.0 L256–280); METR: "no consensus … 'acceptable level'" (metr L104–105). Stelling: tolerance "Ideally expressed quantitatively as probability × severity per unit time" (L1920–1922) | Everyone defers the *value*: to the organisation (IASR, NIST, EU), to governance judgment (FSF), or to an ideal nobody meets (Stelling: no provider expresses one that way). Only the NRR's scale implies one, and it does so implicitly, through what gets planned for |

---

## 3. How the models relate

### 3.1 Lineage and correlation

The derivations below are the ones the sections name, plus the ones I confirmed in the extractions (marked). An arrow means "takes from": a definition, a list, a structure or a template.

```
 Yampolskiy 2016 ──────────────► MIT causal taxonomy (chosen as "best fit", then reworked)
        └──────────────────────► CAIS's four sources (cited as the four-way split)
 CAIS overview ─────────────────► one of MIT's 74 frameworks; cited by IASR 2026 in the loss-of-control section [checked]
 MIT repository ────────────────► cited by IASR 2026 in Ch.3 [checked]

 UK DSIT 2023 "frontier AI" ("match or exceed … today's most advanced models") [checked]
        └─► Seoul commitments (Buhl) ─► EU "high-impact capabilities" wording; Meta 2025; NVIDIA
 G7 Hiroshima Code (2023), Action 1 risk list [checked]
        └─► AI Act recital 110 (near verbatim) ─► Code Appendix 1.4's four specified risks
                                                 ─► FCF / FGF / xAI 2026 (as statutory compliance); Microsoft and
                                                    Amazon 2026 name the same four (my reading: shaped by it)
 EU Code loss-of-control formula (Jul 2025) [checked]
        └─► xAI 2026 (verbatim), OpenAI FGF (embedded), Meta/Amazon/Microsoft 2026 and GDM blog (paraphrase);
            quoted as the Code's by METR and Stix et al.
 California TFAIA / SB 53 (>50 people or $1B; three conducts; critical safety incidents) [checked]
        └─► xAI 2025 FAIF (verbatim) ─► Anthropic FCF and OpenAI FGF "systemic risk" (relabelled)
 OECD 2024 AI-incident definition [checked: perset L1423–1430]
        └─► NIST 600-1 (unattributed, "leads to" → "contributes to"); near-identical harm list in AI Act Art. 3(49)

 IASR interim (2024) three categories ──► NIST 600-1 footnote 5 grouping [checked]
 IASR 2025 glossary ────────────────────► Shanghai AI Lab glossary ("primarily based on" it) [checked: shanghai L2085, L295]
 NIST AI RMF, ISO/IEC 23894, OECD, SRA ─► IASR risk-management structure
 NIST AI RMF, ISO 42001 ────────────────► Microsoft, xAI, Anthropic FCF, OpenAI FGF (as cited)
 ISO 31000 / Guide 73 / OMB A-130 ──────► NIST risk, tolerance, residual risk
 PHIA yardstick (UK intelligence) ──────► NRR likelihood labels and AISI LoO likelihoods

 METR "responsible scaling" (2023) ─► Anthropic RSP ─► GDM v1, OpenAI PF (via Anthropic's reports), the FSF genre
 Meta 2025 criteria ─► OpenAI PF's five admission criteria
 Seoul commitments (May 2024) ─► the obligation to publish FSFs; Buhl's 13 components
 Greenblatt et al. 2024 (AI control) ─► AISI's control paradigm
 Leveson's STPA ─► named by IASR 2025 and the AISI Agenda (method), not used as vocabulary
```

**What the lineage means for reading agreement:**
- **The "four categories" (CBRN, cyber, loss of control, manipulation)** that now appear in the EU Code, both companies' compliance frameworks, xAI, Microsoft and Amazon trace to one list: G7 → recital 110 → Code. Six documents naming the same four risks are largely one decision, echoed. For three of them the derivation is explicit; for Microsoft and Amazon it is my inference.
- **The TFAIA threshold** in four documents is one legislative number.
- **MIT's and CAIS's causal axes** are cousins, not independent findings.
- **Shanghai AI Lab's glossary agreeing with IASR** is a copy, not a second opinion.
- **The UK's two sources share the PHIA yardstick and a government, not a method.** The NRR is a national-risk method and LoO a technical-analysis method, and LoO says it "is not an all-source intelligence assessment" (LoO 502–503).
- **Shared people across AISI's documents** (the section's §9) and AI assistance in LoO's method are further correlations to mark.
- **Correlated upstreams among the frameworks** (Stelling's point): uplift baselines defined as "other publicly available models" make each company's grade depend on the others' releases.

### 3.2 What each covers and leaves out

Legend:
- ● a named risk or category in the model;
- ○ appears as a sub-item, listed source, example, research category, or in a companion document;
- ✕ explicitly excluded or dropped;
- blank = not reported by the section.

For AI-specific scope, the NRR row is omitted: AI is not an NRR risk (§1.4).

| Model | CBRN | Cyber | Loss of control / misalignment | Manipulation / influence | AI R&D automation | Bias / discrimination | Privacy | Labour / economy | Power concentration | Environment | Everyday reliability |
|---|---|---|---|---|---|---|---|---|---|---|---|
| IASR 2026 | ● | ● | ● | ● | | ✕ (2025 only) | ✕ (2025 only) | ● | ✕ (2025 only) | ✕ (2025 only) | ● |
| EU Code | ● | ● | ● | ● | ○ (source) | ○ (propensity, type) | ○ (type) | | ○ (type) | ○ (type) | ○ (propensity) |
| FSF genre | ● | ● | ○ (some; often "exploratory") | ○ (GDM v3+, Amazon/Microsoft/xAI 2026) | ● | ✕ | ✕ | ✕ | ✕ | ✕¹ | ✕¹ |
| Anthropic RSP v3 [FCF] | ● (chem/bio only) | ✕ [● FCF] | ● | ✕ [● FCF] | ● | ✕ | ✕ | ✕ | ✕ | ✕ | ✕ |
| OpenAI PF v2 [FGF] | ● (bio/chem; nuc/rad → Research) | ● | ○ (Research Categories) [● FGF] | ✕ [○ FGF, exploratory] | ● | ✕ | ✕ | ✕ | ✕ | ✕ | ✕ |
| NIST 600-1 | ● | ● (Information Security) | ✕ (speculative; term absent) | ○ (Information Integrity) | | ● | ● | | | ● | ● (Confabulation) |
| CRA (AI chronic risk) | ○ | ○ | ✕ (absent) | ○ (disinformation) | | ○ | ○ | ○ (job displacement) | ○ (tech-company dominance) | | |
| MIT | ● (4.2) | ● (4.2, 2.2) | ● (7.1, 7.2) | ● (4.1, 4.3, 5.2) | ○ (in 7.2) | ● (1.1, 1.3) | ● (2.1) | ● (6.2, 6.3) | ● (6.1) | ● (6.6) | ● (7.3) |
| CAIS | ● (bioterrorism) | ○ (cyberwarfare) | ● (rogue AIs) | ● (persuasive AIs) | | ✕² | ✕² | ○ (automated economy) | ● | ✕² | ○ (organisational accidents) |
| AISI Agenda | ● (Dual-use Science) | ● | ● (Autonomous Systems) | ● (Human Influence) | ○ (Trends: simplified AI R&D) | ✕ (LoO) | | ✕ (LoO) | | ✕ (Trends) | |

¹ By the genre's general exclusion of whatever is "not severe or catastrophic and capability-driven".
² CAIS excludes non-catastrophic harms except as precursors.

Unique coverage worth knowing:
- MIT alone has **AI welfare and rights** (7.5) and **multi-agent risks** (7.6).
- IASR and MIT have **human autonomy** (IASR 2026; MIT 5.2).
- AISI and IASR have **criminal misuse** as its own category.
- The CRA alone models **interactions** as a network; CAIS narrates them (§6); MIT explicitly gives them up.
- The NRR alone has **recovery** and **vulnerable people** as per-risk fields.

### 3.3 Where the models are incompatible, not just different

1. **The unit of analysis.** A model with all its versions (EU Code), a model and deployment (OpenAI), the company's activities as a whole (Anthropic Risk Reports), a system in its context of use (NIST, the EU's high-risk track, NVIDIA), a scenario instance (NRR), a trend (CRA, AISI Trends), a source's category (MIT), a cause category (CAIS), an oversight surface (AISI LoO). The same real-world risk has no common key across these.
2. **Evidence posture.** NIST 600-1 excludes speculative risks by rule. The EU Code applies precaution and extrapolation. The FSFs, Anthropic and OpenAI treat "cannot rule out" as reached. IASR puts both horns in the evidence dilemma. A compiled risk that is "speculative" is *out* of one model and *mandatory* in another.
3. **The admission criteria exclude what other models centre.** OpenAI's "instantaneous or irremediable" criterion, and Meta's "Instantaneous or irremediable", exclude by construction the slow, remediable, accumulating harms that are the CRA's entire subject and IASR's systemic category.
4. **Systemic risk and the capability link** (§2.7): IASR and the EU define it in opposite relation to capability.
5. **Severity bars** (§2.6): >50 deaths, >100, thousands, >1,000, existential, all under "catastrophic", "severe" or "systemic".
6. **Roles** (§2.14): EU legal roles with no developer; NIST task-roles; TFAIA's "frontier developer"; IASR's developer who "adapts".
7. **Incidents** (§2.11): whether harm is required, and whether behaviour during an evaluation counts, are answered opposite ways (AISI vs TFAIA (4)).
8. **Benefits.** NIST counts positive impacts inside "risk". Several FSFs, OpenAI's marginal clause and Anthropic's risk-benefit determination put benefits in the decision. IASR excludes benefits from assessment. The CRA lists "benefits of acting" (co-benefits of mitigation). MIT and the NRR have none.
9. **Time.** NRR windows are 2 and 5 years. FSF safety buffers are measured in compute multiples and months ("6x in effective compute or 3 months"). AISI LoO's regime is "before full automation of AI R&D". The CRA's are "short-term" and "longer-term". IASR's scenarios run "by 2030". There is no shared horizon.

### 3.4 Against Joseph's chain: the sections' closing notes, summarised

*Chain: sources and causes → preventions and controls → risk events × impact radius → mitigations and recovery → policies and decision-making.*

| Model | Where it lines up | Where it cuts across |
|---|---|---|
| IASR | Causes ≈ capability (+ loss-of-control factors); 2026 resilience splits prevention (Resist) from after-the-shock (Absorb, Recover, Adapt) | No event layer (incidents are evidence *for* risks); thin impact radius; policies deliberately replaced by "Challenges for policymakers". Best read as "a capability-indexed risk register with an evidence-maturity overlay" |
| EU | Sources ≈ App. 1.3; preventions ≈ safety, security and governance mitigations; events ≈ serious incidents and near misses; radius ≈ types plus nature (velocity, cascading, irreversibility); policy ≈ the acceptance decision | A process and accountability model with no causal edges. Its central quantity is acceptability against provider-set criteria. The model itself is treated as a possible adversary of mitigations and evaluation |
| FSF | Decision node, with a gate back to preventions. Meta's outcome → scenario → enabling capability, Shanghai's E-T-C and bottleneck reasoning run the chain *backwards* | Events and radius compressed into threshold wording; recovery nearly absent; threat models withheld |
| Anthropic / OpenAI | Capability as cause-enabler; safeguards as prevention; Anthropic's P · H · U is the chain's middle in miniature | Radius collapsed to one deaths-or-dollars bar; recovery nearly absent (OpenAI's irremediability criterion excludes recoverable harms); "policy" points at the developer's own gates |
| NIST | Downstream half: MANAGE ≈ prevention, mitigation and recovery; GOVERN ≈ policy; an explicit radius (individuals → planet) | No causes tree or event taxonomy; users produce those in MAP. 600-1's risks mix outcome, object and source |
| NRR/CRA | The RWCS is an ideated risk event with likelihood; seven impact dimensions plus vulnerable people make a radius; consequences funnel into capabilities, which is mitigation and recovery | Deliberately cause-agnostic at the event. Causes live in the CRA's signed network with no probabilities. The UK splits the chain at the event and gives the halves different methods |
| MIT / CAIS | MIT: sources (Causal) and a mixed harm and mechanism catalogue (Domain), as parallel code-sheets. CAIS: narrates source → source → event chains | Neither has a place for *links*. Both simplified the causal axis the same way, from Yampolskiy |
| AISI | LoO models whether preventions can *see*, with a before / during / after split close to a bow-tie; won't ∨ can't is a statement about preventions | Carved by team and instrument, not causal position; "severity" grades oversight, not harm; the Incident puts the *evaluator* into the causal chain |

Across all eight notes, one thing recurs: **no model holds the links.** Every model either lacks relations between stages (MIT, the EU taxonomy, NIST, IASR) or holds them in narrative, withheld threat models, or unpublished networks (CAIS, FSFs, CRA). Joseph's chain is itself a synthesis that none of the sources contains.

---

## 4. My reading: what the eight suggest about an intermediate step

*This section is mine, not the sources'. It is offered as input to Joseph's decision, not as a recommendation to adopt anything. The full compilation remains the goal in everything below.*

**The main thing that seeing them side by side shows.** The eight are not competing accounts of one object. They are accounts of different objects: a landscape, a gate, a management process, a scenario set, a trend network, a literature, a research programme. A compilation that merges their *claims* before typing their *objects* would reproduce MIT's cost one level up: rows that are events, causes, conditions and capabilities under one label. MIT's own cost list shows what that looks like at scale: no links, a conflated "Other", a lost observed/anticipated distinction. My guess is that whatever comes first, every compiled item needs to carry *what kind of thing its source is talking about*, and *which source-model it came from*, before anything else.

**Three layers look compilable now, without first deciding the schema.** They record facts *about* the models rather than claims about the world, so they don't force a schema choice. Any later schema would need all three.

1. **A term crosswalk:** term × source × sense × verbatim anchor. §2 is a partial seed: about 28 terms, eleven models, many senses already separated. It records collisions without resolving them. It is also the input the coordinator's vocabulary layer needs.
2. **A source-model registry:** one record per model, along the dimensions of §1. These are object modelled, unit, grading scheme, uncertainty posture, evidence posture, force, audience, exclusions, and version and date. The eight sections already are this, in prose. Versioning belongs in it from the start, because these models move fast (§1.4) and often silently (Zhu).
3. **A lineage graph among sources:** copies, citations, templates, shared people. Without it, a compilation counts the EU Code's loss-of-control formula once per copy (nine, in this set) and TFAIA's threshold four times, and reads the echo as consensus (§3.1).

**If Joseph wants to test a schema rather than defer it: one vertical slice.** Carry one risk through all eleven models at full fidelity. There are two candidates, with opposite virtues:
- **CBRN** is the one risk every model names. It tests whether *convergent* content compiles cleanly. It would still surface the severity-bar mismatch (§2.6), the uplift-baseline mismatch (2021 / 2023 / internet / other models, §2.20), and the chem/bio vs radiological/nuclear splits.
- **Loss of control** is the most collided term (§2.8). It is a scenario, risk, ability, conduct or domain depending on the source, and absent from NIST, the NRR, the CRA, the RSP and the PF. It tests whether a schema can hold one concept that different sources place at different points in a chain.

My guess, and it is only a guess, is that loss of control is the more informative slice: a schema that holds it will likely hold CBRN, but not the reverse.

**What the eight suggest the full compilation will need, whichever step comes first.** Each is something no single model does alone.
- **Keep measured, graded and believed apart.** Only the NRR grades on calibrated scales. AISI and NIST 800-2 are careful about what an evaluation measures. IASR tags evidence maturity. The FSF thresholds are judgments by named people. These are different epistemic kinds, and the sources themselves mark them unevenly.
- **An event layer that doesn't assume harm.** Only the NRR (RWCS), the EU (serious incident, near miss), AISI (sample / event / incident) and TFAIA (critical safety incident) model events, and they disagree about whether harm is required (§2.11). AISI's "effect" vs "harm" distinction is the finest-grained of them.
- **An impact radius.** Only the NRR (seven dimensions plus vulnerable people), NIST (individuals → planet) and the EU (types plus nature: velocity, cascading, irreversibility, asymmetry) have one. Every frontier framework collapses it to a single deaths-or-dollars bar.
- **Links.** No model holds them as structure (§3.4). The CRA's signed network is the only structural precedent, and it is unpublished beyond an excerpt.

**On "hazard" in particular.** Joseph's example turns out to be a clean case. The word is almost unclaimed in frontier-AI usage: load-bearing only in the NRR and NVIDIA, and not a term at all in NIST, Anthropic, OpenAI or AISI. That leaves it free to define. But its three established senses from outside AI are mutually incompatible:
- an event or activity with potential to harm (SRA / IASR);
- a system state that leads to loss under worst-case conditions (STPA);
- a non-malicious cause, as opposed to a threat (UK civil contingencies).

Any definition picks one, and the crosswalk should record the other two as collisions rather than as synonyms.

---

## Appendix: where I checked the underlying text

Each item is either something a section left unclear, something that looked like a disagreement, or a lineage claim that needed confirming. Everything else in this overview rests on the sections as written.

| What | Finding | Where |
|---|---|---|
| IASR's claim that the EU AI Act defines systemic risk as risks from models that pose "risks of large-scale harm" | **The phrase is not in the Act, Code or Guidelines extractions.** It is in Anthropic's FCF ("foreseeable and material risks of large-scale harm") and in IASR itself. The Act's definition is the one quoted in §2.7. A PDF-level check would settle it finally, since extractions can drop text, but a whole-file search for "large-scale" and "large scale" in the Act found only unrelated uses | md 487; eu-2024-ai-act (whole-file grep); eu-cop-2025-safety-security; ec-2025-gpai-guidelines; anthropic-2026-frontier-compliance-framework-v2 L118 |
| Whether Shanghai's glossary agrees with IASR independently or by copying | Copying: the framework "builds upon the International AI Safety Report (January 2025)", and its terminology is "primarily based on" it. Hazard, risk, loss of control, misalignment and capabilities match IASR 2025 or 2026 wording | shanghaiailab-2025-frontier L295, L2085, L2100–2135; bengio-2025-international L10969–11380 |
| Origin of NIST 600-1's unattributed AI-incident definition | The OECD (2024) definition, attributed in the OECD/Hiroshima-reporting paper. NIST renders "leads to" as "contributes to" | nationalinstitute…-2024-artificial L2801–2807; perset-2025-how-managing-risks L1423–1430 |
| EU vs OECD incident harm lists | Near-identical four harm kinds; the EU adds "serious" and "irreversible" qualifiers | eu-2024-ai-act L3329–3344 |
| Origin and spread of "reliably direct, modify, or shut down" | EU Code (Jul 2025) is the earliest in the set. xAI 2026, OpenAI FGF, Meta/Amazon 2026 and the GDM blog (Sep 2025) follow. METR and Stix et al. quote it as the Code's. Anthropic's FCF does not use it | eu-cop-2025-safety-security L1530; stix-2025-loss L381, L747, L834; metr-2025-common-elements L1041; gdm-2026-strengthening-fsf-blog (dated 22 Sep 2025) L46; grep over all extractions |
| TFAIA's definitions, which three sections cite second-hand | Catastrophic risk (>50 people or >$1B, single incident, three conducts including "Evading the control of its frontier developer or user"); critical safety incident (four kinds, the fourth excluding evaluation contexts); frontier model (>10^26); deploy (to a third party) | california-2025-sb53 L187–224, L245–246 |
| G7 → recital 110 | The G7 Action 1 list carries the barriers-to-entry, physical-systems control, self-replication and "entire city" chain-reaction items that recital 110 reproduces | g7-2023-hiroshima-code-of-conduct L95–121 |
| NIST 600-1's three-way grouping and IASR | "derived in part from the UK's International Scientific Report on the Safety of Advanced AI" | nationalinstitute…-2024-artificial L203–213 |
| The NRR's PHIA mapping (the section's table looked odd) | As printed: PHIA "Unlikely (25–35%)" and every word above it map to NRR score 5; "Highly unlikely" to 4; "Remote chance" to 3; scores 1–2 have no PHIA word. The NRR also prints "Highly unlikely" as 5–25%, where the official yardstick (gov.uk 2025; the figure in AISI's *Loss of Oversight*) has ≈10–20%: a restatement of an upstream scale with altered values (noted 2026-10-06) | cabinetoffice-2026-nrr L400–427 |
| AISI LoO's PHIA scale | The standard seven-band yardstick | aisi-2026-loss-oversight L502–515 |
| Provenance of "match or exceed … most advanced models" | UK DSIT Oct 2023 discussion paper glossary | dsit-2023-capabilities L1305–1306 |
| STPA's sense of "hazard" | "A system state or set of conditions that, together with a particular set of worst-case environmental conditions, will lead to a loss" (Leveson, via Barrett) | barrett-2025-stampstpa L1075–1076 |
| IASR 2026's citations of MIT and CAIS | Both cited: MIT in Ch.3, CAIS in the loss-of-control section | md 1570, 1668 (MIT); md 1244, 1248, 1315 (CAIS) |
| IASR's threat-modelling definition, which its section cited only by line | Quoted in §2.21 | md 2532 |

I found no place where two sections contradicted each other on a matter of fact. The apparent contradictions were differences in object or sense, which is what §2 records. The one factual discrepancy I found was IASR's quotation of the EU Act, above.
