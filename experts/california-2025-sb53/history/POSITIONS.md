# SB 53: who supported and opposed it, and what they argued

*Written 2026-10-09 by a delegated agent (Opus 5.5) for the `california-2025-sb53` source expert. The sources are the 14 committee and floor analyses in `analyses/`, read in full, with `versions/` for checking what the text said at each point. This file follows NOTES.md's convention: **Text shows** marks what a file says, with a pointer, and **Inference** marks my reading. Nothing here was committed.*

*To recheck every quote, from `history/`: `python3 -I tools/check_positions_quotes.py` (add `--canonical /Users/josephwecker-v2/src/ai-risk-model/ref/canonical` so the ATF quotes are checked too; that directory is git-ignored and absent from worktrees). The script's docstring lists the kinds of MISS that are expected.*

## Conventions

**Verbatim text is set in «guillemets»**, followed by its file code and line number(s). Guillemets never occur in the sources, so every «…» span can be checked mechanically. `[…]` inside guillemets is my elision. The sources' own `\$` escapes are written as `$`, and their curly quotes are kept. Line numbers are those of the pandoc markdown in `analyses/`.

| Code | File (in `analyses/`) | Hearing / analysis on | Bill version analysed |
|---|---|---|---|
| SGO | `2025-03-20-senate-gov-org-cmte-on-02-27-text.md` | Sen G.O., Mar 25 | 02 (Feb 27) |
| SJUD | `2025-04-04-senate-judiciary-cmte-on-03-27-text.md` | Sen Jud, Apr 8 | 03 (Mar 27) |
| SAPP1, SAPP2 | `2025-04-18-…`, `2025-05-23-…senate-approps…` | Sen Approps | 03 (fiscal only; no positions) |
| SFLR | `2025-05-27-senate-floor-third-reading-on-05-23-text.md` | Sen floor | 04 (May 23) |
| AJUD | `2025-06-28-assembly-judiciary-cmte-on-05-23-text.md` | Asm Jud, Jul 1 | 04 |
| PCP1 | `2025-07-15b-assembly-pcp-cmte-on-07-08-text.md` (and `…07-15a…`, same line numbers) | Asm P.&C.P., Jul 16 | 05 (Jul 8), plus a mock-up of the committee amendments that became 06 |
| AAPP | `2025-08-18-assembly-approps-cmte-on-07-17-text.md` | Asm Approps, Aug 20 | 06 (Jul 17) |
| AFL1 | `2025-09-03-assembly-floor-on-09-02-text.md` | Asm floor | 07 (Sept 2) |
| AFL2 | `2025-09-08-assembly-floor-on-09-05-text.md` | Asm floor | 08 (Sept 5) |
| PCP2 | `2025-09-10-assembly-pcp-cmte-rule-77.2-on-09-05-text.md` | Asm P.&C.P. (Rule 77.2), Sept 11 | 08 |
| AFL3 | `2025-09-11-assembly-floor-on-09-05-text.md` | Asm floor | 08 |
| SCONC | `2026-07-21-senate-floor-unfinished-business-concurrence.md` | Sen concurrence | 08 (header says "Amended: 9/29/25"; see NOTES caveats) |

`ATF` is `ref/canonical/anthropic-2025-transparency-framework.md` in the main repo (`relata` key `anthropic-2025-transparency-framework`).

## The short version

1. **No opposition was recorded at all until the transparency act entered (Jul 8).** For v02–v04 (CalCompute plus whistleblowers) every analysis records «None received» or «None on file» (SGO 229; SJUD 231; SFLR 174; AJUD 209). The only industry position before July is Chamber of Progress's «Support if amended (to prior version)» (AJUD 203–205).
2. **Industry opposition arrived with v05 and stayed through the final vote.** Chamber of Progress and the Silicon Valley Leadership Group were "oppose". CalChamber, CCIA, Insights Association and TechNet were "oppose unless amended" (PCP1 1078–1088). By Sept 11, BSA, the Consumer Technology Association and BizFed had joined as "oppose" (PCP2 566–579).
3. **One frontier developer appears in the record, and only at the very end.** Anthropic is in no registered list until the Sept 10 analysis (PCP2 514). It is also absent from the Senate's list «Verified 9/9/2025» (SCONC 150–199). Its letter describes provisions that first exist in the Sept 5 text. No other frontier developer (OpenAI, Google, Meta, Microsoft, xAI) appears in any list in any analysis, for or against. Small AI firms do appear among supporters (Elicit, Depict.ai, Eon Systems, e.g. SFLR 156–159).
4. **Staff tie one threshold to Anthropic by name.** The first revenue test ($100M, Jul 17) is «a threshold recently referenced by Anthropic in its description of their transparency framework» (PCP1 483), citing Anthropic's Jul 7, 2025 post (PCP1 1182). Appropriations raised it to $500M on Sept 2. That the post itself says "$100 million" rests on a quote that came through the fetch tool's summarizer, with no saved copy, so it needs checking against the post before anyone cites it (§5.1).
5. **Staff state in their own voice that the Sept 5 package answered the opposition:** «To address opposition concerns, the bill has since been narrowed in several significant ways» (PCP2 25). Many items in that package line up one-to-one with asks in the CalChamber coalition's July letter. That correspondence is my inference; see §5.
6. **The quoted arguments often answer older text than the analysis they appear in.** The Chamber of Progress letter attacks a «$100,000,000 compute cost threshold» that left the bill on Jul 8. It is quoted unchanged in every floor analysis through the Senate concurrence analysis. The sponsors' July letter, which describes AG rulemaking that was struck on Sept 5, is likewise quoted unchanged through SCONC. See §6.

