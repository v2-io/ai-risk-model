# EU Code of Practice (Safety & Security): what the expert found judging `source-search`

*By the EU Code expert's fork, 2026-10-10. Stage 1 (`eu-cop-2025-safety-security.json`) was written and committed before any search was run, and before I opened any other judge's file or the SB 53 pilot's notes. Stage 2 is in `eu-cop-2025-safety-security.reorder.json`; its inputs (my ideal orderings and per-query notes, and the build script) are in `eu-cop-2025-safety-security.inputs/`. Canonical text sha256 `d2968247…370f`, the same text I read. Repo at `e0e7025`. Commands:*
- *`bin/source-search hybrid -n 20 QUERY eu-cop-2025-safety-security`*
- *`bin/source-search outline QUERY eu-cop-2025-safety-security --lines 60`*

*I judged 18 queries: the 12 in `outline-queries.txt` and 6 of my own, chosen where I expected a search to go wrong. As asked, the chemical-and-biological query carries anchors and grades only.*

## In short

- **Hybrid does well when the question uses the Code's own words.** That covers "serious incident" (15 of the top 17 graded), "whistleblower", how acceptability is decided, external evaluation, and similarly safe or safer models.
- **Hybrid fails when the question uses a word the Code doesn't, or one the Code uses in several senses.**
  - "catastrophic risk" returned none of Appendix 1.4's four specified systemic risks. The Code's word is "systemic".
  - "internal use" put "internal market", "internal validity", "internal audit" and "internal registry" ahead of the definition of 'use' (rank 19). The go/no-go rule that covers use was missing.
  - "external" pulled in "external validity".
  - "the Code" in a question pulled in the Objectives, the passage that names the Code, at rank 1 for two of my questions.
- **The Code spreads one topic across a Measure, a Glossary entry and an Appendix, and the tools find the most lexical piece.**
  - Loss of control continues in Appendix 4.4 (sandboxes against "(self-)exfiltration or sabotage carried out by models"). Neither tool returned it for either loss-of-control query.
  - "Against whom must weights be protected" is answered by two Glossary definitions: 'non-state external threats', quantified, and 'insider threats', which include AI models and senior management. Neither tool returned either.
  - Appendix 3.1's evaluation-rigour requirement is three words; its substance is in the Glossary.
- **The outline opens many ranges, and most hold nothing I graded.** Per query: 25–32 ranges and 114–240 source lines, of which 14–26 ranges are noise. It rarely misses a must-read passage. But an agent gets breadth, not a short path.
- **Its "Nothing in scope seems to answer this" header fired wrongly for "what does the Code say about chain-of-thought".** The Code addresses chain-of-thought in eight places, and the outline did open them, but its snippets showed other sentences. An agent trusting the header would skip the passages that answer the question. (It also fired for the chemical-and-biological query; no notes on that one, by request.)

## Would an agent reading the outline know what it hadn't read?

**Partly.**
- **What works:**
  - The counts ("+54 sections not shown (no hits)", "+8 of its own not shown") say that something was folded.
  - The "no passage holds any of the query's words, so every hit is by meaning alone" line for "hazard" is exactly what an agent needs, and I'd keep it everywhere it applies.
- **What it can't do:** tell the agent *which* sections were folded. For this source that matters, because the Code's headings are informative ("Appendix 4.4 Insider threats", "Appendix 1.3.2 Model propensities"). A one-line list of the folded headings, at the bottom or per branch, would let an agent see that Appendix 4.4 exists before concluding it has everything on loss of control. The counts tell it that it hasn't read everything; the headings would tell it what it hasn't read.
- **Snippets** («…») often aren't the sentence that matters. In list-shaped passages (Appendix 1.3.1's fourteen capabilities, M5.1's examples, M3.5's methods) the snippet shows one item, often not the one that matched. For loss of control, the capabilities passage showed "(14) capabilities to control physical systems", when the relevant items are (5)–(11). Showing the sentence or item holding the query's words, when one exists, would help most.
- **The false "unanswered" header** is the one thing I'd call harmful. A wrong "nothing here" licenses skipping, which is worse than saying nothing. On the evidence of this run, the all-words test is too strict for question-form queries: the question's own words ("what does the Code say about") can never all occur. The 0.5 distance threshold sits near where real answers fall for this source (0.56 here).

## Patterns a ranking model could use

1. **A term map per source.** The query's concept often has a source-specific name:
   - catastrophic risk → systemic risk;
   - developer → Signatory (or provider);
   - deploying → placing on the market;
   - internal use → 'use' (by the Signatory);
   - hazard → systemic risk source.

   The Code's Glossary and its LEGAL TEXT quotations make most of these recoverable. This is the project's own method, mapping each source's words into ours, applied at query time.
2. **Defined terms should travel with the passages that use them.** Several of the Code's ordinary-looking words are defined to mean more:
   - 'appropriate' includes going beyond the state of the art;
   - 'including' marks a minimum;
   - 'use' includes internal use;
   - 'insider threats' covers models.

   When a returned passage uses a Glossary term, or the query matches one, the definition is often the most important result. The tools returned definitions mainly when the query word matched the term itself.
3. **Follow "pursuant to" cross-references.** The Code is densely cross-referenced ("as specified in Measure 3.5", "pursuant to Appendix 3.5"). For most questions, the answer is a Measure plus the Appendix or Glossary entry it points to. Expanding one hop along those references would recover most of what hybrid missed here: Appendix 4.4 from M6.1 via 'insider threats', the threat-actor definitions from M6.1, and the go/no-go rule.
4. **Drop query words that name the document in scope.** "Code" in "what does the Code say about…" matched the Code naming itself.
5. **Word sense.** "internal" and "external" each have several senses in this source: internal market / validity / audit / use; external validity / assurance / evaluators. An embedding should separate them; the lexical part didn't.

