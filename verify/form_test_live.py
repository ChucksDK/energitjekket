from playwright.sync_api import sync_playwright
import sys
B='https://energitjekket.dk'
with sync_playwright() as p:
    br=p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
    pg=br.new_page(viewport={'width':1366,'height':900})
    reqs=[]; pg.on('response',lambda r: 'supabase.co' in r.url and reqs.append((r.request.method,r.status,r.url.split('?')[0])))
    errs=[]; pg.on('pageerror',lambda e: errs.append(str(e)))
    pg.goto(B+'/solceller/kolding/?utm_source=grokbot-live-test',wait_until='networkidle')
    f=pg.locator('#lead-form')
    for step in range(3):
        s=f.locator(f'.step[data-step="{step+1}"]')
        names=set()
        for r in s.locator('input[type=radio]').all():
            n=r.get_attribute('name')
            if n not in names: names.add(n); r.check(force=True)
        for sel in s.locator('select').all():
            try: sel.select_option(index=1)
            except: pass
        vals={'postnummer':'6000','telefon':'12 34 56 78','navn':'TEST Casper','email':'casper@casperlarsen.dk','areal':'140'}
        for inp in s.locator('input[type=text],input[type=tel],input[type=email],input[type=number]').all():
            n=inp.get_attribute('name')
            if n in vals: inp.fill(vals[n])
        if step<2: f.locator('[data-next]').click(); pg.wait_for_timeout(300)
    f.locator('input[name=samtykke]').check()
    f.locator('[data-submit]').click()
    pg.wait_for_url('**/tak/',timeout=15000)
    print('URL after submit:',pg.url); print('supabase calls:',reqs); print('errors:',errs)
    br.close()
