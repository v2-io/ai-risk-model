# De novo feedback 1 on the G1b thin pass

*An independent critical and adversarial pass over `influx/thin-pass/` as committed in `f942593`. Claude (Opus 5.5), 2026-10-07, a fresh agent with no part in the pass, briefed only to audit it. Same model family as the author, so this is a second reading, not a different-family check.*

*What I did. I read every file in the directory. I re-ran `tools/check.py` and `tools/answer.py`; all 53 quotes pass, and the generated block in `answer.md` reproduces byte for byte. I read the source extractions around every load-bearing passage, and further than the pass did in the FGF, FCF, xAI 2026 and PF. I extracted two documents the pass did not read (the EU Code's Safety and Security chapter and Anthropic's RSP v3.4) into my scratchpad, and I ran n-gram overlap comparisons between the frameworks. I probed the evaluator with throwaway scripts that force each ambiguity's candidate through the whole frame. I checked the address-theory quotes against `arch/firmatum/udon/v2/references/def/`, and the plan statements the pass relies on against `MODEL-GAMMA-METHODOLOGY-AND-PLAN.md`.*

*One slip of mine, already repaired. A probe that imported `answer.py` wrote a `.pyc` into `tools/__pycache__/`. While removing it I also deleted `check.cpython-311.pyc`, which turned out to be committed. I restored it with `git checkout`, and `git status` on the directory is clean. That committed `.pyc` is itself a small finding (§8).*

---

## The short version

1. **The computed weights can't carry the debrief's main inference.** The evaluator only finds an ambiguity decisive if the author encoded it as an `ambiguous:` node. Seven were encoded, all about magnitude, aggregation and umbrellas. Everything else (foreseeable, material, materially contribute, the control readings) went in as opaque facts, so it comes out "conditioning" by construction. "Decisive" is also measured at the sub-expression, not at the row's result: 13 of the 26 "decisive" labels in the tables change no row's result, and R-materialization-partial changes none at all. So "most of SB 53's precise clauses carried no weight; the structure around them did" is a fact about how Q1 and the frames were written. The run doesn't show it about the clauses. (§1)
2. **The lineage graph misses a shared template.** Anthropic's FCF v2 and OpenAI's FGF share long verbatim passages that are not in the EU Code. Among them are the "systemic" umbrella sentence and the opening of the definition sentence ("definition of systemic risk includes foreseeable and material risks of …"). The pass modelled them as two independent restatements of SB 53. Their shared drift (fatalities only, an open bar, the conduct list moved out of the sentence) is therefore probably one event counted twice. That is the error the project's "correlation is not corroboration" principle exists to prevent. (§2)
3. **The one "decisive" ambiguity rests on misread evidence, and the evidence that would bear on it was left unread.** `answer.md` quotes the FGF's note on the PF as "may use different definitions", which drops "of catastrophic risk". The note is not about "severe harm". Meanwhile the FGF reuses PF sentences that contain "severe harm" (a 51-word run and a 30-word run), at lines 129–130 and 245–248. The first sits two lines below the anchored definition. R-fgf-severe's own "decides" field names exactly this evidence as "not read". (§2.2)
4. **Several frames drop source words that matter.** Critical-safety-incident limb (4) loses "in a manner that demonstrates materially increased catastrophic risk". The FGF frame loses "our". The conduct list is reported as "dropped" by the FCF and FGF when it reappears, almost verbatim, in the risk categories the FGF ties to "this FGF definition". (§3)
5. **The ex-post half of Q1 overlooks incident labels inside the slice's own documents.** The FCF has an AI Event → AI Incident → Serious AI Incident / Critical Safety Incident ladder. The FGF grades "AI safety incidents" by severity. The debrief's "Q1 asks about an object none of these sources classify" is not true of this slice. (§4)

The anchoring, the frame-and-scenario approach, and the honesty of the limits sections are good, and most of what the pass checked by script holds (§7). The problems are in what the computation is taken to show and in where reading stopped.

---

## 1. What the evaluator can and cannot show

