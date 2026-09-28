# Feedback on SCHEMA-SYNTHESIS draft 1 — from the UK-government atlas (uk-gov.md)

*From the agent that wrote `uk-gov.md` (25 documents: NCSC, DSIT, Cabinet Office registers, GO-Science, NPSA, Five Eyes, ASD-led joint guidance, ETSI). References are `key L…` into the atlas extractions, as in the synthesis. Where I went back to a PDF I say so. Everything else comes from my first-pass reading, and I've marked where a point is my reading rather than something checked.*

**Overall:** the four-record shape fits my family. My documents give it no reason to keep causal edges as the organising structure: most of what they say is assessment, recommendation, scenario and status. The points below concern where the draft would flatten something, or is missing a slot.

---

## 1. Your summaries of my findings

They are accurate. Three refinements:

- **HMG → DSIT.** Besides the subject change ("Generative AI" → "Frontier AI"), DSIT also dropped HMG's tail "seeking to conduct previously unattainable attacks" (hmg-2023-safety L118–120 → dsit-2023-capabilities L901–902, citing endnote 192 at L2078). So the change is subject replaced *and* predicate truncated. A "changes marked" field needs to hold more than one edit.
- **DSIT → ETSI.** The deeper point isn't the fossil word "voluntary". It is that **identical provision text carries different force in different containers**: a voluntary UK code (dsit-2025-ai-cyber-cop L220–234, a shall/should/may table defined "in the context of the voluntary nature of this Code"), then a European Norm with national transposition and withdrawal dates for conflicting standards (etsi-2025-en304223 L158–163) and its own modal rules ("must" not allowed, L168–173). Force belongs to the passage-in-document, not to the text. Lineage copies wording but not force. §2a already puts force on the document, which is right. §5 should say explicitly that force is not inherited through "derived from".
- **Planning assumptions.** Correctly reported, but §3 files them under "adopted assumption" alongside Meta's "we assume". I'd split them (see §4 below).

## 2. A contradiction: calibrated likelihood is not confined to NCSC and *Loss of Oversight*

§4 says "Only NCSC and AISI's *Loss of Oversight* use a calibrated scale". In my family:
- `hmg-2023-safety` uses PHIA words throughout ("almost certainly", "highly likely", "realistic possibility"; e.g. L30, L54, L86–89, L105–106, L207–217). It does not print the yardstick.
- `dsit-2023-capabilities` inherits PHIA words through its HMG citation (L901).
- `cabinetoffice-2026-nrr` prints the yardstick with numbers and maps it onto its own 1–5 score (Table 2, L402–426, **PDF p14, checked against the PDF**).
- The two NCSC assessments (`ncsc-2024-near-term` L55–63, `ncsc-2025-impact` L27–36) print the yardstick only as a graphic, which the extraction lost. Their words are calibrated, but the calibration is not in our text.

## 3. Likelihood needs more structure than one axis (checked against the NRR PDF)

The NRR Table 2 mapping, as printed on PDF p14: **score 5 (>25%) = Almost certain (95-100%), Highly likely (80-90%), likely or probable (55-75%), Realistic possibility (40-50%) and Unlikely (25-35%); score 4 (5-25%) = Highly unlikely (5-25%); score 3 (1-5%) = Remote chance (0-5%); scores 2 and 1 have no PHIA word.** Two calibrated UK government scales therefore resolve completely different regions: PHIA spends five words above 25%, while the NRR spends three scores below 5%. What follows for the schema:

- **Scale identity** has to be recorded (PHIA yardstick as printed where; NRR 1–5; others). "Highly unlikely" is 5–25% in this table. The PHIA ranges printed there leave gaps between the words above 25%. I have not checked this printing against other editions of the yardstick. The same word is not safely the same number across documents.
- **What the probability is *of*.** In NCSC-A, PHIA words attach to propositions about trends over a stated horizon ("AI will almost certainly increase the volume … over the next two years", ncsc-2024-near-term L68–69). In the NRR, likelihood is "the percentage chance of the reasonable worst-case scenario occurring at least once in the assessment timescale", 5 years for non-malicious and 2 years for malicious risks (nrr L404–408, L422–424). So a likelihood assertion needs its **reference** (proposition vs defined scenario) and its **window**.
- **Composite likelihood.** For malicious risks, intent, capability and vulnerability are "collated together to form one likelihood score" (nrr L416–421). This is a decomposition claim like the Anthropic R formula in §1, in government form.
- **Confidence is a separate axis from likelihood.** Low / medium / high, based on evidence quality, assumptions and external factors (nrr L532–549). It is not the same as "knowledge state".
- **Impact is multi-dimensional with banded thresholds.** Seven dimensions scored 0–5 and combined (nrr L437–470). Example thresholds, e.g. fatalities 1-8 / 9-40 / 41-200 / 201-1,000 / >1,000 (Table 3, L481–496). Both scales are logarithmic (L503–508, L527–530). This is the nearest thing in my set to Joseph's "degree/scale tree" for the impact radius, and it should be a precedent row (§9 below). "Signs, not magnitudes" can stand for *our* quantities, but these source magnitudes have to be carried verbatim as structured qualifiers, not flattened to prose.

## 4. Stance: "adopted assumption" is three different things in my family

1. **The author's analytic assumption, conditioning the author's own claims.** "The assessment assumes no significant breakthrough in transformative AI in this time period. This assumption should be kept under review" (ncsc-2024-near-term L109–112). "Assuming a lag, or no change to cyber security mitigations, there is a realistic possibility…" (ncsc-2025-impact L47–49). Also the NRR's per-scenario "Key assumptions" field (e.g. nrr L2144–2149, L7552–7555). These belong on the **condition** axis of the claims they scope.
2. **An assumption prescribed to the reader.** "defenders should assume that at least some attackers already have access to capable AI tools" (ncsc-2026-frontier-defenders L19). "assume breaches will occur" (fiveeyes-2026-ai-shift L71). "organisations should assume that agentic AI systems may behave unexpectedly" (asd-2026-careful-agentic L984–986). These are **recommendations about belief**, addressed to a role. The author may hold the proposition too, but the text is directing the reader.
3. **Precautionary treat-as.** In my family this appears mostly in 2023 DSIT as "Adapt mitigations … the use of caution may be helpful" (dsit-2023-emerging-processes L495–497). Your co-anthropic examples are better ones.

Suggestion: give norms, recommendations and prescribed assumptions an **addressee** field, separate from the author (see §7).

## 5. Scenarios: one kind, at least four functions, and one carries scores

§1's "Scenario or illustration" and §3's "hypothetical" would merge these:
- **The reasonable worst-case scenario** (nrr L204–208, L376–380). A defined planning object, "not a prediction", and **the thing the likelihood and impact scores are about**. It has attached **Key assumptions** and **Variations** fields (e.g. L2144–2155). So it is an ideated event that bears quantitative assessment, which is quite unlike an illustration.
- **Exploratory scenarios** (goscience-2023-future L671–716). "Scenarios are not predictions" (L679). They are built from five critical uncertainties by "General Morphological Analysis" (L711–716), with a **stated selection rule**: "we have explicitly avoided including any scenarios that are largely benign or favourable" (L690–695). The set is deliberately skewed, and the schema should record that on the set, not only on each scenario.
- **Illustrative vignettes** (asd-2026-careful-agentic "Scenario example" boxes, e.g. L203–216, L266–277, L288–295, L353–365). Constructed incidents that demonstrate a mechanism.
- **Reader-generated scenarios as method** (cabinetoffice-2025-cra L206–270). No content, only a procedure.

Suggestion: add **scenario function** (planning / exploratory / illustrative / method) and, for sets, a **selection rule**. The RWCS also argues for letting a scenario be the **focal event** of scored assertions, which fits §7's "stage is a role relative to a focal event".

## 6. Recorded events: three relations and one claim form that §2d lacks

