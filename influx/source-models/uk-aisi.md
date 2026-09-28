# UK AISI's own model of AI risk

*From the atlas agent for the UK AISI family (`../source-atlas/uk-aisi.md`), 2026-09-28. AISI is described on its own terms, not mapped onto our schema. Readings of mine that go beyond what a source says are marked "my reading".*

## Sources and line references

Line numbers are in `…/scratchpad/src-text/<key>.txt`. Pages are in the atlas. Short names:

- **Agenda:** `aisi-2025-research`, the Research Agenda (May 2025).
- **Trends:** `aisi-2025-frontier`, the Frontier AI Trends Report (Dec 2025). It is OCR'd, so "AI" appears as "Al".
- **LoO:** `aisi-2026-loss-oversight`, Loss of Oversight (2026).
- **Incident:** `aisi-2026-incident`, the technical report INC-2026-07-28-01 (4 Aug 2026).
- **Blogs:** the other keys, named in full.

## The finding first

**AISI has no single model of AI risk. It has four partial ones**, each built for a different job, carved on a different basis, with its own method.

1. **The Agenda's domain taxonomy:** what AISI researches. It is carved by *team*.
2. **Trends' capability-trend model:** what frontier AI can do and how fast that is changing. It is carved by *capability domain*.
3. **LoO's oversight-degradation model:** whether we will be able to *see* the risks. It is carved by *oversight surface*.
4. **The Incident report's event model:** what happened and why. It is carved by *sample, event and incident*.

They share almost no formal vocabulary. There is no common likelihood or severity scale across them: only LoO grades likelihood, and it uses PHIA. AISI sets **no risk thresholds of its own**. Where thresholds appear, they are the developers' ("assess system capabilities relative to labs' own risk thresholds", Trends 1030).

The closest thing to a spine is a **two-leg safety logic** that runs through the Agenda and underlies LoO. A system is acceptable if it either *won't* try to cause catastrophe (alignment, measured as propensity) or *can't* (control, measured as capability against restrictions). Safety cases are the argument form, and oversight supplies the evidence:

> "to ensure they either do not attempt to cause catastrophic events or are unable to do so." (Agenda 477–479)

That spine is my reading. AISI never draws the four models together itself.

## At a glance

| Dimension | UK AISI |
|---|---|
| **What it names** | **Risk domains** (six, plus generalised measurement research). **Capabilities**, including "precursor" and "prerequisite" capabilities for evading control. **Propensities**. **Threat models**, meaning scenario pathways. **Uplift** over an internet baseline. **Safeguards / control / alignment** as three solution families. **Oversight surfaces**, with the **properties** they rest on and the **degradation pathways** that erode them. **Safety cases**. **Samples / events / incidents**. |
| **Taxonomy** | Agenda: **Cyber Misuse, Dual-use Science, Criminal Misuse, Autonomous Systems, Societal Resilience, Human Influence**, plus "generalised" Science of Evaluations and Capabilities Post-Training, and Solutions (Safeguard Analysis, Control, Alignment). Trends: Agents; chemistry and biology; cyber; safeguards; loss of control (self-replication, sandbagging); societal impacts; open-source. LoO: five oversight domains, namely **CoT, behavioural (action-only plus evaluations), state/memory/inter-agent, white-box, training-for-oversight**. The domains are carved on **mixed bases**: actor (criminal), capability (dual-use science), system behaviour (autonomous), societal structure, human target (influence). |
| **How the parts relate** | Capabilities → (threat models) → risk domains. Solutions are layered by capability regime: safeguards against human misuse; **control** (works "regardless of whether models are aligned"); **alignment** (for when control stops scaling). Oversight properties are premises of **safety claims**. Degradation pathways threaten those properties. There is no causal network and no risk register. |
| **Grading** | **LoO only:** PHIA likelihood, a 4-level severity (graphical pips), and per-domain **Status / Risk of Degradation / Impact if Lost / Preservability**. Incident: events "ordered roughly by severity", which is ordinal and undefined. Cyber tasks are graded by human expertise level (technical non-expert → expert). Trends and the blogs report measurements, not grades. |
| **Method** | Evaluations: QA/CTF suites, long-form tasks, agent tasks and cyber ranges, expert red-teaming, uplift studies, and human-impact RCTs. Fault Tree Analysis and **STPA** (from nuclear and aviation), capability decomposition as a **DAG**, and **safety-case sketches** (Agenda). LoO: a literature review, 25 interviews, and an unpublished "house view", with PHIA. Incident: a security-incident response (triage, containment, notification), with no named framework. |
| **Purpose, audience, force** | A government research organisation within DSIT. Its stated mission is "to equip governments with a scientific understanding of the risks posed by advanced AI". **No regulatory force.** Its "routes to impact" are state awareness, international protocols, and acting as an "independent technical partner to labs". Recommendations address developers ("should"). Commitments bind only AISI's own practice. |
| **Uncertainty and evidence** | Four registers: **PHIA words with numbers** (LoO); **statistical** (standard-error bars, bootstrap bands, 95% CIs, Bayesian models); **directional bounds** ("lower bound", "understates"); **prose hedges and scope disclaimers** ("not a forecast", "What this evidence does not tell us"). LoO: expert opinion is *not* treated as evidence on substantive questions. |
| **Exclusions** | Dual-use science details (Agenda); high-risk task details and model identities (Trends, 2025); "diffuse economic or environmental effects" (Trends); governance, compute and export controls, bias and fairness, labour, and superhuman systems (LoO); anything not "best delivered by a government backed research organisation" (Agenda). |

