# The EU's model of AI risk: the AI Act and the GPAI Code of Practice (Safety and Security chapter)

*Written by the intl-eu atlas agent, 2026-09-28, for Joseph's side-by-side comparison of source models. It describes the instruments on their own terms. Where I interpret rather than report, I say so.*

*Line references are to the `pdftotext -layout` extractions:*
- `act` = eu-2024-ai-act (Regulation (EU) 2024/1689);
- `cop` = eu-cop-2025-safety-security (Code of Practice, Safety and Security chapter, final July 2025);
- `guid` = ec-2025-gpai-guidelines (the Commission's interpretation);
- `omni` = eu-2026-digital-omnibus-ai (Regulation (EU) 2026/1744, amending the Act).

*The files are at `/private/tmp/claude-505/-Users-josephwecker-v2-src-aisi-eoi/f462f375-61ba-4d02-b4e6-ae440173656f/scratchpad/src-text/<key>.txt`. The atlas entries (`influx/source-atlas/intl-eu.md`) give page numbers and further passages.*

---

## At a glance

| Dimension | The EU model |
|---|---|
| **What it is** | A legal regime (the Act) plus a voluntary, Commission-endorsed compliance instrument (the Code), with Commission guidelines interpreting the Act. The Act's risk model has **two separate tracks**: AI *systems*, graded by use (prohibited / high-risk / transparency / other), and general-purpose AI *models*, graded by capability (GPAI / GPAI with systemic risk). The Code covers only the second track, at its top tier. |
| **Unit of analysis** | For frontier AI, the **model**, meaning a GPAI model with systemic risk, including all its versions (cop 1230–1247). It is "not AI systems" (cop 62–64), though system architecture and inference compute must be considered (cop 64–68). |
| **Core concept** | **Systemic risk**: "a risk that is specific to the high-impact capabilities of general-purpose AI models, having a significant impact on the Union market due to their reach, or due to actual or reasonably foreseeable negative effects on public health, safety, public security, fundamental rights, or the society as a whole, that can be propagated at scale across the value chain" (act 3420–3423). |
| **Risk primitive** | "'risk' means the combination of the probability of an occurrence of harm and the severity of that harm" (act 3142). |
| **Taxonomy** | Code Appendix 1 (cop 1380–1545): 5 **types** (who or what is harmed); **nature** (3 essential and 6 contributing characteristics); **sources** (14 capabilities, 10 propensities, 13 affordances or contextual factors); 4 **specified systemic risks** that must always be assessed: CBRN, loss of control, cyber offence, harmful manipulation. |
| **Process** | Identify → analyse (model-independent information, evaluations, risk modelling, estimation, post-market monitoring) → accept or not (against the provider's own tiers, with a safety margin) → mitigate and re-assess → document (Framework, Model Report) → report incidents. Continuous over the lifecycle (cop 262–276). |
| **Grading** | *Which models are covered:* a binary classification by rebuttable presumption (> 10^25 FLOP) or by Commission designation (Annex XIII criteria). *Whether a model's risk is acceptable:* the provider defines "systemic risk tiers" that are capability-based, measurable, and include at least one tier not yet reached. The Code fixes the **form** of the tiers, not their **values**. *Incidents:* graded by harm type into reporting deadlines of 2, 5, 10 or 15 days. |
| **Method basis** | Probability × severity; EU product-safety law, the "New Legislative Framework" (market placement, conformity, harmonised standards, the Commission's "Blue Guide"); "international approaches" (the G7 Hiroshima risk list, copied into recital 110). No risk-management standard (such as ISO 31000) is cited as a basis. The Code's glossary does borrow "state of the art" and "best practice" and distinguishes "risk modelling" from cybersecurity "threat modelling". |
| **Purpose / audience** | Internal market plus protection of health, safety and fundamental rights (act 3026–3029). Addressed to *roles* (provider, deployer, etc.), not to named firms. The Code is addressed to signatory providers, and its reports go to the AI Office. |
| **Force** | Act: binding, directly applicable; GPAI fines up to 3% of worldwide turnover or EUR 15m (act 7950–7952); provisions apply on staggered dates. Code: voluntary; adherence is a way to *demonstrate* compliance, "not conclusive evidence" of it (cop 30–32), and it gives **no presumption of conformity** (guid 1139–1143; omni 743–746). |
| **Uncertainty and evidence** | A Precautionary Principle recital (cop 123–127); a safety margin in acceptance decisions; elicitation matched to misuse actors; validity and reproducibility requirements; external evaluators by default. The burden falls on the provider to rebut a presumption of systemic risk (guid 519–521). Mitigations cannot be used to escape classification (guid 575–583). |
| **Exclusions** | Military, defence and national security; pre-market research and development (Act); personal non-professional use; open-source relief (not available for systemic-risk models); risks not "specific to high-impact capabilities"; security obligations for models weaker than an open-weight model. Public transparency applies only "if and insofar as necessary". |

---

## Key terms as this model uses them

"Undefined" means the term is used but neither the Act (Art. 3), the Code's glossary, nor the Guidelines defines it. Where the instruments use a term in more than one sense, I say so; several of the collisions are *inside* this model.

| Term | Meaning in this model | Definition / source |
|---|---|---|
| **risk** | Probability of harm combined with its severity. | "'risk' means the combination of the probability of an occurrence of harm and the severity of that harm" (act 3142). The Code adopts it (cop 148, 438). |
| **systemic risk** | Risk specific to frontier ("high-impact") capabilities, with Union-scale impact propagating across the value chain. It is the Code's whole object. | Art. 3(65), act 3420–3423 (quoted in "At a glance"). The Code turns its three limbs into "essential characteristics" (cop 1426–1432). |
| **hazard** | Barely used. It appears twice in the Act, both times in the high-risk-*system* track: "The hazards of AI systems covered by the requirements of this Regulation" (act 1215); "residual risk associated with each hazard" (act 3835–3836, Art. 9). It is not used in the Code or the Guidelines. | Undefined. |
| **harm** | The thing risk is a probability and severity *of*. Its kinds are given by enumeration, not definition: the serious-incident list (act 3331–3344) and the Code's five risk types (cop 1397–1404). | Undefined (185 uses in the Act). |
| **severity** | A factor of risk. It also scales incident-report detail and deadlines ("appropriate for the severity of the incident", cop 1039–1040; act 6880). | Undefined. |
| **probability / likelihood** | "Probability" is a factor of risk (act 3142; cop 438). "Likelihood" appears mainly in a **different sense**: likelihood that a *causal link* exists between a model and an incident ("establish or suspect with reasonable likelihood such a causal relationship", cop 1047–1066; "the reasonable likelihood of such a link", act 6877). That is attribution, not occurrence. | Both undefined. |
| **systemic risk source** | "a factor which alone or in combination with other factors might give rise to systemic risk", with three kinds: capabilities, propensities, affordances or context. "Risk factor" is not used. | cop 1363–1364; lists at cop 1446–1514. |
| **capability** | What a model can do. The general sense is undefined. "High-impact capabilities" are defined relative to the frontier: "capabilities that match or exceed the capabilities recorded in the most advanced general-purpose AI models" (act 3417–3418), and are "not … a fixed level" (guid 562–563). | General: undefined. High-impact: Art. 3(64). |
| **propensity** | "inclinations or tendencies of a model to exhibit some behaviours or patterns". | Inline, cop 1477–1478. |
| **affordance** | "model configurations, model properties, and the context in which the model is made available on the market". | Inline, cop 1494–1495. |
| **threshold** | In the Act and the Guidelines, a **compute** threshold that triggers a legal presumption or classification: 10^25 FLOP for systemic risk (act 5663–5665); 10^23 FLOP (indicative) for being a GPAI model at all; one-third of original compute for a modifier becoming a provider (guid 216–219, 805–809). The Code does not use the word; it uses **tiers** and **trigger points**. | Undefined as a term; set numerically. |
| **systemic risk tier** | "tiers defined in the Framework that corresponds to a certain level of systemic risk stemming from a model"; one type of acceptance criterion. Provider-defined, capability-based, measurable, with at least one tier not yet reached (cop 547–552). | cop 1368–1370. |
| **systemic risk acceptance criteria** | "criteria defined in the Framework that Signatories use to decide whether the systemic risks stemming from their models are acceptable". | cop 1330–1332. "Acceptable" itself is undefined; its content is whatever the provider's justified criteria plus the safety margin say. |
| **trigger points** | Points ("defined in terms of, e.g. time, training compute, development stages, user access, inference compute, and/or affordances") at which lighter-touch evaluations are run. | Inline, cop 235–238. |
| **safety margin** | Allowance in the acceptance decision for uncertainty in sources, assessments and mitigation effectiveness. | Described, not glossed: cop 573–580. |
| **serious incident** | Act (for systems): an incident or malfunctioning that "directly or indirectly leads to" death or serious harm to health, serious and irreversible disruption of critical infrastructure, infringement of fundamental-rights obligations, or serious harm to property or the environment (act 3331–3344). For GPAI models the AI Office reads it to also cover "serious cybersecurity breaches … including the (self-)exfiltration of model parameters" (guid 1169–1178), and the Code follows (cop 1055). | Art. 3(49). Bare "incident" is undefined. |
| **near miss** | "a situation in which a serious incident could have, but ultimately did not, materialise". | cop 1270–1271. |
| **resolved (serious incident)** | The signatory "adopted corrective measures to rectify the harm, if possible, and to assess and mitigate systemic risks related to it". | cop 1307–1309. |
| **loss of control** | One of four specified systemic risks: "Risks from humans losing the ability to reliably direct, modify, or shut down a model", arising from misalignment, self-reasoning, self-replication, self-improvement, deception, resistance to goal modification, power-seeking, or autonomous AI creation (cop 1530–1533). In the Act, only recital 110's "unintended issues of control relating to alignment with human intent" (act 1922–1924). | Code App. 1.4. Undefined in the Act. |
| **control** | At least four senses in the family: (i) *loss of control* above; (ii) the Act's administrative "market surveillance and control"; (iii) a capability, "to control physical systems" (cop 1470); (iv) independence, being "free from the Signatory's control" (cop 1185). The Guidelines also use control over weights as a role test (guid 790–793). | Undefined. |
| **human oversight** | For high-risk *systems*, the designed ability of natural persons to monitor, interpret, override and interrupt ("'stop' button", Art. 14, act 4083–4131). In the Code it is an affordance ("level of human oversight (e.g. degree of model autonomy)", cop 1501), and evading it is a capability (cop 1463). | Undefined; described in Art. 14. |
| **mitigation** | "Systemic risk mitigations" comprise **safety** mitigations (C5), **security** mitigations (C6) and **governance** mitigations (Commitments 1 and 7–10). | cop 1343–1345. "Safety" and "security" are not defined; the Code separates them by object. Security concerns risks "from unauthorised releases, unauthorised access, and/or model theft" (cop 641–645); safety covers the rest. |
| **safeguard** | In the Act, mostly a *legal* protection ("appropriate safeguards for the fundamental rights and freedoms", e.g. act 408, 415). In the Omnibus it also means *technical* measures ("reasonable and adequate technical safety measures and other safeguards", omni 243–245, 1104–1105). The Code uses it once, contractually (cop 1186), and otherwise says "mitigation". | Undefined; two senses within the family. |
| **guardrail** | Used for removable safety behaviour ("the potential to remove guardrails", act 1922; "vulnerability to adversarial removal of guardrails", cop 1502). | Undefined. |
| **alignment / misalignment** | Two senses inside this model. In the Act, **alignment is a training activity**: technical documentation must describe "model adaptations, including alignment and fine-tuning" (act 9125). In the Code, **misalignment is a propensity** of the model: "misalignment with human intent" and "misalignment with human values (e.g. disregard for fundamental rights)" (cop 1479–1480). | Undefined in both. |
| **deception** | "model behaviours that systematically produce false beliefs in others, including model behaviours to achieve goals that involve evading oversight, such as a model's detecting that it is being evaluated and under-performing or otherwise undermining oversight". | cop 1159–1162. |
| **insider threats** | "hostile operations by humans, AI models, and/or AI systems … with access to sensitive organisational resources, and/or accidental model leakage"; models can be insiders ("model self-exfiltration"). | cop 1192–1196. |
| **(self-)exfiltration of model weights** | "access or transfer of weights or associated assets of a model from their secure storage by the model itself and/or an unauthorised actor". | cop 1315–1316. |
| **non-state external threats** | A quantified adversary class: "roughly comparable to ten experienced, professional individuals in cybersecurity … several months with a total budget of up to EUR 1 million … major pre-existing cyberattack infrastructure but no pre-existing access". | cop 1273–1277. |
| **model evaluation / model elicitation** | Evaluation: "a systemic risk assessment technique that can be used in all stages of systemic risk assessment" (cop 1262–1263). Elicitation: "technical work to systematically enhance a model's capabilities, propensities, affordances, and/or effects, thereby facilitating an accurate measurement of the full range" (cop 1257–1260). | Code glossary. |
| **systemic risk scenario / modelling** | Scenario: "a scenario in which a systemic risk stemming from a model might materialise" (cop 1358). Modelling: "a structured process aimed at specifying pathways through which a systemic risk … might materialise; often used interchangeably with the term 'threat modelling'", renamed to avoid the cybersecurity sense (cop 1347–1350). | Code glossary. |
| **state of the art / best practice** | Best practice: "accepted amongst providers … as the processes … that best assess and mitigate systemic risks at any given point in time" (cop 1152–1154). State of the art: "the forefront of relevant research, governance, and technology that goes beyond best practice" (cop 1324–1325). | Code glossary. |
| **post-market monitoring** | Act (systems): "all activities carried out by providers … to collect and review experience gained from the use of AI systems" (act 3216–3218). Code (models): "the monitoring of a model in the time span from when it is placed on the market until the retirement" (cop 1279–1280). | Two definitions, two objects. |
| **model** | Act: "AI model" is undefined; "general-purpose AI model" is defined (act 3411–3415). Code: "a general-purpose AI model with systemic risk", including all versions that "in aggregate, constitute the systemic risk(s)" (cop 1230–1247). | As stated. |
| **provider** | One who "develops … or that has … developed and places it on the market or puts the AI system into service under its own name or trademark". | Art. 3(3), act 3144–3146. |
| **deployer** | "a natural or legal person, public authority, agency or other body using an AI system under its authority except where the AI system is used in the course of a personal non-professional activity". It applies to *systems* only; there is no model-deployer role. | Art. 3(4), act 3148–3149. |
| **developer** | **Not a role in this model.** It appears twice in Act recitals in ordinary usage (act 1616, 2441), never in the Code, and once in the Guidelines. The Guidelines' **downstream modifier** (an actor "distinct from the original provider and not acting on its behalf" who modifies a model, guid 780–782) becomes a provider above the compute test. | Undefined. |
| **downstream provider** | "a provider of an AI system, including a general-purpose AI system, which integrates an AI model". | Art. 3(68), act 3432–3434. |
| **signatory** | A provider that has signed the Code; the bound party of every Commitment. | Used throughout the Code; not glossed. |
| **placing on the market** | "the first making available of an AI system or a general-purpose AI model on the Union market". It is the regime's trigger event. | Art. 3(9), act 3165–3166; examples in guid 699–722. |

---

## 1. Two instruments, three layers of text

- **The Act** is law. It defines, classifies and imposes duties on roles. Its recitals ("Whereas…") are non-binding interpretive text; its articles and annexes bind. The GPAI provisions are Chapter V, Articles 51–56 (act 5641–5961), with enforcement in Articles 88–94 and 101.
- **The Code's Safety and Security chapter** is a text drafted by independent chairs and adopted by signatory providers. It exists "to serve as a guiding document for demonstrating compliance with the obligations provided for in Articles 53 and 55 AI Act, while recognising that adherence to the Code does not constitute conclusive evidence of compliance" (cop 30–32). Every Commitment is headed with the article it serves, e.g. "LEGAL TEXT: Articles 55(1) and 56(5), and recitals 110, 114, and 115 AI Act" (cop 167).
- **The Commission's Guidelines** interpret the Act ("not binding … Nevertheless, these guidelines set out the Commission's interpretation and application of the AI Act, on which it will base its enforcement action", guid 131–135).

The Act asks for the Code's structure. Article 56(2) asks codes to cover "the identification of the type and nature of the systemic risks at Union level, including their sources" and "the measures, procedures and modalities for the assessment and management of the systemic risks" (act 5906–5912). Recital 116 says codes "should help to establish a risk taxonomy of the type and nature of the systemic risks at Union level, including their sources" (act 2038–2040). Appendix 1's headings (types, nature, sources) are that mandate filled in.

The Code has its own three registers:
- recitals, in which signatories "recognise";
- Commitments, in which signatories "commit to";
- Measures, in which signatories "will", sometimes with safe harbours ("This Measure is presumed to be fulfilled, if …", cop 914).

---

## 2. What the model names

### Objects

| Object | Definition (verbatim) | Where |
|---|---|---|
| AI system | "a machine-based system that is designed to operate with varying levels of autonomy and that may exhibit adaptiveness after deployment, and that, for explicit or implicit objectives, infers, from the input it receives, how to generate outputs …" | act 3137–3140 |
| General-purpose AI model | "an AI model … that displays significant generality and is capable of competently performing a wide range of distinct tasks … and that can be integrated into a variety of downstream systems or applications, except AI models that are used for research, development or prototyping activities before they are placed on the market" | act 3411–3415 |
| High-impact capabilities | "capabilities that match or exceed the capabilities recorded in the most advanced general-purpose AI models" | act 3417–3418 |
| Systemic risk | see "At a glance" | act 3420–3423 |
| General-purpose AI system | "an AI system which is based on a general-purpose AI model and which has the capability to serve a variety of purposes" | act 3425–3426 |
| Serious incident (system) | an incident or malfunctioning that "directly or indirectly leads to" death or serious harm to health; "serious and irreversible disruption" of critical infrastructure; infringement of fundamental-rights obligations; "serious harm to property or the environment" | act 3331–3344 |
| "model" (in the Code) | "a general-purpose AI model with systemic risk". References to "model" cover "all model versions that, in aggregate, constitute the systemic risk(s) stemming from the model", including the most advanced, those "with limited or no safety and/or security mitigations", and those "used widely" | cop 1230–1247 |

"AI model" on its own is not defined in the Act. Recital 97 distinguishes models from systems: models "require the addition of further components, such as for example a user interface, to become AI systems" (act 1739–1742).

### Roles

The Act regulates *roles*, not organisations: provider, deployer, authorised representative, importer, distributor, "operator" (the collective term), and downstream provider (act 3144–3161, 3432–3434). There is **no "developer"**. A provider is one who "develops an AI system or a general-purpose AI model or that has an AI system or a general-purpose AI model developed **and places it on the market** … under its own name or trademark" (act 3144–3146).

Roles are conferred by rules (the Guidelines' reading):
- a downstream modifier becomes a provider when its modification compute exceeds a third of the original model's (guid 802–809);
- "who has the control over the model's weights" is a factor in deciding who modified a model (guid 790–793);
- internal use "essential for providing a product or service to third parties" counts as placing on the market (guid 720–722).

The Omnibus later groups providers by **undertaking** for supervision purposes (omni 1695–1696).

### Duties of a GPAI-with-systemic-risk provider (Art. 55(1), act 5856–5869)

> "(a) perform model evaluation in accordance with standardised protocols and tools reflecting the state of the art, including conducting and documenting adversarial testing … (b) assess and mitigate possible systemic risks at Union level, including their sources … (c) keep track of, document, and report, without undue delay … relevant information about serious incidents … (d) ensure an adequate level of cybersecurity protection for the general-purpose AI model with systemic risk and the physical infrastructure of the model."

These come on top of the duties of every GPAI provider under Art. 53: technical documentation, information for downstream providers, a copyright policy, and a training-data summary.

---

## 3. The taxonomy (Code Appendix 1, cop 1380–1545)

Appendix 1 opens by quoting the Act's definitions of high-impact capabilities and systemic risk, then lists "ADDITIONAL LEGAL TEXT: Recital 110 AI Act" (cop 1385–1393). In cases of doubt it is to be read "in good faith in light of: (1) the probability and severity of harm … and (2) the definition of 'systemic risk'" (cop 147–150).

```
SYSTEMIC RISK
├── 1.1 TYPES (what is at risk; "distinct but in some cases overlapping")
│     public health · safety · public security · fundamental rights · society as a whole
│     + examples to draw on: major accidents; critical sectors/infrastructure; public mental
│       health; freedom of expression; non-discrimination; privacy; environment; non-human
│       welfare; economic security; democratic processes; concentration of power; illegal,
│       violent, hateful, radicalising or false content incl. CSAM and NCII     (cop 1397–1415)
│
├── 1.2 NATURE
│     essential (all three required, from the Act's definition):
│       specific to high-impact capabilities · significant impact on the Union market ·
│       propagated at scale across the value chain                              (cop 1426–1432)
│     contributing:
│       capability-dependent · reach-dependent · high velocity ("potentially outpacing
│       mitigations") · compounding or cascading · difficult or impossible to reverse ·
│       asymmetric impact                                                       (cop 1434–1444)
│
├── 1.3 SOURCES ("non-exhaustive, potential")
│     capabilities (14): offensive cyber; CBRN; persistent serious infringement of
│       fundamental rights; manipulate/persuade/deceive; operate autonomously; adaptively
│       learn new tasks; long-horizon planning; self-reasoning ("its ability to know if it is
│       being evaluated"); evade human oversight; self-replicate/self-improve/modify own
│       environment; automate AI R&D; multimodality; tool use incl. "computer use";
│       control physical systems                                                (cop 1451–1470)
│     propensities (10) — "inclinations or tendencies of a model to exhibit some behaviours":
│       misalignment with human intent; misalignment with human values; tendency to deploy
│       capabilities harmfully; hallucination/misinformation; discriminatory bias; lack of
│       performance reliability; lawlessness; "goal-pursuing", harmful resistance to goal
│       modification, "power-seeking"; "colluding"; mis-coordination or conflict with other
│       AI                                                                       (cop 1475–1490)
│     affordances & other sources (13) — "model configurations, model properties, and the
│       context in which the model is made available": access to tools/compute/physical
│       systems; scalability; release and distribution strategies; level of human oversight;
│       vulnerability to guardrail removal; vulnerability to exfiltration; infrastructure
│       security; number of business and end users; offence-defence balance; vulnerability of
│       the affected environment; lack of explainability; interactions with other AI;
│       inappropriate use                                                        (cop 1492–1514)
│
└── 1.4 SPECIFIED SYSTEMIC RISKS (always identified; must use tiers)             (cop 1520–1545)
      CBRN · LOSS OF CONTROL · CYBER OFFENCE · HARMFUL MANIPULATION
```

The four specified risks, verbatim:
- **CBRN**: "Risks from enabling chemical, biological, radiological, and nuclear (CBRN) attacks or accidents. This includes significantly lowering the barriers to entry for malicious actors, or significantly increasing the potential impact achieved …" (cop 1525–1529).
- **Loss of control**: "Risks from humans losing the ability to reliably direct, modify, or shut down a model. Such risks may emerge from misalignment with human intent or values, self-reasoning, self-replication, self-improvement, deception, resistance to goal modification, power-seeking behaviour, or autonomously creating or improving AI models or AI systems" (cop 1530–1533).
- **Cyber offence**: "Risks from enabling large-scale sophisticated cyber-attacks, including on critical systems … e.g. through automated vulnerability discovery, exploit generation, operational use, and attack scaling" (cop 1534–1538).
- **Harmful manipulation**: "Risks from enabling the strategic distortion of human behaviour or beliefs by targeting large populations or high-stakes decision-makers through persuasion, deception, or personalised targeting …" (cop 1539–1545).

How the taxonomy is used, in my reading:
- Types and nature *qualify* a risk.
- Sources are where identification starts. Identification also draws on model-independent information, incidents, and "any other relevant information communicated … by the AI Office, the Scientific Panel … or other initiatives, such as the International Network of AI Safety Institutes" (cop 356–371).
- The specified risks are a floor.
- There is **no causal structure between sources**: the lists are parallel. Causal pathways enter only through the provider's own "systemic risk scenarios" and "risk modelling" (see §4).

Two glossary definitions carry more of the model:
- "Deception": "model behaviours that systematically produce false beliefs in others, including model behaviours to achieve goals that involve evading oversight, such as a model's detecting that it is being evaluated and under-performing or otherwise undermining oversight" (cop 1159–1162).
- "Insider threats": "hostile operations by humans, AI models, and/or AI systems (e.g. … model self-exfiltration)" (cop 1192–1196).

---

## 4. How the parts relate: the process

```
                    (continuous, "along the entire model lifecycle")
lighter-touch evaluations at trigger points · post-market monitoring · serious incidents
                                   │  escalate to ↓
┌───────────────────────── FULL SYSTEMIC RISK ASSESSMENT AND MITIGATION ─────────────────┐
│ 1 IDENTIFY  (C2)  types → nature → sources → identified risks + the 4 specified risks  │
│               └─ systemic risk scenarios for each                                      │
│ 2 ANALYSE   (C3)  model-independent info · model evaluations (App. 3) · risk modelling │
│               · risk estimation (probability × severity) · post-market monitoring      │
│ 3 ACCEPT?   (C4)  compare with the provider's own tiers/criteria, plus a safety margin │
│ 4 if not acceptable: don't place / restrict / withdraw / recall; safety (C5) and       │
│               security (C6) mitigations; loop back to 1                                │
└────────────────────────────────────────────────────────────────────────────────────────┘
      documented in: FRAMEWORK (C1, provider-wide) and MODEL REPORT (C7, per model)
      supported by:  responsibility allocation, resources, risk culture (C8)
      reporting:     SERIOUS INCIDENTS (C9) · documentation and public summaries (C10)
```

- "Signatories will implement a full systemic risk assessment and mitigation process that involves four steps …" (cop 262–272). This is done "at least before placing the model on the market" and whenever a Model Report must be updated (cop 273–275).
- **Mitigations come in three kinds**: safety (C5), security (C6) and governance (Commitments 1 and 7–10) (cop 1343–1345).
  - Safety examples range from data filtering and refusal training through staged access to "techniques to enable safe ecosystems of AI agents" and "defending against a model's ability to subvert its other safety mitigations" (cop 616–631).
  - Security is set against a provider-chosen "Security Goal" naming the threat actors to be resisted (cop 653–657). There is a quantified floor for "non-state external threats": "roughly comparable to ten experienced, professional individuals in cybersecurity … up to EUR 1 million" (cop 1273–1277). Specific controls are in Appendix 4, and the RAND *Securing AI Model Weights* report is cited as guidance (cop 775–776).
- **Accountability is structured within the organisation.** There are four responsibilities (oversight, ownership, support and monitoring, assurance) across five organisational levels, from the board in its supervisory function down to external assurance providers. The support-and-monitoring owner "must not also be responsible for the Signatory's core business activities that may produce systemic risk" (cop 886–948).
- **Revision triggers are part of the model.** The Framework is reassessed at least every 12 months, or sooner when there are "reasonable grounds" (cop 293–306). A Model Report must be updated when "the justification for why the systemic risks stemming from the model are acceptable … has been materially undermined" (cop 822–835). Every Model Report must state "the reasonably foreseeable conditions under which the justification … would no longer hold" (cop 717–718).

### The norm structure

In the Act, each duty has five parts:
- an issuer (the legislature, or the Commission by delegated or implementing act);
- a bound role (provider of a GPAI model with systemic risk);
- a deontic type: obligation (Art. 55); prohibition (Art. 5); exemption, as for open-source models, "unless … systemic risk" (act 5762–5765);
- an applicability condition (classification);
- time, both as deadlines in the text and as dates of application.

The Code converts the obligations into the signatory's own undertakings, which the AI Office then monitors. For signatories, "the Commission will focus its enforcement activities on monitoring their adherence to the code of practice" (guid 1103–1105).

---

## 5. How risk is graded

**Grade 1: is the model in the systemic-risk regime at all?** This is binary.
- Presumption: "A general-purpose AI model shall be presumed to have high impact capabilities … when the cumulative amount of computation used for its training measured in floating point operations is greater than 10^25" (act 5663–5665). Compute is justified as "one of the relevant approximations for model capabilities" (act 1944–1946).
- Designation: the Commission can designate on the Annex XIII criteria. These are parameters, data, compute or its proxies, modalities, benchmarks, "level of autonomy and scalability, the tools it has access to", and reach, which is presumed at "at least 10 000 registered business users established in the Union" (act 9176–9191).
- The referent moves by design. The Commission "does not consider it to refer to a fixed level of capabilities" (guid 562–563). The thresholds can be changed by delegated act (act 5667–5670).

**Grade 2: is a given risk acceptable?** This is provider-defined, in a form the Code prescribes. For each identified risk the provider will "define appropriate systemic risk tiers that: (i) are defined in terms of model capabilities, and may additionally incorporate model propensities, risk estimates, and/or other suitable metrics; (ii) are measurable; and (iii) comprise at least one systemic risk tier that has not been reached by the model" (cop 547–552). Non-tier criteria are allowed except for the four specified risks (cop 553–555).
- For each tier the Framework must say "what safety and security mitigations Signatories would need to implement once each systemic risk tier is reached" (cop 208–209). It must also estimate "timelines when Signatories reasonably foresee that they will have a model that exceeds the highest systemic risk tier already reached", which "may consist of time ranges or probability distributions" (cop 210–216).
- Estimation formats are open: "risk score, risk matrix, probability distribution, or in other adequate formats … quantitative, semi-quantitative, and/or qualitative", e.g. "'moderate' or 'critical'", "'probability: unlikely' x 'impact: high'", "'X-Y%' x 'X-Y EUR damage'" (cop 442–446).
- The decision rule: "Signatories will only proceed with the development, the making available on the market, and/or the use of the model, if the systemic risks stemming from the model are determined to be acceptable" (cop 584–586).
- **The Code sets no threshold values and no acceptable-risk level.** Acceptability is whatever the provider's justified criteria say, plus the safety margin, subject to the AI Office's review of the justification (Model Report, cop 713–723).

**Grade 3: comparative exemption.** A "similarly safe or safer model", benchmarked against a "safe reference model" (cop 1548–1599), can skip external evaluation and publication. Safety is here graded *relative* to another model.

**Grade 4: incidents.** Initial reports are due 2 days after becoming aware for critical-infrastructure disruption, 5 days for a serious cybersecurity breach "including the (self-)exfiltration of model weights", 10 days for a death, and 15 days for other serious harm (cop 1043–1066). Intermediate reports follow every 4 weeks, and a final report within 60 days of resolution (cop 1068–1075).

---

## 6. Method: what it rests on and where it comes from

- **Probability × severity** (Art. 3(2), act 3142) is the risk primitive. The Code's analysis ends in estimating "the probability and severity of harm for the systemic risk" (cop 438).
- **EU product-safety law** supplies the rest of the frame. The Act places itself there explicitly: "Based on the New Legislative Framework, as clarified in Commission notice 'The "Blue Guide" on the implementation of EU product rules 2022' …" (act 1211–1212). The main features:
  - "placing on the market" as the trigger;
  - operators defined by role;
  - conformity with presumptions from harmonised standards: "Compliance with European harmonised standards grants providers the presumption of conformity" (act 5873–5874);
  - codes of practice as an interim route "until a harmonised standard is published" (act 5871–5873).

  The Guidelines interpret "placing on the market" through the Commission's "Blue Guide" on EU product rules (guid 723–726) and use the Blue Guide's "new product" test for modifications (guid 796–801).
- **"International approaches."** The Act tells codes to take "into account international approaches" (act 5892). Recital 110 reproduces, nearly verbatim, the risk list from the G7 Hiroshima Code of Conduct (Action 1): CBRN "barriers to entry", offensive cyber, "the capacity to control physical systems and interfere with critical infrastructure", "making copies of themselves or 'self-replicating' or training other models", and "a chain reaction with considerable negative effects that could affect up to an entire city" (act 1922–1932). The only loss-of-control language in the Act is the phrase it adds to that list: "unintended issues of control relating to alignment with human intent" (act 1922–1924). The Code's specified risks cite recital 110 and "international approaches pursuant to Article 56(1)" (cop 1521–1523).
- **No named risk-management standard.** The identify–analyse–evaluate–treat loop is the general shape of risk-management standards such as ISO 31000. Neither text cites one as its basis; that resemblance is my observation. The Code allows signatories to "rely on international standards to the extent they cover the provisions of this Chapter" (cop 89–90). The Act's own risk-management article for *high-risk systems* (Art. 9, act 3796–3878: "residual risk … judged to be acceptable") is a parallel the Code does not cite.
- **The state of the art as a moving standard.** Measures must be "at least state-of-the-art" (a term defined in the glossary as beyond "best practice", cop 1324–1325), "unless systemic risk can be conclusively ruled out with a less advanced process" (cop 53–56). The standard of care rises as the field moves.

---

## 7. Purpose, audience, force

- **Purpose.** "To improve the functioning of the internal market and promote the uptake of human-centric and trustworthy artificial intelligence (AI), while ensuring a high level of protection of health, safety, fundamental rights … against the harmful effects of AI systems in the Union and supporting innovation" (act 3026–3029). The Code repeats this as its "overarching objective" (cop 22–26).
- **Audience.**
  - The Act: operators by role.
  - The Code: signatory providers. Its artefacts go to the AI Office: the Framework within five business days of confirmation (cop 326–327); the Model Report "without redactions" by market placement (cop 861–866).
  - The public: only summaries, "If and insofar as necessary to assess and/or mitigate systemic risks" (cop 1122–1127).
- **Force.**
  - The Act is binding, but its provisions apply on staggered dates: Chapter V from 2 August 2025, fines from 2 August 2026 (act 8303–8312; guid 1257–1263 notes the obligations "apply" in the gap even though they cannot yet be enforced).
  - The Code is voluntary. The Commission assesses its adequacy (after the Omnibus; before it, the AI Office and the Board, omni 1427–1431). Signing brings closer, adherence-focused supervision and "increased trust" (guid 1103–1108). Adherence can count as a mitigating factor when fines are set (guid 1123–1125). Non-signatories must show "alternative adequate means", for instance "a gap analysis" against the Code, and "may also be subject to a larger number of requests for information" (guid 1109–1122).
  - Codes "have limited legal effect, and in particular do not grant a presumption of conformity" (omni 743–746). Only harmonised standards do, and none yet exist for GPAI.

---

## 8. Uncertainty and evidence

- **Precaution as a rule of the instrument.** "The Signatories recognise the important role of the Precautionary Principle, particularly for systemic risks for which the lack or quality of scientific data does not yet permit a complete assessment. Accordingly … the extrapolation of current adoption rates and research and development trajectories of models should be taken into account for the identification of systemic risks" (cop 123–127).
- **A safety margin on every acceptance decision**, which "take[s] into account potential limitations, changes, and uncertainties of: (a) systemic risk sources (e.g. capability improvements after the time of assessment); (b) systemic risk assessments (e.g. under-elicitation of model evaluations or historical accuracy of similar assessments); and (c) the effectiveness of safety and security mitigations (e.g. mitigations being circumvented, deactivated, or subverted)" (cop 573–580).
- **Evaluation quality is specified.**
  - Evaluations need "high scientific and technical rigour": internal validity, external validity and reproducibility, each defined with examples (cop 1164–1219, 1289–1305, 1606–1611).
  - Elicitation must "minimise the risk of model deception during model evaluations (e.g. sandbagging)" and "match the model elicitation capabilities of misuse actors" (cop 1617–1633).
  - Evaluation teams get access up to "activations, gradients, logits … chains-of-thought" and "the model version(s) with the fewest safety mitigations implemented (such as a helpful-only model version)" (cop 1663–1668).
  - Open-ended testing is required "with a view to identifying unexpected behaviours, capability boundaries, or emergent properties" (cop 418–424).
  - Independent external evaluation is the default, except for similarly-safe models or when no qualified evaluator can be found. In the second case the missing evaluation must count as "potential additional uncertainty" in the acceptance decision (cop 1686–1695).
- **Evidence that does not come from evaluations.** Web searches, literature, market analyses, training-data review, incident databases, forecasting, expert and "lay interviews" (cop 399–411); and post-market signals including "hidden chains-of-thought" (cop 482–484).
- **Burden of proof.** A provider over the threshold may argue that "exceptionally … the general-purpose AI model does not present, due to its specific characteristics, systemic risks" (act 5683–5686). "The burden of adducing evidence that the presumption … should not apply should be borne by that provider" (guid 519–521). Mitigations do not count: arguments "because of mitigations already or planned to be implemented are not suitable grounds … the model still poses systemic risks which must continuously be assessed and mitigated" (guid 577–581). The Code also requires the Model Report to compare risks "with safety and security mitigations implemented and with the model fully elicited" (cop 741–742).
- **Incident causation standard.** Report where the model's involvement led to the harm, "or if the Signatories establish or suspect with reasonable likelihood such a causal relationship" (cop 1047–1066). "The reporting of a serious incident is not an admission of wrongdoing", and evidence must be kept *before* incidents because it "may be lost, overwritten, or fragmented" (cop 153–160).

---

## 9. What is excluded

- **From the Act altogether:**
  - "exclusively for military, defence or national security purposes" (act 3084–3090);
  - models or systems "specifically developed and put into service for the sole purpose of scientific research and development" (act 3104–3105);
  - "any research, testing or development activity … prior to their being placed on the market" (act 3112–3113);
  - personal non-professional use (act 3119–3120).
- **From GPAI duties:**
  - models before they are placed on the market (act 3414–3415);
  - own-model use "for purely internal processes that are not essential for providing a product or a service to third parties" (act 1748–1750).
- **Open-source relief.** Documentation duties are waived for free and open-source models whose weights are public, "This exception shall not apply to general-purpose AI models with systemic risks" (act 5762–5765). Under the Code, security duties end once weights are public or deleted (cop 650–651). Models weaker than some open-weight model are exempt from the security Commitment entirely (cop 647–648).
- **From "systemic" risk.** Anything not "specific to high-impact capabilities" (cop 1428), however serious. The chairs' statement asks the Commission to state that the obligations apply "only … to risks that are specific to the frontier of capabilities" (eu-cop-chairs-2025-statement 82–84).
- **From the Code's object.** AI systems as such (cop 62–64), and so deployers.
- **From public view.** The Framework and Model Reports need not be published beyond summaries "if and insofar as necessary" (cop 1122–1130).

One tension, which is my reading: the Act excludes pre-market development, yet the Code's lifecycle covers "development that occurs before and after a model has been placed on the market" (cop 48–50). Its go/no-go rule governs proceeding "with the development" (cop 538, 584). The Guidelines have notification triggered "before training is complete" (guid 453–455) and the lifecycle beginning "at the start of the large pre-training run" (guid 357–358). The voluntary instrument reaches earlier than the statute's scope clause.

---

## 10. Closing note: where this meets Joseph's chain

This is my reading, and short on purpose. The EU model is a **process and accountability model**, not a causal model. The taxonomy lists *sources* (capabilities, propensities, affordances) and *harm types* in parallel, without edges. Causation is delegated to each provider's "systemic risk scenarios" and "risk modelling" (cop 373–375, 430–435), which the Code requires but does not supply.

Mapped against the chain:
- (sources & causes) ≈ Appendix 1.3;
- (preventions & controls) ≈ safety, security and governance mitigations, plus the tier → mitigation mapping;
- (risk-events, recorded) ≈ serious incidents and near misses (the Code defines "near miss": "a situation in which a serious incident could have, but ultimately did not, materialise", cop 1270–1271);
- impact radius ≈ Appendix 1.1 types and the incident harm list, with degree terms in Appendix 1.2 (velocity, cascading, irreversibility, asymmetry);
- (mitigations & recovery) ≈ corrective measures, withdrawal and recall (cop 592–593) and incident response;
- (policies & decision-making) ≈ the acceptance decision itself, plus the whole norm layer.

Where it cuts across the chain:
- The central quantity is **acceptability relative to provider-set criteria**, not magnitude.
- The model's own boundary is set by a **capability threshold that deliberately moves** ("high-impact" is defined relative to the frontier).
- The model treats **the model as a possible adversary to its own mitigations and to evaluation** (deception, sandbagging, self-exfiltration as an insider threat, "a model's ability to subvert its other safety mitigations"). That is loss of control built into the ordinary machinery, not confined to one of the four specified risks.
