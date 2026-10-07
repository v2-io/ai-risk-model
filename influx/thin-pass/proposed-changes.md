# Proposed changes to the plan and `def/`

*From the G1b thin pass, 2026-10-07, Claude (Opus 5.5); repaired the same day after `de-novo-feedback-1.md`. These are proposals for Joseph's decision; none has been applied. Each points to the defect in `weight-and-defects.md` that gives the evidence. They are ordered by how much downstream work they would change.*

## To the plan, `MODEL-GAMMA-METHODOLOGY-AND-PLAN.md`

1. **§3.8 and G3: relations between occurrences and risks, and conferred event statuses, if the competency questions ask about incidents.**
   - SB 53 alone has two relations (D-materialization):
     - an occurrence *realizes* a risk (materialization), which needs a reading for partial outcomes;
     - an occurrence *demonstrates an increase* in a risk.
   - Extend §3.9's conferral ("X counts as Y in C") from roles to events. The slice confers such statuses in several instruments, and in stages: the FCF's internal "AI Event" assessment feeds the statutory "Critical Safety Incident" (D-conferred-events).

   *Why:* a question about an incident can't be put to these sources without them. *Whether they come first* depends on decision 12. If questions are risk-shaped, these can wait (weight-and-defects.md §1).

2. **A decision for Joseph before G1(e): where a source definition's precision lives.**
   - **Option A, frames in the translation layer** (what this pass did). The lexicon holds the slot vocabulary.
   - **Option B, precise lexicon concepts.** Each source's definition becomes a concept whose delimiting characteristics are the slots, and the translation row maps one to one. This reading fits the plan's stated lexicon shape (§2) and acceptance test 1.

   The slot structure is needed either way. So are inheritance with overrides (two codes, RAISE), a closure attribute ("means" vs "includes"), and separate umbrella and definition kinds. Frame boundaries should follow the source's own tie-ins, such as category tables "this definition … addresses" (D-row-vs-frame, D-frame-inheritance, D-closure, D-umbrella-vs-definition, D-frame-boundary).

   *Why:* every answer in this pass was computed from slot structures, and none could have been computed from SSSOM rows.

3. **§3.4, the resolution record: four fields.**
   - **status**, separate from outcome (D-resolution-status);
   - **two times**, read-as-of and evaluated-at (D-bitemporal);
   - **the source's declared resolution policy, kept apart from ours**, with our preference recorded beside the candidates, never replacing them (D-preference-whose);
   - **for causal slots, a bearer** (D-bearer).

4. **§3.7, lineage: four changes.**
   - Edges say which claim they carry (D-lineage-per-claim).
   - Templates of unknown authorship get their own nodes, and descendants are compared with each other, not only with the root (D-lineage-template). The FCF and FGF share wording that is in neither SB 53 nor the EU Code.
   - Drift is computed per slot from frames, comparing resolved tests as well as words (D-drift-needs-frames). RAISE's bearer slot is the case: same words, different test.
   - Drift reports relocated clauses as moved (D-frame-boundary).

   §1.3 item 2 might add that two of the four recurrences of SB 53's bar change its structure, through one shared template.

5. **§3.3, "bound vs match": split it into two axes.**
   - Who maintains the name's sense: the source, an outside institution, or nobody.
   - How the sense reaches instances: nearly always by match.

   The §22757.14 example's wording ("what it was meant to") already takes the dangle reading. It should name that as one of two, the other being a match drifting with the world (D-bound-vs-match).

   *Why:* this is address theory's own distinction ("Kind follows maintenance").

6. **§3.3 or §3.4: a relation for publisher-level divergence.** Record when one publisher uses one word in two senses across its documents, or, as the FGF may with "severe harm", within one. As it stands, whether this counts as a collision depends on a scope decision (D-collide-scope). Anthropic's note on the RSP (P-fcf-rsp-sense, confirmed by P-rsp34-fn1) is a source-stated case. OpenAI's "severe harm" is our inference, not OpenAI's statement.

7. **§3.5, anchors: three changes.**
   - The position selector is required whenever a quote's match count is above one (D-anchor-duplicates).
   - Each document records its text-normalization rule. The hyphen rejoin is a live hazard in RAISE (D-anchor-normalization).
   - Every passage carries a version-as-read that the text itself supports, or says where the version came from (D-version-as-read).

   The table-cell gap is confirmed (D-anchor-tables).

8. **§3.8 table, SB 53 row.** "No probability or expectation involved" should be marked as a reading. On one candidate for "material" it carries a probability floor (R-material).

9. **§3.4, wording.** "two of the codes it amends" should read "two of the codes it adds chapters to" (P-sb53-enacting).

10. **G4 / G6, instance and scenario facts in our terms.** Instance and scenario facts should be in our vocabulary, with source definitions as tests over them. So the instance record's fields come from the slot vocabulary G2 and G3 define (D-scenario-in-source-terms).

    *Why:* worth deciding before G4. It changes what the pilots' translators produce.

## To the competency questions (`influx/competency-questions-draft.md`, decision 12)

11. **Q1 as written asks the slice's sources something they don't say in those words.** They call risks catastrophic or systemic and harm severe, and they label incidents with other terms ("critical safety incident"; the FCF's and FGF's incident ladders). Some options:
    - split Q1 into ex-ante and ex-post forms (D-q1-type);
    - give it a date (D-q1-date) and an open- or closed-world flag (D-q1-world);
    - say it runs semasiologically, or pair it with a twin in our terms (D-q1-source-words);
    - use a case that discriminates, such as 30 deaths with 30 serious injuries, 40 deaths, or 60 deaths across several incidents (D-q1-discrimination). These discriminate among the bars, not among SB 53's precise clauses; see item 13.

12. **More generally**, every event question needs three things stated: what is stipulated, whether unstated harms are zero, and an as-of date.

13. **G4 and later passes: weigh terms only with a question that can weigh them.** A thin pass can rank terms only by a question that supplies facts they test, so the next weight-finding pass should use a documented instance (Q17–Q19, or AISI's INC-2026-07-28-01), not a two-fact hypothetical. Report weights at the row, and list what the evaluator cannot evaluate (D-encoding-limits).

## To `def/`

Nothing yet. The `ddd:` entries weren't exercised by Q1. The `thin:` terms in `records/terms-thin.yaml` are candidates for G3's *concept list*, not for entries: their glosses are first-pass. `weight-and-defects.md` §1 gives the list, but it is not a ranking. This slice can't rank them.
