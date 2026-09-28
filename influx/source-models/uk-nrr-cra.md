# The UK national risk assessment model: National Risk Register (2026) and Chronic Risks Analysis (2025)

*Written for Joseph by the agent that wrote the UK-government atlas (`../source-atlas/uk-gov.md`). It describes the model on its own terms, not mapped onto ours.*

*Sources:*
- `cabinetoffice-2026-nrr`: *National Risk Register 2026 edition*, Cabinet Office. 223 PDF pages; its printed page numbers run one ahead of the PDF page.
- `cabinetoffice-2025-cra`: *Chronic Risks Analysis*, Cabinet Office and Government Office for Science. 132 PDF pages.

*Citations are `NRR L…` or `CRA L…` into the atlas extractions (`…/scratchpad/src-text/<key>.txt`), with the PDF page as "p". Several tables and figures were checked against the PDF itself; I say so where I did.*

---

## At a glance

| Dimension | National Risk Register (acute) | Chronic Risks Analysis (chronic) |
|---|---|---|
| **What it is** | The public, declassified version of the classified National Security Risk Assessment (NSRA): "the UK government's single, authoritative articulation of the most serious acute risks" (NRR L139–143). | A parallel framework for "longer-term challenges that erode our economy, community, way of life and/or national security" (CRA L111–113). |
| **Unit** | A **risk**, which is one **reasonable worst-case scenario**: 87 standalone risks plus 8 linked scenarios, "a total of 95 risks" (NRR L673–674). | A **chronic risk**: 26 named, 25 assessed (end-to-end encryption is "under review", CRA L286–287, L355–358). They are grouped into 7 themes. |
| **Kinds named** | Malicious threats vs non-malicious hazards; the scenario (with key assumptions and variations); impact dimensions; common consequences; response capabilities (23 generic); vulnerable people; recovery. | Chronic risks, acute risks, **vulnerabilities** (including groups of people); example mitigations; benefits of acting; short-term trajectories and longer-term uncertainties; interactions. |
| **Relations** | Each risk sits at a point on a **likelihood × impact matrix**. Risks → common consequences → generic capabilities. Chronic risks must be shown to "manifest in, interact with and exacerbate" acute ones (NRR L673–678). | A **directed interaction network** among chronic risks, acute risks and vulnerabilities. Edges are labelled with causal sentences, and in one view are signed **Reinforcing / Diminishing** (CRA L4487–4498). |
| **Grading** | Likelihood 1–5 (log bands from <0.2% to >25% over a 2- or 5-year window), mapped to PHIA words. Impact 0–5 on 7 dimensions, combined into a 1–5 score (log). Confidence low/medium/high. | **No probabilistic grading**, deliberately (CRA L145–147). Structure is read from network counts (most connected, "edge" risks, cascade end-points). |
| **Method** | Departmental risk owners, expert consultation, data and modelling; independent-chaired expert challenge panels; RWCS construction; the PHIA yardstick. | Literature and evidence gathering with expert challenge; GO-Science futures methods (workshops, pre-existing scenarios); "impact mapping". |
| **Purpose / audience** | Proportionate contingency planning; local Community Risk Registers; practitioners, businesses, CNI operators, academics. "not targeted at the general public" (NRR L340–342). | Shared understanding; long-term preparedness and policy; practitioners, businesses, academics, policymakers. "not about predicting the future" (CRA L131). |
| **Force** | Informational. The internal process binds risk owners ("must also evidence…", NRR L673–676). | Informational. Its mitigations "may not represent current government policy" (CRA L155–157). |
| **Uncertainty** | Handled *through the scenario*: "worst plausible" after "highly unlikely variations have been discounted". Plus confidence ratings, uncertainty lines on plots, and named Variations. | Handled by refusing point estimates. Futures framing; "snapshot in time"; a "Longer-term uncertainties" field per risk. |
| **Excludes** | Chronic risks; "every risk that the UK could face"; highly unlikely variations; classified detail (some scores grouped, one nuclear scenario withheld); mainly non-domestic impacts. | Probability and impact scores; a regularly updated view; the full network (published only in example sections); the systemic-risk scenarios and case-study system mentioned in its method. |
| **AI** | Not an acute risk. It enters as a templated modifier sentence in about ten risk summaries, and is named as a chronic risk handled by the CRA. | One of the 25 assessed chronic risks ("Impacts from use and capability of artificial intelligence"), focused on frontier AI. It also appears inside several other chronic risks. |

---

## 1. One system in two registers

The UK divides risk by *temporal character* before anything else:

