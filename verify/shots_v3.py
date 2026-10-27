from playwright.sync_api import sync_playwright
B='http://localhost:8765'; OUT='/workspace/leadsites/energi-landingssider/screenshots/v3/'
MOB=dict(viewport={'width':390,'height':844},device_scale_factor=2,is_mobile=True,has_touch=True,user_agent='Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1')
DESK=dict(viewport={'width':1440,'height':900})
with sync_playwright() as p:
    br=p.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--no-sandbox'])
    errs=[]
    def page(ctxargs,path):
        ctx=br.new_context(**ctxargs); pg=ctx.new_page()
        pg.on('console',lambda m: m.type=='error' and errs.append((path,m.text))); pg.on('pageerror',lambda e: errs.append((path,str(e))))
        pg.goto(B+path,wait_until='networkidle'); return ctx,pg
    for path,name in (('/','forside'),('/solceller/kolding/','solceller-kolding'),('/varmepumpe/odense/','varmepumpe-odense')):
        for ca,suf in ((DESK,'desktop'),(MOB,'mobil')):
            ctx,pg=page(ca,path)
            pg.screenshot(path=OUT+f'{name}-{suf}-fold.png')
            pg.screenshot(path=OUT+f'{name}-{suf}.png',full_page=True); ctx.close()
    # åben mobilmenu (+ udfoldet Solceller)
    ctx,pg=page(MOB,'/solceller/kolding/')
    pg.click('.menu-btn'); pg.wait_for_timeout(200); pg.screenshot(path=OUT+'mobilmenu-aaben.png')
    pg.click('.dd:nth-child(1) .dd-t'); pg.wait_for_timeout(200); pg.screenshot(path=OUT+'mobilmenu-solceller-udfoldet.png'); ctx.close()
    # desktop dropdown
    ctx,pg=page(DESK,'/varmepumpe/odense/')
    pg.hover('.dd:nth-child(3) .top'); pg.wait_for_timeout(200); pg.screenshot(path=OUT+'desktop-menu-byer.png')
    pg.hover('.dd:nth-child(1) .top'); pg.wait_for_timeout(200); pg.screenshot(path=OUT+'desktop-menu-solceller.png'); ctx.close()
    # sticky CTA midt på siden (mobil)
    ctx,pg=page(MOB,'/varmepumpe/odense/')
    pg.evaluate('window.scrollTo(0, document.body.scrollHeight*0.45)'); pg.wait_for_timeout(400); pg.screenshot(path=OUT+'mobil-sticky-cta-og-header.png')
    vis=pg.evaluate("!document.getElementById('mcta').classList.contains('hide')")
    pg.evaluate("document.getElementById('lead-form').scrollIntoView()"); pg.wait_for_timeout(400)
    hid=pg.evaluate("document.getElementById('mcta').classList.contains('hide')")
    print('Sticky CTA synlig midt på siden:',vis,'| skjult ved formularen:',hid); ctx.close()
    # formular-test (mobil)
    ctx,pg=page(MOB,'/varmepumpe/esbjerg/')
    pg.click('[data-next]'); r1=pg.inner_text('.form-msg')
    pg.click('label.opt:has(input[value=oliefyr])'); pg.click('[data-next]'); s2=pg.inner_text('.step-count')
    pg.locator('#lead-form').screenshot(path=OUT+'formular-trin2-mobil.png')
    pg.click('[data-next]')
    pg.fill('[name=postnummer]','6700'); pg.fill('[name=navn]','Test Testesen'); pg.fill('[name=telefon]','12345678'); pg.fill('[name=email]','t@example.com')
    pg.click('[data-submit]'); r2=pg.inner_text('.form-msg')
    pg.check('[name=samtykke]'); pg.click('[data-submit]'); r3=pg.inner_text('.form-msg')
    pg.locator('#lead-form').screenshot(path=OUT+'formular-trin3-placeholder-mobil.png')
    print('Uden valg:',r1); print('Trin-tæller på trin 2:',s2); print('Uden samtykke:',r2); print('Med samtykke:',r3); ctx.close()
    # vandret overflow-tjek på mobil
    for path in ('/','/solceller/kolding/','/varmepumpe/odense/','/varmepumpe/aalborg/fjernvarme-eller-varmepumpe/','/solceller/pris/','/solceller/','/om-os/'):
        ctx,pg=page(MOB,path); w=pg.evaluate('document.documentElement.scrollWidth'); print('scrollWidth',path,w); ctx.close()
    print('Konsolfejl:',errs or 'ingen')
    br.close()
