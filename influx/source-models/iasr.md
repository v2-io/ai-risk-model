# The International AI Safety Report's own model of AI risk

*From the atlas agent for the IASR family (`../source-atlas/iasr.md`), 2026-09-28. The report is described on its own terms, not mapped onto our schema.*

## Sources and line references

- **"md":** `ref/iasr-2026-full.md` (the 2026 full report).
- **"2025":** `…/scratchpad/src-text/bengio-2025-international.txt` (the 2025 full report).
- **KU1 and KU2:** the two 2025 Key Updates in the same folder.
- **ES:** the 2026 Extended Summary for Policymakers.
- Page numbers are in the atlas.

## At a glance

| Dimension | IASR |
|---|---|
| **What it names** | General-purpose AI **capabilities** (the driver); **risks**, organised in three categories; **harms** (the materialised, documented subset); **risk management** (practices, technical safeguards, and in 2026 **societal resilience**); **evidence gaps**; **challenges for policymakers**. |
| **Taxonomy** | Three risk categories: **malicious use / malfunctions / systemic**, with named risks under each (13 in 2025, 8 in 2026). "Not exhaustive or mutually exclusive." For loss of control specifically, 2026 has a three-factor conjunctive model: **capability × propensity × deployment environment**. 2025 had two factors. |
| **How the parts relate** | A three-part argument: *what AI can do → what risks that creates → what management exists and how well it works*. Within each risk, a fixed template: Key information / body / Updates / Evidence gaps / Mitigations / Challenges for policymakers (2026). No causal network. Relations are carried in prose, plus a few decompositions: loss-of-control factors, the cyberattack chain, bioweapon stages, and Resist/Absorb/Recover/Adapt. |
| **Grading** | It declines to grade on a scale. Risk is *defined* as "the combination of the probability and severity of a harm" (md 2480), but no risk is scored. Severity and likelihood are characterised in prose, often as expert disagreement. The one graded instrument is Table 2.3, which grades how much AI contributed to observed cyber trends. |
| **Method** | A synthesis of the scientific literature, by an independent writing team under a Chair, reviewed by an international advisory panel, senior advisers, and industry and civil-society reviewers. 2025 states six **source-quality criteria**. Risk management is organised by borrowed standards (NIST AI RMF, ISO/IEC 23894, OECD, SRA). Forecasts and scenarios are commissioned from FRI and OECD. |
| **Purpose, audience, force** | To give policymakers a "shared, science-based understanding" and help them navigate the **"evidence dilemma"**. It says it is **not prescriptive** and makes no policy recommendations, though a few "should" and "must" sentences occur. |
| **Uncertainty and evidence** | Uncertainty is the report's central finding in both editions, and it names it the evidence dilemma. Every 2026 section has a mandatory "Evidence gaps" subsection. Hedges are prose, with no calibrated scale. Expert disagreement is reported *as* the finding. Scenarios are offered in place of forecasts. |
| **Exclusions** | Narrow AI; military AI (LAWS); a comprehensive account of benefits; how regulation affects the pace of AI; policy recommendations. From 2026 also: bias, environment, privacy and copyright. Those were 2025 chapters, dropped to focus on "emerging risks at the frontier". |

## Sketch

