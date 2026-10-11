# Source segments: each source as a small verisectorium (a draft convention)

*Drafted 2026-10-10 by Claude (Opus 5.5, ai-risk-model-61) from a discussion with Joseph the same evening. Each point says whether it's **agreed** (Joseph's words quoted where they're the source), **proposed** (Claude's, not yet answered), or **open**. Nothing here is built. The pilot it proposes is SB 53.*

## 1. What it's for

Joseph, 2026-10-10, after the day's work on the search tool and the source experts:

> "[pdf] -> [naive canonical] ; [niave c.] + fixes (e.g., OCR, offsets, etc.) -> [high-fidelity canonical] … then we have the [hifi-canonical] (which is also the one chunked and embedded) + anchored sidecars … I almost wonder if it makes even more sense to have the hfc, instead of one big document …, *cut up into chunks with the chunks in their own file, with frontmatter & file-name affordances and probably an outline table for reassembling etc.-- "verisecting" them … ensuring that each segment tells exactly how to cite it … and sidecars just attach to the appropriate segment… Each segment, like in all verisectoria, gets to have its own working notes and markdown yaml frontmatter …-- each segment's working-notes is also the collector for issues that anyone uncovers with it-- the usual 'related: #..., #...' slugs in the frontmatter and dependency tree etc. etc. and also easy for us to then tie it into our lexicon *AND* our claims"

What it would fix, from what the day measured:
- **Identity that doesn't move under a rebuild.** Every sidecar today has to anchor by text hash and heading path (`search/DESIGN.md` §13), because line numbers and offsets change whenever `bin/canonicalize` rebuilds a text. The experts' gold judgments (`search/eval/expert-judgments/`) are keyed by passage ord, which changes on any re-chunk. And the tokenizer fix (`influx/spikes/spike-tokenization-2026-10-10/`) renumbers every passage id. A segment's slug is its identity, never its position (`def-atom` in `~/src/arch/firmatum/verisectorium/theory/src/`).
- **Findings at the grain they're found.** Nearly every fault the experts reported was about one passage: a footnote moved away from its marker, a lost article number, the digest's "internet use" (`experts/findings-for-tools.md`). Each would land in that segment's working notes.
- **Relations no tag or similarity can carry.** SB 53's equity exclusion (§22757.16) qualifies the catastrophic-risk definition without using its words. Both search tools missed it, and the shortfall spike counts such cross-references as about 5% of what the outline misses. Between segments, that's an edge.
- **One citable unit** for search results, claims, lexicon citations and gold judgments alike.

It serves the first two of Joseph's layers of truth (`CLAUDE.md`, "The truths it serves"): what the sources state, and what their authors intended.

## 2. The pipeline (agreed in outline)

1. **PDF → naive canonical**: today's `ref/canonical/KEY.md`.
2. **Naive → high-fidelity**: conversion faults fixed in one of two ways. Joseph: "either has generalized fixes to the canonicalizer itself that fix it + other current & future instances of that error, OR (relevant for here) -- *patch sidecars*/scripts that only apply to that single document."
3. **High-fidelity → segments.** After this step the segments are the authored source of truth for that source. Nothing regenerates them, so there's no build for their slugs to survive. A fix found later arrives as a patch to the segments it touches, located through each segment's original-page metadata.

**A per-source inbox** for issues not yet attributable to one segment (Joseph: "probably need an 'influx'/feedback.md or something per source as its own sidecar for issues to accumulate so that things aren't lost that the experts or someone can drain & integrate"). Drained into segment notes, into a canonicalizer fix, or into a patch.

## 3. The segment

**Grain (agreed).** A segment is one citable unit that fails as a whole: source fidelity at this stage; later, a definition that goes unused, an empirical claim that can be falsified. Joseph: "This is exactly the right way to set up a verisectorium-- one thing that is citable and a thing that fails in specific ways as a whole".
- **A rule of thumb** (Joseph): put into one segment "what you would usually want to see holistically as a source-search result". That is a distinct logical chunk. But "logical chunk" ≠ "actual chunk as embedded/vectorized": embedding may widen to neighbouring segments or their summaries. That is a separate decision, not taken here.
- **Whole lists and tables may be one segment** "until there is a later need to actually pull it apart-- for example to challenge a single claim of 7".
- **Splitting is normal** (Joseph): "it's not uncommon to end up splitting a segment for various reasons-- the slugs etc. are easily tracked and reconfigured as necessary."
- The SB 53 expert's gold notes reached the statutory case independently: split statutes on subdivision markers, so that each passage means one thing (`search/eval/expert-judgments/california-2025-sb53.notes.md`, finding 8).

