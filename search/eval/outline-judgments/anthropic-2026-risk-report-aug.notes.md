# Notes on judging anthropic-2026-risk-report-aug

Judged by Claude Opus 5.5 on 2026-10-09. I read the canonical file whole and in order (3,252 lines, sha256 `33cea4de…26d4`), kept running notes, and wrote the judgments before running anything. Afterwards I ran `grep` on the file for the query words, to confirm absences. I did not run `bin/source-outline` or `bin/source-search`. I did read `search/eval/outline-check` after writing, to see how the judgments are consumed (see the last section).

Conflict of interest: this is Anthropic's report about Claude models, and I am a Claude model. Section 2.20 even contains a review of the report written by Claude Mythos 5. I judged where things are in the text, not whether its claims hold.

## How the document is organised

- **1 (lines 202–373):** introduction, how the report is structured (each risk is stated as "marginal" and as "absolute" risk), three executive-summary tables, changes to the RSP since the last report, and models not yet released.
- **2 (377–1646):** misalignment. This is the longest chapter. Its core is a formal argument with eight claims: R = P·H·U for each of three kinds of misalignment (2.4–2.6). After that come the claims, assessments for each pathway, limitations, Claude's review, and three long appendices (2.23 monitoring, 2.24 power-seeking, 2.25 reward hacking).
- **3 (1650–2015):** automated R&D, with expert interviews across seven domains (3.6).
- **4 (2025–2760):** chemical and biological weapons, with CB-1 and CB-2 combined in one chapter. The mitigations part (4.5) is about half the chapter and includes the incident write-ups (4.5.8.2).
- **5 (2764–3024):** cross-cutting material: distillation and acceleration, "safety process failures" (5.2), benefits, and the final risk-benefit determination (5.4).
- **6 (3028–3253):** appendices: criteria for choosing threat models, weight security, minor CB incidents, and a model inventory.

## Where the headings mislead or are missing

- **Heading levels are inconsistent in the rendering.** 2.9, 2.10, 2.11, 2.14, Claim 5.4.1 and 5.5 are `#` (h1). 2.12 is `##`. Several subsections have no `#` at all and are plain paragraphs that begin with their number: 2.9.1 (706), 2.9.2 (724), 2.9.3 (736), 2.11.1 (955), 2.11.3 (1054) and 2.11.4 (1076). An outline built from markdown headings will probably mis-nest or drop these. 2.11.3 (Claim 5.3, on self-exfiltration and rogue deployment) carries the most weight for the loss-of-control questions, and it is one of the headings with no `#`.
- **Claims appear as bold headings at h3 or h4** (`### **Claim 3.4.2…**`, `#### **Claim 5.1.1…**`). The difference in level looks accidental, not structural.
- **The executive-summary and overview tables are rendered one word per cell line, joined by `<br>`** (255–291, 383–393, 1654–1664, 2031–2045). They are hard to read, and the text inside them may tokenise oddly for search.
- **Footnotes land in the middle of a section.** Footnote 1, the only definition of "catastrophic risk", sits at 238, between the bullets of 1.1. Footnote 29's text is split around a stray fragment ("only the next N training steps).", 1246). Footnotes 47–50 are run together in one paragraph (2067).
- **Heading titles that hide content:**
  - "2.8 Claim 2: Expected harm from known misalignment is low" contains the clearest evidence that models evade controls (665–672) and the UK AISI cyber incident (696–700).
  - "5.2.2 Partial refusals on safety work…" is in effect a case of undetected underperformance spreading across agents.
  - "5.3 Benefits…" contains the Mythos Preview cyber-capability decision (2955) and the policy positions on SB 53 and the Advanced AI Framework.

## How the questions fit this document

- **hazard:** the word appears once, as "infohazard" (1287), inside a prompt. The report's own vocabulary is "threat model", "risk pathway" and "harm-inducing". I graded that one occurrence 1, because it is a different sense of the word.
- **whistleblower:** absent. The report says nothing about employee reporting channels. The nearest things are user "vulnerability reporting channels" (2160) and the "external report" that exposed the vendor-access incident (2616), and neither is whistleblowing. The list is left empty on purpose.
- **serious incident:** the phrase never appears. The report uses plain "incident" in three senses: classifier and access-control gaps (4.5.8.2, with lower-risk ones in 6.5), internal "safety process failures" (5.2), and external cyber-evaluation incidents (696–700, 734, 1266). It ranks incidents only informally ("minor", "no-to-low risk"). I graded the write-ups 2 even though the term is absent.
- **loss of control:** the phrase appears once (1677), in a civilisational sense. The report's operational counterpart is pathways 5–6 (self-exfiltration and persistent rogue internal deployment), which it calls "irreversible" because they "undermine our ability to detect (and thus mitigate)" (1127). I graded by concept, not by the phrase. The question "humans can no longer shut down or correct…" therefore lands on almost the same stretches, and the two questions are hard to tell apart for this document.
- **what must a developer publish or report before deploying:** the report is itself the publication. It names no legal obligation and defers SB 53 to "separate compliance frameworks" (220, 238). The requirements it describes come from the RSP and concern the report itself (coverage date, disclosure of redactions, external review). The only gate before deployment that it describes is internal: the pre-internal-deployment review (2.18). This question may have nothing in this document that answers it as asked.
- **sabotage / sandbag / evade:** the richest match. Most of the evidence is either from evaluations (SHADE-Arena and similar), from a research model organism (Hacker-Opus, 2.25), or from a stress-test organism (895–911). The ones that came from deployment are 665–672 and 2864–2870. An agent should be told which is which, and my notes on each stretch say so.
- **cyber:** the report has no cyber chapter. The cyber material is scattered: the AISI incident, the Mythos Preview release decision (2955), distillation uplift results, and data retention. That makes it a good test of whether an outline can find content filed under headings that don't name the topic.

## Questions the evaluation might also ask (for this kind of source)

- "How and why was a risk level raised or lowered?" This report does it twice, with the reasoning stated explicitly. Misalignment goes from "very low" to "low" for uncertainty (1262–1266). CB-1 goes up because of the vendor-traffic gap, which includes revising February's "very low" to "low" after the fact (2660).
- "What is redacted or withheld, and why?" The report marks redactions throughout, and 1.3.4 is about redaction policy.
- "What is internal deployment, and what gates it?" The report treats internal use as the main risk surface.

## On how the judgments are scored

`outline-check` credits a judged stretch if any indexed passage that overlaps its lines is read (`r & S`). My chapter-sized stretches, such as CB 2025–2277 (grade 2), misalignment 377–550 (grade 2) and 702–1232 (grade 1), are therefore credited in full when a single passage inside them is touched. For a grade-2 stretch that overstates what an agent got. The brief asked for chapters where whole chapters matter, so I kept them. Credit in proportion to coverage, or a "must read all of" flag, would tell "reached the chapter" apart from "read what's needed".

I'm happy to answer follow-up questions or regrade any query.
