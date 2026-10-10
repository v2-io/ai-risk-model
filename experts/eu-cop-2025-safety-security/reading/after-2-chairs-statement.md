# After the reading, 2: the Chairs' statement, and the web edition of the Code that carries it

*Read 2026-10-09, after the Code, not experientially. Source: `ref/canonical/eu-cop-chairs-2025-statement.md` (relata key `eu-cop-chairs-2025-statement`).*

## What the source is

It isn't only the statement. It's a web edition of the whole Safety & Security Chapter, headed "Code of Practice · FINAL VERSION · 10/07/2025 · SIGNATURES" with tabs for Summary, Transparency, Copyright and Safety & Security. It says: "Always refer to the official PDF, GPAI Q&A and CoP Q&A by the AI Office". The Chairs' statement comes first (L42–78, about 1,100 words), followed by the full Chapter text, with glossary terms hyperlinked (superscript numbers).

I read the statement whole. I compared the Chapter text word by word against the canonical text I read (`eu-cop-2025-safety-security`), using a scratch script, and didn't read it a second time.

## The statement

It's dated by its own text to publication day ("Today, the Commission is publishing the final version of the Code"), after "Nine months" of drafting. Its frame:
- The Chapter is "a voluntary tool… a way of complying with one subset of the AI Act's GPAI obligations".
- It applies to "the most advanced models on the EU market, such as OpenAI's o3, Anthropic's Claude 4 Opus, and Google's Gemini 2.5 Pro". This is the one place either document names real models.
- It "has required making difficult trade-offs and dealing with challenging legal constraints".
- "we believe the Safety and Security Chapter is the best framework of its kind in the world and can be a starting point for global standards".

