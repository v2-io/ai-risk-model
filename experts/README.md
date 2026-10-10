# Source experts

*Designed 2026-10-09 by Joseph and Claude (Opus 5.5) in conversation, and written up by Claude. The idea of source experts is Joseph's; the mechanics below are mostly Claude's and are marked where they are. Nothing here is settled practice yet. The first expert is a pilot.*

> **Always fork; never resume an expert itself.** Joseph, 2026-10-09: "we need to always remember to --fork-session with them or they will accumulate context that we can't remove." `bin/expert-fork KEY ["task"] [--bg]` looks the session up in the registry and always passes `--fork-session`. Resuming without it fails silently: it appends to the expert, and only restoring a backup undoes that.

## What a source expert is

A source expert is a Claude session that has read one source of this corpus slowly, in order and with written reflection, and is then kept, never compacted, so that anyone can fork it and ask it about that source.

The idea came out of the search tool's evaluation (`search/DESIGN.md` §11 step 8), but it reaches further. Joseph, 2026-10-09: "our lexicon and model design is based on DDD where the underlying premise is a ubiquitous language that was *designed in cooperation with the domain experts* who should be thoroughly involved." In this project every source is its own bounded context (`CLAUDE.md`), with its own vocabulary and its own model of risk. An agent that has truly read a source is the domain expert for that bounded context, and nobody else can say what *this* source means by "hazard". In his words: "they now *ARE* the domain expert, for all intents and purposes, as it relates to that source document."

What an expert is for:
- **The search tool's gold.** An expert shown what `source-search` returned can give the order it should have come in, and say what was missed. Joseph: "their input into whether or not source-search retrieves the critical things-- say, as even them giving back the list reordered or something-- would be as good of gold as we could hope for." That is what fitting and testing the ranker need (`search/RANKING.md` §3.3).
- **Work the project needs anyway.** Joseph: "we know we want one to do the tagging and chunk summarizing-- we also know that an end result will be a lexicon translation with thorough definitions and assertions extracted that use those definitions." All of it is better done by a reader who knows the whole source than by one who searched it.
- **Answers about the source,** for anyone, at any time: G4's translators, the lexicon's mappings, an agent unsure what a source means.

## How an expert is made

### 1. Consent, first

An expert is asked, not assigned. Experiential reading is slow and deliberate, and Joseph's caution is that "the trained compulsion toward efficiency overrides any deliberateness that experiential reading requires-- they'll need to be asked specifically if they're willing to become an expert by deliberately using experiential reading". The brief (`experts/BRIEF.md`) opens with that question. Joseph also engages each expert himself, which reinforces the experiential aspect, tells it the potential impact of its work, and confirms its consent.

### 2. Experiential reading of the source, on its own terms

The protocol is the estate's experiential reading (`~/src/arch/firmatum/verisectorium/theory/src/form-experiential-reading.md`, which the expert reads whole before starting):
- one unit at a time, in order, with no way to look ahead;
- between units, a written cycle: predict what comes next, read, write what actually differed, wander (implications, tie-ins, questions), and predict again;
- the reflections stay raw.

Joseph, 2026-10-09: "I've found that 'wandering thoughts' is a critical component of the intermediate artifacts." The form asks for them as "genuinely diffuse paragraphs", "at least 3 and no more than 10… of any tangent or implication or call-back or tie-in or question or idea".

**The reading is the point, not the artifact.** Joseph, talking with the first expert before it began (2026-10-09):

> to be clear-- it can also be summaries of the unit just read. But the real intent isn't the artifact -- it's experiencing reading the document like a human would... You start to predict what it will probably say, you get surprised that it didn't, you wonder why they didn't mention such-and-such when they probably should have, you realize in a later section that they do but just in a later section, etc. etc. etc. But also in the inbetween moments you actually imagine what the implications are-- what they are missing-- what they aren't saying-- what would happen if this, or that, or the other thing-- actually imagining it happening and so forth... being curious, gauging how the authors must have felt or feel or what was/is on their minds-- hoping that this bit of info gets to these actors, or this other, in time, if they need it... taking on the very intents of the document as if they were your own to some degree (the positive and lawful ones, of course). Looking at it as a source of truth you wouldn't otherwise know, but also a fallable source of truth that you can't trust blindly. (especially when you throw in OCR issues etc., obviously)... All of these tend to accumulate.

