# Source search: design

*A proposal for a local semantic and lexical index over the corpus, drafted 2026-10-09 by Claude (Opus 5.5) at Joseph's request. Steps 1–3 of the build order (§11) are built; §11 says what each found and what is not built yet. The decisions for Joseph are collected in §10, each with a lean and a confidence. It draws on memorata (`~/src/memorata/memorata3/`, read whole: `schema.sql`, `search.py`, the embedder and the CLI) and on `bin/canonicalize`'s output contract (read whole).*

## 0. What the pilot changed (2026-10-09)

A pilot on 10 sources and 16 queries, graded by a blind judge, tested this design: `influx/search-pilot-2026-10-09/REPORT.md`. Its numbers are directions with error bars (16 queries; one judge, same model family). What it changes here:
- **Structure matters more than the embedder.** Fused lexical and semantic ranking with the definition prior beats semantic search alone by +0.107 nDCG@10 (95% interval +0.054 to +0.155; 14 of 16 queries). Inside the fused ranking, bge-m3, snowflake-arctic-embed2, qwen3-8B, bge-large and nomic are indistinguishable (0.77–0.79).
- **The embedder stays bge-m3**, as good enough, not as best. It needs `num_ctx` and `num_batch` raised: by default ollama truncates it at 2,048 tokens without saying so. Two of §5.4's arguments didn't hold and are corrected there.
- **The definition prior is the strongest lever,** with one rule change: boost a definition of the exact queried term fully, a narrower term containing it at a quarter, a broader term never; and parse "definition of / what is X" to X (§6.2).
- **Fusion:** RRF with priors scored better than memorata's geometric-mean mix (+0.036; interval −0.008 to +0.090). RRF with priors is the default and mix stays selectable. *Decided by Joseph, 2026-10-09: "RRF is fine."*
- **A reranker on CPU costs 2.7–2.9 GB, not 18–21** (that was memorata's figure on Metal). It helps paraphrase queries and hurts definitions-first ordering. So it becomes an opt-in `--rerank` that reorders only the results that aren't definitions (§6.4).
- **Chunking and anchors need the changes in §5.2 and §7**: one passage per numbered or bold-labelled item as well as per glossary entry; headings indexed as a lexical field; definitions never split; duplicates collapsed within a document too; quotes built with links masked, widened until unique, and paged by the quoted sentence.
- **Some gaps belong to the lexicon, not the ranker.** Only the reranker connected "developer" to the AI Act's "provider". Query expansion through the per-source term mappings is the real fix, which argues for the translated layer (§9) coming early.

## 1. What it is for

Joseph's words, 2026-10-09: "at the very least it would be nice to be able to say 'I wonder if we've caught all of the mentions of "hazard"' and do a quick `bin/source-search 'hazard'` and get just what you'd expect in exactly the priority order you'd hope, also pulling in the nuance and allowing for narrowing into specific documents/sources or grouping them so you can see how internally consistent they are or if they've been properly translated when we get to that."

That asks for four different things, and one tool should do all of them, as separate modes:

1. **Ranked search.** The best passages for a query, semantic and lexical together, with definitions of the queried term first.
2. **Exhaustive search.** "Have we caught all the mentions?" can't be answered by a top-k list. It needs a concordance: every occurrence, counted by document and by word form, with no retrieval cut-off.
3. **Definitions.** Every place a source defines a term, grouped by source, with the active version first. This is the tool the lexicon's collision tables and the translations will lean on most.
4. **Grouping and narrowing.** Results by document, organisation, family or lineage, so internal consistency, copying and version drift are visible. Later, our terms beside the sources' words (§9).

It is local and specialised: one corpus (the catalog's sources), one database, one embedder. It is not memorata and doesn't replace it.

## 2. Inputs, and the contract with them

| Input | What it gives the index | Changes when |
|---|---|---|
| `source-catalog.md` | the set of keys; each key's status (`superseded-by`, `subsumed-by`, `no-canon`, or active); Influence grouping; family section; catalog code | catalog edits |
| `bib/refs.bib` (from relata) | title, authors (as organisation), date, URL, kind | relata edits, then `relata emit bib` |
| `ref/canonical/KEY.md` | the text, with physical-page markers, printed page labels, and ```` ```pdf-text ```` restored blocks | canonicalizer fixes, new conversions |
| `ref/canonical/msc/KEY/pages.json` | per-source fidelity mark, pages to check, uncertain-break windows | same |

The catalog's parsing contract is §2 of `influx/catalog-update-proposal-2026-10-08.md`. Both contracts, the catalog's and the canonical text's, now live in one module, `bin/corpus.py` (from the canonicalize session, 2026-10-09). It provides `read_catalog()`, `in_scope()`, each entry's `active` key, and the marker constants and regexes. The index imports it, as `bin/canonicalize` does, so the two can't disagree about scope, status or format.

What the canonicalize session reports as stable, and what the index has to allow for (2026-10-09):
- the marker lines and `MARK_RE` are stable;
- page markers can go *backwards*, in texts that aren't conversions of their PDF (today only IASR 2026, with 307 markers), and only those texts have `[not in pdf]`;
- a ```` ```pdf-text ```` block sits at the end of its page's section, in pdftotext's reading order, not where the text stood on the page. A passage from one has the right page but no heading context of its own;
- `pages.json`'s `fidelity.mark`, `pages_to_check`, `differences`, and each break's `page`, `line`, `printed`, `unlocated_letters` and `window_text` are stable; newer fields include `ocr_pages`, `web_render` and `edition_check`;
- `ref/canonical/skipped.json` lists keys not built, and why;
- a key that leaves the catalog keeps its old output on disk, so **the catalog, not the directory, decides what is indexed**;
- IASR's link tooltips stay in the canonical text (canonicalize edits a text's characters only for the recorded OCR "Al"→"AI" correction, `corpus.fix_ocr_ai`), so the chunker drops them from the indexed text (§5.2). The index should apply `fix_ocr_ai` to queries as well, so a query typed from an uncorrected copy still matches.

Who gets indexed: every catalog key with a canonical text, except `subsumed-by` keys, whose text is a copy of another key's. `superseded-by` keys are indexed and marked inactive. `no-canon` keys have no text, so they appear only as metadata.

## 3. Architecture

```
bin/source-index        reconcile the database with the inputs (idempotent; §4)
bin/source-search       query it (§7)
search/
  DESIGN.md             this file
  schema.sql            the database, with its rationale inline (memorata's practice)
  weights.toml          every ranking weight, each with a rationale (§6)
  eval/queries.toml     gold queries with expected results (§8)
  srcsearch/            the Python package: catalog, chunk, index, rank, cli
```

- **Language:** Python. psycopg and pgvector are mature there, `bin/canonicalize` and `bin/corpus.py` are Python, and memorata's mise Python 3.11 already has the dependencies installed.
- **Database:** a local Postgres 18 database, `airisk_sources` (a lean; any name works), with pgvector (0.8.x is installed; `halfvec` needs 0.7 or later), `pg_trgm` and `unaccent`. It is not in the repository; `bin/source-index` builds it from scratch on a new machine.
- **Embedder:** ollama, `bge-m3` (§5.4).

## 4. Idempotency: reconcile, don't append

`bin/source-index` computes the desired state from the inputs and brings the database to it. Running it twice changes nothing the second time. Running it after any input change touches only what changed.

**Three fingerprints per document:**
- *text fingerprint*: sha256 of the canonical file's bytes, plus the chunker's source hash. A changed canonical text, or a changed chunker, re-chunks the document. Taking the chunker's source hash, not a version number, is memorata's `parser_source_hash` lesson: a forgotten version bump can't leave stale chunks.
- *metadata fingerprint*: sha256 of the key's bib entry and its catalog row and status. A change updates the document row only. If the title or heading context that goes into embeddings changes, the affected passages are re-embedded (below).
- *fidelity fingerprint*: sha256 of `pages.json`'s fidelity section. A change updates passage flags only.

**Per run:**
1. Read the catalog, bib and canonical directory, and compute every document's fingerprints.
2. For each document whose fingerprints differ from the database's, or that is new: in one transaction, delete its passages and definitions, re-chunk, insert, and record the new fingerprints.
3. Delete documents whose keys have left the catalog, or whose status became `subsumed-by` (cascading to passages and definitions).
4. Embed every passage whose embedding input has no cached vector (resumable; commits per batch).
5. Garbage-collect cached vectors no passage uses (optional, with `--gc`; keeping them makes a revert free).
6. Record the run: counts of documents added, changed, removed and unchanged, passages embedded, warnings.

**The embedding cache is separate from the passages.** It is keyed by sha256 of (model, embedding input), and it lives in its own schema, so dropping and rebuilding the main tables never re-embeds anything whose text didn't change. Re-chunking a document whose canonical text gained one restored ```` ```pdf-text ```` block re-embeds only the passages that actually differ.

**Rebuild is a supported operation.** `bin/source-index --rebuild` drops the main schema and rebuilds from the inputs, using the cache. Schema changes are handled that way rather than by migrations, because everything outside the cache is derived.

`--dry-run` prints what would change. A run never deletes anything that isn't derived from the inputs, since nothing in the database is hand-entered (weights live in the repo, §6).

## 5. Chunking: structure first

### 5.1 Blocks

The chunker parses each canonical file into blocks and carries state through it:
- **page:** from `[pdf-page N, printed "X"]` markers. A passage records its first and last physical page, and the printed labels. `[not in pdf]` stretches (IASR's web edition) are flagged. For a source marked check-all, the marker's page is approximate: IASR 2026's web edition has no page breaks of its own, so its pages are assigned a line at a time, and a paragraph straddling two pages carries one of them (the pilot found 25 such mismatches in 711 anchors, 2026-10-09). For those sources, the page a result reports is settled by `bin/check-quote`, which checks against the PDF, and it is cached with the passage.
- **heading path:** from markdown headings, cleaned of `<span id=…>` noise, e.g. `2. Risks › 2.2 Risks from malfunctions › 2.2.2 Loss of control`.
- **block kind:** paragraph, list item, table, ```` ```pdf-text ```` (restored text), image (dropped from indexed text), heading.
- **section kind**, elected per section from its heading and its contents: body, glossary, definitions, key-information box, table of contents, references, index, abbreviations, annex, front matter.

### 5.2 Passages

- **Size:** about 800–1,500 characters, split at paragraph and then sentence boundaries, never across a heading, with a one-sentence overlap. That is smaller than memorata's 2,000, because the aim here is to land on the clause that defines or claims, not the page around it.
- **One entry, one passage.** A glossary entry, a statutory definition (each `(c)`, `(h)` of a definitions section), a "Key Definitions" item, or a footnote definition becomes its own passage, however short.
- **Tables:** split by groups of rows, each passage carrying the header row, because thresholds live in table rows.
- **Text indexed vs text shown.** Indexed text drops image links, link targets and their tooltips, and HTML spans. This is the IASR web edition's problem: every footnote's full reference text is repeated in a link tooltip at each citation, which inflated raw counts from about 730 to 993 (plan §3.4). Displayed text and quote anchors use the canonical text's exact characters, through stored offsets, so quotes from the index match the canonical file byte for byte.

### 5.3 Definitions

A `definitions` table records each passage that defines a term, with:
- the term as written;
- a normalised form (casefolded, unaccented, singular, quotes and bold stripped);
- the kind: glossary entry, statutory "means", key-definitions item, inline ("we define", "refers to", "By 'X' in this document, we mean"), or footnote;
- the evidence that fired, and a confidence.

Detection rests on structure as well as wording, because the corpus shows both:
- 26 canonical texts have a heading like "Glossary", "Key Definitions", "Definitions", "Terminology" or "Abbreviations". The IASR 2025 report alone has 24 "Key Definitions" boxes.
- IASR 2026's glossary has **no heading** in the canonical text; it is a long run of `**Term:** definition.` paragraphs. So a run of three or more same-shaped entries is itself evidence of a glossary.
- Statutory definitions are `"X" means` or `'X' means` inside a numbered definitions section: 67 in the AI Act, 15 in SB 53.
- Some definitions are inline or in footnotes: OpenAI's Preparedness Framework defines "severe harm" in footnote 1 ("By 'severe harm' in this document, we mean…").

Detection errs toward recall and marks its confidence. The definitions view shows the evidence, so a false positive is visible and its pattern can be fixed.

### 5.4 Embeddings

Measured on 2026-10-09, on 21 SB 53 passages averaging 2,100 characters, warm:

| Model | Dimensions | Context | Time | Memory loaded |
|---|---|---|---|---|
| bge-m3 | 1024 | 8,192 tokens | 0.9 s | 0.7 GB |
| embeddinggemma:300m | 768 | 2,048 tokens | 1.3 s | |
| snowflake-arctic-embed2 | 1024 | 8,192 tokens | 4.1 s | |
| nomic-embed-text-v2-moe (memorata's) | 768 | **512 tokens** | 0.7 s | 0.6 GB |
| qwen3-embedding | 4096 | 32,768 tokens | 21.3 s | 8.6 GB |

Lean: **bge-m3**. It is fast, small and multilingual (the corpus includes Chinese and EU material), and its context covers any passage whole, but only once `num_ctx` and `num_batch` are raised; by default ollama truncates it at 2,048 tokens. qwen3-embedding is about 16 times slower and holds 10 GB, the kind of memory cost Joseph wants to avoid, and in the pilot it bought nothing.

*Corrected by the pilot (§0):* two arguments here didn't hold. At the designed passage size (about 1,200 characters, median 199 tokens) only 5 of 3,714 passages exceed nomic's 512 tokens, so truncation is no argument against it; it lags on quality instead. And the 0.9 s vs 4.1 s gap to snowflake-arctic-embed2 came from 2,100-character passages; at 1,200 characters they run at the same speed (95 s vs 97 s for 3,714 passages), and arctic2 is an equally good choice.

**Embedding input:** the document's title and the passage's heading path, then the passage text. Context like this makes a bare clause such as "(c) 'Catastrophic risk' means…" findable as SB 53's. Changing a title re-embeds that document's passages, and nothing else.

Estimated cost: the corpus is about 21 MB of text today (89 canonical files), heading toward about 100 MB at 463 keys. At ~1,200 characters a passage that is roughly 80,000 passages, and at bge-m3's measured rate a full first embedding is about an hour. After that, runs embed only what changed. Vectors are stored as `halfvec(1024)`, about 160 MB with its HNSW index at that scale.

### 5.5 What building it found (step 1, 2026-10-09)

Read against SB 53, the AI Act, IASR 2026 and AISI's OCR'd *Frontier AI Trends Report* (`bin/source-index --show KEY` prints any text's passages and definitions):
- **Definitions found:** SB 53's 18 and the AI Act's 68 statutory definitions; IASR 2026's 179 heading-less glossary entries; the EU Code's 35 glossary rows, including qualified ones ("'process' (noun; …)"); OpenAI's footnote "By 'severe harm' in this document, we mean"; AISI's 29 glossary entries, six of which lost their bold in OCR and are caught as plain "Term:" lines. Across the corpus: 2,193 definitions in 201 texts.
- **Heading paths.** Conversions give headings arbitrary levels: the AI Act has `# *Article 4*` at level 1 and its title at level 3. So a heading that is only a label ("Article 3", "ANNEX I", "CHAPTER III", "SECTION 2") nests by its kind, and the title heading after it joins it: `CHAPTER I — GENERAL PROVISIONS › Article 3 — Definitions`. A statute's section numbers in list items act as headings, a code section inside the bill section that adds it (`CHAPTER 138 › SEC. 2 › §22757.12`). A table-of-contents heading no longer parents the front matter after it.
- **Offsets are exact.** Indexed text keeps each character's offset in the canonical file, so a piece of a long block, or a sentence quoted from one, maps to an exact span and page (the pilot located pieces by their first words).
- **A paragraph cut by a page break is joined** when it starts in lower case and the block before it doesn't end a sentence (12 joins in the AI Act, 11 in the AISI report).
- **Weaker evidence, marked weaker.** "The term 'X'" sometimes introduces a definition and sometimes only mentions the word, so it gets 0.6 to "the notion of 'X'"'s 0.8. "We use X as" isn't taken as a definition unless X is quoted or named as a term. `**Label:** text` runs give 1,025 weak (0.35–0.5) definitions; in a sample of 30, about a quarter were real definitions ("CBRN-3: The ability to …"), the rest labels ("Updates:", "Methods:"). Their low confidence keeps them from ranking unless the query is that exact label.
- **Not fixed:** OCR's glued forms such as "AlSI's" are still in the canonical texts (a decision for Joseph, in the canonicalize session's list). Footnotes inside the AI Act's recitals become passages of their own.

## 6. Ranking

### 6.1 Candidates

For a query, the index gathers candidate passages from five signals:
1. **semantic:** cosine distance on the passage embedding (HNSW);
2. **lexical, stemmed:** Postgres full text, `english` configuration;
3. **lexical, exact form:** full text with the `simple` configuration. Stemming conflates words this project keeps apart: "developer" and "development" both stem to *develop*, and "provider" with "provision" is close. An exact-form match counts for more than a stemmed one;
4. **phrase:** `phraseto_tsquery`, words adjacent and in order;
5. **defined term:** passages whose definition's normalised term matches the query, or contains it.

### 6.2 Combining them

Semantic and lexical stay two rankings, fused by reciprocal rank fusion (RRF): each passage scores `1/(60 + rank)` from each side, summed, so a passage that is best on either side floats up. Memorata's `mix` (the geometric mean of the two rank positions) stays selectable; the pilot found RRF better with priors (§0), and Joseph chose it as the default. Lexical evidence (exact form, stemmed, phrase, proximity, density) is folded into one lexical score so nothing is counted twice.

What is built, checked 2026-10-09 against `rank.py`: BM25 on exact word forms, BM25 on Postgres's English stems at half weight, a ×2 phrase factor and a heading factor. Memorata's proximity and density functions were meant to carry over and have not been built. Three changes to the lexical side of `hybrid` (§7), each to be measured on `search/eval/pilot-check` before and after. The first is agreed; the other two are my proposals, which Joseph supported ("possibly influenced by my thoughts on #1", his whole-word preference) without settling them:
- **Proximity and density, ported from memorata.** *Agreed: Joseph, 2026-10-09, "I agree-- already my lean, from the beginning." Built 2026-10-09: proximity multiplies the fused score rather than sitting in the lexical score, and density is off; see §11 step 5.* (`memorata3/search.py`). `proximity_score` combines four things: whether each word matched exactly or as an inflection (an inflection counts 0.55); the tightest window covering the matched words, with small penalties for each extra word and large ones for each sentence and paragraph boundary; whether the words are in the query's order (×0.75 if not); and how many of the query's words appear. It abstains on one-word queries. `keyword_density` blends how often the words occur with their rate per word, since RRF keeps only rank.
- **The phrase factor uses the literal matcher (§7.1)** (my proposal, supported by Joseph), with case and word boundaries, instead of Postgres's lowercased phrase match. Joseph's example: `'AI Concierge'` matches "AI Concierge" and "AI CONCIERGE", since only the capitals are fixed, but not "AI concierge" or "ai concierge". Near misses ("AI-powered concierge", the two words in one sentence) are graded by proximity. A query that must match literally could have a separate flag (`--require`, my suggestion); the default is a boost, never a gate, because a gate would drop the paraphrases that the semantic side exists to find.
- **A word's longer forms replace the stem leg**, at reduced weight (my proposal; Joseph left the rest of this design to me, 2026-10-09). *Measured worse and not adopted, 2026-10-09: the stems stay (§11 step 6).* A query word's longer forms (plurals, past tenses, "hazardous"), found as `lexical` finds them (§7.1), count for less than the word itself. Postgres's stems also merge words that share only a stem ("developer", "development"), and they hide which form matched; this shows each form, and needs no stemmer or lemmatizer. Recall is cheap in a ranking, since a weak match only ranks low.

Then come the query-independent priors, multiplied in. Each is declared in `search/weights.toml` with its rationale, in the spirit of memorata's evidence weights: a weight that can't say why it exists doesn't belong there. The initial set, in rough order of strength:

| Prior | Direction | Why |
|---|---|---|
| **defines the queried term** | strong boost | Joseph: "Whether a chunk is part of something specifically designated as a glossary or definition or something might be very high factor". It applies only when the defined term matches the query; a glossary entry for another term gets nothing |
| **section kind** | contents, index, references and abbreviation lists strongly down | these lines mention every term and say nothing about it |
| **active vs superseded** | superseded down, and collapsed under its active version (§6.3) | the active document is the one the lineage treats as current |
| **Influence** | anchor > major > supporting > corpus, mild | reach in the field, as the catalog declares it |
| **recency** | newer mildly up, measured within the document's organisation | Joseph: "Freshness of document, freshness within a source (company, institute)". Memorata favours *older* text, for provenance; this corpus wants the opposite |
| **fidelity** | none on rank; shown | a `check-all` or check-page passage is as relevant, but its quote needs the PDF; the output says so |

### 6.3 Collapsing, not hiding

- **Verbatim copies across documents.** Passage text is hashed after normalisation. The same text in several documents (the EU Code's loss-of-control formula; SB 53's definitions in RAISE) is shown once, with "also verbatim in: …". Here copying is evidence, the thing the correlation-not-corroboration principle is about, so it is surfaced, not discarded.
- **Near-duplicates across versions** (RSP v3.3 and v3.4) are folded under the active version, with the versions listed. `--history` unfolds them in lineage order, which is the "diffable history" the supersession tags were kept for.

### 6.4 No cross-encoder by default

Memorata's optional reranker (`bge-reranker-v2-m3` in sentence-transformers) peaked at 18–21 GB of Metal memory over six searches, or about 4.8 GB on CPU (its own measurement, 2026-09-24). Here, the structural priors carry most of what a reranker would add: definition, section kind, status and exact form. My lean was to build without one and let the gold queries show whether anything is missing. The pilot (§0) measured the CPU fallback at 2.7–2.9 GB and about 2 s a query, helping paraphrase queries and hurting definitions-first ordering, so it becomes an opt-in `--rerank` that leaves definitions in place.

## 7. The command

*Agreed with Joseph in discussion, 2026-10-09, and built the same day (§11 step 4): `bin/source-search help` is the live description. Joseph proposed the verbs (including the three `exact-*` ones), the positional scope, and `lexical` as the loosest verb, matching words in order within a chunk; the names `hybrid` and `semantic` were worked out between us. He then left the rest of the design of the concordance verbs to me ("this *is* a tool primarily for agents"), so the details below are mine unless marked as his.*

```
source-search [verb] [flags] 'query' [scope …]
```

The query is one argument, as for grep and rg. Everything after it says what to search:
- a relata key;
- a key prefix (`'anthropic-*'`, quoted so the shell leaves it alone);
- a named set (`Au5`);
- a selector over catalog fields (`org:anthropic`, `influence:anchor`).

With no scope, it searches everything indexed. A scope that matches nothing is an error (exit 3), not an empty result. `--in` goes.

**Verbs.** A verb names a common use, so the everyday case needs no flags. It need not name a distinct kind of operation (Joseph: the verb form "is more about usage and not having to remember flags for the sunny-day scenario"). Flags still compose with every verb.

| Verb | What it gives |
|---|---|
| `hybrid` | A ranked list: the semantic and lexical rankings fused by RRF, then our weights (§6.2). It is implied when only a query is given. |
| `semantic` | A ranked list by cosine similarity alone, over the whole corpus rather than a pool of 400, with none of our weights. Set beside `hybrid` on the same query, it shows what the lexical side and the weights change. An exclusion flag drops passages containing the query as a phrase (§7.1), leaving the passages that say it in other words. Joseph proposed the exclusion; matching it as a phrase and calling it `--without-phrase` are my proposals. |
| `defs` | Every definition of a term, grouped by source, active versions first. `--exact` drops the narrower terms that contain it. |
| `lexical` | The loosest concordance: the query's words in order within one passage, with anything between them (§7.1). Each word has a left boundary and may run a few letters further on the right. A table of the distinct spans found comes first, then each occurrence in context. |
| `exact-phrase` | The words in order, adjacent, as whole words exactly as typed. The separators between them stay flexible. |
| `exact-words` | Each word exactly as typed, as a whole word, counted separately wherever it occurs. |
| `exact-bytes` | Those characters, spaces included, with no case folding. |
| `help` | Implied when there are no arguments; `-h` and `--help` work too. |

The four concordance verbs are one operation at different strictnesses, and `--help` groups them so: otherwise an agent may take `exact-phrase` for a different kind of search from `lexical`. Three of them form a ladder, `exact-bytes` → `exact-phrase` → `lexical`, each looser than the one before (not strictly nested: `exact-bytes` alone can match inside a word). `exact-words` sits beside the ladder, since it counts each word on its own.

### 7.1 The literal matcher

One matcher serves the four concordance verbs, the lexical side of `hybrid` (§6.2) and `semantic`'s exclusion flag.
- **Case.** This is Joseph's convention: a lowercase letter matches either case, and an uppercase letter only itself. `'ai'` finds "AI" and "ai"; `'AI'` finds only "AI". It is applied letter by letter, unlike rg's smart-case, where one capital makes the whole pattern case-sensitive. `exact-bytes` folds nothing.
- **Word boundaries.** The `exact-*` verbs put a boundary on both sides of every word, Joseph's first preference. `lexical` keeps the left boundary and allows a few more letters on the right (below), so it gets plurals, past tenses and short derived forms ("hazardous") without a stemmer, and its span table shows each one. A `*` removes the boundary on its side entirely: `'hazard*'` finds every longer word, and `'*hazard'` finds "infohazard". The measurements behind this (2026-10-09, over the canonical texts):
  - `AI` occurs 38,759 times as a whole word. An open right side (before the cap below) adds "AIs" 703 times (wanted), and "AISI" 655, "AISIs" 21, "AIR" 34 and "AIA" 34 (not wanted, but visible in the table).
  - An open left side would add far more noise: "OpenAI" 2,375, "xAI" 752, "CAISI" 568, "GAI" 426, "AAAI" 157. For `act` it would add "impact" 2,113, "practices" 2,106, "practice" 1,378 and "impacts" 1,220. So even the loosest verb keeps the left boundary.
- **Separators** between the words of a phrase are any run of non-alphanumerics, so line breaks, hyphens and punctuation match: "loss-of-control" and "loss of" at the end of one line with "control" on the next.
- **`lexical`'s unit is the passage.** Joseph, 2026-10-09: the words count "when they are in that order in a logically coherent chunk of source text", not when they are in that order across a few sections. A passage never crosses a heading, and a glossary entry or statutory definition is a passage of its own (§5.2). Passages overlap by one sentence, so a span inside the overlap is counted once, by its offsets in the canonical text.
- **Counting `lexical`'s spans.** Each match is the shortest span from a starting word, so overlapping spans aren't counted twice. The span table groups spans by their text, ignoring case and separators. Measured with rg for `loss … control` with at most 40 characters and no full stop between them (2026-10-09; the canonical texts with their markup, which the index strips), it would show "loss of control" 876, "loss-of-control" 45, "loss of human control" 7, "losses of control" 3, "loss-control" 3, "loss of meaningful human control" 2, and one OCR'd "lossof-control". The qualifiers sources put inside a phrase are thus a lexicon finding in themselves. The occurrences are then ordered by `hybrid`'s lexical scoring, proximity included (§6.2), as Joseph suggested: "say 'within chunk' but use our earlier logic for ranking". So a tight span ("loss of human control") comes before one whose words fall in separate sentences of the same passage, which is more often two separate mentions than a wording. Nothing within the passage is excluded; distance only lowers the rank. `--by source` groups the occurrences by document instead.
- **The right side of a `lexical` word.** Each word may end in one of its spelling variants, then up to four more letters, then a plural or possessive ending (*s*, *'s*, *s'*) that doesn't count toward the four. Settled 2026-10-09: the cap was Joseph's idea, and so was counting it from the end of the full word; the spelling rules and the free ending are mine.
  - **Two spelling rules** reach the forms whose ending changes, which a plain open end misses. Measured over the canonical texts, 2026-10-09: "capability*" finds "capability" (3,406) but not "capabilities" (6,731); "define*" misses "defining" (245); "use*" misses "using" (2,180). A final *e* may drop before *i* or *e*, so `use` matches "using" but not "us" or "usual". A final *y* after a consonant may become *ie*, so `capability` matches "capabilities", and `policy` matches "policies" but not "police". Doubled consonants ("planned") need no rule.
  - **The rules strip only where the ending actually changes.** Joseph also floated stemming the word and stripping its final vowels. Measured on 18 key terms, the shortened stems matched other words: `severe` → `sever` matched "several" 953 times; `use` → `us` matched "US", "USA" and "usage"; `policy` → `polic` matched "police"; `deploy` → `depl` matched "deplete". Snowball first was worse: `capability` stems to `capabl`, which misses "capability" and "capabilities" for "capable", and it lowercases `AI`.
  - **The four-letter cap** drops glued compounds and URL fragments ("modelcontextprotocol", "AIStateofScience", "safetywashing"). It also drops long derivations that are really other words: "definition" for `define` (412), "policymakers" for `policy` (356), "harmonisation" and "harmonised" for `harm` (240), "controllability" for `control` (97). Without the free plural ending, the cap would keep "assessment" but drop "assessments" (1,090), and likewise "deployments" (435) and "developments" (247).
  - Irregular forms ("children", "ran") are missed. I expect them to be rare among this corpus's key terms, which I haven't measured, so no inflection library seems needed.
  - The same right side gives `hybrid`'s reduced-weight forms (§6.2). A word typed with a trailing `*` has no cap.
  - These measurements came from a scratch script over the canonical texts with their markup, splitting at hyphens as the matcher will. They cover 18 words I chose, so they are a check, not a sample.
- **Stemming:** `--stem` uses Postgres's Snowball stemmer, which also merges words that share only a stem ("developer", "development"). Its help says so.
- **What a looser match would add.** Every verb reports, by form, what the next verb up the ladder, and a `*` on each bounded side, would have added. So a narrow search shows what it left out, and the wider search is one step away. The JSON carries the same as `not_counted`.
- **Context:** `-C N` for the amount shown around each occurrence. My lean is to count sentences, not lines.

### 7.2 Scopes and sets

Sets live in `catalog/sets/*.yaml` (§13). A set is a list of selectors:
- keys and key globs;
- catalog fields (`org: anthropic`, `influence: anchor`, `status: active`, a catalog section, or any field §13 adds, so many sets need no enumerating);
- other sets;
- exclusions.

The same selectors work inline on the command line, so a one-off scope needs no file. A set name that collides with a key is an error when the sets are loaded. Joseph first suggested `.source-search/{catalog.yaml,sets/*.yaml}`, then left the placement to me. I put them under `catalog/` because they aren't only search configuration. `bin/canonicalize`, relata's bibliography and the translations read the catalog. Au5 serves the outline work, and G4's pilots are a set too.

### 7.3 Output

Every result carries an anchor in the plan's form (plan §3.5, Claude's proposal, endorsed by Joseph 2026-10-09): relata key, physical PDF page, printed page, and the exact quote. This is a requirement, not a default. Joseph, 2026-10-09: "the search results should always come back with your preferred reference format -- key + pdf-page etc. etc." Every verb and the JSON carry it, with a "check against the PDF" flag where the source's fidelity mark calls for it. A quote copied from a result can then be cited as it stands, and checked with `bin/check-quote`, which takes anchors in bulk on stdin (`--batch -`). The concordance counts headings, and counts references separately, and it never matches inside link targets.

Flags shared across verbs: `-n` (how many results), `--explain` (the factors behind each score), `--verify` (runs every anchor through `bin/check-quote`), `--json` (automatic when piped), and, not built yet, `--by source|org|family|lineage` and `--history` (§6.3).

Memorata's hard-won output rules carry over:
- an empty result and a failed search are different outcomes (memorata exits 3 and leaves stdout empty on failure);
- filters widen the retrieval aperture before they report "nothing";
- the snippet shows every match;
- JSON is valid even when empty.

## 8. Knowing it ranks well

Joseph's bar is "just what you'd expect in exactly the priority order you'd hope". That is checkable only against stated expectations, so the index ships with gold queries (`search/eval/queries.toml`) and `bin/source-search --eval`. The eval reports, per query, where each expected passage ranked. The first queries can come from facts the plan already establishes, checked at the source:
- `hazard`: the definitions in IASR 2026's glossary, the NRR, and the OECD paper (which defines "AI hazard" as a potential incident, catalog proposal §7) rank above passages that only use the word;
- `catastrophic risk`: SB 53 §22757.11(c) first, with Labor Code §1107's version and RAISE's copy folded or adjacent;
- `severe harm`: OpenAI's PF footnote 1 and the FGF's §2.1 both in the top five, as different documents;
- `loss of control`: the EU Code's formula, showing its recurrences;
- `developer --defs`: AI Act Art. 3(3) and 3(4), SB 53 §22757.11(h), IASR's "AI developer", NIST's AI actors.

Weights change only with an eval run before and after, recorded in the commit message. Same-model coherence applies: I would be writing both the gold set and the ranker, so the gold set should go to Joseph, or a reader from another model family, before it is trusted as a target.

## 9. The next layer: translated editions

Joseph asked, 2026-10-09, whether the step after `ref/canonical/` is something like `ref/arm-translated/`: canonical text with our terminology notes. The plan has that milestone: G6's *translated editions* (§4 G6, decision 13), "its own text with each key term marked in place as our term beside the original … plus a sidecar document discussing the nuances and translation problems". Under the source-namespace proposal (plan §3.2 note), the in-place marks would be the occurrence marks (`{a | b}` and so on). Two qualifications:
- **Timing.** A translated edition needs the lexicon terms and resolution records it marks with. So it comes after G2–G4 for the pilots, not directly after canonicalization.
- **Licensing.** `ref/canonical/` is git-ignored because most texts can't be republished. Translated editions follow the plan's rule: published only where the licence allows (statutes, US federal works, OGL, CC-licensed); otherwise local, with only the sidecars public.

The index should be ready for it. A translated edition keeps the canonical page markers, so it can be indexed as a second *layer* of the same document, aligned to the canonical passages by page and offset. A result could then show the source's words and our terms side by side, and `--by source` could show where a term was translated, left ambiguous, or not yet translated. The schema leaves room for this (a `layer` column on passages) but builds nothing for it yet.

## 10. Decisions for Joseph

1. ~~Build it as designed, starting with the minimum in §11?~~ *Decided by Joseph, 2026-10-09: yes.* He also said the pilot's `qrels-pilot.json` can stay in the public repo, and `qwen3-embedding:0.6b` stays installed for now.
2. **Embedder: bge-m3**, confirmed by a bake-off on the gold queries once they exist. *Confidence: moderate-high.*
3. **No cross-encoder at first** (§6.4). *Confidence: moderate*; the eval decides.
4. **Recency favours newer**, within each organisation, mildly. This is the opposite of memorata. *Confidence: moderate.* An older document can matter more as a lineage root, which the lineage views handle rather than a weight.
5. **The weights live in the repo** (`search/weights.toml`, each with a rationale), not in the database. This is public and reviewable, and the database stays wholly derived. *Confidence: high.*
6. **Database name `airisk_sources`, outside the repo; Python in `search/`.** *Confidence: high* on the shape, none on the name.
7. ~~Share the catalog parser with `bin/canonicalize`.~~ Done: `bin/corpus.py` (2026-10-09).
8. ~~The command's shape.~~ *Agreed in discussion with Joseph, 2026-10-09* (§7): verbs for the common uses, the query as one argument, keys and sets as scope, whole words by default, `semantic` as cosine alone and `hybrid` as the fused default.
9. ~~The catalog's format.~~ *Joseph, 2026-10-09: "I would prefer to move it to yaml though one way or another. No problem if this affects canonicalizer and so forth."* Where it, the sets and the lock live he left to me (§13).
10. **Whether `source-catalog.md` is generated from the yaml** or retired. My lean is generated (§13). *Confidence: moderate.*

## 11. Build order

1. Schema, catalog reader, chunker and definitions detector, with no embeddings yet. Check by reading the chunk and definition output for SB 53, the AI Act, IASR 2026 and one OCR'd source. *Built 2026-10-09* (`bin/source-index`, `search/srcsearch/`, `search/schema.sql`); what the reading found is in §5.5. The reconcile part of step 2 came with it: a full build of the 201 texts takes about 20 s, and a second run changes nothing (0.1 s).
2. Reconcile and embed, with the cache; run twice to show the second run does nothing; touch one canonical file and show only it changes. *Built 2026-10-09.* bge-m3 embedded all 26,617 distinct passage inputs in 12 min 18 s, with relata's queue paused; a rerun embeds nothing. Batches commit as they go, so a stopped run resumes. (The first attempt held its opening read transaction for the whole run, so nothing committed until the end and a concurrent `--rebuild` waited on its locks; the read is now committed before embedding starts.) Changing one canonical file (NVIDIA's, by one byte, then restored) re-chunked that document alone in 0.2 s, and the next run changed nothing; a change to the chunker's own source re-chunks all 201 (about 35 s) and re-embeds only passages whose text changed. `bin/source-index --dry-run` lists what a run would redo.
   - *Reindexed 2026-10-09, evening,* after relata's new conversions: `bin/canonicalize` built 392 texts (77 keys still await conversion), and the index now holds 392 texts, 48,412 passages (5.47 million words), 20,575 headings and 3,131 definitions. It re-chunked 191 documents and embedded 21,590 new passages in 11 min 41 s, with relata's queue paused.
