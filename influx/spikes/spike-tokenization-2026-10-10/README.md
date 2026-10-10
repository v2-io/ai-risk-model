# Spike: where the search index cuts text into words wrongly (2026-10-10)

*Claude (Opus 5.5), at the request of ai-risk-model-61, for Joseph. Nothing outside this directory was changed. The live database `airisk_sources` was only read; all writes went to a pg_dump copy, `airisk_tokspike`.*

The question (Joseph, via ai-risk-model-61): the shortfall spike found that Postgres reads "chemical/biological" as one token, so BM25 never sees either word. "Make sure there aren't other ones that might surprise us later while you (or the delegated agent) are at it ('%'?)".

**The answer in one paragraph.** The slash case is one of about a dozen. Today, 144,215 (passage, word) pairs are words a reader can see in a passage but that a search for that word can't find there. They span 28,495 passages (46% of the index). That's 22,652 pairs if only words of three or more letters are counted, in 9,022 passages (measured).

The cause isn't one rule but a mismatch between two definitions of a word:
- **Index side.** Postgres's parser glues words into one token across `/`, `.`, `@` and a hyphen before a digit ("chemical/biological", "U.S", "Z.ai", "espionage.144", "2024-2025" read as `2024` and `-2025`, "4.5", "§22757.11").
- **Query side.** The query side (`text.WORD_RE`) splits at exactly those characters, so no query can ever produce those tokens.
- **Accents.** On top of that, queries are accent-folded and the index isn't, so "Schölkopf" can't be found even typed exactly.

"%" itself is harmless: it's a separator on both sides.

The proposed fix is one definition used everywhere: **a word is a run of letters and digits, folded as a query is folded; every other character separates.** It is a SQL function, `src.index_form`, that both the tsvector columns and every query go through, plus the matching one-line change to `text.WORD_RE`. It brings the unfindable pairs from 144,215 to 104, and the 104 are math notation, hex hashes and pieces of a few names. It passes 52 of 52 fixtures, against 7 of 52 today. It leaves the outline and pilot measures where they were (flagged 0.752 → 0.753, experts 0.710 → 0.710, pilot nDCG@10 0.802 → 0.802), because those instruments' queries barely touch the affected words (§4.3). It's in `proposed.patch`, tested through a real `bin/source-index --rebuild` on the copy.

## 1. What the tokenizer does that a reader wouldn't expect

**How this was measured.** Every token Postgres's default parser emits over all 61,559 passages, 14.0M including blanks, was classified by shape (`code/census.sql`, output `runs/census.txt`). A word counts as *unfindable* in a passage when it is visible there (a maximal run of letters and digits) but a query for that word alone, cut by today's query path, gives a lexeme the passage's `tsv_exact` doesn't hold.

| class | what the parser does | example | tokens | passages | unfindable pairs (3+ letters / all) |
|---|---|---|---|---|---|
| A slash-joined words | one `file` token | "and/or" ×1,220, "ISO/IEC" ×270, "chemical/biological", "threats/risks", "safety/security", "Misalignment/Instrumental" | 7,898 | 5,002 | 7,058 / 8,378 |
| B slash-joined numbers | one `file` token | "2024/1689" (AI Act), "04/29/2022", "24/7" | 2,431 | 941 | 0 / 3,104 |
| C dotted abbreviations | one `file` token | "e.g" ×7,282, "i.e", "U.S" ×1,082, "U.K", "Ph.D" | 11,737 | 7,813 | 79 / 15,473 |
| D domains and dotted names | one `host` token | "Z.ai" ×555, "x.AI" ×254, "Claude.ai", "OECD.AI", "Character.AI", "GOV.UK", "openai.com" | 2,323 | 1,576 | 1,868 / 2,884 |
| E1 sentences run together | one `host` token | "knowledge.These", "phases.The", "risks.This" | 103 | 89 | 100 / 109 |
| E2 footnote number after a period | one `file`/`host` token | "espionage.144", "mitigation.54", "behaviors.47" | 1,297 | 777 | 654 / 1,984 |
| E3 code identifiers | one token | "sys.exit", "re.search", "pwn.college" | 423 | 232 | 385 / 433 |
| F labelled numbers | one `file` token | "A.1", "C.2", "v1.0", "V3.1" | 3,535 | 1,715 | 3 / 4,014 |
| I dotted section numbers | one `version` token | "5.7.1", "2.2.1" | 3,797 | 1,845 | 0 / 5,244 |
| J decimals | one `float` token | "4.5", "22757.11", "0.05" | 74,540 | 11,974 | 0 / 63,108 |
| K hyphen before digits | a *signed* integer | "2024-2025" → `2024`, `-2025`; "COVID-19" → `covid`, `-19`; "RSP-2025" | 28,084 | 7,374 | 0 / 14,253 |
| O model names with a decimal | signed float and int | "Llama-3.1-70B" → `llama`, `-3.1`, `-70`, `b` | 325 | 171 | 78 / 549 |
| G filenames, H arXiv categories, M URLs, emails, paths | one token each | "validate_results.py", "cs.CL", "arxiv.org/abs/…", "startup/shutdown/re-startup" | 11,779 | 4,833 | 8,929 / 19,465 |
| N tags and entities | dropped (no mapping in `simple` or `english`) | literal "<sup>" ×476, "R&D;" → `r` | 491 | 292 | 294 / 299 |
| L scientific notation | one `sfloat` | "1e26", "5e-05" | 150 | 64 | 0 / 91 |
| P accents and ligatures | index keeps them, query folds them | "Schölkopf", "Université de Montréal", "naïve", "ﬁles", "Scientiﬁc" | — | — | 3,192 / 3,492 (2,270 passages) |
| total | | | | | 22,652 / 144,215 (28,495 passages) |