> "The risks listed in the NRR are acute risks—discrete events that may require an emergency response from the government. Chronic risks, such as antimicrobial resistance (AMR), impacts of artificial intelligence (AI), reliance on global supply chain and climate change, are not included in this list." (NRR L648–653, p20)

> "Chronic risks are distinct from acute risks in that they pose continuous challenges that erode our economy, community, way of life, and/or national security. Generally, but not always, these manifest over a longer timeframe. Due to the systemic and enduring nature of chronic risks, traditional probabilistic impact assessments are made less effective." (NRR L658–663, p20)

The two are coupled. Chronic risks "can also make acute risks more likely and serious. For example, climate change is making severe weather more likely and impactful" (CRA L92–96, p5). The NRR calls them "these enduring drivers" that risk owners incorporate "when assessing acute threats" (NRR L230, L240).

The machinery around the published documents:

```
             classified                               public
 ┌──────────────────────────────┐         ┌────────────────────────────┐
 │ National Security Risk       │ ──────▶ │ National Risk Register     │
 │ Assessment (NSRA)            │ "external│ (95 acute risks, RWCS)     │
 │  risk owners = departments   │ version" └──────────┬─────────────────┘
 │  RWCS per risk, scored       │                     │ used by Local
 │  expert challenge panels     │                     ▼ Resilience Forums
 └──────────────┬───────────────┘         Community Risk Registers (local)
                │
                ▼  "shift focus away from the risk themselves,
 National Resilience Planning       to the common consequences"
 Assumptions (NRPAs)  ───────────▶  23 generic response capabilities
                                    ("cause-agnostic basis for planning")

 Chronic Risks Analysis (26 chronic risks, 7 themes) ── "parallel" ──▶ NSRA/NRR
   chronic risks ──drive / exacerbate──▶ acute risks
   risk owners "must also evidence how chronic risks … manifest in, interact
   with and exacerbate acute events" (NRR L673–678)
```

Sources for the sketch: NRR L202–214, L362–393 (p8–13); CRA L71–82 (p5).

## 2. The National Risk Register

### 2.1 The unit: a risk is a reasonable worst-case scenario

> "Risks in the NSRA and NRR are assessed as 'reasonable worst‑case scenarios'. These scenarios represent the worst plausible manifestation of that particular risk (once highly unlikely variations have been discounted) to enable relevant bodies to undertake proportionate planning." (NRR L376–381, p13)

> "These scenarios are not a prediction of what is most likely to happen" (NRR L204–206, p8)

So "risk" names a class of event (e.g. "Cyber attack: health and social care system"), and what is actually assessed and scored is one constructed instance of it. Where one topic needs materially different planning, it gets several linked scenarios, numbered with letters (flooding 53a/b/c, NRR L527–531, p17). The count "87 standalone risks, and 8 linked scenarios for a total of 95 risks" (NRR L673–674) counts scenarios as risks.

Inclusion has a threshold, stated qualitatively: "would have a substantial impact on the UK's safety, security or critical systems at a national level" (NRR L195–197, p8). The set is representative, not exhaustive: it does "not aim to capture every risk that the UK could face. Instead it aims to identify a range of risks that are representative of the risk landscape and serve as a cause-agnostic basis for planning for the common consequences" (NRR L389–392, p13).

The top division is **malicious vs non-malicious**: "these risks may be non‑malicious, such as accidents or natural hazards or they may be malicious threats from actors who seek to do us harm" (NRR L197–200). Chapter 4 groups the 95 into: terrorism; cyber; state threats; geopolitical and diplomatic; accidents and systems failures; natural and environmental hazards; human, animal and plant health; societal; conflict and instability (TOC NRR L9–110, p2–4).

### 2.2 The shape of a risk summary

Every risk page follows one template. The example is "Cyber attack: health and social care system", NRR L2139–2210, p65–67:

| Field | What it holds |
|---|---|
| (opening context) | Recent real incidents, the relevant policy or regulation, and trend statements. For cyber risks it also includes the AI sentence (§8). |
| **Scenario** | The RWCS narrative. |
| **Key assumptions** | Conditions the scenario assumes, e.g. "The assessment assumes that disruptions could have major nationwide effects" (p153, checked on the PDF). |
| **Variations** | Alternative manifestations. Sometimes placed explicitly on the trade-off: "A lower‑impact, higher‑probability scenario …", "A higher‑impact, lower‑probability variation …" (volcanic eruption, NRR L5537, L5551). |
| **Response capability requirements** | Split by three responder classes: "Government and Agencies"; "CNI and Wider Private Sector"; "Voluntary, Community and Faith Sector" (introduced NRR L265–272). |
| **Recovery** | The duration and shape of return to normal. |
| **Impact on vulnerable people** | Which groups are disproportionately affected, and how. |
| **Common consequences** | A short list drawn from a shared vocabulary ("disruption to essential services", "potential changes in public behaviour", …). |
| **Score** | A 5×5 plot with a dot. For sensitive risks it is replaced by a box giving the *group average* (e.g. "The average impact score for risks grouped under the 'cyber attacks on infrastructure' category is 3 (moderate) and the average likelihood score is 4 (5‑25%)", NRR L2181–2184, checked on PDF p67). |

### 2.3 Likelihood

> "the relevant government departments and agencies assess the likelihood of the reasonable worst‑case scenario occurring within the assessment period (which is 5 years for non‑malicious risks and 2 years for malicious risks) using insight, extensive data, modelling, and expert analysis." (NRR L404–410, p14)

> "Likelihood is presented as the percentage chance of the reasonable worst‑case scenario occurring at least once in the assessment timescale and is scored on a 1‑5 scale." (NRR L422–425)

For malicious risks, likelihood is a composite: "the intent to carry out an attack, which is balanced against an assessment of their capability to conduct an attack and the vulnerability of their potential targets to an attack. These 3 parameters … are collated together to form one likelihood score" (NRR L416–421). How they are combined is not stated.

**Table 2** (NRR L402–426), as printed on PDF p14 and checked there. The extraction scrambles the rows.

| Score | Percentage chance | PHIA yardstick designation |
|---|---|---|
| 5 | >25% | Almost certain (95-100%); Highly likely (80-90%); likely or probable (55-75%); Realistic possibility (40-50%); Unlikely (25-35%) |
| 4 | 5-25% | Highly unlikely (5-25%) |
| 3 | 1-5% | Remote chance (0-5%) |
| 2 | 0.2-1% | — |
| 1 | <0.2% | — |

The document explains the compression: "The highest score (5) represents a greater than 25% likelihood. The reason that this number is relatively low is that all risks in the NSRA are relatively low likelihood events." (NRR L424–426). The scale is logarithmic: "a score 3 risk is approximately 5 times more likely to occur than a score 2 risk" (NRR L527–530, p17). The same scale is used for malicious and non-malicious risks "to allow like‑for‑like comparison" (NRR L422–424), even though their windows differ.

### 2.4 Impact

Seven dimensions (NRR L437–470, p15):
- **human welfare**: fatalities, casualties including illness, injury and mental health, evacuation and shelter;
- **behavioural**: "changes in individuals' behaviour or levels of public outrage";
- **essential services**;
- **economic**;
- **environmental**, including "timescales for reparation";
- **security**: law enforcement, armed forces, borders, criminal justice;
- **international**: relations, soft power, international law and norms, displacement.

> "Each of the dimensions … is scored on a scale of 0 to 5 based on the scope, scale and duration of the harm that the reasonable worst‑case scenario could foreseeably cause … These scores are then combined to provide a single overall impact score. Risks assessed to have the highest impact score (5) are considered catastrophic." (NRR L449–458, p15)

The combination rule is not published. Scoring focuses "primarily on domestic impacts – even where the risk occurs internationally" (NRR L447–450). Qualitative data is also collected on "future trends, interactions between acute and chronic risks, impacts to critical supply chains and the disproportionate impact … on vulnerable people" (NRR L437–445).

**Table 3, example bands** (NRR L481–496; checked on PDF p16):

| | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| Fatalities | 1-8 | 9-40 | 41-200 | 201-1,000 | >1,000 |
| Casualties | 1-18 | 17-80 | 81-400 | 400-2,000 | >2,000 |
| Economic cost | Millions of £ | Tens of millions £ | Hundreds of millions £ | Billions of £ | Tens of billions £ |

The casualty bands overlap at their edges (17–18, 400) as printed in the source. On the matrix the level names are Minor (1), Limited (2), Moderate (3), Significant (4), Catastrophic (5). The impact scale is also logarithmic (NRR L505–508).

### 2.5 The matrix, confidence, and grouping for secrecy

> "The NRR matrix below presents the impact and likelihood of a plausible worst‑case scenario manifestation of each risk. To enable large differences in impact and likelihood to be shown on the same matrix, non‑linear scales have been used." (NRR L498–504, p16)

