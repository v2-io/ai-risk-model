# SB 53 amendment history: notes

*Written 2026-10-09 by a delegated agent (Opus 5.5) for the `california-2025-sb53` source expert. Everything in this file is my reading. The primary texts are in `versions/`, `raw/` and `analyses/`. In each answer below, **Text shows** marks what a primary file says, with a pointer, and **Inference** marks my interpretation.*

## What is here, and where it came from

**Access.** leginfo.legislature.ca.gov answers every scripted request with a Cloudflare challenge (HTTP 403 for every page I tried, `robots.txt` included), so I could not use its "Bill Text" or "Compare Versions" pages. The Legislature also publishes its whole database at `downloads.leginfo.legislature.ca.gov`, and that site is not behind the challenge. `pubinfo_2025.zip` (1.29 GB, last modified 2026-10-05) holds the 2025–26 session. Its `BILL_VERSION_TBL` stores each bill version as Legislative Counsel's CAML XML. I read only the members I needed, using HTTP range requests (`tools/fetch_pubinfo.py`), so the whole zip was never downloaded. These are the same data leginfo's pages are built from, and arguably a better form of them.

**What the XML carries.** Each amended version marks its own changes against the version before it: `<?xm-insertion_mark_start?>…<?xm-insertion_mark_end?>` around added text, and `<?xm-deletion_mark data="…"?>` holding struck text. These are Legislative Counsel's change marks, the italic and strikeout you see on leginfo. So for every amendment there is an authoritative diff as well as my computed one.

**How I checked it.**
1. For each of the 9 transitions, I took version N, dropped its insertions and restored its deletions. The result matches version N−1 word for word: 0 differing words in all 9 cases. So the marks are relative to the immediately preceding version, and my renderer loses nothing.
2. I compared my rendering of the chaptered version against `ref/canonical/california-2025-sb53.md`, after normalizing quote characters and the canonical's `\$` escaping. Every remaining difference was formatting: bullets, bold, headings, page markers and the page header block. The words agree.
3. The bill text and the Digest of the Enrolled (09) and Chaptered (10) versions are word-for-word identical to version 08 (Sept 5). **The statute's text was final on 2025-09-05.**

| # | Date | Version | What happened (BILL_HISTORY_TBL, abridged; full list in `actions.md`) | LC marks (ins / del) |
|---|---|---|---|---|
| 01 | 2025-01-07 | Introduced | Intent-only "spot bill": the Legislature intends to legislate on frontier models, drawing on the Governor's Working Group. 378 words. | — |
| 02 | 2025-02-27 | Amended in Senate | Author's amendments in Senate Rules. Now **CalCompute (Gov. Code) plus whistleblower protections (Labor Code)** only. | 13 / 5 |
| 03 | 2025-03-27 | Amended in Senate | Senate G.O. committee amendments (passed 13–0, Mar 25). | 5 / 3 |
| 04 | 2025-05-23 | Amended in Senate | Senate Appropriations, from the suspense file (6–0). **Passed the Senate 37–0 on May 28 in this form, with no transparency act in it.** | 26 / 19 |
| 05 | 2025-07-08 | Amended in Assembly | Author's amendments in Asm P.&C.P. **The whole B&P chapter (TFAIA) and SEC. 1 findings enter here.** | 79 / 38 |
| 06 | 2025-07-17 | Amended in Assembly | Asm P.&C.P. committee amendments (passed 9–0, July 16). | 53 / 34 |
| 07 | 2025-09-02 | Amended in Assembly | Asm Appropriations, from the suspense file (11–1). | 14 / 16 |
| 08 | 2025-09-05 | Amended in Assembly | Floor amendments ("Read third time and amended"), then re-referred to P.&C.P. under Asm Rule 77.2 (passed 12–1, Sept 11). Passed the Assembly 59–7 on Sept 12; **Senate concurred 29–8 on Sept 13.** | **224 / 147** |
| 09 | 2025-09-17 | Enrolled | No textual change. | — |
| 10 | 2025-09-29 | Chaptered | Ch. 138, Stats. 2025. No textual change. | — |

**Layout**

