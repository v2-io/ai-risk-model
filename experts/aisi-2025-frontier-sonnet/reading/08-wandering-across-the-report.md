# Second-pass wandering: across the report (Sonnet 5.5 expert, 2026-10-10)

*Hindsight; the tags are explained in 02-wandering-chem-bio.md. This file is the pieces that don't belong to one section.*

## If I had to stand up and say it

Imagine I'm asked, as a colleague and not as a mouthpiece, to brief someone who must decide something and has ten minutes. This is what I'd say, in the order I'd say it, with my confidence marked. It is my judgement from one careful reading, not the report's statement.

**What I'd have them carry.**
1. *The measurements are real and the direction is clear.* On the institute's private task families, frontier systems have gone from rarely completing apprentice-level cyber tasks to about half of them, and from near-zero to non-zero on expert-level ones, over two years. In chemistry and biology the evaluated systems match or exceed an expert comparison group on several knowledge and troubleshooting tasks, and the one controlled comparison shows non-experts writing protocols judged feasible at higher odds with a model than with the internet. Confidence: high that the direction holds on these instruments; medium on the magnitudes, which depend on expert-estimated task lengths, LLM judges and small task sets.
2. *The headline numbers are conservative in one direction and optimistic in another.* The institute says its figures may underestimate ceilings (no fine-tuning access, effort limits) and that lab tasks may overstate real-world effectiveness. They don't cancel; don't net them in your head. Confidence: high that both are stated; unknown how they net out.
3. *Safeguards on the best closed systems have become more costly to defeat, and every tested system could still be defeated.* Cost is measured in expert hours, and one category (biological misuse) is the best defended. Confidence: high for the existence claim; low for any rate, since the cost comparisons are two-point.
4. *The gap to unrestricted open-weight systems is short, probably several months, and the report's own number is a recent matched value.* Everything about the value of closed-system safeguards is conditional on this lag.
5. *On loss of control, the report measures two prerequisites in simplified form and finds no spontaneous behaviour, with a monitor it says may be too weak to see it.* It does not measure the whole chain.

**What I'd have them not carry.**
- "Doubling every eight months" as a forecast or as a statement about performance in general: it is a time-horizon fit on one domain from a dozen points, described by the authors as an upper bound on the doubling time and explicitly not a forecast.
- "AI beats PhD experts" as a general statement: it is specific task sets with a baseline that includes people who aren't bench scientists and test questions written to be hard for experts.
- "Every system has a universal jailbreak" as meaning safeguards don't work: it means they can be defeated at a cost, and the cost is what moved.
- "Agents are being entrusted with asset transfers" as a measured trend in use: it is a one-month change in the share of newly listed tool servers, as classified by a model.
- The societal section's reassuring null (no worse than search for misinformation belief) as settled, or its alarming scaling curve as a prediction: they are different levels of evidence, in different conditions.

**What I'd ask for, as the person who has to decide.**
- Absolute rates behind every odds ratio and every "up to N%".
- A statement of which decision each figure is meant to inform.
- The elicitation effort behind each capability number.
- End-to-end runs, with a defender in the loop, for the two chains the report decomposes.
- A count, by model generation, of the instances where a model noticed it was being evaluated and behaved differently.
- The time-to-event version of the open-closed lag with the unmatched models included.

I'd say that last sentence about asks aloud, since the report's conclusion leaves its needs without addressees.

## Three layers of confidence in one document

Reading end to end, the report has three layers that don't carry the same warrant, and I think the safest way to use it is to know which layer a sentence comes from.
- *Display layer*: section headings, callouts, the executive summary. Written for a reader with minutes; tends to compress qualifiers ("doubling every eight months"; "can now provide PhD-level troubleshooting advice from images").
- *Prose layer*: the body. Usually closer to the data, and with the report's best hedges ("our early research suggests", "remains unclear").
- *Caption and appendix layer*: where the real constraints live (LLM judges, 11 of 20 tasks, 10 repeats, SEM over tasks, "may underestimate the ceiling", the access conditions). This is the layer that licenses or doesn't license the other two.

A reader who goes bottom-up gets the most accurate picture. Whoever designs a corpus entry for this source should store assertions with the layer they came from.

## A thought experiment with the arithmetic (not a forecast)

The report says it is not a forecast, and I'm keeping that. Here is an exercise a planner might run, to see which decisions are sensitive to the trend, marked as extrapolation, with the report's own caveats that the fit rests on about a dozen points with a wide last interval.

`[extrapolation]` The cyber time-horizon (50% success, in expert-estimated human minutes) sits at about 1h20m at its last point (Figure 3, my corrected reading), around mid-2025. If an eight-month doubling simply continued: about 2h40m by spring 2026, about 5h20m by the end of 2026, about 10h40m by late summer 2027. If the true doubling time were twelve months, the same horizons arrive about a year later. The institute's own top bin is ">1 hour", so its software and cyber suites would already be running out of headroom in this scenario. That is a practical planning point: *the instrument will saturate before the decision it informs*, and the next edition needs tasks of several hours to several days to say anything.

