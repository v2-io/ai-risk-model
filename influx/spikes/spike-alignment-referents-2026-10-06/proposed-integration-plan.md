# Proposed integration plan

*Suggestions with reasons, for whoever integrates this spike after verification. They are not a work order. The integrator will know things I don't, including Joseph's decisions on the map and the verifier's corrections.*

## What I'd integrate, and where

1. **`CLAUDE.md`, the open decision on the misalignment referent.** If Joseph agrees with `03-structure.md` §8, the decision could be restated along these lines: "Alignment words: no single-referent default in the records. The lexicon defines the relation's slots (bearer, mode, claimant set, aspect, time, adjudicating standard, normative judge, domain, degree). Translations record slots per source definition, a use type per occurrence, and invariance or sensitivity only for asserted claims where the alignment word carries the verdict. Those judgments use a declared, versioned admissible-candidate set; whether the agent itself is in it is an explicit decision. A view may declare a single-referent projection."
   - *Reason:* §4 means a single default would be adjudication. §5 means "ambiguous" alone over-records. The set-valued default came from the de novo pass.
2. **The gamma plan, §3.4's resolution outcomes.** Add *invariant over S* beside "ambiguous among named candidates", and a *use type* (relational / anaphoric with a pointer to its stipulation / absolute / activity / field). Record absolute and anaphoric uses as **under-specification of an argument place**, not lexical ambiguity (SEP *Ambiguity*, via the literature report).
3. **The gamma plan, §3.9 (actors and parts).** Replace the two-bases framing with plural bases connected by conferral. Institutional roles are conferred on operative facts of several types:
   - writing acts (SB 53's training act; the EU's "significant change" modification);
   - market acts;
   - use;
   - **control** (EU guidelines fn 12: the modification act is attributed partly by "who has the control over the model's weights").

   Take the relations from `03-structure.md` §6.1. *Reason:* `04-actors.md` §5 found the two-bases claim true for AI Act Art. 3 only.
4. **The gamma plan, §3.11 acceptance tests.** A candidate test for the alignment family:
   - every *definition* in `02-sense-inventory.md` §3 resolves slot by slot, with unfilled slots recorded as unfilled;
   - every grouping of "who went wrong" (GDM's four areas, declared "not a categorization"; PF's misaligned-model safeguards; the Model Spec's three risk categories; NIST's integrity attacks) records the referent of its definitions, whether it reads "misaligned" as a state or an origin, and which part of the stack the cause enters.
5. **Competency questions.** `influx/competency-questions-draft.md` lists the alignment referent as waiting on this spike. Two candidates:
   - *for a given event, which sources file it as misuse, misalignment, robustness or security, where did the cause enter (weights or context), and which writer carried it?*
   - *for a given risk, under which referents is it misalignment?*
6. **OVERVIEW §2.15** could gain the items `01-map.md` §2 found beyond its table:
   - claim-internal referent disjunctions with no conflict rule, and the bodies' conflict rules (IASR md 1906–1908; Singapore 2026);
   - NIST AI 100-2's "Misaligned Outputs" (index label for an integrity attack);
   - OpenAI's state/origin usage and GDM's intrinsic-origin requirement;
   - CAISI's "CCP alignment";
   - Davidson's loyalties;
   - Chin's three-valued goal alignment;
   - the Astra "authorized scope" sense;
   - the IASR 2025 → 2026 change ("operators" dropped, "norms" added).
7. **The source catalog.** Two developer documents carry the working conflict rule that the risk literature's "alignment" relies on: Anthropic's constitution and OpenAI's Model Spec. Neither is in the corpus. Adding both (with the conflict-of-interest note) would let the operator-against-users risk and the injection filings be cited from the corpus.
8. **The ETSI / DSIT "affected entities" wording** ("not directly affected"), set against NIST's "directly or indirectly affected". Worth a lineage record and a check at the PDF. Two readings are live: a copying slip, or a deliberate narrowing to the complement of ETSI's end-users.

9. **The actor term group** can draw on the role-vocabulary report's parties × relations table (§6 there) and collision list (§7 there). Those are its strongest contributions to G2.

## What still needs independent eyes (after `de-novo-feedback-1.md`)

- A blind recode of the 50-item sample, under the protocol in `data/misalign-sample-coding.md`. Neither I nor the de novo pass could provide one.
- The role-vocabulary report's quotations the de novo pass did not check: AP2, MCP, IMDA, RFC 8693, the trust-law sources, Kolt, Shavit (I checked Shavit §2.2).
- Mitchell, Agle & Wood 1997 at the primary (urgency and legitimacy).
- The reworked §3 table: GDM's poisoning reading and the PF's poisoning reading are my inferences.
- A different-model-family reader for the whole. The spike, both research agents and the de novo pass are one model family.

## Do not inherit

Interpretive language that is mine, not the sources'. Please don't carry it into lexicon entries or source translations as if a source said it. It belongs in our attributed readings, if anywhere.
- **"absolute" / "anaphoric" / "relational" use**: my labels ("anaphoric" from the de novo pass). The literature's nearer terms are *implicit argument* or *under-specification*.
- **"standing mismatch"**: a coinage of mine, now withdrawn. It merged three confusions; use attribution / force / epistemic status, under the map's own word, *provenance*.
- **"set-valued default"**: the de novo pass's phrase for a declared candidate set, adopted here as a proposal.
- **"claimant set"**: my label for what the literature calls the alignment target or the tetrad.
- **"aspect"**: my label; the literature report says "content", Leike says "preference payload", Askell says "outcome ordering".
- **"invariant over S" / "sensitive"**: my outcome names. The established frame is supervaluation, but the outcome names are mine.
- **"admissibility"**: my word for the legitimacy condition. The constitution's own word is "legitimate".
- **"the eight relations"** (`03-structure.md` §6.1): my decomposition. Each has evidence and most have established names; the set is mine. Each has evidence; the set is mine.
- **"one functional layer and several institutional layers, connected by conferral"**: my reading of the role bases.
- **The six-row no-go table** (§4): my construction. Its cells cite sources, but none of the sources says "this default hides that risk".
- **Characterizations of sources as "careful", "rigorous" or "loose"**: avoid these. I tried not to write any.

## What I would not integrate yet

- Any candidate term in `05-candidate-terms.md` as an entry. They are first-pass and need Joseph's truthification passes.
- The new actor rows. Which of them become rows, and which become attributes or footnotes on the map, is a design call for Joseph.
- The hypothesis that the truthfulness floor holds at the regime level (§6.3). It is untested.