**Counting slash joins.** The shortfall spike counted 4,748 passages with slash joins, and its verifier counted 6,047 with `[A-Za-z]{2,}/[A-Za-z]{2,}`. Mine is different again: 5,002 passages have a letters-only `file` token, and 3,383 lose a word of 3+ letters they don't hold anywhere else. Slashes also hide words inside path-like tokens counted under M ("self-preservation/shutdown-resistance" hides "shutdown").

**The query side.** Today's query path is `parse` → `text.words` → `to_tsvector`. Since `text.words` cuts at `/ . @`, no query can produce a token from A–J, L, M or O. "ISO/IEC 42001", "U.S. government", "Z.ai", "Regulation (EU) 2024/1689" and "Section 22757.11", typed exactly as the source writes them, all fail to reach the passages that hold them (`runs/fixtures-today.txt`). K is the exception: "COVID-19" typed with its hyphen gives `-19` on both sides and matches; "COVID 19" doesn't.

**Characters that are fine.** "50%", "$1B", "10^26", "≥50", "−5", the en dash, curly and straight apostrophes, and "1,000" all separate as a reader would expect (`fixtures/tokenization.json`). "%" is a separator on both sides; a search for "50" finds "50%".

**Things no index form can fix** (canonical text; worth the canonicalizer's list):

| what | where | effect |
|---|---|---|
| footnote digit glued to a word | "misinformation77", "Damage68", "Allaire1", "8SaferAI": 1,404 occurrences in 728 passages of 178 sources | one run of letters and digits, so "misinformation" is unfindable there. It can't be split at the index without also splitting "python3", "Qwen3", "ResNet50". |
| superscripts lost | 22 passages, 14 sources | "10²⁶" indexes as `10`; the exponent is gone. The "10^13" → "1013" flattening (experts/findings-for-tools.md) is a worse form of the same thing; I didn't hunt for it. |
| Cyrillic look-alike letters | "Туре" ×34 in slattery-2026-risk and anwar-2026-decision-theoretic-formalisation | not "Type" to any search |
| line-break hyphenation | about 88 occurrences in 17 sources ("capabili- ties", "Dis- tribution", "inju- ry") | two fragments |
| converter debris around footnotes | "<sup>&</sup>lt;sup>4</sup>We" in ayonrinde-2025-evaluating-explanations-explanatory; literal `<sup>`/`</sup>` survive in 281 passages of 97 sources | "4We" is one word. `text.clean` removes tags before it unescapes entities, so an escaped tag comes back as a tag. |
| U+FFFD | 15 in one source | lost characters |

## 2. Which of these matter for search, and why

A hidden word matters when someone would search for it and the passage doesn't say it another way. The pair counts above already exclude passages that hold the word elsewhere.

- **Matters most: A (slash-joined words), D (organisation names), E1/E2 (prose words run together with a period or footnote), P (names and ligature words).** These are content words: 12,872 pairs of 3+ letters, in 6,639 passages (measured). Among them:
  - chemical/biological weapons and safety/security measures in Anthropic's RSPs;
  - IASR's Misalignment/Instrumental reasoning;
  - Z.ai and x.AI in the FLI index;
  - Claude.ai in RSP v1.0;
  - IASR's own "ﬁles" and "Scientiﬁc";
  - authors' names everywhere in reference lists.

  The lexicon work searches for exactly these: actors, risk categories, capabilities.
- **Matters for looking things up: B, F, I, J, K (numbers and labels).** Section and article numbers ("§22757.11", "Art. 3(3)" is fine, "Annex A.1"), regulation numbers ("2024/1689"), model versions ("Opus 4.5", "Llama-3.1-70B") and the second year of every range ("2024-2025") are unreachable from ranked search today. One by one these are less valuable to BM25 than content words (exact lookups belong to `exact-bytes`), but ranked search shouldn't be blind to them. Of the 94,889 digit pairs, most look like figure and table values and section numbers, which don't matter one by one (estimated from the most frequent).
- **Matters little: C's single letters ("u", "s", "e", "g"), G, H, M, N, L.** These are mostly reference-list and code debris ("cs.CL", "arxiv.org/abs", ".py"). The exception is a word inside a slash path ("startup/shutdown/re-startup"), which the fix recovers anyway.

## 3. The proposed fix

**The rule.** A word is a run of letters and digits, folded (accents and ligatures) as `text.fold` already folds a query. Every other character separates. One SQL function states it:

```sql
create function src.index_form(t text) returns text language sql immutable parallel safe as
$$ select regexp_replace(public.unaccent('public.unaccent'::regdictionary, t), '[^[:alnum:]]+', ' ', 'g') $$;
```

`tsv_exact`, `tsv_stem`, `tsv_head` and `src.headings.tsv` are generated through it. `rank.py` passes every query through it: `_lexemes`, and the phrase, heading and answerability tsqueries. `text.WORD_RE` becomes `[^\W_]+`, so query words, `nwords` (BM25's length), duplicate hashes and anchors cut words the same way. The whole change is `proposed.patch`: 107 lines across `search/schema.sql`, `search/srcsearch/text.py` and `search/srcsearch/rank.py`.

**Why I think it's the principled version, not a patch per class.**
- **One definition, and it's the one the tool already states elsewhere.** The literal matcher (DESIGN §7.1) reads a phrase as words separated by "any run of non-alphanumerics" ("loss-of-control" is three words), and `rank._TOK`, proximity's tokenizer, is already `[^\W_]+`. This makes BM25, the query parser and `nwords` agree with them. H-Q5's three-way inconsistency goes away, except for apostrophes in the literal matcher (§5).
- **No prediction of the parser.** The alternative is a rule per token type ("split `file` tokens, keep `float`s, unsign ints after a letter…"), and the parser has many cases: "Llama-3.1-70B" gives a signed float and a signed int. With only letters, digits and spaces, the parser has nothing left to glue, so its behaviour is the same for every input.
- **It's checkable.** The invariant "every visible word is findable by itself" is a query (`code/invariant.sql`), and the fixtures test each class.
- **For any query without a hyphen, it only widens what's reachable.** Every lexeme such a query can produce today is still in the index under the fix. What the fix removes (`u.s`, `4.5`, `chemical/biological`, `-2025`) was never reachable from a query, so no passage a query reaches today stops being reached. A hyphenated query loses only its compound lexeme (below). Scores do change slightly: `nwords`, and df for words that are now visible in more passages.

**What it costs, and the decisions in it for Joseph:**
1. **Hyphen compounds stop being separate lexemes.** Today "loss-of-control" in a passage is indexed as `loss-of-control` plus its parts, and a query typed with the hyphen gets an extra term from the compound. Under the fix BM25 treats "loss-of-control" and "loss of control" alike, as the phrase factor already does. I also measured the alternative, **H** (`code/variants.sql`: keep a hyphen between two letters, so the parser keeps today's compound-and-parts). H and the proposal (**W**) are identical on every query without a hyphen between letters, by construction. Six eval queries have one ("non-malicious", "chain-of-thought" twice, "open-weight" twice, "real-world"), and the two forms differ on two of them:
   - the pilot's "non-malicious": 0.597 under W, 0.602 under H;
   - the experts' "…real-world capability": opened 0.41 under W and 0.27 under H at B=60, 0.55 and 0.59 at B=120, with flagged equal.

   I'd choose W for the single definition; the evidence doesn't decide it.
2. **Accent folding on both sides.** The query side already folds (`text.fold`), so the fix makes the index agree. The other consistent choice, folding neither, would make "Scholkopf" never find "Schölkopf". This needs the `unaccent` extension (contrib; one `create extension` line in schema.sql).
3. **Apostrophes separate.** H-Q5's hypothesis says "apostrophes inside a word kept", but BM25 has never done that: Postgres always split "AI's" into `ai`, `s`. The fix makes the split explicit everywhere outside the literal matcher. If the hypothesis is to hold instead, that's a different change (possessives would need handling, or "AI" wouldn't find "AI's").
4. **Decimals and section numbers split.** To BM25, "4.5" is now "4" then "5"; so are "4 5" and "4-5". To the phrase factor they already were. Precise lookups remain `exact-bytes`. Keeping digit-dot-digit whole would mean the query side has to keep it too. That's possible (a second regex), but it reintroduces a token type, and no fixture or eval asked for it.
5. **A rebuild renumbers passage ids.** The schema changes, so `bin/source-index --rebuild` is needed. It drops `src` and passage ids restart: live ids run 123671–185229, rebuilt 1–61559. Embeddings aren't redone (the cache is keyed by input, which doesn't change). Chunk boundaries don't move: all 61,559 passages are identical in (doc_key, ord, offsets, text, embed_sha), checked. So anything keyed by passage id needs remapping by (doc_key, ord), notably the shortfall spike's `tagging/tags-*.json` and `runs/table.pkl`. Any rebuild has this cost; this one just makes it due now.
6. **Duplicate grouping widens slightly.** `norm_sha` now treats "loss-of-control" and "loss of control" alike. Passages in duplicate groups go from 3,087 to 3,097 (measured).
7. Single-letter lexemes from abbreviations ("U.S" → `u`, `s`) have low idf. A query containing "U.S." already produces them today.

## 4. Measured before and after

### 4.1 The invariant (`runs/invariant.txt`)

| index | unfindable (passage, word) pairs | passages | of which words of 3+ letters |
|---|---|---|---|
| today | 144,215 | 28,495 | 22,652 |
| W (proposed) | 104 | 82 | 15 |
| H (hyphen compounds kept) | 104 | 82 | 15 |

What W leaves:
- math notation like "pˆ", "βˆ", "Rˆ": `unaccent` turns the modifier into "^", and the metric's split didn't re-apply the index form, so the search itself would find these;
- hex hashes beginning with digits-then-e;
- pieces of a few names ("Köpf", "Özcan") that the metric's splitter cuts differently from `unaccent`.

### 4.2 Fixtures (`fixtures/tokenization.json`, `code/check-fixtures.py`)

There are 26 *forms* (a string and the exact lexemes it should index to) and 26 *findable* cases. Each findable case is a query a reader might type, a passage that visibly holds its words, and a check that every query lexeme is in the passage's stored `tsv_exact`. Most are anchor sources (RSP v3.4, IASR, SB 53, the AI Act, the EU Code); one control is plain words.

| | passes |
|---|---|
| today (live `airisk_sources`, search/ code) | 7 of 52 (`runs/fixtures-today.txt`) |
| proposed.patch, after a real `--rebuild` of the copy | 52 of 52 (`runs/fixtures-rebuilt.txt`) |
| H | 49 of 52: the three forms where it keeps a compound, by design (`runs/fixtures-H.txt`) |

These are fixtures for H-Q5 only. They test whether a word can be matched, not how a passage ranks.

### 4.3 The instruments

The runs, in the order I made them, each with outline-check against the whole-document judges and against the experts, and pilot-check (`runs/LABEL-*.txt`):
- D0: today;
- Q: the query side alone, index unchanged;
- Wn: W with today's `nwords`;
- W, H;
- P: proposed.patch's code on W's columns;
- R: proposed.patch after `--rebuild`.

| run | judges: flagged (B=60) | judges: opened | experts: flagged | experts: opened | pilot nDCG@10 |
|---|---|---|---|---|---|
| D0 today | 0.752 | 0.332 | 0.710 | 0.552 | 0.802 |
| Q | 0.752 | 0.332 | 0.710 | 0.548 | 0.802 |
| Wn | 0.753 | 0.332 | 0.710 | 0.548 | 0.802 |
| W | 0.753 | 0.336 | 0.710 | 0.548 | 0.802 |
| H | 0.753 | 0.336 | 0.710 | 0.544 | 0.803 |
| R (proposed, rebuilt) | 0.753 | 0.336 | 0.710 | 0.548 | 0.802 |

`code/compare.py D0 R` gives the per-query changes. The one I expected: "misalignment" flagged rises 0.63 → 0.65 at every budget, which is IASR's Table 3.5, the shortfall spike's case. Otherwise a handful of rows move by about one stretch either way. "Opened" moves more than "flagged" because it's a budget allocation; for example the experts' "loss of control" opened goes 0.52 → 0.46 while flagged stays 0.67. I didn't trace those moves one by one. The `nwords` change accounts for "catastrophic risk" (experts) 0.55 → 0.53 and "how the severity…" 0.62 → 0.63 (`compare.py Wn W`).

**Why these instruments can't see the effect.** The 47 judged queries use 165 distinct words. Across all passages of the five judged documents, those words are unfindable in 28 (passage, word) pairs:
- "ai", only inside arXiv categories: 9;
- "evaluation": 4;
- chemical, biological, control, models: 2 each;
- misalignment, task, time, theft, "50" and "53" after a hyphen, and one more: 1 each.

So the instruments work as a regression guard here, and they show no regression. The gain is measured by the invariant and the fixtures. An eval that could see it would need queries about organisations, statutes, model versions and slash-paired categories, judged over documents that use those forms. The experts' held-out questions might be a place to look.

## 5. Other things found

- **Proximity and density ignore hyphenated query words today** (measured). `parse` keeps "loss-of-control" whole while `proximity_density` cuts the passage at hyphens, so they never match: proximity is None and density 0.0 for a passage that holds "loss-of-control", against 0.98 and 0.87 for the query "loss of control". The fix's `WORD_RE` change removes this.
- **Stop words leak into BM25 through hyphenated query words** today: "state-of-the-art" sends `of` and `the` (the `simple` configuration has no stop list). The fix removes this too.
- **Definitions have their own word rule (H-Q6).** `norm_term` keeps hyphens, and 435 of 4,030 defined terms have one. "red-teaming" is defined 7 times and "red teaming" separately, so the exact-match definition boost treats them as two terms. Making `norm_term` cut like `index_form` is one character in a regex, but I've left it out of the patch as a separate decision.
- **The literal matcher doesn't fold apostrophes or accents.** `exact-phrase "developer's"` misses "developer’s": 293 passages have a curly apostrophe between letters, against 15,690 with a straight one. "Montreal" misses "Montréal". That may be intended for the exact verbs; if not, it's H-Q5's other half.
- **For the chunker:** 72 passages in 39 sources contain no letter or digit. One is a table rule row, "|----…|--|---|", that `RULE_ROW_RE` misses because one cell has only two dashes. Others are lone punctuation and code fences. There is also the clean-order issue (tags removed before entities are unescaped) above.

## 6. Proposed text for RANKING.md H-Q5

> **H-Q5 Tokens.**
> - Feature: how q and p are cut into words.
> - Hypothesis: the unit of matching is a run of letters and digits, folded (accents, ligatures, case); every other character separates, hyphens, slashes, periods and apostrophes included. "loss-of-control" is three words, as the literal matcher reads it.
> - Encoding (from 2026-10-1x): `src.index_form` (schema.sql) for every tsvector and every query's tsquery; `text.WORD_RE` for query words, `nwords` and duplicate hashes; `rank._TOK` for proximity. The literal matcher agrees except that it keeps a typed apostrophe and doesn't fold.
> - Measured 2026-10-10 (influx/spikes/spike-tokenization-2026-10-10/): before, Postgres's parser glued words across `/ . @` and a hyphen before a digit, and the query side couldn't produce those tokens. That left 144,215 (passage, word) pairs unfindable in 28,495 passages; after, 104 (math notation, hashes). Fixtures: 52 of 52, against 7 before. outline-check and pilot-check unchanged within ±0.005 (they barely contain the affected words).
> - Open: hyphen compounds as extra lexemes (variant H, equal on the evals); apostrophes and folding in the literal matcher; whether `norm_term` (H-Q6) should cut words the same way.

## 7. What I didn't do

- I didn't change `search/`, `bin/` or the live database, per the brief. The patch is ready to apply.
- I didn't trace the outline's per-query "opened" moves (§4.3) one by one.
- I didn't measure query latency formally. The eval runs took about the same time before and after (about 40 s per variant). Single-letter and single-digit lexemes widen candidate sets for queries that contain them, as they already do today.
- I didn't hunt for "10^13 → 1013" flattenings or other numeric damage in the canonical texts beyond the counts in §1.
- No cross-family check.

## Applying it

From the repository root, after the expert session's comparison runs:
1. `git apply influx/spikes/spike-tokenization-2026-10-10/proposed.patch`
2. `bin/source-index --rebuild` (about a minute; no embedding). Then remap anything keyed by passage id by (doc_key, ord) (§3, item 5).
3. `python3 influx/spikes/spike-tokenization-2026-10-10/code/check-fixtures.py` should give 52 of 52. Run the evals as usual and expect `runs/R-*.txt`. The fixtures could move to `search/fixtures/` at that point.
4. Update RANKING.md H-Q5 (§6) and weights.toml's comment trail if wanted.
5. `dropdb-18 airisk_tokspike` frees about 4 GB. It currently holds the proposed index, rebuilt, plus my `tok` analysis tables.

## Files

| Path | What it is |
|---|---|
| `proposed.patch` | the fix: `search/schema.sql`, `search/srcsearch/text.py`, `search/srcsearch/rank.py` |
| `fixtures/tokenization.json` | H-Q5 fixtures: forms and findable cases, each with its class |
| `code/check-fixtures.py` | runs the fixtures against a database and a query path (read-only) |
| `code/census.sql` | the inventory (§1): token census, shape classes, unfindable pairs, glyph damage → `runs/census.txt` |
| `code/invariant.sql` | unfindable pairs for today, W and H → `runs/invariant.txt` |
| `code/variants.sql` | the index forms compared (Q identity, W proposed, H hyphen compounds kept) |
| `code/apply-variant.sh` | regenerates the scratch database's tsvector columns with one variant (only `airisk_tokspike`) |
| `code/experimental-srcsearch.patch`, `code/make-experimental.sh` | the query-side variant used for the Q/W/H/Wn runs; the script recreates it in `code/srcsearch/` (git-ignored) |
| `code/patched.py` | runs an eval script with a different `srcsearch` package (`SRCSEARCH_PARENT`, or the experimental one) |
| `code/evals.sh`, `code/compare.py` | the three instruments for one variant, and per-query differences between two |
| `runs/` | every run's output, named by variant: D0, Q, Wn, W, H, P, R; fixtures; census; invariant; the rebuild log |

## Rerunning

From the repository root:
1. `createdb-18 airisk_tokspike && pg_dump-18 airisk_sources | psql-18 -q -d airisk_tokspike`
2. `psql-18 -d airisk_tokspike -f influx/spikes/spike-tokenization-2026-10-10/code/census.sql`, then `code/invariant.sql`
3. `S=influx/spikes/spike-tokenization-2026-10-10; $S/code/evals.sh D0`
4. `$S/code/make-experimental.sh`, then for each variant v in q, w, h: `$S/code/apply-variant.sh v && $S/code/evals.sh V $S/code/patched.py` (`orig-nwords` as a second argument to apply-variant gives Wn)
5. For the proposed patch itself: apply it to a scratch tree (`git worktree` or a copy), then `AIRISK_SOURCES_DB=airisk_tokspike python3 TREE/bin/source-index --db airisk_tokspike --rebuild --no-embed`, then `SRCSEARCH_PARENT=TREE/search $S/code/evals.sh R $S/code/patched.py`
6. Fixtures: `python3 $S/code/check-fixtures.py` (today, live database, read-only), or `AIRISK_SOURCES_DB=airisk_tokspike python3 $S/code/patched.py $S/code/check-fixtures.py`

## On the brief

The brief was clear about the constraint and its reason (comparable expert runs), and that shaped the method well. It let me make a full copy of the database and test the real rebuild without touching anything shared. It also named where earlier evidence sat (debrief §5, de-novo-feedback-1, H-Q5, findings-for-tools), which saved time.

The one thing I'd add for a similar spike: name the instruments' blind spot up front as a possibility. I spent a little while confirming that outline-check couldn't see this before turning to fixtures. "Use them, or say why they can't see the effect" did leave room for that, and it was the right call.
