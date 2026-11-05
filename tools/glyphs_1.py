"""Glyphs, part one: the Guile, CI and icon-tooling projects.

Each icon is an object: a filled silhouette (one or more parts, shaded by the
canvas) plus white detail, exactly as Tela draws a folder or a terminal.
"""

from svgkit import (FG, DARK, ACCENTS, darken, P, C, E, R, L, PL, G, part,
                    disc, ell, rrect, poly_d, cog, cog_parts)

ICONS = {}


def icon(slug, name, what, accent, parts, details):
    ICONS[slug] = dict(name=name, what=what, accent=accent, parts=parts,
                       details=details)


def deep(accent, amount=0.12):
    return darken(ACCENTS[accent], amount)


# 1. A spider on its web: a crawler that walks a site.
icon("araneola", "Araneola",
     "High-performance web crawler and sitemap generator, pure Guile Scheme",
     "violet",
     [part(ell(38, 37, 8.4, 10.4)),
      part(disc(38, 23, 6.6))],
     G(
         P("M8 30A22 22 0 0 1 30 8", stroke=deep("violet"), sw=2.6, opacity=.6),
         P("M8 21A13 13 0 0 1 21 8", stroke=deep("violet"), sw=2.6, opacity=.6),
         L(8, 8, 26, 26, sw=2.2, color=deep("violet"), opacity=.45),
         L(8, 8, 30, 17, sw=2.2, color=deep("violet"), opacity=.45),
         L(8, 8, 17, 30, sw=2.2, color=deep("violet"), opacity=.45),
         L(38, 16, 38, 8, sw=1.8, color=deep("violet"), opacity=.65),
         P("M31 33 23 26M30 38 20 36M31 42 22 48", stroke=deep("violet"),
           sw=3.6),
         P("M45 33 53 26M46 38 56 36M45 42 54 48", stroke=deep("violet"),
           sw=3.6),
         C(34.6, 22, 1.6, fill=FG, opacity=.9),
         C(41.4, 22, 1.6, fill=FG, opacity=.9),
     ))

# 2. A shield with a keyhole and a double rim: guarding and double encryption.
icon("bewaking", "Bewaking",
     "Encryption, authentication and authorization toolkit for Guile",
     "indigo",
     [part("M32 3 56 12v18c0 15.6-10.4 25.8-24 31C18.4 55.8 8 45.6 8 30V12z")],
     G(
         P("M32 8 51 15v15c0 12.6-8.2 21-19 25.4", stroke=FG, sw=1.8,
           opacity=.35),
         C(32, 28, 6, fill=FG),
         P("M29.4 32h5.2l1.6 10h-8.4z", fill=FG),
     ))

# 3. A gear with a play triangle: build stages that run.
icon("byggsteg", "byggsteg",
     "Readable CI/CD orchestrator: pipelines as Lisp, streamed live",
     "clover",
     cog_parts(32, 32, 20, teeth=8),
     G(
         PL("25,22 41,32 25,42", fill=FG),
     ))

# 4. A dark disc with a git branch and an arrow: Actions bridging into byggsteg.
icon("byggsteg-github", "Byggsteg GitHub",
     "GitHub Actions workflow and action bridging into byggsteg jobs",
     "ink",
     [part(disc(32, 32, 29))],
     G(
         C(19, 20, 4.6, fill=FG),
         C(19, 44, 4.6, fill=FG),
         C(34, 32, 4.6, fill=FG),
         L(19, 24.6, 19, 39.4, sw=4, color=FG),
         P("M34 27.4c0-4.8-6-6.8-10.6-7.4", stroke=FG, sw=4),
         P("M41 44h10M46 39.4l4.6 4.6-4.6 4.6", stroke=FG, sw=3.4),
     ))

# 5. A woodpecker on a trunk: the bridge that hammers away at a job.
icon("byggsteg-woodpecker", "Byggsteg Woodpecker",
     "Woodpecker CI image that runs byggsteg jobs and reports the outcome",
     "ember",
     [part(rrect(48, 5, 11, 50, 5.5), "deep"),
      part(ell(27, 37, 15, 11.5), "main", "rotate(-16 27 37)"),
      part(disc(37, 24, 8.4)),
      part(poly_d([(17, 41), (6, 49), (22, 48)]))],
     G(
         PL("43,20 52,24.5 43,29", fill=FG),
         C(38.6, 21, 1.8, fill=DARK, opacity=.55),
         P("M22 34c6 1.6 10 5.4 11.6 10", stroke=FG, sw=2.4, opacity=.7),
         L(31, 47, 41, 49, sw=2.6),
         L(27, 50, 35, 53, sw=2.6),
         C(52.5, 14, 2.8, fill=DARK, opacity=.45),
     ))

