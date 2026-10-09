# Proposal: updating `source-catalog.md` after the relata additions of 2026-10-08

*Drafted 2026-10-08/09 by a Claude (Opus 5.5) agent, at Joseph's request: "We should update all of source-catalog.md as well, ideally in a way that relata can look at it and generate a bibliography." None of it has been applied, and `source-catalog.md` is unchanged. Joseph reads this first. After him, whoever applies it, and the agent extending `bin/canonicalize`, which should go straight to §2.*

## Contents

0. [What needs deciding](#0-what-needs-deciding)
1. [The premise changed while this was drafted](#1-the-premise-changed-while-this-was-drafted)
2. [Parsing contract, for bin/canonicalize and relata emit](#2-parsing-contract-for-bincanonicalize-and-relata-emit)
3. [Changes to existing rows](#3-changes-to-existing-rows)
4. [New main-table rows, ranked](#4-new-main-table-rows-ranked)
5. [The rest of the corpus, ready to paste](#5-the-rest-of-the-corpus-ready-to-paste)
6. [Other fixes the catalog needs](#6-other-fixes-the-catalog-needs)
7. [Found along the way](#7-found-along-the-way)
8. [How this was built, and its limits](#8-how-this-was-built-and-its-limits)

## 0. What needs deciding

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

**What "superseded" should mean** (decision 1). A text is superseded when the corpus holds another copy of the same text that should be used instead: a re-upload, a mirror on a second site, a doubled relata entry. Earlier versions are not superseded in this sense, for three reasons:
- **Lineage runs through particular versions.** GDM's FSF v1 links the RSP v1.0 announcement. IASR 2025 cites RSP v1.0 and the Preparedness Framework beta. The 2025 Singapore Consensus cites RSP v2.0.
- **Zhu's study is about the differences between versions.** The catalog cites it because "a compiled claim without a version and date goes stale" (OVERVIEW §1.4).
- **The relata additions agent has already filtered.** It left out the same-label re-uploads that Zhu codes as not material.

On this reading, the corpus as it stands has one candidate for "superseded" (§5, US government: the NIST copy of the Kimi K3 assessment) and two keys that cannot be canonicalized because relata holds no document for them.

## 2. Parsing contract, for bin/canonicalize and relata emit

*A proposal for the canonicalize agent to accept, amend or replace. Nothing in the catalog uses it yet.*

**Keys.** Keys are written as now: `` `@key` `` in backticks. Any `@key` anywhere in `source-catalog.md` puts that document in the corpus: in the bibliography, and in canonicalize's scope unless a tag says otherwise. A key mentioned in prose is written bare (`` `perset-2025-how-managing-risks` ``), so that the mention is not read as a listing.

**Status tags.** A status is a bracketed tag immediately after the key's closing backtick, on the same line:

```
`@key`                                  canonicalize (the default; no tag)
`@key` [no-canon: <reason>]             bibliography only; the reason is free text
`@key` [superseded-by: @other-key]      bibliography only; @other-key is the text to use
```

The tag can appear wherever a key appears: in a main-table `relata` cell (including cells that hold several keys), in a list item, or in a table cell elsewhere. It belongs to the one key right before it.

**A regex** that reads both forms. It extends the one `catalog_keys()` already uses:

```python
KEY = r'[A-Za-z0-9_](?:[\w:.#$%&+?<>~/-]*[\w])?'
ITEM = re.compile(r'(?<![\w@])@(?P<key>' + KEY + r')`?'
                  r'(?:[ \t]*\[(?P<status>no-canon|superseded-by):[ \t]*(?P<arg>[^\]\n]*)\])?')
```

`finditer` over the file gives `(key, status, arg)`. For `superseded-by`, `arg` is `@other-key`. Because the match consumes the tag, the `@other-key` inside it is not separately matched.

**What each status means:**

| Status | `relata emit bib` | `bin/canonicalize` | `INDEX.md` (a suggestion) |
|---|---|---|---|
| none | in `refs.bib` | canonicalized | a row with its fidelity mark |
| `no-canon` | in `refs.bib` | skipped | a row giving the reason |
| `superseded-by` | in `refs.bib` | skipped | a row naming the replacement |

**Rules I'd suggest:**
- **One status per key.** Untagged repeats of a key are harmless. Two different tags on the same key are an error.
- **A replacement is listed in its own right.** The key a `superseded-by` names must also appear in the catalog on its own, untagged. The tag doesn't bring it into scope, and chains (A superseded by B, which is superseded by C) are an error.
- **A key relata doesn't hold is an error.** A key with no document, or with no conversion yet, is reported and skipped, not fatal. On 2026-10-09, 318 of the 382 corpus-section keys had no conversion yet; most of them are in relata's queue (`relata prep list`).

**What was tested.** `relata cited` and `relata emit` read keys in the tagged form correctly. On a sample file, `emit` wrote one entry per key and treated the `@other-key` inside a tag as a mention of a key the file already lists. On the current catalog plus the §5 section, `relata emit` wrote 466 entries, with 0 missing. The regex above, run on §5, yields 382 keys, 3 of them tagged.

**Questions for the canonicalize agent** (I can't answer these from here):
1. **Is this syntax workable?** Would you rather have a status *column* in each table instead? The inline tag has two advantages: it works the same in the main table's multi-key cells and in plain lists, and it keeps the status beside the key it governs.
2. **Web pages printed to PDF.** 83 of the 382 corpus-section keys are web pages rendered to PDF, with a provenance first page. Their page numbers are rendering artefacts, by the renderers' own note. Should canonicalize recognise these by itself (the provenance page is uniform), or should the catalog say so with a tag of its own?
3. **Per-source judgments now in code or in INDEX.md.** These include `LOCAL` (a hand-made conversion for the CSB report, and the publisher's web edition for IASR 2026) and the editorial notes Joseph saw in INDEX.md. Should they move into the catalog as tags too, for example a third status naming the markdown to use? Or should they stay in code, with INDEX.md generated wholly from the catalog plus measurements?
4. **INDEX order.** Should it follow catalog order or alphabetical order? With 466 keys, alphabetical order may serve readers better. Catalog order keeps families together.

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

This replaces the catalog's "Not listed" section. Its "Not covered" line is kept, with the edit in §6, F3. Before pasting, delete from it the keys of any rows taken from §3 and §4.

```markdown
## The rest of the corpus

Every other document in relata that this repository cites, by family. Listing a document here makes `relata emit bib` put it in the bibliography and tells `bin/canonicalize` what to do with it. It says nothing about the document's reach: the *Influence* column does that for the rows above. Statuses:
- a key with no tag is canonicalized;
- a key followed by `[no-canon: <reason>]` stays in the bibliography and out of `ref/canonical/`;
- a key followed by `[superseded-by: <key>]`, the key written in the same at-sign form, does the same and names the document whose text to use instead.

Write a key with the at sign only where it is listed. A key mentioned in prose is written bare, in backticks, so that it is not read as a listing.

"Superseded" is kept for duplicates of one text. An earlier version of a document is a source in its own right here, because claims are compiled with their version and date (OVERVIEW §1.4), so earlier versions are canonicalized. A key that moves into the table above comes out of this list, so that each key's status is stated once. Where a family was mapped, the per-family atlas is named; the two relata reports of 2026-10-08 are `influx/relata-aisi-sweep-2026-10-08.md` and `influx/relata-additions-2026-10-08.md`.

### International AI Safety Report series

The full 2025 and 2026 reports are in the table above (IASR 25, IASR 26). Atlas: `source-atlas/iasr.md`.

- **Interim report and the 2025 Key Updates** (3): `@bengio-2024-iasr-interim`, `@bengio-2025-iasr-key-update-1`, `@bengio-2025-iasr-key-update-2`

### Frontier AI developers

Frameworks, their earlier versions, companion documents, system cards and posts. Atlases: `source-atlas/co-anthropic-openai.md`, `source-atlas/co-others.md`; model: `source-models/frontier-safety-frameworks.md`.

- **Anthropic (with Karnofsky's post on RSP v3)** (14): `@anthropic-2023-rsp-v1-0`, `@anthropic-2024-rsp-v2-0`, `@anthropic-2025-fcf-announcement`, `@anthropic-2025-rsp-noncompliance-policy`, `@anthropic-2025-rsp-v2-1`, `@anthropic-2025-transparency-framework`, `@anthropic-2026-constitution`, `@anthropic-2026-frontier-safety-roadmap`, `@anthropic-2026-rsp-noncompliance-policy`, `@anthropic-2026-rsp-v3-1`, `@anthropic-2026-rsp-v3-2`, `@anthropic-2026-rsp-v3-3`, `@anthropic-2026-rsp-v3-announcement`, `@karnofsky-2026-rsp-v3`
- **OpenAI (with Coggins et al. on the Preparedness Framework)** (12): `@coggins-2025-preparedness`, `@openai-2023-preparedness-framework-beta`, `@openai-2026-frontier-governance-framework-announcement`, `@openai-2026-gpt6-astra-system-card`, `@openai-2026-hugging-face-incident`, `@openai-2026-hugging-face-incident-report`, `@openai-2026-misalignment-reporting-framework`, `@openai-2026-model-spec`, `@openai-2026-pacing-model-development`, `@openai-2026-path-to-astra`, `@openai-2026-responding-critical-cyber`, `@openai-2026-third-party-assessments`
- **Google DeepMind and Google** (6): `@gdm-2024-fsf-v1-0`, `@gdm-2025-fsf-v2-0`, `@gdm-2025-fsf-v3-0`, `@gdm-2026-gemini-3-7-flash-fsf-report`, `@gdm-2026-strengthening-fsf-blog`, `@google-2026-ai-responsibility-update`
- **Meta** (1): `@meta-2025-frontier-ai-framework-feb`
- **xAI** (5): `@xai-2025-faif`, `@xai-2025-rmf`, `@xai-2025-rmf-draft-feb10`, `@xai-2025-rmf-draft-feb20`, `@xai-2026-faif`
- **Amazon, Microsoft, Cohere, G42, Magic, NAVER, NVIDIA, Samsung, Shanghai AI Lab** (15): `@amazon-2025-frontier-model-safety-framework`, `@amazon-2026-frontier-model-safety-framework`, `@cohere-2025-secure`, `@g42-2025-frontier`, `@ghosh-2025-safety`, `@magic-2024-agi-readiness`, `@microsoft-2025-frontier-governance-framework`, `@microsoft-2026-frontier-governance-framework`, `@naver-2024-asf`, `@naver-2026-asf2`, `@nvidia-2025-frontier`, `@samsung-2026-ai-safety-framework`, `@shanghaiailab-2025-frontier`, `@shanghaiailab-2025-frontier-practice`, `@shanghaiailab-2026-frontier-practice-v1-5`

### UK AI Security Institute

Its four partial models are in the table above (AISI, AISI-T, AISI-LoO, AISI-INC). Atlas: `source-atlas/uk-aisi.md`; model: `source-models/uk-aisi.md`; enumeration and provenance: the AISI sweep report.

- **Reports, guidance, priorities and joint reports (PDFs)** (15): `@aisi-2024-evals-bounty-rfp`, `@aisi-2025-challenge-fund-priority-areas`, `@aisi-2025-elicitation-protocol`, `@aisi-2025-misuse-safeguards-template`, `@aisi-2025-open-weight-checklist`, `@aisi-2025-sandboxing-technical-guidance`, `@aisi-2026-alignment-project-grants`, `@aisi-2026-openclaw-environment`, `@aisi-thorn-2025-csea-recommended-practice`, `@dsit-2023-introducing-aisi`, `@gal-2024-aisi-priority-research-areas`, `@intlnetwork-2025-joint-testing-agentic`, `@intlnetwork-2026-best-practice-automated-evaluation`, `@usaisi-ukaisi-2024-claude-35-sonnet`, `@usaisi-ukaisi-2024-openai-o1`
- **Research papers listed on aisi.gov.uk/research** (59): `@africa-2025-does`, `@africa-2026-consistency-training-entrench`, `@aisi-2025-misuse-safeguards-principles`, `@aisi-2025-white-box-control-sandbagging`, `@andriushchenko-2024-agentharm-benchmark-measuring`, `@anwar-2026-decision-theoretic-formalisation`, `@ayonrinde-2025-evaluating-explanations-explanatory`, `@ayonrinde-2025-mathematical-philosophy-explanations`, `@balesni-2024-lessons-studying-two`, `@bazinska-2025-breaking-agent-backbones`, `@black-2025-replibench-evaluating-autonomous`, `@bowkis-2026-automated-alignment-harder`, `@browncohen-2025-avoiding-obfuscation-prover`, `@buhl-2025-alignment-safety-case`, `@casper-2026-open-technical-problems`, `@che-2025-model-tampering-attacks`, `@clymer-2025-example-safety-case`, `@cooney-2026-did-you-lie`, `@davies-2025-fundamental-limitations-pointwise`, `@davies-2026-boundary-point-jailbreaking`, `@dubois-2025-skewed-score-statistical`, `@dubois-2026-ask-don-t`, `@dubois-2026-seven-simple-steps`, `@feng-2025-existing-large-language`, `@folkerts-2026-measuring-ai-agents`, `@gausen-2026-realitytest-people-probe`, `@goemans-2024-safety-case-template`, `@hackenburg-2025-levers-political-persuasion`, `@heitmann-2025-understanding-ai-trajectories`, `@hilton-2025-safety-cases-scalable`, `@jarviniemi-2026-propensity-inference-environmental`, `@kirk-2025-human-ai-relationships`, `@kirk-2026-evaluating-whether-ai`, `@korbak-2025-chain-thought-monitorability`, `@korbak-2025-evaluate-control-measures`, `@korbak-2025-sketch-ai-control`, `@lindner-2025-practical-challenges-control`, `@luettgau-2025-conversational-ai-increases`, `@luettgau-2025-hibayes-hierarchical-bayesian`, `@mai-2026-multi-turn-framework`, `@makins-2026-multi-agent-ai`, `@marchand-2026-quantifying-frontier-llm`, `@mckenzie-2025-stack-adversarial-attacks`, `@obrien-2025-deep-ignorance-filtering`, `@pilditch-2026-knowing-stop-bayesian`, `@pilditch-2026-transect-retaining-observability`, `@rivera-2026-item-response-theory`, `@rosser-2026-infusion-shaping-model`, `@slama-2026-llm-preferences-predict`, `@souly-2025-poisoning-attacks-llms`, `@souly-2026-evaluating-whether-gpt`, `@souly-2026-uk-aisi-alignment`, `@stein-2026-ai-agents-used`, `@stickland-2025-async-control-stress`, `@summerfield-2025-lessons-chimp-ai`, `@tan-2025-inoculation-prompting-eliciting`, `@tice-2026-alignment-pretraining-ai`, `@wang-2026-prefill-awareness-large`, `@zou-2025-security-challenges-ai`
- **Blog posts and web pages, rendered to PDF** (39): `@aisi-2024-approach-evaluations`, `@aisi-2024-behave-like-people`, `@aisi-2024-early-lessons-evaluating`, `@aisi-2024-evaluations-may-update`, `@aisi-2024-fourth-progress-report`, `@aisi-2024-fsf-conference`, `@aisi-2024-long-form-tasks`, `@aisi-2024-qa-evaluations-insights`, `@aisi-2024-safety-cases`, `@aisi-2024-systemic-safety-grants`, `@aisi-2025-alignment-project-agenda`, `@aisi-2025-capabilities-mitigations-gap`, `@aisi-2025-crimes-future`, `@aisi-2025-misalignment-investigation`, `@aisi-2025-open-weight-risk`, `@aisi-2025-poisoning-blog`, `@aisi-2025-societal-resilience`, `@aisi-2025-strengthening-resilience`, `@aisi-2025-transcript-analysis`, `@aisi-2026-cheating`, `@aisi-2026-cloud-misconfigurations`, `@aisi-2026-control-red-team`, `@aisi-2026-cyber-horizons`, `@aisi-2026-gpt55-cyber`, `@aisi-2026-inference-scaling-cyber`, `@aisi-2026-labour-market-assessment`, `@aisi-2026-mcp-tools`, `@aisi-2026-mythos-preview-cyber`, `@aisi-2026-network-consensus`, `@aisi-2026-open-weight-cyber`, `@aisi-2026-productivity-gains`, `@aisi-2026-propensity`, `@aisi-2026-sabotage`, `@aisi-2026-sandbox-discovery`, `@aisi-2026-sandbox-escape`, `@aisi-2026-secure-ai-infrastructure-cfi`, `@aisi-2026-secure-eval-environment`, `@aisi-2026-test-time-compute`, `@aisi-caisi-2026-kimi-k3`
- **AISI-affiliated papers that AISI does not list** (46): `@africa-2026-detecting-csam-text`, `@ahlqvist-2026-improving-evaluation-realism`, `@balesni-2024-evaluations-based-safety`, `@barez-2025-open-problems-machine`, `@barkan-2025-large-language-models`, `@bean-2025-measuring-matters-construct`, `@betley-2025-emergent-misalignment-narrow`, `@betley-2025-tell-me-about`, `@browncohen-2026-debate-efficient-time`, `@chan-2023-hazards-increasingly-accessible`, `@chanin-2024-absorption-studying-feature`, `@dasilva-2024-safety-ai-national-labs`, `@dhoot-2026-character-training-risk`, `@dohnany-2025-technological-folie-deux`, `@duzan-2026-chain-thought-monitoring`, `@dziemian-2026-vulnerable-ai-agents`, `@gal-2025-customizable-ai-risks` [no-canon: metadata only; Nature paywalled the text], `@gardnerchallis-2026-trust-untrusted-monitoring`, `@gausen-2026-disclosure-design-identity`, `@golechha-2025-among-us-sandbox`, `@graham-2025-contextbench-modifying-contexts`, `@hackenburg-2026-ai-systems-out`, `@hackenburg-2026-artificial-intelligence-persuade`, `@hadida-2026-behavioural-analysis-alignment`, `@hills-2026-distributed-attacks-persistent`, `@ibrahim-2025-measuring-mitigating-overreliance`, `@ibrahim-2026-sycophantic-ai-makes`, `@kapoor-2026-open-world-evaluations`, `@kirgis-2026-ai-agents-conduct`, `@kirgis-2026-log-analysis-necessary`, `@kirk-2025-neural-steering-vectors`, `@kirk-2026-prism-x-experiments`, `@levy-2026-forecasting-future-behavior`, `@li-2026-evaldetectbench-benchmark-measuring`, `@luettgau-2025-people-readily-follow`, `@mohl-2026-automated-transcript-analysis`, `@nie-2024-secodeplt-unified-platform`, `@obrien-2026-inoculation-midtraining-learned`, `@rottger-2026-measuring-mitigating-persona`, `@summerfield-2024-will-advanced-ai`, `@taylor-2025-auditing-games-sandbagging`, `@voudouris-2026-judge-hacking-debate` [no-canon: metadata only; SSRN refused the download], `@wang-2026-scarce-scalable-cascade`, `@weilnhammer-2026-clinically-validated-framework`, `@yadav-2026-more-capable-less`, `@zhu-2025-establishing-best-practices`
- **Progress reports of the Frontier AI Taskforce and early AISI** (3): `@aisi-2024-third-progress-report`, `@dsit-2023-taskforce-first-progress`, `@dsit-2023-taskforce-second-progress`

### UK government, NCSC, Five Eyes partners, and the UK-hosted summits

Atlas: `source-atlas/uk-gov.md`.

- 19 keys: `@asd-2026-careful-agentic`, `@bletchley-2023-declaration`, `@dsit-2024-frontier-ai-safety-commitments`, `@dsit-2025-ai-cyber-cop`, `@dsit-2025-ai-cyber-cop-guide`, `@dsit-2025-cyber-governance`, `@etsi-2025-en304223`, `@fiveeyes-2026-ai-shift`, `@ncsc-2023-guidelines-secure-ai`, `@ncsc-2024-near-term`, `@ncsc-2025-bugs-to-bypasses`, `@ncsc-2025-prompt-injection`, `@ncsc-2026-defend-agentically`, `@ncsc-2026-frontier-defenders`, `@ncsc-2026-managing-agentic`, `@ncsc-2026-patch-wave`, `@ncsc-2026-retaining-advantage`, `@ncsc-2026-ten-questions`, `@ncsc-2026-thinking-agentic`

### US government

Atlas: `source-atlas/us-gov.md`.

- 29 keys: `@caisi-2026-glm52`, `@colorado-2024-sb24-205`, `@colorado-2026-sb26-189`, `@dhs-2024-ai-roles-framework`, `@eo-2023-14110`, `@eo-2025-14179`, `@eo-2025-14365`, `@eo-2026-14409`, `@nist-2025-caisi-kimi-k2`, `@nist-2025-caisi-openai-anthropic`, `@nist-2026-agent-standards`, `@nist-2026-ai-800-4`, `@nist-2026-ai-800-4-release`, `@nist-2026-ai-consortium`, `@nist-2026-aisi-caisi-kimi-k3` [superseded-by: @aisi-caisi-2026-kimi-k3], `@nist-2026-caisi-agreements`, `@nist-2026-caisi-careers`, `@nist-2026-caisi-deepseek-v4`, `@nist-2026-caisi-glm53`, `@nist-2026-caisi-redteam`, `@nist-2026-caisi-transcripts`, `@nist-2026-intl-network`, `@nist-2026-nccoe-agent-identity`, `@nist-2026-vassilev-proof`, `@nist-2026-vcat-ai-update`, `@nist-caisi-page-2026`, `@vassilev-2025-adversarial`, `@whitehouse-2026-legislative-framework`, `@whitehouse-2026-nspm-11`

### EU, other governments, and intergovernmental bodies

Atlas: `source-atlas/intl-eu.md`.

- 18 keys: `@cac-2023-interim-measures-genai`, `@caisi-ca-2026-evaluators-share`, `@caisi-ca-2026-landing`, `@csa-2026-securing-agentic-addendum`, `@csa-farai-2025-securing-agentic`, `@ec-2025-gpai-serious-incident-template`, `@imda-2026-mgf-agentic-v1-5`, `@ised-2023-voluntary-code-genai`, `@jaisi-2025-national-status`, `@korea-2025-ai-framework-act`, `@korea-2026-ai-framework-act-decree`, `@oecd-2024-defining-ai-incidents`, `@oecd-2024-future-ai-risks`, `@oecd-2026-haip-reporting-v2`, `@tc260-2024-ai-safety-governance-framework`, `@tc260-2025-ai-safety-governance-framework-2`, `@tfs-2025-protecting-gpai`, `@unhlab-2024-governing`

### Industry bodies and METR

- 5 keys: `@fmf-2024-components`, `@fmf-2024-foundational-security`, `@fmf-2025-risk-taxonomy-thresholds`, `@metr-2023-rsp`, `@owasp-2025-agentic-top10`

### Loss of control, systemic risk, and governance literature

Atlases: `source-atlas/lit-a.md`, `source-atlas/lit-b.md`.

- 23 keys: `@barrett-2025-stampstpa`, `@bollinger-2026-signals`, `@brundage-2026-frontier`, `@buhl-2024-safety`, `@chin-2026-reframing`, `@cltr-2026-loc-incidents-worsening`, `@greenblatt-2023-ai-control`, `@gruetzemacher-2026-loss`, `@hamin-2025-cheating`, `@hammond-2025-multi`, `@kasirzadeh-2024-types`, `@kierans-2025-catastrophic`, `@mylius-2025-systematic`, `@ren-2024-safetywashing`, `@schuett-2023-best`, `@shaffershane-2026-scheming-wild`, `@sharma-2026-whos`, `@stix-2025-behind`, `@tkeshelashvili-2026-loc-iw`, `@vaintrob-2023-beware-safety-washing`, `@voudouris-2026-alignment-human`, `@yampolskiy-2016-taxonomy`, `@zwetsloot-2019-thinking`

### Alignment, agency, and role vocabulary

Most are cited by `spikes/spike-alignment-referents-2026-10-06/`.

- 48 keys: `@aguirre-dempsey-surden-reiner-2020-ai-loyalty`, `@askell-2021-general`, `@benthall-shekman-2023-fiduciary`, `@bernheim-whinston-1986-common`, `@cai-2025-getting`, `@carlsmith-2022-power-seeking`, `@chan-2024-visibility`, `@chan-2025-infrastructure`, `@christiano-2018-clarifying`, `@conitzer-2024-social`, `@critch-2020-arches`, `@critch-russell-2017-servant`, `@diaz-2025-secure-agents`, `@edelman-2025-full-stack`, `@feng-2026-decomposing`, `@fickinger-2020-multi-principal`, `@friedman-kahn-borning-2006-value`, `@gabriel-2020-artificial`, `@gabriel-2024-ethics`, `@hadfield-menell-hadfield-2019-incomplete`, `@hellrigel-holderbaum-2025-misalignment`, `@huang-2026-loyal`, `@hubinger-2020-clarifying`, `@jensen-meckling-1976-theory`, `@ji-2023-alignment`, `@kasirzadeh-gabriel-2023-conversation`, `@kenton-2021-alignment`, `@kierans-2024-quantifying`, `@klingefjord-2024-human`, `@kolt-2025-governing`, `@kolt-2026-caputo`, `@korinek-balwit-2022-aligned`, `@lacroix-2026-relative`, `@leike-2018-scalable`, `@mishra-2023-ai`, `@mitchell-agle-wood-1997-toward`, `@ngo-2022-alignment`, `@rfc-2020-8693`, `@riedl-desai-2025-agents`, `@shavit-2023-practices`, `@shen-2024-towards`, `@sorensen-2024-roadmap`, `@w3c-2013-prov-dm`, `@wallace-2024-instruction`, `@yang-2026-multi-user`, `@zhang-2026-many-tier`, `@zhixuan-2024-beyond`, `@zverev-2024-separate`

### Risk analysis, safety science, and risk vocabulary

Most are cited by `gamma-research/risk-formalisms.md`. The precedents from other high-hazard industries are in the table above.

- 18 keys: `@bommasani-2021-opportunities`, `@caa-2026-hydrogen-bowtie`, `@chu-2026-systematic`, `@cobbe-2023-understanding`, `@hopkins-2025-supply`, `@hse-2001-r2p2`, `@ieee-7009-2024-fail-safe-autonomous`, `@ipcc-2022-ar6-wg2-annex-ii`, `@kaplan-garrick-1981-quantitative`, `@koessler-2023-risk`, `@leveson-thomas-2018-stpa`, `@nist-2012-sp800-30r1`, `@nolte-2025-review`, `@reason-2000-human`, `@salem-2024-risk`, `@schnitzer-2023-hazard`, `@sra-2018-glossary`, `@un-2016-a71644`

### Press

Cited for dates and attribution. Atlas: `source-atlas/safety-science-press.md`.

- 4 keys: `@abc-2026-anthropic-appeal`, `@cnbc-2026-anthropic-appeal`, `@npr-2026-anthropic-ruling`, `@npr-2026-anthropic-scr`

**Not covered** (as model-alpha noted, and still true): ISO/IEC 42001 and 23894 (paywalled). Non-English sources are covered only where an official English text or translation exists: Korea's AI Basic Act and Decree (KLRI translations), TC260's framework (2.0 is bilingual). CAC's *Interim Measures* are held in Chinese only.
```

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

**F5. A possible duplicate.** `nist-2026-aisi-caisi-kimi-k3` and `aisi-caisi-2026-kimi-k3` are the same joint UK AISI / CAISI assessment, rendered from NIST's site and from AISI's. Their word sequences agree at 0.85 (difflib ratio). The difference looks like site navigation and AISI's cookie banner, but I haven't read the two side by side. §5 tags the NIST copy `superseded-by` the AISI one. The AISI render has the cookie banner interleaved word by word (source-atlas/uk-aisi.md), so the NIST copy may be the cleaner text. Reverse the tag if so.

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