**Slugs (agreed: lenient).** Joseph: "we should be pretty lenient about the slug names per source… What we don't need is to come up with a clever 3-word description of every single paragraph and bullet-point in the corpus and give it an ontological home. That's the beauty of this, it allows for organic and systemmatic incremental improvement and refinement with minimal impact radiuses."
- **Acceptable forms:** a positional name like `part-2.par-12`, to be split or renamed later; "even a guid or partial sha of the L1 quote"; meaningful names where the source supplies them (`22757.11-c`); hierarchy or namespaces where they help.
- **The estate's precedent** is the reverse of this use: in a verisectorium, order and grouping live in the outline, and the slug carries only identity (`~/src/arch/asf/01-aat-core/OUTLINE.md`; `form-slug-form-kinds`).

**Arrangement by the authors' logical intent (agreed, with a discipline).** Joseph: "we are under no obligation to recreate the original document based on how we segment the paper-- we can essentially segment into what the authors intended logically regardless of the pdf as it was rendered, and we can even go a step further … and have the segments as what the author *intended* but didn't execute well enough." And: "none of those say 'your understanding of the source document must always be reversible into the original document with its flaws.'"
- **The discipline (proposed):** the arrangement is our reading; the words inside the quote marks are the source's.
  - A segment that rejoins a footnote to its marker, rebuilds a table the converter interleaved, or groups a definition with the exclusion that qualifies it says so in a `## Mapping to original` section.
  - That section marks how sure the reading of intent is.
  - A reader can then always tell layer 1 (what was written) from layer 2 (what we take the authors to have meant).

**Back-tracing (agreed).** Joseph's examples: `original-logical-location: blah.md|part 2|chapter 7|section 'blah'` and `original-pages: asdf.pdf pp.332-333 + 419`. These "make it trivial to back-trace for a paper or to propagate forward a typeo-fix". Each segment also says how to cite it: internally by slug, externally by PDF pages (physical and printed), section, and quote.

**The segment file (agreed 2026-10-10):** markdown with YAML frontmatter, in the estate's segment shape. Where an AAT segment has `## Formal Expression` (`~/src/arch/asf/01-aat-core/src/def-mismatch-signal.md`), a source segment has `## Source Content`. In order:
- frontmatter (slug, original pages and logical location, citation, levels, licence, typed edges);
- a title line;
- `## Source Content`: the source's words, with their level marks inline;
- `## Mapping to original`;
- the prose sidecar sections;
- `## Working Notes`.

udon stays the lexicon's format (`def/`). Joseph: other kinds of segment may migrate to udon after udon lite's parser is in place, "a bridge we'll decide when we get to it".