> "Uncertainty is an inherent aspect of risk assessment. Impact and likelihood scores are given a confidence rating (low, medium or high) that takes account of: quality and reliability of the evidence base; assumptions used in the analysis and; external factors … Uncertainty is represented as lines extending from the plotted dots in the individual risk matrices in Chapter 4 to provide a more comprehensive picture of the risk landscape and prevents planning or strategic decisions from being made with false confidence." (NRR L532–549, p17)

On the one individually scored page I viewed (national disruption to data infrastructure, PDF p153), the plot shows a single dot at impact 4 / likelihood 4 with no visible uncertainty lines. I have not checked other pages. The confidence rating itself is not printed on that page either.

Sensitive risks are "thematically grouped", and "The position of each grouped risk on the matrix below is an average of the impact and likelihood scores of all the different risks that belong to that category" (NRR L551–558, L521–525). The grouped categories include "conventional attacks on infrastructure" and "cyber attacks on infrastructure", because of "the sensitive, classified nature of the information" (NRR L594–603, p18).

### 2.6 From risks to consequences to capabilities

The planning logic runs downstream of the event, not upstream to causes:

> "The NRPAs take this analysis, but shift focus away from the risk themselves, to the common consequences of these risks." (NRR L377–380, p13)

> "The UK government maintains 23 generic response capabilities … Despite the extremely wide range of risks represented in the NRR, the capabilities required to respond to their emergence are common to many, necessitating much fewer response capabilities to be managed by the government than there are scenarios." (NRR L393, L541–548)

This is a many-to-few design: 95 scenarios → a shared vocabulary of common consequences → 23 capabilities. Catastrophic risks "may result in whole-system civil emergencies", requiring several capabilities at once "and others not identified within the programme" (NRR L362–366).

### 2.7 Vulnerable people

This edition adds a systematic treatment of who is harmed, following the 2025 Resilience Action Plan:

> "The Resilience Action Plan defines vulnerable people as individuals or communities who may experience more significant and disproportionate impacts during emergencies. Vulnerability is not a fixed characteristic; it is shaped by a complex interplay of factors, which are intersectional and interconnected." (NRR L881–885, p26)

> "Individuals who might be considered vulnerable in the context of one risk might not be for another. For example, older adults might be considered more vulnerable in some virus outbreaks, however, could potentially have higher levels of preparedness for a significant power outage" (NRR L902–907, p27)

It also gives six principles (NRR L895–927, p27). Among them, response itself can harm: "consider how response and recovery actions … may inadvertently create new forms of disproportionate impacts" (Principle 5, L918–921). Harm can also be indirect ("secondary effects", Principle 3) and can change over time (Principle 4).

## 3. The Chronic Risks Analysis

### 3.1 Units and themes

There are 26 chronic risks under 7 themes: security; technology and cyber security; geopolitical; environmental; societal; biosecurity (including health); economic (CRA L83–89, p5; list at L279–358, p11–13). One of the 26, "Impacts from the use of end-to-end encryption", is listed but not assessed: "Analysis of both the short and long-term impacts … are under review" (CRA L286–287, L355–358). The list's column header reads "Theme / Drivers / chronic risk" (CRA L279–282), and each theme opens with a framing paragraph (e.g. technology, CRA L848–867, p27).

### 3.2 Method

> "Chronic risks require a novel assessment approach. Their systemic and enduring nature make traditional, probabilistic impact assessments less effective. To address this, the Government Office for Science and the Cabinet Office developed a new method using futures and systems thinking" (CRA L145–149, p7)

The method has three steps (CRA L145–161):
1. **evidence gathering**, from literature "tested and iterated via challenge from cross-government and academic experts";
2. **futures work**, using "pre-existing government scenarios and futures workshops" and the GO-Science Futures Toolkit;
3. **impact mapping**, "to identify which chronic and acute risks were most likely to interact with each other to develop the systematic risk scenarios and the case study system".

Those systemic-risk scenarios and the case-study system are not in the public document. Risks were "chosen through consultations with both government and external experts" (CRA L160–161).

### 3.3 The shape of a chronic-risk assessment

Each assessment runs 4–5 pages with fixed fields. The example is "Changes in the nature of cyber security threats", CRA L868–1022, p28–31; AI is at L1333–1486, p40–43.

