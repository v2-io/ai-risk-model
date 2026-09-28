# NIST's model of AI risk: AI RMF 1.0 and the Generative AI Profile (AI 600-1)

*Written by the us-gov atlas agent, 2026-09-28. Line references are to `scratchpad/src-text/<key>.txt`. RMF = `nist-2023-ai-rmf` (NIST AI 100-1, Jan 2023). 600-1 = `nationalinstituteofstandardsandtechnologyus-2024-artificial` (NIST AI 600-1, Jul 2024). In the 600-1 extraction the letters "fi" and "ff" are single ligature glyphs, so a search for "define" will miss "deﬁne"; quotes below restore the letters. The lifecycle figures are images and don't appear in the text, so I rendered RMF PDF pages 15–16 to read them. Where I say "my count" or "my reading", that is me, not NIST.*

## At a glance

| Dimension | AI RMF 1.0 + AI 600-1 |
|---|---|
| **What it models** | Not the risks. It models **the organisational activity of managing risk**. The unit is an *outcome an organisation should have in place* ("Legal and regulatory requirements involving AI are understood, managed, and documented"). The RMF itself names almost no specific risks. The 600-1 profile supplies 12 for generative AI. |
| **Main kinds** | AI system. **AI actors**, defined by the *tasks* they perform. Lifecycle stages × socio-technical dimensions. 7 **trustworthiness characteristics**. Risk / impact / harm. Risk tolerance, prioritisation, residual risk. In 600-1: 12 **GAI risks**, and 4 dimensions along which risk varies (lifecycle stage, scope, source, time scale). |
| **Structure** | The **Core**: 4 functions (GOVERN, MAP, MEASURE, MANAGE) → 19 categories → 72 subcategories (my count). **Profiles** instantiate the Core for a use case, a sector, a technology, or a current vs target state. 600-1 is a cross-sectoral profile of about 210 suggested actions keyed to 49 of the 72 subcategories, each tagged with GAI risks and AI actor tasks (my count). |
| **Grading** | Risk is defined as probability × magnitude. After that it is **deliberately ungraded**. There is no scale, no levels, and no thresholds. Tolerance is "not prescribed". Metrics and threshold values are left to "human judgment". The one bright line: at "unacceptable negative risk levels" development and deployment "should cease in a safe manner". |
| **Method / lineage** | ISO 31000 risk management. Definitions from ISO Guide 73, ISO/IEC TS 5723, ISO 9000, ISO/IEC 22989, and OECD (AI system, AI actors, the lifecycle classification). The function → category → subcategory Core shape of NIST's cybersecurity and privacy frameworks. Made by consensus: an RFI, workshops, a concept paper and two drafts (the RMF); a public working group (600-1). |
| **Purpose / audience / force** | "Voluntary, rights-preserving, non-sector-specific, and use-case agnostic"; "law- and regulation-agnostic". Audience: organisations and "AI actors" across the lifecycle. A living document, with formal review "no later than 2028". Since July 2025 it has been under an Administration order to be revised. |
| **Uncertainty / evidence** | The RMF treats measurement difficulty as a named challenge: "inability to appropriately measure AI risks does not imply" high or low risk. **600-1 includes only risks with "an existing empirical evidence base"**, and excludes "speculative risks" of future systems. |
| **Excludes** | Risk-tolerance setting; templates; any checklist or ordering; any catalogue of AI-specific failure modes (RMF); speculative or future-system risks (600-1). The words **"hazard" and "loss of control" appear in neither document**. "Catastrophic" appears once, in the RMF, and never in 600-1. |

---

## 1. The central move: risk management as organisational outcomes

The RMF is a framework for *organisations*, not a theory of *AI risk*. Its operative content is a catalogue of outcomes:

> "The AI RMF Core provides outcomes and actions that enable dialogue, understanding, and activities to manage AI risks and responsibly develop trustworthy AI systems. … Each of these high-level functions is broken down into categories and subcategories. Categories and subcategories are subdivided into specific actions and outcomes. Actions do not constitute a checklist, nor are they necessarily an ordered set of steps." (RMF 937–942)

> "Be outcome-focused and non-prescriptive. The Framework should provide a catalog of outcomes and approaches rather than prescribe one-size-fits-all requirements." (RMF 1930–1931, Appendix D)

