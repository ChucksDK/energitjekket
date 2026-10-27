# Research: optimale lokale leadsider for solceller og luft-til-vand-varmepumper

*Udarbejdet 23/10 2026. Bygger på `../servicefag-top10-byer.md` (SERP-målinger 23/10 2026). Alle kilder er åbnet 23/10 2026.*

## 1. Hvad ligger i top 5 i dag, og hvor er hullet?

| Konkurrent | Hvad siden er | Svaghed vi kan udnytte |
|---|---|---|
| [solvari.dk/solceller/syddanmark/kolding](https://www.solvari.dk/solceller/syddanmark/kolding) | Katalog over "42 installatører" + formular (op til 4 tilbud). Hollandsk firma (Utrecht). | Ingen lokal viden om Kolding. Mange installatører ligger 50-110 km væk. Anmeldelsestal er tynde (13). |
| [elberegner.dk/varmepumpe/varmepumpe-esbjerg](https://elberegner.dk/varmepumpe/varmepumpe-esbjerg/) | ~300 ord, "3 tilbud", prisspænd uden kilde (60-120k for luft-til-vand). | Tynd, ingen kilder, intet om fjernvarme i Esbjerg (DIN Forsynings havvandsvarmepumper), intet om tilskud. |
| [billigstepris.dk/opgaver/varmepumpe-luft-til-luft/odense](https://www.billigstepris.dk/opgaver/varmepumpe-luft-til-luft/odense) | Lang skabelontekst, by-navn byttes ud. Viser luft-til-luft på en luft-til-vand-søgning. Videresender til 3byggetilbud (kommission oplyst). | Forkert intent, ingen lokale fakta. God praksis vi kopierer: tydelig oplysning om kommission. |
| [energisparer.dk/solceller/pris](https://energisparer.dk/solceller/pris/) | Stærk guide med regneeksempler, kildeliste og "3 tilbud"-CTA. | National, ikke lokal. Viser hvad der skal til for E-E-A-T: metode, kilder, opdateringsdato. |
| Kommunernes egne sider (kolding.dk, randers.dk, horsens.dk, vejle.dk) | Ligger ofte #1 på "solceller [by]". | Informationssøgning: regler. Vi skal besvare samme spørgsmål kort og linke til kommunen og så tilbyde næste skridt (tilbud). |

**Konklusion:** Top 5 er enten kataloger/leadsites med udskiftelig skabelontekst eller kommunesider uden handling. Den åbning, der kan ranke og konvertere, er en side, der (a) svarer på de lokale regler og fjernvarmespørgsmålet med kilder, (b) er aktuel for 2026 (elafgift, tilskudsfrist), og (c) har en kort, tryg formular.

## 2. Bedste praksis (SEO)

- **Undgå doorway-sider.** Google kalder sider, der kun bytter bynavn ud, for doorway/cookie-cutter-sider, og det er spam ([Google spam-politik](https://developers.google.com/search/docs/essentials/spam-policies#doorways), [Google om doorway pages](https://developers.google.com/search/blog/2015/03/an-update-on-doorway-pages)). Derfor har hver byside egne, kildebelagte lokale afsnit: kommunens regler, fjernvarmestatus og egen FAQ.
- **Én søgeintention pr. side:** "solceller [by]" og "(luft til vand) varmepumpe [by]". H1 = ydelse + by. Title ≤ ~60 tegn, meta description ≤ ~155 tegn.
- **Struktureret data:** `Service` med `areaServed` (City) + `Organization` som udbyder, `BreadcrumbList` og `FAQPage`. **Ingen `LocalBusiness` med adresse**: en leadside har ingen fysisk adresse i byen, og en falsk adresse ville være vildledende og i strid med Googles retningslinjer for struktureret data ([generelle retningslinjer](https://developers.google.com/search/docs/appearance/structured-data/sd-policies)). FAQ-rich results vises siden 2023 kun for autoritative myndigheds- og sundhedssider ([Google, aug. 2023](https://developers.google.com/search/blog/2023/08/howto-faq-changes)). Vi beholder `FAQPage`, fordi den er gyldig og hjælper forståelsen, men regn ikke med stjerner/FAQ-udvidelse i SERP.
- **Kortpakken:** næsten alle søgningerne viser et kort ([tidligere analyse](../servicefag-top10-byer.md)). En leadside kan ikke få en Google-virksomhedsprofil uden en reel adresse. Målet er organisk #1-3 under kortet.
- **Intern linkning:** en klynge (hub → byer → anden ydelse i samme by → samme ydelse i nabobyer) fordeler autoritet og giver Google kontekst. Breadcrumbs på alle sider.
- **Hastighed og mobil:** ren HTML/CSS, ingen eksterne fonte eller frameworks, under 100 KB pr. side. Core Web Vitals påvirker brugeroplevelsen, og de fleste lokale søgninger sker på mobil.
- **E-E-A-T:** "Om os" med hvem der står bag (navn, CVR), redaktionel metode, "senest faktatjekket"-dato, kildelinks ved hvert tal og en tydelig oplysning om, hvordan siden tjener penge.

## 3. Bedste praksis (konvertering, CRO)

- Formularen skal være synlig over folden på mobil. Brug **flere trin** med lette spørgsmål først (boligtype, varmekilde) og kontaktoplysninger sidst. Det sænker barrieren, og installatøren får bedre leads.
- Kun nødvendige felter: navn, telefon, e-mail, postnummer. Adresse er valgfri.
- Tillid uden falske tal: ingen opdigtede anmeldelser eller kundetal. Brug i stedet konkret nytte: lokale regler, tilskudsfrist, tjekliste til tilbud ([SparEnergi: hvad et tilbud bør indeholde](https://sparenergi.dk/privat/skal-du-renovere-din-bolig/faa-gratis-stroem-fra-solceller)).
- Aktualitet sælger: Varmepumpepuljen (27.000 kr.) lukker senest 30/11 2026 ([ENS, 2/7 2026](https://ens.dk/presse/varmepumpepuljen-aabner-igen-200-mio-kr-skal-hjaelpe-flere-vaek-fra-olie-og-gas)). Man må gerne indhente tilbud før ansøgning, men ikke indgå en bindende aftale før tilsagn. Det er et stærkt og sandt budskab.

## 4. Jura (Danmark)

- **Markedsføringsloven, vildledning:** siden skal tydeligt sige, at den er en formidlingstjeneste og ikke selv installerer. Den skal også oplyse, hvordan den tjener penge (billigstepris gør det i bunden). Det er indbygget i hero, "Sådan virker det" og footer.
- **Samtykke til at blive kontaktet (markedsføringsloven § 10 / reglerne om uanmodede henvendelser):** ifølge [Forbrugerombudsmanden](https://forbrugerombudsmanden.dk/alle-emner/uanmodede-henvendelser/indhentelse-af-samtykke) skal samtykket være aktivt (ingen forudafkrydset boks) og frivilligt. Det skal nævne **hvilke virksomheder** der må kontakte (skal "oplyses klart, hvem disse virksomheder er"), **hvordan** (telefon/e-mail) og **hvilke produkter**, og at det kan trækkes tilbage. Derfor har sitet en partnerside med [PARTNER-INSTALLATØR]-pladsholdere, som samtykketeksten linker til.
- **GDPR:** oplysningspligt (art. 13): dataansvarlig, formål, retsgrundlag, modtagere, opbevaringstid og rettigheder. Videregivelse til installatører til markedsføring kræver udtrykkeligt, specifikt samtykke med konkrete modtagere ([Datatilsynet: direkte markedsføring](https://cdn.datatilsynet.dk/datatilsynet/Media/638237218449834564/Vejledning%20om%20direkte%20markedsf%C3%B8ring.pdf), [Datatilsynet: samtykke](https://cdn.datatilsynet.dk/datatilsynet/Media/0/C/Samtykke%20(3).pdf)). Privatlivspolitikken er en skabelon med pladsholdere. **Lad en jurist læse den, før siden går live.**
- Ingen cookies eller tracking i denne version. Kommer der analytics, skal der en cookiebanner til.

## 5. Fakta brugt på siderne (verificeret 23/10 2026)

**Nationalt**
- Elafgiften er 0,8 øre/kWh ekskl. moms i 2026 og 2027 (ellers 72,7 øre) ([SKM](https://skm.dk/tal-og-metode/satser/satser-og-beloebsgraenser-i-lovgivningen/elafgiftsloven), [Skattestyrelsen](https://skat.dk/erhverv/afgifter-paa-varer-og-ydelser-punktafgifter/nyhedsbrev-afgifter/midlertidig-nedsaettelse-af-elafgiften-i-2026-og-2027)). Lov nr. 1775/2025: 60,9 øre (2015-niveau) fra 2028 ([Retsinformation](https://www.retsinformation.dk/eli/lta/2025/1775/pdf)).
- Varmepumpepuljen: 27.000 kr. til luft-til-vand/jordvarme, kun uden for fjernvarme og planlagt fjernvarme, åben til 30/11 2026 eller til midlerne er brugt ([SparEnergi FAQ](https://sparenergi.dk/privat/soeg-tilskud/varm-op-til-soege-tilskud-til-en-varmepumpe/faq-varmepumpepulje), [ENS](https://ens.dk/presse/varmepumpepuljen-aabner-igen-200-mio-kr-skal-hjaelpe-flere-vaek-fra-olie-og-gas)). Bygningspuljen er lukket og afløst ([ENS](https://ens.dk/tilskud-og-puljer/tilskuds-stoetteordninger/bygningspuljen-opsplittet-i-puljer)).
- Håndværkerfradrag 2026: 9.000 kr. pr. person, kun arbejdsløn, dækker solceller og varmepumper. Kan ikke kombineres med pristillæg på samme solcelleanlæg. **Kan heller ikke kombineres med tilskud fra Varmepumpepuljen til samme varmepumpe** ([SparEnergi FAQ, opdateret 6/8 2026](https://sparenergi.dk/privat/soeg-tilskud/varm-op-til-soege-tilskud-til-en-varmepumpe/faq-varmepumpepulje)). Rettet i fase 2: fase 1 havde et regneeksempel, der fejlagtigt lagde fradraget oven i tilskuddet ([Skat](https://skat.dk/borger/fradrag/servicefradrag/haandvaerkerfradrag), [Skat betingelser](https://skat.dk/borger/fradrag/servicefradrag/generelle-betingelser)).
- Priser:
  - Luft-til-vand koster typisk 100-130.000 kr. at etablere ([SparEnergi](https://sparenergi.dk/privat/tid-til-skifte-varmekilde/hvilken-type-varmepumpe-skal-du-vaelge)).
  - Solceller: 4 kWp ca. 50-55.000 kr., 6 kWp ca. 90-95.000 kr. og 10 kWp ca. 125-135.000 kr. inkl. montering. 6 kWp har ca. 16 års tilbagebetaling ([energisparer.dk, okt. 2026](https://energisparer.dk/solceller/pris/), kommerciel kilde).
  - SparEnergi: samlet besparelse typisk 2.500-7.000 kr./år og overskudssalg 1.000-4.000 kr./år. Simpel tilbagebetaling ved 4.000 kWh/år: 12 år (2 kWp), 15 år (4 kWp) og 17 år (6 kWp) ([SparEnergi](https://sparenergi.dk/privat/skal-du-renovere-din-bolig/faa-gratis-stroem-fra-solceller)).
- Soltimer: landsgennemsnit 1.669 timer/år (1991-2020). Midtjylland har færrest ([DMI](https://www.dmi.dk/klima/temaforside-klimaet-frem-til-i-dag/nedbor-og-sol-i-danmark)).
- Byggetilladelse til solceller på enfamiliehuse: som udgangspunkt ikke nødvendig, når anlægget ligger plant med taget og overholder BR18 og lokalplan/servitutter (se hver kommune nedenfor).

**Lokalt**
- **Kolding:**
  - Kommunens regler for solceller ([kolding.dk](https://www.kolding.dk/erhverv/byggeri-og-ejendom/solcelleanlaeg-og-solfangere); den gamle URL gav 404 pr. 23/10 2026 og er udskiftet).
  - Kortet over fjernvarme, naturgas, tilslutningspligt og elvarmeforbud ([kolding.dk](https://www.kolding.dk/borger/miljoe-natur-og-klima/varme-og-energi/fjernvarme-og-naturgasomraader)).
  - Christiansfeld-udvidelsen blev opgivet i december 2025 ([Fællesavisen 7/1 2026](https://christiansfeld-avis.dk/2026/01/07/naturgas-forbrugere-siger-nej-tak-til-fjernvarme/)).
- **Vejle:**
  - Fjernvarmekortet, frist 2028, TVIS-overskudsvarme og "overvej at vente" ([vejle.dk, 16/3 2026](https://www.vejle.dk/da/service-og-selvbetjening/borger/bolig-byggeri-og-forsyning/forsyning-og-energi/varme/fjernvarme/kan-jeg-faa-fjernvarme-i-min-bolig/)).
  - Store solcelleanlæg og landzone ([vejle.dk](https://www.vejle.dk/da/service-og-selvbetjening/borger/bolig-byggeri-og-forsyning/forsyning-og-energi/groen-energi/solenergi/)).
- **Esbjerg:**
  - DIN Forsyning: ca. 25.500 husstande, havvandsvarmepumper (70 MW) i drift siden december 2024 ([dinforsyning.dk](https://dinforsyning.dk/da-dk/varme/om-vores-varme)).
  - Kommuneplanens regler for solceller på bygninger, VE 11-12 ([kommuneplan.esbjerg.dk](https://kommuneplan.esbjerg.dk/hovedstruktur/sektorer/vedvarende-energi-ve/)).
- **Odense:**
  - Regler for solceller ([odense.dk](https://www.odense.dk/borger/byggeri/byggetilladelse-og-godkendelse-af-byggeri/skilte-facader-solceller-antenner-og-skorstene/solceller)).
  - Fjernvarme Fyn: "De fleste store bebyggede områder er ved at være forbundne" ([fjernvarmefyn.dk](https://www.fjernvarmefyn.dk/overvejer-du-fjernvarme/nye-omraader/)).
- **Aalborg:**
  - Varmeplanen: 21 områder screenet, kun Ajstrup gennemføres, og ingen yderligere udbygning lige nu ([aalborg.dk](https://www.aalborg.dk/om-kommunen/politikker-strategier-og-planer/varmeplan/)).
  - STRAKS-ansøgning ([aalborg.dk](https://www.aalborg.dk/mit-liv/min-bolig/byggeri/enfamiliehus-og-sommerhus/)).
- **Randers:**
  - Kommunens regler for solceller, bl.a. 2,5 m til skel og terrænanlæg på 1,80 m/35 m² ([randers.dk](https://www.randers.dk/borger/bolig/byggeri/foer-du-bygger/hvad-skal-du-i-gang-med/solceller-og-solfangere/)).
  - Verdo i Spentrup: over 580 tilmeldte, de første tilslutninger i november og transmissionsledningen i efteråret 2027 ([TV2 Østjylland](https://www.tv2ostjylland.dk/randers/580-husstande-klar-til-fjernvarme-08817)).
- **Horsens:**
  - Gratis SolarSim til 15/2 2027. Bevaringsværdi 1-4 betyder, at man ikke kan forvente tilladelse ([horsens.dk](https://horsens.dk/bolig/byggeriogejendom/solceller)).
  - Fjernvarme Horsens: 8.200 → 22.400 kunder (2015-2025) og prognose på 25.000 i 2030 ([Dansk Fjernvarme, 17/3 2026](https://danskfjernvarme.dk/aktuelt/nyheder/2026/10-aars-rejse-til-groen-forsyningssikkerhed)).

## 6. Sidestruktur (fase 2: én samlet side med undersider)

**Byside** (`/solceller/{by}/`, `/varmepumpe/{by}/`):
1. Breadcrumb, H1, intro, formidlingsoplysning og formular over folden.
2. Lokale fakta med kilder og lokale kontakter.
3. "Guides til … i {by}": link til den lokale underside og til de 2 nationale guides for ydelsen.
4. Lokal prisboks. For solceller: kort tekst plus link til prisguiden. For varmepumpe: byens fjernvarmepris mod landsgennemsnittet.
5. 2-3 lokale FAQ med FAQPage-schema.
6. Kort "sådan får du tilbud", CTA og linkblok.

Den lange nationale prissektion og de generelle FAQ er flyttet til guiderne. Det har sænket ligheden mellem bysiderne.

**Lokal underside**: breadcrumb (Forside › Ydelse › By › Underside), formular, sektioner med kilder, FAQ og linkblok:
- til bysiden
- til den anden ydelse i samme by og dens underside
- til samme underside i de 6 andre byer
- til guiderne

**Schema:** Organization (med legalName, CVR, adresse og telefon fra config), WebSite, WebPage, BreadcrumbList, Service (areaServed City, kun lokale sider) og FAQPage.

## 7. Søgeordsevidens for undersiderne (hentet 23/10 2026)

**Metode:**
- Google autocomplete (suggestqueries, hl=da, gl=dk) på seeds pr. by og ydelse (`research/kw/ac1.json`, `ac2.json`).
- People Also Ask og relaterede søgninger via Apify google-search-scraper (`research/kw/serp_paa.json`).

Autocomplete giver ingen søgevolumen. Det viser kun, at varianten eksisterer i Googles forslag.

### Valgt
- `/solceller/kolding/regler-og-byggetilladelse/`
  - Søgeord: **solceller kolding kommune**
  - Evidens: Autocomplete: 'solceller kolding' → 'solceller kolding kommune'; 'kolding kommune solceller'. PAA på 'solceller kolding kommune': 'Skal jeg søge byggetilladelse til solceller?'. Top-resultat er kolding.dk.
- `/solceller/vejle/regler-og-byggetilladelse/`
  - Søgeord: **solceller vejle kommune**
  - Evidens: Autocomplete: 'solceller vejle' → 'solceller vejle kommune'; 'vejle kommune solceller'; 'solcelleanlæg vejle'.
- `/solceller/esbjerg/regler-og-byggetilladelse/`
  - Søgeord: **solceller esbjerg kommune**
  - Evidens: Autocomplete: 'solceller esbjerg' → 'solceller esbjerg kommune'; 'solcelleanlæg esbjerg kommune'; 'esbjerg kommune solceller'.
- `/solceller/odense/regler-og-byggetilladelse/`
  - Søgeord: **solceller odense kommune**
  - Evidens: Autocomplete: 'solceller odense' → 'solceller odense kommune' (første forslag); 'odense kommune solceller'; 'solcelleanlæg odense'.
- `/solceller/aalborg/regler-og-byggetilladelse/`
  - Søgeord: **solceller aalborg kommune**
  - Evidens: Autocomplete: 'solceller aalborg' → 'solceller aalborg kommune'; 'aalborg kommune solceller'; 'solcelleanlæg aalborg'.
- `/solceller/randers/regler-og-byggetilladelse/`
  - Søgeord: **solceller randers kommune**
  - Evidens: Autocomplete: 'solceller randers' → 'solceller randers kommune'; 'randers kommune solceller'.
- `/solceller/horsens/regler-og-byggetilladelse/`
  - Søgeord: **solceller horsens kommune**
  - Evidens: Autocomplete: 'solceller horsens' → 'solceller horsens kommune'; 'horsens kommune solceller'. PAA på 'solceller horsens kommune': 'Kan det betale sig at få solceller i 2026?', 'Hvad koster solceller inkl. montering?'.
- `/varmepumpe/kolding/fjernvarme-eller-varmepumpe/`
  - Søgeord: **fjernvarme kolding / varmepumpe eller fjernvarme**
  - Evidens: Autocomplete 'fjernvarme kolding': 10 forslag (bl.a. 'fjernvarme kolding pris', 'fjernvarme kolding kommune', 'trefor fjernvarme kolding'). 'fjernvarme christiansfeld' → 'christiansfeld fjernvarme pris'; 'fjernvarme vamdrup' → 'vamdrup fjernvarme priser'. National: 'fjernvarme eller varmepumpe' (PAA: 'Hvad kan bedst betale sig, fjernvarme eller varmepumpe?').
- `/varmepumpe/vejle/fjernvarme-eller-varmepumpe/`
  - Søgeord: **fjernvarme vejle / varmepumpe eller fjernvarme vejle**
  - Evidens: Autocomplete 'fjernvarme vejle': 10 forslag (bl.a. 'fjernvarme vejle kommune', 'fjernvarme vejle pris', 'vejle fjernvarme priser'). 'fjernvarme give' → 'give fjernvarme priser'; 'fjernvarme jelling' → 'jelling fjernvarme priser'; 'fjernvarme egtved'. 'luft til vand varmepumpe vejle' findes også som forslag.
- `/varmepumpe/esbjerg/fjernvarme-eller-varmepumpe/`
  - Søgeord: **fjernvarme esbjerg / esbjerg fjernvarme varmepumpe**
  - Evidens: Autocomplete 'fjernvarme esbjerg': 10 forslag (bl.a. 'fjernvarme esbjerg pris', 'esbjerg fjernvarme varmepumpe', 'fjernvarme pris esbjerg 2026'). PAA: 'Hvor får Esbjerg fjernvarme fra?'. Også 'fjernvarme ribe' og 'fjernvarme bramming' med prisforslag.
- `/varmepumpe/odense/fjernvarme-eller-varmepumpe/`
  - Søgeord: **fjernvarme odense / varmepumpe odense**
  - Evidens: Autocomplete 'fjernvarme odense': 10 forslag (bl.a. 'fjernvarme odense kommune', 'odense fjernvarme prisstigninger'). 'fjernvarme årslev' → 'fjernvarme fyn årslev'. 'varmepumpe odense' → 'varmepumpe service odense'.
- `/varmepumpe/aalborg/fjernvarme-eller-varmepumpe/`
  - Søgeord: **varmepumpe aalborg fjernvarme / fjernvarme aalborg pris**
  - Evidens: Autocomplete 'varmepumpe aalborg' → 'varmepumpe aalborg fjernvarme', 'varmepumpe aalborg kommune'. 'fjernvarme aalborg': 10 forslag (bl.a. 'fjernvarme aalborg pris', 'aalborg fjernvarme pris 2026'). PAA på 'varmepumpe aalborg fjernvarme': 'Må man installere en varmepumpe, når man har fjernvarme?'. Relaterede: 'Havvandsvarmepumpe Aalborg', 'Norbis Park'.
- `/varmepumpe/randers/fjernvarme-eller-varmepumpe/`
  - Søgeord: **fjernvarme randers / fjernvarme spentrup / varmepumpe randers**
  - Evidens: Autocomplete 'fjernvarme randers': 9 forslag (bl.a. 'verdo fjernvarme randers', 'tilslutning fjernvarme randers'). 'fjernvarme spentrup' → 'tilmelding fjernvarme spentrup'. 'fjernvarme assentoft' → 'fjernvarme assentoft pris'. PAA på 'fjernvarme spentrup': 'Kan man blive tvunget til fjernvarme?'. Relaterede: 'Verdo fjernvarme Assentoft', 'Fjernvarme Stevnstrup', 'Fjernvarme Harridslev'.
- `/varmepumpe/horsens/fjernvarme-eller-varmepumpe/`
  - Søgeord: **fjernvarme horsens / varmepumpe horsens**
  - Evidens: Autocomplete 'fjernvarme horsens': 9 forslag. 'fjernvarme brædstrup' → 'brædstrup fjernvarme priser'; 'fjernvarme østbirk'. 'luft til vand varmepumpe horsens' og 'varmepumpe installation horsens' findes som forslag.
- `/solceller/pris/`
  - Søgeord: **solceller pris / solceller pris inkl montering**
  - Evidens: Autocomplete 'solceller pris': 'inkl montering', 'pr m2', 'med batteri', '2026', 'pr kwh'. PAA: 'Hvad koster solceller inkl. montering?', 'Kan det betale sig at få solceller i 2026?', 'Hvad koster 10m2 solceller?', 'Kan private solceller betale sig?'. Bylokale varianter ('solceller pris kolding' osv.) gav INGEN forslag i nogen af de 7 byer, så der er ingen pris-side pr. by.
- `/solceller/med-batteri/`
  - Søgeord: **solceller med batteri / solceller med batteri pris**
  - Evidens: Autocomplete 'solceller med batteri': 'pris', 'inkl montering', '10 kwh', 'tilbud'. 'solceller pris' → 'solceller pris med batteri'. PAA: 'Kan det betale sig at købe solceller med batteri?', 'Hvad koster et 5 kW solcelleanlæg med batteri?', 'Hvad koster det at få solceller og batteri?', 'Hvilke solceller med batteri er bedst?'. Bylokale varianter gav ingen forslag.
- `/varmepumpe/pris/`
  - Søgeord: **luft til vand varmepumpe pris / pris inkl montering**
  - Evidens: Autocomplete 'luft til vand varmepumpe pris': 10 forslag (bl.a. 'inkl montering', 'inkl montering jylland', '200m2', '250 m2', '300 m2'). PAA: 'Hvad koster en varmepumpe til et hus på 150 m2?', 'Kan det betale sig at få en luft til vand varmepumpe?', 'Hvad koster en luft til vand varmepumpe om året?'. Bylokale varianter ('luft til vand varmepumpe pris odense' osv.) gav INGEN forslag i de 7 byer, så der er ingen pris-side pr. by.
- `/varmepumpe/tilskud/`
  - Søgeord: **varmepumpepuljen 2026 / varmepumpe tilskud**
  - Evidens: Autocomplete 'varmepumpepuljen': '2026', '2027', 'status', 'opbrugt', 'ansøgning', 'udbetaling'. 'varmepumpe tilskud': '2026', '2027', 'og håndværkerfradrag'. PAA: 'Er varmepumpepuljen 2026 opbrugt?', 'Hvornår kan man søge varmepumpepuljen?', 'Er varmepumpepuljen stadig åben?', 'Er der stadig midler i varmepumpepuljen?'. Også 'udfasning af gasfyr' og 'gasfyr til varmepumpe'.

### Fravalgt (risiko for doorway-sider)
- **Prissider pr. by**, fx `/solceller/kolding/pris/`. "solceller pris {by}", "luft til vand varmepumpe pris {by}", "varmepumpe pris {by}" og "solceller med batteri {by}" gav **ingen** autocomplete-forslag i nogen af de 7 byer. Vi har heller ingen kilde til lokale prisforskelle. Derfor er der lavet én national prisside pr. ydelse.
- **Sider for mindre byer**, fx Vamdrup, Ribe, Nørresundby og Brædstrup. "solceller {by}" og "varmepumpe {by}" gav mest kun ekko-forslag uden varianter. Undtagelsen er fjernvarmesøgninger ("fjernvarme ribe/bramming/give/vamdrup/brædstrup", "tilmelding fjernvarme spentrup"). Byerne og deres værker er derfor dækket med rigtige tal i fjernvarmeundersiderne, ikke som egne sider.
- **Kolding Grøn Pulje.** Den gælder kun VE-naboprojekter og er ikke relevant for husejere.

### Nye kilder i fase 2
- Forsyningstilsynets prisstatistik pr. 31/1 2026 (standardhus 130 m², 18,1 MWh, inkl. moms). Siden var nede ved faktatjekket, så tallene er kontrolleret i Wattguidens gengivelse af alle 374 værker.
  - Vægtet landsgennemsnit: 16.953 kr.
  - Værkerne er angivet med postnummer, ikke kommune.
- Bolius: opvarmningsformer for et 130 m² hus.
- Energiankenævnet: udtrædelsesgodtgørelse og faste afgifter.
- Verdo: nye fjernvarmeområder.
- Aalborg Forsyning: Norbis Park.
- Aalborg Kommune: VE-projekter.
- BR18 § 179.
- Vejle Kommune: byggesag og gebyrer.
- Energisparer.dk: varmepumpepris (kommerciel kilde).
- SparEnergi: de 5 krav.
- Statens tilskudspuljer.
- TEKNIQ 13/10 2026: knap 44 mio. kr. tilbage.
- Evida: afkoblingspuljen 2026.

### Lighed mellem sider (difflib på hovedindhold uden formular, header, footer og linkblok, autojunk=False)
- Fase 1, bysider: solceller gns. 73 %, varmepumpe gns. 72 %.
- Fase 2: se output af `verify/check.py`.
