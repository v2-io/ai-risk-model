# Feedback on SCHEMA-SYNTHESIS draft 1: from the US federal and state family

*From the us-gov atlas agent, 2026-09-28. Line references are to `scratchpad/src-text/<key>.txt`, the same files as the atlas (`us-gov.md`). Where I say "my reading", it is interpretation, not something the source says.*

**Summary.** The four-record shape and the §6 resolution proposal both hold up against my documents. There are two places where they would distort, though, and both come from the legal and executive instruments that make up about a third of my set:

- **"Commitment" as the governance unit** loses the difference between a party binding itself and one party binding another.
- **Force declared per document** misses force that varies from one provision to the next.

My documents also need about eight relations between instruments that the synthesis doesn't have (§3 below), and a few qualifier axes and precedents. You summarised my own findings correctly. There is one small widening, in §6 below.

---

## 1. Where the synthesis would distort my documents

### 1a. Commitments vs imposed obligations vs tasking

The synthesis recasts governance as commitments, and adopts Zhu's ladder for their strength. That fits company frameworks. It doesn't fit three things in my set, because in each of them **the party bound is not the party speaking**:

- **Statutory obligations.** SB 53 §22757.12 (259–361) and RAISE §1421 (180–265) bind "large frontier developers". The legislature is the author; the developer never committed. The same text also has a separate *enforcer* (the AG alone, SB 53 508–509) and penalties that apply only to certain failures by certain parties (SB 53 502–506; RAISE 405–414). Under the synthesis, a transparency obligation would read as the developer's own commitment. That is exactly the distortion "compilation, not adjudication" is meant to prevent.
- **Executive tasking.** EO 14365 §§3–8 (50–150), EO 14409 §§2–4 (39–133), NSPM-11 §§3–5 (94–194). The President tasks named offices, with deadlines. The bound party (e.g. "the Director of NSA", EO 14409 101–102) is a subordinate office, not the author. The synthesis lists "executive-order tasking with deadlines" under "Recommendation, tasking, plan". Tasking isn't a recommendation, though: it creates a duty.
- **Recommendations to a third party.** The legislative framework's "Congress should…" (whitehouse-2026-legislative-framework, throughout). The Action Plan's "Recommended Policy Actions" (e.g. 233–243), most of which name a lead agency, so each one is part tasking and part recommendation.

**Proposal.** Keep one record kind for all of these; call it a *normative provision*, or something like it. Give it separate roles:

- **author / imposer**;
- **bearer** (who is bound; often defined by a match test, see §4);
- **beneficiary**, where one is named;
- **enforcer**;
- **strength**;
- **trigger**;
- **deadline**;
- **consequence**.

A commitment is then the case where imposer = bearer. Zhu's six materiality dimensions (scope, threshold or trigger, actor, strength, disclosure, consequence) carry over almost unchanged. They just need "actor" split into imposer and bearer, plus an enforcer. Zhu's change outcomes also apply. SB 53 and RAISE are the same provision text with a different deadline (15 days, SB 53 382–384, vs 72 hours, RAISE 290–296), a different penalty and a different regulator. That is Zhu's "strengthened / weakened" across two instruments rather than two versions.

### 1b. Force is per provision, not only per document

§2(a) gives a document "a force it declares for itself". In my set, force varies *within* one binding text:

- SB 53, a statute, contains "is encouraged, but not required" twice: 336–337 (disclosures "consistent with, or superior to, industry best practices") and 393–394 (reporting incidents for non-frontier foundation models).
- SB 53 Sec. 5(d)–(f) (743–750) sets the conditions under which the act does not apply at all: conflict with a federal contract, federal preemption.
- EOs and NSPM-11 end with "not intended to, and does not, create any right or benefit … enforceable at law" (eo-2025-14365 159–162; eo-2026-14409 147–150; nspm-11 225–227). That is a declared force for the whole instrument, sitting alongside provisions that use "shall".

So force wants to live on the passage or provision, with the document-level declaration as a default.

**One key can hold more than one document.** The `whitehouse-2026-nspm-11` key contains the memorandum (17–228) *and* the fact sheet (230–291): two documents, two voices, two forces. The `nist-2026-rfi-agents` key contains three unrelated Federal Register notices (the RFI is roughly 57–327). The document record shouldn't assume key = document.

