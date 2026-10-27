# -*- coding: utf-8 -*-
"""Statisk site-generator. Kør: python3 build.py  ->  skriver til ../site/"""
import json, os, re, shutil, html
import datetime as dt
from config import *
from data import CONTACTS, S, SERVICES, CITIES, SOL_PRICE_ROWS, VP_PRICE_ROWS, SOL_GENERAL_FAQ, VP_GENERAL_FAQ
from data_sub import SOL_REG, FV_PAGE, NATIONAL, FV_PRICES, FV_AVG, FV_COMPARE_ROWS
import data_local as L
S.update(L.LOCAL_S)
from data_topics import TOPIC_S, T as TOPICS, NAV as TOPIC_NAV
S.update(TOPIC_S)
NATIONAL.update(TOPICS)
import visuals as V
from calc_js import CALC_JS
import elpris as EL
S.update(EL.SOURCES)
S["cvr_virk"] = TOPIC_S["cvr_virk"]

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "site")
OTHER = {"solceller": "varmepumpe", "varmepumpe": "solceller"}

def esc(t): return html.escape(t, quote=True)
def strip(t): return re.sub(r"<[^>]+>", "", t)
def url(path): return SITE_URL + path
def has_vp(c): return CITIES[c].get("vp_page", True)
def p_city(svc, c):
    """Byer med >90 % fjernvarme (vp_page False) har ingen selvstændig varmepumpe-byside: alle links går til fjernvarme-eller-varmepumpe-siden."""
    if svc == "varmepumpe" and not has_vp(c): return p_fv(c)
    return f"/{svc}/{c}/"
def p_hub(svc): return f"/{svc}/"
def p_reg(c): return f"/solceller/{c}/regler-og-byggetilladelse/"
def p_fv(c): return f"/varmepumpe/{c}/fjernvarme-eller-varmepumpe/"
NUMW = {2: "to", 3: "tre", 4: "fire", 5: "fem", 6: "seks", 7: "syv", 8: "otte", 9: "ni", 10: "ti", 11: "elleve", 12: "tolv"}
def n_byer(): return f"{len(CITIES)} byer"
def city_list(): ns = [CITIES[c]["name"] for c in CITIES]; return ", ".join(ns[:-1]) + " og " + ns[-1]
def fit_desc(full, short):
    """Beskrivelse med alle bynavne, så længe den holder sig under 160 tegn; ellers den korte udgave med antal byer."""
    return full if len(full) <= 160 else short
def p_sub(svc, c): return p_reg(c) if svc == "solceller" else p_fv(c)
def sub_label(svc, c):
    n = CITIES[c]["name"]
    return f"Solceller i {n}: regler og byggetilladelse" if svc == "solceller" else f"Fjernvarme eller varmepumpe i {n}?"
def is_ph(v): return str(v).startswith("[")
# FAQ der flyttes fra undersiden til bysiden (så samme spørgsmål ikke står to steder)
SOL_BORROW = {c: (2 if c == "odense" else 1) for c in CITIES}
VP_BORROW = {c: None for c in CITIES}  # VP-bysider får i stedet en lokal fjernvarmepris-boks
NAT_CORE = {"solceller": [("/solceller/pris/", "Solceller pris 2026", "Pris pr. kWp og m², ekstraposter og tilbagebetaling."),
                           ("/solceller/med-batteri/", "Solceller med batteri", "Hvad et batteri koster, og hvornår det kan betale sig.")],
             "varmepumpe": [("/varmepumpe/pris/", "Luft til vand-varmepumpe pris", "Pris inkl. montering, drift pr. år og tilskud."),
                            ("/varmepumpe/tilskud/", "Varmepumpepuljen 2026", "Status, de 5 krav og fristen 30. november 2026.")]}
# v7: alle guides (kerne + nye emnesider). NAT_CORE bruges i bysidernes guides-blok for at holde ligheden lav.
NAT_LINKS = {svc: NAT_CORE[svc] + [(u, t, d) for u, t, d, _ in TOPIC_NAV[svc]] for svc in NAT_CORE}
CALC = ("/beregner/", "Beregner: kan det betale sig?", "Regn selv på tilbagebetalingen for solceller og varmepumpe.")
def checked_c(c):
    """Faktatjek-dato for en by: byens egen 'updated' (daglig rutine), ellers den fælles LAST_CHECKED."""
    return CITIES[c]["updated"][0] if CITIES[c].get("updated") else LAST_CHECKED
def page_upd(g=None, c=None):
    """(synlig dato, ISO) til 'Opdateret' og dateModified."""
    if g and g.get("updated"): return g["updated"]
    if c and CITIES[c].get("updated"): return CITIES[c]["updated"]
    return (LAST_UPDATED, LAST_UPDATED_ISO)

def src_links(keys):
    if not keys: return ""
    parts = [f'<a href="{esc(S[k][1])}" target="_blank" rel="noopener nofollow">{esc(S[k][0])}</a>' for k in keys]
    return '<span class="src">Kilde: ' + "; ".join(parts) + "</span>"

def city_label(svc, c):
    n = CITIES[c]["name"]
    if svc == "varmepumpe" and not has_vp(c): return f"Fjernvarme eller varmepumpe i {n}"
    return f"Solceller i {n}" if svc == "solceller" else f"Varmepumpe i {n}"


def ld_breadcrumbs(items):
    return {"@type": "BreadcrumbList", "@id": url(items[-1][1]) + "#breadcrumbs",
            "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": url(p)} for i, (n, p) in enumerate(items)]}

def ld_org():
    o = {"@type": "Organization", "@id": SITE_URL + "/#org", "name": BRAND, "url": SITE_URL + "/", "description": BRAND_TAGLINE}
    if not is_ph(COMPANY_NAME): o["legalName"] = COMPANY_NAME
    if not is_ph(CVR): o["vatID"] = "DK" + CVR; o["identifier"] = {"@type": "PropertyValue", "propertyID": "CVR", "value": CVR}
    if not is_ph(COMPANY_ADDRESS):
        o["address"] = {"@type": "PostalAddress", "streetAddress": COMPANY_STREET, "postalCode": COMPANY_ZIP, "addressLocality": COMPANY_CITY, "addressCountry": "DK"}
    if not is_ph(CONTACT_PHONE): o["telephone"] = "+45 " + CONTACT_PHONE
    if not is_ph(CONTACT_EMAIL): o["email"] = CONTACT_EMAIL
    o["foundingDate"] = COMPANY_FOUNDED
    o["sameAs"] = [CVR_URL]
    o["logo"] = {"@type": "ImageObject", "url": SITE_URL + "/og/logo.png", "width": 512, "height": 512}
    return o

def ld_faq(path, faqs):
    return {"@type": "FAQPage", "@id": url(path) + "#faq",
            "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": strip(a)}} for q, a, _ in faqs]}

def faq_html(faqs):
    out = ['<div class="faq">']
    for q, a, k in faqs:
        out.append(f'<details><summary>{esc(q)}</summary><p>{a} {src_links(k)}</p></details>')
    out.append("</div>")
    return "".join(out)


# ---------- ikoner (inline SVG, ingen billeder) ----------
ICONS = {
 "sun": '<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/>',
 "pump": '<rect x="2" y="5" width="20" height="14" rx="2"/><circle cx="9" cy="12" r="4"/><path d="M9 8v8M5 12h8M16 9h3M16 12h3M16 15h3"/>',
 "pin": '<path d="M12 22s7-6.2 7-12a7 7 0 0 0-14 0c0 5.8 7 12 7 12z"/><circle cx="12" cy="10" r="2.5"/>',
 "book": '<path d="M4 19.5V5a2 2 0 0 1 2-2h14v16H6a2 2 0 0 0-2 2.5z"/><path d="M8 7h8M8 11h6"/>',
 "check": '<path d="M20 6 9 17l-5-5"/>',
 "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
 "chev": '<path d="m6 9 6 6 6-6"/>',
 "menu": '<path d="M4 6h16M4 12h16M4 18h16"/>',
 "close": '<path d="M6 6l12 12M18 6 6 18"/>',
 "shield": '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/>',
 "doc": '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6M8 13h8M8 17h5"/>',
 "coins": '<circle cx="9" cy="9" r="6"/><path d="M15.5 9.6a6 6 0 1 1-5.9 5.9"/>',
 "battery": '<rect x="2" y="7" width="17" height="10" rx="2"/><path d="M22 11v2M6 10v4M10 10v4"/>',
 "gift": '<rect x="3" y="8" width="18" height="4" rx="1"/><path d="M12 8v13M5 12v9h14v-9M12 8S10 3 7.5 4.5 9 8 12 8zM12 8s2-5 4.5-3.5S15 8 12 8z"/>',
 "building": '<path d="M3 21h18M5 21V9l7-5 7 5v12M9 21v-6h6v6"/>',
 "flame": '<path d="M12 22a7 7 0 0 0 7-7c0-4-3-6-4-10-2 2-3 4-3 6-1-1-2-2-2-4-2 2-5 5-5 8a7 7 0 0 0 7 7z"/>',
 "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
 "list": '<path d="M9 6h11M9 12h11M9 18h11M4 6h.01M4 12h.01M4 18h.01"/>',
 "share": '<path d="M4 12v7a1 1 0 0 0 1 1h14a1 1 0 0 0 1-1v-7M12 3v12M7 8l5-5 5 5"/>',
 "calc": '<rect x="5" y="2" width="14" height="20" rx="2"/><path d="M8 6h8M8 11h.01M12 11h.01M16 11h.01M8 15h.01M12 15h.01M16 15h.01M8 18h8"/>',
 "bolt": '<path d="M13 2 4 14h7l-1 8 9-12h-7z"/>',
 "scale": '<path d="M12 3v18M5 21h14M6 7h12M6 7l-3 7a3 3 0 0 0 6 0zM18 7l-3 7a3 3 0 0 0 6 0z"/>',
}
def ic(name, cls="ic"):
    return f'<svg class="{cls}" viewBox="0 0 24 24" aria-hidden="true" focusable="false">{ICONS[name]}</svg>'
SVC_IC = {"solceller": "sun", "varmepumpe": "pump"}
NAT_IC = {"/solceller/pris/": "coins", "/solceller/med-batteri/": "battery", "/varmepumpe/pris/": "coins", "/varmepumpe/tilskud/": "gift", "/beregner/": "calc", "/elpris/": "bolt"}
NAT_IC.update({u: i for svc in TOPIC_NAV for u, _, _, i in TOPIC_NAV[svc]})

def slug(t):
    t = strip(t).lower()
    for a, b in (("æ", "ae"), ("ø", "oe"), ("å", "aa")): t = t.replace(a, b)
    return re.sub(r"[^a-z0-9]+", "-", t).strip("-")[:48]

LOGO = '<svg class="logo-mark" width="30" height="30" viewBox="0 0 32 32" aria-hidden="true"><rect width="32" height="32" rx="9" fill="#0b4f43"/><circle cx="16" cy="16" r="5.5" fill="#f5b700"/><path d="M16 4.5v3M16 24.5v3M4.5 16h3M24.5 16h3M7.9 7.9l2.1 2.1M22 22l2.1 2.1M7.9 24.1 10 22M22 10l2.1-2.1" stroke="#f5b700" stroke-width="2" stroke-linecap="round"/></svg>'

# ---------- layout ----------
def menu(section):
    def cur(k): return ' aria-current="true"' if section == k else ""
    def dd(key, href, label, panel):
        return (f'<li class="dd"><div class="dd-row"><a class="top" href="{href}"{cur(key)}>{label}</a>'
                f'<button class="dd-t" type="button" aria-expanded="false" aria-label="Vis undermenu: {label}">{ic("chev")}</button></div>'
                f'<div class="panel">{panel}</div></li>')
    def svc_panel(svc):
        s = SERVICES[svc]
        cities = "".join(f'<li><a href="{p_city(svc, c)}">{ic("pin")}{esc(CITIES[c]["name"])}</a></li>' for c in CITIES)
        guides = "".join(f'<li><a href="{u}">{ic(NAT_IC[u])}{esc(t)}</a></li>' for u, t, _ in NAT_LINKS[svc] + [CALC, EL_URL])
        sub = "Lokale regler og byggetilladelse" if svc == "solceller" else "Fjernvarme eller varmepumpe pr. by"
        return (f'<div class="pcol"><p class="ph">{esc(s["name"])} i din by</p><ul class="pcities">{cities}</ul></div>'
                f'<div class="pcol"><p class="ph">Guides</p><ul>{guides}<li><a href="{p_hub(svc)}">{ic("list")}Overblik: alle {len(CITIES)} byer</a></li></ul>'
                f'<p class="pnote">{esc(sub)} finder du på hver byside.</p></div>')
    byer = "".join(f'<li><span class="cn">{esc(CITIES[c]["name"])}</span><a href="{p_city("solceller", c)}">{ic("sun")}Solceller</a><a href="{p_city("varmepumpe", c)}">{ic("pump")}{"Varmepumpe" if has_vp(c) else "Fjernvarme/VP"}</a></li>' for c in CITIES)
    gl = lambda lst: "".join(f'<li><a href="{u}">{ic(NAT_IC[u])}{esc(t)}</a></li>' for u, t, _ in lst)
    return ('<ul class="mnav">'
            + dd("solceller", "/solceller/", "Solceller", svc_panel("solceller"))
            + dd("varmepumpe", "/varmepumpe/", "Varmepumpe", svc_panel("varmepumpe"))
            + dd("byer", "/#byer", "Byer", f'<p class="ph">Vælg by og ydelse</p><ul class="pbyer">{byer}</ul>')
            + dd("guides", "/#guides", "Guides", f'<p class="ph">Solceller</p><ul>{gl(NAT_LINKS["solceller"])}</ul><p class="ph">Varmepumpe</p><ul>{gl(NAT_LINKS["varmepumpe"])}</ul><p class="ph">Værktøj og om os</p><ul>{gl([CALC, EL_URL])}</ul><p class="ph">Om os</p><ul><li><a href="/om-os/">{ic("shield")}Om os og metode</a></li></ul>')
            + '</ul>')

OG_USED = {}
def og_spec(path, title):
    parts = path.strip("/").split("/")
    if path == "/": return "forside", "Solceller og varmepumpe: lokale regler og tilbud i din by", "Regler, fjernvarme, tilskud og priser med kilder", "both"
    if path in NATIONAL:
        g = NATIONAL[path]; return "guide-" + "-".join(parts), g["h1"], ("Tilbud · " if path.endswith("/tilbud/") else "Guide · ") + SERVICES[g["svc"]]["name"], "sol" if g["svc"] == "solceller" else "vp"
    if path == "/elpris/": return "elpris", "Elprisen i dag og i morgen", "Spotpris og anslået samlet pris · DK1 og DK2", "both"
    if path == "/beregner/": return "beregner", "Beregner: kan solceller og varmepumpe betale sig?", "Ret selv tallene. Alle antagelser har en kilde.", "both"
    if len(parts) >= 2 and parts[1] in CITIES:
        c = parts[1]; return "by-" + c, f"Solceller og varmepumpe i {CITIES[c]['name']}", f"Regler, fjernvarme og tilbud · {CITIES[c]['kommune']}", "both"
    if len(parts) == 1 and parts[0] in SERVICES:
        return "hub-" + parts[0], SERVICES[parts[0]]["hub_title"], f"Lokale regler og tilbud i {len(CITIES)} byer", "sol" if parts[0] == "solceller" else "vp"
    return "energitjekket", BRAND, BRAND_TAGLINE, "both"

def head(title, desc, path, graph, noindex=False, section=None, cta=("/#byer", "Få tilbud")):
    ok, ot, osub, motif = og_spec(path, title)
    OG_USED[ok] = (ot, osub, motif)
    og_img = f"{SITE_URL}/og/{ok}.png"
    robots = '<meta name="robots" content="noindex,follow">' if noindex else '<meta name="robots" content="index,follow,max-image-preview:large">'
    ld = f'<script type="application/ld+json">{json.dumps({"@context":"https://schema.org","@graph":graph}, ensure_ascii=False)}</script>' if graph else ""
    return f"""<!doctype html>
<html lang="da">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{url(path)}">
{robots}
<meta property="og:type" content="website">
<meta property="og:locale" content="da_DK">
<meta property="og:site_name" content="{esc(BRAND)}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{url(path)}">
<meta property="og:image" content="{og_img}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{esc(ot)}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(title)}">
<meta name="twitter:description" content="{esc(desc)}">
<meta name="twitter:image" content="{og_img}">
<meta name="twitter:image:alt" content="{esc(ot)}">
<meta name="theme-color" content="#0b4f43">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="/assets/style.css">
<script>document.documentElement.classList.add('js')</script>
{ld}
</head>
<body>
<a class="skip" href="#main">Spring til indhold</a>
<header class="site-header"><div class="wrap hdr">
<a class="logo" href="/" aria-label="{esc(BRAND)} – forside">{LOGO}<span>{esc(BRAND)}</span></a>
<button class="menu-btn" type="button" aria-expanded="false" aria-controls="menu">{ic("menu", "ic i-open")}{ic("close", "ic i-close")}<span>Menu</span></button>
<nav id="menu" class="menu" aria-label="Hovedmenu">{menu(section)}<a class="btn hdr-cta" href="{cta[0]}">{esc(cta[1])}</a></nav>
</div></header>
"""

def footer(mcta=None):
    sol = "".join(f'<li><a href="{p_city("solceller", c)}">Solceller {esc(CITIES[c]["name"])}</a></li>' for c in CITIES)
    reg = "".join(f'<li><a href="{p_reg(c)}">Regler {esc(CITIES[c]["name"])}</a></li>' for c in CITIES)
    vp = "".join(f'<li><a href="{p_city("varmepumpe", c)}">Varmepumpe {esc(CITIES[c]["name"])}</a></li>' for c in CITIES if has_vp(c))
    fv = "".join(f'<li><a href="{p_fv(c)}">Fjernvarme vs. varmepumpe {esc(CITIES[c]["name"])}</a></li>' for c in CITIES)
    guides = "".join(f'<li><a href="{u}">{esc(t)}</a></li>' for svc in NAT_LINKS for u, t, _ in NAT_LINKS[svc] + ([CALC, EL_URL] if svc == "varmepumpe" else []))
    bar = (f'<div class="mcta" id="mcta"><a class="btn btn-lg" href="{mcta[0]}">{esc(mcta[1])}{ic("arrow")}</a></div>') if mcta else ""
    return f"""<footer class="site-footer"><div class="wrap">
<div class="fbrand"><a class="logo logo-inv" href="/">{LOGO}<span>{esc(BRAND)}</span></a><p>{esc(BRAND_TAGLINE)}.</p>
<p class="small">{esc(BRAND)} er en formidlingstjeneste. Vi er ikke selv installatør og udfører ikke arbejdet. {esc(TRUST_TEXT)}</p>
<p class="small nap">{esc(COMPANY_NAME)} · <a href="{CVR_URL}" target="_blank" rel="noopener nofollow">CVR {esc(CVR)}</a><br>{esc(COMPANY_ADDRESS)}<br>{esc(CONTACT_EMAIL)} · {esc(CONTACT_PHONE)}</p></div>
<nav class="fmap" aria-label="Sitemap">
<div><p class="fh"><a href="/solceller/">Solceller</a></p><ul>{sol}</ul></div>
<div><p class="fh">Solceller: lokale regler</p><ul>{reg}</ul></div>
<div><p class="fh"><a href="/varmepumpe/">Varmepumpe</a></p><ul>{vp}</ul></div>
<div><p class="fh">Fjernvarme eller varmepumpe</p><ul>{fv}</ul></div>
<div><p class="fh">Guides</p><ul>{guides}</ul><p class="fh">{esc(BRAND)}</p><ul><li><a href="/">Forside</a></li><li><a href="/om-os/">Om os og metode</a></li><li><a href="/privatlivspolitik/">Privatlivspolitik</a></li></ul></div>
</nav>
<p class="small muted fbase">Tal og regler senest faktatjekket {esc(LAST_CHECKED)}. Ingen cookies. Vi måler kun anonym, samlet besøgsstatistik.</p>
</div></footer>
{bar}
<script src="/assets/form.js" defer></script>
{ANALYTICS_HTML}
</body></html>"""

def breadcrumbs(items):
    lis = []
    for i, (name, path) in enumerate(items):
        if i == len(items) - 1: lis.append(f'<li aria-current="page">{esc(name)}</li>')
        else: lis.append(f'<li><a href="{path}">{esc(name)}</a></li>')
    return f'<nav class="crumbs" aria-label="Brødkrumme"><ol>{"".join(lis)}</ol></nav>'

# ---------- komponenter ----------
def rcard(icon, title, text, href, cls=""):
    return f'<a class="rcard {cls}" href="{href}"><span class="rc-ic">{ic(icon)}</span><span class="rc-b"><strong>{esc(title)}</strong><span>{esc(text)}</span></span>{ic("arrow", "ic rc-go")}</a>'

def chips(items, current=None):
    out = []
    for label, href in items:
        if href == current: out.append(f'<li><span class="chip on" aria-current="page">{esc(label)}</span></li>')
        else: out.append(f'<li><a class="chip" href="{href}">{esc(label)}</a></li>')
    return f'<ul class="chips">{"".join(out)}</ul>'

def toc(items):
    lis = "".join(f'<li><a href="#{i}">{esc(t)}</a></li>' for i, t in items)
    return f'<nav class="toc" aria-label="På denne side"><p class="toc-h">På denne side</p><ol>{lis}</ol></nav>'

def side_cta(svc, c=None):
    n = CITIES[c]["name"] if c else ""
    what = "solceller" if svc == "solceller" else "varmepumpe"
    return f"""<div class="side-cta"><p class="sc-h">Få tilbud på {what}{(' i ' + esc(n)) if n else ''}</p>
<ul class="mini-usp"><li>{ic("check")}Gratis og uforpligtende</li><li>{ic("check")}Tager ca. 1 minut</li><li>{ic("check")}Du vælger selv</li></ul>
<a class="btn btn-block" href="#lead-form">Få gratis tilbud</a></div>"""

def layout(toc_items, inner, svc, c=None):
    return f"""<div class="wrap layout">
<aside class="side">{toc(toc_items)}{side_cta(svc, c)}</aside>
<div class="content">{inner}</div>
</div>"""

def section(id_, h, inner, cls=""):
    c = f' class="{cls}"' if cls else ""
    return f'<section id="{id_}"{c}><h2>{h}</h2>{inner}</section>'