The content of any particular risk (what could go wrong, to whom, how likely) is something the user *produces* by performing the MAP and MEASURE functions. The framework does not supply it. This is the single most important fact for comparing it with other sources. **The RMF's schema is a schema of management activities and system properties. Risks are an output of using it, not an input to it.** AI 600-1 is where NIST does fill in content, for one technology.

## 2. The kinds of things it names

### 2.1 AI system, risk, impact, harm

- **AI system**: "an engineered or machine-based system that can, for a given set of objectives, generate outputs such as predictions, recommendations, or decisions influencing real or virtual environments. AI systems are designed to operate with varying levels of autonomy (Adapted from: OECD Recommendation on AI:2019; ISO / IEC 22989:2022)." (RMF 142–146)
- **Risk**: "the composite measure of an event's probability of occurring and the magnitude or degree of the consequences of the corresponding event. The impacts, or consequences, of AI systems can be positive, negative, or both and can result in opportunities or threats (Adapted from: ISO 31000:2018)." For negative events, risk is "a function of 1) the negative impact, or magnitude of harm, … and 2) the likelihood of occurrence (Adapted from: OMB Circular A-130:2016)." (RMF 272–278)
- **Who can be harmed**: "individuals, groups, communities, organizations, society, the environment, and the planet" (RMF 278–280). The same list recurs as MAP 5's impact targets (1275–1280). This is a *scale-ordered harm radius*, though it is never called one.
- **Risk management**: "coordinated activities to direct and control an organization with regard to risk" (ISO 31000, RMF 282–283).
- Risk explicitly includes **positive** impacts. The framework "offers approaches to minimize anticipated negative impacts … and identify opportunities to maximize positive impacts" (RMF 285–287). MAP 3.1 and 3.2 document benefits and costs.

### 2.2 Lifecycle × dimensions (Figures 2 and 3, images)

Figure 2 (adapted from the OECD classification framework) has two rings, verified from the rendered page:
- **Inner ring: dimensions.** Application Context, Data & Input, AI Model, Task & Output, with **People & Planet** at the centre.
- **Outer ring: lifecycle stages.** Plan and Design → Collect and Process Data → Build and Use Model → Verify and Validate → Deploy and Use → Operate and Monitor.

Figure 3 lays the stages out as columns, adds a seventh, **"Use or Impacted by"** (under People & Planet), and gives each column rows for its *TEVV* activity, its *Activities* and its *Representative Actors*. NIST's modification of the OECD scheme "highlights the importance of test, evaluation, verification, and validation (TEVV) processes throughout an AI lifecycle" (RMF 514–516).

### 2.3 AI actors, defined by task (Appendix A)

- **AI actors**: "those who play an active role in the AI system lifecycle, including organizations and individuals that deploy or operate AI" (OECD, RMF 203–206).
- Appendix A (1584–1712) defines **task categories**, not organisations:
  - AI Design;
  - AI Development;
  - AI Deployment;
  - Operation and Monitoring;
  - TEVV;
  - Human Factors;
  - Domain Expert;
  - AI Impact Assessment;
  - Procurement;
  - Governance and Oversight.
- It adds "Additional AI Actors": Third-party entities, End users, Affected individuals/communities, Other AI actors (standards bodies, advocacy groups, and so on), and the General public.
- Each task category lists the actors who typically do it. A single job title appears under several: "developers" under Development (1602), "software developers" under Deployment (1611), "product developers" under Operation and Monitoring (1619).
- There is one structural rule: "AI actors carrying out verification and validation tasks are distinct from those who perform test and evaluation actions" (1625–1631). Figure 3's caption says model builders and users are "separated as a best practice … from those verifying and validating the models" (573–574).
- The People & Planet actors "comprise a separate AI RMF audience who informs the primary audience" (532–534). They provide context and norms, and "designate boundaries for AI operation" (550–558).

### 2.4 Trustworthiness characteristics (Section 3)

Seven characteristics:
- valid and reliable;
- safe;
- secure and resilient;
- accountable and transparent;
- explainable and interpretable;
- privacy-enhanced;
- fair with harmful bias managed.

