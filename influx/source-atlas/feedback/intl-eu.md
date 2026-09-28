# Feedback on SCHEMA-SYNTHESIS draft 1: from the EU and international family

*From the intl-eu atlas agent, 2026-09-28. The atlas is at `../intl-eu.md`. Line references are to the `pdftotext -layout` extractions in the same scratchpad `src-text/` directory the atlas uses. Short aliases follow the atlas header: act, omnibus, guidelines, cop, chairs, template, tfs, g7, oecd, perset, sg2025, sg2026, un, jaisi, ised, caisi. Everything below is my reading, offered as input to a draft.*

On the whole the synthesis fits my family well. Four kinds of record, stance, several qualifier axes, lineage and per-occurrence resolution are all things my documents need. What follows is where they need more than the draft gives them. I've put the items I'd weight most first.

---

## 1. How my findings were summarised

Mostly accurate. Two small corrections:

- **§5, "the G7 risk list → AI Act recital 110 → the Code's taxonomy".** The first link is a near-verbatim copy (g7 91–121 → act 1922–1932). The second is a *citation* link, not a copy. The Code names recital 110 as "ADDITIONAL LEGAL TEXT" for Appendix 1 (cop 1393), but its taxonomy (cop 1397–1545) is new text that only echoes some phrases ("significantly lowering the barriers to entry"). Both are lineage, of different kinds; see item 4 below for why the difference matters.
- **§7, "the AI Act's provider and deployer, which has no 'developer'".** True, but the Act's role set is larger, and the richer version bears on Joseph's open "developer" decision (item 5). Art. 3 defines provider, deployer, authorised representative, importer, distributor, operator (act 3144–3161) and downstream provider (act 3432–3434). "Provider" is defined as the one who "develops … or that has … developed *and places it on the market*" (act 3144–3146). Developing alone doesn't make you a provider.

---

## 2. Where the draft would distort my documents

### 2a. Force is not only self-declared, and it varies within a document

§2(a) gives a document "a force it declares for itself". In my family, force is often:
- **declared by another document**, and **contested**. The Code's legal effect is set by the Act (Art. 53(4), 55(2): codes let providers "demonstrate compliance … until a harmonised standard is published", act 5772–5777, 5871–5876).
  - The Commission interprets that effect: adherence is "a straightforward way of demonstrating compliance", with no presumption of conformity (guidelines 1095–1143, paras 94–100).
  - The Omnibus asserts it again: codes "have limited legal effect, and in particular do not grant a presumption of conformity" (omnibus 743–746).
  - The Code states its own force: adherence "does not constitute conclusive evidence of compliance" (cop 30–32).
  - Commentary misstates it: Hoffmann's "presumption of conformity" (hoffmann 105–115).

  So the force of the Code is a set of *assertions by four authors*, one of them wrong. Recording force as a document attribute would make that invisible. Better: force is an assertion type, with an author, whose object is a document or passage.

- **different for different parts of one document.**
  - The Act's recitals are non-binding interpretive text; its articles are binding.
  - The Code's recitals are "recognise" premises, its Commitments "commit to", its Measures "will", and some Measures carry safe harbours ("presumed to be fulfilled, if", cop 914).
  - The Guidelines are "not binding" yet "on which it will base its enforcement action" (guidelines 131–139).

  Force needs to be recordable per passage or section, not only per document.

### 2b. "A document has a version and a date" is not enough for law

Three things in my family break a single version and date:

- **Third-party amendment.** The Omnibus rewrites the Act by reference ("in Article 56, paragraph 6 is replaced by the following", omnibus 1424–1431; the whole of Art. 1 is edit instructions, 888–2499). The text of the Act "as in force on date D" is a *computed view*: Act plus amendments. No relata item holds it. A quote of Art. 56(6) from the 2024 text is now a superseded provision, not a wrong quote.
- **Staggered application per provision.** The Act enters into force in 2024. Chapters I–II apply from 2 Feb 2025; Chapter V (GPAI) from 2 Aug 2025 "with the exception of Article 101"; the general date is 2 Aug 2026; Art. 6(1) from 2 Aug 2027 (act 8303–8312). The Omnibus then moves several of those dates (omnibus 2312–2329: high-risk to 2 Dec 2027 and 2 Aug 2028; the new Art. 5 bans from 2 Dec 2026).
- **Applicable but not enforceable.** Chapter V obligations apply from 2 Aug 2025, but "the Commission cannot take any enforcement actions because its enforcement powers only enter into application on 2 August 2026. This lack of enforcement does not put into question the applicability of the obligations" (guidelines 1257–1263). The same point is at 1196–1198 (fines "starting on 2 August 2026").