# 6. A slide chute curling into the pool: the water park site.
icon("carvoeiro-water-fun", "Carvoeiro Water Fun",
     "Static site for the water fun park in Carvoeiro, Algarve",
     "sky",
     [part(disc(32, 32, 29)),
      part(disc(32, 32, 12.4), "deep")],
     G(
         R(28.4, 3, 7.2, 17, rx=1.2, fill=FG, transform="rotate(45 32 32)"),
         R(28.4, 3, 7.2, 17, rx=1.2, fill=FG, transform="rotate(135 32 32)"),
         R(28.4, 3, 7.2, 17, rx=1.2, fill=FG, transform="rotate(225 32 32)"),
         R(28.4, 3, 7.2, 17, rx=1.2, fill=FG, transform="rotate(315 32 32)"),
         P("M48 10c3 5 4 7.4 4 9.2a4 4 0 1 1-8 0c0-1.8 1-4.2 4-9.2z",
           fill=FG, opacity=.85),
     ))

# 7. A cask with a cons pair on its belly: Homebrew casks, Lisp pairs.
icon("cask-and-cons", "Cask & Cons",
     "Declarative macOS dotfiles in Scheme, driven by the caco CLI",
     "cocoa",
     [part("M12 16c0-4 2.4-6 6.4-6h27.2c4 0 6.4 2 6.4 6v5"
           "c4 5.6 4 12.4 0 18 4 5.6 4 12.4 0 18v1c0 4-2.4 6-6.4 6H18.4"
           "c-4 0-6.4-2-6.4-6v-1c-4-5.6-4-12.4 0-18-4-5.6-4-12.4 0-18z"),
      part(ell(32, 12, 20, 5.6), "light"),
      part(rrect(9, 20, 46, 4.4, 2.2), "deep"),
      part(rrect(9, 45, 46, 4.4, 2.2), "deep")],
     G(
         P("M26 45 33 25M31 34 39 45", stroke=FG, sw=3.8),
     ))

# 8. A sealed envelope with a wax seal: secrets concealed.
icon("consceal", "Consceal",
     "Declarative secret management and deployment in Guile Scheme",
     "plum",
     [part(rrect(3, 12, 58, 40, 5)),
      part("M3 17 32 39 61 17v-1a4 4 0 0 0-4-4H7a4 4 0 0 0-4 4z", "light")],
     G(
         C(32, 35, 9.6, fill=FG),
         C(32, 33.4, 2.8, fill=DARK, opacity=.75),
         P("M30.2 35.4h3.6l1.2 5h-6z", fill=DARK, opacity=.75),
     ))

# 9. A painter's palette: collected digital art.
icon("digital-art-dreams", "Digital Art Dreams",
     "Archive of collected digital artwork, released under CC0",
     "pink",
     [part("M32 4c16 0 28 10.4 28 23.4 0 8.4-5.6 12.6-12 12.6-5.4 0-8.4 2-8.4 6"
           " 0 5.4-4.4 8.4-9.6 8.4C16 54.4 4 43.4 4 28.4 4 14 17 4 32 4z"),
      part(ell(39, 44, 6.4, 5), "deep")],
     G(
         C(19, 19, 4.6, fill=FG),
         C(32, 14, 4.6, fill=FG),
         C(45, 20, 4.6, fill=FG),
         C(16, 33, 4.6, fill=FG),
         P("M44 47 55 36", stroke=FG, sw=4.6),
         PL("54,32 59,38 53,40 49,36", fill=FG),
     ))

# 10. A cloche with a lambda on the dome: your DSL, served à la carte.
icon("free-alacarte", "Free à la Carte",
     "Free monads and composable functors for embedded DSLs in Haskell",
     "teal",
     [part("M7 46a25 25 0 0 1 50 0z"),
      part(rrect(3, 46, 58, 8, 4), "light"),
      part(disc(32, 19, 4.4), "light")],
     G(
         P("M24 43 31 27M29 33 37 43", stroke=FG, sw=3.8),
     ))

