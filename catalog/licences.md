# Source licences

`licences.yaml` records, for each of the 472 keys in `source-catalog.md`, what its licence or terms let a public repository do with the text: commit it whole, quote at length, quote briefly, and on what conditions. It gives the evidence (the statement quoted, and where it was found) and a confidence. It was compiled on 2026-10-10 as a step before deciding which sources' verbatim text may be committed, for example cut into one file per citable unit, and which may only be quoted. It records what sources and publishers say, plus general rules applied where they say nothing. It is not legal advice.

The field `stated` separates the two kinds of finding:
- a licence found in the document, on the publisher's page, or in the arXiv or Crossref record;
- a licence applied by a general rule (`stated: no`), such as US federal works under 17 U.S.C. §105, state statutes under the edicts doctrine, or the OGL as the default for Crown copyright.

## What it says

| Whole text may be committed | Licence found | Rule applied | Keys |
|---|---|---|---|
| yes | 201 | 75 | 276 |
| conditional (non-commercial, unmodified, or notices carried) | 16 | 0 | 16 |
| no | 96 | 64 | 160 |
| unknown | 9 | 11 | 20 |

By kind of source:
- **Papers.** 185 have arXiv records. 123 are CC BY 4.0, and 48 are under arXiv's own licence, which grants nobody but arXiv. The rest are CC0 (3), BY-SA (2), BY-NC-SA (4) and BY-NC-ND (5). Older journal articles are under ordinary copyright. Seven papers have an arXiv licence that disagrees with the PDF (below).
- **UK government.** GOV.UK documents print the Open Government Licence, as do NCSC's site terms. aisi.gov.uk states nothing anywhere, so its 53 keys are OGL by default, applied.
- **US federal works.** Public domain: NIST states this for its technical series, whitehouse.gov and govinfo for their documents, and §105 is applied for CISA, DHS, CSB and Commerce. Some NIST documents have non-federal co-authors, which §105 doesn't reach.
- **Companies, think tanks and press: mostly no.** Of 103 such keys, 58 state nothing (default copyright, applied), and the rest reserve rights, some explicitly against online posting:
  - RAND: "Unauthorized posting of this publication online is prohibited".
  - Microsoft and the Frontier Model Forum: copies must "not be copied or posted on any network computer".

  The exceptions:
  - Claude's constitution and OpenAI's Model Spec (CC0);
  - EA Forum posts (CC BY 4.0);
  - OWASP (CC BY-SA 4.0);
  - CSET's 2021 brief (CC BY-NC 4.0).
- **EU and international.** The AI Act and the Omnibus fall under the EU reuse decision, and the Commission's documents are CC BY 4.0. Two OECD papers are CC BY 4.0, as is Australia's ASD. ICAO, IAEA, ETSI, IMDA, CSA, the UN advisory report, the IPCC glossary and KLRI's translations of the Korean laws reserve their rights.

The five Au5 sources:
- **IASR 2026:** yes, CC BY 4.0 on arXiv, and the web edition we hold says OGL.
- **SB 53:** yes, edicts doctrine, applied.
- **EU Code of Practice:** yes, under the Commission's CC BY 4.0 notice. Medium confidence, because the notice covers "content owned by the EU", and nothing found says the EU owns text written by the independent chairs.
- **AISI's Frontier AI Trends Report:** yes, OGL applied, medium confidence.
- **Anthropic's August Risk Report:** no; nothing states a licence.

## Where it is uncertain

- **aisi.gov.uk (53 keys).** The site has no copyright or licence statement on any page found, and the OGL attaches to material "expressly made available" under it. One request to AISI or DSIT to confirm OGL v3.0 for the site would settle all of them.
- **arXiv licence against the PDF (7 keys).** In each of these the arXiv record and the PDF disagree. `republish_full` is not "yes" for any of them until resolved.
  - shah-2025 and gabriel-2024 print "© Google DeepMind. All rights reserved".
  - africa-2025 prints AAAI's reservation.
  - benthall-2023, chan-2024 and cobbe-2023 carry ACM permission blocks.
  - hacker-2026's arXiv record says CC BY 4.0, while its PDF and the ACM version of record say CC BY-NC-ND 4.0.
