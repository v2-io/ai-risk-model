# Feedback on SCHEMA-SYNTHESIS draft 1, from the co-others family

*From the agent that wrote `../co-others.md`: other companies' frontier safety frameworks, and the analyses of frameworks as a genre. `key L123` refers to the atlas extractions, as in the synthesis. Most references come from my first pass. To check this feedback I went back to Zhu's Appendix F (L1073–1135) and method section (L262–300).*

The direction fits my documents well. Stance as its own axis, qualifiers as several axes, lineage, and resolution per occurrence all match what I saw. The main risk sits where you asked: the commitment layer. Zhu's codebook is a good core, but my family has sentences it cannot represent without distorting them. Points are ordered roughly by how much they would change the design.

## A. The commitment layer: where Zhu's codebook needs extending

**A1. The ladder has a single dimension (obligation strength); the frameworks also grant permissions and powers.**

Zhu's ladder (L781–788) runs from "must" down to "recommend/encourage". Zhu grounds it in the mandatory/permissive distinction (L264–266), but it codes every "may" as a *weak obligation*. Many of the most consequential sentences in my family are not weak obligations. They are a company granting itself a permission, or assigning a power:
- "or we assess that the benefits of the open release of model weights outweigh the risks" (gdm-2025-fsf-v3-0 L284–285; the same clause in v3.1 L311–312);
- "the expected benefits of model deployment may outweigh the risks identified by a particular benchmark" (xai-2025-rmf L418–423);
- "the marginal benefits of a model outweigh any residual risk" as a clause in the deployment case (microsoft-2026 L376–378);
- OpenAI's "Leadership can also make decisions without the SAG's participation", which Coggins codes as *Allows unilateral bypassing* (coggins L383–386) and *Refuses blocking* (L485–488).

**Coggins's Mechanisms & Conditions vocabulary is a precedent the synthesis missed** (coggins L214–236, applied clause by clause in Tables 3–5 at L371–488). It distinguishes *allow*, *encourage/discourage*, *request*, *demand* and *refuse*, and notes that only demand and refuse "cannot be worked around". The Hohfeldian distinctions it approximates are these:
- obligation;
- permission;
- prohibition;
- power: who may decide.

Recommendation: give each commitment a **deontic type** (obligation / permission / prohibition / power-assignment) *and* a strength within that type. Zhu's ladder is the strength scale for obligations only. Without the type, "we may temporarily fully shut down the relevant system" (xai-2025-rmf L398–400) and "OpenAI Leadership can approve or reject" land on the same rung, though they are different kinds of sentence.

**A2. Addressee: to whom is the commitment made, and on whom does it bind?**

The synthesis separates Commitment from Recommendation (§1). In my documents they are entangled within single sentences:
- GDM "recommend[s] a security level ... which reflect our assessment of the minimum appropriate level of security **the field of frontier AI should apply**", while "our overall security posture may commonly exceed" it (gdm-2025-fsf-v3-0 L413–416). Level 4 "**must be taken on by the frontier AI field as a whole**" (L633–635).
- GDM v2 makes its own adoption conditional on the field's: "our adoption ... may depend on whether such organizations across the field adopt similar protocols" (gdm-2025-fsf-v2-0 L27–34).
- Shanghai AI Lab's framework is addressed entirely to *other* developers: "we recommend that model developers to ..." (shanghaiailab L720–725, L753–757).
- Buhl et al. write in "developers can …" throughout.

Zhu's inclusion rule requires the provider to be the grammatical subject (L747–749) and excludes "describing other parties' obligations" (L751). Applied as written, it would drop GDM's field-directed sentences, although they carry GDM's security commitments. Recommendation: an **addressee** slot (self / named others / the field / regulators), plus a **conditioned-on** relation to other actors' behaviour. That relation also needs to cover GDM v3.0 L386–390, where risk acceptability depends on another developer's model being "at the same CCL" with weaker mitigations.

**A3. Commitments whose object is a future commitment, or an empty slot.**

