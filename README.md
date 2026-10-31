# Energi-landingssider (kladde – IKKE publiceret)

- `site/` – færdig statisk side (39 HTML-sider + 404: forside, 2 hubs, 14 bysider, 14 lokale undersider, 4 guides, 4 faste sider). Klar til Vercel (root = site/), men må først deployes efter godkendelse.
- `src/config.py` – brand, domæne og firmaoplysninger ét sted. ANGU ApS-oplysninger er udfyldt fra CVR. Resterende [PLADSHOLDERE]: [EMAIL], [ANTAL], [FORRETNINGSMODEL], partnerliste, [OM-AFSENDER], [DATABEHANDLERE] og [OPBEVARINGSPERIODE].
- `src/data.py` – byer, lokale fakta, FAQ, priser og kilder.
- `src/data_sub.py` – undersider (regler for solceller og fjernvarme eller varmepumpe pr. by) og de 4 nationale guides, inkl. søgeord og evidens pr. side.
- `src/build.py` – genbyg: `cd src && python3 build.py` (skriver til ../site/).
- `verify/check.py` – tjek links/JSON-LD/meta; `verify/shots.py` – screenshots + formulartest; `verify/lh-*.json` – Lighthouse.
- `research.md` – research, kilder og sidestruktur.
- Formularen sender intet: submit er en pladsholder i `site/assets/form.js` (skal kobles på backend, fx Supabase).

## v3 – redesign (24. oktober 2026)
- `research-x-design.md` – research fra X (+ NN/g og Baymard) om lead-gen-sider for solceller/varmepumper/håndværk, med links til opslagene og hvad vi gjorde med hver lektion.
- Nyt design i `src/build.py` (indhold, kilder, JSON-LD og pladsholdere er uændrede): sticky header med menu Solceller / Varmepumpe / Byer / Guides (dropdowns + mobilmenu), brødkrummer, "På denne side"-navigation, byvælger, kort med relaterede sider, fuldt sitemap i footeren, sticky mobil-CTA, inline-SVG-ikoner og en tydeligere 3-trins formular (sender stadig intet).
- Verifikation: `verify/check-output-v3.txt`, `verify/shots-v3-output.txt`, `verify/lh-v3-*.json` + `verify/lh-v3-summary.txt`, screenshots i `screenshots/v3/` (gamle screenshots ligger stadig i `screenshots/`, og `screenshots/v3/foer-efter-*.png` viser før/efter).
- Kør screenshots: `/workspace/.venv-pw/bin/python verify/shots_v3.py` (kræver `python3 -m http.server 8765` i site/).
- `_v2-backup/` – kopi af src/ og site/ fra før redesignet.

## v4 – unikt lokalt indhold (24. oktober 2026)
- `src/data_local.py` – nyt, håndskrevet lokalindhold pr. by (tekster, FAQ, sektionsrækkefølge, kilder). Tal kommer fra `src/data_local_gen.py`, som genereres af `research/v4/make_local.py` ud fra rå API-data i `research/v4/*.json`:
  - PVGIS 5.3 (EU JRC, SARAH3): kWh pr. kWp for syd/øst/vest og pr. måned for hver by.
  - Danmarks Statistik: BOL102 (opvarmning), BOL101 (opførelsesår, ejerforhold), BYGB50 (tagmateriale), BY3 (folketal pr. by 1/1 2026).
  - Lokale varmeværker og kommunale tilbud (TREFOR/EWII, TVIS, Fjernvarme Fyn, Verdo, Fjernvarme Horsens, Vejle, Randers, SparEnergi), alle med link.
- Bysider: nye sektioner (produktion, tage, boliger og byer for solceller; opvarmning og by for by for varmepumpe) og forskellig sektionsrækkefølge og FAQ pr. by. Fjernvarme-undersider: hvor varmen kommer fra, andel med fjernvarme og egen udregning af forskellen til en varmepumpe pr. værk. Regel-undersider: én bystatistik pr. by.
- `verify/check.py` måler nu lighed med to metoder: den gamle og en ny, der kun ser på hovedindholdet (uden nav, TOC, CTA, formular, linkblok osv.). Output: `verify/check-output-v4.txt`. Lighthouse: `verify/lh-v4-*.json` og `verify/lh-v4-summary.txt`. Screenshots: `verify/shots_v4.py` → `screenshots/v4/`.
- `_v3-backup-src/` – kopi af src/ og check.py fra før v4.

