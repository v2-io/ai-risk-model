# Aside after unit 31: Figures 1–4, found and looked at

*Joseph asked (after unit 32 was served, before I'd written its reflection) whether I'd looked in `ref/canonical/msc/<key>/`. I hadn't: I'd assumed the figures were lost. They're there as images: `_page_5_Figure_8.jpeg` (Fig. 1, p.6), `_page_7_Figure_1.jpeg` (Fig. 2, p.8), `_page_8_Figure_0.jpeg` (Fig. 3, p.9), `_page_10_Picture_0.jpeg` (Fig. 4, p.11). The file names use zero-based page numbers. All four belong to text I'd already read, so looking at them isn't looking ahead. One thing does leak: the directory holds only these four images, which suggests the Code has no further figures (or none the conversion extracted). Earlier units said the figures were "not in the canonical text". That was true of the `.md` text and false of the canonical directory. A fork should look in `msc/`.*

**Figure 1 (Framework cycle).** Three boxes: Creating → Implementing → Updating, with the arrow from Updating looping back to **Implementing**, not to Creating. The Implementing box is drawn as a **stack** of cards, as if there are many implementations (per model, presumably) under one Framework. The text didn't say "one Framework, many implementations"; the figure does, visually. It fits M1.1 ("taking into account the models they are developing…"). Creation happens once; updating feeds back into implementation.

**Figure 2 (lifecycle timeline).** One horizontal timeline:
- pink dots before market placement: "Conduct lighter-touch model evaluations at appropriate trigger points";
- a blue dot just before "Market placement": "Complete the full systemic risk assessment and mitigation process before market placement";
- a shaded band from market placement onwards: "Conduct post-market monitoring";
- pink dots continue **after** market placement, so lighter-touch evaluations go on post-market too;
- a second blue dot before "**Model Report update**": "Complete the full systemic risk assessment and mitigation process before Model Report updates".

So the figure makes plain what M1.2's text says through cross-reference: the full process recurs before each Model Report update (M7.6's conditions). The rhythm is: light checks throughout, a full process at release and at each Model Report update, monitoring after release. Notably, the timeline's landmarks are **market placement and Model Report update**. Internal deployment has no landmark at all. That's the internal-deployment pattern from units 12–20, drawn.

**Figure 3 (full process loop).** Start → Systemic risk identification → Systemic risk analysis → Systemic risk acceptance determination. "Acceptable" → **Proceed**. "Not acceptable" → Systemic risk mitigation → back to identification. A brace labels identification + analysis + acceptance determination together as "**Systemic risk assessment**", so in the Code's vocabulary *assessment* = identification + analysis + acceptance determination, and *mitigation* is outside assessment. That's a definitional fact the text implied (the title "systemic risk assessment and mitigation") and the figure states. For the lexicon: assessment ⊃ {identification, analysis, acceptance determination}; mitigation is separate.

What the figure lacks: **no "do not proceed" exit.** The only way out of the loop is "Acceptable → Proceed". A risk that can't be made acceptable keeps the loop running forever, and nothing in the figure shows stopping, pausing development or withdrawing. Whatever M4.2 says about not proceeding isn't drawn here. (The text takes precedence, so M4.2 will decide. But a reader taught by the figure would think the only outcomes are "mitigate" or "proceed".)

**Figure 4 (identification).** "Potential systemic risks" (from "Compile a list of risks that could stem from the model and be systemic") go into a **funnel** ("Analyse relevant characteristics of these risks (e.g. their nature and sources)"), and out come "Identified systemic risks" ("Identify the systemic risks stemming from the model"). "**Specified systemic risks**" sit in a separate box and are routed by a line **around** the funnel, straight into Identified systemic risks. Then "Develop appropriate systemic risk scenarios for each of the identified systemic risks" → "Systemic risk scenarios".

This confirms my unit-24 reading exactly: the specified risks bypass the filter; they're identified by stipulation. The funnel metaphor also says that the process risks are *narrowed*: many potential risks, fewer identified. The text's "could stem from the model and be systemic" is the wide mouth; nature and sources are the filter.

**What the figures add, in one line:** (1) one Framework with many implementations; (2) the full process recurs before every Model Report update, and light evaluations continue after release; (3) "assessment" excludes mitigation; (4) there's no drawn exit for "can't be made acceptable"; (5) specified risks bypass the identification funnel.

**Questions to keep.**
- "Where are the Code's figures?" `ref/canonical/msc/eu-cop-2025-safety-security/`, as jpegs, four of them.
- "What does the Code mean by 'systemic risk assessment'?" Fig. 3: identification + analysis + acceptance determination; mitigation is separate.
- Should be asked: "Does the Code show what happens if risk can't be made acceptable?" Fig. 3 has no such exit; see M4.2.
