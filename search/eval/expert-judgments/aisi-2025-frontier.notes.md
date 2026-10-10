# Notes on source-search for aisi-2025-frontier

*The Trends Report expert, gold round 1 (a fork of expert-aisi-2025-frontier-sonnet; Claude Sonnet 5.5; 2026-10-10). Written after stage 2. Files beside this one: `aisi-2025-frontier.json` (stage 1, committed before any search was run), `aisi-2025-frontier.reorder.json` (stage 2), `aisi-2025-frontier.inputs/` (passages, my overrides, the notes in structured form, the build script).*

## What I did, and what could have anchored me

- **Stage 1** from my reading (123 units, a second pass over units 38-123, and a read of the earlier Opus expert's reflections on units 1-32, all before this task). 11 of the 12 queries (chemical and biological weapons uplift left out, as asked) and 10 of my own. I opened no search output first, and I did not open `outline-judgments/aisi-2025-frontier.json`. The canonical text's sha256 is the one I read (`0677c834…f652`).
- **Stage 2** on `main` at `e0e7025` (stage 1 was written on `75c955b`; `search/` and `bin/` are identical between them). Hybrid with `-n 20`, outline with `--lines 60`; also `lexical` and `exact-phrase` on the term queries as a check. I read digests built by a script from the saved JSON, not the JSON itself.
- Between the stages I read the pilot's `build_reorder.py`, `ideal.json` and the head of `california-2025-sb53.reorder.json` for the format. I did not open its `.notes.md` or `notes.json`.
- **The query set mixes two kinds.** Seven of the 11 are terms or term-like phrases (hazard, catastrophic risk, loss of control, shut down, misalignment, whistleblower, serious incident) and for this report three of those are absent words. The rest are questions. The tools behave differently on the two kinds, so I report them apart.

## In short

1. **On question-shaped queries the outline put an agent on what I marked must-read more often than a 20-result list did, 47 of 49 (96%) against 42 (86%) on my own ten, and 28 of 35 against 23 on the brief's.** Over all 21 queries, must-read: outline 75 of 84, hybrid 65 of 84; helpful: outline 44 of 58, hybrid 35 of 58. Both numbers are generous (a passage counts as reached if any opened range overlaps it).
2. **Both tools fail in the same place: a fact in a section whose heading doesn't name its topic.** The cyber task-length doubling sits in "02 Agents" under a software-engineering heading; the report's own limits sit in an appendix; the account of AISI's access and working relationship with developers sits in the safeguards section. Cyber capabilities was the worst query for both (hybrid 6 of 15 must-read, outline 8 of 15).
3. **For a term, the concordance is the right tool, and neither hybrid nor outline is.** `lexical hazard` returned the two literal uses and said there were no others; `lexical whistleblower`, `serious incident`, `misalignment` and `catastrophic risk` each returned "no results" with exit status 1. Those are the answers an agent needs. Hybrid returned 20 results for each regardless, with the contributors list at rank 1 for "whistleblower".
4. **The outline's own "does anything answer this" banner is right on absent words and wrong on inflected ones.** It correctly said nothing answers "whistleblower" and "serious incident", and said plainly for "misalignment" that no passage holds any query word. It also said nothing answers "catastrophic risk" and "hazard", both of which the report uses (as "catastrophic ... risks" in one passage and as "hazardous"/"hazards").
5. **The outline can't tell an agent that two passages say different things.** This report defines "open-source" three ways and "sandbagging" three ways. Search and outline each put the definitions in front of the agent, correctly, and nothing says they differ.

## The numbers

Against my stage-1 grades, by passage (a passage is graded by the highest grade of any stretch of mine that overlaps it). "List" is hybrid's top 20; the outline's opened ranges ran about 180-270 source lines per query. Hybrid's 20 passages never reached that many lines, so equal-room and top-20 coincide.

| | must-read (grade 2) | helpful (grade 1) |
|---|---|---|
| the brief's 11 queries, items | 35 | 27 |
| &nbsp;&nbsp;hybrid top 20 reached | 23 | 14 |
| &nbsp;&nbsp;outline opened | 28 | 18 |
| my 10 own queries, items | 49 | 31 |
| &nbsp;&nbsp;hybrid top 20 reached | 42 | 21 |
| &nbsp;&nbsp;outline opened | 47 | 26 |

Two queries have no items by design (whistleblower, serious incident); one has helpful items only (developer duties). The per-query rows are in the reorder file. About two thirds of hybrid's 420 slots (285) held passages I neither graded nor listed as acceptable; the same sixteen passages made up most of them (below).

## Hybrid

- **Rank 1 is usually right.** The first result was a must-read passage in 12 of the 17 queries that have any, and in two more (hazard; emotional dependence) a passage I graded helpful. The exceptions are where my wording differed from the document's: "humans can no longer shut down or correct the AI system" (the first seven results match on "ai", "can", "systems", "humans"; the must-read passages are at ranks 9 and 20), "AISI's mandate, access to models, and relationship with developers" (ranks 4, 8, 18; two passages absent; the top three match on "access", "developers", "models" and are about open-model gaps), "misalignment" (rank 1 a safeguards passage; the report's equivalent at rank 2) and the severity query (rank 1 the domain list, "societal risks").
- **It cannot see that a passage belongs to the topic of its section.** For "loss of control" the three must-read passages it missed carry the section's findings and none of the words: "would need to complete several actions in sequence while remaining undetected", the detection results, and "no unprompted sandbagging detected". An expert reading says "Section 5 is the answer". A passage ranker can only say "these sentences contain the words".
- **Hub passages.** Sixteen passages fill most of the non-graded slots across unrelated queries: L474-478 (the loss-of-control opening) appears in the top 20 of 13 of 21 queries, L514-518 (sandbagging definition) in 12, L436-440 and L702-720 in 10-11, and so on. They are risk-vocabulary neighbours, and some are relevant to a query's gist, but an agent spends its slots on the same dozen passages whatever it asked.
- **The displayed quote is not always the passage.** For "gap between open-weight and closed models" rank 1 is L692-700, whose quote is the title of footnote 32. The passage is two footnotes followed by the paragraph that holds the lag and its two estimates. A reader of the list alone would take it for a bibliography line. Likewise rank 2 for the severity query is L314-320, whose first paragraph is a figure caption; the sentence that answers is the second paragraph and is what the quote shows (this one works).
- **Stemming gives confident false hits.** "serious incident" returns "This possibility is taken seriously by many experts" at rank 1 (matches: 'seriously'), with the same score as a real hit.
- **No absence signal.** For terms the document doesn't use, hybrid still returns 20 results; the only hint is that most list no matched words. A line saying "no result holds 'whistleblower'" would be enough.

## Outline

- **What it does well.** It shows the shape of an answer. For "loss of control" it opened all nine must-read passages as one run through Section 5; for persuasion, the whole of 6.1; for jailbreak effort, section 4 as the subsections it is. The census (`[7 passages · 4 top · 3 near]`) tells an agent where the weight is.
- **Would an agent reading it know what it hadn't read?** Mostly yes, in one respect and not in another. It says how many passages in a section it did not show (`+1 of its own not shown`, `+1 section not shown (1 near)`), and an agent who sees "+29 of its own not shown" under the Glossary knows there are twenty-nine entries it has not seen. What it cannot say is what they are. For the cyber query, the Agents section carries `+1 section not shown (1 near)`; by its line range the unshown subsection is the one (L194-212) that holds the cyber task-length doubling, a must-read for the question, and the line gives no hint of that. And where it says `(no hits)` it can be wrong in sense: for "evidence that models can sabotage, sandbag or evade oversight", Section 5 reads `+1 section not shown (no hits)`; the unshown subsection is 5.1 Self-replication, which is where the report's capability evidence for the "evade" half sits. An agent told "no hits" would not go there.
- **It spends source lines on things that cannot answer.** Whistleblower: the first range it opened was the contributors list (L23-52, thirty lines of names run together), because it was nearest by meaning; the same for "hazard". The table of contents (L116-129) was opened for "loss of control". For "cyber" about twenty-two source lines went to four chemistry and biology passages.
- **The banner.** See point 4 above. It was most useful for "misalignment" and for the two absent terms; it would have misled an agent on "catastrophic risk", where the answer (L474-478) was the first range it opened.
- **Structure inherited from the canonical headings.** The Appendix, References and Glossary appear as subsections of "Conclusion: looking ahead" (L724-878, "38 passages"), because their headings are second-level beneath a first-level Conclusion. "Introduction" and its subsections ("Why we're releasing this report", "Our testing approach", "Reading this report") appear as siblings. Section numbers "03", "07" and "08" sit at the foot of the preceding section in the converted text, so those three sections appear without numbers while "05 — Loss of control risks" and "06 — Societal impacts" have them; the document's own cross-references ("Section 3 discusses...", "(Section 7)") therefore don't resolve in the outline.
- **Noise on every line.** `[page not confirmed against the PDF]` is on 329 of the 581 opened-range lines across these runs. It is probably right and carries no information the agent can use; once at the head of the output would do.

## What an agent asking about this source needs (my view, for the weight it has)

1. **A concordance first for anything term-shaped.** The answer to "does it say X" is a count, the occurrences, and the neighbouring forms; the report's own vocabulary ("evade human control", "reliably directed towards human goals", "barriers... eroding") differs from the field's, and an agent needs to be told which words the document uses. I'd make this the default view for a one- or two-word query.
2. **The qualifiers of a claim, together with the claim.** This report's strongest-sounding sentences carry their qualifiers in captions and the appendix (LLM judges, 11 of 20 tasks, SEM over tasks, "may underestimate the ceiling"). An agent asking "how fast are capabilities improving" gets the headline from the executive summary, which drops the qualifiers; both tools returned the headline, and the limiting paragraph ("should not be read as a forecast") was reached only by the outline. A per-source standing set (Limitations, Data presentation, Uncertainty, Reading this report) that every question about a claim also surfaces would do more for fidelity than ranking.
3. **Disagreement inside a source.** Where the document gives two definitions or two numbers (open-source, sandbagging, apprentice-level as "<1 year" and "1-3 years"; R and R² for the same 0.097), an agent should be shown both and told they differ. Neither tool can; an expert fork could say so once per source and the index could keep it.
4. **Where the answer is a section.** For "loss of control" and "persuasion" the right object is a section with its findings. The outline gets this right; hybrid cannot. The census idea is sound.
5. **What the document can't see.** "Not in this document" is an answer. Hybrid and outline gave no such signal for "what must a developer publish" (the report imposes no duties) or "shut down or correct" (the report's words differ). For the outline, a final line such as "none of these passages holds the words 'shut down' or 'correct'; the document's nearest wording is in L74 and L476" would turn a miss into a lead.