## v5 – formular på Supabase, partnerside fjernet (25. oktober 2026)
- Formularen sender nu til Supabase-projektet "energitjekket" (ref ckdrjxjdxprezsvfdpet, eu-west-1), tabel `public.leads`. RLS: anon må kun INSERT (ingen SELECT/UPDATE/DELETE). Check constraints på alle felter. Honeypot-felt `website` håndteres i JS. Daglig pg_cron-job sletter leads ældre end 12 måneder. Kun den offentlige publishable key ligger i `src/config.py`.
- `/partnere/` er fjernet. Ny samtykketekst (version i `CONSENT_VERSION`), ny om-os-, privatlivs- og tak-tekst, ingen pladsholdere tilbage.
- Test: `verify/form_test_v5.py` (indsender én testlead – slet den bagefter). Lighthouse: `verify/lh-v5-*.json`. Check: `verify/check-output-v5.txt`. Screenshots: `screenshots/v5-*.png`.

## v6 – ét firma pr. lead + besked til kunden (25. okt. 2026)

**Flow:** Kunden udfylder formularen (samtykke v`2026-10-25-v2`) → rækken lander i `public.leads` → Casper får en e-mail om nyt lead → Casper kontakter selv ét firma og udfylder firmaets navn + CVR på leadet → kunden får automatisk en e-mail fra kontakt@energitjekket.dk med firmaets navn, CVR og hvordan samtykket trækkes tilbage.

### Sådan tildeler du et lead
**Table Editor:** Supabase → projekt *energitjekket* → Table Editor → `leads` → find rækken → udfyld `assigned_company_name` og `assigned_company_cvr` (8 cifre) → Save. `assigned_at` sættes automatisk.

**SQL (SQL Editor):**
```sql
update public.leads
set assigned_company_name = 'Firmanavn ApS',
    assigned_company_cvr  = '12345678'
where id = '<lead-id fra e-mailen>';
```
Udfyld først firmaet, når du faktisk har sendt oplysningerne – kunden får besked med det samme. Kunden får kun én e-mail pr. lead (`customer_notified_at`). Status/fejl står i `notify_error`.

### Database (migration `leads_assignment_and_notify`, fil: `supabase/migrations/20261025_leads_assignment_and_notify.sql`)
- Nye kolonner: `assigned_company_name`, `assigned_company_cvr` (^[0-9]{8}$), `assigned_at`, `customer_notified_at`, `owner_notified_at`, `notify_error`.
- `anon` har kun kolonne-INSERT på formularfelterne; kan ikke læse, opdatere eller sætte tildelings-/notifikationskolonner.
- Triggere (pg_net → edge function `notify-recipient`): AFTER INSERT → e-mail til Casper; AFTER UPDATE af firmafelterne (kun når de ændres og begge er udfyldt) → e-mail til kunden. Fejl i kaldet stopper aldrig selve indsendelsen.

### Edge function `notify-recipient` (`supabase/functions/notify-recipient/`)
- `index.ts` (logik) og `templates.ts` (e-mailskabeloner, dansk HTML + tekst).
- Slår leadet op med service role og handler kun ud fra databasens tilstand; idempotent.
- Uden `RESEND_API_KEY` (eller med secret `DRY_RUN=1`): sender intet, logger og skriver fx `[kunde] RESEND_API_KEY mangler – ingen e-mail sendt` i `notify_error`.
- Valgfri secret `OWNER_EMAIL` (standard casper@casperlarsen.dk).

### Aktivering af e-mails (når domænet er købt)
1. Køb energitjekket.dk.
2. Opret en konto på resend.com → Domains → Add domain `energitjekket.dk` (region EU, fx eu-west-1).
3. Læg de DNS-poster Resend viser (SPF/MX på `send`-subdomænet, DKIM `resend._domainkey`, evt. DMARC) ind hos din DNS-udbyder, og vent til Resend viser *Verified*.
4. Resend → API Keys → opret en nøgle med *Sending access* kun for energitjekket.dk.
5. Supabase → Edge Functions → Secrets → tilføj `RESEND_API_KEY` (eller `supabase secrets set RESEND_API_KEY=... --project-ref ckdrjxjdxprezsvfdpet`). Ingen redeploy nødvendig.
6. Sørg for at kontakt@energitjekket.dk kan modtage svar (mailboks/videresendelse), da kunderne skriver dertil for at trække samtykke tilbage.
7. Test: indsend et testlead med din egen e-mail, tildel et testfirma, tjek begge e-mails, slet testrækken.

## LIVE – 25. okt. 2026 (ca. 16:15 CET)

