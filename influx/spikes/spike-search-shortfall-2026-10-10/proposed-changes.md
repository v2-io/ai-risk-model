# Proposed changes, from the shortfall spike

*Suggestions, not edits. Nothing in `search/`, `bin/` or the database was changed. Each item gives its evidence and tier (see `debrief.md`), and what would make it wrong.*

## To the tool

1. **Fix the slash tokenization** (H-Q5). Postgres reads "Misalignment/Instrumental" or "chemical/biological" as one `file` token, invisible to BM25. 4,748 passages in 393 texts are affected (measured).
   - One way: index a copy of the text with `/` between word characters replaced by ` / ` (generated columns from a normalised text, or a custom parser).
   - Evidence that it matters for ranking: one judged stretch (estimated); for correctness, many.
   - Wrong if: some slash tokens should stay whole (URLs are already stripped from indexed text, per DESIGN §5.2; `ISO/IEC` would split, which seems harmless).

2. **Add document-side concept tags as their own ranking legs**, behind a flag first. That means BM25 over tags and an embedding of the tags, each fused like today's legs, not folded into the passage's vector.
   - Measured on Au5: +0.068 (+0.030 to +0.107) alone; +0.118 with query expansion matched against them; the outline's opened recall at 200 lines 0.653 → 0.774. A no-knowledge control gives nothing.
   - DESIGN §12 and §13 already have the storage (`ref/canonical-meta/<key>/`, anchored by text sha) and the caveats: tags are our reading, shown as ours, may raise a passage and never exclude one.
   - Before building:
     - a bare-prompt tagging control, since my brief told the taggers the purpose (upper-bound caveat);
     - a tagger from another family on a subset;
     - a decision on vocabulary. Free tags drifted between batches ("sandbagging" vs "underperformance on evaluations"). Tags drawn from the lexicon's terms would let query and document meet exactly, and would make the tags a first form of the translated editions (DESIGN §9).
   - Who writes them: the source experts are natural taggers for their own sources; a batch model call per passage is the cheap path (about 50M tokens corpus-wide at the agent rate measured here, much less batched; estimated).
   - Wrong if: the bare-prompt control or a cross-family tagger loses most of the gain. Then the gain was the framing or shared priors.

3. **Expansion through the lexicon (H-Q8) should include relations, not only equivalences.**
   - Blind model-written expansions measured +0.025 to +0.050. Neighbours (related concepts) helped as much as rephrasings, and the classification puts neighbours at 37% of the shortfall against rewordings' 26% (estimated).
   - The lexicon's broader/narrower/related relations and its per-source mappings are both expansion sources.
   - Keep each expansion visible in `--explain`, as H-Q8 already says.
   - Until the lexicon has mappings, a model-written expansion behind a flag (shown and attributable) would capture some of it now.
   - Wrong if: curated mappings turn out narrower than a model's free expansion and lose its neighbour coverage. Measure both.

4. **Compound word forms.** "cyber" should reach "cyberattack(s)", and "shut down" should reach "shutdown". Neither the stem leg nor `lexical`'s cap covers compounds. Small (3% of the shortfall, estimated), and a word-form hypothesis to register under H-Q7 rather than a patch.

5. **Cross-references inside a statute** as an outline feature, not a ranking factor. When an exact definition opens, name the defined terms it uses that the same document defines (from `src.definitions`), and any section that cites it. SB 53's "Property" and equity exclusion qualify "catastrophic risk" and were marked must-read or helps (estimated, 5%).

6. **Not worth doing for quality** (measured nulls; may still be worth doing for clarity):
   - stop-list changes (−0.001 to −0.012);
   - a full-scan semantic pool (+0.005);
   - dropping the title or path from the embedding input (±0.01);
   - swapping bge-m3 for another small embedder (±0.02, reshuffles).
   - H-Q1's two lists can still be unified for clarity.

## To the plan (RANKING §8)

7. **Put new evidence legs before the combiner rebuild.** The logistic fit on today's features doesn't help the outline's measure (measured: flagged 0.703–0.740 held out against today's 0.752). The combiner can be rebuilt for clarity at any time. It would have more to say after tags and expansion exist as features.

8. **Fit to the measure the tool is for.** Passage-level likelihood rose (AUC 0.866 → 0.88–0.89) while stretch-level flagged fell. If the combiner is a logistic model, weight each passage by its stretch's gain over the stretch's size, or fit a listwise objective. Otherwise the model is pulled toward the big stretches.

9. **Register updates** (for whoever maintains RANKING's register; my suggestions of status):

| Hypothesis | Suggested status |
|---|---|
| H-C1 | measured: 0.057 of judged gain has no candidate; widening the semantic pool to all passages recovers +0.005 |
| H-M2 | measured, null on flagged (±0.01), helpful for AUC (text only: 0.845 → 0.798) |
| H-Q1 | variants measured, null |
| H-Q5 | the slash `file` token found (item 1) |
| H-Q8 | estimated ceiling from blind expansions, +0.025 to +0.050 |
| H-F1 / §3.2 | §8.7's fit run; see item 7 |
| new, document-side tags (a Role- or Meaning-group hypothesis: "a passage tagged with the query's concept is more likely relevant") | measured as above, with its caveats |

## To the evaluation

10. **Report flagged beside its random baseline** (about 0.22 at 10% over Au5). Report must-read separately: the shortfall is mostly grade 1.

11. **Get a second judge per document where it matters.** On SB 53, a third or more of each judge's unflagged material was marked by that judge alone (measured). Grade-1 "context" items (11% of the shortfall, estimated) may not be retrieval targets at all.

12. **Get a second reader for the classification** (`runs/classification.tsv`), blind to mine, before "37% neighbours" is relied on.

13. **The cut is relative to the scope** (10% of 1,872 here). For queries with many relevant passages (misalignment: 276), it binds; for queries with few (hazard: 11), it admits noise. A calibrated probability (RANKING §3.2's argument) is where the logistic model earns its keep: a floor, not a reweighting.
