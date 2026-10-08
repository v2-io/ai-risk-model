# Response to `de-novo-feedback-1.md`

*For Joseph and the coordinator, from the thin pass's author, 2026-10-07. I checked each finding at the source, or by re-running the computation, before accepting it. The verifier's report is the better account of what the first version showed. Where they differ, this response and the repaired files follow the report except where noted under "What I contest".*

## The headline, first

**Withdrawn:** "most of SB 53's precise clauses carried no weight; the structure around them did". The coordinator relayed it to Joseph as the main finding, so the correction comes first.

It doesn't follow from the computation, for three reasons:
- **Q1 stipulates two facts.** Any clause that tests other facts could only come out "open".
- **The evaluator could only find decisive what I had encoded** as an ambiguity, and I had encoded only the magnitude, aggregation and umbrella side.
- **"Decisive" was measured below the row's result.** Re-run at the row, 13 of the 26 labels changed nothing.

**What the slice does support:**
- **This slice can't rank lexicon terms for refinement.**
- **For a two-fact hypothetical,** SB 53's precise clauses can be named but not weighed.
- **What the computation shows at the row** is narrow and stated in `weight-and-defects.md` §1. Four things change a row's result:
  - the FGF's "severe harm" sense;
  - pooling of casualties, in one variant;
  - what "a single incident" attaches to, in another variant;
  - closure, for the companies' own sentences.
- **To weigh SB 53's clauses,** a question has to supply the facts they test, such as a documented instance.

## What I accepted and changed

