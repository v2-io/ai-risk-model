# Verification of NOTES.md against the primary texts

*Written 2026-10-09 by an independent verifier (Opus 5.5), at the request of the `california-2025-sb53` source expert. I did not write NOTES.md or any other file in this directory, and I have not edited them.*

## How I checked

- **My own extraction, not the history agent's.** I wrote a separate ~30-line extractor (reproduced at the end of this file) that reads `raw/*.xml` directly and produces, for each version, (i) the text as amended, (ii) the prior text reconstructed from the marks, and (iii) a marked text with `{+…+}` and `[-…-]`. Every verdict below rests on that extraction of `raw/`, not on `versions/`, `diffs/` or `sections/`. Where I quote line numbers in `analyses/`, they are lines of the pandoc markdown. I spot-checked the quotes NOTES relies on against the original `.docx` files, and all of them were there.
- **Two primaries NOTES did not use.** To check the vote counts, which are not in `raw/`, I fetched `BILL_HISTORY_TBL.dat` and `BILL_SUMMARY_VOTE_TBL.dat` from the same `pubinfo_2025.zip`, using the history agent's `tools/fetch_pubinfo.py` as a range-request client. I stored them outside the repo, in `/tmp/sb53v/pub/`, which will not persist.
- **The outside texts.** I checked the New York RAISE text at `/Users/josephwecker-v2/src/ai-risk-model/ref/canonical/ny-2026-raise-s8828.md`, and SB 53's canonical text in the same directory.

**Verdicts:** **confirmed**; **partly right** (the core holds, with a stated correction); **wrong**; **couldn't check**. "Inference" marks a claim that NOTES states as fact but that the texts do not establish.

## What a citer most needs to know

Nothing NOTES says about *when a clause entered or changed* turned out to be wrong. Every date-of-entry claim I tested against the raw XML held. The corrections are these:

1. **The Asm P.&C.P. vote of July 16 was 10–0, not 9–0.** The Legislature's own history text says "(Ayes 9. Noes 0.)", and NOTES and `actions.md` copy it faithfully. But `BILL_SUMMARY_VOTE_TBL` records location `CX32`, 2025-07-16, **10 ayes, 0 noes, 5 not voting**. The Sept 10 analysis says "previously passed this Committee on a 10-0 vote", and the Sept 11 floor analysis says "10-0-5". The likely cause is a member adding on after the roll call, but that is my inference. If you cite it, cite 10–0 and name the vote table, or give both figures.
2. **Q1: "the CSI definition, for one" is true only of the Labor Code.** In the chaptered B&P chapter, "property" appears in only two operative places: the "catastrophic risk" definition (§22757.11(c)(1)) and the "Property" definition itself ((l)). The B&P critical-safety-incident definition says "death or bodily injury" and never mentions property. The Labor Code CSI (§1107(c)(1)) does mention property.
3. **"Nearly three times as many change marks" is true of marks, not of volume.** Measured in words, Sept 5 inserted about as much as Jul 8 (2,909 words against 2,941) but struck far more (1,952 against 397). Its total of changed words is about 1.5 times Jul 8's. The claim that most of the narrowing arrived on Sept 5 is supported by the *content* of the marks, not by their count.
4. **Q2: the "full set of differences" omits one comma.** B&P reads "exfiltration of, the model weights" and the Labor Code reads "exfiltration of the model weights". The agent's own diff file shows this, but NOTES' summary dropped it. It is trivial in meaning, but it bears on the copy question (see *Missed*).
5. **Q6: the Report date is now attested.** NOTES gives June 17, 2025 for the final Report from memory, as unchecked. Footnote 1 of the Sept 10 P.&C.P. analysis cites "'California Report on Frontier AI Policy' (June 17, 2025)" (checked in the `.docx` footnotes too). The March 18 draft date is still unchecked.
6. **The RAISE path.** `ref/canonical/ny-2026-raise-s8828.md` is git-ignored. It exists in the main checkout, not in this worktree. Line 204 there is as NOTES says.

## Verdicts, claim by claim

### Method and provenance

