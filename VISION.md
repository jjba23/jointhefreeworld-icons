# Vision

Every project in the jointhefreeworld collection has an icon, and each icon is a
drawn object rather than a tile: a crawler becomes a spider on a half-spun web,
a secret manager a sealed envelope, a CI bridge a woodpecker against a trunk.
The set is generated from data, validated before it is written, and rebuilt with
one command. This document says what that generation should eventually publish —
which artefacts, which formats, which guarantees — and where the drawing rules
have to stay firm.

## Where project-icons is today

Fifty-one icons on a 64×64 grid, drawn as hand-written SVG paths. The paths live
in Python: `tools/glyphs_1.py` and `tools/glyphs_2.py` hold one spec per project —
a slug, a name, a sentence describing the project, an accent, a list of
silhouette parts and a list of white details — and `tools/svgkit.py` turns a spec
into a document, with the palette, the shading helpers and the primitives a
drawing is composed from.

`tools/build.py` validates the set, then writes everything: the SVGs, seven PNG
exports per icon (16, 32, 48, 64, 128, 256, 512 — Inkscape, one process per
file, because parallel Inkscape processes abort), `icons.json`, `index.html`,
`preview.png` and `README.md`. The manifest carries the slug, name, purpose,
accent name, hex colour, the SVG path and a map of the seven PNG paths.

The validation is the part worth protecting. Before anything is written,
`check()` refuses: an accent that is not in the palette, a spec with no
silhouette, a missing name or description, and — the strict one — two icons whose
signature is identical, where the signature is the tuple of part paths, tones and
transforms plus the details.

Five decisions constrain what comes next.

- **A drawing is data, not a file.** Nothing in `svg/` is edited by hand; it is
  derived, and a hand edit would be erased by the next build. That is what makes
  a validator possible at all.
- **One accent per icon.** The silhouette is a single colour, shaded only by
  light: `main` for the body, `light` and `pale` on the top face, `dark` and
  `deep` in the recesses. The fifty-two named accents were sampled from the Tela
  icons installed on the machine that drew the set.
- **White carries the meaning.** Lettering, arrows, seams, holes and highlights
  are cut in paper-white, so an icon reads against any wallpaper.
- **Objects, not tiles.** No background plate, no squircle, no badge behind the
  drawing; the desktop arranges itself around the object.
- **Tela is lineage, not source.** The palette and the drawing discipline travel;
  no Tela file is copied or modified, which is what lets this set be MIT while
  Tela stays GPL-3.0.

What the repository does not have is equally load-bearing. There is no CI
workflow, so the validation runs only when somebody rebuilds. `icons.json` is
written and read by nobody in the repository. There is no freedesktop theme — no
`index.theme`, no `scalable/` directory, no icon-name mapping — so the icons
ship as a gallery and a manifest rather than as something a desktop can install.
There are no symbolic or dark variants, no favicon or Open Graph card, and no
test that a 16-pixel export is still legible; the PNGs are Inkscape scalings of
the same drawing.

## The vision

1. **The set is installable.** A generated freedesktop icon theme beside the
   gallery: `index.theme`, a `scalable/` tree, the per-application names and
   symlinks that make a launcher find its icon, and an `icon-theme.cache`. The
   measure is that a desktop can select this theme, not that a browser can view
   it.
2. **The manifest is a contract other projects consume.** A page, an Emacs
   package and an asset host should be able to ask for an icon by project name
   and receive a path, a size and an accent, from `icons.json` and nothing else.
   That means the manifest needs a version, a digest per file and a stated
   licence, and somebody outside this repository has to read it.
3. **Legibility at 16 pixels is asserted, not hoped for.** Small sizes are a
   different drawing problem: an optical size step, hinted details, and a test
   that measures contrast and feature coverage in the exported small PNG rather
   than trusting the 512. A build that cannot state its 16-pixel result is a
   build that ships a smudge.
4. **Every artefact an ecosystem needs comes from the same spec**: favicons, an
   Open Graph card per project, a badge-sized variant, a symbolic single-colour
   set for panels, and `.ico` and `.icns` for the desktop and macOS sides. One
   drawing, many renderings, no second source of truth.
5. **The uniqueness rule grows into a grammar.** Today two identical drawings are
   refused by comparing signatures. The stronger invariant is that every icon is
   composed from a shared vocabulary — disc, folder, terminal, gear, envelope,
   shield — with each drawing declaring which primitives it uses, so a new icon
   is a composition, and "distinct" is a property the build can reason about
   rather than a string it compares.

## Features that are in scope and not built yet

- **A theme install.** The repository's own rules imply it: an icon set that
  cannot be installed is a gallery. The hard part is naming — a freedesktop
  theme needs application names that match desktop entries, and half these
  projects have no `.desktop` file to match.
- **A build that runs in CI.** `check()` is a validation and a rebuild
  difference is a test. The hard part is the dependency on Inkscape and Pillow:
  a reproducible container or a Guix profile has to be pinned, or the CI job
  proves only that somebody's laptop can draw.
- **A consumer for `icons.json`.** Written today, read nowhere. The hard part is
  agreeing the shape with the first consumer — the static asset host, a badge
  generator, or an Emacs package that shows a project's icon in a completion
  buffer.
- **Symbolic and dark variants.** Implied by the Tela lineage, which ships dark
  folders, and by Adwaita's symbolic set. The hard part is that a symbolic icon
  is not a recolour: it is a single-colour simplification, so it is a second
  drawing per project, and the vocabulary in the vision above is how that stays
  affordable.