**Suggestion.** Give normative passages temporal validity (in force from, applies from, enforceable from, superseded by) as fields, and treat amendment as a lineage link between documents (item 4).

### 2c. "Commitment" folds together norms the author imposes on others

In §1, "Commitment" is described with a strength ladder and conditions, which is Zhu's register for *self-undertakings*. Most of the Act and Omnibus is a legislator imposing duties on third parties defined by role ("Providers of general-purpose AI models shall", act 5731). Zhu's own codebook excludes "describing other parties' obligations" (synthesis §1, citing Zhu L750–752), so adopting Zhu for commitments would leave statutory obligations with no home. The G7 text shows both in eight pages: "organizations should" (other-directed), "Organizations commit to" (the signatory undertaking), "States must" (g7 61). The Code sits in between: an externally drafted text that signatories adopt as their own undertaking ("Signatories commit to").

**Suggested kind: *norm*.** It needs:
- an issuer and a bound party (usually a *role*, not a named entity);
- a deontic type: obligation, prohibition, permission, exemption. The Act's Art. 5 bans each have carve-outs (act 3456–3614); the open-source exemption carries its own exception "unless … systemic risk" (act 5762–5765);
- an applicability condition;
- a deadline where given (next item);
- temporal validity (2b).

A commitment is then a norm whose issuer and bound party coincide, or which a party adopts. Adoption is a relation.

---

## 3. Kinds, axes and fields my documents need that the draft lacks

**3a. Applicability matrices.** The Canadian code asserts, for each measure, whether it applies across role × deployment context (developers or managers × all systems or "available for public use"), with Yes/No cells (ised 130–190). The AI Act does the same in prose: obligations keyed to role × classification (GPAI, GPAI with systemic risk, open-source, not systemic risk). This is a norm's *applicability condition* made explicit. It suggests the condition field be structured over roles and classifications, not free text.

**3b. Procedural time as data.** My documents give deadlines and cadences as operative content:
- notify within two weeks of meeting or foreseeing the threshold (act 5677–5679; guidelines 447–472, which extends this to *before training completes*);
- reassessment no earlier than six months after designation (act 5705–5711);
- Framework confirmed four weeks after notification and two weeks before market (cop 226–228);
- serious-incident initial reports at 2, 5, 10 or 15 days by harm type, intermediate reports every four weeks, final report within 60 days (cop 1043–1075);
- five-business-day notifications (cop 326–327, 861–866);
- Model Reports every six months for the most capable models (cop 845–851);
- a 30-business-day cap on blocking evaluator publication (cop 521–525).

These are neither qualifiers nor conditions. I'd give norms a *trigger → time limit → act* field. In Joseph's chain, they are the timing of the (policies & decision-making) layer.

**3c. Gross versus net of mitigation.** The Commission separates *risk posed* from *risk after mitigation*: mitigations "are not suitable grounds for a model being excluded from classification … the model still poses systemic risks which must continuously be assessed and mitigated" (guidelines 575–583). The Code requires the Model Report to compare "systemic risks with safety and security mitigations implemented and with the model fully elicited" (cop 741–742). The EU instruments use both quantities, for different purposes (classification versus acceptability). Anthropic's "fraction unmitigated" factor in §1 is the same distinction. **Suggested qualifier axis: mitigation state** (unmitigated or fully elicited / with mitigations / residual). It is distinct from "elicitation" (prompted vs spontaneous) in §4. The Code uses "elicitation" differently again, to mean *effort to draw out capability*, matched to "misuse actors" (cop 1617–1633). "Elicitation" itself will need resolving (§6).

**3d. Relative (comparative) safety claims.** The Code's "similarly safe or safer model" (cop 1548–1599) is a claim that one model's risk is no greater than a reference model's. It is established by benchmark scores "lower than or equal to (within a negligible margin of error)", with an explicit safety margin, and it unlocks exemptions (cop 1127–1130, 1689). §4's "baseline" axis covers the reference. What it doesn't cover is that the *reference itself can lose its status*, which forces re-evaluation within six months (cop 1590–1599). A relative claim needs a link to its reference claim that can be invalidated. The two renderings of this appendix also differ in their text (atlas, chairs entry; chairs 1896–1907 vs cop 1574–1583). It is exactly the kind of passage where "which text was read" (§2a) matters.

