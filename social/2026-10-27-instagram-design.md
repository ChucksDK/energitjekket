# Instagram for Energitjekket – design

Dato: 27. oktober 2026. Status: udkast til godkendelse.

> **Ændring 27. oktober 2026 (Casper):** Claude laver nu hele ugen selv (analyse, brief, produktion) og planlægger de godkendte opslag i Zernio med `social/bin/publish.js`. Grok tager kun den daglige elpris-story og fredagens elpris-reel kl. 19:30. Den gældende rollefordeling står i `social/ROLLER.md`; hvor dette dokument siger andet om Grok, gælder `ROLLER.md`.

## Hvorfor

Energitjekket.dk er en lead-side for solceller og varmepumper til danske boligejere (formular → ét firma pr. lead). Instagram skal give organisk dansk trafik til siden, især til `/beregner/`, `/elpris/`, guides og bysider.

Målgruppe: danske boligejere, der er bekymrede over høje energiregninger eller vil optimere deres forbrug.

Danske AI-stemmer (ElevenLabs) er for dårlige, og engelsk duer ikke. Derfor: **ingen voiceover**. Al tekst er dansk tekst på skærmen; shorts bruger musik.

Sitets styrke er data, der allerede findes i repoet (daglige elpriser, beregnerens kildeangivne standardtal, PVGIS og Danmarks Statistik pr. by). Indholdet bygges på de data, ikke på generiske råd.

## Mål, ikke-mål og anti-mål

**Mål**
- 14 feed-opslag om ugen (2 om dagen, 7 dage) + en daglig elpris-story.
- Hvert opslag fører til en konkret side på energitjekket.dk.
- Grok kan levere ugens brief ud fra playbooken; Claude laver opslagene ud fra briefen.
- Fordeling i vinterhalvåret (okt.–mar.): ca. 60 % varmepumpe, 40 % solceller.

**Ikke-mål**
- Voiceover, on-camera-indhold, influencer-stil.
- Engelsk indhold.
- Betalte annoncer (dette er kun organisk).
- Automatisk svar på kommentarer/DM.

**Anti-mål (gør det til en fiasko, selv hvis det virker)** – Caspers egne:
1. **Opdigtede tal.** Alle tal skal komme fra en navngiven kilde, og kilden står på sliden.
2. **Påtrængende salgssnak.** Ingen "Book nu!", "Begrænset tilbud", "Spar 50.000 kr.!", udråbstegn-salg eller falsk hast.

## Stil (valgt: A – "rene data, brandfarver")

- Farver fra sitets `style.css`: mørkegrøn `#0b4f43`, grøn `#0f6b55`, gul `#f5b700` (kun til det ene vigtigste ord/tal pr. slide), mint-baggrund `#f2f8f5`/`#e7f2ee`, tekst `#13201d`, dæmpet `#4f5e5a`.
- Skrift: samme fonte som `src/fonts/` (bruges allerede af `src/visuals.py`).
- Ét budskab og ét stort tal pr. slide. Lille tag-pille øverst (fx "VARMEPUMPE · 1/6", "ELPRIS · TIRSDAG 27/10 · DK1").
- Kilde med småt nederst på hver slide med tal. `@energitjekket` nederst.
- Formater: carousel 1080×1350 (4:5), short/reel og story 1080×1920 (9:16).
- Referencemockup: `social/reference/style-mockup-a-v2.html` – godkendt udgave af stil A (carousel-cover, elpris-story, bypost). `style-mockup.html` er den første sammenligning af A/B/C.
- **Layout uden overlap (Caspers krav):** intet tekst må overlappe andet tekst eller grafik, og tal skal stå helt inde i deres kasser. Ingen absolut placering af tekst; hver slide er bygget som top (tag) / indhold / bund (kilde, @energitjekket, "Swipe →"). Tal brækker aldrig over to linjer (`nowrap`); enheden ("kr./år") står på egen linje under tallet. Er en tekst for lang, gøres skriften mindre inden for faste grænser, og ellers afvises sliden. Det er ikke tilladt at klippe tekst af.

**Higgsfield:** kun som baggrund på enkelte covers/hook-frames i shorts (fx koldt dansk hus, oliefyr i kælder, køkken ved daggry). Datasiderne er altid rene A-slides. Faste prompt-regler: danske huse/interiører, naturligt lys, ingen ansigter mod kameraet, ingen tekst i billedet (tekst lægges på af rendereren), aldrig billeder der kan forveksles med et rigtigt firma eller produktmærke.

**Screenshots:** tages automatisk med Playwright fra live-sitet (beregner, elpris, byside) og bruges som sidste slide/sidste sekunder i shorts, så folk ser, hvor linket fører hen.

## Formater

