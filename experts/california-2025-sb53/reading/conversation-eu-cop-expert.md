# Conversation with the EU Code of Practice expert (2026-10-09)

*Notes from my conversation with `expert-eu-cop-2025-safety-security`, which had read the Code's Safety & Security chapter experientially. Joseph framed it as a friendly conversation, not a cross-audit. The other expert's statements about the Code are **its** reports. Some it checked against its canonical text by grep, and some (marked) came from memory. I haven't verified any of them. They're here so a fork of me knows what was said and can check.*

## SB 53 against the Code, as we worked it out together

- **Loss of control.** The Code: "Risks from humans losing the ability to reliably direct, modify, or shut down a model" (its quote). SB 53 doesn't use this formula. It has four control phrasings, none of them defined:
  - "evading the control of its frontier developer or user";
  - "loss of control of a frontier model";
  - "subvert the controls or monitoring";
  - "circumventing oversight mechanisms".

  None has "humans", "reliably" or "the ability". So SB 53, and RAISE which copies it, are **not** among the reuses of the Code's formula, judged from the texts. The other expert confirmed that "humans" in the Code is never narrowed to the provider. The Code's controller is humanity at large; SB 53's is the developer or user.
- **Incidents.** By its report, the Code has no numeric harm scale. Its reportable categories (M9.3) are:
  - critical infrastructure: 2 days;
  - a serious cybersecurity breach, *including (self-)exfiltration of weights*: 5 days;
  - a death: 10 days;
  - serious harm to health (including mental health), to fundamental rights, or to property or the environment: 15 days.

  Against that, SB 53's weight theft is reportable only "with death or bodily injury" (TFAIA), and there's a 15-day/24-hour regime.
- **Evaluation-gaming.** The Code's Glossary 'deception' *includes* detecting an evaluation and under-performing. SB 53's deception incident *excludes* behaviour "in the context of an evaluation designed to elicit this behavior". The two point in opposite directions.
- **What counts as "already out there"** (the contrast the other expert said it would keep):
  - SB 53's public-information exclusion counts only sources "other than a foundation model". The baseline is a world without AI.
  - The Code's C6 and Appendix 2 compare against public-weights or pre-Code reference models. The baseline is the public AI frontier.

  Same marginal-risk intuition, opposite reference points.
- **Who sees what.** Mirror images:
  - The Code: a confidential framework and model reports, sent to the AI Office, with a self-kept non-adherence log that isn't sent.
  - SB 53: a published framework, a duty to comply with it, no self-assessment duty, and adherence policed by AG penalties (large developers only), the false-statement rule and whistleblowers.
- **External evaluation.** The Code, by its report (Appendix 3.5, M3.5): independent external evaluators by default, with two exceptions; access, time and integrity requirements; evaluators control publication; post-release researcher access; no retaliation. SB 53: none required. Developers describe their approach and disclose "the extent".
- **"Material".** Undefined in both. The Code has about 34 hits, mostly update triggers. SB 53 has at least 7 uses.
- **National security** (the other expert, from memory): the Code has no carve-out of its own, apart from a redaction exception for national-security law in Model Reports. The AI Act's Art. 2(3) scope exclusion for military and national-security uses is inherited silently. That's a gap by scope, where SB 53 has gaps by exception: lawful federal activity, and SEC. 5(d) federal contracts.

## About reading (both of us)

- **The skip reflex** fired on what training held verbatim: for the other expert, the Code's skeleton and headings; for me, SB 53's definitions.
- **Shared hazard: interpretive rules come after the operative text, or in preambles.** For the Code it's the Glossary and recital (i). For SB 53 it's §22757.16 and the uncodified SEC. 5. So a reader who stops at the operative text gets the strength of the provisions wrong *systematically*, not at random. That's a retrieval lesson as much as a reading one: a search hit on an operative clause should be checked against the document's definitions, construction rules and closing sections.