def faq_html(faqs):
    out = ['<div class="faq">']
    for q, a, k in faqs:
        out.append(f'<details><summary>{esc(q)}<span class="pm" aria-hidden="true"></span></summary><div class="fa"><p>{a} {src_links(k)}</p></div></details>')
    out.append("</div>")
    return "".join(out)

# ---------- formular ----------
ON = ' class="on"'
def opt(name, value, label, req=False, kind="radio"):
    r = " required" if req else ""
    return f'<label class="opt"><input type="{kind}" name="{name}" value="{value}"{r}><span class="ob">{ic("check", "ic oc")}{label}</span></label>'

def form(svc, c=None):
    cname = CITIES[c]["name"] if c else ""
    if svc == "solceller":
        labels = ["Bolig", "Forbrug", "Kontakt"]
        step1 = f"""<fieldset class="step" data-step="1"><legend>Hvilken bolig drejer det sig om?</legend>
<div class="opts">{opt("boligtype","parcelhus","Parcelhus",True)}{opt("boligtype","raekkehus","Række- eller dobbelthus")}{opt("boligtype","landejendom","Landejendom")}{opt("boligtype","sommerhus","Sommerhus")}</div>
<label class="fld">Tagtype <span class="opt-l">(valgfrit)</span><select name="tagtype"><option value="">Vælg</option><option>Tegl</option><option>Betontagsten</option><option>Eternit/fibercement</option><option>Stål/tagplader</option><option>Fladt tag (tagpap)</option><option>Ved ikke</option></select></label>
</fieldset>
<fieldset class="step" data-step="2"><legend>Dit forbrug og ønsker <span class="opt-l">(alt er valgfrit)</span></legend>
<label class="fld">Årligt elforbrug<select name="elforbrug"><option value="">Vælg</option><option>Under 4.000 kWh</option><option>4.000-6.000 kWh</option><option>6.000-10.000 kWh</option><option>Over 10.000 kWh</option><option>Ved ikke</option></select></label>
<div class="opts">{opt("oensker","batteri","Interesseret i batteri",kind="checkbox")}{opt("oensker","elbil","Har eller får elbil",kind="checkbox")}{opt("oensker","varmepumpe","Har eller får varmepumpe",kind="checkbox")}</div>
<label class="fld">Hvornår vil du gerne have anlægget?<select name="tidshorisont"><option value="">Vælg</option><option>Inden for 3 måneder</option><option>3-6 måneder</option><option>Senere / undersøger bare</option></select></label>
</fieldset>"""
        produkt = "solceller"
    else:
        labels = ["Varme", "Huset", "Kontakt"]
        step1 = f"""<fieldset class="step" data-step="1"><legend>Hvordan varmer du huset op i dag?</legend>
<div class="opts">{opt("varmekilde","oliefyr","Oliefyr",True)}{opt("varmekilde","naturgas","Naturgas")}{opt("varmekilde","elvarme","Elvarme (paneler)")}{opt("varmekilde","biokedel","Træpille-/biokedel")}{opt("varmekilde","andet","Andet / ved ikke")}</div>
<label class="fld">Ligger boligen i et fjernvarmeområde? <span class="opt-l">(valgfrit)</span><select name="fjernvarme"><option value="">Vælg</option><option>Nej</option><option>Ja / planlagt</option><option>Ved ikke</option></select></label>
</fieldset>
<fieldset class="step" data-step="2"><legend>Om huset <span class="opt-l">(alt er valgfrit)</span></legend>
<label class="fld">Boligareal (m²)<input type="number" name="areal" inputmode="numeric" min="20" max="1000" placeholder="fx 140"></label>
<label class="fld">Varmesystem<select name="varmesystem"><option value="">Vælg</option><option>Radiatorer</option><option>Gulvvarme</option><option>Begge</option><option>Ved ikke</option></select></label>
<label class="fld">Hvornår vil du gerne skifte?<select name="tidshorisont"><option value="">Vælg</option><option>Inden for 3 måneder</option><option>3-6 måneder</option><option>Senere / undersøger bare</option></select></label>
</fieldset>"""
        produkt = "luft til vand-varmepumper"
    stepper = "".join(f'<li{ON if i == 0 else ""}><span>{i+1}</span>{esc(l)}</li>' for i, l in enumerate(labels))
    return f"""<form class="lead" id="lead-form" action="#" method="post" novalidate data-service="{svc}" data-city="{esc(cname)}" aria-label="Få tilbud">
<div class="lead-h"><span class="lead-ic">{ic(SVC_IC[svc])}</span><div><strong>Få uforpligtende tilbud{(' i ' + esc(cname)) if cname else ''}</strong><span>Gratis · tager ca. 1 minut · <span class="step-count">3 korte trin</span></span></div></div>
<ol class="stepper" aria-hidden="true">{stepper}</ol>
<div class="progress" aria-hidden="true"><span></span></div>
<input type="hidden" name="service" value="{svc}"><input type="hidden" name="by" value="{esc(cname)}">
{step1}
<fieldset class="step" data-step="3"><legend>Hvordan kan installatøren kontakte dig?</legend>
<div class="row2"><label class="fld">Postnummer<input type="text" name="postnummer" inputmode="numeric" pattern="[0-9]{{4}}" maxlength="4" required autocomplete="postal-code"></label>
<label class="fld">Telefon<input type="tel" name="telefon" required autocomplete="tel" pattern="[0-9 +]{{8,}}"></label></div>
<label class="fld">Fulde navn<input type="text" name="navn" required autocomplete="name"></label>
<label class="fld">E-mail<input type="email" name="email" required autocomplete="email"></label>
<label class="fld">Adresse <span class="opt-l">(valgfrit, hjælper installatøren)</span><input type="text" name="adresse" autocomplete="street-address" maxlength="150"></label>
<div class="hp" aria-hidden="true"><label>Lad dette felt være tomt<input type="text" name="website" tabindex="-1" autocomplete="off"></label></div>
<label class="consent"><input type="checkbox" name="samtykke" value="ja" required> <span class="consent-txt">Ja tak. Jeg giver {esc(COMPANY_NAME)} ({esc(BRAND)}) samtykke til at give mit navn, telefonnummer, e-mail, postnummer, eventuelle adresse og mine svar videre til <strong>én udvalgt installatør</strong> i mit område, så installatøren kan kontakte mig <strong>på telefon og e-mail</strong> med et tilbud på {produkt}. Så snart mine oplysninger er sendt, får jeg en e-mail med installatørens navn og CVR-nummer. Jeg kan altid trække samtykket tilbage ved at skrive til {esc(CONTACT_EMAIL)}.</span></label>
<p class="small muted">Vi bruger kun dine oplysninger til at formidle din forespørgsel og sletter dem efter 12 måneder. Læs <a href="/privatlivspolitik/">privatlivspolitikken</a>. {esc(BRAND)} er en formidlingstjeneste og ikke selv installatør.</p>
</fieldset>
<div class="nav-btns"><button type="button" class="btn ghost" data-prev>Tilbage</button><button type="button" class="btn" data-next>Næste{ic("arrow")}</button><button type="submit" class="btn" data-submit>Send min forespørgsel{ic("arrow")}</button></div>
<p class="form-foot">{ic("shield")}Gratis og uforpligtende. Du vælger selv, om du vil sige ja til tilbuddet.</p>
<div class="form-msg" role="status" aria-live="polite"></div>
</form>"""

# ---------- fælles sektioner ----------
def steps_html(what):
    return f"""<ol class="steps">
<li><span class="st-ic">{ic("list")}</span><strong>Fortæl kort om dit hus</strong><span>Udfyld formularen. Det tager omkring et minut, og det er gratis og uforpligtende.</span></li>
<li><span class="st-ic">{ic("share")}</span><strong>Vi formidler din forespørgsel</strong><span>Vi vælger én installatør, der dækker dit område, og sender din forespørgsel dertil. Du får en e-mail med firmaets navn og CVR-nummer, så snart det er sket.</span></li>
<li><span class="st-ic">{ic("scale")}</span><strong>Få et tilbud og vælg selv</strong><span>Installatøren kontakter dig og giver et uforpligtende tilbud på {what}. Du bestemmer selv, om du vil sige ja.</span></li>
</ol>"""

def how_it_works(svc):
    what = "solceller" if svc == "solceller" else "en luft til vand-varmepumpe"
    return f"""<section id="saadan-virker-det"><h2>Sådan virker det</h2>
{steps_html(what)}
<p class="note"><strong>Vigtigt:</strong> {esc(BRAND)} er en formidlingstjeneste og ikke en installatør. {esc(TRUST_TEXT)}</p>
</section>"""

def short_how(svc):
    what = "solceller" if svc == "solceller" else "en luft til vand-varmepumpe"
    return f"""<section id="saadan-virker-det" class="how-short"><h2>Sådan får du tilbud</h2><p>Udfyld formularen. Vi sender din forespørgsel til én udvalgt installatør i dit område, og du får en e-mail med firmaets navn og CVR-nummer, så snart det er sket. Installatøren giver et uforpligtende tilbud på {what}, og du vælger selv.</p>
<a class="btn" href="#lead-form">Få gratis tilbud{ic("arrow")}</a></section>"""

def upd_html(upd):
    return f'Opdateret <time datetime="{upd[1]}">{esc(upd[0])}</time>'
def trust_line(upd=None, how=True):
    upd = upd or page_upd()
    lnk = ' <a href="#saadan-virker-det">Sådan virker det</a>' if how else ' <a href="/om-os/">Om os</a>'
    return f'<p class="disclose">{ic("shield")}<span>{esc(BRAND)} er en formidlingstjeneste, ikke en installatør. Drevet af {esc(COMPANY_NAME)} · CVR {esc(CVR)} · {upd_html(upd)}.{lnk}</span></p>'

def hero(crumbs, h1, intro, svc, c=None, usp=True, eyebrow="", jump=None, upd=None):
    u = (f'<ul class="usp"><li>{ic("check")}Gratis og uforpligtende</li><li>{ic("check")}Lokale regler og tilskud med kilder</li><li>{ic("check")}Du vælger selv, om du vil sige ja</li></ul>') if usp else ""
    j = f'<a class="txtlink" href="#{jump[0]}">{esc(jump[1])}{ic("chev")}</a>' if jump else ""
    eb = f'<p class="eyebrow">{ic(SVC_IC[svc])}{esc(eyebrow)}</p>' if eyebrow else ""
    return f"""<section class="hero"><div class="wrap hero-grid">
<div class="hero-txt">
{breadcrumbs(crumbs)}
{eb}<h1>{esc(h1)}</h1>
<p class="lead-p">{intro}</p>
{u}
<div class="hero-actions"><a class="btn btn-lg" href="#lead-form">Få gratis tilbud{ic("arrow")}</a>{j}</div>
{trust_line(upd)}
</div>
<div class="hero-form">{form(svc, c)}</div>
</div></section>"""

def guides_block(svc, c):
    n = CITIES[c]["name"]
    teaser = SOL_REG[c]["intro"] if svc == "solceller" else FV_PAGE[c]["intro"]
    sub_ic = "building" if svc == "solceller" else "flame"
    nat = "".join(rcard(NAT_IC[u], t, d, u) for u, t, d in NAT_CORE[svc])
    return f"""<section id="guides"><h2>Guides til {esc(SERVICES[svc]['name_lc'])} i {esc(n)}</h2>
{rcard(sub_ic, sub_label(svc, c), teaser, p_sub(svc, c), "rcard-hl")}
<div class="rgrid">{nat}</div></section>"""

def link_block(svc, c, here="city"):
    """Relaterede sider + byvælger. Ligger i section.links (udelades i lighedsmålingen)."""
    o = OTHER[svc]; n = CITIES[c]["name"]
    other_label = f"Luft til vand-varmepumpe i {n}" if o == "varmepumpe" else f"Solceller i {n}"
    other_txt = ("Overvejer du også at skifte varmekilde? Se fjernvarmestatus og tilskud i " + n + ".") if o == "varmepumpe" else ("Solceller og varmepumpe passer godt sammen. Se reglerne for solceller i " + n + ".")
    cards = []
    if here == "sub" and p_city(svc, c) != p_sub(svc, c):
        cards.append(rcard(SVC_IC[svc], city_label(svc, c), f"Overblik, lokale fakta og tilbud på {SERVICES[svc]['name_lc']} i {n}.", p_city(svc, c)))
    if p_city(o, c) != p_sub(o, c):
        cards.append(rcard(SVC_IC[o], other_label, other_txt, p_city(o, c)))
    cards.append(rcard("building" if o == "solceller" else "flame", sub_label(o, c), f"Den lokale guide til {SERVICES[o]['name_lc']} i {n}.", p_sub(o, c)))
    if here == "sub":
        cards += [rcard(NAT_IC[u], t, d, u) for u, t, d in NAT_CORE[svc]]
    cards.append(rcard("calc", CALC[1], CALC[2], CALC[0] + ("#solceller" if svc == "solceller" else "#varmepumpe")))
    same = [(CITIES[x]["name"], p_city(svc, x)) for x in CITIES]
    subs = [(CITIES[x]["name"], p_sub(svc, x)) for x in CITIES]
    others = [(CITIES[x]["name"], p_city(o, x)) for x in CITIES]
    sub_h = "Regler og byggetilladelse i andre byer" if svc == "solceller" else "Fjernvarme eller varmepumpe i andre byer"
    cur_same = p_city(svc, c) if here == "city" else None
    cur_sub = p_sub(svc, c) if here == "sub" else None
    guides = "".join(f'<li><a href="{u}">{ic(NAT_IC[u])}{esc(t)}</a></li>' for s2 in (svc, o) for u, t, _ in NAT_LINKS[s2])
    return f"""<section class="links" id="mere" aria-labelledby="mere-h"><h2 id="mere-h">Mere om {esc(SERVICES[svc]['name_lc'])} og varmepumper</h2>
<div class="rgrid">{''.join(cards)}</div>
<div class="picker">
<div class="pk"><h3>{ic(SVC_IC[svc])}{esc(SERVICES[svc]['name'])} i andre byer</h3>{chips(same, cur_same)}<a class="more" href="{p_hub(svc)}">Alle byer: {esc(SERVICES[svc]['name_lc'])}{ic("arrow")}</a></div>
<div class="pk"><h3>{ic("building" if svc == "solceller" else "flame")}{esc(sub_h)}</h3>{chips(subs, cur_sub)}</div>
<div class="pk"><h3>{ic(SVC_IC[o])}{esc(SERVICES[o]['name'])} i andre byer</h3>{chips(others)}<a class="more" href="{p_hub(o)}">Alle byer: {esc(SERVICES[o]['name_lc'])}{ic("arrow")}</a></div>
<div class="pk"><h3>{ic("book")}Guides</h3><ul class="glist">{guides}</ul></div>
</div></section>"""

def checklist(svc):
    if svc == "solceller":
        items = ["Størrelse (kWp) og placering på taget", "Samlet pris for anlæg og installation, med arbejdsløn for sig (til håndværkerfradrag)",
                 "Forventet, og helst garanteret, elproduktion i kWh om året", "Garantier på paneler, inverter og arbejde",
                 "Forsikringsmuligheder", "Økonomiberegning med den elpris, der er brugt, og forventet køb og salg af el"]
        extra = "Vælg gerne en VE-godkendt installatør, og bed om garanti for, at taget kan bære anlægget."
        k = ["se_sol"]
    else:
        items = ["Model og energimærke (A++/A+++), som Varmepumpepuljen stiller krav til", "Dimensionering ud fra husets varmebehov og varmesystem",
                 "Samlet pris med arbejdsløn for sig (håndværkerfradrag kan kun bruges, hvis du ikke får tilskud)", "Placering af udedel og forventet støj over for naboer",
                 "Hvad der sker med det gamle fyr, og om radiatorer eller rør skal ændres", "Service, garanti, og hvem der søger tilskud"]
        extra = "Skriv ikke under, før du har tilsagn om tilskud, hvis du søger Varmepumpepuljen."
        k = ["se_vp", "vpp_ens"]
    if svc != "solceller": k = ["se_vp", "vpp_ens", "vpp_faq"]
    lis = "".join(f"<li>{esc(i)}</li>" for i in items)
    return f"""<section id="tjekliste"><h2>Tjekliste: det skal et godt tilbud indeholde</h2><ul class="check">{lis}</ul><p>{esc(extra)} {src_links(k)}</p></section>"""

def blocks_html(blocks):
    out = []
    for b in blocks:
        kind = b[0]
        if kind == "p": out.append(f"<p>{b[1]} {src_links(b[2])}</p>")
        elif kind == "note": out.append(f'<div class="note">{b[1]} {src_links(b[2])}</div>')
        elif kind == "example": out.append(f'<div class="example">{b[1]} {src_links(b[2])}</div>')
        elif kind == "ul": out.append('<ul class="facts">' + "".join(f"<li>{t} {src_links(k)}</li>" for t, k in b[1]) + "</ul>")
        elif kind == "table":
            th = "".join(f"<th>{esc(h)}</th>" for h in b[1])
            rows = "".join("<tr>" + "".join(f"<td>{esc(x)}</td>" for x in r) + "</tr>" for r in b[2])
            out.append(f'<div class="tbl"><table><thead><tr>{th}</tr></thead><tbody>{rows}</tbody></table></div>{src_links(b[3])}')
    return "".join(out)


def ld_page(path, title, desc, crumbs, about=None, upd=None, typ="WebPage"):
    upd = upd or page_upd()
    wp = {"@type": typ, "@id": url(path) + "#webpage", "url": url(path), "name": title, "description": desc, "inLanguage": "da-DK",
          "isPartOf": {"@id": SITE_URL + "/#website"}, "breadcrumb": {"@id": url(path) + "#breadcrumbs"}, "dateModified": upd[1],
          "author": {"@id": SITE_URL + "/#org"}, "publisher": {"@id": SITE_URL + "/#org"},
          "primaryImageOfPage": {"@type": "ImageObject", "url": f"{SITE_URL}/og/{og_spec(path, title)[0]}.png", "width": 1200, "height": 630}}
    if about: wp["about"] = about
    return [ld_org(), wp, {"@type": "WebSite", "@id": SITE_URL + "/#website", "url": SITE_URL + "/", "name": BRAND, "inLanguage": "da-DK", "publisher": {"@id": SITE_URL + "/#org"}},
            ld_breadcrumbs(crumbs)]

def ld_service(path, name, svc, c):
    d = CITIES[c]
    return {"@type": "Service", "@id": url(path) + "#service", "name": name, "serviceType": SERVICES[svc]["service_type"],
            "provider": {"@id": SITE_URL + "/#org"}, "areaServed": {"@type": "City", "name": d["name"], "containedInPlace": {"@type": "AdministrativeArea", "name": d["kommune"]}},
            "description": "Formidling af uforpligtende tilbud fra installatører. " + BRAND + " udfører ikke selv arbejdet."}


def local_snapshot(svc, c):
    n = CITIES[c]["name"]
    if svc == "solceller":
        return f"""<section id="pris"><h2>Pris på solceller i {esc(n)}</h2><p>Vi har ikke fundet kilder, der viser en særlig pris i {esc(n)}. Tag, anlægsstørrelse og installatør afgør prisen. Et 6 kWp-anlæg til et parcelhus koster typisk ca. 90.000-95.000 kr. inkl. montering. {src_links(["es_sol"])} Se priser pr. kWp og m², ekstraposter og tilbagebetaling i <a href="/solceller/pris/">guiden til solceller pris 2026</a>, og om et <a href="/solceller/med-batteri/">batteri</a> kan betale sig.</p></section>"""
    v, pn, pris, mwh = FV_PRICES[c][0]
    return f"""<section id="pris"><h2>Fjernvarmeprisen i {esc(n)} og prisen på en varmepumpe</h2>
<p>Hos {esc(v)} koster fjernvarme til et standardhus på 130 m² <strong>{pris} kr. om året</strong> inkl. moms. Landsgennemsnittet er {FV_AVG} kr. {src_links(["ft_pris", "wg_pris"])}</p>
<p>Sammenlign med <a href="{p_fv(c)}">de andre værker omkring {esc(n)}</a>, <a href="/varmepumpe/pris/">prisen på en varmepumpe</a> og <a href="/varmepumpe/tilskud/">Varmepumpepuljen</a>.</p></section>"""



# ---------- v4: lokale datablokke (PVGIS + Danmarks Statistik) ----------
MONTHS = ["jan", "feb", "mar", "apr", "maj", "jun", "jul", "aug", "sep", "okt", "nov", "dec"]
SOL_PROD_SRC = {"vejle": ["pv_vejle", "pvo_vejle", "pvv_vejle"], "esbjerg": ["pv_esbjerg", "esb_sol"], "horsens": ["pv_horsens", "pvo_horsens", "hor_sol"], "randers": ["pv_randers"]}
SOL_HOMES_SRC = {"odense": ["ode_sol"], "randers": ["ran_sol"], "esbjerg": ["bolius_mont"]}
VP_HEAT_SRC = {"kolding": ["kol_chr"], "aalborg": ["aal_fv"], "randers": ["verdo_omr"], "horsens": ["hor_fv"]}
SOL_PROD_SRC.update(L.SOL_PROD_SRC_NEW); SOL_HOMES_SRC.update(L.SOL_HOMES_SRC_NEW); VP_HEAT_SRC.update(L.VP_HEAT_SRC_NEW)

def tbl(head, rows, cls=""):
    th = "".join(f"<th>{h}</th>" for h in head)
    tr = "".join("<tr>" + "".join(f"<td>{x}</td>" for x in r) + "</tr>" for r in rows)
    return f'<div class="tbl {cls}"><table><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></div>'

def chart_data(kind, c):
    if kind == "heat":
        H = L.HEAT[c]; T = L.hs(c); D = L.HEAT["dk"]; TD = L.hs("dk")
        return [(lab.split(" (")[0], 100 * H[k] / T, 100 * D[k] / TD) for k, lab in L.VP_HEAT_ROWS]
    return [m * 6 for m in L.PV[c]["months"]]
