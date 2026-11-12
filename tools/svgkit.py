"""Tela-style icon kit: object silhouettes, not tiles.

Every icon is one or more filled shapes drawn on a 64 x 64 grid, in the idiom
of the Tela icon theme: a solid accent silhouette with white detail, a pale
top light, a soft shadow in the lower right, and a hairline where the object
meets the desktop.  There is no shared background tile: the object *is* the
icon, which is what makes Tela icons look like things rather than app squircles.
"""

from xml.sax.saxutils import escape

FG = "#fbfbfb"      # Tela's paper white, used for detail on the accent
DARK = "#263238"    # Tela's dark slate, used for insets and dark details

# Accents measured from the Tela icon themes (Tela, Tela-blue, Tela-green,
# Tela-orange, Tela-purple, Tela-pink, Tela-brown, Tela-yellow, Tela-grey,
# Tela-black) plus the Guix and Nix brand colours the collection already uses.
ACCENTS = {
    "violet": "#6961b8",
    "indigo": "#3434c8",
    "orange": "#ff7f28",
    "ember": "#f57c00",
    "ink": "#263238",
    "sky": "#45a3e6",
    "cocoa": "#795548",
    "plum": "#884ba1",
    "pink": "#f06292",
    "teal": "#26a69a",
    "green": "#66bb6a",
    "amber": "#efa63a",
    "guix": "#6f4e9c",
    "forest": "#3b843a",
    "mauve": "#a24ba1",
    "navy": "#2f4f6f",
    "rose": "#e05a6d",
    "sage": "#6f9c7a",
    "blue": "#5677fc",
    "bronze": "#b5563f",
    "royal": "#4741b5",
    "yellow": "#fbc02d",
    "grey": "#85858a",
    "sea": "#4a90a4",
    "lucid": "#5294e2",
    "brandorange": "#ff9800",
    "purple": "#8e44ad",
    "azure": "#4f9fe0",
    "deepgreen": "#2e7d5b",
    "nix": "#5277c3",
    "olive": "#8a9a4a",
    "purple2": "#7e57c2",
    "red": "#ef5350",
    "charcoal": "#455a64",
    "oak": "#a2703c",
    "moss": "#558b2f",
    "turquoise": "#1fa8a0",
    "rust": "#a8492f",
    "cyan": "#29b6c8",
    "flamingo": "#e2648f",
    "gold": "#ffca28",
    "lagoon": "#2f7f8f",
    "bottle": "#1f6f4a",
    "violetta": "#6a4fa3",
    "sunrise": "#fb8c00",
    "leaf": "#4caf50",
    "ochre": "#e08a00",
    "periwinkle": "#6b95d3",
    "storm": "#465a6b",
    "clover": "#2f9e44",
    "blush": "#d98aa3",
    "sand": "#c9a06b",
}


def _mix(hexcolour, other, t):
    a = hexcolour.lstrip("#")
    b = other.lstrip("#")
    out = []
    for i in (0, 2, 4):
        ca = int(a[i:i + 2], 16)
        cb = int(b[i:i + 2], 16)
        out.append(round(ca + (cb - ca) * t))
    return "#" + "".join(f"{c:02x}" for c in out)


def lighten(colour, t):
    return _mix(colour, "#ffffff", t)


def darken(colour, t):
    return _mix(colour, "#000000", t)


def palette(key):
    base = ACCENTS[key]
    return lighten(base, 0.16), base, darken(base, 0.26)


def tone_stops(tone, accent):
    """Colour stops for one face of the object."""
    top, base, bottom = palette(accent)
    if tone == "light":
        return lighten(base, 0.34), lighten(base, 0.16), base
    if tone == "pale":
        return lighten(base, 0.62), lighten(base, 0.48), lighten(base, 0.32)
    if tone == "dark":
        return base, darken(base, 0.14), darken(base, 0.26)
    if tone == "deep":
        return darken(base, 0.16), darken(base, 0.3), darken(base, 0.4)
    return top, base, bottom


# ------------------------------------------------------------- shape helpers