| Claim | Verdict | What I looked at / deciding text |
|---|---|---|
| Each version's LC marks are relative to the immediately preceding version (check 1); dropping insertions and restoring deletions in N gives N−1 | **Confirmed** | My extractor, all 9 transitions: zero differing words apart from the XML metadata header (`caml:Id`, version number, action history) |
| 09 and 10 are word-for-word identical to 08, including the Digest; text final on 2025-09-05 | **Confirmed** | 08 vs 09 and 08 vs 10: only the metadata header differs. `raw/09` and `raw/10` contain no change marks |
| The chaptered rendering matches `ref/canonical/california-2025-sb53.md` apart from formatting (check 2) | **Confirmed** | My extraction against the canonical text, after normalizing quotes and `\$`: the only differences were the canonical's header and vote-key block and spacing at heading boundaries ("22757.12.(a)" against "22757.12. (a)") |
| Mark counts per version (13/5, 5/3, 26/19, 79/38, 53/34, 14/16, 224/147) | **Confirmed** | `grep -o` count of `xm-insertion_mark_start` and `xm-deletion_mark` in each `raw/` file |
| Ch. 138, Stats. 2025 | **Confirmed** | `raw/10`: `<caml:ChapterNum>138</caml:ChapterNum>`; BILL_HISTORY_TBL: "Chapter 138, Statutes of 2025." |
| Version 01 is 378 words | **Couldn't check exactly** | My count is 308 to 436, depending on what is included. It doesn't matter |
| The pubinfo data are "the same data leginfo's pages are built from"; the marks are "the italic and strikeout you see on leginfo" | **Inference** (background) | Plausible, and consistent with the round-trip test, but not something these files can show |

### The version table

| Claim | Verdict | Deciding text |
|---|---|---|
| 01: an intent-only spot bill drawing on the Working Group | **Confirmed** | "It is the intent of the Legislature to enact legislation … that may include, but is not limited to, the findings of the Joint California Policy Working Group on AI Frontier Models" |
| 02: author's amendments in Senate Rules; CalCompute and whistleblower only | **Confirmed** | History: "From committee with author's amendments … Re-referred to Com. on RLS."; text has Gov. Code §11547.6.1 plus Lab. Code ch. 5.1 |
| 03: Senate G.O. amendments, 13–0, Mar 25 | **Confirmed** | History; summary vote table `CS48` 13-0-0 |
| 04: Senate Appropriations from suspense, 6–0; passed the Senate 37–0 on May 28 with no transparency act | **Confirmed** | Vote table `CS61` 2025-05-23 6-0-0, `SFLOOR` 2025-05-28 37-0-3. No version exists between 05-23 and 07-08 (`caml:History`). 04 has no B&P chapter |
| 05: author's amendments in Asm P.&C.P.; the B&P chapter and the SEC. 1 findings enter | **Confirmed** | History of 07-08; `raw/05` inserts SEC. 1 findings and "Chapter 25.1 (commencing with Section 22757.10)" |
| 06: P.&C.P. committee amendments, **passed 9–0**, July 16 | **Partly right** | The history text says 9–0; the vote table and two analyses say 10–0–5 (correction 1) |
| 07: Asm Appropriations from suspense, 11–1 | **Confirmed** | Vote table `CX25` 2025-08-29 11-1-3 |
| 08: floor amendments; Rule 77.2 re-referral, 12–1 Sept 11; Assembly 59–7 Sept 12; Senate concurrence 29–8 Sept 13 | **Confirmed** | History; vote table `CX32` 2025-09-11 12-1-2, `AFLOOR` 59-7-14, `SFLOOR` 2025-09-13 29-8-3 |
| Rule 77.2 is a re-referral "for substantial amendments" | **Inference** | The history says only "pursuant to Assembly Rule 77.2". I did not check the Assembly Rules |

### Q1. The equity sections