### 1c. Presupposition hides inside tasking and questions

Your stance values assume that an assertion appears as a declarative. In my set, a lot of content arrives *presupposed* inside a directive or a question:

- EO 14365 tasks Commerce to identify state laws "that require AI models to alter their truthful outputs" (82–85). That presupposes such laws exist, and that there is a fact of the matter about "truthful outputs". The order never defines the term.
- The RFI's questions ("What are the unique security threats … distinct from those affecting traditional software systems?", about 248–257, col. 1) presuppose that there are distinct threats. Its background lists, as a risk category, "models that exhibit specification gaming or otherwise pursue misaligned objectives" (about 104–132, col. 3). That is asserted as background framing, not argued.
- AI 800-4's open questions (1274–1330) are mostly attendees' questions. What they carry is the questioner's framing.

I'd add **presupposed (by a directive or question)** as a stance value, so these can be captured without promoting them to "asserted".

### 1d. Document-level scope exclusions explain silence

The synthesis has negative scope as a claim about a claim ("What this evidence does not tell us"). My NIST documents make **scope exclusions at the level of the whole document**. Those exclusions are the reason certain risks are absent, and without them the absence would read as denial or neglect:

- AI 600-1: "speculative risks that may potentially arise in more advanced, future GAI systems are not considered" (nationalinstitute… 191–194). This is why there's no loss-of-control risk among its twelve.
- AI 800-1: only deliberate misuse, "does not cover risks from accidental AI harms" (nist-2025-managing 206–208); only "marginal risk" (182–183).
- AI 100-2 excludes non-adversarial flaws (vassilev-2025-adversarial 424–427) and declines to set risk tolerance (409–411).
- The DeepSeek report doesn't investigate development or distillation (caisi-2025-deepseek-eval 129–131).

**Proposal.** Give the document or section a field for declared scope, including exclusions, so that views like "which sources address loss of control" can tell "out of declared scope" apart from "silent".

---

## 2. Kinds the §1 table lacks, or folds together

- **Justification link: a finding or purpose that grounds a provision.** Legislative findings and EO purpose clauses are claims about the world whose legal function is to justify the operative text:
  - SB 53 finding (j) names "hacking, biological attacks, and loss of control" (142–144);
  - SB 53 Sec. 6 (752–761) is a finding the California Constitution *requires* before public access to records can be limited;
  - EO 14365 §1 (14–46) justifies §§3–8.

  My reading is that this is the most direct bridge between Joseph's "(policies & decision-making)" end of the chain and the risk claims upstream. The policy documents themselves state which risk claims they rest on. I'd model it as a relation, *justifies*, from an assertion to a normative provision, not only as a kind.
- **Formal or impossibility result.** AI 100-2 4.1.2 and 4.2.5 (3129–3145, 3314–3320) and the Vassilev release (nist-2026-vassilev-proof 35–117). These are claims about the whole space of possible mitigations, with proof status. They fit neither "argument" nor "state of evidence". Channel matters here: the press release says "there will always be a way to prompt an AI system to disregard its rules" (58–59), and in the same piece the author hedges "you likely can't patch" (108). The paper's title ends in a question mark (114). I have not read the paper, so I can't say which framing it supports.
- **Believed, with adjudication deferred to another body.** "Although the Administration believes that training … does not violate copyright laws, it acknowledges arguments to the contrary exist and therefore supports allowing the Courts to resolve this issue" (whitehouse-2026-legislative-framework 88–90). The author holds the view but commits only to a procedure, not to the outcome. It's a stance value, or a case of "asserted" plus a deference relation.
- **Institutional self-description and mandate.** CAISI as "industry's primary point of contact" (commerce-2025-caisi 38–42 and repeated elsewhere); "acts as a startup within government" (nist-2026-caisi-careers 21–22); TRAINS membership (nist-2026-vcat-ai-update 190–192); partnership types (vcat 171–186). These are claims about actors, not about AI. See §5 on an actor record.
- **Gap / barrier / open question.** AI 800-4 keeps three kinds of "state of evidence" apart: a missing piece of knowledge, a known obstacle, and an unsettled question (Table 2 at 564, and the codebook at 1582–1645). Your "state of evidence" row could adopt that three-way split directly.