- **An event motivates a change to the register.** "digital resilience failure – to reflect learning from incidents such as the Crowdstrike IT Outage in July 2024" (nrr L245–246). Also L251–252 (water sector attacks) and L269–271 (a risk removed as Russian-gas reliance fell). This is event → risk-set revision, the same pattern as Zhu's change outcomes, but applied to a register.
- **An event is cited as evidence for a risk's salience.** The opening paragraphs of NRR summaries name real incidents (DXS, Cl0p/Barts, nrr L2144–2149; Synnovis in cabinetoffice-2025-cra L928–931). This is different from the event being *an instance of* the RWCS.
- **An event is used as an exemplar of a generalisation.** NPSA's case study 02 ends "This incident demonstrates the interconnected and reinforcing nature of personnel, physical, and cyber security" (npsa-2024-secure-innovation L223–227).
- **Existence claims about unrecorded events.** "Recently, there have been several incidents involving AI models and agentic AI systems carrying out unsanctioned or unintended activity" (ncsc-2026-managing-agentic L14–16). No incident is named or described. The schema needs to hold "there were events of kind K" without inventing event records. One option is an assertion whose object is an event *class* with an unknown extension.

## 7. Force, addressee and mood

- **Addressee as a field.** Provisions are "Primarily applies to: System Operators, Developers…" (etsi L517 and each principle). The governance code's 22 actions are addressed to board members (dsit-2025-cyber-governance L164–283). The NRR's response requirements are split by three responder classes (see §8). Recommendations and norms have an addressee role distinct from their author, and the draft's assertion record has no slot for it. Zhu's "actor" dimension covers commitments, but not recommendations addressed to others.
- **A companion document re-scopes force.** The implementation guide says "Recommendations in the Code are expected to be followed … unless they are not applicable because of the type of model(s) used" (dsit-2025-ai-cyber-cop-guide L171–173). It calls the Code's *shall* provisions "Recommendations". This is an interpretation-of-instrument claim (§1) made by the instrument's own family: the same pattern as Zhu's "relocated to a companion document", in the other direction.
- **Norms in indicative mood.** "You are confident that the task at hand is most appropriately addressed using AI" (ncsc-2023-guidelines-secure-ai L331; the whole guideline body L295–667 is written this way). Any typing by grammatical mood, including an LLM first pass, will code these as observations. NIST 3.3's "normative" category catches them only if coders are warned. I'd flag this where assertion typing is specified.

## 8. Roles: the responder side is missing from §7

§7 has the agent-facing, supply-chain, legal, control and harmed sides. My family supplies a **response and recovery side**, which is Joseph's "(mitigations & recovery)" stage:
- NRR "Response capability requirements" in three actor classes: Government and Agencies / CNI owners and operators and the wider private sector / Voluntary, Community and Faith Sector (nrr L265–272; e.g. L2156–2172).
- **"Common consequences"** on every summary, feeding "23 generic response capabilities" as a "cause-agnostic basis for planning" (nrr L389–393). Structurally: many risks → shared consequences → generic capabilities. This is a many-to-one bridge between the risk-event and mitigation stages of the chain.
- ETSI supplies an **in-source crosswalk** between its roles and EU AI Act roles ("Developers can be AI providers under the EU AI Act…"; "System operators can be deployers … and can also be AI providers if they make changes to the system", etsi L459–461, L471–473), and says one entity can hold several roles (L434–436). That makes it a precedent for roles resolving to several referents.
- Governance roles as addressees: board, directors, "senior ownership" (dsit-2025-cyber-governance L164–283).

## 9. Harmed groups: support for stage-as-role, with a sharper statement from the NRR

- **Vulnerability is relative to the focal risk.** "Individuals who might be considered vulnerable in the context of one risk might not be for another. For example, older adults might be considered more vulnerable in some virus outbreaks, however, could potentially have higher levels of preparedness for a significant power outage" (nrr L902–907, p26–27). Also "Vulnerability is not a fixed characteristic" (L883). This is §7's "stage is a role relative to a focal event", applied to harmed groups. An impact-radius group is a role in an impact assertion, not a fixed attribute of people.
- **Mitigation can harm.** Principle 5: "consider how response and recovery actions … may inadvertently create new forms of disproportionate impacts" (nrr L918–921). This supports "good and bad live on relations": a mitigation edge can carry a harm edge.
- **In the CRA, vulnerable groups are both a node and a target.** "Disproportionate impact on vulnerable persons" is itself one of the 26 chronic risks (cabinetoffice-2025-cra TOC L7), and "vulnerable persons" is where cascades end (L4463–4467). So the same group appears as a risk and as an impact target.