| Claim | Verdict | Deciding text |
|---|---|---|
| B&P §22757.16 and Lab. §1107.2 were both added Sept 5 with identical wording, and nothing changed after | **Confirmed** | `raw/08` marked: `{+22757.16.The loss of value of equity does not count as damage to or loss of property for the purposes of this chapter.` and the same for `1107.2.` |
| No "equity" in 01–07 | **Confirmed** | 0 occurrences in my extraction of each |
| The Sept 10 analysis lists it among exemptions and files it as a fourth "Excludes from 'catastrophic risk'" item | **Confirmed** | `analyses/2025-09-10…md` l. 39 "Adding various exemptions, including … risks that would result in loss of the value of equity"; l. 81, item 4 under "Excludes from 'catastrophic risk'" |
| It reaches every use of "property" in the chapter, "the CSI definition, for one" | **Partly right** | True of the Labor Code (§1107(c)(1) "damage to, or loss of, property"). In B&P, the CSI definition has no "property" (correction 2) |
| B&P defines "Property" as tangible or intangible from Jul 17 (06); the Labor Code never defines it | **Confirmed** | `raw/06`: `{+(i) "Property" means tangible or intangible property.`; no "Property" definition in any Labor Code chapter text |
| "a sentence copied into both chapters" | **Inference**, and labeled as one | Consistent with the identical wording and the simultaneous insertion |

### Q2. Labor Code §1107 against B&P §22757.11

| Claim | Verdict | Deciding text |
|---|---|---|
| 02–04: only the Labor Code defines a risk, "critical risk", with >100 people / $1B "in damage to rights in money or property", four routes, the Penal Code route requiring "intent, recklessness, or gross negligence"; "Developer" defined by $100M of cloud compute; no CSI | **Confirmed** | 02/03/04 §1107(b), (c); 0 "critical safety incident" and 0 "catastroph" in 02–04; the Gov. Code section defines no risk |
| 05–07: the Labor Code cross-refers "catastrophic risk", "large developer" and "foundation model" to §22757.11 and has no CSI | **Confirmed** | §1107(b), (c), (e): "has the meaning defined in Section 22757.11 of the Business and Professions Code" |
| 08: the Labor Code restates "catastrophic risk" and adds "critical safety incident" in full; "foundation model", "frontier developer" and "large frontier developer" "still cross-refer" | **Partly right** | The restatement is confirmed (§1107(a), (c)). The word "still" fits only "foundation model": "frontier developer" and "large frontier developer" are new terms on Sept 5. Sept 5 also struck the Labor Code's own "Artificial intelligence model" definition, which NOTES does not mention |
| No version had two identical restated texts | **Confirmed** | Follows from the three rows above |
| The four listed differences in the final text | **Confirmed**, but the list is incomplete | My word diff of chaptered B&P (c)–(d) against Lab. (a), (c) finds the four, plus the comma in correction 4 |
| On Sept 5, B&P's loss-of-control CSI dropped property; before Sept 5, B&P's weight-theft CSI had no harm requirement (05–07) | **Confirmed** | 05–07 (c)(1): "…exfiltration of, the model weights of a foundation model." with nothing after; 08 marks: `causing[- death, bodily injury, or damage to, or loss of, property.-]{+ death or bodily injury.+}` |
| "B&P never had the property-loss form of the weight-theft clause" | **Confirmed** as worded | But see *Missed*, item 6: the same harm list did exist in B&P, in a different clause |
| "a separately edited copy taken from a Sept 5 working draft"; "foundation model" is "a deliberate widening" | **Inference**, and labeled as one | Textually, Labor Code "catastrophic risk" covers "a frontier developer's … deployment of a foundation model", so it reaches a frontier developer's models below the compute line. Whether that was deliberate, the texts can't say |

### Q3. "comply with" in §22757.12(a)

| Claim | Verdict | Deciding text |
|---|---|---|
| Entered Jul 17 (06) | **Confirmed** | `raw/06`: `write, implement,{+ comply with,+} and clearly and conspicuously publish` |
| The Digest never includes it (05–10); LC edited that Digest sentence on Sept 5 without adding it | **Confirmed** | Digest in 05–10: "require a large developer to write, implement, and clearly and conspicuously publish". 08 marks: `require a large{+ frontier+}` … `a[- safety and security protocol that describes in specific detail,-]{+ frontier AI framework …+}` with no "comply with" |
| The July 15 mock-up shows §22757.12(a) without it; the floor analyses from Sept 3 on and the concurrence analysis have it | **Confirmed** | 07-15b l. 631 "shall write, implement, and clearly…"; 09-03 l. 17, 09-08 l. 17, 09-10 l. 109, 09-11 l. 17, concurrence l. 90 all include "comply with" |
| Added after the mock-up was finalized; the Digest was never updated | **Inference**, and labeled as one | Nothing in the July 15 analysis's comment on committee amendments (§8) mentions it |
| The Digest's penalty sentence has no "large" restriction | **Confirmed** | 08–10 Digest: "The TFAIA would impose a civil penalty for noncompliance with the TFAIA to be enforced by the Attorney General, as prescribed." |