3. Search: ranked, `--defs`, `--all`, `--explain`, `--json`. *Built 2026-10-09* (`bin/source-search`), with `--in` and `--verify` (runs every anchor through `bin/check-quote`). Checked two ways:
   - **Against the pilot's blind grades**, narrowed to its 10 sources (`search/eval/pilot-check`): nDCG@10 0.776 with RRF and the priors, against the pilot's 0.786; mix 0.724, lexical alone 0.702. That is the pilot's ordering, and the gap to the pilot is within the noise it warned of (±0.05 on 16 queries). The priors the pilot didn't test (Influence, recency, superseded, restored text) add 0.02 on this set: noise-level, and not harmful. Scoring a built passage against a quote the pilot graded needs a tolerant match (80% of the quote's letters in one run), since the pilot cut passages differently and kept footnote markers.
   - **Anchors**, run through `check-quote` for the pilot's 16 queries over the whole corpus: ranked, 156 of 160 ok; `--defs`, 239 of 241 ok. The six others are one SaferAI page that quotes the same sentence two or four times, and their anchors say the quote isn't unique on its page. `--all` (about 32,300 anchors, since it quotes every occurrence; measured when `--all` matched by substring, as `'*term*'` now does) about 96% ok; most of the rest are table and contents-page text, whose order in the PDF's text layer differs from the canonical text's, so `check-quote` can't confirm the page from the PDF (673 "unconfirmed"), and IASR's web-only text, which isn't in the PDF and is flagged so (106). Quotes keep footnote markers and citation link texts ("including7 the", "(Illinois House Bill 5116 2024)"), which the indexed text drops: `check-quote` matches them. Quotes are widened until unique on their page, counted the way `check-quote` counts (letters only, so SB 53's "(e) 'Frontier developer' has the meaning …" also matches inside "(f) 'Large frontier developer' has the meaning …"), and kept clear of "[…]" and "...", which `check-quote` reads as gaps. Where a passage is genuinely repeated on its page (SaferAI quotes the same OpenAI sentence four times on p. 202), the anchor says so.
   - Ranked search takes 1–2 s, most of it loading bge-m3 for the query; `--defs` and `--all --counts` well under a second.