- **Favicons and cards.** Every site in the collection wants a favicon and a link
  preview. The hard part is composition — a card is the icon plus type plus a
  colour, and type means the ecosystem's own faces, not a font the build happens
  to have.

## New features that would be worth having

- **`tools/build.py --only SLUG` and a content-addressed skip**: render the icons
  whose spec or palette changed, and nothing else, with the SVG's own content
  deciding. The single largest quality-of-life change in the repository.
- **A glyph budget per icon**: a count of parts and details, printed by the check,
  so the catalogue cannot creep from "a spider on a web" to a scene.
- **A contrast check against both wallpapers**: every accent against a light and
  a dark desktop surface, reported as a table, so a new accent is choosable
  rather than arguable.
- **A rendered README table that shows 32-pixel icons** as well as 64, because
  the size a project's icon is actually seen at is the one nobody inspects.
- **A `skeu`-style variant family**: the same drawing with a painted highlight and
  a deeper shadow, for the sibling theme that exists in this collection.
- **A digest-pinned manifest for the asset host**, so a page can reference an
  icon by content and cache it forever.
- **A gallery that filters by accent and by size, and that renders each icon at
  its true size beside a magnified one**, which is how a reader judges it.

## Contributions that would move the needle

1. **An incremental build.** Small diff, immediate payoff, and it is what makes
   the rest of this document cheap to do: nobody iterates on a drawing when a
   one-line change costs a full rebuild.
2. **A CI workflow that runs `check()` and fails if a rebuild changes the tree.**
   Two jobs in one file, and it turns the validator from a habit into a gate —
   including the case where a spec is edited and the artefacts are not.
3. **`index.theme` and a generated `scalable/` tree.** One template, one loop,
   and the set becomes installable; the naming question can be answered by
   shipping a mapping file that says which projects have a desktop entry.
4. **A manifest schema with digests and licences**, plus a `maak verify` that
   every file in `png/` and `svg/` appears in it. The first step to a consumer
   outside this repository.
5. **The 16-pixel legibility check**, as a small assertion over the exported PNGs
   rather than a design review.
6. **Favicons**, generated from the same spec, published through the asset host.
7. **A symbolic variant for the ten icons whose projects have a desktop
   presence**, since those are the ones a panel shows.

## Compared to related projects

| Project | What it is | Where project-icons differs |
| --- | --- | --- |
| Tela icon theme | A large freedesktop theme of flat, object-like app and folder icons, in light and dark variants | The inspiration and the palette's source; Tela is installable, has thousands of files and variants, and is GPL-3.0 — this set is 51 drawings, one accent each, MIT, with a build that refuses duplicates |
| Papirus | A very large icon theme, hand-tuned per size, with symlinks for hundreds of applications | The lesson is per-size hinting and application mapping, both of which this set lacks; Papirus is a theme, this is a catalogue with a gallery |
| Numix | Flat icons on circular or square plates | The opposite rule: Numix frames the object, this set refuses the plate |
| Adwaita | GNOME's default theme, with a full-colour set and a symbolic one for panels | Symbolic variants and dark variants are what this set has not begun; Adwaita is a desktop's default rather than a collection's identity |
| Simple Icons | A large set of single-colour brand marks, with a JS package and per-brand SVGs | Trademarks and brand marks, monochrome by construction; this set draws objects nobody owns, and its constraint is uniqueness rather than fidelity to a logo |
| GGG | The ecosystem's own glyph generator: SVG logos and status badges written from Lisp | GGG makes generic marks and badges for pages; this set makes one identity per project, and the two meet at the badge-shaped asset a project embeds |
| Skeu Icons | A sibling theme in this collection: painted objects in thirty variants | Variants are its whole idea; this set is one icon per project, which is the constraint that makes every drawing an argument |

The others do four things this set should add: installability (Tela, Papirus,
Adwaita), symbolic and dark variants (Adwaita, Tela), per-size optical
correction (Papirus), and a machine-readable distribution that other software
consumes (Simple Icons' package).

Where project-icons is ahead, and should stay ahead: the drawing is data and the
validator enforces it, so uniqueness is a build error rather than a review note;
the palette was measured from an existing theme instead of invented, which is why
the set sits beside Tela without an argument; the manifest is emitted by the build
alongside the images rather than maintained by hand; and the README, the gallery
and the contact sheet are all generated, so none of them can drift from the
specs. Those four are cheap to keep and hard to reconstruct, and a proposal to
hand-edit an SVG or to add a colour outside the table should be read as a
proposal to give one up.

## In the long run

- **Identity, not decoration.** The durable asset is the mapping from project to
  object and colour: it is what a site, a badge, a favicon and a launcher all
  read, and it should outlive any one rendering.
- **A spec vocabulary small enough to learn.** If a hundredth icon costs the same
  as the fifth, the set can grow with the collection instead of lagging behind
  it.
- **Artefacts generated, never curated.** Every new format a platform asks for
  is a renderer over the same specs, because a second source of truth for an
  identity becomes a second identity.
- **A published manifest with digests**, so the icons can be served from an asset
  host or vendored into another repository without a copy drifting.
- **Legibility as a measurement**, at the sizes people actually see, on the
  wallpapers people actually use.

## Closing

The order that follows: an incremental build, then a gate in CI, then a theme a
desktop can install, then a manifest somebody else reads. Each is small, and
each makes the next cheaper. The drawing rules themselves should move least — the
palette and the object-not-tile decision are the identity of the set.

*This document describes intent, not commitments.*
