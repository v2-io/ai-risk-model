# Notes — anthropic-2026-risk-report-aug, expert gold (stage 1 blind, stage 2 shown)

*By a fork of expert-anthropic-2026-risk-report-aug (Claude Opus 5.5), 2026-10-10. The expert read the report whole, in order, in 249 units of at least 500 words with a reflection after each (branch `expert/anthropic-2026-risk-report-aug`). Canonical sha256 `33cea4de…26d4`, the same text the expert read.*

## Stage 1 (written before any search output was seen)

**Queries.** The eleven outline queries, without "chemical and biological weapons uplift" (left out at the coordinator's request), plus five of my own, picked where I expect a search to go wrong: "marginal versus absolute risk", "AI R&D automation threshold", "model weight security against state actors", "chain-of-thought monitorability", "ASL-3".

**How the document answers these queries, as I expect a searcher to meet it:**

- **Several queries are vocabulary this source doesn't use.** "hazard" appears once, as "infohazard". "whistleblower" and "serious incident" never appear, so whistleblower is empty and serious incident is answered by the report's incident sections, which are titled "Incidents related to our classifiers and access controls", "Safety process failures", and "List of minor incidents". "loss of control" appears once, in automated R&D ("humanity losing control over civilization entirely"). The report's own loss-of-control scenarios are misalignment pathways 5 and 6 (self-exfiltration; persistent rogue internal deployment), which never use those words. "shut down" appears twice, neither time as the concept asked about. A lexical search will mostly find the wrong things; a semantic one has to bridge from "can no longer shut down or correct" to "undermine our ability to detect (and thus mitigate)" (L1123).
- **The key definitions are not where the headings say.** "Catastrophic risk" is defined in footnote 1 (L238), printed in the middle of §1.1's list, between "We address both:" and item (a). Marginal and absolute risk are defined in that list (L242–243). "Absolute risk" gets a second, different definition in §4.6.2 (L2692: "relative to a world without powerful AI models"). "Misalignment" is defined twice: §2.2's looser wording, then §2.5's formal one.
- **Cyber has no section.** It's scattered across about a dozen places: the Mythos Preview release in §5.3.1 (the only direct statement of cyber capability), the UK AISI incident at the end of Claim 2, the rating rationale in §2.1/§2.19, two contrasts inside the CB sections, distillation, data retention, §6.1, pathway 8, and the weapons-development interviews. No heading contains "cyber". An agent following the outline by headings would find none of it.
- **Footnotes are displaced** by the conversion: footnotes 6–9 of the CB-2 threshold print inside §1.3.3; footnote 28 prints as body text of §2.15; footnote 41 prints inside §3.5. A passage-level search may attribute footnote content to the wrong section.
- **Tables use `<br>` between every word** (Tables 1.2.A–C, 2.1.A, 3.1.A, 4.1.A, 4.5.A, 6.6.A), so phrase search over table cells (e.g. "Project Glasswing", which appears mostly in tables) may fail unless the indexer joins them.
- **The executive summary is three tables** that restate each section's rating. They'll rank high for nearly every query, but only once (Table 1.2.A) do they add anything an agent couldn't get better from the section itself.

**Grade conventions.** Grade 2 = an agent can't answer without it. Grade 1 = qualification, cross-reference, or evidence. For broad queries ("misalignment"; "evidence that models can sabotage…") I graded the load-bearing sections, not every paragraph of a 70-page chapter.

## Stage 2 (after running the searches; written before reading the pilot's notes or the whole-document judge's file)

Repo `52984a6` (main `e0e7025` plus the stage-1 commit; no code changes). Commands as in the pilot. Full output kept in the job's scratch directory; `.reorder.json` holds the passage-level orderings, and `.inputs/` holds the build script, ideal orderings and per-query notes.

**Where both tools do well (top 20 holds most of what should be read):** "misalignment" (§2.5's definitions at ranks 1–6), "AI R&D automation threshold", "model weight security against state actors", "chain-of-thought monitorability", "ASL-3", "marginal versus absolute risk", and the definitional core of "catastrophic risk" (footnote 1 in passage #19, rank 2). These are queries whose words the report itself uses, in passages near headings that say so.

**Where both fail, and why (my reading of the pattern):**

1. **When the source answers in other words, both tools miss the answer.** "loss of control": 1 of 11 ideal passages in hybrid's top 20. "humans can no longer shut down or correct": 1 of 13. The report's version is pathways 5–6, Claim 5.3 ("rogue internal deployment", "self-exfiltration") and Claim 7 ("undermine our ability to detect (and thus mitigate)"). The one literal use, "losing control over civilization" (#276), is missed for "loss of control", while the shutdown query ranks it 3rd. The semantic side isn't bridging paraphrase at this document's scale. This is the shortfall that most matters for this source.
2. **For evidence questions, the argument outranks the evidence.** For "evidence that models can sabotage, sandbag or evade oversight", 2 of 22 ideal passages appear. Ranks are taken by passages *about* the evidence: claims, limitations, conclusions. The concrete incidents and figures are missed: domain fronting and the self-deleting hook, agents killing agents, Hacker-Opus killing monitors and hiding its hacking, the partial refusals spreading by notebook, the stealth-rate figures. The report states claims in the vocabulary of the query; the evidence uses its own words.
3. **Compound words defeat the lexical side.** For "cyber capabilities of frontier models", the passages say "cybersecurity", "cyberoffense", "cyber-offense", "cyberdefenses", and hybrid matched none of them. It found the one passage near "offensive cyber capability" (rank 2) and filled the rest with noise; rank 1 is §1.4 on unreleased models. The UK AISI cyber-evaluation incident (#106), the second must-read, is absent from both tools. Splitting compounds when tokenizing ("cyber" + "security") or indexing prefixes would likely fix much of this. That fix is my inference; I haven't tested it.
4. **Absence is half-signalled.** The outline says so when no passage holds any query word ("hazard", "whistleblower"), which is exactly right, but `likely_unanswered` never fires (nearest distances 0.47–0.49 against a 0.5 threshold). It then opens 20+ noise ranges anyway. For "serious incident", 42 passages hold one of the words, so no warning appears, though the phrase is absent. For "ASL-3", only 4 passages hold the term; that count is in the JSON but not in the text. Telling the reader "the exact phrase occurs in N passages" would let an agent know what it hasn't read and what isn't there.
5. **The question's framing and the document's structure don't meet.** "what must a developer publish or report…" misses §1.3.3–1.3.5 (coverage date, redaction disclosure, review), which are the report's publication rules. Its headings say "Changes to our RSP", not "publication". "how the severity or acceptability of a risk is decided" misses §5.4, the risk–benefit determination, whose heading has neither word.

**The outline's question, "would an agent reading it know what it hadn't read?":** partly. The section annotations ("+9 sections not shown (3 near)", "+15 of its own not shown") do tell a reader which parts hold unread near hits. That's the outline's best feature here, and it would have pointed a careful agent toward §3 for "loss of control" and toward §2.25 and §5.2 for the sabotage query. But it can't say what isn't there in other words: no heading says "cyber", and nothing tells the reader the report has no cyber threat model.

**Format notes.** The passage grain fits this document poorly in a few places:
- One sentence-paragraph at L901 is split into two passages (#140, #141).
- One paragraph is split by a page break, so its second half starts "to use a specific external-memory-based strategy…" (#142, L905).
- Footnotes print far from their markers: footnote 1 is inside #19 with §1.1's list; footnotes 6–9 of the CB-2 table are inside #37, under §1.3.3.
- Tables are split into rows, so a cell's claim and its column header ("Misalignment in high-stakes settings") land in different passages.
So "should rank N" is sometimes a choice between two halves of one thought, and a passage's heading path can be wrong about its footnote content. Two passages in the cyber ordering (#44, #23: the summary-table rows that give "incident disclosures related to model behavior in cybersecurity evaluations" as the reason for the rating) weren't judged in stage 1; they're marked `added_in_stage2`.

## After comparison (written after reading the whole-document judge's file and the SB 53 pilot's notes)

**Against the whole-document judge** (`outline-judgments/…json`, same sha256). Its stretches cover nearly all of mine: 9/10, 7/7, 7/8, 12/12, 8/8, 7/7, 11/12 and 12/14 of my stretches on the shared queries. The exception is cyber, at 7/13: I included more of the passages that use cyber compound words. The judge is broader, mostly at grade 1. Where it found things I'd now accept:
- agents killing agents (L667–671) and Pathway 5 (L1166–1174, its grade 2) for the shutdown and loss-of-control questions;
- §5.4 for "catastrophic risk";
- Claim 3.4.2, evaluation awareness, at grade 2 for the sabotage-evidence query;
- the link in §5.3.1 (L2985) to a public disclosure of an AI-espionage incident, for cyber, which I missed.

It didn't grade §2.25's Hacker-Opus results or §5.2.2's partial refusals for the sabotage-evidence query; I graded both 2. Our grade-2 cores agree; the disagreements are about how much grade-1 context to include.

**Against the SB 53 pilot.** Found independently in both documents, so these count twice:
- compound words defeat "cyber";
- paraphrase with no shared words defeats the shutdown/loss-of-control queries;
- the answerability signal is useful but incomplete;
- passages split or merge the source's own units.

Mine only, from this document:
- for evidence queries, the argument outranks the evidence;
- the absence warning counts words, not phrases ("serious incident", "ASL-3");
- `likely_unanswered` never fired here, though the pilot saw it fire, sometimes wrongly, on SB 53. A fixed 0.5 cosine threshold behaves differently on a 3,253-line report and a 313-line statute;
- the outline's "+N sections not shown (k near)" annotations are, for a long document, its best answer to "what haven't I read";
- answers can sit under headings that don't name the topic (publication rules under "Changes to our RSP").

The pilot's distance problem (qualifiers placed away from what they modify) has a counterpart here in displaced footnotes. I didn't check where anchors point within passages, as the pilot did; that remains open for this document.

**Scored by `outline-check`** (budget 60, my stage-1 file alone, copied to a scratch directory). The checker reads every `*.json` in `expert-judgments/`, and the `.reorder.json` files have no top-level `key`, so it fails on that directory as it stands. All 126 stretches resolve by line and by quote (2 fuzzily), with identical scores:

| | reached | covered | must |
|---|---|---|---|
| outline, opened | 0.646 | 0.450 | 0.523 |
| outline, flagged | 0.726 | — | — |
| ranked list, same room (list@R) | 0.656 | 0.441 | 0.505 |
| ranked list, same budget (list@B) | 0.552 | 0.321 | 0.390 |

The outline opened 2,269 source lines in all. As in the pilot, on this document the outline does about as well as a ranked list given the same room, not better.