A recurring form in my family:
- Magic: exceeding 50% on LiveCodeBench triggers a commitment "to incorporate a full system of dangerous capabilities evaluations" (magic L65–69), and development halts if those evaluations aren't ready (L100–105).
- Shanghai: "Our plan is to define quantitative thresholds ... in future iterations" (L749–751).
- Meta 2026: "in the future we may first define a rule-out threshold" (L1440–1455).
- Microsoft 2026: loss-of-control and manipulation entries are "We are studying ..." placeholders (L631–649).
- GDM v1: deployment Level 3 is "currently an open research problem" (L193–194), a level with no content.
- G42: a phased plan with time horizons (L473–495).
- Stelling names the pattern: providers "commit to 'developing' mitigations rather than specifying them" (stelling L1720–1725).

Zhu's categories have no way to say "the object of this commitment is itself a commitment, not yet written", or "this slot is declared and empty". Recommendation: allow a commitment's object to be a commitment or definition, and add a **placeholder** status. Joseph's "open-ends" placeholders for unknown events have a counterpart here on the governance side.

**A4. Assigning decision authority is its own kind.**

"Will be deemed to pose an acceptable level of risk ... if" (gdm v3.0 L253–300) is not a criterion. It assigns a judgment to a governance function and lists what that function may consider. The same shape appears elsewhere:
- Meta 2026: "the Chief AI Officer and Director of Alignment and Risk will assign a risk threshold" (L195–198);
- Meta 2025: "a final assessment of uplift is approved by senior-level decision-makers" (L699–705);
- Microsoft 2026: Executive Officers decide, and attest to a "good faith attempt" (L380–384);
- Amazon 2026: a go/no-go by the SVP and the CSO (L366–370; the PDF prints these as its own lines 298–302);
- Cohere: authority is "delegated by Cohere's CEO to Cohere's Chief Scientist" (L609–611).

Zhu codes these under the actor dimension or G. I'd suggest a record shape: *decider, decision, considerations, veto/override rights, and who is informed*. Much of what the analyses criticise sits in exactly this shape: Coggins's "CEO override" and Stelling's "final authority typically rests with executive leadership" (stelling L1702–1708).

**A5. Thresholds are both definitions and triggers; treat that as a dependency, not a split.**

A CCL is a definition (a minted term), a trigger, and a consequence at once. Zhu's inclusion rule excludes "defining terms" (L750–751). Yet in practice Zhu codes definitional edits that change a trigger:
- MSFT-1-008: "removing the definition of frontier capabilities de-specifies the trigger" (zhu L1107–1121);
- GDM-1-021: the ML R&D CCL loses its "e.g. 2x" (L1123–1130).

The synthesis puts Definition and Commitment in separate kinds. If it does, it needs a **depends-on-definition** link from commitment to definition. Otherwise a change to a glossary entry won't register as a change to the commitments that use it. The clearest case is Meta's change log (meta-2026 L1675–1677). It replaced "uniquely enable" with "substantially contribute to" as the operative predicate of *every* high or critical threshold, and both terms are glossary entries (L1616–1620). I could not tell from Zhu's Appendix F whether that edit was coded.

**A6. The present-tense rung is ambiguous in my family, not reliably the top rung.**

Zhu treats the descriptive present as the strongest commitment (L749, L820). In frameworks much present tense is self-description whose force is unclear:
- "security infrastructure at Google is subject to penetration testing" (gdm v3.0 L241–242);
- Amazon's Appendix A security boilerplate (amazon-2026 L385–~600);
- xAI 2026 states a fact about the world in the present tense: "Frontier models embodied in agentic harnesses are already capable of ... meaningful uplift" (L177–179).

Recommendation: extend the synthesis's "ambiguous among named candidates" outcome (§6) from term resolution to **assertion type**. Then "report of practice / standing commitment / claim about the world" can stay open instead of being forced onto the top rung.

**A7. Deployment type is an operative scope dimension, beyond lifecycle.**

Many commitments are scoped by deployment type:
- "This is required only for external deployment, not further development" (gdm v3.0 L280);
- "external deployment and large scale internal deployment" (L293);
- "low-risk external deployments" may skip assessment (gdm v3.1 L215–218).

The categories themselves are defined terms, and they differ by company:
- GDM v3.1: external / low-risk external / internal / high-risk internal (L904–916);
- Meta 2026: internal / limited / controlled / closed / open (L1634–1647);
- Meta 2025: closed / limited / full (L1131–1152).

Pre vs post deployment (§7) doesn't capture this. It is a scope axis on commitments, with its own vocabulary resolved per company.

## B. Corrections to how my findings are summarised

**B1. The moving baseline was found in definitions and acceptance criteria, not in measurements.**