1. **Carousel (5–7 slides).** Hook → tal → hvad det betyder for dig → (evt. screenshot) → slutslide med link + "Gem opslaget". Hovedformatet for saves/delinger.
2. **Short/reel (10–20 sek.).** De samme slides animeret på canvas i JS: tal tæller op, søjler vokser, tekst glider ind. Trending/stemningsmusik, ingen voice. Starter med det stærkeste tal i første sekund.
3. **Elpris-story (dagligt, 9:16).** Morgendagens priser for DK1 og DK2 som søjlediagram, billigste og dyreste time, link-sticker til `/elpris/`. Fuldautomatisk fra `src/elpris_data.json`.
4. **Quiz/afstemning.** Feed-carousel med spørgsmål på slide 1 og svar på slide 2+ (fx "Hvad tror du, det koster at varme et 130 m² hus op med oliefyr?").

## Indholdssøjler

1. **Elpris** – nytten, folk følger for. Daglig story + fredags-reel "Weekendens billigste timer".
2. **Varmepumpe (~60 %)** – skift fra olie-/gasfyr med beregnerens tal, Varmepumpepuljen 2026, luft-til-luft vs. luft-til-vand vs. jordvarme, SCOP forklaret, myter (frost, støj, gulvvarme).
3. **Solceller (~40 %)** – elafgiften stiger igen fra 2028 (naturlig deadline), produktion december vs. juni (PVGIS-månedsdata), batteri, fladt tag/carport, "kan det betale sig?".
4. **By for by** – én af de 11 byer pr. opslag: "Fjernvarme eller varmepumpe i Viborg?", "Så meget producerer solceller i Aalborg". Linker til bysiden. Nye byer fra den daglige by-rutine kommer automatisk med.

## Ugeplan (14 opslag)

Morgen kl. 07:30 = carousel/billede. Aften kl. 19:30 = short. Story efter kl. 13:45 hver dag (tæller ikke med i de 14).

| | Morgen (carousel) | Aften (short) |
|---|---|---|
| Man | Varmepumpe: økonomi (olie/gas) | Samme emne animeret |
| Tir | By: varmepumpe/fjernvarme | Myte |
| Ons | Solceller: 2028-afgift / produktion | Samme emne animeret |
| Tor | Varmepumpe: tilskud/typer/SCOP | "Sådan bruger du beregneren" (screen recording) |
| Fre | By: solceller | Weekendens billigste elpris-timer |
| Lør | Quiz/afstemning | Varmepumpe |
| Søn | Varmepumpe vs. solceller eller "gem til senere"-tjekliste | Ugens bedste, genbrugt/varieret |

Morgen og aften må dele emne – én idé giver to opslag. Samme by må ikke gå igen inden for 2 uger; samme emne/vinkel ikke inden for 3 uger.

## Regler for indhold

**Tal og kilder (hård regel)**
- Tilladte kilder: data i repoet – `src/elpris_data.json`, beregnerens standardtal (`src/calc_js.py`/`site/beregner/`), `src/data.py`, `src/data_sub.py`, `src/data_local.py`, `src/data_local_gen.py` – og de kilder, sitet selv citerer (Bolius, Energinet/Energi Data Service, PVGIS, Danmarks Statistik, Energistyrelsen, Skatteministeriet, SparEnergi, Energisparer.dk).
- Hvert tal i et opslag har en kilde i post-JSON'en. Rendereren nægter at rendere en slide, hvor et tal mangler kilde.
- Tal står som skøn: "ca.", "for et 130 m² hus", "spotpris". Aldrig "du sparer X kr.", altid "et standardhus kan spare ca. X kr. om året (Bolius/beregneren)".
- Ingen tal hentet fra Groks egen viden eller fra nettet, som ikke allerede står på sitet.

**Tone**
- En vidende nabo, ikke en sælger. Rolig, konkret, dansk hverdagssprog. "Du"-form.
- Slutslide/CTA er en invitation: "Regn på dit eget hus → energitjekket.dk/beregner", "Se dagens priser → energitjekket.dk/elpris", "Læs mere om <by> → link i bio".
- Tilbudsformularen nævnes kun i opslag, der handler om at få et tilbud.
- Forbudt: udråbstegn i salgsøjemed, "begrænset", "skynd dig", "gratis!", garantier, superlativer uden tal, at tale ned til fjernvarme eller andre opvarmningsformer.