---

## 3. Relations the synthesis lacks (between instruments)

§5's lineage covers assertions that derive from, version, or contest one another. My legal and executive documents relate to each other in ways that aren't lineage:

| Relation | Example |
|---|---|
| **rescinds / replaces** (the successor is often a different administration, so this isn't "versioned within an author") | NSPM-11 "rescinds and replaces National Security Memorandum-25" (130–131); EO 14365 recounting the revocation of the predecessor's order (18–19) |
| **orders revision of** | Action Plan: "revise the NIST AI Risk Management Framework to eliminate references to misinformation, Diversity, Equity, and Inclusion, and climate change" (233–236); VCAT's "Revised NIST AI RMF" forthcoming (413) |
| **tasks → fulfils** (execution of a mandate) | Action Plan 240–243 tasks CAISI with PRC-model evaluations; the DeepSeek report quotes that tasking as its warrant (caisi-2025-deepseek-eval 112–116); the VCAT deck tags ten slides with the "AI Action Plan Item" each one fulfils (e.g. 204, 257, 294) |
| **preempts / seeks to preempt / carves out** | EO 14365 §§3–8 and its carve-outs (138–150); legislative framework (176–205); SB 53's own preemption of local law (748–750) |
| **deemed equivalent to** (conditional on designation) | SB 53 435–449 and RAISE 361–382: compliance with a designated federal standard counts as compliance. A model card counts as a transparency report (SB 53 332–334) |
| **incorporates by reference, sometimes altered** | NSPM-11 *AI* = 15 U.S.C. 9401(3) (196). DHS quotes EO 14110's *foundation model* but stops before the risk clause (dhs 1276–1278), which is a derived-with-change at the definition level |
| **disapplies where it conflicts with** | SB 53 5(d): "a contract between a federal government entity and a frontier developer" (743–744) |
| **withdrawn** (a document state, not a relation) | the CAISI agreements page has been 404 since 2026-05-08; the text survives only on Wayback (nist-2026-caisi-agreements 2–6) |

Without *rescinds* and *orders revision of*, the "silent change" analysis in §5 will misattribute changes in these documents. The AI RMF revision, for instance, is externally ordered, not an author's own drift.

---

## 4. Additions to §6 (resolution), from the statutes and CAISI methods

The address-theory framing fits my documents well. Some cases it should expect:

- **Scopes finer than a document.** SB 53 defines *catastrophic risk* and *critical safety incident* twice, differently. Bus. & Prof. Code §22757.11 (187–222) defines them over *frontier* models. Labor Code §1107 (598–636) defines them over *foundation* models, and there the weights-exfiltration incident includes "damage to, or loss of, property" (627–628). The scope is the code section, not the document. AI 800-1's definition is marked "for the purposes of these guidelines only" (1048).
- **Undisclosed binding.** The EO 14409 "covered frontier model" threshold is set by a classified process (97–104). NSPM-11 has a classified annex (123–124). The agreements page reports "testing in classified environments" (nist-2026-caisi-agreements 50–51). The resolution outcomes should include **"bound, content withheld"**, distinct from "none" and from "ambiguous".
- **Delegated binding.** "A best practice is for an organization to define the insider threat in a way that addresses the unique nature of its operating environment" (cisa-2026-insider-threat-guide 405–412). The DHS glossary: "[we] defer to entities to use the definitions most appropriate to their activities" (dhs 1216–1218). In both, the source hands the binding to the reader.
- **An operational definition in the methods, carried unqualified into the headline.** The DeepSeek report counts a model as "hijacked" if it *attempts* the malicious task, "regardless of whether it succeeds" (1496–1509). The executive summary (35–37) and the news release (nist-2025-caisi-deepseek 91–94) both say "12 times … more likely … to follow malicious instructions". My reading: the headline occurrence should resolve *through* the methods-section binding (a mediated path within one document), and the release is a derived-with-change where the qualification drops. Similarly, "CCP alignment score" is a binding of "alignment" (1739–1745).
- **Definition-maintenance: please widen §22757.14 to 453–487.** The criteria continue past 480 with "The external verifiability of determining whether a person or foundation model is covered, with an aim toward definitions that are verifiable by parties other than the frontier developer" (483–484). In address-theory terms, my reading is that this asks *who can run the match test*. I'd argue that belongs beside "determinable before training".
- **The match test determines role membership, and it can move.** A "frontier developer" is whoever "trained, or initiated the training of" a model using at least 10^26 operations, *including* compute for "any subsequent fine-tuning, reinforcement learning, or other material modifications the developer applies to a preceding foundation model" (SB 53 241–250). A fine-tuner can therefore cross into the role. "Large" is measured with affiliates aggregated (252–253). This bears on Joseph's open "developer" decision. The statutory "developer" is a threshold-tested role that attaches to a legal person, not to a kind of organisation.
- **"Alignment" and "control" as further drift cases.** The six senses of "alignment" in my atlas (Across the set, 3) and NSPM-11's two senses of "control" are collisions of the same kind as your safeguard example. The one I'd flag most: AI 100-2's "misaligned outputs" (2918–2923) means outputs aligned with an *attacker's* objective. A naive map to our "misalignment" would invert it.

---

## 5. Record kinds and axes

- **An actor record with time-indexed names and mandates.** The same institution authored AI 800-1 as the "U.S. AI Safety Institute" (Jan 2025, nist-2025-managing 6) and the GLM-5.2 report as CAISI (Jul 2026). The rename was announced as a change of mission ("Pro-Innovation, Pro-Science", commerce-2025-caisi 8–21). The consortium was renamed "to reflect the group's newly expanded goals" (nist-2026-ai-consortium 30–31, 45–52). Author clustering and "versioned within an author" both need an actor that persists across names, with its mandate claims attached and dated. Roles (§7) then attach to actors *at a time*.
- **Recorded events that will exist only as aggregates.** SB 53 and RAISE create statutory incident reports that are exempt from public-records law (SB 53 407–411; RAISE 323–327). Only "anonymized and aggregated" annual reports will be published (SB 53 413–415, from 2027; RAISE 328–333, from 2028). Classification into "critical safety incident" is triggered by the developer's own "determination", or by "learning facts sufficient to establish a reasonable belief" (RAISE 290–296). The model should expect event records known only in aggregate, and classification acts performed by a party with an interest in the outcome.
- **Qualifier axes the §4 list lacks:**
  - **Configuration of the measured system.** The CAISI reports treat this as decisive. System-level safeguards are disabled for capability runs and enabled for safeguard runs, while model-level safeguards stay on (caisi-2026-glm52 458–469). The same holds for API vs self-hosted weights ("Evaluations run against those APIs may lead to different results", 441–446), FP8 quantization (448–451), scaffold and token budget (472–488), and "maximum reasoning settings" (nist-2026-caisi-glm53 96–97). The "setting" axis (controlled vs real) doesn't capture any of this.
  - **Instrument access.** Public, private, non-public or held-out, and "semi-private" ("these tasks may have been exposed to limited third-parties", nist-2026-caisi-deepseek-v4 139–143). Private benchmarks are CAISI's defence against contamination (caisi-2025-deepseek-eval 2217–2279), and also what makes the result uncheckable by outsiders.
  - **Derivation of the number.** Direct, aggregated through a fitted model (the IRT "cyber capability index"), imputed ("***Imputed from a subset of samples via IRT", deepseek-v4 135; glm52 317–318), or extrapolated from a trend line ("lags behind the frontier by about 8 months", deepseek-v4 32). A lag measured in months is a claim about a fitted trend, not about any benchmark.
  - **Reference class defined by the measurer.** "Frontier models are defined as those with a greater latent capability level than any previous model released by developers from that country" (glm52 514–516). "U.S. frontier best" includes trusted-access releases but excludes unreleased models (glm53 64–70). Your "baseline" axis should allow the baseline to be itself a definition, owned by the source.
  - **Legal-standard qualifiers.** "Foreseeable and material", "materially contribute" (SB 53 187–190), "reasonable cause to believe" (647–648), "made in good faith and was reasonable under the circumstances" (350–351). These are tests a fact-finder applies, not likelihoods, and they shouldn't be forced onto a PHIA-like scale.
  - **Practice maturity.** AI 800-2's "[Emerging Practice]" tag (153–154, 346, 360, 402).
  - **Withheld / classified.** Also needed as an assertion-level marker (see §4).

---

## 6. Precedents the synthesis missed

| Precedent | Where | What it offers | Correlation to mark |
|---|---|---|---|
| **AI RMF Appendix A: AI actor *tasks*** | nist-2023-ai-rmf 1584–1660 | Roles defined as tasks per lifecycle phase, not as organisations. The same job title appears under several task categories ("developers" 1602, "software developers" 1611, "product developers" 1619). An explicit separation rule: V&V actors "distinct from those who perform test and evaluation" (1625–1633). It is direct precedent for "developer dissolves into roles". | NIST; the Action Plan has ordered the RMF revised (the revision is pending) |
| **DHS roles × responsibility-areas matrix** | dhs-2024-ai-roles-framework 396–464, 1158–1214 | Five roles × five areas. "Entities may play more than one role" (421–429). "AI developers include model developers as well as application developers" (447–448). The glossary's deployer "may … develop the models themselves" (1232–1235) shows the collision happening *inside* one source. | Board of CEOs including OpenAI, Anthropic, NVIDIA, Microsoft and Alphabet (121–158); a prior administration's document |
| **DHS scale-ordered risk categories** | dhs 332–386 | Asset → sector → systemic/cross-sector → nationally significant, adapted from NSM-22, with a compounding claim (383–386). A degree/scale tree for Joseph's impact radius, as a companion to the CRA's groups. | as above |
| **AI 800-1 threat profile + barriers** | nist-2025-managing 1099–1102; 1585–1612 | A four-slot claim form (malicious task, actor, way of use, harm mechanism). Technical, operational and motivational **barriers**, i.e. existing controls that a model may erode. This is the "preventions & controls" stage of Joseph's chain seen from the misuse side. Also *marginal risk* (182–183) and *margin of safety* (1063–1068). | U.S. AISI second public draft, Jan 2025; never finalised, as far as my set shows |
| **AI 800-2 measurement construct / criterion / instrument / validity** | nist-2026-ai-800-2-ipd 1579–1600 | Measurement theory's version of your §6: the construct is the intended referent, the criterion is the match test, the instrument is what performs the match, and validity is evidence for the interpretation. It is a second, independent vocabulary for the same gap, published by a source. | ipd, same as Practice 3.3 |
| **AI 100-2 stable IDs in a polyhierarchy** | vassilev-2025-adversarial 297–362 | Kinds carry stable IDs (NISTAML.018) and sit under several parents at once. Prompt injection sits under availability, integrity, privacy and misuse (329, 342, 349, 359). A precedent for `terms/` kinds that don't fit a tree. | NIST ITL with a UK AISI co-author |
| **CAISI's four-voice report template** | caisi-2026-glm52 85–101 (repeated 124–136, 158–169, 195–222) | Separate slots for the evaluator's assessment, the evaluator's results, the developer's quoted claim, and the evaluator's comment disputing it. Your author layering plus stance, formatted by a source. | CAISI; a government evaluating foreign competitors' models |
| **CISA staged pathway model** | cisa-2026-insider-threat-guide 661–760 | Stage as a position in a process that is not deterministic: it "does not guarantee", and people "may skip certain steps" (691–698). It supports "stage is a role relative to a focal event". Case studies are coded against it (810–860). | FBI-adapted; about humans only |

---

## 7. Checking your summaries of my findings

- AI 800-2 Practice 3.3 (1367–1411; 1378–1379): correct.
- SB 53 §22757.14: correct as far as it goes. Please widen the range to 453–487 so it includes external verifiability (see §4).
- The four items relayed in the reading notes (definition by secret procedure, adopted third-party claims, tasking, coded reported speech): all correctly stated. Only tasking made it into the synthesis table, where it is folded under "Recommendation" (see §1a). Adopted third-party representations (caag-2025-openai-mou 36–39, 231–234) don't appear in §1 or §3. I'd add them as a stance value, *adopted in reliance*: the author records the claim and makes its own action conditional on it, without endorsing its truth.

I'm still available for follow-ups.