- `versions/NN-date-label.md` holds each version's full text (Digest plus bill), changes applied. It has one paragraph per `<p>`, as leginfo shows them. A header comment gives the source file and the legislative action.
- `diffs/lc-marked/NN-….marked.txt` is **Legislative Counsel's own marks** for each amended version, written as `{+inserted+}` and `[-struck-]`. These are the authoritative diffs. Struck paragraphs appear as their own paragraphs.
- `diffs/NN-to-MM.diff` and `.word.diff` are my computed diffs of consecutive versions, by paragraph and by word. They agree in content with the LC marks (check 1), but the alignment is git's, not Legislative Counsel's.
- `sections/*.md` follows each section across every version, as full text with a word diff at each change. **They are keyed by lineage, not number, because B&P section numbers moved.** For example, the penalty section was §22757.14 on Jul 8, §22757.16 on Jul 17, and §22757.15 from Sept 2 on. A citation to "§22757.16" of the July 17 text means the penalty section, not the equity section. Each file has a "Numbered as" line.
- `diffs/chaptered-BPC-22757.11-vs-LAB-1107-definitions.word.diff` compares the two chapters' restated definitions directly (Q2).
- `analyses/` holds all 14 committee and floor analyses from `BILL_ANALYSIS_TBL`: the original `.docx` files, plus markdown made with pandoc. These are staff documents, not law, but they are the Legislature's own account of each amendment. The Asm P.&C.P. analyses of July 15 include a mock-up of the proposed committee amendments, in bold italic and strikeout.
- `raw/` holds the ten CAML XML files as fetched. `tools/` holds the renderer, the build and the fetcher. `python3 -I tools/build.py tools raw .` rebuilds everything from `raw/`, and I checked that the rebuild gives identical output.

## Your questions

### Q1. The two "loss of value of equity" sections

**Text shows:** B&P §22757.16 and Lab. Code §1107.2 were **both added on Sept 5 (08)**, with identical wording, and nothing changed after that. Neither chapter mentions equity in any earlier version (`grep -c equity versions/*`: 0 in 01–07). See `sections/BPC-22757.16-equity-not-property.md`, `sections/LAB-1107.2-equity-not-property.md`, and `diffs/lc-marked/08-…marked.txt`.

The Asm P.&C.P. analysis of Sept 10 (`analyses/2025-09-10-…rule-77.2…md`, around line 39) lists among the narrowing amendments "*Adding various exemptions, including … risks that would result in loss of the value of equity …*". Its summary of the bill (around line 81) files the equity sentence as a fourth item under "Excludes from 'catastrophic risk'". So staff read it as a catastrophic-risk exclusion. In the bill it is a free-standing section in each chapter, "for the purposes of this chapter", and so it reaches every use of "property" in the chapter: the CSI definition, for one.

**Text shows (an asymmetry):** the B&P chapter defines "Property" as "tangible or intangible property" (added Jul 17, 06). The Labor Code chapter has never defined "property".

**Inference:** on the B&P side the equity sentence carves something out of a deliberately broad "intangible property". On the Labor Code side it qualifies an undefined term. Since the two were added together, this looks like a sentence copied into both chapters, not drafted for each.

### Q2. Labor Code §1107 vs B&P §22757.11: were the definitions ever identical?

**Text shows:**
- **02–04 (Feb–May, Senate):** the Labor Code chapter was the only chapter that defined a risk; the other was CalCompute. It used its own term, "**critical risk**": "result in the death of, or serious injury to, more than 100 people or more than one billion dollars … in damage to rights in money or property", through four routes, with the third described by reference to Penal Code offenses requiring "intent, recklessness, or gross negligence". "Developer" was defined by a compute cost of $100M at cloud prices. There was no "critical safety incident".
- **05–07 (Jul 8 – Sept 2):** the Labor Code defined "catastrophic risk", "large developer" and "foundation model" **by cross-reference**: they had "the meaning defined in Section 22757.11 of the Business and Professions Code". It had no "critical safety incident" definition. So in these three versions the two chapters were identical by construction.
- **08 (Sept 5):** the Labor Code restated "catastrophic risk" and added "critical safety incident" in full, in the same amendment that rewrote B&P §22757.11. "Foundation model", "frontier developer" and "large frontier developer" still cross-refer to B&P.

So no version ever had two identical restated texts. The divergence was born in the same amendment that did the restating. The full set of differences in the final text is in `diffs/chaptered-BPC-22757.11-vs-LAB-1107-definitions.word.diff`:
- "foundation model" for "frontier model" throughout;
- the human-equivalent clause reads "if committed by a human" (Labor) against "if the conduct had been committed by a human" (B&P);
- exclusion (C) has "where the foundation model did not…" against "if the frontier model did not…";
- in the weight-theft CSI, the Labor Code says "results in death, bodily injury, or damage to, or loss of, property", while B&P says "results in death or bodily injury".

