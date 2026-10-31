import os, re, json, urllib.request, html
from html.parser import HTMLParser
ROOT=os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','site'))  # 31/10 2026: relativ, så en worktree tjekker sin egen site/
BASE=os.environ.get('CHECK_BASE','http://localhost:8765')
class P(HTMLParser):
    def __init__(s): super().__init__(); s.links=[]; s.ld=[]; s._ld=False; s.h1=0; s.title=''; s._t=False; s.meta={}; s.canon=None; s.ids=set()
    def handle_starttag(s,t,a):
        a=dict(a)
        if 'id' in a: s.ids.add(a['id'])
        if t=='a' and 'href' in a: s.links.append(a['href'])
        if t in('link','script') and a.get('href') and t=='link' and a.get('rel')=='stylesheet': s.links.append(a['href'])
        if t=='script' and a.get('src') and not a['src'].startswith('/_vercel/'): s.links.append(a['src'])  # /_vercel/* findes kun på Vercel
        if t=='script' and a.get('type')=='application/ld+json': s._ld=True; s.ld.append('')
        if t=='h1': s.h1+=1
        if t=='title': s._t=True
        if t=='meta' and a.get('name'): s.meta[a['name']]=a.get('content','')
        if t=='link' and a.get('rel')=='canonical': s.canon=a['href']
    def handle_endtag(s,t):
        if t=='script': s._ld=False
        if t=='title': s._t=False
    def handle_data(s,d):
        if s._ld: s.ld[-1]+=d
        if s._t: s.title+=d
pages={}
for dp,_,fs in os.walk(ROOT):
    for f in fs:
        if re.fullmatch(r'google[0-9a-f]+\.html',f): continue  # Search Console-verifikationsfil, ikke en side (tjekkes separat nedenfor)
        if f.endswith('.html'):
            rel='/'+os.path.relpath(os.path.join(dp,f),ROOT).replace('index.html','')
            p=P(); p.feed(open(os.path.join(dp,f),encoding='utf-8').read()); pages[rel]=p
checked={}; broken=[]; nlinks=0; ext=set()
# 31/10 2026: uden lokal server (fx python3 -m http.server 8765 i site/) bliver ALLE interne links 'brudte' (Connection refused). Stop tidligt med en klar besked i stedet.
try: urllib.request.urlopen(BASE+'/',timeout=5)
except Exception as e:
    if not getattr(e,'code',None): import sys as _x; print(f'FEJL: ingen server på {BASE} ({e}). Start: cd site && python3 -m http.server 8765, eller sæt CHECK_BASE.'); print('GATE: FEJL ingen lokal server'); _x.exit(2)
for rel,p in pages.items():
    for h in p.links:
        if h.startswith('http'): ext.add(h); continue
        if h.startswith('mailto:') or h.startswith('tel:'): continue
        if h.startswith('#'):
            if h[1:] and h[1:] not in p.ids: broken.append((rel,h,'missing anchor'))
            continue
        nlinks+=1
        path=h.split('#')[0]
        if path not in checked:
            try: checked[path]=urllib.request.urlopen(BASE+path).status
            except Exception as e: checked[path]=getattr(e,'code',str(e))
        if checked[path]!=200: broken.append((rel,h,checked[path]))
ld_ok=0; ld_err=[]; types={}
for rel,p in pages.items():
    for blk in p.ld:
        try:
            d=json.loads(blk); ld_ok+=1
            for g in d.get('@graph',[]): types[g['@type']]=types.get(g['@type'],0)+1
        except Exception as e: ld_err.append((rel,str(e)))
print(f'Sider: {len(pages)} | interne links tjekket: {nlinks} ({len(checked)} unikke URL) | brudte: {len(broken)}')
for b in broken: print('  BRUDT',b)
print(f'JSON-LD blokke OK: {ld_ok} | fejl: {len(ld_err)} {ld_err}')
print('Schema-typer:',types)
print('Eksterne kildelinks (unikke):',len(ext))
issues=[]
for rel,p in sorted(pages.items()):
    t=html.unescape(p.title); d=p.meta.get('description','')
    if p.h1!=1: issues.append((rel,'h1=%d'%p.h1))
    if len(t)>68: issues.append((rel,'title %d tegn'%len(t)))
    if not (50<=len(d)<=165): issues.append((rel,'description %d tegn'%len(d)))
    if rel not in ('/404.html',) and (not p.canon or not p.canon.endswith(rel)): issues.append((rel,'canonical '+str(p.canon)))
