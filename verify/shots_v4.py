from playwright.sync_api import sync_playwright
B='http://localhost:8765'; OUT='/workspace/leadsites/energi-landingssider/screenshots/v4/'
import os; os.makedirs(OUT,exist_ok=True)
DESK=dict(viewport={'width':1366,'height':860}); MOB=dict(viewport={'width':390,'height':844},device_scale_factor=2,is_mobile=True,has_touch=True)
errs=[]
with sync_playwright() as p:
    br=p.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--no-sandbox'])
    def page(ca,path):
        ctx=br.new_context(**ca); pg=ctx.new_page()
        pg.on('console',lambda m: m.type=='error' and errs.append((path,m.text))); pg.on('pageerror',lambda e: errs.append((path,str(e))))
        pg.goto(B+path,wait_until='networkidle'); return ctx,pg
    for path,name in (('/solceller/kolding/','solceller-kolding'),('/varmepumpe/odense/','varmepumpe-odense')):
        for ca,suf in ((DESK,'desktop'),(MOB,'mobil')):
            ctx,pg=page(ca,path)
            pg.screenshot(path=OUT+f'{name}-{suf}-fold.png')
            pg.screenshot(path=OUT+f'{name}-{suf}.png',full_page=True)
            first={'solceller-kolding':'#produktion','varmepumpe-odense':'#opvarmning'}[name]
            pg.locator(first).screenshot(path=OUT+f'{name}-{suf}-ny-sektion.png'); ctx.close()
    for path in ('/solceller/kolding/','/varmepumpe/odense/','/varmepumpe/aalborg/fjernvarme-eller-varmepumpe/','/solceller/esbjerg/','/varmepumpe/horsens/'):
        ctx,pg=page(MOB,path); print('scrollWidth',path,pg.evaluate('document.documentElement.scrollWidth')); ctx.close()
    br.close()
print('console errors:',errs)
