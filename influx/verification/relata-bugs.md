# relata: issues found on 2026-09-27

*By the academic/NGO verification agent, while filing sources for the AISI risk-factor report. The shared data dir is `/Users/josephwecker-v2/.local/share/relata`. Several agents were ingesting concurrently. Times are UTC, from `relata log`.*

These are ordered by how much damage each can do in a multi-agent setting. Issue 1 is the real one. Issue 2 is a design gap it exposed. I first reported issue 2 to the coordinator as a mis-identification. It isn't; see the note there.

---

## 1. `relata ingest --retry <file>` ignores the file argument and re-assesses the whole needs-review queue

**What I ran.** The cwd was `/Users/josephwecker-v2/src/aisi-eoi`. The file had been staged into the spool earlier, by `relata ingest --keep cset-ai-accidents.pdf fli-w25-full.pdf fli-s26-full.pdf`, run from a scratch directory, and it had parked as needs-review. I had then added a proper entry (`relata add arnold-2021-ai-accidents`, BibTeX on stdin, with its DataCite DOI 10.51593/20200072). I wanted relata to re-assess *that one file* so it could see the new entry:

```
$ relata ingest --retry cset-ai-accidents.pdf
file not found: cset-ai-accidents.pdf
retry: re-staged 25 needs-review item(s) for re-assessment
```