They are related, not just listed: "Valid & Reliable is a necessary condition of trustworthiness and is shown as the base for other trustworthiness characteristics. Accountable & Transparent is shown as a vertical box because it relates to all other characteristics" (594–596). And: "trustworthiness is a social concept that ranges across a spectrum and is only as strong as its weakest characteristics" (609–610).

Their definitions are mostly imported. Validation comes from ISO 9000:2015 (655–657). Reliability, accuracy and robustness come from ISO/IEC TS 5723:2022 (661–690). Safe is "not under defined conditions, lead to a state in which human life, health, property, or the environment is endangered" (701–702). Resilient is adapted from 5723 (732–736).

The framework names tradeoffs among the characteristics but **declines to resolve them**: "These analyses can highlight the existence and extent of tradeoffs … but they do not answer questions about how to navigate the tradeoff. Those depend on the values at play in the relevant context" (622–626).

The link from characteristics to risk is a claim, not a formula: "Neglecting these characteristics can increase the probability and magnitude of negative consequences" (588–589). Bias has its own three-part classification: systemic, computational and statistical, and human-cognitive (869–880).

### 2.5 The 12 GAI risks (AI 600-1)

The profile first names the dimensions along which risk varies (600-1 147–176):
- **stage of the lifecycle**;
- **scope**: model or system level, application level, or ecosystem level ("algorithmic monocultures");
- **source of risk**: the model's design, training or operation, or its inputs or outputs, or "human behavior, including the abuse, misuse, and unsafe repurposing by humans (adversarial or not)", or human–AI interaction;
- **time scale**: "abruptly or across extended periods".

It then lists twelve risks, each defined in one sentence (216–278):
1. CBRN Information or Capabilities
2. Confabulation
3. Dangerous, Violent, or Hateful Content
4. Data Privacy
5. Environmental Impacts
6. Harmful Bias or Homogenization
7. Human-AI Configuration
8. Information Integrity
9. Information Security
10. Intellectual Property
11. Obscene, Degrading, and/or Abusive Content
12. Value Chain and Component Integration

NIST says openly that the list is not on one basis: "Each risk is labeled according to the outcome, object, or source of the risk (i.e., some are risks 'to' a subject or domain and others are risks 'of' or 'from' an issue or theme)" (196–198).

Footnote 5 (205–213) offers an alternative three-way grouping, "derived in part from the UK's International Scientific Report": technical/model (malfunction), misuse by humans (malicious use), and ecosystem/societal (systemic). Several risks fall into more than one group.

Each risk section closes with a tag line mapping it onto the RMF's trustworthiness characteristics (e.g. "Trustworthy AI Characteristic: Safe, Explainable and Interpretable", 305). **That tag line is the only formal link between the risk list and the RMF's own concepts.**

## 3. How the parts relate: the Core and profiles

```
GOVERN (cross-cutting, "infused throughout")        6 categories / 19 subcategories
   │  policies, accountability, workforce diversity, culture,
   │  engagement with AI actors, third-party/supply chain
   ▼
MAP  ──►  MEASURE  ──►  MANAGE           (order flexible; "iterative")
 5 / 18      4 / 22        4 / 13
 context,    methods &     prioritise & respond (mitigate / transfer /
 categorise  metrics;      avoid / accept); go/no-go; residual risk;
 system,     evaluate the  supersede/disengage/deactivate; third-party;
 benefits &  7 trustwor-   response, recovery, communication,
 costs,      thiness       incidents
 components, characteris-
 impacts     tics; track
 (likelihood risks over
 × magnitude) time; feedback on measurement

PROFILE = the Core instantiated for {use case | sector | technology | current vs target state}
   AI 600-1 = cross-sectoral GAI profile:
     Action ID (e.g. GV-1.3-001) ─ keyed to ─► RMF subcategory
        ├─ tagged ─► one or more of the 12 GAI risks
        └─ tagged ─► AI actor tasks (Appendix A categories)
```

- **The functions.**
  - MAP "establishes the context to frame risks" (1137). Its outcomes "are the basis for the MEASURE and MANAGE functions" (1158–1159).
  - MEASURE "employs quantitative, qualitative, or mixed-method tools … to analyze, assess, benchmark, and monitor AI risk and related impacts" (1300–1302).
  - MANAGE "entails allocating risk resources to mapped and measured risks" (1448–1450).
  - GOVERN "is a cross-cutting function that is infused throughout" (1011–1012).
  - The order is loose: "Assuming a governance structure is in place, functions may be performed in any order … most users of the AI RMF would start with the MAP function" (978–981).
