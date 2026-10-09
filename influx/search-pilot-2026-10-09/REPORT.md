# Search pilot: embedders, ranking, chunking, anchors

*2026-10-09, by Claude (Opus 5.5). For the coordinating agent, Joseph, and whoever builds `bin/source-search` from `search/DESIGN.md`. All numbers come from 10 sources and 16 queries. Treat them as directions with error bars.*

*Saved by the coordinating agent: the harness wouldn't let the pilot agent write report files. The text is the pilot's, verbatim, except one bracketed correction in §2.*

## In short

- **The embedder matters less than DESIGN.md assumes; the structure around it matters more.**
  - The query set was graded blind (§1). Once lexical evidence and the definition prior are fused with semantic search, the reasonable embedders all land within about 0.02 nDCG@10 of each other. bge-m3, snowflake-arctic-embed2, qwen3-8B, bge-large and nomic score 0.77–0.79.
  - Every bootstrap interval between them spans zero.
  - What the pilot does resolve: fused ranking with priors beats semantic search alone by +0.107 nDCG@10 (95% interval +0.054 to +0.155). It wins 14 of 16 queries.
- **Embedder: bge-m3.** I'm moderately confident it is good enough, and not confident it is the best.
  - It loads at 963 MB.
  - It embeds 3,714 passages in 95 s on an idle machine.
  - Its 8,192-token window is real only if `num_batch` and `num_ctx` are raised. By default ollama truncates bge-m3 at 2,048 tokens without saying so.
  - snowflake-arctic-embed2 is an equal alternative. It runs at the same speed, loads at 1.5 GB, and has the best semantic-only score, though not significantly.
  - The 8B qwen3 bought nothing for 16× the time and 10 GB.
- **The definition prior is the strongest single lever.** It took lexical search alone from 0.540 to 0.697. One fix was needed: never boost a definition of a *broader* term. Before the fix, bare "risk" definitions were boosted for "catastrophic risk".
- **A cross-encoder doesn't need 18–21 GB.**
  - On CPU, bge-reranker-v2-m3 peaked at 2.7–2.9 GB and took about 2 s per query for 30 passages.
  - It helps paraphrase and rare-term queries, and hurts the definitions-first ordering that term queries want.
  - I'd make it opt-in (`--rerank`), not the default.
- **Some of DESIGN.md's specifics need changing** (§8): passage boundaries, heading indexing, `--all`'s word-form matching, and quote generation.
- **Some gaps are lexicon problems, not ranking problems.** "Developer" vs the AI Act's "provider" is the clearest case; the fix is query expansion through the context maps.

## 1. What was run