The order is mine, with Joseph's leave ("I'm happy to defer to you"), 2026-10-09:

4. The verbs, the literal matcher and scopes (§7), with sets resolved against the catalog fields the index already holds, so the switch to yaml doesn't block them. *Built 2026-10-09* (`search/srcsearch/match.py`, `concord.py`, `scope.py`; `catalog/sets/` holds Au5, G4-pilots and Anchors, the last by selector). Checked:
   - `hybrid` gave identical top tens to the previous code on 6 queries (lexical-only fusion, on one database state), and `pilot-check` scores 0.777, against 0.776 before the reindex of 2026-10-09.
   - `exact-phrase 'loss of control'` agrees with rg on SB 53, the AISI report and the EU Code; on IASR it finds 49 against rg's 55, the difference being link markup the index strips. `exact-words AI` on the NRR finds 33, as before.
   - An unknown scope exits 3; a retired flag (`--all`, `--defs`, `--in`) exits 2 and names its replacement.

   Decisions §7 didn't settle, mine:
   - function words (of, the, to …) stay whole words in `lexical`, or 'of' would find "often";
   - a query with a capital keeps case in the forms table ("AISI" apart from "AIs");
   - `exact-bytes` matches the indexed text (markup removed, runs of spaces made one);
   - `--without-phrase` drops passages whose words are adjacent, each with `lexical`'s run-on;
   - in selectors, `,` means any of these values and `+` means all of these fields; `year:` takes N, N..M, >=N or <=N; `set:Name` is explicit, set names are case-insensitive, and only set files can exclude;
   - concordance matches are ordered by memorata's in-order proximity weights (0.03 a word between, 0.25 a sentence break, 0.6 a paragraph break) until step 5 ports the full function; an anchor quotes the sentence where a span starts;
   - `--fusion` stays on `hybrid`, hidden, for `pilot-check`.

   Found: the cap still admits short derivations ("severity" for `severe`, "harmful" and "harmless" for `harm`, "users" for `use`), all shown in the forms table; and `lexical` spans across table cells are noisy ("loss of gas supply … heating controls", 138 words), sorting to the bottom. The concordance verbs have no `-n`; `--counts` gives the tables alone. A full `lexical 'loss of control'` over the corpus (1,095 occurrences) takes about 8 s, mostly building anchors.