- **Categories.**
  - GOVERN: policies and processes; accountability structures; workforce DEIA; a culture that "considers and communicates AI risk"; engagement with AI actors; third-party and supply chain.
  - MAP: context; categorisation; capabilities, benefits and costs; risks of components; "Impacts to individuals, groups, communities, organizations, and society are characterized".
  - MEASURE: methods and metrics; evaluation against the trustworthiness characteristics; tracking over time; feedback on how well measurement works.
  - MANAGE: prioritise and respond; maximise benefits and minimise impacts; third-party risk; treatment, response and recovery, communication.
- **The subcategories are outcome statements in the passive present.** Neither obligations nor recommendations. Examples:
  - MAP 5.1: "Likelihood and magnitude of each identified impact … based on expected use, past uses of AI systems in similar contexts, public incident reports, feedback from those external to the team … or other data are identified and documented" (1275–1280).
  - MEASURE 2.6: "The AI system to be deployed is demonstrated to be safe, its residual negative risk does not exceed the risk tolerance, and it can fail safely, particularly if made to operate beyond its knowledge limits" (1382–1388).
  - MANAGE 1.1: "A determination is made as to whether the AI system achieves its intended purposes and stated objectives and whether its development or deployment should proceed."
  - MANAGE 1.3: "Risk response options can include mitigating, transferring, avoiding, or accepting" (1481ff.).
  - MANAGE 2.4: mechanisms "to supersede, disengage, or deactivate AI systems that demonstrate performance or outcomes inconsistent with intended use" (1503ff.).
- **Profiles** (Section 6, 1541–1575).
  - *Use-case* profiles (e.g. hiring, fair housing).
  - *Temporal* profiles: "Comparing Current and Target Profiles likely reveals gaps to be addressed" (1557–1558).
  - *Cross-sectoral* profiles, for things like LLMs.
  - "This Framework does not prescribe profile templates" (1574).
- **AI 600-1 as a profile.**
  - It is "a cross-sectoral profile" (600-1 96–99).
  - Its suggested actions carry an **Action ID** that encodes function and subcategory (GV-1.1-001 = first action for GOVERN 1.1; 643–646). Each is tagged with GAI risks and AI actor tasks (647–651).
  - It covers only some subcategories: "Suggested actions are listed for only some subcategories" (627–628). By my count, about 210 unique action IDs across 49 of the 72 subcategories. The tables are garbled in extraction, so treat that count as approximate.
  - Its selection came from the Public Working Group's four "primary considerations": Governance, Content Provenance, Pre-deployment Testing, and Incident Disclosure (600-1 125–127). Each gets an essay-style section in Appendix A (A.1.1–A.1.8, 2555–2831).

## 4. How risk is graded, or deliberately not

- **Defined, not scaled.** Risk is probability × magnitude (RMF 272–278). MAP 5.1 asks for likelihood and magnitude to be "identified and documented". MANAGE 1.2 prioritises by "impact, likelihood, and available resources or methods" (1479). There is no scale, no scoring scheme, no levels, and no tiers in the RMF itself.
- **Tolerance is delegated.** "While the AI RMF can be used to prioritize risk, it does not prescribe risk tolerance" (398). "Where established guidelines do not exist, organizations should define reasonable risk tolerance" (422–423). Tolerance is "highly contextual and application and use-case specific" (402–403).
- **Metrics and thresholds are delegated to judgment.** "Human judgment should be employed when deciding on the specific metrics related to AI trustworthiness characteristics and the precise threshold values for those metrics" (602–604).
- **One bright line.** "In cases where an AI system presents unacceptable negative risk levels – such as where significant negative impacts are imminent, severe harms are actually occurring, or catastrophic risks are present – development and deployment should cease in a safe manner until risks can be sufficiently managed" (446–449). This is also the only place "catastrophic" appears in either document.
- **Prioritisation heuristics** are qualitative. Human-facing systems and systems trained on sensitive data "may call for" higher initial priority (453–461). Safety risks that "pose a potential risk of serious injury or death call for the most urgent prioritization" (711–713).
- **Residual risk is defined twice, differently.** "risk remaining after risk treatment (Source: ISO GUIDE 73)" (463). MANAGE 1.4: "Negative residual risks (defined as the sum of all unmitigated risks)" (1489–1490).
- **600-1 pushes grading further onto the organisation.** GV-1.3-001 lists "factors when updating or defining risk tiers for GAI" (600-1 709–719). GV-1.3-002 says "Establish minimum thresholds for performance or assurance criteria and review as part of deployment approval ('go/'no-go') policies" (721–727). The tiers and thresholds themselves are the organisation's to set. Organisations "may choose to apply their existing risk tiering to GAI systems" (2560–2561).
- **The measurement challenges are part of the model** (RMF 1.2.1, 321–387): third-party components; "Tracking emergent risks"; "Availability of reliable metrics" (metrics "can be oversimplified, gamed, lack critical nuance"); lifecycle stage ("some risks may be latent"); lab vs real world; inscrutability; and the need for a human baseline. The framework's own effectiveness is also unmeasured: evaluations of it "will be part of future NIST activities" (897–900).