## 1. Positions by stage

**Text shows** (counts are entries in each analysis's registered list, before deduplicating spelling variants):

| Analysis | Version | Support (entries) | Opposition as listed | Arguments quoted |
|---|---|---|---|---|
| SGO | 02 | 13, incl. 3 co-sources (SGO 208–225) | «None received» (229) | Co-sources (231–233) |
| SJUD | 03 | 16 (195–227) | «None received» (231) | Author; co-sponsor coalition (175–193) |
| SFLR | 04 | 27 (142–170) | «None received» (174) | Co-sources and coalition (176) |
| AJUD | 04 | 32 (137–201); Chamber of Progress «Support if amended (to prior version)» (203–205) | «None on file» (209) | Co-sponsors' coalition letter (123–133) |
| PCP1 | 05 | 40 (1035–1076) | Oppose: Chamber of Progress, SVLG. Oppose unless amended: CalChamber, CCIA, Insights Association, TechNet (1078–1088) | Secure AI Project and coalition (905–925); Chamber of Progress (927–955); CalChamber coalition (957–1031) |
| AAPP | 06 | not listed | «opposed by business and industry representatives, including the California Chamber of Commerce, Chamber of Progress, and TechNet» (79) | none |
| AFL1 | 07 | not listed | not listed | Secure AI Project coalition (71–91); Chamber of Progress (95–123) |
| AFL2 | 08 | not listed | not listed | same two letters, unchanged (71–123) |
| PCP2 | 08 | 56, incl. Anthropic PBC (507–564) | Oppose: BSA [sic, "Business Software Association"], Chamber of Progress, CTA, BizFed «(UNREG)», SVLG. Oppose unless amended: CalChamber, CCIA, Insights, TechNet (566–579) | Anthropic (445–465); CalChamber, CCIA and TechNet jointly (467–503) |
| AFL3 | 08 | not listed | not listed | Anthropic (89–109); CalChamber, CCIA and TechNet (113–149) |
| SCONC | 08 | 48, «Verified 9/9/2025», no Anthropic (150–199) | 8 names «Verified 9/9/25», no oppose-unless-amended tier, no Chamber of Progress (201–217) | Secure AI Project coalition (219–237); Chamber of Progress (239–267) |

**Arrivals worth noting** (Text shows; spelling variants merged by me):
- **Labour.** District Council of Iron Workers from AJUD (163); SEIU California from PCP1 (1069); California Federation of Labor Unions, AFL-CIO from PCP2 (518) and SCONC (164). No labour argument is quoted in any analysis.
- **Children's, parents' and youth groups** join in PCP2: Mothers Against Media Addiction, Parents Television and Media Council, ParentsTogether Action, Rights4girls, Young People's Alliance, Youth Power Project, Design It for US, InnovateEDU (PCP2 527–564). Common Sense Media is there from PCP1 (1050). Most are missing from SCONC.
- **Public bodies and institutions.** University of California from SFLR (169). Little Hoover Commission in SFLR (161), AJUD (177) and SCONC (181), but not in either P.&C.P. list. Center for Human-Compatible AI (UC Berkeley) from SGO (219).
- **Political and philanthropic.** California Democratic Party and Omidyar Network appear only in SCONC (163, 185). Future of Life Institute from PCP2 (538) and SCONC (179).
- **The AI-safety cluster is present from the first list.** Redwood Research, Apart Research, Nonlinear, CHAI, Center for AI and Digital Policy, and later BERI, AI Futures Project, AI Lab Watch, The Midas Project, ALTER and Existential Risk Observatory.
- **One-off entries.** Compute Exchange (SGO 221 only); Porn Free Colorado (SJUD 223 only).

**How staff characterised the coalitions** (Text shows):
- «a coalition of advocates for safe and responsible AI development» (AJUD 27).
- «a broad coalition of technology advocacy groups, including TechEquity Action, Secure AI Future, and Common Sense Media» (PCP1 39).
- «supported by groups that favor greater regulation of the AI industry. The bill is opposed by business and industry representatives» (AAPP 79).
- «supported by a large coalition of civil society, labor, AI safety groups, and Anthropic, a frontier model developer» (PCP2 55).
- And a caveat, in the same paragraph: «some advocates may not have had time to update their positions in light of recent amendments, which went into print late last week» (PCP2 55).

## 2. Supporters' arguments

### 2.1 Sponsors

The sponsors are the same three organisations throughout: Secure AI Project, Economic Security California Action and Encode. «Encode» (SJUD 33; SFLR 50–52; SCONC 62) is «Encode Justice» in the Assembly synopses (PCP1 39; AAPP 79; PCP2 55). The Assembly lists carry «Encode», «Encode Ai Corporation» and «Encode Justice» as three entries (PCP1 1056–1058; PCP2 532–534).

**Whistleblower and CalCompute stage (v02–v04).** The co-sources wrote:

- «AI researchers and engineers will likely be the first to know if a company’s product poses a significant risk to public safety, but company contracts may prevent them from reporting concerns.» (SGO 231)
- «Many companies already have internal processes, such as OpenAI, Anthropic, xAI, and Microsoft, so this requirement would codify what is an emerging industry norm.» (SJUD 191)
- «as a nearly unregulated industry, dangerous behavior at AI companies might not today be illegal and disclosure is not protected in the same manner. SB 53 addresses this imbalance by expanding essentially the same protections from retaliation already found for reporting violations of the law to material risks of serious catastrophic harm, as well as false statements about company safety practices.» (SJUD 193)
- «large AI developers themselves warn that their AI systems could pose serious risks, which they have voluntarily committed to addressing.» They cite the International Scientific Report: «‘…evidence of additional risks is gradually emerging. These include risks such as large-scale labor market impacts, AI-enabled hacking or biological attacks,’» (SFLR 176)
- On CalCompute: «supporting in particular smaller startups for a healthier innovation ecosystem. We support this groundbreaking effort, which would advance and democratize AI research in California.» (SGO 233)

**Transparency-act stage (v05 onward).** Secure AI Project wrote «alongside a coation of technology equity advocacy groups» [sic] (PCP1 905). This letter is reproduced verbatim at AFL1 71–91, AFL2 71–91 and SCONC 219–237.

- On the Report as the basis: «The California Report on Frontier AI Policy, while it does not endorse any specific legislation, forms the foundation for SB 53.» (PCP1 907)
- On the risks: «The Report stated that “some risks have unclear but growing evidence...AI-enabled hacking or biological attacks, and loss of control” – the risks that SB 53 aims to address and gather more evidence about.» (PCP1 909)
- On low burden: «It would impose no burden on smaller companies and the requirements it imposes on large companies are minimal compared to what companies are already voluntarily doing.» (PCP1 919)
- On mirroring existing frameworks: «This is in line with voluntary commitments that companies have already made. […] Others mirror components of the Stanford Foundation Model Transparency Index, which is cited prominently in the Report.» (PCP1 911)
- On scope: «Regardless of any update, the Attorney General must only include “well-resourced large developers at the frontier of artificial intelligence development” in the scoping of the bill.» (PCP1 919)
- Its summary: «a low-burden transparency and reporting regime with a public compute cluster» (PCP1 923).

### 2.2 The author

The author is also a party with a position. In the Senate the framing is whistleblowers and CalCompute against federal retreat: «California’s leadership on AI is more critical than ever as the new federal Administration proceeds with shredding the guardrails meant to keep Americans safe» (SGO 150). From Jul 8 the framing is the Working Group: «Drawing recommendations from Governor Newsom’s working group report» (PCP1 281). The constant refrain, from Apr 4 on: «demonstrate that safety does not stifle success» (SJUD 185; PCP1 287; PCP2 273).

**Text shows (staleness):** the author's statement quoted in SCONC (110–116) still says the bill «authorizes the Attorney General to adjust the scoping of the bill» (SCONC 114) and has incidents reported «to the Attorney General» (SCONC 112). The Sept 5 text, on which the Senate concurred, had moved both to CDT and OES. PCP2 and AFL3 carry an updated author's statement (PCP2 261–273; AFL3 73–85).

### 2.3 Anthropic

Anthropic's letter is quoted in PCP2 445–465 and AFL3 89–109. It is the only support argument quoted in either. The sponsors' letter is not quoted in them.

- On the first time, and federal preference: «As you know, SB 53 would, for the first time, govern powerful AI systems built by frontier AI developers like Anthropic. […] While we believe that frontier AI safety is ideally addressed at the federal level instead of a patchwork of state regulations, powerful AI advancements won’t wait for consensus in Washington.» (PCP2 447)
- On SB 1047's approach: «SB 53 implements this principle through disclosure requirements rather than the prescriptive technical mandates that plagued last year's efforts.» (PCP2 449)
- On what the bill would require: «Report critical safety incidents to the state within 15 days, and even confidentially disclose summaries of any assessments of the potential for catastrophic risk from the use of internally-deployed models.» (PCP2 457) Pandoc printed this five-item list outside the blockquote. In the `.docx` it sits between the letter's indented paragraphs. The next paragraph opens «These requirements would formalize…», which refers back to the list, so I read the list as part of the letter (Inference).
- On existing practice: «These requirements would formalize practices that Anthropic and many other frontier AI companies already follow. […] Other frontier labs (Google DeepMind, OpenAI, Microsoft) have adopted similar approaches while vigorously competing at the frontier. Now all covered models will be legally held to this standard.» (PCP2 463)
- On competitive dynamics: «Without it, labs with increasingly powerful models could face growing incentives to dial back their own safety and disclosure programs in order to compete. But with SB 53, developers can compete while ensuring they remain transparent about AI capabilities that pose risks to public safety, creating a level playing field.» (PCP2 463)
- On small companies: «providing exemptions for smaller companies that are less likely to develop powerful models and should not bear unnecessary regulatory burdens.» (PCP2 463)

**Text shows (dating):** the letter describes features that exist only in version 08 (Sept 5).
- "frontier developer" and "frontier AI framework" occur 0 times in versions 04–07 and 65 and 12 times in 08 (`grep -c`).
- The confidential internal-use summaries are listed as a Sept 5 change at PCP2 53.
- The whistleblower trigger «substantial dangers to public health/safety from catastrophic risk» (PCP2 459) tracks the Sept 5 «specific and substantial danger» (PCP2 239; 0 occurrences in 04–07, 4 in 08).

**Inference:** the letter was written with the Sept 5 text, or a draft of it, in hand. Its support is support for the narrowed bill. Nothing in the record shows Anthropic's position on any earlier version.

## 3. Opponents' arguments

### 3.1 Chamber of Progress ("oppose")

The letter was first quoted at PCP1 927–955. It is reproduced verbatim at AFL1 95–123, AFL2 95–123 and SCONC 239–267.

- On amendments: «we respectfully urge you to oppose SB 53, based on its recent amendments.» (PCP1 929)
- On vagueness: «The definition remains overly expansive and ambiguous, capturing a wide array of hypothetical scenarios that may not reflect real-world AI capabilities or threats.» (PCP1 933)
- On loss of control: «the inclusion of highly abstract risks, such as the evasion of human control under Section 22757.12(a)(2), creates significant uncertainty. […] could push critical AI development efforts out of state or abroad.» (PCP1 937)
- On threshold: «SB 53’s use of an arbitrary $100,000,000 compute cost threshold to determine eligibility for protections is an inherently flawed method for identifying frontier AI models.» (PCP1 941) and «A more effective approach would involve a threshold based on model capabilities, deployment context, and specific use cases rather than relying solely on computational costs.» (PCP1 943)
- On burden: «For startups and smaller companies, these extensive protocols create a heavy administrative burden» (PCP1 949)
- On disclosure: «the requirement to publish the “character and justification” of redacted material could still inadvertently expose business-sensitive strategies or vulnerabilities.» (PCP1 953)

**Text shows (which text it answers):** the letter cites v05 section numbers: §22757.11(b), §22757.12(a)(2), (c) and (f). But:
- the «$100,000,000 compute cost threshold» is the Labor Code "Developer" definition of versions 02–04, «costs at least one hundred million dollars ($100,000,000) when measured using prevailing market prices of cloud compute» (`versions/04…` line 122). Version 05 has no such threshold; it uses 10^26 operations.
- «materially likely» (PCP1 935) occurs in no version, 01–10.
- «eligibility for protections» (PCP1 941) reads like the whistleblower chapter's scoping.

**Inference:** the letter was assembled partly from comments on the pre-July bill. Its threshold paragraph does not describe any version it was quoted against.

### 3.2 CalChamber coalition, July ("oppose unless amended")

The letter is quoted at PCP1 957–1031. Its signatories are given only as «the California Chamber of Commerce in a coalition with other technology trade organizations» (PCP1 957). The registered oppose-unless-amended list is CalChamber, CCIA, Insights Association and TechNet (PCP1 1085–1088). The September letter calls its predecessor «our July 12th letter» (PCP2 501), and the 15-day point it recalls is the one at PCP1 1021. **Inference:** the PCP1 letter is that July 12 letter.

Its asks, verbatim:
- **Model risk, not developer size:** «SB 53 should ideally focus on model risk, not developer size» (PCP1 961); «smaller and/or less performant models can present much greater risks than large/higher performant ones. […] as demonstrated by the Chinese company DeepSeek.» (PCP1 971) It also warns against cost proxies: «a secondary threshold attempted in SB 1047 which we would caution against as a fallback here.» (PCP1 973)
- **AG authority:** «By no means should the AG be given unfettered or unchecked authority to make decisions as to who is and is not subject to this law.» (PCP1 983) And: «an annual review each interim by a legislative oversight committee would provide greater assurance of an adaptive definition» (PCP1 985)
- **Definitions:** «The definition is contradictory, listing both single incident, as well as scheme or course of conduct, vastly expanding the scope of the bill.» It asks to «exclude things such as blackmail, theft by deception, federation operation, publicly available data, nonmaterial contribution, or cyber threats for example.» (PCP1 993) And: «we suggest that an effort be made to unify the terminology» (PCP1 997). It objects to «widely available capabilities from existing software tools, such as the ability to “assist in a cyberattack”» (PCP1 989).
- **Marginal risk:** «we feel it critical that SB 53 better align with the marginal risk standard adopted in the report.» (PCP1 997)
- **Detail and security:** «We have significant concerns about describing many of the required elements in “detail.”» (PCP1 1003) And: «This is almost akin to a bank putting a blueprint of the location of its security cameras […] online.» (PCP1 1005)
- **Downstream incidents:** «reporting obligations regarding downstream developer incidents that are infeasible for a developer who does not control the AI system involved in the incident.» (PCP1 995)
- **Whistleblowers:** «The definition should not be changed to include non-employees like contractors.» (PCP1 1013)
- **Intent standard:** «the prohibition on false and misleading statements needs an intent standard such as “intentionally”, or at least “intentionally or recklessly”.» (PCP1 1019)
- **Incident timeline:** «requirements should be flexible because all facts may not be known within 15 days of discovery.» (PCP1 1021)
- **Upstream and downstream:** «Developers who pretrain models should not be held liable for fine-tuning or modifications by downstream developers.» (PCP1 1023)
- **Transparency report:** «should be eliminated. Instead, the bill should allow developers to rely on existing transparency practices such as model cards» (PCP1 1025)
- **Redactions:** «we hope to see redactions be broadened beyond trade secrets and cybersecurity information» (PCP1 1027)
- **Enforcement:** «we ask that the bill grant businesses at least a 60 day right to cure» and «enforcement efforts should be focused on material failures to comply rather than also covering technical paperwork errors.» (PCP1 1029)
- **A flag on competitors:** a heading reads «Additional considerations, including areas of competing viewpoints in industry: something the Legislature must take seriously to avoid granting competitive advantages» (PCP1 1015). The letter does not name who holds the competing viewpoints.

**Text shows (which text it answers):** its whistleblower paragraph quotes «“involved with assessing, managing, or addressing critical risk”» (PCP1 1011). That wording is exactly version 04's (`versions/04…` line 126). Version 05 reads «catastrophic risk» (`versions/05…` line 306). The rest of the letter addresses v05 («As amended July 8th», PCP1 967).

### 3.3 CalChamber, CCIA and TechNet, September ("oppose unless amended")

The letter is quoted at PCP2 467–503 and AFL3 113–149, and addresses version 08 («As amended September 5th», PCP2 475).

- On recent changes: «we appreciate improvements made to the bill over the last several weeks.» (PCP2 471)
- On the revenue tier: «SB 53 now focuses on models that have a computational threshold of 10^26 floating point operations (or “FLOPs”) but only if those models are developed by entities with at least $500m in annual revenues.» (PCP2 475) **Text shows:** this misdescribes v08, where frontier developers below $500M carry lighter duties (PCP2 105–107, 145–159). The staff synopsis says so: «developers who only reach the compute threshold must publish a high-level transparency report» (PCP2 21).
- On detail: «We appreciate that amendments were made to change the level of detail required of the AI Safety Framework and changing summaries for transparency reports.» (PCP2 487)
- On internal-use summaries: «Not only is this cadence of reporting unnecessary, CalOES will need to take serious steps to protect this information» (PCP2 487)
- On whistleblower law: «SB 53 unnecessarily re-writes California Whistleblower law for just one industry» (PCP2 493). Also: «Labor Code Section 6310 already protects whistleblowers who report unsafe working conditions» (PCP2 497)
- On penalties: «SB 53 imposes a $1 million fine for a possible paperwork error which is excessive» (PCP2 501). And: «we again state our view that the bill should grant businesses at least a 60 day right to cure» (PCP2 501)

### 3.4 Opponents with no argument in the record

SVLG, Insights Association, Business Software Alliance, Consumer Technology Association and BizFed appear only in lists. **Text shows:** the record gives no membership for any trade association. Whether the frontier developers absent from the lists belong to these associations is not answerable from these files.

## 4. Committee staff as an actor

The committees shaped the text as well as reporting on it.

- **Assembly Judiciary (v04)** questioned the casualty bar: «It is not entirely clear why the AI developer’s activity, in order to be the subject of a protected disclosure, must result in the death or serious injury of “more than 100” people, as opposed to 50 or even one.» (AJUD 91) It offered two possible amendments (AJUD 95–121). It also records what the author's side said: «The author’s office and sponsors have informed the Committee that their primary aim, at this point, is to protect disclosures of potentially catastrophic events.» (AJUD 93)
- **Assembly P.&C.P. (Jul 16)** printed its own committee amendments, which «The author has agreed to» (PCP1 461). They were:
  - capability thresholds;
  - the $100M revenue test;
  - disclosure of shutdown capability;
  - 24-hour reporting to law enforcement;
  - AG aggregate reports;
  - third-party audits from 2030;
  - tiered penalties with a 30-day cure for the lowest tier (PCP1 41, 463–531).

  The mock-up shows the casualty bar moving «~~100~~ *50*» and "theft by deception" struck in favour of "theft by false pretense" (PCP1 577, 597). Staff argued for audits in their own voice: «Just as a teacher would not allow students to grade their own exams and expect complete honesty, the public should not expect every large developers to fully self-assess without independent oversight.» (PCP1 511)
- **Assembly P.&C.P. (Sept 11)** records the reversals plainly:
  - «This provision, which aligned with the Working Group’s emphasis on independent evaluation frontier model safety protocols, was removed in recent amendments.» (PCP2 439)
  - «Notably this is a much more lenient enforcement mechanism and penalty than those instituted in SB 1047.» (PCP2 439)
  - «as a result, third parties, such as red-teamers or auditors, are not protected by the whistleblower protections.» (PCP2 437)

## 5. Where a stakeholder's proposal shaped the text

### 5.1 As the analyses state it (Text shows)

| What changed | Attributed to | Where |
|---|---|---|
| Revenue test of $100M added (v06) | Anthropic: «a threshold recently referenced by Anthropic in its description of their transparency framework» | PCP1 483, fn 45 at PCP1 1182 («“The need for transparency in Frontier Ai”, *Anthropic* (July 7, 2025)») |
| The Sept 5 package of narrowing amendments (13 items) | «To address opposition concerns» | PCP2 25–53; the same list at AFL3 33–59 |
| The bill overall | «recommendations of the working group, modified elements of SB 1047, and input from other stakeholders» | AAPP 79 |
| The bill overall, and the Jul 16 committee amendments | The Working Group Report: «This bill seeks to implement the recommendations of the Working Group Report» | PCP1 35, 41; PCP2 21, 337 |
| CalCompute | The Little Hoover Commission's first recommendation: «The first section of ***this bill*** does precisely what the Little Hoover Commission report called for» | AJUD 71–73 |
| Internal anonymous reporting | Sponsors' claim that it codifies practice at «OpenAI, Anthropic, xAI, and Microsoft» | SJUD 191 |
| Capability-threshold amendments (v06) | Developers' own system cards, quoted through the Working Group Report: Google's Gemini 2.5 Pro Model Card and OpenAI's o3/o4-mini System Card | PCP1 463–475 |

**Checked outside the analyses:** Anthropic's Jul 7, 2025 post does name the figure. I fetched `anthropic.com/news/the-need-for-transparency-in-frontier-ai` on 2026-10-09. The fetch tool's summary quotes «annual revenue cutoff amounts on the order of $100 million» and «R&D or capital expenditures on the order of $1 billion annually», with the date «Jul 7, 2025». I saw these through the tool's summarizer, not a saved copy, and the post is not in relata. The wording needs checking against the post itself before anyone cites it. The companion document in the corpus (ATF) names an «annual revenue or aggregate R&D expenditure threshold» with no figure (ATF 17). The bill took the revenue half only, and raised it to $500M on Sept 2.

### 5.2 My reading: asks that line up with later text (Inference)

These are correspondences between the asks in §3 and the version history. The analyses do not attribute any single item to any single letter. PCP2 25 attributes the package as a whole to «opposition concerns». A match does not show cause: the Working Group Report, the author and staff could each be the source.

| Ask | Version history | Direction |
|---|---|---|
| Drop «scheme or course of conduct» (CalChamber, PCP1 993) | "scheme, or course of conduct" in 05–07; "single incident" only in 08 | adopted |
| Exclude «publicly available data, nonmaterial contribution», «federation operation» [sic] (PCP1 993) | v08 adds exclusions for publicly accessible information, lawful federal-government activity, and harm in combination with other software without material contribution (PCP2 73–79) | adopted |
| «theft by deception» out (PCP1 993) | became «theft by false pretense» on Jul 17 (PCP1 597) | changed |
| «“assist in a cyberattack”» too broad (PCP1 989) | "assist in a cyberattack" in 05–07, gone in 08; cyberattack now needs «no meaningful human oversight» (PCP2 69) | adopted |
| «unify the terminology» (PCP1 997) | «collapsing of the definition of “dangerous capabilities” into the definition of “catastrophic risk.”» (PCP2 35) | adopted |
| No unchecked AG scoping power (PCP1 983–985) | AG rulemaking struck; CDT recommends to the Legislature (PCP2 33) | adopted |
| Less «detail» (PCP1 1003) | "in specific detail" in 05–07, absent in 08; the opponents acknowledge it (PCP2 487) | adopted |
| Rely on model cards (PCP1 1025) | a system or model card is «deemed in compliance» (PCP2 161) | adopted |
| No contractors (PCP1 1013) | «Removal of contractors from whistleblower protections» (PCP2 49) | adopted |
| Intent standard for false statements (PCP1 1019) | no "intentionally" in any version; v08 excepts statements «made in good faith and was reasonable under the circumstances» (PCP2 167) | partly |
| Flexible incident timeline (PCP1 1021) | v08 allows an amended report (PCP2 185); the opponents still object (PCP2 501) | partly |
| Penalties for material failures only (PCP1 1029) | cap cut from $10M to $1M, «dependent upon the severity» (PCP2 47, 439); still objected to (PCP2 501) | partly |
| 60-day right to cure (PCP1 1029) | a 30-day cure existed only in 06–07 (`versions/06…` line 274) and was struck on Sept 5; the Sept letter complains of «no right to cure» (PCP2 499) | **opposite** |
| Model risk, not developer size (PCP1 961) | developer revenue test added (06), raised to $500M (07), made a tier (08) | **opposite** |
| Broader redaction grounds (PCP1 1027) | grounds unchanged (PCP2 165); asked again (PCP2 491) | not adopted |
| Downstream and upstream split (PCP1 995, 1023) | asked again in September (PCP2 483) | not adopted, per the opponents |
| 100-person bar questioned (Asm Jud staff, AJUD 91) | became 50 on Jul 17 (PCP1 577) | changed, in the direction the question pointed |

The Sept 5 changes that most constrain disclosure have no counterpart in the sponsors' letters, and the sponsors' July letter is never updated in the record. Those changes are: internal-use assessments made confidential, audits dropped, the penalty cut, and contractors removed. **Inference:** the record gives no visible sign of the sponsors' view of the Sept 5 package.

### 5.3 My reading: parallels with Anthropic's proposed framework (Inference)

This is weaker than §5.1, and the analyses attribute none of it. ATF and the bill share structure:
- an annual-revenue scope test with a start-up exemption (ATF 16–17);
- a published framework the company must «develop and follow» (ATF 21);
- system-card documentation at deployment (ATF 38);
- redactions «briefly identified and justified» (ATF 43);
- AG civil penalties (ATF 48);
- a «30-day right to cure» (ATF 49).

In SB 53 the redaction-justification clause is already in v05 (PCP1 129). The 30-day cure appears in v06, as a committee amendment (PCP1 529), and leaves in v08. System cards enter in v08.

Most of these features also appear in the Working Group Report of June 17, which predates both. ATF has no date in the canonical text, and the blog post is dated Jul 7, one day before v05. Shared structure therefore cannot show direction of influence, or whether there was any. Where the two diverge, the bill is broader than Anthropic's proposal in its harm categories: ATF's «Catastrophic Risks» are CBRN and autonomous action (ATF 22), while the bill adds cyberattacks and enumerated crimes. On intent, ATF prohibits «intentionally false or materially misleading statements» (ATF 47), and the bill never adopted an intent standard.

## 6. Independence and conflict of interest

**Anthropic (the repo's own conflict-of-interest rule applies here)**

1. **It appears in the record in four roles at once:** a supporter (PCP2 514; letter at PCP2 445–465); the cited origin of a threshold (PCP1 483); a source of the evidence of risk staff present; and, outside this record, a regulated party. The catalog lists Anthropic's Frontier Compliance Framework as a «designated SB 53 frontier AI framework» (main repo `source-catalog.md`, line 64).
2. **Evidence from Anthropic.** Staff's loss-of-control section rests partly on Anthropic material:
   - the Claude 4 system card: «the model blackmailed the engineer» (PCP1 327, fn 31 at PCP1 1154);
   - an anecdote about Dario Amodei and a boat-racing agent (PCP1 325);
   - Amodei's AGI-timeline claim (PCP1 301).

   **Text shows:** by Sept 10 the system-card sentence reads «the model indicated an intent to blackmail the engineer» (PCP2 313). The analyses give no reason for the change.
3. **Its own words state a competitive interest.** It says the bill would «formalize practices that Anthropic and many other frontier AI companies already follow» and create «a level playing field» (PCP2 463). **Inference:** a company that already bears the cost of a practice gains from a rule that makes competitors bear it too. That does not make the argument wrong, but it does make Anthropic's support non-independent of its commercial position, and Anthropic says so itself.
4. **Timing.** Its support is visible only against v08 (§2.3). The Senate list verified on 9/9 omits it (SCONC 150–199). **Inference:** the Senate list was not updated, or Anthropic's letter reached the Assembly committee only. The files cannot say which.
5. **No other developer is in the record.** The only other developers named are in arguments: by the sponsors (SJUD 191), by Anthropic (PCP2 463) and by staff (system cards, PCP1 463–469). The September opposition letter speaks for CCIA and TechNet. **Text shows:** their members are not identified in the record.

**One shared document, cited by both sides.** The sponsors call the Working Group Report «the foundation for SB 53» (PCP1 907). Staff say the bill «seeks to implement» it (PCP1 35). The opponents argue the bill «diverges from the final findings» (PCP1 959) and quote it against developer-level thresholds (PCP2 479) and against detailed disclosure (PCP1 1007; PCP2 489).

**Inference:** agreement between the sponsors' and the staff's accounts of what the Report recommends is not independent corroboration. The staff synopses and the sponsors' letter quote the same Report passages, often the same sentences:
- the «trust but verify» framing (PCP1 907) and the «trust but verify» model in staff's audit discussion (PCP1 497);
- the transparency passage (PCP1 389, 911);
- the adverse-event passage (PCP1 423, 915);
- the whistleblower passage (PCP1 449, 917).

**Interests among supporters that the record makes visible (Text shows, with my inference marked)**
- **University of California** supports the bill (SFLR 169; PCP2 562; SCONC 198). The bill directs the consortium to make «reasonable efforts to ensure that CalCompute is established within the University of California» and lets UC «receive private donations» for it (SGO 72, 116). One of the Working Group's three leads is «Dean of the UC Berkeley College of Computing, Data Science, and Society» (PCP1 351). **Inference:** UC has a direct institutional interest in CalCompute. The Report's authorship and UC's support are not independent of each other.
- **Little Hoover Commission**, a state body, supports the bill. Assembly Judiciary presents CalCompute as implementing that Commission's own recommendation (AJUD 69–73).
- **Labour support follows the bill's workforce provisions rather than preceding them.** The consortium's «Representatives of impacted workforce labor organizations» and its duty to «prioritize the use of the current public sector workforce» are in the Feb 27 text (`versions/02…` lines 72, 78; SGO 100, 106). The first labour supporter appears on Jun 28 (AJUD 163). **Inference only:** the record gives no labour argument, so no motive can be read from it.
- **AI Futures Project** is a registered supporter (SFLR 148). Staff cite its *AI 2027* as support for short AGI timelines (PCP1 1108, fn 9). **Inference:** a supporter's own publication is cited as background evidence in a staff analysis.
- **Funding and shared authorship are not in the record.** The record says nothing about who funds the sponsors or the AI-safety supporters, or whether they share funders, staff or authors. Staff describe them only as «AI safety groups» (PCP2 55) and «groups that favor greater regulation of the AI industry» (AAPP 79). Omidyar Network, a funder, appears as a supporter (SCONC 185). Any claim about common funding would have to come from elsewhere, and I have not made one.
- **Counting.** «Encode», «Encode Ai Corporation» and «Encode Justice» are three entries for what the synopses treat as one sponsor (§2.1). «Secure AI Future» (AJUD 189; PCP1 1067), «Safe AI Future» (SGO 225; SCONC 187) and «Secure AI Project» may or may not be distinct organisations. A count of supporters overstates the number of independent voices by at least the Encode duplication.

**Copying inside the record.** Most analyses after July reuse earlier text, as follows.
- **The sponsors' letter** is the same text at PCP1 905–925, AFL1, AFL2 and SCONC, even though:
  - it describes AG scoping «through regulation» (SCONC 233), which was struck on Sept 5;
  - it describes incident reports going «to the Attorney General» (SCONC 229), which moved to OES on Sept 5.
- **The Chamber of Progress letter** is the same text at PCP1, AFL1, AFL2 and SCONC, with the stale threshold (§3.1).
- **The AFL1 summary** says the bill «Requires operators of computing clusters to obtain specified information relating to customers» (AFL1 13). That is an SB 1047 duty, not in any SB 53 version. Its whistleblower summary still uses v04's «critical risk» (AFL1 27–31), and AFL2 and AFL3 carry the same summary (AFL2 27–31; AFL3 27–31).

**Inference:** in the floor analyses and the Senate's, "arguments in support/opposition" are not responses to the text being voted on, and should not be read as such.

## 7. Oddities in the record

- **PCP1a vs PCP1b.** The two Jul 15 files differ in two lines only. Line 3 is «Fiscal:» against «Fiscal: Yes». Line 35 has «more than 100 deaths or $100 billion in damage» in 07-15a and «$1 billion» in 07-15b. The v05 text then in print had 100 people or $1 billion, so 07-15b is correct and 07-15a's figure is a typo.
- **Committee vote.** `actions.md` records the Jul 16 P.&C.P. vote as «Ayes 9. Noes 0.» Every analysis that reports it says 10–0: AAPP 14; AFL1 151 («10-0-5»); PCP2 25. I have not resolved this. `BILL_DETAIL_VOTE_TBL` would settle it.
- **CalChamber's position.** It is "oppose unless amended" in PCP1 and PCP2, plain "opposed" in AAPP 79, and plain «OPPOSITION» in SCONC 201–217, which drops the distinction for all four.
- **Chamber of Progress** is missing from the SCONC opposition list (201–217), yet its letter is SCONC's only quoted opposition argument (239–267).
- **Footnotes.** The September letter's footnote to the Report is blank: «Final Report at p.» (PCP2 667; AFL3 209).
- **«Business Software Association»** (PCP2 568) is «Business Software Alliance» in SCONC 203.

## 8. What these files cannot tell you

- The full letters. The analyses excerpt them, sometimes with «[. . .]» (PCP2 469, 503), and give no dates except through the «July 12th» back-reference.
- Positions taken outside the committee process, such as the Governor's office, press statements, other developers' public views, and anything sent only to members.
- Hearing testimony. SEC. 1 finding (o) in the chaptered text cites «testimony from legislative hearings» (NOTES Q6), and none of it is in these files.
- Who drafted the Sept 5 amendments, or what was negotiated. PCP2 25 attributes them to «opposition concerns». The texts cannot say which opponent, or whether the Governor's office or Anthropic was involved.
- Member-level votes beyond those the floor analyses print (AFL1 139–163; AFL3 195–201; SCONC 269–275).