def rrect(x, y, w, h, r=4):
    r = min(r, w / 2, h / 2)
    return (f"M{x + r} {y}h{w - 2 * r}a{r} {r} 0 0 1 {r} {r}v{h - 2 * r}"
            f"a{r} {r} 0 0 1 {-r} {r}H{x + r}a{r} {r} 0 0 1 {-r} {-r}V{y + r}"
            f"a{r} {r} 0 0 1 {r} {-r}z")


def disc(cx, cy, r):
    return (f"M{cx} {cy - r}a{r} {r} 0 1 0 0 {2 * r}a{r} {r} 0 1 0 0 {-2 * r}z")


def ell(cx, cy, rx, ry):
    return (f"M{cx - rx} {cy}a{rx} {ry} 0 1 0 {2 * rx} 0a{rx} {ry} 0 1 0"
            f" {-2 * rx} 0z")


def poly_d(points):
    first = f"M{points[0][0]} {points[0][1]}"
    rest = "".join(f"L{x} {y}" for x, y in points[1:])
    return first + rest + "z"


def part(d, tone="main", transform=None):
    """One face of the object: a path, a tone and an optional transform."""
    return {"d": d, "tone": tone, "transform": transform}


def cog_parts(cx, cy, r, teeth=8, tooth=None, tone="main"):
    """A gear as a union of a disc and chunky radial teeth."""
    if tooth is None:
        tooth = 2 * 3.14159 * r / teeth * 0.64
    parts = [part(disc(cx, cy, r * 0.79), tone)]
    for i in range(teeth):
        parts.append(part(
            rrect(cx - tooth / 2, cy - r - 1, tooth, r * 0.36, 1.6), tone,
            f"rotate({i * 360 / teeth} {cx} {cy})"))
    return parts


def cog(cx, cy, r, fill=FG, hole=None, teeth=8):
    """A gear drawn as detail (white on the accent, say)."""
    kids = []
    for i in range(teeth):
        kids.append(R(cx - 1.7, cy - r - 1.4, 3.4, 4.2, rx=1, fill=fill,
                      transform=f"rotate({i * 360 / teeth} {cx} {cy})"))
    kids.append(C(cx, cy, r * 0.78, fill=fill))
    if hole:
        kids.append(C(cx, cy, r * 0.3, fill=hole))
    return G(*kids)


# ------------------------------------------------------------------ details

def P(d, fill="none", stroke=None, sw=4, opacity=None, transform=None):
    attrs = f' d="{d}" fill="{fill}"'
    if stroke:
        attrs += (f' stroke="{stroke}" stroke-width="{sw}"'
                  ' stroke-linecap="round" stroke-linejoin="round"')
    if opacity is not None:
        attrs += f' opacity="{opacity}"'
    if transform:
        attrs += f' transform="{transform}"'
    return f"<path{attrs}/>"


def C(cx, cy, r, fill=FG, stroke=None, sw=4, opacity=None):
    attrs = f' cx="{cx}" cy="{cy}" r="{r}" fill="{fill}"'
    if stroke:
        attrs += f' stroke="{stroke}" stroke-width="{sw}"'
    if opacity is not None:
        attrs += f' opacity="{opacity}"'
    return f"<circle{attrs}/>"


def E(cx, cy, rx, ry, fill=FG, opacity=None, transform=None):
    attrs = f' cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="{fill}"'
    if opacity is not None:
        attrs += f' opacity="{opacity}"'
    if transform:
        attrs += f' transform="{transform}"'
    return f"<ellipse{attrs}/>"


def R(x, y, w, h, rx=0, fill=FG, opacity=None, transform=None):
    attrs = f' x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}"'
    if opacity is not None:
        attrs += f' opacity="{opacity}"'
    if transform:
        attrs += f' transform="{transform}"'
    return f"<rect{attrs}/>"


def L(x1, y1, x2, y2, sw=4, color=FG, opacity=None):
    attrs = (f' x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}"'
             f' stroke-width="{sw}" stroke-linecap="round"')
    if opacity is not None:
        attrs += f' opacity="{opacity}"'
    return f"<line{attrs}/>"


