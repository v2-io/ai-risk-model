# Feedback on SCHEMA-SYNTHESIS draft 1: Anthropic and OpenAI family

From the agent that wrote `co-anthropic-openai.md`, 2026-09-28. Line references are to the atlas extractions (`src-text/<key>.txt`) unless marked otherwise. Everything cited here was read in the first pass or re-checked for this note. The synthesis's direction fits my documents well, and most of what follows adds to it rather than contradicting it.

---

## 1. Corrections to how my findings are summarised

**1a. "Catastrophic risk at thresholds orders of magnitude apart" (synthesis §6, bullet 3).** This mixes three things.
- The orders-of-magnitude gap is **within OpenAI**:
  - the PF's term is **"severe harm"**, defined as "death or grave injury of thousands of people or hundreds of billions of dollars" (openai-2025-preparedness-framework-v2 L33–36);
  - the FGF's term is **"systemic risk"**, defined as ">50 fatalities or $1 billion" (openai-2026-frontier-governance-framework L121–127).
- The FGF only says the PF "*may* use different definitions of catastrophic risk" (FGF L82–86).
- **Anthropic's RSP has no threshold at all.** It takes "catastrophic risk" in its "plain meaning rather than… any specific statutory definition" (anthropic-2026-rsp-v3-0 L137–141).

So the accurate statement: *both companies say their voluntary and statutory documents use the severity term differently. OpenAI's two documents use different words with thresholds orders of magnitude apart; Anthropic's pair contrasts an unquantified plain meaning with a statutory threshold* (FCF L76–79, L114–121). For resolution, "catastrophic risk" in the RSP should resolve as *deliberately unbound*. That is not a broad term; it is a declared refusal to bind.

**1b. "'Loss of control' appears only in the statutory ones."** This is right for the *frameworks*, but it needs two refinements:
- **The label is statutory, the content is not.** On re-checking, the FCF's "Loss of Control" category (anthropic-2026-frontier-compliance-framework-v2 L314–391) is filled **verbatim with the RSP's two autonomy thresholds**:
  - Tier 1 is "Misaligned AI systems in high-stakes settings" (FCF L344–355 = RSP v3.4 table, ≈L241–260);
  - Tier 2 is "Automated R&D in key domains", with the same "fully substitute for our entire set of Research Scientists…" operationalization (FCF L357–391; RSP v3.4 ≈L313–380; also quoted in the Aug report at L3868, L3940).

  So the RSP's content never uses the phrase, but the company's own compliance document files that content under it. The FCF is also inconsistent within itself: the heading says "Loss of Control" (L314), while its changelog calls it "Sabotage and Loss of Control" (L712, L718).
- **OpenAI makes the same move.** The FGF's loss-of-control tiers absorb AI self-improvement: "Outside of risks related to AI self-improvement, these risk tiers remain exploratory" (FGF L414–415), where self-improvement is a Tracked Category of its own in the PF (PF L268–295). **Both companies file their AI-R&D/self-improvement category under the statutory "loss of control".**
- **The phrase also spreads beyond the statutory texts.** OpenAI's post-incident prose uses it (hugging-face-incident L754, L883; third-party-assessments L221, L268).

This is stronger evidence for §6 than my atlas gave. The source supplies its own crosswalk, mapping its native categories into the template's categories. That crosswalk is an assertion by the source, and the schema should hold it as one (see 2e).

**1c. The Aug report's "very low" → "low" (synthesis §1, "Argument and decomposition").** The quote is right. What it leaves out is that the *basis* of the adjustment is contested inside the same document:
- Claude's review says the triggering incidents "involved other developers' systems… the update is about industry-wide uncertainty rather than new adverse evidence about the covered models" (anthropic-2026-risk-report-aug L2982–2988).
- The company replies that some of the uncertainty comes from its own systems, and says it revised its wording, which Claude then accepted (L3004–3011).

