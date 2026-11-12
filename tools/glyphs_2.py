"""Glyphs, part two: the applications, Emacs packages and web projects.

Same rule as part one: each icon is an object silhouette shaded by the canvas,
with white detail on top.
"""

import math

from svgkit import (FG, DARK, ACCENTS, darken, P, C, E, R, L, PL, G, part,
                    disc, ell, rrect, poly_d)

ICONS = {}


def icon(slug, name, what, accent, parts, details):
    ICONS[slug] = dict(name=name, what=what, accent=accent, parts=parts,
                       details=details)


def deep(accent, amount=0.12):
    return darken(ACCENTS[accent], amount)


def star(cx, cy, outer, inner, points=8, rotate=0):
    pts = []
    for i in range(points * 2):
        radius = outer if i % 2 == 0 else inner
        angle = math.radians(rotate + i * 180 / points - 90)
        pts.append((round(cx + radius * math.cos(angle), 2),
                    round(cy + radius * math.sin(angle), 2)))
    return poly_d(pts)


# 26. A terminal with a hammer over its corner: tasks as Scheme, built hard.
icon("maak", "maak",
     "Infinitely extensible command runner and project automator in Scheme",
     "brandorange",
     [part(rrect(2, 22, 60, 38, 5)),
      part(rrect(2, 22, 60, 9, 5), "dark"),
      part(rrect(40, 8, 8, 24, 3.5), "light", "rotate(26 46 14)"),
      part(rrect(30, 2, 32, 11, 2.5), "deep", "rotate(26 46 14)")],
     G(
         P("M12 38 20 44 12 50", stroke=FG, sw=3.4),
         L(28, 50, 44, 50, sw=3.4, color=FG),
         L(48, 46, 52, 46, sw=2.6, color=FG, opacity=.5),
     ))

# 27. A disc holding parentheses and a hammer: maak inside Emacs.
icon("maak.el", "maak.el",
     "Emacs integration for maak: discover, inspect and run tasks from Emacs",
     "purple",
     [part(disc(32, 32, 29))],
     G(
         P("M22 12c-6.2 5-6.2 35 0 40", stroke=FG, sw=3.4),
         P("M42 12c6.2 5 6.2 35 0 40", stroke=FG, sw=3.4),
         R(26, 20, 21, 7.4, rx=2, fill=FG, transform="rotate(22 36 24)"),
         P("M35 27 28 45", stroke=FG, sw=3.6),
     ))

# 28. A buffer above a lit mode line: the bar at the bottom of an Emacs frame.
icon("modusregel", "modusregel",
     "Clean, fast, tree-sitter aware Emacs mode line",
     "azure",
     [part(rrect(4, 5, 56, 31, 4), "dark"),
      part(rrect(2, 37, 60, 19, 6))],
     G(
         L(10, 14, 54, 14, sw=2.4, color=FG, opacity=.45),
         L(10, 20, 46, 20, sw=2.4, color=FG, opacity=.35),
         L(10, 26, 50, 26, sw=2.4, color=FG, opacity=.25),
         R(8, 43, 16, 7, rx=3, fill=FG),
         R(28, 43, 9, 7, rx=3, fill=FG, opacity=.7),
         C(52, 46.5, 3, fill=FG, opacity=.85),
     ))

# 29. A database cylinder with an up arrow: migrations moving forward.
icon("mutastructura", "Mutastructura",
     "Checksummed SQL migrations for SQLite, PostgreSQL, CockroachDB and MySQL",
     "deepgreen",
     [part("M6 12v32c0 5.6 11.6 10 26 10s26-4.4 26-10V12z"),
      part(ell(32, 12, 26, 7), "light")],
     G(
         P("M6 26c0 5.6 11.6 10 26 10s26-4.4 26-10", stroke=FG, sw=2.2,
           opacity=.35),
         P("M6 38c0 5.6 11.6 10 26 10s26-4.4 26-10", stroke=FG, sw=2.2,
           opacity=.2),
         P("M47 40V24M41.8 29.2 47 24l5.2 5.2", stroke=FG, sw=3.4),
     ))

