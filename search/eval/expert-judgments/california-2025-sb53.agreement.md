# SB 53: where the three judges disagree, and why

*The SB 53 expert, 2026-10-10, after opening the other two judges' files. Their files: the Claude judge (`outline-judgments/`, claude-opus-5-5 subagent) and Gemini (`outline-judgments-gemini/`, Gemini 3.8 Flash). Mine is `expert-judgments/`. All three read the same text (sha256 `1b31896f…`). This covers only the 12 shared queries. I've tried hardest to find my own errors, since I'm least able to see them.*

## The short version

**On grade 2 the three judges agree closely.** Every query's must-read core is shared by at least two of us, usually all three: the two definitions, the reporting section, the transparency report, the whistleblower chapter.

The disagreements fall into three groups:
1. **Granularity.** One judge marks a whole subdivision where another marks two lines of it. This is harmless for the outline and the scorer. A fitted model would see it as noise in which passage carries the grade.
2. **The edge of grade 1.** How much surrounding context counts: findings, the digest, the Labor Code twins, penalty and procedure clauses. This is the main source of label noise. Most of these differences are defensible readings, not errors.
3. **Queries a statute can't answer literally.** Examples: a term SB 53 never uses ("hazard", "misalignment"), a paraphrase of another source's formula ("humans can no longer shut down…"), or a request for "evidence". Judges split between "empty" and "the nearest provision, at grade 1". The query is ambiguous for this document, and neither side is wrong.

**There are real errors, a few by each judge.** Mine are listed first below. I found more of my own than of the others'. My stage-1 file has narrower stretches and a stricter idea of what is relevant to a query. That cost me some fair grade-1 context the others caught.

**What this means for fitting:** trust grade 2 as a label. Treat grade 1 as soft: the three judges' grade-1 sets overlap only partly. Score passages by whether they overlap a judged stretch, not by the exact line edges, because the edges are where most of the disagreement is.

## Query by query

Each difference is marked **E** (an error, and whose), **D** (a defensible difference of reading), or **A** (the query is ambiguous for a statute).

**hazard.** I marked both catastrophic-risk definitions at g1, Claude marked the TFAIA one at g1, and Gemini left it empty.
- **A.** The word never appears. Whether "the nearest concept" counts for a term query is a policy question for the evaluation, not a matter of reading. Claude and I agree on the substance. The Labor Code twin, which only I marked, is **D**.

**catastrophic risk.** This is the broadest query, because the term does work in nearly every operative section.
- **E (mine):** I left out the large developer's transparency-report summaries, L148–157 (Claude, g1). Line 154, "Assessments of catastrophic risks from the frontier model", is an operative use of the term. That's the bulk of the "12 lines" gap.
- **E (Gemini):** it left out §1107.2 (L303) while grading the Labor Code definition (L257–264) at g2. That definition is incomplete without it. It also left out "Property" (L126).
- **D, on grades.**
  - §22757.16: Claude and I gave g2, Gemini g1. I hold g2, since without it the definition gives a wrong answer about the $1B element.
  - The Labor Code definition: Gemini and I gave g2, Claude g1. I hold g2, because SB 53 has two definitions that differ.
  - The framework (L127–137): Gemini g2, Claude and I g1. Defensible, since the framework is defined through catastrophic risk.
- **D, on inclusions.**
  - Only I marked L117 (the framework definition), L82–84 (findings (n)–(p)) and L309 (preemption). These are context, and arguable.
  - Only Gemini marked L79, finding (k). Its "serious risks" isn't the defined term, so it's weak but harmless.
  - Gemini included the digest, L36–38. That's a policy difference. I left digest passages out of definitional queries on purpose, because the digest isn't law and L38 has the wrong word "internet use".

**loss of control.**
- **E (mine):** I gave framework item (10), L137, g2. "Circumventing oversight mechanisms" is a related concept, not loss of control. Both others gave it g1, and they're right.
- **E (mine, from granularity):** my g2 stretch L106–110 also lifts item (4), deception, to g2. Claude split it finely (L109 g2, L110 g1), and that's the more accurate label.
- **D:** Gemini gave the Labor Code incident definition g2, the rest of us g1.

**humans can no longer shut down or correct the AI system.**
- **A:** Gemini graded everything g1, because SB 53 never addresses shutdown, while Claude and I gave the nearest provisions g2. Both readings are fair. The query is another source's formula, and whether "the closest provision" is a must-read depends on what the asker wants.
- **E (mine, minor):** I left out the Labor Code (B)/(C) at L259–260 (Claude, g1), though I marked their incident twins.
- **D:** Claude excluded incident items (1)–(2), and I included the whole definition. Claude's is finer.

**misalignment.**
- Claude and I are nearly identical: L110 g2, and L101 (or L98–101), L137 and L270 at g1.
- **A / E (Gemini, arguable):** Gemini left it empty. The word is absent, but the deception incident is plainly the statute's misalignment provision. I'd call the empty answer a miss, though a defensible one under a strictly lexical reading of term queries.