| § | Finding | Checked at | Change |
|---|---|---|---|
| 1.1 | Only encoded ambiguities can be decisive; tier C was "conditioning" by construction | `records/translation.yaml` (`ambiguous:` nodes); `resolutions.yaml` | §1 of `weight-and-defects.md` rewritten. `answer.py` now prints the recorded ambiguities it cannot evaluate (R-material, R-control, R-findings-cr) and the delegated ones. Resolution records say whether they are encoded. `terms-thin.yaml` says "by construction" |
| 1.2 | "Decisive" measured at the node, not the row | Re-ran with each candidate forced through the whole frame (`answer.py`, now built in) | Reproduced exactly: R-fgf-severe 5/5, R-pooling 4/9, R-single-incident-attachment 4/9, R-materialization-partial 0/3. Tables now report rows changed / clause only / reached. The materialization claims in `answer.md`, `weight-and-defects.md` and `terms-thin.yaml` are corrected |
| 1.3 | Closure wasn't computed; `answer.py` never read it | `grep closure tools/answer.py` gave 0 | Added a closure probe: each open class's unbound genus is marked, and the row is re-evaluated with the class read as closed. It changes the companies' own-sentence rows in all three variants and never the umbrella rows, as the verifier found. The own sentences are now rows |
| 1.4 | Tier A depends on keeping a feature of Q1 I called a defect | — | Tier A withdrawn as a tier. The relations and statuses are listed as needed *if* questions ask about incidents, which is decision 12 |
| 1.5 | The tables read as the sources' verdicts | — | Column is now "Result under our frame (unreviewed)", and `answer.md` says so up front |
| 2.1 | The FCF and FGF share a template that isn't in the EU Code | `tools/shared_runs.py` (added) on both extractions and on the EU Code: runs of 37, 31, 31, 25 and 23 tokens, plus the 10-token definition opening. Longest FCF–Code run is 12 tokens | New record L-fcf-fgf-template. L-fcf-derived and L-fgf-derived are marked `not_independent_of` it. New defect D-lineage-template. The root count (one) stands |
| 2.2 | The FGF reuses PF sentences containing "severe harm", and I misquoted the FGF's note | FGF L129–130 = PF L139–140; FGF L246–248 = PF L168–169; FGF L84–86 reads "different definitions of catastrophic risk". All four FGF uses of "severe" were checked | New passages and L-fgf-pf-reuse. R-fgf-severe's evidence rewritten, with a correction note and a lean at low-moderate confidence. New R-fgf-severe-reused. Quote fixed in `answer.md`. D-collide-scope reworded so OpenAI isn't credited with a statement it didn't make |
| 2.3 | RSP v3.4's footnote; "would not call … catastrophic" overreaches; umbrella tests asymmetric | RSP v3.4 L142–145 (effective 2026-07-08) | A-fcf-rsp-sense upgraded. R-fcf-rsp-catastrophic's outcome is now "deliberately unbound", not "no". R-fcf-umbrella gets the exhaustive candidate R-fgf-umbrella-closure has, encoded the same way |
| 3.1 | Limb (4) drops "in a manner that demonstrates materially increased catastrophic risk"; the Labor Code's limb (4) is unanchored | SB 53 L220–222, L634–636 | Frames repaired; P-sb53-lab-csi4 added. New term `thin:risk-increase-evidenced`, a second occurrence–risk relation. D-materialization and proposed change 1 cover both relations |
| 3.2 | "our" lost from the FGF frame | FGF L121–127; FCF L115–116 | Both frames test `model_is_publishers_own`. (The FCF's "our models" is in §2.1, L115, not its scope sentence at L87; the point stands) |
| 3.3 | The conduct list moved into the category tables rather than dropping out | FGF L142–144, L200–210; FCF L146–148 | Category slots added with R-fcf-categories and R-fgf-categories (restrictive or illustrative). Drift now reports "words and test differ" rather than "dropped". New defect D-frame-boundary |
| 3.4 | The property-only candidate still required the conduct list | `F-sb53-bp-cr` as committed | The conduct test moved inside each attachment candidate, so property-only frees the casualty arm. The v-several-incidents result was re-run: 4 rows, as before |
| 3.5 | xAI's footnote doesn't quote the exclusions | xAI FAIF L32–44 | `answer.md` corrected. P-xai25-fn-conducts added; the script now checks (A)–(C) too (exact) |
| 4 | Incident labels in the FCF's and FGF's §2.6 | FCF L442–489; FGF L491–522 | D-q1-type, D-conferred-events, `answer.md` short answer 1 and `terms-thin.yaml` corrected. The ladders are recorded as out of coverage, not translated |
| 5 | Overstatements: unconditional critical-safety-incident claim; "two limbs"; "two orders of magnitude"; "only one with consequences"; xAI "superseded" | Each against the records | Each corrected in `answer.md`, `debrief.md`, `terms-thin.yaml`. xAI's 2026 FAIF footnote 1 confirmed (EU Code terminology, L41–42). Both xAI end dates are now "undetermined", and the in-force table prints that |
| 6 | Row vs frame is Joseph's lexicon-shape decision; D-bound-vs-match overstated; D-anchor-tables overgeneralized; R-control's evidence orphaned | Plan §3.3 wording; FGF L200–210 | D-row-vs-frame now poses the choice, as proposed change 2. D-bound-vs-match narrowed (the plan's "what it was meant to" does take the dangle reading). D-anchor-tables narrowed, and the loss-of-control cell anchored whole. R-control cites P-fcf-loc and P-fgf-loc-cell |
| 8 | Smaller items | — | `.pyc` untracked, with `.gitignore` added. SKOS note clarified. RAISE's different trigger stated. R-material gets a passage per candidate, with the magnitude candidate flagged as having none. "machine-based" recorded as a live normalization instance. The README says why Q1 was used. AI Act Art. 3(65) read and anchored (P-act-3-65); the EU member is now a frame |

## What I contest, or accept only in part

- **§2.2, revisit the lean on R-fgf-severe.** Revisited, and kept at lower confidence. The definition sentence is the FGF's defining act, and it states its own example (">50 fatalities") inside "severe harm". On the PF reading that sentence contradicts itself, while the reused sentences may simply carry inherited wording. The reuse is real evidence the other way, which the first version hadn't read. The more interesting outcome may be both: the FGF using one phrase in two senses within one document. R-fgf-severe-reused records that possibility without choosing.
- **§8, the AI Act as "the cheapest single read that would change the answer".** I read Art. 3(65). It has no casualty bar, as the verifier recalled, and its conditions (high-impact capabilities, Union-market impact, propagation) are none of them stated by Q1. So reading it changes *why* the umbrella rows stay open, not *whether* they do.
- **§1.3, "a judgment about the sentences … not a computation".** That was true of the first version. With the own sentences as rows and the closure probe, the sentence-level contrast is now computed. It remains true that no *umbrella* row shows it, because of the EU member.

- **§3.3, "omits murder".** Accepted at first, then corrected while writing `notation/`. The FCF's class is "serious crimes (such as assault, extortion, or theft)", which is open, so murder is missing from the examples, not excluded from the class. Its list is *wider* than SB 53's closed four, not narrower. The thin-pass files now say so.

## What remains open

- A different-family translator on the same slice, diffing frames slot by slot. That is still the real check on every reading here, the computed weights included.
- A weight-finding pass on a documented instance, so that SB 53's precise clauses can be weighed, with R-material and R-control encoded.
- The direction of the FCF/FGF template; FCF v1 (not in relata under the key tried).
- The EU Code's systemic-risk tests, and xAI's 2026 "systemic risk", neither of them translated.
- The FCF's and FGF's incident ladders.

## A pattern worth naming

Most of the first version's errors had one shape. A plausible structural reading was written down, and then the computation was read as confirming it, when the computation could only return what the encoding allowed.
- The tier labels were the clearest case: "computed" was attached to results that could not have come out otherwise.
- The misquote of the FGF's note was the same move at the level of evidence. A passage that fitted the reading was cited for it without re-reading what it is about.

The repair's guard against both is mechanical. The evaluator now prints what it cannot evaluate, and every weight is reported where it could have come out the other way.