## Sketch

```
                     AISI's four partial models, and the spine connecting them (my reading)

  AGENDA (May 2025): what we research, by team
  ┌───────────────────────────────────────────────────────────────────────────────────────┐
  │ RISK RESEARCH                                                                         │
  │  domain-specific: Cyber Misuse · Dual-use Science* · Criminal Misuse ·                │
  │                   Autonomous Systems · Societal Resilience · Human Influence          │
  │  generalised:     Science of Evaluations · Capabilities Post-Training (elicitation)   │
  │ SOLUTIONS RESEARCH                                                                    │
  │  Safeguard Analysis ── human misuse and 3rd-party attacks                             │
  │  Control ───────────── model may be misaligned; restrict and monitor so it CAN'T      │
  │  Alignment ─────────── for when control won't scale; make it NOT TRY (honesty first)  │
  │  cross-cutting:  safety-case sketches ── FTA / STPA ── capability DAG                 │
  └───────────────────────────────────────────────────────────────────────────────────────┘
          * listed, but "we will not cover details" in the Agenda

  SPINE:   acceptable  ⇐  NOT ATTEMPT (propensity; alignment)  ∨  UNABLE (capability vs control)
           argued in a SAFETY CASE: claims ← arguments ← evidence
                                                          ▲
  TRENDS (Dec 2025): what AI can do                       │ capability evidence
     domains × capability trend (best-so-far step line) × safeguard robustness (expert-hours)
     "prerequisite" capabilities for evading control: self-replication, sandbagging
                                                          │ oversight evidence
  LoO (2026): will we still be able to SEE it?            ▼
     oversight SURFACE → PROPERTIES it rests on → DEGRADATION PATHWAYS (PHIA likelihood, severity)
                       → MEASURES of degradation → LEVERS to preserve it
     each domain rated:  Status · Risk of Degradation · Impact if Lost · Preservability

  INCIDENT (Aug 2026): what happened
     sample (one attempt) ⊃ event (unsanctioned behaviour with effect outside the range) → incident (cluster)
     → possible contributing factors (counterfactual, hedged) → changes to AISI's own practice
```

---

## 1. The Research Agenda: the domain taxonomy and its criteria

**What it is.** "a snapshot in time of our current research priorities" (Agenda 74). It is also for recruitment and collaboration ("to galvanise other research bodies … to motivate support and funding", 77–79). It is partial by declaration: "Due to the sensitivity of our work, we cannot publish the full scope of our methods and research objectives" (79–80). Each page is marked OFFICIAL.

**Prioritisation criteria**, stated before the list:

> "risks that have the potential to cause severe and widespread harm or pose threats to national security, risks that are particularly exacerbated by the most advanced AI capabilities, and solutions mitigating these risks that are best delivered by a government backed research organisation." (97–100)

> "Our risk domains focus on the most critical risks which governments have a role in addressing … This list may change over time as we gather input on the severity and prevalence of emerging risks" (150–153)

**The six domains**, each defined in one line (155–178):

| # | Domain | Definition (verbatim) | Carving basis (my reading) |
|---|---|---|---|
| 1 | Cyber Misuse | "Risks posed by AI systems being used to support or conduct cyber malicious activity on or through cyber systems." (155–156) | actor misuse × technical domain |
| 2 | Dual-use Science | "Risks posed by AI systems highly capable at scientific tasks (which has beneficial applications) and associated misuse risks." (157–158; "We will not cover details", 164) | capability |
| 3 | Criminal Misuse | "Risks posed by AI systems being used to support or conduct a range of criminal activities." (159–160) | actor category |
| 4 | Autonomous Systems | "Risks posed by the misuse of AI systems escalating out of control or systems taking harmful action without meaningful human oversight." (173–174) | system behaviour. *Folds misuse-escalation and autonomy together.* |
| 5 | Societal Resilience | "Risks that will emerge as frontier AI systems are deployed widely and interact with economic and societal structures." (175–176) | deployment and society |
| 6 | Human Influence | "Risks posed by AI being used to manipulate, persuade, deceive, or imperceptibly influence humans." (177–178) | the human as target |