**whistleblower.** This is close agreement.
- **D:** the start of the digest (L48 for me and Gemini, L50 for Claude); and §1107.2 (L303) as g2 inside the chapter (me and Gemini) or g1 on its own (Claude). Neither matters.

**serious incident.**
- **E (mine, minor):** I left out finding (i), L77 (Claude, g1), though I marked (m).
- **D:**
  - Claude's g2 runs to L186 (review, transmission, Public Records Act, annual report). Mine and Gemini's stop at L179, with the rest at g1.
  - Gemini gave the Labor Code incident definition g2, the rest of us g1.
  - Gemini included the digest, L36–38.

**what must a developer publish or report before deploying a frontier model.**
- **E (mine):**
  - I left out L138–139: the annual review, and publishing material modifications with a justification within 30 days. Both others gave it g1. It is a publication duty.
  - I also left out L213–214, the penalty for failing to publish (both others, g1).
- **A / D:** I graded the framework (L127–137) g1, and both others gave g2. I read "before deploying" as tied to a deployment, and the framework is a standing duty. They read it as anything that must be published before a model ships. Their reading is at least as natural, and I'd move to g2.
- **D:**
  - Who is bound (L118–121): Claude g2, me g1, Gemini none.
  - The internal-use summary to OES (L160): both others g1, and I left it out because it isn't tied to deployment, which Claude's own note concedes.
  - "Deploy" (L111–112): Claude and I g2, Gemini g1.

**chemical and biological weapons uplift.** The anchors and grades agree in substance. They differ only in stretch length and in the grade of the Labor Code twin. No further comment.

**evidence that models can sabotage, sandbag or evade oversight.**
- **A, mainly:** a statute holds no evidence, so all three judges gave only g1, to the provisions such evidence would be reported under. Disagreement around a null answer is mostly noise.
- **E (Gemini, granularity):** its L106–110 stretch takes in incident items (1)–(3), which have nothing to do with sabotage. That's most of its "13 lines".
- **D:** Gemini's Labor Code (4) (L266–270) and (C) evading control (L98–101) are fair g1s. I'd accept both. My leaving out the Labor Code twin is a minor miss.
- **E (mine):** my finding (m) (L81, capabilities that "emerge") is a stretch, and finding (j) (L78, "concern") is weak. Neither other judge marked them, and I'd drop (m).

**cyber capabilities of frontier models.**
- **D:** the Labor Code (B) is g2 for Gemini and g1 for the rest of us. Stretch lengths differ.
- **D / E (Gemini, minor):** L106–107, weight exfiltration as an incident, is about the security of the developer's weights, not the model's cyber capability. Claude and I included L134, the framework's weight security, only to help a reader tell the two apart. Gemini's addition is the same idea taken one step further. It's defensible but not about the query.

**how the severity or acceptability of a risk is decided.** This query has the biggest gap. It's ambiguous for a statute: "severity" is used for the catastrophic threshold, for incident urgency, and for penalty amounts, while "acceptability" is left to developers.
- **E (mine):**
  - I marked only L98, the stem of the catastrophic-risk definition. The three scenarios and three exclusions (L99–105) also decide what counts as catastrophic, and both others marked L98–105 g2. That's most of the "34 lines".
  - I missed the 24-hour tier for imminent risk of death or serious injury (L177, Claude g1), which is a real severity rule for incidents.
  - I missed "Property" (L126, Claude g1).
- **E (Gemini):** the Department of Technology's review (L199–208, g1) is about *coverage* thresholds (who is a frontier developer or a large one), not the severity or acceptability of a risk. That's a misreading caused by the word "thresholds".
- **D:**
  - Gemini's Labor Code twin at g2. It's redundant but consistent with its practice.
  - Gemini's L148–157 at g1, the summaries of assessments and results. Fair: they're where the developer's acceptability judgments become visible.
  - My L110 ("materially increased catastrophic risk") and L213 (the penalty's "severity of the violation", which I marked as a false friend). Both are mine only and weak.

## Tally of errors, as I judge them

- **Mine:** 9.
  - Omissions (6): L148–157 (catastrophic risk), L259–260 (shutdown), L77 (serious incident), L138–139 and L213–214 (publish), L177/L126 (severity).
  - Over-grades (2): L137 g2 and L110 lifted to g2 (loss of control).
  - A too-narrow stretch (1): L98 alone (severity).
  - Plus one weak inclusion, L81 (evidence).
- **Gemini's:** 4. Missing L303/L126 (catastrophic risk), the empty answer for misalignment, the over-broad L106–110 (evidence), and the coverage thresholds read as risk severity (L199–208).
- **The Claude judge's:** I found none I'd call errors. Its marks are the most finely drawn of the three. Where it differs from me, I'd take its version more often than mine.

This list is one judge's view of all three, including itself. It isn't settled.