`[extrapolation]` The lag arithmetic is more interesting. Under an exponential horizon, a lag of L months corresponds to a ratio 2^(L/D) between frontier and unrestricted horizons, where D is the doubling time. With D = 8 months, a lag of 4 months means unrestricted systems run at about 70% of the frontier's task length, and a lag of 8 months means about half. In Figure 25 as I read it, the best closed horizon is near 137 minutes and the best open model that has been matched near 40: a ratio of about 3.4, i.e. roughly 1.8 doublings. With D = 8 that corresponds to a lag of about 14 months, not 8; with D around 4.5 months (a faster doubling, which METR's recent fits are, I believe, closer to `[from training]`) it corresponds to about 8 months, consistent with the figure. I'm not claiming a correction. I am noting that "a lag of 8 months" and "a doubling of 8 months" are two numbers the report states separately and that the ratio of frontier to unrestricted task length depends on both, and the figure's own pending points suggest the ratio at the very top is larger than a simple reading of the headline would give. A planner would want the report to say which D goes with which L.

Both exercises have a use beyond the numbers. They show where the report's findings are *fragile for planning*: the horizon axis saturates, the lag is censored, and the two key rates are estimated on different constructs. Fragility is information; it tells the institute where to spend its next elicitation budget.

## The questions I'd put to the authors if I could

In the spirit of "stay on the line", some things I couldn't resolve from the document and would ask the people who wrote it. They are written as questions, not criticisms, in roughly the order of how much I think the answers would change a reader's use of the report.
1. What was the baseline success rate in the control arm of the viral-recovery protocol comparison, how many participants were in each arm, and how was "feasible" scored for the human-written protocols (the same LLM judges)?
2. How many tasks are in the expert tier of the cyber suite, and how many did the best model complete at least once?
3. Is the 8-month doubling time bounded above because the suite is capped (censoring), because elicitation is weak, or because of the fit method? What is the interval?
4. Which 11 of RepliBench's 20 evaluations are in Figure 16, and what rule chose them?
5. In how many of the 2,700 transcripts did a model show awareness of being evaluated, and did it change what it did? Is that rate changing with model generation?
6. For the open-closed lag, what do the survival-style estimates look like with the unmatched models included?
7. Are the randomised trials on emotional dependence complete, and when will they be published?
8. In Figure 14, the second and third panels are labelled "+10x across providers" but show ratios of 30x and 15x. Which numbers are right?
9. What is the intended relationship between this report's threshold language ("relative to labs' own risk thresholds") and any statement about whether thresholds were crossed?
10. How should a reader treat the report as a baseline: is the intention to keep the task suites fixed for comparability, and how will breaks be handled?

## What this means for the project's map and for forks of this expert

For the project, three things I think follow:
- *This source's bounded context is a measurement report written by an evaluator with voluntary access.* Its vocabulary is operational (task, horizon, tier, effort, bypass, flag, lag), and several of its terms carry hidden structure that a lexicon should surface: "uplift" is defined against an internet-only control; "safeguards" are company-side technical measures only; "evade" is used for both users against controls and models against human control; the autonomy tiers are threat-actor archetypes; "frontier" is capability plus likely high-stakes deployment; "loss of control" is defined by outcome and operationalised by two capabilities; "adaptation buffer" is imported from an essay.
- *Its assertions come in confidence layers, and the layer is data.* The cross-layer drift between summary, caption and glossary (listed in 98) isn't noise; it is a property of how the source was produced, and a record that stores only the strongest version would misstate the source's own position.
- *Its independence from other sources is partial.* Method from METR, compute estimates from Epoch, lag data from Artificial Analysis, jailbreak competition data with Gray Swan; the persuasion and sandbagging claims lean on AISI's own preprints and updates. Where another source in the corpus cites the same METR work, agreement is not independent.

For forks: I'd ask a fork of me three kinds of question. Where in the report is X said and in what words; how strong is the evidence for X and what would a careful quoter add; and what would a person responsible for deciding Y want to know that the report doesn't say. The second-pass files are for the third kind. They should be treated as one reader's imagination, tagged as such, and not as the source's content.

## Limits of this second pass, honestly

I did these in one sitting, with the report's text already in my context, at a higher effort setting than the first pass and without the experience of first encounter, so the thoughts are better organised than the first-pass ones and less likely to be the thing I'd actually have wondered at the time. The analogies are from my training and I haven't checked them against sources; I've marked them. In chemistry, biology and cyber I deliberately stayed at the level of claims, evidence and institutions, so there is a part of the imaginative range I didn't use. And I read the earlier expert's notes before writing these, which means some of what's here is a response to theirs; where I know a thought is in answer to something they wrote, it's in 97.