def chart_fig(kind, c):
    n = L.NAMES[c]; k = CITIES[c]["kommune"]
    if kind == "heat":
        rows = chart_data("heat", c)
        alt = f"Søjlediagram: opvarmning af huse i {k} mod hele landet. " + "; ".join(f"{l} {L.pct(a, 100, 1)} mod {L.pct(b, 100, 1)}" for l, a, b in rows) + "."
        src, w, h, cap = f"/assets/charts/opvarmning-{c}.svg", 640, 64 + 52 * len(rows) + 16, f"Andel af husene i {esc(k)} pr. opvarmningsform, sammenlignet med hele landet. Vores grafik ud fra Danmarks Statistik, BOL102 (2026)."
    else:
        m = chart_data("sun", c); top = max(range(12), key=lambda i: m[i])
        alt = f"Søjlediagram: et sydvendt 6 kWp-anlæg i {n} giver ca. {L.tal(sum(m))} kWh om året, mest i {MONTHS[top]} (ca. {L.tal(m[top])} kWh) og mindst i {MONTHS[min(range(12), key=lambda i: m[i])]} (ca. {L.tal(min(m))} kWh)."
        src, w, h, cap = f"/assets/charts/solproduktion-{c}.svg", 640, 300, f"Produktion pr. måned for et sydvendt 6 kWp-anlæg (35°) i {esc(n)}. Vores grafik ud fra PVGIS 5.3."
    return f'<figure class="chart"><img src="{src}" width="{w}" height="{h}" alt="{esc(alt)}" loading="lazy" decoding="async"><figcaption>{cap}</figcaption></figure>'

def sol_prod_html(c):
    p = L.PV[c]; h, txt = L.SOL_PROD[c]
    rows = [(f"Syd, 35°", L.tal(p["syd"]), L.tal(p["syd"] * 6)), ("Øst, 35°", L.tal(p["oest"]), L.tal(p["oest"] * 6)), ("Vest, 35°", L.tal(p["vest"]), L.tal(p["vest"] * 6))]
    mv = [L.tal(m * 6) for m in p["months"]]
    months = '<div class="mgrid">' + tbl(MONTHS[:6], [mv[:6]], "tbl-months") + tbl(MONTHS[6:], [mv[6:]], "tbl-months") + '</div>'
    src = SOL_PROD_SRC.get(c, [f"pv_{c}"])
    return f"""<section id="produktion"><h2>{esc(h)}</h2><p>{txt()} {src_links(src)}</p>
{tbl(["Tagets retning", "kWh pr. kWp om året", "6 kWp-anlæg, kWh om året"], rows)}
{chart_fig("sol", c)}
<p class="small">Sydvendt 6 kWp-anlæg i {esc(L.NAMES[c])}, kWh pr. måned:</p>{months}
<p class="small muted">Beregnet i PVGIS 5.3 (strålingsdata {esc(p['db'])}) for {esc(L.NAMES[c])} by med 14 % systemtab. Skygge og din tagflade betyder mere end byen. {src_links(["pvgis"])}</p>
<p>Et 6 kWp-anlæg koster typisk ca. 90.000-95.000 kr. inkl. montering. {src_links(["es_sol"])} Se <a href="/solceller/pris/">priser og tilbagebetaling</a> og om et <a href="/solceller/med-batteri/">batteri</a> kan betale sig.</p></section>"""

def sol_roof_html(c):
    h, txt, src = L.SOL_ROOF[c]; R = L.ROOF[c]; D = L.ROOF["dk"]
    top = sorted(R["T"].items(), key=lambda kv: -kv[1])[:5]
    lab = {"06": "Fibercement/eternit (inkl. asbest)", "08": "Betontagsten (cementsten)", "10": "Tegl", "04": "Tagpap med hældning", "02": "Fladt tag (built-up)", "12": "Metalplader", "16": "Fibercement, asbestfri", "14": "Stråtag"}
    rows = [(esc(lab.get(k, L.ROOF_LABELS[k])), L.pct(v, R["tot"], 1), L.pct(D["T"][k], D["tot"], 1)) for k, v in top]
    return f"""<section id="tage"><h2>{esc(h)}</h2><p>{txt()} {src_links(src)}</p>
{tbl(["Tagtype", esc(CITIES[c]["kommune"]), "Hele landet"], rows)}</section>"""

def sol_homes_html(c):
    towns = " · ".join(f"{esc(n)} {L.tal(v)}" for n, v in L.TOWNS[c][:8])
    return f"""<section id="boliger"><h2>{esc(L.SOL_HOMES_H[c])}</h2><p>{L.SOL_HOMES[c]()} {src_links(["dst_bol101"] + SOL_HOMES_SRC.get(c, []))}</p>
<p class="small"><strong>Største byer i {esc(CITIES[c]['kommune'])}</strong> (indbyggere 1. januar 2026): {towns}. {src_links(["dst_by3"])}</p>{cross_link_html(c)}</section>"""

def cross_link_html(c):
    """Én inline-tekstlink til administratortjekket.dk for byer med en live byside dér (CROSS_CITY_LINKS i config.py)."""
    p = CROSS_CITY_LINKS.get(c)
    if not p: return ""
    n = CITIES[c]["name"]
    return f'\n<p class="small">Bor du i en ejer- eller andelsboligforening i {esc(n)}, og skal solceller på foreningens tag? Se også <a href="{CROSS_SITE_URL}{p}">ejendomsadministration i {esc(n)}</a> på Administratortjekket.</p>'

def vp_heat_html(c):
    h, txt = L.VP_HEAT[c]; H = L.HEAT[c]; T = L.hs(c); D = L.HEAT["dk"]; TD = L.hs("dk")
    rows = [(esc(lab), L.tal(H[k]), L.pct(H[k], T, 1), L.pct(D[k], TD, 1)) for k, lab in L.VP_HEAT_ROWS]
    adv = ""
    if c in L.VP_ADVICE:
        a, k = L.VP_ADVICE[c]
        adv = f'<div class="note note-ic">{ic("clock")}<div><strong>Lokal rådgivning:</strong> {a} {src_links(k)}</div></div>'
    return f"""<section id="opvarmning"><h2>{esc(h)}</h2><p>{txt()} {src_links(["dst_bol102"] + VP_HEAT_SRC.get(c, []))}</p>
{chart_fig("heat", c)}
{tbl(["Opvarmning", "Huse", "Andel", "Hele landet"], rows)}
<p class="small muted">Beboede parcel- og stuehuse samt række-, kæde- og dobbelthuse, 2026 ({L.tal(T)} i alt).</p>{adv}</section>"""

def vp_towns_html(c):
    pop = dict(L.TOWNS[c])
    rows = [(esc(t), L.tal(pop[t]) if t in pop else "–", f"{esc(st)} {src_links(k)}") for t, st, k in L.VP_TOWNS[c]]
    return f"""<section id="lokale-byer"><h2>By for by: fjernvarme i {esc(CITIES[c]['kommune'])}</h2>
{tbl(["By", "Indbyggere 2026", "Fjernvarme"], rows, "tbl-towns")}{src_links(["dst_by3"])}
<p>{esc(L.VP_TOWNS_NOTE[c])}</p></section>"""

# ---------- sider ----------
def city_page(svc, c):
    d = CITIES[c]; n = d["name"]; path = p_city(svc, c)
    if svc == "solceller":
        title = f"Solceller {n} 2026: regler, pris og tilbud | {BRAND}"
        desc = f"Solceller i {n}: hvad {d['kommune']} kræver, hvem du kontakter, og hvad et anlæg koster i 2026. Få uforpligtende tilbud fra installatører."
        h1 = f"Solceller i {n}"
        intro, facts = d["sol_intro"], d["sol_facts"]
        xf = [(q, a(), k) for q, a, k in L.SOL_XFAQ.get(c, [])]
        lfaq = d["sol_faq"] + xf + [SOL_REG[c]["faq"][SOL_BORROW[c]]]
        local_h = f"Det skal du vide om solceller i {n}"
        order = L.SOL_ORDER[c]
    else:
        title = f"Varmepumpe {n}: luft til vand, tilskud og pris | {BRAND}"
        desc = f"Luft til vand-varmepumpe i {n}: fjernvarmestatus i {d['kommune']}, lokal fjernvarmepris og tilskud på 27.000 kr. (frist 30/11 2026). Få tilbud."
        h1 = f"Luft til vand-varmepumpe i {n}"
        intro, facts = d["vp_intro"], d["vp_facts"]
        xf = [(q, a(), k) for q, a, k in L.VP_XFAQ.get(c, [])]
        lfaq = d["vp_faq"] + xf + ([FV_PAGE[c]["faq"][VP_BORROW[c]]] if VP_BORROW[c] is not None else [])
        local_h = f"Fjernvarme eller varmepumpe i {n}?"
        order = L.VP_ORDER[c]
    faqs = lfaq
    crumbs = [("Forside", "/"), (SERVICES[svc]["name"], p_hub(svc)), (n, path)]
    graph = ld_page(path, title, desc, crumbs, upd=page_upd(c=c)) + [ld_service(path, h1, svc, c), ld_faq(path, faqs)]
    ck = "sol" if svc == "solceller" else "vp"
    contacts_html = f'<div class="note note-ic">{ic("building")}<div><strong>Hvem kan svare på spørgsmål om din adresse i {esc(n)}?</strong><ul class="plain">' + "".join(f'<li>{esc(a)}: {esc(b)} {src_links([k])}</li>' for a, b, k in CONTACTS[c][ck]) + '</ul></div></div>'
    facts_html = "".join(f"<li>{t} {src_links(k)}</li>" for t, k in facts)
    blocks = {
        "lokalt": (f"""<section id="lokalt"><h2>{esc(local_h)}</h2><ul class="facts">{facts_html}</ul>
{contacts_html}
<p class="small muted">Faktatjekket {esc(checked_c(c))}. Regler og puljer kan ændre sig, så tjek altid {esc(d['kommune'])}s egne sider, før du skriver under.</p></section>""", "Lokale regler og fakta"),
        "guides": (guides_block(svc, c), "Guides"),
        "faq": (f"""<section id="faq"><h2>Ofte stillede spørgsmål om {esc(SERVICES[svc]['name_lc'])} i {esc(n)}</h2>{faq_html(faqs)}</section>""", "Spørgsmål og svar"),
    }
    if svc == "solceller":
        blocks["produktion"] = (sol_prod_html(c), "Produktion i " + n)
        blocks["tage"] = (sol_roof_html(c), "Tagene i kommunen")
        blocks["boliger"] = (sol_homes_html(c), "Boliger og byer")
    else:
        blocks["opvarmning"] = (vp_heat_html(c), "Sådan varmes husene op")
        blocks["lokale-byer"] = (vp_towns_html(c), "By for by")
        blocks["pris"] = (local_snapshot(svc, c), "Fjernvarmepris")
    inner = "\n".join(blocks[k][0] for k in order) + f"\n{el_box(c, svc)}\n{short_how(svc)}\n{link_block(svc, c)}"
    tocs = [(k, blocks[k][1]) for k in order] + [("saadan-virker-det", "Sådan får du tilbud"), ("mere", "Andre byer og guides")]
    body = f"""{head(title, desc, path, graph, section=svc, cta=("#lead-form", "Få tilbud"))}
<main id="main">
{hero(crumbs, h1, esc(intro), svc, c, eyebrow=f"{'Solceller' if svc == 'solceller' else 'Varmepumpe'} · {d['kommune']}", jump=("lokalt", f"Se hvad der gælder i {n}"), upd=page_upd(c=c))}
{layout(tocs, inner, svc, c)}
</main>
{footer(("#lead-form", f"Få gratis tilbud i {n}"))}"""
    return path, body

def reg_page(c):
    d = CITIES[c]; n = d["name"]; r = SOL_REG[c]; path = p_reg(c)
    title = f"Solceller {d['kommune']}: regler og byggetilladelse | {BRAND}"
    if len(title) > 68: title = f"Solceller {d['kommune']}: regler og tilladelse | {BRAND}"
    desc = f"Skal du søge byggetilladelse til solceller i {d['kommune']}? Kommunens regler, undtagelser, BBR og kontakt, med kilder. Opdateret {checked_c(c)}."
    h1 = f"Solceller i {d['kommune']}: regler og byggetilladelse"
    crumbs = [("Forside", "/"), ("Solceller", p_hub("solceller")), (n, p_city("solceller", c)), ("Regler og byggetilladelse", path)]
    faqs = [f for i, f in enumerate(r["faq"]) if i != SOL_BORROW[c]]
    graph = ld_page(path, title, desc, crumbs, about={"@type": "Thing", "name": "Byggetilladelse til solceller i " + d["kommune"]}, upd=page_upd(c=c)) + [ld_service(path, f"Solceller i {n}", "solceller", c), ld_faq(path, faqs)]
    ids = [slug(h) for h, _ in r["sections"]]
    secs = "".join(f'<section id="{i}"><h2>{esc(h)}</h2>{blocks_html(b)}</section>' for i, (h, b) in zip(ids, r["sections"]))
    inner = f"""{secs}
<p>{esc(L.reg_age_note(c, d['kommune'])[0])} {src_links(["dst_bol101"] + L.reg_age_note(c, d['kommune'])[1])}</p>
<p class="small muted">Faktatjekket {esc(checked_c(c))} på {esc(d['kommune'])}s egne sider. Reglerne kan ændre sig, og lokalplanen for din adresse går altid forud.</p>
<section id="faq"><h2>Spørgsmål om solceller og tilladelser i {esc(n)}</h2>{faq_html(faqs)}</section>
<p>Se også <a href="{p_city('solceller', c)}">solceller i {esc(n)}</a>, <a href="/solceller/pris/">priser</a> og <a href="/solceller/med-batteri/">batteri</a>.</p>
{short_how("solceller")}
{link_block("solceller", c, here="sub")}"""
    tocs = [(i, h) for i, (h, _) in zip(ids, r["sections"])] + [("faq", "Spørgsmål og svar"), ("mere", "Relaterede sider")]
    body = f"""{head(title, desc, path, graph, section="solceller", cta=("#lead-form", "Få tilbud"))}
<main id="main">
{hero(crumbs, h1, esc(r['intro']), "solceller", c, usp=False, eyebrow=f"Solceller · {n} · regler", jump=(ids[0], "Læs reglerne"), upd=page_upd(c=c))}
{layout(tocs, inner, "solceller", c)}
</main>
{footer(("#lead-form", f"Få gratis tilbud i {n}"))}"""
    return path, body

def fv_page(c):
    d = CITIES[c]; n = d["name"]; f = FV_PAGE[c]; path = p_fv(c)
    title = f"Fjernvarme eller varmepumpe i {n}? Priser 2026 | {BRAND}"
    desc = f"Fjernvarme eller luft til vand-varmepumpe i {n}? Lokale fjernvarmepriser pr. værk, status for udbygningen og tilskudsregler, med kilder."
    h1 = f"Fjernvarme eller varmepumpe i {n}?"
    crumbs = [("Forside", "/"), ("Varmepumpe", p_hub("varmepumpe"))] + ([(n, p_city("varmepumpe", c))] if has_vp(c) else []) + [("Fjernvarme eller varmepumpe", path)]
    faqs = [x for i, x in enumerate(f["faq"]) if i != VP_BORROW[c]]
    if not has_vp(c):  # ingen varmepumpe-byside: dens lokale FAQ hører hjemme her
        faqs = faqs + d["vp_faq"] + [(q, a(), k) for q, a, k in L.VP_XFAQ.get(c, [])]
    graph = ld_page(path, title, desc, crumbs, about={"@type": "Thing", "name": "Fjernvarme og varmepumper i " + d["kommune"]}, upd=page_upd(c=c)) + [ld_service(path, f"Luft til vand-varmepumpe i {n}", "varmepumpe", c), ld_faq(path, faqs)]
    status = "".join(f"<li>{t} {src_links(k)}</li>" for t, k in f["status"])
    def dvp(p):
        d_ = int(str(p).replace(".", "")) - 9386
        return ("+" if d_ > 0 else "−") + L.tal(abs(d_)) + " kr."
    rows = "".join(f"<tr><td>{esc(v)}</td><td>{pn}</td><td>{p} kr.</td><td>{m} kr.</td><td>{dvp(p)}</td></tr>" for v, pn, p, m in FV_PRICES[c])
    rows += f'<tr class="avg"><td>Landsgennemsnit (vægtet, 374 værker)</td><td>–</td><td>{FV_AVG} kr.</td><td>–</td><td>{dvp(FV_AVG)}</td></tr>'
    num = lambda t: int(t.replace(" kr.", "").replace(".", ""))
    cmp = [(f"Fjernvarme: {v}", int(p.replace(".", ""))) for v, pn, p, m in FV_PRICES[c]] + [(a, num(b)) for a, b, x in FV_COMPARE_ROWS]
    cmp_rows = "".join(f"<tr><td>{esc(a)}</td><td>{v:,} kr.</td></tr>".replace(",", ".") for a, v in sorted(cmp, key=lambda r: r[1]))
    ca, cb, ck = f["contact"]
    blocks = {
        "status": (f"""<section id="status"><h2>Status for fjernvarmen i {esc(n)}</h2><ul class="facts">{status}</ul>
<div class="note note-ic">{ic("building")}<div><strong>Spørgsmål om din adresse:</strong> {esc(ca)}: {esc(cb)} {src_links([ck])}</div></div></section>""", "Status for fjernvarmen"),
        "varmekilder": (f"""<section id="varmekilder"><h2>{esc(L.FV_SOURCES_H[c])}</h2><ul class="facts">{''.join(f"<li>{t} {src_links(k)}</li>" for t, k in L.FV_SOURCES[c])}</ul></section>""", "Hvor kommer varmen fra?"),
        "andel": (f"""<section id="andel"><h2>Hvor mange huse har fjernvarme i {esc(d['kommune'])}?</h2><p>{L.FV_SHARE[c]()} {src_links(["dst_bol102"])}</p></section>""", "Andel med fjernvarme"),
        "priser": (f"""<section id="priser"><h2>Fjernvarmepriser i og omkring {esc(n)}</h2>
<div class="tbl"><table><thead><tr><th>Værk</th><th>Postnr.</th><th>Årspris, standardhus inkl. moms</th><th>Pr. MWh</th><th>Forskel til varmepumpe</th></tr></thead><tbody>{rows}</tbody></table></div>
{src_links(["ft_pris", "wg_pris"])}
<p class="small muted">Sidste kolonne er vores egen udregning: værkets årspris minus driften af luft til vand med radiatorer (9.386 kr., Bolius, samme hus). {src_links(["bolius_varme"])}</p></section>""", "Fjernvarmepriser"),
        "billigst": (f"""<section id="billigst"><h2>Fjernvarme eller varmepumpe i {esc(n)}: hvad er billigst?</h2>
<div class="tbl"><table><thead><tr><th>Opvarmning, 130 m² hus</th><th>Årlig varmeudgift</th></tr></thead><tbody>{cmp_rows}</tbody></table></div>
{src_links(["ft_pris", "bolius_varme"])}
<div class="note"><strong>Vores vurdering (egen læsning af tallene):</strong> {esc(f['local_take'])}</div>
<p class="small">Udmelding af fjernvarmen kan koste udtrædelsesgodtgørelse, ofte 10.000-100.000 kr. {src_links(["ean_udtr"])}</p></section>""", "Hvad er billigst?"),
        "faq": (f"""<section id="faq"><h2>Spørgsmål om fjernvarme og varmepumpe i {esc(n)}</h2>{faq_html(faqs)}</section>""", "Spørgsmål og svar"),
    }
    if not has_vp(c):  # varmepumpe-indholdet fra den sparede byside
        vfacts = "".join(f"<li>{t} {src_links(k)}</li>" for t, k in d["vp_facts"])
        blocks["lokalt"] = (f"""<section id="lokalt"><h2>Luft til vand-varmepumpe i {esc(n)}: tilskud og varmeplan</h2><p>{esc(d['vp_intro'])}</p><ul class="facts">{vfacts}</ul>
<p class="small muted">Faktatjekket {esc(page_upd(c=c)[0])}. Tjek altid {esc(d['kommune'])}s egne sider og Plandata.dk for din adresse, før du skriver under. {src_links(["plandata"])}</p></section>""", "Varmepumpe: tilskud og varmeplan")
        blocks["opvarmning"] = (vp_heat_html(c), "Sådan varmes husene op")
        blocks["lokale-byer"] = (vp_towns_html(c), "By for by")
    order = L.FV_ORDER[c]
    inner = "\n".join(blocks[k][0] for k in order) + f"""
<p>{f'Uden for fjernvarmen? Se <a href="{p_city("varmepumpe", c)}">varmepumpe i {esc(n)}</a>, <a href="/varmepumpe/pris/">priser</a> og <a href="/varmepumpe/tilskud/">tilskud</a>.' if has_vp(c) else f'Uden for fjernvarmen i {esc(n)}? Se <a href="/varmepumpe/pris/">prisen på en luft til vand-varmepumpe</a>, <a href="/varmepumpe/tilskud/">Varmepumpepuljen</a> og <a href="/solceller/{c}/">solceller i {esc(n)}</a>.'}</p>
{"" if has_vp(c) else el_box(c, "varmepumpe")}
{short_how("varmepumpe")}
{link_block("varmepumpe", c, here="sub")}"""
    tocs = [(k, blocks[k][1]) for k in order] + [("mere", "Relaterede sider")]
    body = f"""{head(title, desc, path, graph, section="varmepumpe", cta=("#lead-form", "Få tilbud"))}
<main id="main">
{hero(crumbs, h1, esc(f['intro']), "varmepumpe", c, usp=False, eyebrow=f"Varmepumpe · {n} · fjernvarme", jump=("priser", "Se de lokale priser"), upd=page_upd(c=c))}
{layout(tocs, inner, "varmepumpe", c)}
</main>
{footer(("#lead-form", f"Få gratis tilbud i {n}"))}"""
    return path, body