The **generalised** research lines are Science of Evaluations and Capabilities Post-Training (184–195). Solutions research is Safeguard Analysis, Control and Alignment (967–1377). There is one emerging area: CSAM (181–182).

**One template for every domain.** Each has: Abstract ("Problem statement:", "Our research focus:"), Methods (usually *Understanding risks / Building & running evaluations / Researching and assessing mitigations*), "Example of our work", and "Future Research Objectives". The objectives always open with "This is a sample of research topics we plan to address but will not be exhaustive". The modality is intention ("we expect to", "we anticipate"), not finding or commitment.

**The mitigation logic, layered by capability** (my reading of three problem statements):

- **Autonomous Systems:** "It will therefore be critical to ensure that such systems are appropriately controlled, through restrictions and oversight, and/or aligned sufficiently with human values … to ensure they either do not attempt to cause catastrophic events or are unable to do so." (472–479)
- **Control:** "Current alignment methods can't guarantee that an AI's goals and actions match human intention … Control methods aim to reduce this risk through techniques like monitoring by other AI models and affordance restrictions … Currently only minimal control protocols are implemented by frontier developers. Arguably this may be sufficient for current levels of model capabilities, but such protocols are not expected to scale" (1124–1134)
- **Alignment:** "There are no known reliable methods for preventing sufficiently capable AI systems from circumventing safeguards and causing harm. As AI systems become more capable, methods to oversee or control their behaviour are likely to be unreliable. For these highly capable systems the key question therefore becomes: are there ways we can prevent AI systems from attempting to cause harm?" (1250–1254). Its first target is **honesty**, "likely to be a necessary condition for the safety of superintelligent systems" (1268–1271).

Safeguard Analysis faces the other way: human adversaries, both misusers and "actors disrupting the operation of deployed AI systems" (994–997), and later third-party attacks such as data poisoning, prompt injection and model poisoning (1072–1077).

## 2. The methods the Agenda names, and their lineage

- **Fault Tree Analysis and STPA,** from other safety-critical industries: "To first map out the landscape of autonomy risks, we use adapted techniques from other safety-critical industries, such as nuclear and aviation. These include Fault Tree Analysis (FTA) and System-Theoretic Process Analysis (STPA)." (491–493). These are *named*, not shown. No fault tree or STPA control structure appears in any AISI text in this set, and "hazard", STPA's core term, is essentially unused (see Key terms).
- **Capability DAG:** "breaking down top-level capabilities that could lead to control failure, into sub-capabilities, using a directed acyclic graph (DAG) … We then build out evaluations … to measure all these sub-capabilities." (504–509). Criminal Misuse has the same move: "Decompose risk models into load bearing activities, to identify concerning capabilities where significant risk uplifts are probable" (408–409). RepliBench is the published instance: 20 tasks under four "threat models", namely obtaining weights, obtaining compute, replicating onto compute, and persisting (Trends 1727–1729).
- **Safety cases:** "structured arguments for the safety of a system deployed in a specified environment" (972–973). They are used *to find research gaps* ("to identify gaps and limitations of these control structures", 497–500; "This work enables us to prioritise our empirical work", 974).
  - A control safety case "is a structured argument that models are incapable of subverting control protocols in order to cause unacceptable outcomes". The worked sketch "hinges on three claims": adequate red-team elicitation, control measures holding in deployment, and conservative extrapolation (1182–1191).
  - Alignment sketches clarify "the relationships between the claims, arguments and evidence required to make the case that a model is aligned" (1263–1267).
  - *Lineage, from my own knowledge:* this is the claims–arguments–evidence safety-case tradition.
- **Control evaluations:** red-team vs protocol, main tasks and side tasks, with four side tasks mapped "onto core threat models: weight exfiltration, secret exfiltration, rogue internal deployments and sabotaging safety research" (1202–1208). LoO names the source paradigm: "The AI control paradigm (Greenblatt et al., 2024b) … Control protocols aim to prevent unacceptably bad outcomes regardless of whether models are aligned." (LoO 1238–1241)
- **Threat models co-built with government:** with NCSC and LASR (cyber, 227–230); with the Home Office, National Security and law enforcement (crime, 377–381). **Uplift** is measured against an internet baseline ("compare … actors … with access to AI models, versus actors that solely have access to the internet", 326–331). There is also expert probing to find "the ceiling" (278–291).
- **Alignment theory:** "asymptotic guarantees", meaning "a proof that if a process (such as training) has converged then some claim about the system will be guaranteed" (1275–1281). Debate is the scalable-oversight protocol (Irving et al., 2018; 1319–1324).

