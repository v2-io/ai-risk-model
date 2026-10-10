# Spike: why source-search misses what careful readers say matters (2026-10-10)

*Claude (Opus 5.5), at the request of ai-risk-model-61, for Joseph. Read `debrief.md` first; `proposed-changes.md` has the suggestions. Nothing outside this directory was changed.*

The question: `source-search outline` flags about three quarters of what whole-document judges marked (`search/eval/outline-judgments/`). Where does the other quarter come from, and what would fix it?

The answer in one paragraph: little of it is reachable by re-weighting today's features, swapping embedders, changing the embedding input or the stop list (each ±0.02). Most of it is linked to the query by domain knowledge rather than by similarity: conceptual neighbours (about 37%, estimated) more than rewordings (about 26%). Knowledge supplied from outside the similarity computation recovers it. Blind query expansion gives +0.025 to +0.050, model-written document tags +0.068, and both together +0.118 (flagged 0.752 → 0.870, must-read 0.849 → 0.959), with caveats in the debrief.

## Files

| Path | What it is |
|---|---|
| `debrief.md` | findings, with tiers, for Joseph and the coordinating session |
| `proposed-changes.md` | suggested changes to the tool, the plan and the evaluation |
| `runs/` | every run's output, named by what it measured; `classification.tsv` is my category for each unflagged stretch; `blind-expansions.json` is the blind expander's lists |
| `tagging/tags-*.json` | the Sonnet taggers' concept tags for every Au5 passage, by passage id (our words; the input batches hold source text and are git-ignored) |
| `code/` | the scripts (below) |
| `cache/` | re-embedded vectors (git-ignored; rebuilt by `code/reembed.py`) |

## Rerunning

All scripts read `search/` code and the `airisk_sources` database and write only here. Run from this directory. The database must be as of commit `fafaa73`'s index, since passage ids are keys throughout.

1. `python3 code/build_table.py`: the per-query, per-passage table (`runs/table.pkl`). Everything else reads it.
2. `python3 code/decompose.py 188`, `code/curves.py`, `code/section_measure.py`, `code/structure.py`, `code/judges.py`: the decomposition and the measure's properties.
3. `python3 code/fit_lr.py`: Fable's logistic fit (RANKING §8.7).
4. `python3 code/reembed.py bge-m3`, then `code/emb_variants.py bge-m3`. Other models are `reembed.py MODEL full`, then `emb_variants.py MODEL`.
5. `python3 code/parsing.py`: stop-list variants.
6. `python3 code/expansion.py`: blind query expansion (needs `runs/blind-expansions.json`; writes `runs/expansion-scores.pkl`).
7. `python3 code/tags_eval.py`, `code/tags_controls.py`: document-side tags (needs `tagging/tags-*.json`).
8. `python3 code/by_category.py`: what each remedy recovers, by category.
9. `python3 code/outline_with.py today|exp|tags|exp+tags`: `outline-check`'s own scoring with a remedy's ranking substituted.

`code/rescore.py` rebuilds today's hybrid from the table with parts swapped. It reproduces today's 0.752 exactly, and `outline_with.py today` reproduces `outline-check`'s table.