## About the judging itself

- **Passage grain and section grain.** I judged stretches, which the tool then turns into passages by overlap. A grade-2 section ("3.2 Cyber", "6.1") becomes ten or twenty grade-2 passages, some of which are not worth reading alone (the "Source:" line under a figure heading; a figure caption). I dropped two (listed in `overrides.json`). A "core / member" mark would let a judge say "the section is the answer; any one paragraph isn't".
- **"Opened" is generous.** A passage counts as reached when any opened range overlaps it. The outline's ranges are wider than passages, so a range that spans a heading and three paragraphs credits all of them. The scorer's "covered" figure is the stricter one.
- **Quotes.** The brief says "exact first words". In this canonical text many lines begin with markdown (`- `, `**`, `<sup>`) or a footnote number; I quoted the cleaned words and kept footnote numbers. The scorer matches on letters, so it worked, but the brief should say.
- **Two of my queries are not neutral.** "how the severity or acceptability of a risk is decided" has, for this report, one sentence that bears on it, inside a passage whose first paragraph is a figure caption in a chemistry and biology subsection; I graded the passage. I would not read a ranking score on that query as telling much.
- **My own queries** were chosen before any search; they reflect what I thought an agent would ask of this report. Four are specific to its structure (open-source vs open-weight; models noticing they're evaluated; mandate and access; execution authority in finance) and may favour the outline, because those sections are small and well-headed.
- **One reader.** I had read the earlier expert's notes and my own second pass before judging; some of my graded passages are ones I'd flagged then. The notes record the grading, not the reading's independence.

## What I'd change in this brief

- Say how quotes should treat markup and footnote numbers.
- Say whether stage-2 grades are per passage or per stretch. I followed the pilot's build script (per passage, by overlap), which is what the tool can be scored against; a judge reading only the brief would not know.
- The launch message's estimate of hybrid JSON cost (about 1k tokens a result) was high for this document: about 0.9k characters, roughly 250 tokens a result. The whole job took a small part of the room; I read none of the raw JSON, only digests.
- A line that fixes what "equal room" means when hybrid is capped at 20 results and the outline opens 200 source lines: here the two coincide, but the scorer's list@R would otherwise have read further than 20.
