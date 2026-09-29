# alignment-model

Builds the "Aligned to whom?" map (everything above the rule: masthead, actor table, lines, the agent's stack, notes, footnote) from `alignment.md`.

```sh
python3 build.py                 # alignment.md -> alignment.html (self-contained)
python3 build.py --link          # links the CSS / JS instead — edit CSS and just reload
python3 build.py --palette       # also writes palette.html (every colour class)
python3 build.py other.md -o other.html
python3 contrast.py              # CAM02-UCS contrast report -> contrast-report.md
python3 fit_palette.py --dry-run # re-fit the colour families (see its header); drop --dry-run to write palette.css
```

Standard library only.

| File | What to change there |
|---|---|
| `alignment.md` | All content: intro, lead (`>` paragraph), stack boxes, actors, edges, highlights, notes, footnote |
| `palette.css` | All colour: paper and ink, the ten families, the family / step / accent classes |
| `style.css` | Layout and type: fonts, column widths, box shapes, spacing |
| `template.html` | Page structure and slots (`{{title}}`, `{{rows}}`, `{{stack}}`, …) |
| `lines.js` | How lines are drawn: stroke width/opacity per weight, curve bend, endpoint spacing |
| `build.py` | Markdown parsing and HTML generation |
| `contrast.py` | Perceptual check of the palette (CIECAM02 / CAM02-UCS ΔE′, WCAG) |
| `fit_palette.py` | Regenerates the family colours in `palette.css` from a few settings (distance from the paper, step lifts, colourfulness, red trim, darkening cap, hues) |

**Edges.** In the actors table, `edges` is a comma list of stack ids, each optionally `:weight` (`context:2`, `ephemeral:3`). Lines are drawn in the browser from the rendered layout, so row heights, box sizes and CSS can change freely without touching coordinates. A line takes its colour from the `--edge` of the box it lands on.

**Colours.** Ten families — stone, rose, clay, sand, sage, jade, teal, slate, iris, mauve — each with a three-step fill scale, a border, a line colour and an accent ink. Rows and boxes take the same classes:

- `sand` — normal (the palest step)
- `sand deep` — one step deeper
- `sand deeper` — two steps deeper
- add `accent` to put the row's or box's name in the family's ink

The fills are fitted in CAM02-UCS against the paper: every family's deeper fill is ≈ 10 from the paper, deep and normal are constant lifts toward it (≈ 6.7 and 3.3), the nine hues are spread ~40° apart at equal colourfulness, reds are 10% less colourful, and darkening is capped so families near the paper's own hue stay pastel. The header of `palette.css` has the details, `fit_palette.py` regenerates them (with no options it reproduces the current palette; its header explains each setting) and `contrast.py` measures them.

**Other classes.** `referent` (owed-alignment rows: no lines, drawn below the map), `context`, `goal`, `current` (box shapes) and `end` (pin a nested box to the bottom of its parent) are plain CSS classes; add one with a rule in `style.css`.

**Adding a display column.** Add a column to the actors table; every column except `edges` and `class` is shown, in order.