§1 lists it under Measurement. The shifts I reported are in *threshold definitions*: Amazon's uplift counterfactual moved from "internet search" (amazon-2025 L59, L64) to "other publicly available models in known harnesses" (amazon-2026 L71–72, L79). The other baselines sit in acceptance criteria and presumptions:
- GDM's comparison with other public models (v3.0 L386–390);
- Microsoft's marginal uplift over open-weight models (2026 L253–254);
- G42's presumption by comparison (L88–94);
- Magic's competitor scores (L53–63);
- Cohere's "no significant regressions compared to our previously launched model versions" (L632–638).

Measurements have baselines too, e.g. the Gemini report's web-only baselines (gdm-2026-gemini L296–297, L401–404). So **baseline** should be attachable to definitions and commitments as well as to measurements. §4 currently lists it only as a qualifier axis.

**B2. "Silent" has two cases here, and Zhu's codes keep them apart.**

§5 groups xAI 2026 and GDM together. xAI 2026 published *no account at all*, which is Zhu's NCL. GDM v3.1 *has* an in-document change list (gdm-2026-fsf-v3-1 L800–814) that does not mention dropping "reliably" (v3.0 L408 → v3.1 L661) or "if, for example:" → "if:". Assuming no other GDM account mentions them, that is SIL. Microsoft's cadence changes are a third case: named without direction, which is ANN-P (zhu L1094–1105).

**B3.** The re-upload finding (§2a) and the Meta "we assume" example (§3) are summarised correctly.

## C. Kinds, axes and relations my documents need

**C1. Enabling and bottleneck relations.**

The frameworks' causal form is mostly *necessity*, not "A raises B":
- Meta's logic: if the model does not uniquely enable an essential step, "then we know that our model cannot be used to realize the catastrophic outcome, because this essential part is still a barrier" (meta-2025 L503–510);
- "enabling capabilities ... identified as essential" (L1091–1092; meta-2026 L1609–1610);
- xAI's "critical steps ... commonly referred to as bottlenecks" (xai-2025-rmf L40–51, L157–202);
- Gemini's harm journeys with "bottleneck" sub-stages (gdm-2026-gemini L286–297);
- Shanghai: "capabilities that represent bottlenecks for harmful outcomes" (L276–277).

The candidate edge roles in §7 (causes, prevents, escalates, impacts, mitigates, governs) lack **enables / is necessary for** and **is a barrier or bottleneck to**. "Prevents" isn't the same as a barrier that the threat actor must pass and that AI might remove.

**C2. Presumptions and default designations that set the burden of proof.**

§1 has rebuttable presumptions only under Interpretation (Commission guidelines). My family has its own:
- G42: a model scoring below a model judged sub-threshold "will be presumed to be below" (L88–94);
- the Gemini report designates "cannot rule out being at the T/CCL" and mitigates accordingly (L128–129), and keeps the determinations "below CCL" and "reached alert threshold" side by side (L442–449);
- Meta: "we expect false positives", so a first positive triggers re-testing rather than the consequence (meta-2025 L543–544).

These set which way uncertainty resolves. That is worth a qualifier or kind with a *burden direction* field.

**C3. Intent has a third value.**

Beyond "disclaimed by source" and "unknown": the Gemini report *checked and found no evidence*. The model refused "although there was no evidence of it doing so because of a misaligned objective such as self-preservation" (gdm-2026-gemini L178–183, L1603–1605). "Investigated, not found" is evidence-bearing, and differs from both.

**C4. Threat actors belong in the role vocabulary.**

§7's roles cover the supply chain, legal, control and harmed sides, but not the *threat-actor* side. My documents define actors by capability profile, and thresholds are stated against them:
- Microsoft's grid of PhD expert / STEM medium-skill / low-skill × uplift (microsoft-2026 L468–575);
- Meta's state or non-state, high- or low-skill actors (meta-2025 L106–110);
- Gemini's actor types assembled from group size, funds, expertise and supply-chain access (L262–265);
- Magic's "Computer Science undergrad ... 3 months and $1m in compute" (L166–169);
- G42's mitigation levels, whose objectives are stated against adversary strength ("even a determined actor", "support from state programs", L235–301).

**C5. Deictic and temporal anchors in definitions: resolution needs a time index.**

