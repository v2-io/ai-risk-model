# Proposed integration plan

*Suggestions with reasons, for whoever integrates this spike after verification. They are not a work order. The integrator will know things I don't, including Joseph's decisions on the map and the verifier's corrections.*

## What I'd integrate, and where

1. **`CLAUDE.md`, the open decision on the misalignment referent.** If Joseph agrees with `03-structure.md` §8, the decision could be restated along these lines: "Alignment words: no default referent in the records. The lexicon defines the relation's slots (bearer, mode, claimant set, aspect, time, adjudicating standard, judge, domain, degree). Translations record which slots each source fills, and for absolute uses whether a claim is invariant over a named candidate set or sensitive among named candidates. A view may declare a projection default." *Reason:* §4's no-go means a record-level default would be adjudication. §5 means "ambiguous" alone over-records.
2. **The gamma plan, §3.4's resolution outcomes.** Add *invariant over S (S named)* beside "ambiguous among named candidates", and a *use type* (relational / absolute / activity / field). Record the absolute use as **under-specification of an argument place**, not lexical ambiguity (SEP *Ambiguity*, via the literature report). *Reason:* §5, and the de novo review's §2.7 point that outcome and reason should be kept apart.
3. **The gamma plan, §3.9 (actors and parts).** Replace the two-bases framing ("lifecycle or market" vs. "writes into") with plural bases connected by conferral. Institutional roles are conferred on operative facts, and several of those are writing acts: SB 53's training act; the EU guidelines' modification threshold, "who has the control over the model's weights"; ETSI's operators becoming providers "if they make changes". Add the relations of `04-actors.md` §1 to the term group. *Reason:* `04-actors.md` §5 found the basis-of-division claim true for AI Act Art. 3 only.
4. **The gamma plan, §3.11 acceptance tests.** A candidate test for the alignment family: every definition in `02-sense-inventory.md` §3 resolves slot by slot, with unfilled slots recorded as unfilled. Every partition label (misuse / misalignment / mistakes / structural; malicious user / misaligned model; Model Spec's three risk categories) records its claimant and the writer basis it uses.
5. **The gamma plan's competency questions,** if adopted (de novo review §2.1). Two that this spike suggests:
   - *for a given event, which sources file it as misuse, misalignment, robustness or security, and which writer carried the intent?*
   - *for a given risk, under which referents is it misalignment?*
6. **OVERVIEW §2.15** could gain the items `01-map.md` §2 found beyond its table:
   - the list definitions and their missing conflict rule;
   - NIST AI 100-2's "Misaligned Outputs";
   - CAISI's "CCP alignment";
   - Davidson's loyalties;
   - Chin's three-valued goal alignment;
   - the Astra "authorized scope" sense;
   - the IASR 2025 → 2026 change ("operators" dropped, "norms" added).
7. **The source catalog.** Two developer documents carry the working conflict rule that the risk literature's "alignment" relies on: Anthropic's constitution and OpenAI's Model Spec. Neither is in the corpus. Adding both (with the conflict-of-interest note) would let the operator-against-users risk and the injection filings be cited from the corpus.
8. **The ETSI / DSIT "affected entities" wording** ("not directly affected"), set against NIST's "directly or indirectly affected". Worth a lineage record and a check at the PDF. It is my inference that the ETSI text derives from NIST's.

## What needs the verifier's eyes first (load-bearing)

- `03-structure.md` §2 (the list-degeneracy argument) and §4 (the no-go table, row by row: does each cited risk really come out *aligned* under that default?).
- The partition table in §3: each filing, at its line.
- The coded sample (`data/misalign-sample-coding.md`): a blind recode, preferably from a different model family. I proposed the idea being tested, so my coding is the weakest evidence in the spike.
- The company quotes I verified at the primary (constitution, Model Spec, both downloaded 2026-10-06). The pages change, so a dated archive copy would help.
- The literature report's [P] quotes, sampled. Its author and I are the same model, so its agreement with my structure is coherence, not confirmation.

## Do not inherit

Interpretive language that is mine, not the sources'. Please don't carry it into lexicon entries or source translations as if a source said it. It belongs in our attributed readings, if anywhere.
- **"absolute" vs. "relational" use**: my labels. The literature's nearer terms are *implicit argument* or *under-specification*.
- **"standing mismatch"**: my coinage, for a channel given more standing than its writer has.
- **"claimant set"**: my label for what the literature calls the alignment target or the tetrad.
- **"aspect"**: my label; the literature report says "content", Leike says "preference payload", Askell says "outcome ordering".
- **"invariant over S" / "sensitive"**: my outcome names. The established frame is supervaluation, but the outcome names are mine.
- **"admissibility"**: my word for the legitimacy condition. The constitution's own word is "legitimate".
- **"the six relations"** in `04-actors.md` §1: my decomposition. Each has evidence; the set is mine.
- **"one functional layer and several institutional layers, connected by conferral"**: my reading of the role bases.
- **The six-row no-go table** (§4): my construction. Its cells cite sources, but none of the sources says "this default hides that risk".
- **Characterizations of sources as "careful", "rigorous" or "loose"**: avoid these. I tried not to write any.

## What I would not integrate yet

- Any candidate term in `05-candidate-terms.md` as an entry. They are first-pass and need Joseph's truthification passes.
- The new actor rows. Which of them become rows, and which become attributes or footnotes on the map, is a design call for Joseph.
- The hypothesis that the truthfulness floor holds at the regime level (§6.3). It is untested.
