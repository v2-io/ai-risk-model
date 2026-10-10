# After reading the earlier expert's reflections (2026-10-10; Sonnet 5.5 expert)

Read after my own reading was finished and committed: their 000-before, 001-032, text-suspicions (they read 32 units at --min-words 100, Opus 5.5). Written to keep what the comparison taught apart from my first-encounter notes.

## Corrections to my own notes
1. "All systems" (my unit 34) was a conversion error for "AI systems"; they had logged it. Already corrected (98, 01).
2. Figure 3 last point: I wrote ~1h10m with an interval from under an hour to over 1h35m (my unit 30). Re-measuring the image's gridlines, their reading is right: about 1h20m, interval about 1h00m to 1h37m. The qualitative point (the "over an hour" headline rests on one model; every other point is below 45 minutes) stands, but the lower end of the interval sits at about one hour, so the headline is borderline at its lower bound rather than clearly straddling it.
3. Both of us inferred in the same wrong direction that the error bars capture repeat noise and not task selection (their unit 20, my unit 25); the appendix (my unit 112) says the SEM is over tasks. Two instances of nearby models reading the same sentence agreed with each other and were both wrong, which is a small live specimen of "agreement among our readings is restatement, not corroboration".

## Things they saw that I did not (or not as sharply)
- Figure 1.2: at about 2025.3 the expert-tier success (about 18%) sits above the practitioner tier (about 5%): the difficulty ladder is not monotone in model success, and the expert tier may be only a few tasks. I recorded both tier values but not the ordering.
- Figure 1.3: the late-2025 AI R&D point (~19%, interval ~0-40%) sits far below the 42% envelope: the envelope holds a high early point while a later model scores lower (the winner's-curse pattern). I noted the wide bars, not the lower later model.
- The report's x-axis is initial-release date, so "trend" is over release dates (they inferred it early; the appendix confirms it, my unit 110).
- Staff lineage (several AISI staff come from the labs whose models are tested) as shared-lineage information for the independence ledger; the "Security" rename as a possible scope signal; the report's single verb "evade" for both users-against-safeguards and models-against-human-control.

## What my later reading answers for them
- Who graded long-form protocols (their unit 18)? Fig 7's caption: an LLM judge with two grading models; real-world feasibility validated on "select" protocols. Troubleshooting is "auto-graded by a set of LLM judges" (Fig 8). Grader identity for the open-ended QA sets is not stated in the report.
- Is AGI defined (their unit 15)? Yes, in the glossary: "matches or surpasses humans across most cognitive tasks".
- Practitioner tier range (their unit 29)? Glossary: 3-10 years; apprentice is 1-3 years there, against "<1 year" in a caption.
- Is the software-task/AI R&D link argued in Section 5 (their unit 12)? No. See the next item.

## A finding from the comparison that neither of us made alone
Fig 1.3's caption says "See Section 5 of the report for more about our autonomy tasks", and the contents names Section 5 "Loss of control risks". Section 5 as I read it holds only self-replication (5.1, RepliBench) and sandbagging (5.2). The "simplified AI R&D" and "basic precursor skills" lines of Fig 1.3 are not discussed in Section 5 at all; their only appearances are in Fig 1.3, the autonomy domain list, and the software-task figures of Section 2 (Agents), which are not labelled as AI R&D there. So the pointer lands on a section that covers one of the three risk areas; and their expectation that the software tasks "end up in the LoC section" (their unit 13) did not hold. A fork asked what the report says about AI R&D acceleration should answer: a risk-area label and one proxy figure (hour-long software tasks), no argument.

## Style note, for whoever compares the two readings
They tied their notes to the repository's lexicon and CLAUDE.md as they went (e.g. candidate `aisi:` terms, the EU Code formula, the alignment map); I kept the repository's material out until the end. Theirs are richer as lexicon work-in-progress; mine are closer to the text and were less likely to carry a project frame into a claim. I can't say which is better for forks; they are different instruments.