5. Proximity and density in `hybrid`'s lexical side (§6.2), measured on pilot-check before and after. *Done 2026-10-09*, with step 6: pilot-check 0.777 → 0.803 (lexical side alone 0.703 → 0.770). Each value and its measurement is in `search/weights.toml`. Briefly:
   - **Proximity is on**, at memorata's 0.6, multiplying the fused score as memorata does: +0.026 (interval −0.002 to +0.073), most of it one query ("information hazard", +0.339). Folded into the lexical score instead, as §6.2 first had it, it changed nothing, because RRF keeps only the lexical rank.
   - **Density is off.** It cost one-word queries, where it is the only signal ("whistleblower" −0.084).
6. A word's longer forms in place of the stem leg, and the literal matcher in the phrase factor (§6.2), each measured the same way. *Done 2026-10-09:*
   - **My proposal to replace the stems with longer forms measured worse:** −0.011 replacing them, −0.003 beside them. The query word is often the derived form itself: "misalignment" needs "misaligned" (−0.060 without stems), and "whistleblower" needs "whistleblowing" (−0.166). So the stems stay, and the forms code is kept, switched off (`forms_weight = 0`).
   - **The phrase factor had a bug.** It ran Postgres's phrase match on the content words alone, so it looked for "loss control" and never fired for "loss of control" (0 passages over the pilot's sources; the literal matcher finds 37). It now uses the literal matcher with longer forms: +0.001 fused, +0.045 by the lexical side alone.
   - **A cue for queries nothing answers,** for §11 step 8: `rank.answerability()` flags a query when no passage in scope holds all its content words and the nearest passage is at cosine distance 0.50 or more. Over Au5 that flagged all 20 off-topic test queries and none of 21 on-topic ones; over all texts, 10 of 20 and none on-topic. It labels results and never hides them, and it is untested on queries near the corpus's subjects that it doesn't answer. Nothing calls it yet.