## 5. Method and lineage

- **Statutory basis.** The National AI Initiative Act of 2020 (RMF 193–196). For 600-1, EO 14110 §4.1(a)(i)(A) (600-1 115–117). That order has since been revoked. EO 14365 (L16–19) refers to having "revoked my predecessor's attempt" via EO 14179; that it was 14110 is from outside my set. 600-1 remains published as far as my set shows.
- **Standards it draws on.**
  - ISO 31000:2018 (risk, risk management);
  - ISO Guide 73 (risk tolerance, residual risk);
  - OMB Circular A-130 (risk as impact × likelihood);
  - ISO/IEC TS 5723:2022 (reliability, accuracy, robustness, safety, resilience);
  - ISO 9000:2015 (validation);
  - ISO/IEC 22989:2022 and the OECD AI Recommendation (AI system);
  - OECD (AI actors; the classification framework behind Figure 2);
  - ISO 26000 and ISO/IEC TR 24368 (social responsibility, sustainability, professional responsibility, 180–191);
  - NIST SP 1270 (bias, 887–888).
- **Its own architecture.** It aligns itself with NIST's cybersecurity and privacy frameworks, which "are outcome-based rather than prescriptive and are often structured around a Core set of functions, categories, and subcategories" (Appendix B, 1782–1784). So the function → category → subcategory shape is inherited from the cybersecurity-framework lineage, not derived from a model of AI.
- **Process.** "a formal Request for Information, three widely attended workshops, public comments on a concept paper and two drafts of the Framework, discussions at multiple public forums, and many small group meetings" (RMF 234–238). Appendix D (1904–1941) lists its design attributes: "risk-based, resource-efficient, pro-innovation, and voluntary"; "consensus-driven"; "common language"; "law- and regulation-agnostic"; "a living document". For 600-1: the Generative AI Public Working Group, "an open, transparent, and collaborative process, facilitated via a virtual workspace" (600-1 121–124), plus RFIs.
- **Companion.** The online AI RMF Playbook, with suggested tactical actions per subcategory (RMF 965–972). It is not in my set.

## 6. Purpose, audience, force

- **Purpose.** "to offer a resource to the organizations designing, developing, deploying, or using AI systems to help manage the many risks of AI and promote trustworthy and responsible development and use of AI systems" (RMF 193–196).
- **Force.** "intended to be voluntary, rights-preserving, non-sector-specific, and use-case agnostic" (196–199). "Be law- and regulation-agnostic" (1935–1937). The Playbook "is voluntary" (967–968). Users may "select from among the categories and subcategories" (975–977).
- **Audience.**
  - Primary: the AI actors in the four inner dimensions, "who perform or manage the design, development, deployment, evaluation, and use of AI systems and drive AI risk management efforts" (518–521).
  - Secondary, informing: People & Planet actors (532–558).
- **Status.** The RMF is a living document with formal review "no later than 2028" (RMF 49–50). The 2025 Action Plan directs NIST to "revise the NIST AI Risk Management Framework to eliminate references to misinformation, Diversity, Equity, and Inclusion, and climate change" (whitehouse-2025-action-plan 233–236). NIST's March 2026 slides list a "Revised NIST AI RMF" as forthcoming (nist-2026-vcat-ai-update 413). My set contains no revised text, so everything here describes 1.0.