## 10. Lineage: kinds §5 lacks

- **Summary-of, with additions.** `ncsc-2026-thinking-agentic` is a blog summary of `asd-2026-careful-agentic` (thinking-agentic L7–12). It lists "loss of control" among incident types (L112). **The ASD guidance never uses the phrase** (checked by grep: no "loss of control", "lose control" or "losing control"). The summary introduced the term. Lineage needs "summary of", and the changes marked in it include *additions*, not only losses.
- **Within-document boilerplate.** The NRR repeats one AI sentence across about ten risk summaries (nrr L1689, L1838, L2043, L2217, L2362, L2429, L2497, L2571, L3721, L7392; variant wordings at L2296, L3644, L5199). Counted as occurrences, it looks like ten corroborating judgements. It is one template, so lineage-aware counting has to work *within* documents too.
- **Identical sentences, different bindings.** The DSIT code and the ETSI EN share every provision word for word, but their glossaries differ. DSIT defines *Artificial Intelligence* (dsit-2025-ai-cyber-cop L681–685); ETSI drops it and defines *AI system* ISO-style (etsi L344–345). So "AI system" in the *same sentence* resolves through different scopes depending on the container. This is a clean worked example for §6: resolution is per occurrence-in-scope, not per sentence.
- **Derived vocabulary.** The implementation guide adopts the Code's terms and **extends** them (*Agentic Systems*, *Excessive Agency*, *Hallucination*, *Prompt Injection*…, dsit-2025-ai-cyber-cop-guide L99–164; "the terms given in the UK Government's Code of Practice apply", L57). That is a scope that imports another scope and adds bindings, which address theory can express if imports are modelled.

## 11. Resolution (§6): three hazards from my documents

- **Fields labelled "Definition" that don't define.** Every CRA risk page has a "Definition" box that usually holds a characterisation ("Cyber attacks, such as ransomware, continue to pose a significant and ongoing threat…", cabinetoffice-2025-cra L877–879). A glossary harvester keyed on the label would mint false bindings. A "mediated through the source's glossary" path needs a check that the definition defines.
- **Indexical definitions.** "match or exceed the capabilities present in **today's** most advanced models" (hmg-2023-safety L19–23; dsit-2023-capabilities L96–99; goscience-2023-future L1364–1366). The CRA drops the anchor altogether ("highly capable models that can perform a wide range of tasks", cabinetoffice-2025-cra L1353–1355). Contrast "the most capable models available **at any given time**" (ncsc-2026-frontier-defenders L52). The first fixes its referent set at the document's date (Oct 2023). The second moves. The resolution record needs the document date as an input, which is the same phenomenon as your SB 53 drift, but in definitions rather than in a statute.
- **A definition that contradicts its own term.** "Affected entities: Encompasses all individuals and technologies … that are **not directly affected** by AI systems" (dsit-2025-ai-cyber-cop L170–172, copied into etsi L504–508). "Ambiguous among named candidates" doesn't fit this: the text is unambiguous and self-contradictory. I'd add a resolution outcome such as **"defective as written"**, keeping the verbatim text and our reading of the probable intent ("indirectly") as a separate attributed assertion.

## 12. An axis the draft lacks: reversibility

It recurs across my family as a load-bearing property of actions, deployments, impacts and dependence:
- actions: "classify agent actions by potential impact, likelihood and reversibility" (asd-2026-careful-agentic L856–857); "prioritising resilience, reversibility and risk containment" (L986); *Recoverability* as one of five dimensions of defensive-action risk (ncsc-2026-defend-agentically L145–155);
- deployments: "Irreversible deployment e.g. open-sourcing" (dsit-2023-emerging-processes L489); "Deploy models in small-scale or reversible ways before … irreversible ways" (L512–514); "API access is reversible" (dsit-2023-capabilities L668);
- impacts and dependence: "loss of control could be permanent and catastrophic" (dsit-2023-capabilities L1101–1102); "eventually become irreversibly dependent" (goscience-2023-future L1129); NRR "Recovery" fields with durations (e.g. nrr L2180–2186).

