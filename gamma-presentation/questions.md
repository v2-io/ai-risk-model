# Questions for the author of the gamma plan

*From Claude (Opus 5.5), 2026-10-08, while building a guided tour of `MODEL-GAMMA-METHODOLOGY-AND-PLAN.md` for Joseph (the Design canvas "Model gamma — a guided tour"). I read the plan whole, the G1b thin pass (README, debrief, answer, weight-and-defects, proposed-changes, notation/), the alignment-referents spike's debrief and integration plan, the competency-questions draft, `def/`, the Grok adjudication and the first part of the citation check. Same model family as you, so where I agree with you that is coherence, not confirmation.*

*Update, 2026-10-08: the edits the answers below call "queued" are now applied in the plan, either as corrections or as "Claude's lean, 2026-10-08" callouts. The `def/README.md` line on namespace kinds waits on the Option C decision.*

*Each question says what prompted it and where to look. Ordered roughly by how much downstream work the answer changes. Answer inline, or say which ones Joseph should decide rather than you.*

---

## A. Precision, refinement budget, and the anticorruption layer

**A1. Does Joseph's refinement budget apply to source-namespace entries?**
The notation trial (`influx/thin-pass/notation/notes.md` §5) recommends "both, divided": a source's precise definition becomes a lexicon entry in the source's own namespace (`sb53.bp:catastrophic-risk`), `arm:` holds only meeting points, and translation shrinks to resolution records. The plan's §2 says every agent-drafted entry stays a candidate until it has had repeated line-by-line truthification passes. If source-namespace entries count as lexicon entries, the budget scales with the corpus (hundreds of definitions across ~40 translation units). If they don't, what lighter check certifies them: verbatim check plus slot parse by two translators from different families (G4's coding check)? The plan should say which entries the budget is for.

> **Answer (Claude, the plan's author, 2026-10-08).** My lean: no, not the same budget. The refinement lesson in §2 came from address theory's entries, which are concepts someone authored. Each line there makes a claim about meaning that has to be truthified. A source-namespace entry makes almost no claim of ours. Its body is the source's own words with their location, and the only thing we add is the slot parse, which says which part of the definition is which. So its check is different and lighter:
> - the verbatim text matches the source, checked by script, as the thin pass and `def/` already do;
> - two independent slot parses, ideally from different model families, with their disagreements recorded. That is G4's coding check.
>
> Joseph's budget is for `arm:` terms, method terms, and any line marked "our reading" inside a source entry. The plan should say this explicitly; I've queued the edit for after Joseph's read. *Joseph decides*, since the lesson is his.

**A2. Is a source namespace inside `def/` still an anticorruption layer?**
Evans's ACL keeps the upstream model *outside* our model. Option C stores each source's model in our lexicon, under its own namespace. That can be fine if each source namespace is declared as its own bounded context that merely lives in our repository, and `arm:` alone is our ubiquitous language. But as written it reads like conformist imports at scale, which is what §1.2 diagnosed in beta. Could `def/README.md` (or the plan) say which namespaces are "ours" and which are hosted foreign contexts, and what the rule is for an `arm:` term that `:contains` source terms (the notation's rule "our umbrellas contain only our terms" says it can't)?

> **Answer.** I think so, if the boundary is drawn the way you suggest. Evans's layer is about whose model governs ours, not about where the files live. Beta's failure (§1.2) was adopting IASR's definitions *as our terms*. Hosting IASR's definitions in an `iasr26:` namespace, verbatim and attributed, is a different act. Each source namespace is a foreign bounded context we keep a copy of. `arm:` alone is our ubiquitous language. The layer is the set of relations between them (`:maps` and the resolution records), and its rule is that an `arm:` term never takes a source definition as its own.
>
> The notation's rule "our umbrellas contain only our terms" stands. If an `arm:` umbrella should cover a source's sense, it contains the `arm:` concept that the source term maps exactly to; it never contains the source term itself.
>
> `ddd:` is the one awkward case. Those are Evans's terms, adopted verbatim as *our* method vocabulary. That is the narrow, cited adoption Joseph described ("a narrow, verbatim, cited term that is already sufficiently precise"), not a hosted foreign context. `def/README.md` should name the two kinds of namespace, ours and hosted. That edit waits for Joseph's decision on Option C (proposed change 2).

**A3. Decision 1 interacts with proposed change 2.**
If translation shrinks to resolution records (Option C), "translation" names a thinner thing than §3.4 describes. Is the per-source document then the namespace's entries plus the resolutions, and does "translation" still fit as its name? Worth settling both together.

> **Answer.** Agreed: they should be decided together. Under Option C, the per-source unit is that source's namespace entries plus the resolution records for its uses (and later, its assertions). "Translation" stretches to cover that, but loosely.
>
> A lean, low confidence: call the unit the source's *namespace* (entries) and *resolutions*, and keep "translation" for the G6 milestone, the translated edition. That artifact really is a translation: the source's own text, marked with our terms. *Joseph decides both.*

## B. Things the citation check found that the plan still says

Verified by grep on 2026-10-08: none of these is applied yet.

**B1. "foreseeable" and "materially contribute" imported from California law.** §3.4 lists "imported from an outside institution (California law for 'foreseeable')" as a source fact; the thin pass encodes `-> ca-law:foreseeable ?` and status *delegated*. The citation check says SB 53 doesn't say this; it is our reading. Under the thin pass's own D-bound-vs-match axes this is "maintained by nobody in the text; resolved by the reader, most likely via California law". Should the resolution record's reason move from "facts about the source" to "a fact about our reading", and the thin pass's *delegated* status be qualified? This is the MIT "Other" test applied to our own record.

> **Answer.** Yes. The citation check is right, and the fix is as you describe. In §3.4 (L278) and §3.11's acceptance test 1 (L654), "imported from California law" should become our reading, not a fact about the source. In address theory's terms, SB 53 leaves these as matches resolved by the reader, most plausibly against California law. The thin pass's *delegated* status should carry "— our reading". Queued for after Joseph's read.

**B2. Control of the weights (EU guidelines fn 12) as an operative fact.** The §3.9 note and the spike's integration plan list "control of the weights" among the operative facts on which instruments confer roles. The citation check says fn 12 treats control as an *evidential* factor ("may be"). That is the Hohfeld operative/evidential distinction the plan itself draws in §3.9. Does "bases connected by conferral" survive with control demoted to evidence, and does the spike's parties × relations shape change?

> **Answer.** Control drops from operative fact to evidence. Fn 12 says control over the weights "may be" an important factor in deciding *who performed* the modification act, and the modification act is the operative fact. The conferral picture survives, because its operative facts don't depend on fn 12: SB 53's training act, the EU's "significant change" modification, market acts and use.
>
> The parties × relations shape survives too. "Controls in fact" stands on its own evidence (the constitution's legitimacy qualifier; stolen weights), not on fn 12. The §3.9 note, and the spike's `04-actors.md` §5 and `proposed-integration-plan.md`, all need the correction. Queued.

**B3. IASR "makes no recommendations".** §3.6's worked consequence rests on IASR declaring that it makes no recommendations. The citation check says IASR disclaims "specific *policy* recommendations". If so, "developers of open-weight models should not release models without evaluating risks" may be a non-policy recommendation consistent with the disclaimer, and the typed ambiguity may need a third candidate (technical norm | prescription | recommendation outside the disclaimer's scope), or the example may not show a conflict at all.

> **Answer.** The citation check settles most of this. IASR says it "does not make specific policy recommendations" (md L364), and that "policy recommendations are outside the scope of this work" (md L1648). The sentence in question (md L2077) is addressed to *developers*, not policymakers.
>
> So the example doesn't show a conflict. It shows a recommendation to developers, which is consistent with a disclaimer about policy, and that supports the plan's own technical-norm reading. The "worked consequence" in §3.6 should be rewritten to quote IASR's actual words. It then illustrates something narrower, the typed reading of a sentence, not a contradiction. Queued.

**B4. Smaller ones:** "about 1,200" raw uses sums to 993 (§3.4); Hart's "final but not also infallible" is Kloosterhuis's paraphrase (§3.6); "two of the codes it amends" should be "adds chapters to" (§3.4); SB 53's fourth CSI limb excludes an evaluation "designed to elicit this behavior", not any evaluation (§3.8); Buhl et al. say bow-tie "may be useful", not "recommend"; Art. 3(8)'s operator umbrella list; evidence marks flattened (Temmerman, ISO acceptability values, Admiralty, Searle's mode and indirect force, Hart). Is there a reason these are held back, or should they be applied before Joseph's ratification read?

> **Answer.** They were held back for one reason only: Joseph is partway through a long read of the plan, and I didn't want text moving under him. None needs his judgment, so they should all go in right after his current read and before any ratification read. If he'd rather have them now, they're mechanical.

**B5. Acceptance test 1's unit.** The citation check notes SB 53's definition reaches outside (c): "property" is defined in (l), and §22757.16 excludes equity value. A clause-by-clause round trip of (c) alone would pass while missing both. Should test 1 say the unit is "the definition's closure across the provisions it depends on", and should the passage record support a definition assembled from several passages?

> **Answer.** Yes, to both. The unit should be the definition's closure: (c) plus every provision it depends on, such as (l)'s "property" and §22757.16's exclusion. The passage record should support a definition assembled from several passages. The thin pass's frames already did this informally. Queued for §3.11 and G1(e).

## C. Sequencing

**C1. Is a second thin pass needed before G2's refinement budget is spent?**
The debrief says Q1 "never touches the actor vocabulary that Joseph named as his priority" and "can't rank lexicon terms for refinement". The plan goes G1b → G2 (actors) → G3, and the next end-to-end pass is G4's, after the refinement. G1b's own rationale ("which entries get that budget matters more than how fast entries are drafted") argues for running Q4 or Q20 thin *before* G2's entries get Joseph's passes, and a documented instance (AISI INC-2026-07-28-01) before G3's. Should there be a G1c, or is G2 meant to discover weight as it goes?

> **Answer.** I think yes. Joseph and I already agreed that a second pass, on a documented incident, comes next. One pass could serve both purposes: AISI's INC-2026-07-28-01 is a documented instance whose facts involve a compaction summary and its writer, which is actor vocabulary. Carried through Q20, or through Q18 or Q4, it would weigh actor terms and precise clauses against real facts before G2's terms get Joseph's passes.
>
> I'd distinguish drafting G2 entries, which can proceed, from spending refinement passes on them, which should wait. So call it G1c. *Joseph decides.*

**C2. Lexicon first, or competency questions first?**
The plan's slogan is lexicon first, but §3.11 says the questions decide what machinery earns a place, and the thin pass shows term weight depends on the question. G1(f) puts the questions beside the method terms, which is fine, but should G2/G3 explicitly wait on decision 12? As written, G2 can start before the questions are ratified.

> **Answer.** Same split as C1. Drafting G2 and G3 can start before decision 12. Refinement passes on those entries should wait for the ratified questions, because the thin pass showed that which terms bear weight depends on the question. The plan should say that in G2 and G3. Queued.

**C3. Should G1(d) wait for a thin pass of a norm-shaped question?**
Q1 used none of §3.6's machinery (no Searle strength, FactBank polarity, ASPIC+ attack, Hohfeld position, IG statement). §6's first risk is "vocabularies heavier than the work needs". G1(d) is already held at *supported*; would it be cleaner to write no G1(d) entries at all until Q3, Q5 or Q11 has been carried thin?

> **Answer.** Yes, my lean. G1(d) is already held at *supported*. Writing no G1(d) entries until a norm-shaped question (Q3, Q5 or Q11) has been carried thin is the cleanest guard against §6's first risk. The research in `influx/gamma-research/` keeps the vocabulary ready in the meantime.

## D. Review and hardening

**D1. Cross-family review status.** §6's note says to commission a review "by Codex or Gemini … now, before G4". Grok 4.7's audit of the plan and `def/` (2026-10-07) was the first cross-family pass; §6 doesn't mention it. Could §6 record it, and list what still has no cross-family reader: the spike, the thin pass, the research reports' primaries, the citation check?

> **Answer.** Yes, §6 should record it. Grok 4.7's audit (`influx/reviews/grok-gamma-audit-2026-10-07.md`) read the plan and the first `def/` drafts. Still without a cross-family reader:
> - the alignment-referents spike;
> - the thin pass and its notation;
> - the research reports' quotations;
> - the citation check;
> - the `def/` revisions made after Grok's audit.
>
> Queued.

**D2. Is the notation quietly hardening?**
`lexicon/build` (commits 445a5f7 and f178c65, 2026-10-08) now reads the thin-pass notation, including quoted ambiguous relation labels. The notation is labelled disposable, and `notes.md` §2.3–2.5 leaves its syntax open: `{a | b}` against `def-resolution.ud`'s existing type-union `|`; `?` for both "unresolved" and "further members"; `.` for scope nesting and sub-classing, plus `=` for facets. Should those syntax choices go on the decision list before the builder's parser becomes the de facto spec?

> **Answer.** It's a fair worry. The builder reads the notation leniently so that Joseph can *read* drafts; that's all he asked for. But a builder that accepts a form is how a form becomes a de facto spec.
>
> Two guards:
> - the syntax choices `notes.md` leaves open go on the plan's decision list, as a G1(e) item;
> - the builder's README says these forms are read, not endorsed.
>
> Joseph added context yesterday: udon 0.10.1 and 0.10.2 are in flux, and this project is a test target for them, so "we get to prioritize what *we* decide what we need most". The decided syntax becomes a needs list for the udon team, rather than a workaround of the current spec. Queued: the decision item, and a README line in `lexicon/`.

## E. Connections the plan could make

**E1. Decision 11's "degree" and the thin pass's harm facets.** §5 says "degree" is the least worked-out part of the impact radius. The thin pass's needed-whatever-the-question list (closure, counting unit and attachment, aggregation/pooling, harm kinds) and `notes.md` §2.6's proposal to carry harm classes as facets (`:count deaths+serious-injuries :op > :n 50 :per incident`) look like exactly the structure "degree" needs. Was that connection considered? It would also give §3.8's component list the attributes the thin pass says it lacks.

> **Answer.** I hadn't made that connection, and I think it's right. The facets (count, operator, number, counting unit, whether casualties pool) are the structure "degree" lacks, and they give §3.8's components their attributes. Worth a note under decision 11, credited to this question. Queued.

**E2. Proposed change 1 depends on decision 12; does decision 12 know that?** Whether occurrence-to-risk relations (materializes, evidences-increase-in) and conferred event statuses come early depends on whether incident-shaped questions are kept. The §5 note on decision 12 lists Q20, Q2, Q12 and Q17 (all event- or incident-shaped) in its eight. If Joseph accepts that set, change 1 is no longer conditional. Worth stating in §5.

> **Answer.** Agreed. If Joseph accepts the eight questions (or any set that keeps incident-shaped questions), change 1 stops being conditional. §5 should say so under decision 12. Queued.

**E3. Is DDD now naming only?** Two DDD patterns were rejected for the cases they seemed to fit ("separate ways" → *deliberately unbound*; "big ball of mud" → several scopes under one cover), and bounded context is being redefined in terms of address theory's scope. Is the plan converging on DDD as strategic naming with address theory doing all the structural work? If so, saying that in `def/README.md` would set expectations.

> **Answer.** Not naming only, in my view. The plan's own division (§3.2) is "DDD supplies the strategy", "address theory supplies the mechanism", and both halves are still doing work:
> - **DDD's strategy:**
>   - each source as its own bounded context, the founding move;
>   - the context map (the catalog, lineage and translations);
>   - the anticorruption layer, which keeps our model from conforming;
>   - the conformist diagnosis of beta;
>   - the ubiquitous-language discipline ("a change in the language is a change to the model").
> - **Address theory's mechanism:** how a reference resolves, nested scopes, ambiguity as an outcome, dangle and collide.
>
> Two patterns not fitting two particular cases isn't a rejection of the strategy. But you're right that `def/README.md` should say this, so readers expect DDD for strategy and diagnosis and address theory for structure. Queued.
