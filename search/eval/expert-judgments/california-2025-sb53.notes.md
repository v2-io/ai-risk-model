# SB 53: the expert's notes on its judgments and on what the search tools returned

*The SB 53 source expert (a fork of `expert-california-2025-sb53`), 2026-10-10. Canonical text sha256 `1b31896f…`, the same as the one read. Searches were run at repo sha `f1c93eb`. Stage 1 (`california-2025-sb53.json`) was written and committed (`1188a5c`) before any search output was seen. Stage 2 is `california-2025-sb53.reorder.json`. The other judges' files haven't been opened.*

## What I judged

The 12 outline queries, plus 6 of my own. The six are the retrieval test cases from my reading (`questions.md`), where I expected search to go wrong:
- the definition of catastrophic risk;
- whether developers must comply with their frameworks;
- who can be penalised;
- whether weight theft is an incident;
- whether third-party evaluation is required;
- internal use.

**A confound in my own queries:** five of the six name "SB 53". In single-document scope, that seems to pull the digest heading "SB 53, Wiener." (passage #3) to rank 1 for three of them. An agent would naturally write "SB 53" in such a question, so the confound is real for users too. One fix would be to drop a document's own name or code from the query when the scope is that document.

## The reorder file's shape

The brief suggested keying items by anchor. I keyed them instead by **the tool's own passages** (`src.passages` `ord`, with line range and first words). Both tools return passages, so "should rank N" is only well defined at passage grain. Each item's grade is the highest stage-1 grade of any judged stretch inside it. The `meta.passages` table maps passage numbers to line ranges, so a rebuild can be re-matched.

The outline has no ranks. Instead of `shown_rank`, each outline item has `opened` (whether any opened range overlaps it). Each outline entry also has `flagged_unanswered` and `source_lines_in_opened_ranges`. "Noise" excludes passages I list per query as relevant but ungraded; those lists are in the build script's input, under `ok` per query.

## The main findings, by mechanism

1. **Qualifiers placed away from what they modify are missed.** The equity exclusions (§22757.16, L215; Lab. §1107.2, L303) change the $1B element of both catastrophic-risk definitions. Neither contains the words "catastrophic risk". Hybrid missed both for "catastrophic risk" and for the definition question. The outline opened both for the bare term, but only L303 for the question form. "Property" (L126) was missed too. An agent reading the results gets an incomplete definition, and nothing tells it so. The EU Code expert reports the same pattern in its document: Glossary entries and recitals after the operative text quietly set strength. This looks general: a passage that modifies an element of a defined term needs a structural link to the definition. Neither lexical nor semantic matching will find it.
2. **The digest outranks the law.** Legislative Counsel's summary (L30–60) is dense with keywords and plain in language. It ranks above the operative text for "whistleblower" (ranks 1 and 3) and for my questions. That matters because the digest is wrong in ways the questions test: it omits "comply with" and the large-only limit on penalties, and has "internet use" for "internal use". It's a different author and isn't law. It should be tagged as summary or front matter and ranked below enacted text by default.
3. **Single words matching on their own make false friends.**
   - "loss" matched "loss of value of equity";
   - "control" matched "controlling, controlled by" (affiliate);
   - "evidence" matched the burden-of-proof clause;
   - "comply" matched the federal-equivalence "intends to comply";
   - "internal" matched the whistleblower "internal process";
   - "independent" matched "legitimate, independent reasons";
   - "evaluation" matched CalCompute's report contents.

   Weighting by proximity, or by phrase, for multi-word queries would remove most of the noise I marked.
4. **Compound words.** "cyber capabilities" found neither "cyberattack" nor "cybersecurity". The one place SB 53 treats cyber as a model capability, (B) at L100, came at rank 13, and its Labor Code twin was missed.
5. **Paraphrase with no shared words.** "humans can no longer shut down or correct the AI system" is the EU formula. SB 53 says "evading the control" and "loss of control". Hybrid put the right passages at ranks 11–16, or missed them, and rank 1 was OES revoking a regulation.
6. **Defining passages are recognised only for the bare term.** For "catastrophic risk" the definitions were flagged `defines` and came top. For "what is SB 53's definition of catastrophic risk" they fell to ranks 5–6, under the Department of Technology's "management of catastrophic risk".
7. **The anchor within a passage can point at the wrong sentence.** For "loss of control", #19 was anchored on the "$1B … loss of property" sentence, not on (C) "Evading the control". #55 was anchored on weight theft, not on item (3). #30 was repeatedly anchored on item (6), not item (10). An agent that reads the anchor and not the passage reads the wrong line.
8. **Passages cross the statute's own boundaries.**
   - #33 mixes the end of the transparency-report list with the separate duty to send internal-use summaries to OES (L160).
   - #29 and #30 split framework item (5) mid-line.
   - #12 and #14 each hold four or five findings.
   - #36 holds the 15-day duty, the 24-hour duty, amendment, the encouragement clause and OES review.

   For statutes, splitting on subdivision markers would make passages that mean one thing.
9. **Chrome and boilerplate get through:** L14 (site navigation), L20 ("SHARE THIS"), L26–28 (approval line), L56–60 (vote line). These are front matter with no content, and should be excluded from ranking.

## The outline specifically

- **For a 313-line statute at `--lines 60`, it opens about half the document.** It opened 156–192 source lines per query, 3,084 over 18 queries, which is 55% of the lines in total. `outline-check` scores it 0.939 against my grades, but so does a ranked list given the same room (list@R). At this length the outline's coverage says little. What would help an agent is *which part* of a 39-line range like L127–165 matters. The quote shown on each range (its best passage) does that partly, and well when the anchor is right.
- **Would an agent know what it hadn't read?** Partly, yes.
  - The skeleton, with section counts and "+N of its own not shown", tells it the shape of what's folded.
  - The answerability line is the outline's most useful feature here. It was right for "hazard", and fair for "misalignment" and the shutdown paraphrase, since both terms are absent.
  - It was **wrong for one query** (08): it flagged "likely unanswered" although passages #19 and #53 answer it, and hybrid ranked them 1–2. Its rule needs all query words in one passage, and a query word was absent from the document.
  - It was missing where it matters most: it didn't flag "evidence that models can sabotage…", which a statute can't answer, because topic overlap passed the semantic test.
  - Nothing marks the structural dependency in finding 1: an agent can't tell that §22757.16 modifies a definition it has opened.
- **Both of SB 53's parallel definitions are reached by both tools**, and the path shows the chapter, so an agent can tell the TFAIA version from the Labor Code version. That's good. But nothing says they differ: Labor Code versions use "foundation model", and add property loss to weight theft.

## About this brief and format

- The two stages worked. Writing blind first made the reorder easy and honest, because each disagreement was already a written judgment.
- The anchor-based keying suggested for stage 2 doesn't fit how the tools rank (passages), so I changed it, as said above.
- Running the commands for 18 queries cost much less than feared once the full output went to files (in the job's tmp, not committed) and I read compact digests. Hybrid's JSON is about 1k tokens per result, so 20 results is about 20k tokens a query if read raw. An agent using the tool by default gets that JSON, because stdout isn't a terminal. That cost is itself a finding about the tool's agent-facing form.
- Line ranges straddling a page marker (the transparency report's (2), L148/L152) are fine for the checker.