| Field | What it holds |
|---|---|
| **Definition** | Usually a *characterisation* of the risk, not a definition of a term: "Cyber attacks, such as ransomware, continue to pose a significant and ongoing threat…" (CRA L877–879). |
| **Current evidence** | A snapshot, with headline statistics in sidebars ("43% of UK businesses experienced cyber attacks within a year", L889–890). |
| **Example vulnerabilities** | Groups, sectors or conditions that are exposed ("Lower-income individuals, older adults, and people with certain disabilities are at greater risk of cyber crime…", L907–910). |
| **Example mitigations** | Existing activities and policies, "but may not represent current government policy" (L155–157). |
| **Examples of additional benefits from taking action** | Co-benefits of mitigation. |
| **What the future might hold** | Split into **Short-term trajectories** and **Longer-term uncertainties** (e.g. L956–979). |
| **Example connections with other chronic and acute risks** | A diagram. Nodes are chronic or acute risks. Edges carry short causal sentences ("Lower barriers to offensive cyber tools give terrorists' new capabilities they couldn't previously access", L992–994). |

### 3.4 The interaction network

> "Chronic risks do not operate in a vacuum and are instead interlinked with other chronic and acute risks. Chronic risks can therefore have both direct and indirect cascading impacts on vulnerabilities that gradually erode our economy, environment, way of life, and/or national security." (CRA L4421–4424, p128)

The network has three node types: chronic risk, acute risk and **vulnerability**. "Each vulnerability is represented by this unique shape. Each risk is represented by a circle" (CRA L4490–4492). "Groups of people" is a vulnerability node. Edges are directed, and in the groups-of-people visualisation they are scored:

> "Diminishing — The risk weakens or lessens the impacts of the other risk or lessens the negative impacts on the vulnerability. Reinforcing — The risk exacerbates or increases the impacts of the other risk or increases the negative impacts on the vulnerability." (CRA L4491–4498, p130)

The document then reads structure from the graph, as a kind of network analysis (CRA L4421–4473, p128–129):
- "Challenges to international institutions has the largest number of direct impacts on other risks and vulnerabilities";
- "State threats has the largest total number of direct impacts … 11 in total" into acute risks;
- risks "at the edge of the network … may require more targeted mitigation methods";
- risks "affected by numerous other risks but with minimal direct impacts themselves may signify the final stage in a cascade. These include vulnerable persons and biological data";
- it also notes conflicting interests, e.g. digital reliance increases exposure "but also connects geographically isolated locations" (CRA L4453–4456).

Only "an example section of a full impact map" is published (CRA L4465–4467), and that shows only chronic risks (footnote, L4509). The counts above therefore describe a network the reader cannot see.

### 3.5 Interventions

For the workshop method it hands to readers, the CRA classifies interventions (CRA L248–257, p10):
- **Mitigate**: "what to change now to reduce the impact";
- **Adapt**: "what to change to cope with the impact";
- **Exploit**: "what to take advantage of";
- **Continue**: "what you can keep doing regardless";
- **Terminate**: "what do you need to begin closing down".

## 4. Method and lineage

- **NSRA as the base.** "The NRR is based directly on the NSRA – an internal, classified risk assessment" (NRR L212–214). "The NSRA is produced using a rigorous and well‑tested methodology, based on international best practice. It draws on input and challenge from hundreds of experts" (NRR L216–224). "The UK has improved its approach to assessing these risks over the last two decades" (NRR L136–138).
- **Ownership.** "Risks are owned by departments or other government organisations, who are responsible for assessing the impact and likelihood of their risks." (NRR L373–375)
- **Expert challenge.** "risks are reviewed by panels of technical and scientific experts, each led by an independent chairperson. Each panel is focused around different impact dimensions" (NRR L483–486, p16). Their role is to supplement, identify uncertainty, resolve scoring inconsistencies, improve communication and identify long-term trends (L489–495). The foreword adds a "refreshed Expert Advisory Programme" that challenges "'Groupthink' and conventional wisdom" (NRR L151–153).
- **Borrowed calibration.** Likelihood words come from the intelligence community's PHIA yardstick (§2.3).
- **Revision.** The NSRA is now "a dynamic assessment process" with risks "updated as frequently as needed" (NRR L147–151, L362–364). Edition changes are listed: new risks, a removed one ("The disruption of Russian gas supplies to Europe risk has been removed as reliance on Russian gas imports has significantly reduced", L269–271), rescoring, and new text sections (L247–272, p9). New risks are explicitly motivated by events ("digital resilience failure – to reflect learning from incidents such as the Crowdstrike IT Outage in July 2024", L245–246).
- **COVID-19 as a stated lesson.** It is named as "The most significant risk to materialise in the UK in recent years". Pandemic planning "has been based on influenza", and lessons led to "including multiple and varied scenarios" (NRR L283–301, p10).
- **CRA lineage.** GO-Science futures and foresight (the Futures Toolkit; PESTLE; futures wheels, CRA L206–237), plus systems thinking. It is "developed and tested both within and outside of government" (CRA L131–133).

