#!/usr/bin/env python3
"""Generate PWA / iOS icons from the equirectangular earth texture.

View: centered on the Atlantic so the Americas + Africa/Europe edges show
(Kai is US-based). Full-bleed circle on deep-space background, soft
atmosphere glow, anti-aliased edge via supersampling.
"""
import sys
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance, ImageChops

SRC = "earth.jpg"
OUT = "."
BG = (1, 3, 10, 255)          # --bg #01030a
GLOW = (61, 139, 255)         # atmosphere blue

tex = Image.open(SRC).convert("RGB")
W, H = tex.size
assert W >= 1024 and H >= 512, f"texture too small: {W}x{H}"

# Square crop: height = H, centered on x = 30% of width (Americas/Atlantic)
side = H
cx = int(W * 0.30)
x0 = max(0, min(W - side, cx - side // 2))
globe = tex.crop((x0, 0, x0 + side, side))


def make_icon(size, earth_frac, path):
    SS = 4  # supersample
    S = size * SS
    img = Image.new("RGBA", (S, S), BG)

    d = int(S * earth_frac)
    off = (S - d) // 2

    # atmosphere glow: blurred blue disc slightly larger than the earth
    glow = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    g = int(d * 1.06)
    goff = (S - g) // 2
    gd.ellipse([goff, goff, goff + g, goff + g], fill=GLOW + (110,))
    glow = glow.filter(ImageFilter.GaussianBlur(S * 0.045))
    img = Image.alpha_composite(img, glow)

    # earth disc (slight pop so it reads on a home screen)
    earth = globe.resize((d, d), Image.LANCZOS).convert("RGBA")
    earth = ImageEnhance.Brightness(earth).enhance(1.13)
    earth = ImageEnhance.Color(earth).enhance(1.18)
    mask = Image.new("L", (d, d), 0)
    md = ImageDraw.Draw(mask)
    md.ellipse([0, 0, d, d], fill=255)
    img.paste(earth, (off, off), mask)

    # terminator shading: stepped radial gradient (draw replaces, so no
    # alpha compounding), blurred smooth, darkest toward bottom-right rim
    sa = Image.new("L", (d, d), 0)
    sad = ImageDraw.Draw(sa)
    ccx, ccy = d * 0.70, d * 0.72
    for i in range(48, 0, -1):
        r = d * 0.98 * i / 48
        v = int(165 * (1 - i / 48) ** 1.6)
        sad.ellipse([ccx - r, ccy - r, ccx + r, ccy + r], fill=v)
    sa = sa.filter(ImageFilter.GaussianBlur(d * 0.06))
    shade_img = Image.new("RGBA", (d, d), (0, 0, 10, 255))
    img.paste(shade_img, (off, off), ImageChops.multiply(sa, mask))

    img = img.resize((size, size), Image.LANCZOS).convert("RGB")
    img.save(path, "PNG")
    print("wrote", path, size)


make_icon(180, 0.94, f"{OUT}/icon-180.png")           # apple touch icon
make_icon(192, 0.94, f"{OUT}/icon-192.png")
make_icon(512, 0.94, f"{OUT}/icon-512.png")
make_icon(512, 0.74, f"{OUT}/icon-maskable-512.png")  # safe-zone padding
print("done")
