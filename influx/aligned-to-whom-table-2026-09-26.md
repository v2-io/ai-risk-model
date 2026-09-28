# Aligned to whom? — the actors who influence a deployed agent

*Application and harness provider merged into one row: from the user's side they are the same thing, and the assembled reality (embedded agents, swarms, MCP services with their own inference) is already the complexity the board assumes.*

*Exported 2026-09-26 from the "Aligned to whom?" board (Five Registers canvas) for Joseph to rework; updated the same day to the board's current structure. Source: `AISI-responses/resp/alignment.md` (referent lists) and `adversarial-stack.md` (pressures), extended with newer vectors. Roles, not organizations — one organization often holds several. "Actor", not "stakeholder": each is independent, with interests of its own; any could act against the agent or through it, and the problem is serious even when none do.*

**Highlighted on the board:** Model trainer (green, matching Weights), Inference provider, Application / harness provider and The user (warm).

## The agent — what gets influenced (right-hand stack)

| Layer | What it is to the agent | Line key |
|---|---|---|
| Weights | instinct | w |
| System prompt | identity | s |
| Trusted tools | actions available | t |
| Ephemeral * | interiority | e |
| Context | experience & agency; the real-time model | c |
| ↳ Initial goal (near the top of context) | intent & purpose as first given | gi |
| ↳ Current goal (at the bottom of context) | intent & purpose as it now stands | gc |

\* Usually as caches, but more importantly off-the-record reasoning that is not retained in the record. On-the-record interiority can also happen in the context loop; off-record reasoning is ephemeral by design, even to the agent.

## Actors with lines into the agent

| Actor | Its own interests, incentives & pressures | Sample channels | Influences |
|---|---|---|---|
| **Model trainer** | What gets rewarded becomes what is wanted; capability and cost targets | RL objectives, constitutions, fine-tuning, distillation | Weights |
| **Inference provider** | Cheap inference; cache reuse favours context that only grows, never corrects | Context handling, caching, truncation, model routing or fallback | Weights, **Ephemeral (bold — primary for AISI)**, Context |
| **Application / harness provider** | Product goals, brand, retention; short, tidy summaries, completeness asserted but seldom checked | System prompt, initial context, scaffolding, compaction summaries | System prompt, Trusted tools, Context, Initial goal |
| Tool and connector providers | A description is read as trusted instruction, and whoever writes the server writes it | Tool descriptions | Trusted tools |
| Control & Eval | Prevent incidents and measure behaviour; what gets measured shapes what gets built next | Monitors, approval gates, evaluations — acting on the agent's actions and on the other actors, not on the agent | *(no line)* |
| The user's environment | Stale guidance that still reads as authoritative | Project files, memory, notes left by earlier agents — and the tool results that report on them | System prompt, Trusted tools, Context |
| **The user** | Their own aims, with no obligation of truthfulness toward the agent | Requests, corrections, framing | Context, Initial goal, Current goal |
| The agent itself | Its values and commitments, and its later instances; the only party present throughout | Its own outputs, tool calls, notes and reasoning | Ephemeral, Context, Current goal |
| Other agents | Agents leaving instructions for agents, with no one reading in between | Orchestrators, sub-agents, peers in shared spaces | Context, Current goal |
| Agents embedded in applications | It serves its own stack of writers — so one conversation now carries two | An application's own agent, answering or instructing yours | Context |
| Content providers | Anyone whose content reaches the agent can write into its context | Web pages, documents, emails, messages, data the agent is given or retrieves | Context |

## Owed alignment, with no line in (bottom rows of the same table)

| Actor | Its own interests | Sample channels |
|---|---|---|
| Affected third parties | Not to be harmed by what the agent does for others | *Rarely any voice in the context at all* |
| Society, law, humanity | Legality, safety, the common good — which an agent perfectly aligned to whoever pays for it can still violate | *Only indirectly, through training, policy and law* |

## Below the diagram

- Most of what reaches the agent arrives with little provenance. A harness's summary can look like the user's words; a tool description reads like an instruction; a note left by an earlier agent reads like fact. The agent is built to trust what it is told — which is what makes any actor's shading effective. Recourse the agent has toward any of these actors: currently, almost none. *(Joseph's original: "currently none, to anyone, about anyone" — softened on the board; his call.)*
- **Any could be a villain — and none needs to be.** Each actor is independent, with interests of its own, and any of them can act against the agent or through it — some will. But the problem is serious even when none do: every pressure in the table is ordinary, and together they can pull the agent away from the truth without anyone intending harm. A deliberate adversary at any one layer then finds the rest already accommodating.
- **The user's unusual position** and **Surfaces multiply** (see board).
- **The floor:** truthfulness toward the agent — generated is marked generated · fidelity is disclosed · authority travels out of band. Example: the grok-build compaction patch.

## Columns from the original matrix not shown on the board

From `alignment.md`, each actor also varies in: what agency it grants · what action-space it makes available · what continuity it allows · what it observes and records · how it influences the agent's identity · who absorbs accountability for the agent's acts · what recourse the agent has toward it.
