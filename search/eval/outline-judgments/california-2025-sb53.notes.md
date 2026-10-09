# california-2025-sb53: judge's notes

Claude Opus 5.5, 2026-10-09. I read `ref/canonical/california-2025-sb53.md` (sha256 `1b31896f…`) whole and in order, and wrote the judgments before running any search tool. Afterwards I ran `search/eval/outline-check` on my file alone, to confirm every item resolves (all do), and looked at `bin/source-outline` for two queries, to make the heading notes below accurate.

## How the document is organised

It is the enrolled bill as shown on leginfo, 313 lines:

- L30–60: Legislative Counsel's Digest, a plain summary of everything that follows.
- L64–84: SEC. 1, the findings (a)–(p). Finding (j) (L78) is the only place the bill names its risk areas in prose: "hacking, biological attacks, and loss of control".
- L85–215: SEC. 2, B&P Code Chapter 25.1, the Transparency in Frontier AI Act. It contains:
  - 22757.11, definitions (L91–126);
  - 22757.12, the frontier AI framework, the transparency report, internal-use summaries, false statements and redactions (L127–165);
  - 22757.13, OES incident reporting (L166–198);
  - 22757.14, the annual review of the definitions (L199–212);
  - 22757.15, penalties (L213–214);
  - 22757.16, the equity exclusion (L215).
- L219–250: SEC. 3, CalCompute. Not relevant to any of the twelve questions.
- L251–303: SEC. 4, Labor Code Chapter 5.1, the whistleblower provisions. It contains its own definitions in 1107 (L255–273), the operative section 1107.1 (L277–302), and 1107.2 (L303).
- L304–312: SEC. 5 (severability, liberal construction, preemption) and SEC. 6 (Public Records Act findings).

## Where the structure misleads

- **The two copies of the definitions are not identical.** Labor Code 1107 repeats "catastrophic risk" and "critical safety incident" with "foundation model" in place of "frontier model". That widens the whistleblower chapter beyond the 10^26 threshold. Its CSI (1) also adds "damage to, or loss of, property" (L267, against L107). An index or reader that treats the second copy as a duplicate loses both differences. So I graded the Labor Code copies 1 rather than leaving them out.
- **The catastrophic-risk definition is only complete with two later provisions.** "Property" is defined at L126. The equity exclusion sits on its own at L215 (22757.16), after the penalties, and again at L303 (1107.2). Neither sits next to the definition.
- **22757.14 is mostly about updating the definitions, but its (d) (L210–212) is the Attorney General's annual report on whistleblower reports.** Someone following the headings would look for that in Chapter 5.1.
- **22757.13(h)–(j) (L187–198)** lets a developer be deemed compliant through a designated federal incident-reporting regime. It sits inside the OES section with nothing to signal it.
- **The section headings in the outline carry no titles.** "SEC. 2/3/4" are bare numbers; only the chapter headings beneath SEC. 2 and SEC. 4 carry titles. "CHAPTER 138" (L24) is the statute's chaptering number, so the whole bill hangs under it.

## Questions that are vocabulary gaps for this document

- **"hazard", "misalignment"**: neither word appears. I pointed at the nearest provisions at grade 1. For misalignment I gave CSI (4) grade 2: deceptive subversion of controls "outside of the context of an evaluation designed to elicit this behavior". The grades in this section are my reading, not the bill's words.
- **"humans can no longer shut down or correct the AI system"**: SB 53 never mentions shutdown or correction. Its formulations are:
  - "Evading the control of its frontier developer or user" (prong (C));
  - "no meaningful human oversight, intervention, or supervision" (prong (B));
  - "subvert the controls or monitoring" (CSI (4));
  - "circumventing oversight mechanisms" (22757.12(a)(10)).
  
  "Loss of control" is used (L78, L109) but never defined.
- **"serious incident"**: the bill's term is "critical safety incident". "Serious injury" (L98) and "serious physical injury" (L177) are lexical traps.
- **"evidence that models can sabotage, sandbag or evade oversight"**: a statute presents no evidence. Its relevance is that it makes such behaviour reportable, and it excludes behaviour elicited by evaluations. Both grades are 1.
- **"how the severity or acceptability of a risk is decided"**: "severity of the violation" (L213) concerns penalty size, not risk. I left it out. The real answer has two halves:
  - severity is fixed by the statute's thresholds (L98–105);
  - acceptability is delegated to each developer's own framework (L127–137).
- **"cyber capabilities"**: 22757.12(a)(7) (L134) is about the developer's cybersecurity, not the model's cyber capability. I graded it 1 so that the two stay distinguishable.

## On the scoring

- `resolve()` credits a lines-item when **any** passage overlapping its range is read. So a wide grade-2 stretch is credited by its least relevant passage. For example, reading L271 ("Foundation model" has the meaning defined in…) would credit my whole 1107-definitions item. For this reason I split "whistleblower" into 1107 and 1107.1, and kept the other items tight. Other judges' whole-chapter items will be more lenient than they look.
- In this document, passage 19 is the whole catastrophic-risk definition (L98–105), passage 12 holds findings (f)–(j), and passage 14 holds (m)–(p). So items at prong or finding level can't be told apart from their neighbours.
- The totals pool the five Au5 documents under one shared budget. A file from one judge therefore can't show how the outline does on that judge's document. A per-document mode (`keys=[key]`) would let each judge see that.

## Questions the evaluation might also ask

For this document and its neighbours:

- **"internal use / internal deployment"**: a thread running through SB 53, at L36, L131, L137, L160, L170–172, L183 and L312.
- **"who is covered" (thresholds)**: 10^26 operations, $500M revenue, the definitions review.
- **"third-party evaluation"**.
- **"redaction and confidentiality"**.
- **"preemption"**.
- **"penalties and enforcement"**.

## One thing I noticed in the outline, beyond the brief

For the shutdown query, scoped to SB 53 alone at 120 lines, the outline opened the approval line (L26–28), the vote line (L56–60) and the CalCompute section line (L219) alongside the relevant definition. When a short document has no strong match, the budget fills with whatever ranks next.
