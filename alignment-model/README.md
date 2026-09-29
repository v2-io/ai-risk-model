# alignment-model

Builds the "Aligned to whom?" map (everything above the rule: masthead, actor table, lines, the agent's stack, notes, footnote) from `alignment.md`.

```sh
bundle install        # once: slim, sass-embedded (bundles Dart Sass), rake
rake                  # alignment.md -> alignment.html (self-contained)
rake palette          # also palette.html (every colour class)
rake link             # links styles.css + lines.js instead of inlining (rebuild after editing Sass)
rake contrast         # CAM02-UCS contrast report -> contrast-report.md   (python3)
rake fit              # dry-run of fit_palette.py: print a re-fitted palette  (python3)

ruby build.rb other.md -o other.html     # any other markdown file
```

Ruby and Python versions are pinned in `mise.toml` (run `mise trust` once). The two Python scripts use the standard library only.

| File | What to change there |
|---|---|
| `alignment.md` | All content: intro, lead (`>` paragraph), stack boxes, actors, edges, highlights, notes, footnote |
| `styles/palette.sass` | All colour: paper and ink, the ten families (their tokens and the `$families` list the classes are generated from), step and accent classes |
| `styles/style.sass` | Layout and type: fonts, column widths, box shapes, spacing |
| `templates/page.slim` | Page structure; `actor.slim` (one row) and `box.slim` (one stack box, recursive) are its partials |
| `templates/palette.slim` | The swatch page |
| `lines.js` | How lines are drawn: stroke width/opacity per weight, curve bend, endpoint spacing |
| `build.rb` | Markdown parsing into a small model (`Page`, `Box`, `Group`, `Actor`) and rendering |
| `contrast.py` | Perceptual check of the palette (CIECAM02 / CAM02-UCS ΔE′, WCAG) |
| `fit_palette.py` | Regenerates the family tokens in `styles/palette.sass` from a few settings (distance from the paper, step lifts, colourfulness, red trim, darkening cap, hues); its header explains each |

**Edges.** In the actors table, `edges` is a comma list of stack ids, each optionally `:weight` (`context:2`, `ephemeral:3`). Lines are drawn in the browser from the rendered layout, so row heights, box sizes and CSS can change freely without touching coordinates. A line takes its colour from the `--edge` of the box it lands on.

**Colours.** Ten families — stone, rose, clay, sand, sage, jade, teal, slate, iris, mauve — each with a three-step fill scale, a border, a line colour and an accent ink. Rows and boxes take the same classes:

- `sand` — normal (the palest step)
- `sand deep` — one step deeper
- `sand deeper` — two steps deeper
- add `accent` to put the row's or box's name in the family's ink

The fills are fitted in CAM02-UCS against the paper: every family's deeper fill is ≈ 10 from the paper, deep and normal are constant lifts toward it (≈ 6.7 and 3.3), the nine hues are spread ~40° apart at equal colourfulness, reds are 10% less colourful, and darkening is capped so families near the paper's own hue stay pastel. The header of `styles/palette.sass` has the details, `fit_palette.py` regenerates them (with no options it reproduces the current palette) and `contrast.py` measures them.

**Other classes.** `referent` (owed-alignment rows: no lines, drawn below the map), `context`, `goal`, `current` (box shapes) and `end` (pin a nested box to the bottom of its parent) are plain CSS classes; add one with a rule in `styles/style.sass`.

**Adding a display column.** Add a column to the actors table; every column except `edges` and `class` is shown, in order.

**A note on indented Sass.** A `//` comment on the same line as a custom property (`--x: 1px  // …`) becomes part of the value; keep those comments on their own line.
