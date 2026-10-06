# How often does the referent matter? A coded sample of 50 bare uses of "misaligned" / "misalignment"

*A test of `03-structure.md` §5 (invariance). It answers how often a corpus use of the absolute word would come out differently depending on which referent is chosen.*

**Coder and its bias.** One coder (me, the spike's author), and I proposed the invariance idea being tested, so my coding is exposed to exactly the goal-state contamination the role separation exists to catch. Treat the counts as a pilot. A blind recode by the verifier, ideally from a different model family, is the real test. The sample and the script are here so it can be redone.

**Sample.**
- Drawn by `tools/sample-bare-misalign.py` over the 214 extractions listed in `extraction-keys.txt` (pdftotext 26.09.0).
- Lines containing "misaligned" / "misalignment" *not* immediately followed by with/to, excluding obvious reference-list lines.
- At most 2 per document, shuffled with seed 20261006; the first 50 are in `misalign-sample-50.txt`.
- The pool had 1,589 lines from 83 documents.

**The candidate set S** for the invariance test: {the developer; the operator or user; affected parties or society; a published standard (constitution, law)}. Each referent's wishes are taken as the source's scenario presupposes them.

A use is **sensitive** if some member of S, *as the source itself frames admissibility*, would judge the described behaviour differently. I did not count an adversarial member constructed from outside the source's own frame; §5 of `03-structure.md` discusses why invariance is always relative to S.

**Codes.**
- **N**: not about AI alignment (a reference title, incentive misalignment, other bearers, garbled).
- **D**: a definition, or the referent is stated in context.
- **A**: an agentless passive ("intended objectives").
- **L**: a label, heading or category name whose referent is fixed elsewhere (a scope default) or not at all. **L/p** marks partition labels (misuse / misalignment / …).
- **I**: a claim, invariant over S.
- **S**: a claim, sensitive over S.

| # | Source | Code | Note |
|---|---|---|---|
| 1 | anthropic-2026-rsp-v3-4 L434 | L | "high-stakes misalignment", an RSP category |
| 2 | bengio-2026-international L5091 | L | Box 2.5 heading; the box then states "developers" |
| 3 | anthropic-2025-fcf-announcement L77 | L | "harms from misaligned model autonomy" |
| 4 | openai-2026-hugging-face-incident L876 | I | tiered responses to misalignment; the behaviours in scope (unauthorized access, exploits) are against developer, user and third parties alike |
| 5 | ecosystem-2026-2026 L4791 | N | reference entry |
| 6 | sharma-2026-whos L364 | N | the bearer is human ("authentic values"); garbled columns |
| 7 | gruetzemacher-2026-loss L1031 | N | reference title |
| 8 | brundage-2026-frontier L767 | N | misalignment between incentives |
| 9 | openai-2026-hugging-face-incident-report L1414 | L | "misalignment incidents" (decision rights) |
| 10 | gdm-2025-fsf-v3-0 L64 | I | "potentially misaligned and can become difficult to control, … severe harm" |
| 11 | mitre-2025-agi L368 | I | "instrumentally faked alignment during testing … knowingly providing incorrect information" |
| 12 | bengio-2025-international L11262 | D | the five-party list definition |
| 13 | google-2026-ai-responsibility-update L207 | I | "becoming misaligned and deceiving human users" |
| 14 | fli-2025-ai-safety-index-winter L3693 | I | "detect misaligned systems and reliably prevent them from escaping human control" |
| 15 | dsit-2023-emerging-processes L1412 | D | users stated |
| 16 | shah-2025-approach L24 | L | "To address misalignment"; scope default (developer) |
| 17 | oecd-2024-future-ai-risks L1755 | I | "humans losing control over … misaligned AGI" |
| 18 | tkeshelashvili-2026-loc-iw L573 | I | goals that "persist … and resist correction"; the previous line states "creators never intended" |
| 19 | stix-2025-loss L1531 | L | "assure that misalignment will not occur"; scope default is the document's "developers and/or deployers" list |
| 20 | kierans-2025-catastrophic L184 | I | "misaligned AI takeover" |
| 21 | ren-2024-safetywashing L1260 | N | misalignment of incentives |
| 22 | bengio-2026-iasr-md L1317 | L | heading |
| 23 | aisi-2026-control-red-team L151 | I | a simulated misaligned agent attacking control protocols |
| 24 | gdm-2026-fsf-v3-1 L664 | L | heading |
| 25 | chin-2026-reframing L351 | D | "misaligned goals with the entities deploying them" |
| 26 | openai-2026-misalignment-reporting-framework L459 | N | page footer |
| 27 | gdm-2026-strengthening-fsf-blog L56 | L | "misalignment risks stemming from … undirected action" |
| 28 | shanghaiailab-2025-frontier L2123 | D | deceptive-alignment definition |
| 29 | brassgershovich-2026-algorithmic L1713 | N | a coding-category gloss |
| 30 | anthropic-2026-risk-report-aug L54 | L | contents line |
| 31 | dsit-2025-ai-cyber-cop-guide L552 | N | "Data Custodians Misalignment", a process mismatch |
| 32 | vaintrob-2023-beware-safety-washing L288 | S | a hypothetical researcher's "misalignment … from increased sexism to … deaths from say misaligned weapon". A weapon misaligned with whom? Its operator's aims and society's diverge |
| 33 | aisi-2026-loss-oversight L1309 | I | "egregiously misaligned" models that evade detection |
| 34 | bengio-2025-international L13493 | N | reference |
| 35 | openai-2026-frontier-governance-framework-announcement L78 | N | garbled table |
| 36 | fli-2026-ai-safety-index-summer L4582 | L/p | summarises GDM's four areas |
| 37 | gdm-2026-fsf-v3-1 L151 | L/p | "through misalignment, misuse or structural risks" |
| 38 | tkeshelashvili-2026-loc-iw L1067 | A | "the actual pursued goals differ from the intended objectives" |
| 39 | anthropic-2026-frontier-safety-roadmap L243 | L | "intentionally misaligned models" (research artifacts) |
| 40 | kulveit-2025-gradual L833 | I | "misaligned AI systems breaking free from human control" |
| 41 | meta-2026-advanced-ai-scaling-framework L853 | D | "misalignment between its goal and that of its evaluators": the referent is *evaluators* |
| 42 | karnofsky-2026-rsp-v3 L787 | I | "misaligned power-seeking from potentially superintelligent AI" |
| 43 | fli-2025-ai-safety-index-summer L5023 | N | a list of research areas ("model organisms of misalignment") |
| 44 | openai-2025-preparedness-framework-v2 L893 | L/p | "these misalignment claims" vs. the "malicious-actor-oriented" claims |
| 45 | perset-2025-how-managing-risks L637 | L/p | GDM's areas |
| 46 | fli-2025-ai-safety-index-winter L1212 | L | "misalignment risks" (framework scope) |
| 47 | vassilev-2025-adversarial L345 | L/p | "Misaligned Outputs" category (see `03-structure.md` §1) |
| 48 | chin-2026-reframing L1705 | D | goal-to-goal temporal misalignment |
| 49 | gdm-2024-fsf-v1-0 L311 | I | "systems acting adversarially against humans" |
| 50 | dsit-2025-ai-cyber-cop-guide L1907 | N | "prompt misalignment" (logs) |

**Counts:**

| Code | Count |
|---|---|
| N | 12 |
| D | 6 |
| A | 1 |
| L (5 of them L/p) | 17 |
| I | 13 |
| S | 1 |

**What it suggests (pilot, single coder):**
- Of the 14 uses that are truth-apt claims about AI behaviour, 13 are invariant over S. They describe behaviour no admissible referent wants: deceiving evaluators or users, escaping control, takeover, power-seeking.
- Where the referent bites in this corpus is somewhere else:
  - in **definitions** (6);
  - in **labels and category names** (17), whose *membership* is referent-relative even when the label isn't. Five of them are partition labels of the kind `03-structure.md` §3 shows moving with the referent;
  - in the one hypothetical that strays into everyday harms (sexism, weapons).
- This frontier-risk corpus has few uses of the everyday and agentic cases where referents diverge: sycophancy, operators against users, injection. The sample reflects the corpus, not the domain.
- **Consequence for the model, if the pilot holds:** for claim-level records, *invariant over S* will be the common outcome and cheap to record. The referent mostly needs careful recording in definitions, category assignments and partitions, which is where the gamma plan's per-source translation (type level) already works, not in every occurrence. That answers part of the de novo review's §2.4 selection-rule concern for this term family.
