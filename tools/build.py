#!/usr/bin/env python3
"""Build the project icon set: SVG sources, PNG exports, gallery, manifest.

Run from anywhere:  python3 project-icons/tools/build.py
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

TOOLS = Path(__file__).resolve().parent
ROOT = TOOLS.parent
sys.path.insert(0, str(TOOLS))

from svgkit import ACCENTS, svg_document  # noqa: E402
from glyphs_1 import ICONS as PART_ONE  # noqa: E402
from glyphs_2 import ICONS as PART_TWO  # noqa: E402

ICONS = {**PART_ONE, **PART_TWO}
SVG_DIR = ROOT / "svg"
PNG_DIR = ROOT / "png"
SIZES = (16, 32, 48, 64, 128, 256, 512)


def signature(spec):
    parts = tuple((p["d"], p.get("tone", "main"), p.get("transform"))
                  for p in spec["parts"])
    return parts, spec["details"]


def check():
    problems = []
    seen = {}
    for slug, spec in ICONS.items():
        if spec["accent"] not in ACCENTS:
            problems.append(f"{slug}: unknown accent {spec['accent']!r}")
        if not spec.get("parts"):
            problems.append(f"{slug}: no silhouette")
        sig = signature(spec)
        if sig in seen:
            problems.append(f"{slug}: drawing identical to {seen[sig]}")
        seen[sig] = slug
        if not spec["name"] or not spec["what"]:
            problems.append(f"{slug}: missing name or description")
    if problems:
        raise SystemExit("icon set is not valid:\n  " + "\n  ".join(problems))


def write_svgs():
    SVG_DIR.mkdir(parents=True, exist_ok=True)
    for slug, spec in ICONS.items():
        doc = svg_document(slug, spec["accent"], spec["parts"], spec["details"],
                           f"{spec['name']} — {spec['what']}")
        (SVG_DIR / f"{slug}.svg").write_text(doc, encoding="utf-8")


def render_pngs():
    """One Inkscape process per file: parallel Inkscape processes abort."""
    PNG_DIR.mkdir(parents=True, exist_ok=True)
    jobs = [(SVG_DIR / f"{slug}.svg", PNG_DIR / f"{slug}-{size}.png", size)
            for slug in ICONS for size in SIZES]
    for i, (src, dst, size) in enumerate(jobs, 1):
        subprocess.run(
            ["inkscape", str(src), f"--export-filename={dst}",
             f"--export-width={size}", f"--export-height={size}"],
            check=True, capture_output=True,
        )
        if i % 49 == 0:
            print(f"  rendered {i}/{len(jobs)} PNGs")


def gallery_html():
    cards = []
    for slug, spec in ICONS.items():
        accent = ACCENTS[spec["accent"]]
        cards.append(f'''    <article class="card">
      <img src="png/{slug}-128.png" width="128" height="128" alt="{spec["name"]} icon">
      <h2>{spec["name"]}</h2>
      <p>{spec["what"]}</p>
      <p class="files"><a href="svg/{slug}.svg">svg</a> · <a href="png/{slug}-512.png">512 png</a>
        <span class="swatch" style="background:{accent}" title="{spec["accent"]} {accent}"></span></p>
    </article>''')

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Project icons — Tela palette</title>
<style>
  :root {{
    color-scheme: light dark;
    --bg: #f9f9f9; --panel: #ffffff; --ink: #263238; --muted: #5c6b73;
    --line: #e0e4e6; --accent: #5294e2;
  }}
  @media (prefers-color-scheme: dark) {{
    :root {{ --bg:#1c2329; --panel:#232c33; --ink:#f2f2f2; --muted:#a7b3ba;
             --line:#2f3a42; --accent:#66bcff; }}
  }}
  * {{ box-sizing: border-box; }}
  body {{ margin:0; background:var(--bg); color:var(--ink);
         font:16px/1.55 "Cantarell","Noto Sans",system-ui,sans-serif; }}
  header {{ max-width:1180px; margin:0 auto; padding:3.5rem 1.5rem 1.5rem; }}
  h1 {{ font-size:clamp(1.7rem,4vw,2.6rem); margin:0 0 .4rem; letter-spacing:-.02em; }}
  header p {{ margin:0; color:var(--muted); max-width:62ch; }}
  main {{ max-width:1180px; margin:0 auto; padding:1rem 1.5rem 4rem;
          display:grid; gap:1rem; grid-template-columns:repeat(auto-fill,minmax(210px,1fr)); }}
  .card {{ background:var(--panel); border:1px solid var(--line); border-radius:14px;
           padding:1.1rem 1rem 1rem; text-align:center; }}
  .card img {{ image-rendering:auto; display:block; margin:0 auto .7rem; }}
  .card h2 {{ font-size:.98rem; margin:0 0 .3rem; letter-spacing:-.01em; }}
  .card p {{ margin:0; font-size:.78rem; color:var(--muted); }}
  .files {{ margin-top:.7rem !important; display:flex; align-items:center;
            justify-content:center; gap:.45rem; }}
  .files a {{ color:var(--accent); text-decoration:none; }}
  .files a:hover {{ text-decoration:underline; }}
  .swatch {{ width:.8rem; height:.8rem; border-radius:50%;
             border:1px solid rgba(0,0,0,.15); display:inline-block; }}
  footer {{ max-width:1180px; margin:0 auto; padding:0 1.5rem 3rem;
            color:var(--muted); font-size:.82rem; }}
</style>
</head>
<body>
<header>
  <h1>jointhefreeworld-icons</h1>
  <p>One hand-drawn icon per project in <code>~/Hacking</code>, drawn the way Tela
  draws its own: each icon is an object — a document, a disc, a folder, a
  terminal, a cloud — in Tela's palette, with white detail and a soft corner
  shade. 64×64 vector sources, 16–512 px exports, a unique silhouette and glyph
  per project. <a href="preview.png">Contact sheet</a>.</p>
</header>
<main>
{chr(10).join(cards)}
</main>
<footer>{len(ICONS)} icons · Tela palette · sources in <code>svg/</code>,
renders in <code>png/</code>, manifest in <code>icons.json</code>.</footer>
</body>
</html>
'''


def preview_png():
    """A labelled contact sheet of the whole set, 128 px per icon."""
    try:
        from PIL import Image, ImageDraw, ImageFont
    except ImportError:
        print("  (skipping preview.png: Pillow is not installed)")
        return

    cols, cell, pad, line = 7, 128, 12, 20
    rows = (len(ICONS) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * (cell + pad) + pad,
                              rows * (cell + line + pad) + pad),
                      (247, 247, 248))
    draw = ImageDraw.Draw(sheet)
    try:
        font = ImageFont.truetype(
            "/usr/share/fonts/dejavu-sans-fonts/DejaVuSans.ttf", 12)
    except OSError:
        font = ImageFont.load_default()

    for i, (slug, spec) in enumerate(ICONS.items()):
        row, col = divmod(i, cols)
        x = pad + col * (cell + pad)
        y = pad + row * (cell + line + pad)
        icon = Image.open(PNG_DIR / f"{slug}-128.png").convert("RGBA")
        sheet.paste(icon, (x, y), icon)
        draw.text((x + cell // 2, y + cell + 2), slug, fill=(38, 50, 56),
                  font=font, anchor="ma")
    sheet.save(ROOT / "preview.png")


def readme_md():
    rows = "\n".join(
        f"| ![{spec['name']}](png/{slug}-64.png) | `{slug}` | {spec['name']} | {spec['what']} | `{ACCENTS[spec['accent']]}` |"
        for slug, spec in ICONS.items()
    )
    return f'''# jointhefreeworld-icons 🌿

![Every icon in the set](preview.png)

One hand-drawn icon for every project in the jointhefreeworld collection:
fifty objects, fifty colours, not one repeated glyph.

- `svg/<project>.svg` — the 64×64 source, hand-written paths, no bitmaps.
- `png/<project>-{{16,32,48,64,128,256,512}}.png` — transparent PNG exports.
- `index.html` — the gallery, open it in a browser.
- `preview.png` — a labelled contact sheet of the whole set.
- `icons.json` — name, purpose and accent colour per icon.

## The cloth

*Tela* is Latin for cloth — the warp stretched on the loom before the weaver
begins. The Tela icon theme takes that name seriously. It does not draw
pictures inside rounded squares; it draws *things*. A folder with a tab that
lifts. A terminal with a lip. A disc worn smooth by handling. Nothing is
framed, because nothing needs a frame: the object simply is, and the desktop
arranges itself around it.

These icons are a small act of divination from that cloth. Every project in
the collection was read — its README, its source, the reason it exists — and
then asked what shape it would wear if it had to survive outside the screen.
A crawler became a spider on a half-spun web; a CI bridge became a woodpecker
against a trunk; a secret manager became a sealed envelope; a test framework
became scales that still balance. The answer was cut from the same cloth Tela
weaves: one accent carrying the whole silhouette, a pale face where the light
lands, a shade falling to the lower right, a thin dark line keeping the edge
honest. The colours were not guessed — they were measured from the Tela icons
installed on this machine, so the set can sit beside them without breaking
the circle.

No two drawings are alike, and the build refuses to let them become so: two
projects sharing a silhouette or a glyph is a build error, not a style note.

## The fifty

| Icon | Folder | Name | What it is | Accent |
| --- | --- | --- | --- | --- |
{rows}

## The rules of the weave

- **Objects, not tiles.** A folder is a folder, a terminal is a terminal. No
  background plate, no squircle, no badge behind the drawing.
- **One accent per icon.** A silhouette in a single colour, shaded only by
  light: `main` for the body, `light` and `pale` for the top face, `dark` and
  `deep` for the sides and the recesses.
- **White carries the meaning.** Lettering, arrows, seams, holes and highlights
  are cut in paper-white, the way Tela marks its folders and drives.
- **Light from above, shade to the lower right.** A clipped gloss across the
  top, a soft diagonal shadow in the corner, and a hairline outline so the
  object keeps its edge on a pale wallpaper.
- **One family per idea.** Related projects share a form on purpose — the four
  Emacs extensions are all discs, distinguished by what they hold — while
  everything else earns its own silhouette.

## Rebuilding

```sh
python3 tools/build.py
```

Requires Python 3, Inkscape (for the PNG exports) and Pillow (for
`preview.png`). The build validates the set first, then writes `svg/`,
`png/`, `icons.json`, `index.html`, `preview.png` and this file.

## Lineage and licence

This set is original work, released under the MIT licence (see `LICENSE`).
Its inspiration is the [Tela icon theme](https://github.com/vinceliuice/Tela-icon-theme)
by Vinceliuice, which is GPL-3.0: no Tela file is copied or modified here.
What travels between the two sets is colour and discipline — the palette was
sampled from Tela's own icons, and the drawing rules follow its example.
'''


def manifest():
    return {
        "theme": "jointhefreeworld-icons, after Tela",
        "grid": 64,
        "sizes": list(SIZES),
        "icons": [
            {
                "slug": slug,
                "name": spec["name"],
                "purpose": spec["what"],
                "accent": spec["accent"],
                "colour": ACCENTS[spec["accent"]],
                "svg": f"svg/{slug}.svg",
                "png": {str(s): f"png/{slug}-{s}.png" for s in SIZES},
            }
            for slug, spec in ICONS.items()
        ],
    }


def main():
    check()
    print(f"{len(ICONS)} icons, {len(ACCENTS)} accent families")
    write_svgs()
    render_pngs()
    (ROOT / "icons.json").write_text(
        json.dumps(manifest(), indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8")
    (ROOT / "index.html").write_text(gallery_html(), encoding="utf-8")
    (ROOT / "README.md").write_text(readme_md(), encoding="utf-8")
    preview_png()
    print(f"wrote {len(ICONS)} SVGs and {len(ICONS) * len(SIZES)} PNGs to {ROOT}")


if __name__ == "__main__":
    main()