## 5. Purpose, audience, force

- **NRR purpose:** "to enable relevant bodies to undertake proportionate planning" (L380–381); a "transparent by default" approach (L214, L287–288); the basis of local **Community Risk Registers** (L383–385, L299–307).
- **NRR audience:** practitioners (including voluntary and community sector), businesses and CNI operators, academics. "This edition of the NRR is available to all but not targeted at the general public" (NRR L319–344, p11).
- **CRA purpose:** shared understanding, business planning information, thinking about interconnection, prompting preventative measures (CRA L117–129). Its audience is practitioners, businesses, academics and policymakers, "for whom tailored versions of this analysis will be of increased relevance" (CRA L172–192). So non-public versions exist.
- **Force.** Neither document imposes duties on outside parties. Internally, risk owners "must also evidence how chronic risks … manifest in, interact with and exacerbate acute events" (NRR L673–678). The CRA disclaims that its mitigations are policy (L155–157), "is designed to complement, not replace, existing plans or strategies", and is "a snapshot in time" (CRA L135–138).

## 6. How uncertainty is handled

- **In the NRR, through the choice of scenario.** The RWCS is the worst *plausible* case after discounting "highly unlikely variations". The document states the scenario's assumptions and names alternative Variations, some placed explicitly as lower-impact / higher-probability.
- **By scale design.** Log scales on both axes; score 5 is an open band (>25%).
- **By confidence ratings** (low / medium / high) based on evidence quality, assumptions and external factors, and by uncertainty lines on plots, so as not to plan "with false confidence" (§2.5).
- **In the CRA, by refusing point estimates.** It uses futures framing, a Short-term / Longer-term split, and the declaration "This analysis is not about predicting the future" (CRA L131). The ministerial foreword adds: "None of the risks are static; each one is evolving … This assessment represents a snapshot in time" (CRA L52–55).

## 7. What the model excludes

- From the NRR: chronic risks (§1); risks that don't reach the national-impact threshold; completeness ("do not aim to capture every risk"); highly unlikely variations; much international impact from scoring; classified detail. Some risks are "not shown in the matrix above or are grouped together due to national security or commercial implications" (NRR L673–675). "A separate scenario involving a nuclear attack on the UK mainland or UK overseas interests exists and is held internally at a higher classification" (NRR L7566, p221).
- From the CRA: numeric likelihood and impact; causal quantification of the network edges (they have direction and sign, not magnitude); the full network; one of the 26 risks (encryption, under review); the systemic-risk scenarios.
- **Both documents are about the UK.** Harms abroad count mostly through their effect on the UK and on British nationals.

## 8. Where AI appears, and how

**In the NRR, AI is a modifier of acute risks, not a risk itself.**
- It is placed by definition with the chronic risks: "in relation to AI, the government is focusing on how it develops and proliferates. The growth and use of AI may exacerbate NRR risks but also provide opportunities to mitigate them" (NRR L655–657, p20).
- It enters risk summaries mainly through one templated sentence: "AI can automate the process of launching cyber-attacks … [the sector] will continue to monitor how current and emerging AI influences this risk". It appears at NRR L1689, L1838, L2043, L2217, L2362, L2429, L2497, L2571, L3721 and L7392, with variant wordings at L2296, L3644 and L5199. These are energy, fuel, transport, telecoms, data, water, police, civil nuclear, PNT and space risks.
- The fullest statement is in the health and social care cyber risk: "AI is increasing the scale, speed and volume of cyber attacks … AI is accelerating the discovery and exploitation of vulnerabilities, reducing the time organisations have to respond. The widespread adoption of AI is also expanding the attack surface and systemic risk, particularly through complex systems and emerging 'agentic AI', where autonomy, access, and unclear ownership can significantly amplify the impact of failure." (NRR L2152–2163, p66)
- One risk names the AI Security Institute: "DSIT and the AI Security Institute are continuing to explore how current and emerging AI will continue to influence this risk going forward" (national disruption to data infrastructure, NRR L5199–5201, p153).
- The foreword lists "rapid AI developments" among 2026's pressures (NRR L127).
- **In every AI mention in the NRR (found by a full-text search), AI sits in the risk's context paragraph, not in the scenario itself.** It is an accelerant of cyber attack and a subject to monitor. The health-and-care paragraph comes closest to treating AI as a failing component ("agentic AI … can significantly amplify the impact of failure"). No scenario has an AI system as its actor.