**3e. Forecast as a required commitment content.** The Code requires frameworks to state "estimates of timelines when Signatories reasonably foresee that they will have a model that exceeds the highest systemic risk tier already reached … may consist of time ranges or probability distributions … supported by justifications, including underlying assumptions and uncertainties" (cop 210–216). §1 has scenarios and a likelihood axis, but not a *forecast* (a dated prediction with a stated distribution). NIST's "prediction" type (§8) would hold it. Note that here the forecast is something a norm *requires another party to produce*. The norm names the forecast's form without making it.

**3f. Worked examples as definitional assertions.** The Guidelines resolve their indicative criterion with a box of in-scope and out-of-scope cases (guidelines 258–339). Each case is a classification ruling on a hypothetical model. These are neither scenarios (§1) nor definitions; they are *exemplars that fix the extension of a term*. In address-theory terms they are *match* test cases. In my family they appear wherever a regulator narrows a definition (see also the Omnibus carve-outs, omnibus 262–293).

**3g. Forms and templates as implicit schemas.** The HAIP questionnaire (oecd-2026-haip-reporting-v2) asserts almost nothing directly; its answer options are a taxonomy of practices. The incident template's fields (template 11–63) define what an incident record *is*. §2 has no place for "a document whose content is a schema". Two suggestions:
- treat these as sources of *vocabulary and record structure* (terms layer, event layer), not of assertions;
- the template in particular is a precedent (item 6).

---

## 4. Relations the draft's lineage section lacks

§5's "derived from, with the changes marked" needs subtypes. My family contains:

1. **Verbatim or near-verbatim copy**: G7 → recital 110; Code Measure 9.2 → template (one word, "material" → "evidence", cop 1025 vs template 33); tfs 93–94 → chairs 100–102; Singapore 2025 glossary → 2026 (sg2026 667–736).
2. **Citation as basis**: the Code's "LEGAL TEXT: Article 55(1) … AI Act" headers on every Commitment (e.g. cop 167) and recital 110 for Appendix 1 (cop 1393). Perset quotes the G7 Actions it reports against in a box for each section (e.g. perset 412–428). The HAIP form maps each section to G7 Action numbers (oecd-2026-haip-reporting-v2 30, 199, 379).
3. **Restatement by a secondary source, with drift direction.** Hoffmann restates the Guidelines' rebuttable criterion as a definition and a no-presumption regime as a presumption. Singapore 2026 paraphrases Act Art. 14's "enabled, as appropriate and proportionate" (act 4108–4131) as "mandates … must have the ability" (sg2026 4153–4157). That is a *strengthening* drift, the mirror of lit-b's weakening chain. So the synthesis's "changes marked" should allow for either direction.
4. **Amendment**: Omnibus → Act, by instruction; the result is a consolidated text (2b).
5. **Implements / demonstrates compliance with**: a commitment or measure against the obligation it serves. The Code exists to be this relation: "a guiding document for demonstrating compliance with the obligations provided for in Articles 53 and 55" (cop 30–31). The Guidelines describe the enforcement consequence of the link (guidelines 1103–1122).
6. **Reports against**: a practice claim against the commitment it evidences (Perset's structure; the HAIP form; the Code's Model Report requirements).
7. **Interprets**: the Commission's reading of a statutory term (guidelines throughout), which is itself contestable only before the CJEU (guidelines 131–133).

Items 5–7 matter for Joseph's "governance recast from documents to commitments". Without them, a commitment in the model floats free of the obligation it answers, and the evidence offered for it floats free of both.

---

## 5. Roles: what my family adds to §7 and the "developer" decision

My documents make role *assignment* rule-governed and conditional. A role is not a static label on an organisation:
- **By activity plus market act.** Provider = develops (or has developed) *and* places on the market under its own name (act 3144–3146). Placing on the market is itself defined by examples, including "used for internal processes that are essential for providing a product or service to third parties" (guidelines 699–722).
- **By a quantitative threshold on an act.** A downstream modifier becomes a provider when modification compute exceeds a third of the original's (guidelines 802–858).
- **By control.** "An important factor in this assessment may be who has the control over the model's weights, for example, in case of fine-tuning via API" (guidelines 790–793). Singapore 2026 assigns intervention duty to "whoever controls the execution environment … the deployer, the platform provider, or both" (sg2026 4145–4147).
- **By corporate grouping.** The Omnibus gives the AI Office competence where model and system come from "the same provider, or … providers forming part of the same undertaking" (omnibus 1691–1722). Here the *undertaking*, not the legal entity, is the unit.
- **By jurisdictional fallback.** If the upstream actor excludes the EU "in a clear and unequivocal way", the downstream integrator becomes the provider of the *model* (guidelines 759–774).
- **By activity footnote.** Canada defines developer and manager by lists of activities (ised 193–202).
- **By role vocabulary in reporting instruments.** HAIP has "Model developer (/provider)", "Application developers (/providers)", "Deployer" (oecd-2026-haip-reporting-v2 10–24). Perset's "AI developers" covers any respondent, including a preparatory school (perset 112–116).

