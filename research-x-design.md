# Research: hvad gør lead-gen-sider for solceller, varmepumper og håndværk gode? (X + web)

Researchet 24. oktober 2026 via X' offentlige søgning (søgninger på "lead gen" + landing page/form/quiz, home services/solar/HVAC + conversion, "rank and rent", "multi-step form", sticky/tap-to-call mobile CTA, local SEO city pages + internal links/navigation, trust signals/stock photos, page speed). Alle opslag nedenfor er hentet og læst i fuld tekst. Likes/følgere er fra hentningstidspunktet. Mange af opslagene er praktikeres egne erfaringer og påstande, ikke kontrollerede studier, så tal i dem (fx "konvertering 2,3 % → 7,8 %") er anekdoter og bruges ikke på sitet.

## De vigtigste lektioner (og hvad vi gjorde med dem)

### 1. Heroen skal sige hvad, hvor og hvorfor stole på det på 3-5 sekunder, med ÉN klar handling
- @thetimnewton: "Headline: Service + City + Benefit", "One clear CTA", "Dedicated page, small navigation, loads fast." https://x.com/thetimnewton/status/2113390472106479930
- @boringlocalseo (homepage local relevance audit): "Can a stranger understand the service and market in 3 seconds?" … "Use one clear next step … Do not make the buyer choose between six buttons." https://x.com/boringlocalseo/status/2113963559214604703
- @LewisFontan: "Can a stranger say what you sell in 5 seconds? One button, one action. Proof above the fold. Works on a phone." https://x.com/LewisFontan/status/2109053529931567114
- @DanielPriestley: hook → tre grunde til at stole på dig → værditilbud → ét specifikt næste skridt (knap + formular). https://x.com/DanielPriestley/status/2110823051625410734
- **Gjort:** H1 = ydelse + by (fandtes), ny hero med kort værdiløfte, tre dokumenterbare forsikringer, én primær knap ("Få gratis tilbud") og formularen ved siden af på desktop.

### 2. For mange CTA'er dræber konverteringen; knappen skal sige hvad man får
- @jarydesign: "too many damn calls to action … 1 primary CTA (… sticky on mobile) … 2 max if you must (call + ultra-short form)." https://x.com/jarydesign/status/2023197132573073795
- @yasiruiux: "The CTA says 'Submit' instead of what you actually get." https://x.com/yasiruiux/status/2111819594495394004
- **Gjort:** Kun én handling går igen over hele sitet (tilbudsformularen). Knapteksterne er "Få gratis tilbud" og "Få mine tilbud", ikke "Send"/"Submit". Ingen chat-widgets eller pop-ups.

### 3. Mobil: en sticky CTA og store trykflader
- @coling_pcc: "Over 70 percent of home service leads come from mobile … CTA … Large and easy to tap … Sticky so it stays visible while scrolling." https://x.com/coling_pcc/status/1889177740693123159
- @noelcetaSEO: header (sticky), hero, mellem sektioner, footer; "Large touch targets, Minimal typing required." https://x.com/noelcetaSEO/status/2054268189438079446
- @sandislonjsak (launch-checkliste): "Sticky mobile CTA", "Breadcrumb navigation", "Clear navigation with important pages easy to reach", "Custom 404 page with useful navigation". https://x.com/sandislonjsak/status/2087897662792032365
- **Gjort:** Sticky header, sticky CTA-bjælke nederst på mobil (skjules når formularen er i billedet), mobilmenu, trykflader ≥ 44 px. Tap-to-call er bevidst IKKE tilføjet: det eneste kendte nummer er CVR-nummeret 29 72 84 48, som sandsynligvis er privat (se config.py). Kan slås til, når der er et dedikeret nummer.

### 4. Tillid ved siden af CTA'en, men kun ægte bevis (ingen stockfotos, ingen opdigtede anmeldelser)
- @HVACSEO: "real photos of your team and your work not stock photos", besvar "Who are you? What can you do for me? Why should I pick you?" https://x.com/HVACSEO/status/2031369230973808974
- @noahiglerSEO's master list (bl.a. "3 reassurances near your CTA", "Real photos from actual jobs, not stock images", "FAQ section answering common objections", "Service process breakdown so they know what to expect", "Pricing context … to pre-qualify leads"). https://x.com/noahiglerSEO/status/2011143218310848935
- @ecomsamguy: "Physical address + phone (if local)", "Verified reviews with dates". https://x.com/ecomsamguy/status/2015443676135108771
- **Gjort:** Vi HAR ingen anmeldelser, kundetal eller job-fotos, så vi bruger de dokumenterbare tillidssignaler: firmanavn og CVR (ANGU ApS, CVR 40086560) i hero og footer, "faktatjekket 23. oktober 2026", kildehenvisning ved hvert tal, en tydelig "sådan virker det"-proces og ærlig formidlings-disclaimer. Ikoner er inline-SVG, ingen fotos af personer. Stjerner, "X kunder" og testimonials er bevidst udeladt (de ville være opdigtede).