def national_page(path):
    g = NATIONAL[path]; svc = g["svc"]; o = OTHER[svc]
    title = f"{g['title']} | {BRAND}"
    if len(title) > 68: title = g["title"]
    crumbs = [("Forside", "/"), (SERVICES[svc]["name"], p_hub(svc)), (g["crumb"], path)]
    upd = page_upd(g)
    graph = ld_page(path, title, g["desc"], crumbs, upd=upd) + [ld_faq(path, g["faq"])]
    is_offer = path.endswith("/tilbud/")
    ids = [slug(h) for h, _ in g["sections"]]
    secs = "".join(f'<section id="{i}"><h2>{esc(h)}</h2>{blocks_html(b)}</section>' for i, (h, b) in zip(ids, g["sections"]))
    city_cards = "".join(f'<li><span class="cn">{ic("pin")}{esc(CITIES[c]["name"])}</span><a href="{p_city(svc, c)}">{esc(city_label(svc, c))}</a>{"" if p_city(svc, c) == p_sub(svc, c) else f'<a class="small" href="{p_sub(svc, c)}">{"Regler og byggetilladelse" if svc == "solceller" else "Fjernvarme eller varmepumpe"}</a>'}</li>' for c in CITIES)
    others = "".join(rcard(NAT_IC[u], t, d, u) for u, t, d in NAT_LINKS[svc] + [CALC] if u != path)
    checked = upd[0] if g.get("updated") else LAST_CHECKED
    extra = (checklist(svc) + how_it_works(svc)) if g.get("checklist") else ""
    inner = f"""{secs}{extra}
<p class="small muted">Faktatjekket {esc(checked)}. Priser er vejledende spænd fra de angivne kilder, ikke tilbud.</p>
<section id="faq"><h2>Ofte stillede spørgsmål</h2>{faq_html(g['faq'])}</section>
{"" if g.get("checklist") else short_how(svc)}
<section class="links" id="mere" aria-labelledby="mere-h"><h2 id="mere-h">Lokale regler og tilbud i din by</h2>
<h3>{ic(SVC_IC[svc])}{esc(SERVICES[svc]['name'])} i din by</h3><ul class="citylist">{city_cards}</ul>
<h3>{ic("book")}Flere guides</h3><div class="rgrid">{others}</div>
<p><a class="more" href="{p_hub(o)}">{esc(SERVICES[o]['name'])} i de samme byer{ic("arrow")}</a> <a class="more" href="{p_hub(svc)}">Overblik: {esc(SERVICES[svc]['name_lc'])} i alle byer{ic("arrow")}</a></p></section>"""
    tocs = [(i, h) for i, (h, _) in zip(ids, g["sections"])] + ([("tjekliste", "Tjekliste til tilbud"), ("saadan-virker-det", "Sådan virker det")] if g.get("checklist") else []) + [("faq", "Spørgsmål og svar"), ("mere", "Find din by")]
    body = f"""{head(title, g['desc'], path, graph, section="guides", cta=("#lead-form", "Få tilbud"))}
<main id="main">
{hero(crumbs, g['h1'], esc(g['intro']), svc, None, usp=is_offer, eyebrow=f"{'Tilbud' if is_offer else 'Guide'} · {SERVICES[svc]['name']}", jump=(ids[0], "Se priser og tjekliste" if is_offer else "Læs guiden"), upd=upd)}
{layout(tocs, inner, svc)}
</main>
{footer(("#lead-form", "Få gratis tilbud"))}"""
    return path, body

def hub_page(svc):
    path = p_hub(svc); s = SERVICES[svc]; o = OTHER[svc]
    if svc == "solceller":
        title = f"Solceller 2026: regler og tilbud i {n_byer()} | {BRAND}"
        desc = fit_desc(f"Solceller i {city_list()}: kommunernes regler, priser i 2026, elafgift og håndværkerfradrag.",
                        f"Solceller i {n_byer()} fra {CITIES[next(iter(CITIES))]['name']} til {CITIES[list(CITIES)[-1]]['name']}: kommunernes regler, priser i 2026, elafgift og håndværkerfradrag.")
        intro = "Reglerne for solceller er nogenlunde ens i hele landet, men kommunerne formulerer dem forskelligt. I Randers står der fx, at det \"i udgangspunktet\" kræver byggetilladelse, og Esbjerg har detaljerede krav til placeringen på taget. Vælg din by og se, hvad der gælder."
    else:
        title = f"Luft-vand-varmepumpe: tilskud og tilbud i {n_byer()} | {BRAND}"
        desc = fit_desc(f"Varmepumpe i {city_list()}: fjernvarmestatus, tilskud på 27.000 kr. (frist 30/11 2026) og priser.",
                        f"Luft til vand-varmepumpe i {n_byer()}: lokal fjernvarmestatus, tilskud på 27.000 kr. (frist 30/11 2026) og priser. Vælg din by.")
        intro = "Det vigtigste spørgsmål før en luft til vand-varmepumpe er, om der kommer fjernvarme til din adresse. Det afgør også, om du kan få tilskud. Status er meget forskellig fra by til by. Vælg din by og se den lokale status."
    crumbs = [("Forside", "/"), (s["name"], path)]
    cards = "".join(f'<div class="card"><a class="card-t" href="{p_city(svc,c)}">{ic("pin")}<strong>{esc(city_label(svc,c))}</strong></a><span>{esc(strip((CITIES[c]["sol_facts"] if svc=="solceller" else CITIES[c]["vp_facts"])[0][0])[:140])}…</span>{"" if p_city(svc,c) == p_sub(svc,c) else f'<a class="sub" href="{p_sub(svc,c)}">{"Regler og byggetilladelse" if svc=="solceller" else "Fjernvarme eller varmepumpe?"}{ic("arrow")}</a>'}</div>' for c in CITIES)
    guides = "".join(rcard(NAT_IC[u], t, d, u) for u, t, d in NAT_LINKS[svc]) + rcard("calc", CALC[1], CALC[2], CALC[0] + "#" + svc) + rcard("bolt", EL_URL[1], EL_URL[2], EL_URL[0])
    faqs = SOL_GENERAL_FAQ if svc == "solceller" else VP_GENERAL_FAQ
    graph = ld_page(path, title, desc, crumbs, typ="CollectionPage") + [ld_faq(path, faqs)]
    inner = f"""<section id="byer"><h2>Vælg din by</h2><div class="cards">{cards}</div></section>
<section id="guides"><h2>Guides til {esc(s['name_lc'])}</h2><div class="rgrid">{guides}</div></section>
{how_it_works(svc)}
{checklist(svc)}
<section id="faq"><h2>Ofte stillede spørgsmål</h2>{faq_html(faqs)}</section>
<section class="links" id="mere">{rcard(SVC_IC[o], SERVICES[o]['name'] + ' i de samme byer', SERVICES[o]['hub_title'], p_hub(o))}</section>"""
    tocs = [("byer", "Vælg din by"), ("guides", "Guides"), ("saadan-virker-det", "Sådan virker det"), ("tjekliste", "Tjekliste til tilbud"), ("faq", "Spørgsmål og svar")]
    body = f"""{head(title, desc, path, graph, section=svc, cta=("#lead-form", "Få tilbud"))}
<main id="main">
<section class="hero"><div class="wrap hero-grid">
<div class="hero-txt">{breadcrumbs(crumbs)}<p class="eyebrow">{ic(SVC_IC[svc])}{esc(s['name'])} · {n_byer()}</p><h1>{esc(s['hub_title'])}</h1><p class="lead-p">{esc(intro)}</p>
<div class="hero-actions show"><a class="btn btn-lg" href="#byer">Vælg din by{ic("chev")}</a></div>
{trust_line()}</div>
<div class="hero-form">{form(svc)}</div></div></section>
{layout(tocs, inner, svc)}
</main>
{footer(("#lead-form", "Få gratis tilbud"))}"""
    return path, body

def home():
    path = "/"
    title = f"{BRAND}: tilbud på solceller og varmepumpe i din by"
    desc = fit_desc(f"Lokale regler, fjernvarmestatus, tilskud og priser for solceller og luft til vand-varmepumper i {city_list()}.",
                    f"Lokale regler, fjernvarmestatus, tilskud og priser for solceller og luft til vand-varmepumper i {n_byer()}, fra {city_list().split(', ')[0]} til {CITIES[list(CITIES)[-1]]['name']}.")
    graph = [g_ for g_ in ld_page(path, title, desc, [("Forside", "/")]) if g_.get("@type") != "BreadcrumbList"]
    graph[1].pop("breadcrumb", None)
    city_cards = "".join(f"""<li class="city"><p class="city-n">{ic("pin")}<strong>{esc(CITIES[c]["name"])}</strong><span>{esc(CITIES[c]["kommune"])}</span></p>
<div class="city-a"><a class="cbtn" href="{p_city("solceller",c)}">{ic("sun")}Solceller {esc(CITIES[c]["name"])}</a><a class="cbtn" href="{p_city("varmepumpe",c)}">{ic("pump")}{"Varmepumpe " + esc(CITIES[c]["name"]) if has_vp(c) else "Fjernvarme/varmepumpe"}</a></div>
<div class="city-s"><a href="{p_reg(c)}">Regler og byggetilladelse</a>{f'<a href="{p_fv(c)}">Fjernvarme eller varmepumpe?</a>' if has_vp(c) else ""}</div></li>""" for c in CITIES)
    guides = "".join(rcard(NAT_IC[u], t, d, u) for svc in NAT_LINKS for u, t, d in NAT_LINKS[svc]) + rcard("calc", CALC[1], CALC[2], CALC[0]) + rcard("bolt", EL_URL[1], EL_URL[2], EL_URL[0])
    svc_cards = (f'<a class="svc" href="/solceller/"><span class="svc-ic">{ic("sun")}</span><strong>Solceller</strong><span>Kommunens regler, pris i 2026, elafgift og håndværkerfradrag.</span><span class="svc-go">Se byer og regler{ic("arrow")}</span></a>'
                 f'<a class="svc" href="/varmepumpe/"><span class="svc-ic">{ic("pump")}</span><strong>Luft til vand-varmepumpe</strong><span>Fjernvarme eller ej, tilskud på 27.000 kr. (frist 30/11 2026).</span><span class="svc-go">Se fjernvarmestatus{ic("arrow")}</span></a>')
    body = f"""{head(title, desc, path, graph, cta=("#byer", "Find din by"))}
<main id="main">
<section class="hero hero-home"><div class="wrap hero-grid">
<div class="hero-txt">
<p class="eyebrow">{ic("pin")}{" · ".join(esc(CITIES[c]["name"]) for c in CITIES)}</p>
<h1>Solceller og varmepumpe: lokale regler og tilbud i din by</h1>
<p class="lead-p">{esc(BRAND)} samler det, du skal vide før du køber, og formidler din forespørgsel til installatører. Det gælder kommunens regler, fjernvarmestatus, tilskud og typiske priser, alt sammen med kilder.</p>
<div class="svc-grid">{svc_cards}</div>
<ul class="usp usp-row"><li>{ic("check")}Gratis og uforpligtende</li><li>{ic("check")}Lokale regler og tilskud med kilder</li><li>{ic("check")}Du vælger selv, om du vil sige ja</li></ul>
<div class="hero-actions"><a class="btn btn-lg" href="#byer">Find din by{ic("chev")}</a></div>
<p class="disclose">{ic("shield")}<span>{esc(BRAND)} er en formidlingstjeneste, ikke en installatør. Vi arbejder kun med installatører, der lever op til vores krav og har positiv feedback fra tidligere kunder. Drevet af {esc(COMPANY_NAME)} · CVR {esc(CVR)} · {upd_html(page_upd())}. <a href="/om-os/">Om os</a></span></p>
</div>
<div class="hero-pick"><p class="hp-h">{ic("pin")}Find din by</p>
<p class="hp-l">{ic("sun")}Solceller i</p>{chips([(CITIES[c]["name"], p_city("solceller", c)) for c in CITIES])}
<p class="hp-l">{ic("pump")}Luft til vand-varmepumpe i</p>{chips([(CITIES[c]["name"], p_city("varmepumpe", c)) for c in CITIES])}
<p class="hp-f">Hver byside har kommunens regler, lokale kontakter og fjernvarmestatus, med kilder.</p></div>
</div></section>
<div class="wrap content-wide">
<section id="byer"><h2>Vælg by og ydelse</h2><p class="sub-h">Hver by har sine egne regler, fjernvarmeplaner og kontakter. Vælg din by for at se, hvad der gælder lokalt.</p><ul class="citygrid">{city_cards}<li class="city city-other"><p class="city-n">{ic("list")}<strong>Bor du et andet sted?</strong></p><p class="small">Indtil videre har vi lokale sider for {len(CITIES)} byer. De nationale guides gælder for hele landet.</p><div class="city-s"><a href="/solceller/">Solceller: overblik</a><a href="/varmepumpe/">Varmepumpe: overblik</a><a href="/varmepumpe/tilskud/">Varmepumpepuljen</a></div></li></ul></section>
<section id="saadan-virker-det"><h2>Sådan virker det</h2>{steps_html("solceller eller en varmepumpe")}</section>
<section id="guides"><h2>Guides og beregner</h2><div class="rgrid rgrid-2">{guides}</div></section>
<section id="hvem" class="about-band"><div><h2>Hvem står bag?</h2><p>{esc(BRAND)} drives af {esc(COMPANY_NAME)} (CVR {esc(CVR)}), {esc(COMPANY_ADDRESS)}. Alle tal på sitet har en kildehenvisning, og indholdet blev senest faktatjekket {esc(LAST_CHECKED)}. Vi viser ingen anmeldelser eller kundetal, som vi ikke kan dokumentere.</p><a class="btn ghost" href="/om-os/">Om os og metode{ic("arrow")}</a></div></section>
</div>
</main>
{footer(("#byer", "Find din by"))}"""
    return path, body

def simple_page(path, title, desc, h1, inner, noindex=False):
    crumbs = [("Forside", "/"), (h1, path)]
    graph = ld_page(path, title, desc, crumbs)
    up = "" if noindex else f'<p class="small muted upd">{upd_html(page_upd())}</p>'
    return path, f"""{head(title, desc, path, graph, noindex)}
<main id="main"><div class="wrap content narrow">{breadcrumbs(crumbs)}<h1>{esc(h1)}</h1>{up}{inner}</div></main>
{footer()}"""

# ---------- v7: beregner ----------
def calc_field(name, label, value, unit, keys, step="any", help_=""):
    h = f'<span class="cf-h">{help_} {src_links(keys)}</span>' if (help_ or keys) else ""
    return f'<label class="cf"><span class="cf-l">{label}</span><span class="cf-in"><input type="number" name="{name}" value="{value}" step="{step}" min="0" inputmode="decimal"><span class="cf-u">{unit}</span></span>{h}</label>'

def calc_el_today():
    """Valgfri knap: brug dagens gennemsnitlige samlede elpris (kildebaseret standard 1,45 kr. bevares)."""
    days, stale = el_days()
    if not days or stale: return ""
    b = "".join(f'<button type="button" class="chip" data-set="el" data-v="{EL.stats(ELD, days[0], a)["tot_avg"]:.2f}">{a}: {kr2(EL.stats(ELD, days[0], a)["tot_avg"])} kr.</button>' for a in EL.AREAS)
    return f'<div class="cf cf-x"><span class="cf-l">Brug dagens gennemsnitspris ({dk_date(days[0], False)})</span><span class="cf-btns">{b}</span><span class="cf-h">Anslået samlet pris inkl. moms fra <a href="/elpris/">elprissiden</a>. Én dags pris siger mindre om et helt år end tallet ovenfor.</span></div>'

def calc_page():
    path = "/beregner/"
    title = f"Beregner: kan solceller og varmepumpe betale sig? | {BRAND}"
    if len(title) > 68: title = "Beregner: kan solceller og varmepumpe betale sig?"
    desc = "Regn selv på tilbagebetalingstiden for solceller og luft til vand-varmepumpe. Ret alle tal, og se kilden bag hver standardværdi. Intet gemmes."
    h1 = "Beregner: kan solceller eller en varmepumpe betale sig?"
    crumbs = [("Forside", "/"), ("Beregner", path)]
    upd = page_upd({"updated": ("25. oktober 2026", "2026-10-25")})
    graph = ld_page(path, title, desc, crumbs, upd=upd) + [{"@type": "WebApplication", "@id": url(path) + "#app", "name": "Energitjekket-beregner", "applicationCategory": "FinanceApplication", "operatingSystem": "Alle browsere", "url": url(path), "isAccessibleForFree": True, "offers": {"@type": "Offer", "price": "0", "priceCurrency": "DKK"}, "provider": {"@id": SITE_URL + "/#org"}}]
    sol = f"""<form class="calc" data-k="sol" aria-labelledby="solceller-h" novalidate>
<div class="cgrid">
{calc_field("kwp", "Anlæggets størrelse", "6", "kWp", ["es_sol"], help_="Et typisk parcelhusanlæg er 6 kWp.")}
{calc_field("pris", "Pris inkl. montering", "92000", "kr.", ["es_sol"], step="1000", help_="Ca. 90.000-95.000 kr. for 6 kWp.")}
{calc_field("prod", "Produktion pr. kWp om året", "950", "kWh", ["es_sol", "pvgis"], step="10", help_="Ca. 950-1.050 kWh mod syd. Se tallet for din by på bysiden.")}
{calc_field("eg", "Andel du selv bruger", "35", "%", ["es_sol"], step="1", help_="35 % uden batteri. Elbil eller varmepumpe i dagtimerne hæver andelen.")}
{calc_field("p1", "Værdi pr. kWh, du selv bruger, 2026-2027", "1.13", "kr.", ["es_sol", "elafgift"], step="0.01", help_="Lav elafgift (0,8 øre) i 2026 og 2027.")}
{calc_field("p2", "Værdi pr. kWh, du selv bruger, fra 2028", "2.03", "kr.", ["es_sol", "elafgift_lov"], step="0.01", help_="Elafgiften stiger igen fra 2028 efter gældende lov.")}
{calc_field("aar", "Hele år med lav elafgift tilbage", "1", "år", [], step="1", help_="Vores antagelse: et anlæg sat op i slutningen af 2026 har ét helt år (2027) med lav afgift.")}
{calc_field("salg", "Salgspris for overskudsstrøm", "0.52", "kr./kWh", ["es_sol"], step="0.01")}
{calc_field("drift", "Faste udgifter pr. år", "500", "kr.", ["se_sol"], step="50", help_="Gebyr og abonnement til netselskabet.")}
</div>
<div class="cres" aria-live="polite"><p class="cres-h">Resultat</p><dl>
<div><dt>Produktion om året</dt><dd data-o="prod">–</dd></div>
<div><dt>Gevinst pr. år med lav elafgift</dt><dd data-o="g1">–</dd></div>
<div><dt>Gevinst pr. år fra 2028</dt><dd data-o="g2">–</dd></div>
<div class="big"><dt>Tilbagebetalingstid</dt><dd data-o="tb">–</dd></div>
<div><dt>Nettogevinst efter 25 år</dt><dd data-o="tot">–</dd></div></dl>
<p class="small muted">Uden renter, effekttab og inverterskifte (typisk 8.000-18.000 kr. efter ca. 10 år). Elpriserne holdes uændrede. {src_links(["es_sol", "se_sol"])}</p>
<button class="btn ghost" type="reset">Nulstil til standardværdier</button></div>
</form>"""
    kilde = "".join(f'<option value="{v}"{" selected" if v == "18433" else ""}>{esc(l)} ({v[:-3]}.{v[-3:]} kr.)</option>' for l, v in [("Gasfyr", "18433"), ("Oliefyr", "32388"), ("Elradiatorer", "30974"), ("Fjernvarme, landsgennemsnit", "16953")])
    vp = f"""<form class="calc" data-k="vp" aria-labelledby="varmepumpe-h" novalidate>
<div class="cgrid">
<label class="cf"><span class="cf-l">Det varmer du med i dag</span><span class="cf-in"><select name="kilde">{kilde}</select></span><span class="cf-h">Udfylder varmeudgiften med Bolius' driftstal for et 130 m² hus. {src_links(["bolius_varme"])}</span></label>
{calc_field("old", "Din varmeudgift i dag pr. år", "18433", "kr.", [], step="100", help_="Ret til din egen regning, hvis du kender den.")}
{calc_field("beh", "Varmebehov inkl. varmt vand", "18100", "kWh", ["bolius_varme"], step="100", help_="Bolius' standardhus på 130 m².")}
{calc_field("scop", "Varmepumpens SCOP", "3.5", "", ["es_vp"], step="0.1", help_="1 kWh strøm giver ca. 3-4 kWh varme. Gulvvarme giver højere SCOP.")}
{calc_field("el", "Samlet elpris", "1.45", "kr./kWh", ["es_vp"], step="0.01", help_="Ca. 1,45 kr. i DK1 og 1,55 kr. i DK2 i fyringssæsonen 2026.")}
{calc_el_today()}
{calc_field("serv", "Service pr. år", "0", "kr.", ["bolius_varme"], step="100", help_="Sat til 0, fordi varmeudgiften ovenfor heller ikke har service med. Bolius anslår ca. 2.000 kr. for en varmepumpe.")}
{calc_field("pris", "Pris inkl. montering", "110000", "kr.", ["es_vp", "se_vp"], step="1000", help_="Luft til vand: typisk 90.000-150.000 kr.")}
<label class="cf cf-chk"><span class="cf-l"><input type="checkbox" name="tils" checked> Jeg regner med tilskud fra Varmepumpepuljen</span><span class="cf-h">Lukker senest 30. november 2026. Kræver bl.a., at huset ligger uden for fjernvarme. {src_links(["se_vpp", "vpp_faq"])}</span></label>
{calc_field("tilsk", "Tilskud", "27000", "kr.", ["se_vpp"], step="1000")}
</div>
<div class="cres" aria-live="polite"><p class="cres-h">Resultat</p><dl>
<div><dt>Varmepumpens elforbrug</dt><dd data-o="kwh">–</dd></div>
<div><dt>Drift pr. år med varmepumpe</dt><dd data-o="drift">–</dd></div>
<div><dt>Besparelse pr. år</dt><dd data-o="spar">–</dd></div>
<div><dt>Din pris efter tilskud</dt><dd data-o="net">–</dd></div>
<div class="big"><dt>Tilbagebetalingstid</dt><dd data-o="tb">–</dd></div></dl>
<p class="small muted">Uden renter og uden den højere elafgift fra 2028. Med standardværdierne giver det samme resultat som Energisparer.dk's eksempel for et gasfyr (ca. 8 år). {src_links(["es_vp"])}</p>
<button class="btn ghost" type="reset">Nulstil til standardværdier</button></div>
</form>"""
    inner = f"""<section id="solceller"><h2 id="solceller-h">{ic("sun")}Solceller: tilbagebetaling</h2>
<p>Strøm, du selv bruger, er mere værd end strøm, du sælger. Derfor betyder andelen, du selv bruger, mest. Læs baggrunden i <a href="/solceller/kan-det-betale-sig/">kan solceller betale sig?</a></p>
{sol}</section>
<section id="varmepumpe"><h2 id="varmepumpe-h">{ic("pump")}Luft til vand-varmepumpe: tilbagebetaling</h2>
<p>Besparelsen er din varmeudgift i dag minus varmepumpens elregning. Ligger huset i et fjernvarmeområde, kan du ikke få tilskud. Se <a href="/varmepumpe/">status i din by</a>.</p>
{vp}</section>
<section id="metode"><h2>Sådan regner beregneren</h2>
<ul class="facts"><li>Solceller: produktion = kWp × kWh pr. kWp. Gevinst pr. år = (egen andel × værdi pr. kWh) + (solgt andel × salgspris) − faste udgifter. Tilbagebetalingstiden tæller år for år, først med lav elafgift og derefter med fuld afgift.</li>
<li>Varmepumpe: elforbrug = varmebehov ÷ SCOP. Drift = elforbrug × elpris + service. Tilbagebetalingstid = (pris − tilskud) ÷ (varmeudgift i dag − drift).</li>
<li>Beregneren kører kun i din browser. Den sætter ingen cookies, sender intet og gemmer intet.</li></ul>
<p class="small muted">Standardværdierne er tjekket {esc(upd[0])}. Resultatet er et overslag, ikke et tilbud. Få en konkret pris fra en installatør.</p></section>
<section id="tilbud" class="how-short"><h2>Vil du have en konkret pris?</h2><p>Udfyld en kort formular, så sender vi din forespørgsel til én udvalgt installatør i dit område. Det er gratis og uforpligtende.</p>
<p class="hero-actions show"><a class="btn" href="/solceller/tilbud/">Tilbud på solceller{ic("arrow")}</a> <a class="btn" href="/varmepumpe/tilbud/">Tilbud på varmepumpe{ic("arrow")}</a></p></section>"""
    tocs = [("solceller", "Solceller"), ("varmepumpe", "Varmepumpe"), ("metode", "Sådan regner vi"), ("tilbud", "Få en konkret pris")]
    body = f"""{head(title, desc, path, graph, section="guides", cta=("/#byer", "Få tilbud"))}
<main id="main">
<section class="hero hero-calc"><div class="wrap"><div class="hero-txt">{breadcrumbs(crumbs)}<p class="eyebrow">{ic("calc")}Beregner · solceller og varmepumpe</p><h1>{esc(h1)}</h1>
<p class="lead-p">Ret tallene, så de passer til dit hus. Alle standardværdier kommer fra de kilder, der står ved hvert felt. Beregneren gemmer intet og bruger ingen cookies.</p>
<div class="hero-actions show"><a class="btn btn-lg" href="#solceller">{ic("sun")}Solceller</a><a class="btn btn-lg" href="#varmepumpe">{ic("pump")}Varmepumpe</a></div>
{trust_line(upd, how=False)}</div></div></section>
<div class="wrap layout"><aside class="side">{toc(tocs)}</aside><div class="content">{inner}</div></div>
</main>
<noscript><p class="wrap small">Beregneren kræver JavaScript. Formlerne står under "Sådan regner beregneren".</p></noscript>
<script src="/assets/calc.js" defer></script>
{footer()}"""
    return path, body