# 30. A parcel carrying a snowflake: everything packaged for Nix.
icon("nix-jointhefreeworld", "nix-jointhefreeworld",
     "Nix flake carrying the whole jointhefreeworld package collection",
     "nix",
     [part(rrect(6, 22, 52, 36, 4)),
      part(rrect(6, 14, 52, 10, 4), "light")],
     G(
         L(32, 26, 32, 52, sw=3),
         L(21.6, 31, 42.4, 47, sw=3),
         L(42.4, 31, 21.6, 47, sw=3),
         C(32, 39, 3, fill=FG),
         L(12, 52, 22, 52, sw=2.4, color=FG, opacity=.45),
         L(42, 52, 52, 52, sw=2.4, color=FG, opacity=.45),
     ))

# 31. An olive sprig between braces: a CSS framework grown from Lisp.
icon("olive-css", "Olive CSS",
     "Utility-first vanilla CSS framework generated with Scheme",
     "olive",
     [part(ell(32, 30, 4.4, 15)),
      part(ell(22, 18, 10.4, 5), "light", "rotate(-38 22 18)"),
      part(ell(42, 24, 10.4, 5), "main", "rotate(38 42 24)"),
      part(ell(21, 33, 10.4, 5), "main", "rotate(-38 21 33)"),
      part(ell(39, 40, 9.4, 4.6), "light", "rotate(38 39 40)"),
      part(disc(32, 49, 8.6), "deep")],
     G(
         P("M10 12c-3.6 0-4.8 2-4.8 5.2v5c0 3.2-1.4 4.6-4 5"
           " 2.6.4 4 1.8 4 5v5c0 3.2 1.2 5.2 4.8 5.2",
           stroke=DARK, sw=2.6, opacity=.8),
         P("M54 12c3.6 0 4.8 2 4.8 5.2v5c0 3.2 1.4 4.6 4 5"
           " -2.6.4-4 1.8-4 5v5c0 3.2-1.2 5.2-4.8 5.2",
           stroke=DARK, sw=2.6, opacity=.8),
     ))

# 32. A flask holding an Org asterisk: Org-mode transmuted by a grammar.
icon("orgwebalchemy", "OrgWebAlchemy",
     "Guile library that parses Org-mode with PEG and renders HTML, Markdown or SXML",
     "purple2",
     [part("M25 4h14v15l11 26c1.6 3.8-1.2 8-5.4 8H19.4"
           "c-4.2 0-7-4.2-5.4-8L25 19z")],
     G(
         L(17, 41, 47, 41, sw=2.6, color=FG, opacity=.55),
         P("M32 43v13M26 46.4l12 6.4M38 46.4l-12 6.4", stroke=FG, sw=2.6),
         C(23, 48, 2.2, fill=FG, opacity=.6),
         C(41, 45, 1.8, fill=FG, opacity=.45),
     ))

# 33. A winged envelope broadcasting: the notification nexus.
icon("pingwing", "PingWing",
     "Lisp-powered notification nexus: HTTP in, queued and retried SMTP out",
     "red",
     [part(rrect(4, 18, 56, 38, 5)),
      part("M8 26C2 23 1 13 6 8c7 2 11 7 12 14z", "light")],
     G(
         P("M4 21 32 42 60 21", stroke=FG, sw=2.6, opacity=.5),
         P("M50 12a9 9 0 0 1 0 13", stroke=deep("red"), sw=2.6),
         P("M56 8a16 16 0 0 1 0 21", stroke=deep("red"), sw=2.6,
           opacity=.7),
     ))

