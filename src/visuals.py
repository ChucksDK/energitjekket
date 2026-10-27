# -*- coding: utf-8 -*-
"""v7: originale grafikker, genereret ved hvert build (ingen stockfotos, ingen personer).
- og_image(): 1200x630 PNG-delebilleder (Pillow) til og:image / twitter:image
- heat_svg() / sun_svg(): SVG-diagrammer pr. by ud fra data_local (DST BOL102 og PVGIS)
Nye byer i CITIES/data_local får automatisk begge dele."""
import os, html
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
FONT_B = os.path.join(HERE, "fonts", "DejaVuSans-Bold.ttf")
FONT_R = os.path.join(HERE, "fonts", "DejaVuSans.ttf")
G, G2, Y, INK, MINT = (11, 79, 67), (15, 107, 85), (245, 183, 0), (19, 32, 29), (207, 229, 221)

def _wrap(draw, text, font, width):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=font) <= width: cur = t
        else:
            if cur: lines.append(cur)
            cur = w
    if cur: lines.append(cur)
    return lines

def og_image(fp, title, sub, brand="Energitjekket", domain="energitjekket.dk", motif="both"):
    W, H = 1200, 630
    im = Image.new("RGB", (W, H), G)
    d = ImageDraw.Draw(im)
    # baggrundsform: lysere diagonal flade + sol
    d.polygon([(760, 0), (W, 0), (W, H), (560, H)], fill=G2)
    cx, cy, r = 1010, 170, 74
    for i in range(12):
        import math
        a = i * math.pi / 6
        d.line([(cx + math.cos(a) * (r + 18), cy + math.sin(a) * (r + 18)), (cx + math.cos(a) * (r + 46), cy + math.sin(a) * (r + 46))], fill=Y, width=10)
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=Y)
    # hus med solcelletag og varmepumpe (geometrisk, egen tegning)
    hx, hy = 770, 360
    d.polygon([(hx, hy + 70), (hx + 150, hy - 40), (hx + 300, hy + 70)], fill=(232, 241, 237))
    d.rectangle([hx + 30, hy + 70, hx + 270, hy + 250], fill=(232, 241, 237))
    d.rectangle([hx + 125, hy + 160, hx + 175, hy + 250], fill=G)
    if motif in ("both", "sol"):
        for row in range(2):
            for col in range(3):
                x0 = hx + 84 + col * 46 - row * 14; y0 = hy + 8 + row * 28
                d.rectangle([x0, y0, x0 + 40, y0 + 24], fill=(31, 64, 99), outline=(140, 170, 200), width=2)
    if motif in ("both", "vp"):
        d.rounded_rectangle([hx + 290, hy + 175, hx + 370, hy + 250], 8, fill=(250, 250, 250), outline=(180, 195, 190), width=3)
        d.ellipse([hx + 300, hy + 188, hx + 350, hy + 238], outline=(120, 140, 135), width=5)
        d.line([(hx + 325, hy + 192), (hx + 325, hy + 234)], fill=(120, 140, 135), width=4)
        d.line([(hx + 304, hy + 213), (hx + 346, hy + 213)], fill=(120, 140, 135), width=4)
    d.rectangle([600, hy + 250, W, hy + 262], fill=(9, 64, 54))
    # brand
    d.rounded_rectangle([64, 56, 112, 104], 12, fill=Y)
    d.ellipse([78, 70, 98, 90], fill=G)
    d.text((128, 58), brand, font=ImageFont.truetype(FONT_B, 38), fill=(255, 255, 255))
    # titel (skaleres ned til max 4 linjer)
    for size in (68, 62, 56, 52, 48, 44):
        f = ImageFont.truetype(FONT_B, size)
        lines = _wrap(d, title, f, 640)
        if len(lines) <= 3: break
    y = 170
    for ln in lines:
        d.text((64, y), ln, font=f, fill=(255, 255, 255)); y += int(size * 1.18)
    fs = ImageFont.truetype(FONT_R, 30)
    for ln in _wrap(d, sub, fs, 640)[:2]:
        d.text((64, y + 18), ln, font=fs, fill=MINT); y += 40
    d.text((64, H - 76), domain, font=ImageFont.truetype(FONT_B, 32), fill=Y)
    os.makedirs(os.path.dirname(fp), exist_ok=True)
    im = im.quantize(colors=96, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE)
    im.save(fp, "PNG", optimize=True)

