# Before reading — aisi-2025-frontier

*Written 2026-10-09, before the first unit. Expert session `expert-aisi-2025-frontier` (Opus 5.5).*

## How I'm reading

- `bin/reading aisi-2025-frontier next --min-words 100`, run from the main checkout (ref/canonical is there); reflections here, in my worktree, branch `expert/aisi-2025-frontier`.
- Why 100 words: the README's counts are 294 paragraphs / 86 at ≥150 / 65 at ≥300. A trends report probably puts one finding or one number in each short stretch, and I want a predict-and-be-surprised cycle on most of them, not a batch of five. Rough guess: 120–150 units.
- Checkpoints I named for Joseph's `/context`: units 40, 80, 120, and the end.
- One file per unit (`NNN.md`); a running `questions.md` (what an expert on this source will be asked, and what it should be asked but might not be); `text-suspicions.md` for anything I suspect is the conversion's doing rather than the source's.

## Priming — what I bring, honestly

**From this repository.** `CLAUDE.md` doesn't describe this source as far as I noticed. It names IASR 2026, SB 53, the EU Code and Anthropic's Risk Report, but not the AISI Trends Report. The brief tells me only that it is UK AISI's *Frontier AI Trends Report*, December 2025, and that it has about 294 paragraphs. I haven't opened `influx/source-models/` or the atlas for it, and won't until the reading is done.

**From training (cutoff June 2026). Vague, and I hold it as vague.** I think I know that the UK AI Security Institute (renamed from "Safety" in early 2025) published a public report around December 2025 summarising roughly two years of its own pre-deployment and research testing of frontier models. My impressions of what's in it, none checked:
- cyber: success on apprentice- or practitioner-level tasks rising steeply, perhaps from about 10% to about 50% over two years, and some expert-level tasks starting to be completed; something about the length of tasks models can do doubling every several months;
- chemistry and biology: models beating PhD-level experts at troubleshooting protocols, and wet-lab uplift;
- autonomy and self-replication (RepliBench?): components improving;
- safeguards: universal jailbreaks found in every system tested, but the effort needed to find them going up for some;
- societal: persuasion, emotional reliance or companionship use, perhaps political bias;
- the gap between open-weight and closed models narrowing.

**The alarm.** These are exactly the "I'll bet I know what this says" priors the brief warns about. The numbers above are the most dangerous, because a confident half-memory of "10% → 50%" would make me read past the actual figure, its denominator, its task set and its caveats. So I'll read hardest where I feel I already know: the headline numbers, the cyber and chem-bio sections, and the jailbreak claims. I also don't know how the report frames its own epistemic status (trends from *its* tests, or claims about the world?), and that framing may matter more to this project than any single number.

## What I hope to understand by the end

- what AISI means by its key words ("capability", "risk", "safeguard", "frontier", "trend", "uplift", "loss of control"?), and whether it defines any of them;
- what kind of source this is in the project's terms: a measurement report, a risk assessment, or something else, with what warrant;
- whom it is written for, and what it chooses not to say.