# 34. A locked notebook with rings: notes that stay private.
icon("private-notes", "private-notes",
     "Personal knowledge vault: diary, contacts, career and engineering notes",
     "charcoal",
     [part(rrect(7, 3, 50, 58, 5)),
      part(rrect(7, 3, 13, 58, 5), "dark"),
      part(rrect(2, 12, 14, 5, 2.5), "light"),
      part(rrect(2, 24, 14, 5, 2.5), "light"),
      part(rrect(2, 36, 14, 5, 2.5), "light"),
      part(rrect(2, 48, 14, 5, 2.5), "light")],
     G(
         P("M35 34a6 6 0 0 1 12 0", stroke=FG, sw=2.6),
         R(30.6, 33.4, 20.8, 13, rx=2.4, fill=FG),
         C(41, 39.4, 2.4, fill=DARK, opacity=.7),
         L(28, 17, 46, 17, sw=2.4, color=FG, opacity=.55),
         L(28, 24, 40, 24, sw=2.4, color=FG, opacity=.4),
     ))

# 35. A quill over its log lines: structured logging.
icon("scriba", "Scriba",
     "Structured, levelled, taggable logging for GNU Guile",
     "oak",
     [part("M59 2C36 6 16 23 7 53c16 5 33-5 42-19 5-9 9-19 10-32z")],
     G(
         P("M11 51 48 14", stroke=FG, sw=2.6, opacity=.9),
         P("M20 32c5-2 10-7 13-12", stroke=DARK, sw=1.8, opacity=.25),
         P("M9 52 6 56", stroke=FG, sw=2.6, opacity=.8),
     ))

# 36. A sieve with parentheses going in: formatter, linter, tidy output.
icon("sift", "sift",
     "Dialect-aware formatter, linter and language server for Scheme and the Lisps",
     "moss",
     [part(poly_d([(4, 5), (60, 5), (39, 36), (25, 36)])),
      part(rrect(21, 35, 22, 6, 3), "light"),
      part(rrect(24, 46, 16, 5, 2.5), "deep"),
      part(rrect(28, 54, 8, 5, 2.5), "deep")],
     G(
         P("M27 12c-2.8 3.2-2.8 9.6 0 12.8", stroke=FG, sw=2.4),
         P("M37 12c2.8 3.2 2.8 9.6 0 12.8", stroke=FG, sw=2.4),
         C(27, 38, 1.8, fill=DARK, opacity=.4),
         C(32, 38, 1.8, fill=DARK, opacity=.4),
         C(37, 38, 1.8, fill=DARK, opacity=.4),
     ))

# 37. A template grid with a delta and a plus: scaffolding from templates.
icon("skapa", "Skapa",
     "Project scaffolding and templating with S-expression templates",
     "turquoise",
     [part(rrect(3, 3, 25, 25, 6)),
      part(rrect(36, 3, 25, 25, 6), "light"),
      part(rrect(3, 36, 25, 25, 6), "light"),
      part(rrect(36, 36, 25, 25, 6))],
     G(
         P("M48 8 55 23H41z", fill=FG),
         P("M48 44v10M43 49h10", stroke=FG, sw=2.8),
     ))

# 38. The Tela folder, enamel and gloss: icons painted as objects.
icon("skeu-icons", "Skeu Icons",
     "Skeuomorphic Linux icon theme built from painted objects, in 30 variants",
     "rust",
     [part("M4 13c0-3.4 2-5 5.4-5h11l6 6h27.2c3.4 0 5.4 1.6 5.4 5v5H4z",
           "light"),
      part("M4 19h56v31c0 3.6-2 5.6-5.6 5.6H9.6C6 55.6 4 53.6 4 50z")],
     G(
         P("M4 19h56v10C42 23 18 23 4 30z", fill=FG, opacity=.22),
         L(11, 48, 19, 48, sw=2, color=FG, opacity=.45),
         L(23, 48, 31, 48, sw=2, color=FG, opacity=.45),
         L(35, 48, 43, 48, sw=2, color=FG, opacity=.45),
         L(47, 48, 55, 48, sw=2, color=FG, opacity=.45),
     ))