### 5. Korte formularer, gerne i trin: få felter tæller mere end få trin
- @noahiglerSEO: "Form no longer than 3 required fields". https://x.com/noahiglerSEO/status/2011143218310848935
- @alaramarketing (rengøringskunde): "New landing page w/ simple layout ✅ Multi-step form" som de største ændringer. https://x.com/alaramarketing/status/1579815144477306880
- @JHarulow: "Changing from a standard form to a multi-step form … doubled conversion rates." https://x.com/JHarulow/status/1361346973287202818
- @JimLeadGen: "use a multi step form with logic that only counts conversions from higher quality leads". https://x.com/JimLeadGen/status/1794929627707686944
- Web, Baymard (checkout-research, 2024): antallet af felter påvirker brugbarheden mere end antallet af trin; brug ét "Fuldt navn"-felt. https://baymard.com/blog/checkout-flow-average-form-fields
- **Gjort:** Formularen er stadig 3 trin, men har nu en trinviser ("Bolig → Forbrug → Kontakt", "Trin 1 af 3"), store valgfelter, alle felter i trin 2 er valgfri, ét navnefelt, og knappen hedder "Få mine tilbud". Den sender stadig intet (pladsholder).

### 6. Bysider skal være reelt forskellige og bundet sammen. En skabelon hvor kun bynavnet skiftes, ligner doorway-sider
- @ChrisSimpson: "I'd never build a city page by swapping out the city name … one page wearing five name tags, and Google can tell." https://x.com/ChrisSimpson/status/2109697812761837588
- @brass_seo: "Six city pages, one template, city name swapped … ranks all six worse than one strong page would." https://x.com/brass_seo/status/2108225946541248846
- @grownaAI: "Forty city pages, one template … Google mostly reads it as doorway pages." https://x.com/grownaAI/status/2109267160283677149
- @theseoguy_: unikke lokationssider, og "Your homepage links to your service pages. Your service pages link to your location pages. Your location pages link back to related services." https://x.com/theseoguy_/status/2007624038831554884
- **Gjort:** Det lokale indhold (kommunens regler, fjernvarmepriser pr. værk, lokale kontakter) er bevaret uændret. Redesignet rører kun layout og navigation, ikke det kildebelagte indhold.

### 7. Navigation og intern linking: hierarki, kontekstuelle links, footer-sitemap, brødkrummer
- @ChrisSimpson (roofing-playbook): "use header nav, footer nav, and links between the service pages themselves … convert that same list into a static HTML sitemap page in your footer." https://x.com/ChrisSimpson/status/2110480606983573676
- @stephendbaker: "Every page should have 3-5 internal links to other relevant pages", og footer-links alene vægter lidt, så der skal også være kontekstuelle links. https://x.com/stephendbaker/status/2029696962170343872
- @_toddanderson: "Homepage → Service Pages … Service Pages → Location Pages". https://x.com/_toddanderson/status/1912974737849848163
- @AlexLathery (struktur for et lokalt SEO-site, 248 likes): hero med værdiløfte + CTA, serviceområde-oversigt, interne links til kerneydelser, FAQ og proces pr. side. https://x.com/AlexLathery/status/2033665120937590816
- Web, NN/g om brødkrummer: de skal supplere, ikke erstatte, den globale navigation, starte med forsiden, og må ikke ombrydes til flere linjer eller være for små på mobil. https://www.nngroup.com/articles/breadcrumbs/
- **Gjort:** Sticky menu med Solceller / Varmepumpe / Byer / Guides (dropdowns på desktop, foldbar mobilmenu), brødkrummer på én linje (vandret scroll på mobil), "På denne side"-indholdsfortegnelse, byvælger, kort med relaterede sider (by ↔ underside ↔ anden ydelse ↔ guides) og et fuldt HTML-sitemap i footeren.

### 8. Hastighed: under 3 sekunder på mobil
- @Nick_zv_: "Site loads in under 3 seconds", "Mobile-first design … Clear CTA above the fold on every page", "Kill the stock photo slideshow homepage". https://x.com/Nick_zv_/status/2021963333700591653
- @HVACSEO (top 10): "A website that loads in under three seconds on mobile", "City pages for every service you offer". https://x.com/HVACSEO/status/2087966415764570422
- **Gjort:** Ingen webfonte, ingen billeder (kun inline-SVG), én CSS-fil og ét lille script. Målt med Lighthouse (se verify/).

## Andre relevante opslag (læst, brugt som baggrund)
- @freeconlon: en side pr. ydelse/område med én CTA; påstår 2,3 % → 7,8 % for en solcellekunde (anekdote). https://x.com/freeconlon/status/1988708390516711516
- @JobairMahmud365: "The button is hidden. The form is too long. The phone number is not clickable on mobile." https://x.com/JobairMahmud365/status/2103452647466696805
- @seo_bint_ejamil: "Location pages with real value … Changing the city name in a template isn't a strategy." https://x.com/seo_bint_ejamil/status/2111019333904449810
- @briansooy: kunderejsen nysgerrighed → afklaring → beslutning; sitet skal svare på pris og forløb. https://x.com/briansooy/status/2108549289773617339
- @bloggersarvesh: "Local landing pages > homepage", "Call to action above the fold". https://x.com/bloggersarvesh/status/2105349994639474913

## Bevidst fravalgt (selv om opslagene anbefaler det)
- Stjernevurderinger, antal anmeldelser, "X jobs this month", testimonials, partnerlogoer og badges: vi har ingen ægte data, og at opfinde dem er både vildledende og ulovligt (markedsføringsloven).
- At fjerne al navigation på landingssider (@noahiglerSEO, @coling_pcc): det giver mening for betalt trafik, men sitet er bygget til organisk lokal SEO, hvor navigation og intern linking er vigtige (lektion 7). Til betalte kampagner kan man senere lave en navigationsfri variant.
- Tap-to-call: se lektion 3.