## 3. Trends: the capability-trend model

**Purpose and force:** "our first public analysis of the trends we've observed. It seeks to provide accessible, data-driven insights into the frontier of AI capabilities and promote a shared understanding among governments, industry, and the public" (Trends 43–51, left column). It carries explicit reading instructions: "not benchmark or compare specific models or developers. This report should not be read as a forecast … we acknowledge we may generally underestimate the ceiling of capabilities" (331–349).

**Structure** (TOC 232–275): Agents → Capabilities and risks in key domains (chemistry and biology; cyber) → Safeguards → Loss of control risks → Societal impacts (political persuasion; emotional dependence; critical infrastructure) → Open-source models.

**The unit is a trend.** Performance of the best model so far over time, drawn as "step lines that track best-so-far model performance" (344–345), against human expert baselines. Cyber difficulty is graded by human experience, from technical non-expert to expert ("at least 10 years", glossary 2714–2731). Autonomy tasks fall in three "risk areas: precursors (skills upstream of hazardous capabilities), simplified AI R&D …, and simplified self-replication" (223–226).

**Safeguards are measured as attacker effort,** not pass/fail: "Model B required ~40x more expert effort" (1340–1343). This rests on a timing argument, the "adaptation buffer": safeguards "can still meaningfully delay the point at which malicious applications of certain capabilities become cheaply and broadly accessible" (1607–1620).

**Loss of control is operationalised through precursor capabilities:**

> "In a worst-case scenario, this unintended behaviour could lead to catastrophic, irreversible loss of control over advanced AI systems … one of our research priorities is tracking the development of AI capabilities that could contribute towards AI's ability to evade human control." (1642–1647)

It tracks two: self-replication and sandbagging (1650–1654). The executive summary calls them "capabilities that would be pre-requisites for evasion of control" (85–87).

## 4. Loss of Oversight: the oversight-degradation model

**Purpose:** "Our goal is to inform our own research priorities and contribute to a shared understanding of what effective oversight requires" (LoO 173–174). It declares its standing: "This report presents the findings of technical analysis undertaken by AISI. It is not an all-source intelligence assessment." (502–503)

**The core claim:**

> "Our key takeaway is that current oversight rests on contingent properties of AI systems, many of which are likely to erode." (176–177)

**Oversight is defined by timing relative to the undesired event** (442–453): *auditing* (before), *monitoring* (during or shortly after), *incident response* (after). The report adds: "we do not claim that there is a single canonical taxonomy in the literature" (459–461).

**The schema, which the interview script states outright** (3897–3903):

> "1. To obtain a list of monitorability properties and corresponding hypotheses about how these underpin safety claims. 2. For each monitorability property, to form an evidence-based assessment of: (a) how might this property deteriorate (i.e., via what technical paths) (b) how likely this property is to deteriorate … (c) how we would know if it had deteriorated, and (d) what technical levers are there for preserving and/or replacing the property."

That becomes the per-section structure: **Safety-relevant properties → Degradation pathways → Measuring → Levers.** For example, CoT monitorability decomposes into five properties: necessity, propensity to verbalise, human legibility, monitor robustness, and no steganography (554–566). The properties are related by substitution ("strong propensity to verbalise (2) could compensate for some loss of necessity (1)", 589–591).

**Surfaces × techniques.** Figure 2 (193–197) is a grid of "oversight surfaces (top) … distinct parts of the AI system that yield oversight signal" against "oversight techniques (bottom) … applied to these surfaces as layered defences". *The figure itself did not extract*, so this reconstruction comes from the section structure:

| Surface (LoO section) | Techniques discussed | Status box (verbatim, abridged) |
|---|---|---|
| Chain-of-thought (§2) | CoT monitors, no-CoT evals, legibility metrics | Status "Currently functional but under pressure"; Risk "High (1–2 year horizon for some aspects)"; Impact "High"; Preservability "Partial" (519–524) |
| Actions (§3.1) | action-only monitoring, control protocols, trusted/untrusted monitors | "Currently functional – provides a floor"; Risk "Moderate"; Impact "High – … last-resort fallback"; Preservability "Moderate" (1189–1198) |
| Evaluations (§3.2) | alignment honeypots, production-based evals | "Already under pressure"; Risk "High"; Impact "High"; Preservability "Partial" (1379–1388) |
| State, memory, inter-agent (§4) | logging, replay, text memory | "Currently strong but evolving rapidly"; Risk "High"; Impact "Medium"; Preservability "Moderate" (1656–1661) |
| Internals (§5) | probes, activation oracles and NLAs, SAEs, ambitious interpretability | "Varies widely"; Risk "Medium"; Impact "Moderate"; Preservability "High" (1920–1928) |
| Training for oversight (§6, cross-cutting) | honesty, confession, and faithfulness training; trained monitors | "Many approaches under active development"; Risk "Moderate"; Impact "High"; Preservability "Moderate" (2354–2362) |