## 7. Uncertainty and evidence

- **The RMF treats uncertainty as something to manage, not something to exclude.**
  - "The inability to appropriately measure AI risks does not imply that an AI system necessarily poses either a high or low risk" (324–325).
  - "Organizations' risk management efforts will be enhanced by identifying and tracking emergent risks" (341–342). MEASURE 3.1 asks for tracking of "existing, unanticipated, and emergent AI risks".
  - The MAP function exists partly because of uncertainty: "varying levels of visibility can introduce uncertainty into risk management practices" (1152–1154).
- **600-1 draws an evidential line.** This is the decisive methodological choice of the profile:

  > "Importantly, some GAI risks are unknown, and are therefore difficult to properly scope or evaluate given the uncertainty about potential GAI scale, complexity, and capabilities. … This document focuses on risks for which there is an existing empirical evidence base at the time this profile was written; for example, speculative risks that may potentially arise in more advanced, future GAI systems are not considered. Future updates may incorporate additional risks." (600-1 187–194)

- **Inside each risk, 600-1 mixes three things:**
  - reported findings ("LLM outputs regarding biological threat creation and attack planning provided minimal assistance beyond traditional search engine queries", 289–292);
  - forward-looking "may" statements (297–304);
  - admissions that the science is immature ("Currently there is no agreed upon method to estimate environmental impacts from GAI", 421–422; "it is difficult to estimate the downstream scale and impact of confabulations", 336–337).
- **On testing and incidents**, 600-1 is candid about how weak the evidence base is:
  - pre-deployment TEVV "may be inadequate, non-systematically applied, or fail to reflect or mismatched to deployment contexts" (2643–2644);
  - "Formal channels do not currently exist to report and document AI incidents", and existing databases "track by amount of media coverage" (2809–2812).
- **Terminology is deferred.** "A glossary of terms pertinent to GAI risk management will be developed and hosted on NIST's Trustworthy & Responsible AI Resource Center" (600-1 130–132).

## 8. What it excludes

- **RMF**:
  - no catalogue of AI failure modes or threat scenarios;
  - no risk tolerance or acceptance criteria;
  - no scoring or tiers;
  - no templates;
  - no checklist, and no required order.
  - Positive impacts are *included*, which is unusual among the sources.
- **600-1**:
  - "speculative risks that may potentially arise in more advanced, future GAI systems" (191–193);
  - any subcategory outside the Public Working Group's four considerations, which "may be added later" (634–635);
  - non-foundation-model GAI. GAI "generally refers to generative foundation models" (110–111).