# ---------- elpris (/elpris/ + boks på bysider) ----------
ELD = EL.load()
EL_NOW = EL.now_cph()
EL_URL = ("/elpris/", "Elprisen i dag og i morgen", "Timepriser for DK1 og DK2 med nettarif, elafgift og moms.")
WD = ["mandag", "tirsdag", "onsdag", "torsdag", "fredag", "lørdag", "søndag"]
MN = ["januar", "februar", "marts", "april", "maj", "juni", "juli", "august", "september", "oktober", "november", "december"]
def dk_date(d, wd=True):
    d = dt.date.fromisoformat(d) if isinstance(d, str) else d
    return (WD[d.weekday()] + " " if wd else "") + f"{d.day}. {MN[d.month - 1]} {d.year}"
def kr2(x): return f"{x:.2f}".replace(".", ",").replace("-", "−")
def el_days():
    """(dage der vises, forældet?) – i dag og i morgen, ellers seneste dag i datafilen."""
    if not ELD or not ELD.get("days"): return [], True
    t = EL_NOW.date(); ds = sorted(ELD["days"])
    show = [x for x in (t.isoformat(), (t + dt.timedelta(days=1)).isoformat()) if x in ds]
    return (show, False) if show and show[0] == t.isoformat() else (ds[-1:], True)
def price_area(c):
    if CITIES[c].get("price_area"): return CITIES[c]["price_area"]
    reg = CITIES[c].get("region") or CITY_REGION.get(c)
    if reg not in EL.REGION_AREA: raise SystemExit(f"Ukendt prisområde for {c}: sæt CITIES['{c}']['price_area'] = 'DK1'/'DK2' eller region i city-queue.json")
    return EL.REGION_AREA[reg]
try:
    CITY_REGION = {x["slug"]: x["region"] for x in json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "city-queue.json"), encoding="utf-8"))}
except Exception:
    CITY_REGION = {}
# De 7 første byer står ikke i køen. Alle ligger vest for Storebælt (DK1).
for _c in ("kolding", "vejle", "esbjerg", "odense", "aalborg", "randers", "horsens"): CITY_REGION.setdefault(_c, "Region Syddanmark" if _c in ("kolding", "vejle", "esbjerg", "odense") else "Region Midtjylland" if _c in ("randers", "horsens") else "Region Nordjylland")
def el_hhmm(h): return f"{h}:00"
def el_span(h): return f"kl. {int(h):02d}-{(int(h) + 1) % 24:02d}"

def el_svg(d, a, uid):
    ts, spot, tot = EL.series(ELD, d, a)
    W, H, l, r, t, b = 720, 270, 46, 8, 12, 30
    lo = min(0, min(spot)); hi = max(max(tot), max(spot)) * 1.08
    step = 0.5 if hi - lo <= 4 else 1.0
    y = lambda v: t + (hi - v) / (hi - lo) * (H - t - b)
    n = len(ts); bw = (W - l - r) / n
    def path(vals, inset):
        out = []
        for i, v in enumerate(vals):
            x0 = l + i * bw + inset; w = max(bw - 2 * inset, 0.6); y0, y1 = y(0), y(v)
            out.append(f"M{x0:.1f} {min(y0, y1):.1f}h{w:.1f}v{abs(y1 - y0):.1f}h-{w:.1f}z")
        return "".join(out)
    grid = []
    v = 0.0
    while v <= hi:
        grid.append(f'<path d="M{l} {y(v):.1f}H{W - r}" stroke="#e1e8e5"/><text x="{l - 6}" y="{y(v) + 4:.1f}" text-anchor="end">{kr2(v)}</text>'); v += step
    if lo < 0: grid.append(f'<path d="M{l} {y(lo):.1f}H{W - r}" stroke="#e1e8e5"/><text x="{l - 6}" y="{y(lo) + 4:.1f}" text-anchor="end">{kr2(lo)}</text>')
    xl = "".join(f'<text x="{l + i * bw:.1f}" y="{H - 10}" text-anchor="middle">{t_[:2]}</text>' for i, t_ in enumerate(ts) if t_.endswith(":00") and int(t_[:2]) % 3 == 0 and (i == 0 or ts[i - 1][:2] != t_[:2]))
    s = EL.stats(ELD, d, a)
    desc = (f"Søjler: anslået samlet pris inkl. moms, i gennemsnit {kr2(s['tot_avg'])} kr. pr. kWh. Mørke søjler: spotpris ekskl. moms, i gennemsnit {kr2(s['spot_avg'])} kr. "
            f"Billigst {el_span(s['cheap_h'][0])} ({kr2(s['cheap_h'][1])} kr. samlet), dyrest {el_span(s['exp_h'][0])} ({kr2(s['exp_h'][1])} kr. samlet).")
    return (f'<svg class="elsvg" viewBox="0 0 {W} {H}" role="img" aria-label="Elpris {dk_date(d)}, {EL.AREA_NAME[a]}, pr. {"kvarter" if n > 30 else "time"}. {esc(desc)}" data-d="{d}" data-a="{a}" data-n="{n}" data-l="{l}" data-w="{W - l - r}" data-top="{t}" data-h="{H - t - b}">'
            f'<g class="ax">{"".join(grid)}{xl}</g><path class="b-tot" d="{path(tot, 0.4)}"/><path class="b-spot" d="{path(spot, bw * 0.28)}"/></svg>')

def el_keys(d, a):
    s = EL.stats(ELD, d, a); net = EL.default_net(ELD, d, a)
    return f"""<dl class="elkeys">
<div><dt>Spotpris, gennemsnit</dt><dd>{kr2(s['spot_avg'])} kr.<small>pr. kWh ekskl. moms</small></dd></div>
<div><dt>Anslået samlet pris, gennemsnit</dt><dd>{kr2(s['tot_avg'])} kr.<small>pr. kWh inkl. moms ({esc(net)})</small></dd></div>
<div><dt>Billigste time</dt><dd>{el_span(s['cheap_h'][0])}<small>{kr2(s['cheap_h'][1])} kr. samlet · spot {kr2(dict(s['hours_spot'])[s['cheap_h'][0]])} kr.</small></dd></div>
<div><dt>Dyreste time</dt><dd>{el_span(s['exp_h'][0])}<small>{kr2(s['exp_h'][1])} kr. samlet · spot {kr2(dict(s['hours_spot'])[s['exp_h'][0]])} kr.</small></dd></div>
</dl>"""

def el_table(d, a):
    s = EL.stats(ELD, d, a); hs = dict(s["hours_spot"])
    ts, spot, _ = EL.series(ELD, d, a)
    rng = {}
    for t_, p in zip(ts, spot): rng.setdefault(t_[:2], []).append(p)
    rows = [(el_span(h), kr2(hs[h]), f"{kr2(min(rng[h]))} til {kr2(max(rng[h]))}", f"<strong>{kr2(v)}</strong>") for h, v in s["hours_tot"]]
    return tbl(["Tid", "Spotpris, gns. (kr./kWh ekskl. moms)", "Laveste og højeste kvarter", f"Anslået samlet pris inkl. moms ({esc(EL.default_net(ELD, d, a))})"], rows, "tbl-el")

def el_panel(a, days, stale):
    out = []
    t = EL_NOW.date().isoformat()
    for i, d in enumerate(days):
        lab = "I dag" if d == t else ("I morgen" if d > t else "Seneste data")
        uid = f"el-{a.lower()}-{i}"
        out.append(f"""<h3 id="{uid}-h">{lab}: {dk_date(d)}</h3>{el_keys(d, a)}
<figure class="chart elchart">{el_svg(d, a, uid)}<figcaption><span class="lg lg-tot"></span>Anslået samlet pris inkl. moms <span class="lg lg-spot"></span>Spotpris ekskl. moms. Pr. {"kvarter" if EL.stats(ELD, d, a)['n'] > 30 else "time"}, kr. pr. kWh. Vores grafik ud fra Energi Data Service.</figcaption></figure>
<details class="eldet"><summary>Se alle timer {dk_date(d, False)}</summary>{el_table(d, a)}</details>""")
    if len(days) == 1 and not stale:
        out.append('<p class="note">Morgendagens priser er ikke offentliggjort endnu. De kommer normalt i løbet af eftermiddagen. Energinet anbefaler at hente dem mellem kl. 13 og 14. ' + src_links(["eds_dap"]) + '</p>')
    return f'<div class="el-panel" id="{a.lower()}" role="tabpanel" aria-labelledby="tab-{a.lower()}"><h2 class="el-ph">{EL.AREA_NAME[a]}: {EL.AREA_SHORT[a]}</h2>{"".join(out)}</div>'

def el_net_table(d):
    rows = []
    for a in EL.AREAS:
        for lab, _, _ in EL.NET[a]:
            if lab not in ELD["days"][d]["net"][a]: continue
            s = EL.stats(ELD, d, a, lab)
            nh = ELD["days"][d]["net"][a][lab]
            rows.append((a, esc(lab), f"{kr2(min(nh))} til {kr2(max(nh))}", kr2(s["tot_avg"]), f"{el_span(s['cheap_h'][0])}: {kr2(s['cheap_h'][1])}", f"{el_span(s['exp_h'][0])}: {kr2(s['exp_h'][1])}"))
    return tbl(["Område", "Netselskab", "Nettarif C ekskl. moms", "Samlet pris, gns.", "Billigste time", "Dyreste time"], rows, "tbl-el")

def el_stamp():
    f = dt.datetime.fromisoformat(ELD["fetched"]).astimezone(EL.CPH)
    return f'<time datetime="{f.isoformat(timespec="minutes")}">{dk_date(f.date(), False)} kl. {f:%H:%M}</time>'

def el_data_json(days):
    out = {"days": {}}
    for d in days:
        out["days"][d] = {}
        for a in EL.AREAS:
            ts, spot, tot = EL.series(ELD, d, a)
            out["days"][d][a] = {"t": ts, "s": [round(x, 3) for x in spot], "p": [round(x, 3) for x in tot]}
    return json.dumps(out, separators=(",", ":"))

def el_box(c, svc):
    """Lille 'Elpris i dag'-boks på bysider. <aside> tælles ikke med i lighedsmålingen (fælles datablok)."""
    days, stale = el_days()
    if not days: return ""
    a = price_area(c); d = days[0]; s = EL.stats(ELD, d, a); n = CITIES[c]["name"]
    if svc == "solceller":
        tip = f"Strøm fra dine solceller, som du selv bruger, sparer dig den samlede pris. Midt på dagen (kl. 10-16) er den i dag i gennemsnit {kr2(el_avg(d, a, 10, 16, 'p'))} kr. pr. kWh. Solgt overskudsstrøm afregnes typisk til spotprisen minus et gebyr. Spotprisen er i dag {kr2(el_avg(d, a, 10, 16, 's'))} kr. i samme tidsrum. {src_links(["es_sol"])}"
    else:
        tip = f"Kan din varmepumpes styring flytte noget af forbruget, fx opvarmning af varmt vand, er de billigste 3 timer i dag kl. {int(s['best3'][0]):02d}-{(int(s['best3'][2]) + 1) % 24:02d} (gns. {kr2(s['best3'][1])} kr. samlet)."
    lab = "i dag" if not stale else dk_date(d)
    return f"""<aside class="elbox" aria-labelledby="elbox-{svc[:3]}" data-elday="{d}">
<h2 id="elbox-{svc[:3]}">{ic("bolt")}Elprisen {lab} i {esc(n)}</h2>
<p class="small">{esc(n)} ligger i prisområde {a} ({esc(EL.AREA_SHORT[a])}). {dk_date(d).capitalize()}:</p>
<ul class="elmini"><li><span>Spotpris, gns.</span><strong>{kr2(s['spot_avg'])} kr.</strong></li><li><span>Samlet pris, gns.</span><strong>{kr2(s['tot_avg'])} kr.</strong></li><li><span>Billigst</span><strong>{el_span(s['cheap_h'][0])}</strong></li><li><span>Dyrest</span><strong>{el_span(s['exp_h'][0])}</strong></li></ul>
<p class="small">{tip}</p>
<p class="small muted">Pr. kWh. Samlet pris er anslået inkl. nettarif ({esc(EL.default_net(ELD, d, a))}), Energinets tariffer, elafgift og moms, men uden elselskabets tillæg og abonnementer. Hentet {el_stamp()}. {src_links(["eds_dap", "eds_tarif"])}</p>
<p class="el-stale small" hidden>Priserne er fra {dk_date(d)}. Se de nyeste på elprissiden.</p>
<a class="more" href="/elpris/#{a.lower()}">Se timepriser for i dag og i morgen{ic("arrow")}</a></aside>"""

def el_avg(d, a, h0, h1, k):
    ts, spot, tot = EL.series(ELD, d, a)
    v = [(p if k == "s" else q) for t_, p, q in zip(ts, spot, tot) if h0 <= int(t_[:2]) < h1]
    return sum(v) / len(v)

def el_today_avg(a):
    days, _ = el_days()
    return EL.stats(ELD, days[0], a)["tot_avg"] if days else None

def elpris_page():
    path = "/elpris/"
    days, stale = el_days()
    d0 = days[0]
    title = f"Elpris i dag og i morgen: timepriser DK1 og DK2 | {BRAND}"
    if len(title) > 68: title = "Elpris i dag og i morgen: timepriser DK1 og DK2"
    s1, s2 = EL.stats(ELD, d0, "DK1"), EL.stats(ELD, d0, "DK2")
    desc = f"Elprisen {dk_date(d0, False)}: spotpris og anslået samlet pris pr. kWh i Vest- og Østdanmark, billigste og dyreste timer. Data fra Energinet."
    h1 = "Elprisen i dag og i morgen"
    crumbs = [("Forside", "/"), ("Elpris", path)]
    upd = (dk_date(d0, False), d0) if not stale else (dk_date(ELD["fetched"][:10], False), ELD["fetched"][:10])
    ds = {"@type": "Dataset", "@id": url(path) + "#dataset", "name": f"Elpriser for DK1 og DK2, {dk_date(days[0], False)}" + (f" og {dk_date(days[-1], False)}" if len(days) > 1 else ""),
          "description": "Day-ahead-spotpriser i 15-minutters opløsning for de to danske prisområder og en anslået samlet pris pr. kWh inkl. nettarif C, Energinets tariffer, elafgift og moms.",
          "temporalCoverage": f"{days[0]}/{days[-1]}", "spatialCoverage": {"@type": "Place", "name": "Danmark (DK1 og DK2)"},
          "creator": {"@id": SITE_URL + "/#org"}, "dateModified": ELD["fetched"][:10], "isAccessibleForFree": True, "inLanguage": "da-DK",
          "isBasedOn": [S["eds_dap"][1], S["eds_tarif"][1]],
          "variableMeasured": ["Spotpris (kr. pr. kWh ekskl. moms)", "Anslået samlet elpris (kr. pr. kWh inkl. moms)"]}
    graph = ld_page(path, title, desc, crumbs, upd=upd) + [ds]
    tabs = "".join(f'<button type="button" role="tab" id="tab-{a.lower()}" aria-controls="{a.lower()}" aria-selected="{"true" if a == "DK1" else "false"}" data-area="{a.lower()}">{EL.AREA_NAME[a]}<small>{EL.AREA_SHORT[a]}</small></button>' for a in EL.AREAS)
    panels = "".join(el_panel(a, days, stale) for a in EL.AREAS)
    fees = ELD["days"][d0]["fees"]
    staletxt = f'<p class="note">Vi kunne ikke hente nye priser. Tallene er fra {dk_date(d0)}.</p>' if stale else ""
    byer = {a: [c for c in CITIES if price_area(c) == a] for a in EL.AREAS}
    city_li = "".join(f'<li><span class="cn">{ic("pin")}{esc(CITIES[c]["name"])} ({price_area(c)})</span><a href="{p_city("solceller", c)}">Solceller i {esc(CITIES[c]["name"])}</a><a href="{p_city("varmepumpe", c)}">{esc(city_label("varmepumpe", c))}</a></li>' for c in CITIES)
    no_dk2 = "" if byer["DK2"] else " Vi har endnu ingen lokale sider øst for Storebælt."
    sd = {a: (el_avg(d0, a, 10, 16, "p"), el_avg(d0, a, 10, 16, "s")) for a in EL.AREAS}
    peak = [h for h, v in enumerate(ELD["days"][d0]["net"]["DK1"][EL.default_net(ELD, d0, "DK1")]) if v == max(ELD["days"][d0]["net"]["DK1"][EL.default_net(ELD, d0, "DK1")])]
    _nh = ELD["days"][d0]["net"]["DK1"][EL.default_net(ELD, d0, "DK1")]
    low = [h for h, v in enumerate(_nh) if v == min(_nh)]
    lowpk = f"kl. {low[0]:02d}-{low[-1] + 1:02d}" if low and low[-1] - low[0] + 1 == len(low) else "om natten"
    _all = [h for ar in EL.AREAS for h in ELD["days"][d0]["net"][ar].values()]
    _same = all([i for i, v in enumerate(h) if v == min(h)] == low and [i for i, v in enumerate(h) if v == max(h)] == peak for h in _all)
    pk_who = "hos alle netselskaberne i tabellen" if _same else f"hos {EL.default_net(ELD, d0, 'DK1')}"
    pk = f"kl. {peak[0]:02d}-{peak[-1] + 1:02d}" if peak and peak[-1] - peak[0] + 1 == len(peak) else "i spidslastperioden"
    b3 = {a: EL.stats(ELD, d0, a)["best3"] for a in EL.AREAS}
    b3t = lambda a: f"kl. {int(b3[a][0]):02d}-{(int(b3[a][2]) + 1) % 24:02d} (gns. {kr2(b3[a][1])} kr.)"
    faqs = [("Hvorfor er elprisen forskellig i Vest- og Østdanmark?", "Danmark er delt i to prisområder ved Storebælt: DK1 (Jylland og Fyn) og DK2 (Sjælland, øerne og Bornholm). Hvert område har sin egen day-ahead-pris, fordi udbud, forbrug og forbindelser til nabolandene er forskellige.", ["eds_dap"]),
            ("Hvornår kommer morgendagens elpriser?", "Day-ahead-priserne for næste døgn offentliggøres om eftermiddagen. Energinet anbefaler at hente dem mellem kl. 13 og 14. Vi opdaterer siden dagligt efter kl. 13.", ["eds_dap"]),
            ("Hvad er elafgiften i 2026?", f"Elafgiften er sat ned til 0,8 øre pr. kWh ekskl. moms ({kr2(fees['elafgift'] * 1.25)} kr. inkl. moms) i 2026 og 2027.", ["elafgift_skat", "eds_tarif"]),
            ("Hvorfor er min elregning højere end spotprisen?", "Spotprisen er kun prisen for selve strømmen på elbørsen. Oven i kommer nettarif til netselskabet, Energinets tariffer, elafgift, moms, elselskabets tillæg og faste abonnementer.", ["eds_tarif"]),
            ("Hvorfor er prisen i 15-minutters intervaller?", "Siden 1. oktober 2025 fastsættes day-ahead-prisen pr. kvarter i stedet for pr. time. Vi viser kvartererne i grafen og gennemsnittet pr. time i tabellen.", ["eds_dap"])]
    graph.append(ld_faq(path, faqs))
    inner = f"""{staletxt}<section id="priser" aria-labelledby="priser-h"><h2 id="priser-h" class="vh">Elpriser pr. prisområde</h2>
<div class="el-tabs" role="tablist" aria-label="Vælg prisområde">{tabs}</div>{panels}
<p class="small muted">Samlet pris = (spotpris + nettarif C + Energinets tariffer + elafgift) + 25 % moms. Uden elselskabets tillæg og faste abonnementer. {src_links(["eds_dap", "eds_tarif", "elafgift_skat"])}</p></section>
<section id="netselskaber"><h2>Samlet pris hos forskellige netselskaber {dk_date(d0, False)}</h2>
<p>Nettariffen afhænger af, hvilket netselskab der ejer elnettet ved din adresse. Den er lavest {lowpk} og højest {pk} {pk_who}. Her er dagens anslåede samlede pris hos {sum(len(v) for v in EL.NET.values())} netselskaber, hvor prisområdet er entydigt. Dit netselskab står på elregningen.</p>
{el_net_table(d0)}<p class="small muted">Nettarif C er tariffen for almindelige husstande på 0,4 kV-nettet. {src_links(["eds_tarif"])}</p></section>
<section id="solceller"><h2>Hvad er strømmen fra solceller værd i dag?</h2>
<p>Strøm, du selv bruger, sparer dig den samlede købspris. Strøm, du sælger gennem en produktionselleverandør, afregnes typisk til spotprisen minus et gebyr. {src_links(["es_sol", "se_sol"])} I dag mellem kl. 10 og 16 er den anslåede samlede pris i gennemsnit <strong>{kr2(sd['DK1'][0])} kr.</strong> i DK1 og <strong>{kr2(sd['DK2'][0])} kr.</strong> i DK2, mens spotprisen er {kr2(sd['DK1'][1])} og {kr2(sd['DK2'][1])} kr. pr. kWh. {src_links(["eds_dap", "eds_tarif"])}</p>
<p>Derfor betyder egetforbruget mest for, om solceller kan betale sig. Læs <a href="/solceller/kan-det-betale-sig/">kan solceller betale sig</a>, regn på dit eget hus i <a href="/beregner/#solceller">beregneren</a>, eller <a href="/solceller/tilbud/">få tilbud på solceller</a>.</p></section>
<section id="varmepumpe"><h2>Hvornår er strømmen billigst til varmepumpen?</h2>
<p>Det er elprisen over hele fyringssæsonen, der afgør driftsudgiften, ikke en enkelt time. Har din varmepumpe en styring, der kan flytte noget af forbruget, fx opvarmning af varmt vand, er de billigste 3 sammenhængende timer i dag {b3t('DK1')} i DK1 og {b3t('DK2')} i DK2, målt på samlet pris. {src_links(["eds_dap", "eds_tarif"])}</p>
<p>Se <a href="/varmepumpe/skift-gasfyr/">skift fra gasfyr</a>, <a href="/varmepumpe/skift-oliefyr/">skift fra oliefyr</a>, regn på driften i <a href="/beregner/#varmepumpe">beregneren</a>, eller <a href="/varmepumpe/tilbud/">få tilbud på en varmepumpe</a>.</p></section>
<section id="metode"><h2>Sådan regner vi</h2><ul>
<li><strong>Spotpris:</strong> day-ahead-prisen fra datasættet Day-Ahead Prices hos Energi Data Service (Energinet), omregnet fra kr. pr. MWh til kr. pr. kWh. Energinet omregner fra euro med Nationalbankens kurs, så prisen kan afvige lidt fra andre danske kilder. {src_links(["eds_dap"])}</li>
<li><strong>Nettarif C:</strong> netselskabets timetarif for husstande, hentet fra DatahubPricelist. Standard er {esc(EL.default_net(ELD, d0, "DK1"))} i DK1 og {esc(EL.default_net(ELD, d0, "DK2"))} i DK2. Rabatter, som netselskabet selv har lagt ind, er trukket fra. {src_links(["eds_tarif"])}</li>
<li><strong>Energinet:</strong> transmissionsnettarif {kr2(fees['transmission'])} kr. og systemtarif {kr2(fees['system'])} kr. pr. kWh ekskl. moms. {src_links(["eds_tarif"])}</li>
<li><strong>Elafgift:</strong> 0,8 øre ({kr2(fees['elafgift'])} kr.) pr. kWh ekskl. moms i 2026 og 2027. {src_links(["elafgift_skat"])}</li>
<li><strong>Moms:</strong> 25 % af det hele.</li>
<li><strong>Ikke med:</strong> elselskabets tillæg og abonnementer samt netselskabets faste abonnement. Din faktiske pris er derfor lidt højere.</li>
<li>Data hentet {el_stamp()}. Vi opdaterer siden hver dag efter kl. 13, når morgendagens priser er offentliggjort.</li></ul></section>
<section id="byer"><h2>Elprisen i din by</h2><p>Vores bysider viser dagens elpris for byens prisområde.{no_dk2}</p><ul class="citylist">{city_li}</ul></section>
<section id="faq"><h2>Ofte stillede spørgsmål om elprisen</h2>{faq_html(faqs)}</section>
<section id="tilbud" class="how-short"><h2>Vil du bruge mindre strøm fra nettet?</h2><p>Udfyld en kort formular, så sender vi din forespørgsel til én udvalgt installatør i dit område. Det er gratis og uforpligtende.</p>
<p class="hero-actions show"><a class="btn" href="/solceller/tilbud/">Tilbud på solceller{ic("arrow")}</a> <a class="btn" href="/varmepumpe/tilbud/">Tilbud på varmepumpe{ic("arrow")}</a></p></section>"""
    tocs = [("priser", "Priser i dag og i morgen"), ("netselskaber", "Netselskaber"), ("solceller", "Solceller"), ("varmepumpe", "Varmepumpe"), ("metode", "Sådan regner vi"), ("byer", "Din by"), ("faq", "Spørgsmål og svar")]
    lead = (f"Spotprisen og den anslåede samlede pris pr. kWh i Vest- og Østdanmark, kvarter for kvarter. "
            f"{dk_date(d0).capitalize()} er spotprisen i gennemsnit {kr2(s1['spot_avg'])} kr. i DK1 og {kr2(s2['spot_avg'])} kr. i DK2. Med nettarif, afgift og moms er det ca. {kr2(s1['tot_avg'])} og {kr2(s2['tot_avg'])} kr. pr. kWh.")
    body = f"""{head(title, desc, path, graph, section="guides", cta=("/#byer", "Få tilbud"))}
<main id="main">
<section class="hero hero-calc"><div class="wrap"><div class="hero-txt">{breadcrumbs(crumbs)}<p class="eyebrow">{ic("bolt")}Elpris · DK1 og DK2</p><h1>{esc(h1)}</h1>
<p class="lead-p">{lead}</p>
<p class="el-now" hidden></p>
<p class="disclose">{ic("shield")}<span>Data fra Energinet (Energi Data Service), hentet {el_stamp()}. {esc(BRAND)} drives af {esc(COMPANY_NAME)} · CVR {esc(CVR)} · {upd_html(upd)}.</span></p>
<p class="el-stale note" data-elday="{d0}" hidden>Priserne her er fra {dk_date(d0)}. Nyere priser kommer, når siden opdateres.</p></div></div></section>
<div class="wrap layout"><aside class="side">{toc(tocs)}</aside><div class="content">{inner}</div></div>
</main>
<script type="application/json" id="elpris-data">{el_data_json(days)}</script>
<script src="/assets/elpris.js" defer></script>
{footer()}"""
    return path, body

