from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox','--disable-blink-features=AutomationControlled'])
    pg=b.new_page(user_agent='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36'); reqs=[]; errs=[]
    pg.on('response',lambda r: reqs.append((r.request.method,r.status,r.url)) if '/_vercel/' in r.url else None)
    pg.on('console',lambda m: errs.append(m.text) if m.type=='error' else None)
    for path in ['/','/solceller/kolding/']:
        pg.goto('https://energitjekket.dk'+path,wait_until='networkidle'); pg.wait_for_timeout(2500)
    pg.goto('https://energitjekket.dk/om-os/',wait_until='networkidle'); pg.wait_for_timeout(2000)
    for r in reqs: print(*r)
    print('console errors:',errs); b.close()