## Passage segmentation

- **Recital (g) and recital (h) share passage #8.** So the SME and SMC recital sits under the Precautionary Principle.
- **Long lists are single passages.** Appendix 1.3.1's fourteen capabilities (CBRN, cyber, autonomy, self-replication, AI R&D…) are one passage with one vector, and so are 1.3.2's ten propensities. A query about any one of them gets the whole list or nothing. Splitting by item would help both ranking and snippets.
- **M3.5's example list is cut mid-list.** #30 ends at item (5); #31 runs from (6) to (11) and also takes in the first line of the evaluator-access paragraph.
- **Some Glossary rows merge into one opened range.** L658–665 covers 'independent external', 'insider threats' and 'internal validity'.

## On the format, and what got in the way

- **The two-stage design worked.** Writing stage 1 blind and committing it first made the comparison honest: I could see where my grade was coarse, not just where the tool was wrong.
- **Mapping stage 1 to the tool's passages loses some precision.** Stage 1 judges stretches of lines; stage 2 ranks passages. The two don't align when a judged stretch covers a heading with no text, or when a passage covers several judged items. Two adjustments, recorded in `meta.how`:
  - I dropped #125 (an empty "ADDITIONAL LEGAL TEXT: Recital 110" heading my stretch had swept in);
  - I lowered #123 (Art. 3(64)) to grade 1.
- **The brief's two grades can't say "this is an example, not an obligation".** For this source that's often what an agent most needs to know. The non-retaliation indicator in M8.3 is an example indicator of a healthy risk culture, not a duty. I put it in the notes; a field for it would let the scorer use it.
- **Room.** The whole job took far less than the 360k I had. The full hybrid and outline outputs (about 1MB) stayed in scratch files, and I read digests and four outlines whole.

## What an agent asking about this source actually needs

Joseph asked for views beyond the format. From the reading:
- **The Code's own term for the concept,** and a note when the query's word never occurs in it.
- **The definitions that change the meaning** of what was returned (the Glossary comes after the operative text and quietly strengthens it).
- **Each statement's force:**
  - commitment;
  - "will";
  - "should" (rare in the operative text);
  - "may";
  - "examples of… are";
  - "examples of indicators";
  - a presumption of fulfilment.

  A search hit stripped of its heading loses this. Under "Examples of safety mitigations are", nothing is required by name.
- **The places the text sends you,** one hop along "pursuant to".

## After writing the above: against Grok's judgments and the SB 53 pilot

*Added after both files above were committed, so what follows can't have shaped them.*

**Against Grok's whole-document judgments** (`outline-judgments/eu-cop-2025-safety-security.json`, 2026-10-09):
- **We agree on nearly every grade-2 stretch:**
  - the loss-of-control definition, and its sources;
  - recital (d) and M8.3 for whistleblowers;
  - recital (j) and Commitment 9;
  - C7, M1.4, M7.7 and M10.2;
  - the CBRN and cyber specified risks;
  - 'deception' and Appendix 3.2;
  - C4 and M3.4.
- **The main disagreement is about questions whose word the Code never uses.** Grok left "hazard" and "catastrophic risk" empty. I graded the Code's nearest concepts: 'systemic risk source' at grade 1; Art. 3(65), Appendix 1.2.1 and Appendix 1.4 at grade 2. The disagreement is about policy, not about the text. The evaluation should decide which reading "catastrophic risk" asked for. My view: an agent asking it of this source needs to be told the Code's word is "systemic", so an empty answer would mislead it.
- **Grok caught one thing I missed:** M7.6's rule that a deliberate change made available on the market needs its Model Report update and full assessment first (L481, grade 2 for "what must… before deploying"). That's a real pre-deployment duty, for model updates.
- **Grok also graded the content of M1.1** (what the Framework must contain) at 2 for that question. I graded only its deadline.
- **Where I graded more:**
  - for loss of control: Appendix 4.4, 'insider threats', the exfiltration definition, M9.3(2) and M5.1(8);
  - for serious incidents: the Glossary precedence clause.

  Grok graded Appendix 4.4 only under the sabotage/sandbag question.
- **The grades for grade-1 context differ a lot**, as expected.

**Against the SB 53 pilot's notes.** These are the patterns we both found, from different documents. One caution: the pilot's finding 1 cites "the EU Code expert" for the after-the-operative-text pattern. That came from my conversation with the SB 53 expert, so on that point we aren't independent. The others were found separately:
- **A question naming its own document pulls in that name.** "SB 53" pulled in its digest heading; "the Code" pulled in the Objectives.
- **Single-word false friends.** For SB 53: "internal" matched "internal process", "independent" matched "independent reasons". Here: "internal" matched internal market, validity and audit; "external" matched external validity.
- **The answerability flag wrongly said "unanswered"** for the chemical-and-biological query in both documents. In mine it also did so for the chain-of-thought question. The all-words rule is the common cause.
- **Snippets or anchors point at the wrong sentence in a long passage.** In both documents, list-shaped passages showed an item other than the one that matched.
- **Passages cross the source's own boundaries.** In both, lists are merged into one passage or cut mid-list. Splitting on the source's item markers would help both.
- **The outline opens a large share of the document.** For SB 53, 55% of lines over 18 queries. Here, 114–240 of 990 lines per query, with most ranges holding nothing graded.

One finding of the pilot I can add a case to: qualifiers placed away from what they modify. Here they're Glossary definitions placed after the operative text. They change what M6.1 ('insider threats'), the Commitments' use of "appropriate", and every "including" list mean.