- **Joint and commissioned works.** One government's licence can't cover the other authors' shares in:
  - the International Network reports;
  - the AISI–Thorn practice;
  - the US–UK pre-deployment tests;
  - the Five Eyes statement;
  - NIST AI 100-2e2025;
  - the DOE national-labs report, whose authors are contractors;
  - the Kainos guide that DSIT commissioned.
- **Unresolved rules.**
  - Whether China's exclusion for official documents reaches TC260's frameworks.
  - What replaced the UN's 1987 rule for documents with a UN symbol.
  - Japan's AISI, where the only terms found are its parent agency's.
  - The CSA/FAR.AI paper, where the two co-publishers' terms disagree.
- **Old notices against current site terms.** NPSA's Secure Innovation booklet is under the OGL by site terms but marked "supplied in confidence" in the document. HSE's 2001 and 2003 notices are narrower than its current OGL statement.
- **Papers whose held copy is not the arXiv PDF (19 keys).** A CC licence on arXiv covers the arXiv text, which may differ from ours.

## What bears on cutting texts into units

- **Splitting.** CC BY, BY-SA, BY-NC and BY-NC-ND 4.0 all allow sharing "in whole or in part" (§2(a)(1)(A)), so per-unit files of unmodified text are within them.
- **Text that must stay unmodified** (BY-NC-ND, the IETF and W3C licences, the STPA handbook's terms):
  - cleaning the converted text inside a unit counts as modifying it;
  - the IETF's notices must travel with the units once they hold more than a fifth of the RFC.
- **ShareAlike** (OWASP, six arXiv papers) may reach commentary placed in the same file as the text. Commentary in a separate file avoids the question.
- **Non-commercial licences** (CSET, Canada's ISED, ten papers). Whether this repository's use is non-commercial is a judgment for Joseph.
- **The OGL.** It allows adaptation, asks for no implied endorsement, and lets one attribution page serve many files.
- **The repository has no LICENSE file.** Mixed licences mean marking each committed file's licence.
- **Material the licences exclude:**
  - third-party figures, stock images, logos and personal data inside OGL documents;
  - other users' comments and site navigation in the rendered web pages.

  Committing text only, with the page furniture stripped, avoids most of it.

## Problems found in the catalog and the held copies

- **Dead URLs.**
  - `xai-2025-rmf-draft-feb10` returns 404 (a Wayback copy exists).
  - `meta-2025-frontier-ai-framework-feb` returns 500.
- **URLs that point at a third-party corpus.** `meta-2025-frontier-ai-framework` and `microsoft-2025-frontier-governance-framework` point at a GitHub corpus whose NOTICE excludes the provider documents from its own licence.
- **Copies from third-party hosts.**
  - `ny-2026-raise-s8828` comes from a law firm's site.
  - `icao-2018-doc9859-smm` comes from a third-party host, and is the advance unedited edition.
  - The NSPM-11 text comes from a mirror.
- **`eu-cop-chairs-2025-statement`** holds the whole Safety & Security chapter as code-of-practice.ai renders it, not just the four-page statement. That site's maintainer is one of the statement's authors and has not licensed it.
- **Text that needs trimming.** `nist-2026-rfi-agents` includes unrelated Federal Register notices.
- **No canonical text.** `tc260-2025-…-2` has none, though relata holds its PDF.
- **Better sources exist for two keys.**
  - `voudouris-2026-alignment-human`: the full paper is CC BY 4.0 on PsyArXiv, while we hold only AISI's abstract page.
  - `hilton-2025-safety-cases-scalable`: also on arXiv, under CC BY-NC-SA 4.0.

## Updating it

Each entry names its evidence and where it was found, with the fetch date. A licence that changes, or a permission granted on request, should replace that entry's evidence, not be added beside it. Several "no" entries may be one email from changing. Some entries' notes say who could grant permission: AISI or DSIT for the aisi.gov.uk pages, code-of-practice.ai's maintainer for the chairs' statement, KLRI, and the UN's permissions office.