(I didn't capture the exit code; my shell pipeline masked it.)

**What happened.**
- The argument was resolved against the cwd, not against the spool, where the file lived as `ingest/cset-ai-accidents.pdf.needs-review`. It wasn't found.
- Instead of stopping, the command went on to a **global** retry. It renamed every `X.needs-review` in `ingest/` back to bare `X`, keeping its `.needs-review.json` / `.needs-review.md` sidecars. That was 25 items, most belonging to other agents or older sessions (active-inference papers, geoscience PDFs, `Pearl_2009_Causality.pdf`, `rules-of-order.pdf`, …).
- Re-staged items no longer show in `relata pending`, so their owners lose sight of them.
- The next `relata ingest` by *anyone* drains them, even an ingest of an unrelated file. The spool walk covers everything, as the `skipped=363` counts show. The re-assessment then **changes verdicts** for some items: `relata ingest --dry-run` immediately afterwards showed six items going from parked to auto-processed:

```
  processed  1-s2.0-S2405844017304966-main.pdf  — §11.19 WOULD AUTO-CREATE a new entry from the verified crossref record and attach this pdf — 2017 A multi-resolution HEALPix data structure for spherically mapped point data
  processed  aguilera-2022-how-particular-fep.pdf  — §11.19 WOULD AUTO-CREATE a new entry from the verified arxiv record and attach this pdf — 2021 How particular is the physics of the free energy principle?
  processed  coatleven-2024-large.pdf  — §11.19 WOULD AUTO-ATTACH to `coatleven-2024-large` (identifier-grade: doi-exact, filename-author+year, doi-position(masthead-primary), record-agrees:firstauthor+year(±1); posterior 1.0).
  processed  dacosta-2020-active-inference-discrete.pdf  — §11.19 WOULD AUTO-CREATE a new entry from the verified arxiv record and attach this pdf — 2019 A Short Survey on Probabilistic Reinforcement Learning
  processed  f000200_9780262369978.pdf  — §11.19 WOULD AUTO-CREATE a new entry from the verified crossref record and attach this pdf — 2022 Active Inference
  processed  sajid-2021-active-inference-demystified.pdf  — §11.19 WOULD AUTO-CREATE a new entry from the verified arxiv record and attach this pdf — 2019 Learning to Learn and Predict: A Meta-Learning Approach for Multi-Label Classification
promoted=0 rejected=0 needs-review=19 skipped=363 skipped-nonbib=0 processed=6
```

**What I did.** I didn't drain. I renamed exactly the 25 bare files that had `.needs-review.md` sidecars back to `X.needs-review`, the inverse of what the retry did. `relata pending` showed 25 needs-review again, and `relata ingest --dry-run` reported `processed=0`.

**It then reproduced independently.** At 21:50:58Z another agent (the log doesn't record who) imported `bengio-2025-iasr-key-update-1`, `bengio-2025-iasr-key-update-2` and `buhl-2025-emerging`. At 21:51:18–36Z a full re-assessment ran. It attached those three "identifier-grade", re-parked nine other items, and **auto-filed the same six** shown above. That fits the same workflow: import an entry, then `--retry` to get a parked PDF attached to it. The workflow is natural enough that other agents will keep reaching for it.

**Suggested fixes (my guesses; you know the design):**
- Resolve `--retry` file arguments against spool names, the way `decide <file>` already does.
- If a named file isn't found, exit non-zero **before** any re-staging.
- Scope `--retry` to the named files, and make a global retry require an explicit flag such as `--retry --all`.
- Consider having re-assessment of other people's items stay "park-only" unless run on a TTY, or at least print the verdict changes (parked → auto) prominently.
- A lighter alternative for my actual need: after `relata add`, let `decide <file> --choose attach:<key>` be the advertised path. It works, and I used it successfully afterwards, but a non-TTY caller only discovers it from `--help` text, because the JSON choices list doesn't offer `attach:<key>` when the entry didn't exist at ingest time.

---

## 2. Verdicts flip between first pass and retry, and the auto path hides filename-vs-content conflicts

**Correction first.** I told the coordinator that two of the six would be "wrong entries". I judged that from the filenames. Opening the stored PDFs shows **relata identified the contents correctly. The files were mislabeled downloads**:

| Spool file (name asserts…) | Content actually is | Entry auto-created at 21:51:31Z / 21:51:35Z |
|---|---|---|
| `dacosta-2020-active-inference-discrete.pdf` (Da Costa et al. 2020, existing entry `costa-2020-active`, DOI 10.1016/j.jmp.2020.102447) | Russel, "A Short Survey on Probabilistic Reinforcement Learning", arXiv:1901.07010v1 (title page) | `russel-2019-short` |
| `sajid-2021-active-inference-demystified.pdf` (Sajid et al. 2021, existing entry `sajid-2021-active`, DOI 10.1162/neco_a_01357) | Wu, Xiong & Wang, "Learning to Learn and Predict…", arXiv:1909.04176v1 | `wu-2019-learning` |

**The actual issues:**

(a) **The same bytes get different verdicts on the first pass and on retry, with no new evidence about that item.** The first-pass memos, as `relata pending` showed after my restore:
```
dacosta-2020-active-inference-discrete.pdf  needs-review  ambiguous: best candidate `costa-2020-active` at posterior 0.8699 (below τ, or a standing refutation — §7.3 soft-veto)…
sajid-2021-active-inference-demystified.pdf needs-review  ambiguous: best candidate `wu-he-2018-groupnorm` at posterior 0.9478 (below τ, or a standing refutation — §7.3 soft-veto)…
```
On retry the verdicts were: `AUTO-CREATED russel-2019-short … (consistency check: {posterior: 0.9964, factors: ["doi-position(masthead-primary)", "record-agrees:title-tokens-strong"]…})`, and the same shape for `wu-2019-learning`. The first pass apparently weighed the filename's author+year toward the existing entry and parked. The retry apparently didn't, or the soft-veto didn't survive. Whichever pass is "right", a retry that silently discards a standing refutation is surprising.

(b) **A filename-vs-content conflict is exactly what a human should see, and the auto path never surfaces it.** Someone saved the file as Da Costa 2020 because they wanted Da Costa 2020. After auto-creation, the owner gets an unwanted `russel-2019-short`, their `costa-2020-active` still has no PDF, and nothing tells them their download was wrong. A possible rule: when filename-author+year points at an existing entry and the masthead identifier points elsewhere, park with a headline like "file name suggests `costa-2020-active`; contents are arXiv 1901.07010 — mislabeled download?", even at identifier-grade.

(c) **A duplicate was auto-created** in the same run. `f000200_9780262369978.pdf` became a new entry `parr-2022-active-inference` (DOI 10.7551/mitpress/12441.001.0001, posterior 0.9941). But `parr-2022-active`, "Active Inference: The Free Energy Principle in Mind, Brain, and Behavior", MIT Press 2022 with no DOI recorded, is the same book. The attached PDF is 8 pages, "a portion of the eBook" (front matter). The identifier-grade path evidently checks identifiers but not title/author/year against existing entries that lack an identifier. `relata possible-duplicates --key parr-2022-active-inference` does list both. `relata possible-duplicates --author parr --year 2022` returned "no possible duplicates found", which may be a separate small bug in `--author` matching.

**Library state left for an owner's decision.** I didn't change any of it: merge the two parr entries; keep or remove `russel-2019-short` and `wu-2019-learning`; fetch the real Da Costa 2020 and Sajid 2021 PDFs. The other three auto-filed items are correct: `youngren-2017-multi`, `aguilera-2021-particular`, and the attach to `coatleven-2024-large`.

---

## Safe reproduction (not run; offered as a sketch)

With a throwaway `RELATA_DATA_DIR`: ingest two PDFs that park as needs-review; `cd` elsewhere; run `relata ingest --retry <first-file-name>`. You should see `file not found` followed by `re-staged 2 needs-review item(s)`, with both items gone from `relata pending`.
