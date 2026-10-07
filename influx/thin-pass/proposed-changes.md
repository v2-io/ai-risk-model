# Proposed changes to the plan and `def/`

*From the G1b thin pass, 2026-10-07, Claude (Opus 5.5). These are proposals for Joseph's decision; none has been applied. Each points to the defect in `weight-and-defects.md` that gives the evidence. They are ordered by how much downstream work they would change.*

## To the plan, `MODEL-GAMMA-METHODOLOGY-AND-PLAN.md`

1. **§3.8 and G3: add the risk-to-occurrence relation, and conferred event statuses.**
   - Add a relation from an occurrence to the risk it realizes, with a reading for partial outcomes (D-materialization).
   - Extend §3.9's conferral ("X counts as Y in C") from roles to events, so that SB 53's "critical safety incident", the EU's "serious incident" and the like are statuses an instrument confers, not kinds of event (D-conferred-events).

   *Why:* without these, a question about an incident can't be put to the statutes. G3 is where they belong, and they fit the components list without displacing anything.

2. **G1(e): make the definition frame a record type, and route the translation row through it.**
   - The SSSOM-shaped row stays for words that map to one term.
   - Definitions translate to frames: a concept plus slots, each slot with the source's words, its resolution, and a closure attribute ("means" vs "includes"). Frames need inheritance with overrides and frame substitution (D-row-vs-frame, D-frame-inheritance, D-closure, D-umbrella-vs-definition).

   *Why:* every answer in this pass was computed from frames, and none could have been computed from rows.

3. **§3.4, the resolution record: four fields.**
   - **status**, separate from outcome (D-resolution-status);
   - **two times**, read-as-of and evaluated-at (D-bitemporal);
   - **the source's declared resolution policy, kept apart from ours**, with our preference recorded beside the candidates, never replacing them (D-preference-whose);
   - **for causal slots, a bearer** (D-bearer).

4. **§3.7, lineage: two changes.**
   - Edges say which claim they carry (D-lineage-per-claim).
   - Drift is computed per slot from frames, comparing resolved tests as well as words (D-drift-needs-frames). RAISE's bearer slot is the case for the second: same words, different test.

   §1.3 item 2 might add that two of the four recurrences of SB 53's bar change its structure (L-fcf-derived, L-fgf-derived).

5. **§3.3, "bound vs match": split it into two axes.**
   - Who maintains the name's sense: the source, an outside institution, or nobody.
   - How the sense reaches instances: nearly always by match.

   The §22757.14 example should then say whether it is a match drifting with the world or a dangle of a binding to the legislature's intent (D-bound-vs-match).

   *Why:* this is address theory's own distinction, and the current wording collapses it in the one place the plan uses it.

6. **§3.3 or §3.4: a relation for publisher-level divergence.** Record when one publisher uses one word in two senses across its documents. As it stands, whether this counts as a collision depends on a scope decision (D-collide-scope). The FCF's and FGF's own notes (P-fcf-rsp-sense, P-fgf-pf-sense) are the evidence a record like this would cite.

7. **§3.5, anchors: three changes.**
   - The position selector is required whenever a quote's match count is above one (D-anchor-duplicates).
   - Each document records its text-normalization rule (D-anchor-normalization).
   - Every passage carries a version-as-read that the text itself supports, or says where the version came from (D-version-as-read).

   The table-cell gap is confirmed (D-anchor-tables).

8. **§3.8 table, SB 53 row.** "No probability or expectation involved" should be marked as a reading. On one candidate for "material" it carries a probability floor (R-material).

9. **§3.4, wording.** "two of the codes it amends" should read "two of the codes it adds chapters to" (P-sb53-enacting).

10. **G4 / G6, instance and scenario facts in our terms.** Instance and scenario facts should be in our vocabulary, with source definitions as tests over them. So the instance record's fields come from the slot vocabulary G2 and G3 define (D-scenario-in-source-terms).

    *Why:* worth deciding before G4. It changes what the pilots' translators produce.

## To the competency questions (`influx/competency-questions-draft.md`, decision 12)

11. **Q1 as written can't be answered by any source in this slice**, which classify risks and harms, not incidents. Some options:
    - split Q1 into ex-ante and ex-post forms (D-q1-type);
    - give it a date (D-q1-date) and an open- or closed-world flag (D-q1-world);
    - say it runs semasiologically, or pair it with a twin in our terms (D-q1-source-words);
    - use a case that discriminates, such as 30 deaths with 30 serious injuries, 40 deaths, or 60 deaths across several incidents (D-q1-discrimination).

12. **More generally**, every event question needs three things stated: what is stipulated, whether unstated harms are zero, and an as-of date.

## To `def/`

Nothing yet. The `ddd:` entries weren't exercised by Q1. The `thin:` terms in `records/terms-thin.yaml` are candidates for G3's *concept list*, not for entries: their glosses are first-pass. The ranking in `weight-and-defects.md` §1 is a suggestion for which concepts get refinement passes first.