def _e(t): return html.escape(str(t), quote=True)
FONT_CSS = "font-family:system-ui,-apple-system,'Segoe UI',Roboto,Arial,sans-serif"

def heat_svg(name, rows):
    """rows: [(label, pct_kommune(float), pct_dk(float))]"""
    W, top, rh, lab = 640, 64, 52, 210
    H = top + rh * len(rows) + 16
    mx = max(max(a, b) for _, a, b in rows) or 1
    bw = W - lab - 70
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-labelledby="t">',
           f'<title id="t">Opvarmning af huse i {_e(name)} sammenlignet med hele landet</title>',
           f'<style>text{{{FONT_CSS};font-size:15px;fill:#13201d}}.v{{font-size:13px;fill:#4f5e5a}}.l{{font-size:14px}}</style>',
           f'<rect width="{W}" height="{H}" fill="#fff"/>',
           f'<rect x="{lab}" y="14" width="14" height="14" rx="3" fill="#0f6b55"/><text x="{lab+20}" y="26" class="l">{_e(name)}</text>',
           f'<rect x="{lab+190}" y="14" width="14" height="14" rx="3" fill="#b8c7c1"/><text x="{lab+210}" y="26" class="l">Hele landet</text>']
    for i, (l, a, b) in enumerate(rows):
        y = top + i * rh
        out.append(f'<text x="0" y="{y+19}">{_e(l)}</text>')
        wa, wb = max(2, bw * a / mx), max(2, bw * b / mx)
        out.append(f'<rect x="{lab}" y="{y+4}" width="{wa:.1f}" height="18" rx="3" fill="#0f6b55"/><text x="{lab+wa+6:.1f}" y="{y+18}" class="v">{a:.1f} %</text>'.replace(".", ",", 0))
        out.append(f'<rect x="{lab}" y="{y+25}" width="{wb:.1f}" height="12" rx="3" fill="#b8c7c1"/><text x="{lab+wb+6:.1f}" y="{y+36}" class="v">{b:.1f} %</text>')
    out.append("</svg>")
    s = "".join(out)
    import re
    return re.sub(r'>(\d+)\.(\d) %<', r'>\1,\2 %<', s)

def sun_svg(name, months_kwh):
    W, H, pl, pb, pt = 640, 300, 48, 34, 36
    mx = max(months_kwh); top = (int(mx / 200) + 1) * 200
    cw = (W - pl - 10) / 12
    lab = ["jan", "feb", "mar", "apr", "maj", "jun", "jul", "aug", "sep", "okt", "nov", "dec"]
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-labelledby="t">',
           f'<title id="t">Månedlig produktion fra et sydvendt 6 kWp-solcelleanlæg i {_e(name)}</title>',
           f'<style>text{{{FONT_CSS};font-size:13px;fill:#4f5e5a}}.m{{fill:#13201d}}</style><rect width="{W}" height="{H}" fill="#fff"/>']
    ph = H - pb - pt
    for k in range(0, top + 1, 200):
        y = pt + ph - ph * k / top
        out.append(f'<line x1="{pl}" x2="{W-6}" y1="{y:.1f}" y2="{y:.1f}" stroke="#e1e8e5"/><text x="{pl-6}" y="{y+4:.1f}" text-anchor="end">{k}</text>')
    for i, v in enumerate(months_kwh):
        h = ph * v / top; x = pl + i * cw + cw * 0.18
        out.append(f'<rect x="{x:.1f}" y="{pt+ph-h:.1f}" width="{cw*0.64:.1f}" height="{h:.1f}" rx="3" fill="#f5b700"/>')
        out.append(f'<text x="{x+cw*0.32:.1f}" y="{H-12}" text-anchor="middle" class="m">{lab[i]}</text>')
    out.append(f'<text x="{pl}" y="14">kWh pr. måned</text></svg>')
    return "".join(out)

def logo_png(fp):
    import math
    im = Image.new("RGB", (512, 512), G); d = ImageDraw.Draw(im)
    cx = cy = 256
    for i in range(8):
        a = i * math.pi / 4
        d.line([(cx + math.cos(a) * 128, cy + math.sin(a) * 128), (cx + math.cos(a) * 186, cy + math.sin(a) * 186)], fill=Y, width=26)
    d.ellipse([cx - 92, cy - 92, cx + 92, cy + 92], fill=Y)
    os.makedirs(os.path.dirname(fp), exist_ok=True)
    im.quantize(colors=16).save(fp, "PNG", optimize=True)