# 11. A badge ribbon with a "g" and a spark: glyphs and badges generated.
icon("ggg", "GGG",
     "Guile Glyph Generator: SVG logos and status badges from Lisp",
     "green",
     [part("M8 14h34l11 13-11 13H8a4 4 0 0 1-4-4V18a4 4 0 0 1 4-4z")],
     G(
         C(26, 24.5, 5.4, fill="none", stroke=FG, sw=3),
         P("M31.4 19.4v12c0 3.4-2.4 5-5.2 5", stroke=FG, sw=3),
         P("M49 24l1.8 4.4 4.4 1.8-4.4 1.8L49 36.4l-1.8-4.4-4.4-1.8 4.4-1.8z",
           fill=FG, opacity=.9),
         P("M20 38l1.3 3.1 3.1 1.3-3.1 1.3L20 47l-1.3-3.1-3.1-1.3 3.1-1.3z",
           fill=FG, opacity=.7),
     ))

# 12. A spec document yielding a lambda: OpenAPI in, Guile out.
icon("guile-openapi-generator", "Guile OpenAPI Generator",
     "Generates idiomatic Guile server and client code from an OpenAPI 3 spec",
     "amber",
     [part("M10 8a4 4 0 0 1 4-4h25l13 13v39a4 4 0 0 1-4 4H14a4 4 0 0 1-4-4z"),
      part(poly_d([(39, 4), (52, 17), (43, 17), (39, 13)]), "light")],
     G(
         P("M17 24h18M17 31h18M17 38h9", stroke=FG, sw=2.8, opacity=.85),
         P("M24 51l-4 4 4 4", stroke=FG, sw=2.6, opacity=.7),
         P("M31 58h9", stroke=FG, sw=2.6, opacity=.7),
         P("M36 34 42 22M39.6 27.4 47 38", stroke=FG, sw=3.4),
     ))

# 13. A sealed parcel with a lambda: the signed Guix package channel.
icon("guix-jointhefreeworld", "guix-jointhefreeworld",
     "GNU Guix channel packaging the whole jointhefreeworld collection",
     "guix",
     [part(poly_d([(32, 4), (59, 16), (32, 28), (5, 16)]), "light"),
      part("M5 16v29l27 13V28z"),
      part("M59 16v29L32 58V28z", "dark")],
     G(
         P("M14 30 19 20M17 24 23 32", stroke=FG, sw=2.8),
         C(44, 34, 1.8, fill=FG, opacity=.55),
         C(44, 40, 1.8, fill=FG, opacity=.4),
         C(44, 46, 1.8, fill=FG, opacity=.28),
         P("M12 16 32 25l20-9", stroke=FG, sw=1.6, opacity=.25),
     ))

# 14. A terminal under a witch's hat: the witch's Bash configuration.
icon("heks-bash", "Heks BASH",
     "Declarative Bash configuration and prompt, generated from Scheme",
     "forest",
     [part(poly_d([(32, 1), (44, 17), (20, 17)]), "light"),
      part(rrect(14, 15, 36, 6, 3), "deep"),
      part(rrect(3, 22, 58, 38, 5)),
      part(rrect(3, 22, 58, 9, 5), "dark")],
     G(
         L(24, 12, 40, 12, sw=2.8, color=FG, opacity=.85),
         P("M12 36l7 5-7 5", stroke=FG, sw=3.4),
         L(24, 46, 38, 46, sw=3.4, color=FG),
         L(48, 46, 52, 46, sw=3.4, color=FG, opacity=.5),
     ))

# 15. A disc holding parentheses and a lambda: the witch's Emacs temple.
icon("heks-emacs", "heks-emacs",
     "Modular, reproducible Emacs configuration built with Elpaca",
     "mauve",
     [part(disc(32, 32, 29))],
     G(
         P("M23 12c-6.4 5-6.4 35 0 40", stroke=FG, sw=3.6),
         P("M41 12c6.4 5 6.4 35 0 40", stroke=FG, sw=3.6),
         P("M27 44 33 25M31 32l6 12", stroke=DARK, sw=3.6),
     ))