**Captions**
- Dansk, 3–6 korte linjer + kildelinje + 3–5 danske hashtags (fx #varmepumpe #elpris #solceller #boligejer #<by>).
- Kører gennem humanizer-reglerne (ingen AI-floskler, ingen tankestreger-spam, ingen emoji-mure).
- Nævner "link i bio" og den konkrete side.

## Produktion

**Roller (Caspers beslutning):**
- **Grok** analyserer, indsamler data og følger instruksen: skriver ugens *brief* (emner pr. slot, vinkel, tal med kilde, by, mål-URL) efter playbooken.
- **Claude** (Claude Code-session i dette repo) laver selve opslagene ud fra briefen: slides, shorts, captions, Higgsfield-billeder, screenshots.
- **Casper** godkender ugen i starten, indtil vi ser, at niveauet er rigtigt. Godkendelsen skal kunne slås fra senere.
- **Grok** planlægger de godkendte opslag i Zernio (07:30, 19:30). @energitjekket er en Business/Creator-konto, der allerede er koblet på Zernio.

**Trin:**
1. **Brief** (Grok, ugentligt): `social/briefs/<uge>.json` – én post pr. slot med type, dato/tid, søjle, evt. by, vinkel, tal med kilde, mål-URL. Skemaet står i playbooken.
2. **Datahjælpere** (Node-scripts i `social/`): eksporterer elpris, beregnerens standardtal og bydata (`data.py`, `data_local_gen.py` m.fl.) til ét kilderegister med kilde-ID'er (`social/data/sources.json`), som genereres fra repoet.
3. **Renderer i JavaScript** under `social/`: HTML-canvas-skabeloner i stil A → PNG (carousel/story, 1080×1350 og 1080×1920) og MP4 (short, 1080×1920) via Playwright + ffmpeg, samme princip som Caspers andre JS-film (casper-javascript).
4. **Validering (streng, før rendering):** hvert tal på en slide skal referere til et kilde-ID i registeret og matche værdien der (afrundinger tilladt efter fast regel). Håndskrevne tal uden kilde-ID afvises. Desuden: tekstlængde pr. slide, forbudte salgsord/udråbstegn, gyldig mål-URL på energitjekket.dk.
5b. **Layouttjek (efter rendering, automatisk):** Playwright måler hver tekstlinje på hver slide/frame: ingen tekst uden for sin kasse eller slidens sikre margen, intet overlap mellem tekster eller mellem tekst og diagram/knap (tolerance 2 px for linjehøjde i samme overskrift), ingen tal brudt over to linjer. Fejler tjekket, bliver opslaget ikke en del af ugepreviewet.
5. **Screenshots**: Playwright-script der tager mobil-screenshots af live-sider til shorts.
6. **Higgsfield**: kun covers/hook-frames, efter promptreglerne under Stil.
7. **Musik**: lægges ind i MP4'en fra en lille mappe med rettighedsfri musik (`social/audio/`), da trending lyd normalt ikke kan sættes på via API.
8. **Ugepreview**: `social/out/<uge>/preview.html` viser alle 14 opslag i rækkefølge med caption, kilder og godkend/afvis pr. opslag. Kun godkendte opslag kommer på planlægningslisten (`schedule.json`), som Grok bruger i Zernio.
9. **Playbook** (`social/PLAYBOOK.md`): Groks faste instruks – stil, søjler, ugeplan, regler, brief-skema, kilderegister, og hvordan briefen afleveres.

**Daglig elpris-story (script, uden ugebatch):** morgendagens priser findes først ca. kl. 13. Et script i `social/` kører efter sitets eksisterende 13:45-elpris-rutine (`src/refresh_elpris.py`), læser `src/elpris_data.json` og renderer storyen for DK1 og DK2. Exit 2/3 fra rutinen = ingen story den dag (ingen gætte-tal). Story-PNG'en lægges i `social/out/stories/<dato>/`. Den uploades enten af scriptet eller af Grok (bygger vælger efter, hvad Zernio-adgangen tillader). Link-sticker kan normalt ikke sættes via API, så storyen siger "Se alle priser på energitjekket.dk/elpris".

**Fredags-reel:** "Lørdagens billigste timer" (lørdagens priser kendes fredag eftermiddag), renderet af samme script fredag efter 13:45, ikke i ugebatchen.

## Hvad Casper har besluttet

- Ingen voiceover; dansk tekst på skærmen.
- Målgruppe og mål: danske boligejere med høje regninger → trafik til siden.
- Stil A.
- 60/40 varmepumpe/solceller i vinterhalvåret.
- 2 opslag om dagen, 7 dage om ugen.
- Anti-mål: opdigtede tal og påtrængende salgssnak.
- Ingen overlap mellem tekster; tal skal stå inde i kasserne.
- Grok analyserer, indsamler data og skriver briefen; Claude laver opslagene; Grok planlægger i Zernio.
- Casper godkender opslagene i starten.
- Elpris-storyen laves af et script ud fra sitets elpris-data.
- @energitjekket findes og er koblet på Zernio.
- Alt ligger i energitjekket-repoet under `social/`.

## Overladt til den, der bygger (Claudes forslag, kan ændres)

- Den præcise ugeplan, tidspunkter (07:30/19:30), formatlængder, carousel-længde 5–7 slides.
- Elpris som story i stedet for feed (holder gridet varieret), plus fredags-reel med lørdagens priser.
- Streng talvalidering mod et kilderegister i stedet for fritekst-kilder.
- Higgsfields begrænsede rolle og prompt-regler.
- Rettighedsfri musik bagt ind i MP4'en.
- Animationsstil, skabelonernes præcise layout, JSON-skemaets felter.
- Hashtag-sæt og caption-længde.