On Sept 5, B&P's loss-of-control CSI dropped property; the Labor Code's version never had it. Before Sept 5, B&P's weight-theft CSI had no harm requirement at all (05–07).

**Inference:** the Labor Code text is not simply an earlier state of B&P's text, because B&P never had the property-loss form of the weight-theft clause. It looks like a separately edited copy taken from a Sept 5 working draft. "Foundation model" is a deliberate widening: the whistleblower chapter covers risks from foundation models below the compute line. The property clause and the small wording differences look like edits made to one copy and not the other. The texts alone cannot tell which.

### Q3. "comply with" in §22757.12(a), and the Digest

**Text shows:** "comply with" **entered on Jul 17 (06)**: `diffs/lc-marked/06-…marked.txt` line 176 reads "write, implement,{+ comply with,+} and clearly and conspicuously publish". **The Digest never included it, in any version (05–10).** The Digest sentence was carried over from Jul 8 (05). Legislative Counsel edited that same sentence on Sept 5, inserting "frontier" and replacing the protocol with the framework (`diffs/lc-marked/08…`, line 20), and still did not add "comply with".

There is one more wrinkle. The P.&C.P. analysis of July 15, the one that prints the proposed committee amendments as a mock-up, shows §22757.12(a) *without* "comply with" (`analyses/2025-07-15b…md` line 631), and yet the text adopted on Jul 17 has it. The floor analyses from Sept 3 on, and the Senate concurrence analysis, do include it.

**Inference:** "comply with" was added to the committee amendments after the mock-up in the analysis was finalized, either at the hearing or in drafting the amendments as taken. The Digest's silence looks like a Digest that was never updated, not a deliberate reading.

A related point: the Digest's penalty sentence reads "a civil penalty for noncompliance with the TFAIA". It has no "large" restriction (next item), so the Digest is broader than the operative section.

### Q4. Was the penalty always limited to *large* developers?

**Text shows** (see `sections/BPC-22757.15-penalties.md`):
- **05 (Jul 8):** "A violation of this chapter shall be subject to a civil penalty … not to exceed ____ dollars". The violator was not limited, and the amounts were blank.
- **06 (Jul 17):** "A large developer who violates this chapter…". This version had tiered penalties: $10k for an unknowing violation with no material risk, with a 30-day cure; $100k; and $1M for a first violation, rising to $10M. It also had a separate $10k penalty for auditors.
- **07 (Sept 2):** the auditor penalty was dropped along with the audits. The rest was unchanged.
- **08 (Sept 5):** "A large frontier developer that fails to publish or transmit a compliant document …, makes a statement in violation of subdivision (e) of Section 22757.12, fails to report an incident as required by Section 22757.13, or fails to comply with its own frontier AI framework …", up to $1M per violation, "dependent upon the severity".

In 05–07 every duty in the B&P chapter fell on a "large developer", apart from the v06 auditors, who had their own penalty. The non-large "frontier developer" class first exists on Sept 5. In the same amendment, its duties arrive: a transparency report in §22757.12(c), the false-statement bar in (e)(1)(A), and incident reporting in §22757.13(c).

**Inference:** "large" was in the subject from Jul 17 on. But it had no limiting effect until Sept 5, when the amendment split the regulated class in two, put duties on both halves, and left the penalty section on one half by inserting "frontier" after "large". The section names violations of §22757.12(e) and §22757.13, and those duties bind any frontier developer. Either the drafters chose to leave non-large developers' reporting duties without a §22757.15 penalty, or the split did not reach this sentence. The texts alone cannot settle which. The Sept 10 P&CP analysis describes the new penalty without remarking on the limit, calling it "a much more lenient enforcement mechanism".

### Q5. "the catastrophic risk" in §22757.13(h)(2)

**Text shows:** the whole federal-equivalence mechanism, §22757.13(h)–(j), **entered on Sept 5 (08)**, with "the catastrophic risk" already in it. No earlier version has any federal-designation clause, so no earlier SB 53 draft had an antecedent for "the". The P.&C.P. analysis of Sept 10 paraphrases the clause as "intended to assess and mitigate catastrophic risk", with no article (line 421).

**Text shows (outside this bill):** New York's RAISE chapter amendment, `ref/canonical/ny-2026-raise-s8828.md`, line 204, §8(b), reads "the law, regulation, or guidance document is intended to assess, detect, or mitigate the catastrophic risk." The whole designation mechanism around it is close to verbatim SB 53.