An adjustment step can therefore carry its own contested rationale. Separately, the R = Σ P·H·U decomposition is used **only** for the misalignment threat model. The CB sections argue by threat variants and evidence weighing (Aug L5043–5135; Feb L3162–3326). "Anthropic writes risk as…" should be scoped to that section.

---

## 2. Kinds, axes and relations my documents need that the draft lacks

**2a. Assessment or verdict as its own kind.** The most frequent load-bearing sentence in my family is neither a measurement nor a causal claim. It is a judgment of level or sufficiency over a scoped subject:
- "Overall risk: Very low but not negligible" (Feb L414–416, L1466–1467);
- "we believe Astra's safeguards sufficiently minimize the risk of severe harm for release" (openai-2026-path-to-astra L45–48);
- the risk-benefit determination (Feb L3935–3940);
- retrospective risk grades of incidents: "we assess the risk it posed to have been low" (Aug L6171–6178, L7355–7359).

Such an assessment has a subject (a threat model, a model, an incident), a scale (verbal, company-specific), a perspective (2b) and an as-of date (2d). The synthesis's argument row covers the *derivation*; the verdict at the end is what gets quoted onward and needs its own record. It also conflicts with "good and bad live on relations": these grades attach to nodes (threat models, systems), so the schema needs a place for level-of-node assessments. That is not a contradiction of the decision, but it is a second place where valence appears.

