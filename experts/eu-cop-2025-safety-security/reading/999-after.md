# After the reading

*Written 2026-10-09, straight after unit 124, before reading anything else about the source. Unlike the per-unit files, this one is a look back over the whole. It's still my own reading and not a verified extraction: everything in it comes from the unit files, which quote the canonical text; where I'm unsure, it says so. For anything that matters, the unit files and the text itself are the authority.*

## What the reading was like

- **My training holds the Code's skeleton almost exactly, and its substance much less.** I predicted many headings, numbers and phrases word for word: the names of the recitals, the five C3 elements, the safety-margin triad, the 2/5/10/15-day incident deadlines, "20 business days", the four specified risks. The surprises were all at the level of the clause and the definition. So the skip reflex here fires on headings. The places I'd have been most wrong had I skipped are the ones whose titles felt most familiar.
- **The Glossary changed my reading of the body more than any other part.** It comes after the operative text and quietly redefines words that read as soft or narrow:
  - 'appropriate' is demanding: "suitable and necessary…", reached through best practice, the state of the art, or beyond it;
  - 'including' is a minimum;
  - 'insider threats' covers AI models (self-exfiltration) and senior management;
  - 'non-state external threats' is quantified;
  - 'use' covers the signatory's own use;
  - 'model' means all of a model's versions, taken together;
  - 'systemic risk mitigations' include governance;
  - 'state of the art' sits above 'best practice'.

  A reader of the body alone would misread the Code in a consistent direction: as weaker and narrower than it is.
- **Where it slowed me down:** recital (a)'s burden of proof; M4.2's "only proceed"; the Glossary; Appendix 1.4(2). **Where my attention thinned:** the governance prose of C8 (I said so at unit 63) and the security checklists of Appendix 4. Read those again before answering detailed questions about them.

## Corrections I made while reading (each is in its unit file)

- Unit 9: I took the precautionary principle to apply only to identification. M4.2 applies it to the go/no-go decision too ("reasonably foreseeable to be soon not determined to be acceptable").
- Unit 13: I thought the forecasting requirement went silent at a top tier. M4.1(1)(a)(iii) requires at least one tier not yet reached.
- Unit 27: my gloss of 'model-independent information' was wrong. The Glossary's definition is "not tied to a specific model". Training-data review sits awkwardly under M3.1.
- Unit 45: I thought the Code defines security only by threat-actor *type*. 'non-state external threats' is quantified: roughly ten professionals, several months, up to EUR 1 million, existing infrastructure, no prior access.
- Unit 45 again: I predicted the Code wouldn't name RAND. M7.3(3)(c) names the RAND *Securing AI Model Weights* report.
- Unit 53: I first over-read external evaluators as reporting their findings directly to the AI Office. The direct route concerns access-and-resources information; their findings come through M7.4.
- Units 47 and 85: "no Model Report for internal-only models" stands. But 'use' includes the signatory's own use, so the substantive rules (the Framework, "only proceed", what the Model Report must describe) do reach internal use.
- Unit 105: I thought Appendix 2.2 lacked a safety margin. Unit 106 requires "a sufficiently wide safety margin".

## Where things live (for forks)

- **Loss of control** is spread across at least seven places:
  - Appendix 1.4(2), the definition: "Risks from humans losing the ability to reliably direct, modify, or shut down a model";
  - Appendix 1.3.1–1.3.2, its sources;
  - the Glossary entries 'deception', 'insider threats' and '(self-)exfiltration of model weights';
  - M5.1(8), defending against a model subverting its own mitigations;
  - M4.1, the safety margin's "subverted";
  - M9.3(2), where self-exfiltration is a reportable breach;
  - Appendix 4.4, sandboxes and sabotage by models.

  In the definition, keep "humans", "reliably" and "the ability". Those are the points where paraphrases drift.
- **Internal deployment:** the substantive rules reach it. That means the Framework, the go/no-go rule, the Model Report's description of use (including AI R&D), incident reporting "along the entire model lifecycle", and 'use' as defined. The procedural clocks and documents are anchored to market placement:
  - the full assessment "at least before placing the model on the market";
  - the Model Report;
  - the 12-month and six-month clocks;
  - post-market monitoring;
  - access for external evaluators to the most capable *marketed* version.