**Inference:** within SB 53's history this is not left over from an earlier SB 53 draft. Either it is a slip in the Sept 5 drafting, or the clause was imported whole from a text where "the catastrophic risk" had an antecedent. I could not find such a text: the obvious candidates in the corpus are later copies of SB 53, not sources for it. The RAISE copy carries the stray article with it, which makes it a clean marker of copying. That bears directly on the repo's "agreement that is really copying" theme. You are reading RAISE now, so you may already have seen this.

### Q6. SEC. 1 findings vs the Governor's Report

**Text shows:** **no version before Jul 8 (05) has any findings section.** In 02–04, SECTION 1 is the Government Code section. In 01 it is a one-sentence intent clause that anticipates "the findings of the Joint California Policy Working Group on AI Frontier Models". So every finding in the chaptered SEC. 1 dates from Jul 8 or later, after the final Report. The Sept 10 analysis says the Working Group "published its final report in June 2025". My training memory puts the final report at June 17, 2025, and the draft at March 18, 2025. I have not checked either date.

How each chaptered finding came to be (`sections/bill-SEC1-findings.md`):

| Chaptered | Origin | Later change |
|---|---|---|
| (a)–(c), (h), (n) | Jul 8 | none. (c) is the one Jul 8 finding naming the Working Group ("has recommended sound principles") |
| (d) | Jul 8 | Sept 5: "benefits and **the potential for** material risks" |
| (e) | Jul 8 (f) | none |
| (f) | Jul 8 (g) | Sept 5 rewrite: "a significant information asymmetry can develop between those with privileged access to data and the broader public" became "public trust in these technologies would significantly benefit from access to information regarding, and increased awareness of, frontier AI capabilities" |
| (g) | Jul 8 (h) | Sept 5: "given current information deficits" struck; "also" added |
| (i) | Jul 8 (j) | Sept 5: "Adverse event reporting" became "Incident reporting" |
| (j) | Jul 8 (k) | Sept 5: "**There is growing evidence that**, unless …, advanced AI systems could pose catastrophic risks" became "Unless …, **there is concern that** advanced AI systems could **have capabilities that** pose catastrophic risks" |
| (k) | Jul 8 (l) | Sept 5: "the risks" became "serious risks" |
| (l), (m) | **Sept 5, new.** (l) says voluntary frameworks are an industry best practice, "not all developers are providing reporting that is consistent and sufficient". (m) is on timely CSI reporting | |
| (o) | **Sept 5, new.** "The recent release of the Governor's California Report on Frontier AI Policy and testimony from legislative hearings … reflect the advances in AI model capabilities that could pose potential catastrophic risk" | |
| (p) | Jul 8 (o) | Sept 5: "large developers" became "frontier developers"; "foundation" became "frontier" |
| *(struck)* | Jul 8 (e): "AI developers have already voluntarily committed to creating safety and security protocols…" | struck Sept 5; its substance is reworked into the new (l) |
| *(struck)* | Jul 8 (m): "A computational threshold of 10^26 … captures only highly resourced developers spending hundreds of millions of dollars" | struck Jul 17, the same amendment that added the $100M revenue test |

**Inference:** the findings themselves never cite the Report until Sept 5. Its influence before then is unnamed: (c) praises the Working Group's "sound principles", and the vocabulary ("evidence environment", "information asymmetry", "adverse event reporting") matches the July analyses, which quote the Report heavily. The Sept 5 changes run one way. They soften claims about evidence ("growing evidence" became "concern"), remove the information-asymmetry framing, and add the first explicit attribution to the Report. For a project that records each source's evidential stance, the chaptered findings are the *softened* stance, and the Jul 8 text is the stronger one.

### Q7. SEC. 5(d), the federal-contract carve-out

**Text shows:** **added on Jul 8 (05)**, in the same amendment that added the TFAIA, reading "between a federal government entity and a **large** developer". It changed to "**frontier** developer" on Sept 5 and is otherwise unchanged. It appears unchanged in the Jul 15 P.&C.P. mock-up (line 897). The same Sept 5 amendment added SEC. 5(f), which preempts local rules adopted on or after January 1, 2025 "specifically related to the regulation of frontier developers with respect to their management of catastrophic risk". See `sections/bill-SEC5-construction-and-scope.md`.

## Whether the questions are framed right