7. The catalog in yaml, the lock and `ref/canonical-meta/` (§13).
8. The folded outline on Au5 and the definitions pass (§12). Joseph gave the go on 2026-10-09: "The one thing I'm particularly excited to see is the aspectus-like (in spirit) ToC contextual hybrid-- the holy grail here so to speak." *The outline is built, as a prototype* (`search/srcsearch/outline.py`; for now a separate command, `bin/source-outline 'loss of control' Au5 --lines 40`). How it works:
   - **The tree comes from each passage's heading path**, which is fuller than the headings table: SB 53's "§22757.12" is a path element with no heading row of its own.
   - A title that recurs after a different section starts a new node, since IASR's many "Key information" boxes would otherwise merge into false ranges. Restored PDF text joins the section of the passage before it.
   - **Every passage in scope is scored by `hybrid`.** "top" is the best 2% in scope and "near" the next, to 10%.
   - **Passages open in score order under the line budget.** An exact definition of the term opens first, and adjacent passages merge into one range.
   - **No fold is silent.** Sections without a top passage are counted on their parent's line ("+9 sections not shown (5 near)"), and lines left over go back to naming them.
   - Each opened range gives its lines of `ref/canonical/KEY.md`, for reading, and an anchor, for citing. A heat column (█▓▒░) marks a section whose best passage is in the best 1%, 2%, 5% or 10% of the scope.

   Measured against the pilot's blind grades (111 grades of 2 or 3, in four Au5 documents), as recall weighted by grade:

   | Lines | Outline opens | Ranked list, same output lines | Ranked list, same source lines read |
   |---|---|---|---|
   | 40 | 0.749 | 0.680 | 0.814 |
   | 60 | 0.898 | 0.724 | 0.890 |
   | 120 | 0.922 | 0.853 | 0.949 |
   | 200 | 0.955 | 0.904 | 0.955 |

   So in the same output space the outline points to more of what matters, while a list read to the same number of source lines does about as well or slightly better. The grades were pooled from ranked lists, which favours the list. Two choices were measured, and both reversed the first guess:
   - **Opening by score beat opening by value per line.** Opened recall at 120 and 200 lines was 0.85 and 0.92 with no cost weighting, against 0.79 and 0.90 with cost to the power 0.5.
   - **Counting quiet sections on the parent's line beat giving each a line.** Opened recall at 60 lines was 0.32 with a line per section, 0.71 counting sections without hits, and 0.90 counting sections without a top passage too.

   The tiers are ranks, so a query that nothing in scope answers still gets a "top 2%" ('zzqqxx' does, by meaning alone). The outline says so when no passage holds a query word. An absolute cosine floor isn't supported by measurement: over all texts the nearest passage to 15 off-topic queries was at distance 0.405 or more, while the median pilot query's tenth-nearest was 0.401. This is a question for `hybrid` too.

   **Judged whole, 2026-10-09.** Five judges each read one Au5 document whole and in order, then marked, for each of the 12 queries, what an agent must read (grade 2) and what would help (grade 1), without seeing the outline (`search/eval/outline-judgments/`, with each judge's notes). Four were fresh Claude agents; the EU Code went to Grok (Joseph's arch-expert agent), since Codex was out of usage. Gemini's second, independent reading of SB 53, for cross-family agreement, was still running when this was written. Scored on the committed outline (`outline-check --judgments`, recall weighted 3 for grade 2 and 1 for grade 1):

   | Lines | Outline opens | Outline flags (opens, or names as a folded section with hits) | List, same output lines | List, same source lines |
   |---|---|---|---|---|
   | 60 | 0.332 | 0.749 | 0.227 | 0.417 |
   | 120 | 0.544 | 0.749 | 0.353 | 0.606 |
   | 200 | 0.669 | 0.749 | 0.476 | 0.707 |

   The pilot's grades had made this look easier (0.898 opened at 60 lines), because they only covered passages some ranking had surfaced. The judges also marked what never uses the query's words. What the numbers show:
   - In the same output lines, structure lines included, the outline opens more than a list (0.33 against 0.23 at 60). Given as much source text as the outline opens, a list does slightly better.
   - What the outline is mostly for is the flags column. Joseph, 2026-10-09: the outline "is mostly for helping agents know what they *don't* know after having read the relevant parts". It flags 0.75 of what the judges marked, at every budget, and a list has nothing comparable. The rest sits in sections the outline names but counts as having no hits.
   - The unflagged quarter is a paraphrase problem in the ranking, not a folding problem. Flagged share by query: "humans can no longer shut down or correct the AI system" 0.40 (the documents say "reliably direct, modify, or shut down", "self-exfiltration", "rogue internal deployment"); "misalignment" 0.63; "loss of control" 0.67; but "whistleblower" and "serious incident", whose words the documents use, 0.94–1.0. The lexicon's term mappings were always the planned fix for this (§0).

   Faults the judges found in the scorer, not yet fixed:
   - A stretch counts as read if any passage in it opens, so a must-read chapter is credited by one paragraph.
   - A quote taken from a heading line can't be found again after a rebuild, since headings belong to no passage.
   - All documents share one budget; there is no per-document score.
   - The docstring says only grade 2 counts, but the code scores grade 1.

   Their notes also record where each document's headings mislead: IASR's glossary is under no heading, the Risk Report's Claim 5.3 has no heading marker, and AISI's chapter numbers are empty headings. On a short document with no strong match, the outline fills its lines with noise.

   Not yet measured, and the measure closest to the outline's purpose: an agent given the outline and a question chooses what to read, and the result is judged.

   Still to do: the outline as a verb of `source-search`; the scorer fixes, by someone other than the outline's author.

   Found along the way, for the chunker and ranking:
   - In IASR, the glossary entry "Reinforcement learning with verifiable rewards" has the path "Conclusion › The value of shared understanding", which splits the glossary in two.
   - In Anthropic's Risk Report, everything after "2.14 Claim 8", §§3–5 included, nests under it (326 passages).
   - The Risk Report's front-matter contents (L40–69) is indexed as body text, so it ranks high for "hazard".
   - IASR's Figure 2.1 data text ranks first for "hazard", above IASR's own definition.