# 39. An event burst crossed by a pulse: privacy-friendly analytics.
icon("symbanta", "Symbanta",
     "Privacy-friendly, free analytics core that records events, not people",
     "cyan",
     [part(star(32, 32, 30, 17.5, points=8, rotate=0))],
     G(
         P("M8 33h9l4-11 6 22 6-28 6 20 4-4h13", stroke=FG, sw=3),
         C(27, 22, 2.2, fill=FG),
         C(33, 44, 2.2, fill=FG),
     ))

# 40. A frosted chart panel: the calm dashboard.
icon("symbanta-dashboard", "Symbanta Dashboard",
     "React dashboard that visualises a symbanta instance without surveillance",
     "flamingo",
     [part(rrect(3, 7, 58, 50, 6)),
      part(rrect(3, 7, 58, 12, 6), "light")],
     G(
         P("M12 46c6 0 8-17 15-17s6 12 13 12 5-8 11-8",
           stroke=FG, sw=3),
         L(12, 51, 52, 51, sw=2.2, color=FG, opacity=.45),
         R(12, 16, 18, 4, rx=2, fill=DARK, opacity=.25),
     ))

# 41. A disc holding an A, a smaller a and a scale: proportional type sizes.
icon("tekengrootte.el", "tekengrootte.el",
     "Proportional, scale-relative Emacs face sizes from nano to colossal",
     "gold",
     [part(disc(32, 32, 29))],
     G(
         P("M14 45 23 18 32 45", stroke=DARK, sw=3.6),
         L(17.6, 36, 28.4, 36, sw=3.2, color=DARK),
         C(44, 38, 5.8, fill="none", stroke=DARK, sw=2.8),
         L(49.8, 32.2, 49.8, 45, sw=2.8, color=DARK),
         L(10, 50, 24, 50, sw=2, color=FG, opacity=.55),
         L(38, 50, 54, 50, sw=2, color=FG, opacity=.35),
     ))

# 42. A down arrow dropping into a tray: ingesting files into the archive.
icon("torikomi", "torikomi",
     "Artemis service that sinks remote URLs into a local media archive",
     "lagoon",
     [part(poly_d([(26, 5), (38, 5), (38, 21), (46, 21), (32, 34),
                   (18, 21), (26, 21)]), "light"),
      part("M4 30v15a6 6 0 0 0 6 6h44a6 6 0 0 0 6-6V30H39l-3 7H27l-3-7z"),
      part(rrect(6, 46, 52, 9, 4), "deep")],
     G(
         L(12, 52, 52, 52, sw=2.4, color=FG, opacity=.55),
     ))

# 43. Scales balancing on a checked base: truth, weighed.
icon("veritas", "Veritas",
     "Guile test framework where a test is a form and the report is a hierarchy",
     "bottle",
     [part(rrect(16, 49, 32, 9, 4.5), "light"),
      part(rrect(29, 9, 6, 44, 3)),
      part(rrect(8, 14, 48, 5, 2.5)),
      part("M8 20a8 8 0 0 0 16 0z"),
      part("M40 20a8 8 0 0 0 16 0z")],
     G(
         C(32, 16.5, 2.8, fill=FG),
         P("M24 53.4l3.4 3.4 7-8", stroke=FG, sw=2.6),
         L(16, 20, 16, 17, sw=2, color=FG, opacity=.5),
         L(40, 20, 40, 17, sw=2, color=FG, opacity=.5),
     ))

# 44. A disc with parentheses around a check: Veritas driven from Emacs.
icon("veritas.el", "veritas.el",
     "Emacs integration for the Veritas test framework: run, report, navigate",
     "violetta",
     [part(disc(32, 32, 29))],
     G(
         P("M23 12c-6.4 5-6.4 35 0 40", stroke=FG, sw=3.4),
         P("M41 12c6.4 5 6.4 35 0 40", stroke=FG, sw=3.4),
         P("M26 32l4.6 6 9-13", stroke=DARK, sw=3.6),
     ))