- **Live URL:** https://energitjekket.dk (kanonisk). `www.energitjekket.dk` → 308 til apex. `energitjekket-preview.vercel.app` → 308 til apex (via `redirects` i vercel.json).
- **Vercel-projekt:** energitjekket-preview (prj_ERx7JzVzUASXNpzMZTTk27Fj9Sha). Produktion: dpl_EXVvPAHWfcBzvhJUzER3a6bBe6D3.
- **DNS (Simply):** A `energitjekket.dk` → 76.76.21.21, CNAME `www` → cname.vercel-dns.com. Vercel: ikke fejlkonfigureret, SSL udstedt. (Vercel foreslår nu også nyere IP'er 216.198.79.1/64.29.17.1 – valgfrit.)
- **Beskyttelse:** Vercel Authentication = "all_except_custom_domains": egne domæner er offentlige; previews og *.vercel.app-deployment-URL'er kræver stadig login.
- **SEO:** X-Robots-Tag noindex fjernet; `SITE_URL` = https://energitjekket.dk (canonical, og:url, sitemap, robots). Kun /tak/ og 404-siden har bevidst `noindex,follow`.
- **Ny deploy:** `cd src && python3 build.py`, upload `site/` som produktion (vercel.json bygges af build.py).
- **Verifikation:** verify/live-check.txt (37/37 sider 200, 0 brudte links, 0 noindex), verify/lh-live-summary.txt (Lighthouse mobil 100/100/100/100), live-formular testet (Resend-id på ejer-mail), testrække slettet.

## Statistik (Vercel Web Analytics + Speed Insights) – 25. okt. 2026

- Web Analytics er slået til i Vercel-dashboardet (af Casper). Speed Insights kører også (gratis på alle planer).
- Snippets indsættes på alle sider af `src/build.py` (`ANALYTICS_HTML`) og styres af `WEB_ANALYTICS` / `SPEED_INSIGHTS` i `src/config.py`. Scripts: `/_vercel/insights/script.js` og `/_vercel/speed-insights/script.js` (statiske, ingen npm).
- Cookieless. Privatlivspolitikken (afsnit "Cookies og statistik") og footeren er opdateret.
- Custom event `lead_submitted` er ikke sat op, fordi custom events kræver Pro/Enterprise.
- Hobby-grænser: Web Analytics 50.000 events/md. for hele teamet (indsamlingen pauser ved loft; man kan ikke købe flere events på Hobby). Speed Insights 10.000 events pr. løbende 30 dage (pauser 14 dage ved loft).
- Dashboards: https://vercel.com/chucksdks-projects/energitjekket-preview/analytics og https://vercel.com/chucksdks-projects/energitjekket-preview/speed-insights
- Produktions-deploy: `dpl_A843MMnaAu6YDqbVsRH9w4W9KLzm`.
- Verificeret: scripts giver 200, `POST /_vercel/insights/view` giver 200, ingen konsolfejl (`verify/analytics_check.py`). Scriptet ignorerer selv headless/automatiserede browsere. Lighthouse mobil 100/100/100/100 på forside og /solceller/kolding/ (`verify/lh-analytics-summary.txt`). check.py: 39 sider, 0 brudte links.

## v7 – SEO-udvidelse (25. okt. 2026)

**Nye sider** (data i `src/data_topics.py`, samme blokformat som `NATIONAL` i `data_sub.py`; alle tal har kilde):
`/varmepumpe/jordvarme-pris/`, `/varmepumpe/luft-til-luft-pris/`, `/varmepumpe/skift-oliefyr/`, `/varmepumpe/skift-gasfyr/`,
`/solceller/kan-det-betale-sig/`, `/solceller/fladt-tag-og-carport/`, `/solceller/tilbud/`, `/varmepumpe/tilbud/` (begge med den eksisterende formular + tjekliste) og `/beregner/` (`calc_page()` i `build.py`, JS i `src/calc_js.py` → `/assets/calc.js`; ingen cookies, intet gemmes, ingen netværkskald).
Navigation: `NAT_LINKS` = `NAT_CORE` (de 4 gamle guides) + `data_topics.NAV`. Bysidernes guide-blok bruger kun `NAT_CORE` (holder ligheden lav); alle guides ligger i linkblokken, menuen, footeren, hubs og forsiden.

**Delebilleder:** `head()` sætter `og:image` (+ width/height/alt) og `twitter:card=summary_large_image` på alle sider. Billederne (1200×630 PNG, egen grafik, ingen fotos/personer) laves af `src/visuals.py` (Pillow, fonte i `src/fonts/`) til `/og/`: ét pr. by (`by-<slug>.png`, deles af by- og undersider), ét pr. guide, hubs, forside, beregner + `logo.png`.

**Diagrammer pr. by:** `/assets/charts/opvarmning-<slug>.svg` (DST BOL102: kommunen vs. hele landet) på varmepumpe-bysiden og `/assets/charts/solproduktion-<slug>.svg` (PVGIS, 6 kWp syd pr. måned) på solcelle-bysiden. Genereres i `main()` ud fra `L.HEAT[c]` og `L.PV[c]["months"]`.

**Tillid:** synlig "Opdateret <time>" i trust-linjen (alle sider) + `dateModified`, `author` og `publisher` = organisationen (ingen opfunden person). Sitemap `lastmod` tages fra sidens `dateModified`. Organisation: ANGU ApS, CVR 40086560, Prins Christians Vænge 16, 8660 Skanderborg, startdato 10.12.2018 – tjekket på datacvr.virk.dk 25/10 2026 (`CVR_URL` i `config.py`, kilde `cvr_virk` på om-os). Telefonnummeret står ikke på datacvr.virk.dk.

**Tilskudssiden:** status pr. 25/10 2026 (SparEnergi 23/10: åben; TEKNIQ 13/10 + Installatør 14/10: knap 44 mio. kr.) + tydelig note om lukning senest 30/11 2026. Opdatér `"updated"` og teksten, når der kommer nyt tal, og når puljen lukker.

### Den daglige by-rutine (2 nye byer pr. dag fra `city-queue.json`)
Når en ny by er lagt ind i datafilerne (samme felter som de eksisterende byer: `CITIES`/`CONTACTS` i `data.py`, `SOL_REG`/`FV_PAGE`/`FV_PRICES` i `data_sub.py` og de lokale data i `data_local.py` via `research/v4/make_local.py`: `PV`, `HEAT`, `ROOF`, `TOWNS`, `NAMES` osv.), sker resten automatisk ved `cd src && python3 build.py`:
- by- og undersider, menu, footer, linkblokke, sitemap
- de to SVG-diagrammer for byen og delebilledet `og/by-<slug>.png`
- `verify/check.py` læser bylisten fra `src/data.py` og tjekker nu også og:image/twitter, synlig dato og at diagrammerne findes.
Husk: sæt `CITIES[slug]["updated"] = ("26. oktober 2026", "2026-10-26")` (dagens dato) på nye byer, så "Opdateret" og `dateModified` passer. Uden feltet bruges `LAST_UPDATED` fra `config.py`. Antal byer og bylister i hub-titler/beskrivelser, forside og 404 beregnes nu i `build.py` (`n_byer()`, `city_list()`, `fit_desc()`); "syv/seks byer" i `data_local.py` er erstattet af `nw()`, og `CLAIMS` nederst i `data_local.py` får bygget til at fejle, hvis en ny by gør et sammenlignende udsagn ("højeste", "flest" ...) forkert.
**Byer med >90 % fjernvarme:** sæt `CITIES[slug]["vp_page"] = False`. Så bygges ingen `/varmepumpe/<slug>/`; alle varmepumpe-links peger på fjernvarme-eller-varmepumpe-siden, som får varmepumpe-blokkene (`lokalt`, `opvarmning`, `lokale-byer` i `FV_ORDER`) og en 307-redirect fra `/varmepumpe/<slug>/` i `vercel.json`. `check.py` håndterer det og viser lighed for nye sider mod de eksisterende.
Deploy-flow (fra 26/10 2026): kør `python3 src/refresh_elpris.py` i stedet for build.py; den bygger, tjekker og laver upload-listen. Se "Elpris-rutinen" nederst.
- 2026-10-26: Aarhus (93 % fjernvarme, `vp_page` False: solceller, regler, fjernvarme-eller-varmepumpe) og Viborg (alle 4 sider) tilføjet og deployet til produktion (`dpl_FjjBzTSbKW78uKzEUWEZskze7W1J`). check.py: 55 sider, 0 brudte links, 55 JSON-LD OK; nye sider lighed (ny metode) gns 17-30 %, maks 36 %; Lighthouse mobil 100/100/100/100 (`verify/lh-v8-summary.txt`). Backup før ændringer: `_backup-2026-10-26/`. 58 byer tilbage i køen.
- 2026-10-27: Næstved (DK2, Region Sjælland; alle 4 sider) og Silkeborg (alle 4 sider) tilføjet og deployet til produktion (`dpl_7neGvocGTYRZWTeQxDrKRfUJy5jt`). Solceller-hubtitlen er ændret til "Solceller i din by: lokale regler, priser og tilbud" (Næstved ligger på Sjælland). Sammenlignende tekster i `data_local.py` er gjort dynamiske med `rk()`/`above()`, og `CLAIMS` er tilpasset (Randers-FJ-vagten fjernet, Næstved-gasfyr-vagt tilføjet). Varmepumpe-hubtitlen er forkortet til "Luft-vand-varmepumpe: ..." (69 > 68 tegn med 11 byer). `verify/check.py` finder nu selv den nyeste by-batch (`NEW`). Krydslinks: én inline-tekstlink i boliger-afsnittet på solcelle-bysiden til administratortjekket.dk (`CROSS_CITY_LINKS` i `config.py`, kun live sider: aarhus, odense, aalborg, randers, naestved, kolding, vejle). check.py: 64 sider, 0 brudte links, GATE OK; nye sider lighed (ny metode) maks 39 pct.; Lighthouse mobil lokalt 100/100/96/100 (best practices -4 kun pga. 404 på /_vercel-scripts lokalt; `verify/lh-v9-summary.txt`). `--verify-live` OK. Backup: `_backup-2026-10-27/`. 56 byer tilbage i køen.
- 2026-10-28: Holbæk (DK2, alle 4 sider; Fors Varme/FORS, Mørkøv) og Slagelse (DK2, alle 4 sider; SK Varme, Hashøj Kraftvarmeforsyning) tilføjet. Kilder: DST BOL102/BOL101/BYGB50/BY3 (316/330), PVGIS 5.3, Forsyningstilsynet prisstatistik jan. 2026, kommunernes egne sider. `CLAIMS` tilpasset de nye byer: Vejle-VP-overskrift og Næstved-gas-overskrift omskrevet (Holbæk har nu flest gasfyr og flest varmepumper), Viborg-før-1960 og Vejle-højeste-VP fjernet, Esbjerg-PV og Aalborg-juni lempet til top 3, ny Holbæk-vagt. Krydslink Silkeborg -> administratortjekket.dk/ejendomsadministration/silkeborg/ (gik live 28.10). check.py: 72 sider, 0 brudte links, GATE OK; nye sider lighed (ny metode) maks 40 pct.; Lighthouse mobil lokalt 100/100/96/100 (`verify/lh-v10-summary.txt`). Backup: `_backup-2026-10-28/`. 54 byer tilbage i køen.
- 2026-10-29: Roskilde (DK2, alle 4 sider; Fors Varme Roskilde, Svogerslev Fjernvarmecentral; fjernvarmeprojekterne i Jyllinge, Viby-Dåstrup, Gadstrup-Snoldelev og St. Valby-Ågerup bortfaldet 5/8 2026) og Sønderborg (DK1, alle 4 sider; Sønderborg Varme, SONFOR på Nordals; udbygning mod Nybøl, V. Sottrup, Avnbøl, Ullerup, Blans) tilføjet. Kilder: DST BOL102/BOL101/BYGB50/BY3 (265/540), PVGIS 5.3, Forsyningstilsynet prisstatistik jan. 2026, Roskilde/Sønderborg Kommunes sider, Fors, Sønderborg Varme, SONFOR, ProjectZero (log: `research/v5/fetch_2026-10-29.log`). `CLAIMS`: Roskilde har nu højeste ejerandel, så Horsens-teksterne bruger `rk(_EJ, ...)` (vagt: top 2); Esbjerg-PV og Aalborg-juni lempet til top 4; nye vagter for Roskilde-gas- og Sønderborg-fjernvarme-overskrifterne. Nyt valgfrit felt `CITIES[c]["vp_title"]`/`["fv_title"]` i `build.py`, kun til byer hvor standardtitlen bliver > 68 tegn (bruges af Sønderborg). check.py: 80 sider, 0 brudte links, GATE OK; nye sider lighed (ny metode) maks 42 pct.; Lighthouse mobil lokalt 100/100/96/100 og 99/100/96/100 (`verify/lh-v11-summary.txt`). 52 byer tilbage i køen.

## Elpris – /elpris/ og "Elprisen i dag"-bokse (26. okt. 2026)

Første elpris-deploy: dpl_9kzvBYzHxAisopJgJuQRkACNjm3w (26. okt. 2026).

**Hvad:** `/elpris/` viser spotprisen og en anslået samlet pris pr. kWh for DK1 og DK2 for i dag og (efter ca. kl. 13) i morgen, kvarter for kvarter, med billigste/dyreste time, sammenligning af 6 netselskaber, afsnit om solceller og varmepumpe og en FAQ. Alle bysider (solceller + varmepumpe; for byer med `vp_page` False fjernvarme-siden) har en "Elprisen i dag i <by>"-boks for byens prisområde, med link til `/elpris/#dk1`/`#dk2`. Beregneren har valgfrie knapper "Brug dagens gennemsnitspris" (standarden 1,45 kr. med kilde bevares).

**Kilder (kun åbne, gratis):**
- Spotpris: Energi Data Service, datasæt `DayAheadPrices` (15-min.-opløsning; `Elspotprices` sluttede 30/9 2025).
- Nettarif C (husstande, 0,4 kV), Energinets transmissionsnettarif (40000) og systemtarif (41000) samt elafgift (EA-001): `DatahubPricelist`. Netselskaber og koder står i `src/elpris.py` (`NET`). Standard: N1 (DK1) og Radius (DK2). Rabatkoder (Konstant, Cerius) lægges til.
- Elafgift 2026-2027: 0,8 øre/kWh ekskl. moms, tjekket hos Skattestyrelsen 26/10 2026 (samme sats som EA-001).
- Samlet pris = (spot + nettarif C + transmission + system + elafgift) × 1,25. Uden elselskabets tillæg og abonnementer.
- Prisområde pr. by: `CITIES[slug]["price_area"]` hvis sat, ellers regionen fra `city-queue.json` (Nordjylland/Midtjylland/Syddanmark = DK1, Sjælland/Hovedstaden = DK2). Ukendt region stopper buildet med en tydelig fejl.
- API'et tillader ikke CORS fra browseren, så siden opdateres ved build (dagligt). JS (`/assets/elpris.js`) skifter område, markerer "lige nu" og viser en note, hvis data ikke er fra i dag. Ingen cookies/storage.

**Filer:** `src/elpris.py` (hent/beregn/valider), `src/elpris_data.json` (sidst gode data), `src/refresh_elpris.py` (kommandoen), elpris-delen i `src/build.py`, gate + elpris-tjek i `verify/check.py` (exit 1 ved fejl), `deploy/` (manifest, baseline, base64-filer).

### Elpris-rutinen (dagligt ca. 13:45) og by-rutinen (ca. 08:00)
1. `python3 src/refresh_elpris.py` – henter i dag + i morgen, validerer (96 kvarterer pr. område, priser mellem -5 og 15 kr./kWh, tariffer og afgifter til stede, i morgen påkrævet efter kl. 13:30), bygger, kører `verify/check.py` på en midlertidig lokal server og laver `deploy/files.json` (alle filer) og `deploy/upload.json` (kun ændrede filer siden sidste deploy, med sti til base64-fil i `deploy/b64/`). Fejler hentningen, bruges sidst gode data, hvis de dækker i dag. Status i `deploy/status.json`.
   - Exit 0: klar (eller `nothing_changed: true` → intet at deploye). Exit 2: ingen gyldige data for i dag → deploy ikke. Exit 3: morgendagens priser mangler efter 13:30 → kør igen om 15-30 min. Exit 4: build/check fejlede → deploy ikke, se `verify/check-output-elpris-latest.txt`.
2. Deploy (kun ved exit 0 og `upload > 0`) via Vercel MCP: for hver post i `deploy/upload.json` kald `upload_file` (teamId `team_l9YfcotvB0nBpn4CAogk8M3g`, `xVercelDigest` = sha, `contentLength` = size, `requestBody` = `"$file:<b64-sti>"`). Kald derefter `create_deployment` med `name`/`project` `energitjekket-preview`, `target` `production`, `projectSettings` `{"framework": null}`, `skipAutoDetectionConfirmation` `"1"` og `files` = indholdet af `deploy/files.json`.
3. `python3 src/refresh_elpris.py --verify-live` – tjekker at /elpris/ giver 200 og indeholder dagens (og evt. morgendagens) dato i HTML, og at alle sitemap-URL'er giver 200.
4. `python3 src/refresh_elpris.py --mark-deployed <dpl-id>` – gemmer baseline, så næste kørsel kun uploader ændrede filer.

Instagram-story: når `refresh_elpris.py` har givet exit 0, kør `node social/bin/elpris-story.js`. Scriptet opdaterer selv kilderegisteret (`social/data/export_sources.py`) og skriver morgendagens spotpriser for Vestdanmark (DK1) og Østdanmark (DK2) som story-PNG'er til `social/out/stories/<dato>/` (`elpris-DK1.png`, `elpris-DK2.png`; begge eller ingen). Exit 3 = datoen mangler i elpris-data, intet skrives; exit 4 = eksport-, render-/layoutfejl eller manglende lydfil. Fredag efter 13:45 køres `node social/bin/elpris-story.js --reel` (morgendagen er lørdag), som også laver `reel-<dato>.mp4` til fredagens 19:30-slot; musikken vælges på skift fra `social/audio/` efter dato.

By-rutinen kl. 08:00 bruger samme kommando i stedet for `cd src && python3 build.py` (efter nye byer er lagt ind), så bysiderne får friske elpriser. Kommandoen er idempotent og låst mod samtidige kørsler (`deploy/.lock`).

## Egen cookiefri statistik (26. okt. 2026)
- `src/config.py`: `FIRST_PARTY_ANALYTICS = True` indsætter et inline script (<1 KB) på alle sider via `ANALYTICS_HTML` (ved siden af Vercel Web Analytics/Speed Insights, som er uændrede). Det kører derfor automatisk med i både 08:00-byrutinen og 13:45-elpris-rutinen (begge bygger via `build.py`).
- Hændelser: `pageview`, `form_open` (første fokus/ændring i #lead-form), `form_submit` (kun service+by; se fix nedenfor), `cta_click` (klik på links til `/tilbud/`).
- Sender kun når hostname er energitjekket.dk/www, ikke ved Do Not Track eller `navigator.webdriver` (så check.py/Lighthouse/Playwright ikke tæller).
- Endpoint: CRM-Supabase (casper-crm, eu-central-1) edge-funktionen `track`. Ingen nøgler i browseren. Detaljer: `/workspace/leadsites/crm-analytics/DATA_CONTRACT.md`.
- Første deploy med statistik: dpl_DCRCX5qNLPBt7fyCaaMzZxJcwAxD.
- 2026-10-26 fix af tabt `form_submit`: beaconet blev droppet når form.js straks skiftede til /tak/. Nu gemmer form.js `{service, city, p: formularsidens sti}` i `sessionStorage['et_fs']` ved vellykket POST (ikke ved honeypot) og redirecter; `FP_JS` sender på /tak/ (efter pageview) `form_submit` med formularsidens sti (`t(e,x,p)` har valgfri sti) og sletter nøglen. Ligger i `build.py`, så rutinerne bevarer det. Backup: `_backup-2026-10-26-fsfix/`. Deploy: `dpl_EuAmX45hxn2oe4uzdHK56q2LVtpP`. Caspers test-lead (10:10:13Z) er lagt ind manuelt i `web_analytics.events` (id 14) og `daily_counts.accepted` +1.
- Google Search Console: `googleef0dc5cbecefbd94.html` (indhold: `google-site-verification: googleef0dc5cbecefbd94.html`) skrives i roden af `build.py` ved hvert build. Skal blive liggende permanent, er ikke i sitemap, og `verify/check.py` springer den over som side men fejler, hvis den mangler eller er ændret. Første deploy: dpl_U2xSkGRqqA7RJPjUEngWUpdxQLqk (27. okt. 2026).

## GitHub og deploy (fra 27. okt. 2026)

- Repo: https://github.com/ChucksDK/energitjekket (branch `main`). Vercel-projekt `energitjekket-preview` i ChucksDK-teamet (aldrig casper@casperlarsen.dk-kontoen).
- **Push til `main` = produktion.** Vercel bygger ikke noget: den statiske side i `site/` committes færdigbygget, og `vercel.json` i repo-roden (genereres af `src/build.py`) siger `framework: null`, ingen build/install og `outputDirectory: "site"`. `site/vercel.json` er samme config uden output-feltet og bruges ved fil-deploys via MCP.
- Flow: byg (`python3 src/refresh_elpris.py` eller `cd src && python3 build.py`), kør `verify/check.py`, og så `git add -A && git commit -m "..." && git push origin main`.
- Fil-deploys via MCP (elpris- og byrutinerne) virker stadig, men så halter GitHub bagefter. Commit og push derfor også efter hver rutine-kørsel, så repoet altid svarer til det, der er live.
- Ikke i git (`.gitignore`): `screenshots/`, `*.zip`, `_backup-*/`, `_v*-backup*/`, `deploy/` (upload-manifest og base64), `verify/lh-*.json`, `.env*`, `.vercel/`. Ingen hemmeligheder i repoet; nøgler ligger som Supabase-secrets.
- 2026-10-29: krydslinks Viborg og Roskilde -> administratortjekket (begge 200 live).
- 2026-10-30: Køge (DK2, alle 4 sider; Køge Fjernvarme K02/K05-K08, Bjæverskov Fjernvarme, Borup Varmeværk, Køge Varme A/S) og Svendborg (DK1, alle 4 sider; Svendborg Fjernvarme, Stenstrup, Skårup; Ollerup/V. Skerninge/Ulbølle og Lundeborg udlagt til individuel varme) tilføjet. Kilder: DST BOL102/BOL101/BYGB50/BY3 (259/479), PVGIS 5.3, Forsyningstilsynet prisstatistik jan. 2026 (Køge Fjernvarme/VEKS indgår ikke), Køge/Svendborg Kommunes sider, Køge Fjernvarme, Svendborg Fjernvarme, Dansk Fjernvarme (log: `research/v5/fetch_2026-10-30.log`). `CLAIMS`: Køge har nu flest gasfyr, så Holbæk-overskriften er omskrevet ("Mange gasfyr og færrest med fjernvarme ...", vagt top 2); Randers-olieteksten bruger `above()` (vagt top 3); Esbjerg-PV top 5, Aalborg-juni top 6; nye vagter for Køge-gas- og Svendborg-fjernvarme-overskrifterne; `_ORDP`/`_NUMW` udvidet til 18. check.py: 88 sider, 0 brudte links, GATE OK; nye sider lighed (ny metode) maks 46 pct.; Lighthouse mobil lokalt 100/100/96/100 (`verify/lh-v12-summary.txt`). 50 byer tilbage i køen.
- 2026-10-30: krydslink Holbæk -> administratortjekket (/ejendomsadministration/holbaek/ 200 live, commit 01ff05c).
- 2026-10-31: Faaborg (DK1, Faaborg-Midtfyn Kommune, alle 4 sider; FFV Varme, Midtfyns Fjernvarme, Kværndrup Fjernvarme; Korinth aflyst 10/12 2025, Espe afsluttet, Brobyværk/Vester Åby/Horne/Falsled/Millinge-Svanninge på pause) og Aabenraa (DK1, alle 4 sider; Aabenraa Fjernvarme: Bolderslev 1. kvt. 2027, Varnæs, konverteringsbidrag; Tumbøl/Felsted overskudsvarme) tilføjet. Kilder: DST BOL102/BOL101/BYGB50/BY3 (430/580), PVGIS 5.3, Forsyningstilsynet prisstatistik jan. 2026, fmk.dk, ffv.dk, aabenraa.dk, aabenraa-fjernvarme.dk, Dansk Fjernvarme (log: `research/v5/fetch_2026-10-31.log`). Nyt valgfrit felt `CITIES[c]["reg_title"]` i `build.py` (kun når kommunenavnet gør regel-titlen > 68 tegn; bruges af Faaborg-Midtfyn). `CLAIMS`: Esbjerg-PV lempet til top 6; nye vagter for Faaborg-FJ, Aabenraa-FJ og Aabenraa-elvarme-overskriften; `_ORDP`/`_NUMW` udvidet til 20. check.py: 96 sider, 0 brudte links, GATE OK; nye sider lighed (ny metode) maks 45 pct.; Lighthouse mobil lokalt 99/100/96/100 og 100/100/96/100 (`verify/lh-v13-summary.txt`). 48 byer tilbage i køen.
- 2026-10-31 (branch `seo-gap-2026-10-31`, ikke merget): SEO-gap runde 1 fra SEO Research (`/workspace/rank-tracking/gap-2026-10-31.md`). Nye guides `/varmepumpe/luft-til-luft/`, `/varmepumpe/luft-til-vand/` og `/ladeboks/` (data_topics.py, UPD2). `/ladeboks/` har `noform: True`: ingen tilbudsformular, fordi formular og backend kun kender solceller og varmepumpe (`hero_noform`, `noform_side` i build.py). Brand: brødkrummen og BreadcrumbList kalder forsiden "Energitjekket" (`crumb_name`), forsidens H1 starter med brandet, footer "Energitjekket forside", /om-os/ har H1 "Om os og vores metode". /varmepumpe/pris/ linker til /varmepumpe/luft-til-vand/ og bruger nu Energisparer.dk's tal for 150 m². check.py: 98 sider, 0 brudte links, GATE OK.
