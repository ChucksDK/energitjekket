# Playbook: Instagram for @energitjekket

Fast instruks for alle, der laver indhold til @energitjekket. **Hvem der gør hvad står i `social/ROLLER.md`**: Claude laver og planlægger ugens 13 faste opslag; Grok tager kun den daglige elpris-story og fredagens elpris-reel kl. 19:30. Designet bag står i `social/2026-10-27-instagram-design.md`. Et komplet eksempel på en uge ligger i `social/briefs/EXAMPLE-2026-W45.json` og bygger uden fejl.

## Første gang (opsætning)

Kræver Node 20+, Python 3, ffmpeg/ffprobe og Chromium til Playwright.

```sh
cd social && npm ci                       # installerer playwright 1.48.2 fra package-lock.json
npx playwright install chromium           # henter chromium-1140 (den version 1.48.2 bruger)
#   Ligger browserne et andet sted (fx delt cache), så sæt PLAYWRIGHT_BROWSERS_PATH=<mappe> før kommandoerne.
ffmpeg -version && ffprobe -version       # macOS: brew install ffmpeg
python3 --version                         # bruges af social/data/export_sources.py
npm test                                  # ca. 2–3 min.; alt skal bestå
```

Zernio: konto-id og tidszone står i `social/publish.json`. Nøglen (`ZERNIO_API_KEY`) ligger lokalt i den fil, `keyFile` peger på, eller i miljøet, aldrig i repoet. `node social/bin/queue.js list` tjekker, at adgangen virker.

## Roller

| Hvem | Hvad | Hvornår |
|---|---|---|
| **Claude** | Analyserer tidligere uger og Zernio-køen, skriver ugens brief `social/briefs/<uge>.json`, laver Higgsfield-billeder til covers, kører `build-week`, retter tekst indtil `errors.json` er tom, ser alle slides igennem og kører captions gennem humanizer-reglerne. | Én gang om ugen, før ugen starter |
| **Casper** | Godkender eller afviser hvert opslag i previewet. Godkendelsen kan slås fra i `social/config.json` (`"require_approval": false`). | Før Claude planlægger |
| **Claude** | Planlægger de godkendte opslag i Zernio på @energitjekket med `social/bin/publish.js` og læser dem tilbage. | Efter godkendelse |
| **Grok** | Kun den daglige elpris-story og fredagens elpris-reel kl. 19:30 (kan ikke laves på forhånd). Se `social/ROLLER.md`. | Dagligt / fredag |

## Ugeplan

Morgen kl. 07:30 = carousel. Aften kl. 19:30 = short (10–20 sek., musik, ingen voice). Elpris-story hver dag efter kl. 13:45. Ugens brief har **13 opslag**: 7 carousels og 6 shorts. Fredag kl. 19:30 er reserveret til elpris-reelen, som laves af `elpris-story.js --reel` fredag eftermiddag og ikke står i briefen (Ruling F1: elpriser kendes først dagen før, så et elpris-opslag i ugens brief kan ikke bygges igen senere).

| | Morgen (carousel) | Aften (short) |
|---|---|---|
| Man | Varmepumpe: økonomi (olie/gas) | Samme emne animeret |
| Tir | By: varmepumpe/fjernvarme | Myte |
| Ons | Solceller: 2028-afgift / produktion | Samme emne animeret |
| Tor | Varmepumpe: tilskud/typer/SCOP | "Sådan bruger du beregneren" (med screenshot-slide) |
| Fre | By: solceller | *Elpris-reel: lørdagens billigste timer (scriptet, ikke i briefen)* |
| Lør | Quiz/afstemning | Varmepumpe |
| Søn | Varmepumpe vs. solceller eller "gem til senere"-tjekliste | Ugens bedste, genbrugt eller varieret |

**Søjlefordeling okt.–mar.:** mindst 8 af de 13 opslag om varmepumpe (inkl. byopslag om varmepumpe/fjernvarme), resten om solceller. Elpris kommer fra story og fredags-reel. Apr.–sep. kan det vendes.

**Variation:** samme by må ikke gå igen inden for 2 uger. Samme vinkel ikke inden for 3 uger. Morgen og aften må dele emne. Mindst to byopslag om ugen med forskellige byer.