# 45. The sun rising over the horizon: a quiet welcome screen.
icon("welkomscherm.el", "welkomscherm.el",
     "Small, calm, theme-respecting welcome screen for Emacs",
     "sunrise",
     [part("M13 43a19 19 0 0 1 38 0z"),
      part(rrect(3, 43, 58, 9, 4.5), "light")],
     G(
         P("M32 18V8M17 32 9 24M47 32 55 24", stroke=deep("sunrise"), sw=2.8),
         L(11, 47.5, 26, 47.5, sw=2.4, color=FG, opacity=.8),
         L(32, 47.5, 45, 47.5, sw=2.4, color=FG, opacity=.45),
     ))

# 46. A book carrying a note and wiki brackets: music as a shared library.
icon("wikimusic", "WikiMusic",
     "Collaborative music wiki built with GNU Artanis and Guile",
     "blush",
     [part(rrect(3, 5, 58, 54, 5)),
      part(rrect(3, 5, 12, 54, 5), "light")],
     G(
         C(27, 41, 7.4, fill=FG),
         L(34.4, 41, 34.4, 18, sw=3.4, color=FG),
         P("M34.4 18c7.4 2 11.6 7.4 11.6 14", stroke=FG, sw=3.2),
         L(20, 16, 20, 34, sw=2.2, color=FG, opacity=.5),
         L(24, 14, 24, 36, sw=2.2, color=FG, opacity=.5),
         P("M50 24h-3v18h3", stroke=FG, sw=2.4, opacity=.8),
         P("M56 24h-3v18h3", stroke=FG, sw=2.4, opacity=.55),
     ))

# 47. A striped traffic cone: the maintenance page standing in for a site.
icon("wip-site", "wip-site",
     "Dependency-free maintenance and coming-soon status page",
     "ochre",
     [part(poly_d([(32, 3), (48, 47), (16, 47)])),
      part(poly_d([(26.4, 19), (37.6, 19), (39.6, 27), (24.4, 27)]), "pale"),
      part(poly_d([(22.4, 34), (41.6, 34), (43.6, 42), (20.4, 42)]), "pale"),
      part(rrect(9, 46, 46, 10, 5), "light")],
     G(
         L(14, 51, 50, 51, sw=2.2, color=FG, opacity=.4),
     ))

# 48. A castle riding a cloud: the Hetzner cloud castle.
icon("wolkenschloss", "Wolkenschloss",
     "Hetzner Cloud infrastructure managed from the REST API",
     "periwinkle",
     [part(disc(17, 44, 10), "light"),
      part(disc(32, 37, 14), "light"),
      part(disc(47, 44, 10), "light"),
      part(rrect(6, 43, 52, 14, 7), "light"),
      part(rrect(18, 20, 9, 27)),
      part(rrect(37, 20, 9, 27)),
      part(rrect(27, 27, 10, 20)),
      part(rrect(18, 15, 3.4, 5)),
      part(rrect(23.6, 15, 3.4, 5)),
      part(rrect(37, 15, 3.4, 5)),
      part(rrect(42.6, 15, 3.4, 5))],
     G(
         R(20.6, 26, 3.8, 5, rx=1.4, fill=FG),
         R(39.6, 26, 3.8, 5, rx=1.4, fill=FG),
         P("M29.6 47v-9a2.6 2.6 0 0 1 5.2 0v9", fill=FG),
         L(32, 27, 32, 18, sw=2, color=FG),
         PL("32,18 39,20.4 32,22.8", fill=FG),
     ))