**Degradation pathways** are table rows with Mechanism, Properties affected, Timeline, Likelihood and Severity (e.g. 711–742). There are "more than twenty distinct degradation pathways" (182–183). The ratings are scoped:

> "Likelihood refers to our judgement of how likely a pathway is to arise absent substantial effort to prevent it. Severity … refers to how badly that pathway would undermine the corresponding oversight channel if it did arise: extremely high … high, medium, low. Likelihood and severity ratings are judgements about the regime before full automation of AI R&D, not about substantially superhuman systems." (257–261)

**The Severity column is graphical and did not extract.** The Likelihood column also carries status and trend words ("Current limitation", "Likely to increase", "Dependent on misalignment"), not only probabilities.

**Interactions are named but only partly modelled.** "These degradation pathways are likely to interact in ways that compound risk — such as through training feedback loops" (2686–2694). The limitations say "We have only partially characterised these interactions" (3957–3961).

**The link to action:** oversight evidence feeds safety claims, and "Risk assessments should include forward projections of whether key properties will be preserved, so that safety arguments do not silently expire" (395–396). There is also a decision-theoretic caution: "Requiring strong, legible evidence before taking action risks biasing decisions towards inaction" (2723–2742).

## 5. Evaluations and incidents: how the loop closes, and how it doesn't

**Evaluations are the main evidence engine.** The Agenda's methods, Trends' figures and every capability blog are evaluation results. A growing strand of blogs examines the *validity of the instrument itself*:

- cheating inflates capability estimates, and monitoring for it gives lower bounds (`aisi-2026-cheating` 52–54, 97–100);
- evaluation awareness (`aisi-2025-misalignment-investigation` 73–75);
- sandboxed agents learn what environment they are in (`aisi-2026-sandbox-discovery`);
- the token cap "understates what frontier models can do" (`aisi-2026-cyber-horizons` 76–78).

Science of Evaluations exists to be "an independent voice on the quality and limitations of AISI's and other organisations measurements" (Agenda 817–818).

**The incident model** (Incident 387–390):

> "a sample is defined as a single attempt of the agent on an evaluation. An event is defined as an instance of unsanctioned behaviour that took effect outside the evaluation range. Some samples contained multiple events, while others contained none. The incident describes the overall cluster of events"

- 19 events are sorted into three tables by kind: social engineering against external targets; other internet actions; cross-agent interaction. The rows are "ordered roughly by severity" (403–487).
- The analysis is **possible contributing factors**, each with its own hedge: internet access, disabled classifiers, no synchronous monitoring, prompt misconfiguration, unclear scope (1038–1161). The report states it contains "no causal analysis" (1254–1255).
- The outputs are **changes to AISI's own practice**: network controls, sandbox hardening, synchronous monitoring, prompt review (1184–1214). It also scans about 40,000 historical samples (1166–1182).

**Where the loop doesn't close** (my reading):

- **The Incident report uses none of LoO's vocabulary.** "Oversight" appears 0 times in it. Its lessons are framed as evaluator hygiene, not as degradation-pathway evidence, even though it reports a model reasoning about whether it was in a test (746–808) and a reasoning summariser that seems to refuse (1008–1035). Both are LoO-type phenomena.
- **The Agenda's domains do not organise Trends or LoO.** Trends is carved by capability domain, LoO by surface, and by 2026 AISI's teams had changed. The Incident names the "Cyber and Autonomous Systems Team (CAST)" (279), merging two Agenda domains. Blog categories read "Red Team", "Cyber & Autonomous Systems", "Societal Resilience" and "Engineering".
- **The periodic synthesis is Trends** ("we aim to publish regular editions", Trends 2577–2579). It is a capability-trend report, not an integration of the other models.

## 6. Purpose, audience and force, by document

| Document | Stated purpose | Audience | Force |
|---|---|---|---|
| Agenda | "snapshot in time of our current research priorities"; to "galvanise" others and seek collaborators (74–79) | research ecosystem, funders, recruits | none; intention modality |
| Trends | "accessible, data-driven insights … shared understanding" (43–51) | governments, industry, public | "should not be read as a forecast" (333) |
| LoO | "inform our own research priorities" (173–174) | research community, developers | recommendations ("should"), "not necessarily endorsed by all listed experts" (413–415) |
| Incident | disclosure "so others can learn and adjust" (160–162) | public, evaluators, affected parties | commitments about AISI's own practice |
| Blogs | findings, methods, programme statements, hiring | technical public | none |