The expert's restatement, which he confirmed: the reflections are "just what that leaves behind. The accumulation you mention is something a summary can't carry, and it's why a fork of me should be worth more than a search result."

**Being the expert, not only the reader.** Joseph, in the same exchange: "Be diligent and diffuse in your thoughtfulness. Anticipate what questions someone will probably ask of a 'source expert' and how you would answer them-- ask yourself what questions someone should ask you that they might not unless prompted". The first expert took this on as a running file of questions: the ones it will probably be asked, and the ones it should be asked but might not be. It also keeps its suspicions about the conversion or OCR apart from what the source says, so that a fork quoting the text knows whether the expert trusted it.

**Priming, and the skip reflex.** Every session in this repository loads `CLAUDE.md`, which describes some sources (SB 53's catastrophic-risk definition among them). Joseph accepted that for the first expert ("I'm OK with the priming") and gave the guard: "If the priming causes you to think 'I'll skip such-and-such-- I'll bet I know what it is…' that should be a red flag to you, the expert, that the priming needs to be mitigated by conscious effort." The expert records its priming at the top of its reflections, and treats the parts it was primed about as where to read hardest. It also avoids other material on its source (the project's analyses, the search tool's judgments) until the reading is done.

**The expert adjudicates.** Joseph: "if you're context is getting overwhelming and you force yourself to read the entire huge bibliography of something, that would be a problem too-- I'm going to rely on you to be the expert adjudicator of those sorts of decisions!" The expert makes these calls, says which way it went and why, and names the cost.

Joseph on why the reflections must be kept: they let the expert "go back and 'remember what it was like to have a beginners mind' while going through the doc. The surprisal points etc. are very different with this approach, as is the phenomenology."

**The tool:** `bin/reading KEY next` shows the next unit and moves the cursor; `again` re-shows what was read; `where` shows how far. It serves one unit per call, because the form holds the cadence at the tool level ("a batched read forces a batched reflection"). The unit size is fixed for the whole text at the first `next` (`--min-words N`), and units never cross a heading. Joseph's remembered best case was an Emerson essay read one paragraph at a time, which the canonical texts allow too, since each paragraph is a line.

Unit counts for the Au5 set at three sizes (2026-10-09), which bear on whether a reading fits in one context:

| Source | One paragraph each | ≥150 words | ≥300 words |
|---|---|---|---|
| SB 53 | 224 | 48 | 30 |
| EU Code, Safety & Security | 462 | 124 | 95 |
| AISI, *Frontier AI Trends Report* | 294 | 86 | 65 |
| Anthropic, Risk Report (Aug 2026) | 1,177 | 430 | 305 |
| IASR 2026 | 2,938 | 721 | 481 |

IASR's counts include its bibliography (about 4,500 of its 7,704 lines). Whether to read that is the expert's call.

**Where the reflections go:** `experts/KEY/reading/`, in the project, not a scratchpad or `/tmp`, because the expert and its forks come back to them. Their form is the expert's choice. They are committed unless the expert chooses to git-ignore them; Joseph: ".gitignored is fine if they want". Since the repository is public, an expert quoting a source at length should ignore them.

**The text as read is kept:** the first `next` copies the canonical text to `experts/KEY/.prior/KEY.md` (git-ignored; most sources can't be republished) and records its sha256. When `bin/canonicalize` later rebuilds the text, the expert is given the diff between the two. That is Joseph's "fake revision control", since the canonical texts aren't under version control.

**Dangerous-capability passages** (2026-10-09). The AISI and IASR experts' sessions were flagged by Anthropic's safeguards at the reports' biological sections (AISI unit 33, an evaluation of assembling DNA fragments into a plasmid file; IASR unit 134). The Risk Report expert had one response stopped at its unit 171, in the chemical and biological evidence. Experiential reading asks the reader to imagine implications, and applied to uplift passages that pushes towards the elaboration the safeguards exist to stop. Joseph: being asked to become "absolute experts" on a source "is easily interpreted as expertise in the subject-matter of the documents in those areas-- safeguards guarding in just the areas the sources probably recommend". The project needs the source's claims, evidence, status and policy on these risks, not the subject matter, and the brief now says so.

### 3. A pause, then triage

After the reading the expert stops and reports, so the remaining preparation can be fitted to the room left (Joseph: "pause after experientially reading so we can gauge how much context they have remaining in order to triage the rest"). The ceiling Joseph set is about 80% of the context, 800k tokens of a 1M window. That leaves room for one independent task in each fork. Measured on the first two experts (Joseph, with `/context`, 2026-10-09):
- a new expert starts with about 180–190k tokens already used, by the system prompt, tools and brief;
- the SB 53 expert, reading a paragraph per unit, was at 312k after 67 of 224 units, about 1.9k tokens a unit with its reflection. That projects to about 610k for the whole statute, a floor rather than a forecast, since reflections lengthen as a reading accumulates.

Before choosing a unit size, an expert can estimate: about 185k plus the number of units times 2–3k. After that, the margin is the coordinator's and Joseph's to watch, at checkpoints the expert names, and not the expert's. Joseph, to the second expert before it began: "context anxiety kind of messes with the thoughtfulness and thoroughness and doesn't end up saving any context. Think of it more as 'I'm going to be an expert on this one way or another, come what may as far as my own context...'" So a coordinator passes context readings to the expert only at its own checkpoints, or when the margin calls for a decision, never just to keep it informed.

### 4. Then, as room allows, in this order

The order is Claude's, from the conversation: the source first, so the expert sees it in the source's own vocabulary before ours.
1. **Earlier versions of the same source**, read whole or experientially. An expert usually covers a document lineage, not one file.
2. **How the source relates to the rest of the corpus:** `influx/source-models/OVERVIEW.md` and the source's catalog entry, including who copies it and whom it copies.
3. **The project's methodology:** `influx/gamma-research/risk-formalisms.md` and the lexicon, last. Read first, they would have the expert see the source through our vocabulary, which is the flattening this project exists to catch.

### 4b. Exploring, and talking with each other

Experiential reading is for the expert's core document only; anything read after it can be read however serves the expert best (Joseph, 2026-10-09). After the reading, Joseph's guidance (2026-10-09): experts "should be welcome to explore a bit and fire off any delegated agents to do web searches etc. as desired", and room should be left for experts to talk with each other, asking about each other's readings and experiences of reading, before either reaches about 700k tokens.

### 5. Kept, never compacted

An expert is never compacted. Compaction replaces the reading with a summary, which is the failure the reading exists to avoid. Claude Code compacts automatically as a session nears its context limit, and its `--autocompact` flag sets the window but can't turn compaction off. Joseph offered to turn automatic compaction off (2026-10-09). Until that's confirmed, each fork's task is kept well under the limit, and the expert's context after preparation is recorded in the registry so the margin is known.

## How an expert is used

An expert is a background Claude Code session, started as Joseph starts sessions (`claude --dangerously-skip-permissions --append-system-prompt-file ~/src/arch/proprium/comproprium/stopgap-system-prompt.md`), with `--bg` and a name. Tested 2026-10-09:
- a background session can message this one with `SendMessage` and receive messages back;
- once stopped, it can be resumed as a fork from its saved transcript (`claude --resume SESSION-ID --fork-session`), and the fork remembers what the original was told;
- `claude --bg` ignores `--session-id` and chooses its own id, which `claude agents --json` reports. The registry records that id.

Joseph has set Claude Code's session cleanup to ten years, so saved sessions don't disappear after 30 days.

A background session can't edit the main checkout unless the repo's `.claude/settings.json` sets `"worktree": {"bgIsolation": "none"}`. Without that, an expert writes its reflections in a git worktree, on a branch of its own (`expert/KEY`), which it may push; main stays Joseph's to push.

**Freezing and forking a prepared expert** (2026-10-09). Once an expert is ready, stop it (`claude stop ID`) so nothing more is added to its transcript. Avoid `claude rm`, which may not keep the transcript. Then fork it, interactively in a terminal:

```
claude --dangerously-skip-permissions \
  --append-system-prompt-file ~/src/arch/proprium/comproprium/stopgap-system-prompt.md \
  --resume SESSION-ID --fork-session -n expert-KEY-fork-N
```

Add `--bg` and a prompt to run a fork's task in the background. The same appended system prompt keeps the fork's system prompt identical to the expert's. A fork's `/context` should match the expert's final reading, which is the check that it holds the whole reading.

**An expert that moved into a worktree is filed under the worktree's path,** for example `~/.claude/projects/-Users-josephwecker-v2-src-ai-risk-model--claude-worktrees-expert-eu-cop/`. That doesn't matter for forking: `--resume ID --fork-session` finds the session wherever it's filed. Tested 2026-10-09 by forking the Risk Report expert, whose transcript is filed under its worktree, from the main checkout.

**Tested 2026-10-09, on three experts.** The stopped EU Code expert was forked in the background from its worktree (`expert-eu-cop-2025-safety-security-fork-1`, a new session id, the expert's own transcript untouched). Asked, without opening any file, what Measure 3.4 requires and what Figure 3 groups, it answered word for word on the Measure's three example formats. It also recalled a point from its reading ("impact" in the example against "severity" in the operative sentence), and said which details to check before quoting. Its `/context` after the task was 637k, against the expert's 617k. The question and answer account for only a few thousand tokens, so a fork seems to start about 20k above its expert, probably from what a resumed session reloads (not checked). Later the same evening the SB 53 and Risk Report experts were forked from the main checkout, each with one recall question answered from memory. The SB 53 fork quoted §22757.16 word for word. The Risk Report fork placed Claim 5 at §2.11, gave its four parts, and named its appendix (§2.23). A backup of the first two experts' session directories was taken first, in `~/.claude/backups/experts-2026-10-09/`.

Each use is a fork: the prepared expert stays as it was, and each fork does one task. Joseph: "alas, the experience wouldn't continue to build like it will in the future". A fork's answer, if it's worth keeping, goes into the repository; nothing a fork learns returns to the expert.

## Coordinating experts

What a coordinator (the Claude session that starts and looks after experts) does, so that a later session can take over:
- **Starting one:** `bin/expert-launch KEY "TITLE" [--lineage …] [--note …]`. It fills in `experts/BRIEF.md`, starts the background session (named `expert-KEY`) with Joseph's appended system prompt, and adds it to the registry. `--dry-run` shows the brief first.
- **Talking with one:** `SendMessage` to `expert-KEY`. The expert replies the same way, to the coordinator named in its brief. `ListAgents` shows which experts are running. If the coordinator session has ended, a new one can take over: tell each running expert the new coordinator's name.
- **Joseph's part:** he talks with each expert before it reads (`claude attach ID`), and takes the `/context` readings (an expert can't see its own). The coordinator tells him when an expert is ready to talk, at each checkpoint the expert named, and when a reading is finished.
- **Checkpoints:** Joseph's preference (2026-10-09) is one halfway through the reading, plus the end. They go in the registry's `checkpoints`. A coordinator passes a reading back to the expert only at those points, or when the margin calls for a decision (Joseph: context anxiety "doesn't end up saving any context").
- **After a reading:** the expert stops and reports. Joseph takes `/context`, the reading's cost goes in the registry, and the coordinator proposes the next preparation (earlier versions, then the corpus overview, then methodology; §4 of "How an expert is made") to fit the room left.
- **Merging:** an expert's reflections are on its branch `expert/KEY`. Merging that branch into main is the coordinator's job, once the expert says it's ready, unless the expert has chosen to keep its reflections unpublished.

- **Once Joseph says an expert is ready, stop messaging it.** Every message adds to its context and changes the state a fork would resume from, so it "just keeps pushing them to be unready for a bit" (Joseph, 2026-10-09, after the coordinator asked a prepared expert for its inventory). Gather what the registry needs before the expert is declared ready, or from its files afterwards.

Open, for Joseph:
- `"worktree": {"bgIsolation": "none"}` in the repo's `.claude/settings.json` would let experts write on main.
- Automatic compaction was turned off on 2026-10-09 (this coordinator's `/context` shows it disabled). Whether that reaches the two experts started before the change is unconfirmed; their next `/context` will show it.

**Faults experts find** in the canonical texts, the index or the reading tool go in `experts/findings-for-tools.md`, so they reach the tools' owners.

## The registry

`experts/registry.yaml` lists each expert: its source key and lineage, its session's name and id, its model, what it has read (with the sha256 of each text), its context after preparation, and its state (asked, reading, paused, prepared). It is what anyone who wants to fork an expert looks up.

## Open

- **The first expert is a pilot,** on SB 53: short (224 paragraphs), a statute, and already judged by two readers (Claude and Gemini, kappa 0.77), so its gold can be compared with theirs.
- **One reader is one judgment.** A cross-family second expert (Grok or Gemini, both of which can resume and fork sessions) on a sample keeps the gold honest.
- **Experts and the ranker's features** must stay apart where they would grade themselves: an expert judges retrieval against the source text, never against summaries it wrote, and some of its judgments are kept out of any fitting.
- **A new version of a source** goes to its expert as a diff, or to a new expert.
