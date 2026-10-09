# Proposal: updating `source-catalog.md` after the relata additions of 2026-10-08

*Drafted 2026-10-08/09 by a Claude (Opus 5.5) agent, at Joseph's request: "We should update all of source-catalog.md as well, ideally in a way that relata can look at it and generate a bibliography." It was applied to `source-catalog.md` on 2026-10-09, with Joseph's decisions: see *Applied* below. The agent extending `bin/canonicalize` should go straight to §2.*

## Contents

- [Applied, 2026-10-09](#applied-2026-10-09)

0. [What needs deciding](#0-what-needs-deciding)
1. [The premise changed while this was drafted](#1-the-premise-changed-while-this-was-drafted)
2. [Parsing contract, for bin/canonicalize and relata emit](#2-parsing-contract-for-bincanonicalize-and-relata-emit)
3. [Changes to existing rows](#3-changes-to-existing-rows)
4. [New main-table rows, ranked](#4-new-main-table-rows-ranked)
5. [The rest of the corpus, ready to paste](#5-the-rest-of-the-corpus-ready-to-paste)
6. [Other fixes the catalog needs](#6-other-fixes-the-catalog-needs)
7. [Found along the way](#7-found-along-the-way)
8. [How this was built, and its limits](#8-how-this-was-built-and-its-limits)

## Applied, 2026-10-09

Joseph decided the first two questions in §0 and left the rest to the coordinator and me. I applied the proposal to `source-catalog.md` on 2026-10-09. The catalog is now the reference; this file records why it looks the way it does. `bib/refs.bib` has not been regenerated, because that was outside what I was asked to write. `relata emit bib` will regenerate it, with 466 entries and none missing.

**His decisions:**
- **"Superseded" is split in two.** Joseph: "I'm ok with keeping older versions as evidence and as a sort of diffable history, but we definitely need to mark supersession in the broader sense. I vote we say that the strict 'supersession' is instead termed 'subsumed by' [implying a copy isn't required at all], vs 'superseded' [implying we probably have a copy, and can reference it, but not reference it as 'active' in whatever sense that document's lineage considers supersession and what's active]." So there are three statuses: `subsumed-by` (my strict sense), `superseded-by` (an earlier version, still canonicalized) and `no-canon`. §2 now defines all three.
- **The syntax:** "sounds great".

**What went into the catalog:**
- **§3, all of it (A1–A6).** The earlier versions are in their rows, tagged `superseded-by`.
- **§4, rows B1–B25.** That is the nine anchors, the nine majors (B10–B18) and seven supporting rows (B19–B25). The table now has 99 rows.
  - *Left out:* B26 (AISI's labour-market assessment, which the repo does not use) and B27 (the vocabulary sources). B27 is a scope question for Joseph: whether the catalog lists the lexicon's sources as well as models of risk. Both stay in the corpus section.
- **§5, as *The rest of the corpus*.** It lists 335 keys in 10 families. The keys promoted to the table came out. `perset-2025-how-managing-risks` came in, because it is no longer mentioned with an at sign elsewhere. The IASR family emptied once its three documents became rows, so it was dropped.
- **§6, F1–F5.** The upstream table is renamed "… not held". F6 is a set of relata corrections and was not applied. F7, the exclusions, holds.

**Lineages marked `superseded-by`** (17 lineages, 34 tags; each tag names the next version, and each chain ends at the active one):
- **Developer frameworks and policies:**
  - Anthropic's RSP, v1.0 to v3.4.
  - The RSP noncompliance policy, 2025 to 2026. The 2026 text says it "has been updated".
  - Anthropic's Risk Reports, February to August 2026.
  - OpenAI's Preparedness Framework, beta to v2.
  - GDM's FSF, v1.0 to v3.1.
  - Meta: the February text, then the March re-upload, then v2. v2 is "previously titled the Frontier AI Framework".
  - xAI: the two RMF drafts, the RMF, the FAIF of December 2025, then the FAIF of June 2026. The atlas read the 2025 FAIF as a revision of the RMF.
  - Microsoft, 2025 to 2026.
  - Amazon, 2025 to 2026.
  - NAVER, ASF to ASF 2.0.
  - Shanghai AI Lab's practice report, v1 to v1.5.
- **Government and intergovernmental:**
  - TC260, 1.0 to 2.0.
  - Colorado SB 24-205 to SB 26-189. SB 26-189 "repeal[s] and reenact[s]" the part SB 24-205 added.
  - NCSC's January 2024 assessment to the May 2025 one, which "builds on" it.
- **The IASR series:** the interim report to IASR 2025, then IASR 2026; both 2025 Key Updates to IASR 2026.
- **Index and consensus editions:** the FLI index, Summer 2025 to Winter 2025 to Summer 2026; the Singapore Consensus, 2025 to 2026.

**Not marked**, because no held document replaces them as active:
- EO 14110: revoked, but the revoking order is not in relata, and EO 14179 calls 14110 "revoked" rather than replacing it.
- The AI Act: amended by the Omnibus, not replaced.
- OpenAI's PF v2 and FGF: the repo doesn't show the FGF replacing the PF.
- The Taskforce and AISI progress reports: successive reports, not versions.
- Press releases beside their reports: different texts.

**Where I changed my mind while applying it:**
1. **The Kimi pair is `subsumed-by`, not `superseded-by`.** That follows from the new vocabulary.
2. **`superseded-by` names the next version, not the latest, and chains are allowed.** My draft rule "chains are an error" now applies only to `subsumed-by`. Naming the next version keeps the diffable history Joseph asked for, and the active version is wherever a chain ends.
3. **Several tags on one key are allowed, but only `no-canon` with `superseded-by`.** A copy (`subsumed-by`) has no status of its own.
4. **IASR 2025 is tagged `superseded-by` IASR 2026,** even though it covers topics 2026 dropped. "Not active" is a statement about the series, not about content, so the row's basis still says what 2025 alone covers. The same reasoning applies to the February Risk Report.
5. **The intro now says the relata-10-08 rows were not "read directly in later rounds".** I wrote them as a separate sentence, so the existing list keeps its meaning.
6. **Some new rows got a leading date in place of a range**, so that "newest first" sorts them, for example AISI-ALN "Sep 28, 2026 (also …)".
7. **The Key Updates' row lost my "could equally go into the IASR 25 row" aside,** since it is now a row.

## 0. What needs deciding

*As proposed on 2026-10-08. Joseph's decisions on items 1 and 2 are in* Applied *above.*

In the order I'd take them:

1. **What "superseded" means** (§1). I propose that it means *a duplicate of the same text*, and nothing more. Earlier versions of a document are then sources in their own right, and they get canonicalized. The alternative is to treat every earlier version as superseded by the latest. That would leave `bin/canonicalize` without the RSP v1.0 that GDM's FSF v1 cites, and without the versions Zhu measures change across.
2. **The status syntax** (§2). It needs the canonicalize agent's agreement before anything is pasted.
3. **The existing-row changes** (§3). They involve little judgment: mostly earlier versions added to rows whose basis already rests on those versions, plus two factual corrections.
4. **New rows** (§4). They are ranked, so you can take them from the top and stop anywhere. The first nine are anchors whose basis the repo already shows, or now shows.
5. **The corpus section** (§5). It is 382 keys in 11 families, and pasting it in place of "Not listed" makes the catalog cover the whole corpus. `relata emit` on the current catalog plus this section resolves all 466 keys, with none missing.

## 1. The premise changed while this was drafted

The brief I started from said the catalog should not change yet. `bin/canonicalize` takes its source list from the catalog's `@key`s, and adding keys would silently widen a run that was in progress. Partway through, Joseph reversed that. His note to the canonicalize agent:

> "I noticed that INDEX.md has a lot of editorialization etc.-- that it's not just automatically generated from bin/canonicalize . We have hundreds of new sources to add for canonicalization-- (just look at `relata prep list`). Decisions like which ones don't need canonicalization and are superseded etc. etc. should be made in source-catalog and correctly understood by bin/canonicalize ."

So the catalog now governs canonicalize's scope, and each key needs a status there. §2 proposes the form. §5 lists everything outside the main table with its status. I had first planned a separate `bib/src/corpus.md`, which `relata emit` would read and canonicalize would not. That only made sense under the old premise, and I have dropped it.

**It is already true today** that every `@key` anywhere in `source-catalog.md` reaches canonicalize, not only the keys in the main table. `catalog_keys()` scans the whole file. The upstream table's OECD row mentions `@perset-2025-how-managing-risks` in passing, as the place the lineage was checked, and that is why `perset-2025-how-managing-risks` has a row in `ref/canonical/INDEX.md`. The contract below makes this explicit: the at sign means "listed". Prose that only mentions a key writes it bare.

**What "superseded" should mean** (decision 1; Joseph split it into `subsumed-by` and `superseded-by`, see *Applied*). A text is superseded when the corpus holds another copy of the same text that should be used instead: a re-upload, a mirror on a second site, a doubled relata entry. Earlier versions are not superseded in this sense, for three reasons:
- **Lineage runs through particular versions.** GDM's FSF v1 links the RSP v1.0 announcement. IASR 2025 cites RSP v1.0 and the Preparedness Framework beta. The 2025 Singapore Consensus cites RSP v2.0.
- **Zhu's study is about the differences between versions.** The catalog cites it because "a compiled claim without a version and date goes stale" (OVERVIEW §1.4).
- **The relata additions agent has already filtered.** It left out the same-label re-uploads that Zhu codes as not material.

On this reading, the corpus as it stands has one candidate for "superseded" (§5, US government: the NIST copy of the Kimi K3 assessment) and two keys that cannot be canonicalized because relata holds no document for them.

## 2. Parsing contract, for bin/canonicalize and relata emit

*Agreed by Joseph on 2026-10-09 ("sounds great"), with the third status he added. The catalog now uses it. The canonicalize agent may still amend it, and the questions at the end are for it.*

**Keys.** Keys are written as before: `` `@key` `` in backticks. Any `@key` anywhere in `source-catalog.md` puts that document in the corpus: in the bibliography, and in canonicalize's scope unless a tag says otherwise. A key mentioned in prose is written bare (`` `perset-2025-how-managing-risks` ``), so that the mention is not read as a listing.

**Status tags.** Tags come right after the key's closing backtick, on the same line, and there may be more than one. Joseph's terms: "'subsumed by' [implying a copy isn't required at all], vs 'superseded' [implying we probably have a copy, and can reference it, but not reference it as 'active' in whatever sense that document's lineage considers supersession and what's active]."

```
`@key`                                  canonicalize (the default; no tag)
`@key` [no-canon: <reason>]             bibliography only; the reason is free text
`@key` [subsumed-by: @other-key]        a copy of the same text as @other-key; bibliography only
`@key` [superseded-by: @next-key]       an earlier version; @next-key is the next version in its lineage.
                                        Canonicalized, and citable as history, not as the active document
`@key` [superseded-by: @next-key] [no-canon: <reason>]
                                        an earlier version that is also not canonicalized
```

**Where tags may appear.** A tag can follow any listed key: in a main-table `relata` cell (including cells that hold several keys), in a list item, or in a table cell elsewhere. It belongs to the one key before it.

**A regex** that reads keys and their tags. It extends the one `catalog_keys()` used before:

```python
KEY  = r'[A-Za-z0-9_](?:[\w:.#$%&+?<>~/-]*[\w])?'
TAG  = r'\[(?:no-canon|subsumed-by|superseded-by):[^\]\n]*\]'
ITEM = re.compile(r'(?<![\w@])@(?P<key>' + KEY + r')`?(?P<tags>(?:[ \t]*' + TAG + r')*)')
TAGS = re.compile(r'\[(?P<status>no-canon|subsumed-by|superseded-by):[ \t]*(?P<arg>[^\]\n]*)\]')
```

`ITEM.finditer` over the file gives each key with its run of tags, and `TAGS.findall` on the `tags` group splits the run. Because `ITEM` consumes the tags, a key named inside a tag is not matched as a separate listing.

**What each status means:**

| Status | `relata emit bib` | `bin/canonicalize` | `INDEX.md` (a suggestion) |
|---|---|---|---|
| none | in `refs.bib` | canonicalized | a row with its fidelity mark |
| `no-canon` | in `refs.bib` | skipped | a row giving the reason |
| `subsumed-by` | in `refs.bib` | skipped | a row naming the copy that is used |
| `superseded-by` | in `refs.bib` | canonicalized | a row with its fidelity mark, marked "superseded by …" |

**Rules:**
- **One status per key, per kind.** A key's tags are stated once. Untagged repeats of a key elsewhere are harmless, and two different runs of tags on the same key are an error.
- **Which combinations are allowed.** `no-canon` combines with `superseded-by`. `subsumed-by` stands alone, because a copy has no status apart from the text it copies.
- **Targets are listed in their own right.** The key a `subsumed-by` or `superseded-by` names is also listed elsewhere in the catalog. The tag doesn't bring it into scope.
- **`subsumed-by` does not chain.** It names a key that is not itself subsumed.
- **`superseded-by` names the next version, not the latest.** Chains (v1.0 → v2.0 → … → v3.4) are expected. Following them from any version ends at a key with no `superseded-by`, which is the active one. A cycle is an error.
- **Missing documents.** A key relata doesn't hold is an error. A key with no document, or with no conversion yet, is reported and skipped, not fatal. On 2026-10-09, 318 of the 382 keys outside the original 84 had no conversion yet; most are in relata's queue (`relata prep list`).

**What was tested,** on the catalog as applied:
- `relata emit` wrote 466 entries, with 0 missing.
- The regex above reads 466 keys, 37 of them tagged: 34 `superseded-by`, 2 `no-canon` and 1 `subsumed-by`.
- Every tag's target is listed.
- Every `superseded-by` chain ends at an untagged key. There are 17 lineages, each ending at its active version.
- 463 keys are to be canonicalized.

`relata emit` ignores the brackets, as a sample file showed before the catalog was changed.

**Questions for the canonicalize agent** (I can't answer these from here):
1. **Is this syntax workable?** Would a status *column* in each table work better? The inline tag has two advantages: it works the same in the main table's multi-key cells and in plain lists, and it keeps the status beside the key it governs.
2. **Web pages printed to PDF.** 83 of the keys outside the original 84 are web pages rendered to PDF, with a provenance first page. Their page numbers are rendering artefacts, as the renderers note. Should canonicalize recognise them by itself (the provenance page is uniform), or should the catalog say so with a tag of its own?
3. **Per-source judgments now in code or in INDEX.md.** These include `LOCAL` (a hand-made conversion for the CSB report, and the publisher's web edition for IASR 2026) and the editorial notes Joseph saw in INDEX.md. Should they move into the catalog as tags too, for example a status naming the markdown to use? Or should they stay in code, with INDEX.md generated wholly from the catalog plus measurements?
4. **INDEX order.** Should it follow catalog order or alphabetical order? With 466 keys, alphabetical order may serve readers better; catalog order keeps families and lineages together.

## 3. Changes to existing rows

Each change below names the keys to delete from the §5 lists if it is applied, so that each key appears once. Tags for keys added to an existing row: **P** stays for the versions the verification files read. The added versions are **U**, because they have not been read, beyond the checks named below.

**A1. ANT-RSP: add the earlier versions.** The row says "the template role belongs to the series and its earlier versions", but it lists only v2.2, v3.0 and v3.4. relata now holds every version from v1.0 to v3.4; there was no v1.1 (Zhu, via the additions report). What the repo can now show about which versions others took up:
- GDM's FSF v1 links `anthropic.com/news/anthropics-responsible-scaling-policy`, the v1.0 announcement (`gdm-2024-fsf-v1-0`, fn 1, p. 1).
- IASR 2025 cites "Anthropic's Responsible Scaling Policy, Version 1.0" (its reference 595, p. 259).
- The 2025 Singapore Consensus cites "Responsible Scaling Policy (Version 2.0)".
- OpenAI's PF v2 (15 Apr 2025) cites "Anthropic's updated RSP" (p. 5, fn 2). That could be v2.0 (15 Oct 2024) or v2.1 (31 Mar 2025).

Proposed row:

| Date | Code | Document | Kind | relata | Tag | Set | Influence | Basis / note |
|---|---|---|---|---|---|---|---|---|
| Jul 8, 2026 (v3.4 effective; v3.3 May 26, v3.2 Apr 29, v3.1 Apr 2, v3.0 Feb 24, 2026; v2.2 May 14, 2025; v2.1 Mar 31, 2025; v2.0 Oct 15, 2024; v1.0 Sep 19, 2023) | ANT-RSP | Anthropic, *Responsible Scaling Policy* v3.4 | Company framework, self-described "voluntary" | `@anthropic-2026-rsp-v3-4`, `@anthropic-2026-rsp-v3-3`, `@anthropic-2026-rsp-v3-2`, `@anthropic-2026-rsp-v3-1`, `@anthropic-2026-rsp-v3-0`, `@anthropic-2025-rsp-v2-2`, `@anthropic-2025-rsp-v2-1`, `@anthropic-2024-rsp-v2-0`, `@anthropic-2023-rsp-v1-0` | P (v3.4, v3.0, v2.2); U (others) | added | anchor | The RSP series is a template for the framework genre. GDM's FSF v1 cites it among the work that informed it, linking the v1.0 announcement. OpenAI's PF v2 says its "adoption of Capability Reports and Safeguards Reports parallels Anthropic's updated RSP" (source-models/frontier-safety-frameworks.md §6; source-models/anthropic-openai.md B5), which fits v2.0 or v2.1. IASR 2025 cites v1.0; the 2025 Singapore Consensus cites v2.0 (catalog-update-proposal-2026-10-08.md §3). The template role belongs to the series and its earlier versions; v3 moved from a capability gate toward periodic Risk Reports (OVERVIEW §1.1) |

Delete from §5: the six `anthropic-…-rsp-v…` keys under Anthropic.

**A2. OAI-PF: add the beta.** GDM's FSF v1 (May 2024) cites "OpenAI's Preparedness Framework" by linking `openai.com/preparedness/` (fn 1, p. 1). The beta of December 18, 2023 was the only version then. IASR 2025 cites the beta by name (reference 594, p. 259). Change the relata cell to `` `@openai-2025-preparedness-framework-v2`, `@openai-2023-preparedness-framework-beta` ``, the date cell to "Apr 15, 2025 (v2; beta Dec 18, 2023)", and the Tag to "P (v2); U (beta)". Add to the basis: "GDM's FSF v1 links the Preparedness Framework when only the beta existed, and IASR 2025 cites the beta." Delete from §5: `openai-2023-preparedness-framework-beta`.

**A3. META: add the February text.** `meta-2025-frontier-ai-framework` is Meta's March 28, 2025 re-upload, under the same "v1.1" label. `meta-2025-frontier-ai-framework-feb` is the text first published on February 3, 2025. Zhu codes two of the re-upload's changes as material: the scope narrows from "match or exceed" to "exceed", and the object of the non-release trigger changes from "a catastrophic outcome" to "a threat scenario" (additions report). Add the key to the relata cell. Change the date cell to "Apr 7, 2026 (v2; v1.1 Feb 3, 2025, re-uploaded Mar 28, 2025 with material changes)". Add the Tag "U (Feb text)". Add to the basis: "PF v2's 'recent' does not say which of the two v1.1 texts it means." Delete from §5: `meta-2025-frontier-ai-framework-feb`.

**A4. GDM-FSF: add the earlier versions, and correct "earliest".** The row's basis rests on v1, but the row lists only v3.1. relata holds v1.0, v2.0 and v3.0 (`gdm-2024-fsf-v1-0`, `gdm-2025-fsf-v2-0`, `gdm-2025-fsf-v3-0`). Add them. The FSF section and the atlas read all four, so P is defensible for all four if that reading counts. Otherwise use "P (v3.1); U (others)". The basis also says "Its v1 is the earliest framework in the set". That is true of the FSF section's set, which leaves out the RSP and the Preparedness Framework (its title says so). It is not true of the catalog: RSP v1.0 (Sep 2023) and the PF beta (Dec 2023) are earlier. Proposed wording: "Its v1 (May 2024) is the earliest framework in the FSF section's set, which excludes Anthropic's and OpenAI's; almost every later framework in that set repeats the core components v1 states." Delete from §5: the three `gdm-…-fsf-v…` keys.

**A5. ANT-FCF: v1 is no longer obtainable.** The date cell reads "(v1 Dec 19, 2025)". The additions report found that the FCF has only ever been hosted in Anthropic's Trust Center. That listing now offers only v2. Zhu recorded v1, v1.1 (Mar 2, 2026) and v1.2 (Jun 8, 2026) as withdrawn by 2026-09-02. Proposed date cell: "Jul 24, 2026 (v2; v1 Dec 19, 2025, v1.1 Mar 2, 2026 and v1.2 Jun 8, 2026 withdrawn, known from v2's changelog)". `influx/thin-pass/` cites a key for v1, `anthropic-2025-frontier-compliance-framework`, that does not exist in relata. Its dates before v1.1 rest on v2's changelog, not on v1's text (additions report).

**A6. IASR 26: point at the interim report.** If row B1 is added, the IASR 26 basis can say "(see IASR 24)" after its NIST 600-1 sentence.

## 4. New main-table rows, ranked

**Set and Tag for these rows.** I propose a new *Set* value, defined in the catalog's column list as follows:

> **relata-10-08**: not in model-alpha's list, and not yet read in a verification round. Added to relata on 2026-10-08 (`relata-aisi-sweep-2026-10-08.md`, `relata-additions-2026-10-08.md`). The basis passages were checked against the source text in `catalog-update-proposal-2026-10-08.md`.

Every proposed row is tagged **U**. I checked the passages the basis rests on, and for B1–B9 also each document's title and printed date. That is narrower than the reading the existing P rows had. A reading round can raise them.

**Ranking.** Anchors whose basis the repo already shows come first, then anchors whose basis this proposal shows, then *major* rows, then *supporting*. Within each group, the rows that more of the existing analysis relies on come first. I checked each basis passage in the source text; the location follows it. "Title match" means the cited title was found in the citing document's text by search. The citation was not read in context.

### B1–B9: anchors

In rank order: B1 IASR 24 · B2 OECD-INC · B3 Seoul · B4 EO-14110 · B5 METR-23 · B6 Bletchley · B7 Control · B8 SRA · B9 Yampolskiy.

| Date | Code | Document | Kind | relata | Tag | Set | Influence | Basis / note |
|---|---|---|---|---|---|---|---|---|
| May 2024 | IASR 24 | Bengio (chair) et al., *International Scientific Report on the Safety of Advanced AI: Interim Report* | Evidence synthesis (interim) | `@bengio-2024-iasr-interim` | U | relata-10-08 | anchor | NIST 600-1's three-way grouping is "derived in part from the UK's International Scientific Report on the Safety of Advanced AI" (600-1 fn 5, p. 7; OVERVIEW §3.1 and Appendix). The grouping is this report's "malicious use risks, risks from malfunctions, and systemic risks" (p. 12), which the 2025 and 2026 editions keep (OVERVIEW §1.1). IASR 2025 says it builds on it (p. 8) |
| May 2024 | OECD-INC | OECD, *Defining AI Incidents and Related Terms* (OECD Artificial Intelligence Papers No. 16) | Intergovernmental definitions paper | `@oecd-2024-defining-ai-incidents` | U | relata-10-08 | anchor | NIST 600-1 quotes its AI-incident definition (p. 8) without attribution, rendering "leads to" as "contributes to" (OVERVIEW §2.11, §3.1, Appendix). The AI Act's serious-incident harm list is nearly the same, which the repo records as a parallel, not a derivation. The OVERVIEW counts it among three upstream sources that shape several of the eight models ("How to read this") |
| May 21, 2024 (page updated Feb 7, 2025) | Seoul | DSIT, *Frontier AI Safety Commitments, AI Seoul Summit 2024* | Voluntary company commitments, published by a government | `@dsit-2024-frontier-ai-safety-commitments` | U | relata-10-08 | anchor | Signatories undertake to publish "a safety framework focused on severe risks" (the opening undertaking), which turned the framework genre into an obligation. Microsoft says its framework "has its genesis in" these commitments, Meta and Amazon cite them, and Buhl et al. build their components from them (source-models/frontier-safety-frameworks.md §6; OVERVIEW §3.1). Its footnote 1 defines "frontier AI" in DSIT 2023's words, without "today's" (OVERVIEW §3.1) |
| Oct 30, 2023 (FR Nov 1, 2023); revoked by Jan 23, 2025 | EO-14110 | Executive Order 14110, *Safe, Secure, and Trustworthy Development and Use of Artificial Intelligence* | US executive order (revoked) | `@eo-2023-14110` | U | relata-10-08 | anchor | NIST 600-1 takes its definitions of "generative AI" and "dual-use foundation model" and was written under its §4.1(a)(i)(A) (600-1 p. 5; source-models/nist.md). NIST 800-1 quotes its dual-use definition, including "permitting the evasion of human control or oversight through means of deception or obfuscation" (EO p. 4; 800-1 p. 5 and glossary p. 27; source-atlas/us-gov.md). DHS quotes its "foundation model" (source-atlas/feedback/us-gov.md). EO 14179 calls it "the revoked Executive Order 14110" (p. 1); the definitions live on in NIST text |
| Sep 26, 2023 | METR-23 | Barnes, Wijk & Chan (METR), "Responsible Scaling Policies (RSPs)" | Concept proposal (blog post) | `@metr-2023-rsp` | U | relata-10-08 | anchor | METR says it introduced the concept (metr L64–66; source-models/frontier-safety-frameworks.md §1). GDM's FSF v1 cites this post among the work that informed it (fn 1, p. 1). Anthropic's RSP v1.0 says its commitments follow "the Responsible Scaling Policy (RSP) framework being developed by Paul Christiano and ARC Evals" (p. 1); ARC Evals is METR's former name, which the repo does not itself show |
| Nov 1, 2023 (page updated Feb 13, 2025) | Bletchley | *The Bletchley Declaration by Countries Attending the AI Safety Summit, 1–2 November 2023* | Intergovernmental declaration | `@bletchley-2023-declaration` | U | relata-10-08 | anchor | The IASR series exists under its mandate: IASR 2026 "builds on the mandate by world leaders at the 2023 AI Safety Summit at Bletchley Park" (md 308) and takes its focus from the Declaration's "particular safety risks arise at the 'frontier' of AI" (md 362), and the interim report was "commissioned at the Bletchley Park AI Safety Summit" (p. 7). The Declaration's gloss of "frontier" carries DSIT 2023's "match or exceed the capabilities present in today's most advanced models" (catalog-update-proposal-2026-10-08.md §7) |
| Dec 2023 (arXiv 2312.06942; v5 held) | Control | Greenblatt, Shlegeris, Sachan & Roger (Redwood Research), *AI Control: Improving Safety Despite Intentional Subversion* | Research paper | `@greenblatt-2023-ai-control` | U | relata-10-08 | anchor | The source of UK AISI's control paradigm (OVERVIEW §2.9, §3.1). AISI's own papers cite it for that: "control measures offer a complementary strategy that limits a model's ability to cause harm even if it harbors misaligned goals (Greenblatt …)" (korbak-2025-evaluate-control-measures p. 1), and "An 'AI control' argument (Greenblatt et al., 2023)" (hilton-2025-safety-cases-scalable p. 7). *Loss of Oversight* and the Research Agenda do not cite it |
| Aug 2018 (approved Jun 2015) | SRA | Society for Risk Analysis, *Society for Risk Analysis Glossary* | Professional society glossary | `@sra-2018-glossary` | U | relata-10-08 | anchor | MIT adopts its definition of risk: "We followed the Society for Risk Analysis in defining 'AI risk' as 'the possibility of an unfortunate occurrence associated with the development or deployment of artificial intelligence'" (slattery p. 16). IASR's risk-management structure borrows from it, with the NIST AI RMF, ISO/IEC 23894 and the OECD (OVERVIEW §1.3, §3.1), and IASR 2026 cites it on risk-management terminology (md 1652, reference 974). The lexicon research leans on it (gamma-research/risk-formalisms.md §2.3, §4.1) |
| 2016 (AAAI workshop; arXiv 2015) | Yampolskiy | Yampolskiy, "Taxonomy of Pathways to Dangerous Artificial Intelligence" | Taxonomy paper | `@yampolskiy-2016-taxonomy` | U | relata-10-08 | anchor | MIT chose it as its "initial best-fit framework" for the causal taxonomy (slattery p. 22), and CAIS cites it for its four-way split (source-models/mit-cais.md). That is why MIT's causal axis and CAIS's four sources are cousins (OVERVIEW §3.1). relata's `year` is 2015, so the bibliography will print 2015 (§6, F6) |

Rows 2, 3, 5, 7 and 9 come out of the "Upstream sources … not read" table (§6, F2). B1 cuts the IASR 26 basis short (A6). For every row, delete its key from §5.

### B10–B18: major, plus one supporting row that belongs with the IASR series

In rank order: B10 IASR 25-KU · B11 AISI-SC · B12 TC260 · B13 KR-AI · B14 ANT-Const · B15 OAI-Spec · B16 STPA · B17 IMDA-AG · B18 EO-14179.

| Date | Code | Document | Kind | relata | Tag | Set | Influence | Basis / note |
|---|---|---|---|---|---|---|---|---|
| Oct 2025; Nov 2025 | IASR 25-KU | *International AI Safety Report 2025: First Key Update* (capabilities and risk implications) and *Second Key Update* (technical safeguards and risk management) | Evidence synthesis (interim updates) | `@bengio-2025-iasr-key-update-1`, `@bengio-2025-iasr-key-update-2` | U | relata-10-08 | supporting | The series between its 2025 and 2026 editions. The repo shows no citation of them by name: a title search found none in IASR 2026, either Singapore Consensus edition, MIT or SaferAI. They could equally go into the IASR 25 row's relata cell |
| Feb 10, 2025; Jan 28, 2025; Nov 2024 | AISI-SC | UK AISI's safety-case line: Hilton, Buhl, Korbak & Irving, *Safety Cases: A Scalable Approach to Frontier AI Safety*; Korbak et al., *A sketch of an AI control safety case*; Goemans et al., *Safety case template for frontier AI: A cyber inability argument* | Method papers (safety cases) | `@hilton-2025-safety-cases-scalable`, `@korbak-2025-sketch-ai-control`, `@goemans-2024-safety-case-template` | U | relata-10-08 | major | A standing reference the repo now shows in use. GDM's FSF v2.0 defines a safety case and refers to AISI's inability template "for reference" (fn 7, p. 4; source-models/frontier-safety-frameworks.md §6). AISI's Research Agenda gives the control safety-case sketch as an "Example of our work" (p. 28), and the OVERVIEW reads the Agenda's spine as argued in safety cases (§1.1). IASR 2026 cites Hilton et al. and the sketch (references 1037, 751) |
| Sep 2025 (2.0); Sep 9, 2024 (1.0) | TC260 | National Technical Committee 260 on Cybersecurity of SAC, *AI Safety Governance Framework* 2.0 and 1.0 | National standards-committee framework (China); 2.0 bilingual, 1.0 in English | `@tc260-2025-ai-safety-governance-framework-2`, `@tc260-2024-ai-safety-governance-framework` | U | relata-10-08 | major | China's national AI safety governance framework. Shanghai AI Lab's framework "builds upon the International AI Safety Report (January 2025) and AI Safety Governance Framework v1.0" (shanghaiailab-2025-frontier p. 9, fn 6). IASR 2026 names 2.0 as guidance "on risk categorisation and countermeasures" (md 1822). Shanghai's uptake is declared, so *anchor* is arguable, but the repo has not checked what wording passes |
| Jan 21, 2025 (Act No. 20676; amended Jan 20, 2026); Enforcement Decree 2026 | KR-AI | Republic of Korea, *Framework Act on the Development of Artificial Intelligence and the Creation of a Foundation for Trust* (the "AI Basic Act"), and its Enforcement Decree (Presidential Decree No. 36053) | Law (KLRI English translation; the Korean text is authoritative) | `@korea-2025-ai-framework-act`, `@korea-2026-ai-framework-act-decree` | U | relata-10-08 | major | Binding national law. NAVER's ASF 2.0 is built around it (naver-2026-asf2 p. 4; source-models/frontier-safety-frameworks.md §6). IASR 2026 cites it for its "high-impact" requirements (md 1818). Decree Art. 24 sets the compute trigger for the Act's Art. 32 safety duty (relata additions report) |
| Jan 21, 2026 | ANT-Const | Anthropic, *Claude's Constitution* | Developer's governing document for model behaviour | `@anthropic-2026-constitution` | U | relata-10-08 | major | Anthropic's own governing statement of how its models should behave, and to whom they answer. The alignment-referents spike draws principal and operator vocabulary from it (spikes/spike-alignment-referents-2026-10-06/research/lit-role-vocabularies.md). The 2026 Singapore Consensus (its reference Anthropic-I) and AISI's *Loss of Oversight* cite it. IASR 2026 cites the 2023 post of the same name, not this document. Anthropic material: the conflict-of-interest principle applies (CLAUDE.md) |
| Aug 18, 2026 (version) | OAI-Spec | OpenAI, *Model Spec* (2026-08-18) | Developer's governing document for model behaviour | `@openai-2026-model-spec` | U | relata-10-08 | major | OpenAI's counterpart to ANT-Const, and the spike's other source of principal vocabulary (same file). The web page is the source of record; this is the version served on 2026-10-08 |
| 2018 | STPA | Leveson & Thomas, *STPA Handbook* | Method handbook (systems-theoretic hazard analysis) | `@leveson-thomas-2018-stpa` | U | relata-10-08 | major | The method's own handbook, by its originator. IASR 2025 and the AISI Research Agenda name STPA (OVERVIEW §3.1). Mylius et al. and Barrett et al. apply it to frontier AI (source-atlas/lit-a.md). OVERVIEW §2.1 takes STPA's sense of "hazard" as its seventh. Whether the lexicon adopts STPA's vocabulary is an open decision (CLAUDE.md) |
| May 20, 2026 (v1.5) | IMDA-AG | IMDA (Singapore), *Model AI Governance Framework for Agentic AI*, v1.5 | Official guidance (voluntary) | `@imda-2026-mgf-agentic-v1-5` | U | relata-10-08 | major | Official government guidance. The gamma plan takes "component" partly from its "Core components of an agent", checked at p. 6 (reviews/citation-check-2026-10-07.md), and the role-vocabulary report uses its split between app developer and deploying organisation (spikes/…/research/lit-role-vocabularies.md). The 2026 Singapore Consensus cites it (title match) |
| Jan 23, 2025 | EO-14179 | Executive Order 14179, *Removing Barriers to American Leadership in Artificial Intelligence* | US executive order | `@eo-2025-14179` | U | relata-10-08 | major | Binding executive direction. It orders the action plan that became AAP (§4; AAP p. 4 cites it) and a review of everything done under "the revoked Executive Order 14110" (§5, p. 1) |

### B19–B27: supporting, and one *major* by the catalog's own rule

In rank order: B19 AISI-CTRL · B20 AISI-PDT · B21 INM · B22 AISI-TRJ · B23 AISI-SG · B24 AISI-ALN · B25 FMF-RT · B26 AISI-LAB · B27 the other vocabulary sources.

These are mostly UK AISI's. Given who the repo is likely to be read by, I'd take at least B19–B21. Apart from Microsoft's declared use of the FMF report, none of them has an uptake the repo shows beyond being cited.

| Date | Code | Document | Kind | relata | Tag | Set | Influence | Basis / note |
|---|---|---|---|---|---|---|---|---|
| May 7, 2025 (AISI listing; arXiv 2504.05259) | AISI-CTRL | Korbak, Balesni, Shlegeris & Irving, *How to evaluate control measures for LLM agents? A trajectory from today to superintelligence* | Research paper (UK AISI) | `@korbak-2025-evaluate-control-measures` | U | relata-10-08 | supporting | AISI's own statement of the control paradigm that OVERVIEW §2.9 attributes to it. Both Singapore Consensus editions cite it (title match) |
| Nov 19, 2024; Dec 18, 2024 | AISI-PDT | US AISI and UK AISI, *Joint Pre-Deployment Test*: Anthropic's upgraded Claude 3.5 Sonnet (51 pp.), and OpenAI o1 (37 pp.) | Government evaluation reports | `@usaisi-ukaisi-2024-claude-35-sonnet`, `@usaisi-ukaisi-2024-openai-o1` | U | relata-10-08 | supporting | The only published joint government pre-deployment evaluations (AISI sweep report). IASR 2025 cites the Claude 3.5 Sonnet test (reference 1142, p. 286). The o1 test came out after IASR 2025 was written. CAISI-DS sets the precedent for supporting |
| Jul 2025; Jul 2026; Feb 2026 | INM | International Network for Advanced AI Measurement, Evaluation and Science: *International Joint Testing Exercise: Agentic Testing* (99 pp.); *Best Practice: Automated Evaluation of Large Language Models*; consensus areas on evaluation practice (NIST page; AISI post) | Intergovernmental evaluation methodology | `@intlnetwork-2025-joint-testing-agentic`, `@intlnetwork-2026-best-practice-automated-evaluation`, `@nist-2026-intl-network`, `@aisi-2026-network-consensus` | U | relata-10-08 | supporting | A measurement model beside NIST 800-2 (OVERVIEW §1.4) |
| Oct 23, 2025 | AISI-TRJ | Heitmann, Hinrichsen, Africa & Sandbrink (UK AISI), *Understanding AI Trajectories: Mapping the Limitations of Current AI Systems* | Technical analysis | `@heitmann-2025-understanding-ai-trajectories` | U | relata-10-08 | supporting | AISI's model of capability limitations. IASR 2026 cites it (reference 672) |
| Feb 4, 2025 | AISI-SG | UK AISI, *Principles for Evaluating Misuse Safeguards of Frontier AI Systems*, and the *Template* | Guidance (recommendations to developers) | `@aisi-2025-misuse-safeguards-principles`, `@aisi-2025-misuse-safeguards-template` | U | relata-10-08 | supporting | AISI's own vocabulary for safeguards, one of the senses OVERVIEW §2.10 records as colliding. The repo shows no uptake |
| Nov 2025 – Sep 2026 | AISI-ALN | UK AISI's alignment and propensity evaluations: *UK AISI Alignment Evaluation Case-Study*; *Evaluating whether AI models would sabotage AI safety research*; *Evaluating Whether GPT-6 Astra Performs Unsanctioned Supply-Chain Attacks* | Evaluation reports (papers) | `@souly-2026-uk-aisi-alignment`, `@kirk-2026-evaluating-whether-ai`, `@souly-2026-evaluating-whether-gpt` | U | relata-10-08 | supporting | *Loss of Oversight* cites the sabotage paper. The Astra paper sits next to AISI-INC (AISI sweep report) |
| Jun 18, 2025 | FMF-RT | Frontier Model Forum, *Risk Taxonomy and Thresholds for Frontier AI Frameworks* | Industry-body technical report | `@fmf-2025-risk-taxonomy-thresholds` | U | relata-10-08 | supporting | Microsoft 2026 says it will "contribute to and leverage learnings from relevant Frontier Model Forum Issue Briefs and Technical Reports, such as the Technical Report on Risk Taxonomy and Thresholds for Frontier AI Frameworks" (microsoft-2026 p. 11). IASR 2026 cites it (reference 1117) |
| Jan 28, 2026 | AISI-LAB | UK AISI and DSIT, *Assessment of AI capabilities and the impact on the UK labour market* | Government assessment (web page) | `@aisi-2026-labour-market-assessment` | U | relata-10-08 | major (by the rule) | The catalog's rule makes a government assessment *major*. AISI's only impact assessment (AISI sweep report). The repo does not use it yet, and if that should keep it out of the table, it stays in §5 |
| 2001; 2012; 2016; 2022; 1981 | — | The other vocabulary sources: HSE, *Reducing Risks, Protecting People* (R2P2); NIST SP 800-30 Rev. 1; UN A/71/644 (the disaster-risk terminology working group); IPCC AR6 WGII Annex II, glossary; Kaplan & Garrick, "On the Quantitative Definition of Risk" | Regulator guidance; official guidance; intergovernmental terminology; assessment glossary; paper | `@hse-2001-r2p2`, `@nist-2012-sp800-30r1`, `@un-2016-a71644`, `@ipcc-2022-ar6-wg2-annex-ii`, `@kaplan-garrick-1981-quantitative` | U | relata-10-08 | major (the first four, by the rule); supporting (Kaplan & Garrick) | One row or five, if the catalog is also to list the lexicon's sources. gamma-research/risk-formalisms.md reads each (§2.2, §2.8, §2.10). It is a scope question for Joseph: today the catalog lists models of AI risk and the precedents of organizational failure, not vocabulary sources |

**Not proposed as rows** (they stay in §5): CAC's interim measures (Chinese text only, which the catalog does not cover), both Colorado laws (consequential-decision law, used only for role vocabulary), CSA Singapore's two documents, NIST NCCoE's concept paper, Samsung's framework, NVIDIA's agentic framework (`ghosh-2025-safety`), the xAI drafts, Anthropic's transparency proposal, OWASP, the FMF's two 2024 briefs, AISI's blog posts and other papers, and the alignment and role-vocabulary literature. Microsoft, Amazon, xAI, NAVER, G42, Cohere, NVIDIA, Magic and Shanghai remain, as now, outside the table, entering through METR-CE and the FSF section.

## 5. The rest of the corpus, ready to paste

Applied: this is now the section *The rest of the corpus* in `source-catalog.md`, which is the reference. The block proposed here (382 keys, before rows were promoted and before supersession was marked) is in git history at commit `fabe41d`.

## 6. Other fixes the catalog needs

**F1. The opening paragraph.** "This is not a list of every document in relata: the per-family atlases (`influx/source-atlas/`) cover 212" stops being true once §5 is in. Proposed: "The table lists the model's main sources. The section after it, *The rest of the corpus*, lists every other document in relata that the repository cites, so that `relata emit bib` covers the whole corpus and `bin/canonicalize` knows what to do with each." The *relata* column's definition could add: "A key may carry a status tag (see *The rest of the corpus*)."

**F2. The "Upstream sources … not read" table.** relata now holds all five of its documents, so their rows move to the main table: Seoul (B3), OECD (B2), Greenblatt (B7), METR (B5), Yampolskiy (B9). What remains, or newly belongs here, is upstream in the lineage but not held. Each row is tagged U, with its location in the repo:

| Date | Document | What the repo says it shapes | Tag |
|---|---|---|---|
| 2022 | Weidinger et al., the taxonomy of language-model harms | MIT's best-fit source for its Domain Taxonomy, as Yampolskiy is for the Causal (OVERVIEW §1.3) | U |
| 2023 | Christiano and ARC Evals, the RSP framework as developed before METR's post | "designed in the spirit of" it: Anthropic RSP v1.0, p. 1 | U |
| — | ISO 31000 and ISO Guide 73 | NIST's senses of risk, tolerance and residual risk (OVERVIEW §3.1) | U |
| — | ISO/IEC 23894 | IASR's risk-management structure (OVERVIEW §1.3); Shanghai cites it (source-models/frontier-safety-frameworks.md §6) | U |
| — | ISO/IEC 42001 | Cited by Microsoft, xAI, Anthropic's FCF and OpenAI's FGF (OVERVIEW §3.1) | U |
| 2025 | The UK Professional Head of Intelligence Assessment's probability yardstick (PHIA) | The NRR's likelihood labels and *Loss of Oversight*'s likelihoods (OVERVIEW §3.1; Appendix, on the NRR's altered bands) | U |

The OECD row's note that mentions `perset-2025-how-managing-risks` with an at sign goes with the row. If that key should stay canonicalized (it is in `ref/canonical/INDEX.md` today), list it in §5, under EU, other governments and intergovernmental bodies.

**F3. "Not listed" and "Not covered".**
- **"Not listed"** is replaced by §5. Most of the families it names are in relata and now listed: the other frameworks, the developers' posts and system cards, AISI's and NCSC's other publications, the US executive orders, the OECD and Canadian pages, and the loss-of-control literature.
- **"Not covered"** needs the nuance in §5's closing line. TC260 2.0 is bilingual, the Korean texts are official translations, and the CAC measures are held only in Chinese.

**F4. Model-alpha's DSIT row.** Its basis says DSIT's glossary is "the source of that wording in the Seoul commitments". The wording the Seoul commitments share is closer to DSIT's body text than to its glossary, and the Bletchley Declaration has it too (§7, item 2). I'd change the location in the basis to "DSIT p. 4 (and its glossary)". Whether Bletchley belongs in the chain is Joseph's call.

**F5. A possible duplicate.** `nist-2026-aisi-caisi-kimi-k3` and `aisi-caisi-2026-kimi-k3` are the same joint UK AISI / CAISI assessment, rendered from NIST's site and from AISI's. Their word sequences agree at 0.85 (difflib ratio). The difference looks like site navigation and AISI's cookie banner, but I haven't read the two side by side. The catalog tags the NIST copy `subsumed-by` the AISI one (it was `superseded-by` in the first draft of this proposal). The AISI render has the cookie banner interleaved word by word (source-atlas/uk-aisi.md), so the NIST copy may be the cleaner text. Reverse the tag if so.

**F6. Bibliography years that don't match the key, or the year by which the work is cited.** `relata emit` prints relata's `year`:
- `yampolskiy-2016-taxonomy` will print 2015 (arXiv). MIT cites the 2016 AAAI workshop version.
- `kasirzadeh-gabriel-2023-conversation` will print 2022 (arXiv v1). The note on the entry explains.
- `kolt-2026-caputo` names its second author, not a title word.

These are relata corrections, not catalog ones, and they are noted here because they now reach `bib/refs.bib`.

**F7. Entries cited in the repo but deliberately left out of §5.** These 11 keys are cited only in `verification/relata-bugs.md`, `verification/absence-claim.md` and `verification/academic-ngo.md`, as misfiled or mislabelled downloads from another project's active-inference reading: `aguilera-2021-particular`, `coatleven-2024-large`, `costa-2020-active`, `parr-2022-active`, `parr-2022-active-inference`, `russel-2019-short`, `sajid-2021-active`, `tschantz-2019-learning`, `wu-2019-learning`, `wu-he-2018-groupnorm`, `youngren-2017-multi`. Listing them would put them in the bibliography. `ieee-7009-2024-fail-safe-autonomous`, cited by `gamma-research/risk-formalisms.md`, is in §5.

## 7. Found along the way

1. **The OECD paper also defines "AI hazard"**: "an event, circumstance or series of events where the development, use or malfunction of one or more AI systems could plausibly lead to an AI incident" (oecd p. 8). It is not among OVERVIEW §2.1's eight senses of "hazard". It sets hazard against incident as potential against actual, on the same harm list, and the open hazard-versus-threat decision may want it.
2. **The "frontier AI" lineage has a third member.**
   - **Bletchley.** The Declaration (Nov 1, 2023) glosses the frontier as "highly capable general-purpose AI models, including foundation models, that could perform a wide variety of tasks … which match or exceed the capabilities present in today's most advanced models" (as rendered, the paragraph that begins "Particular safety risks").
   - **DSIT.** DSIT's discussion paper of Oct 25, 2023 has "highly capable general-purpose AI models that can perform a wide variety of tasks and match or exceed the capabilities present in today's most advanced models" in its body (p. 4, "For the purposes of the Summit"). The glossary that OVERVIEW §2.26 quotes has a shorter form.
   - **Seoul.** The Seoul commitments' footnote 1 matches the body text, minus "today's".

   DSIT is still the earliest. Bletchley is either a conduit or a sibling, and the repo's chain (DSIT → Seoul) skips it.
3. **The control-paradigm lineage was not, until today, shown where OVERVIEW §2.9 implies.** OVERVIEW §2.9 gives AISI's control paradigm as "from Greenblatt et al. 2024". Neither *Loss of Oversight* nor the Research Agenda cites Greenblatt et al. In *Loss of Oversight*, Greenblatt appears as a contributor and as Greenblatt (2025a, b), on other topics. The attribution holds through two of today's additions, Korbak et al. 2025 and Hilton et al. 2025, which cite "Greenblatt et al., 2023" for it. The year is 2023 on arXiv and 2024 at ICML.
4. **TC260 version.** The additions report proposes TC260 2.0 because "Shanghai AI Lab cites it". Shanghai's v1.0 (Jul 2025) cites and builds on TC260 1.0 (fn 6). Version 2.0 (Sep 2025) came later. Row B12 carries both.
5. **Who cites AISI.** I searched the citing documents' texts for the titles of every corpus document (§8 says how). The AISI items cited by the documents the catalog treats as anchors or majors:
   - IASR 2026 cites Hilton et al., the control-case sketch, Heitmann et al., RepliBench, STACK, the CoT-monitorability paper, deep ignorance, the poisoning paper and the open-weight problems paper.
   - IASR 2025 cites the Claude 3.5 Sonnet joint pre-deployment test and the May 2024 evaluations update.
   - The 2026 Singapore Consensus cites the control-evaluation trajectory and several of the same papers.
   - *Not found anywhere*: the misuse-safeguards principles. Nor did any developer framework I searched cite an aisi.gov.uk page except GDM FSF v2.0 (the inability template).

   This is title matching, not reading, but it may matter for how AISI's own work is represented.
6. **Older AISI web renders.** The 17 AISI blog renders made on 2026-09-27 have the cookie banner interleaved with the text. The sweep's 20 newer renders hid it with CSS. Re-rendering the older 17 the same way would improve their canonical texts.

## 8. How this was built, and its limits

- **The corpus.** I took every token in the repo's tracked files (outside `ref/`) that matches a relata key: 477 keys. I set aside the 11 misfiled entries (F7), which left 466: 84 already in the catalog and 382 in §5. The two reports' keys and the atlas's 212 are all inside that set. No relata entry that an ai-risk-model agent added is left out, except three that the same misfiling produced (`levine-2018-reinforcement`, `subramanian-2019-approximate`, `sun-firestone-2020-darkroom`). They are cited nowhere in this repo and are omitted.
- **Families.** These follow the atlas and the two reports, regrouped by publisher type. A few placements are judgment calls: the summits sit under UK government, and the Taskforce progress reports sit under AISI.
- **Basis checks.** Every quoted basis passage in §3–§4 and §7 was read in a `pdftotext -layout` extraction of relata's PDF, or in `ref/iasr-2026-full.md` ("md" line numbers). Pages are physical PDF pages. For web renders, which carry rendering-artefact pages, I name the passage instead. Line references to source-model files are theirs, unchecked.
- **Title matching** (§4 "title match", §7 item 5) searched the texts of 19 documents, most of them catalog anchors and majors, for a normalised prefix of each corpus title: the part before the first colon when that was long enough, cut to nine words. It finds reference-list entries, not uses. It can false-match generic titles: I discarded the matches for "Frontier AI Framework, Version 1.1" (it cannot tell Meta's two uploads apart), for "Anthropic's Responsible Scaling Policy" (which also matches the v3 announcement), and for NVIDIA's generically titled "Frontier AI Risk Assessment". Spot-checking the matches §4 relies on caught two more, both corrected above. "Claude's Constitution" in IASR 2026 is the 2023 post of that name. The Key Updates' titles begin "International AI Safety Report 2025", so the search matched the main report, and a search for "Key Update" finds no citation. Each title match that §4 uses was then re-run on the first twelve words of the title.
- **Duplicates.** I ran `relata possible-duplicates --title` over every corpus key. It found only known distinct pairs: editions, versions, blog against report, and press release against report. It missed the Kimi pair, which I found by reading the AISI sweep report.
- **Not done.** I read none of the 382 documents beyond the passages named. I did not check §5 key by key against each atlas family's own judgments about misfiled documents. The atlas README says several atlas agents flagged documents that are "not what their key or title suggests". Those notes are in the atlas files and are worth a pass before anything gets `[no-canon]` for that reason.

*On the brief I was given:* it was clear and well-scoped. The one thing it couldn't know was the reversal in §1, and the coordinator relayed that mid-run. The brief said `relata list` truncates long keys. I worked from the entry files directly, so that didn't bite.