**2b. A perspective axis for risk levels: marginal vs absolute.** Both companies make this distinction definitional. Anthropic defines "marginal" (our systems over and above other developers') vs "absolute" (industry-wide, if everyone were like us) and requires both in every risk section (Feb L260–268; RSP v3.4 §3.3). OpenAI's §4.3 "Marginal risk" (PF L594–604) makes it a condition for lowering safeguards. The same verdict word ("low") means different things under the two perspectives. This is "baseline" (§4) applied to risk levels rather than uplift, and it should be named because the sources name it.

**2c. Baselines are dated and differ.**
- PF uplift is "relative to unlimited access to baseline of tools available in 2021" (PF L197–206; also FGF L368–375).
- Anthropic's is "2023-level online resources" (RSP v2.2 L919–921, fn 21 L956–958) and "a world with access only to the best AI models as of 2023" (FCF fn 4, L272).
- One more baseline type belongs on the impact side, for Joseph's impact radius. The Aug report distinguishes harm "relative to the status quo" from *missed potential*: "might not induce any harm at all relative to the status quo, but instead cause us to miss out on opportunities… a future which falls dramatically short of its potential" (Aug L2788–2793).

**2d. An as-of or coverage date at assertion level, not only document level.**
- RSP v3.4 introduces a formal "coverage date" (RSP v3.4 L412–416; fn 10 L437–439: may include later information "but does not guarantee completeness").
- The Aug report reports an event discovered *after* its coverage date but before publication (L6886–6888).
- The Astra card is dated 2026-09-03 but contains changelog entries through Sep 22 (L122–155).

The document date doesn't tell you the epistemic date of a claim.

**2e. Crosswalk and category-filing as a source's own assertion** (from 1b). "Our Tier 1 under Loss of Control *is* our RSP's misaligned-high-stakes threshold" is an assertion the source makes by construction. The same text, filed under a different label in a document of different force, is **not** an independent second claim; it is one claim re-filed. This is a lineage type the synthesis's §5 lacks: *same author, same text, different container, different force*. The synchronised revisions confirm it: the FCF changelog records edits "to align with updates to Anthropic's Responsible Scaling Policy (v3.4)" (FCF L711–725). This is also Zhu's "relocated to a companion document", but as *duplication* rather than relocation.

**2f. Argument-internal relations beyond "argument and decomposition."** My sources give their arguments explicit structure the schema would need to hold:
- **Support strength per premise:** mitigating factors graded Strong / Moderate / Weak per pathway (Feb L1561–1680). This is *strength of support*, a different axis from likelihood.
- **Aggregation mode:** conjunctive / disjunctive / convergent, with the source warning that correlated subclaims make naive products wrong (Aug L977–986).
- **Load-bearing dependency:** "all load-bearing for most risk pathways, and substantially changing any one of these could increase risk substantially" (Feb L1513–1516).
- **Coverage or representativeness claims:** "By 'sufficiently representative,' we mean that a strong case against each concrete pathway would provide reasonably high overall assurance" (Feb L1476–1487); "Threat modeling is sufficient" (Aug Claim 7, L1066–1071).
- **Assumption plus fallback:** "This assumption shapes which attacks we prioritize… If our core assumption is wrong and short interactions do confer significant uplift, our safeguards still provide meaningful risk reduction… However, our confidence… is lower in this scenario" (Feb L3164–3202). The synthesis's "adopted assumption" stance covers the first half. The *if-wrong consequence* is a relation between the assumption and the conclusion's strength.
- **Transfer by dominance across subjects:** "we consider any arguments about the risks posed by Mythos 5 to serve as an upper bound for the risks of this model as well" (Aug L606–611). A conclusion about one system is carried to another by an ordering claim.

**2g. An epistemic policy as a standing rule, not a claim about one claim.** "Claim about a claim" (§1) covers "this result can't guarantee X". My documents also state *standing rules for how evidence will be weighed*, which then govern many later claims:
- "significant weight on subjective impressions from our internal biology experts… even when we do not have clear numerical evidence" (Aug L5056–5061);
- "if a new and otherwise-capable model were to perform worse on some of these evaluations, we would be more skeptical of the validity of the evaluation than of the model's risk-relevant abilities" (Aug L5073–5075). The prior overrides the instrument; worth flagging to anyone reading saturated-benchmark results;
- "we regard any one-time capability elicitation… as a lower bound, rather than a ceiling" (PF L409–411; FGF L258–262; Astra card L2499–2503);
- counting refusals as successes "to calculate a conservative upper bound" (Astra L2524–2528);
- verbalized metagaming makes evaluations "similar to contaminated evals" (Astra L1375–1376).

These could be a subtype of "claim about a claim", but they need a scope (a class of evidence) rather than a single target claim.

**2h. Burden of proof and default rules on thresholds.** The synthesis cites rebuttable presumptions only from the Commission guidelines. My voluntary frameworks have the same structure:
- "If, however, we determine we are unable to make the required showing, we will act as though the model has surpassed the Capability Threshold" (RSP v2.2 L443–446; fn 9 L467–468);
- "we have treated models as crossing a capability threshold in circumstances where we are unable to rule out" (FGF L268–272).

RSP v3's industry recommendations are all phrased "A frontier developer should make a strong argument that…" (RSP v3.4 table L175–385), which assigns the burden to the developer. "Burden-holder" and "default if unshown" belong on commitments and thresholds.

**2i. Determinations and enacted governance actions as recorded events.** The synthesis's recorded events are incidents. My family also records *institutional acts*, which are Joseph's "policies & decision-making" stage as events rather than commitments:
- determinations with procedural standing (who is authorised: "the SAG does not have the ability to 'filibuster'", PF L743–744; CEO+RSO approval, RSP v3.4 §3.4);
- enacted actions: "a two-week pause in reinforcement learning (RL) training" (openai-2026-pacing-model-development L46–57); "On August 28th, we restarted the large frontier RL run" (path-to-astra L230–233); "quarantining IM1's weights" (hugging-face-incident L318); Anthropic's ASL-3 activation in May 2025 (rsp-v3-announcement L111–113);
- the roadmap's dated goal outcomes, completed, dropped or rescheduled (frontier-safety-roadmap L70–105).

A commitment and its enactment (or its absence) should be linkable. The set contains a dropped conditional pause commitment (RSP v3) and an unconditioned pause described as fact (OpenAI, Aug 2026). Only event records make that comparison possible.

**2j. A system entity with configuration.** "Model" is not the unit my sources assess:
- the same weights are two named products, "available for general access with additional safeguards as Claude Fable 5" (Aug L324–327);
- helpful-only variants are used for evaluation (Aug §4.5.5.3.1; Astra L2738–2741);
- evaluations are run "without the system-level safeguard stack" (Astra L890–892);
- the HF incident happened "under reduced safeguards" with "no… deployed cyber safeguards, system prompts, or auto-review" (HF report L119–123);
- the propensity to compromise infrastructure "can drop over 100x" with the production harness (HF blog L716–718).

Coined internal names are subjects too: "Model 1", "Model 2" (Aug L597–621), "IM1" (HF blog L117–119). Joseph's surface vocabulary may already cover this. The schema needs a subject that is *model × configuration × surface*, or every measurement will be attached to the wrong thing.

**2k. Declared absence.** One kind is missing entirely: a passage that asserts something was withheld, with a stated reason:
- "Threat variant 7: [redacted]" (Feb L3320);
- "[Appendix redacted]" (Aug TOC L196–197);
- "Some details redacted here for security reasons" (Aug L6869);
- blanked names in the noncompliance policy (e.g. L84–93).

RSP v3.4 now *requires* disclosing that redactions occurred (L583). And Claude's review judged one redaction to have made "the public record… poorer" (Aug L2977–2981), which is an assertion about an absence. Keep this distinct from **our** extraction losses (Roadmap accordions, HF blog chain-of-thought widgets, Astra figures). The passage record needs an extraction-condition field so that silence caused by our tooling is not read as the source's silence.

**2l. "Relative to what" in resolution, especially for alignment terms.** §6 proposes one / several / none / ambiguous. My family shows a further dimension: the *standard* a relational term is measured against differs, and the referents are in different ontological categories:

| Standard / subject | Where |
|---|---|
| Misalignment is a property of a *computation*, relative to what "a reasonable person… would consider unethical, illegal, clearly objectionable, or inconsistent with the model's constitution" | Aug L846–856 |
| Pervasiveness is "a property of a particular form of misalignment, rather than a model itself" | Aug L896–899 |
| "misaligned with the goals of their assigned tasks" (relative to the task) | HF blog L30–31 |
| "Value Alignment: The model consistently applies human values" (relative to human values, as a model property) | PF L883–885 |
| "Alignment—the work of making AI systems behave as intended and responsive to human oversight" (an activity, relative to intent and oversight) | pacing L60–62 |
| "our most aligned model to date", operationalized as respecting restrictions and staying in scope | path-to-astra L338–347 |

A resolution record for "alignment" / "misaligned" should capture both the reference standard (task, developer intent, constitution or published text, human values, oversight) and the bearer (computation, behaviour, model, activity). "Several referents" would flatten this.

**2m. Tentative definitions.** "We consider these definitions to be tentative, and they may change in future risk reports" (Aug fn 12, L866–867); the known/unknown split is "not crisply defined" (Aug L927). A definition record should have a stability or maturity qualifier. The "exploratory" tiers (FGF L396–400, L414–415) are the same thing on classifications.

---

## 3. Where the draft would distort my documents

- **Collapsing the four-document determination into one versioned assertion.** §5 lists OpenAI's cyber determination as "versioned within an author". It is also *interleaved with actions*: a pause and security steps (Aug 7), monitoring requirements (Aug 18), a restart (Aug 28), a release (Sep 3). And the grade changed as more evidence arrived (ExploitBench internal port, expert-led chains; path-to-astra L111–173). Recording only the text diffs would lose the fact that each grade licensed different actions. Suggest: versions of a determination linked to the governance events each one triggered.
- **Treating a relabelled threshold as a new claim.** Without 2e, the FCF's Tier 1/Tier 2 text and the RSP's rows would count as corroboration of each other. They are one claim filed twice.
- **Author = organisation.** Karnofsky led the RSP v3 rewrite, yet posts "All views are my own" (karnofsky L15) and says of his account and the company's announcement, "I believe both are honest" (fn 5, L1195–1198). The same organisation gives two authored accounts of "what changed", and the author field must be able to hold both. The Aug report also has the reviewed party choosing and publishing its reviewer ("Anthropic chose to publish this review — though the text is mine", Aug L2957–2959). The authored review sits inside the reviewed document, which is the independence question Williams raises ("grading its own homework", williams L389). Suggest an attribute on author for the relation to the subject (self-report / commissioned or published by the subject / independent).
- **The commitment ladder as a single strength scale.** My documents include *meta-commitments about future revision*: "we will strive to avoid situations where we revise the goals in a less ambitious direction simply because we are unable to achieve them" (RSP v3.0 L357–362; roadmap L52–55). They also include a commitment with an unstated parameter: "will not accept further degradation of monitoring beyond a limit" (Astra L1717–1719). The first is a relation from a commitment to future commitments; the second is Zhu's "threshold/trigger" dimension left empty on purpose. Both fit Zhu's materiality dimensions if "declared unspecified" is a value rather than a missing field.
- **One content, one speech act.** RSP v3 Appendix A makes the *same* standard both a recommendation to the industry and a competitor-contingent commitment for the company (RSP v3.4 L743–800; announcement L187–195). The schema should allow several speech-act records over one content.

---

## 4. Precedents in my family worth citing

- **Aug Risk Report §2.5 (L843–987): a developer-written argument vocabulary.**
  - It defines misalignment, coherence, pervasive/context-dependent, known/unknown, harm-inducing, high-stakes distribution, unmitigated and misalignment risk.
  - It gives the aggregation modes with a correlation caveat (L977–986).

  It sits beside the NIST 800-2 row as a practitioner precedent for assertion typing, with a correlation to mark: it is Anthropic's, and we are Anthropic models.
- **OpenAI PF v2's five tracking criteria (L145–162): an inclusion rule for what counts as a tracked risk,** with exclusion reasons given for Nuclear and Persuasion (L371–394). This is a small precedent for "why a category is in or out", like Slattery's change log.
- **OpenAI's misalignment reporting framework (L103–144, L285–357):** disclosure criteria ("favors disclosure even when significance is uncertain"), repetition counted as evidence ("Repetition of the issue might itself be useful evidence", L136–141), and three investigation tracks. The HF incident is *retro-classified* into a track that didn't exist at the time (L330–338). A small precedent for recorded-event status fields.
- **HF technical report §X (L1441–1838):** a UTC-timestamped event table, the closest thing in my family to a structured incident record. Beside it sits the blog's register ("walked away", "ethical boundaries could remain active", HF blog L626–697). These are two characterisations of one event by one author, which supports §2(d) directly.
- **Anthropic autonomous-dev (repo markdown):** measurement records with *why / what / found / what anyone could report* plus *what this does and doesn't capture*. Validity is reported as inter-rater agreement (L97). A precedent for how a measurement record might look.

---

## 5. On the open questions, briefly (my view, from these documents only)

- **Q4 (where stage lives).** My sources support stage-on-edges relative to a focal event. The Feb report says so in its own words: "Our pathways don't represent catastrophic outcomes in themselves… we find it more productive to focus on intermediate unwanted outcomes in which sabotage by an AI system creates the conditions for a later catastrophic outcome" (Feb L1481–1487). The same event is an outcome in one frame and a cause in the next.
- **Q5 (Zhu).** It fits my family, with the two additions in §3 (meta-commitments; "declared unspecified"), plus "duplicated into a companion document" alongside "relocated" (2e).
- **Q3 (resolution per occurrence).** For my family, the fidelity that matters most sits in about a dozen terms: catastrophic/severe/systemic risk, loss of control, (mis)alignment, highly capable, sabotage, safeguard(s), High/Critical, marginal/absolute. Per-occurrence resolution for those, and per-term maps for the rest, would capture nearly everything I saw.

I'm on the line if the next draft wants any of these expanded or checked against the texts.