## Hårde regler

1. **Tal kun som `{fakta.id}`.** Ingen cifre i slide-tekst, caption eller hashtags, undtagen inde i en pladsholder og årstal 2020–2035. Det gælder også "m²" (brug `{bolius.hus.m2}`), "DK1"/"DK2" (skriv "Vestdanmark"/"Østdanmark") og datoer ("en tirsdag i oktober", ikke "27/10").
2. **Find fakta-id'er** med `node social/bin/facts.js <prefix>`, fx `facts.js bolius`, `facts.js pv.aalborg`, `facts.js heat.`, `facts.js elpris`. Findes et tal ikke i registeret, bruges det ikke. Ingen må finde på tal eller hente dem fra nettet.
3. **Ingen salgssnak.** Forbudt (uanset store/små bogstaver): `!`, `book nu`, `begrænset`, `skynd dig`, `gratis`, `garanti`, `kun i dag`, `spar op til`. Ingen superlativer uden tal. Tal aldrig ned til fjernvarme eller andre opvarmningsformer.
4. **`tilbud`** (og URL'er under `/tilbud/`) er kun tilladt i opslag med `"quote": true`, altså opslag der handler om at få et tilbud.
5. **Én side pr. opslag.** `target_url` starter med `https://energitjekket.dk/` og peger på den konkrete side (guide, byside, `/beregner/`, `/elpris/`).
6. **Tal som skøn med kilde:** "ca.", "i et standardhus på {bolius.hus.m2}", "spotpris". Aldrig "du sparer X kr.". Kilden sættes automatisk på hver slide og i captionen.
7. **Længder (efter opløsning af pladsholdere):** tag højst 24 tegn, titel højst 60, brødtekst højst 160. Hold titler under ca. 40 tegn, så de står stort.
8. **Danske sammensatte ord:** bindestreg-ord som "luft til vand-varmepumpe" og "vand-/varmepumpe" holdes automatisk samlet på slides (hård bindestreg), men lange sammensætninger fylder meget. Skriv hellere "varmepumpe (luft til vand)" i titler eller "luft til vand" i en KPI-label.
9. **Elpris er altid spotpris.** Ethvert elpris-tal skal kaldes spotpris i teksten ("Spotpris: billigst …"). Det er prisen uden afgifter, nettarif og moms. Kildelinjen viser "Energi Data Service · spotpris".
10. **Pladsholdere kun i tekstfelter.** `{fakta.id}` må stå i tag, titel, `value`, brødtekst, `highlight`, KPI-`label`/`value` og caption, men ikke i `hashtags` eller KPI-`unit`.
11. **Link på slutslidet kommer fra `target_url`.** Skriv aldrig adressen selv i slide-teksten; `end`-slidet laver link-boksen.
12. **Ingen elpris-opslag i ugens brief.** Layoutet `bars` og fakta-id'er `elpris.<dato>…` hører til `elpris-story.js`. `build-week` afviser `bars` med en dato, der ikke findes i elpris-data, og ethvert opslag fredag kl. 19:30.

## Brief-skema

```json
{
  "week": "2026-W46",
  "posts": [ { ...ét objekt pr. slot, 13 i alt (ingen fredag 19:30)... } ]
}
```

| Felt | Krav |
|---|---|
| `id` | `YYYY-MM-DD-am` eller `YYYY-MM-DD-pm`. Unikt, og datoen skal være slottets dato. |
| `slot` | `YYYY-MM-DDT07:30` (carousel) eller `YYYY-MM-DDT19:30` (short), lokal tid i Danmark. Hvert slot bruges én gang. Fredag 19:30 er ikke tilladt (elpris-reelen). |
| `type` | `carousel` (5–7 slides) eller `short` (3–6 slides, 10–20 sek. i alt). |
| `pillar` | `varmepumpe`, `solceller` eller `by`. |
| `city` | Kun på byopslag, fx `"viborg"` (samme stavning som i fakta-id'erne). |
| `angle` | Vinklen i én linje. Bruges til at undgå gentagelser. Quiz-opslag skal have "Quiz" i vinklen. |
| `quote` | `false`, medmindre opslaget handler om at få et tilbud. |
| `target_url` | Den side, opslaget fører til. |
| `audio` | Kun shorts: et filnavn i `social/audio/`: `bright-explainer-01.m4a`, `bright-explainer-02.m4a`, `melodic-guitar-01.m4a`, `melodic-guitar-02.m4a`. Skift mellem dem. |
| `slides` | Se layouts herunder. `bg` kun på første slide. |
| `caption` | Se caption-regler. Kildelinjen tilføjes automatisk. |
| `hashtags` | 3–5 danske hashtags uden tal og uden pladsholdere, fx `#varmepumpe`. |

**Shortens længde:** hver slide varer 2,5 sek. + 0,25 sek. pr. ord (titel + tal + brødtekst), højst 5 sek. Overgange trækker 0,3 sek. fra pr. skift. Fire slides med 8–12 ord hver giver ca. 18–19 sek. Tre korte slides kan blive under 10 sek.

### Layouts med eksempler

Alle eksempler er fra eksempel-ugen.

**`cover`** – første slide. Mørkegrøn, eller med et Higgsfield-billede via `bg`. `value` er valgfri.
```json
{ "layout": "cover", "tag": "VARMEPUMPE", "title": "Har du stadig oliefyr?",
  "value": "{bolius.oliefyr}",
  "body": "Så meget koster varmen om året i et standardhus på {bolius.hus.m2}.",
  "bg": "assets/EXAMPLE-2026-W45/oliefyr.png" }
```

**`stat`** – ét stort tal med titel over og forklaring under.
```json
{ "layout": "stat", "tag": "SCOP", "title": "Én kWh strøm giver ca.",
  "value": "{beregner.scop}", "body": "kWh varme over et år. Det tal hedder SCOP." }
```

**`kpi2`** – to tal side om side. Enheden står i `unit` og vises på egen linje. Tallet skrives uden enhed (den fjernes automatisk, når `unit` er sat).
```json
{ "layout": "kpi2", "tag": "VIBORG KOMMUNE", "title": "Sådan varmes boligerne op",
  "kpis": [
    { "label": "Fjernvarme", "value": "{heat.viborg.fjernvarme_pct}", "unit": "% af boligerne" },
    { "label": "Varmepumpe", "value": "{heat.viborg.varmepumpe_pct}", "unit": "% af boligerne" } ] }
```

**`bars`** – søjlediagram med 24 timepriser (spotpris). Bruges kun af `elpris-story.js` (story og fredags-reel), ikke i ugens brief. Kildelinjen "Energi Data Service · spotpris" sættes automatisk.

**`text`** – titel og brødtekst, uden tal eller med tal som pladsholder. `highlight` lægger gult på ét ord (første forekomst i både titel og brødtekst, så vælg et ord, der kun står i titlen).
```json
{ "layout": "text", "tag": "HUSK", "title": "Det er udgiften til drift", "highlight": "drift",
  "body": "Tallene viser varmen om året. Prisen for selve varmepumpen skal regnes med for sig." }
```

**`screenshot`** – mobil-screenshot af en side på energitjekket.dk i en telefonramme. Nøgler: `beregner`, `elpris`, `by:<by>:solceller`, `by:<by>:varmepumpe` (kun byer med en byside; Aarhus har ingen varmepumpe-byside).
```json
{ "layout": "screenshot", "tag": "BEREGNEREN", "title": "Sådan ser den ud på mobilen",
  "screenshot": "beregner" }
```

**`end`** – slutslide med link-boks og "Gem opslaget til senere". Linket i boksen laves automatisk ud fra opslagets `target_url` (skriv det ikke selv), og teksten foran følger sidetypen: guides under `/varmepumpe/` og `/solceller/` → "Læs guiden", bysider → "Se tallene for <By>", `/beregner/` → "Regn på dit eget hus", `/elpris/` → "Se dagens priser". Lange adresser brydes efter `/` og krymper, så de altid står inde i boksen. Skriv "Link i bio" i brødteksten: links i Instagram-opslag kan ikke klikkes.
```json
{ "layout": "end", "tag": "LÆS GUIDEN", "title": "Skift oliefyr til varmepumpe",
  "body": "Økonomi, tilskud og olietanken i én guide. Linket står i bio." }
```
giver boksen "Læs guiden → energitjekket.dk/varmepumpe/skift-oliefyr".

### Et helt opslag (short)

```json
{
  "id": "2026-11-07-pm", "slot": "2026-11-07T19:30", "type": "short",
  "pillar": "varmepumpe", "angle": "Gasfyr mod varmepumpe", "quote": false,
  "target_url": "https://energitjekket.dk/varmepumpe/skift-gasfyr/",
  "audio": "melodic-guitar-01.m4a",
  "slides": [
    { "layout": "cover", "tag": "GASFYR", "title": "Har du gasfyr? Det koster ca.", "value": "{bolius.gasfyr}", "body": "om året i et standardhus." },
    { "layout": "stat", "tag": "VARMEPUMPE", "title": "Med varmepumpe og radiatorer", "value": "{bolius.ltv_radiator}", "body": "om året i samme hus." },
    { "layout": "text", "tag": "FØRST", "title": "Kommer der fjernvarme til dig?", "body": "Tjek kommunens varmeplan for din adresse, før du vælger varmepumpe." },
    { "layout": "end", "tag": "LÆS GUIDEN", "title": "Skift gasfyr i tre trin", "body": "Varmeplan, økonomi og tilskud i én guide. Link i bio." }
  ],
  "caption": "Gasfyr: ca. {bolius.gasfyr} om året. Varmepumpe med radiatorer: ca. {bolius.ltv_radiator}.\nTallene er Bolius' for et standardhus på {bolius.hus.m2}.\nStart med varmeplanen for din adresse. Guiden om at skifte gasfyr ligger på energitjekket.dk (link i bio).",
  "hashtags": ["#varmepumpe", "#gasfyr", "#boligejer"]
}
```

## Higgsfield-billeder

- Kun som `bg` på et cover (carousel slide 1) eller hook-frame i en short. Datasider er altid rene slides uden foto.
- Højst ét eller to billeder om ugen. Ingen billede er bedre end et dårligt billede.
- Promptregler: danske huse og interiører (parcelhus, kælder med fyr, køkken ved daggry, tag med solceller i gråvejr), naturligt lys, ingen ansigter mod kameraet, **ingen tekst i billedet** (teksten lægges på af rendereren), ingen logoer, mærker eller produkter, der kan forveksles med et rigtigt firma.
- Format: stående 4:5 til carousel, 9:16 til short. Motivet skal kunne tåle mørk gradient i bunden, hvor teksten står.
- Gem filen i `social/briefs/assets/<uge>/<navn>.png` (den committes sammen med briefen) og skriv `"bg": "assets/<uge>/<navn>.png"` i briefen. `build-week` kopierer den ind i ugemappen, så ugen kan bygges igen fra et rent checkout.

## Caption-regler

- 3–6 korte linjer, dansk, "du"-form, rolig vidende nabo.
- Første linje bærer tallet eller spørgsmålet.
- Nævn den konkrete side og "link i bio", fx "Guiden om at skifte oliefyr ligger på energitjekket.dk/varmepumpe/skift-oliefyr (link i bio)."
- Kildelinjen ("Kilde: Bolius …") og hashtags tilføjes automatisk i `caption.txt`. Skriv dem ikke selv.
- 3–5 danske hashtags: `#varmepumpe #solceller #elpris #boligejer #<by>` m.fl.
- Humanizer-pass før godkendelse: ingen AI-floskler ("i en verden hvor", "dyk ned i", "lad os se på"), ingen kæder af tankestreger, ingen emoji-mure, ingen tomme forstærkere.

## Kommandoer i rækkefølge

Alle kommandoer køres fra repo-roden.

```sh
# 1. Opdater kilderegisteret (elpris, Bolius, beregner, PVGIS, Danmarks Statistik)
python3 social/data/export_sources.py

# 2. Find fakta-id'er til briefen
node social/bin/facts.js bolius
node social/bin/facts.js pv.aalborg
node social/bin/facts.js heat.viborg

# 3. (Claude) Læg eventuelle Higgsfield-billeder i social/briefs/assets/<uge>/

# 4. Byg ugen: validering, screenshots fra live-sitet, PNG/MP4, captions, preview
node social/bin/build-week.js social/briefs/<uge>.json
#    Offline: server site/ lokalt og tilføj --base http://127.0.0.1:<port>
#    Fejl står i social/out/<uge>/errors.json. Ret teksten i briefen og byg igen, til filen er [].

# 5. Godkend i previewet (Casper)
node social/bin/preview-server.js <uge>          # åbn http://127.0.0.1:8787/
#    Godkendte opslag skrives til social/out/<uge>/schedule.json

# 6. (Claude) Planlæg de godkendte opslag i Zernio på @energitjekket
node social/bin/queue.js list                     # hvad ligger der allerede? sammenstød?
node social/bin/publish.js <uge>                  # tørløb: viser hvad der sendes
node social/bin/publish.js <uge> --send           # uploader, planlægger og læser hvert opslag tilbage
#    Planlagte opslag skrives i social/out/<uge>/sent.json og sendes aldrig igen.
#    Flyt/aflys: queue.js move <zernio-id> <YYYY-MM-DDTHH:MM> --send / queue.js cancel <zernio-id> --send
```

### schedule.json (det publish.js sender)

Hvert opslag i `social/out/<uge>/schedule.json` har:

```json
{ "id": "2026-11-02-am", "slot": "2026-11-02T07:30:00+01:00", "type": "carousel",
  "files": ["/…/social/out/2026-W45/2026-11-02-am/2026-11-02-am-01.png", "…"],
  "caption": "…hele caption.txt…" }
```

- `slot` har eksplicit offset for Europe/Copenhagen: `+01:00` om vinteren, `+02:00` om sommeren. Brug tidspunktet præcis som det står.
- `files` er absolutte stier på maskinen, i den rækkefølge de skal postes (carousel: slide 1, 2, …; short: én MP4). `publish.js` uploader filerne fra de stier.
- `caption` er den færdige tekst inkl. kildelinje og hashtags.
- Kun godkendte opslag står i filen. Bygges ugen igen, tømmes den, til Casper har godkendt igen.

### Daglig elpris-story og fredags-reel

Morgendagens priser kommer ca. kl. 13. Efter sitets elpris-rutine kl. 13:45:

```sh
node social/bin/elpris-story.js            # hver dag: morgendagens story for Vestdanmark og Østdanmark
node social/bin/elpris-story.js --reel     # fredag: også reelen med lørdagens billigste timer
```

Scriptet opdaterer selv kilderegisteret først (samme eksport som `build-week`). Output ligger i `social/out/stories/<dato>/`: `elpris-DK1.png` (Vestdanmark), `elpris-DK2.png` (Østdanmark) og om fredagen `reel-<lørdagens dato>.mp4`. Begge story-billeder laves, eller ingen af dem.

- Exit 3: morgendagens priser findes ikke endnu. Så laves der ingen story (ingen gætte-tal); prøv igen senere.
- Exit 4: eksport-, render- eller layoutfejl, manglende lydfil, eller `--reel` på en dato, der ikke er en lørdag.
- Grok planlægger (se `social/ROLLER.md`) storyen samme dag og reelen **fredag kl. 19:30** (det tomme slot i ugen) med filen `social/out/stories/<lørdagens dato>/reel-<lørdagens dato>.mp4` og en kort caption i stil med: "Lørdagens billigste timer på elmarkedet (spotpris) for Vestdanmark og Østdanmark. Se alle timepriser på energitjekket.dk/elpris (link i bio). Kilde: Energi Data Service." plus `#elpris #spotpris #strømpris`. Ingen tal i captionen: tallene står i videoen.
- Link-sticker kan ikke sættes via API, så storyen siger "Se alle priser på energitjekket.dk/elpris".
- Musikken til reelen vælges på skift fra `social/audio/` efter dato.

## Tjekliste før aflevering (Claude)

- `errors.json` er `[]`, og alle 13 opslag står i previewet (fredag 19:30 er tom til elpris-reelen).
- Mindst én slide fra hver carousel og to frames fra hver short er set igennem: intet overlap, tal inde i kasserne, ingen grimme ombrydninger.
- Fordelingen holder (≥ 8 varmepumpe, ≤ 6 solceller), og ingen by eller vinkel gentager sig for tidligt.
- Captions har "link i bio", den konkrete side og 3–5 hashtags.