EL_JS = r"""(function(){
var d=document,el=d.getElementById('elpris-data');if(!el)return;var D=JSON.parse(el.textContent);
var tabs=[].slice.call(d.querySelectorAll('.el-tabs [role=tab]'));
function sel(a){tabs.forEach(function(t){var on=t.getAttribute('data-area')===a;t.setAttribute('aria-selected',on?'true':'false');t.tabIndex=on?0:-1;var p=d.getElementById(t.getAttribute('aria-controls'));if(p)p.hidden=!on})}
tabs.forEach(function(t,i){t.addEventListener('click',function(){sel(t.getAttribute('data-area'))});t.addEventListener('keydown',function(e){if(e.key==='ArrowRight'||e.key==='ArrowLeft'){var n=tabs[(i+(e.key==='ArrowRight'?1:tabs.length-1))%tabs.length];n.focus();sel(n.getAttribute('data-area'))}})});
var h=(location.hash||'').slice(1);sel(h==='dk2'?'dk2':'dk1');
window.addEventListener('hashchange',function(){var h=location.hash.slice(1);if(h==='dk1'||h==='dk2')sel(h)});
var f=new Intl.DateTimeFormat('sv-SE',{timeZone:'Europe/Copenhagen',year:'numeric',month:'2-digit',day:'2-digit',hour:'2-digit',minute:'2-digit',hour12:false}).format(new Date());
var day=f.slice(0,10),hm=f.slice(11,16),q=hm.slice(0,3)+('0'+Math.floor(parseInt(hm.slice(3),10)/15)*15).slice(-2);
var T=D.days[day];
function k(x){return x.toFixed(2).replace('.',',').replace('-','\u2212')}
if(T){var i=T.DK1.t.indexOf(q);if(i<0)i=T.DK1.t.indexOf(hm.slice(0,3)+'00');
 if(i>=0){var n=d.querySelector('.el-now');n.textContent='Lige nu (kl. '+T.DK1.t[i]+'): '+k(T.DK1.p[i])+' kr. pr. kWh i DK1 og '+k(T.DK2.p[i])+' kr. i DK2, anslået samlet pris inkl. moms. Spotpris '+k(T.DK1.s[i])+' og '+k(T.DK2.s[i])+' kr.';n.hidden=false;
 [].slice.call(d.querySelectorAll('svg.elsvg[data-d="'+day+'"]')).forEach(function(s){var N=+s.getAttribute('data-n'),x=+s.getAttribute('data-l')+(+s.getAttribute('data-w'))*(i+.5)/N;var ln=d.createElementNS('http://www.w3.org/2000/svg','path');ln.setAttribute('d','M'+x.toFixed(1)+' '+s.getAttribute('data-top')+'v'+s.getAttribute('data-h'));ln.setAttribute('class','now');s.appendChild(ln)})}}
})();"""

def pages_static():
    src_list = "".join(f'<li><a href="{esc(u)}" target="_blank" rel="noopener nofollow">{esc(n)}</a></li>' for n, u in S.values())
    om = simple_page("/om-os/", f"Om {BRAND}: hvem vi er og hvordan vi arbejder", f"Hvem står bag {BRAND}, hvordan vi vælger installatører, og hvordan vi faktatjekker regler, priser og tilskud.", f"Om {BRAND}", f"""
<p>{esc(BRAND)} drives af {esc(COMPANY_NAME)} (CVR {esc(CVR)}), {esc(COMPANY_ADDRESS)}. Vi har lavet sitet, fordi lokale regler, fjernvarmeplaner og tilskud er svære at finde samlet ét sted, når man overvejer solceller eller en varmepumpe.</p>
<h2>Vi er en formidlingstjeneste</h2>
<p>Vi sælger, installerer og servicerer ikke selv solceller eller varmepumper. Når du udfylder formularen og giver samtykke, sender vi din forespørgsel til én installatør, der dækker dit område. Så snart det er sket, får du en e-mail med firmaets navn og CVR-nummer.</p>
<h2>Hvem vi arbejder sammen med</h2>
<p>{esc(TRUST_TEXT)} Vi nævner ikke installatørerne på sitet, men du får altid at vide, hvilket firma der har fået dine oplysninger.</p>
<h2>Sådan laver vi indholdet</h2>
<p>Hver byside bygger på kommunens egne sider, fjernvarmeselskabernes oplysninger og officielle kilder som Energistyrelsen, SparEnergi, Skattestyrelsen, Danmarks Statistik og PVGIS. Alle tal har en kildehenvisning ved siden af. Vi viser ingen anmeldelser, kundetal eller "vurderinger", som vi ikke kan dokumentere. Indholdet blev senest faktatjekket {esc(LAST_CHECKED)}.</p>
<h2>Kilder brugt på sitet</h2><ul class="srclist">{src_list}</ul>
<h2>Virksomhedsoplysninger</h2><p>{esc(COMPANY_NAME)}, CVR {esc(CVR)}, {esc(COMPANY_ADDRESS)}. Anpartsselskab registreret i CVR siden 10. december 2018. {src_links(["cvr_virk"])}</p>
<h2>Kontakt</h2><p>{esc(COMPANY_NAME)}, {esc(COMPANY_ADDRESS)} · {esc(CONTACT_EMAIL)} · {esc(CONTACT_PHONE)}</p>""")
    priv = simple_page("/privatlivspolitik/", f"Privatlivspolitik | {BRAND}", f"Sådan behandler {BRAND} dine personoplysninger, når du beder om tilbud.", "Privatlivspolitik", f"""
<h2>Dataansvarlig</h2><p>{esc(COMPANY_NAME)}, CVR {esc(CVR)}, {esc(COMPANY_ADDRESS)}, {esc(CONTACT_EMAIL)}.</p>
<h2>Hvilke oplysninger og hvorfor</h2><p>Når du udfylder formularen, behandler vi navn, telefon, e-mail, postnummer, eventuel adresse og dine svar om boligen. Vi gemmer også, hvilken side du kom fra, din browsertype, eventuelle kampagneparametre i linket (utm) samt den samtykketekst, du accepterede, og tidspunktet. Formålet er at formidle din forespørgsel til installatører, så de kan give dig tilbud, og at kunne dokumentere dit samtykke.</p>
<h2>Retsgrundlag</h2><p>Dit samtykke (databeskyttelsesforordningens art. 6, stk. 1, litra a) til at vi giver oplysningerne videre til én udvalgt installatør i dit område, og til at installatøren kontakter dig på telefon og e-mail med et tilbud. Du kan trække samtykket tilbage når som helst. Det påvirker ikke lovligheden af det, der skete, før du trak det tilbage.</p>
<h2>Modtagere</h2><p><strong>Installatør:</strong> én installatør, der dækker dit område, og som vi vælger ud fra din forespørgsel. Installatøren er selvstændigt dataansvarlig for de oplysninger, den modtager. Så snart vi har sendt dine oplysninger, får du en e-mail med firmaets navn og CVR-nummer.</p>
<p><strong>Databehandlere:</strong> Vercel Inc. (hosting af hjemmesiden og anonym besøgsstatistik), Supabase Inc. (databaser i EU: forespørgsler gemmes i Irland, vores egen besøgsstatistik i Frankfurt) og Resend Inc. (afsendelse af e-mails, fx beskeden om hvilken installatør der har fået dine oplysninger). Databehandlerne må kun behandle oplysningerne efter vores instruks. Hvis oplysninger overføres til lande uden for EU, sker det på grundlag af EU-Kommissionens standardkontraktbestemmelser i databehandleraftalerne.</p>
<h2>Opbevaring</h2><p>Vi sletter dine oplysninger 12 måneder efter din forespørgsel. Trækker du samtykket tilbage, sletter vi dem hurtigst muligt.</p>
<h2>Dine rettigheder</h2><p>Du kan trække dit samtykke tilbage og bede om indsigt, berigtigelse, sletning, begrænsning eller dataportabilitet ved at skrive til {esc(CONTACT_EMAIL)}. Trækker du samtykket tilbage, giver vi besked videre til den installatør, der har modtaget dine oplysninger. Du kan klage til Datatilsynet (datatilsynet.dk).</p>
<h2>Cookies og statistik</h2><p>Sitet bruger ikke cookies. Vi bruger Vercel Web Analytics og Vercel Speed Insights til anonym, samlet besøgsstatistik (fx hvilke sider der besøges, og hvor hurtigt de indlæses). Værktøjerne sætter ingen cookies, gemmer ikke personoplysninger om dig og følger dig ikke på tværs af andre websites.</p>
<p>Derudover har vi vores egen cookiefri statistik. Den registrerer sidevisninger, om formularen bliver åbnet og sendt, og klik til tilbudssiderne. Vi gemmer siden, den side du kom fra (kun domænet), eventuelle kampagnekoder i adressen (utm), enhedstype, browsertype og land. Vi gemmer ikke din IP-adresse eller din browsers fulde identifikation, og vi gemmer intet af det, du skriver i formularen. For at kunne tælle unikke besøgende laver vi en envejs-kode ud fra IP-adresse og browser plus en tilfældig værdi, der skiftes hver dag og slettes efter to dage. Koden kan derfor ikke føres tilbage til dig og kan ikke bruges til at genkende dig fra dag til dag.</p>
<p>Statistikken bruges kun samlet, til at forbedre sitet. Den opbevares hos Supabase på servere i EU (Frankfurt), og hændelser slettes automatisk efter 13 måneder. Har du slået "Do Not Track" til i din browser, sender vi ingen hændelser til vores egen statistik.</p>""")
    tak = simple_page("/tak/", f"Tak for din forespørgsel | {BRAND}", "Kvittering for din forespørgsel.", "Tak for din forespørgsel", f"""<p>Vi har modtaget din forespørgsel.</p>
<h2>Hvad sker der nu?</h2><ol class="check"><li>Vi vælger én installatør, der dækker dit område, og sender din forespørgsel dertil.</li><li>Så snart det er sket, får du en e-mail med firmaets navn og CVR-nummer.</li><li>Installatøren kontakter dig på telefon eller e-mail med et uforpligtende tilbud. Du bestemmer selv, om du vil sige ja.</li></ol>
<p>Har du spørgsmål, eller vil du trække dit samtykke tilbage, så skriv til {esc(CONTACT_EMAIL)}.</p>
<p><a class="btn" href="/">Tilbage til forsiden</a></p>""", noindex=True)
    return [om, priv, tak]