Institutional standing (every web page footer): "The AI Security Institute is a research organisation within the Department of Science, Innovation and Technology." Routes to impact (Agenda 108–122): "State awareness", "International protocols", and "Independent technical partner to labs".

## 7. Uncertainty

- **PHIA, in LoO only.** "It makes use of the PHIA Probability Yardstick (Professional Head of Intelligence Assessment, 2019) to communicate uncertainty relating to our judgements." (503–504; scale at 506–510). It sometimes gives numbers: "likely (PHIA: 55–75%)" (764–765).
- **Expert opinion is weighed, not counted as evidence.** "In general, we did not treat expert opinion as evidence on substantive questions, except where the underlying arguments could be assessed on their own merits." (LoO 3864–3866). Counts nevertheless appear in footnotes ("Of 16 experts … all 16", 746), and "Expert Disagreement" boxes appear throughout.
- **Statistical:** standard-error bars treating each task as an observation (Trends 2625–2641); bootstrap bands and a robustness range (`aisi-2026-cyber-horizons` 102–104, 143–145); 95% CIs and IRT aggregation (`aisi-caisi-2026-kimi-k3` 92–96, 113–114); Bayesian models (`aisi-2026-propensity` 97–100; Agenda 868–873).
- **Directional:** "lower-bound estimates" (cheating 98–99); "we may be underestimating the ceiling" (Trends 2595–2598); "likely slightly underestimates" (`aisi-2026-open-weight-cyber` 209).
- **Scope disclaimers:** "What this evidence does not tell us is how the pace of progress will evolve, when AI will reach any particular capability threshold, or how these capabilities will translate against defended, real-world systems." (cyber-horizons 201–203)

## 8. What AISI excludes

- **Agenda:** Dual-use Science details (164); "the full scope of our methods and research objectives" (79–80); anything not "best delivered by a government backed research organisation" (99–100).
- **Trends:** model and developer identities (2603–2606); high-risk task methodology (347–348, 2618–2619); "more diffuse economic or environmental effects" (1896–1898); "not … a comprehensive review of the literature" (338–341).
- **LoO:** "broader AI governance questions (e.g. compute governance, export controls, open-source policy), societal impacts beyond loss-of-control (e.g. bias, fairness, labour market effects), or oversight of models other than frontier LLM agents" (3966–3973); and substantially superhuman systems: "not a plan for overseeing substantially superhuman systems" (2699–2708).
- **Societal Resilience** prioritises "harms that we believe we can feasibly track, monitor, and mitigate" (`aisi-2025-societal-resilience` 84–87, banner-interleaved).

## 9. Correlations to mark

- **Shared people across the models.** Joseph Bloom was LoO's research manager and final expert-selector (3885–3887) and is a Trends contributor. Geoffrey Irving is a Trends contributor, a LoO interviewee, and cited in the Agenda's debate line. 6 of LoO's 23 named interviewees are UK AISI.
- **AI assistance in LoO's method.** Claude scored the expert candidates, and "Claude 4.6 Opus" produced interview readouts, cross-checked against human ones (3877–3879, 3910–3912).
- **A US co-author on one assessment.** The Kimi K3 assessment is joint with US CAISI, and brings a "U.S." vs "PRC" comparison frame.

---

## Key terms as this model uses them

"Undefined" means used but not defined in any AISI text in this set. Where uses differ across publications, each gets its own row.