**In the CRA, AI is one assessed chronic risk, and a recurring driver inside others.**
- The dedicated assessment is "Impacts from use and capability of artificial intelligence (AI)" (CRA L1333–1486, p40–43). It defines AI as "machines performing cognitive functions like learning, reasoning, decision-making, and problem-solving" and focuses "on risks from cutting-edge frontier AI, highly capable models that can perform a wide range of tasks" (L1343–1356). Its contents:
  - evidence of compute growth ("doubling every 3-4 months", L1369–1370);
  - bias, data poisoning, privacy, misuse and labour-market impacts (L1375–1395);
  - vulnerabilities (L1377–1388);
  - mitigations naming the AI Security Institute and the Laboratory for AI Security Research (L1414–1426);
  - short-term trajectories: AI-enabled disinformation, and open-source models empowering "less sophisticated malicious actors" (L1417–1423);
  - longer-term uncertainties: job displacement, and "an AI arms race may ensue" (L1425–1435).
- Its connections diagram links AI to:
  - CBRN attack: "Frontier AI may be used to design bioweapons";
  - cyber attack: "AI could be used to orchestrate increasingly sophisticated cyber attacks";
  - serious and organised crime;
  - fraud;
  - disinformation;
  - dominance of global tech companies: "Frontier AI tools tend to be owned by global tech companies … further concentrating their power";
  - vulnerable persons (L1453–1481, p43).
- AI also appears as a driver inside other chronic risks:
  - terrorism: AI used "to uplift their capability to perform cyber attacks, run disinformation campaigns and facilitate the design of biological weapons" (L429–431);
  - serious and organised crime (L594–596);
  - fraud (L711–713);
  - state threats (L1738–1739);
  - disinformation (L2856–2858);
  - engineering biology: "combining artificial intelligence and EB to create engineered biological weapons" (L3719–3721);
  - skills (L4257–4259).
- "Artificial intelligence" is a node in the published network view (L4526).
- **Absent from both:** loss of control, misalignment, autonomous replication, and AI systems as actors in their own right. The CRA's AI risk is about human use, capability diffusion, economic effects and concentration.

## 9. Key terms as this model uses them

"Undefined" means the word is used, sometimes heavily, but never given a definition in these two documents.