**Where each sidecar lives** (Claude's rule; Joseph deferred sidecar architecture to Claude, 2026-10-10). A sidecar lives where its changes come from:
- **What changes one segment at a time stays in the segment file:** Source Content, Mapping to original, Working Notes, findings and observations, and the typed edges in frontmatter. Keeping the stable text beside the working area in one digestible file is the readability gain Joseph named.
- **What changes in a pass over a whole source lives in one file per kind of pass, per source, keyed by slug:** model-written concept tags, an expert's tag pass, a classifier's role tags, family summaries, and lexicon marks written in bulk. A pass then makes one diff and one reviewable, revertible change, instead of touching every segment and colliding with people's notes.

This is co-change cohesion (TST's measure, as Joseph put it) counted by change event rather than by frequency alone. Logical udon stores may later make the split transparent.

**Where segments live** (agreed 2026-10-10). Each source has a directory `sources/KEY/`, flat inside:
- `SLUG.md`: one per segment;
- `outline.md`: the source's front door and its own table of contents, the first view. Document-level facts go in its frontmatter and head: licence, whether its Source Content is sealed, lineage and versions;
- `influx.md`: issues not yet placed in a segment (Joseph: "influx", "the name it's given everywhere else");
- `sidecars/`: the per-pass files (`tags.free.yaml`, `tags.expert.yaml`, …), each keyed by slug;
- `.decrypted/`: git-ignored.

Three further points:
- **No README per source.** Joseph's concern: "in other projects outline tends to get checked rigorously over and over along with the segments, and stuff that would normally be in the readme ends up in outline but more current". `asf/01-aat-core/` has none, since a README nobody read was a surface nobody kept fresh. One `sources/README.md` explains the convention once, sealing included.
- **The source's own model of risk** (today's `influx/source-models/`) is our reading of the whole document, so it becomes a record of its own, linked from the outline.
- **Only sources being worked get a directory:** Au5 and the pilot first.

**Citing a segment** (agreed): `KEY#slug` (`california-2025-sb53#22757.11-c`), resolving to `sources/KEY/SLUG.md`. Slugs need only be unique within their source. Joseph: "as long as we are consistent, it will be easy to change wholesale if udon/verisectorium develops a principled standard for us."

**Starting a source** (agreed): a `sources/.new/` template-with-instructions and a `bin/` utility that copies it into place, built with the SB 53 pilot so the template is shaped by what the pilot needs.

## 4. Verbatim text and its marks (agreed)

The verbatim section is generated by the high-fidelity pass plus its patches. Everything else in a segment is authored. Edits inside the marks are forbidden once a span is at level 3.

| Mark | Level | Meaning |
|---|---|---|
| `‹⟨…⟩›` | 1 | a raw estimate that needs fixes |
| `«⟨…⟩»` | 2 | a likely correct copy that still needs final verification and normalisation |
| `«⟪…⟫»` | 3 | done: verified against the source, page included, and normalised to the project's conventions |

- **The levels say what has been done to the text.** Level 3 is required for anything cited externally or load-bearing. Joseph's reason for marking it in-band: an agent meeting an odd phrase "by the delimiter know[s] that no one has yet double-checked the pdf".
- **Normalisation** (`$…$` mathematics, heading and footnote notation, whitespace) can happen at any level, and level 3 can equal level 1's text "when justified" (Joseph). Level 3 means checked and in the conventions, not altered.
- **Earned, not typed** (agreed with Joseph's "I agree 100% with your refinements"):
  - level 2 can be certified by `bin/check-quote` itself;
  - level 3 needs a recorded act (who looked at which page, when), kept in the segment's working notes;
  - tools may downgrade a mark that no record supports.
- **Per span, lowest wins.** A segment can hold spans at different levels, and a quote crossing them takes the lowest.
- **Two kinds of error** (proposed):
  - a *conversion* error is fixed inside the marks with a recorded patch ("1013" → "10^13" because the PDF says so), and the fixed span earns level 3 as it's fixed;
  - the *authors'* own error is kept exactly and noted (the Legislative Counsel's digest writes "internet use" for "internal use").
- **Search output follows the same marks.** Today every result's quote shows `«⟨…⟩»` whatever its state, which overstates most of them. The marks are taught in `--help` (glyphs are interfaces: `form-agentic-eyes`, concern 5).

**Evidence that agents read them** (`~/src/arch/asf/empirica/glyph-sequence-perception/spikes/quote-level-marks-2026-10-10/REPORT.md`, commit `4ee2b895`, run at Joseph's request the same evening):
- **Frontier readers were right on every item:** Opus 5.5, Sonnet 5.5, Grok 4.6, Gemini 3.1 Pro and Gemini 3.8 Flash. That covers levels, which quotations may be cited, single versus double, grouping, spotting a mismatched closing mark, and writing the marks back, with the legend in context and without, in lists and inline. Opus and Gemini Flash did most of it with no thinking tokens.
- **The one slip:** Haiku 4.5 with thinking off got 111 of 120 inline quotations right, every error pointing downward (level 2 read as level 1). It never read a quotation upward, and its lists of citable quotations were right every time.
- **Gaps:** no GPT data (the account was at its limit), and no small local model was usable.
- **The marks stay as designed** (Joseph: "I like them as we designed"). The report's option of changing level 1's inner mark, to widen its margin from level 2, wasn't taken.

## 5. Licences, and sealed source content (agreed)

`catalog/licences.yaml` (commit `657a166`; summary in `catalog/licences.md`) covers all 472 catalog keys:

| May the whole text be committed? | Sources |
|---|---|
| yes | 276 (75 by a general rule) |
| conditional | 16 |
| no | 160 |
| unknown | 20 |

Of Au5, four are committable and Anthropic's August Risk Report isn't. SB 53 is a US state edict (public domain by general rule, high confidence).

**One file per segment, with its Source Content sealed where the licence says no** (agreed 2026-10-10; this replaces an earlier "two records per slug", which assumed the verbatim text in a file of its own):
- **Everything but `## Source Content`** (frontmatter, mapping, sidecars, working notes, brief quotes in them) is always committed in plain text.
- **`## Source Content`** is committed in plain text where the licence allows. Where it doesn't, the committed file holds a sealed block in its place: armoured ciphertext naming its key. Nothing is git-ignored.

Why encrypted rather than ignored: after the high-fidelity pass a segment's verbatim text is authored (patched, arranged by intent, verified), so it can't be regenerated from the PDF. Ignored, it would live on one machine with no history. Encrypting it keeps it versioned and shared, readable only by someone who holds the source. Joseph's idea; Claude had proposed git-ignoring it.

**The encryption** (agreed; Joseph: "vetted AEAD sounds perfect"):
- **The cipher:** a vetted AEAD from a standard library, never anything bespoke. It runs in a deterministic SIV mode, so a ciphertext stays unchanged while its text does and git doesn't churn. That leaks only whether two segments are identical.
- **Data key and wraps:** each source has a random data key, wrapped once for each known byte-identical PDF of it. A re-uploaded or differently-sourced copy of the PDF is added as one more wrap.
- **The key that wraps it** is derived with BLAKE3's key-derivation mode, from the PDF's bytes, a context string (`ai-risk-model verbatim v1`) and a random per-source salt kept in the repository.
- **The rule on digests** (Joseph's wording added): it is never derivable from any digest we publish, such as the sha256 a planned lock file would record. And it is "never derivable from any obvious digest of pdfs that someone else might publish either". Only the file itself, with the salt and context, gives the key.
- **The key check comes from the wraps:** if no wrap opens with a PDF's key, the tool says that no known PDF matches the copy at hand. A segment that then fails its own tag is corrupt, not locked.
- **PDFs are found only through relata** (Joseph, 2026-10-10: "hardcode using relata to actually get the pdf's local location"). That works the same in every worktree, and no second local copy of a PDF exists to commit by accident.

**The workflow** (agreed, Joseph's design):
- **Where decrypted text lives:** a git-ignored `.decrypted/` working directory beside each source's segments holds whole segment files with their Source Content unsealed. Agents read and edit there, and the tools map a sealed segment to its `.decrypted/` copy.
- **The tool does the work, and git hooks call it:**
  - a pre-commit hook seals changed decrypted files, and refuses any staged plaintext verbatim of a source whose licence says no (checked against `catalog/licences.yaml`);
  - post-checkout and post-merge hooks decrypt.
- **Attestation in the commit message** (Joseph: the hooks are "the perfect place to have a developer affirm that they meant to change a verbatim quote, that it is a correction, and/or attest that the correct checks have been done for a level upgrade"). The suite's no-prompts norm rules out asking interactively, and agents commit non-interactively, so a commit-msg hook checks trailers. A commit that changes a Source Content section or raises a level without a matching trailer is refused, and the refusal names the missing trailer and why. Examples:

  ```
  Verbatim-Change: correction (conversion error; checked against the PDF, p. 12)
  Level: 22757.11-c 2→3 (pages 3–4 checked by eye)
  ```

  The trailers are the recorded acts that make a level earned: a segment's level can be computed from its history.
- **One install step:** hooks don't travel with a clone, so each clone needs `git config core.hooksPath .githooks`, and the tool warns when they're inactive.
- **Git's clean/smudge filters** (git-crypt's approach) were considered and not chosen. In a clone without the filter configured, git silently commits plaintext. The `.decrypted/` design fails closed instead.

**On distributing encrypted copies** (Joseph's decision and reasons, 2026-10-10): "I am comfortable taking accountability and responsibility-- especially since we aren't encrypting the pdf or anything but rather our completely torn up and annotated version-- which, even unencrypted, isn't enough to recreate the source (necessarily…), and in practice each segment on its own would almost certainly fall under fair-use doctrine-- especially considering our usecase… the law cares about intent-- and this is far from being careless and is clearly a good-faith effort to support the underlying licenses and rights, not loophole around them." The licence table isn't legal advice, and nor is this note.

**Cautions still open from the licence survey:**
- **No-derivatives texts** (and IETF and W3C documents) mustn't be modified, so normalising them could count as modifying them.
- **ShareAlike** (7 sources: 3 CC BY-SA, 4 CC BY-NC-SA) extends to our commentary in the same file. Agreed (Joseph): such segments say so in their frontmatter and in a one-line notice, and the whole segment is offered under the source's licence.
- **The repository has no LICENSE file,** so mixed licences mean marking each committed file. Committed verbatim files carry their licence's attribution notice.
- **Ten papers, Canada's ISED pages and one CSET brief are non-commercial only.** Whether this repository counts as commercial is Joseph's call.

## 6. Sidecars

Joseph's list, as given (2026-10-10):

> [commentary:findings (e.g., "This is inconsistent here vs in the executive summary, which ....")], [structural-tags (e.g., normalize as frontmatter->section->subsection->subsubsection->backmatter or something accross many document variations)], [commentary:observations (e.g., from wandering thoughts etc.)], [commentary:summary:family-1], [chunk-boundaries?], [epistemic-labels?], [authority?], [model-role-tags? (that is, from the perspective of risk-analysis models etc.-- "<hazard>" -- this is stuff that is among the first that will need the lexicon as a rosetta stone where the term is the most useful from a risk-analysis-modeling perspective -- i.e., independent of "AI" and actual risk/hazard instances...)], [lexical-tags?], [relational-context-tags?], ...

What has been measured so far, and where it fits:
- **Concept tags** (what a passage is about, in the field's usual words) are RANKING's H-M3. Tagged by Sonnet agents blind to the queries, on Au5:
  - +0.068 to the outline's flagged score against the whole-document judges;
  - +0.042 against the experts' blind judgments, an interval crossing zero;
  - +0.098 against the experts when combined with query expansion (the robust result).

  Sources: `influx/spikes/spike-search-shortfall-2026-10-10/` and its `de-novo-feedback-1.md`. They work mostly by restating a passage in standard vocabulary. Free tags drift between batches, so the proposal is three labelled tiers: tags a model writes, an expert's source-aware tags, and the lexicon's terms, the last superseding the others as entries land.
- **Role tags** (what a passage *is* in its document: operative text, the source's own summary, example rather than obligation, front matter, navigation, interpretive rule) answer findings the experts made: the digest outranking the law (H-R4), site chrome ranking (H-R3), and the EU Code expert's "example, not obligation". These are Joseph's structural tags and `authority`.
- **Relations** (qualifies, cites, near-copy-of) are edges between segments, not tags on one. They're Joseph's relational-context tags.
- **Summaries and observations** are commentary, ours, and shown as ours.

Every sidecar is our reading, never quoted as the source's words. Search may let a sidecar raise a segment, never exclude one (DESIGN §12).

## 7. What it would change in the tools (proposed, nothing decided)

- `bin/source-index` reads segments where a source has them, and the canonical text where it doesn't yet. Search results carry slugs.
- `bin/check-quote` certifies level 2 and reports each quote's level.
- `bin/reading` serves an expert one segment, or a run of them, at a time.
- The experts' gold judgments get re-keyed from passage ords to slugs, which tests whether the slugs hold.

## 8. The pilot (proposed)

SB 53:
- **It's public domain,** so the public form can be tested whole.
- **It has natural units** (subdivisions).
- **It has an expert,** whose findings become the first working notes.
- **Its gold has three judges** (Claude, Gemini, the expert), to re-key as an identity test.

Then the search index reads SB 53's segments, and we see what breaks before touching the other 471 keys.

## 9. A prediction

Joseph, 2026-10-10: "while a lot of the commentary and all of the lexicon + risk modeling etc. will stay unique to this project, I predict that a lot of this pdf -> verisectorium w/ encryption & license awareness etc. will eventually move over to be standard within verisectorium or even from within relata itself." Recorded so that it can be checked later, and so the tools are built with that move in mind: the sealing, the licence awareness and the template kept separable from this project's lexicon and models.

## 10. Open

- **The segment file's format:** markdown with YAML frontmatter, as in other verisectoria, or udon like the lexicon.
- **Typed edges:** their vocabulary, and whether only `qualifies` and `cites` cascade.
- **How a segment's working notes and the per-source inbox are drained,** and by whom.
- **The high-fidelity conventions themselves** (mathematics, headings, footnotes). They become level 3's definition.