# 49. A lyre, the instrument of the singer: music played from Emacs.
icon("orpheus.el", "orpheus.el",
     "Music player for Emacs with pluggable MPD, mpv, SSH and local backends",
     "orange",
     [part("M17.5 7C10.5 13.5 8.5 23 12.5 31.5C14.2 35 16.8 37.8 20.4 39.8"
           "L23.6 35.4C20.8 33.4 18.6 30.8 17.4 27.6C14.6 20.8 16.4 13.4"
           " 23 8.6z"),
      part("M17.5 7C10.5 13.5 8.5 23 12.5 31.5C14.2 35 16.8 37.8 20.4 39.8"
           "L23.6 35.4C20.8 33.4 18.6 30.8 17.4 27.6C14.6 20.8 16.4 13.4"
           " 23 8.6z",
           "main", "translate(64 0) scale(-1 1)"),
      part(ell(32, 45, 14, 11)),
      part(ell(32, 44.2, 10.8, 7.8), "light"),
      part(rrect(15, 4, 34, 5.6, 2.8), "light"),
      part(disc(12.4, 6.8, 3.2), "dark"),
      part(disc(51.6, 6.8, 3.2), "dark")],
     G(
         R(25.5, 37.4, 13, 3.2, rx=1.6, fill=FG),
         L(26, 9.8, 27.2, 37.6, sw=1.5, color=FG),
         L(29, 9.8, 29.8, 37.6, sw=1.5, color=FG),
         L(32, 9.8, 32, 37.6, sw=1.5, color=FG),
         L(35, 9.8, 34.2, 37.6, sw=1.5, color=FG),
         L(38, 9.8, 36.8, 37.6, sw=1.5, color=FG),
         P("M16.6 13C11.6 19 11.2 26 14.6 30.6", stroke=FG, sw=1.4,
           opacity=.35),
         P("M47.4 13C52.4 19 52.8 26 49.4 30.6", stroke=FG, sw=1.4,
           opacity=.35),
         C(32, 47.8, 2.6, fill="none", stroke=FG, sw=1.4, opacity=.55),
         C(32, 47.8, 1, fill=FG, opacity=.55),
         C(12.4, 6.8, 1.2, fill=FG, opacity=.8),
         C(51.6, 6.8, 1.2, fill=FG, opacity=.8),
     ))

# 50. A cloud holding a server rack: a personal cloud, provisioned by Lisp.
icon("wolk-jjba", "wolk-jjba",
     "Personal cloud and server fleet provisioned as a Guile program",
     "storm",
     [part(disc(16, 31, 9), "light"),
      part(disc(31, 25, 13), "light"),
      part(disc(46, 31, 9), "light"),
      part(rrect(7, 29, 50, 15, 7), "light"),
      part(rrect(19, 28, 27, 23, 3))],
     G(
         P("M24 34l3 2-3 2", stroke=DARK, sw=1.8),
         L(24, 42, 41, 42, sw=1.8, color=DARK, opacity=.3),
         L(24, 46.4, 35, 46.4, sw=1.8, color=DARK, opacity=.22),
         C(41, 33.6, 1.7, fill=DARK, opacity=.5),
         C(41, 38.4, 1.7, fill=DARK, opacity=.35),
     ))

# 51. A whelk shell standing on its spire: the shell that hosts the desktop.
icon("whelk", "whelk",
     "Wayland shell in C, GTK4 and Guile: status bar, launcher and notifications",
     "sand",
     [part(ell(30, 43, 21.5, 16.5), "main", "rotate(-12 30 43)"),
      part(ell(34, 27.5, 15, 12), "main", "rotate(-12 34 27.5)"),
      part(ell(38.5, 16, 10, 8.4), "main", "rotate(-12 38.5 16)"),
      part("M42.6 2.4c1.8 1.4 2.8 3.4 2.8 5.6 0 2.6-1.6 4.2-3.6 4.6"
           "-2-.4-3.6-2-3.6-4.6 0-2.2 1-4.2 2.8-5.6z"),
      part(ell(22.5, 46.5, 7, 12), "deep", "rotate(8 22.5 46.5)")],
     G(
         P("M29.5 46.5a7 12 0 1 0 -14 0a7 12 0 1 0 14 0", stroke=FG,
           sw=1.8, opacity=.75, transform="rotate(8 22.5 46.5)"),
         P("M35 27.5c4.4 6 5.6 15.5 3.2 24.5", stroke=FG, sw=1.8, opacity=.4),
         P("M41 27c4 6 5 13 3 20", stroke=FG, sw=1.8, opacity=.28),
         P("M46 39c1.6 3.4 2 7 1.4 10", stroke=FG, sw=1.6, opacity=.22),
     ))
