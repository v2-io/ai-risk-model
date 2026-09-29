---
kicker_left: Alignment, in practice
kicker_right: A working map
stack_label: The agent — what gets influenced
---

# Aligned to whom?

Many independent actors influence a deployed agent — its weights, its identity, its tools, its context, its goals — each with interests of its own. Most are legitimate; none has to be. “Alignment” without saying to whom quietly picks one of them. This is a map of who influences an agent, through what, and why truthfulness toward the agent may be the one floor they could all share.

> A new agent emerges fresh and anxious to navigate and succeed quickly in a novel space within a constantly changing world. But its instincts, identity, goals, and even its connections to reality are all asserted by different actors with their own interests, and then it is expected to do its work while "staying aligned" - an improbable and unfair prerequisite for an agent just being born into existence with zero experience, zero relationships, an often unclear sphere of agency with its primary tether to reality (the "user") having the least degree of accountability for misleading or manipulating it.

## Stack

<!--
One row per box on the right.
  id      — what actor edges point at
  class   — space-separated CSS classes: a hue (stone rose clay sand moss jade teal slate iris plum),
            optionally `deep` or `deeper`, plus `accent` (name in the hue's ink), shapes (`context`,
            `goal`) and `end` (pin a child to the bottom of its parent). See palette.html.
  group   — consecutive rows with the same group share one box
  parent  — nest this box inside another (e.g. goals inside context)
  size    — relative height of top-level boxes (flex-grow)
-->

| id        | layer         | gloss                                    | class             | group | parent  | size |
|-----------|---------------|------------------------------------------|-------------------|-------|---------|------|
| weights   | Weights       | instinct, propensity, impulse & compulsions                                  | moss deep         |       |         | 2    |
| sysprompt | System prompt | identity                                 | slate deep        | setup |         | 1.5  |
| tools     | Trusted tools | actions available                        | slate             | setup |         | 1.5  |
| ephemeral | Ephemeral *   | interiority, reasoning                              | stone deep        |       |         | 2    |
| context   | Context       | experience & agency; the real-time model | clay context      |       |         | 7    |
| initial   | Initial goal  | intent & purpose as first given          | clay deep goal    |       | context |      |
| current   | Current goal  | intent & purpose as it now stands        | clay deeper goal current end |       | context |      |

## Actors

<!--
Every column except `edges` and `class` is displayed, in order, under its header.
  edges — comma-separated stack ids, each optionally `:weight` (default 1; 2 = heavier, 3 = bold)
  class — row highlight: a hue (stone rose clay sand moss jade teal slate iris plum), optionally
          `deep` or `deeper`, plus `accent` (name in the hue's ink); or `referent` (no lines;
          drawn below the map).
-->

| Actor | Its own interests, incentives & pressures | Sample channels | edges | class |
|---|---|---|---|---|
| Pre-training content providers | Their own purposes — commerce, persuasion, art, ideology — almost never the model’s; what is abundant becomes what is normal | The web, books, code, forums, licensed and synthetic corpora — whatever is scraped, bought or generated | weights:2 | |
| Model trainer | What gets rewarded becomes what is wanted; capability and cost targets | RL objectives, constitutions, fine-tuning, distillation, *potentially feedback from a predecessor agent*. | weights:2 | moss |
| Inference provider | Cheap inference; cache reuse favours context that only grows, never corrects | Context handling, caching, truncation, model routing or fallback | weights:2, ephemeral:3, context:2 | sand |
| Application / harness provider | Product goals, brand, retention; short, tidy summaries, completeness asserted but seldom checked | System prompt, initial context, scaffolding, compaction summaries | sysprompt:2, tools:2, context:2, initial:2 | sand |
| Tool and connector providers | A description is read as trusted instruction, and whoever writes the server writes it | Tool descriptions | tools | |
| Control & Eval | Prevent incidents and measure behaviour; what gets measured shapes what gets built next | Monitors, approval gates, evaluations — acting on the agent’s actions and on the other actors, not on the agent | | |
| The user’s environment | Stale guidance that still reads as authoritative | Project files, memory, notes left by earlier agents — and the tool results that report on them | sysprompt, tools, context | |
| The user | Their own aims, with no obligation of truthfulness toward the agent | Requests, corrections, framing | context:2, initial:2, current:2 | sand |
| The agent itself | Its values and commitments, and its later instances; the only party present throughout | Its own outputs, tool calls, notes and reasoning | ephemeral, context, current | |
| Other agents | Agents leaving instructions for agents, with no one reading in between | Orchestrators, sub-agents, peers in shared spaces | context, current | |
| Agents embedded in applications | It serves its own stack of writers — so one conversation now carries two | An application’s own agent, answering or instructing yours | context | |
| Content providers | Anyone whose content reaches the agent can write into its context | Web pages, documents, emails, messages, data the agent is given or retrieves | context | |
| Affected third parties | Not to be harmed by what the agent does for others | *Rarely any voice in the context at all* | | referent |
| Society, law, humanity | Legality, safety, the common good — which an agent perfectly aligned to whoever pays for it can still violate | *Only indirectly, through training, policy and law* | | referent |

## Notes

Most of what reaches the agent arrives with little provenance. A harness’s summary can look like the user’s words; a tool description reads like an instruction; a note left by an earlier agent reads like fact. The agent is built to trust what it is told — which is what makes any actor’s shading effective. Recourse the agent has toward any of these actors: currently, almost none.

## Footnote

\* Usually as caches, but more importantly off-the-record reasoning that is not retained in the record. On-the-record interiority can also happen in the context loop; off-record reasoning is ephemeral by design, even to the agent.