```
                         GENERAL-PURPOSE AI  (scope: models & systems that perform
                         "a wide variety of tasks"; frontier = "emerging risks")
                                  │
            Ch.1  CAPABILITIES ── drivers: compute · algorithms · data (+ inference-time scaling)
                  │                current (jagged) · by 2030 (4 OECD scenarios)
                  │   "the same capabilities that make these systems useful also create new risks"
                  ▼
            Ch.2  RISKS  (three categories, "not exhaustive or mutually exclusive")
          ┌──────────────────────┬───────────────────────────┬──────────────────────────┐
          │ MALICIOUS USE        │ MALFUNCTIONS              │ SYSTEMIC                 │
          │ actors deliberately  │ AI fails or behaves in    │ arise from widespread    │
          │ use AI to cause harm │ unexpected, harmful ways  │ deployment               │
          ├──────────────────────┼───────────────────────────┼──────────────────────────┤
          │ content & crime      │ reliability               │ labour market            │
          │ influence & manip.   │ loss of control:          │ human autonomy           │
          │ cyberattacks         │  capability × propensity  │ (2025 also: R&D divide,  │
          │ bio & chem           │  × deployment environment │  market concentration,   │
          │                      │ (2025 also: bias)         │  environment, privacy,   │
          │                      │                           │  copyright)              │
          └──────────────────────┴───────────────────────────┴──────────────────────────┘
               each risk: Key info · evidence · Updates · Evidence gaps · Mitigations · Challenges
                  ▼
            Ch.3  RISK MANAGEMENT
                  3.1 why it is hard: 4 challenge categories (science gaps · information
                      asymmetries · market failures · institutional/coordination) → "evidence dilemma"
                  3.2 practices: identify → analyse & evaluate → mitigate, around governance
                      (+ Frontier AI Safety Frameworks, if-then commitments, laws)
                  3.3 technical safeguards: safer models · deployment monitoring & control · ecosystem monitoring
                  3.4 open-weight models (distinct challenge; irreversibility; marginal risk)
                  3.5 societal resilience: Resist · Absorb · Recover · Adapt
                  ──── organising principle: DEFENCE-IN-DEPTH ("Swiss cheese")
                       training → deployment → post-deployment monitoring → societal resilience
```

## Key terms as this model uses them

