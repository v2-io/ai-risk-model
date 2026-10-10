# Flags for tool owners and quoters (aisi-2025-frontier, read 2026-10-09 by the Sonnet 5.5 expert)

Conversion / reading-tool observations (separate from what the source says):
- Figures sit on their own line at the end of a unit's text and are shown at the head of the next unit (by design). Several figure/text pairings are therefore offset by one unit (Figs 10, 13, 16, 17, 19). A hint in the output would help.
- RESOLVED 2026-10-10 by checking the PDF (54 pages): pdf-pages 50-51 (printed "48"-"49") are the reference list, 37 entries (23 on printed 48, 14 on printed 49), image-only with no text layer, so pdftotext gives nothing; the converted markdown does contain all 37 entries but under the pdf-page 49 / printed "47" marker. No content lost; the page labels on the references table are wrong by two pages. Entry 20 in the converted table is cut ("...202") but the PDF page shows "2025". Entries without authors or dates (5, 14, 15, 18, 21, 22, 33, 35, 36) are that way in the PDF too.
- RESOLVED the same way: the printed-"6" / pdf-page 8 gap. That page holds "Why we're releasing this report" and "Our testing approach", which I read as units 18-22 under a p.7 / printed "5" label. No content lost; the converter's page labels run one page early in that stretch. pdf-page 46 (printed 44, Figure 25) matches what I read in unit 105. I checked only these pages, not all 54.
- Literal "\n" in the Data Presentation paragraph; "AlSI's" (unit 11); "sustems" (unit 52); "A ccordingly" (unit 68); a dropped word in the plasmid glossary entry ("circular found"); reference 20 truncated ("202"); "the potential lag time" in Fig 11/4 annotations ("of" for "or"). Hyphens dropped at line breaks in places ("PhDlevel", "capturethe-flags").
- Figure text extraction: Fig 15's plot text is extracted as a jumble (units 67); the plot itself could not be seen by the tool output (no figure path). The unit 22-23 page jump (p.7 to p.9) was checked and holds no missing text.

Internal inconsistencies in the source worth knowing before quoting (all with unit numbers in 01-reflections.md):
- Apprentice-level cyber: "<1 year" (caption, unit 13) vs "1-3 years" (glossary, unit 121).
- Fig 15: "R = 0.097" (caption) vs "R² = 0.097" (prose), unit 67.
- Fig 14: the category and access panels both labelled "+10x across providers" while showing 30x and 15x, unit 64.
- Troubleshooting "absolute score of 44%" is the biology expert baseline, not the model score (unit 41/43).
- Open-source defined three ways (units 10, 101, 119).
- Sandbagging defined as possibility (77), as strategic underperformance (73), as a phenomenon (glossary, 120).
- Self-replication stages: prose says persistence is weak; Fig 17 shows 70% top score for persisting (unit 77).
- "First model" (units 5, 47) vs "All systems are just beginning" (unit 34) for expert-level cyber tasks.
- Fig 11 dev set vs "separate development task set" (units 49-50).
- Exec-summary compressions: "doubling every eight months" omits "upper bound"; "5% to 60%" omits "11 of 20 tasks" and "closed models only"; "over a third" is 33%; "up to 60%/90%" are best-model relative scores; the persuasion belief null result is omitted.