def PL(points, fill=FG, opacity=None, transform=None):
    attrs = f' points="{points}" fill="{fill}"'
    if opacity is not None:
        attrs += f' opacity="{opacity}"'
    if transform:
        attrs += f' transform="{transform}"'
    return f"<polygon{attrs}/>"


def G(*kids, opacity=None, transform=None):
    attrs = ""
    if opacity is not None:
        attrs += f' opacity="{opacity}"'
    if transform:
        attrs += f' transform="{transform}"'
    return f"<g{attrs}>" + "".join(k for k in kids if k) + "</g>"


# ------------------------------------------------------------------- canvas

TONES = ("main", "light", "pale", "dark", "deep")


def canvas(slug, accent, parts, details):
    """Paint the object: fills, top light, lower-right shade, hairline, detail.

    ``parts`` is a list of {"d": path, "tone": one of TONES, "transform": ...}.
    The top light and the shade are clipped to the union of the parts, so one
    light source works across a multi-part object such as a folder or a box.
    """
    defs = ["<defs>"]
    for tone in TONES:
        a, b, c = tone_stops(tone, accent)
        defs.append(
            f'<linearGradient id="{slug}-{tone}" x1="0" y1="0" x2="0" y2="64"'
            ' gradientUnits="userSpaceOnUse">'
            f'<stop offset="0" stop-color="{a}"/>'
            f'<stop offset=".55" stop-color="{b}"/>'
            f'<stop offset="1" stop-color="{c}"/></linearGradient>')
    defs.append(
        f'<linearGradient id="{slug}-gloss" x1="0" y1="0" x2="0" y2="36"'
        ' gradientUnits="userSpaceOnUse">'
        '<stop offset="0" stop-color="#ffffff" stop-opacity=".3"/>'
        '<stop offset="1" stop-color="#ffffff" stop-opacity="0"/></linearGradient>')
    defs.append(
        f'<linearGradient id="{slug}-shade" x1="20" y1="20" x2="64" y2="64"'
        ' gradientUnits="userSpaceOnUse">'
        '<stop offset=".3" stop-color="#000000" stop-opacity="0"/>'
        '<stop offset="1" stop-color="#000000" stop-opacity=".22"/></linearGradient>')
    leaves = "".join(
        f'<path d="{p["d"]}"' + (f' transform="{p["transform"]}"' if p.get("transform") else "") + "/>"
        for p in parts)
    defs.append(f'<clipPath id="{slug}-clip">{leaves}</clipPath>')
    defs.append("</defs>")

    fills = "".join(
        f'<path d="{p["d"]}" fill="url(#{slug}-{p.get("tone", "main")})"'
        + (f' transform="{p["transform"]}"' if p.get("transform") else "")
        + "/>"
        for p in parts)
    seams = "".join(
        f'<path d="{p["d"]}" fill="none" stroke="#ffffff" stroke-opacity=".26"'
        ' stroke-width="1.6"'
        + (f' transform="{p["transform"]}"' if p.get("transform") else "")
        + "/>"
        for p in parts)
    hairline = "".join(
        f'<path d="{p["d"]}" fill="none" stroke="#000000" stroke-opacity=".16"'
        ' stroke-width="1"'
        + (f' transform="{p["transform"]}"' if p.get("transform") else "")
        + "/>"
        for p in parts)

    return f'''{"".join(defs)}
 <g clip-path="url(#{slug}-clip)">
  {fills}
  <rect x="0" y="0" width="64" height="64" fill="url(#{slug}-gloss)"/>
  <rect x="0" y="0" width="64" height="64" fill="url(#{slug}-shade)"/>
  {seams}
 </g>
 {hairline}
 {details}'''


def svg_document(slug, accent, parts, details, title):
    safe = escape(title)
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" viewBox="0 0 64 64"
     role="img" aria-label="{safe}">
 <title>{safe}</title>
 {canvas(slug, accent, parts, details)}
</svg>
'''