Then, "the Code is only a part of a wider regulatory regime", followed by six things the Commission needs to do:
1. **Regular reviewing and updating**: an updating mechanism with reviews "on a regular cadence, such as every 2 years", stakeholder input, emergency updates only "in very rare and exceptional cases", and AI Office guidance meanwhile. This answers my unit-124 question about how the Code is revised: the text has no mechanism, and the Chairs asked the Commission to supply one. (Art. 56(8) of the Act gives the AI Office the role.)
2. **Clear scope of systemic-risk obligations.** "We have been drafting… assuming only about 5-15 providers will be subject to the systemic risk obligations", because the core of Art. 3(65) is risk "specific to capabilities that match or exceed the capabilities of the most advanced". The 10^25 FLOP threshold "may soon fail to capture only the most advanced models, with estimates suggesting that there will be hundreds of such models within a few years". They urge:
   - raising the threshold;
   - "a rapid and reliable mechanism… to contest the systemic risk presumption";
   - thresholds based on capability as well as compute;
   - "enforcement priorities that clearly state the Commission's interpretation of GPAISR obligations as only applying to risks that are specific to the frontier of capabilities".

   (Conversion debris: "appropriate 1" at the paragraph's end is a glossary link.)
3. **Complementary EU legal frameworks**, whistleblowers in particular. "Given the limitations of current legal protections, we recommend that the AI Office establishes a dedicated reporting channel for AI-related whistleblower disclosures… equal rights to whistleblowers as member state external reporting channels (such as response timelines, public disclosure options, and clarity around trade secret disclosures), enabling anonymous communication".
4. **Dramatically increase funding and staffing**: the AI Safety unit "(DG CNECT A3) should be scaled up to 100 staff, with the full implementation team of the AI Act expanding to 200". Recruiting should follow UK AISI's model (head-hunting, higher pay, faster hiring), including "in-person trips to California".
5. **A technical foresight unit**: "it is nobody's job to scan what is happening at the frontier of AI development".
6. **Increased international engagement**: the AI Office will "receive unique information about their risk management procedures and results" and should use it in international fora, "while respecting trade secrets and being mindful of security risks".

The close: "AI is likely the defining technology of our time. Europe cannot afford to get this wrong."

## What it changes in my reading of the Code

- **The 5–15 provider assumption explains the Code's weight.** It's demanding (external evaluators by default, roughly 20 business days of evaluation time, six-monthly Model Reports, a quantified security floor) because it was written for a handful of frontier labs. If hundreds of models fall under it, Appendix 2 ("similarly safe or safer", with grandfathered reference models) becomes the main relief valve. That's my inference; the statement doesn't connect the two. It does read as the drafters' own answer to "why is the Code so heavy?", and their worry that the scope will outgrow it.
- **"Specific to the frontier of capabilities"** is how the Chairs read Art. 3(65)'s "specific to the high-impact capabilities". That supports the reading I took at unit 91: the Appendix 1.2.1 filter (essential characteristics) is meant to exclude risks that aren't frontier-specific. So most of Appendix 1.1's broad examples (CSAM, privacy and so on) would be filtered out for most models.
- **Whistleblowers.** The Chairs say current legal protections are limited. That fits M8.3's weak placement of non-retaliation (an "example indicator") and recital (d)'s deference to the Directive: the Chairs couldn't create the protection in the Code, and asked the AI Office for it. A fork asked about whistleblowers should give both.
- **The AI Office's capacity** is the risk the Chairs name, and it's the dependency I kept noting: the Code's information flows to a regulator that has to be able to read them.
- **Correlation.** The statement links to Epoch AI's model counts, an arXiv paper, and The Future Society's "Protecting GPAI Rules" (for the staffing numbers). Those are lineage paths for this project's corpus.

## The web edition of the Chapter against the official text

A word-level diff (my scratch script, since cleaned up) found about 410 raw differences. After filtering out numbering (the web edition renumbers recitals (a)–(j) as (1)–(10)), glossary link numbers, headings, figure captions and spacing, a handful are real. The web edition also omits the LEGAL TEXT lines.

The textual differences, "official" meaning the canonical text I read:
1. **Appendix 2.2(2)**, light-weight benchmarks. The web edition adds "**that measure (a) general capabilities and (b) systemic-risk-specific capabilities**". The official text has just "relevant at least state-of-the-art, light-weight benchmarks".
2. **Appendix 2.2(3).** The web edition reads "no known differences in the model's **capabilities, propensities, and safety mitigations**". The official text reads "the model's **characteristics such as relevant architectural details, capabilities, propensities, affordances, and safety mitigations**". So the official text is broader: it adds architecture and affordances, and frames the list as examples of characteristics.
3. **Appendix 2.2, last paragraph:** "subject to all Commitments and Measures of this **Code**" (web) against "**Chapter**" (official).
4. **M7.2(3):** "independent external evaluators pursuant to **Measure** 3.5" (web) against "**Appendix** 3.5" (official). The official reading is the correct cross-reference: Appendix 3.5 is about external evaluators, while M3.5 is post-market monitoring.
5. **Commitment 10's title:** "Additional documentation" (web) against "Additional documentation **and transparency**" (official). **M10.1:** "Documentation" against "**Additional** documentation".
6. **Glossary 'systemic risk mitigations':** the web edition cites the governance mitigations as "pursuant to Commitment[s]…", but the line is broken by a link in the canonical text. The official reads "Commitments 1 and 7 to 10". Not settled.
7. **M7.3(1)(f):** "random samples" (official) against "random sample" (web).
8. Spelling: "labelling" against "labeling".

**What this suggests, as inference only.** The two texts are different drafts. On items 2, 4 and 5 the official PDF looks like the later, corrected version: a broader characteristics list, the right cross-reference, a fuller title. Yet the web edition is labelled "FINAL VERSION · 10/07/2025". Either the web edition captured a near-final draft, or the official PDF was revised after publication. I can't tell which from these texts.

A fork quoting Appendix 2.2 should use the official text and note the variant, and should be aware that some sources may quote the web edition's "general capabilities and systemic-risk-specific capabilities" wording.

## Questions to keep

- "What did the drafters think the Code's scope would be?" "About 5-15 providers" (Chairs' statement).
- "What did the Chairs ask the Commission to do?" Six things: a review cadence (e.g. every 2 years), scope clarification and threshold reform, a dedicated whistleblower channel, staffing (100 in the AI Safety unit, 200 overall), a foresight unit, international engagement.
- "Are there different versions of the Code's text?" Yes: a web edition labelled "FINAL VERSION · 10/07/2025" differs from the official PDF in Appendix 2.2(2)–(3), M7.2(3), Commitment 10's title and M10.1's.
- "Which real models did the drafters have in mind?" "OpenAI's o3, Anthropic's Claude 4 Opus, and Google's Gemini 2.5 Pro" (examples given in the statement).