### Q4. The penalty section

| Claim | Verdict | Deciding text |
|---|---|---|
| The section was numbered §22757.14 (05), §22757.16 (06) and §22757.15 (07 on) | **Confirmed** | Section heads in my extraction |
| 05: "A violation of this chapter shall be subject to a civil penalty … not to exceed ____ dollars", violator unrestricted | **Confirmed** | 05 §22757.14(a) |
| 06: "A large developer who violates…", tiered at $10k (unknowing, no material risk, 30-day cure for a first violation), $100k, and $1M rising to $10M; a $10k auditor penalty | **Confirmed** | 06 §22757.16(a)(1)–(3), (b). NOTES compresses this: the $100k tier covers a knowing violation without material risk *or* an unknowing one with it, and the $1M/$10M tier is for a knowing violation that creates material risk |
| 07: auditor penalty and audits dropped, the rest unchanged | **Confirmed** | 07 §22757.15 has (a) and (b) only; no "auditor" in 07 |
| 08: the "large frontier developer that fails to publish or transmit…" text, ≤$1M "dependent upon the severity" | **Confirmed** | 08 §22757.15(a) |
| In 05–07 every B&P duty fell on a "large developer" (apart from the v06 auditors) | **Confirmed** for regulated persons | The Attorney General also carries duties in 05–07, as a government actor |
| "frontier developer" first exists on Sept 5, with its duties in §22757.12(c), (e)(1)(A) and §22757.13(c) | **Confirmed** | 0 occurrences of "frontier developer" in 01–07. 08: "(c)(1) … a frontier developer shall clearly and conspicuously publish … a transparency report"; "(e)(1)(A) A frontier developer shall not make a materially false or misleading statement…"; §22757.13(c)(1) "a frontier developer shall report any critical safety incident…" |
| The Sept 10 analysis calls it "a much more lenient enforcement mechanism", without remarking on the limit | **Confirmed** | l. 439, which continues "…than those instituted in SB 1047". The comparison is to SB 1047 |
| Chosen or overlooked; the texts can't settle which | **Inference**, and labeled as one | One more fact sharpens it: §22757.13(i)(2)(B) makes a *frontier* developer's failure under a designated federal standard "a violation of this chapter", but §22757.15 reaches only large frontier developers |

### Q5. "the catastrophic risk" in §22757.13(h)(2)

| Claim | Verdict | Deciding text |
|---|---|---|
| §22757.13(h)–(j) all entered Sept 5 with "the catastrophic risk" already in them; no earlier designation clause | **Confirmed** | 08 marks: (h) through (j) sit inside one `{+…+}` block; "guidance document", "substantially equivalent" and "designat" do not occur in 01–07, and neither does the phrase "the catastrophic risk" |
| The Sept 10 analysis paraphrases it without the article | **Confirmed** | l. 421 "intended to assess and mitigate catastrophic risk" |
| RAISE (S8828) §8(b) reads "intended to assess, detect, or mitigate the catastrophic risk", in a near-verbatim copy of the mechanism | **Confirmed** | Main checkout, `ref/canonical/ny-2026-raise-s8828.md` l. 204; subdivisions 8–10 follow SB 53 (h)–(j) nearly word for word |
| "I could not find such a text" (a source with an antecedent) | **Couldn't check** | NOTES does not say what was searched |

### Q6. SEC. 1 findings