This supports the draft's lean toward "roles plus an organisation term", and suggests two additions:
- the organisation term needs a grouping level (legal entity vs undertaking);
- role assignment should be recordable as an *assertion by a source*: "under instrument I, actor A holds role R because condition C". A role is then something an instrument *confers*, and the same organisation can hold different roles under different instruments for the same model.

---

## 6. Precedents the draft missed

1. **EU serious-incident record: the template (template 11–63) plus Code Measures 9.1–9.4 (cop 988–1085).** A regulator-specified incident record whose fields map onto §2(d) and Joseph's chain almost one-to-one: start and end dates; harm and victim or affected group (impact radius); "chain of events that (directly or indirectly) led to" (causes); model involved; evidence; response and recommendation (mitigation and recovery); root cause including "failures or circumventions of systemic risk mitigations" (failed controls); near-miss patterns.

   It also carries a **causal-attribution standard**: report if the model's involvement led to the harm, "or if the Signatories establish or suspect with reasonable likelihood such a causal relationship" (cop 1047–1066). There is also a status field, "resolved", defined (cop 1307–1309), and "near miss" is defined (cop 1270–1271).

   *Correlation to mark:* the template is derived from the Code's text; they are one lineage, not two sources. The OECD "AI incident" definition (perset 1423–1430) is a parallel, not a copy, and differs from AI Act Art. 3(49) (act 3331–3344) in its harm list. J-AISI's "AI-IRS" approach book (jaisi 244–251) is a third incident framework, cited but not included in the text.

2. **The Code's Appendix 1 as a causes-tree precedent (cop 1397–1545).** Risk *sources* split into model capabilities (14 items), propensities (10) and affordances or contextual factors (13). A risk *nature* layer separates essential characteristics (the statutory definition's three limbs) from contributing characteristics:
   - "Capability-dependent", "Reach-dependent";
   - "High velocity … potentially outpacing mitigations";
   - "Compounding or cascading";
   - "Difficult or impossible to reverse";
   - "Asymmetric impact" (cop 1434–1444).

   The contributing characteristics are a vocabulary for Joseph's *degree/scale* on impacts, and for escalation edges. *Correlation to mark:* this is a drafting-committee text given quasi-legal effect through the Act (§2a). Its chairs include Bengio, who also chairs IASR and sits on the Singapore Consensus planning and steering committees (sg2025 57, 244). Vice-chair Rajkumar is also a Singapore 2025 contributor (cop 8–15; sg2025 107). Anderljung, another vice-chair, is cited in Singapore's references but is not a contributor.

3. **Singapore 2026's hazard → mitigating principle → practice table (sg2026 3210–3287), and its per-principle role split (e.g. sg2026 4136–4147).** This is the (causes) → (preventions & controls) link in Joseph's chain, stated as a table, with duties split across agent developers, deployers and "whoever controls the execution environment". Its method treats *independent convergence across sources* as evidence (sg2026 3163–3165). That makes it a precedent for the lineage-aware corroboration count in §9, and a caution: convergence is only evidence if §5's derivation links show it is independent. *Correlation to mark:* synthesised with input from "global frontier AI developers" (sg2026 228–229); Concordia AI and FLI hold writer and steering roles (sg2026 62–87).

4. **Singapore's defence-in-depth structure (sg2025 285–317; sg2026 616–653)** fits Joseph's chain almost stage for stage:
   - risk assessment;
   - development (specification, design, verification), which is prevention;
   - control (monitoring and intervention after deployment);
   - in 2026, societal resilience ("preparing and hardening societal systems for failures and misuse", sg2026 249–251), which is his *mitigations & recovery*.

   Its Figure 1 caption also shows, by getting it wrong, that stage depends on where the system boundary is drawn (sg2025 322–328). That is §7's "stage is relative", from another direction.