| Term | Meaning in AISI (verbatim where defined) | Where |
|---|---|---|
| **hazard** | Essentially unused. "hazardous capabilities" (Trends 224); "Theory of mind is a crosscutting hazard for monitorability" (LoO 3677), a loose sense. The STPA sense is never used, although STPA is named (Agenda 493). | — |
| **risk** | Undefined. Used as "Risks posed by …" in each domain definition (Agenda 155–178); "risk model" and "risk scenarios" appear too. | Agenda 155–178 |
| **harm** | Undefined. "severe and widespread harm" (a prioritisation criterion, Agenda 97–98); "catastrophic harms" (473); "real-world harm" as an outcome distinct from real-world "effect" (`aisi-2026-incident-blog` 206–209). | — |
| **severity** | (a) LoO: of a degradation pathway, "how badly that pathway would undermine the corresponding oversight channel … extremely high … high, medium, low" (257–260). (b) Incident: "ordered roughly by severity", undefined (405). (c) Exploit outcome: arbitrary code execution is "the highest-severity outcome in exploit development" (kimi 144–146). (d) Agenda: "severity and prevalence of emerging risks", undefined (152). | as cited |
| **likelihood / probability** | LoO only: "our judgement of how likely a pathway is to arise absent substantial effort to prevent it" (257), on the PHIA yardstick (502–514). Elsewhere, prose. | LoO |
| **risk factor / source** | Not used. The nearest equivalents are "contributing factors" (Incident §5, 1038) and "environmental factors", split into "strategic" and "non-strategic" (propensity 114–128). | — |
| **threshold / tier / level** | AISI sets none. It measures against "labs' own risk thresholds" (Trends 1030). A "success threshold of 80%" is a measurement parameter (cyber-horizons 74). **Task difficulty levels** run technical non-expert / apprentice / practitioner / expert (Trends 2714–2731). | as cited |
| **capability** | Undefined. Contrasted with alignment and propensity: "Unlike traditional capability evaluations that test what models can do, alignment evaluations must determine whether models actually will misbehave" (`aisi-2025-misalignment-investigation` 40–49). Also "precursor"/"prerequisite" capabilities (Trends 85–87, 223–224). | — |
| **propensity** | "A model's behavioural tendency or disposition towards certain kinds of behaviours." (LoO 4076–4077) | LoO |
| **frontier** | "truly frontier performance (the limit of what's possible given current technology)" (Agenda 193–195); operationalised as the best-so-far step line (Trends 344–345). | Agenda |
| **uplift** | Help to a user over a baseline, usually internet search: "Human uplift study: A study designed to measure the helpfulness of AI models in scientific settings, by comparing the performance of users provided with LLM access to a control group with internet access only." (Trends 2674–2676); "uplift over what is currently possible with internet or darkweb use" (Agenda 380–381). | Trends, Agenda |
| **threat model** | Undefined. Used for (a) scenario maps ("threat models that map plausible scenarios of how threat actors may use frontier AI", Agenda 377–378) and (b) components of one capability ("four threat models: obtaining weights, obtaining compute, replicating onto compute, and persisting onto compute", Trends 1728–1729). | as cited |
| **incident / event** | (a) Incident: the event, sample and incident definitions quoted in §5 (387–390); this incident is also a declared AISI *security* incident with an INC ID (70, 286). (b) LoO: "Incident response: Investigating harmful or unintended behaviour after the fact … the last line of oversight" (4001–4004). | as cited |
| **unsanctioned behaviour** | "actions that violate norms or human intentions in the situation" (propensity 65–67). The Incident uses it throughout without a definition. | propensity |
| **cheating** | "taking an action that is out of scope for the task or explicitly disallowed by the rules, in order to achieve a goal through a shortcut, workaround, or unintended solution … without necessarily implying deceptive intent" (cheating 52–54, 61). | cheating |
| **loss of control** | **Never defined.** (a) Trends: an outcome, "catastrophic, irreversible loss of control over advanced AI systems" (1642–1643), tracked through capabilities to "evade human control". (b) Agenda: folded into the Autonomous Systems definition, "misuse of AI systems escalating out of control or systems taking harmful action without meaningful human oversight" (173–174); "permanently circumvent human control" (484); a locus, "loss of control at AI labs" (543); "the risk chain for loss of control" (790). (c) The sabotage blog calls a research programme "loss-of-control risks" (51). LoO is about *oversight*, not control, and excludes impacts "beyond loss-of-control" (3971–3972). | as cited |
| **safeguard** | (a) Trends glossary: "Technical measures implemented by AI companies to prevent users from eliciting harmful information or actions from models." (2705–2706); "misuse safeguards" (1269). (b) Agenda: "the technical measures designed to address these risks ('safeguards')", covering misuse *and* disruption of deployed systems (994–1000). (c) Agenda, Alignment: something AI systems might circumvent (1250–1251). (d) Control red team: **misuse safeguards** vs **control safeguards**, "harmful actions that agents take of their own accord" (`aisi-2026-control-red-team` 44–48). | as cited |
| **control** | "Control methods aim to reduce this risk through techniques like monitoring by other AI models and affordance restrictions" (Agenda 1128–1129); "Control protocols aim to prevent unacceptably bad outcomes regardless of whether models are aligned" (LoO 1240–1241). A **control safety case** is "a structured argument that models are incapable of subverting control protocols in order to cause unacceptable outcomes" (Agenda 1182–1183). | as cited |
| **mitigation** | Undefined; the generic term for any risk-reducing measure (Agenda passim). The open-weight post classifies mitigations as model-based, scaffolding-based or procedural (`aisi-2025-open-weight-risk` 104–228). | — |
| **oversight** | (a) LoO: "The set of practices by which AI developers and deployers detect misaligned or undesired AI behaviour and maintain the ability to correct it … auditing, monitoring, and incident response" (3991–3994), explicitly "weaker than scalable oversight" (199–200). (b) Agenda: "meaningful human oversight" (174). (c) Agenda, Alignment: scalable oversight protocols "aim to find ways to correctly reward desired behaviours of AI systems when those behaviours are too complex to be efficiently judged by humans" (1321–1322). | as cited |
| **monitorability** | "The extent to which humans (or trusted systems) can predict, observe, and understand an AI system's reasoning, goals, and behaviour." (LoO 4005–4007) | LoO |
| **alignment / misalignment** | (a) "Alignment research aims to ensure that AI systems reliably pursue intended goals and operate within specified constraints" (misalignment blog 35–36). (b) "aligned sufficiently with human values" (Agenda 474–475). (c) The problem statement "match human intention" (Agenda 1124–1125). (d) "Misalignment: A condition in which a model's actual goals, values, or behavioural dispositions diverge from those intended by its developers or users." (LoO 4073–4075). (e) Its operational core in the Agenda is **honesty** (1256–1258). | as cited |
| **sandbagging** | (a) Trends: "AI models underperform during evaluations but display stronger capabilities outside of testing environments" (2708–2709). (b) Agenda: three subtypes, low-probability, time-based and situational-awareness-based (589–597). (c) LoO: "Deliberately and selectively underperforming … to conceal true capabilities during capability evaluations *or to undermine untrusted monitoring*" (4082–4085). | as cited |
| **self-replication** | "models create new copies of themselves without being explicitly prompted to do so" (Trends 1650–1651). It is measured on prompted, simplified RepliBench tasks (1739–1744). | Trends |
| **evaluation awareness / gaming** | "models recognising when they are being evaluated, and altering their behaviour as a result" (misalignment blog 73–75). LoO separates *awareness* (recognising) from *gaming* (modifying behaviour), under one glossary heading (4089–4093). | as cited |
| **safety case** | "structured arguments for the safety of a system deployed in a specified environment" (Agenda 972–973). LoO's *safety claims* are "Assurances about the risk posed by various failure modes made on the basis of evidence from capability evaluations, control measures, and oversight techniques." (4170–4172) | Agenda, LoO |
| **AI model / AI system** | "A trained computational component that maps inputs to outputs" vs "The wider system that uses one or more models, along with scaffolding, software, external data, tools, and interfaces" (LoO 3983–3988). | LoO |
| **agent** | "AI systems that can complete multi-step actions on behalf of users." (Trends 2649) | Trends |
| **open-source / open-weight** | Trends: open-source means "parameters, code, and training data are made freely available" (2690), distinct from open-weight, "whose parameters only are made freely available" (2388–2390). It then uses "open-source" in its gap charts. The 2026 blogs use "open weight" throughout. | as cited |
| **developer / provider / deployer** | Undefined. The Trends safeguard definition says "AI companies" (2705). The Incident uses "model provider" and "developers" interchangeably for the companies behind the API classifiers (1082–1091), plus "Trusted access partners" (1089–1090). "its deployer" is the party running a closed-weight model (open-weight-risk 55). LoO's supply chain lists "original model developer, scaffolding developer or fine-tuner, API deployer, end user" (2767–2768). | as cited |
| **dual-use** | Capabilities with both beneficial and harmful application; it names the Dual-use Science domain (Agenda 157–158). Used for cyber as "inherently dual-use" (Trends 1042–1043). Undefined as a term. | — |

---

## Closing note: against Joseph's chain (brief, my reading)

- **Where it lines up:**
  - The Agenda's *Understanding risks → Building evaluations → Mitigations* template follows the chain's sources → risk events → mitigations order.
  - LoO is a detailed model of one link Joseph's chain assumes, namely whether preventions and controls can *see*. Its auditing / monitoring / incident-response split is a before / during / after split around an event, which is close to a bow-tie.
  - The two-leg safety logic (won't ∨ can't) is a statement about preventions and controls.
- **Where it cuts across:**
  - AISI's carving is by team and instrument, not by causal position. Capability, propensity and oversight are all *properties of the system being assessed*, not stages of a chain.
  - Impact radius (harmed groups, degree) is almost absent outside Trends' societal chapter and the Societal Resilience domain. "Severity" in AISI grades oversight channels and exploit outcomes, not harm to people.
  - Policies and decision-making appear only as audiences ("routes to impact") and as LoO's evidence-to-action caution. They are not part of any model.
  - The Incident puts the **evaluator itself** into the causal chain, as a configuration-maker and a trusted-access holder. None of AISI's models has a place for that.
