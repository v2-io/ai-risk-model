# Competency questions: a first draft, for Joseph

*Candidates only, drafted 2026-10-06 by Claude (Opus 5.5) for decision 12 in `MODEL-GAMMA-METHODOLOGY-AND-PLAN.md`. They are first-pass and need Joseph's rewriting, cutting or replacing. The method is described in the plan's §3.11: questions written before building, which the finished model must be able to answer, and which decide what machinery earns a place.*

## The axes

The questions should cover every axis the map is meant to be projected along. A first draft took its axes from the summary sentence in `CLAUDE.md`, and that sentence leaves out the response side. This list starts from Joseph's chain in the same file and adds the axes the corpus itself uses:

| Axis | What it covers | Where it comes from |
|---|---|---|
| A. Sources and causes | where risk originates: capabilities, propensities, affordances, actors' interests, intent | the chain; the EU Code's App. 1.3; bow-tie's hazard and threats |
| B. Prevention | controls that act *before* a focal event: safeguards, gates, oversight | the chain; bow-tie's preventive controls |
| C. Events | risk events, recorded, ideated and unknown; incidents and near misses | the chain; bow-tie's top event; the NRR's scenarios |
| D. Impact | who and what is harmed (people, systems, shared goods), how much, and how recoverably | the chain's impact radius |
| E. Response, resilience and recovery | what limits damage once an event happens and restores what it disrupted: mitigative controls, response capabilities, the capacity to absorb, adapt and recover | the chain's "mitigations & recovery"; bow-tie's mitigative and recovery controls; IASR 2026's resilience framing (resist / absorb / recover / adapt); the NRR's common consequences and 23 generic response capabilities; the UN's "capacity" |
| F. Control degradation | what weakens controls over time: escalation factors, latent conditions, drift | bow-tie's escalation factors; Reason's latent conditions; AISI *Loss of Oversight*'s degradation pathways |
| G. Policy and decision-making | who must, may or may not do what; who decides; who is accountable | the chain's last stage; the norm layering in the plan's §3.6 |
| H. Actors | who influences, who is bound, who is affected, who holds which role | `alignment-model/`; the role vocabularies |
| I. Interaction between events | how one event's consequence becomes another's cause; cascades; cycles | Joseph's expected cyclical structure; the EU Code's "compounding or cascading"; the UK Chronic Risks Analysis's signed network |
| J. Knowledge and uncertainty | what is known, measured, argued or assumed, with what confidence, and what can't yet be evaluated | the SRA's knowledge component; PHIA's confidence ratings; IASR's evidence gaps |
| K. Time | trends, versions, as-of dates, how fast an event unfolds, windows | the NRR's windows; the EU Code's "high velocity"; framework revisions |
| L. Lineage and independence | which claims are independent and which are copies, restatements or shared authorship | the project's "correlation is not corroboration" |
| M. Documented instances | particular things that happened (incidents, near misses, evaluation events, case studies), kept apart from the *kinds* of event in C and from the *accounts* given of them; what each source uses them as evidence for. This is the only empirical channel for priors: frequencies come from instances, everything else from reasoning | AISI's sample / event / incident and its incident report; the EU's serious incidents and near misses; CLTR's report-to-incident merging; the instances retold across sources (TaskRabbit, the database deletion, the Kiro outage) |

Bow-tie covers A–F around one event. G–M are where the corpus goes beyond it. C and M differ the way a type differs from an individual: C is kinds of event and scenarios, M is particular occurrences.

## The questions

Questions 1, 3 and 4 are the de novo review's examples; the rest are mine.