CSS = r"""
:root{--g:#0b4f43;--g2:#0f6b55;--g3:#e7f2ee;--g4:#f2f8f5;--y:#f5b700;--y2:#fff5d1;--ink:#13201d;--mut:#4f5e5a;--line:#e1e8e5;--bg:#f6f8f7;--r:14px;--sh:0 1px 2px rgba(16,40,34,.06),0 8px 24px rgba(16,40,34,.08);--hh:64px}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%;scroll-behavior:smooth;scroll-padding-top:calc(var(--hh) + 12px)}
@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}*{transition:none!important}}
body{margin:0;font:16px/1.65 system-ui,-apple-system,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif;color:var(--ink);background:#fff;text-rendering:optimizeLegibility}
@media(min-width:900px){body{font-size:17px}}
a{color:var(--g2);text-underline-offset:2px}a:hover{color:var(--g)}
:focus-visible{outline:3px solid var(--y);outline-offset:2px;border-radius:4px}
.wrap{max-width:1200px;margin:0 auto;padding:0 20px}.narrow{max-width:780px}
.skip{position:absolute;left:-999px}.skip:focus{left:8px;top:8px;background:#fff;padding:8px;z-index:99}
.ic{width:1.15em;height:1.15em;fill:none;stroke:currentColor;stroke-width:2;stroke-linecap:round;stroke-linejoin:round;flex:none;vertical-align:-.2em}
h1,h2,h3{letter-spacing:-.015em;color:var(--ink)}
h1{font-size:clamp(1.85rem,4.6vw,2.9rem);line-height:1.1;margin:.25em 0 .4em;font-weight:800}
h2{font-size:clamp(1.35rem,2.6vw,1.8rem);line-height:1.22;margin:0 0 .6em;font-weight:780}
h3{font-size:1.05rem;margin:.2em 0 .6em;font-weight:720;display:flex;align-items:center;gap:8px}h3 .ic{color:var(--g2)}
p{margin:0 0 1em}
/* header + menu */
.site-header{position:sticky;top:0;z-index:50;background:#fff;border-bottom:1px solid var(--line)}
.hdr{display:flex;align-items:center;gap:16px;min-height:var(--hh)}
.logo{display:flex;align-items:center;gap:10px;font-weight:800;font-size:1.18rem;color:var(--ink);text-decoration:none;letter-spacing:-.02em;margin-right:auto}
.logo-mark{flex:none}
.menu{display:flex;align-items:center;gap:6px}
.mnav{list-style:none;margin:0;padding:0;display:flex;gap:2px}
.dd{position:relative}.dd-row{display:flex;align-items:center}
.top{display:block;padding:10px 4px 10px 12px;font-weight:650;color:var(--ink);text-decoration:none;border-radius:10px;white-space:nowrap}
.top[aria-current]{color:var(--g2);box-shadow:inset 0 -3px 0 var(--y)}
.dd-t{border:0;background:none;color:var(--mut);padding:10px 8px 10px 2px;cursor:pointer;display:flex;min-height:44px;align-items:center;border-radius:8px}
.dd-t .ic{transition:transform .15s}.dd.open .dd-t .ic{transform:rotate(180deg)}
.panel{display:none;position:absolute;left:0;top:100%;background:#fff;border:1px solid var(--line);border-radius:var(--r);box-shadow:var(--sh);padding:18px;min-width:280px;z-index:60}
.panel ul{list-style:none;margin:0 0 6px;padding:0}.panel li a{display:flex;align-items:center;gap:9px;padding:7px 8px;border-radius:8px;color:var(--ink);text-decoration:none;font-size:.95rem}
.panel li a:hover{background:var(--g4);color:var(--g)}.panel li a .ic{color:var(--g2)}
.ph{font-size:.75rem;text-transform:uppercase;letter-spacing:.08em;color:var(--mut);font-weight:700;margin:0 0 6px}.ph+ul{margin-bottom:12px}
.pnote{font-size:.85rem;color:var(--mut);margin:6px 8px 0}
.pbyer li{display:flex;align-items:center;gap:4px;flex-wrap:wrap}.pbyer .cn{font-weight:700;min-width:84px;font-size:.95rem}.pbyer li a{font-size:.9rem;padding:6px 8px}
.menu-btn{display:none;align-items:center;gap:8px;border:1px solid var(--line);background:#fff;border-radius:10px;padding:8px 12px;font:inherit;font-weight:650;color:var(--ink);min-height:44px;cursor:pointer}
.menu-btn .i-close{display:none}.menu-btn[aria-expanded=true] .i-close{display:block}.menu-btn[aria-expanded=true] .i-open{display:none}
@media(min-width:960px){
 .dd:hover .panel,.dd:focus-within .panel,.dd.open .panel{display:block}
 .dd:nth-child(-n+2) .panel{display:none;grid-template-columns:1fr 1fr;gap:24px;min-width:520px}
 .dd:nth-child(-n+2):hover .panel,.dd:nth-child(-n+2):focus-within .panel,.dd:nth-child(-n+2).open .panel{display:grid}
 .dd:nth-child(3) .panel{min-width:430px}.dd:last-child .panel{right:0;left:auto}
}
@media(max-width:959px){
 .js .menu-btn{display:flex}
 .js .menu{display:none;position:fixed;inset:var(--hh) 0 0 0;background:#fff;flex-direction:column;align-items:stretch;padding:12px 20px 28px;overflow-y:auto;border-top:1px solid var(--line);gap:12px}
 .js .menu.open{display:flex}
 html:not(.js) .hdr{flex-wrap:wrap}html:not(.js) .menu{flex-wrap:wrap}
 .mnav{flex-direction:column;gap:0}
 .dd{border-bottom:1px solid var(--line)}
 .top{flex:1;padding:14px 4px;font-size:1.1rem}
 .top[aria-current]{box-shadow:none}
 .dd-t{padding:12px}
 .panel{position:static;box-shadow:none;border:0;padding:0 0 12px;min-width:0}
 .dd.open .panel{display:block}
 html:not(.js) .panel{display:block}
 .pcities{display:grid;grid-template-columns:1fr 1fr}
 .hdr-cta{width:100%;text-align:center;justify-content:center}
 body.menu-open{overflow:hidden}
}
.hdr-cta{margin-left:6px}
/* buttons */
.btn{display:inline-flex;align-items:center;justify-content:center;gap:8px;background:var(--g);color:#fff;border:0;border-radius:11px;padding:12px 18px;font:inherit;font-weight:720;cursor:pointer;text-decoration:none;min-height:46px;line-height:1.2;transition:background .15s,transform .15s}
.btn:hover{background:var(--g2);color:#fff}.btn:active{transform:translateY(1px)}
.btn.ghost{background:#fff;color:var(--g);border:1.5px solid #c7d6d0}.btn.ghost:hover{border-color:var(--g2);background:var(--g4)}
.btn-lg{padding:15px 22px;font-size:1.05rem;min-height:52px}.btn-block{width:100%}
.txtlink{display:inline-flex;align-items:center;gap:6px;font-weight:650;text-decoration:none;padding:12px 4px}
/* hero */
.hero{background:radial-gradient(1200px 400px at 85% -10%,#fff4cc 0,rgba(255,244,204,0) 60%),linear-gradient(180deg,var(--g3),#fff 85%);padding:20px 0 34px;border-bottom:1px solid var(--line)}
.hero-grid{display:grid;grid-template-columns:minmax(0,1fr);gap:26px}
@media(min-width:960px){.hero-grid{grid-template-columns:minmax(0,1.05fr) minmax(0,.95fr);align-items:start;gap:48px}.hero{padding:30px 0 56px}.hero-txt{padding-top:18px}}
.eyebrow{display:inline-flex;align-items:center;gap:8px;font-size:.85rem;font-weight:700;color:var(--g);background:#fff;border:1px solid var(--line);border-radius:999px;padding:5px 12px;margin:14px 0 4px}.eyebrow .ic{color:#c98f00}
.lead-p{font-size:1.1rem;color:#24332f;max-width:62ch}@media(min-width:900px){.lead-p{font-size:1.18rem}}
.usp{list-style:none;padding:0;margin:16px 0}.usp li{display:flex;gap:10px;align-items:center;margin:8px 0;font-weight:650}
.usp .ic{color:#fff;background:var(--g2);border-radius:50%;padding:3px;width:22px;height:22px;stroke-width:3}
.usp-row{display:flex;flex-wrap:wrap;gap:4px 24px}
.hero-actions{display:flex;flex-wrap:wrap;gap:8px 16px;align-items:center;margin:18px 0}
@media(min-width:960px){.hero-actions:not(.show){display:none}}
@media(max-width:959px){.hero-grid{gap:0}.hero-txt{display:contents}.hero-txt>*{order:1}.hero-form{order:2;margin-top:8px}.hero-txt>.disclose{order:3;margin-top:18px}.hero-pick{order:4}.hero .lead-p{font-size:1.05rem;margin-bottom:12px}.hero-txt>.usp{margin-top:0}.hero-actions{margin:6px 0 18px}}
.disclose{display:flex;gap:10px;align-items:flex-start;font-size:.9rem;color:var(--mut);background:rgba(255,255,255,.8);border:1px solid var(--line);border-radius:12px;padding:10px 12px;max-width:62ch;margin:14px 0 0}.disclose .ic{color:var(--g2);margin-top:2px}
.crumbs ol{list-style:none;padding:0;margin:0;display:flex;font-size:.88rem;color:var(--mut);white-space:nowrap;overflow-x:auto;scrollbar-width:none}
.crumbs ol::-webkit-scrollbar{display:none}
.crumbs li{display:flex;align-items:center}.crumbs li+li:before{content:"›";margin:0 8px;color:#8a9a95}
.crumbs a{color:var(--mut);text-decoration:none;padding:8px 0;display:inline-block}.crumbs a:hover{color:var(--g)}.crumbs [aria-current]{color:var(--ink);font-weight:600}
/* form */
.lead{background:#fff;border:1px solid var(--line);border-radius:18px;box-shadow:0 2px 4px rgba(16,40,34,.05),0 18px 48px rgba(16,40,34,.12);padding:20px;scroll-margin-top:calc(var(--hh) + 12px)}
@media(min-width:600px){.lead{padding:26px}}
.lead-h{display:flex;gap:12px;align-items:center;margin-bottom:14px}.lead-h strong{display:block;font-size:1.2rem;line-height:1.25}.lead-h span{font-size:.9rem;color:var(--mut)}
.lead-ic{flex:none;width:44px;height:44px;border-radius:12px;background:var(--y2);display:flex;align-items:center;justify-content:center;color:#946a00}.lead-ic .ic{width:24px;height:24px}
.stepper{list-style:none;display:flex;gap:6px;padding:0;margin:0 0 10px;font-size:.82rem;color:var(--mut)}
.stepper li{flex:1;display:flex;align-items:center;gap:6px;font-weight:600}
.stepper li span{width:22px;height:22px;border-radius:50%;background:var(--bg);border:1px solid var(--line);display:flex;align-items:center;justify-content:center;font-size:.75rem;flex:none}
.stepper li.on{color:var(--ink)}.stepper li.on span{background:var(--y);border-color:var(--y);color:var(--ink)}
.stepper li.done span{background:var(--g2);border-color:var(--g2);color:#fff}
.progress{height:6px;background:#e8eeeb;border-radius:9px;margin:0 0 16px;overflow:hidden}.progress span{display:block;height:100%;width:33%;background:linear-gradient(90deg,var(--y),#f9cf4a);transition:width .25s}
fieldset{border:0;margin:0;padding:0;min-width:0}legend{font-weight:750;font-size:1.05rem;margin-bottom:10px;padding:0}
.js .step{display:none}.js .step.on{display:block}
html:not(.js) .progress,html:not(.js) .stepper{display:none}
.opts{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-bottom:12px}
.opt{cursor:pointer;display:block}.opt input{position:absolute;opacity:0;pointer-events:none}
.ob{display:flex;gap:10px;align-items:center;border:1.5px solid #d5dfdb;border-radius:12px;padding:12px;min-height:52px;font-size:.95rem;font-weight:600;line-height:1.25;background:#fff;transition:border-color .15s,background .15s}
.oc{width:20px;height:20px;border:1.5px solid #b9c8c2;border-radius:6px;padding:2px;stroke:transparent;stroke-width:3;background:#fff}
.opt:hover .ob{border-color:var(--g2)}
.opt input:checked+.ob{border-color:var(--g2);background:var(--g4)}.opt input:checked+.ob .oc{background:var(--g2);border-color:var(--g2);stroke:#fff}
.opt input:focus-visible+.ob{outline:3px solid var(--y);outline-offset:2px}
.fld{display:block;font-size:.93rem;font-weight:650;margin:10px 0}
.opt-l{font-weight:400;color:var(--mut);font-size:.88rem}
.fld input,.fld select{display:block;width:100%;margin-top:5px;font:inherit;font-size:16px;padding:11px 12px;border:1.5px solid #cfdad6;border-radius:10px;min-height:48px;background:#fff;color:var(--ink)}
.fld input:focus,.fld select:focus{border-color:var(--g2);outline:3px solid rgba(245,183,0,.45);outline-offset:0}
.row2{display:grid;grid-template-columns:1fr 1fr;gap:10px}.row2 .fld{margin-top:0}
.consent{display:flex;gap:10px;align-items:flex-start;font-size:.88rem;margin:12px 0 8px;background:var(--bg);padding:12px;border-radius:10px;line-height:1.5}
.hp{position:absolute!important;left:-9999px!important;width:1px;height:1px;overflow:hidden}
.consent input{margin-top:3px;min-width:20px;min-height:20px;accent-color:var(--g2)}
.nav-btns{display:flex;gap:10px;justify-content:space-between;margin-top:14px}.nav-btns [data-next],.nav-btns [data-submit]{flex:1}
.js [data-prev],.js [data-submit]{display:none}
html:not(.js) [data-next],html:not(.js) [data-prev]{display:none}
.form-foot{display:flex;align-items:center;gap:8px;justify-content:center;font-size:.85rem;color:var(--mut);margin:12px 0 0}.form-foot .ic{color:var(--g2)}
.form-msg{margin-top:10px;font-size:.92rem}.form-msg:empty{display:none}.form-msg.err{color:#a1261b;background:#fdeceb;padding:10px 12px;border-radius:10px}.form-msg.ok{background:var(--y2);border:1px solid #f0d77a;padding:10px 12px;border-radius:10px}
/* content layout */
.layout{display:grid;grid-template-columns:minmax(0,1fr);gap:0 48px;padding-top:8px}
@media(min-width:1080px){.layout{grid-template-columns:250px minmax(0,1fr)}.side{position:sticky;top:calc(var(--hh) + 20px);align-self:start;padding-top:40px}}
.content{max-width:800px;min-width:0}
.content>section,.content-wide>section{padding:40px 0 4px;border-bottom:1px solid var(--line)}
.content>section:last-child,.content-wide>section:last-child{border-bottom:0}
.content>p{margin-top:24px}
.toc-h{font-size:.75rem;text-transform:uppercase;letter-spacing:.08em;color:var(--mut);font-weight:700;margin:0 0 8px}
.toc ol{list-style:none;margin:0;padding:0}
.toc a{display:block;text-decoration:none;color:var(--mut);font-size:.93rem;padding:6px 12px;border-left:2px solid var(--line)}
.toc a:hover{color:var(--g);border-left-color:var(--g2)}.toc a.on{color:var(--g);border-left-color:var(--y);font-weight:650}
.side-cta{margin-top:24px;background:var(--g);color:#fff;border-radius:var(--r);padding:18px}.side-cta .sc-h{font-weight:750;font-size:1.05rem;margin-bottom:8px}
.side-cta .btn{background:var(--y);color:var(--ink)}.side-cta .btn:hover{background:#ffcb2e;color:var(--ink)}
.mini-usp{list-style:none;padding:0;margin:0 0 14px;font-size:.9rem}.mini-usp li{display:flex;gap:8px;align-items:center;margin:4px 0}.mini-usp .ic{color:var(--y)}
@media(max-width:1079px){
 .side-cta{display:none}
 .side{padding-top:18px}
 .toc{display:flex;align-items:center;gap:10px;overflow-x:auto;scrollbar-width:none;margin:0 -20px;padding:0 20px 4px}
 .toc::-webkit-scrollbar{display:none}
 .toc-h{margin:0;white-space:nowrap}
 .toc ol{display:flex;gap:8px}
 .toc a{border:1px solid var(--line);border-radius:999px;white-space:nowrap;padding:8px 14px;background:#fff}
}
.facts{list-style:none;padding:0;margin:0 0 18px}
.facts li{position:relative;padding:14px 16px 14px 48px;margin:10px 0;background:var(--g4);border:1px solid #dcebe5;border-radius:12px}
.facts li:before{content:"";position:absolute;left:16px;top:17px;width:20px;height:20px;border-radius:50%;background:var(--g2) url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23fff' stroke-width='3.2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M20 6 9 17l-5-5'/%3E%3C/svg%3E") center/13px no-repeat}
.src{display:block;font-size:.8rem;color:var(--mut);margin-top:4px}.src a{color:var(--mut)}
.steps{counter-reset:s;list-style:none;padding:0;display:grid;gap:14px;margin:0 0 18px}
@media(min-width:760px){.steps{grid-template-columns:repeat(3,1fr)}}
.steps li{border:1px solid var(--line);border-radius:var(--r);padding:18px;position:relative;background:#fff}
.steps li:after{counter-increment:s;content:counter(s);position:absolute;top:16px;right:16px;font-weight:800;color:#c9d5d1;font-size:1.4rem}
.st-ic{width:44px;height:44px;border-radius:12px;background:var(--g3);color:var(--g);display:flex;align-items:center;justify-content:center;margin-bottom:10px}.st-ic .ic{width:22px;height:22px}
.steps strong,.steps span{display:block}.steps span{color:var(--mut);font-size:.95rem}
.note{background:var(--y2);border:1px solid #f2e3a6;padding:14px 16px;border-radius:12px;font-size:.95rem;margin:16px 0}
.note-ic{display:flex;gap:12px;background:#fff;border:1px solid var(--line)}.note-ic>.ic{color:var(--g2);width:24px;height:24px;margin-top:2px}
.tbl{overflow-x:auto;border:1px solid var(--line);border-radius:12px;margin:8px 0}
table{border-collapse:collapse;width:100%;font-size:.93rem}th,td{text-align:left;padding:11px 12px;border-bottom:1px solid var(--line);vertical-align:top}
tbody tr:last-child td{border-bottom:0}thead th{background:var(--g4);font-weight:700;white-space:nowrap}
tr.avg td{font-weight:700;background:var(--bg)}
@media(max-width:600px){th,td{padding:9px 7px;font-size:.86rem}thead th{white-space:normal}td+td{white-space:nowrap}.tbl-towns td+td+td{white-space:normal}}
.tbl-months th,.tbl-months td{padding:8px 6px;text-align:center;font-size:.85rem;min-width:44px}
.tbl-towns td .src{display:block;margin-top:2px}
.mgrid{display:grid;grid-template-columns:1fr 1fr;gap:8px}@media(max-width:700px){.mgrid{grid-template-columns:1fr;gap:0}}
.example{background:#fffbea;border:1px solid #f3e3a1;border-radius:var(--r);padding:14px 16px;margin:14px 0;font-size:.95rem}
.check{list-style:none;padding:0}.check li{padding-left:30px;position:relative;margin:8px 0}
.check li:before{content:"";position:absolute;left:0;top:4px;width:18px;height:18px;border:2px solid var(--g2);border-radius:5px}
.faq details{border:1px solid var(--line);border-radius:12px;margin:10px 0;background:#fff;transition:box-shadow .15s}
.faq details[open]{box-shadow:var(--sh)}
.faq summary{cursor:pointer;font-weight:700;padding:16px 48px 16px 16px;list-style:none;position:relative}
.faq summary::-webkit-details-marker{display:none}
.pm{position:absolute;right:16px;top:50%;width:20px;height:20px;margin-top:-10px;border-radius:50%;background:var(--g3)}
.pm:before,.pm:after{content:"";position:absolute;left:5px;right:5px;top:9px;height:2px;background:var(--g)}.pm:after{transform:rotate(90deg);transition:transform .15s}
details[open] .pm:after{transform:rotate(0)}
.fa{padding:0 16px 4px}.fa p{margin:0 0 14px}
.how-short{background:var(--g4);border:1px solid #dcebe5!important;border-radius:var(--r);padding:24px!important;margin-top:36px}
/* cards */
.rgrid{display:grid;gap:12px;margin:12px 0}@media(min-width:700px){.rgrid{grid-template-columns:1fr 1fr}}
.rcard{display:flex;gap:14px;align-items:flex-start;border:1px solid var(--line);border-radius:var(--r);padding:16px;text-decoration:none;color:var(--ink);background:#fff;transition:border-color .15s,box-shadow .15s,transform .15s}
.rcard:hover{border-color:var(--g2);box-shadow:var(--sh);transform:translateY(-1px);color:var(--ink)}
.rc-ic{flex:none;width:42px;height:42px;border-radius:11px;background:var(--g3);color:var(--g);display:flex;align-items:center;justify-content:center}.rc-ic .ic{width:22px;height:22px}
.rc-b{flex:1;min-width:0}.rc-b strong{display:block;font-size:1.02rem;line-height:1.3;margin-bottom:3px}.rc-b span{display:block;color:var(--mut);font-size:.92rem;line-height:1.5}
.rc-go{color:var(--g2);margin-top:12px}
.rcard-hl{background:linear-gradient(135deg,var(--g4),#fff);border-color:#cfe3db}.rcard-hl .rc-ic{background:var(--y2);color:#8a6200}
.links{padding-bottom:28px!important}
.picker{display:grid;gap:22px;margin-top:22px}@media(min-width:760px){.picker{grid-template-columns:1fr 1fr}}
.chips{list-style:none;padding:0;margin:0 0 8px;display:flex;flex-wrap:wrap;gap:8px}
.chip{display:inline-flex;align-items:center;min-height:40px;padding:8px 14px;border:1px solid #d3ded9;border-radius:999px;text-decoration:none;color:var(--ink);font-size:.93rem;font-weight:600;background:#fff}
a.chip:hover{border-color:var(--g2);color:var(--g);background:var(--g4)}.chip.on{background:var(--g);border-color:var(--g);color:#fff}
.more{display:inline-flex;align-items:center;gap:6px;font-weight:650;text-decoration:none;font-size:.93rem;margin-right:16px;padding:6px 0}
.glist{list-style:none;padding:0;margin:0}.glist a{display:flex;gap:8px;align-items:center;padding:6px 0;text-decoration:none;font-weight:600}
.citylist{list-style:none;padding:0;margin:0 0 20px;display:grid;gap:8px}@media(min-width:700px){.citylist{grid-template-columns:1fr 1fr}}
.citylist li{display:flex;flex-direction:column;border:1px solid var(--line);border-radius:12px;padding:12px 14px}.citylist .cn{display:flex;gap:6px;align-items:center;font-weight:750}.citylist .cn .ic{color:var(--g2)}.citylist a{text-decoration:none;font-weight:600}.citylist a{display:inline-block;padding:3px 0;min-height:24px}
.cards{display:grid;gap:14px}@media(min-width:700px){.cards{grid-template-columns:repeat(2,1fr)}}
.card{display:flex;flex-direction:column;gap:6px;border:1px solid var(--line);border-radius:var(--r);padding:16px;background:#fff;transition:border-color .15s,box-shadow .15s}.card:hover{border-color:var(--g2);box-shadow:var(--sh)}
.card-t{display:flex;align-items:center;gap:8px;text-decoration:none;font-size:1.05rem}.card-t .ic{color:var(--g2)}.card span{font-size:.92rem;color:var(--mut)}
.card .sub{display:inline-flex;align-items:center;gap:6px;margin-top:auto;padding-top:6px;font-size:.92rem;font-weight:650;text-decoration:none}
/* home */
.hero-home{padding:28px 0 44px}@media(min-width:960px){.hero-home{padding:48px 0 64px}.hero-home h1{max-width:20ch}}
.svc-grid{display:grid;gap:14px;margin:24px 0 8px}@media(min-width:760px){.svc-grid{grid-template-columns:1fr 1fr;max-width:920px}}
.svc{display:flex;flex-direction:column;gap:6px;background:#fff;border:1px solid var(--line);border-radius:18px;padding:22px;text-decoration:none;color:var(--ink);box-shadow:var(--sh);transition:transform .15s,border-color .15s}
.svc:hover{transform:translateY(-2px);border-color:var(--g2);color:var(--ink)}
.svc-ic{width:52px;height:52px;border-radius:14px;background:var(--y2);color:#8a6200;display:flex;align-items:center;justify-content:center;margin-bottom:6px}.svc-ic .ic{width:28px;height:28px}
.svc strong{font-size:1.3rem;letter-spacing:-.01em}.svc>span{color:var(--mut)}.svc .svc-go{display:inline-flex;align-items:center;gap:6px;color:var(--g2);font-weight:700;margin-top:6px}
.content-wide>section{padding:52px 0 12px}
.sub-h{color:var(--mut);max-width:62ch}
.citygrid{list-style:none;padding:0;margin:18px 0 0;display:grid;gap:14px}@media(min-width:640px){.citygrid{grid-template-columns:1fr 1fr}}@media(min-width:1000px){.citygrid{grid-template-columns:repeat(3,1fr)}}
.city{border:1px solid var(--line);border-radius:var(--r);padding:16px;background:#fff;display:flex;flex-direction:column;gap:10px}
.city-n{display:flex;align-items:baseline;gap:8px;margin:0;flex-wrap:wrap}.city-n strong{font-size:1.2rem}.city-n span{color:var(--mut);font-size:.88rem}.city-n .ic{color:var(--g2);align-self:center}
.city-a{display:grid;grid-template-columns:1fr;gap:8px}@media(min-width:640px) and (max-width:999px){.city-a{grid-template-columns:1fr 1fr}}
.cbtn{display:flex;align-items:center;gap:8px;justify-content:center;text-align:center;border-radius:10px;padding:10px;min-height:46px;background:var(--g4);border:1px solid #d6e8e0;text-decoration:none;color:var(--g);font-weight:700;font-size:.92rem;line-height:1.2}
.cbtn:hover{background:var(--g);color:#fff;border-color:var(--g)}
.city-s{display:flex;flex-wrap:wrap;gap:4px 14px;font-size:.88rem}.city-s a{color:var(--mut);padding:4px 0}
.about-band>div{background:var(--g);color:#e6f1ed;border-radius:20px;padding:28px}.about-band h2{color:#fff}.about-band .btn.ghost{background:transparent;color:#fff;border-color:rgba(255,255,255,.5)}
.about-band{border:0!important;padding-bottom:56px!important}
.city-other{background:var(--bg);border-style:dashed}.city-other p.small{margin:0;color:var(--mut)}
.hero-home .hero-grid{align-items:center}
.hero-pick{background:#fff;border:1px solid var(--line);border-radius:18px;box-shadow:var(--sh);padding:22px}
.hp-h{display:flex;align-items:center;gap:8px;font-weight:800;font-size:1.2rem;margin:0 0 12px}.hp-h .ic{color:var(--g2)}
.hp-l{display:flex;align-items:center;gap:8px;font-weight:700;font-size:.92rem;color:var(--mut);margin:14px 0 8px}.hp-l .ic{color:#c98f00}
.hp-f{font-size:.85rem;color:var(--mut);margin:12px 0 0}
@media(max-width:959px){.hero-pick{display:none}}
@media(max-width:759px){.svc{display:grid;grid-template-columns:48px 1fr;column-gap:14px;padding:16px}.svc-ic{grid-row:span 3;width:48px;height:48px;margin:0}.svc-ic .ic{width:24px;height:24px}.svc strong{font-size:1.12rem}.svc>span{font-size:.93rem}}
/* simple pages */
.content.narrow{padding:24px 20px 40px}.content.narrow h2{margin-top:1.6em}
/* footer */
.site-footer{background:#0a2a24;color:#cfe0da;margin-top:56px;padding:44px 0 28px;font-size:.93rem}
.site-footer a{color:#fff;text-decoration:none}.site-footer a:hover{text-decoration:underline}
.site-footer .wrap{display:grid;gap:30px}@media(min-width:1000px){.site-footer .wrap{grid-template-columns:280px 1fr}}
.logo-inv{color:#fff;margin-bottom:10px}
.fmap{display:grid;gap:22px;grid-template-columns:repeat(2,1fr)}@media(min-width:760px){.fmap{grid-template-columns:repeat(5,1fr)}}
.fh{font-weight:750;color:#fff;margin:0 0 8px;font-size:.92rem}
.site-footer ul{list-style:none;padding:0;margin:0 0 14px}.site-footer li{margin:0}.site-footer li a{display:inline-block;padding:4px 0;color:#d6e6e0}
.small{font-size:.86rem}.muted{color:var(--mut)}.site-footer .muted{color:#9fbab2}
.fbase{grid-column:1/-1;border-top:1px solid rgba(255,255,255,.12);padding-top:16px;margin:0}
.plain{list-style:none;padding:0;margin:6px 0 0}.plain li{margin:4px 0}
.srclist li{margin:4px 0;font-size:.92rem}
/* sticky mobil-CTA */
.mcta{display:none}
@media(max-width:959px){
 .js .mcta{display:block;position:fixed;left:0;right:0;bottom:0;z-index:40;padding:10px 14px calc(10px + env(safe-area-inset-bottom));background:rgba(255,255,255,.97);border-top:1px solid var(--line);box-shadow:0 -6px 20px rgba(16,40,34,.08);transition:transform .2s}
 .js .mcta .btn{width:100%;background:var(--y);color:var(--ink)}
 .js .mcta.hide{transform:translateY(120%)}
 .js body{padding-bottom:76px}
}
@media(max-width:420px){.opts{grid-template-columns:1fr}.row2{grid-template-columns:1fr}.logo span{font-size:1.05rem}}
/* v7: diagrammer, beregner, opdateret-dato */
.chart{margin:18px 0}.chart img{display:block;width:100%;height:auto;border:1px solid var(--line);border-radius:12px;background:#fff}.chart figcaption{font-size:.84rem;color:var(--mut);margin-top:6px}
.calc{display:grid;gap:20px;border:1px solid var(--line);border-radius:var(--r);padding:20px;background:var(--g4);margin:16px 0}
@media(min-width:1000px){.calc{grid-template-columns:1.5fr 1fr}}
.cgrid{display:grid;gap:16px}@media(min-width:600px){.cgrid{grid-template-columns:1fr 1fr}}
.cf{display:flex;flex-direction:column;gap:4px;font-size:.92rem}.cf-l{font-weight:650}.cf-in{display:flex;align-items:center;gap:8px}
.cf-in input,.cf-in select{width:100%;min-height:44px;padding:8px 10px;border:1px solid #b9c9c3;border-radius:10px;font:inherit;background:#fff;color:var(--ink)}
.cf-u{color:var(--mut);white-space:nowrap;font-size:.85rem}.cf-h{font-size:.8rem;color:var(--mut);line-height:1.45}.cf-h .src{display:inline;margin:0}
.cf-chk{grid-column:1/-1}.cf-chk input{width:20px;height:20px;vertical-align:-4px;margin:0 6px 0 0;accent-color:var(--g)}
.cres{background:#fff;border:1px solid var(--line);border-radius:12px;padding:16px;align-self:start}
@media(min-width:1000px){.cres{position:sticky;top:calc(var(--hh) + 12px)}}
.cres-h{font-weight:780;margin:0 0 6px}.cres dl{margin:0 0 10px}.cres dl>div{display:flex;justify-content:space-between;gap:12px;padding:8px 0;border-bottom:1px solid var(--line)}
.cres dt{color:var(--mut);font-size:.9rem}.cres dd{margin:0;font-weight:700;text-align:right}.cres .big dd{font-size:1.25rem;color:var(--g)}
.hero-calc .hero-txt{max-width:860px}.upd{margin:-4px 0 18px}

/* elpris */
.vh{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
.el-tabs{display:none;gap:8px;margin:6px 0 4px;flex-wrap:wrap}.js .el-tabs{display:flex}
.el-tabs button{font:inherit;cursor:pointer;border:1px solid var(--line);background:#fff;color:var(--ink);border-radius:12px;padding:10px 14px;min-height:48px;text-align:left;display:flex;flex-direction:column;font-weight:700}
.el-tabs button small{font-weight:400;color:var(--mut);font-size:.82rem}
.el-tabs button[aria-selected=true]{border-color:var(--g);background:var(--g3);box-shadow:inset 0 0 0 1px var(--g)}
.el-panel{margin-top:6px}.el-panel h3{margin-top:22px}.el-ph{font-size:1.25rem;margin:18px 0 0}
.elkeys{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:10px;margin:12px 0}
.elkeys div{background:#fff;border:1px solid var(--line);border-radius:12px;padding:10px 12px}
.elkeys dt{font-size:.84rem;color:var(--mut)}.elkeys dd{margin:2px 0 0;font-weight:800;font-size:1.15rem}.elkeys dd small{display:block;font-weight:400;font-size:.8rem;color:var(--mut)}
.elsvg{display:block;width:100%;height:auto;background:#fff;border:1px solid var(--line);border-radius:12px}
.elsvg text{font:12px system-ui,-apple-system,Segoe UI,Roboto,sans-serif;fill:#4f5e5a}
.elsvg .b-tot{fill:#9fd3bf}.elsvg .b-spot{fill:#0b4f43}.elsvg .now{stroke:#c0392b;stroke-width:2}
.lg{display:inline-block;width:12px;height:12px;border-radius:3px;vertical-align:-1px;margin:0 4px 0 0}.lg-tot{background:#9fd3bf}.lg-spot{background:#0b4f43;margin-left:10px}
.eldet{margin:8px 0 4px}.eldet summary{cursor:pointer;font-weight:700;color:var(--g);padding:10px 0;min-height:44px}
.tbl-el td:first-child{white-space:nowrap}
.el-now{font-weight:700;background:#fff;border:1px solid var(--line);border-left:4px solid #c0392b;border-radius:10px;padding:10px 12px;max-width:62ch}
.elbox{background:var(--g4);border:1px solid var(--line);border-radius:var(--r);padding:16px 18px;margin:28px 0}
.elbox h2{font-size:1.2rem;display:flex;gap:8px;align-items:center;margin:0 0 6px}.elbox h2 .ic{color:var(--y)}
.elmini{list-style:none;padding:0;margin:10px 0;display:grid;grid-template-columns:repeat(auto-fit,minmax(120px,1fr));gap:8px}
.elmini li{background:#fff;border:1px solid var(--line);border-radius:10px;padding:8px 10px;display:flex;flex-direction:column}.elmini span{font-size:.8rem;color:var(--mut)}.elmini strong{font-size:1rem}
.cf-x .cf-btns{display:flex;gap:8px;flex-wrap:wrap;margin:6px 0}.cf-x .chip{font:inherit;cursor:pointer;min-height:44px}
"""