| Claim | Verdict | Deciding text |
|---|---|---|
| No findings before Jul 8; in 02–04 SECTION 1 is the Gov. Code section; in 01 it is the intent clause | **Confirmed** | "finds and declares" first occurs in 05; 02/04 "SECTION 1.Section 11547.6.1 is added to the Government Code" |
| The Sept 10 analysis says the Working Group "published its final report in June 2025" | **Confirmed** | Verbatim in `analyses/2025-09-10…md` |
| June 17 (final) and March 18 (draft) | **Partly confirmed** | June 17 is attested by the analysis footnote (correction 5); March 18 remains unchecked |
| Every row of the origin table: (a)–(c), (h), (n) unchanged since Jul 8; (d) "the potential for"; (e) = Jul 8 (f); (f) rewritten; (g) "given current information deficits" struck, "also" added; (i) "Adverse event"→"Incident"; (j) "There is growing evidence that"→"there is concern that … have capabilities that"; (k) "the"→"serious"; (l), (m), (o) new Sept 5; (p) large→frontier, foundation→frontier; Jul 8 (e) struck Sept 5; Jul 8 (m) struck Jul 17 | **Confirmed** | 08 marks for SEC. 1, each as quoted; 06 marks: `[-(m) A computational threshold of 10^26…` struck. One unrecorded detail: (f) also changed "When" to "As" |
| Jul 8 (m) struck "the same amendment that added the $100M revenue test" | **Confirmed** | 06: `{+(ii) The person had annual gross revenues in excess of one hundred million dollars ($100,000,000)` |
| (c) is the only Jul 8 finding that names the Working Group | **Confirmed** | 05 SEC. 1 |
| The struck Jul 8 (e)'s "substance is reworked into the new (l)" | **Inference** (stated as fact in the table) | Reasonable: both concern voluntary commitments or frameworks |
| The Sept 5 changes "run one way", softening the evidential claims | **Inference**, and labeled as one | Fair to the marks: "growing evidence" became "concern", and "information asymmetry" and "information deficits" were both struck |

### Q7. SEC. 5(d) and (f)

| Claim | Verdict | Deciding text |
|---|---|---|
| (d) added Jul 8 with "large developer"; "frontier developer" from Sept 5; otherwise unchanged | **Confirmed** | 05: `{+(d) This act shall not apply to the extent that it strictly conflicts with the terms of a contract between a federal government entity and a large developer.`; 08: `a[- large-]{+ frontier+} developer` |
| Unchanged in the July 15 mock-up (l. 897) | **Confirmed** | 07-15b l. 897 |
| (f), local preemption from January 1, 2025, added Sept 5 | **Confirmed** | 08: `{+(f) This act preempts any rule … adopted … on or after January 1, 2025, specifically related to the regulation of frontier developers with respect to their management of catastrophic risk.` |

### "Whether the questions are framed right": the Sept 5 package