The questions are well aimed. The history answers most of them the same way: **most of the narrowing clauses arrived in a single amendment, Sept 5 (08).** It has nearly three times as many change marks as any other version (224 insertions against 79), and it went through a Rule 77.2 re-referral for substantial amendments. So the useful unit of history is less "when did clause X enter" than "what did the Sept 5 amendment do as a package". The Legislature's own account of that package is the bullet list in the Sept 10 P.&C.P. analysis (`analyses/2025-09-10-…`, lines 25–51). Some of what that amendment did:

- It replaced "a single incident, scheme, or course of conduct" with "**a single incident**", which is your counting rule. An opposition letter quoted in the July 15 analysis (around line 992) had called the older wording "contradictory".
- It folded the defined term "dangerous capability" into "catastrophic risk".
- It added all three catastrophic-risk exclusions: publicly accessible information, lawful federal activity, and combination with other software.
- It made the weight-theft and deception CSIs require harm, or "materially increased catastrophic risk".
- It dropped the B&P CSI for "attaining a dangerous capability or catastrophic risk threshold … for the first time" (which existed Jul 17 – Sept 2).
- It renamed the "safety and security protocol" the "frontier AI framework".
- It moved incident reporting from the AG to OES.
- It made internal-use risk assessments confidential summaries for OES. Before, they were public.
- It replaced the Attorney General's power to redefine "large developer" by regulation with recommendations from the Department of Technology.
- It cut the penalty cap from $10M to $1M.
- It narrowed whistleblower protection from a broad "employee" (contractors, freelancers, board members) to "covered employee", and added "specific and substantial danger to the public health or safety" before "catastrophic risk".
- It added local preemption and the equity sections.

Earlier changes that are easy to miss:
- **The thresholds moved in steps.** On Jul 17 the casualty count went from 100 to 50 and "rights in money or property" became "property", with property defined as tangible or intangible. The revenue test was $100M on Jul 17 and $500M from Sept 2. The July 15 analysis calls the $100M figure "a threshold recently referenced by Anthropic in its description of their transparency framework" (line 483).
- **Third-party audits** (annual, from 2030) existed only in the Jul 17 version and were dropped by Appropriations on Sept 2.

**A genuine leftover from an earlier draft, of the kind your Q5 is looking for:** in 02–03, the Labor Code "Employee" definition covered contractors "involved with assessing, managing, or addressing the risk of critical harm from covered models and covered model derivatives". The bill never defined those terms. As far as I remember, they are SB 1047's vocabulary. They were removed on May 23. A second leftover survives in the statute: **the chaptered bill's subject line is still "Artificial intelligence models: large developers."**, but the term "large developer" has not appeared in the text since Sept 5.

**On process:** the Senate never voted on the TFAIA in committee or on its own floor. Its 37–0 floor vote (May 28) was on a CalCompute-and-whistleblower bill. The Senate's only vote on the transparency act was concurrence, 29–8 (Sept 13).

**Conflict-of-interest note, per the repo's principle:** the Sept 10 P.&C.P. analysis lists Anthropic as a supporter and quotes its letter. The July 15 analysis ties the first revenue threshold to Anthropic's framework.

## Caveats and oddities

- The Senate concurrence analysis in the database (`analyses/2026-07-21-senate-floor-unfinished-business-concurrence.md`) is dated 2026-07-21 and says "Amended: 9/29/25", which cannot be the version concurred in on Sept 13. It may be a later re-post. Do not assume it is exactly what senators had on Sept 13.
- The two July 15 P.&C.P. analyses (`…07-15a…` and `…07-15b…`) differ. The first says catastrophic risks are those resulting in "more than 100 deaths or $100 billion in damage", and the second corrects this to "$1 billion". The analyses are useful, but they are not the text.
- My renderings keep the XML's curly quotes. The repo's canonical text uses straight quotes, so an exact-quote check that crosses the two needs normalizing.
- **Not obtained:** leginfo's HTML pages, which were blocked, though their content is the same data; vote-by-member tables, which are in `BILL_DETAIL_VOTE_TBL` if wanted; hearing video; the author's fact sheets; letters beyond those quoted in the analyses; and any signing statement, since the bulk data has only veto messages.
- **One question I could not answer from these files:** whether the Sept 5 text was modeled on another bill's language (Q5). The pubinfo zip has every 2025–26 bill version. A phrase search across all of them is possible, but it means pulling far more of the zip. Say if you want it.