JS = r"""(function(){
  var d=document, b=d.body;
  // mobilmenu
  var mb=d.querySelector('.menu-btn'), menu=d.getElementById('menu');
  function setMenu(o){ if(!mb) return; mb.setAttribute('aria-expanded',o?'true':'false'); menu.classList.toggle('open',o); b.classList.toggle('menu-open',o); }
  if(mb){ mb.addEventListener('click',function(){ setMenu(mb.getAttribute('aria-expanded')!=='true'); });
    menu.addEventListener('click',function(e){ var a=e.target.closest('a'); if(a && a.getAttribute('href').indexOf('#')>-1) setMenu(false); }); }
  // dropdowns
  [].slice.call(d.querySelectorAll('.dd-t')).forEach(function(t){ t.addEventListener('click',function(){
    var li=t.closest('.dd'), o=!li.classList.contains('open');
    [].slice.call(d.querySelectorAll('.dd.open')).forEach(function(x){ if(x!==li){x.classList.remove('open'); x.querySelector('.dd-t').setAttribute('aria-expanded','false');} });
    li.classList.toggle('open',o); t.setAttribute('aria-expanded',o?'true':'false'); }); });
  d.addEventListener('keydown',function(e){ if(e.key==='Escape'){ setMenu(false); [].slice.call(d.querySelectorAll('.dd.open')).forEach(function(x){x.classList.remove('open');}); } });
  d.addEventListener('click',function(e){ if(!e.target.closest('.dd')) [].slice.call(d.querySelectorAll('.dd.open')).forEach(function(x){ if(window.innerWidth>=960){x.classList.remove('open'); x.querySelector('.dd-t').setAttribute('aria-expanded','false');} }); });
  // sticky mobil-CTA: skjul når formularen eller bunden er synlig
  var mc=d.getElementById('mcta'), f=d.getElementById('lead-form');
  if(mc && 'IntersectionObserver' in window){ var seen=new Set(); mc.classList.add('hide');
    var io=new IntersectionObserver(function(es){ es.forEach(function(en){ if(en.isIntersecting) seen.add(en.target); else seen.delete(en.target); }); mc.classList.toggle('hide',seen.size>0); },{rootMargin:'0px 0px -8% 0px'});
    [d.querySelector('.hero-actions'),f,d.getElementById('byer'),d.querySelector('.site-footer')].forEach(function(t){ if(t) io.observe(t); }); }
  // aktiv sektion i "På denne side"
  var tl=[].slice.call(d.querySelectorAll('.toc a'));
  if(tl.length && 'IntersectionObserver' in window){ var map={}; tl.forEach(function(a){ map[a.getAttribute('href').slice(1)]=a; });
    var so=new IntersectionObserver(function(es){ es.forEach(function(en){ if(en.isIntersecting){ tl.forEach(function(a){a.classList.remove('on');}); var a=map[en.target.id]; if(a) a.classList.add('on'); } }); },{rootMargin:'-20% 0px -70% 0px'});
    Object.keys(map).forEach(function(id){ var s=d.getElementById(id); if(s) so.observe(s); }); }
  // elpris: vis note, hvis den indbyggede dag ikke er i dag (siden er statisk og opdateres dagligt)
  try{ var td=new Intl.DateTimeFormat('sv-SE',{timeZone:'Europe/Copenhagen'}).format(new Date()).slice(0,10);
    [].slice.call(d.querySelectorAll('[data-elday]')).forEach(function(x){ if(x.getAttribute('data-elday')!==td){ var n=x.classList.contains('el-stale')?x:x.querySelector('.el-stale'); if(n) n.hidden=false; } }); }catch(_){}
  // formular: sender til Supabase (kun INSERT tilladt via RLS)
  if(!f) return;
  var steps=[].slice.call(f.querySelectorAll('.step')), i=0, sl=[].slice.call(f.querySelectorAll('.stepper li')), cnt=f.querySelector('.step-count');
  var bar=f.querySelector('.progress span'), prev=f.querySelector('[data-prev]'), next=f.querySelector('[data-next]'), sub=f.querySelector('[data-submit]'), msg=f.querySelector('.form-msg');
  function show(n,focus){ steps.forEach(function(s,k){s.classList.toggle('on',k===n)}); i=n;
    sl.forEach(function(li,k){ li.classList.toggle('on',k===n); li.classList.toggle('done',k<n); });
    if(cnt) cnt.textContent='Trin '+(n+1)+' af '+steps.length;
    bar.style.width=((n+1)/steps.length*100)+'%';
    prev.style.display=n>0?'inline-flex':'none'; next.style.display=n<steps.length-1?'inline-flex':'none'; sub.style.display=n===steps.length-1?'inline-flex':'none'; msg.textContent=''; msg.className='form-msg';
    if(focus){ var l=steps[n].querySelector('legend'); var r=f.getBoundingClientRect(); if(r.top<60) f.scrollIntoView({block:'start'}); var el=steps[n].querySelector('input:not([type=hidden]),select'); if(el && window.innerWidth>=960) el.focus({preventScroll:true}); } }
  function valid(s){ var bad=null; [].slice.call(s.querySelectorAll('input,select')).forEach(function(el){ if(!bad && !el.checkValidity()) bad=el; });
    if(bad){ msg.textContent= bad.type==='checkbox' ? 'Du skal give samtykke, før vi kan sende din forespørgsel videre.' : (bad.type==='radio' ? 'Vælg en af mulighederne for at fortsætte.' : 'Tjek feltet: '+((bad.closest('label')||{}).textContent||'').trim().split('\n')[0].split('(')[0].trim()); msg.className='form-msg err'; if(bad.focus) bad.focus(); return false;} return true; }
  next.addEventListener('click',function(){ if(valid(steps[i])) show(i+1,true); });
  prev.addEventListener('click',function(){ show(i-1,true); });
  var SB_URL='__SB_URL__', SB_KEY='__SB_KEY__', CV='__CV__', busy=false;
  function val(n){ var el=f.elements[n]; if(!el) return ''; if(el.length!==undefined && !el.tagName){ for(var k=0;k<el.length;k++){ if(el[k].checked) return el[k].value; } return ''; } return (el.value||'').trim(); }
  function utm(){ var o={}; try{ var q=new URLSearchParams(location.search); ['utm_source','utm_medium','utm_campaign','utm_term','utm_content','gclid','fbclid'].forEach(function(k){ var v=q.get(k); if(v) o[k]=v.slice(0,100); }); }catch(_){} return o; }
  f.addEventListener('submit',function(e){ e.preventDefault(); if(busy || !valid(steps[i])) return;
    // honeypot: udfyldt af bots -> lad som om alt gik godt, men send intet
    if(val('website')){ location.href='/tak/'; return; }
    var skip={service:1,by:1,navn:1,email:1,telefon:1,postnummer:1,samtykke:1,website:1}, ans={};
    [].slice.call(f.elements).forEach(function(el){ if(!el.name || skip[el.name] || el.type==='button' || el.type==='submit') return; if((el.type==='radio'||el.type==='checkbox') && !el.checked) return; var v=(el.value||'').trim(); if(v) ans[el.name]=v.slice(0,200); });
    var ct=f.querySelector('.consent-txt'), row={ service:f.getAttribute('data-service'), city:(f.getAttribute('data-city')||'').slice(0,60)||null,
      page_url:(location.origin+location.pathname).slice(0,500), answers:ans, name:val('navn').slice(0,120), email:val('email').slice(0,254),
      phone:val('telefon').replace(/[^0-9 +]/g,'').slice(0,20), postal_code:val('postnummer'), consent_text:ct?ct.textContent.replace(/\s+/g,' ').trim():'',
      consent_version:CV, user_agent:(navigator.userAgent||'').slice(0,500), utm:utm() };
    busy=true; sub.disabled=true; msg.className='form-msg'; msg.textContent='Sender …';
    fetch(SB_URL+'/rest/v1/leads',{method:'POST',headers:{'apikey':SB_KEY,'Content-Type':'application/json','Prefer':'return=minimal'},body:JSON.stringify(row)})
      .then(function(r){ if(!r.ok) throw new Error('HTTP '+r.status); try{ sessionStorage.setItem('et_fs',JSON.stringify({service:row.service||'',city:row.city||'',p:location.pathname})); }catch(_){} location.href='/tak/'; })
      .catch(function(){ busy=false; sub.disabled=false; msg.className='form-msg err';
        msg.textContent='Beklager, vi kunne ikke sende din forespørgsel lige nu. Tjek dine oplysninger og prøv igen om lidt, eller skriv til __MAIL__.'; });
  });
  show(0);
})();"""

FAVICON = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><rect width="24" height="24" rx="5" fill="#0b4f43"/><circle cx="12" cy="12" r="5" fill="#f5b700"/></svg>'

def write(path, content):
    fp = os.path.join(OUT, path.lstrip("/"))
    if path.endswith("/"): fp = os.path.join(fp, "index.html")
    os.makedirs(os.path.dirname(fp), exist_ok=True)
    open(fp, "w", encoding="utf-8").write(content)


from config import WEB_ANALYTICS, SPEED_INSIGHTS, FIRST_PARTY_ANALYTICS, FP_ANALYTICS_ENDPOINT, FP_ANALYTICS_SITE
# Cookiefri førstepartsstatistik (<1 KB). Sender kun på det rigtige domæne, respekterer Do Not Track og automatiserede browsere.
FP_JS = ("(function(w,d,n){var E='__E__',S='__S__',H=location.hostname;"
  "if(H!==S&&H!=='www.'+S||n.doNotTrack=='1'||w.doNotTrack=='1'||n.webdriver)return;"
  "function t(e,x,p){try{var q=new URLSearchParams(location.search),b={s:S,e:e,p:p||location.pathname,r:d.referrer,t:d.title,"
  "us:q.get('utm_source'),um:q.get('utm_medium'),uc:q.get('utm_campaign')};if(x)b.x=x;b=JSON.stringify(b);"
  "if(!(n.sendBeacon&&n.sendBeacon(E,b)))fetch(E,{method:'POST',body:b,keepalive:true})}catch(_){}}"
  "w.etT=t;t('pageview');"
  "try{var k=sessionStorage.getItem('et_fs');if(k&&location.pathname=='/tak/'){sessionStorage.removeItem('et_fs');k=JSON.parse(k);"
  "t('form_submit',{service:k.service||'',city:k.city||''},k.p)}}catch(_){}"
  "d.addEventListener('click',function(e){var a=e.target.closest('a[href*=\"/tilbud/\"]');"
  "if(a)t('cta_click',{href:a.getAttribute('href').slice(0,100)})},true);"
  "var o=0;function f(e){var m=!o&&e.target.closest('#lead-form');"
  "if(m){o=1;t('form_open',{service:m.getAttribute('data-service')||'',city:m.getAttribute('data-city')||''})}}"
  "d.addEventListener('focusin',f,true);d.addEventListener('change',f,true)"
  "})(window,document,navigator);").replace("__E__", FP_ANALYTICS_ENDPOINT).replace("__S__", FP_ANALYTICS_SITE)
ANALYTICS_HTML = (("<script>window.va = window.va || function () { (window.vaq = window.vaq || []).push(arguments); };</script><script defer src=\"/_vercel/insights/script.js\"></script>" if WEB_ANALYTICS else "")
                  + ("<script>window.si = window.si || function () { (window.siq = window.siq || []).push(arguments); };</script><script defer src=\"/_vercel/speed-insights/script.js\"></script>" if SPEED_INSIGHTS else "")
                  + (f"<script>{FP_JS}</script>" if FIRST_PARTY_ANALYTICS else ""))

def main():
    if os.path.exists(OUT): shutil.rmtree(OUT)
    os.makedirs(OUT)
    pages = ([home()] + [hub_page(s) for s in SERVICES] + [city_page(s, c) for s in SERVICES for c in CITIES if s == "solceller" or has_vp(c)]
             + [reg_page(c) for c in CITIES] + [fv_page(c) for c in CITIES] + [national_page(p) for p in NATIONAL] + [calc_page(), elpris_page()] + pages_static())
    for p, b in pages: write(p, b)
    write("/assets/style.css", re.sub(r"\n\s*", "\n", CSS.strip()))
    write("/assets/form.js", JS.replace("__SB_URL__", SUPABASE_URL).replace("__SB_KEY__", SUPABASE_PUBLISHABLE_KEY).replace("__CV__", CONSENT_VERSION).replace("__MAIL__", CONTACT_EMAIL))
    write("/favicon.svg", FAVICON)
    write("/assets/calc.js", CALC_JS)
    write("/assets/elpris.js", EL_JS)
    # v7: diagrammer pr. by (genereres automatisk for nye byer)
    for c in CITIES:
        write(f"/assets/charts/opvarmning-{c}.svg", V.heat_svg(CITIES[c]["kommune"], chart_data("heat", c)))
        write(f"/assets/charts/solproduktion-{c}.svg", V.sun_svg(L.NAMES[c], chart_data("sun", c)))
    _, nf = simple_page("/404.html", f"Siden findes ikke | {BRAND}", "Siden findes ikke.", "Siden findes ikke", '<p>Siden findes ikke (længere). Prøv en af disse:</p><div class="rgrid">' + rcard("sun", "Solceller", f"Regler og tilbud i {n_byer()}.", "/solceller/") + rcard("pump", "Luft til vand-varmepumpe", f"Fjernvarmestatus og tilskud i {n_byer()}.", "/varmepumpe/") + rcard("pin", "Find din by", city_list() + ".", "/#byer") + '</div>', noindex=True)
    write("/404.html", nf)
    # v7: delebilleder (1200x630) for alle sider + firkantet logo
    for k, (t, sub, motif) in OG_USED.items():
        V.og_image(os.path.join(OUT, "og", k + ".png"), t, sub, BRAND, SITE_URL.replace("https://", ""), motif)
    V.logo_png(os.path.join(OUT, "og", "logo.png"))
    idx = [p for p, _ in pages if p not in ("/tak/",)]
    lm = {p: (re.search(r'"dateModified": "(\d{4}-\d\d-\d\d)"', b) or [None, LAST_UPDATED_ISO])[1] for p, b in pages}
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f"  <url><loc>{url(p)}</loc><lastmod>{lm[p]}</lastmod></url>\n" for p in idx) + "</urlset>\n"
    write("/sitemap.xml", sm)
    # Google Search Console-verifikation: skal ligge permanent i roden, ikke i sitemap
    write("/googleef0dc5cbecefbd94.html", "google-site-verification: googleef0dc5cbecefbd94.html")
    write("/robots.txt", f"User-agent: *\nAllow: /\nDisallow: /tak/\n\nSitemap: {SITE_URL}/sitemap.xml\n")
    vj = {"trailingSlash": True, "redirects": [{"source": "/(.*)", "has": [{"type": "host", "value": h}], "destination": "https://energitjekket.dk/$1", "permanent": True} for h in ("energitjekket-preview.vercel.app", "energitjekket-preview-chucksdks-projects.vercel.app")] + [{"source": src_, "destination": p_fv(c), "permanent": False} for c in CITIES if not has_vp(c) for src_ in (f"/varmepumpe/{c}", f"/varmepumpe/{c}/")], "headers": [{"source": "/assets/(.*)", "headers": [{"key": "Cache-Control", "value": "public, max-age=604800"}]}, {"source": "/og/(.*)", "headers": [{"key": "Cache-Control", "value": "public, max-age=604800"}]}]}
    write("/vercel.json", json.dumps(vj, indent=2))
    # Git-deploy (GitHub ChucksDK/energitjekket -> Vercel): repo-roden får samme config + outputDirectory "site".
    # site/vercel.json bruges stadig ved fil-deploys (MCP), hvor site/ er roden.
    with open(os.path.join(OUT, "..", "vercel.json"), "w", encoding="utf-8") as f:
        f.write(json.dumps({"framework": None, "buildCommand": "", "installCommand": "", "outputDirectory": "site", **vj}, indent=2) + "\n")
    print(f"Byggede {len(pages)} sider til {os.path.abspath(OUT)}")

if __name__ == "__main__": main()