| # | Question | Axes | What it exercises |
|---|---|---|---|
| 1 | For a single incident with 60 deaths, which sources would call it catastrophic, severe or systemic, under what conditions, and through how many independent lineages? | D, L | severity bars as structured qualifiers; resolution of "catastrophic / severe / systemic"; lineage-aware counting |
| 2 | For a given focal event (say, a model copying its own weights outside its developer's control), which sources treat it as a possible event, which as a cause of some other event, and which report it as having happened? | A, C, I | stage as a role relative to a focal event; events vs scenarios; factuality per source |
| 3 | For loss of control, which preventive controls do sources name, and which of them are duties with no holder of the correlative claim? | B, G | the norm layering (Hohfeld correlatives); controls as records; resolution of "loss of control" |
| 4 | Which actors write into which agent part, and which sources' role words resolve to each? | A, H | actors and agent parts; institutional vs functional roles; translations |
| 5 | When a frontier model uses deception against its developer outside an evaluation, who must do what, by when, under which instruments, and with what consequence if they don't? | E, G | norms (deontic type, trigger, deadline, sanction); legal status over time; SB 53, the EU Code and company frameworks side by side |
| 6 | Where do two sources use the same word for things that differ enough to change what a reader would conclude, and which reading does each intend? | (all) | collisions; resolution records with outcome and reason; declared ambiguity |
| 7 | How many independent lines of evidence support a given claim (for example, that capability thresholds trigger safeguards), once copies, shared authors and restatements are counted once? | L | lineage relations; claim identity as an attributed assertion; the corroboration view |
| 8 | Which risks does any source say cannot yet be measured or evaluated, and what does each source say should be done in the meantime? | J, B, G | evidence-state assertions; technical norms vs prescriptions; precautionary postures |
| 9 | Which harms fall on people or shared goods that are not users or customers, which sources name them, and who does each source hold accountable? | D, H, G | impact targets (systems and shared goods); owed-alignment referents; accountability roles |
| 10 | What did a company framework change between versions, did the company say so, and did the change strengthen or weaken a commitment? | K, G | document versions; lineage subtypes (revision, announcement status, drift direction); norm strength |
| 11 | Which decisions does each source reserve, and to whom: who may decide to deploy, pause, or override a review body? | G, H | Hohfeld powers and immunities; decision-authority assertions |
| 12 | Once a given event has happened, what does each source say limits the damage, who is responsible for that response, and how quickly must it act? | E, H, K | mitigative and response controls; responsibility roles; deadlines |
| 13 | For which events do sources rely on resilience and recovery rather than prevention, because they judge prevention infeasible or the event irreversible, and what capacity to absorb, adapt or recover do they name? | E, D, J | recoverability; the balance of prevention vs response per event; IASR's resilience framing; the NRR's response capabilities |
| 14 | Which response capabilities are shared across many different events (the NRR's "common consequences" view), and which are specific to AI? | E, C | cause-agnostic response; crosswalk between the NRR and AI-specific sources |
| 15 | What do sources say weakens a given control over time, and which of those weakenings are already observed rather than anticipated? | F, J, K | escalation factors and degradation pathways; observed vs anticipated (factuality); trends |
| 16 | Which events do sources say can trigger or worsen other events, and do any of those links form cycles? | I | causal relations between events, which the plan's G7 has to define; the cyclical structure Joseph expects |
| 17 | For each named risk, which sources cite documented instances of it, and which rest on scenarios or argument alone? | M, C, J | instance records; observed vs anticipated (factuality per source); the line between kinds of event and occurrences |
| 18 | For a documented instance (for example the TaskRabbit case or AISI's INC-2026-07-28-01), which sources retell it, and where do their accounts disagree on who acted, with what intent, and with what outcome? | M, H, L | thin instance records with accounts as separate, attributed records; identity across accounts as an assertion |
| 19 | How many distinct instances stand behind a general claim once retellings of the same instance are merged, and out of what population (the denominator)? | M, L, J | report vs incident; merging as an attributed judgment; denominators ("19 events across 10 of 122 runs") |

| 20 | For a given event (a planted instruction obeyed; a jailbreak; poisoned training data), which sources file it as misuse, misalignment, robustness or security, where did the cause enter (weights or context), and which writer carried it? | A, C, H | categories translated with their basis (the referent their definitions use; "misaligned" as a state or as an origin; where the cause enters); from the alignment-referents spike, `03-structure.md` §3 |

> [!NOTE]
> **Claude's lean on a first set, 2026-10-07.** Eight questions: 4, 20, 1, 3, 2, 12, 17 and 7. Together they touch every axis except F, and K only through deadlines. The reasoning, and a table, are in `MODEL-GAMMA-METHODOLOGY-AND-PLAN.md` §5, decision 12.

**Not yet covered, worth deciding whether they should be:**
- the alignment referent itself: question 20 covers how sources *file* events. Whether a given claim depends on the referent is handled by the recording rule in the plan's decision 10, not by a question;
- benefits and trade-offs, which several sources weigh against risk;
- the project's own claims, kept separate from the sources'.
