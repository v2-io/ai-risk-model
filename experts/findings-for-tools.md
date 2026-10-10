# What the experts found about the tools and texts

*Faults in the canonical texts, the search index and the reading tool that source experts reported while reading, kept here so they reach `bin/canonicalize`, `bin/source-index` and `bin/reading` instead of staying in a conversation. Started 2026-10-09 by the coordinator, ai-risk-search-tool. Each entry names the expert, the source, what it found, and what has been done.*

## Canonical texts (`bin/canonicalize`)

- **Paragraphs split across page breaks.** SB 53 expert, `california-2025-sb53`: L148/L152 and L292/L296 are each one paragraph cut by a page marker, so each yields two half-passages. The expert's suggested fix: rejoin a line that ends without terminal punctuation to the line after the marker. The search chunker already joins such breaks when the next block starts in lower case (`search/DESIGN.md` §5.5); `bin/reading` does not. Not fixed.
- **A threshold that exact search can't find.** SB 53 expert, `ny-2026-raise-s8828`: RAISE's compute threshold is rendered "10º26" (an ordinal or degree sign), not "10^26". Not fixed.
- **Line numbers and hyphen breaks in a statute.** SB 53 expert, `ny-2026-raise-s8828`: New York's bill text carries its line numbers and line-end hyphenation into the canonical text ("fron- 18 tier"), which breaks phrase matching. Not fixed.

- **Article numbers lost in conversion.** EU Code expert, `eu-cop-2025-safety-security`: the LEGAL TEXT lines of Commitments 1 and 10 have lost their article numbers. Not fixed.
- **A cited text that isn't there.** EU Code expert: Appendix 1 names "Recital 110 AI Act" under ADDITIONAL LEGAL TEXT, but no recital text follows. Whether the PDF holds it is unchecked. Not fixed.

- **Footnotes moved away from their markers.** Risk Report expert, `anthropic-2026-risk-report-aug`: the conversion often puts a footnote's text far from its marker, which caused two of the expert's early misreadings. Its `reading/conversion.md` lists them. Not fixed.

## Ranking (`search/RANKING.md`)

- **A summary inside the source outranks the text it gets wrong.** SB 53 expert: the Legislative Counsel's Digest drops decisive qualifiers and misprints "internal use" as "internet use", yet is keyword-dense. Registered as H-R4, proposed.
- **A definition completed by a provision that never names it.** SB 53 expert: the catastrophic-risk definition needs §22757.16 (equity value isn't property loss), which doesn't contain "catastrophic risk", so lexical search misses it. Evidence for the Meaning group (H-M1) and for whole-document readers as the source of labels.

- **Interpretive rules sit after the operative text, or before it in a preamble.** Both experts, from their conversation (2026-10-09): SB 53's §22757.16 and its uncodified SEC. 5 (liberal construction, severability, preemption); the Code's glossary and recital (i). A reader or a search that stops at the operative clauses gets the strength of every provision wrong, and wrong in the same direction every time. For ranking, a passage that states how other provisions are to be read is relevant to queries about those provisions, though it shares none of their words. Not yet registered as a hypothesis.

- **IASR marks industry-authored references.** IASR 2026 expert: the web edition's citation tooltips prefix industry-authored references with "[industry]", so a grep over the canonical text can count industry-authored evidence per section. A possible feature, and evidence for the conflict-of-interest principle.

## The reading tool (`bin/reading`)

- **Figures were dropped.** EU Code expert: the tool showed only captions, so the expert took the figures to be lost. Fixed 2026-10-09 (`babdc38`): a figure shows as ⟦figure: path⟧ at the end of its unit.
- **A figure alone on a line goes with the next unit.** AISI Sonnet expert, `aisi-2025-frontier`: an image after a paragraph probably belongs to that paragraph, but `bin/reading` attaches it to the unit after, which can mislead. Moving it to the previous unit would renumber nothing (figures don't count towards `--min-words`), but it changes what a reader sees mid-reading, so it waits until the current readings are done. A hint in the output would do meanwhile. Not fixed.
- **Tables aren't cleaned.** IASR 2026 expert, `bengio-2026-international` (2026-10-09): inside table cells, `bin/reading` keeps link targets and citation tooltips in full, so a footnoted table such as Table 1.1 (unit 38) costs several times its prose. The cause is in `bin/reading` itself: it cleans paragraphs but passes table rows through as they are. Not fixed yet, on purpose. Cleaning tables changes their word counts and so, with `--min-words`, could move unit boundaries under the three experts reading now. The fix should clean what is shown while keeping the grouping on the raw text, or wait until those readings are done. Whether the search index's chunker cleans table cells needs checking separately.
- **A stale line in the help.** SB 53 expert: the help said the reflections were git-ignored. Fixed (`a62338f`).