| Claim | Verdict | Deciding text |
|---|---|---|
| "a single incident, scheme, or course of conduct" → "a single incident" | **Confirmed** | 05–07 (b); 08 (c)(1) |
| The July 15 opposition letter called that wording "contradictory" | **Confirmed** | 07-15b l. 993: "The definition is contradictory, listing both single incident, as well as scheme or course of conduct" |
| "dangerous capability" folded into "catastrophic risk" | **Confirmed** | 08 strikes "(d) 'Dangerous capability' means…"; (c)(1)(A)–(C) carry the capabilities |
| All three exclusions are new Sept 5 | **Confirmed** | No "publicly accessible", "lawful activity" or exclusion paragraph in 05–07 |
| Weight-theft and deception CSIs now require harm or "materially increased catastrophic risk"; the CSI for attaining a threshold for the first time (Jul 17 – Sept 2) dropped | **Confirmed** | 06/07 (c)(5) present, absent from 05; 08 marks as quoted under Q2 |
| SSP renamed "frontier AI framework"; incident reporting moved from the AG to OES | **Confirmed** | 08 marks throughout §22757.12–.13 |
| Internal-use assessments: public before, confidential OES summaries after | **Confirmed** | 07 (d) "shall clearly and conspicuously publish on its internet website any assessment of catastrophic risk … resulting from internal use"; 08 "transmit to the Office of Emergency Services a summary of"; §22757.13(b)(1) "confidentially submit" |
| The AG's power to redefine "large developer" replaced by Department of Technology recommendations | **Confirmed** | 08 §22757.14(a): `[- Attorney General may adopt regulations-]{+ Department of Technology shall assess … and shall make recommendations…+}`, now covering three definitions |
| Cap $10M → $1M | **Confirmed** | 06/07 against 08 |
| Whistleblower: broad "employee" (contractors, freelancers, board members) → "covered employee"; "specific and substantial danger to the public health or safety" added | **Confirmed** | 05–07 §1107(d) list; 08 §1107(b) "'Covered employee' means an employee responsible for assessing, managing, or addressing risk of critical safety incidents"; §1107.1 "pose a specific and substantial danger to the public health or safety resulting from a catastrophic risk" |
| Casualties 100→50 and "rights in money or property"→"property" on Jul 17; revenue $100M (Jul 17) → $500M (Sept 2) | **Confirmed** | 05 against 06 (b); 07 marks: `in excess of[- one-]{+ five+} hundred million dollars` |
| The July 15 analysis ties $100M to Anthropic (l. 483) | **Confirmed** | "a threshold recently referenced by Anthropic in its description of their transparency framework" (also in the `.docx`) |
| Third-party audits, annual from 2030, only in 06 | **Confirmed** | 06 §22757.14 "Beginning January 1, 2030, and at least annually thereafter"; 0 "auditor" in 05 and 07 |
| Leftover: 02–03 "Employee" covers those "involved with assessing, managing, or addressing the risk of critical harm from covered models and covered model derivatives"; removed May 23 | **Confirmed** | 02/03 §1107(d)(1)(A); 04 reads "involved with assessing, managing, or addressing critical risk" |
| …and these are SB 1047's terms ("as far as I remember") | **Partly confirmed** | The analyses' own summaries of SB 1047 use "critical harms" (Senate G.O. and Judiciary analyses) and "covered model" (July 15). "Covered model derivatives" is not attested on disk |
| The chaptered subject line is "Artificial intelligence models: large developers.", but "large developer" is absent from the text since Sept 5 | **Confirmed** | `raw/10` `<caml:Subject>`; 0 occurrences of "large developer" in the chaptered Digest or bill text |
| The Senate never voted on the TFAIA in committee or on its own floor; its only vote on it was concurrence, 29–8 | **Confirmed** | Every Senate committee and floor vote is dated 2025-05-28 or earlier (vote table), before the TFAIA entered on Jul 8 |
| The Sept 10 analysis lists Anthropic as a supporter and quotes its letter | **Confirmed** | l. 55 and l. 445–463 |

### Caveats section

| Claim | Verdict | Deciding text |
|---|---|---|
| The concurrence analysis is dated 2026-07-21 and says "Amended: 9/29/25" | **Confirmed** | l. 22. "May be a later re-post" is labeled as inference |
| The two July 15 analyses differ on $100 billion against $1 billion | **Confirmed** | `diff` of the two: that sentence, and "Fiscal:" against "Fiscal: Yes"; both checked in the `.docx` |
| The bulk data has only veto messages, no signing statements | **Partly confirmed** | The zip listing has `VETO_MESSAGE_TBL`; I did not check for the absence of anything else |

## Missed by NOTES

These matter for the expert's questions, and I found them in the primaries while checking:

1. **A stale cross-reference in the Sept 2 text, of the kind Q5 looks for.** The 07 "large developer" definition says "'large developer' has the meaning defined by a regulation adopted by the Attorney General pursuant to Section 22757.15". In 07, §22757.15 is the *penalty* section. The AG's regulation power is §22757.14, renumbered on Sept 2 when the audit section was dropped. The reference was correct in 05 and 06 (§22757.15 was the AG section then) and disappeared on Sept 5 with the whole definition. It never reached the statute, but it is direct evidence of renumbering without updating references, and so it bears on how much weight a slip like Q5's can carry.
2. **The autonomous-conduct route narrowed on Sept 5.** 07 "dangerous capability" (2) "Conduct or assist in a cyberattack" and (3) "Engage in conduct, with limited human intervention, that would … constitute the crime of…" became, in 08 (c)(1)(B), "Engaging in conduct with **no meaningful human oversight, intervention, or supervision** that is either a cyberattack or…". "Assist" is gone, and a cyberattack now counts only under the no-oversight condition.
3. **A good-faith exemption to the false-statement bar** (§22757.12(e)(2), Sept 5): "This subdivision does not apply to a statement that was made in good faith and was reasonable under the circumstances." The Sept 10 analysis lists it among the narrowings; NOTES' package list doesn't.
4. **Revenue aggregation with affiliates** (Sept 5): the new "(a) 'Affiliate'" definition, and "(j) 'Large frontier developer' means a frontier developer that together with its affiliates collectively had annual gross revenues in excess of five hundred million dollars". Before, it was "The person had annual gross revenues…".
5. **The compute threshold moved from the developer to the model** (Sept 5): the new "(i) 'Frontier model'" carries the 10^26 test, which before sat inside the "large developer" definition, and "frontier developer" is defined by having trained a frontier model.
6. **Evidence on the Q2 copy question.** The Labor Code's weight-theft harm list, "death, bodily injury, or damage to, or loss of, property", is word for word the harm list of B&P's *loss-of-control* CSI in 06–07. The Labor Code copy also lacks B&P's comma after "exfiltration of". Both fit NOTES' "separately edited copy" reading. The first also suggests where the property clause came from.
7. **SEC. 6** (the public-access findings that a Public Records Act exemption needs) first appears Jul 17 (06). It is absent from 05.

