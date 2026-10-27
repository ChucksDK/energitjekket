from playwright.sync_api import sync_playwright
B='http://localhost:8765'; OUT='/workspace/leadsites/energi-landingssider/screenshots/'
with sync_playwright() as p:
    br=p.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--no-sandbox'])
    errs=[]
    def shot(path,name,mobile=False):
        ctx=br.new_context(viewport={'width':390,'height':844},device_scale_factor=2,has_touch=True,user_agent='Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1') if mobile else br.new_context(viewport={'width':1366,'height':900})
        pg=ctx.new_page(); pg.on('console',lambda m: m.type=='error' and errs.append((path,m.text))); pg.on('pageerror',lambda e: errs.append((path,str(e))))
        pg.goto(B+path,wait_until='networkidle'); pg.screenshot(path=OUT+name,full_page=True); ctx.close()
    shot('/solceller/kolding/','solceller-kolding-desktop.png')
    shot('/solceller/kolding/','solceller-kolding-mobil.png',mobile=True)
    shot('/varmepumpe/odense/','varmepumpe-odense-desktop.png')
    shot('/solceller/','solceller-hub-desktop.png')
    shot('/varmepumpe/aalborg/fjernvarme-eller-varmepumpe/','underside-fjernvarme-aalborg-desktop.png')
    shot('/varmepumpe/aalborg/fjernvarme-eller-varmepumpe/','underside-fjernvarme-aalborg-mobil.png',mobile=True)
    shot('/solceller/esbjerg/regler-og-byggetilladelse/','underside-regler-esbjerg-desktop.png')
    shot('/varmepumpe/tilskud/','guide-varmepumpepuljen-desktop.png')
    shot('/','forside-desktop.png')
    # formular-test
    ctx=br.new_context(viewport={'width':390,'height':844},is_mobile=True); pg=ctx.new_page()
    pg.goto(B+'/varmepumpe/esbjerg/')
    pg.click('[data-next]'); r1=pg.inner_text('.form-msg')
    pg.check('input[name=varmekilde][value=oliefyr]'); pg.click('[data-next]'); pg.click('[data-next]')
    pg.fill('[name=postnummer]','6700'); pg.fill('[name=navn]','Test'); pg.fill('[name=telefon]','12345678'); pg.fill('[name=email]','t@example.com')
    pg.click('[data-submit]'); r2=pg.inner_text('.form-msg')
    pg.check('[name=samtykke]'); pg.click('[data-submit]'); r3=pg.inner_text('.form-msg')
    pg.locator('#lead-form').screenshot(path=OUT+'formular-trin3-placeholder-mobil.png')
    print('Uden valg:',r1); print('Uden samtykke:',r2); print('Med samtykke:',r3)
    print('Konsolfejl:',errs or 'ingen')
    br.close()