# 16. A monitor showing a cog and a lambda: a programmable GNU/Linux system.
icon("heks-linux", "Heks GNU/Linux",
     "Modular, programmable GNU/Linux desktop written as Scheme modules",
     "navy",
     [part(rrect(3, 5, 58, 36, 5)),
      part(rrect(7, 9, 50, 28, 3), "dark"),
      part(rrect(28, 41, 8, 9, 2), "light"),
      part(rrect(17, 49, 30, 7, 3.5), "light")],
     G(
         cog(21, 23, 8.4, fill=FG, hole=DARK),
         P("M35 33 42 14M39.6 22 47 33", stroke=FG, sw=3.6),
     ))

# 17. A key cap beside a palette: keys, wallpapers and colours.
icon("heks-toon", "heks-toon",
     "GTK4 window showing the desktop's keybindings, wallpapers and palettes",
     "rose",
     [part(rrect(3, 7, 36, 36, 7)),
      part("M7 40h28l-4 13H11z", "light"),
      part(disc(45, 43, 15), "dark")],
     G(
         L(14, 16, 14, 33, sw=3.4, color=FG),
         L(14, 24.5, 23, 16, sw=3, color=FG),
         L(14, 24.5, 23, 33, sw=3, color=FG),
         C(39, 37, 2.6, fill=FG, opacity=.85),
         C(47, 34, 2.6, fill=FG, opacity=.85),
         C(51, 42, 2.6, fill=FG, opacity=.85),
         C(44, 47, 2.4, fill=FG, opacity=.7),
     ))

# 18. A browser window: an S-expression on the left, rendered UI on the right.
icon("hygguile", "Hygguile",
     "Cozy, accessible server-rendered UI framework: SXML in, HTML out",
     "sage",
     [part(rrect(3, 8, 58, 48, 5)),
      part(rrect(3, 8, 58, 11, 5), "light"),
      part(rrect(33, 25, 24, 25, 3), "pale")],
     G(
         C(9.5, 13.5, 1.8, fill=DARK, opacity=.45),
         C(15, 13.5, 1.8, fill=DARK, opacity=.45),
         P("M22 26c-4 3.4-4 12.6 0 16", stroke=FG, sw=2.8),
         P("M30 26c4 3.4 4 12.6 0 16", stroke=FG, sw=2.8),
         C(26, 34, 1.8, fill=FG),
         R(37, 29, 16, 4.4, rx=2, fill=DARK, opacity=.3),
         L(37, 38, 53, 38, sw=2, color=DARK, opacity=.25),
         L(37, 43, 47, 43, sw=2, color=DARK, opacity=.25),
     ))

# 19. An app container becoming a grid of icons: icns to freedesktop theme.
icon("icns2linux", "icns2linux",
     "Turns macOS .icns trees into a reproducible freedesktop icon theme",
     "blue",
     [part(rrect(2, 13, 29, 29, 9)),
      part(poly_d([(30, 26), (35, 26), (35, 21), (41, 32), (35, 43),
                   (35, 38), (30, 38)]), "deep"),
      part(rrect(43, 12, 7, 7, 2), "light"),
      part(rrect(51, 12, 7, 7, 2)),
      part(rrect(43, 21, 7, 7, 2)),
      part(rrect(51, 21, 7, 7, 2), "light"),
      part(rrect(43, 30, 7, 7, 2), "light"),
      part(rrect(51, 30, 7, 7, 2), "dark"),
      part(rrect(43, 39, 7, 7, 2), "dark"),
      part(rrect(51, 39, 7, 7, 2), "light")],
     G(
         R(8, 19, 17, 17, rx=5, fill=FG),
     ))

# 20. A CV page with a portrait and a road: the journey of a life.
icon("iter-vitae", "Iter Vitae",
     "Multi-language CV generator: one Scheme file to HTML and plain text",
     "bronze",
     [part("M10 8a4 4 0 0 1 4-4h26l14 14v38a4 4 0 0 1-4 4H14a4 4 0 0 1-4-4z"),
      part(poly_d([(40, 4), (54, 18), (44, 18), (40, 14)]), "light")],
     G(
         C(24, 24, 7.6, fill=FG),
         L(35, 21, 47, 21, sw=2.8, color=FG, opacity=.8),
         L(35, 28, 47, 28, sw=2.8, color=FG, opacity=.8),
         P("M19 50c8-4 6-12 13-12s5 8 12 5", stroke=FG, sw=2.6, opacity=.85),
         C(19, 50, 2.4, fill=FG),
         C(44, 43, 2.4, fill=FG),
     ))