## On method, and on the brief

- **What made NOTES checkable.** The round-trip test on Legislative Counsel's own marks was the right foundation, and I reproduced it with independent code. Because of it, every "entered on date X" claim reduces to locating one mark, and none failed. NOTES' separation of **Text shows** from **Inference** was mostly honest. The slips were small: "still cross-refer", "the CSI definition, for one", and a table cell that states "its substance is reworked into" as fact.
- **The two misses of method.** First, vote counts were taken from the history's prose when the same zip has vote tables. The one disagreement turned up only because the analyses were cross-read. Second, mark counts were used as a measure of an amendment's size. Neither error changes a date.
- **Where my check is thin.** I did not audit `sections/`, `versions/` or the per-version `diffs/`, except where NOTES' pointers ran through them (all three line pointers I followed resolved). I relied on pandoc's conversion of the analyses, and spot-checked it against the `.docx` only for the quotes NOTES uses. A fork citing other passages from the analyses would want the same spot-check.
- **On the framing.** Asking for verdicts against `raw/`, and warning that the derived files share the author's possible errors, was the right instruction. It is why I wrote a separate extractor instead of reading `versions/`. The one thing I would add for next time is a note that the vote counts live in tables outside `raw/`, so a verifier knows they need a primary of their own.

## The extractor (for reproduction)

Run with `python3 -I x.py raw OUTDIR`. It writes `NN….cur.txt` (as amended), `….prev.txt` (reconstructed prior text) and `….mk.txt` (marked text).

```python
import re, sys, html, os
src, out = sys.argv[1], sys.argv[2]
ins = re.compile(r'<\?xm-insertion_mark_start\?>(.*?)<\?xm-insertion_mark_end\?>', re.S)
dele = re.compile(r'<\?xm-deletion_mark data="([^"]*)"\?>', re.S)
def clean(t):
    t = re.sub(r'</(?:xhtml:)?p>', '\n', t)
    t = re.sub(r'<(?:xhtml:)?span class="EnSpace"\s*/>', ' ', t)
    t = re.sub(r'<\?xm-[^?]*\?>', '', t)
    t = re.sub(r'<!--.*?-->', '', t, flags=re.S)
    t = re.sub(r'<[^>]+>', '', t)
    return re.sub(r'[ \t]+', ' ', html.unescape(t))
for fn in sorted(f for f in os.listdir(src) if f.endswith('.xml')):
    s = open(os.path.join(src, fn), encoding='utf-8').read(); b = fn[:-4]
    cur  = dele.sub('', s)
    prev = dele.sub(lambda m: html.unescape(m.group(1)), ins.sub('', s))
    mk   = dele.sub(lambda m: '[-' + html.unescape(m.group(1)) + '-]', ins.sub(lambda m: '{+' + m.group(1) + '+}', s))
    for suf, t in (('cur', cur), ('prev', prev), ('mk', mk)):
        open(f'{out}/{b}.{suf}.txt', 'w').write(clean(t))
```

The vote check: `BILL_SUMMARY_VOTE_TBL.dat`, rows for `202520260SB53`. The `CX32` row dated 2025-07-16 reads `10 0 5 (PASS)`.