9. The gold queries, now partly reframed by §12's evaluation idea, then `--eval` and tuning.
10. Grouping, `--history`, and the embedder bake-off.

## 12. Another shape for results: a folded outline (an open idea, 2026-10-09)

Joseph, after steps 1–3, doubting that gold queries can be written except over a few sources: "Essentially what we're trying to do is give us all the right intuition and relevant info from a set of sources without requiring you or a sub-agent to have to ingest the entire things into context first.... Another perspective we might use would be more like 'context prepping' -- where it's looking for line ranges within documents that the agent who uses it will want to look at most carefully and probably ingest. Like a very smart index/ToC table." His sketch was a document's outline with only the relevant branches unfolded, down to line ranges and their text, each passage with its heading context. He offered it "as a mental model and thought and brainstorm", not as a design ruling.

What the index already has for it: each passage's heading path (`src.passages.path`) and its offsets in `ref/canonical/KEY.md`, and every heading with its level, path and offsets (`src.headings`). Line numbers follow from the offsets, and they are what an agent's file reader takes. Heading coverage, measured 2026-10-09 over the 201 texts: 142 have at least one heading per page, 51 have between 0.3 and 1, 4 have fewer, and 4 short web pages have none. Where headings are sparse, page ranges would have to stand in for sections.

My lean, not yet tried:
- Every section stays on the screen. Unrelated sections are folded to a single line, with their length and how many weak hits they hold. A section the ranking misjudges then stays visible as a folded line that the reader can open. In a ranked list it would just be missing. (This is aspectus's rule, that a fold is shown with what it holds, applied to a document.)
- Unfolding is chosen by hit density within a section, under a line budget for the whole output, the way `aspectus --lines` works. Adjacent hits merge into one range. A definition of the query term is always unfolded.
- Each range carries both a line range, for reading now, and the usual anchor (key, PDF page, quote), for citing. Line numbers change whenever `bin/canonicalize` rebuilds a file, and the anchor does not.
- This would also change the evaluation. A reader who has read one document whole can say which of its sections matter for many questions at once, so the cost is one whole read per document rather than per query. The measure would be how many of those sections were unfolded within a given number of lines.

Joseph, continuing the same thought: a preparatory pass in which a Sonnet agent writes "one line summaries and tags … for the document hierarchy -- potentially all the way to table and paragraphs". The tags would mark things like "their definitive definition, or common frontmatter parts / bibliographies / abstracts & executive summaries", and together with the layout hierarchy they would be "allowed to influence the rankings". The summaries would do two things. They could rank: "if the summary ranks high in cosine space it is a more salient/intrinsic part of the passage itself which would get a boost from it". And in the outline they would sit between the matching parts, "[discusses …]", "to give additional *surrounding context*".

The size, measured 2026-10-09: 26,792 passages (25,518 distinct texts), 2.86 million words, 12,431 headings. The definitions detector's lowest tier, confidence 0.35, holds 987 detections. That tier includes the bold-label items, of which about a quarter were real definitions in a sample of 30.

My lean, not yet tried:
- A summary is our reading, not the source's words. It is shown in brackets as ours, never quoted and never cited. In ranking it may raise a passage but never exclude one, so a passage with a wrong summary still ranks on its own text.
- A model will summarise toward the familiar sense of a word, which is the flattening this project exists to catch. Two sources that mean different things by "catastrophic risk" may get the same summary. That is fine for finding passages and wrong as a reading of them, so translation (G4) works from the source's words. It also bears on the conflict-of-interest principle: Anthropic's documents would be summarised by an Anthropic model.
- Summaries and tags are cached like embeddings, keyed by model, prompt version and the sha of the node's text. A section's summary depends on its children's, so a change propagates upward only.
- The best first use may be the definitions: have the model judge the 987 low-confidence detections, which can be checked against a hand sample. Tagging abstracts and executive summaries, which the rules don't detect, is next. Summaries for every node come after that.

**The Au5 set** (Joseph's name, 2026-10-09: the "golden" sources for this discussion). These are the documents the outline view is first built and judged on, and the ones a reader would read whole for its evaluation. Asked which four sources mattered most if everything else were lost, I chose four, and they were the plan's G4 pilot set. That match is not independent agreement, since I had read the plan and my criterion, the four that overlap least, is close to its criterion, four very different sources. Joseph then asked for the source most important to AISI, which makes five:
- `bengio-2026-international`, IASR 2026: the widest picture of risks and evidence, with a 179-entry glossary and over 1,100 references;
- `eu-cop-2025-safety-security`, the EU Code's Safety & Security chapter: the developer-framework genre written as obligations, and the source of the loss-of-control formula that nine later documents use;
- `california-2025-sb53`: binding law with the densest definitions, copied into RAISE and into three companies' frameworks;
- `anthropic-2026-risk-report-aug`, Anthropic's August 2026 Risk Report: the only document in the catalog's main table in which a developer says how risky its own systems are now. The conflict-of-interest principle applies;
- `aisi-2025-frontier`, AISI's *Frontier AI Trends Report*: AISI's own measurements across the domains the other four discuss (agents, chemistry and biology, cyber, safeguards, loss of control, societal impacts). It is where the other four's claims can be set beside a government's test results.

The UK government's place for AI was the runner-up. The NRR leaves AI out of its 95 risks ("Chronic risks, such as antimicrobial resistance (AMR), impacts of artificial intelligence (AI), … are not included in this list"). Its other mentions of AI are mostly one repeated sentence about automating cyber-attacks, across its cyber risks. That points to the *Chronic Risks Analysis* (`cabinetoffice-2025-cra`), which has a section on the impacts of AI. Before checking, I had named the NRR, which the NRR's own text contradicts. The Trends Report's headings are uneven (findings set as headings, section numbers in their own headings), which makes it a useful hard case for the outline.

Found while checking that: `--all` matched word forms by substring, so "AI" also counted "rail" and "faith". It now follows Joseph's case and word-boundary convention (§7). The NRR has 33 occurrences of "AI", all of which `check-quote` confirms, and the CRA has 20 of "artificial intelligence". `'*hazard*'` gives the pilot's count for the NRR: 73 in body text and 6 in headings.

## 13. Files beside the index: the catalog, sets, the lock and canonical-meta

*Discussed with Joseph, 2026-10-09; not built yet. He proposed a `canonical-meta/<key>/` that `bin/canonicalize` never overwrites, and moving the catalog to yaml. The lock and sets built from catalog selectors were my suggestions, which he welcomed ("love the lock"; "love that idea"). The anchoring rule and the two dispositions below were my points, to which he replied "sounds good". The placement of the files is mine.*

The aim, in Joseph's words: "to make a lot more of the process part of the repo instead of part of the opaque (from the public's perspective, other than the schema) database -- so if someone clones it and has a legitimate way to populate their own relata / ref/canonical/ -- everything else would work as expected". So everything we write by hand or pay a model to write lives in files, and the database stays wholly derived (§4).

**The catalog moves to yaml: `catalog/sources.yaml`.** Each row keeps today's columns:
- Date, Code, Document, Kind, Tag, Set, Influence, and the basis note, which is prose;
- its keys, with the status tags as fields.

More fields can follow for the sets to select on (organisation, jurisdiction, genre), so "every company framework" or "everything Anthropic published" needs no list. `bin/corpus.py` is the one parser `bin/canonicalize` and the index share (§2), so it becomes a yaml reader and both follow.

My lean is that `source-catalog.md` is generated from the yaml, with a header saying so. The README's link and its readable tables then stay, and `relata emit bib`, which reads the `@key`s through `bib/src/source-catalog.md` (a symlink), keeps working unchanged. The conversion is a script, checked by regenerating the markdown and diffing it against today's. Other sessions edit the catalog (the canonicalize session among them), so the switch needs a moment when no one else is.

**Sets: `catalog/sets/*.yaml`** (§7.2).

**The lock: `ref/canonical.lock`, written by `bin/canonicalize`, committed.** (Joseph: "love the lock.") It is a lockfile in the package-manager sense: the catalog says what we want, and the lock records exactly what was built. Per key, it records:
- the sha256 of the PDF;
- the sha256 of the markdown the text was built from (relata's conversion or a `canon-text` file);
- the sha256 of the canonical text;
- the canonicalizer's source hash.

Canonicalize already writes the first two into each `pages.json` (`pdf_sha256`, `markdown_sha256`); the last two would be new. The lock is what the committed sidecar data below anchors to. Someone who builds their own `ref/canonical/` can compare it document by document, and see where our overrides and summaries describe the same text as theirs.

**`ref/canonical-meta/<key>/`, never written by `bin/canonicalize`.** (The existing sidecar, `ref/canonical/msc/<key>/`, is rewritten on every run: marker's images and metadata, the conversion log, `pages.json`.) It holds:
1. chunking intermediates;
2. chunking and indexing overrides and one-off fixes;
3. labels and tags;
4. summaries (§12);
5. anything else better kept as a file than in the database.

Several hand fixes now live in code and would become per-source data here:
- `SECTION_PATTERNS` in `search/srcsearch/chunk.py`;
- `INLINE` in `search/srcsearch/defs.py`;
- `SKIP_REASON` in `bin/canonicalize`;
- the OCR "Al" fix in `bin/corpus.py`.

Three rules:
- **Anchoring.** An entry is keyed by the sha256 of its node's normalised text and the node's heading path, never by line numbers or offsets, which change whenever a text is rebuilt. An unchanged section keeps its summary across rebuilds. An entry whose text has changed is reported as stale, never dropped silently. This is the embedding cache's rule (§4) applied to our own writing.
- **Two dispositions.** Our own words (overrides, tags, summaries) are committed and public, quoting the source briefly at most. Intermediates that contain the source's text are git-ignored, like `ref/canonical/`.
- **Format:** yaml, to match the catalog. udon is the alternative, matching the lexicon. Joseph named yaml, udon and markdown as all acceptable.

`bin/source-index` reads all of these as inputs, and each gets a fingerprint like the canonical text's (§4), so a changed summary or override redoes only what depends on it. Nothing watches the files. Reconciling is a run of `bin/source-index`, as now.