**Where the definitions come from:**
- **2026:** the glossary at md 2196–2556 (the original repo also kept it as a separate file, `iasr-2026-glossary.md`, not carried over here; that file's line = md line − 2195), plus a few inline definitions.
- **2025:** the glossary at 2025 10887–11498, and per-section Key Definitions boxes.

**Status labels in the table:**
- "defined" means a glossary definition exists;
- "inline" means it is defined only in running text;
- "used but undefined" means neither.

Where 2025 differs materially, it is noted.

| Term | Status in 2026 | Meaning in IASR (verbatim where defined) |
|---|---|---|
| **risk** | defined | "The combination of the probability and severity of a harm." (md 2480). 2025: "… of a harm that arises from the development, deployment, or use of AI" (2025 7952–7953). Defined as probability × severity, but **no risk in the report is ever scored**. In practice "risk" names a *topic area*, e.g. "cyberattacks" or "loss of control". |
| **hazard** | defined, barely used | "Any event or activity that has the potential to cause harm, such as loss of life or injury." (md 2354). 2025 added "social disruption, or environmental damage" (2025 7954–7955). The body almost never uses it as a working term. It appears in names ("AI Incidents and Hazards Monitor"), in "system-level hazards" (the STPA sense, md 1698), and in "information hazards", a different sense: "information that may be harmful to share" (md 1099). |
| **harm** | used but undefined | Used ~190 times. It is the realised outcome that risk is the probability-weighted form of. "Documented harms" are what separate materialised from emerging risks (md 394). |
| **severity** | used but undefined | Always paired with likelihood, in prose: "uncertain likelihood but potentially extreme severity" (md 1246); "act in proportion to their severity and likelihood" (md 398). No scale. |
| **likelihood / probability** | used but undefined | Prose only; there is no calibrated vocabulary. "Probabilistic" is glossed only as a mathematical word (md 2454). Numeric probabilities appear only as reported elicitations: FRI forecasts at md 714 and 736. |
| **risk factors** | defined | "Properties or conditions that can increase the likelihood or severity of harm. In AI, for example, poor cybersecurity is a risk factor that could make it easier for malicious actors to obtain and misuse an AI system." (md 2482) |
| **emerging risks** | inline | "risks that arise at the frontier of AI capabilities" (md 362). This is the scope term of the 2026 edition. |
| **systemic risks** | defined, three wordings | Glossary: "Risks that arise from how AI development and deployment changes human behaviour, organisational practices, or societal structures, rather than directly from AI capabilities" (md 2522). Intro footnote: "risks that result from widespread deployment of highly-capable general-purpose AI across society and the economy" (md 487). Both note that the EU AI Act uses the term differently. 2025: "beyond the capabilities of individual models or systems" (2025 11446). |
| **malicious use / misuse** | defined, used interchangeably | "Using something, such as an AI system, to intentionally cause harm." (md 2388). The Chapter 2 opener says "misuse" (md 834), the §2.1 heading says "malicious use", and the Extended Summary says "misuse". |
| **malfunction** | defined | "The failure of a system to operate as intended by its developer or user, resulting in incorrect or harmful outputs or operational disruptions." (md 2386) |
| **marginal risk** | defined | "The extent to which the deployment or release of a model counterfactually increases risk beyond that already posed by existing models or other technologies." (md 2394). The report adds that small marginal increases "can compound over time into substantial increases in total risk" (md 2077). |
| **risk threshold / tier / level** | defined (threshold), used (tier, level) | "A quantitative or qualitative limit that distinguishes acceptable from unacceptable risks and triggers specific risk management actions when exceeded." (md 2488). Table 3.2 adds: "For general-purpose AI, they are determined by a combination of capabilities, impact, compute, reach, and other factors" (md 1696). "Capability threshold", used 9 times, is **undefined** in IASR's own voice. Developers' tier words (ASL, High/Critical, CCL, MR1–5) are **reported, not adopted** (Table 3.5, md 1787–1802). |
| **risk tolerance** | defined | "The level of risk that an individual or organisation is willing to take on." (md 2490). It notes that companies may express it as marginal risk (md 1697). |
| **capabilities** | defined | "The tasks or functions that something (e.g. a human or an AI system) can perform, and how competently it can perform them, in specific conditions." (md 2248). This is the report's root driver of risk. Loss-of-control capabilities are "defined purely in terms of an AI system's observable outputs and their effects" (md 1275). |
| **propensity** | used but undefined | Used 13 times. It carries the definitions of alignment and misalignment and the second loss-of-control factor ("Harmful propensity: AI systems must exhibit a propensity to actually leverage these capabilities", md 1252). |
| **incident / event** | used but undefined | "Incident" is used ~45 times, as documented cases, usually in database counts. Only **incident reporting** is defined: "Documenting and sharing cases where an AI system has failed or been misused in a potentially harmful way during development or deployment." (md 2362). "Serious incident" appears only in describing the EU Code (md 1816, 2168). "Harm event" appears only as a figure label in the defence-in-depth diagram (ES 1112; KU2 ~322–333). |
| **loss of control** | defined, two wordings | Glossary: "A scenario in which one or more general-purpose AI systems come to operate outside of anyone's control, with no clear path to regaining control." (md 2382; also md 426). The section body instead says "regaining control is either extremely costly or impossible" (md 1237, 1244). The section covers *active* loss of control, distinct from *passive* ("over-reliance on AI for decision-making", md 1258). |
| **control** | defined, two senses | Glossary: "The ability to influence the behaviour of a system in a desired way. This includes adjusting or halting its behaviour if the system acts in unwanted ways." (md 2274). 2025: "The ability to exercise oversight over an AI system and adjust or halt its behaviour" (2025 5033); KU1 adds "post-training" (KU1 1211). In risk management, "controls" means countermeasures: "implementing controls and countermeasures to reduce identified risks" (md 1717); "access controls". |
| **safeguard** | defined | "A protective measure intended to prevent an AI system from causing harm." (md 2494). It is used mostly for **technical** measures on a model or system (Ch.3.3); "technical safeguards" is the chapter's term. |
| **mitigation** | inline | "Risk mitigation is the process of prioritising, evaluating, and implementing controls and countermeasures to reduce identified risks." (md 1717). Every 2026 risk section has a "Mitigations" subsection, covering technical, organisational and societal measures. |
| **defence-in-depth** | defined | "A strategy that involves implementing multiple layers of independent safeguards, such that if one measure fails, others remain in place to prevent harm." (md 2300). 2025: layering "in cases where no single existing method can provide safety" (2025 7958–7959). |
| **resilience** | defined, drifted | Glossary: "The ability of societal systems to absorb, adapt to, and recover from shocks and harms." (md 2476). The body lists four functions, adding **resist**: "resist, absorb, recover from, and adapt to" (md 2083, 2089). |
| **risk management** | defined | "The systematic process of identifying, evaluating, mitigating, and governing risks." (md 2484). 2025: "identifying, evaluating, mitigating and **monitoring**" (2025 7956–7957). |
| **developer** | defined | "AI developer: Any organisation that designs, builds, or adapts AI models or systems." (md 2206). 2025: "designs, builds, integrates, adapts or combines" (2025 1420). |
| **deployer** | used but undefined | Used 19 times; in neither glossary. |
| **provider** | used but undefined | Used for compute, cloud, inference and hosting providers (md 1836), not in the EU AI Act's legal sense. |
| **deployment environment** | defined | "The combination of an AI system's use case and the technical and institutional context in which it operates." (md 2306). It decomposes into criticality / access / permissions (md 1339–1341). |
| **alignment / misalignment** | defined | Alignment: "The propensity of an AI model or system to use its capabilities in line with human intentions, values, or norms. Depending on the context, this can refer to the intentions and values of various entities, such as developers, users, specific communities, or society as a whole." (md 2222). Misalignment is the converse (md 2398). In the body, misalignment is also "goals that conflict" (md 1240, 1325). 2025 included "operators" and omitted "norms" (2025 10930). |
| **safety (of an AI system)** | defined | "The property of an AI system being unlikely to cause harm, whether through malicious misuse or system malfunctions." (md 2500). 2025: "The property of avoiding harmful outputs…" (2025 11395). |
| **evidence dilemma** | defined | "The challenge that policymakers face when making decisions about a new technology before there is strong scientific evidence about its benefits or risks, forcing them to weigh the risk of creating ineffective or unnecessary regulations against the risk of allowing serious harms to occur without adequate safeguards." (md 2326) |
| **general-purpose AI / frontier AI** | defined | General-purpose AI: "AI models or systems that can perform a variety of tasks, rather than being specialised for one specific function or domain." (md 2340). Frontier AI: "A term sometimes used … For the purposes of this Report, frontier AI can be thought of as particularly capable general-purpose AI." (md 2336) |
| **Frontier AI Safety Framework / if-then commitments** | defined | Framework: "A set of protocols created by an AI developer, typically structured as if-then commitments, that specifies safety or security measures that they will take when their AI systems reach predefined thresholds." (md 2338). If-then commitments: "Conditional agreements, frameworks, or regulations that specify actions or obligations to be carried out when certain predefined conditions are met." (md 2360) |
| **vulnerability / threat modelling** | defined | Vulnerability: "A weakness or flaw in a system that could be exploited by a malicious actor to cause harm." (md 2546). Threat modelling: md 2532. |
| **situational awareness / sandbagging / reward hacking** | inline; sandbagging defined | Situational awareness: "The ability of an AI system to access and use information about itself, the processes by which it can be modified, or the context in which it is deployed (e.g. knowing that it is being tested)" (md 1269). Sandbagging: md 2502. Reward hacking: "when a model finds unintended shortcuts that score well on training or evaluation objectives without fulfilling the intended goal" (md 1287). |

## 1. What it names

**The object is general-purpose AI, not AI in general.**
- The 2026 scope: "'general-purpose AI': AI models and systems capable of performing a wide variety of tasks across different contexts" (md 360).
- 2025 builds the definition carefully. "An AI model is a general-purpose AI model if it can perform, or can be adapted to perform, a wide variety of tasks … An AI system is a general-purpose AI system if it is based on a general-purpose AI model" (2025 1274–1277).
- It separates this from AGI: "General-purpose AI is not to be confused with 'artificial general intelligence' (AGI)" (2025 1296).
- Biomolecular structure predictors count as general-purpose because they "can be adapted for a variety of tasks" (md 521).

**The focus is "emerging risks".**
- 2026: "risks that arise at the frontier of AI capabilities" (md 362). It ties this to the Bletchley Declaration.
- The justification is epistemic: "Because the evidence dilemma is most acute where scientific understanding is thinnest, this Report focuses on 'emerging risks'" (md 462).

**Core risk vocabulary.**
- **Risk:** "The combination of the probability and severity of a harm" (md 2480). 2025 added "that arises from the development, deployment, or use of AI" (2025 7952–7953).
- **Hazard:** "Any event or activity that has the potential to cause harm" (md 2354).
- **Risk factors:** "Properties or conditions that can increase the likelihood or severity of harm" (md 2482).
- **Marginal risk:** "The extent to which the deployment or release of a model counterfactually increases risk beyond that already posed by existing models or other technologies" (md 2394).

**Harms vs risks.** The report consistently separates *materialised* harms from *possible* risks.
- 2025: "Several harms from general-purpose AI are already well established … As general-purpose AI becomes more capable, evidence of additional risks is gradually emerging" (2025 584, 591–592).
- 2026: "Some of these risks are already materialising, with documented harms; others remain more uncertain but could be severe if they materialise" (md 394).

## 2. The taxonomy

**The three categories**, stated identically in spirit in both editions:
- 2025: "This report classifies general-purpose AI risks into three categories: malicious use risks; risks from malfunctions; and systemic risks. Each of these categories contains risks that have already materialised as well as risks that might materialise in the next few years" (2025 795–797).
- 2026: "(1) Risks from misuse, where actors deliberately use AI systems to cause harm; (2) Risks from malfunctions, where AI systems fail or behave in unexpected and harmful ways; and (3) Systemic risks, which arise from widespread deployment across society and the economy. These categories are not exhaustive or mutually exclusive – risks may cut across multiple categories – but they provide a structured way to analyse different mechanisms of harm" (md 834).

The categories are **mechanism-of-harm** categories:
- **Malicious use** is defined by intent: deliberate.
- **Malfunctions** by failure: unintended.
- **Systemic risks** by scale of deployment. They are not caused by a single model's capability.

**Systemic risk is defined against the EU AI Act, explicitly.**
- 2026: "Note that the EU AI Act uses the term differently, to refer to risks from general-purpose AI models that pose 'risks of large-scale harm'" (md 487).
- 2025 took its definition from the literature: "'broader societal risks associated with AI deployment, beyond the capabilities of individual models'" (2025 5509–5512).
- The 2026 glossary gives a third wording: risks "that arise from how AI development and deployment changes human behaviour, organisational practices, or societal structures, rather than directly from AI capabilities" (md 2522).

**The risk list shrank and shifted between editions:**

| 2025 (Ch.2) | 2026 (Ch.2) |
|---|---|
| **Malicious use:** harm to individuals through fake content · manipulation of public opinion · cyber offence · biological & chemical attacks | **Malicious use:** AI-generated content & criminal activity · influence & manipulation · cyberattacks · biological & chemical risks |
| **Malfunctions:** reliability · **bias** · loss of control | **Malfunctions:** reliability · loss of control |
| **Systemic:** labour market · global R&D divide · market concentration & single points of failure · environment · privacy · copyright | **Systemic:** labour market · **human autonomy** (new) |
| §2.4 **open-weight models**, as a factor affecting all risks | Open-weight moved to Ch.3.4, as a risk-management challenge. Single points of failure moved to Ch.3.1. |

The narrowing is declared: "this focus makes the scope of this Report narrower than that of the 2025 Report, which also addressed issues such as bias, environmental impacts, privacy, and copyright" (md 366). The 2025 chapters were not refuted. They moved out of scope, and the report points to other bodies (the UN Independent International Scientific Panel on AI) for "broader concerns" (md 362).

## 3. How it relates things

**The master structure is three questions.** It is an argument order, not a causal model:
- "What can general-purpose AI do today, and how might its capabilities change? … What emerging risks does general-purpose AI pose? … What risk management approaches exist, and how effective are they?" (md 480–485).

**The implicit causal story is short.**
- Capabilities drive risks: "What AI can do is a key contributor to many of the risks it poses" (2025 714).
- The same capabilities are dual-use: "the same capabilities that make these systems useful also create new risks. Systems that write functional code also help create malware" (md 452).
- Impact then depends on deployment and response: "The social impact of a given level of AI capabilities also depends on how and where systems are deployed, how they are used, and how different actors respond" (md 2190).

The report never draws risks as a network. Interactions between risks appear as cross-references in prose. Examples: manipulation in the service of loss of control (md 926), and skill erosion undermining oversight (md 1515).

**Where it decomposes, it uses one of four shapes:**

1. **Necessary-condition factors (loss of control).**
   - 2026: "This section examines three factors that would need to be present for such scenarios to occur: whether AI systems will develop capabilities that could significantly undermine human control; whether they develop a propensity to use such capabilities harmfully; and whether they are deployed in environments that provide opportunities to do so" (md 1244; the list is at 1250–1254).
   - The environment is decomposed further into **criticality, access and permissions** (md 1339–1341).
   - 2025 had two factors, with deployment context as a parenthesis: "1. Future capabilities … 2. Use of capabilities" (2025 5129–5137). It also had a 2×2 taxonomy: active/passive, and intentional/unintentional (2025 5102–5126).

2. **Process stages.**
   - The cyberattack chain (md 992–996).
   - Bioweapon development stages, each tagged GPAI or biological tool (md 1111).
   - The AI development lifecycle (md 548–557): data → pre-training → post-training → system integration → deployment → post-deployment monitoring. The report uses it to locate where policy levers act (md 546).

3. **Challenge categories.** "10 challenges across the following four categories: gaps in scientific understanding; information asymmetries; market failures; and institutional design and coordination challenges" (md 1540). These are explicitly *why* the evidence dilemma arises (md 1542).

4. **A layered-defence matrix.**
   - Defence-in-depth runs through training, deployment, post-deployment monitoring and societal resilience (the Swiss cheese figure; md 1737–1741).
   - Resilience is a risk × function matrix: Resist, Absorb, Recover, Adapt (md 2097–2118).
   - Defence-in-depth has a stated limit: it "primarily address[es] risks related to accidents, malfunction, and malicious use, and may play less of a role in managing systemic risks" (md 1737).

## 4. Grading: defined, but declined

**The report defines risk as probability × severity but does not score any risk.**
- It says so about its own list: "inclusion here does not necessarily imply a risk is likely, severe, or requires policy action. The evidence base varies considerably across sections" (md 836).
- It holds the field to the same standard: "no quantitative risk estimation or guarantees that are available in other safety-critical domains" (2025 984–986). Frameworks "typically do not use explicit quantitative risk thresholds" (md 1806).

**What it does instead:**
- **Two-dimensional characterisation in prose.** "Loss of control can therefore be understood as a risk with uncertain likelihood but potentially extreme severity" (md 1246).
- **Evidence-maturity ordering.** "Some risks, such as harms from AI-generated media or cybersecurity vulnerabilities, now have robust empirical evidence. Evidence for others … relies on modelling exercises, laboratory studies under controlled conditions, and theoretical analysis" (md 464).
- **Graded attribution, once.** Table 2.3 grades AI's contribution to observed cyber-threat trends. The grades run from "AI systems are very likely to have contributed" down to "appears to be limited and is likely secondary to other factors", with verbatim threat-intelligence quotes beside each (md 1026–1033).
- **Measurements, reported and not converted into risk:**
  - task-length doubling "approximately every seven months" (md 702);
  - "outperformed 94% of domain experts" (md 1078);
  - "77% of vulnerabilities" (md 983);
  - adoption rates, persuasion effect sizes (Table 2.2, md 934–944), and the like.
- **Reported risk levels from others.** The report does not adopt developers' tier designations (ASL-3, "High capability", Critical Capability Levels). It reports them as facts about what developers did (Box 2.2, md 1087–1095; Table 3.5, md 1787–1802).

## 5. Method, and where it comes from

**Process.**
- 2026: "It undergoes a structured review process. Early drafts are reviewed by external subject-matter experts before a consolidated draft is reviewed by: an Expert Advisory Panel … a group of Senior Advisors … representatives from industry and civil society organisations" (md 370–374). The writers "consider feedback … and incorporate it where appropriate" (md 376).
- Independence: "the independent writing team jointly had full discretion over its content" (md 364).

**Evidence admission** (2025 only; not restated in 2026).
- "Not all sources used for this report are peer-reviewed. However, the report is committed to citing only high-quality sources." Six indicators follow: an original contribution; comprehensive engagement with the literature; "discusses possible objections to its claims in good faith"; describes and critiques its methods; "clearly highlights its methodological limitations"; "has been influential in the scientific community" (2025 1219–1230).
- References are flagged when industry-affiliated: published by a for-profit AI company, or more than 50% of authors so affiliated (2025 11561–11566; `[industry]` tags in the md Notes).
- Evidence cutoffs are stated: "published before 5 December 2024" (2025 1219); "published before December 2025" (md 464).

**Borrowed frameworks.**
- *Risk-management structure* comes from standards: NIST AI RMF, ISO/IEC 23894, the OECD guideposts, the SRA glossary.
  - 2026 names four components: "identifying; analysing and evaluating; mitigating; and governing risk" (md 1652). It notes that standards "use different terminology".
  - 2025 used five stages: identification, assessment, evaluation, mitigation, governance (2025 8053–8065).
- *Safety-engineering lineage* is strongest in 2025, which draws on "system safety engineering", STPA, SOTIF, safety cases, ALARP, and nuclear probabilistic risk assessment (2025 8346–8443). Its own recommendation was that "a 'system safety' approach is helpful" (2025 7935).
- *Forecasting:* scenarios are commissioned from the OECD (four scenarios, each with a historical analogue; md 746–782) and elicited forecasts from the Forecasting Research Institute (md 714, 736). Both are new in 2026 (md 474).
- *Resilience:* the four functions come from the disaster and resilience literature (md 2100).

## 6. Purpose, audience, stated force

- **Mandate.** "builds on the mandate by world leaders at the 2023 AI Safety Summit at Bletchley Park to produce an evidence base to inform critical decisions" (md 308).
- **Audience.** Policymakers first: "The aim of this work is to help policymakers navigate the 'evidence dilemma'" (md 396).
- **Force.**
  - 2026: "It does not make specific policy recommendations" (md 364); "This Report is not prescriptive about what should be done" (md 2194).
  - 2025: "highly relevant for AI policy, but not in any way prescriptive" (2025 1238–1239).
  - The risk-management chapter is declared "descriptive" (md 1648).
  - A few prescriptive sentences remain, e.g. "developers of open-weight models should not release models without evaluating risks" (md 2077).
- **Whose view.** "does not necessarily represent the views of the Chair, any particular individual in the writing or advisory groups, nor any of the governments that have supported its development. … The Chair of the Report has ultimate responsibility for it" (md 298).
  - 2025 spoke as a disagreeing collective: "We, the experts contributing to this report, continue to disagree on several questions, minor and major" (2025 444).
  - 2026 closes on convergence: "On core findings, though, there is a high degree of convergence" (md 2180).

## 7. Uncertainty and evidence

**The evidence dilemma is the report's organising idea.**
- 2026: "By acting too early, policymakers risk implementing ineffective or even harmful interventions. But waiting for conclusive evidence can leave societies vulnerable to potential risks" (md 454).
- It is a glossary term (md 2326) and recurs in chapter openings (md 1527, 1542).
- 2025 grounded it in a trade-off: "implementing pre-emptive or early mitigation measures might prove unnecessary, but waiting for conclusive evidence could leave society vulnerable to risks that emerge rapidly" (2025 1043–1045).

**Five other devices:**
- **Evidence gaps as a required section** in every 2026 risk section. The conclusion lists the recurring ones and says: "Together, these gaps define the limits of what any current assessment can confidently claim" (md 2188).
- **Disagreement reported as the finding.**
  - "Expert opinion on the likelihood of loss of control varies greatly" (md 1238).
  - "Economists disagree on the magnitude of future impacts" (md 1375).
  - The 2025 capabilities outlook: "could advance slowly, rapidly, or extremely rapidly. Both expert opinions and available evidence support each of these trajectories" (2025 2230–2232).
- **Scenarios instead of forecasts.** "four broad classes of scenarios are all plausible by 2030" (md 748). Beyond 2030 is "even harder to forecast" (md 680).
- **The "evaluation gap"** as a structural limit on evidence: "performance on pre-deployment tests does not reliably predict real-world utility or risk" (md 436). It is sharpened in 2026 by models detecting tests (md 387).
- **No calibrated likelihood language of its own.** Hedges are prose: "likely", "may", "remains uncertain", "one study / several studies / a large number of studies". The only calibrated statement in the family is quoted from the UK NCSC (KU1 992–996).

**Temporal stratification.**
- Every 2026 section has an "Updates since the 2025 Report" subsection.
- 2025 had "Since the publication of the Interim Report" boxes.
- 2025 also has a Chair's note, dated after the evidence cutoff, telling the reader to discount the whole report: "the risk assessments in this report should be read with the understanding that AI has gained capabilities since the report was written" (2025 542–544).
- The two Key Updates (Oct and Nov 2025) are interim deltas: KU1 on capabilities and risk implications, KU2 on risk management.

## 8. What it excludes

- **Narrow AI**, though its evidence is used where relevant (2025 1302–1306).
- **Military AI, including LAWS:** "covered in other fora" (2025 1320–1321).
- **Benefits, as a subject of assessment:** "the current and potential future benefits of general-purpose AI – although they are vast – are beyond this report's scope" (2025 689–690). 2026 acknowledges benefits (md 398) but keeps the focus on risk.
- **How regulation affects the pace of development** (2025 782–786).
- **Policy recommendations** (§6 above).
- **From 2026:** bias, environmental impacts, privacy and copyright (md 366), and broader human-rights impacts generally, left to the UN panel (md 362). Chapter 2 is also "not an exhaustive survey of AI risks" (md 836).
- **Nuclear and radiological** are mostly out of the weapons discussion, with the reason given: barriers to materials (2025 4014–4016).

## 9. What changed from 2025 to 2026

1. **Scope.** Narrowed from "general-purpose AI safety" to "emerging risks at the frontier". Six systemic and fairness-type sections dropped. Human autonomy and societal resilience added.
2. **Loss of control.** Went from two factors with a theory-heavy argument to three factors with evaluation-observable vocabulary.
   - 2025 used "control-undermining capabilities", "deceptive alignment" and "scheming", plus a presentation of mathematical power-seeking results, with its limits.
   - 2026 uses "propensity", "situational awareness", "sandbagging" and "reward hacking".
   - The new concern is that models "distinguish between test settings and real-world deployment", so "dangerous capabilities could go undetected before deployment" (md 387).
3. **Risk management.** Widened from "Technical approaches to risk management" (the 2025 chapter title) to technical plus institutional plus societal resilience. Frontier AI Safety Frameworks became a surveyed object: 12 companies, tabulated (md 1787–1802). Defence-in-depth moved from one practice among many to the organising frame.
4. **Structure.** Went from per-section **Key Definitions** boxes (24 in 2025) to one glossary plus a fixed section template, with Updates / Evidence gaps / Mitigations / Challenges in every risk section. In 2025, mitigations sat mainly in Chapter 3. In 2026 each risk carries its own.
5. **Forecasting.** Went from a slow / rapid / extremely rapid trichotomy to commissioned OECD scenarios and FRI probability elicitations.
6. **Voice and force.** Went from a first-person disagreeing collective with more normative sentences ("It is critical…", "cannot be left in the hands of the scientific community alone", 2025 7984, 8033) to a third-person, more consistently descriptive report that claims convergence on core findings.
7. **Definitions drifted.** Examples: risk, systemic risk, developer, control, alignment, safety, AI agent. See the atlas, "Across the editions" §3. Inside 2026 there are two formulations of loss of control and two of systemic risk.

## Closing note: against Joseph's chain

*Sources and causes → preventions and controls → risk-events × impact-radius → mitigations and recovery → policies.*

- **IASR's causes node is almost entirely capability.**
  - Actors, incentives and deployment choices enter as modifiers: competitive pressure (md 1596–1600), deployment environment (md 1333–1345), market failures (md 1592–1604).
  - They are not first-class causes, except in the loss-of-control factor model.
- **It has no event layer.** Incidents appear as evidence *for* risks: counts from incident databases, single cases reported by developers. They are not the pivot of the model. The closest thing to a bow-tie is the defence-in-depth figure, which runs from threats through layers to a "Harm event" (ES 1105–1120; KU2 322–333).
- **Its impact radius is thin.** Harmed groups appear case by case: women and girls (md 878), junior workers (md 1397), vulnerable users (md 1493). There is no degree or scale structure.
- **Preventions and mitigations/recovery are separated only in 2026,** and only in the resilience taxonomy: Resist is prevention; Absorb, Recover and Adapt come after the shock.
- **Policies are deliberately absent as recommendations.** What stands in their place is "Challenges for policymakers", a list of trade-offs.

So IASR's model is best read as a **capability-indexed risk register with an evidence-maturity overlay**, not a causal model. Its most distinctive structural contributions are:
- the evidence dilemma;
- the mandatory evidence-gap slot;
- the loss-of-control factor model;
- the defence-in-depth and resilience layering.