**Corpus:** 10 sources, cut into 3,714 passages of about 1,200 characters.
- `california-2025-sb53`
- `openai-2025-preparedness-framework-v2`
- `eu-cop-2025-safety-security`
- `nvidia-2025-frontier`
- `nist-2023-ai-rmf`
- `cabinetoffice-2026-nrr`
- `eu-2024-ai-act`
- `bengio-2026-international`
- `anthropic-2026-risk-report-aug`
- `bengio-2026-international-extended` (OCR'd, marked check-all)

**Embedders (9 via ollama):**
- bge-m3, snowflake-arctic-embed2, bge-large, nomic-embed-text-v2-moe, embeddinggemma:300m, mxbai-embed-large, granite-embedding:30m, qwen3-embedding:0.6b, qwen3-embedding (8B).
- Each was given the query and document prefixes its authors specify.
- A Hugging Face control was also run (§2).

**Ranking modes (`search.py`):**
- `sem`: cosine only.
- `lex+p`: BM25 on exact word forms, plus half-weight BM25 on Postgres's `english_stem`, plus a phrase bonus.
- `mix+p`: memorata's geometric mean of the two rank positions.
- `rrf+p`: reciprocal-rank fusion.
- `+p` adds priors: a definition boost of ×(1 + 2·match·confidence), and ×0.3 for tables of contents and references.
- `+d` adds per-document decay.

Ranking ran in memory with numpy. No database was created, and `memorata3` was not touched.

**Gold:**
1. **`gold-draft.json`.** My expectations, written from the sources before any ranking ran. It proved too thin. For example, it gives no credit to the AI Act "stop button" passage on the shut-down paraphrase query.
2. **A blind judged pool**, the TREC method.
   - It is the union of every configuration's top 10, shuffled and unlabelled.
   - A separate Claude instance graded all 711 passages 0–3. It never saw my expectations, the configurations or the rankings.
   - Its rules and findings are in `judging-notes.md`, which is worth reading on its own.
3. **`qrels-pilot.json`.** The same grades, re-keyed as anchors (key + PDF page + quote) so they survive re-chunking. 679 of 711 anchors pass `bin/check-quote` (§7).

The judge is the same model family as me. That beats me grading my own pool, but it isn't the cross-family review needed before tuning.

## 2. The embedder

Scores are nDCG@10 against the judged pool, using the v1 definition rule. Every configuration below was pooled, so its top 10 is fully judged.

| model | dims | loaded | s / 3,714 | sem | mix+p | rrf+p | sem term / nl |
|---|---|---|---|---|---|---|---|
| snowflake-arctic-embed2 | 1024 | 1.5 GB | 97–102 | **0.694** | 0.731 | 0.759 | 0.77 / 0.46 |
| bge-large | 1024 | 0.7 GB | 93 | 0.680 | 0.744 | 0.744 | 0.76 / 0.43 |
| bge-m3 | 1024 | 1.0 GB | 95¹ | 0.654 | 0.739 | **0.761** | 0.70 / 0.52 |
| embeddinggemma:300m | 768 | 0.7 GB | 78 | 0.652 | 0.733 | 0.752 | 0.64 / **0.70** |
| qwen3-embedding:0.6b | 1024 | 6.3 GB² | 153 | 0.635 | 0.733 | 0.742 | 0.68 / 0.52 |
| nomic-embed-text-v2-moe | 768 | 0.6 GB | 71 | 0.631 | 0.722 | 0.752 | 0.69 / 0.45 |
| mxbai-embed-large | 1024 | 0.7 GB | 102 | 0.625 | 0.725 | 0.708 | 0.69 / 0.43 |
| qwen3-embedding (8B) | 4096 | 10 GB | 1,543 | 0.572 | 0.693 | 0.743 | 0.57 / 0.59 |
| granite-embedding:30m | 384 | 0.07 GB | 41 | 0.472 | 0.641 | 0.691 | 0.52 / 0.34 |
| *lexical + priors only* | | | | 0.697 | | | 0.75 / 0.54 |

¹ The first bge-m3 run took 218 s. It ran while relata's 2,143-page OCR job was competing for the machine, before Joseph halted it at about 21:45. *[Coordinator's correction: the paper being converted, `sharma-2026-whos`, is 73 pages. The 2,143 in relata's progress display was a count of text bounding boxes (Joseph). I passed the wrong figure on to the pilot.]* The bge-m3 raw-input and 600-character runs fell in the same window. Re-timed on an idle machine it took 95 s, with identical vectors (minimum cosine 0.9999998). All other timings were taken after the halt.

² qwen3-0.6B's loaded size is mostly KV cache at an 8,192-token context.

With the v2 definition rule (§3), `rrf+p` becomes:

| model | rrf+p (v2) |
|---|---|
| bge-m3 | 0.786 |
| arctic2 | 0.778 |
| qwen3-8B | 0.778 |
| bge-large | 0.771 |
| nomic | 0.771 |
| embeddinggemma | 0.766 |
| qwen3-0.6B | 0.766 |
| mxbai | 0.738 |
| granite | 0.717 |
| lexical + priors only | 0.731 |

**Paired bootstrap over the 16 queries (`compare.py`):**

| comparison | Δ | 95% interval | wins / losses / ties |
|---|---|---|---|
| bge-m3 rrf+p − bge-m3 sem (v1) | +0.107 | +0.054, +0.155 | 14/2/0 |
| bge-m3 rrf+p − lexical+priors (v2) | +0.055 | −0.020, +0.146 | 8/2/6 |
| bge-m3 − arctic2, both rrf+p (v2) | +0.007 | −0.027, +0.043 | 6/7/3 |
| bge-m3 − qwen3-8B, both rrf+p (v2) | +0.008 | −0.067, +0.069 | 9/4/3 |
| arctic2 sem − bge-m3 sem | +0.040 | −0.015, +0.094 | 10/5/1 |
| v2 rule − v1 rule (bge-m3 rrf+p) | +0.024 | +0.001, +0.061 | 4/0/12 |

**What this shows.**
- Fused ranking with priors beats semantic search alone.
- Inside the fused ranking, the top embedders can't be told apart.
- The embedder adds about +0.05 over lexical search with priors, and even that interval spans zero.

**What it can't show.**
- Sixteen queries can't rank close embedders.
- My draft gold put bge-m3 first on semantic-only search. The judged pool puts arctic2 first and bge-m3 third. That reordering is itself the result.
- Settling it needs about 50 judged queries, ideally graded by another model family.

**Why bge-m3 anyway.**
- It ties for the best fused score.
- It is small and multilingual.
- It is fast. The coordinator's 0.9 s vs 4.1 s gap against arctic2 didn't reproduce on 1,200-character passages: 95 s vs 97 s.
- arctic2 is an equally good choice.
- The cache keyed by model makes swapping later cheap, and that matters more than this choice.

**Against qwen3.**
- The 8B took 1,543 s, against bge-m3's 95 s.
- Packaging was ruled out: Hugging Face Qwen3-Embedding-0.6B (via sentence-transformers) matched ollama's vectors (mean cosine 0.9994) and scored the same, 0.635.
- The instruction prefix carries the model:

| qwen3-0.6B query instruction | sem |
|---|---|
| none | 0.27 |
| generic web-search instruction | 0.61 |
| my domain instruction | 0.64 |

- I pulled `qwen3-embedding:0.6b` with your agreement. I'd remove it unless someone wants to rerun `hf_check.py`: `ollama rm qwen3-embedding:0.6b` frees 640 MB.

**On DESIGN.md §5.4's reasoning.**
- *"nomic's 512-token context would truncate most passages"* doesn't hold at the designed passage size.

  | passage size | median bge-m3 tokens | 90th percentile | passages over 512 tokens |
  |---|---|---|---|
  | ~1,200 chars | 199 | 350 | 5 of 3,714 |
  | ~2,000 chars | | | 249 of 2,863 |

  nomic does lag on quality, but not for that reason.
- *bge-m3 "covers any passage whole"* is true only with `num_batch` and `num_ctx` set; `embed.py` sets both.

**Chunk size and input (draft gold, bge-m3, sem).** These are consistent with DESIGN's choices and give no reason to change them.

| comparison | Δ | 95% interval |
|---|---|---|
| 1,200 vs 600 characters | +0.007 | −0.022, +0.032 |
| 2,000 vs 1,200 characters | −0.039 | −0.119, +0.017 |
| title-and-heading prefix vs raw text | +0.040 | −0.030, +0.109 |

## 3. What carries the ranking

- **The definition prior.** Lexical search went from 0.540 to 0.697 with it.
  - The v1 rule also boosted definitions of terms the query contains. The judge graded those boosted passages 0: bare "risk" definitions for "catastrophic risk", and "Hazard" for "information hazard".
  - The v2 rule:
    - exact term: full boost;
    - narrower term that contains the query: 0.25 of the boost;
    - broader term: no boost;
    - "definition of / what is / define X" is parsed to X.
  - v2 scores +0.024 (interval +0.001 to +0.061). It was shaped by the judged misses, so that number is optimistic.
  - A 0.5 narrower-term boost flooded "definition of risk" with the Code of Practice's twenty "systemic risk …" glossary rows.
- **Fusion.**
  - With priors, RRF beat the geometric mean by +0.036 (interval −0.008 to +0.090; 7 wins, 3 losses).
  - Without priors, the geometric mean lost even to semantic-only on the draft gold (0.608 vs 0.687).
  - My lean is `rrf+p` as the default with `mix` kept selectable. memorata's mix was Joseph's design, so that choice is his.
- **Lexical vs semantic.**
  - On term queries, lexical search with priors is as good as anything (0.79 under v2).
  - On natural-language queries, semantic retrieval is needed. The shut-down paraphrase scores 0.29 with the best fused ranking and 0.58 with the reranker.
  - embeddinggemma had the best semantic-only score on natural-language queries (0.70) but among the weakest on terms.
- **Diversification.**
  - The NRR fills "hazard"'s first page with industrial-sense mentions.
  - Per-document decay lowered judged nDCG (0.766 → 0.722), because the judge graded other-sense mentions 1: they are mentions Joseph wants caught.
  - This belongs in `--by source`, not in a default weight.
- **Hub passages.**
  - Short generic glossary entries appeared in up to 8 of the 16 pools and were mostly graded 0. Examples: IASR "Risk", "Risk factors", "Safety"; AI Act Art. 3(2).
  - The effect is stronger in qwen3-8B.
  - Worth watching at 25× the corpus size. A length prior is one option; I didn't test it.

## 4. The reranker (`rerank_test.py`; bge-reranker-v2-m3 on CPU, top 30)

- **Cost:** peak RSS 2.7–2.9 GB; 30–43 s for 16 queries, about 2 s per query. memorata's 18–21 GB figure was on Metal.
- **Scores.** The 13 passages it promoted from ranks 11–30 were judged in a third batch.

  | first stage | first stage | reranked | folded in as a factor |
  |---|---|---|---|
  | rrf+p (v2) | 0.786 | **0.813** | 0.792 |
  | sem | 0.654 | 0.764 (a floor) | 0.698 |

- **Where it helps:** the shut-down paraphrase (0.29 → 0.58), "information hazard" (0.58 → 0.92), and "severe harm".
- **Where it hurts:** "death or serious injury to more than 50 people…" (0.87 → 0.68), "whistleblower" and "developer". It demotes definitions because it knows nothing of the priors.
- Overall on the fused head: 8 wins, 6 losses, 2 ties.
- **It was the only thing that found the AI Act's Art. 3(3) "provider" for "developer".**
- **On DESIGN §6.4:** "the priors carry what a reranker would add" holds for term queries but not for paraphrase.
- **My lean:** off by default; offer `--rerank` on CPU; and when it is used, let it reorder only the results that aren't definitions.

## 5. Chunking and definitions (`chunk.py`, a sketch of DESIGN §5)

**What worked**
- **Statutory definitions.** All 68 AI Act Art. 3 definitions and all 18 of SB 53's were detected.
  - Art. 3(58), "'subject', for the purpose of real-world testing, means", was missed in the runs and fixed after them. It is a scoped definition.
- **IASR's glossary, which has no heading.** A run of five or more `**Term:**` paragraphs in alphabetical order found 179 of 179 entries, with no false glossaries.
  - Non-alphabetical runs, such as key-information boxes and contributor lists, became weak "bold-lead" definitions instead.
- **The Code's glossary table, which wraps across rows and pages.** All 36 entries were grouped once continuation rows (empty first cell) were attached.

**What DESIGN §5.2 needs**
- **One entry per passage must also cover numbered and bold-labelled items.**
  - The Code's "(2) Loss of control: Risks from humans losing the ability to reliably direct, modify, or shut down a model" was first packed with its three sibling risks.
  - Packed, it ranked 381st semantically for "loss of control". Standalone, it ranks in the top 3.
- **Index headings as a lexical field.** 6 of the NRR's 79 "hazard" forms and 5 of NVIDIA's 30 are in headings only.
- **Statute section numbers sit inside list items** (`- **22757.12.** (a) …`). Treat them as pseudo-headings.
- **The table-of-contents section kind should apply only to its own heading's blocks.** IASR nests Secretariat, Scope and Forewords under "Table of contents".
- **Restored ```` ```pdf-text ```` blocks (93 passages) inherit the wrong heading.**
  - The NRR's carry the risk-matrix legend ("140 Catastrophic 5 Significant 4 …"), which matches "catastrophic" lexically.
  - They want their own section kind and lower lexical weight.
- **Definitions still split across passages.**
  - Anthropic #63→#64, and #119→#120 split mid-sentence.
  - Code of Practice lead-ins are separated from their lists.
  - A passage holding a definition should run long rather than be cut.
- **Collapse duplicates within a document, not only across documents.**
  - One NRR sentence recurs on 20 pages.
  - IASR restates its definitions in the executive summary, the extended summary and the glossary.
  - Keep near-duplicates such as SB 53's frontier/foundation parallels visible as variants, because the differences between them are findings.

**Reach, against the judge's 55 grade-3 passages.**
- Before the prose patterns, the boost fired on 30 of them; 35 had some detected definition.
- Most misses are prose definitions:
  - "Loss of control scenarios are scenarios in which …"
  - "In this report, systemic risks are risks that …"
  - AI Act recital 13, "The notion of 'deployer' …"
  - NRR #36, "… are considered catastrophic"
- I added two high-precision patterns: "the notion of 'X'" and a repeated head noun ("X scenarios are scenarios in which"). Together they found 18.
- The judge counted that heading-based flags alone catch about a third. Joseph's "very high factor" needs pattern detection to reach the rest.
- **Counterpart terms in other sources** ("serious incident" ↔ "critical safety incident", "deployer" ↔ "deploy", "developer" ↔ "provider") deserve their own measure, as the judge suggests.
  - The only thing that bridged developer → provider was the reranker.
  - That is the job of the lexicon's context maps used as query expansion.

## 6. IASR tooltips, `--all`, OCR

- **IASR's web edition is 2.14 MB raw and 0.85 MB once indexed.** Link targets are 742 KB of it and tooltips 518 KB.
  - "hazard" counts 17 raw vs 14 cleaned (11 in the body, 3 in references).
  - NVIDIA's "developer" counts 26 raw vs 17 once the `developer.nvidia.com` URLs are dropped.
- **`--all` (`defs.py --all hazard`)**
  - Match word forms by substring. That catches "infohazard" (Anthropic) and "biohazards" (IASR), which DESIGN's form list misses.
  - Count headings, count references separately, and exclude link targets.
  - Pilot body counts: hazardous 42, hazards 37, hazard 33, biohazards 1, infohazard 1.
- **`--defs` (`defs.py --defs developer`)** groups definitions by source, with the evidence that matched. For developer it returns:
  - SB 53's four (§22757.11 (h) and (j), plus the §1107 cross-references);
  - IASR's "AI developer" and "Downstream AI developer".
- **OCR "Al" for "AI"** is now fixed upstream. It had cost the OCR'd source lexical matches and quote confirmation.

## 7. Anchors

Every printed result carries key, PDF page, printed page and an exact quote. After the 22:4x rebuild:
- **Final configuration, top 10 for all 16 queries:** 159 of 160 pass `bin/check-quote --batch` (137 exact). The one failure is ambiguous: SB 53's "'Frontier developer' has the meaning defined in Section 22757." occurs twice on p. 10.
- **All 711 judged anchors:** 679 pass.

Lessons for the builder:
- **Build quotes in check-quote's normalization.** Drop tags, `&lt;br&gt;`, table pipes and emphasis.
- **Find sentences with links masked, and never let a quote span a link.** The tooltip's letters are in the canonical text.
  - My first version took seven quotes from inside IASR tooltips. They were reference text, which check-quote then found on the endnote pages.
  - It also took 18 quotes that started inside URLs.
- **Widen quotes until unique.** An NRR boilerplate sentence recurs on 20 pages.
- **Take the page from the quoted sentence, not from the passage start.** 350 of 3,714 passages span pages, and 7 run backwards.
- **For check-all sources, cite the page `bin/check-quote` settles from the PDF, not the canonical marker.**
  - IASR's web edition gets per-line pages, so a paragraph straddling two pages carries one of them.
  - IASR after both fixes: 195 ok, 16 page-mismatches (15 off by one, 1 a stale pilot passage), 5 `[not in pdf]`.
  - Before (old canonical text, quotes taken from raw text): 169 ok, 23 mismatches (7 of them large, e.g. p. 161 vs 79 and p. 194 vs 106), 18 not found, 6 `[not in pdf]`.
  - The large jumps came from two causes:
    - the canonicalize link-pattern bug you fixed (nested parentheses);
    - my tooltip quotes.
- **`[not in pdf]` text (web-only tables) does appear in results**, so the display must flag it.
- **The embedded and judged passages were cut before the rebuilds.** `search.anchor()` re-chunks the current text and checks that the passages still line up before quoting. The anchors here and in `qrels-pilot.json` come from the rebuilt texts.

## 8. On DESIGN.md

- **§1:** The four-mode split holds. Ranked search can't answer "have we caught them all": NVIDIA's "hazardous knowledge" was never surfaced.
- **§5.2 / §5.3:** As §5 above.
- **§5.4:** bge-m3 is fine, with `num_batch` and `num_ctx` set, and each model's prompts. The 512-token argument against nomic doesn't hold at this passage size.
- **§6.1:** Weighting exact forms above stems behaved as intended.
- **§6.2:**
  - The definition prior should be exact &gt; narrower &gt; never broader, and should parse definition intent from the query.
  - My lean is RRF with priors as the default.
  - Diversity belongs in `--by source`.
- **§6.3:** Collapse duplicates within documents too.
- **§6.4:** An opt-in CPU reranker that leaves definitions in place.
- **§7:** Anchors as in §7 above.
- **§8:** Build the eval from pooled judgments from the start, add a counterpart-term measure, and reach about 50 queries before tuning.
- **§9:** The counterpart-term finding argues for doing the translated layer early.

## 9. What this pilot can't tell you

- Differences within about ±0.05 are noise with 16 queries.
- There was one judge, from the same model family, in one pass. Recall means recall within the pool.
- The v2 rule and prose patterns were fitted to the judged misses.
- The reranker's semantic-head score is a floor.
- Extrapolated to about 80,000 passages: about 35 minutes for bge-m3, and about 9 hours for qwen3-8B.

## 10. Housekeeping

- **Models.** One at a time; the largest was qwen3-8B at 10 GB. None are loaded now. The 70B chat models were not touched.
- **relata.** I ran `relata prep pause`, and later **`relata prep resume --background`**. I confirmed it was converting `stix-2025-behind`.
- **Before the rebuild:** I read all ten texts. The ones that changed were `bengio-2026-international`, its extended summary, and `nvidia-2025-frontier`.
- **Files in `influx/search-pilot-2026-10-09/`:**
  - `chunk.py`, `embed.py`, `search.py`, `eval.py`, `compare.py`, `table.py`, `defs.py`, `pool.py`, `rerank_test.py`, `hf_check.py`: pilot code, not the index.
  - `gold-draft.json`
  - `qrels-pilot.json`: holds about 700 short source quotes. Trim it if that's too much for a public repo.
  - `judging-notes.md`
  - `results/`: the eval rows and embedding timings.
- **Scratch only, not in the repo:** vectors, passage caches, and the judging pools (which hold source text). To rerun, set `PILOT_SCRATCH`; `PILOT_DEF_RULE=v2` selects the revised definition rule.

---

**On the brief:** nothing in it was wrong. Two of its figures didn't hold up, and both matter for the decision:
- **Timing:** the bge-m3 vs arctic2 gap (0.9 s vs 4.1 s) doesn't reproduce at 1,200-character passages; they run at the same speed.
- **Truncation:** DESIGN's argument that nomic would truncate most passages assumed 2,100-character passages.
