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

Semantic and lexical stay two rankings, fused by reciprocal rank fusion (RRF): each passage scores `1/(60 + rank)` from each side, summed, so a passage that is best on either side floats up. Memorata's `mix` (the geometric mean of the two rank positions) stays selectable; the pilot found RRF better with priors (§0), and Joseph chose it as the default. Lexical evidence (exact form, stemmed, phrase, proximity, density) is folded into one lexical score so nothing is counted twice. Memorata's proximity and density functions carry over nearly unchanged; they are careful work (exact versus inflected, query order, sentence and paragraph distance).

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

```
bin/source-search 'hazard'                      ranked: definitions of the term first, then usage
bin/source-search --defs hazard                 every definition of "hazard", grouped by source, active first
bin/source-search --all hazard                  every occurrence: counts by document and word form, then keyword-in-context lines
bin/source-search 'loss of control' --by source grouped by document (also: org, family, lineage)
bin/source-search 'severe harm' --in oai-pf oai-fgf     narrowed to documents, catalog codes, organisations or families
bin/source-search 'frontier developer' --history        superseded versions unfolded in lineage order
bin/source-search … --explain                    the per-factor score behind each result
bin/source-search … --json                       for agents; automatic when piped
```

Every result carries an anchor in the plan's form (plan §3.5, Claude's proposal, endorsed by Joseph 2026-10-09): relata key, physical PDF page, printed page, and the exact quote. This is a requirement, not a default. Joseph, 2026-10-09: "the search results should always come back with your preferred reference format -- key + pdf-page etc. etc." Every mode, `--all` and `--defs` included, and the JSON, carry it, with a "check against the PDF" flag where the source's fidelity mark calls for it. A quote copied from a result can then be cited as it stands, and checked with `bin/check-quote`, which takes anchors in bulk on stdin (`--batch -`).

`--all` matches word forms by substring, never by stemming alone, so it catches `hazard`, `hazards`, `hazardous`, and also `infohazard` and `biohazards`, which a list of forms would miss (pilot §6). It counts headings, and counts references separately, and it never matches inside link targets. It prints which forms it matched and how many of each, so "did we catch them all" has a checkable answer, including what the pattern didn't cover.

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

## 11. Build order

1. Schema, catalog reader, chunker and definitions detector, with no embeddings yet. Check by reading the chunk and definition output for SB 53, the AI Act, IASR 2026 and one OCR'd source. *Built 2026-10-09* (`bin/source-index`, `search/srcsearch/`, `search/schema.sql`); what the reading found is in §5.5. The reconcile part of step 2 came with it: a full build of the 201 texts takes about 20 s, and a second run changes nothing (0.1 s).
2. Reconcile and embed, with the cache; run twice to show the second run does nothing; touch one canonical file and show only it changes. *Built 2026-10-09.* bge-m3 embedded all 26,617 distinct passage inputs in 12 min 18 s, with relata's queue paused; a rerun embeds nothing. Batches commit as they go, so a stopped run resumes. (The first attempt held its opening read transaction for the whole run, so nothing committed until the end and a concurrent `--rebuild` waited on its locks; the read is now committed before embedding starts.) Changing one canonical file (NVIDIA's, by one byte, then restored) re-chunked that document alone in 0.2 s, and the next run changed nothing; a change to the chunker's own source re-chunks all 201 (about 35 s) and re-embeds only passages whose text changed. `bin/source-index --dry-run` lists what a run would redo.
3. Search: ranked, `--defs`, `--all`, `--explain`, `--json`. *Built 2026-10-09* (`bin/source-search`), with `--in` and `--verify` (runs every anchor through `bin/check-quote`). Checked two ways:
   - **Against the pilot's blind grades**, narrowed to its 10 sources (`search/eval/pilot-check`): nDCG@10 0.776 with RRF and the priors, against the pilot's 0.786; mix 0.724, lexical alone 0.702. That is the pilot's ordering, and the gap to the pilot is within the noise it warned of (±0.05 on 16 queries). The priors the pilot didn't test (Influence, recency, superseded, restored text) add 0.02 on this set: noise-level, and not harmful. Scoring a built passage against a quote the pilot graded needs a tolerant match (80% of the quote's letters in one run), since the pilot cut passages differently and kept footnote markers.
   - **Anchors**, run through `check-quote` for the pilot's 16 queries over the whole corpus: ranked, 156 of 160 ok; `--defs`, 239 of 241 ok. The six others are one SaferAI page that quotes the same sentence two or four times, and their anchors say the quote isn't unique on its page. `--all` (about 32,300 anchors, since it quotes every occurrence) about 96% ok; most of the rest are table and contents-page text, whose order in the PDF's text layer differs from the canonical text's, so `check-quote` can't confirm the page from the PDF (673 "unconfirmed"), and IASR's web-only text, which isn't in the PDF and is flagged so (106). Quotes keep footnote markers and citation link texts ("including7 the", "(Illinois House Bill 5116 2024)"), which the indexed text drops: `check-quote` matches them. Quotes are widened until unique on their page, counted the way `check-quote` counts (letters only, so SB 53's "(e) 'Frontier developer' has the meaning …" also matches inside "(f) 'Large frontier developer' has the meaning …"), and kept clear of "[…]" and "...", which `check-quote` reads as gaps. Where a passage is genuinely repeated on its page (SaferAI quotes the same OpenAI sentence four times on p. 202), the anchor says so.
   - Ranked search takes 1–2 s, most of it loading bge-m3 for the query; `--defs` and `--all --counts` well under a second.
4. The gold queries, with Joseph, then `--eval`, then tuning.
5. Grouping, `--history`, and the embedder bake-off.

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