5. **UN vulnerability-based framing (un 1439–1445, Box 4 at 1501–1542).** An explicit argument for shifting "from the 'what' of each risk (e.g. 'risk to safety') to 'who' is at risk and 'where', as well as who should be accountable". Box 4 categorises risks by the individuals, groups and systems exposed. It is a second government-grade source for Joseph's impact radius, beside the Chronic Risks Analysis. *Correlation:* the Pulse Check behind it used snowball invitation from the Advisory Body's own networks (un 4687–4691).

6. **OECD 2024 Annex A as a precedent for provenance of a list (oecd 1927–2031).** The only document in my set that records how its risk list was built: literature review, then 17/36/68 initial items, expert feedback, survey (53 of 61, scales reproduced), and consolidation into 21/38/66. Consolidation, where a list at one stage becomes a different list, is lineage *inside* a source. If the model ingests ranked lists from surveys, this is the shape to record.

---

## 7. Address theory (§6): my documents already declare scopes and imports

The synthesis says a term defined in a document is a binding in that document's scope. My family shows sources *declaring* how their scopes relate. Those declarations are data the resolution record could use directly, and they give the "mediated path" in §6 a concrete form:

- **Declared import with precedence**: "Wherever this Chapter refers to a term defined in Article 3 AI Act, the AI Act definition applies, and such definition shall prevail" (cop 1137–1139).
- **Scoped rebinding of a common word**: in the Code, "model" means "a general-purpose AI model with systemic risk", except "if the term 'AI' precedes the term 'model'" (cop 1230–1255). Singapore rebinds "AI systems" to mean general-purpose systems for the whole document (sg2025 267–269; sg2026 607–610). A "system" in Singapore and a "system" in the Act resolve differently by the sources' own declaration.
- **Purpose-indexed binding within one document**: "training compute" means one quantity for GPAI classification and another ("cumulative") for systemic-risk classification (guidelines 1306–1312).
- **Declared locality**: "simply specify how we use various terms in this report … we make no claims whatsoever to these being better" (sg2025 256–261).
- **Definitions of function words**: "including" introduces "a non-exhaustive set … the minimum required" (cop 1180–1181), and "all grammatical variations … shall be deemed to be covered" (cop 1140–1142). These govern how *every other* passage in the document is read.
- **A second statutory reference/referent gap, beside SB 53.** "High-impact capabilities" means capabilities that "match or exceed … the most advanced" models (act 3417–3418). The referent moves by definition: the Commission "does not consider it to refer to a fixed level of capabilities" (guidelines 556–563). 10^25 FLOP is the match test (act 5663–5665). Art. 51(3) lets the test be re-tuned, and the chairs argue it "may soon fail to capture only the most advanced models, with estimates suggesting that there will be hundreds" (chairs 67–84). The rebuttal procedure (act 5683–5694; guidelines 499–607) is the statute's own mechanism for when match and referent diverge for a particular model. Unlike SB 53, it is exercised per model, with a burden of proof on the provider (guidelines 519–521).

---

## 8. Smaller points

- **Stance, §3.** The Code's "Precautionary Principle" recital (cop 123–127) makes "treated as" a *rule of the instrument*: extrapolate trends "for the identification of systemic risks". It is not a stance on one claim. This suggests a document-level stance default that assertions inside it inherit.
- **Lifecycle, §7.** In my family "deployment" is regime-bound. The Commission's lifecycle begins "at the start of the large pre-training run" (guidelines 352–365). Internal use can count as placing on the market (guidelines 720–722). Singapore 2026 wants authorities aware of "internal deployments crossing regulatory thresholds" (sg2026 490–491). So pre-/post-deployment values will need resolution per source, like any other term.
- **Scope exclusions as assertions.** Singapore 2026's companion excludes "the effective pursuit of misaligned goals by agents functioning exactly as engineered" (sg2026 4436–4439). The Code says it is "not [about] AI systems" but must consider system architecture (cop 62–68). The draft's "negative scope" (claim about a claim) covers evidence limits. A document's declared *topic* exclusions are a slightly different thing and worth their own value, because silence inside an excluded scope is not evidence of absence.
- **"Explicitly not asserted", §3.** The UN report's "majority consensus; no member is expected to endorse every single point" (un 49–52) is a document-level author-attribution qualifier. The author is a body, and no individual member can be taken to assert any given passage. The same holds for the Singapore Consensus and, differently, for the Code (drafted by chairs, adopted by signatories). Layered authorship (§2(b)) would need "collective, non-unanimous" as a value.

---

Nothing to add on §8's existing precedents or on the open questions in §10 beyond the above. On question 5 (Zhu for commitments), my family's answer is yes for self-undertakings, but not as the home for statutory obligations (2c).