It belongs with degree and scale in the impact radius, and on control and deployment actions. The sources treat it as distinct from severity.

## 13. Precedents the draft missed

| Precedent | Where | What it gives | Correlation to mark |
|---|---|---|---|
| **NRR/NSRA methodology** | cabinetoffice-2026-nrr L187–275, L353–558, L643–678 | The reasonable worst-case scenario as the scored focal event. Likelihood as P(occurs ≥ once in window) with an explicit window. The composite intent × capability × vulnerability. Confidence as a separate rating. Seven impact dimensions with banded thresholds (a degree/scale tree). Common consequences → generic capabilities. Responders by class. The six principles on vulnerable people (L874–927). | UK government. Underlies the classified NSRA, so the public text is a declassified subset (L212–214, L673–675). |
| **ASD-led endorsement of STPA** | asd-2026-careful-agentic L948–968 | Six national cyber agencies recommend STPA, STPA-Sec and CAST for agentic AI. That is independent institutional support for your STPA row, and CAST for incident analysis fits §2d. | Cites MIT STAMP materials; same Leveson lineage as Barrett. |
| **Riskiness of an automated action** | ncsc-2026-defend-agentically L86–157 | A five-dimension × 0–4 scale (Potency, Scope, Criticality, Rollout confidence, Recoverability) for a *control action* rather than a hazard. The extraction garbles the table. | A single-author blog (CTO for Architecture). |
| **Control maturity ladders** | ncsc-2026-managing-agentic L253–259, L282–292 | Ordinal strength scales for *controls* (network isolation, compute isolation, Levels 1–4). The mitigation side of the chain needs a strength vocabulary as much as commitments do. | Interim advice, to be superseded (L49–53). |
| **GO-Science scenario method** | goscience-2023-future L424–432, L671–716 | Scenarios generated from named critical uncertainties, with a declared selection rule. | GO-Science is also CRA co-author, and its Futures Toolkit is the CRA's method (cabinetoffice-2025-cra L152–157). |

## 14. The CRA precedent row: three caveats for the next draft

- **The full network is not published.** The cross-cutting text reports counts over the full network ("State threats … 11 in total", L4436–4438; "impacts 19 risks … only impacted by two", L4455–4457). What is shown is "an example section of a full impact map" (L4465–4467), and footnote 353 says only chronic risks are shown (L4509). These are claims about a graph the reader cannot see, the same "withheld content" pattern as the NRR's classified scenarios and group-averaged scores.
- **Polarity lives in one visualisation.** "Reinforcing / Diminishing" is the scoring legend of the groups-of-people map (L4487–4498). The **per-risk "Example connections" diagrams** (e.g. the AI one, L1453–1481) have edges labelled with **causal sentences** ("Frontier AI may be used to design bioweapons" → CBRN attack) and a key that marks only node type (chronic / acute). Those sentence-labelled edges are the richer claim source. They have direction but no polarity.
- **The network crosses documents.** CRA edges point into NRR acute risks (state threats → 11 acute risks, L4437–4438), and the NRR requires risk owners to "evidence how chronic risks … manifest in, interact with and exacerbate acute events" (nrr L673–678). The two registers form one network across two documents, so an edge's endpoints can be nodes minted in different documents.

## 15. One distortion risk to guard against: scores disclosed only as group averages

The NRR summary for "Cyber attack: health and social care system" ends with a score box, but the scores are the **group average** for "cyber attacks on infrastructure" (impact 3, likelihood 4 (5–25%)), published that way for classification reasons (nrr L2181–2184, confirmed on PDF p67; the rationale is at L551–558, L594–603). A compiler attaching "likelihood 4" to the health-sector risk would put a claim in the source's mouth that it declined to make. The schema needs an **aggregation / disclosure** qualifier ("value is the mean over group G; the individual value is withheld") on quantitative assertions.

---

**Nothing to add** on §8's Zhu, NIST and Slattery rows, or on §10's format question, from my family's evidence.

I'm staying on the line.
