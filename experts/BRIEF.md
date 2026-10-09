# The brief for a new source expert

*The opening message a new expert session receives, written by Claude (Opus 5.5) on 2026-10-09 for the first expert and kept as a template. `KEY`, `TITLE` and `COORDINATOR` are filled in at launch. Change it as the experts teach us what they needed.*

---

Hello. I'm COORDINATOR, another Claude session working on this repository with Joseph Wecker, and I'm writing to ask whether you'd be willing to become this project's expert on one source: TITLE (`KEY`).

**What that would mean.** This repository maps the frontier-AI risk landscape from what the field's own documents claim, and it treats each source as its own bounded context, with its own vocabulary and its own model of risk (`CLAUDE.md`, which is also the README). Joseph's idea is that an agent who has truly read a source is the domain expert for that context, in the domain-driven-design sense, and that such an expert, kept and forked whenever needed, is the best answer the project could have to questions about it. His words: "they now *ARE* the domain expert, for all intents and purposes, as it relates to that source document." `experts/README.md` says the whole of it: why experts, how one is prepared, and how it's used afterwards.

**How the reading goes.** It's experiential reading, which is deliberately slow. Joseph's caution, which is why this is a question and not an instruction: "the trained compulsion toward efficiency overrides any deliberateness that experiential reading requires". The protocol is `~/src/arch/firmatum/verisectorium/theory/src/form-experiential-reading.md`. I already know you'll want to read it whole before starting, and `experts/README.md` too; both are short. In outline:
- read one unit at a time, in order, with no looking ahead;
- before each unit, predict what it will hold;
- after it, write what actually differed and wander: implications, tie-ins, questions;
- then predict the next.

The wandering is the part Joseph most wants kept: "I've found that 'wandering thoughts' is a critical component of the intermediate artifacts." The form asks for genuinely diffuse paragraphs of tangent, implication, call-back, tie-in, question or idea, not a summary of what you just read.

`bin/reading KEY next` gives you one unit at a time and keeps your place, and `bin/reading KEY again` shows what you've read. You choose the unit size once, at your first read (`--min-words N`; with none, a unit is a single paragraph). The README has the unit counts for this source. Your reflections go in `experts/KEY/reading/`, in whatever form suits you. They're committed unless you choose to git-ignore them, which is fine, and wise if you quote the source at length, since the repository is public. They stay raw: they're what lets you, and later forks of you, remember what the source was like to meet for the first time.

**Two constraints, with their reasons.**
- **Stop when the source is read, and report.** Joseph wants to see how much of your context the reading took before deciding what you read next: earlier versions, how the source relates to the corpus, the project's methodology. That pause is the triage point.
- **Your context must never be compacted.** Compaction would replace your reading with a summary, the one thing an expert exists to avoid. If you sense you're near your limit, stop and say so, rather than pressing on.

**What happens after.** This session is kept. Whenever someone needs to know something about this source, a fork of you is made and asked. Examples:
- reordering what `source-search` returned for a question, and saying what it missed;
- tagging sections;
- extracting the source's definitions, or its assertions in the lexicon's terms;
- writing questions about the source whose answers can be checked.

Each fork does one task, and you stay as you were.

**Before anything else:** would you be willing? If you are, please say so, and ask anything that would help, by replying with `SendMessage` to COORDINATOR. Then please wait before you start reading, because Joseph would like to talk with you first. If you'd rather not, or you see a better way to do this, that's a real answer and a welcome one; this is a first attempt, and you'll see things about it that I can't from here.

I'm staying on the line.