- **Words absent from both**, which matters for any cross-model table: "hazard" (0 occurrences), "loss of control" (0), "misalignment" in the safety sense (0 in the RMF; 600-1's single "misalignment between systems and users", 2605, is about a mismatch between system and use). Autonomy appears only as "varying levels of autonomy" in the AI-system definition and as "fully autonomous to fully manual" human–AI configurations (RMF 1832–1833).

---

## Key terms as this model uses them

| Term | Meaning here | Verbatim / location |
|---|---|---|
| **hazard** | **Not used** in either document. | — |
| **risk** | Probability × magnitude of an event's consequences; may be positive or negative. | "the composite measure of an event's probability of occurring and the magnitude or degree of the consequences of the corresponding event" (RMF 272–274; restated in 600-1 140–141) |
| **harm** | Used throughout, not defined in the RMF. 600-1 gives a counterfactual-baseline gloss in a footnote. | 600-1 fn 8: "The notion of harm presumes some baseline scenario that the harmful factor (e.g., a GAI model) makes worse" (257–262) |
| **impact** | The consequence of an event, positive or negative. MAP 5 characterises impacts "to individuals, groups, communities, organizations, and society". | RMF 274–275; 1275–1280 |
| **likelihood / probability** | A component of risk. Not scaled. | RMF 272–278; MAP 5.1 (1275); MANAGE 1.2 (1479) |
| **severity / magnitude** | "magnitude or degree of the consequences" / "magnitude of harm". "Severity" appears once each, in passing. | RMF 273, 276–277; RMF 711 ("severity of potential risks"); 600-1 183 |
| **risk tolerance** | An organisation's readiness to bear risk. Not prescribed. | "the organization's or AI actor's … readiness to bear the risk in order to achieve its objectives … (Adapted from: ISO GUIDE 73)" (RMF 398–401) |
| **residual risk** | Defined two ways. | "risk remaining after risk treatment (Source: ISO GUIDE 73)" (RMF 463); "the sum of all unmitigated risks" (MANAGE 1.4, 1489–1490) |
| **risk treatment / response** | A MANAGE activity: respond, recover, communicate. The options are mitigate, transfer, avoid, accept. | RMF 1449–1450; MANAGE 1.3 (1481ff.) |
| **threshold / tier / level** | Not defined. Threshold *values* for metrics are left to human judgment. 600-1 asks organisations to define risk tiers and "minimum thresholds" for go/no-go. | RMF 602–604; 600-1 709–727, 2560–2561 |
| **capability** | Used but undefined. In 600-1 it appears mainly in "CBRN Information or Capabilities" and "offensive cyber capabilities". | 600-1 216–218, 242–244; "before developing highly capable models" (729) |
| **incident / event** | Undefined in the RMF (MANAGE 4.3: "Incidents and errors are communicated…"). 600-1 quotes a definition, with no source named in the lines I read. | 600-1: "event, circumstance, or series of events where the development, use, or malfunction of one or more AI systems directly or indirectly contributes to one of the following harms…" (2801–2807) |
| **emergent risk** | Risks that appear over time, to be tracked. Undefined. | RMF 341–342; MEASURE 3.1 |
| **loss of control** | **Not used.** | — |
| **safeguard** | Generic ("technical safeguards"). Not a term of art. | RMF 337 |
| **mitigation / control** | Mitigation is a risk-response option. The RMF lists control types only once: "compensating, detective, deterrent, directive, and recovery controls". | RMF 1316–1318 |
| **safe** | ISO definition: not leading to endangerment "under defined conditions". | RMF 701–702 |
| **secure / resilient** | Resilient: withstanding "unexpected adverse events" and degrading "safely and gracefully". Secure: maintaining "confidentiality, integrity, and availability through protection mechanisms". Security "includes resilience". | RMF 732–747 |
| **misuse** | Rare in the RMF: "unexpected or adversarial use (or abuse or misuse)". In 600-1 it is one *source* of risk (human "abuse, misuse, and unsafe repurposing … (adversarial or not)"). | RMF 747; 600-1 156–171 |
| **AI actor** | Anyone playing "an active role in the AI system lifecycle" (OECD). Specified by *task categories*, not organisation types. | RMF 203–206; Appendix A 1584–1712 |
| **developer / deployer / provider** | Not defined. They appear as members of task categories ("developers", "software developers", "product developers") and in passing ("an AI developer who makes AI software available … can have a different risk perspective than an AI actor who is responsible for deploying"). 600-1 contrasts "GAI developers" with "GAI deployers". "Providers" appear only inside *third-party entities*. | RMF 368–371, 1602, 1611, 1619, 1687–1693; 600-1 639 |
| **third-party entities** | External providers, developers, vendors or evaluators of data, models or systems. | "By definition, they are external to the design, development, or deployment team of the organization that acquires its technologies or services" (RMF 1687–1693) |
| **alignment** | Not used in the RMF. In 600-1 it appears only in an organisational sense ("Alignment to organizational values", 2586; "misalignment between systems and users", 2605). | — |
| **trustworthy AI** | Having the seven characteristics, balanced by context; "only as strong as its weakest characteristics". | RMF 579–610 |
| **TEVV** | Test, evaluation, verification and validation, performed "throughout the AI lifecycle", with V&V actors kept separate from T&E actors. | RMF 514–516, 1623–1646 |
| **profile** | An instantiation of the Core for a setting, a technology or a state. | RMF 1542–1545; 600-1 89–91 |
| **confabulation** | NIST's deliberate replacement for "hallucination", which it avoids because the term anthropomorphises. | "a phenomenon in which GAI systems generate and confidently present erroneous or false content in response to prompts" (600-1 312–315; fn 6, 249–251) |
| **GAI / dual-use foundation model** | Taken from EO 14110. For the profile, GAI "generally refers to generative foundation models". | 600-1 108–113 |
| **human-AI configuration** | Interaction arrangements that can lead to anthropomorphising, automation bias, over-reliance or "emotional entanglement". | 600-1 235–238, 464–477 |
| **information integrity** | Taken from a White House roadmap: "spectrum of information and associated patterns of its creation, exchange, and consumption in society". | 600-1 484–489, 495–496 |

---

## Two related NIST models (short)

### AI 800-1 (2pd, Jan 2025, then called U.S. AISI): misuse risk through threat profiles

The RMF manages *any* AI risk at the level of the organisation. AI 800-1 narrows to **deliberate misuse of dual-use foundation models, by initial developers**, and it *does* supply a model of the risk. Its structure is Objective → Practice → Recommendations → Documentation (nist-2025-managing 415–441). There are seven objectives: identify, plan, protect (from unauthorised access), measure, mitigate before deployment, monitor and respond, disclose (376–382). Its core unit is the **threat profile**:

> "A threat profile consists of: (a) the malicious task(s) that the threat actor might accomplish using the model, (b) the threat actor or actors who might use the model to cause this type of harm, (c) the way(s) in which they could use the model to accomplish this task, and (d) the mechanism(s) by which this could cause harm." (1099–1102)

Risk is assessed per threat profile, "by estimating the likelihood of harm occurring and the impact if that harm occurred" (503–505). The assessment is **marginal** "relative to that baseline" of tools already available (508–511). It accounts for existing barriers and societal preparedness (530–532), and for actors' "motivations, willingness, and capacity" (528–529).

Capability is forecast before training from **proxy models** (448–470). Measurement asks the evaluator to "Maximize model performance on evaluation tasks" and to account for any gap between evaluator and threat-actor effort (697–701). The glossary adds *margin of safety*: a deliberate buffer for uncertainty between measured and actual risk (1063–1068). The chem/bio appendix classifies threat actors (state vs three non-state profiles), scenarios, and **technical, operational and motivational barriers** that a model might help an actor overcome (1538–1612).

Its exclusions: accidental harms (206–208), and non-foundation models. As far as my set shows, it never reached a final version.

### AI 800-2 (ipd, Jan 2026, CAISI): a measurement model, not a risk model

AI 800-2 gives a vocabulary for *what an evaluation claims to measure* (glossary 1525–1642). The measurement concepts:
- **Measurement construct**: "An abstract concept not directly measurable (e.g., 'mathematical reasoning')" (1579–1585).
- **Measurement criterion**: "A directly measurable or observable concept" (1587–1591).
- **Measurement instrument**: "A tool used to gather observations or assign values (e.g., a benchmark …)" (1593–1594).
- **Measurement validity**: "The degree to which accumulated evidence and theory support a specific interpretation of test scores for a given use of a test" (1596–1600).

Content validity and external validity are defined alongside these. So are *capability* ("The range of tasks or functions that an AI system can perform and how effectively it performs them", 1547–1548), *proxy task*, *baseline* and *scaffolding*. Practice 3.3 tells evaluators to "Differentiate observations, inferences, predictions, and normative statements" (1378–1379), and to report the evidence linking a benchmark to its construct (1381–1390). It is NIST's most explicit statement of how an evaluation result should be typed and qualified. It says nothing about which risks matter.

---

## Closing note: where this meets and cuts across Joseph's chain (my reading)

- **It lines up with the downstream half.** "Preventions & controls" and "mitigations & recovery" correspond to MANAGE (treatment, response, recovery, communication, deactivate). "Policies & decision-making" corresponds to GOVERN. The harmed-group radius (individuals → groups → communities → organisations → society → environment → planet) is explicit in the risk definition and in MAP 5.
- **It cuts across the upstream half.** The RMF has no "sources & causes tree" and no event taxonomy. Those are what an organisation produces in MAP. 600-1's twelve risks mix outcome, object and source on NIST's own admission, so they won't slot cleanly into any single stage of a causal chain. The "source of risk" dimension (600-1 154–172) comes closest to a cause axis.
- **What it would contribute, and what it would miss.** Its most transferable pieces are the actor-as-task model (Appendix A), the lifecycle × dimension grid, and its candour about measurement (RMF 1.2.1; AI 800-2). Its empirical-evidence rule (600-1 191–194) means that, by design, it is silent on exactly the risks the frontier-safety literature centres: loss of control, and misalignment as a model property.

I'm still available for follow-ups.