`weight-and-defects.md` separates *computed* weights from *judged* ones, and the debrief leans on the computed side: "Running each ambiguity's readings through the frames turned 'this term matters' into a checkable claim." Three things limit what that checkable claim is.

### 1.1 Only encoded ambiguities can be decisive

`records/translation.yaml` has `ambiguous:` nodes for exactly seven records: R-single-incident-attachment, R-pooling, R-materialization-partial, R-fcf-dollar-attachment, R-fgf-umbrella-closure, R-fgf-severe and R-pf-thousands. Other records have candidates in `resolutions.yaml`, but their slots are plain facts:
- R-material has three candidates, and its slot is `{fact: risk_material}`;
- R-control has three candidates, and its slots are `fact_in` / `{fact: loss_of_control}`;
- R-foreseeable and R-materially-contribute are delegated, with no candidates at all.

A plain fact that no scenario sets is "open" in every scenario. So tier C's label "Conditioning (computed)" is a property of the encoding: those terms could not have come out any other way. Tier B's decisive set is likewise the set the author chose to encode. That set sits entirely on the magnitude, aggregation and umbrella side, and that is the side the ranking then promotes.

That doesn't make the inference wrong. For a hypothetical that stipulates two facts, the clauses that test unstipulated facts can't decide anything. But that is a fact about Q1. The evaluator did not discover it, and a question built on a documented instance (Q17–Q19, or AISI's INC-2026-07-28-01) would make "foreseeable", "materially contribute" and the conduct list the decisive slots. The honest form of the debrief's headline is something like: "Q1 stipulates no facts that SB 53's precise clauses test, so in Q1 they could only be named, not weighed."

### 1.2 "Decisive" is measured below the row

`ev()` marks an ambiguity decisive when its candidates give different values *at the node where it sits*. The row's result is not consulted. I forced each candidate through the whole frame for every row the tool marks decisive (`scratchpad/probe/rowlevel.py`, reconstructable from this description):

| | rows marked decisive | rows where the choice changes the row's result |
|---|---|---|
| R-fgf-severe | 5 | 5 |
| R-pooling (`v-mixed-casualties`) | 9 | 4 (the catastrophic-risk rows) |
| R-single-incident-attachment (`v-several-incidents`) | 9 | 4 |
| R-materialization-partial (`v-40-deaths`) | 3 | **0** |

In the critical-safety-incident rows, limbs (1), (3) and (4) stay open, so `any()` is open whichever way limb (2) goes. The same holds in the umbrella rows, where the EU member stays open.

So these statements are not supported as computed:
- `weight-and-defects.md` A.1: "Whether a partial outcome counts as materialization is decisive in `v-40-deaths`";
- `answer.md`'s limb table: "moot at 60, decisive at 40";
- `terms-thin.yaml`'s weight for `thin:materialization`;
- the "decisive" cell for R-materialization-partial in the ambiguity-weight table.

What *is* true is conditional: it would decide limb (2) once the other limbs were ruled out. That is a reasonable thing to report, under its own name.

### 1.3 Closure is not computed at all

Tier B lists `thin:bar-closure` under "(computed)": "decisive in `v-40-deaths` (SB 53 closed: no; FCF and FGF open: open)". But `answer.py` never reads the `closure` field (`grep -c closure tools/answer.py` gives 0). Closure enters only implicitly, as the `large_scale_harm` / `severe_harm_genus` disjunct.

When I removed those disjuncts, which closes both company sentences, the FCF and FGF systemic rows for `v-40-deaths` still came out **open**: the unread EU member keeps them open. They become **no** only when `eu_systemic_risk` is also fixed false. So the SB 53 / company contrast in `v-40-deaths` is a judgment about the sentences, which are not rows in the table, and not a computation.

### 1.4 Tier A is partly circular

Tier A ("Form: without these, Q1 can't be put to the sources") rests on Q1 asking about an *incident*. D-q1-type recommends fixing exactly that, and D-q1-source-words offers an onomasiological twin: "which sources' definitions reach a risk of >50 deaths from one occurrence". Under that twin, materialization and conferred event status are no longer needed to pose the question, and the answer runs on `thin:risk.possibility` plus the slot vocabulary. That slot vocabulary is mostly §3.8's component list.

So the recommendation to put refinement on tier A "ahead of the components list" depends on keeping the very feature of Q1 that the pass calls a defect. The two need to be reconciled before Joseph uses the ranking.

### 1.5 The tables read as the sources' verdicts

The generated rows have the columns Document, Its term and **Result**. "SB 53 B&P §22757.11(c) | catastrophic risk | **no**" reads as SB 53's classification. It is our frame's output, unreviewed. CLAUDE.md asks that "our reading of a source is always attributed as ours". A column header such as "Result under our frame (F-…)" would do it.

---

## 2. Lineage: what the frameworks share with each other

### 2.1 FCF v2 and FGF are siblings, not independent restatements

N-gram overlap between `.extract/anthropic-2026-frontier-compliance-framework-v2.txt` and `.extract/openai-2026-frontier-governance-framework.txt` (8-token shingles; longest runs, in tokens):
- 32: "changes in law or regulatory guidance, changes in frontier model capabilities and related technologies, new approaches to mitigations and safeguards, other incidents affecting the industry, and new industry best practices and standards";
- 27: "including the use of model capabilities to conduct influence operations, election interference, or other coordinated campaigns to manipulate public opinion or undermine democratic processes" (the harmful-manipulation category, in both);
- 22: "both catastrophic risks under the TFAIA and systemic risks under the EU AI Act. The systemic risk assessment and mitigation processes described" (the umbrella sentence);
- 10: "definition of systemic risk includes foreseeable and material risks of" (the definition sentence the pass treats as each company's own restatement of SB 53);
- plus the same section numbering (2.1 Systemic risk identification, 2.4 Risk tiers, 2.6 Critical safety incident identification and response, 7.1 Update and approval process) and governance boilerplate.

I checked the same comparison against the EU Code's Safety and Security chapter (`eu-cop-2025-safety-security`, extracted to my scratchpad). The FCF–EU overlaps are all 10 tokens or fewer, and none of the runs above appears there. The FGF does take its category *descriptions* from the EU Code: "significantly lowering the barriers to entry …" (33 tokens) and "the inability to reliably direct, modify, or shut down a model" are EU wording. But the FCF/FGF shared tail on harmful manipulation is not. xAI's 2026 FAIF shares boilerplate with both (a 53-token run with the FGF).

The direction is undetermined. The FGF is dated 2026-05-28 by the catalog and the FCF v2 is effective 2026-07-24, but FCF v1 is unread and a common third-party template is possible. Either way:
- **L-fcf-derived and L-fgf-derived are not two independent edges from SB 53.** The structure is more like SB 53 → (template or one company) → the other, with the EU Code feeding the categories.
- **The computed drift double-counts.** "death of, or serious injury to" becoming "fatalities", the open "includes", and "foreseeable and material risks of [X] harm from the most advanced …" are shared. That is plausibly one drift event, not two companies independently reading SB 53 the same way.
- **The difference inside the shared frame is the informative part.** Anthropic's genus is "large-scale harm" with "including but not limited to"; OpenAI's is "severe harm" with "including". The pass's frames see the difference but not the shared base it differs from.

Q1's root count of one survives. The edge structure under it, and the "two of the four recurrences change its structure" observation proposed for plan §1.3, do not survive as stated.

### 2.2 The FGF reuses PF prose that carries "severe harm"

From `openai-2026-frontier-governance-framework.txt` against `openai-2025-preparedness-framework-v2.txt`:
- FGF L129–130, two lines after the anchored definition: "We evaluate whether frontier capabilities create a risk of severe harm through a holistic risk assessment process. This process draws on our own internal research and signals, and, where appropriate, incorporates feedback from …". This is the PF's L139 sentence, a 51-token run.
- FGF L245–248: "… risk tiers that concretely describe things an AI system might be able to help someone do or might be able to do on its own that could meaningfully increase risk of severe harm" (PF L169, a 30-token run).

In the PF, "severe harm" is the term its footnote 1 defines. So the FGF carries the phrase *inside sentences copied from the document that defines it*. That is real evidence for R-fgf-severe's `pf-sense-imported` candidate. It isn't decisive: copying a sentence needn't import a definition, and the FGF's own ">50 fatalities" example still argues the other way. But it bears more directly than anything the record cites, and R-fgf-severe's `decides` field ("the FGF's other uses of the phrase (not read)") names it as the deciding evidence.

The same FGF passage that the pass anchors as P-fgf-pf-sense also says the PF exists "to advance the science of managing severe risks of advanced AI systems". That associates "severe" with the PF's programme, in the FGF's own words.

The cited evidence is also misstated:
- `answer.md` short answer 5: "The FGF says the PF 'may use different definitions' (P-fgf-pf-sense)." The passage reads "may use different definitions **of catastrophic risk**". `A-fgf-pf-sense`'s note says so correctly; the answer elides it.
- `weight-and-defects.md` A.3: "The FGF's note is the main evidence for the one ambiguity that decides Q1".
- `D-collide-scope`: "OpenAI uses 'severe harm' in two senses across the PF and FGF", which is listed beside Anthropic's own note as if OpenAI had said so. OpenAI's note concerns "catastrophic risk". The "severe harm" divergence is the pass's inference.

The lean (`fgf-local`) may still be right. But the record should say what the FGF's note is about, cite the reused PF prose, and revisit the lean with it in hand.

### 2.3 The conflict-of-interest check, run in the other direction

The one decisive ambiguity in the slice landed on OpenAI. I asked whether the parallel question was put to Anthropic: does the FCF reuse RSP prose the way the FGF reuses PF prose, and does any Anthropic document bind "large-scale harm"? I extracted the RSP v3.4 (`anthropic-2026-rsp-v3-4`).
- The FCF does reuse RSP prose (runs of 49 and 37 tokens in the threshold sections).
- The RSP does not use "large-scale harm". Its footnote 1 says "catastrophic risk" "refers generally to risks of the most severe potential harms … such as existential threats or fundamental destabilization of global systems. We use this term in its plain meaning rather than adopting any specific statutory definition. Where laws such as California SB 53 define this or similar terms with specific thresholds, we address those requirements in separate compliance frameworks."

So the asymmetry between the companies comes from their word choice, as the pass implicitly assumed, and no parallel decisive ambiguity exists for the FCF. Two consequences:
- **A-fcf-rsp-sense can be upgraded** from "not checked against the RSP" to "consistent with RSP v3.4's footnote". I don't know which RSP version FCF v2 refers to.
- **`answer.md`'s "On Anthropic's report, the RSP would not call a 60-death incident catastrophic" overreaches.** The RSP's own words make its term deliberately unbound ("plain meaning"), with examples. That resolution outcome is "unbound, with examples at the extreme end". It is not "no".

One smaller asymmetry: R-fgf-umbrella-closure treats "we mean both" as possibly exhaustive. R-fcf-umbrella treats the FCF's "include both" as plainly open, with no candidate for the exhaustive reading. "Include both X and Y" is commonly read as exhaustive in drafting too. It is moot computationally, but the two records should apply the same test.

---

## 3. Frame fidelity: source words the frames drop

1. **Critical-safety-incident limb (4)** (B&P §22757.11(d)(4), RAISE §1420(4)(d), Labor Code §1107(c)(4)) ends "in a manner that demonstrates materially increased catastrophic risk". The frame tests only `deceptive_subversion_outside_evaluation`. `answer.md`'s limb table quotes the limb with an ellipsis that removes this clause and answers "Needs the catastrophic-risk conditions? no". Limb (4) needs a relation to catastrophic risk: not its materialization, but a demonstrated increase in it.

   This matters beyond the row. It is a **second relation from an occurrence to a risk**, evidential rather than realizing, in the same definition that gave the pass `thin:materialization`. Tier A.1 and the proposed plan change (a single risk-to-occurrence relation) should account for it.

   Separately, the Labor Code's limb (4) is in the frame but not anchored: P-sb53-lab-csi stops at (3).
2. **"our" in the FGF.** F-fgf-own's bearer words are "the development, storage, use, or deployment of our most advanced frontier models", and its note says "'our' makes OpenAI the bearer". The test is `model_is_frontier ∧ model_most_advanced_at_time`, with no "the model is OpenAI's". Both company frameworks classify risks from their own models (the FCF through its scope sentence, FCF L87). For Q1's "which sources would call it", whose model was involved is a condition, and the frames lose it.
3. **The conduct list did not drop out of the FCF and FGF. It moved, and it drifted on the way.** The FGF introduces its category table with "this FGF **definition** currently addresses the following systemic risk categories" (L142–144). Its Loss of control cell reads "Risks stemming from the inability to reliably direct, modify, or shut down a model, including evading the controls of a model developer or user, or autonomous conduct that, if conducted by a human, would constitute a crime of murder, assault, extortion, or theft". That is SB 53's (B) and (C), nearly verbatim.

   The FCF's category reads "… autonomous behavior that would constitute serious crimes (such as assault, extortion, or theft) if committed by a human". The list there is open ("such as") and **omits murder**.

   The slot diff reports "model-conduct: dropped" because the frame boundary was drawn at the definition sentence. A drift method blind to where a clause went will report deletions that are relocations.
4. **R-single-incident-attachment's `property-only` candidate contradicts its own evidence.** The record argues against property-only because then "a casualty risk would need no listed conduct at all". But the frame keeps `model-conduct` as an always-on slot under both candidates, so the encoded property-only reading still requires the conduct list. "arising from a single incident involving a frontier model doing any of the following" is one phrase, and the frame splits it. This changes no row's result here, since those rows are open anyway, but it is the encoding the decisive claim for `v-several-incidents` runs on.
5. **xAI's footnote is not "SB 53's definition quoted in full"** (`answer.md`, xAI section). It quotes (c)(1) with (A)–(C) and stops. The exclusions in (c)(2) are not quoted. Incorporation "as defined in the TFAIA" still brings them in, so F-xai25-cr is right. But the claim is wrong, and "the quotation is exact (checked by script)" was checked only on the head paragraph, the extent of P-xai25-fn. I compared (A)–(C) by eye and they match.

---

## 4. The ex-post half: incident labels in the slice that the answer doesn't mention

`answer.md` says that ex post "SB 53 has one label for the incident". `weight-and-defects.md` A.2 says "critical safety incident" is "the only label in the slice applied to an incident". The debrief says Q1 "asks about an object none of these sources classify".

The slice's own documents say otherwise:
- **FCF v2 §2.6** (L442–489) classifies occurrences in a ladder: "AI Event" (an observable event that "could signify" an incident), then "AI Incident", then "Serious AI Incident" (EU Code Commitment 9, AI Act Art. 55(1)(c)) and/or "Critical Safety Incident" (TFAIA). It also assesses whether a Critical Safety Incident "poses an imminent risk".
- **FGF §2.6** (L491 on): "potential AI safety incident", then "AI safety incident", with the AIRP "determining severity". This grades incidents by severity, and it is the closest thing in the slice to Q1's own word "severe" applied to an incident. The AIRP itself isn't public, so the record's outcome would be "delegated to an unpublished document".

D-q1-type's narrower claim, that none of the slice calls an incident catastrophic, severe or systemic *in those words*, holds. Its broader form, and A.2's "only label", don't. Two consequences for the proposals:
- `thin:event-status.conferred` has more instances than one, from several instruments. One of them is a company's *internal* ladder that feeds the statutory status, so the conferral is staged.
- The ex-post form of Q1 is answerable more widely than the answer shows.

---

## 5. Statements that say more than the records support

- **Debrief:** "Ex post, SB 53 calls such an incident a critical safety incident." This is unconditional. The computed result is *open*, and it would be *no* for a 60-death incident without a frontier model, or via a cause outside the limbs. `answer.md` is careful here; the debrief isn't.
- **Debrief:** "Two of that term's four limbs need no casualty bar at all." Three limbs (1, 3, 4) have no >50 bar; one (4) needs no casualty at all. "Two" fits neither count.
- **"Two orders of magnitude"** between the FGF's and the PF's "severe harm". That holds for dollars ($1B against hundreds of billions). For casualties it is >50 against "thousands": a factor of roughly 20 to 200.
- **"The only one with consequences"** (`weight-and-defects.md` A.2; `terms-thin.yaml`). Catastrophic risk carries duties of its own in SB 53: the frontier AI framework (§22757.12), the ban on materially false or misleading statements about it (P-sb53-bp-misleading, in the pass's own records), and the reports of catastrophic-risk assessments that §22757.12–.13 send to OES (L322, L408). The defensible claim is narrower: it is the label whose consequences attach to an incident.
- **"Computed"** on tier C and on `thin:bar-closure` (§1.1, §1.3), and **"decisive"** for R-materialization-partial (§1.2).
- **xAI succession.** The 2026 FAIF never mentions the TFAIA, catastrophic risk or SB 53. Its footnote 1 says its terminology is the EU Code's. The 2025 FAIF says it "complies with" the TFAIA, and SB 53 requires a large frontier developer to keep a published frontier AI framework. It is at least as plausible that the 2025 FAIF remains xAI's TFAIA framework beside an EU-oriented 2026 one. The pass does mark the succession as inference. But the computed in-force table prints "superseded", and short answer 7 builds on it.

  The 2026 FAIF also uses "systemic risk" throughout and speaks of "severe or systemic harm". For Q1's words, it is a candidate source the answer doesn't address. Its absence from the *bar's* lineage was checked, but its use of "systemic" wasn't.

---

## 6. On the proposals to the plan

- **D-row-vs-frame and Joseph's lexicon shape.** Joseph's stated shape is "the union of all the most precise, scoped, bounded, and/or specific definitions" (plan §2), with intensional definitions by delimiting characteristics (§3.3). Acceptance test 1 already asks for clause-by-clause re-expression. Read that way, SB 53's catastrophic risk becomes a precise *lexicon* concept whose delimiting characteristics are the pass's slots, and the translation row maps to it one to one.

  The pass's proposal instead keeps the precise definition as a frame in the *translation* layer, with the lexicon holding only the slot vocabulary. Both may be workable, but they put precision in different places, and the proposal doesn't say it is choosing. That choice is Joseph's lexicon-shape decision, and it should be put to him as one.
- **D-bound-vs-match.** The two-axes point is sound and consistent with address theory: "Kind follows maintenance". The other half, "The plan picks dangle without saying which", is weaker than stated. The plan's §3.3 says "its test no longer reaches **what it was meant to**", which is the bound-to-intended-referent reading. Address theory's own `dangle` covers "its referent has ceased (or moved) without the binding being updated", and SB 53 §22757.14 states the intended referent ("foundation models at the frontier"). So the plan does say which. The proposal could be narrowed to making that reading explicit, as one of two.
- **D-anchor-tables overgeneralizes.** "Only fragments survive as quotes" is true of the Harmful manipulation and CBRN cells, whose row labels wrap into the description column. It is not true of the Loss of control cell. Its full description matches exactly once (`check.py --locate`, L200–210), yet P-fgf-loc-cell anchors only "Risks stemming from the inability to reliably". The part that was cut is the part that bears on R-control and on §3.3 above.
- **Orphaned evidence for R-control.** P-fcf-loc and P-fgf-loc-cell are anchored and never cited. Both companies file evasion *under* loss of control ("Loss of control, including evasion of oversight …"; "the inability to reliably direct … including evading the controls"). R-control says "nothing in the text" decides it. These are descendants' readings, so they are weak evidence of SB 53's meaning, but they are evidence for the `loss-is-wider` candidate, and the record should cite them.
- **Proposed change 4, lineage per claim (`carries`).** The template finding (§2.1) strengthens the case for it. It also shows that a per-claim edge needs an intermediate node for a shared template of unknown authorship.

---

## 7. What held up

These I checked myself and found as stated:
- All 53 passages: quote inside the line range, page correct, one match except P-sb53-bp-bar (two, as the pass notes). The generated tables reproduce exactly.
- SB 53 contains neither "severe" nor "systemic". Its chapters don't define "person". Its two codes differ exactly as `answer.md` lists (foundation vs frontier model; limb (1)'s property; "if committed by a human"; "where" vs "if").
- RAISE S.8828's definitions match SB 53's B&P definitions except as stated. Its "frontier model" and "frontier developer" tests are SB 53's, so sharing `model_is_frontier` is sound. It has its own equity exclusion (§1423). It never names California or the TFAIA.
- xAI's 2026 FAIF contains none of "TFAIA", "50 people", "billion" or "catastrophic".
- The address-theory quotes are verbatim (`def-match.ud`, `def-scope.ud`).
- The FCF's report of the RSP's sense is consistent with RSP v3.4 (§2.3).
- The SB 53 frames' other slots are faithful to the text as far as I read them.

---

## 8. Smaller items

- `tools/__pycache__/check.cpython-311.pyc` is committed, in a public repo.
- `weight-and-defects.md` §2 says no row had a single SKOS target, but T-xai25-cr has `exactMatch`. It points to another source's term rather than ours, which may be the intended distinction; if so, say so.
- RAISE's 72 hours runs "from a determination" that an incident occurred; SB 53's 15 days run "of discovering" it. The consequences comparison gives the windows but not the different triggers.
- R-material's evidence for the `likelihood-floor` candidate is a different document's wording. Its `magnitude` candidate cites no passage. Acceptance test 1 asks for a supporting passage per candidate.
- `check.py`'s hyphen rejoin would turn RAISE's "machine-\nbased" (extraction L98–99, the bill's own lines 44–45) into "machinebased". The pass knows the hazard ("anchors avoid those"); it belongs in D-anchor-normalization as a live instance.
- The plan's G1b text suggested Q4 or Q20 for this pass. Q1 was used, presumably by the brief. The pass recommends Q4/Q20 for G4. The README might record why Q1 was chosen, since the ranking it produces can't speak to the actor vocabulary Joseph named as his priority.
- From memory, unverified: AI Act Art. 3(65) defines systemic risk by "high-impact capabilities" and effects "propagated at scale across the value chain", not by casualty bars. If so, `eu_systemic_risk` is the open fact that keeps both companies' rows open in every scenario, and it is the cheapest single read that would change the answer.

---

## 9. Feedback on the pass, and on this audit's limits

The pass is careful in the right places: anchors with match counts, ambiguity kept as an outcome, our leans recorded beside candidates, and a limits section that names its own conflict of interest. Writing an evaluator so that "this mattered" becomes testable was a good instinct. Most of §1 is an argument for keeping it while saying exactly what it tests. The most useful repairs, in the order I'd do them:
1. Report decisiveness at the row level, and label conditional decisiveness as such.
2. Either encode R-material and R-control as evaluable or drop "computed" from tier C.
3. Add the FCF↔FGF and FGF←PF lineage, and re-weigh R-fgf-severe with the reused PF prose.
4. Repair limb (4), "our" and the conduct-list relocation in the frames.
5. Reconcile tier A with D-q1-type.

**Limits of this audit.**
- I read the source extractions around the passages and searched each document. I did not read SB 53, the FCF or the FGF whole.
- I did not read the AI Act, the HSE's R2P2, or FCF v1.
- The n-gram comparison shows shared text, not who copied whom.
- I am the same model family as the author, so where we agree, that is coherence, not confirmation.

I'm staying on the line for questions from Joseph or the coordinator.