print('On-page issues:',issues or 'ingen')
# interlink-krav
import sys as _s, os as _o; _s.path.insert(0, _o.path.join(_o.path.dirname(_o.path.abspath(__file__)), '..', 'src'))
from data import CITIES as _C
from data_topics import NAV as _NAV
cities=list(_C)  # v7: læses fra src/data.py, så nye byer fra den daglige rutine kommer med automatisk
SUB={'solceller':'regler-og-byggetilladelse','varmepumpe':'fjernvarme-eller-varmepumpe'}
# 26/10 2026: byer med vp_page False (>90 % fjernvarme, fx Aarhus) har ingen /varmepumpe/<by>/; bysiden ER fjernvarme-undersiden
def hasp(svc,c): return svc=='solceller' or _C[c].get('vp_page',True)
def pc(svc,c): return f'/{svc}/{c}/' if hasp(svc,c) else f'/{svc}/{c}/{SUB[svc]}/'
_LATEST=max(_C[c].get('updated',('',''))[1] for c in cities)  # nyeste by-batch (daglig rutine)
NEW=[c for c in cities if _C[c].get('updated',('',''))[1]==_LATEST]
NAT={'solceller':['/solceller/pris/','/solceller/med-batteri/'],'varmepumpe':['/varmepumpe/pris/','/varmepumpe/tilskud/']}
NAT_ALL={s:NAT[s]+[u for u,_,_,_ in _NAV[s]] for s in NAT}
miss=[]
for svc,o in (('solceller','varmepumpe'),('varmepumpe','solceller')):
    for c in cities:
        city=pc(svc,c); sub=f'/{svc}/{c}/{SUB[svc]}/'
        if f'/{svc}/{c}/' in pages and not hasp(svc,c): miss.append((f'/{svc}/{c}/','findes, men vp_page er False'))
        if hasp(svc,c):
            L=set(pages[city].links)
            need={pc(o,c),f'/{svc}/',f'/{o}/',sub,f'/{o}/{c}/{SUB[o]}/'}|{pc(svc,x) for x in cities if x!=c}|set(NAT[svc])
            if need-L: miss.append((city,need-L))
        L=set(pages[sub].links)
        need={city,f'/{svc}/',pc(o,c),f'/{o}/{c}/{SUB[o]}/'}|{f'/{svc}/{x}/{SUB[svc]}/' for x in cities if x!=c}|set(NAT[svc])
        need.discard(sub)
        if need-L: miss.append((sub,need-L))
    for n in NAT[svc]:
        L=set(pages[n].links); need={f'/{svc}/'}|{pc(svc,x) for x in cities}|{f'/{svc}/{x}/{SUB[svc]}/' for x in cities}
        if need-L: miss.append((n,need-L))
    for n in NAT_ALL[svc][2:]:
        L=set(pages[n].links); need={f'/{svc}/'}|{pc(svc,x) for x in cities}
        if need-L: miss.append((n,need-L))
    L=set(pages[f'/{svc}/'].links); need={f'/{svc}/{x}/{SUB[svc]}/' for x in cities}|set(NAT_ALL[svc])|{'/beregner/#'+svc}
    if need-L: miss.append((f'/{svc}/',need-L))
# indgående links pr. side
inbound={r:0 for r in pages}
for rel,p in pages.items():
    for h in set(p.links):
        h=h.split('#')[0]
        if h in inbound and h!=rel: inbound[h]+=1
orph=[r for r,v in inbound.items() if v==0 and r not in ('/404.html','/tak/','/')]
print(f'Interlink-krav opfyldt ({sum(hasp(s,c) for s in SUB for c in cities)} bysider, {2*len(cities)} lokale undersider, {sum(map(len,NAT_ALL.values()))} guides, 2 hubs)' if not miss else miss)
# v7: delebilleder, diagrammer og synlig opdateret-dato
ogm=[]
for rel in pages:
    h=open(ROOT+(rel if rel.endswith('.html') else rel+'index.html'),encoding='utf-8').read()
    im=re.search(r'<meta property="og:image" content="https://[^/]+(/og/[^"]+)"',h)
    if not im or not os.path.exists(ROOT+im.group(1)) or 'twitter:card' not in h: ogm.append(rel)
    if rel not in ('/404.html','/tak/') and ('dateModified' not in h or ('<time datetime=' not in h)): ogm.append(rel+' (dato)')
