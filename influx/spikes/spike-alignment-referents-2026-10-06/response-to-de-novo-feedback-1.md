# Response to `de-novo-feedback-1.md`

*For Joseph, from the spike's author, 2026-10-06. I re-checked each correction at the source before accepting it. The coordinator had independently checked two of them.*

## What I accepted and changed

| # | Finding | Checked at | Change |
|---|---|---|---|
| 1.1 | OpenAI does not file subversion two ways. The PF's heading is "C.2 Safeguards against a misaligned model", and subversion is one cause inside it. The Model Spec's "Misaligned goals" includes "due to misalignment … or being misled by a third party". In both, the state contains the origin | pf-v2 L871–875; Model Spec (downloaded) | `03` §3 rebuilt. The "one developer, two filings" claim is deleted. The disagreement is now stated as state vs. origin, and as where the cause enters the stack (weights vs. context). The misreading came from the literature report. I had "confirmed" it by finding the phrase, not by checking what the passage says. |
| 1.2 | GDM files injection (§6.4: "Even if the AI system is not misaligned …") and jailbreaks (§5.3.2, under misuse), and calls its areas "not a categorization" | shah L4658–4659, L3209, L192 | `03` §3 cites both. "Partitions" are now called groupings defined against a referent, with GDM's mitigation basis stated |
| 1.3 | The corpus does discuss conflict rules, and the Singapore quote was cut before its "However …" | md 1906–1908; sg2026 L1427–1431 | `03` §2 now separates definitions (no rule) from bodies (several rules) and from the companies' documents (operative rules). The Singapore quote is restored in full; it no longer serves as evidence for the society row |
| 1.4 | EU guidelines fn 12 attributes the modification act by control, and ⅓ is an "indicative criterion" | gpai-guidelines L779–806 | `04` §3 and §5: **control** added as its own operative-fact type, and "significant change" given as the rule. This strengthens the conferral picture rather than breaking it |
| 1.5 | AISI pools "scaffolding developer or fine-tuner" | LoO L2767 | `04` §3 corrected |
| 2.1 | The degeneracy conclusion overreached (counter-example); glossaries are sense reports; OECD uses "and" | the passages | `03` §2: the conclusion is narrowed to the three failure conditions, and the argument is aimed at disjunctions inside claims. The glossaries are recognised as sense reports, which §5's implicit-argument analysis vindicates. `01` §2 corrected |
| 2.2 | The no-go rows are uneven. Society and law were indeterminacy, not "aligned". The developer row is conditional. The agent row was uncounted. Ren names no risk. Gabriel and Keeling over-include | shah L2630–2645 (Paternalism); EO L31–35; FLI winter L4976–4977; davidson L86–94 | `03` §4 table redone: seven rows, conditions stated, Ren removed. Society now rests on GDM's Paternalism scenario. Law rests on the EO's attributed claim; the CAISI/PRC pair is marked as needing an uncorpused premise. The developer row uses Davidson's head-of-state case. "Misaligned *simpliciter*" is added as a cost |
| 2.2 (meta) | Adopt a declared, versioned, set-valued candidate set, not per-record S | — | Adopted as a proposal (`03` §4, §8; integration plan item 1) |
| 2.3 | Granularity: §5 vs. §8 pulled in opposite directions | — | Three recording levels (`03` §5, §8; `05` §E) |
| 2.4 | "Judge" merged the normative judge and the measurement procedure | — | Split: CAISI's scorer moved to methodology (`02`, `05`, `03` §8) |
| 3.1 | "95% absolute" merged anaphoric and generic uses | sg2025 L718–723; stix L1454–1455 | **Anaphoric** use type added. The claims are restated as "almost never followed by a complement". Singapore and Stix reclassified |
| 3.2 | The pilot: S excluded the agent; the coding rule deferred admissibility; the I/L boundary was unstable; IASR counted twice | — | Numbers withdrawn as a result (`data/` status note, `03` §5). The mechanism (a stated harm carries the verdict) is kept as a recording rule |
| 4.1 | "Standing mismatch" merged attribution, force and epistemic status; compaction is epistemic, and its writer is unknown | aisi-2026-incident L804–808 | Coinage withdrawn. `03` §6.2 rewritten around the map's own word, *provenance* |
| 4.2 | The relation lists were inconsistent across files | — | One list of eight, in `03` §6.1; the others point to it |
| 4.3 | Agent-with-interests claim too strong; Stix doesn't support raters' own aims; ETSI pre-judged; Mitchell, Agle & Wood mapping wrong; AI Act users nuance; writer counts | slattery L463; aug L7046–7048; act L5586–5588, L9189–9191 | All corrected in `04`, `06` and the debrief. Mitchell, Agle & Wood checked only via secondary sources: urgency means immediacy, so it maps to none of the relations |
| §6 | The 80% figure is one model and second-hand; "any plausible intent" is an inference; NIST's "one sentence"; Amazon is an activity sense | LoO L1439–1441 | Corrected in `03` and the debrief |

## What I contest, or accept only in part

- **§1.2, "an alternative explanation (mitigation purpose) isn't considered".** I accept it as an explanation of *why* GDM groups as it does. I keep the narrower claim: GDM's *definitions* are developer-relative, so membership by those definitions moves with the referent, whatever purpose drove the grouping.
- **§4.1, the three confusions as independent.** I accept that they are three, and the coinage is withdrawn. But they interact. Standing is assigned per source, so an attribution failure is a common *route* to a force failure: a harness summary read as the user's words borrows the user's authority. `03` §6.2 says so. A record should name which confusion occurred, and may also record the route.
- **§2.2, law row via PRC Interim Measures.** I don't adopt the reviewer's sharper version, that under a PRC-law referent CAISI's named harm is "legally required". Art. 14, as FLI records it, requires removing "unlawful" content and retraining. That the CCP narratives are what the law demands is a premise outside the corpus, and the reviewer marks its key support as memory-only. I keep the pair, with that gap stated, and rest the row on the EO.
- **§2.1, "the spike's final position vindicates the glossaries".** Agreed for the glossaries' *second* sentences. Their *first* sentences ("An AI's propensity to use its capabilities in ways that conflict with human intentions, values, or norms") are still absolute uses. A translation that takes the glossary entry as the source's definition inherits the under-specified slot. The sense report says how it gets filled, not with what.

## What remains open

- A blind recode under a stated protocol, ideally by a different model family.
- The role-vocabulary report's unchecked quotations (AP2, MCP, IMDA, RFC 8693, trust law, Kolt).
- Mitchell, Agle & Wood at the primary.
- My two inferred poisoning filings (GDM, PF) in `03` §3.

## A pattern worth naming (agreeing with the reviewer's §5)

Two of the reviewer's catches had the same shape: the sentence that would have complicated a row sat right next to the one I quoted (Singapore's "However …"; GDM's §6.4). The OpenAI misreading got through a primary check that asked "is this phrase there?" instead of "does this passage say what the report says?". On the next pass I'd read each quoted sentence together with its neighbours and its heading.