| Term | Meaning in this model | Verbatim / reference |
|---|---|---|
| **risk** | Undefined as a general concept. In the NRR it names a class of emergency *and* its scored scenario, counted as a unit ("87 standalone risks, and 8 linked scenarios for a total of 95 risks"). In the CRA it names a long-term trend. | NRR L673–674. Used but undefined. |
| **acute risk** | A discrete emergency-triggering event. | "discrete events that may require an emergency response from the government" (NRR L649–650). "those events severe enough to require an emergency response from the UK civil contingencies system" (CRA L113–115). |
| **chronic risk** | A long-term, continuous erosion. | "longer-term challenges that erode our economy, community, way of life and/or national security. They can also increase the likelihood and impact of acute risks" (CRA L111–114). "Generally, but not always, these manifest over a longer timeframe" (NRR L660–661). |
| **reasonable worst-case scenario (RWCS)** | The assessed instance of a risk. | "the worst plausible manifestation of that particular risk (once highly unlikely variations have been discounted)" (NRR L376–380; also L204–208). Once called "a plausible worst‑case scenario manifestation" (L500–501). |
| **threat** | A malicious risk; an actor with intent. | "malicious threats from actors who seek to do us harm" (NRR L199–200). Used, not formally defined. |
| **hazard** | A non-malicious source, especially natural or environmental (a chapter heading), and in regulatory names ("major hazard (COMAH) site"). Not a system state or a harm. | "non‑malicious, such as accidents or natural hazards" (NRR L197–198). Used but undefined. |
| **likelihood** | P(RWCS occurs at least once in the window), banded 1–5. | NRR L404–410, L422–425; Table 2 (§2.3). |
| **probability** | Not a working term. Appears in "lower‑probability variation" and the CRA's rejection of "traditional, probabilistic impact assessments". | NRR L5551; CRA L145–147. |
| **impact** | A score, 0–5 per dimension, combined to 1–5, of "the harm that the reasonable worst‑case scenario could foreseeably cause". | NRR L449–458. Seven dimensions at L443–470. |
| **harm** | What impact measures. Not separately defined. | NRR L451–453. Used but undefined. |
| **catastrophic** | Impact score 5. | "Risks assessed to have the highest impact score (5) are considered catastrophic" (NRR L456–458). |
| **severity** | Informal. Not a scale name (the scale is "impact"). | e.g. NRR L202 "different levels of severity". Used but undefined. |
| **confidence** | Low / medium / high on each score. | NRR L532–541. |
| **vulnerability** | Four senses. (1) **vulnerable people**, as defined in the next row. (2) **Target vulnerability** as one of the three inputs to malicious likelihood. (3) The CRA's "Example vulnerabilities" field (exposed groups, sectors, conditions). (4) A CRA **network node type**, distinct from risks. | (2) NRR L416–418. (3) e.g. CRA L905–920. (4) CRA L4421–4424, L4490–4492. |
| **vulnerable people** | Individuals or communities who may be disproportionately impacted. Risk-relative and non-fixed. | "individuals or communities who may experience more significant and disproportionate impacts during emergencies" (NRR L881–883; definition credited to the Resilience Action Plan). |
| **capability** | Two opposite senses. (1) **Response capability**: government's generic means of response (23 of them). (2) An **attacker's capability**, one of the inputs to malicious likelihood. The CRA also speaks of AI "capability". | (1) NRR L383–393. (2) NRR L416–418. CRA L1338–1339. |
| **common consequences** | Consequence types shared across risks. The cause-agnostic planning layer. | "shift focus away from the risk themselves, to the common consequences" (NRR L379–380). Per-risk lists. |
| **variation** | An alternative manifestation of a risk beside the RWCS. | Per-risk field, e.g. NRR L5537, L5551. |
| **key assumptions** | Conditions the RWCS assumes. | Per-risk field, e.g. NRR L2144–2149. |
| **threshold** | (1) The qualitative bar for NRR inclusion. (2) In other senses: regulatory scope thresholds, and NATO's Article 5 threshold. Not a risk tier. | (1) NRR L195–197. (2) L1682, L7491, L7537. |
| **risk owner** | The government department that assesses a risk. | NRR L373–375; L673–676. |
| **driver** | A chronic risk seen from the acute side. | "these enduring drivers" (NRR L240); "Theme / Drivers / chronic risk" (CRA L279). Used but undefined. |
| **reinforcing / diminishing** | The sign of a directed interaction. | CRA L4491–4498 (quoted in §3.4). |
| **mitigation** | CRA: existing actions against a risk, "may not represent current government policy". In the workshop method, one of five intervention types ("what to change now to reduce the impact"). The NRR speaks instead of *response*, *recovery* and *capabilities*. | CRA L155–157, L251. |
| **incident / event** | An ordinary-language occurrence. "Event" is used in the definition of acute risk. Neither is defined. | Used but undefined. |
| **emergency** | What an acute risk would require a response to. | Used but not defined in either document. The statutory definition, in the Civil Contingencies Act 2004 by my background knowledge, is not quoted. |
| **safeguard** | Not a risk-control term here. It appears only in the social-care sense ("safeguarding") and in "an additional safeguard against acquisition by adversarial actors". | NRR L2762, L5814; CRA L3720. |
| **loss of control; alignment; developer / deployer; risk factor** | **Not used** in either document. "Provider" appears only as service provider, and "alignment" only in the everyday sense (e.g. "Table 2 … alignment of the final 1-5 likelihood score"). | Grep counts: zero, or everyday senses only. |

## Closing note: where this lines up with, and cuts across, Joseph's chain

*(My reading, kept short. It is secondary to the description above.)*

- **It lines up in the middle and at the end.** The RWCS is exactly an "ideated" risk-event with an assessed likelihood. The seven impact dimensions with bands, plus "impact on vulnerable people", are an impact radius with both a degree/scale tree and harmed groups. "Response capability requirements", "Recovery" and the common-consequences → capabilities funnel are "mitigations & recovery".
- **It cuts across at the front.** The NRR is **deliberately cause-agnostic**, planning for consequences whatever produced them. The only causal structure inside an acute risk is the intent × capability × vulnerability composite for malicious likelihood. Prevention barely appears. Causes live in the *other* register: the CRA's chronic risks are the UK's "sources & causes" layer, and its network is a signed causal graph. So the UK splits Joseph's chain at the event and gives the two halves different methods: probabilistic scoring for the event and its consequences; futures and systems mapping, with no probabilities, for the drivers.
- **"Recorded" events** appear only as motivation (a risk added "to reflect learning from" an incident) and as context paragraphs, never as data in the model.
- **Policy** is outside the model on purpose ("may not represent current government policy").