from PIL import Image as _I
sizes={_I.open(ROOT+'/og/'+f).size for f in os.listdir(ROOT+'/og') if f!='logo.png'}
ch=[c for c in cities if not (os.path.exists(ROOT+f'/assets/charts/opvarmning-{c}.svg') and os.path.exists(ROOT+f'/assets/charts/solproduktion-{c}.svg'))]
print('og:image+twitter+dato på alle sider:', 'ja' if not ogm else ogm, '| billedstørrelser:', sizes, '| byer uden diagrammer:', ch or 'ingen')
print('Sider uden indgående links:',orph or 'ingen', '| min. indgående for undersider:', min(v for r,v in inbound.items() if r.count('/')==4))
sm=open(ROOT+'/sitemap.xml').read(); locs=set(re.findall(r'<loc>https://[^/]+(/[^<]*)</loc>',sm))
idx=[r for r in pages if r not in ('/404.html','/tak/')]
print('Sitemap:',len(locs),'URL | mangler:',sorted(set(idx)-locs) or 'ingen')
import difflib, sys
MODE = 'begge'
def main_txt_old(rel):
    """Gammel metode (v2/v3): fjerner kun script/style/form/footer/header og section.links."""
    h=open(ROOT+rel+'index.html',encoding='utf-8').read()
    h=re.sub(r'<(script|style|form|footer|header)[\s\S]*?</\1>','',h)
    h=re.sub(r'<section class="links"[\s\S]*?</section>','',h)
    return re.sub(r'\s+',' ',re.sub(r'<[^>]+>',' ',h)).split()
FURNITURE = [
    r'<nav[\s\S]*?</nav>',                              # brødkrumme + indholdsfortegnelse (TOC)
    r'<aside[\s\S]*?</aside>',                          # sidekolonne: TOC + side-CTA
    r'<form[\s\S]*?</form>',                            # tilbudsformular
    r'<p class="disclose">[\s\S]*?</p>',                # trust-linje (ANGU ApS · CVR · faktatjekket)
    r'<p class="eyebrow">[\s\S]*?</p>',                 # lille overrubrik i hero
    r'<ul class="usp">[\s\S]*?</ul>',                   # USP-punkter i hero
    r'<div class="hero-actions">[\s\S]*?</div>',        # hero-knapper
    r'<section class="links"[\s\S]*?</section>',        # relaterede sider + byvælger
    r'<section id="saadan-virker-det"[\s\S]*?</section>',  # fælles CTA-boks "Sådan får du tilbud"
]
def main_txt_new(rel):
    """Ny metode (v4): kun <main>, og fælles sideinventar fjernes, så målingen dækker indholdet."""
    h=open(ROOT+rel+'index.html',encoding='utf-8').read()
    m=re.search(r'<main[^>]*>([\s\S]*?)</main>',h); h=m.group(1) if m else h
    h=re.sub(r'<(script|style)[\s\S]*?</\1>','',h)
    for pat in FURNITURE: h=re.sub(pat,'',h)
    return re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>',' ',h))).split()
_cache={}
SIMS=[]
def txt(rel,fn):
    k=(rel,fn.__name__)
    if k not in _cache: _cache[k]=fn(rel)
    return _cache[k]
def sim(label, rels, fn):
    rs=[]
    for i,a in enumerate(rels):
        for b in rels[i+1:]:
            rs.append(difflib.SequenceMatcher(None,txt(a,fn),txt(b,fn),autojunk=False).ratio())
    w=[len(txt(r,fn)) for r in rels]
    print(f'  {label}: lighed gns {sum(rs)/len(rs):.0%}, maks {max(rs):.0%} | ord {min(w)}-{max(w)}')
    if fn.__name__=='main_txt_new': SIMS.append((label,sum(rs)/len(rs),max(rs)))
    return sum(rs)/len(rs), max(rs)
