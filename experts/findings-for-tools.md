# What the experts found about the tools and texts

*Faults in the canonical texts, the search index and the reading tool that source experts reported while reading, kept here so they reach `bin/canonicalize`, `bin/source-index` and `bin/reading` instead of staying in a conversation. Started 2026-10-09 by the coordinator, ai-risk-search-tool. Each entry names the expert, the source, what it found, and what has been done.*

## Canonical texts (`bin/canonicalize`)

- **Paragraphs split across page breaks.** SB 53 expert, `california-2025-sb53`: L148/L152 and L292/L296 are each one paragraph cut by a page marker, so each yields two half-passages. The expert's suggested fix: rejoin a line that ends without terminal punctuation to the line after the marker. The search chunker already joins such breaks when the next block starts in lower case (`search/DESIGN.md` §5.5); `bin/reading` does not. Not fixed.
- **A threshold that exact search can't find.** SB 53 expert, `ny-2026-raise-s8828`: RAISE's compute threshold is rendered "10º26" (an ordinal or degree sign), not "10^26". Not fixed.
- **Line numbers and hyphen breaks in a statute.** SB 53 expert, `ny-2026-raise-s8828`: New York's bill text carries its line numbers and line-end hyphenation into the canonical text ("fron- 18 tier"), which breaks phrase matching. Not fixed.

- **Article numbers lost in conversion.** EU Code expert, `eu-cop-2025-safety-security`: the LEGAL TEXT lines of Commitments 1 and 10 have lost their article numbers. Not fixed.
- **A cited text that isn't there.** EU Code expert: Appendix 1 names "Recital 110 AI Act" under ADDITIONAL LEGAL TEXT, but no recital text follows. Whether the PDF holds it is unchecked. Not fixed.

- **Footnotes moved away from their markers.** Risk Report expert, `anthropic-2026-risk-report-aug`: the conversion often puts a footnote's text far from its marker, which caused two of the expert's early misreadings. Its `reading/conversion.md` lists them. Not fixed.

- ~~**Pages with no text.**~~ AISI Sonnet expert, `aisi-2025-frontier`: it first reported PDF pages 50–51 as empty, then checked the PDF and withdrew it. Nothing was lost; the page labels were off.

- **Superscripts flattened into wrong numbers.** IASR Sonnet expert, `bengio-2026-international`: exponents lost their superscript, so "10^13 tokens" reads as "1013 tokens", and some citation markers vanish ("(MMLU, )"). A reader or a search takes the wrong number at face value; the same kind of fault as RAISE's "10º26". Not fixed.
- **Image figures and tables missing from a web edition, partly.** IASR Sonnet expert: figures and tables that are images (Fig 1.2) aren't in the text, and IASR web edition's image files aren't local. Corrected by its own fork: some image tables' text *is* in the canonical file, in restored `pdf-text` blocks (44 in IASR) displaced from their captions and flattened. Table 1.4's lists are at L709–711, under the next heading. So the fault is the displacement, not the absence. Not fixed.
- **Citation link text stripped in reading.** IASR Sonnet fork: "(MMLU, )" isn't a conversion fault. The canonical file has the citations, but `bin/reading`, like the search index, drops citation link text from prose. That's right for ranking, but it leaves holes a reader notices. Not fixed.
- **Inline footnote bodies.** IASR Sonnet expert: footnote text set inline swells some units to 6–9k tokens. Not fixed.
- **Smaller faults in IASR's web edition.** IASR Sonnet expert: a duplicate table of contents without titles, detached asterisks, and a dangling link for the Panel's membership. Not fixed.

## Ranking (`search/RANKING.md`)