# 21. A globe with a star: joining the free world.
icon("jointhefreeworld", "jointhefreeworld",
     "Personal homepage, blog and movement site built from Org with Emacs",
     "royal",
     [part(disc(32, 32, 29))],
     G(
         P("M32 3c10.4 7.6 10.4 50.4 0 58", stroke=FG, sw=2.2, opacity=.55),
         P("M32 3c-10.4 7.6-10.4 50.4 0 58", stroke=FG, sw=2.2, opacity=.55),
         L(3.4, 32, 60.6, 32, sw=2.2, opacity=.55),
         P("M6 22c12 4.4 40 4.4 52 0", stroke=FG, sw=2, opacity=.4),
         P("M6 42c12-4.4 40-4.4 52 0", stroke=FG, sw=2, opacity=.4),
         P("M44 10l2 4.8 4.8 2-4.8 2-2 4.8-2-4.8-4.8-2 4.8-2z", fill=FG),
     ))

# 22. A lightning bolt between braces: power and reliable helper tools.
icon("kracht", "kracht",
     "Batteries-included utility library for Guile Scheme programming",
     "yellow",
     [part(poly_d([(35, 4), (18, 35), (26, 35), (28, 58), (46, 27),
                   (36, 27)]))],
     G(
         P("M14 12c-4 0-5.4 2-5.4 5.4v5.2c0 3-1.4 4.4-3.6 4.8"
           " 2.2.4 3.6 1.8 3.6 4.8v5.2c0 3.4 1.4 5.4 5.4 5.4",
           stroke=DARK, sw=2.8, opacity=.85),
         P("M50 12c4 0 5.4 2 5.4 5.4v5.2c0 3 1.4 4.4 3.6 4.8"
           " -2.2.4-3.6 1.8-3.6 4.8v5.2c0 3.4-1.4 5.4-5.4 5.4",
           stroke=DARK, sw=2.8, opacity=.85),
     ))

# 23. A dock strip with a lambda in it: a dock you reprogram while it runs.
icon("lambdock", "lambdock",
     "Wayland dock in C and GTK4, with a live Guile Scheme brain",
     "grey",
     [part(rrect(2, 34, 60, 24, 12)),
      part(rrect(7, 40, 12, 12, 3.5), "deep"),
      part(rrect(22, 40, 12, 12, 3.5), "deep"),
      part(rrect(37, 40, 12, 12, 3.5), "light"),
      part(disc(52, 24, 7), "light")],
     G(
         P("M40 49 45 39M42.6 43.6 47.6 49", stroke=FG, sw=2.8),
         C(52, 24, 2.6, fill=FG, opacity=.85),
     ))

# 24. A jar of collected bookmarks: links kept as one Scheme file.
icon("lenkesamler", "Lenkesamler",
     "Bookmark manager and archive that exports HTML, Markdown, Org and XBEL",
     "sea",
     [part(rrect(13, 15, 38, 44, 9)),
      part(rrect(9, 6, 46, 12, 5), "light"),
      part(rrect(13, 15, 38, 10, 5), "dark")],
     G(
         P("M21 27h10v17l-5-4.2-5 4.2z", fill=FG),
         P("M35 27h10v17l-5-4.2-5 4.2z", fill=FG, opacity=.65),
         L(18, 36, 18, 50, sw=2.4, color=FG, opacity=.3),
     ))

# 25. Three kanban columns at different depths: a priority-ordered plan.
icon("lucidplan", "LucidPlan",
     "Free project management: multi-project workspace with kanban boards",
     "lucid",
     [part(rrect(4, 8, 17, 46, 4)),
      part(rrect(23, 8, 17, 33, 4), "light"),
      part(rrect(42, 8, 17, 40, 4), "dark")],
     G(
         R(7, 12, 11, 8, rx=2.4, fill=FG),
         R(26, 12, 11, 8, rx=2.4, fill=FG),
         R(45, 12, 11, 8, rx=2.4, fill=FG),
         R(7, 24, 11, 8, rx=2.4, fill=FG, opacity=.6),
         R(26, 24, 11, 8, rx=2.4, fill=FG, opacity=.6),
         P("M48 26l2.6 3.4 5.4-6.4", stroke=FG, sw=2.6, opacity=.85),
     ))