- **Marginal risk and baselines:**
  - C6's exemption from security duties for models whose capabilities are inferior to at least one open-weight model;
  - Appendix 2: a safe reference model (marketed before the Chapter was published, or assessed under it; with visibility into it, which means the signatory's own models or models with parameters available); similarly safe or safer (scenarios, light-weight benchmarks, characteristics, a safety margin).

  Appendix 2 lightens the duties in M3.5, M7.6, M10.2 and Appendix 3.5, and its use must be justified in the Model Report (M7.3(1)(h)).
- **What reaches the public and what reaches only the AI Office:**
  - Frameworks and Model Reports go to the AI Office, confidentially under Art. 78. They're unredacted, except for redactions national-security law requires in Model Reports (M7.7).
  - The public gets summaries "if and insofar as necessary" (M10.2), the published criteria for selecting evaluators (M3.5), the responsible-disclosure procedure (M3.5), the whistleblower policy (suggested in M8.3(6)), and the model spec if it's hyperlinked.
- **The numbers**, from the unit files. The section and unit are given so each can be checked.

| What | Number | Where (unit) |
|---|---|---|
| Framework confirmed | ≤ 4 weeks after the Art. 52(1) notification, and ≤ 2 weeks before market | M1.1 (14) |
| AI Office's access to the Framework | within 5 business days of confirmation | M1.4 (21) |
| Framework assessment | every 12 months from market placement, or sooner on grounds | M1.3 (18) |
| Delay or block on publishing evaluators' findings | ≤ 30 business days, "unless… exceptionally necessary" | M3.5 (35) |
| Model Report | by market placement; an update within 5 business days of confirmation; delay ≤ 15 business days, with an interim report | M7.7 (60) |
| Periodic Model Report update | at least every 6 months for models "amongst their respective most capable" (with exceptions) | M7.6 (58) |
| Development look-ahead | next six months | M7.3(4) (54) |
| Evaluation samples | at least five, random, per relevant evaluation | M7.3(1)(f) (52) |
| First report on a serious incident | 2 days (critical infrastructure) / 5 (cyber, incl. self-exfiltration) / 10 (death) / 15 (other serious harm) | M9.3 (73–74) |
| Intermediate and final incident reports | at least every 4 weeks; final ≤ 60 days after resolution | M9.3 (74–75) |
| Retention | incident documentation ≥ 5 years; documentation in general ≥ 10 years after market | M9.4 (76), M10.1 (78) |
| Evaluation time | "for example… at least 20 business days" | App. 3.4 (112) |
| Search for an external evaluator | e.g. a public call open for 20 business days | App. 3.5 (114) |
| Minimum non-state attacker | ~10 professionals, several months, ≤ EUR 1M | Glossary (83) |
| Encryption of weights | ≥ 256-bit, keys on a TPM | App. 4.2 (118) |
| Review of authorised access to weights | at least every 6 months | App. 4.3 (120) |
| Losing a safe reference model | 6 months to find another or apply everything in full | App. 2.2 (106) |

## Conversion issues noticed (check against the PDF before quoting)

- The **LEGAL TEXT** lines of C1 (unit 11) and C10 (unit 77) have lost article and recital numbers.
- The "ADDITIONAL LEGAL TEXT: Recital 110 AI Act" heading in Appendix 1 has no text after it (unit 88). The PDF may only name the recital.
- Hyphens lost at line breaks: "systemic-riskproducing" (64), "generalpurpose" (88), "selfreasoning" (100).
- Spaces missing: "(10)collecting" and "(11)monitoring" (32), "Chapter(as" (77).
- Some sentences are split across lines at page breaks (28, 54).
- "The safety margin will:" is rendered as a heading (39).
- Glossary table rows are split, and some words sit one per line (81–84).
- The figures exist only as jpegs in `ref/canonical/msc/eu-cop-2025-safety-security/` (note 031a).

## Open questions I couldn't settle from the text

- What "acceptable" means. It isn't defined; it rests on each signatory's justified criteria (M4.1).
- Whether "if and insofar as necessary" in M10.2 makes publication the norm for frontier models. The exemptions suggest it does; the text doesn't settle it.
- Whether "publishing… to competent authorities" in M8.3(7) covers public disclosure.
- Whether the cyber-breach incidents in M9.3 widen the AI Act's Art. 3(49) "serious incident". I haven't read the Act's text in this session.
- Whether "non-human welfare" (Appendix 1.1) includes AI systems.
- Whose control and whose intent and values are meant: "humans" is unqualified in Appendix 1.4(2) and Appendix 1.3.2.
- What the "exceptional circumstances" that excuse missing incident deadlines (M9.3) are.
- How post-market monitoring ends for an open-weight model ("retirement… from being made available").

## Judgment calls and what they cost

- **Unit size:** at least 150 words, 124 units. Some units were single headings, which I combined into one file. Some ran past 150 words because the tool doesn't cross headings. I don't think anything was too coarse to reflect on. The cost: within long Measures I reflected on several clauses at once.
- **Read everything:** recitals, Glossary, every appendix. I skipped nothing.
- **Figures:** I missed them on first pass (the tool then dropped them; it has since been fixed). I looked at them after unit 32, at Joseph's prompt.
- **Material I avoided:** Grok's judgements on this source, `influx/source-models/`, the atlas, anything else in the repo about the Code, and the Chairs' statement. All still unread.

## Since then (same day)

- `after-1-ai-act-anchors.md`, from the Act's text and a PDF check:
  - The C1 and C10 LEGAL TEXT damage is confirmed as conversion loss, and the full lines are given there.
  - The recital 110 heading is empty in the PDF too.
  - Art. 3(49) is defined for AI *systems* and has no cybersecurity category, so the Code's "serious cybersecurity breach" category is an addition.
  - The development / market / use triad comes from Art. 55(1)(b).
  - Art. 2(3) excludes AI systems used *exclusively* for military, defence or national-security purposes.
  - The loss-of-control formula is the Code's own; recital 110 has only "unintended issues of control relating to alignment with human intent".
- `after-2-chairs-statement.md`, from the Chairs' statement:
  - It assumed "about 5-15 providers".
  - It asks for a review cadence (e.g. every 2 years), a dedicated whistleblower channel, staffing, a foresight unit, and international engagement.
  - The source also carries a web edition of the Chapter, labelled "FINAL VERSION · 10/07/2025", which differs from the official text in Appendix 2.2(2)–(3), M7.2(3), and the titles of Commitment 10 and M10.1.
