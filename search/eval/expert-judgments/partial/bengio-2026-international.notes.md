# Notes on judging the IASR 2026 for the outline evaluation (stage 1, blind)

*By the IASR source expert's fork (Claude Sonnet 5.5), 2026-10-10. Written after the fragments, before any `source-search` run. Reference list (lines 3137–7704, "Notes") not read experientially; the footnote bodies were seen inline in the text.*

## How the document is organised

- Front matter and contributors (to ~L450), executive summary (L420–L490), introduction (L494–L560), then Chapter 1 (background and capabilities, to ~L980 including a technical supplement), Chapter 2 (risks, ~L990–L1760), Chapter 3 (risk management, ~L1880–L2720), conclusion, glossary (L2735–L3115), citation, then Notes.
- Every chapter section follows a tail pattern: Key information → body → Updates → Evidence gaps → (Mitigations) → Challenges for policymakers. The same claim is therefore often made three times: in the executive summary, in a section's Key information box, and in the body. They differ in strength (summaries and boxes tend to be stronger; see below), so for most queries the body passage is the one that must be read and the summary/box is "helps".

## Where the headings mislead, or the outline will likely go wrong

- **Line ranges are coarse.** A paragraph is one line and carries its footnote bodies inline, so a "line" can be several thousand characters. Tables are one line per row. A single sentence of interest (e.g. the marginal-risk "compound" sentence) cannot be pointed to below the line.
- **Non-breaking spaces** sit inside headings and prose at unpredictable places ("loss of control", "Figure 2.1"). A quote copied from a rendering with ordinary spaces will not match; I verified every quote against the file.
- **Sections without introductions:** §2.1 and §2.3 go straight from the heading to the first subsection; the definition of "systemic risks" is in a note under the chapter map (L541) and the glossary (L3077), not in §2.3.
- **Detached material:** figure and table text leaks into neighbouring units (e.g. Figure 2.12's transcript sits after the next heading); some tables' images are absent.
- **The glossary is under-used by the term.** Several terms the body uses constantly have no glossary entry ("deployer", "evaluation gap", "emerging risks", "catastrophic"); some have two or three wordings (loss of control, systemic risks, defence-in-depth, misalignment).

## Questions that don't fit this document well

- *hazard*: the Report uses the word in one glossary entry and a few phrases ("risk and hazard taxonomies", "hazard analysis", the OECD "Incidents and Hazards Monitor"); the earlier fork's judgments stand.
- *catastrophic risk*: the Report almost never says "catastrophic"; its words are "severe harm", "extinction", "mass harm", "large-scale harm". Only three prose uses, none defined.
- *serious incident*: used three times, never defined; the definitional help is the two (different) incident-reporting definitions.
- *what must a developer publish or report before deploying*: the Report is descriptive and states few duties; it says what developers do (model cards, frameworks, transparency reports) and what some instruments require in outline. An agent needs the instruments themselves for "must".
- *humans can no longer shut down or correct the AI system*: not the Report's wording ("regaining control", "adjusting or halting", "resist shutdown"); the judged stretches are by meaning.
- Line 9 was left out as instructed; I did not judge it.

## Questions the evaluation might add

- Terms the Report coins or re-uses in several senses: *evaluation gap*, *evidence dilemma*, *emerging risks*, *defence-in-depth*, *systemic risk* (three senses incl. the EU AI Act's), *loss of control* (two wordings), *'closed' models* (closed-source / closed-weight / first four levels of Table 3.9). I judged four of these as own questions (files 13–17).
- Actor-term questions ("who is a developer / deployer").
- Evidence-status questions: "which claims rest on developers' own reports?", "where does the Report say evidence is limited because of legal or information-hazard constraints?" — these cut across sections and are the ones I'd expect a lexical or semantic search to get wrong.
- Summary-vs-body questions: several digest sentences are stronger than their bodies (the maths-olympiad "leading systems", "studies show 96%…", the 77% denominator, "no effect on aggregate employment"). A good retrieval for any of those should surface the body line; I graded the body 2 and the summary 1 or 2 depending on whether the summary alone answers the question faithfully.

## Grading convention I used

Grade 2 = an agent answering faithfully must read it (definition, the Report's one statement, or the line that carries the answer's qualification). Grade 1 = context, the summary version of the same claim, a cross-reference, a list mention, or a neighbouring concept. Where a section is the answer (e.g. §2.2.2 for loss of control) I gave the sub-sections separate grades, rather than one grade for the chapter, because only some of it is needed.