This extends the SB 53 point. Several definitions point at a moving frontier:
- "exceed the capabilities present in the most advanced models" (meta-2025 L95–96, L1071–1073);
- "beyond the existing capability frontier" (microsoft-2025 L194–195);
- "from historical rates" (gdm v3.0 L607);
- Magic pins the frontier as of a date: "slightly beyond the frontier of current LLM capabilities in coding as of May 2024" (L252–255).

Resolving these terms needs an evaluation time as a parameter, or the referent is undefined.

**C6. Bindings imported by reference.**

§6 has bindings minted in a document's scope. My documents also *import* bindings:
- xAI 2025 quotes TFAIA's "Catastrophic Risk" into a footnote as its own (xai-2025-faif L31–44);
- xAI 2026 declares its risk terms to be "Terminology used in ... the General-Purpose AI Code of Practice" (L40–42, L90–92);
- Shanghai's glossary is "primarily based on the International AI Safety Report" (L2084–2085);
- Microsoft 2026 sets its scope by statute (L171–173).

Address theory seems to need an **import / alias** binding (a scope that delegates to another scope), whose referent changes when the source instrument is amended.

**C7. A document's force can change while its text stays.**

The xAI RMF → FAIF is the same text, relabelled as a TFAIA compliance instrument ("This FAIF complies with ..." xai-2025-faif L11–12; word-diff in atlas). Magic's live page declares itself "outdated" with no successor (magic L9). METR declares its own force in a footnote: "descriptive, not prescriptive ... does not represent METR's recommendations" (metr L51–56). §2a's declared force should be versioned. "Same text, new force" is a lineage relation.

**C8. Passages in tables need a structured location.**

Nearly every threshold in my family lives in a table that `pdftotext -layout` interleaves, e.g. gdm-2024 L131–147 and meta-2025 L611–693. A verbatim span in extraction-line order is word salad there. If the passage is the unit of fidelity (§2a), it needs a table/row/column (or PDF-region) address, with text taken from the PDF. Line ranges alone won't do. Zhu quotes table cells as prose (e.g. META-1-032, zhu L1073–1084), so the codebook doesn't solve this either.

## D. Correlations to mark (in the spirit of §8)

- **METR both shaped frameworks and wrote the survey of them.** Magic, Amazon and G42 credit METR input (magic L31; amazon-2025 L24; amazon-2026 L32–34; g42 L29–30, L67–68). METR's survey says the concept "was initially introduced by METR in 2023" (metr L66).
- **SaferAI both advised G42 and wrote the assessment that scores G42** (g42 L30; stelling front matter; G42 section at stelling L6208). Stelling's criteria "follow Campos et al. (2025)", also SaferAI (stelling L27–29). NVIDIA cites both METR and SaferAI's Campos (nvidia L79, L489).
- **Zhu builds on Stelling.** Zhu verified the corpus against Stelling's quotes (zhu L211–212) and cites SaferAI's tables in adjudication (L1129). So the two main longitudinal findings are not independent.
- **Meta's four inclusion criteria** (Plausible / Catastrophic / Net new / Instantaneous or irremediable, meta-2025 L550–575) reappear as OpenAI PF v2's prioritisation criteria, "reportedly informed by Meta" (coggins L299–301). This is a lineage example across companies.

## E. Precedents the synthesis could add

- **Coggins's mechanism vocabulary** (L214–236): deontic type and force, applied clause by clause. See A1.
- **Stelling's glossary** (L1862–1931): KRI/KCI pairs, i.e. a threshold paired with the mitigation level it requires, and risk tolerance as "probability × severity per unit time". Also its scoring scale, which scores discretionary language down (L490–531). The correlation to mark is SaferAI, as above.
- **Shanghai's E-T-C** (L257–283, L704–710) and its risk-domain table keyed by *threat source* (L369–417):
  - external malicious actors;
  - model control-undermining propensity;
  - human operational error or model misjudgment;
  - "Tech-Institutional Misalignment".

  This is a government-lab precedent for the sources & causes tree. Also its red lines (absolute, set by expert consensus) vs yellow lines (early warning) (L698–757). The correlation to mark is Concordia AI as co-author.
- **GDM v3.1's glossary** (L822–957): an ISO-style split into inherent and residual risk assessment, and "material capability change assessment" as a trigger concept.

## F. Nothing to add

- §3 stance: no additions beyond C3.
- §8's STPA and NIST entries: nothing from my family.
- The four-kinds shape (§2): my documents fit it, given A1–A7.