- **A summary inside the source outranks the text it gets wrong.** SB 53 expert: the Legislative Counsel's Digest drops decisive qualifiers and misprints "internal use" as "internet use", yet is keyword-dense. Registered as H-R4, proposed. A second instance (AISI Sonnet expert): the *Frontier AI Trends Report*'s executive summary drops qualifiers the body gives ("doubling every eight months" is an "estimated upper bound"; "5% to 60%" self-replication is 11 of 20 tasks, closed models, "simplified") and omits a null result on persuasion. A third, IASR Sonnet expert: IASR's summary *strengthens* qualified or single-study body claims ("leading systems" at the IMO; "studies show 96%"; "77% of vulnerabilities", which in the body are those introduced by the organisers; "no effect on aggregate employment").
- **A definition completed by a provision that never names it.** SB 53 expert: the catastrophic-risk definition needs §22757.16 (equity value isn't property loss), which doesn't contain "catastrophic risk", so lexical search misses it. Evidence for the Meaning group (H-M1) and for whole-document readers as the source of labels.

- **Interpretive rules sit after the operative text, or before it in a preamble.** Both experts, from their conversation (2026-10-09): SB 53's §22757.16 and its uncodified SEC. 5 (liberal construction, severability, preemption); the Code's glossary and recital (i). A reader or a search that stops at the operative clauses gets the strength of every provision wrong, and wrong in the same direction every time. For ranking, a passage that states how other provisions are to be read is relevant to queries about those provisions, though it shares none of their words. Not yet registered as a hypothesis.

- **IASR marks industry-authored references.** IASR 2026 expert: the web edition's citation tooltips prefix industry-authored references with "[industry]", so a grep over the canonical text can count industry-authored evidence per section. A possible feature, and evidence for the conflict-of-interest principle.

- **Measured in the gold pilot** (SB 53 expert's fork, 2026-10-10; `search/eval/expert-judgments/california-2025-sb53.notes.md` has the evidence and passage numbers). Of the patterns above, two showed up in the rankings themselves:
  - The digest outranks the law: Legislative Counsel's digest took ranks 1 and 3 for "whistleblower" (H-R4). The expert's proposal is to tag it as front matter and rank it below enacted text.
  - Qualifiers set apart from a definition are missed: `hybrid` missed both equity exclusions (§22757.16 L215, Lab. §1107.2 L303) for "catastrophic risk" and for the definition question. The outline opened both for the bare term only. The expert reads this as needing a structural link from a modifying provision to the definition, not better matching.

  New with the pilot:
  - **Single words match on their own** in multi-word queries: "loss" → "loss of value of equity", "control" → the affiliate definition, "evidence" → the burden of proof. Related to H-Q1 and H-W4.
  - **Compound words:** "cyber" finds neither "cyberattack" nor "cybersecurity", since the four-letter run-on cap and the stems both stop short (H-Q7). SB 53's one cyber-capability clause came 13th.
  - **Definition-first works only for the bare term:** for "what is SB 53's definition of catastrophic risk" the definitions fell to ranks 5–6. `rank.DEF_INTENT` doesn't strip "SB 53's" (H-Q2).
  - **A query naming the scope's own document** ("SB 53") pulls the digest heading to rank 1. The expert's idea: drop a document's own name or code from the query when the scope is that document.
  - **Site chrome and the vote line rank** (L14, L20, L26–28, L56–60): H-R3, still unbuilt.
- **The answerability cue** (`rank.answerability`; the outline's "nothing in scope seems to answer this"), from the same pilot. It was the outline's most useful line, right for "hazard", "misalignment" and the shutdown paraphrase. It was also wrong both ways:
  - a false alarm on query 08, which passages #19 and #53 answer: its rule needs every query word in one passage, and one word isn't in SB 53;
  - silent for "evidence that models can sabotage…", which a statute can't answer, because topic overlap passed the semantic test.

## The reading tool (`bin/reading`)

- **Figures were dropped.** EU Code expert: the tool showed only captions, so the expert took the figures to be lost. Fixed 2026-10-09 (`babdc38`): a figure shows as ⟦figure: path⟧ at the end of its unit.
- **A figure alone on a line goes with the next unit.** AISI Sonnet expert, `aisi-2025-frontier`: an image after a paragraph probably belongs to that paragraph, but `bin/reading` attaches it to the unit after, which can mislead. Moving it to the previous unit would renumber nothing (figures don't count towards `--min-words`), but it changes what a reader sees mid-reading, so it waits until the current readings are done. A hint in the output would do meanwhile. Not fixed.
- **Tables aren't cleaned.** IASR 2026 expert, `bengio-2026-international` (2026-10-09): inside table cells, `bin/reading` keeps link targets and citation tooltips in full, so a footnoted table such as Table 1.1 (unit 38) costs several times its prose. The cause is in `bin/reading` itself: it cleans paragraphs but passes table rows through as they are. Not fixed yet, on purpose. Cleaning tables changes their word counts and so, with `--min-words`, could move unit boundaries under the three experts reading now. The fix should clean what is shown while keeping the grouping on the raw text, or wait until those readings are done. Whether the search index's chunker cleans table cells needs checking separately.
- **A stale line in the help.** SB 53 expert: the help said the reflections were git-ignored. Fixed (`a62338f`).

## The index and the output (`search/srcsearch/chunk.py`, `bin/source-search`)

- **Passages cross a statute's subdivisions.** SB 53 expert's fork, gold pilot: #33 joins the end of the transparency report's list to the separate duty to send OES internal-use summaries (L160); #29 and #30 split framework item (5) mid-line; #36 holds five duties. The proposal is to split statutes on subdivision markers, so each passage means one thing. Not fixed.
- **The anchor quotes the wrong sentence of its passage.** Same pilot, e.g. #19 for "loss of control" is anchored on the "$1B … loss of property" sentence instead of (C) "Evading the control". Seen first-hand by the coordinator (ai-risk-model-61) the same day: the paraphrase query's top results quote their passage's first sentence. An agent that reads only the anchor reads the wrong line. Not fixed.
- **JSON is expensive and is the default for agents.** Same pilot: about 1k tokens a result, so `-n 20` costs about 20k tokens a query. JSON is chosen whenever stdout isn't a terminal, which is how every agent runs the tool. Not fixed.
- **A flag before the verb turns the verb into the query.** The coordinator, 2026-10-10: `source-search --text semantic 'QUERY' Au5` searches for "semantic" and reports that the real query "matches no document" (exit 3). Not fixed.
- **The "matches" line breaks the tool's own matching rules.** The coordinator, 2026-10-10: it lists "incorrect" for "correct" and "systematically" for "system", against the left boundary and the four-letter cap in `help`. Where the list comes from isn't traced. Not fixed.

## The evaluation tools (`search/eval/`)

- **`outline-check --agree` counts a query one judge never saw as judged empty.** The coordinator, 2026-10-10: comparing the SB 53 expert (18 queries) with the Claude judge (12), its six own queries were counted as disagreements, giving a marked-or-not kappa of 0.74. On the 12 shared queries it's 0.83 (Gemini 0.75 against the expert; Claude–Gemini 0.77). The judgment format keeps "judged empty" (a key with `[]`) apart from "not judged" (no key) for exactly this reason. Comparisons should keep to queries both judges have. Fixed 2026-10-10 (`802f6c7`): `--agree` compares only queries both judged and lists the rest. The same commit stops `outline-check` reading the experts' `.reorder.json` files as judgments, which crashed it (reported by the Risk Report expert's fork).