for name,fn in (('GAMMEL metode (hele siden minus header/footer/form/links)',main_txt_old),('NY metode (kun hovedindhold; uden nav, TOC, side-CTA, trust-linje, hero-knapper, formular, linkblok, CTA-boks, footer)',main_txt_new)):
    print('Lighed,',name)
    for svc in ('solceller','varmepumpe'):
        sim(f'Bysider {svc}', [f'/{svc}/{c}/' for c in cities if hasp(svc,c)], fn)
        sim(f'Undersider {SUB[svc]}', [f'/{svc}/{c}/{SUB[svc]}/' for c in cities], fn)
    sim('Guides (4 nationale)', NAT['solceller']+NAT['varmepumpe'], fn)
    sim(f'Alle guides og tilbudssider ({sum(map(len,NAT_ALL.values()))})', NAT_ALL['solceller']+NAT_ALL['varmepumpe'], fn)
    rs=[difflib.SequenceMatcher(None,txt(f'/{s}/{c}/',fn),txt(f'/{s}/{c}/{SUB[s]}/',fn),autojunk=False).ratio() for s in SUB for c in cities if hasp(s,c)]
    print(f'  Byside vs egen underside: gns {sum(rs)/len(rs):.0%}, maks {max(rs):.0%}')
    if NEW:
        print(f'  Nye sider ({", ".join(NEW)}) mod de eksisterende sider af samme type:')
        old=[c for c in cities if c not in NEW]
        for s_ in SUB:
            for kind,mk in (('byside',lambda s_,c: f'/{s_}/{c}/'),('underside',lambda s_,c: f'/{s_}/{c}/{SUB[s_]}/')):
                for c in NEW:
                    if kind=='byside' and not hasp(s_,c): continue
                    a=mk(s_,c); others=[mk(s_,x) for x in cities if x!=c and (kind!='byside' or hasp(s_,x))]
                    rs=[difflib.SequenceMatcher(None,txt(a,fn),txt(b,fn),autojunk=False).ratio() for b in others]
                    print(f'    {a}: gns {sum(rs)/len(rs):.0%}, maks {max(rs):.0%} ({others[rs.index(max(rs))]}) | {len(txt(a,fn))} ord')

# ---- elpris (26/10 2026) ----
elm=[]
if '/elpris/' not in pages: elm.append('/elpris/ mangler')
else:
    h=open(ROOT+'/elpris/index.html',encoding='utf-8').read(); L_=set(pages['/elpris/'].links)
    for need in ('/solceller/tilbud/','/varmepumpe/tilbud/','/beregner/#varmepumpe'):
        if need not in L_: elm.append('/elpris/ mangler link '+need)
    if '"Dataset"' not in h: elm.append('/elpris/ mangler Dataset')
    if 'class="elsvg"' not in h or 'id="elpris-data"' not in h: elm.append('/elpris/ mangler graf/data')
    if not os.path.exists(ROOT+'/assets/elpris.js'): elm.append('elpris.js mangler')
for c in cities:
    for rel in ([pc('solceller',c),pc('varmepumpe',c)]):
        h=open(ROOT+rel+'index.html',encoding='utf-8').read()
        if 'class="elbox"' not in h or '/elpris/#dk' not in h: elm.append(rel+' mangler elpris-boks')
print('Elpris: side, links og bokse på alle bysider:', 'ok' if not elm else elm)
# ---- samlet gate (bruges af src/refresh_elpris.py) ----
gate=[]
if broken: gate.append(f'{len(broken)} brudte links')
if ld_err: gate.append('JSON-LD-fejl')
if miss: gate.append('interlink-krav')
if ogm: gate.append('og/dato')
if sorted(set(idx)-locs): gate.append('sitemap')
if orph: gate.append('sider uden indgående links')
if ch: gate.append('diagrammer')
if elm: gate.append('elpris')
if [i for i in issues if i[0] not in ('/404.html','/tak/')]: gate.append('on-page')
_gv=os.path.join(ROOT,'googleef0dc5cbecefbd94.html')
if not os.path.exists(_gv) or open(_gv,encoding='utf-8').read()!='google-site-verification: googleef0dc5cbecefbd94.html' or 'googleef0dc5cbecefbd94' in sm: gate.append('google-verifikation')
print('Google-verifikationsfil:', 'OK' if 'google-verifikation' not in gate else 'FEJL')
LIM={'Bysider':(0.35,0.50),'Undersider':(0.40,0.50),'Guides':(0.30,0.50),'Alle guides':(0.30,0.50)}
for label,avg,mx in SIMS:
    for k,(la,lm) in LIM.items():
        if label.startswith(k) and (avg>la or mx>lm): gate.append(f'lighed {label} gns {avg:.0%} maks {mx:.0%}')
print('GATE:', 'OK' if not gate else 'FEJL '+'; '.join(gate))
sys.exit(0 if not gate else 1)
