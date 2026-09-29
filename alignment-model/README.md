# alignment-model

Builds the "Aligned to whom?" map (everything above the rule: masthead, actor table, lines, the agent's stack, notes, footnote) from `alignment.md`.

```sh
python3 build.py                 # alignment.md -> alignment.html (self-contained)
python3 build.py --link          # links style.css / lines.js instead — edit CSS and just reload
python3 build.py --palette       # also writes palette.html (every hue class and modifier)
python3 build.py --theme themes/spread.css --palette     # alternative palette -> alignment-spread.html, palette-spread.html
python3 contrast.py [--theme themes/spread.css]          # CAM02-UCS contrast report -> contrast-report[-spread].md
python3 build.py other.md -o other.html
```

Standard library only.

| File | What to change there |
|---|---|
| `alignment.md` | All content: intro, lead (`>` paragraph), stack boxes, actors, edges, highlights, notes, footnote |
| `style.css` | Colours (tokens on `:root`), fonts, column widths, box styling, row highlight classes |
| `template.html` | Page structure and slots (`{{title}}`, `{{rows}}`, `{{stack}}`, …) |
| `lines.js` | How lines are drawn: stroke width/opacity per weight, curve bend, endpoint spacing |
| `build.py` | Markdown parsing and HTML generation |

**Edges.** In the actors table, `edges` is a comma list of stack ids, each optionally `:weight` (`context:2`, `ephemeral:3`). Lines are drawn in the browser from the rendered layout, so row heights, box sizes and CSS can change freely without touching coordinates. A line takes its colour from the `--edge` of the box it lands on.

**Colours.** `style.css` defines ten colour families — stone, rose, clay, sand, moss, jade, teal, slate, iris, plum — each with three fills plus a border, a line colour and an accent ink. Rows and boxes use the same classes:

- `sand` — normal (the palest step)
- `sand deep` (alias `dark`) — one step deeper
- `sand deeper` (alias `darker`) — two steps deeper
- add `accent` to put the row's or box's name in the family's ink

The default palette ("lift") puts every family's deeper fill ΔE′ 12 from the paper in CAM02-UCS, with the nine hues spread as far apart as possible; deep and normal are constant lifts toward the paper, so they sit 8 and 4 from it and every step is ≈ 4. `ochre`, `sage` and `indigo` still work as aliases for moss, jade and iris. `python3 build.py --palette` writes `palette.html`.

**Themes.** A file in `themes/` overrides the colour tokens after `style.css`: `balanced-mid.css` and `spread.css` are the alternatives, `lift.css` restores the default. `themes/old/` holds earlier palettes in the previous token format (not compatible with the current classes).

```sh
python3 build.py --theme themes/spread.css --palette   # -> alignment-spread.html, palette-spread.html
python3 contrast.py [--theme themes/spread.css]        # CAM02-UCS report -> contrast-report[-spread].md
```

**Classes.** Other class values (`referent`, `context`, `goal`, `current`, `end`, …) are plain CSS classes; add one with a rule in `style.css`.

**Adding a display column.** Add a column to the actors table; every column except `edges` and `class` is shown, in order.
