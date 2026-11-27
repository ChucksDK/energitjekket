# -*- coding: utf-8 -*-
"""Indhold: kilder, nationale fakta og lokale afsnit pr. by. Alle tal har en kilde (S[...])."""

S = {
 # nationale kilder
 "elafgift": ("Skatteministeriet: satser i elafgiftsloven 2026-2027", "https://skm.dk/tal-og-metode/satser/satser-og-beloebsgraenser-i-lovgivningen/elafgiftsloven"),
 "elafgift_lov": ("Retsinformation: lov nr. 1775 af 29/12 2025", "https://www.retsinformation.dk/eli/lta/2025/1775/pdf"),
 "vpp_faq": ("SparEnergi: spørgsmål til Varmepumpepuljen", "https://sparenergi.dk/privat/soeg-tilskud/varm-op-til-soege-tilskud-til-en-varmepumpe/faq-varmepumpepulje"),
 "vpp_ens": ("Energistyrelsen: Varmepumpepuljen åbner igen (2. juli 2026)", "https://ens.dk/presse/varmepumpepuljen-aabner-igen-200-mio-kr-skal-hjaelpe-flere-vaek-fra-olie-og-gas"),
 "hvfradrag": ("Skattestyrelsen: håndværkerfradrag 2026", "https://skat.dk/borger/fradrag/servicefradrag/haandvaerkerfradrag"),
 "hvbeting": ("Skattestyrelsen: betingelser for håndværkerfradrag", "https://skat.dk/borger/fradrag/servicefradrag/generelle-betingelser"),
 "se_vp": ("SparEnergi: hvilken type varmepumpe skal du vælge?", "https://sparenergi.dk/privat/tid-til-skifte-varmekilde/hvilken-type-varmepumpe-skal-du-vaelge"),
 "se_sol": ("SparEnergi: få gratis strøm fra solceller", "https://sparenergi.dk/privat/skal-du-renovere-din-bolig/faa-gratis-stroem-fra-solceller"),
 "es_sol": ("Energisparer.dk: solceller pris 2026 (kommerciel kilde, okt. 2026)", "https://energisparer.dk/solceller/pris/"),
 "dmi": ("DMI: nedbør og sol i Danmark", "https://www.dmi.dk/klima/temaforside-klimaet-frem-til-i-dag/nedbor-og-sol-i-danmark"),
 "plandata": ("Plandata.dk: kort over fjernvarmeområder", "https://kort.plandata.dk/spatialmap"),

 # nye kilder (undersider, okt. 2026)
 "br18_179": ("Bygningsreglementet BR18 § 179 (gengivet på Jurabibliotek.dk)", "https://www.jurabibliotek.dk/bygningsreglementet/paragraf/179"),
 "vej_byg": ("Vejle Kommune: enfamiliehus (byggesag, forhåndsdialog og gebyrer 2026)", "https://www.vejle.dk/da/service-og-selvbetjening/borger/bolig-byggeri-og-forsyning/byg-om-eller-byg-nyt/enfamiliehus/"),
 "aal_ve": ("Aalborg Kommune: solcelle- og vindmølleprojekter (opdateret 30/9 2026)", "https://www.aalborg.dk/om-kommunen/udvikling-og-projekter/baeredygtig-kommune/klima/solcelle-og-vindmoelleprojekter-i-aalborg-kommune/"),
 "aal_forsyning": ("Aalborg Forsyning: fremtidens fjernvarme (Norbis Park)", "https://aalborgforsyning.dk/vores-ansvar/fremtidens-fjernvarme/"),
 "verdo_omr": ("Verdo: nye fjernvarmeområder", "https://www.verdo.com/dk/privat/fjernvarme/omraader/"),
 "ft_pris": ("Forsyningstilsynet: fjernvarmepriser jan. 2026", "https://forsyningstilsynet.dk/analyser-og-tal/forbrugerpriser/fjernvarmepriser"),
 "wg_pris": ("Wattguiden: fjernvarmepris pr. værk", "https://wattguiden.dk/fjernvarme/pris"),
 "bolius_varme": ("Bolius: pris på opvarmningsformer", "https://www.bolius.dk/det-koster-de-forskellige-opvarmningsformer-887"),
 "ean_udtr": ("Energiankenævnet: udtrædelsesgodtgørelse", "https://energianke.dk/temaer/fjernvarme/udtraedelsesgodtgoerelse"),
 "es_vp": ("Energisparer.dk: varmepumpe pris 2026 (kommerciel kilde, okt. 2026)", "https://energisparer.dk/varmepumpe/pris/"),
 "se_vpp": ("SparEnergi: søg tilskud til en varmepumpe (5 krav)", "https://sparenergi.dk/privat/soeg-tilskud/varm-op-til-soege-tilskud-til-en-varmepumpe"),
 "vpp_puljer": ("Statens tilskudspuljer: Varmepumpepuljen (redigeret 4/8 2026)", "https://www.statens-tilskudspuljer.dk/klima-energi-og-forsyningsministeriet/energistyrelsen/42"),
 "vpp_tekniq": ("TEKNIQ 13/10 2026: Husk varmepumperne i Finansloven", "https://www.tekniq.dk/nyheder/tekniq-husk-varmepumperne-i-finansloven/"),
 "evida_afk": ("Evida: Afkoblingspuljen for 2026 er åben", "https://evida.dk/nyheder/afkoblingspulje-2026/"),
 "ean_fast": ("Energiankenævnet: spørgsmål om varme", "https://energianke.dk/ofte-stillede-spoergsmaal/varme"),
 "fo_samtykke": ("Forbrugerombudsmanden: indhentelse af samtykke", "https://forbrugerombudsmanden.dk/alle-emner/uanmodede-henvendelser/indhentelse-af-samtykke"),
 # lokale kilder
 "kol_sol": ("Kolding Kommune: solcelleanlæg og solfangere", "https://www.kolding.dk/erhverv/byggeri-og-ejendom/solcelleanlaeg-og-solfangere"),
 "kol_fv": ("Kolding Kommune: fjernvarme- og naturgasområder", "https://www.kolding.dk/borger/miljoe-natur-og-klima/varme-og-energi/fjernvarme-og-naturgasomraader"),
 "kol_chr": ("Fællesavisen 7/1 2026: Naturgas-forbrugere siger nej tak til fjernvarme", "https://christiansfeld-avis.dk/2026/01/07/naturgas-forbrugere-siger-nej-tak-til-fjernvarme/"),
 "vej_fv": ("Vejle Kommune: kan jeg få fjernvarme i min bolig? (opdateret 16/3 2026)", "https://www.vejle.dk/da/service-og-selvbetjening/borger/bolig-byggeri-og-forsyning/forsyning-og-energi/varme/fjernvarme/kan-jeg-faa-fjernvarme-i-min-bolig/"),
 "vej_sol": ("Vejle Kommune: solenergi", "https://www.vejle.dk/da/service-og-selvbetjening/borger/bolig-byggeri-og-forsyning/forsyning-og-energi/groen-energi/solenergi/"),
 "esb_fv": ("DIN Forsyning: om vores varme", "https://dinforsyning.dk/da-dk/varme/om-vores-varme"),
 "esb_sol": ("Esbjerg Kommune: kommuneplan, vedvarende energi (VE 11-12)", "https://kommuneplan.esbjerg.dk/hovedstruktur/sektorer/vedvarende-energi-ve/"),
 "ode_sol": ("Odense Kommune: solceller", "https://www.odense.dk/borger/byggeri/byggetilladelse-og-godkendelse-af-byggeri/skilte-facader-solceller-antenner-og-skorstene/solceller"),
 "ode_fv": ("Fjernvarme Fyn: nye områder", "https://www.fjernvarmefyn.dk/overvejer-du-fjernvarme/nye-omraader/"),
 "aal_fv": ("Aalborg Kommune: varmeplan (opdateret 17/12 2025)", "https://www.aalborg.dk/om-kommunen/politikker-strategier-og-planer/varmeplan/"),
 "aal_byg": ("Aalborg Kommune: enfamiliehus og sommerhus (byggeri)", "https://www.aalborg.dk/mit-liv/min-bolig/byggeri/enfamiliehus-og-sommerhus/"),
 "ran_sol": ("Randers Kommune: solceller og solfangere (opdateret 29/9 2026)", "https://www.randers.dk/borger/bolig/byggeri/foer-du-bygger/hvad-skal-du-i-gang-med/solceller-og-solfangere/"),
 "ran_fv": ("TV2 Østjylland: 580 husstande klar til fjernvarme (Spentrup)", "https://www.tv2ostjylland.dk/randers/580-husstande-klar-til-fjernvarme-08817"),
 "hor_sol": ("Horsens Kommune: solceller på dit tag", "https://horsens.dk/bolig/byggeriogejendom/solceller"),
 "hor_fv": ("Dansk Fjernvarme 17/3 2026: 10 års rejse til grøn forsyningssikkerhed (Fjernvarme Horsens)", "https://danskfjernvarme.dk/aktuelt/nyheder/2026/10-aars-rejse-til-groen-forsyningssikkerhed"),
 # lokale kilder, daglig by-rutine 26. okt. 2026 (Aarhus, Viborg)
 "aar_fv": ("Aarhus Kommune: fjernvarme (opdateret 4/6 2026)", "https://aarhus.dk/borger/bolig-byggeri-og-miljoe/for-grundejere/fjernvarme"),
 "aar_olie": ("Aarhus Kommune: skal du udskifte dit oliefyr? (opdateret 17/8 2023)", "https://aarhus.dk/borger/bolig-byggeri-og-miljoe/for-grundejere/fjernvarme/skal-du-udskifte-dit-oliefyr"),
 "aar_mr": ("Aarhus Kommune: miljørapport til forslag til Energiplan 2025-2045 (PDF, høring til 11/1 2026)", "https://deltag.aarhus.dk/sites/default/files/documents/Milj%C3%B8rapport%20Energiplan%202025-2045%20Aarhus%20Kommune_ver.1.0_0.pdf"),
 "aar_ff": ("Deltag Aarhus: Kredsløbs planforslag Fremtidens Fjernvarme (opdateret 16/3 2026)", "https://deltag.aarhus.dk/hoering/fremtidens-fjernvarme"),
 "aar_geo": ("Dansk Fjernvarme 26/6 2026: 111 MW geotermi på vej til Aarhus", "https://danskfjernvarme.dk/aktuelt/nyheder/2026/111-mw-geotermi-paa-vej-til-aarhus"),
 "aar_egaa": ("Aarhus Kommune 7/8 2026: screeningsafgørelse, 8 MW varmepumpe på Egå Renseanlæg (PDF)", "https://deltag.aarhus.dk/sites/default/files/documents/Screeningsfg%C3%B8relse_0.pdf"),
 "kredslob": ("Kredsløb: kundeservice fjernvarme", "https://www.kredslob.dk/kundeservice-og-drift/kundeservice-fjernvarme"),
 "vib_sol": ("Viborg Kommune: solceller (opdateret 13/10 2026)", "https://viborg.dk/borger/byggeri-og-bolig/byg-nyt-eller-byg-om/solceller/"),
 "vib_byg": ("Viborg Kommune: når du vil bygge (opdateret 13/10 2026)", "https://viborg.dk/borger/byggeri-og-bolig/byg-nyt-eller-byg-om/naar-du-vil-bygge/"),
 "vib_ans": ("Viborg Kommune: søg byggetilladelse (opdateret 5/8 2026)", "https://viborg.dk/borger/byggeri-og-bolig/byg-nyt-eller-byg-om/naar-du-vil-bygge/soeg-byggetilladelse/"),
 "vib_vp": ("Viborg Kommune: varmeplan (opdateret 13/10 2026)", "https://viborg.dk/borger/byggeri-og-bolig/affald-energi-og-miljoe/energi/udfasning-af-olie-og-gas/varmeplan/"),
 "vib_strat": ("Viborg Kommune: Energistrategi for Viborg Kommune (endeligt vedtaget, PDF)", "https://viborg.dk/media/2t1dtyf0/energistrategi-for-viborg-kommune_endelig-vedtaget.pdf"),
 "vib_slip": ("Viborg Varme, Slip Gassen: projekter (status oktober 2026)", "https://slipgassen.dk/projekter/"),
 "vib_lise": ("Viborg Kommune 7/9 2026: screeningsafgørelse, fjernvarme ved Liseborg (PDF)", "https://viborg.dk/media/fxcfgnj5/omraade-ved-liseborg-screeningsafgoerelse-for-projekt-for-fjernvarmeforsyning-af-omraade-ved-liseborg-i-viborg.pdf"),
 "vib_budget": ("Viborg Varme 25/9 2025: budget og takstblad for 2026", "https://viborgvarme.dk/nyheder/budget-og-takster-for-2026/"),
 "vib_df": ("Dansk Fjernvarme 28/4 2026: Omsider er overskudsvarmen på vej til Viborg", "https://danskfjernvarme.dk/aktuelt/nyheder/2026/omsider-er-overskudsvarmen-paa-vej-til-viborg"),
}

SERVICES = {
 "solceller": {
   "slug": "solceller", "name": "Solceller", "name_lc": "solceller",
   "hub_title": "Solceller i din by: lokale regler, priser og tilbud",
   "service_type": "Formidling af tilbud på solcelleanlæg til private boliger",
 },
 "varmepumpe": {
   "slug": "varmepumpe", "name": "Luft til vand-varmepumpe", "name_lc": "luft til vand-varmepumpe",
   "hub_title": "Luft til vand-varmepumpe: fjernvarme, tilskud og tilbud i din by",
   "service_type": "Formidling af tilbud på luft til vand-varmepumper til private boliger",
 },
}

# Rækkefølge = rækkefølge i linkblokke
CITIES = {
 "kolding": {
  "name": "Kolding", "kommune": "Kolding Kommune",
  "sol_intro": "Overvejer du solceller på dit hus i Kolding? Her får du det korte overblik over, hvad Kolding Kommune kræver, hvad et anlæg typisk koster i 2026, og hvordan du får et uforpligtende tilbud.",
  "sol_facts": [
    ("På enfamiliehuse, sommerhuse og rækkehuse kan solceller på den eksisterende tagflade <strong>ofte sættes op uden tilladelse</strong> fra Kolding Kommune.", ["kol_sol"]),
    ("Du skal kontakte kommunen, hvis huset er omfattet af en lokalplan, byplanvedtægt eller deklaration med regler om solceller, tagmateriale eller refleksioner. Det samme gælder, hvis bygningen er bevaringsværdig eller fredet, hvis panelerne skal vinkles op på stativer, eller hvis anlægget skal stå på jorden.", ["kol_sol"]),
    ("Ligger ejendommen i landzone, og kræver anlægget byggetilladelse, skal du også have landzonetilladelse.", ["kol_sol"]),
    ("Kræver anlægget ikke tilladelse, skal du sende anlæggets areal og ydelse til kommunen (byggesag@kolding.dk), så det kan blive registreret i BBR.", ["kol_sol"]),
  ],
  "sol_faq": [
    ("Skal jeg søge byggetilladelse til solceller i Kolding?", "Som regel ikke, hvis anlægget ligger på den eksisterende tagflade af et enfamiliehus, rækkehus eller sommerhus. Du skal dog henvende dig til Kolding Kommune, hvis der er en lokalplan, deklaration eller bevaringsværdi, hvis panelerne vinkles op, eller hvis anlægget står på jorden.", ["kol_sol"]),
    ("Hvordan bliver mit solcelleanlæg registreret i BBR i Kolding?", "Kræver anlægget ikke tilladelse, beder Kolding Kommune dig sende oplysninger om anlæggets areal og ydelse til byggesag@kolding.dk, så det kan indberettes i BBR.", ["kol_sol"]),
  ],
  "vp_intro": "Skal dit olie- eller gasfyr skiftes ud i Kolding? Før du vælger en luft til vand-varmepumpe, er det vigtigste spørgsmål, om der kommer fjernvarme til din adresse. Her er status, tilskudsreglerne og de typiske priser.",
  "vp_facts": [
    ("Kolding Kommune har et kort, hvor du kan se, om din ejendom ligger i et område med fjernvarme eller naturgas, har <strong>tilslutningspligt</strong> eller er omfattet af et forbud mod elvarme.", ["kol_fv"]),
    ("Forbuddet mod elvarme gælder elvarme som primær opvarmning i fjernvarmeområder. Kommunen oplyser, at der er undtagelser og mulighed for dispensation, bl.a. for eldrevne varmepumper. Spørg kommunen, før du bestiller.", ["kol_fv"]),
    ("Tilslutningspligt betyder, at du skal betale tilslutningsafgift og en årlig afgift. Du har ikke pligt til at aftage varmen, og i nye områder pålægges der ikke længere tilslutningspligt.", ["kol_fv"]),
    ("I <strong>Christiansfeld</strong> er udvidelsen af fjernvarmen til naturgaskunderne opgivet. Ved fristen i december 2025 var der langt fra nok bindende tilsagn. For de berørte boliger er en individuel løsning som en varmepumpe derfor det realistiske alternativ.", ["kol_chr"]),
  ],
  "vp_faq": [
    ("Kommer der fjernvarme til mit område i Kolding Kommune?", "Tjek kommunens kort over fjernvarme- og naturgasområder. I Christiansfeld er udvidelsen til naturgaskunderne opgivet, fordi der ikke kom nok bindende tilsagn.", ["kol_fv", "kol_chr"]),
    ("Må jeg sætte en varmepumpe op, hvis der er forbud mod elvarme i mit område?", "Kolding Kommune oplyser, at der er undtagelser og mulighed for dispensation fra forbuddet, bl.a. for eldrevne varmepumper. Kontakt kommunens Team Energi, før du bestiller.", ["kol_fv"]),
  ],
 },
 "vejle": {
  "name": "Vejle", "kommune": "Vejle Kommune",
  "sol_intro": "Solceller på taget i Vejle: her kan du se, hvilke regler der gælder for dit hus, hvad du kan forvente at betale i 2026, og hvordan du sammenligner tilbud fra installatører.",
  "sol_facts": [
    ("Vejle Kommunes egne retningslinjer for solenergi handler mest om <strong>store anlæg</strong>. De er som udgangspunkt lokalplanpligtige, hvis de producerer mere end til eget forbrug. Skillelinjen er typisk 1 ha.", ["vej_sol"]),
    ("Et mindre solcelleanlæg i landzonen kræver landzonetilladelse, når det sidestilles med ny bebyggelse. Normalt kan det kun tillades i tilknytning til eksisterende bebyggelse.", ["vej_sol"]),
    ("På parcelhusets tag gælder de generelle regler: kommunen skal godkende placeringen, hvis lokalplaner, fredninger eller servitutter regulerer det. Anlæg på jorden skal altid godkendes.", ["se_sol"]),
  ],
  "sol_faq": [
    ("Hvad gælder for solceller på jorden i Vejle Kommune?", "Solceller på jorden skal altid godkendes af kommunen. I landzonen kræver mindre anlæg landzonetilladelse, og de skal normalt placeres i tilknytning til eksisterende bebyggelse.", ["vej_sol", "se_sol"]),
    ("Kan jeg få solceller, hvis mit hus i Vejle ligger i et lokalplanområde?", "Ofte ja, men lokalplanen kan have krav til fx tagmateriale eller placering. Så skal kommunen godkende placeringen, inden du går i gang.", ["se_sol"]),
  ],
  "vp_intro": "Varmepumpe eller fjernvarme i Vejle? Vejle Kommune er midt i en udrulning af fjernvarme, og det afgør både, om en luft til vand-varmepumpe er det rigtige valg, og om du kan få tilskud.",
  "vp_facts": [
    ("Vejle Kommunes fjernvarmekort viser tre farver. <strong>Gul</strong> betyder fjernvarme i dag. <strong>Blå</strong> betyder, at selskaberne er i gang med at udrulle eller forventer at gøre det, hvis der er nok tilmeldte. <strong>Grøn</strong> betyder, at der er potentiale, og at der regnes på det.", ["vej_fv"]),
    ("Kommunen har sendt breve til alle, der står med olie- eller gasfyr i BBR. Fjernvarmeselskaberne har <strong>frem til 2028</strong> til at udrulle. Et projektforslag tager 3-6 måneder at godkende, og selve udrulningen op til 18 måneder.", ["vej_fv"]),
    ("Må man installere en varmepumpe? Kommunens svar er ja, men overvej nøje, om det er værd at vente, til fjernvarmen er rullet ud i dit område. Står dit område ikke på kortet, er der ingen umiddelbare planer om fjernvarme.", ["vej_fv"]),
    ("Er der et godkendt projektforslag for fjernvarme i dit område, kan du ikke få tilskud til en varmepumpe. Størstedelen af fjernvarmen i Vejle Kommune er overskudsvarme leveret af TVIS.", ["vej_fv"]),
  ],
  "vp_faq": [
    ("Skal jeg vente på fjernvarme i Vejle eller købe en varmepumpe nu?", "Tjek din adresse på Vejle Kommunes fjernvarmekort. Er dit område gult, blåt eller grønt, anbefaler kommunen at overveje nøje, om det er værd at vente. Står det ikke på kortet, er der ingen umiddelbare planer, og så er en varmepumpe typisk det oplagte valg.", ["vej_fv"]),
    ("Kan jeg få tilskud til varmepumpe i Vejle?", "Kun hvis du bor i et område med individuel varmeforsyning. Er der et godkendt projektforslag for fjernvarme i dit område, kan du ikke søge. Varmepumpepuljen giver 27.000 kr. og lukker senest 30. november 2026.", ["vej_fv", "vpp_faq"]),
  ],
 },
 "esbjerg": {
  "name": "Esbjerg", "kommune": "Esbjerg Kommune",
  "sol_intro": "Solceller i Esbjerg: Esbjerg Kommune har usædvanligt konkrete retningslinjer for, hvordan et anlæg skal se ud på taget. Her er reglerne, priserne og vejen til et uforpligtende tilbud.",
  "sol_facts": [
    ("Ifølge kommuneplanen skal solenergianlæg på bygninger samles i én <strong>rektangulær eller kvadratisk form</strong>, helst på én tagflade, og følge tagets hældning.", ["esb_sol"]),
    ("På tegl- og skifertage bør to rækker tagsten ved tagets top og bund og tre rækker langs siderne holdes fri. På andre tage bør der være mindst 50 cm til top, bund og sider. Stråtage, kviste og valme skal holdes fri.", ["esb_sol"]),
    ("På ejendomme med en <strong>bevarende lokalplan eller deklaration</strong> kan der som udgangspunkt ikke opsættes solenergianlæg. Det samme gælder bygninger med høj bevaringsværdi (SAVE 1-3) i et udpeget kulturmiljø.", ["esb_sol"]),
    ("Kommunen kræver antirefleksbehandling, hvis der er risiko for genskin over for naboer og trafikanter. Det kan også være relevant tæt på Esbjerg Lufthavn.", ["esb_sol"]),
  ],
  "sol_faq": [
    ("Hvordan skal solceller placeres på taget i Esbjerg?", "Esbjerg Kommunes kommuneplan siger, at anlægget skal være én samlet rektangulær eller kvadratisk flade og følge tagets hældning. På tegl og skifer friholdes to rækker sten ved top og bund og tre langs siderne. Stråtag, kviste og valme skal holdes fri.", ["esb_sol"]),
    ("Kan jeg få solceller på et bevaringsværdigt hus i Esbjerg?", "Ligger huset i en bevarende lokalplan, eller er det i SAVE 1-3 i et kulturmiljø, kan der som udgangspunkt ikke gives tilladelse. Ved andre bevaringsværdige bygninger vurderer kommunen hver sag konkret.", ["esb_sol"]),
  ],
  "vp_intro": "Luft til vand-varmepumpe i Esbjerg: I Esbjerg by får de fleste fjernvarme fra DIN Forsyning, som selv kører store havvandsvarmepumper. Her kan du se, hvornår en varmepumpe i dit eget hus giver mening, og hvad den koster.",
  "vp_facts": [
    ("DIN Forsyning leverer fjernvarme til Esbjerg by, herunder bl.a. Sædding, Hjerting, Tarp og Tjæreborg, samt til Varde, Alslev og Nordby på Fanø. Det er <strong>ca. 25.500 husstande</strong> i alt.", ["esb_fv"]),
    ("Det kulfyrede Esbjergværk blev taget ud af drift i sommeren 2024. Siden december 2024 har to <strong>havvandsvarmepumper</strong> på Esbjerg Havn (op til 70 MW) leveret grundlast sammen med en elkedel og en fliskedel.", ["esb_fv"]),
    ("Bor du uden for fjernvarmenettet, fx i landsbyerne eller i landzone med oliefyr, gasfyr eller elvarme, er en luft til vand-varmepumpe typisk det oplagte grønne alternativ. Her kan du også søge tilskud.", ["esb_fv", "vpp_faq"]),
  ],
  "vp_faq": [
    ("Kan jeg få fjernvarme i stedet for en varmepumpe i Esbjerg?", "Det afhænger af adressen. DIN Forsyning dækker Esbjerg by med bl.a. Sædding, Hjerting, Tarp og Tjæreborg. Tjek din adresse hos DIN Forsyning eller på Plandata.dk, før du vælger varmepumpe.", ["esb_fv", "plandata"]),
    ("Hvorfor taler alle om varmepumper på Esbjerg Havn?", "DIN Forsyning har siden december 2024 haft havvandsvarmepumper på op til 70 MW i drift. Det er en del af fjernvarmen, ikke noget du selv køber. Din egen varmepumpe er relevant, hvis du bor uden for fjernvarmenettet.", ["esb_fv"]),
  ],
 },
 "odense": {
  "name": "Odense", "kommune": "Odense Kommune",
  "sol_intro": "Solceller i Odense: Odense Kommune har en enkel tommelfingerregel for parcel- og rækkehuse. Her får du reglerne, priserne for 2026, og hvordan du sammenligner tilbud.",
  "sol_facts": [
    ("Bor du i et enfamiliehus eller rækkehus, skal du <strong>ikke søge byggetilladelse</strong>, hvis solcellerne ligger plant på taget uden stativ.", ["ode_sol"]),
    ("Du skal dog søge tilladelse eller dispensation, hvis en lokalplan, byplanvedtægt eller tinglyst servitut siger noget om solceller eller tagets udseende, eller hvis huset er udpeget som bevaringsværdigt i kategori 4 eller lavere.", ["ode_sol"]),
    ("Kommunen anbefaler, at du orienterer de naboer, der kan blive generet af genskin. Anlægget skal registreres i BBR.", ["ode_sol"]),
  ],
  "sol_faq": [
    ("Skal jeg søge tilladelse til solceller på mit rækkehus i Odense?", "Nej, ikke hvis panelerne ligger plant på taget uden stativ, og der ikke er en lokalplan, byplanvedtægt, servitut eller bevaringsværdi (kategori 4 eller lavere), som regulerer det. Ellers skal du søge byggetilladelse eller dispensation.", ["ode_sol"]),
    ("Må jeg sætte solcellerne op på stativ på et fladt tag i Odense?", "Odense Kommunes undtagelse gælder kun for solceller, der ligger plant på taget uden stativ. Med stativ bør du spørge kommunens byggesagsafdeling, før du går i gang.", ["ode_sol"]),
  ],
  "vp_intro": "Luft til vand-varmepumpe i Odense og omegn: i selve Odense er fjernvarmen udbredt, så en varmepumpe er især relevant for huse uden for nettet. Her er, hvad du skal tjekke, hvad det koster, og hvilket tilskud du kan søge.",
  "vp_facts": [
    ("Fjernvarme Fyn skriver, at de fleste store bebyggede områder er ved at være forbundne, og at antallet af nye områder og kunder derfor er stabilt. Pr. oktober 2026 står <strong>Lundsmarken i Årslev</strong> som det område, der er åbent for tilmelding.", ["ode_fv"]),
    ("Bor du uden for fjernvarmen, fx i landzone eller i en mindre by med oliefyr, gasfyr eller elvarme, er luft til vand den mest almindelige løsning til et helårshus med radiatorer eller gulvvarme.", ["se_vp"]),
    ("Varmepumpepuljen giver kun tilskud, hvis boligen hverken ligger i et fjernvarmeområde eller et område med planlagt fjernvarme. Du kan tjekke din adresse hos Fjernvarme Fyn og på Plandata.dk.", ["vpp_faq", "plandata", "ode_fv"]),
  ],
  "vp_faq": [
    ("Kan jeg få fjernvarme i stedet for varmepumpe i Odense?", "Tjek din adresse hos Fjernvarme Fyn. Selskabet oplyser, at de fleste store bebyggede områder er ved at være forbundne. Ligger du uden for, er en luft til vand-varmepumpe det typiske valg.", ["ode_fv"]),
    ("Hvad koster en luft til vand-varmepumpe på Fyn?", "SparEnergi angiver typisk 100.000-130.000 kr. at etablere. Den endelige pris afhænger af huset, og om der skal ændres på radiatorer eller rør. Indhent derfor flere tilbud.", ["se_vp"]),
  ],
 },
 "aalborg": {
  "name": "Aalborg", "kommune": "Aalborg Kommune",
  "sol_intro": "Solceller i Aalborg: her er de regler, du skal tjekke for dit hus, hvad et anlæg typisk koster i 2026, og hvordan du får et uforpligtende tilbud.",
  "sol_facts": [
    ("Aalborg Kommune skriver, at alt byggeri altid skal overholde bygningsreglementet, lokalplanen og tinglyste servitutter, også når det ikke kræver tilladelse. Tjek først lokalplan eller byplanvedtægt for din ejendom.", ["aal_byg"]),
    ("Solceller, der ligger plant på taget af et enfamiliehus og overholder bygningsreglementets højde- og afstandskrav, kræver som udgangspunkt ikke byggetilladelse. Til gengæld skal kommunen godkende placeringen, hvis en lokalplan, fredning eller servitut regulerer den.", ["se_sol"]),
    ("Kræver dit projekt tilladelse, tilbyder Aalborg Kommune en <strong>STRAKS-ansøgning</strong>. Er ansøgningen fyldestgørende og lovlig, kvitterer kommunen med en tilladelse senest 3 uger efter, at sagen er oprettet.", ["aal_byg"]),
  ],
  "sol_faq": [
    ("Hvor hurtigt kan jeg få tilladelse i Aalborg, hvis mit anlæg kræver det?", "Med Aalborg Kommunes STRAKS-ansøgning giver kommunen tilladelse senest 3 uger efter, at sagen er oprettet, hvis ansøgningen er fyldestgørende og overholder reglerne.", ["aal_byg"]),
    ("Kan solceller betale sig i Aalborg?", "Det afhænger mest af, hvor meget af strømmen du selv bruger. SparEnergi angiver en samlet besparelse på typisk 2.500-7.000 kr. om året. Antallet af soltimer varierer mellem landsdelene. Ifølge DMI har Kattegat-regionen flest og det midterste Jylland færrest, men skygge og tagets retning betyder meget for dit konkrete tag.", ["se_sol", "dmi"]),
  ],
  "vp_intro": "Luft til vand-varmepumpe i Aalborg: Aalborg Kommune har meldt klart ud om, hvor fjernvarmen ikke kommer. Bor du uden for fjernvarmen, er en varmepumpe det oplagte næste skridt. Her er tilskud, priser og tilbud.",
  "vp_facts": [
    ("I varmeplanen fra 2022 blev <strong>21 områder</strong> screenet for fjernvarme. Fire havde potentiale (Ajstrup, Hostrup, St. Restrup og Nr. Kongerslev), men ved udgangen af 2025 gennemføres kun konverteringen af Ajstrup.", ["aal_fv"]),
    ("Kommunen skriver, at der på nuværende tidspunkt ikke er mulighed for yderligere udbygning med fjernvarme, og at borgere i områderne bør overveje andre grønne opvarmningsformer, fx varmepumper.", ["aal_fv"]),
    ("Står du uden for fjernvarmen med olie, gas eller elvarme, kan du søge 27.000 kr. fra Varmepumpepuljen, så længe der er midler, dog senest 30. november 2026.", ["vpp_faq", "vpp_ens"]),
  ],
  "vp_faq": [
    ("Kommer der fjernvarme til Hostrup, St. Restrup eller Nr. Kongerslev?", "Ifølge Aalborg Kommunes varmeplan (opdateret december 2025) gennemføres kun konverteringen af Ajstrup, og der vurderes ikke at være mulighed for yderligere udbygning lige nu.", ["aal_fv"]),
    ("Hvad skal jeg vælge, hvis jeg ikke kan få fjernvarme i Aalborg Kommune?", "Kommunen peger selv på andre grønne løsninger, fx varmepumper. Til et helårshus med radiatorer eller gulvvarme er luft til vand den mest almindelige type ifølge SparEnergi.", ["aal_fv", "se_vp"]),
  ],
 },
 "randers": {
  "name": "Randers", "kommune": "Randers Kommune",
  "sol_intro": "Solceller i Randers: Randers Kommune formulerer reglerne strammere end mange andre kommuner. Her kan du se, hvornår dit anlæg kræver byggetilladelse, hvad det koster, og hvordan du får tilbud.",
  "sol_facts": [
    ("Randers Kommune skriver, at du <strong>i udgangspunktet skal søge byggetilladelse</strong> til solceller og solfangere. Anlæg på fritliggende enfamiliehuse, dobbelthuse, rækkehuse, sommerhuse og sekundære bygninger er dog undtaget, hvis byggeretten i bygningsreglementets kapitel 8 ikke overskrides.", ["ran_sol"]),
    ("Du skal have tilladelse, hvis anlægget kommer tættere på skel end 2,50 m. Det gælder også anlæg på terræn, der er højere end 1,80 m og/eller større end 35 m².", ["ran_sol"]),
    ("Tjek lokalplanen for forbud mod blanke og reflekterende overflader, krav om tegl eller skifer, bevaringsbestemmelser eller krav om, at anlægget skal indbygges i taget.", ["ran_sol"]),
    ("På fredede bygninger tillades solceller ikke. På bygninger med bevaringsværdi 1-3 i kulturmiljøer gives der som udgangspunkt ikke tilladelse.", ["ran_sol"]),
  ],
  "sol_faq": [
    ("Kræver solceller byggetilladelse i Randers?", "Kommunen skriver, at det i udgangspunktet kræver byggetilladelse. Anlæg på enfamiliehuse, rækkehuse og lignende er dog undtaget, hvis byggeretten i BR18 kapitel 8 overholdes, og anlægget ikke kommer tættere end 2,50 m på skel.", ["ran_sol"]),
    ("Hvad skal en ansøgning om solceller i Randers indeholde?", "Mindst en kort beskrivelse af anlæggets størrelse, effekt og antal celler, en tegning over placeringen og en fuldmagt fra ejeren, hvis du ikke selv ejer huset. Du søger via Byg og Miljø.", ["ran_sol"]),
  ],
  "vp_intro": "Luft til vand-varmepumpe i Randers: Verdo udbygger fjernvarmen i flere byer i kommunen lige nu. Tjek derfor fjernvarmen først. Her får du overblikket, priserne og tilskudsreglerne.",
  "vp_facts": [
    ("I <strong>Spentrup</strong> er gravearbejdet til fjernvarme i gang. Over 580 husstande, ca. 60 % af byen, har tilmeldt sig. De første boliger forventes tilsluttet i november, og transmissionsledningen ventes færdig i efteråret 2027.", ["ran_fv"]),
    ("Bor du i et område, hvor fjernvarmen er besluttet eller planlagt, kan du ikke få tilskud fra Varmepumpepuljen. Tjek din adresse på Plandata.dk og hos Verdo, før du vælger.", ["vpp_faq", "plandata"]),
    ("Uden for fjernvarmen er luft til vand det typiske valg til et helårshus med vandbåren varme. SparEnergi angiver, at du kan spare op til 70 % i forhold til opvarmning med el eller gas.", ["se_vp"]),
  ],
  "vp_faq": [
    ("Kommer der fjernvarme til Spentrup?", "Ja. Ifølge TV2 Østjylland er Verdo i gang med at grave. Over 580 husstande har tilmeldt sig, de første tilslutninger ventes i november, og transmissionsledningen forventes færdig i efteråret 2027.", ["ran_fv"]),
    ("Kan jeg få tilskud til varmepumpe i Randers Kommune?", "Ja, hvis din bolig ligger uden for fjernvarmeområder og områder med planlagt fjernvarme, og du skifter fra olie, gas, el eller biokedel. Tilskuddet er 27.000 kr., og puljen lukker senest 30. november 2026.", ["vpp_faq"]),
  ],
 },
 "horsens": {
  "name": "Horsens", "kommune": "Horsens Kommune",
  "sol_intro": "Solceller i Horsens: Horsens Kommune giver lige nu gratis adgang til et uvildigt beregningsværktøj. Her er det, reglerne for dit tag og de typiske priser, så du kan sammenligne tilbud.",
  "sol_facts": [
    ("Horsens Kommune giver frem til <strong>15. februar 2027</strong> gratis adgang til værktøjet SolarSim. Det beregner anlægsstørrelse, tilbagebetalingstid, og om et batteri kan betale sig, ud fra din adresse og dit elforbrug.", ["hor_sol"]),
    ("Kommunen skriver, at et solcelleanlæg kan være omfattet af lokalplaner, servitutter, byplanvedtægter, naturbeskyttelsesloven og fredninger, selvom det ikke kræver byggetilladelse.", ["hor_sol"]),
    ("Er din ejendom optaget i kommuneplanen med <strong>bevaringsværdi 1-4</strong>, kan du ikke forvente at få tilladelse til solceller. På fredede bygninger må der som udgangspunkt ikke opsættes solceller.", ["hor_sol"]),
    ("Du skal altid anmelde anlægget til BBR med adresse, areal og samlet effekt i kW.", ["hor_sol"]),
  ],
  "sol_faq": [
    ("Hvordan regner jeg på solceller til mit hus i Horsens?", "Horsens Kommune tilbyder gratis adgang til SolarSim frem til 15. februar 2027. Du indtaster adresse og elforbrug og tegner tagfladerne, og så får du anlægsstørrelse, pris og tilbagebetalingstid. Brug resultatet, når du sammenligner tilbud.", ["hor_sol"]),
    ("Kan jeg få solceller på et bevaringsværdigt hus i Horsens?", "Har ejendommen bevaringsværdi 1-4 i kommuneplanen, skriver Horsens Kommune, at du ikke kan forvente at få tilladelse.", ["hor_sol"]),
  ],
  "vp_intro": "Varmepumpe i Horsens: Fjernvarme Horsens er gået fra 8.200 til 22.400 kunder på ti år, så start med at tjekke, om din adresse er dækket. Ligger du uden for fjernvarmen med olie, gas eller elvarme, er en luft til vand-varmepumpe det typiske valg. Her er priser, tilskud og tilbud.",
  "vp_facts": [
    ("Fjernvarme Horsens er gået fra <strong>8.200 til 22.400 kunder</strong> fra 2015 til 2025 og har lagt 470 km nye ledninger. De sidste kunder i det store udbygningsprojekt kunne tilslutte sig i 2023.", ["hor_fv"]),
    ("Selskabet forventer at nå 25.000 kunder i 2030, heriblandt flere erhvervskunder.", ["hor_fv"]),
    ("Står dit hus stadig med olie, gas eller elvarme uden for fjernvarmeområdet, er en luft til vand-varmepumpe det typiske valg, og så kan du søge tilskud fra Varmepumpepuljen.", ["vpp_faq", "se_vp"]),
  ],
  "vp_faq": [
    ("Kan jeg stadig få fjernvarme i Horsens?", "Fjernvarme Horsens har udbygget kraftigt og forventer 25.000 kunder i 2030. Kontakt selskabet eller tjek Plandata.dk for at se, om din adresse ligger i et fjernvarmeområde.", ["hor_fv", "plandata"]),
    ("Hvad koster en luft til vand-varmepumpe i Horsens?", "SparEnergi angiver typisk 100.000-130.000 kr. at etablere. Uden for fjernvarmeområder kan du søge 27.000 kr. i tilskud, før du skriver under.", ["se_vp", "vpp_faq"]),
  ],
 },
 "aarhus": {
  "name": "Aarhus", "kommune": "Aarhus Kommune", "updated": ("26. oktober 2026", "2026-10-26"),
  # Over 90 % af husene har fjernvarme: ingen selvstændig varmepumpe-byside. Varmepumpe-indholdet ligger på fjernvarme-eller-varmepumpe-siden.
  "vp_page": False,
  "sol_intro": "Solceller på dit hus i Aarhus: Aarhus Kommunes vejledning har konkrete grænser, fx 1 meter over flade tage og 1,8 meter for anlæg på jorden i byzone. Her er reglerne, priserne og vejen til et uforpligtende tilbud.",
  "sol_facts": [
    ("Solcelleanlæg må ikke sidde på bygninger, der står <strong>tættere end 2,5 meter på skel</strong> (5 meter i sommerhusområder ved nabo- og stiskel). Vil du tættere på, skal du søge byggetilladelse.", ["aar_sol"]),
    ("På flade tage vurderer Aarhus Kommune anlæg, der står <strong>mere end 1 meter over tagfladen</strong>, som en bygningslignende konstruktion, der kræver byggetilladelse.", ["aar_sol"]),
    ("Kommunen betragter ikke solceller som reflekterende materialer. Står der i lokalplanen, at solenergianlæg skal indgå i tagfladen, må panelerne på eksisterende huse sidde parallelt med taget og højst 15 cm over det.", ["aar_sol"]),
    ("Er huset optaget i kommuneplanen med <strong>bevaringsværdi 1-4</strong>, kan du ikke forvente tilladelse. Anlægget skal altid anmeldes til BBR med areal og samlet effekt i kW.", ["aar_sol"]),
  ],
  "sol_faq": [
    ("Kræver solceller på et parcelhus i Aarhus byggetilladelse?", "Som regel ikke, hvis huset står mindst 2,5 meter fra skel, højdekravene i bygningsreglementet overholdes, og hverken lokalplan, servitut eller bevaringsværdi siger andet. På flade tage kræver anlæg mere end 1 meter over tagfladen dog tilladelse.", ["aar_sol"]),
    ("Koster det gebyr at søge om solceller i Aarhus Kommune?", "Søger du sammen med byggetilladelsen til et nyt hus, opkræver kommunen ikke et selvstændigt gebyr for solcellerne. Søger du til et eksisterende hus eller et anlæg på terræn, opkræves et selvstændigt gebyr.", ["aar_sol"]),
  ],
  "vp_intro": "Varmepumpe eller fjernvarme i Aarhus? Over ni ud af ti huse i kommunen har fjernvarme, så en luft til vand-varmepumpe er kun aktuel for de huse, der ligger uden for nettet. Her er de lokale priser, planerne og tilskudsreglerne.",
  "vp_facts": [
    ("Kommunens forslag til Energiplan 2025-2045 udlægger <strong>varmeplansområder</strong>, der forventes at få fjernvarme inden for 12 år. Inden for dem kan du ikke få tilskud til en varmepumpe.", ["aar_mr"]),
    ("<strong>Lillering, Hørret og Fårup</strong> er undersøgt af Kredsløb, men der var ikke nok tilslutning blandt beboerne, og byerne udlægges derfor ikke som varmeplansområde.", ["aar_mr"]),
    ("Siden 1. januar 2019 har det ikke været muligt at pålægge ny tilslutningspligt til fjernvarme, men eksisterende tilslutningspligt gælder fortsat. Aarhus Kommune skriver, at du i dag frit kan vælge andre opvarmningsformer.", ["aar_mr", "aar_fv"]),
    ("Har du oliefyr, må du ifølge bygningsreglementet ikke installere et nyt oliefyr, når du kan få fjernvarme. Kommunen opfordrer alle med olie til at undersøge fjernvarmen først.", ["aar_olie"]),
  ],
  "vp_faq": [
    ("Kan jeg få tilskud til varmepumpe i Lillering, Hørret eller Fårup?", "Byerne udlægges ikke som varmeplansområde i forslaget til Energiplan 2025-2045, fordi der ikke var nok tilslutning til fjernvarme. Tilskuddet kræver dog også, at du skifter olie, gas, el eller biokedel ud, og at adressen ikke ligger i et fjernvarmeområde. Tjek Plandata.dk, før du søger.", ["aar_mr", "se_vpp", "plandata"]),
    ("Må jeg skifte fjernvarmen ud med en varmepumpe i Aarhus?", "Aarhus Kommune skriver, at du i dag frit kan vælge andre opvarmningsformer, men eksisterende tilslutningspligt fra før 2019 gælder fortsat. Spørg dit fjernvarmeværk, hvad det betyder for din adresse, og husk, at værket kan kræve udtrædelsesgodtgørelse, hvis du melder dig ud.", ["aar_fv", "aar_mr", "ean_udtr"]),
  ],
 },
 "viborg": {
  "name": "Viborg", "kommune": "Viborg Kommune", "updated": ("26. oktober 2026", "2026-10-26"),
  "sol_intro": "Solceller i Viborg: Viborg Kommunes regel er kort. Ligger panelerne parallelt med taget, og holder huset sig inden for højde- og afstandskravene, kræver det ingen byggetilladelse. Her er undtagelserne, priserne og vejen til et tilbud.",
  "sol_facts": [
    ("Kan bygningen med solcellerne <strong>parallelt med tagbeklædningen</strong> overholde højde- og afstandskravene i bygningsreglementet eller lokalplanen, kræver anlægget ingen byggetilladelse.", ["vib_sol"]),
    ("Sættes panelerne op på <strong>stativ</strong>, eller afviger bygningen fra højde- og afstandskravene, skal du have byggetilladelse, før anlægget sættes op.", ["vib_sol"]),
    ("Anlægget må ikke være reflekterende, og placeringen bør tilpasses, så den ikke generer naboerne. Kan reglerne ikke overholdes, vurderer kommunen sagen konkret, og det kan betyde en høring i området.", ["vib_sol"]),
    ("Anlæg på jorden og på landbrugs-, erhvervs- og driftsbygninger kræver altid byggetilladelse, og i landzone kan det også kræve landzonetilladelse.", ["vib_sol"]),
  ],
  "sol_faq": [
    ("Skal jeg søge byggetilladelse til solceller i Viborg?", "Ikke hvis panelerne ligger parallelt med tagbeklædningen, og bygningen overholder højde- og afstandskravene i bygningsreglementet eller lokalplanen. Stativer, anlæg på jorden og afvigelser fra kravene kræver tilladelse.", ["vib_sol"]),
    ("Hvordan registrerer jeg mine solceller i BBR i Viborg Kommune?", "Når anlægget er færdigt, skal det registreres i BBR. Viborg Kommune har en selvbetjening til at sende BBR-oplysninger om tekniske anlæg.", ["vib_sol"]),
  ],
  "vp_intro": "Luft til vand-varmepumpe i Viborg: lidt over halvdelen af husene i kommunen har fjernvarme, og Viborg Varme konverterer gasområder i Viborg by kvarter for kvarter. Tjek derfor din adresse først. Her er status, priserne og tilskudsreglerne.",
  "vp_facts": [
    ("Viborg Kommunes varmeplan er et kort over <strong>potentielle nye fjernvarmeområder</strong>. Planen bliver til virkelighed gennem konkrete projektforslag, og kortet ligger på kommunens Minimap.", ["vib_vp"]),
    ("I <strong>Planetkvarteret</strong> i Overlund (Merkurvej, Neptunvej og Saturnvej) er Viborg Varme i gang med at erstatte naturgassen med fjernvarme. Ved Liseborgvej starter etape 1 i november 2026, og Gråmejsevej og Sortmejsevej følger i februar 2027.", ["vib_slip", "vib_budget"]),
    ("Ligger dit hus i et område med planlagt fjernvarme, kan du ikke få tilskud fra Varmepumpepuljen. Kommunen skriver til boligejere med olie- og gasfyr i områder, der ikke forventes at få fjernvarme, og som kan få tilskud.", ["se_vpp", "vib_strat"]),
    ("Byrådets mål er, at alle oliefyr og naturgasfyr i kommunen er omstillet til vedvarende energi i 2030.", ["vib_strat"]),
  ],
  "vp_faq": [
    ("Kommer der fjernvarme til mit gasområde i Viborg?", "Se Viborg Varmes projektliste på slipgassen.dk. Planetkvarteret er i gang, Liseborgvej etape 1 starter i november 2026, og fx Engbakkevej/Nørresøvej Nord, Engelsborg og Lupinmarken er planlagt fra 2027 til 2030. Uden for projekterne kan du tjekke kommunens varmeplan på Minimap.", ["vib_slip", "vib_vp"]),
    ("Kan jeg få tilskud til varmepumpe i Viborg Kommune?", "Ja, hvis boligen ligger uden for fjernvarme og planlagt fjernvarme, og du skifter olie, gas, el eller biokedel ud. Tilskuddet er 27.000 kr., og puljen lukker senest 30. november 2026.", ["se_vpp", "vpp_faq"]),
  ],
 },
}


# Fælles (nationale) afsnit, gyldige for alle byer
SOL_PRICE_ROWS = [
  ("4 kWp (ca. 9-10 paneler)", "ca. 50.000-55.000 kr.", "ca. 3.800-4.200 kWh"),
  ("6 kWp (typisk parcelhus)", "ca. 90.000-95.000 kr.", "ca. 5.700-6.300 kWh"),
  ("10 kWp (stort forbrug/elbil)", "ca. 125.000-135.000 kr.", "ca. 9.500-10.500 kWh"),
]
VP_PRICE_ROWS = [
  ("Luft til vand-varmepumpe", "typisk 100.000-130.000 kr.", "op til 70 %"),
  ("Jordvarme (væske til vand)", "typisk 130.000-200.000 kr.", "op til 70 %"),
  ("Luft til luft (supplement)", "typisk 30.000-40.000 kr.", "op til 40 %"),
]

SOL_GENERAL_FAQ = [
  ("Hvad koster solceller i 2026?", "Ifølge Energisparer.dk (oktober 2026) koster et 6 kWp-anlæg til et parcelhus typisk ca. 90.000-95.000 kr. inkl. montering, et 4 kWp-anlæg ca. 50.000-55.000 kr. og et 10 kWp-anlæg ca. 125.000-135.000 kr. Prisen på dit hus kender du først, når du har tilbud.", ["es_sol"]),
  ("Hvad betyder den lave elafgift i 2026 og 2027 for solceller?", "Elafgiften er sat ned til 0,8 øre pr. kWh (ekskl. moms) i 2026 og 2027. Hver kWh, du selv bruger, sparer dig derfor mindre i de to år, og tilbagebetalingstiden bliver lidt længere. Efter gældende lov stiger afgiften igen fra 2028.", ["elafgift", "elafgift_lov"]),
  ("Kan jeg få håndværkerfradrag for solceller?", "Ja. Installation af solceller er omfattet af håndværkerfradraget med op til 9.000 kr. pr. person i 2026. Det gælder kun arbejdslønnen, ikke materialer, og du kan ikke både få pristillæg og håndværkerfradrag for samme anlæg.", ["hvfradrag", "hvbeting"]),
  ("Er I selv solcelleinstallatør?", "Nej. Vi er en formidlingstjeneste. Med dit samtykke sender vi din henvendelse til én udvalgt installatør i dit område, og det er installatøren, der giver tilbud og udfører arbejdet. Du får en e-mail med firmaets navn og CVR-nummer, så snart vi har sendt dine oplysninger.", []),
]
VP_GENERAL_FAQ = [
  ("Hvor meget kan jeg få i tilskud til en luft til vand-varmepumpe?", "Varmepumpepuljen giver 27.000 kr. til en helårsbolig, der skifter olie-, gas-, el- eller biokedel ud. Boligen må ikke ligge i et fjernvarmeområde eller et område med planlagt fjernvarme. Puljen er åben til 30. november 2026, eller til midlerne er brugt.", ["vpp_faq", "vpp_ens"]),
  ("Må jeg indhente tilbud, før jeg søger tilskud?", "Ja. Energistyrelsen skriver, at du gerne må kontakte installatører og indhente tilbud før ansøgningen. Du må bare ikke indgå en bindende aftale, bestille materialer, betale eller gå i gang, før du har fået tilsagn.", ["vpp_ens"]),
  ("Kan jeg få håndværkerfradrag for en varmepumpe?", "Kun hvis du ikke får tilskud fra Varmepumpepuljen til den samme varmepumpe. SparEnergi skriver, at du ikke må få støtte til samme projekt fra andre offentlige ordninger, herunder det grønne håndværkerfradrag. Uden tilskud er installationen omfattet af håndværkerfradraget med op til 9.000 kr. pr. person i 2026 for arbejdslønnen.", ["vpp_faq", "hvfradrag"]),
  ("Er I selv VVS- eller varmepumpeinstallatør?", "Nej. Vi er en formidlingstjeneste. Med dit samtykke sender vi din henvendelse til én udvalgt installatør i dit område, og det er installatøren, der giver tilbud og udfører arbejdet. Du får en e-mail med firmaets navn og CVR-nummer, så snart vi har sendt dine oplysninger.", []),
]

# Lokale kontakter (fra de samme kommune-/forsyningssider som ovenfor)
CONTACTS = {
 "kolding": {"sol": [("Kolding Kommune, Byggesag", "79 79 60 40 · byggesag@kolding.dk", "kol_sol")],
             "vp":  [("Kolding Kommune, Team Energi", "79 79 79 79 · energi@kolding.dk", "kol_fv")]},
 "vejle":   {"sol": [("Vejle Kommune", "76 81 00 00 · post@vejle.dk", "vej_sol")],
             "vp":  [("Vejle Kommune, Team Varme", "51 68 60 95 · jordogvarme@vejle.dk", "vej_fv")]},
 "esbjerg": {"sol": [("Esbjerg Kommune, Teknik & Miljø", "76 16 16 16", "esb_sol")],
             "vp":  [("DIN Forsyning (fjernvarme)", "74 74 74 74 · post@dinforsyning.dk", "esb_fv")]},
 "odense":  {"sol": [("Odense Kommune, Byggesag", "65 51 24 62 (man-tors kl. 10-12)", "ode_sol")],
             "vp":  [("Fjernvarme Fyn", "65 47 30 00 · kontakt@fjernvarmefyn.dk", "ode_fv")]},
 "aalborg": {"sol": [("Aalborg Kommune, Byggeri", "99 82 82 00 · byggeri@aalborg.dk", "aal_byg")],
             "vp":  [("Aalborg Kommune, Teknik og Miljø (varmeplan)", "99 31 20 00 · teknik.miljoe@aalborg.dk", "aal_fv")]},
 "randers": {"sol": [("Randers Kommune (Kontakt om byggeri)", "89 15 15 15", "ran_sol")],
             "vp":  [("Randers Kommune", "89 15 15 15", "ran_sol")]},
 "horsens": {"sol": [("Horsens Kommune", "76 29 29 29", "hor_sol")],
             "vp":  [("Horsens Kommune", "76 29 29 29", "hor_sol")]},
 "aarhus":  {"sol": [("Aarhus Kommune, Byggeri", "89 40 22 13 (man-fre kl. 9.30-11.30) · byggesag@mtm.aarhus.dk", "aar_sol")],
             "vp":  [("Kredsløb, kundeservice fjernvarme", "77 88 10 10 (hverdage kl. 9-14)", "kredslob")]},
 "viborg":  {"sol": [("Viborg Kommune, Teknik & Miljø, Byggeri", "87 87 52 52 · byggeri@viborg.dk", "vib_sol")],
             "vp":  [("Viborg Kommune, Teknik & Miljø, Strategi og Udvikling", "87 87 86 01 · strategiogudvikling@viborg.dk", "vib_vp"),
                     ("Viborg Varme", "87 27 58 00 · post@viborgvarme.dk", "vib_slip")]},
}

# ---------- daglig by-rutine 27. okt. 2026: Næstved og Silkeborg ----------
S.update({
 "nae_byg": ("Næstved Kommune: byggeri, herunder krav til opsætning af solcelleanlæg", "https://www.naestved.dk/bolig-og-miljoe/byg/byggeri"),
 "nae_fv": ("Næstved Kommune: spørgsmål og svar om fjernvarme (Varmeplan 2022-2030, opdateret 26/6 2025)", "https://www.naestved.dk/bolig-og-miljoe/byg/varme/fjernvarme"),
 "nae_vest": ("Næstved Fjernvarme: 1.300 ejendomme i Holsted Vest får ikke fjernvarme", "https://naestvedfjernvarme.dk/nyheder/pressemeddelelse-1300-ejendomme-i-naestved-holsted-vest-faar-ikke-fjernvarme"),
 "nae_syd": ("Næstved Fjernvarme: ca. 270 ejendomsejere i Holsted Syd får ikke fjernvarme (juni 2026)", "https://naestvedfjernvarme.dk/nyheder/pressemeddelelse-ca-270-ejendomsejere-i-naestved-holsted-syd-faar-ikke-fjernvarme"),
 "nae_nord": ("Næstved Fjernvarme 21/10 2026: tilslutningsprocent for område 50, Holsted Nord", "https://naestvedfjernvarme.dk/nyheder/tilslutningsprocent-for-omraade-50-holsted-nord-21-10-2026"),
 "nae_om": ("Næstved Fjernvarme: om os (varmekilder og historie)", "https://naestvedfjernvarme.dk/om-os"),
 "nae_lnn": ("TV2 ØST: Endnu et fjernvarmeprojekt kuldsejlet (Lille Næstved Nord)", "https://www.tv2east.dk/naestved/endnu-et-fjernvarmeprojekt-kuldsejlet"),
 "nae_pkn101": ("Planklagenævnet: afgørelse om solceller efter lokalplan nr. 101 i Næstved (gengivet på Lovguiden.dk)", "https://www.lovguiden.dk/dokument/planklagenaevnet/24-04622-afg%C3%B8relse-i-klagesag-om-n%C3%A6stved-kommunes-afslag-p%C3%A5-dispensation-fra-lokalplan-til-montering-af-solceller-p%C3%A5-taget-af-et-enfamiliehus-p%C3%A5-a1-n%C3%A6stved"),
 "nae_pkn102": ("Planklagenævnet 18/2 2026: solcelletagsten i Appenæs, lokalplan nr. 102 (gengivet på Lovguiden.dk)", "https://www.lovguiden.dk/dokument/planklagenaevnet/18-02-2026-afslag-paa-dispensation-til-solcelletagsten-i-bevaringsvaerdigt-kulturmiljoe-i-appenaes-25-09812"),
 "sil_byg": ("Silkeborg Kommune: ansøg om byggetilladelse, herunder solceller og gebyrer 2026", "https://silkeborg.dk/borger/bolig-og-byggeri/byg-i-silkeborg/ansoeg-om-byggetilladelse"),
 "sil_pkn": ("Planklagenævnet: solcelleanlæg efter lokalplan nr. 132.20, Øster Bordingvej, Silkeborg (gengivet på Lovguiden.dk)", "https://www.lovguiden.dk/dokument/planklagenaevnet/23-06894-afg%C3%B8relse-i-klagesag-om-silkeborg-kommunes-dispensation-fra-lokalplan-til-solcelleanl%C3%A6g-p%C3%A5-a1-silkeborg"),
 "sil_syd": ("Silkeborg Forsyning 10/4 2026: fjernvarme til byerne syd for Silkeborg", "https://www.silkeborgforsyning.dk/nyheder/fjernvarme-til-silkeborg-syd-det-sker-der-lige-nu"),
 "sil_voel": ("Silkeborg Forsyning 9/2 2026: Voel siger ja tak til fjernvarme", "https://www.silkeborgforsyning.dk/nyheder/voel-siger-ja-tak-til-fjernvarme"),
 "sil_faq": ("Silkeborg Forsyning: spørgsmål og svar om fjernvarme", "https://www.silkeborgforsyning.dk/fjernvarme/sp%C3%B8rgsm%C3%A5l-svar"),
 "sil_df": ("Dansk Fjernvarme 4/9 2026: Silkeborg indvier nye fjernvarmeanlæg", "https://danskfjernvarme.dk/aktuelt/nyheder/2026/silkeborg-indvier-nye-fjernvarmeanlaeg-med-markant-lavere-co2-udledning"),
 "sil_kontakt": ("Silkeborg Forsyning: kontakt", "https://www.silkeborgforsyning.dk/kontakt"),
})
CITIES["naestved"] = {
  "name": "Næstved", "kommune": "Næstved Kommune", "updated": ("27. oktober 2026", "2026-10-27"),
  "sol_intro": "Solceller i Næstved: følger panelerne tagets hældning på et enfamilie-, sommer- eller dobbelthus, skal du ikke søge. Men fredede og bevaringsværdige huse, tage med farvekrav i lokalplanen og grunde ved fortidsminder kræver altid tilladelse. Her er reglerne, priserne og vejen til et tilbud.",
  "sol_facts": [
    ("På <strong>enfamiliehuse, sommerhuse og dobbelthuse</strong> kan du sætte solceller op uden ansøgning, når anlægget følger tagets hældning, enten oven på taget eller nedfældet i det.", ["nae_byg"]),
    ("Du skal selv undersøge tinglyste servitutter og lokalplaner, og om de konstruktionsmæssige regler kan overholdes. Anlægget skal anmeldes til BBR med effekt og størrelse.", ["nae_byg"]),
    ("Fritstående anlæg, fredede og bevaringsværdige bygninger og arealer inden for <strong>fortidsmindebeskyttelseslinjen</strong> kræver altid byggetilladelse. Det samme gælder, hvis plangrundlaget stiller krav til tagets udseende eller farve.", ["nae_byg"]),
    ("I Appenæs forbyder lokalplan nr. 102 solcellepaneler. I februar 2026 stadfæstede Planklagenævnet kommunens afslag på solcelletagsten på et hus, der før havde stråtag.", ["nae_pkn102"]),
  ],
  "sol_faq": [
    ("Skal jeg søge om lov til solceller på mit hus i Næstved?", "Nej, ikke på et enfamilie-, sommer- eller dobbelthus, hvis panelerne følger tagets hældning, og ingen servitut eller lokalplan forbyder dem. Fredede og bevaringsværdige huse, tage med farve- eller udseendekrav i plangrundlaget og grunde inden for fortidsmindebeskyttelseslinjen kræver altid tilladelse.", ["nae_byg"]),
    ("Skal solceller i BBR i Næstved Kommune?", "Ja. Næstved Kommune skriver, at du selv skal anmelde anlægget til BBR, herunder anlæggets effekt og størrelse, også når det ikke kræver byggetilladelse.", ["nae_byg"]),
  ],
  "vp_intro": "Luft til vand-varmepumpe i Næstved: kun knap hvert tredje hus i kommunen har fjernvarme, og flere fjernvarmeprojekter i Næstved by er droppet, fordi for få tilmeldte sig. Mange gasfyr skal derfor skiftes på anden måde. Her er status, priserne og tilskudsreglerne.",
  "vp_facts": [
    ("Næstved Kommunes status for Varmeplan 2022-2030: fjernvarme er godkendt i <strong>Næstved by, Glumsø og Karrebæk</strong> og i den sydlige del af Fensmark. I <strong>Mogenstrup</strong> er fjernvarme undersøgt og kan ikke lade sig gøre.", ["nae_fv"]),
    ("I Holsted Vest (ca. 1.300 ejendomme) nåede tilmeldingen 51 % og i Holsted Syd 13 %, så Næstved Fjernvarme har opgivet begge områder. Kravet er mindst 60 % målt pr. kvadratmeter.", ["nae_vest", "nae_syd"]),
    ("Kommunen peger selv på egen varmepumpe, varmepumpe på abonnement eller en fælles løsning med naboerne, hvis der ikke kommer fjernvarme i dit område.", ["nae_fv"]),
    ("Varmepumpepuljen giver kun tilskud uden for fjernvarmeområder og områder med planlagt fjernvarme. Tjek din adresse på kommunens kort, før du søger.", ["se_vpp", "nae_fv"]),
  ],
  "vp_faq": [
    ("Får jeg fjernvarme i Holsted i Næstved?", "Ikke i Holsted Vest og Holsted Syd, hvor projekterne er droppet efter 51 % og 13 % tilmelding. I Holsted Nord (bl.a. Fagotvej, Galaksevej, Kometvej og Maglebjerg Alle) var tilslutningen 8 % den 21. oktober 2026. Fristen er 30. november 2026, og der skal 60 % til.", ["nae_vest", "nae_syd", "nae_nord"]),
    ("Kan jeg få tilskud til varmepumpe i Mogenstrup?", "Næstved Kommune skriver, at fjernvarme i Mogenstrup er undersøgt og ikke kan lade sig gøre. Skifter du olie, gas, el eller biokedel ud i en helårsbolig uden for fjernvarmeområder, kan du søge 27.000 kr. fra Varmepumpepuljen, der lukker senest 30. november 2026.", ["nae_fv", "se_vpp", "vpp_faq"]),
  ],
}
CITIES["silkeborg"] = {
  "name": "Silkeborg", "kommune": "Silkeborg Kommune", "updated": ("13. november 2026", "2026-11-13"),
  "sol_intro": "Solceller i Silkeborg: Silkeborg Kommune nævner fire tilfælde, hvor du skal have byggetilladelse, bl.a. anlæg på terræn og anlæg, der står for højt i forhold til skel. Ellers handler det om lokalplanen. Sagsbehandlingen er lige nu lang, så tjek reglerne først. Her er de, og priserne.",
  "sol_facts": [
    ("Byggetilladelse kræves, hvis anlægget står på <strong>terræn</strong>, sidder på fx erhvervsbygninger, skoler, ridehaller eller etageboliger, står for højt i forhold til afstanden til naboskel, eller hvis <strong>tagkonstruktionen skal ændres</strong> på grund af øget last.", ["sil_byg"]),
    ("Er ejendommen omfattet af en lokalplan, byplanvedtægt eller tinglyst servitut med regler om tagets materialer eller udseende, skal du søge dispensation. Planerne står på Silkeborglokalplaner.dk.", ["sil_byg"]),
    ("Fra 1. januar 2026 tager Silkeborg Kommune <strong>700 kr. i timen</strong> for at behandle byggesager, også for solceller på et eksisterende hus. Søger du solceller sammen med et nyt hus, er der intet særskilt gebyr.", ["sil_byg"]),
    ("Kommunen oplyser en forøget sagsbehandlingstid på ca. <strong>12-14 uger</strong> for bl.a. enfamiliehuse og rækkehuse, fordi der er kommet ekstraordinært mange ansøgninger.", ["sil_byg"]),
  ],
  "sol_faq": [
    ("Kræver solceller byggetilladelse i Silkeborg?", "Kun i fire tilfælde ifølge kommunen: anlæg på terræn, anlæg på bygninger som erhverv, skoler og etageboliger, anlæg der står for højt i forhold til naboskel, og anlæg der kræver ændring af tagkonstruktionen. Lokalplan og servitutter kan dog kræve dispensation.", ["sil_byg"]),
    ("Kan jeg få vejledning om solceller hos Silkeborg Kommune?", "Ja. Du kan booke en samtale på 20 minutter med en byggesagsbehandler, før du sender ansøgningen. Vær opmærksom på, at kommunen tager gebyr for forespørgsler og forhåndsdialoger om byggeloven.", ["sil_byg"]),
  ],
  "vp_intro": "Varmepumpe i Silkeborg: Silkeborg Forsyning lægger fjernvarme ud i en række byer uden for Silkeborg, bl.a. Virklund, Sejs-Svejbæk, Them, Salten og Voel. Bor du dér, skal du nok ikke have varmepumpe. Bor du uden for projekterne, er en luft til vand-varmepumpe et oplagt valg. Her er status, priserne og tallene.",
  "vp_facts": [
    ("Fjernvarmeprojektet <strong>Silkeborg Syd</strong> omfatter Virklund, Sejs-Svejbæk, Them og Salten. Gravearbejdet i byerne forventes at begynde i slutningen af 2026, og projektet ventes færdigt i første halvår af 2029. Knudlund er udgået på grund af lav tilmelding.", ["sil_syd", "sil_faq"]),
    ("I <strong>Voel</strong> rundede tilslutningen 59 % i februar 2026, over målet på 55 %. Gravearbejdet forventes at begynde i andet halvår af 2026 og vare ca. to år.", ["sil_voel"]),
    ("Ligger dit hus i et område med planlagt fjernvarme, kan du ikke få tilskud fra Varmepumpepuljen. Tjek adressen hos Silkeborg Forsyning og på Plandata.dk.", ["se_vpp", "plandata"]),
    ("Ifølge Silkeborg Forsyning har 70 % af husstandene med gasfyr i Silkeborg Syd tilmeldt sig fjernvarme, men kun 8 % af dem, der allerede har varmepumpe.", ["sil_syd"]),
  ],
  "vp_faq": [
    ("Kommer der fjernvarme til Them, Virklund og Sejs-Svejbæk?", "Ja. Projektet Silkeborg Syd er godkendt, og gravearbejdet i byerne forventes at begynde i slutningen af 2026. Silkeborg Forsyning venter at være helt færdig i første halvår af 2029. Den forventede tidsplan for hver by står på byens projektside.", ["sil_syd", "sil_faq"]),
    ("Hvad hvis mit gasfyr går i stykker, før fjernvarmen kommer?", "Er du tilmeldt fjernvarme i Silkeborg Syd, er du automatisk med i en garantiordning, så det nuværende anlæg kan repareres mod en egenbetaling på 2.500 kr.", ["sil_syd"]),
  ],
}
CONTACTS["naestved"] = {"sol": [("Næstved Kommune, Center for Teknik og Miljø", "55 88 61 10 · byggesag@naestved.dk", "nae_byg")],
                        "vp":  [("Næstved Fjernvarme", "55 72 56 65 · info@naestvedfjernvarme.dk", "nae_nord")]}
CONTACTS["silkeborg"] = {"sol": [("Silkeborg Kommune, Team Byg", "89 70 14 14 · byg@silkeborg.dk", "sil_byg")],
                         "vp":  [("Silkeborg Forsyning", "89 20 64 00", "sil_kontakt")]}

# ---------- daglig by-rutine 28. okt. 2026: Holbæk og Slagelse ----------
S.update({
 "hol_sol": ("Holbæk Kommune: solcelle- og solfangeranlæg (opdateret 5/7 2026)", "https://holbaek.dk/service-og-selvbetjening/bolig-og-byggeri/byggeri/solcelle-og-solfangeranlaeg"),
 "hol_disp": ("Holbæk Kommune, Udvalget for Klima og Miljø 22/11 2011: retningslinjer for dispensationer til solceller (PDF)", "https://cdn1.gopublic.dk/holbaekkommune/media/65468/kmu_solceller.pdf"),
 "hol_pkn": ("Planklagenævnet: afslag på dispensation til solceller efter lokalplan nr. 3.14 i Holbæk ophævet (gengivet på Lovguiden.dk)", "https://www.lovguiden.dk/dokument/planklagenaevnet/22-17349-oph%C3%A6velse-af-afslag-p%C3%A5-dispensation-til-solceller-p%C3%A5-grund-af-kommunes-forkerte-retsopfattelse"),
 "hol_fv": ("Holbæk Kommune: fjernvarmeplaner (opdateret 25/3 2026)", "https://holbaek.dk/service-og-selvbetjening/teknik-og-miljoe/klima-og-energi-/opvarmning-/fjernvarmeplaner"),
 "hol_ext": ("Holbæk Kommune 18/6 2026: fjernvarmetilmelding forlænges til maj 2027", "https://holbaek.dk/om-kommunen/nyheder-og-presse/nyheder/2026/jun/fjernvarmetilmelding-forlaenges-til-maj-2027"),
 "fors_hol": ("Fors: fjernvarme til Holbæk by (projektstatus og tilslutningsprocent pr. 4/8 2026)", "https://www.fors.dk/fjernvarme/fjernvarme-til-holbaek-by/"),
 "slg_sol": ("Slagelse Kommune: vil du opsætte solcelleanlæg?", "https://www.slagelse.dk/da/service-og-selvbetjening/bolig-og-byggeri/el-og-varme/solcelleanlaeg/"),
 "slg_adm": ("Slagelse Kommune: administrationsgrundlag for solfangere og solcelleanlæg (rev. 19/9 2022, PDF)", "https://www.slagelse.dk/media/a2mmalxi/solfanger-og-solcelleanlaeg-administrationsgrundlag-webtil.pdf"),
 "slg_fv": ("Slagelse Kommune: kan jeg få fjernvarme? (status pr. lokalområde)", "https://www.slagelse.dk/da/service-og-selvbetjening/bolig-og-byggeri/el-og-varme/fjernvarme/"),
 "slg_byg": ("Slagelse Kommune: få hjælp af en byggesagsbehandler", "https://www.slagelse.dk/da/service-og-selvbetjening/erhverv/erhvervsarealer-boligarealer-og-byggeri/faa-hjaelp-af-en-byggesagsbehandler/"),
 "env_ve": ("Envafors: vi leverer fjernvarme på 95 % VE (Slagelse og Korsør)", "https://www.envafors.dk/slagelse/klima---milj%c3%b8/vi-leverer-fjernvarme-p%c3%a5-95---ve"),
 "sn_skae": ("Sjællandske Nyheder 29/8 2026: forslag om fjernvarme til ca. 1.600 kunder i Skælskør", "https://www.sn.dk/art6631532/slagelse-kommune/nyhed/forsyningsselskab-vil-levere-fjernvarme-til-1600-kunder/"),
})
CITIES["holbaek"] = {
  "name": "Holbæk", "kommune": "Holbæk Kommune", "updated": ("28. oktober 2026", "2026-10-28"),
  "sol_intro": "Solceller i Holbæk: følger panelerne tagets hældning på en privat bolig, kræver de som udgangspunkt ikke byggetilladelse. Står de på stativ eller på jorden, skal du altid søge. Lokalplaner, deklarationer og grundejerforeningens vedtægter kan dog sætte grænser. Her er reglerne, priserne og vejen til et tilbud.",
  "sol_facts": [
    ("Solceller, der <strong>følger tagets hældning</strong> på en privat bolig eller en sekundær bygning, kræver som udgangspunkt ikke byggetilladelse i Holbæk Kommune.", ["hol_sol"]),
    ("Solceller på <strong>stativ på taget</strong> og alle anlæg <strong>på jorden</strong> kræver altid byggetilladelse. Står et jordanlæg i landzone, skal det også have landzonetilladelse.", ["hol_sol"]),
    ("Byplanvedtægter, lokalplaner, tinglyste deklarationer, grundejerforeningens vedtægter, fredning og naturbeskyttelseslinjer kan kræve dispensation. Den søges via Byg og Miljø eller på mail.", ["hol_sol"]),
    ("Kræver anlægget ikke tilladelse, skal du efter monteringen sende antal paneler, areal i m² og ydelse i kW til kommunen, så det kan registreres i BBR.", ["hol_sol"]),
  ],
  "sol_faq": [
    ("Skal jeg søge om lov til solceller på mit hus i Holbæk?", "Som udgangspunkt ikke, hvis panelerne følger tagets hældning. Står de på stativ eller på jorden, kræver det altid byggetilladelse. Tjek også lokalplan, deklarationer og grundejerforeningens vedtægter, før du bestiller.", ["hol_sol"]),
    ("Hvordan kommer mine solceller i BBR i Holbæk Kommune?", "Kræver anlægget ikke tilladelse, sender du efter monteringen antal paneler, areal i m² og ydelse i kW (ikke kWh) til byggesag@holb.dk. Kræver det tilladelse, sker registreringen gennem byggesagen.", ["hol_sol"]),
  ],
  "vp_intro": "Luft til vand-varmepumpe i Holbæk: under hvert tiende hus i kommunen har fjernvarme, og over 40 % har naturgas. Fjernvarmen i Holbæk by mangler stadig tilmeldinger, og kommunen har ingen planer om flere fjernvarmeområder. Her er status, priserne og tilskudsreglerne.",
  "vp_facts": [
    ("Fjernvarme til <strong>Holbæk by, etape 1</strong> blev godkendt i marts 2024, men kræver, at 70 % af det opvarmede areal tilmelder sig. Tilslutningen var 12,09 % den 4. august 2026, og arbejdet er forlænget til <strong>1. maj 2027</strong>.", ["hol_fv", "fors_hol", "hol_ext"]),
    ("Ud over Holbæk by har kommunen fjernvarme eller projekter i Jyderup, Mørkøv og St. Merløse. Holbæk Kommune skriver, at der ikke er planer om flere fjernvarmeområder.", ["hol_fv"]),
    ("Tilslutningspligt til naturgas bortfaldt ved en lovændring 10. maj 2022, også hvis den står i lokalplanen. Du må altså frit skifte gasfyret ud med en luft til vand-varmepumpe.", ["hol_fv"]),
    ("Varmepumpepuljen giver kun tilskud uden for fjernvarmeområder og områder med planlagt fjernvarme. Etape 1 i Holbæk by er godkendt til fjernvarme, så tjek din adresse, før du søger.", ["se_vpp", "fors_hol"]),
  ],
  "vp_faq": [
    ("Kommer der fjernvarme i Holbæk by?", "Det er uafklaret. Etape 1 er godkendt, men kræver 70 % tilslutning målt på opvarmet areal. Den 4. august 2026 var den 12,09 %, og arbejdet er forlænget til 1. maj 2027. Tilslutning koster 25.000 kr. til kampagnepris, indtil gravemaskinerne har været forbi, og derefter 50.000 kr.", ["fors_hol", "hol_ext"]),
    ("Skal jeg beholde mit gasfyr, hvis der står tilslutningspligt i lokalplanen?", "Nej. Holbæk Kommune skriver, at al tilslutningspligt til naturgas bortfaldt ved en lovændring 10. maj 2022, også selvom den står i lokalplaner og servitutter. Du kan frit skifte til fx en luft til vand-varmepumpe.", ["hol_fv"]),
  ],
}
CITIES["slagelse"] = {
  "name": "Slagelse", "kommune": "Slagelse Kommune", "updated": ("17. november 2026", "2026-11-17"),
  "sol_intro": "Solceller i Slagelse: ligger huset uden for en lokalplan, og overholder anlægget byggeretten i bygningsreglementet, skal du ikke søge. Stiller lokalplanen krav til taget, eller ligger huset i en bevarende lokalplan i Slagelse, Korsør eller Skælskør, skal du søge dispensation. Her er reglerne, priserne og vejen til et tilbud.",
  "sol_facts": [
    ("Uden lokalplan skal du ikke søge, hvis anlægget på taget <strong>overholder byggeretten</strong> i bygningsreglementet, bl.a. afstanden til skel. Anlægget skal indberettes til BBR, når det er sat op.", ["slg_adm", "slg_sol"]),
    ("Kræver lokalplanen en bestemt tagdækning, fx røde teglsten, skal du søge <strong>dispensation</strong>. Kommunen skriver, at den er indstillet på at give den efter en konkret vurdering, normalt efter naboorientering.", ["slg_adm"]),
    ("I de <strong>bevarende lokalplaner</strong> i Slagelse, Korsør, Skælskør og en række landsbyer vurderes hver sag konkret. Har bygningen SAVE-værdi 1-2, kan der normalt ikke dispenseres.", ["slg_adm"]),
    ("Anlæg på terræn i <strong>landzone</strong> kræver altid landzonetilladelse, uanset størrelse.", ["slg_adm"]),
  ],
  "sol_faq": [
    ("Skal jeg søge om lov til solceller på mit hus i Slagelse?", "Ikke hvis huset ligger uden for en lokalplan med krav til taget, og anlægget overholder byggeretten i bygningsreglementet. Ellers skal du søge byggetilladelse eller dispensation. Anlægget skal altid indberettes til BBR.", ["slg_adm", "slg_sol"]),
    ("Hvor lang tid tager en dispensation til solceller i Slagelse Kommune?", "Kommunens administrationsgrundlag siger mindst 6 uger, og længere, hvis naboer eller andre parter skal høres.", ["slg_adm"]),
  ],
  "vp_intro": "Varmepumpe i Slagelse: fjernvarmen bliver udbygget i Slagelse by, men i Skælskør, Vemmelev, Forlev og Sørbymagle er fjernvarmeprojekterne droppet. Dér skal husene have en individuel løsning – typisk en luft til vand-varmepumpe. Her er status, priserne og tilskudsreglerne.",
  "vp_facts": [
    ("<strong>Slagelse SV</strong> (mellem Idagårdsvej, Skælskørvej/Bjergbygade og Vestmotorvejen) nåede 61 % tilslutning og får fjernvarme. I <strong>Slagelse Øst</strong> (øst for Klosterbanken) er projektet planlagt til 2027 og kræver 60 % tilslutning.", ["slg_fv"]),
    ("Byrådet annullerede i 2025 fjernvarmeprojekterne i det centrale <strong>Skælskør</strong> og i <strong>Vemmelev og Forlev</strong>. Boligejerne dér kan igen søge tilskud til varmepumpe.", ["slg_fv"]),
    ("I Sørbymagle og Rosted er der ikke udsigt til et fællesvarmeprojekt, og Frølunde Fed er udlagt til individuel opvarmning.", ["slg_fv"]),
    ("Varmepumpepuljen giver kun tilskud uden for fjernvarmeområder og områder med planlagt fjernvarme. Tjek din adresse på kommunens kort, før du søger.", ["se_vpp", "slg_fv"]),
  ],
  "vp_faq": [
    ("Kommer der fjernvarme i Skælskør?", "Ikke foreløbig. Byrådet annullerede 26. maj 2025 projektet for det centrale Skælskør, fordi den forventede investering var steget fra under 300 til over 500 mio. kr. I august 2026 lå et nyt forslag om fjernvarme til ca. 1.600 kunder fra et andet selskab hos politikerne.", ["slg_fv", "sn_skae"]),
    ("Kan jeg få tilskud til varmepumpe i Vemmelev eller Forlev?", "Ja, hvis du opfylder de øvrige krav. Byrådet annullerede fjernvarmeprojektet i august 2025, så området igen er udlagt til individuel opvarmning. Varmepumpepuljen lukker senest 30. november 2026.", ["slg_fv", "se_vpp", "vpp_faq"]),
  ],
}
CONTACTS["holbaek"] = {"sol": [("Holbæk Kommune, Byggesag", "72 36 36 36 · byggesag@holb.dk", "hol_sol")],
                       "vp":  [("Holbæk Kommune, fjernvarmeplaner", "72 36 36 36", "hol_fv")]}
CONTACTS["slagelse"] = {"sol": [("Slagelse Kommune, Byggeri", "58 57 37 37 · teknik@slagelse.dk", "slg_byg")],
                        "vp":  [("Envafors (fjernvarme i Slagelse og Korsør)", "58 36 25 00 · kontakt@envafors.dk", "env_ve")]}

# ---------- daglig by-rutine 29. okt. 2026: Roskilde og Sønderborg ----------
S.update({
 "ros_byg": ("Roskilde Kommune: jeg vil bygge nyt hus eller bygge til mit hus (afsnit om solceller/solfangere)", "https://www.roskilde.dk/da-dk/service-og-selvbetjening/borger/bolig-og-byggeri/byggeri/byg-og-miljo-jeg-vil-bygge-nyt-hus-eller-bygge-til-mit-hus/"),
 "ros_lz": ("Roskilde Kommune: Landzonestrategi, endeligt vedtaget december 2021 (PDF)", "https://www.roskilde.dk/media/c2wmj23c/landzonestrategi-endelig-vedtagelse-dec-2021.pdf"),
 "ros_ve": ("Roskilde Kommune: etablering af større vedvarende energianlæg (opdateret 26/5 2026)", "https://www.roskilde.dk/da-dk/service-og-selvbetjening/erhverv/erhvervsaffald-energi-og-miljo/etablering-af-storre-vedvarende-energianlaeg-solenergi-ogeller-vindmoller-over-25-meter/"),
 "ros_tjek": ("Roskilde Kommune: tjekliste til ansøgningsmateriale, enfamiliehuse og mindre rækkehuse (PDF)", "https://www.roskilde.dk/media/u1hfiml4/tjekliste_vedr_ansoegningsmateriale_enfamiliehuse_og_mindre_raekkehuse_0.pdf"),
 "ros_varme": ("Roskilde Kommune: varmeforsyning (opdateret 28/9 2026)", "https://www.roskilde.dk/da-dk/service-og-selvbetjening/borger/bolig-og-byggeri/energi-og-miljo/varmeforsyning/"),
 "ros_jyl": ("Roskilde Kommune 5/8 2026: afgørelse om bortfald af fjernvarmeprojektet for Jyllinge (PDF)", "https://www.roskilde.dk/media/sdokjnhm/afgorelse-om-bortfald-af-projektgodkendelse-for-fjernvarmeforsyning-jyllinge.pdf"),
 "fors_ref": ("Fors: bestyrelsesreferat 10/3 2026, status på fjernvarmeudrulningen (PDF)", "https://www.fors.dk/media/xq5m5nfe/10-03-2026-bestyrelsesreferat.pdf"),
 "fors_ved": ("Fors: fjernvarme til Veddelev (projektstatus 23/10 2026)", "https://www.fors.dk/fjernvarme/fjernvarmeprojekter/veddelev/"),
 "fors_aar": ("Fors Varme Roskilde A/S: årsrapport 2025", "https://www.fors.dk/om-os/publikationer/aarsrapporter/aarsrapport-fors-varme-roskilde-as-2025/"),
 "sk_sol": ("Sønderborg Kommune: varmekilder og energi (solceller, varmepumper)", "https://sonderborgkommune.dk/varmekilder-energi"),
 "pz_varme": ("ProjectZero: skift til grønnere varme (varmekilde og forsyningsselskab pr. by i Sønderborg Kommune)", "https://projectzero.dk/skift-til-groen-varme-2/"),
 "df_blans": ("Dansk Fjernvarme 16/3 2026: Avnbøl, Ullerup og Blans melder klar til fjernvarmen", "https://danskfjernvarme.dk/aktuelt/nyheder/2026/avnboel-ullerup-og-blans-melder-klar-til-fjernvarmen"),
 "sn_blans": ("SønderborgNYT: grønt lys til fjernvarme i Blans", "https://www.sonderborgnyt.dk/nu-er-der-groent-lys-til-fjernvarme-i-blans/"),
 "df_sv29": ("Dansk Fjernvarme 2026: Sønderborg Varme stræber efter at blive CO2-neutrale i 2029", "https://danskfjernvarme.dk/aktuelt/nyheder/2026/soenderborg-varme-straeber-efter-at-blive-co2-neutrale-i-2029"),
 "sonfor_na": ("SONFOR: fjernvarme på Nordals (Nordborg til Guderup, Dyndved)", "https://sonfor.dk/projekter/fjernvarme-paa-nordals/"),
 "sonfor_halm": ("Sønderborg Forsyning 2023: næste skridt med potentielle fjernvarmeområder på Nordals (PDF)", "https://sonfor.dk/wp-content/uploads/2023/08/090223-soenderborg-forsyning-tager-naeste-skridt-med-potentielle-fjernvarmeomrader.pdf"),
 "sv_nyb": ("Sønderborg Varme: fjernvarme til Nybøl og Vester Sottrup (etableringsplan)", "https://www.sonderborg-varme.dk/overvejer-du-fjernvarme/vaerd-at-vide-om-fjernvarme/fjernvarme-til-nyboel-og-vester-sottrup/"),
})
CITIES["roskilde"] = {
  "name": "Roskilde", "kommune": "Roskilde Kommune", "updated": ("29. oktober 2026", "2026-10-29"),
  "sol_intro": "Solceller i Roskilde: sætter du panelerne på det eksisterende tag på dit enfamiliehus, kræver det som udgangspunkt ikke tilladelse efter byggeloven. Højde- og afstandsreglerne i bygningsreglementet, lokalplaner, deklarationer og bevaringshensyn gælder dog stadig. Her er reglerne, priserne og vejen til et tilbud.",
  "sol_facts": [
    ("Solceller og solfangere på det <strong>eksisterende tag på et enfamiliehus</strong> kræver som udgangspunkt ikke tilladelse efter byggeloven i Roskilde Kommune.", ["ros_byg"]),
    ("Anlægget må ikke stride mod bygningsreglementets regler om <strong>højde og afstand</strong>. Roskilde Kommune regner solceller og solfangere for det samme i denne sammenhæng.", ["ros_byg"]),
    ("Før du bestiller, beder kommunen dig gennemgå lokalplan, tinglyste deklarationer, regler om fredning og bevaring af bygninger og naturbeskyttelse.", ["ros_byg"]),
    ("Et mindre solcelleanlæg <strong>på terræn i landzone</strong> kræver landzonetilladelse. Anlæg på erhvervsbygninger kræver altid byggetilladelse.", ["ros_lz", "ros_byg"]),
  ],
  "sol_faq": [
    ("Skal jeg søge om lov til solceller på mit hus i Roskilde?", "Som udgangspunkt ikke, når panelerne sidder på det eksisterende tag på et enfamiliehus og overholder bygningsreglementets højde- og afstandsregler. Lokalplan, deklarationer, fredning, bevaring og naturbeskyttelse kan dog kræve en tilladelse eller dispensation.", ["ros_byg"]),
    ("Må jeg sætte solceller på jorden ved mit hus på landet i Roskilde Kommune?", "Det kræver landzonetilladelse. Kommunen lægger bl.a. vægt på, at anlægget ikke generer naboer eller påvirker landskabet, at det er afskærmet, og at det ligger i tilknytning til ejendommens øvrige bygninger.", ["ros_lz"]),
  ],
  "vp_intro": "Luft til vand-varmepumpe i Roskilde: fjernvarmeprojekterne i Jyllinge, Viby-Dåstrup, Gadstrup-Snoldelev og Store Valby-Ågerup er aflyst i 2026, og områderne er tilbage på naturgas. Kommunen skriver selv, at en varmepumpe for de fleste vil være den oplagte løsning dér. Her er status, priserne og tilskudsreglerne.",
  "vp_facts": [
    ("Roskilde Kommune har i 2026 truffet endelig afgørelse om, at fjernvarmeprojekterne i <strong>Jyllinge, Viby-Dåstrup, Gadstrup-Snoldelev og Store Valby-Ågerup</strong> er bortfaldet, fordi der ikke var tilslutning nok.", ["ros_varme", "ros_jyl"]),
    ("Fors oplyste i marts 2026, at tilslutningen i de fire byer lå mellem 29 og 38 % og stod stille eller faldt svagt, bl.a. fordi flere havde valgt en individuel varmepumpe.", ["fors_ref"]),
    ("Fjernvarme bliver fortsat lagt ud i <strong>Veddelev</strong> (fra 2026), og udrulningen i <strong>Himmelev</strong> og <strong>Vindinge</strong> er i gang.", ["ros_varme", "fors_ved"]),
    ("Boligejere i de aflyste områder kan søge Varmepumpepuljen, hvis de i øvrigt opfylder betingelserne.", ["ros_varme", "se_vpp"]),
  ],
  "vp_faq": [
    ("Kommer der fjernvarme i Jyllinge eller Viby?", "Nej, ikke efter de nuværende planer. Roskilde Kommune traf 5. august 2026 afgørelse om, at projektgodkendelserne er bortfaldet, fordi den forudsatte tilslutning på 70 % ikke kunne nås. Områderne er dermed igen udlagt til naturgas.", ["ros_jyl", "ros_varme"]),
    ("Må jeg skifte til elvarme i stedet for en varmepumpe i Roskilde?", "Roskilde Kommune skriver, at du ikke må etablere elvarme som hovedopvarmning i nye huse eller i eksisterende huse med vandbårent centralvarmesystem. Forbuddet gælder ikke eldrevne varmepumper.", ["ros_varme"]),
  ],
}
CITIES["soenderborg"] = {
  "name": "Sønderborg", "kommune": "Sønderborg Kommune", "updated": ("29. oktober 2026", "2026-10-29"),
  "vp_title": "Varmepumpe Sønderborg: luft til vand, tilskud, pris | Energitjekket",
  "fv_title": "Fjernvarme eller varmepumpe i Sønderborg? Pris 2026 | Energitjekket",
  "sol_intro": "Solceller i Sønderborg: sidder panelerne direkte på tagfladen af dit hus, kræver de ikke byggetilladelse. Står de på stativ, skal du altid have kommunens tilladelse. Lokalplaner, bevaringsværdige bygninger, beskyttelseslinjer og kirkelandskaber kan dog kræve dispensation. Her er reglerne, priserne og vejen til et tilbud.",
  "sol_facts": [
    ("Solceller og solfangere <strong>direkte på tagfladen</strong> kræver ikke byggetilladelse i Sønderborg Kommune, medmindre det er en erhvervsbygning eller en etageejendom.", ["sk_sol"]),
    ("Solceller på <strong>stativ</strong>, både fritstående og på taget, kræver altid kommunens tilladelse: en landzonetilladelse eller en byggetilladelse.", ["sk_sol"]),
    ("Er ejendommen omfattet af en lokalplan eller byplanvedtægt, skal du kontakte kommunen. Ved ukomplicerede dispensationssager forsøger kommunen at svare inden for <strong>2 uger</strong>.", ["sk_sol"]),
    ("Ligger huset i et <strong>kirkelandskab</strong>, kræver solceller tilladelse fra Haderslev Stift.", ["sk_sol"]),
  ],
  "sol_faq": [
    ("Skal jeg søge om lov til solceller på mit hus i Sønderborg?", "Ikke hvis panelerne sidder direkte på tagfladen, og huset ikke er berørt af lokalplan, bevaringsværdi, fredning, beskyttelseslinjer eller kirkelandskab. Det kan du se på kommunens digitale kort. Husk at indberette anlægget til BBR.", ["sk_sol"]),
    ("Hvad skal en ansøgning om solceller i Sønderborg Kommune indeholde?", "Adresse, anlæggets størrelse i m², effekt, en begrundelse for placeringen og en tegning af placeringen med højde. Ansøgningen kan sendes på mail til byg-bolig@sonderborg.dk.", ["sk_sol"]),
  ],
  "vp_intro": "Luft til vand-varmepumpe i Sønderborg: tre ud af fem huse har allerede fjernvarme, og nettet bliver udbygget mod vest til Nybøl, Vester Sottrup, Avnbøl, Ullerup og Blans. I flere landsbyer på Nordals blev fjernvarmen droppet, og dér er en varmepumpe det oplagte valg. Her er status, priserne og tilskudsreglerne.",
  "vp_facts": [
    ("Sønderborg Varme lægger fjernvarme ud i <strong>Nybøl og Vester Sottrup</strong> og har sat gang i <strong>Avnbøl, Ullerup og Blans</strong>. Varmen ventes frem i Avnbøl og Ullerup i 2027 og i Blans i 2028.", ["sv_nyb", "df_blans"]),
    ("På Nordals leverer SONFOR fjernvarme fra Nordborg til Guderup. I <strong>Dyndved</strong> blev projektet ikke gennemført, og i Oksbøl, Broballe, Mjels og Elstrup var der ikke tilslutning nok.", ["sonfor_na", "sonfor_halm"]),
    ("Sønderborg Kommune skriver, at du ikke skal have tilladelse til en varmepumpe, men anbefaler at placere den, så hverken familien eller naboerne generes af støjen.", ["sk_sol"]),
    ("Varmepumpepuljen giver kun tilskud uden for fjernvarmeområder og områder med planlagt fjernvarme. Tjek din by hos ProjectZero, før du søger.", ["se_vpp", "pz_varme"]),
  ],
  "vp_faq": [
    ("Kommer der fjernvarme i Blans?", "Ja. Natur-, Klima- og Miljøudvalget sænkede kravet til tilslutning fra 75 til 65 %, og med 67 % tilmeldt er der grønt lys til anlægsstart i 2027. Sønderborg Varme forventer at levere varme i Blans i 2028.", ["sn_blans", "df_blans"]),
    ("Skal jeg have tilladelse til en varmepumpe i Sønderborg Kommune?", "Nej. Kommunen skriver, at en varmepumpe ikke kræver tilladelse, men anbefaler en faguddannet installatør og en placering, hvor støjen ikke generer dig eller naboerne. Et jordvarmeanlæg kræver derimod tilladelse.", ["sk_sol"]),
  ],
}
CONTACTS["roskilde"] = {"sol": [("Roskilde Kommune, Byggesag", "46 31 30 00 · byggesag@roskilde.dk", "ros_varme")],
                        "vp":  [("Roskilde Kommune, Klima- og Energiteamet", "46 31 30 00 · klima@roskilde.dk", "ros_varme")]}
CONTACTS["soenderborg"] = {"sol": [("Sønderborg Kommune, Byg (Kvik-Caféen)", "88 72 40 82 · byg-bolig@sonderborg.dk", "sk_sol")],
                           "vp":  [("Sønderborg Varme", "73 43 50 00 · post@sfjv.dk", "pz_varme")]}

# ---------- daglig by-rutine 30. okt. 2026: Køge og Svendborg ----------
S.update({
 "koe_energi": ("Køge Kommune: energikilder og opvarmning (solenergi, varmepumpe, naturgas, oliefyr)", "https://www.koege.dk/borger/bolig-og-byggeri/energi-varme-og-miljoe/energikilder-og-opvarmning"),
 "koe_disp": ("Køge Kommune: dispensationer fra lokalplaner", "https://www.koege.dk/virksomhed/opstart-og-aendring-af-virksomhed/plantilladelser/dispensationer"),
 "koe_lz": ("Køge Kommune: landzone og landzonetilladelser", "https://www.koege.dk/borger/bolig-og-byggeri/byggeri/landzone-og-landzonetilladelser"),
 "kfv_pm": ("Køge Fjernvarme 5/10 2026: gentænker fjernvarmeprojektet omkring midtbyen (K05, K06, K08), FAQ opdateret 26/10 2026", "https://www.koegefjernvarme.dk/nyheder/pressemeddelelse"),
 "kfv_nyl": ("Køge Fjernvarme 20/3 2026: fjernvarmeudbygningen omkring Nylandsvej (K02)", "https://www.koegefjernvarme.dk/nyheder/fjernvarmeudbygningen-omkring-nylandsvej"),
 "kfv_grav": ("Køge Fjernvarme 20/4 2026: gravestart Ølsemaglevej Øst og Strandlodsvej", "https://www.koegefjernvarme.dk/nyheder/gravestart-oelsemaglevej-oest-og-strandlodsvej"),
 "df_bjae": ("Dansk Fjernvarme 1/10 2026: fra nul til 850 fjernvarmekunder i Bjæverskov", "https://danskfjernvarme.dk/aktuelt/nyheder/2026/fra-nul-til-850-fjernvarmekunder-i-bjaeverskov"),
 "koe_borup": ("Køge Kommune: VVM-screeningsafgørelse for Borup Varmeværk, ny elkedel", "https://www.koege.dk/om-koege-kommune/presse-og-kommunikation/nyheder-og-aktuelt/nyheder/vvm-screeningsafgoerelse-vedroerende-borup-varmevaerk-ny-elkedel"),
 "kv_aar": ("Køge Varme A/S: årsrapport 2025 (PDF, KLAR Forsyning)", "https://klarforsyning.dk/files/media/document/K%C3%B8ge%20Varme%20-%20%C3%85rsrapport%202025_489070_0.2.pdf"),
 "svb_sol": ("Svendborg Kommune: overvejer du solceller? (tilladelser på tag, landbrugsbygninger og terræn)", "https://www.svendborg.dk/borger/bolig-og-byggeri/el-og-varme/overvejer-du-solceller/"),
 "svb_vp": ("Svendborg Kommune: varmepumper (tilladelse, støj og tilskud)", "https://www.svendborg.dk/borger/bolig-og-byggeri/el-og-varme/varmepumper/"),
 "svb_fv": ("Svendborg Kommune: fjernvarme og Varmeplan 2030", "https://www.svendborg.dk/borger/bolig-og-byggeri/el-og-varme/fjernvarme/"),
 "svb_vp2030": ("Svendborg Kommune: kommer der fjernvarme i dit område? (revideret Varmeplan 2030)", "https://www.svendborg.dk/nyheder/kommer-der-fjernvarme-i-dit-omraade/"),
 "svb_oll": ("Svendborg Kommune: Ollerup, Vester Skerninge og Ulbølle ikke længere udlagt til fjernvarme", "https://www.svendborg.dk/nyheder/nu-kan-du-soege-tilskud-til-varmepumpe-i-ollerup-vester-skerninge-og-ulboelle/"),
 "svb_lund": ("Svendborg Kommune 26/11 2025: afgørelse om individuel varmeforsyning i Lundeborg", "https://www.svendborg.dk/hoeringer-og-afgoerelser/individuel-varmeforsyning-i-lundeborg/"),
 "svb_elv": ("Svendborg Kommune: elvarmeforbud", "https://www.svendborg.dk/borger/bolig-og-byggeri/el-og-varme/elvarmeforbud/"),
 "sfv_ud": ("Svendborg Fjernvarme: få fjernvarme (plan for nye områder)", "https://svendborgfjernvarme.dk/faa-fjernvarme"),
 "df_svb": ("Dansk Fjernvarme 8/5 2026: elektrificering gør Svendborg klar til fremtiden", "https://danskfjernvarme.dk/aktuelt/nyheder/2026/elektrificering-goer-svendborg-klar-til-fremtiden"),
})
CITIES["koege"] = {
  "name": "Køge", "kommune": "Køge Kommune", "updated": ("30. oktober 2026", "2026-10-30"),
  "sol_intro": "Solceller i Køge: Køge Kommune kræver som udgangspunkt ingen tilladelse til solceller eller solfangere på taget af et enfamiliehus. Lokalplanen og bygningsreglementet skal dog overholdes, og særlige forhold kan kræve dispensation eller landzonetilladelse. Her er reglerne, priserne og vejen til et tilbud.",
  "sol_facts": [
    ("Solcelle- og solfangeranlæg <strong>på taget af et enfamiliehus</strong> kræver som udgangspunkt ikke tilladelse fra Køge Kommune.", ["koe_energi"]),
    ("Anlægget skal tage hensyn til bestemmelserne i <strong>lokalplanen</strong> og bygningsreglementet.", ["koe_energi"]),
    ("Særlige forhold kan betyde, at anlægget kræver <strong>dispensation fra lokalplanen</strong> eller en landzonetilladelse.", ["koe_energi"]),
    ("Kommunen kan kun i mindre grad dispensere fra en lokalplan, og aldrig fra planens principper om formål og anvendelse.", ["koe_disp"]),
  ],
  "sol_faq": [
    ("Skal jeg søge om lov til solceller på mit hus i Køge?", "Som udgangspunkt ikke, når anlægget sidder på taget af et enfamiliehus. Du skal dog overholde lokalplanen og bygningsreglementet, og særlige forhold kan kræve dispensation eller landzonetilladelse.", ["koe_energi"]),
    ("Hvordan søger jeg dispensation fra lokalplanen i Køge Kommune?", "Sammen med en ansøgning om byggetilladelse i Byg og Miljø, eller som en begrundet ansøgning på mail til tmf@koege.dk.", ["koe_disp"]),
  ],
  "vp_intro": "Luft til vand-varmepumpe i Køge: halvdelen af husene i kommunen varmes op med naturgas, og i oktober 2026 bad Køge Fjernvarme om at annullere fjernvarmeprojektet for kvartererne omkring midtbyen. I Bjæverskov er et nyt fjernvarmeværk derimod åbnet. Her er status, priserne og tilskudsreglerne.",
  "vp_facts": [
    ("Køge Fjernvarme vil anmode Køge Kommune om at annullere projektforslaget for <strong>K05, K06 og K08</strong> omkring midtbyen og venter et nyt projektforslag i løbet af 2027.", ["kfv_pm"]),
    ("Områderne K05, K06 og K08 er fortsat udlagt til fjernvarme, og Køge Fjernvarme forventer ikke, at varmeplanerne ændres i mellemtiden.", ["kfv_pm"]),
    ("Omkring <strong>Nylandsvej</strong> (K02) er gravearbejdet i gang ved Ølsemaglevej Øst og Strandlodsvej, mens Forsythiavej, Tranholmsvej og Stevnsbovej er sendt i nyt udbud.", ["kfv_grav", "kfv_nyl"]),
    ("Ved naboklager over støj bruger Køge Kommune Miljøstyrelsens vejledende grænser: i de fleste tilfælde <strong>35 dB(A)</strong> ved naboens skel om natten.", ["koe_energi"]),
  ],
  "vp_faq": [
    ("Kan jeg få tilskud til en varmepumpe i K05, K06 eller K08 i Køge?", "Køge Fjernvarme skriver, at områderne fortsat er udlagt til fjernvarme, fordi projektforslaget endnu ikke er annulleret, og at varmeplanerne ikke ventes at blive ændret i mellemtiden. Varmepumpepuljen giver ikke tilskud i fjernvarmeområder.", ["kfv_pm", "se_vpp"]),
    ("Må jeg skifte mit gasfyr ud med en varmepumpe, hvis jeg bor i et område med tilslutningspligt til naturgas?", "Køge Kommune skriver, at du skal søge dispensation hos Plan, hvis du bor i et område med tilslutningspligt til naturgasnettet og vil bruge en anden energikilde.", ["koe_energi"]),
  ],
}
CITIES["svendborg"] = {
  "name": "Svendborg", "kommune": "Svendborg Kommune", "updated": ("30. oktober 2026", "2026-10-30"),
  "sol_intro": "Solceller i Svendborg: på et almindeligt parcelhus kræver solceller umiddelbart hverken byggetilladelse eller landzonetilladelse. Lokalplaner, byplanvedtægter og tinglyste deklarationer kan dog have særlige regler for tagmateriale eller solceller. Her er reglerne, priserne og vejen til et tilbud.",
  "sol_facts": [
    ("Solceller på et <strong>almindeligt parcelhus</strong> kræver umiddelbart ikke byggetilladelse eller landzonetilladelse i Svendborg Kommune.", ["svb_sol"]),
    ("Tjek om der er en <strong>lokalplan, byplanvedtægt eller tinglyst deklaration</strong>, der har særlige regler for tagmateriale eller solceller.", ["svb_sol"]),
    ("Solceller på <strong>terræn</strong> under 40 m² kræver ikke byggetilladelse, hvis de højst er 1,8 m høje og ikke strider mod deklarationer, lokalplan og naturbeskyttelseslovens afstandslinjer.", ["svb_sol"]),
    ("På landbrugsbygninger kræver de fleste anlæg byggetilladelse, fordi de øger lasten på taget med mere end 5 %.", ["svb_sol"]),
  ],
  "sol_faq": [
    ("Skal jeg søge om lov til solceller på mit hus i Svendborg?", "Umiddelbart ikke på et almindeligt parcelhus. Kommunen beder dig dog tjekke lokalplan, byplanvedtægt og tinglyste deklarationer, som kan have særlige regler for tagmateriale eller solceller.", ["svb_sol"]),
    ("Må jeg sætte solceller op i haven i Svendborg Kommune?", "Ja, uden byggetilladelse, hvis anlægget er under 40 m², højst 1,8 m højt på stativ og ikke strider mod deklarationer, lokalplan eller naturbeskyttelseslovens afstandslinjer. I landzone skal det også ligge højst 20 m fra hovedbygningen for at undgå landzonetilladelse.", ["svb_sol"]),
  ],
  "vp_intro": "Luft til vand-varmepumpe i Svendborg: kun hvert fjerde hus i kommunen har fjernvarme, og Svendborg Fjernvarme skal først have en ny stor varmepumpe i drift, før nettet kan udvides. I Ollerup, Vester Skerninge, Ulbølle og Lundeborg er fjernvarmen droppet. Her er status, priserne og tilskudsreglerne.",
  "vp_facts": [
    ("Luft til luft- og luft til vand-varmepumper kan sættes op <strong>uden tilladelse</strong> fra Svendborg Kommune, men servitutter og lokalplaner kan have retningslinjer.", ["svb_vp"]),
    ("Udedelen må højst støje <strong>35 dB</strong> ind mod naboen i nattetimerne, og den må ikke stå inde i et skur eller en garage.", ["svb_vp"]),
    ("Ollerup, Vester Skerninge og Ulbølle er ikke længere udlagt til fjernvarme, og i Lundeborg blev fjernvarmeprojektet annulleret i november 2025. Her kan du søge tilskud fra Varmepumpepuljen.", ["svb_oll", "svb_lund"]),
    ("I områder med <strong>vedtaget fjernvarme</strong> i Varmeplan 2030 kan du ikke få tilskud fra Varmepumpepuljen.", ["svb_vp2030", "se_vpp"]),
  ],
  "vp_faq": [
    ("Kommer der fjernvarme i mit kvarter i Svendborg?", "Svendborg Fjernvarme har en plan for boliger i Nordøst, Sydøst, Tved, Øst og Christiansminde samt Ryttermarken, Frederiksø og Kogtved. Først skal en ny varmepumpe på Bodøvej bygges, og selskabet regner med omkring fem år, til den sidste ejendom er tilsluttet. Slå din adresse op på kommunens varmeplanskort.", ["sfv_ud", "svb_fv"]),
    ("Må jeg skifte til elradiatorer i stedet for en varmepumpe i Svendborg?", "Ikke som primær opvarmning i fjernvarme- og naturgasforsynede områder, hvor der er elvarmeforbud. Forbuddet gælder ikke varmepumper og jordvarme.", ["svb_elv"]),
  ],
}
CONTACTS["koege"] = {"sol": [("Køge Kommune, Byggesag", "56 67 24 55 · byg@koege.dk", "koe_energi")],
                     "vp":  [("Køge Kommune, Plan (naturgas og varmeplan)", "56 67 21 11 · plan@koege.dk", "koe_energi")]}
CONTACTS["svendborg"] = {"sol": [("Svendborg Kommune, Byg og BBR", "62 23 33 33", "svb_sol")],
                         "vp":  [("Svendborg Fjernvarme", "62 21 33 21 · info@svendborgfjernvarme.dk", "sfv_ud")]}

# ---------- daglig by-rutine 31. okt. 2026: Faaborg (Faaborg-Midtfyn) og Aabenraa ----------
S.update({
 "fmk_elv": ("Faaborg-Midtfyn Kommune: el og varme (solenergianlæg, varmepumper, fjernvarmeselskaber)", "https://www.fmk.dk/borger/natur-og-miljoe/energi-og-miljoe/el-og-varme/"),
 "fmk_vp": ("Faaborg-Midtfyn Kommune: Varmeplan 2022-2030", "https://www.fmk.dk/politik/politikker-planer-og-strategier/varmeplan/"),
 "fmk_kor": ("Faaborg-Midtfyn Kommune 10/12 2025: projektgodkendelse, aflysning af fjernvarme til Korinth (PDF)", "https://www.fmk.dk/media/4hmn3xwf/projektgodkendelse-for-aflysning-af-fjernvarmeforsyning-til-korinth.pdf"),
 "fmk_byg": ("Faaborg-Midtfyn Kommune: tilladelse til erhvervsbyggeri (kontakt BYG)", "https://www.fmk.dk/erhverv/byggeri-og-erhvervsgrunde/tilladelse-til-erhvervsbyggeri/"),
 "ffv_proj": ("FFV Varme A/S: fjernvarmeprojekter (Faaborg nordvest, landsbyer, Korinth, Espe)", "https://www.ffv.dk/fjernvarme/fjernvarmeprojekter/"),
 "ffv_pause": ("FFV 5/12 2025: fjernvarmeprojekter sættes på pause pga. manglende tilslutning", "https://www.ffv.dk/nyheder/artikler/fjernvarmeprojekter-saettes-paa-pause-pga-manglende-tilslutning/"),
 "ffv_rug": ("FFV Varme 26/8 2026: gravearbejde på Rugagervej i Faaborg", "https://www.ffv.dk/nyheder/artikler/gravearbejde-paa-rugagervej-ny-fjernvarmeledning-paa-vej/"),
 "df_mfe": ("Dansk Fjernvarme 5/5 2026: fynboer kan få fjernvarme og spare penge (Midtfyns Energi)", "https://danskfjernvarme.dk/aktuelt/nyheder/2026/fynboer-kan-faa-fjernvarme-og-spare-penge"),
 "abr_sol": ("Aabenraa Kommune: solenergianlæg", "https://aabenraa.dk/borger/flytning-bolig-og-byggeri/andre-anlaeg-og-konstruktioner/solenergianlaeg"),
 "abr_byg": ("Aabenraa Kommune: søg om byggetilladelse og tilladelse til nedrivning", "https://aabenraa.dk/borger/flytning-bolig-og-byggeri/byggeri-og-nedrivning/soeg-om-byggetilladelse"),
 "abr_bom": ("Aabenraa Kommune: vejledning til brug af Byg og Miljø (PDF)", "https://aabenraa.dk/media/4ekpya0x/vejledning-til-brug-af-byg-og-miljoe.pdf"),
 "abr_stoej": ("Aabenraa Kommune: støjgener fra private (støj fra varmepumper)", "https://aabenraa.dk/borger/klima-natur-og-miljoe/miljoe/miljoe-i-dagligdagen/stoejgener-fra-private"),
 "abr_vpl": ("Aabenraa Kommune: varmeplanlægning for forsyningsområder (udfasning af gas)", "https://aabenraa.dk/borger/klima-natur-og-miljoe/miljoe/varmeforsyning/varmeplanlaegning"),
 "abr_vp22": ("Aabenraa Kommune: Varmeplan for områder med kollektiv varmeforsyning 2022 (PDF)", "https://aabenraa.dk/media/mdrl4ay3/wt-kollektiv-varmeforsyning-2022.pdf"),
 "afv_bol": ("Aabenraa Fjernvarme: tidsplan for Bolderslev (opdateret 21/10 2026)", "https://www.aabenraa-fjernvarme.dk/tidsplaner/bolderslev"),
 "afv_bol_op": ("Aabenraa Fjernvarme: opstart i Bolderslev (transmissionsledning og ny fjernvarmecentral)", "https://www.aabenraa-fjernvarme.dk/om-os/nyheder/opstart-i-bolderslev"),
 "afv_var": ("Aabenraa Fjernvarme: tidsplan for Varnæs (opdateret 20/8 2026)", "https://www.aabenraa-fjernvarme.dk/tidsplaner/varnaes"),
 "afv_pris": ("Aabenraa Fjernvarme: priser 2026, konverterings- og transmissionsbidrag", "https://www.aabenraa-fjernvarme.dk/priser"),
 "afv_gylle": ("Aabenraa Fjernvarme: fra gylle til varme (overskudsvarme til Tumbøl og Felsted)", "https://www.aabenraa-fjernvarme.dk/om-os/nyheder/fra-gylle-til-varme"),
 "ens_stoej": ("Energistyrelsen: støjberegner for varmepumper", "https://ens.dk/forsyning-og-forbrug/stoejberegner-varmepumper"),
})
CITIES["faaborg"] = {
  "name": "Faaborg", "kommune": "Faaborg-Midtfyn Kommune", "updated": ("31. oktober 2026", "2026-10-31"),
  "reg_title": "Solceller Faaborg-Midtfyn: regler og byggetilladelse | Energitjekket",
  "sol_intro": "Solceller i Faaborg: på den eksisterende tagkonstruktion af et parcelhus, dobbelthus, rækkehus eller sommerhus kræver solceller ikke byggetilladelse i Faaborg-Midtfyn Kommune, så længe byggeretten overholdes. Lokalplaner, servitutter og strandbeskyttelseslinjen kan dog stille krav. Her er reglerne, priserne og vejen til et tilbud.",
  "sol_facts": [
    ("Solceller på den <strong>eksisterende tagkonstruktion</strong> af et enfamiliehus, dobbelthus, rækkehus eller sommerhus kræver ikke byggetilladelse.", ["fmk_elv"]),
    ("På et <strong>fladt tag</strong> må anlægget være op til 1,5 m højt uden byggetilladelse.", ["fmk_elv"]),
    ("Anlægget skal overholde byggeretten, fx det skrå højdegrænseplan og <strong>mindst 2,5 m til skel</strong> ved enfamiliehuse. Ellers kræver det byggetilladelse.", ["fmk_elv"]),
    ("Ligger ejendommen inden for <strong>strandbeskyttelseslinjen</strong>, kræver solceller altid tilladelse fra Kystdirektoratet.", ["fmk_elv"]),
  ],
  "sol_faq": [
    ("Skal jeg søge om lov til solceller på mit hus i Faaborg?", "Ikke når anlægget sidder på den eksisterende tagkonstruktion af et enfamiliehus, dobbelthus, rækkehus eller sommerhus, og byggeretten er overholdt. Lokalplan, byplanvedtægt, servitutter, fredning og strandbeskyttelseslinjen kan dog kræve dispensation eller tilladelse.", ["fmk_elv"]),
    ("Skal jeg melde mine solceller til BBR i Faaborg-Midtfyn Kommune?", "Ja. Kræver anlægget ikke byggetilladelse, skal du selv sende areal, opførelsesår, effekt i kW, fabrikat/type og en tegning med placeringen, så BBR kan blive ajourført.", ["fmk_elv"]),
  ],
  "vp_intro": "Luft til vand-varmepumpe i Faaborg: kun hvert tredje hus i Faaborg-Midtfyn Kommune har fjernvarme, og flere planlagte fjernvarmeprojekter er sat på pause eller aflyst. I Korinth og Espe bliver der ikke fjernvarme. Her er status, priserne og tilskudsreglerne.",
  "vp_facts": [
    ("Faaborg-Midtfyn Kommune har godkendt, at fjernvarmeprojektet i <strong>Korinth</strong> annulleres, så husejerne i stedet kan få tilskud til en individuel løsning.", ["fmk_kor"]),
    ("Fjernvarmeprojekterne i <strong>Brobyværk, Vester Åby, Horne, Falsled og Millinge/Svanninge</strong> er sat på pause i ca. et år, og i Espe er projektet afsluttet uden fjernvarme.", ["ffv_pause", "ffv_proj"]),
    ("Udvidelsen af fjernvarmen i <strong>Faaborg nordvest</strong> er sat midlertidigt på pause, fordi de lave gaspriser gør det svært at få nok tilslutninger.", ["ffv_proj"]),
    ("Varmeplanen er kun vejledende. Først når et konkret fjernvarmeprojekt er godkendt, og anlægsfasen går i gang, <strong>bortfalder muligheden for statstilskud</strong> til fx en varmepumpe.", ["fmk_vp"]),
  ],
  "vp_faq": [
    ("Kan jeg få tilskud til en varmepumpe i Korinth?", "Ja, det er formålet med aflysningen: projektforslaget blev sendt ind, så forbrugerne i området i stedet kan få tilskud til en individuel løsning. Tilskuddet kræver, at du skifter olie, gas, el eller biokedel ud.", ["fmk_kor", "se_vpp"]),
    ("Hvad sker der med fjernvarmen i Brobyværk, Horne og Vester Åby?", "Projekterne er sat på pause, ikke skrinlagt. FFV, kommunen og de lokale arbejdsgrupper har udskudt den endelige beslutning i ca. et år og venter på den politiske aftale om varmeforsyningen i 2026.", ["ffv_pause"]),
  ],
}
CITIES["aabenraa"] = {
  "name": "Aabenraa", "kommune": "Aabenraa Kommune", "updated": ("31. oktober 2026", "2026-10-31"),
  "sol_intro": "Solceller i Aabenraa: Aabenraa Kommune beder dig undersøge byggelovgivningen og en eventuel lokalplan, før du sætter solceller op. I Byg og Miljø kan du se, om din ejendom har en lokalplan eller andre bindinger. Her er reglerne, priserne og vejen til et tilbud.",
  "sol_facts": [
    ("Før du sætter solceller op, skal du tjekke de forhold i <strong>byggelovgivningen og en eventuel lokalplan</strong>, som skal overholdes.", ["abr_sol"]),
    ("I <strong>Byg og Miljø</strong> kan du se, om der er en lokalplan eller andre bindinger på din ejendom.", ["abr_byg"]),
    ("Kræver dit anlæg tilladelse, søger du byggetilladelse digitalt via Byg og Miljø, og alle bilag skal være i pdf-format.", ["abr_sol", "abr_byg"]),
    ("Elinstallationen skal altid udføres af en <strong>autoriseret elinstallatør</strong>.", ["abr_sol"]),
  ],
  "sol_faq": [
    ("Skal jeg søge om lov til solceller på mit hus i Aabenraa?", "Det afhænger af byggelovgivningen og en eventuel lokalplan for din ejendom. Kommunen henviser til vejledningen 'Gode råd inden du opsætter solenergianlæg', og i Byg og Miljø kan du se lokalplaner og andre bindinger. Er du i tvivl, kan du kontakte Team Byg.", ["abr_sol", "abr_byg"]),
    ("Hvad koster en byggesag om solceller i Aabenraa Kommune?", "Kræver anlægget tilladelse, opkræver kommunen et byggesagsgebyr efter den tid, sagen tager. Det har været reglen siden 1. januar 2015, og taksterne står i kommunens gebyrvedtægt.", ["abr_byg"]),
  ],
  "vp_intro": "Luft til vand-varmepumpe i Aabenraa: halvdelen af husene i kommunen har fjernvarme, og Aabenraa Fjernvarme er i gang med Bolderslev og Varnæs. Uden for fjernvarmen skal gasfyrene skiftes til fx varmepumper, og kommunen advarer om støj. Her er status, priserne og tilskudsreglerne.",
  "vp_facts": [
    ("Aabenraa Kommune støtter målet om, at der i <strong>2035 ikke bruges gas til rumopvarmning</strong>. Gasområder skal enten have fjernvarme eller individuel opvarmning, fx med varmepumper.", ["abr_vpl"]),
    ("Kommunen har ingen faste afstandsregler, men den vejledende <strong>støjgrænse om natten</strong> i boligområder er lav, og varmepumper kører i døgndrift.", ["abr_stoej"]),
    ("Får naboen medhold i en klage, kan du blive pålagt at <strong>dokumentere støjen</strong> og betale for støjdæmpning. Kommunen skriver, at billige varmepumper ofte støjer mere end dyrere.", ["abr_stoej"]),
    ("Energistyrelsens <strong>støjberegner</strong> kan hjælpe med at finde den bedste placering af udedelen på grunden.", ["abr_stoej", "ens_stoej"]),
  ],
  "vp_faq": [
    ("Kommer der fjernvarme til Bolderslev?", "Ja. Aabenraa Fjernvarme tog første spadestik på transmissionsledningen 4. maj 2026, og ledningen ventes færdig i december 2026. De første forbrugere ventes at få fjernvarme i 1. kvartal 2027.", ["afv_bol"]),
    ("Kan Aabenraa Kommune kræve, at jeg flytter min varmepumpe?", "Kommunen kan regulere støj fra varmepumper efter miljøaktivitetsbekendtgørelsen og miljøbeskyttelsesloven, hvis den vurderer, at støjen er en væsentlig gene for naboerne, og kan give påbud om at sænke støjen.", ["abr_stoej"]),
  ],
}
CONTACTS["faaborg"] = {"sol": [("Faaborg-Midtfyn Kommune, BYG", "72 53 21 04 · byg@fmk.dk", "fmk_byg")],
                       "vp":  [("FFV Varme A/S", "62 61 16 66 · ffv@ffv.dk", "ffv_proj")]}
CONTACTS["aabenraa"] = {"sol": [("Aabenraa Kommune, Team Byg", "73 76 73 47 · byg@aabenraa.dk", "abr_sol")],
                        "vp":  [("Aabenraa Fjernvarme", "74 62 40 98 · info@aabenraa-fjernvarme.dk", "afv_pris")]}

# ---------- daglig by-rutine 1. nov. 2026: Herning (DK1) og Greve (DK2) ----------
S.update({
 "her_sol": ("Herning Kommune: solceller, jordvarme og vindmøller", "https://www.herning.dk/borger/byudvikling-byggeri-og-grundsalg/din-ejendom/el-vand-og-varme/solceller-jordvarme-og-vindmoeller"),
 "her_br18": ("Herning Kommune: hvad er undtaget ifølge BR18", "https://www.herning.dk/borger/byudvikling-byggeri-og-grundsalg/byggeri/kraever-dit-projekt-en-byggetilladelse/hvad-er-undtaget-ifoelge-br18"),
 "her_soeg": ("Herning Kommune: sådan søger du byggetilladelse", "https://www.herning.dk/borger/byudvikling-byggeri-og-grundsalg/byggeri/ansoegning-om-byggetilladelse/saadan-soeger-du"),
 "her_faelles": ("Herning Kommune: få en fælles varmeløsning (pulje til fælles varmeløsninger)", "https://www.herning.dk/borger/byudvikling-byggeri-og-grundsalg/din-ejendom/el-vand-og-varme/faa-en-faelles-varmeloesning"),
 "verdo_her_pris": ("Verdo: fjernvarmepriser og tilslutningsbidrag i Herning (priser pr. 1/4 2026 og fra 1/1 2027)", "https://www.verdo.com/dk/privat/fjernvarme/priserogvilkaar/herning/"),
 "verdo_her": ("Verdo: skift til fjernvarme i Herning", "https://www.verdo.com/dk/privat/fjernvarme/skift/herning/"),
 "gre_byg": ("Greve Kommune: skal du søge byggetilladelse?", "https://greve.dk/by-og-bolig/byggeri/skal-du-soege-byggetilladelse"),
 "gre_tjek": ("Greve Kommune: tjekliste før opsætning af solceller (PDF, rev. 21.11.2019)", "https://greve.dk/media/psepmnwk/tjekliste-foer-opsaetning-af-solceller-i-greve-kommune.pdf"),
 "gre_varme": ("Greve Kommune: varme (fjernvarme, naturgas, jordvarme og luftvarmepumper)", "https://greve.dk/by-og-bolig/spildevand-el-vand-og-varmeforsyning/varme"),
 "gre_tune": ("Greve Kommune 2026: Tuneborgerne får ikke fjernvarme", "https://greve.dk/nyheder/2026/tuneborgerne-faar-ikke-fjernvarme"),
 "gre_vpl": ("Greve Kommune: Varmeplan 2022-2038 (PDF)", "https://greve.dk/media/zz1prqgh/varmeplan-2022-2038.pdf"),
 "gre_pf1": ("Projektforslag 2022: konvertering fra naturgas til fjernvarme øst for motorvejen, fase 1 (Greve Kommune, PDF)", "https://greve.dk/media/nqlbg0ed/konvertering-fra-naturgas-til-fjernvarme-oest-for-motorvejen-fase-1-2022.pdf"),
 "gfv_kan": ("Greve Fjernvarme: kan du få fjernvarme? (faser og tilmeldingsstatus, læst 1/11 2026)", "https://grevefjernvarme.dk/ny-kunde/kan-du-faa-fjernvarme"),
 "gfv_pris": ("Greve Fjernvarme: hvad koster det at få fjernvarme?", "https://grevefjernvarme.dk/ny-kunde/hvad-koster-det-at-faa-fjernvarme"),
})
CITIES["herning"] = {
  "name": "Herning", "kommune": "Herning Kommune", "updated": ("1. november 2026", "2026-11-01"),
  "sol_intro": "Solceller i Herning: monteres panelerne fladt på den eksisterende tagkonstruktion og øger lasten med højst 5 %, kræver de ikke tilladelse efter byggeloven i Herning Kommune. Lokalplaner, deklarationer og bygningsreglementet skal dog overholdes, og anlæg på jorden kræver altid tilladelse. Her er reglerne, priserne og vejen til et tilbud.",
  "sol_facts": [
    ("Solcellepaneler, der monteres <strong>fladt på en eksisterende tagkonstruktion</strong>, kræver ikke tilladelse efter byggeloven, hvis anlægget højst øger lasten på taget med 5 %.", ["her_sol"]),
    ("Kommunen anbefaler altid at sende <strong>skitser og en beregning af lasten</strong> via Byg og Miljø, så den kan vurdere, om anlægget kræver tilladelse.", ["her_sol"]),
    ("Anlægget må ikke stride mod bygningsreglementet, <strong>lokalplaner, byplanvedtægter</strong>, tinglyste deklarationer, fredninger eller grundejervedtægter.", ["her_sol"]),
    ("Solceller <strong>på jorden</strong> kræver tilladelse og må højst stå 20 m fra ejendommens samlede bygninger. I landzone kræver de også landzonetilladelse.", ["her_sol"]),
  ],
  "sol_faq": [
    ("Skal jeg søge om lov til solceller på mit hus i Herning?", "Ikke efter byggeloven, hvis panelerne monteres fladt på den eksisterende tagkonstruktion og højst øger lasten med 5 %. Kommunen skriver, at et anlæg på et enfamiliehus normalt ikke belaster taget så meget, at det ikke kan bære det. Lokalplaner og deklarationer skal stadig overholdes.", ["her_sol"]),
    ("Hvad gør jeg, hvis naboen kan blive generet af genskin fra mine solceller?", "Herning Kommune anbefaler, at du lader leverandøren af anlægget vurdere risikoen for genskin, før det bliver sat op.", ["her_sol"]),
  ],
  "vp_intro": "Luft til vand-varmepumpe i Herning: næsten fire ud af fem huse i Herning Kommune har fjernvarme, men i en række landsbyer er der hverken fjernvarme eller planer om det. Her støtter kommunen fælles varmeløsninger med rådgivning, og jordvarme kræver tilladelse. Her er status, priserne og tilskudsreglerne.",
  "vp_facts": [
    ("Verdo leverer fjernvarme til <strong>35.000 adresser</strong> i Herning og omegn, og 90 % produceres på biomasse.", ["verdo_her"]),
    ("Kommunen har haft en <strong>pulje på 600.000 kr.</strong> for 2024 og 2025 til fælles varmeløsninger i lokalområder og landsbyer uden fjernvarme.", ["her_faelles"]),
    ("Støtten gives som <strong>rådgivningstimer</strong>, fx til en teknisk analyse af jordvarme eller en fælles luft-vand-varmepumpe. Der gives ikke penge til selve anlægget.", ["her_faelles"]),
    ("Et <strong>jordvarmeanlæg</strong> kræver tilladelse fra Herning Kommune, som du søger via Byg og Miljø, før du går i gang.", ["her_sol"]),
  ],
  "vp_faq": [
    ("Kan vores landsby få hjælp til en fælles varmeløsning i Herning Kommune?", "Ja, en lokal arbejdsgruppe kan søge kommunens pulje til fælles varmeløsninger på varme@herning.dk. Kriterierne er bl.a. mindst 10 boliger, at mindst halvdelen i dag har olie- eller gasfyr, og at området ligger uden for fjernvarmen. Puljen var øremærket 2024 og 2025, så spørg kommunen, om der stadig er midler.", ["her_faelles"]),
    ("Skal jeg have tilladelse til jordvarme i Herning?", "Ja. Du søger via Byg og Miljø med en pdf-skitse af matriklen, hvor bygninger, jordvarmeanlæg og eventuelle boringer er vist, og du må først gå i gang, når du har fået kommunens tilladelse.", ["her_sol"]),
  ],
}
CITIES["greve"] = {
  "name": "Greve", "kommune": "Greve Kommune", "updated": ("1. november 2026", "2026-11-01"),
  "sol_intro": "Solceller i Greve: på et skråt tag eller en facade af et parcel- eller rækkehus kræver solceller ikke byggetilladelse i Greve Kommune, når bygningsreglementets højder og afstande overholdes. Dækker anlægget mere end ca. 75 % af en tagflade, skal sagen behandles efter lokalplanen. Her er reglerne, priserne og vejen til et tilbud.",
  "sol_facts": [
    ("Solceller på <strong>skrå tage og facader</strong> af enfamilie- og rækkehuse kræver ikke byggetilladelse, når anlægget holder sig inden for BR18's højder og afstande.", ["gre_tjek"]),
    ("Anlæg på <strong>terræn</strong> og på erhvervsbyggeri kræver altid byggetilladelse.", ["gre_tjek"]),
    ("Dækker anlægget <strong>mere end ca. 75 % af en enkelt tagflade</strong>, skal sagen behandles efter lokalplanen. Kommunen træffer afgørelsen uden gebyr.", ["gre_tjek"]),
    ("Kommunen anbefaler <strong>antirefleksbehandlede</strong> paneler, og det er et krav, hvis lokalplanen forbyder blanke og reflekterende tagmaterialer.", ["gre_tjek"]),
  ],
  "sol_faq": [
    ("Skal jeg søge om lov til solceller på mit hus i Greve?", "Ikke hvis anlægget sidder på et skråt tag eller en facade af et enfamilie- eller rækkehus og holder sig inden for bygningsreglementets højder og afstande. Lokalplaner, tinglyste deklarationer, fredning og naturbeskyttelse kan dog kræve tilladelse eller dispensation.", ["gre_tjek"]),
    ("Skal jeg melde mine solceller til BBR i Greve Kommune?", "Ja. Send en mail til bbrteam@greve.dk med anlæggets størrelse (antal paneler og m²) og ydelsen i kWp.", ["gre_tjek"]),
  ],
  "vp_intro": "Luft til vand-varmepumpe i Greve: over halvdelen af husene i Greve Kommune har stadig naturgas, og Greve Fjernvarme udbygger nettet øst for motorvejen i faser frem mod 2038. I Tune er fjernvarmeprojektet aflyst, så husejerne igen kan søge tilskud til en varmepumpe. Her er status, priserne og tilskudsreglerne.",
  "vp_facts": [
    ("Høje Taastrup Fjernvarme har <strong>aflyst fjernvarmen i Tune</strong>, fordi tilslutningen faldt fra 60 % til 46 %. Borgerne kan igen søge tilskud fra statens pulje til varmepumper.", ["gre_tune"]),
    ("En <strong>luftvarmepumpe</strong> kræver ikke tilladelse, men den skal overholde støjkravene i skel, og Greve Kommune følger normalt Miljøstyrelsens støjgrænser.", ["gre_varme"]),
    ("Kommunen er <strong>restriktiv med dybe jordvarmeboringer</strong> mellem motorvejen og ca. 1 km fra kysten, fordi boringer gennem lerlagene kan trække saltvand ind i drikkevandet.", ["gre_varme"]),
    ("<strong>Greve Landsby, Kildebrønde og Karlslunde Landsby</strong> ligger uden for Greve Fjernvarmes forsyningsområde.", ["gfv_kan"]),
  ],
  "vp_faq": [
    ("Får Tune fjernvarme?", "Nej. Høje Taastrup Fjernvarme har aflyst projektet i Tune, Reerslev og Stærkende, fordi tilslutningen faldt til 46 %. Tune er ikke længere udlagt som fjernvarmeområde, og borgerne kan igen søge tilskud fra statens pulje til varmepumper.", ["gre_tune"]),
    ("Må jeg lave jordvarme med en dyb boring i Greve?", "Det kræver kommunens tilladelse, og i området mellem motorvejen og ca. 1 km fra kysten er kommunen restriktiv, fordi der er risiko for saltvand i vandboringerne. Jordvarme med vandrette slanger kræver også tilladelse, og den normale afstand til en vandboring er 50 m.", ["gre_varme"]),
  ],
}
CONTACTS["herning"] = {"sol": [("Herning Kommune, Byggesag", "96 28 80 15 · byggesag@herning.dk", "her_sol")],
                       "vp":  [("Herning Kommune, varmeforsyning", "varme@herning.dk", "her_faelles")]}
CONTACTS["greve"] = {"sol": [("Greve Kommune, Byggesagsbehandling", "43 97 91 96", "gre_byg")],
                     "vp":  [("Greve Kommune, Natur og Miljø (varme)", "43 97 94 48 · varme@greve.dk", "gre_varme")]}

# ---------- daglig by-rutine 2. nov. 2026: Hjørring (DK1) og Holte/Rudersdal (DK2) ----------
S.update({
 "hjo_sol": ("Hjørring Kommune: solceller (individuelle anlæg)", "https://hjoerring.dk/borger/bolig/byggeri/solceller-individuelle-anlaeg"),
 "hjo_vpl": ("Hjørring Kommune: varmeplan og varmebreve", "https://hjoerring.dk/borger/bolig/energi/varmeplan-og-varmebreve"),
 "hjo_vpl22": ("Hjørring Kommune: Varmeplan 2022 (PDF)", "https://cdn.hjoerring.dk/hjoerringkommune/Media/638054784607057193/Varmeplan%202022.pdf"),
 "hjv_status": ("Hjørring Varmeforsyning: status for fjernvarme til omkringliggende byer (læst 2/11 2026)", "https://www.hjvarme.dk/ny-kunde/bliv-fjernvarmekunde/status-for-fjernvarme-til-omkringliggende-byer/"),
 "hjv_tilslut": ("Hjørring Varmeforsyning: tilslutningsafgifter", "https://www.hjvarme.dk/priser/tilslutningsafgifter/"),
 "hjv_pris": ("Hjørring Varmeforsyning: varmepris 2024-2026", "https://www.hjvarme.dk/priser/varmepris/"),
 "df_haestrup": ("Dansk Fjernvarme 27/5 2026: overskudsvarmesamarbejde indgået i Vendsyssel (renseanlægget i Hæstrup)", "https://danskfjernvarme.dk/aktuelt/nyheder/2026/overskudsvarmesamarbejde-indgaaet-i-vendsyssel"),
 "df_hjv2026": ("Dansk Fjernvarme 5/11 2025: Hjørring Varmeforsyning hæver varmeprisen i 2026", "https://danskfjernvarme.dk/aktuelt/nyheder/2025/hjoerring-varmeforsyning-haever-varmeprisen-i-2026"),
 "rud_solvp": ("Rudersdal Kommune: hvis du vil have solceller eller varmepumpe", "https://rudersdal.dk/borger/bolig-og-byggeri/varme-og-energi/hvis-du-vil-have-solceller-eller-varmepumpe"),
 "rud_fjv": ("Rudersdal Kommune: status på fjernvarme i Rudersdal (læst 2/11 2026)", "https://rudersdal.dk/borger/bolig-og-byggeri/varme-og-energi/status-paa-fjernvarme-i-rudersdal"),
 "nf_holte": ("Norfors: til fjernvarmekunder i Norfors, Holte Fjernvarme", "https://norfors.dk/til-fjernvarmekunder-i-norfors-holte-fjernvarme"),
 "nf_takst26": ("Norfors: takstblad 1. januar 2026 (PDF)", "https://backend.norfors.dk/sites/default/files/2025-12/Norfors%20Takstblad%202026_0.pdf"),
 "nf_just26": ("Norfors: sådan justeres fjernvarmepriserne i 2026 (PDF)", "https://backend.norfors.dk/sites/default/files/2025-12/S%C3%A5dan%20justeres%20fjernvarmepriserne%20i%202026.pdf"),
})
CITIES["hjoerring"] = {
  "name": "Hjørring", "kommune": "Hjørring Kommune", "updated": ("2. november 2026", "2026-11-02"),
  "sol_intro": "Solceller i Hjørring: følger panelerne tagets hældning eller sidder parallelt med facaden, kræver de ikke byggetilladelse i Hjørring Kommune. Lokalplan, tinglyste servitutter og kommuneplanens rammer for solenergi skal dog overholdes, og anlæg på terræn kræver både byggetilladelse og landzonetilladelse. Her er reglerne, priserne og vejen til et tilbud.",
  "sol_facts": [
    ("Private solceller, der <strong>følger tagets hældning</strong> eller sidder parallelt med facaden, kræver ikke byggetilladelse i Hjørring Kommune.", ["hjo_sol"]),
    ("Anlægget skal overholde bygningsreglementet, <strong>lokalplanen, tinglyste servitutter</strong> og kommuneplanens generelle rammer for solenergianlæg.", ["hjo_sol"]),
    ("Strider anlægget mod lokalplan eller servitut, søger du <strong>dispensation</strong> via en planmæssig forespørgsel i Byg og Miljø eller på byggeri@hjoerring.dk.", ["hjo_sol"]),
    ("Solceller <strong>på terræn</strong> kræver byggetilladelse og landzonetilladelse, skal stå inden for ca. 20 m fra hovedbygningen og være antirefleksbehandlede.", ["hjo_sol"]),
  ],
  "sol_faq": [
    ("Skal jeg søge om lov til solceller på mit hus i Hjørring?", "Nej, ikke byggetilladelse, hvis panelerne følger tagets hældning eller sidder parallelt med facaden. Lokalplan, servitutter og kommuneplanens rammer for solenergi skal stadig overholdes, og anlægget skal indberettes til BBR, når det er sat op.", ["hjo_sol"]),
    ("Skal et batteri til mine solceller godkendes i Hjørring Kommune?", "Er der koblet et batterianlæg på over 20 kWh til solcellerne, kan det være omfattet af beredskabsloven og skal i høring hos Nordjyllands Beredskab. Kommunen står for høringen, så kontakt Team Byggeri.", ["hjo_sol"]),
  ],
  "vp_intro": "Luft til vand-varmepumpe i Hjørring: næsten to ud af tre huse i Hjørring Kommune har fjernvarme, men Hjørring Varmeforsyning har opgivet at føre fjernvarme ud til en række landsbyer, fordi en varmepumpe ifølge værket bliver billigere for husejeren. Her er status, priserne og tilskudsreglerne.",
  "vp_facts": [
    ("Hjørring Varmeforsyning har undersøgt fjernvarme til <strong>Skibsby, Vidstrup, Harken/Hæstrup Mølleby, Bjergby, Tornby, Horne og Ilbro</strong>, men har indstillet arbejdet.", ["hjv_status"]),
    ("Værket regnede med en engangsudgift på typisk <strong>150.000-180.000 kr.</strong> inkl. moms pr. ejendom for at konvertere fra naturgas, og ca. 200.000 kr. i alt med ændringerne i huset.", ["hjv_status"]),
    ("Ifølge Hjørring Varmeforsyning vil det derfor være <strong>billigere for den enkelte husejer at investere i en varmepumpe</strong> i de byer.", ["hjv_status"]),
    ("Alle boligejere i kommunen uden fjernvarme har fået et <strong>varmebrev</strong> med en boliganalyse, og der kommer ikke nye tilslutningspligtige områder.", ["hjo_vpl"]),
  ],
  "vp_faq": [
    ("Får Tornby, Horne og Bjergby fjernvarme?", "Ikke fra Hjørring Varmeforsyning foreløbig. Værket har indstillet arbejdet med fjernvarme til Skibsby, Vidstrup, Harken/Hæstrup Mølleby, Bjergby, Tornby, Horne og Ilbro, fordi kravet om 70 % tilslutning ikke vurderes realistisk, og en varmepumpe bliver billigere for den enkelte.", ["hjv_status"]),
    ("Er der tilslutningspligt til fjernvarme i Hjørring Kommune?", "Der kommer ikke nye tilslutningspligtige områder. I naturgasområder bortfalder tilslutningspligten, men i fjernvarmeområder med tilslutningspligt gælder den foreløbig stadig.", ["hjo_vpl"]),
  ],
}
CITIES["holte"] = {
  "name": "Holte", "kommune": "Rudersdal Kommune", "cross_name": "Rudersdal Kommune", "updated": ("2. november 2026", "2026-11-02"),
  "sol_intro": "Solceller i Holte: i Rudersdal Kommune kræver solceller ikke tilladelse fra Byplan, når huset ikke er fredet eller bevaringsværdigt (værdi 1-3), og anlægget overholder lokalplan, servitutter og bygningsreglementet. Ældre lokalplaner fra tidligere Søllerød kan dog regulere solanlæg. Her er reglerne, priserne og vejen til et tilbud.",
  "sol_facts": [
    ("Solceller kræver <strong>ikke tilladelse fra Byplan</strong>, når bygningen ikke er fredet eller bevaringsværdig med værdi 1-3, og anlægget overholder lokalplan, servitutter og bygningsreglementet.", ["rud_solvp"]),
    ("Er du omfattet af en <strong>ældre lokalplan fra før 2000</strong>, fx nr. 10, 31 eller 49 fra tidligere Søllerød Kommune, kan den regulere tagbelægning og solanlæg, så du skal søge dispensation.", ["rud_solvp"]),
    ("Dispensation og tilladelse til <strong>bevaringsværdige huse</strong> søges ved at skrive til byplan@rudersdal.dk med situationsplan, facadetegninger og datablad.", ["rud_solvp"]),
    ("Kommunen anbefaler materialer, der <strong>ikke er blanke eller reflekterende</strong>, og nogle lokalplaner forbyder reflekterende materialer.", ["rud_solvp"]),
  ],
  "sol_faq": [
    ("Skal jeg søge om lov til solceller på mit hus i Holte?", "Ikke hvis huset hverken er fredet eller bevaringsværdigt med værdi 1-3, ikke ligger i en fredning og anlægget overholder lokalplan eller byplanvedtægt, servitutter og bygningsreglementet. Ellers skal du skrive til Byplan i Rudersdal Kommune.", ["rud_solvp"]),
    ("Skal solceller meldes til BBR i Rudersdal Kommune?", "Ja. Kommunen beder dig anmelde opsætningen til BBR-afdelingen på BBR@rudersdal.dk.", ["rud_solvp"]),
  ],
  "vp_intro": "Luft til vand-varmepumpe i Holte: seks ud af ti huse i Rudersdal Kommune har naturgas, og i juni 2026 blev fjernvarmeprojekterne for Holte, Øverød, Gl. Holte, Nærum, Søllerød, Trørød og Skodsborg aflyst. Kommunen peger nu selv på varmepumper som alternativ. Her er status, priserne og tilskudsreglerne.",
  "vp_facts": [
    ("Projekterne <strong>\"Holte, Øverød\" og \"Gl. Holte, Nærum, Søllerød, Trørød og Skodsborg\"</strong> er formelt aflyst efter kommunalbestyrelsens møde 24. juni 2026.", ["rud_fjv"]),
    ("Norfors kan ikke levere mere varme fra Usserødværket, og der er ikke fundet <strong>realistiske placeringer til nye lokale varmepumpeanlæg</strong>.", ["rud_fjv"]),
    ("En varmepumpe af sædvanligt omfang kræver som udgangspunkt <strong>ikke byggetilladelse</strong>, og udedelen må stå tættere på skel end 2,5 m, hvis støjgrænsen overholdes.", ["rud_solvp"]),
    ("Skifter du kun olie- eller gasfyret til en varmepumpe, <strong>udløser det ikke tilslutningspligt</strong> til fjernvarme, og du skal ikke søge dispensation.", ["rud_fjv"]),
  ],
  "vp_faq": [
    ("Får Holte fjernvarme?", "Ikke foreløbig. Projektforslaget for Holte og Øverød og forslaget for Gl. Holte, Nærum, Søllerød, Trørød og Skodsborg er trukket tilbage, fordi Norfors ikke har fundet placeringer til de nødvendige lokale varmepumpeanlæg. Kommunen henviser til varmepumpe og andre varmekilder, og Varmepumpepuljen er åbnet igen.", ["rud_fjv"]),
    ("Skal jeg have byggetilladelse til en varmepumpe i Rudersdal Kommune?", "Som udgangspunkt nej. Ligger huset i et værdifuldt kulturmiljø, er det omfattet af en bevarende lokalplan, fredet eller bevaringsværdigt med værdi 1-3, skal du søge Byplan om tilladelse, og står udedelen for tæt på skel i forhold til højden, kræver den byggetilladelse.", ["rud_solvp"]),
  ],
}
CONTACTS["hjoerring"] = {"sol": [("Hjørring Kommune, Team Byggeri", "72 33 65 70 · byggeri@hjoerring.dk", "hjo_sol")],
                         "vp":  [("Hjørring Varmeforsyning", "96 24 15 00 · hv@hjvarme.dk", "hjv_tilslut")]}
CONTACTS["holte"] = {"sol": [("Rudersdal Kommune, Byplan", "46 11 25 00 · byplan@rudersdal.dk", "rud_solvp")],
                     "vp":  [("Rudersdal Kommune, Klima, Natur og Miljø", "46 11 24 00 · knm@rudersdal.dk", "rud_fjv")]}

# ---------- daglig by-rutine 3. nov. 2026: Nykøbing Falster/Guldborgsund (DK2) og Haderslev (DK1) ----------
S.update({
 "gul_faq": ("Guldborgsund Kommune: ofte stillede spørgsmål om byggetilladelse (kræver solceller en byggetilladelse?)", "https://www.guldborgsund.dk/borger/flytte-bo-og-bygge/byggetilladelse/ofte-stillede-spoergsmaal"),
 "gul_vpl": ("Guldborgsund Kommune: høring om forslag til Varmeplan 2025 (frist 26/3 2026)", "https://www.guldborgsund.dk/hoeringer/2026/hoering-forslag-til-varmeplan-2025"),
 "gfo_varme": ("Guldborgsund Forsyning: varme (forsyningsområde og kontakt)", "https://www.guldborgsundforsyning.dk/varme/"),
 "gfo_takst26": ("Guldborgsund Forsyning: alle takster 2026, varme (PDF)", "https://www.guldborgsundforsyning.dk/thogoagr/2025/11/Alle-takster-2026-varme.pdf"),
 "gfo_dekl25": ("Guldborgsund Varme A/S: fjernvarmedeklaration 2025 (PDF, 6/8 2026)", "https://www.guldborgsundforsyning.dk/thogoagr/2026/08/Fjernvarmedeklaration-2025.pdf"),
 "gul_lz": ("Guldborgsund Kommune: landzonetilladelse", "https://www.guldborgsund.dk/borger/flytte-bo-og-bygge/landzonetilladelse"),
 "had_sol": ("Haderslev Kommune: solceller", "https://www.haderslev.dk/service/bolig-og-byggeri/byggeri/solceller"),
 "had_fjv": ("Haderslev Kommune: fjernvarme, sådan rulles fjernvarmen ud (læst 3/11 2026)", "https://www.haderslev.dk/udvikling/udvikling-og-projekter/vi-udvikler-naturen-og-klimaet/opvarmning-af-boliger-og-erhvervsbygninger/fjernvarme"),
 "had_vpl": ("Haderslev Kommune: Varmeplan for gasområder 2022 (PDF)", "https://www.haderslev.dk/media/smlnv0lg/varmeplan-gasomraader_endelig-udgave.pdf"),
 "hfv_tid": ("Haderslev Fjernvarme: tidslinje for kampagneprisen (læst 3/11 2026)", "https://haderslev-fjernvarme.dk/information/udvidelsesplan/tidslinje"),
 "hfv_gf25": ("Haderslev Fjernvarme: generalforsamlingsfolder 24. april 2025 (PDF)", "https://haderslev-fjernvarme.dk/p/Haderslev%20Fjernvarme/Generalforsamling/Beretninger%20-%20GF-Folder/Generalforsamlingsfolder-2025.pdf"),
})
CITIES["nykoebing-falster"] = {
  "name": "Nykøbing Falster", "kommune": "Guldborgsund Kommune", "cross_name": "Guldborgsund Kommune", "updated": ("3. november 2026", "2026-11-03"),
  "sol_title": "Solceller Nykøbing Falster: regler, pris og tilbud | Energitjekket",
  "vp_title": "Varmepumpe Nykøbing Falster: luft til vand, tilskud | Energitjekket",
  "fv_title": "Fjernvarme eller varmepumpe i Nykøbing Falster? 2026 | Energitjekket",
  "sol_intro": "Solceller i Nykøbing Falster: på et parcel-, række- eller dobbelthus kræver solceller ikke byggetilladelse i Guldborgsund Kommune, når de følger tagets hældning og ikke øger lasten på taget med 5 % eller mere. Fladt tag, terræn og landzone kræver derimod tilladelse. Her er reglerne, priserne og vejen til et tilbud.",
  "sol_facts": [
    ("Solceller på et <strong>enfamilie-, række-, dobbelt- eller sommerhus</strong> kræver ikke byggetilladelse, når de følger tagets hældning og overholder bygningsreglementets afstands- og højdekrav.", ["gul_faq"]),
    ("Lastvirkningen fra panelerne skal holdes <strong>under 5 %</strong> i forhold til husets eksisterende dokumentation.", ["gul_faq"]),
    ("Solceller på <strong>fladt tag eller på terræn</strong> kræver byggetilladelse i Guldborgsund Kommune.", ["gul_faq"]),
    ("Ligger ejendommen i <strong>landzone</strong>, kræver solcelleanlægget også en landzonetilladelse.", ["gul_faq"]),
  ],
  "sol_faq": [
    ("Skal jeg søge om lov til solceller på mit hus i Nykøbing Falster?", "Ikke byggetilladelse, hvis panelerne følger tagets hældning, lasten holdes under 5 %, og bygningsreglementets krav til afstand og højde, lokalplanen og tinglyste servitutter overholdes. Du skal selv sørge for at få anlægget registreret i BBR.", ["gul_faq"]),
    ("Hvem kontakter jeg om solceller i Guldborgsund Kommune?", "Bolig & Byggesag i Center for Teknik & Miljø på 54 73 20 95 i telefontiden (mandag-onsdag kl. 9-11, torsdag kl. 14-16, fredag kl. 9-11).", ["gul_faq"]),
  ],
  "vp_intro": "Luft til vand-varmepumpe i Nykøbing Falster: Danmarks Statistik registrerer ingen huse med naturgas i Guldborgsund Kommune, men mange med oliefyr og elvarme. Kommunens forslag til Varmeplan 2025 vil udfase oliefyrene og anbefaler grønne individuelle løsninger, hvor fjernvarme ikke kan nå ud. Her er status, priserne og tilskudsreglerne.",
  "vp_facts": [
    ("Forslaget til <strong>Varmeplan 2025</strong> erstatter varmeplanen fra 2010 og var i høring til 26. marts 2026.", ["gul_vpl"]),
    ("Fjernvarmen i de fleste byer og større landsbyer skal <strong>bevares og udbygges</strong>, og uden for fjernvarmeområderne skal oliefyrene udfases.", ["gul_vpl"]),
    ("I de mindre landsbyer åbner planen for <strong>lokale energifællesskaber</strong> med fælles varmeløsninger baseret på vedvarende energi.", ["gul_vpl"]),
    ("Hvor fjernvarme eller fælles løsninger ikke kan realiseres, anbefaler kommunen <strong>individuelle grønne løsninger</strong>, fx en varmepumpe.", ["gul_vpl"]),
  ],
  "vp_faq": [
    ("Kommer der fjernvarme til min landsby i Guldborgsund Kommune?", "Forslaget til Varmeplan 2025 bevarer og udbygger fjernvarmen i de fleste byer og større landsbyer og åbner for lokale energifællesskaber i de mindre landsbyer. Hvor fjernvarme eller en fælles løsning ikke kan realiseres, anbefaler kommunen en individuel grøn løsning.", ["gul_vpl"]),
    ("Hvor kan Guldborgsund Varme levere fjernvarme?", "Guldborgsund Varme forsyner ca. 7.000 kunder i Nykøbing F., Ønslev, Eskilstrup, Ovstrup, Gundslevmagle og Systofte. Andre byer i kommunen, fx Sakskøbing, Nysted og Stubbekøbing, har egne værker.", ["gfo_varme", "ft_pris"]),
  ],
}
CITIES["haderslev"] = {
  "name": "Haderslev", "kommune": "Haderslev Kommune", "updated": ("3. november 2026", "2026-11-03"),
  "sol_intro": "Solceller i Haderslev: på et parcel-, tofamilie-, række- eller sommerhus kræver solceller ikke byggetilladelse i Haderslev Kommune, når de følger tagets hældning og holder mindst 2,5 m til skel. Panelerne tæller med i bygningshøjden, og lokalplaner og deklarationer kan forbyde dem. Her er reglerne, priserne og vejen til et tilbud.",
  "sol_facts": [
    ("Private solceller på <strong>enfamilie-, tofamilie-, række- og sommerhuse</strong> kræver hverken byggetilladelse eller anmeldelse, når de følger tagets hældning og står mindst 2,5 m fra skel.", ["had_sol"]),
    ("Panelerne skal <strong>medregnes i bygningshøjden</strong>, som stadig skal være overholdt.", ["had_sol"]),
    ("Lokalplaner, byplanvedtægter og tinglyste deklarationer kan <strong>regulere eller forbyde</strong> solceller.", ["had_sol"]),
    ("Opsætningen skal <strong>altid registreres i BBR</strong> på bbr@haderslev.dk, også når den ikke kræver byggetilladelse.", ["had_sol"]),
  ],
  "sol_faq": [
    ("Skal jeg søge om lov til solceller på mit hus i Haderslev?", "Nej, ikke på et privat enfamilie-, tofamilie-, række- eller sommerhus, når panelerne følger tagets hældning, står mindst 2,5 m fra skel og overholder bygningshøjden. Er huset fredet eller bevaringsværdigt, eller står anlægget på terræn, kræver det byggetilladelse.", ["had_sol"]),
    ("Kan mit tag bære solceller?", "Haderslev Kommune anbefaler, at en professionel rådgiver gennemgår, om tagkonstruktionen kan bære vægten. Hører taget til en højere konstruktionsklasse end 1, skal en certificeret rådgiver tilknyttes.", ["had_sol"]),
  ],
  "vp_intro": "Luft til vand-varmepumpe i Haderslev: hvert fjerde hus i Haderslev Kommune har naturgas, og fjernvarmen rulles kun ud i Haderslev, Vojens og Gram. Fjernvarmeselskaberne ser ikke mulighed for at nå lokalbyerne med naturgas, så her anbefaler kommunen varmepumpe, jordvarme eller en fælles løsning. Her er status, priserne og tilskudsreglerne.",
  "vp_facts": [
    ("Ca. <strong>4.135 boliger</strong> i Haderslev, Vojens og Gram får efter planen mulighed for fjernvarme inden udgangen af 2026, ca. 40 % af kommunens boliger med gas eller olie.", ["had_fjv"]),
    ("Fjernvarmeselskaberne ser <strong>ikke mulighed for at tilbyde fjernvarme</strong> til lokalbyer og mindre bysamfund med naturgas. Undtagelsen er Marstrup, hvor fjernvarmen kan etableres, hvis 85 % af ejendommene tilslutter sig frivilligt.", ["had_fjv"]),
    ("Uden for udvidelsesprojekterne anbefaler kommunen som udgangspunkt <strong>individuelle varmepumper, jordvarme eller biomasse</strong> i stedet for naturgassen.", ["had_vpl"]),
    ("Lokal fjernvarme eller <strong>termonet</strong> kan være en mulighed i nogle områder, men det forudsætter et markant lokalt engagement.", ["had_vpl"]),
  ],
  "vp_faq": [
    ("Får min landsby i Haderslev Kommune fjernvarme?", "Sandsynligvis ikke fra de tre fjernvarmeselskaber. De har vurderet, at de ikke kan tilbyde fjernvarme uden for de godkendte udvidelsesprojekter i Haderslev, Vojens og Gram, fordi områderne ligger for langt væk eller har for få olie- og gasfyr. Kommunen peger på varmepumpe, jordvarme, biomasse eller en fælles løsning.", ["had_fjv", "had_vpl"]),
    ("Kan jeg risikere at blokere for fjernvarmen, hvis jeg køber varmepumpe?", "Ja, det advarer Haderslev Kommune om: udbredelsen af fjernvarme kan blive forhindret, hvis for mange i et kommende fjernvarmeområde vælger varmepumpe. Ligger du i et af udvidelsesområderne, så tal med fjernvarmeselskabet først.", ["had_fjv"]),
  ],
}
CONTACTS["nykoebing-falster"] = {"sol": [("Guldborgsund Kommune, Bolig & Byggesag", "54 73 20 95", "gul_faq")],
                                 "vp":  [("Guldborgsund Forsyning (Guldborgsund Varme)", "72 44 12 12 · forbrug@guldborgsundforsyning.dk", "gfo_varme")]}
CONTACTS["haderslev"] = {"sol": [("Haderslev Kommune, Teknik og Klima", "74 34 34 34 · bbr@haderslev.dk (BBR)", "had_sol")],
                         "vp":  [("Haderslev Fjernvarme", "74 52 21 88 · info@haderslev-fjernvarme.dk", "hfv_tid")]}

# ---------- daglig by-rutine 4. nov. 2026: Frederikshavn (DK1) og Hedensted (DK1) ----------
S.update({
 "fre_sol": ("Frederikshavn Kommune: grøn energi, solcelleanlæg og solfangere (læst 4/11 2026)", "https://frederikshavn.dk/borger/bolig-og-byggeri/skal-du-bygge/groen-energi"),
 "fre_scr": ("Frederikshavn Kommune: screening af varmeområdet 2022 (PDF, 26/10 2022)", "https://frederikshavn.viewer.dkplan.niras.dk/media/710662/screening-af-varmeomraadet-i-frederikshavn-kommune-_2022.pdf"),
 "ffv_varme": ("Frederikshavn Forsyning: fjernvarme og varmekilder", "https://www.forsyningen.dk/varme"),
 "ffv_pris": ("Frederikshavn Forsyning: priser på fjernvarme 2026", "https://www.forsyningen.dk/varme/priser"),
 "ffv_faa": ("Frederikshavn Forsyning: få fjernvarme (tilslutningspris)", "https://www.forsyningen.dk/varme/faa-fjernvarme/faa-fjernvarme"),
 "ffv_aar25": ("Frederikshavn Varme A/S: årsrapport 2025 (PDF)", "https://www.forsyningen.dk/media/xkgncbwc/frederikshavn-varme-a_s-underskrevet-aarsrapport-for-2025.pdf"),
 "hed_sol": ("Hedensted Kommune: solceller (læst 4/11 2026)", "https://www.hedensted.dk/service-og-selvbetjening/affald-bolig-og-miljoe/energi/solceller"),
 "hed_fjv": ("Hedensted Kommune: fjernvarme (læst 4/11 2026)", "https://www.hedensted.dk/service-og-selvbetjening/affald-bolig-og-miljoe/energi/fjernvarme"),
 "hed_red": ("Hedensted Kommune: forvaltningens oplæg til reduktionsområdet, klimaplan (dagsorden 2/9 2026, bilag 6, PDF)", "https://www.hedensted.dk/Agenda/GetFile?fileName=Punkt+105+-+Bilag+6+-+Bilag+6+-+Reduktionsopl%C3%A6g&filePath=%2Fdagsorden%2F2026UKlima%2F02-09-2026%2FDagsorden%28ID551%29%2FBilag%2FPunkt_105_Bilag_6_Bilag+6+-+Reduktionsoplaeg.pdf"),
 "hfj_pris": ("Hedensted Fjernvarme: priser og prisstigning pr. 1/11 2026", "https://hedensted-fjernvarme.dk/oekonomi/priser"),
 "hfj_spild": ("Hedensted Fjernvarme: i 2027 bliver dit spildevand til billig fjernvarme", "https://hedensted-fjernvarme.dk/nyheder/i-2027-bliver-dit-spildevand-til-billig-fjernvarme"),
 "hfj_miljo": ("Hedensted Fjernvarme: miljø og grøn omstillingsplan", "https://hedensted-fjernvarme.dk/om-os/om-os/miljoe"),
 "df_daug": ("Dansk Fjernvarme: Hedensted Fjernvarme kobler 330 nye forbrugere på (23/6 2025)", "https://danskfjernvarme.dk/aktuelt/nyheder/2025/hedensted-fjernvarme-kobler-330-nye-forbrugere-paa-fjernvarmen"),
})
CITIES["frederikshavn"] = {
  "name": "Frederikshavn", "kommune": "Frederikshavn Kommune", "updated": ("4. november 2026", "2026-11-04"),
  "vp_title": "Varmepumpe Frederikshavn: luft til vand og tilskud | Energitjekket",
  "fv_title": "Fjernvarme eller varmepumpe i Frederikshavn? 2026 | Energitjekket",
  "reg_title": "Solceller Frederikshavn: regler og byggetilladelse | Energitjekket",
  "sol_intro": "Solceller i Frederikshavn: på taget af dit hus kræver solceller som udgangspunkt ikke byggetilladelse i Frederikshavn Kommune, når anlægget overholder bygningsreglementets højde- og afstandskrav. Stativer på jorden, bevaringsværdige og fredede huse og ejendomme inden for bygge- og naturbeskyttelseslinjer kræver tilladelse. Her er reglerne, priserne og vejen til et tilbud.",
  "sol_facts": [
    ("Solceller på taget kræver som udgangspunkt <strong>ikke byggetilladelse</strong>, når anlægget overholder bygningsreglementets højde- og afstandskrav. Stativer eller bærebeslag, der vinkler panelerne op fra tagfladen, kan udløse krav om tilladelse.", ["fre_sol"]),
    ("Anlæg på <strong>stativer på jorden</strong> og på etageboliger, erhvervsbygninger og landbrugsbygninger med dyrehold kræver byggetilladelse.", ["fre_sol"]),
    ("<strong>Bevaringsværdige og fredede</strong> ejendomme og ejendomme inden for bygge- og naturbeskyttelseslinjer kræver også byggetilladelse.", ["fre_sol"]),
    ("Kræver anlægget ikke tilladelse, skal du stadig sende <strong>areal og ydelse til BBR</strong>, når det er sat op.", ["fre_sol"]),
  ],
  "sol_faq": [
    ("Skal jeg søge om lov til solceller på mit hus i Frederikshavn?", "Som udgangspunkt ikke, når panelerne ligger på taget og overholder bygningsreglementets højde- og afstandskrav. Har lokalplanen, byplanvedtægten eller en tinglyst deklaration regler om solceller, tagmaterialer eller refleksioner, kan det kræve dispensation. Det spørger du om i Byg og Miljø som en 'Planmæssig forespørgsel'.", ["fre_sol"]),
    ("Hvem kontakter jeg om solceller i Frederikshavn Kommune?", "Byg i Center for Teknik og Miljø på 98 45 63 98. Skal du søge byggetilladelse, vælger du 'Faste konstruktioner, som ikke er en bygning' i Byg og Miljø.", ["fre_sol"]),
  ],
  "vp_intro": "Luft til vand-varmepumpe i Frederikshavn: næsten to ud af tre huse i Frederikshavn Kommune har fjernvarme, men byer som Ålbæk, Jerup, Kvissel og Ravnshøj er udlagt til naturgas, og kommunens varmescreening fra 2022 fandt ingen økonomi i at føre fjernvarme dertil. Her er status, priserne og tilskudsreglerne.",
  "vp_facts": [
    ("I kommunens <strong>naturgas-byer</strong> skal ejendommene senest i 2035 omstilles til en anden varmeforsyning, skriver varmescreeningen fra 2022.", ["fre_scr"]),
    ("I <strong>Ålbæk</strong> havde 497 af 883 ejendomme naturgas ifølge BBR-tallene i screeningen. Med ca. 20 km til både Skagen og Frederikshavn var det ikke økonomisk fordelagtigt at føre fjernvarme dertil.", ["fre_scr"]),
    ("Naturgasområderne i <strong>landområderne</strong> bliver ikke konverteret til fjernvarme. Her må ejendommene overgå til individuel opvarmning.", ["fre_scr"]),
    ("Frederikshavn Varmes <strong>4,8 km lange ringledning</strong>, som også kan forsyne Gærum, ventes sat i drift ultimo 2026.", ["ffv_aar25"]),
  ],
  "vp_faq": [
    ("Kommer der fjernvarme til Ålbæk eller Jerup?", "Ikke efter kommunens varmescreening fra 2022. Afstanden til Skagen Varmeværk, Strandby Varmeværk og Frederikshavn Varme gjorde det ikke økonomisk fordelagtigt at føre fjernvarme dertil. For Ålbæk peger screeningen på at afklare, om der er interesse for en fælles løsning, fx et eget fjernvarmenet med en stor varmepumpe.", ["fre_scr"]),
    ("Hvad laves fjernvarmen i Frederikshavn af?", "Frederikshavn Forsyning skriver, at affaldskraftvarmeværket står for ca. 30 % af varmen og varmepumpen på Vendsysselvej for ca. 35 %. Den sidste del kommer fra to kedelcentraler, der især bruges i de koldeste måneder, og en ny 20 MW elkedel blev færdig ultimo 2025.", ["ffv_varme", "ffv_aar25"]),
  ],
}
CITIES["hedensted"] = {
  "name": "Hedensted", "kommune": "Hedensted Kommune", "updated": ("4. november 2026", "2026-11-04"),
  "sol_intro": "Solceller i Hedensted: på taget af dit hus kræver solceller hverken byggetilladelse eller landzonetilladelse i Hedensted Kommune, når de følger tagets hældning uden stativ, ikke er af reflekterende materiale og kun forsyner din egen ejendom. Anlæg på stativ på jorden kræver tilladelse. Her er reglerne, priserne og vejen til et tilbud.",
  "sol_facts": [
    ("Solceller på taget kræver <strong>hverken byggetilladelse eller landzonetilladelse</strong>, når de følger tagets hældning og ikke monteres på stativ.", ["hed_sol"]),
    ("Panelerne må <strong>ikke være af reflekterende materiale</strong>, anlægget skal overholde byggeretten og må kun forsyne din egen ejendom.", ["hed_sol"]),
    ("Et anlæg på <strong>stativ på jorden</strong> kræver byggetilladelse og i landzone også landzonetilladelse. Dér skal det stå højst 20 meter fra boligen og i samme terrænhøjde.", ["hed_sol"]),
    ("Når anlægget er sat op, skal du sende areal og ydeevne til <strong>BBR@Hedensted.dk</strong>.", ["hed_sol"]),
  ],
  "sol_faq": [
    ("Skal jeg søge om lov til solceller på mit hus i Hedensted?", "Nej, ikke når panelerne følger tagets hældning uden stativ, ikke reflekterer, overholder byggeretten og kun forsyner din egen ejendom, medmindre servitutterne eller lokalplanen siger noget andet. Er huset bevaringsværdigt eller fredet, så skriv til plan@hedensted.dk først.", ["hed_sol"]),
    ("Hvem kontakter jeg om solceller i Hedensted Kommune?", "Om byggetilladelse: byg@hedensted.dk eller 79 75 56 05. Om landzone: landskab@hedensted.dk. Om lokalplaner: plan@hedensted.dk eller 79 75 56 06.", ["hed_sol"]),
  ],
  "vp_intro": "Luft til vand-varmepumpe i Hedensted: hvert femte hus i Hedensted Kommune har allerede varmepumpe, og hvert femte har stadig naturgas. Af de fire byområder, som kommunens varmeplan fra 2022 pegede på til fjernvarme, er tre siden taget ud igen. Her er status, priserne og tilskudsreglerne.",
  "vp_facts": [
    ("Ifølge BBR var ca. <strong>9.180 boliger</strong> i Hedensted Kommune stadig opvarmet med naturgas, olie eller fast brændsel, da forvaltningen i september 2026 lagde op til en revideret klimaplan.", ["hed_red"]),
    ("Tre af de fire byområder, som <strong>varmeplanen fra 2022</strong> udpegede til fjernvarme, er siden taget ud, så kommunen ikke længere arbejder aktivt for fjernvarme dér. Borgerne kan stadig selv arbejde for det.", ["hed_red"]),
    ("Forvaltningen anbefaler at flytte målet om <strong>CO₂-neutral varmeforsyning fra 2030 til 2035</strong> og at lave en strategisk varmeplan i 2027.", ["hed_red"]),
    ("Et tilbud om fjernvarme er altid <strong>frivilligt</strong>: kommunen hverken kan eller vil tvinge nogen til at tilslutte sig.", ["hed_fjv"]),
  ],
  "vp_faq": [
    ("Kommer der fjernvarme til min by i Hedensted Kommune?", "Det afhænger af byen. Hedensted Fjernvarme har ført fjernvarme til Daugård, hvor projektet ventedes færdigt i 2026, men tre af de fire byområder fra varmeplanen 2022 er taget ud af planen. Vil I have fjernvarme, kan I kontakte et af kommunens fem fjernvarmeselskaber eller skrive til varme@hedensted.dk.", ["df_daug", "hed_red", "hed_fjv"]),
    ("Hvad koster fjernvarme hos Hedensted Fjernvarme fra november 2026?", "Fra 1. november 2026 er det variable bidrag 931,25 kr. pr. MWh og det faste bidrag 33,75 kr. pr. m² inkl. moms, en stigning på 9,6 % og 3,8 %. Priserne gælder også fra 1. januar 2027.", ["hfj_pris"]),
  ],
}
CONTACTS["frederikshavn"] = {"sol": [("Frederikshavn Kommune, Center for Teknik og Miljø, Byg", "98 45 63 98", "fre_sol")],
                             "vp":  [("Frederikshavn Forsyning, Varme", "98 29 90 00 · varme@forsyningen.dk", "ffv_faa")]}
CONTACTS["hedensted"] = {"sol": [("Hedensted Kommune, Byggeri", "79 75 56 05 · byg@hedensted.dk", "hed_sol")],
                         "vp":  [("Hedensted Kommune, klimasekretariatet", "varme@hedensted.dk", "hed_fjv")]}

# keyword-backlog 4/11 2026: Vejle (luft til luft) og Horsens (varmepumpe horsens) opdateret
CITIES["vejle"]["updated"] = ("4. november 2026", "2026-11-04"); CITIES["horsens"]["updated"] = ("4. november 2026", "2026-11-04")

# ---------- daglig by-rutine 5. nov. 2026: Ringkøbing (DK1, Ringkøbing-Skjern Kommune) og Helsingør (DK2) ----------
S.update({
 "rks_kp": ("Ringkøbing-Skjern Kommune: Kommuneplan 2021-2033, gældende retningslinjer for solceller (gengivet i forslag til tillæg nr. 46, 16/4 2024, PDF)", "https://www.rksk.dk/Edoc/Dagsordenspublicering/Teknik-%20og%20Milj%C3%B8udvalget/2024-08-20%2013.00/Dagsorden/Referat/Hjemmeside/2024-08-21%2015.03.23/Attachments/4131373-6509322-1.pdf"),
 "rks_byg": ("Ringkøbing-Skjern Kommune: byggeri og byggetilladelse (læst 5/11 2026)", "https://www.rksk.dk/borger/bolig-byggeri-og-flytning/byggeri-og-byggetilladelse"),
 "rks_varme": ("Ringkøbing-Skjern Kommune: varmeforsyning i landsbyer og landdistrikter, strategisk varmeplan (læst 5/11 2026)", "https://www.rksk.dk/om-kommunen/planer-og-kort/varmeinfo"),
 "rks_fjel": ("Ringkøbing-Skjern Kommune: udpegning af Fjelstervang til individuelle varmeløsninger (Klima-, Miljø- og Naturudvalget 9/6 2026, PDF)", "https://www.rksk.dk/Edoc/Dagsordenspublicering/Klima-,%20Milj%C3%B8-%20og%20Naturudvalget/2026-06-09%2013.00/Dagsorden/Referat/Hjemmeside/2026-06-10%2010.54.19/PDFs/e0bfca2b-771a-4dd6-829b-43b47125f30d.pdf"),
 "rks_svp": ("Ringkøbing-Skjern Kommune: strategisk varmeplan, byrådets beslutning 13/12 2022 (PDF)", "https://www.rksk.dk/Edoc/Dagsordenspublicering/Byr%C3%A5det/2022-12-13%2016.00/Dagsorden/Referat/Hjemmeside/2022-12-14%2010.21.32/PDFs/cb5b4b34-ec86-4374-8b55-af9b8580c603.pdf"),
 "df_rfv": ("Dansk Fjernvarme: Ringkøbing vinker farvel til gas (30/7 2025)", "https://danskfjernvarme.dk/aktuelt/nyheder/2025/ringkoebing-vinker-farvel-til-gas"),
 "rfv_pris": ("Ringkøbing Fjernvarme: priser og takstblad 2026 (også Tim Kraftvarmeværk)", "https://www.rfv.dk/priser/"),
 "df_hsfv": ("Dansk Fjernvarme: Hvide Sande, varmepris i vedvarende medvind (27/5 2026)", "https://danskfjernvarme.dk/aktuelt/nyheder/2026/hvide-sande-varmepris-i-vedvarende-medvind"),
 "hsfv_ned": ("Hvide Sande Fjernvarme: Hvide Sande Fjernvarme sænker prisen (pr. 1/4 2026)", "https://hsfv.dk/nyheder/hvide-sande-fjernvarme-saenker-prisen"),
 "hel_sol": ("Helsingør Kommune: energiløsninger, vejledning om solceller (læst 5/11 2026)", "https://www.helsingor.dk/borger/byggeri/nye-energiloesninger"),
 "fh_nye": ("Forsyning Helsingør: nye fjernvarmeområder", "https://www.fh.dk/varme/nye-fjernvarmeomraader"),
 "fh_status": ("Forsyning Helsingør: flere og flere kobles fortsat på fjernvarme (8/9 2026)", "https://www.fh.dk/nyheder/flere-og-flere-kobles-fortsat-paa-fjernvarme"),
 "fh_esp": ("Forsyning Helsingør: Espergærde C (udbygning 2023-2028)", "https://www.fh.dk/varme/nye-fjernvarmeomraader/espergaerde-c"),
 "fh_pris": ("Forsyning Helsingør: priser og tilslutning til fjernvarme", "https://www.fh.dk/varme/priser"),
})

# ---------- daglig by-rutine 6. nov. 2026: Stenløse (DK2, Egedal) og Frederikssund (DK2) ----------
S.update({
 "ege_sol": ("Egedal Kommune: solceller og solfangere (læst 6/11 2026)", "https://egedalkommune.dk/mit-liv/byggeri/solceller-og-solfangere"),
 "ege_fv": ("Egedal Fjernvarme: fjernvarme i Ølstykke og Stenløse, etape 11-20 (læst 6/11 2026)", "https://www.egedalfjernvarme.dk/vil-du-have-fjernvarme/igangvaerende-projekter/etape-11-20-oelstykke-og-stenloese"),
 "ege_pris": ("Egedal Fjernvarme: priser for 2026 og 2027 (læst 6/11 2026)", "https://www.egedalfjernvarme.dk/priser"),
 "frs_sol": ("Frederikssund Kommune: solfangere og solcelleanlæg (læst 6/11 2026)", "https://www.frederikssund.dk/Borger/Bolig--byggeri/din-ejendom/El-og-varme/Solfangere-og-solcelleanlaeg"),
 "frs_varme": ("Frederikssund Kommune: varme (læst 6/11 2026)", "https://www.frederikssund.dk/Borger/Bolig--byggeri/din-ejendom/El-og-varme/varme"),
 "frs_faq": ("Frederikssund Kommune: ofte stillede spørgsmål om varme (læst 6/11 2026)", "https://www.frederikssund.dk/Borger/Bolig--byggeri/din-ejendom/El-og-varme/varme/ofte-stillede-spoergsmaal-om-varme"),
 "frs_klima": ("Frederikssund Kommune: klimastatus juli 2026 (Teknik og Klima 11/8 2026, bilag)", "https://www.frederikssund.dk/Dagsordener/Teknik_og_Klima(2026)/11-08-2026/Dagsorden(ID5759)-2608121555/Bilag/Punkt_107_Bilag_3_KLIMASTATUS_JULI_2026.pdf"),
 "vf_energi": ("Vestforbrænding: kontrakt om energicentral på plads (26/5 2026)", "https://vestfor.dk/bliv-klogere/nyheder/nyhedsoverblik/kontrakt-om-energicentral-paa-plads"),
})
CITIES["ringkoebing"] = {
  "name": "Ringkøbing", "kommune": "Ringkøbing-Skjern Kommune", "cross_name": "Ringkøbing-Skjern", "updated": ("5. november 2026", "2026-11-05"),
  "vp_title": "Varmepumpe Ringkøbing: luft til vand og tilskud | Energitjekket",
  "fv_title": "Fjernvarme eller varmepumpe i Ringkøbing? 2026 | Energitjekket",
  "reg_title": "Solceller Ringkøbing-Skjern: regler og tilladelse | Energitjekket",
  "sol_intro": "Solceller i Ringkøbing: små anlæg på taget af dit hus kræver som udgangspunkt ikke tilladelse fra Ringkøbing-Skjern Kommune, men kommuneplanen siger, at panelerne skal have samme hældning som taget. I Ringkøbings indre by og ved Vedersø Klit kan bevarende lokalplaner forhindre solceller på bygningerne. Her er reglerne, priserne og vejen til et tilbud.",
  "sol_facts": [
    ("Mindre solcelleanlæg på <strong>tagflader</strong> kræver som udgangspunkt ikke tilladelse fra kommunen.", ["rks_kp"]),
    ("Panelerne skal have <strong>samme hældning som taget</strong> og nedfældes i tagfladen. Er panelets højde under 100 cm, må det dog anbringes på tagfladen.", ["rks_kp"]),
    ("Bygninger omfattet af en <strong>bevarende lokalplan</strong>, fx i den indre by i Ringkøbing og ved Vedersø Klit, kan være udelukket fra solceller på bygningen.", ["rks_kp"]),
    ("Solceller på <strong>terræn</strong> kræver tilladelse, og i sommerhusområder gives der som udgangspunkt ikke tilladelse til dem.", ["rks_kp"]),
  ],
  "sol_faq": [
    ("Skal jeg søge om lov til solceller på mit hus i Ringkøbing?", "Som udgangspunkt ikke, når anlægget ligger på taget og har samme hældning som taget. Ligger huset i et område med en bevarende lokalplan, fx i Ringkøbings indre by, så tjek lokalplanen først, fordi solceller på bygningen her kan være udelukket.", ["rks_kp"]),
    ("Hvem kontakter jeg om solceller i Ringkøbing-Skjern Kommune?", "Land, By og Kultur på 99 74 15 15 eller land.by.kultur@rksk.dk. Kommunen har midlertidigt telefontid om mandagen kl. 10-17 på byggesagsområdet.", ["rks_byg"]),
  ],
  "vp_intro": "Luft til vand-varmepumpe i Ringkøbing: tre ud af fem huse i Ringkøbing-Skjern Kommune har fjernvarme, og flere af værkerne her er blandt landets billigste. Uden for byerne har mange stadig oliefyr, og kommunens strategiske varmeplan peger i store dele af landområderne på individuelle løsninger. Her er status, priserne og tilskudsreglerne.",
  "vp_facts": [
    ("Kommunens <strong>strategiske varmeplan</strong> fra 13. december 2022 deler kommunen i fire kategorier: områder med fjernvarme, godkendt udrulning, potentiale for fjernvarme og områder, hvor individuelle løsninger eller mindre fællesanlæg er det primære.", ["rks_varme"]),
    ("<strong>I det åbne land</strong> kommer der ikke fjernvarme, skrev kommunen, da varmeplanen blev vedtaget. Her er det individuelle løsninger eller mindre fællesanlæg, der er de primære.", ["rks_svp"]),
    ("<strong>Fjelstervang</strong> blev i juni 2026 taget ud som muligt fjernvarmeområde, fordi projektet ikke fik tilslutning nok. Borgerne kan nu søge statslige tilskud til fx varmepumper.", ["rks_fjel"]),
    ("Kommunen har lavet <strong>varmescreeninger</strong> for en række landsbyer, bl.a. Hee, Stauning, Ølstrup, No og Vorgod-Barde.", ["rks_varme"]),
  ],
  "vp_faq": [
    ("Kan jeg få fjernvarme i min landsby i Ringkøbing-Skjern Kommune?", "Det afhænger af, hvilken kategori din by har i kommunens strategiske varmeplan. I gule områder kan fjernvarme komme, hvis der lokalt samles opbakning nok, mens kommunen i røde områder vurderer, at fjernvarme ikke er realistisk. Kommunen svarer på varme@rksk.dk.", ["rks_varme"]),
    ("Hvorfor blev der ikke fjernvarme i Fjelstervang?", "Projektet krævede, at mindst 75 % af borgerne gav bindende tilsagn om tilslutning, og den opbakning kom ikke. Foreningen bag blev nedlagt 16. marts 2026, og kommunen har derfor ændret varmeplanen, så borgerne kan søge tilskud til individuelle varmeløsninger.", ["rks_fjel"]),
  ],
}
CITIES["helsingoer"] = {
  "name": "Helsingør", "kommune": "Helsingør Kommune", "updated": ("5. november 2026", "2026-11-05"),
  "sol_intro": "Solceller i Helsingør: på et enfamiliehus, dobbelthus, rækkehus eller sommerhus er solceller undtaget fra byggetilladelse efter BR18, når anlægget overholder byggerettens højde- og afstandsbestemmelser og de brandmæssige løsninger, skriver Helsingør Kommune. En lokalplan kan dog kræve, at panelerne ikke reflekterer. Her er reglerne, priserne og vejen til et tilbud.",
  "sol_facts": [
    ("Solceller på <strong>enfamiliehuse, dobbelthuse, rækkehuse og sommerhuse</strong> er undtaget for byggetilladelse efter BR18 § 5, stk. 3, når byggerettens højde- og afstandsbestemmelser og de brandmæssige præ-accepterede løsninger er overholdt.", ["hel_sol"]),
    ("En <strong>lokalplan</strong> kan regulere reflekterende materialer, så du kun kan bruge solceller, der ikke reflekterer.", ["hel_sol"]),
    ("Solcelleanlæg på <strong>jorden</strong> kræver altid byggetilladelse, og fritstående anlæg i landzone kan som udgangspunkt ikke forvente landzonetilladelse.", ["hel_sol"]),
    ("Kommunens vejledning dækker kun bygge- og planloven. Reglerne for <strong>afregning</strong> med energiselskabet skal du selv sætte dig ind i.", ["hel_sol"]),
  ],
  "sol_faq": [
    ("Skal jeg søge om lov til solceller på mit hus i Helsingør?", "Som udgangspunkt ikke på et enfamiliehus, dobbelthus, rækkehus eller sommerhus, når anlægget overholder byggerettens højde- og afstandsbestemmelser og de brandmæssige løsninger. Tjek lokalplanen, fordi den kan kræve ikke-reflekterende paneler.", ["hel_sol"]),
    ("Hvem kontakter jeg om solceller i Helsingør Kommune?", "Center for By, Land og Vand på 49 28 28 28 eller blv@helsingor.dk.", ["hel_sol"]),
  ],
  "vp_intro": "Luft til vand-varmepumpe i Helsingør: næsten fire ud af ti huse i Helsingør Kommune har stadig naturgas, flere end der har fjernvarme. Forsyning Helsingør udbygger fjernvarmen i fem godkendte områder frem til 2028, og andre dele af Helsingør, Espergærde og Snekkersten kan tidligst komme i gang efter 2028. Her er status, priserne og tilskudsreglerne.",
  "vp_facts": [
    ("Helsingør Kommune godkendte i 2022 fem <strong>konverteringsområder</strong> fra naturgas til fjernvarme: Søhelte-kvarteret, Helsingør Bykerne, Marienlyst-kvarteret, Yderområder i Helsingør og Espergærde C.", ["fh_nye"]),
    ("Søhelte-kvarteret er færdigt. I Marienlyst-kvarteret er anlægsarbejdet under afslutning, og i bykernen og Yderområde 1 og 2 er det i gang (status september 2026).", ["fh_status"]),
    ("Forsyning Helsingør havde ved udgangen af juli 2026 etableret <strong>1.146 nye fjernvarmestik</strong> siden 2022.", ["fh_status"]),
    ("<strong>Yderligere dele af Helsingør, Espergærde og Snekkersten</strong> er med i de kommende planer, men kan tidligst sættes i gang efter 2028.", ["fh_nye", "fh_status"]),
  ],
  "vp_faq": [
    ("Kommer der fjernvarme til mit område i Helsingør?", "Frem til 2028 udbygger Forsyning Helsingør kun i de fem områder, byrådet allerede har godkendt. Andre dele af Helsingør, Espergærde og Snekkersten er med i de kommende planer, men tidligst efter 2028, og det kræver sund økonomi og tilslutning nok. Tjek din adresse på fh.dk, før du vælger.", ["fh_nye", "fh_status"]),
    ("Hvad koster det at få fjernvarme i Helsingør?", "Forsyning Helsingør tager 33.750 kr. for at tilslutte et enfamiliehus inkl. gravearbejde, stikledning og reetablering. Dertil kommer fjernvarmeenheden, som typisk koster 40.000-45.000 kr. hos en VVS'er, eller et abonnement til 350 kr. om måneden.", ["fh_pris"]),
  ],
}
CONTACTS["ringkoebing"] = {"sol": [("Ringkøbing-Skjern Kommune, Land, By og Kultur", "99 74 15 15 · land.by.kultur@rksk.dk", "rks_byg")],
                           "vp":  [("Ringkøbing-Skjern Kommune, varmeplan", "varme@rksk.dk", "rks_varme")]}
CONTACTS["helsingoer"] = {"sol": [("Helsingør Kommune, Center for By, Land og Vand", "49 28 28 28 · blv@helsingor.dk", "hel_sol")],
                          "vp":  [("Forsyning Helsingør", "48 40 50 50", "fh_nye")]}

CITIES["stenloese"] = {
  "name": "Stenløse", "kommune": "Egedal Kommune", "updated": ("6. november 2026", "2026-11-06"),
  "vp_title": "Varmepumpe Stenløse: luft til vand og tilskud | Energitjekket",
  "fv_title": "Fjernvarme eller varmepumpe i Stenløse? 2026 | Energitjekket",
  "reg_title": "Solceller Stenløse/Egedal: regler og tilladelse | Energitjekket",
  "sol_intro": "Solceller i Stenløse: Egedal Kommune skriver, at du selv skal sikre, at anlægget følger bygningsreglementet, lokalplanen og eventuelle deklarationer. Kræver lokalplanen eller en deklaration ikke-reflekterende tag, skal du søge dispensation. Anlæg på terræn kræver byggetilladelse. Her er reglerne, priserne og vejen til et tilbud.",
  "sol_facts": [
    ("Det er dit ansvar at sikre, at anlægget følger <strong>bygningsreglementet</strong>, lokalplanen og tinglyste deklarationer – også når der ikke kræves tilladelse.", ["ege_sol"]),
    ("Hvis lokalplanen eller en deklaration kræver en bestemt <strong>tagbelægning</strong> eller forbyder reflekterende materialer, skal du søge dispensation.", ["ege_sol"]),
    ("Solceller på <strong>terræn</strong> kræver byggetilladelse. Ansøgningen sker via Byg og Miljø under kategorien «Faste konstruktioner, som ikke er bygning».", ["ege_sol"]),
    ("Kommunen skal normalt sende ansøgningen i <strong>nabohøring</strong>, før den kan behandles.", ["ege_sol"]),
  ],
  "sol_faq": [
    ("Skal jeg søge om lov til solceller på mit hus i Stenløse?", "Ikke nødvendigvis på taget, hvis anlægget overholder bygningsreglementet og lokalplanen. Kræver lokalplanen eller en deklaration ikke-reflekterende tag, skal du søge dispensation. Anlæg på terræn kræver altid byggetilladelse.", ["ege_sol"]),
    ("Hvem kontakter jeg om solceller i Egedal Kommune?", "Byggesag på Dronning Dagmars Vej 200 i Ølstykke, telefon 72 59 72 60, eller via digital post til kommunen.", ["ege_sol"]),
  ],
  "vp_intro": "Luft til vand-varmepumpe i Stenløse: næsten fire ud af ti huse i Egedal Kommune har stadig naturgas, flere end der har fjernvarme. Egedal Fjernvarme udbygger i Ølstykke og Stenløse i etape 11-20, og tilmelder du dig i tide, kan tilslutningen i 2027 koste 15.000 kr. i stedet for 45.000 kr. Her er status, priserne og tilskudsreglerne.",
  "vp_facts": [
    ("Egedal Fjernvarme udbygger fjernvarmen i <strong>Ølstykke og Stenløse</strong> i etape 11-20. Flere etaper har afsluttet gravearbejde, andre er i gang eller indkalder til informationsmøde.", ["ege_fv"]),
    ("Tilmelder du dig, før gravearbejdet starter i dit delområde, kan du i 2027 blive tilsluttet til <strong>kampagnepris 15.000 kr.</strong> Normalprisen er 45.000 kr.", ["ege_fv"]),
    ("Fjernvarmeunit kan fås på <strong>abonnement</strong> til ca. 310 kr. om måneden i 2027 (A-model), eller du kan eje anlægget selv (E-model).", ["ege_fv"]),
    ("Danmarks Statistik registrerer <strong>6.166 huse med naturgas</strong> i Egedal Kommune i 2026 – flere end dem med fjernvarme.", ["dst_bol102"]),
  ],
  "vp_faq": [
    ("Kommer der fjernvarme til mit område i Stenløse eller Ølstykke?", "Egedal Fjernvarme udbygger i etape 11-20. Se oversigtskortet og tidsplanen på egedalfjernvarme.dk, og tilmeld dig, hvis du bor i et udvidelsesområde. Informationsmøde holdes typisk ca. seks måneder før gravestart.", ["ege_fv"]),
    ("Hvad koster det at få fjernvarme i Stenløse i 2027?", "Kampagnepris 15.000 kr., hvis du tilmelder dig, før gravearbejdet starter i dit delområde. Ellers 45.000 kr. Unit på abonnement koster ca. 310 kr. om måneden i 2027.", ["ege_fv"]),
  ],
}
CITIES["frederikssund"] = {
  "name": "Frederikssund", "kommune": "Frederikssund Kommune", "updated": ("6. november 2026", "2026-11-06"),
  "vp_title": "Varmepumpe Frederikssund: luft til vand og tilskud | Energitjekket",
  "fv_title": "Fjernvarme eller varmepumpe i Frederikssund? | Energitjekket",
  "reg_title": "Solceller Frederikssund: regler og tilladelse | Energitjekket",
  "sol_intro": "Solceller i Frederikssund: anlæg på hustage er omfattet af bygningsreglementet. Du skal søge, hvis anlægget ikke overholder højde- og afstandskrav, eller hvis lokalplan, byplanvedtægt eller servitut kræver dispensation. Anlæg på terræn kræver byggetilladelse. Her er reglerne, priserne og vejen til et tilbud.",
  "sol_facts": [
    ("Solenergianlæg på hustage er omfattet af <strong>bygningsreglementet</strong>. Du skal søge, hvis anlægget ikke ligger inden for højde- og afstandskravene, eller hvis det kræver dispensation fra lokalplan eller lignende.", ["frs_sol"]),
    ("Tjek <strong>lokalplan</strong>, byplanvedtægt og tinglyste servitutter for bestemmelser om tagmateriale og refleksion. Kommunens digitale kort viser lokalplaner.", ["frs_sol"]),
    ("Anlæg inden for <strong>fredning</strong> eller bygge- og beskyttelseslinjer (fx strand- eller fortidsmindebeskyttelse) kræver dispensation.", ["frs_sol"]),
    ("Fritstående anlæg på terræn, på erhvervsbygning, etagebolig eller landbrugsbygning kræver <strong>byggetilladelse</strong> via Byg &amp; Miljø. I landzone kan der også kræves landzonetilladelse.", ["frs_sol"]),
  ],
  "sol_faq": [
    ("Skal jeg søge om lov til solceller på mit hus i Frederikssund?", "Du skal søge, hvis anlægget ikke overholder bygningsreglementets højde- og afstandskrav, eller hvis lokalplan, byplanvedtægt eller servitut kræver dispensation. Anlæg på terræn kræver altid byggetilladelse.", ["frs_sol"]),
    ("Skal jeg give besked, når anlægget er sat op?", "Ja. Kommunen beder dig give besked, så anlægget kan registreres i BBR som teknisk anlæg.", ["frs_sol"]),
  ],
  "vp_intro": "Luft til vand-varmepumpe i Frederikssund: næsten fire ud af ti huse i kommunen har naturgas, mens kun ca. hvert fjerde har fjernvarme. Vestforbrænding planlægger udrulning i Frederikssund by, Græse Bakkeby, Vinge og St. Rørbæk senest 2030, mens Skibby og Slangerup tidligst kan være klar i 2032. Her er status, priserne og tilskudsreglerne.",
  "vp_facts": [
    ("Kommunens klimastatus juli 2026 forventer fjernvarme i <strong>Frederikssund by, Græse Bakkeby, Vinge og St. Rørbæk</strong> inden udgangen af 2030.", ["frs_klima"]),
    ("<strong>Skibby</strong> har et godkendt projektforslag, men Skibby Fjernvarme genberegner projektet i 2026. <strong>Slangerup</strong>: Vestforbrænding regner på fire scenarier, som præsenteres for borgerne sommeren 2026. Begge byer kan tidligst få fjernvarme i 2032, hvis projekterne fortsætter.", ["frs_klima"]),
    ("Vestforbrænding bygger en <strong>energicentral</strong> i Frederikssund med 19 MW elkedel og 8.500 m³ akkumuleringstank. Anlægsarbejde forventes i efteråret 2026, drift forår 2028, kapacitet til 2.000-2.700 standardhuse. Den skal også forsyne dele af Egedal.", ["vf_energi"]),
    ("Hvor fjernvarmen ikke kommer, opfordrer kommunen til <strong>individuelle varmepumper</strong> eller mindre fællesløsninger.", ["frs_faq"]),
  ],
  "vp_faq": [
    ("Kommer der fjernvarme til mit område i Frederikssund Kommune?", "Frederikssund by, Græse Bakkeby, Vinge og St. Rørbæk forventes klar inden udgangen af 2030. Skibby og Slangerup er usikre og tidligst 2032. Tjek kommunens kort og din adresse, før du vælger.", ["frs_klima", "frs_faq"]),
    ("Kræver en varmepumpe tilladelse i Frederikssund?", "Som udgangspunkt ikke for en luft til vand-varmepumpe. Jordvarme kræver tilladelse. Varmepumpen skal overholde støjgrænserne 35 dB om natten og 45 dB om dagen i skel.", ["frs_faq"]),
  ],
}
CONTACTS["stenloese"] = {"sol": [("Egedal Kommune, Byggesag", "72 59 72 60", "ege_sol")],
                          "vp":  [("Egedal Fjernvarme", "30 20 10 19 · adm@egedalfjernvarme.dk", "ege_fv")]}
CONTACTS["frederikssund"] = {"sol": [("Frederikssund Kommune, Byggeri", "47 35 10 00", "frs_sol")],
                             "vp":  [("Frederikssund Kommune, varme", "47 35 10 00", "frs_varme")]}

# ---------- daglig by-rutine 9. nov. 2026: Skanderborg (DK1) og Vordingborg (DK2) ----------
S.update({
 "skb_sol": ("Skanderborg Kommune: solcelleanlæg (læst 9/11 2026)", "https://www.skanderborg.dk/borger/flytte-bo-og-bygge/byggeri/solcelleanlaeg"),
 "skb_solsim": ("Skanderborg Kommune: solceller på tage og beregningsværktøj (læst 9/11 2026)", "https://www.skanderborg.dk/solceller"),
 "skb_varme": ("Skanderborg Kommune: varme i din bolig og strategisk varmeplan (læst 9/11 2026)", "https://www.skanderborg.dk/borger/flytte-bo-og-bygge/varme-i-din-bolig"),
 "skb_mesing": ("Klima-, Miljø- og Planudvalget, Skanderborg Kommune 4/11 2026: fjernvarme til Mesing (gengivet af Sagsvagt)", "https://sagsvagt.dk/sag/skanderborg-2026-11-04-klima-miljoe-og-planudvalget-6.html"),
 "vor_sol": ("Vordingborg Kommune: solceller (læst 9/11 2026)", "https://www.vordingborg.dk/borger/bolig-og-byggeri/byggeri-og-bbr/solceller-og-vindmoeller"),
 "vor_byg": ("Vordingborg Kommune: søg byggetilladelse (læst 9/11 2026)", "https://www.vordingborg.dk/borger/bolig-og-byggeri/byggeri-og-bbr/soeg-byggetilladelse"),
 "vor_varme": ("Vordingborg Kommune: varmeforsyning (læst 9/11 2026)", "https://www.vordingborg.dk/borger/bolig-og-byggeri/bolig-og-oekonomi/varmeforsyning"),
 "vor_ep": ("Vordingborg Kommune: Strategisk Energiplan 2023, del 2 – varmeforsyning (PDF)", "https://cdn.vordingborg.dk/vordingborgkommune/Media/638488539928581016/strategisk-energiplan-2023-del-2-af-3-varmeforsyning.pdf"),
 "vf_nyraad": ("Vordingborg Forsyning: fjernvarme til Nyråd, status (læst 9/11 2026)", "https://vordingborgforsyning.dk/projekter/@7/fjernvarme-til-nyr%C3%A5d"),
 "vf_nyraad_faq": ("Vordingborg Forsyning: spørgsmål og svar om fjernvarme i Nyråd (læst 9/11 2026)", "https://vordingborgforsyning.dk/fjernvarme/projekt-og-driftsinformation/fjernvarme-til-nyr%C3%A5d/sp%C3%B8rgsm%C3%A5l-og-svar"),
 "vf_oerslev": ("Vordingborg Forsyning: fjernvarme til Ørslev 2021-2024 (læst 9/11 2026)", "https://vordingborgforsyning.dk/fjernvarme/projekt-og-driftsinformation/fjernvarme-til-%C3%B8rslev"),
})
CITIES["skanderborg"] = {
  "name": "Skanderborg", "kommune": "Skanderborg Kommune", "updated": ("9. november 2026", "2026-11-09"),
  "vp_title": "Varmepumpe Skanderborg: luft til vand og tilskud | Energitjekket",
  "fv_title": "Fjernvarme eller varmepumpe i Skanderborg? | Energitjekket",
  "reg_title": "Solceller Skanderborg: regler og tilladelse | Energitjekket",
  "sol_intro": "Solceller i Skanderborg: på enfamiliehuse, dobbelthuse og sommerhuse kan du som regel sætte anlægget op uden at søge, hvis det følger tagets hældning, højst hæves 1 m over et fladt tag og overholder lokalplan og deklarationer. Forbyder lokalplanen blanke overflader, skal du søge dispensation. Her er reglerne, priserne og vejen til et tilbud.",
  "sol_facts": [
    ("Uden ansøgning på enfamiliehuse, dobbelthuse og sommerhuse, når anlægget <strong>følger tagets hældning</strong> og på flade tage højst hæves 1 m over tagfladen.", ["skb_sol"]),
    ("Tilladelse eller dispensation kræves, hvis lokalplan, byplanvedtægt eller deklaration har <strong>forbud mod blanke og reflekterende overflader</strong>, særlige bevaringskrav eller krav om indbygning i taget.", ["skb_sol"]),
    ("Fritstående anlæg på terræn over <strong>1,8 m</strong> kræver byggetilladelse, og på terræn skal anlægget som udgangspunkt holde 2,5 m til skel (5 m i sommerhusområder).", ["skb_sol"]),
    ("Nær skov, sø, å eller i fredede områder kan der kræves tilladelse efter naturbeskyttelsesloven. Kontakt Åben Land.", ["skb_sol"]),
  ],
  "sol_faq": [
    ("Skal jeg søge om lov til solceller på mit hus i Skanderborg?", "Som regel ikke, hvis anlægget følger tagets hældning (eller højst hæves 1 m på fladt tag) og overholder lokalplan, byplanvedtægt og deklarationer. Forbyder de blanke overflader eller kræver indbygning i taget, skal du søge dispensation.", ["skb_sol"]),
    ("Hvem kontakter jeg om solceller i Skanderborg Kommune?", "Byggesag på byggesag@skanderborg.dk eller telefon 87 94 77 03. Ligger huset nær skov, sø eller å, kontakt Åben Land på aabenland@skanderborg.dk.", ["skb_sol"]),
  ],
  "vp_intro": "Luft til vand-varmepumpe i Skanderborg: to ud af tre huse i kommunen har fjernvarme, men i landsbyer som Herskind, Låsby og Skovby syd er fjernvarmeprojekter stoppet på grund af for få tilmeldinger. Kommunens varmeplan peger på varmepumper og fælles løsninger uden for nettet. Her er status, priserne og tilskudsreglerne.",
  "vp_facts": [
    ("Kredsløb har forsøgt at give <strong>Herskind, Låsby, Galten syd og Skovby syd</strong> fjernvarme, men projekterne er stoppet på grund af for få tilmeldinger.", ["skb_varme"]),
    ("<strong>Dørup, Sjelle og Skjørring</strong> er ifølge den strategiske varmeplan ikke potentielle til fjernvarme. Voerladegård ligger for langt fra de eksisterende værker.", ["skb_varme"]),
    ("Skanderborg-Hørning Fjernvarme har søgt om at føre fjernvarme til <strong>Mesing</strong> (112 ejendomme). Projektet afhænger af en vindmølle og tilskud fra fjernvarmepuljen, og udvalget udsatte sagen 4. november 2026.", ["skb_mesing"]),
    ("Jordvarme kræver <strong>tilladelse</strong> af hensyn til grundvandet. Kommunen opfordrer til at vælge en støjsvag luft til vand-varmepumpe.", ["skb_varme"]),
  ],
  "vp_faq": [
    ("Kan jeg få fjernvarme i min landsby i Skanderborg Kommune?", "Tjek kommunens kort. Galten nord samt Skovby, Storring og Stjær har fået fjernvarme. Herskind, Låsby, Galten syd og Skovby syd er stoppet pga. for få tilmeldinger, og Dørup, Sjelle og Skjørring er ikke potentielle til fjernvarme.", ["skb_varme"]),
    ("Kræver en varmepumpe tilladelse i Skanderborg?", "En luft til vand-varmepumpe kræver normalt ikke tilladelse, men kommunen beder dig vælge en støjsvag model og tage hensyn til naboen. Jordvarme kræver tilladelse først.", ["skb_varme"]),
  ],
}
CITIES["vordingborg"] = {
  "name": "Vordingborg", "kommune": "Vordingborg Kommune", "updated": ("9. november 2026", "2026-11-09"),
  "vp_title": "Varmepumpe Vordingborg: luft til vand og tilskud | Energitjekket",
  "fv_title": "Fjernvarme eller varmepumpe i Vordingborg? | Energitjekket",
  "reg_title": "Solceller Vordingborg: regler og tilladelse | Energitjekket",
  "sol_intro": "Solceller i Vordingborg: på huse, sommerhuse, garager og udhuse kan anlægget sættes op uden ansøgning, når det følger tagets hældning. Du skal selv tjekke servitutter og lokalplaner og anmelde anlægget til BBR. Fredede og bevaringsværdige huse og anlæg på stativ kræver altid byggetilladelse. Her er reglerne, priserne og vejen til et tilbud.",
  "sol_facts": [
    ("Uden ansøgning på enfamiliehuse, sommerhuse, dobbelt- og rækkehuse, garager og udhuse, når anlægget <strong>følger tagets hældning</strong> – lagt oven på eller nedfældet i taget.", ["vor_sol"]),
    ("Du skal selv undersøge <strong>tinglyste servitutter og lokalplaner</strong>. Kommunen skriver, at mange lokalplaner har vilkår om solceller.", ["vor_sol"]),
    ("<strong>Fredede og bevaringsværdige bygninger</strong> og anlæg på stativ på fladt tag eller terræn kræver altid byggetilladelse – i landzone evt. også landzonetilladelse.", ["vor_sol"]),
    ("Anlægget skal <strong>anmeldes til BBR</strong>, også når det ikke kræver tilladelse.", ["vor_sol"]),
  ],
  "sol_faq": [
    ("Skal jeg søge om lov til solceller på mit hus i Vordingborg?", "Ikke hvis anlægget følger tagets hældning, og servitutter og lokalplan ikke forbyder det. Fredede og bevaringsværdige huse og anlæg på stativ eller terræn kræver altid byggetilladelse.", ["vor_sol"]),
    ("Hvem kontakter jeg om solceller i Vordingborg Kommune?", "Byggeri på telefon 55 36 24 50 (hverdage kl. 9-12) eller byg@vordingborg.dk. Lokalplaner og beskyttelseslinjer kan ses på KortVordingborg.", ["vor_byg"]),
  ],
  "vp_intro": "Luft til vand-varmepumpe i Vordingborg: kun hvert tredje hus i kommunen har fjernvarme, og andelen med elvarme og med oliefyr er blandt de højeste af byerne på Energitjekket. Kommunen forventer, at de fleste naturgasområder går over til individuel opvarmning, mens fjernvarmen udbygges i Nyråd, Stensved og dele af Præstø. Her er status, priserne og tilskudsreglerne.",
  "vp_facts": [
    ("Vordingborg Kommunes varmeplan forventer fjernvarme til <strong>Stensved og dele af Præstø</strong> frem mod 2028. Kun få andre naturgasområder har potentiale, så de forventes primært at overgå til individuel opvarmning.", ["vor_varme"]),
    ("I <strong>Nyråd</strong> forventer Vordingborg Forsyning, at en stor del af byen kan få fjernvarme omkring efteråret 2026. Der kan ikke søges tilskud til varmepumper i Nyråd, fordi området er udlagt til fjernvarme.", ["vf_nyraad_faq"]),
    ("Hvor der er tilslutningspligt uden fremført fjernvarme, skriver kommunen, at <strong>varmepumper er at foretrække</strong>, fordi huset senere kan omstilles til fjernvarme.", ["vor_varme"]),
    ("Kommunens energiplan anslår, at et skift til luft til vand eller jordvarme koster <strong>80.000-150.000 kr.</strong> afhængigt af husets størrelse og teknologi.", ["vor_ep"]),
  ],
  "vp_faq": [
    ("Kommer der fjernvarme til mit område i Vordingborg Kommune?", "Fjernvarme findes i Vordingborg by, Præstø, Stege, Lendemarke, Ørslev og Nyråd. Planen er udbygning til Stensved og dele af Præstø frem mod 2028. De fleste andre gas- og olieområder forventes at få individuel opvarmning, fx varmepumper.", ["vor_varme"]),
    ("Kan jeg få varmepumpetilskud i Nyråd?", "Nej. Vordingborg Forsyning skriver, at det ikke er muligt at søge tilskud til varmepumper i Nyråd, fordi området er udlagt som fjernvarmeområde.", ["vf_nyraad_faq"]),
  ],
}
CONTACTS["skanderborg"] = {"sol": [("Skanderborg Kommune, Byggesag", "87 94 77 03 · byggesag@skanderborg.dk", "skb_sol")],
                           "vp":  [("Skanderborg-Hørning Fjernvarme", "87 93 29 29 · cafe@skfj.dk", "skb_varme")]}
CONTACTS["vordingborg"] = {"sol": [("Vordingborg Kommune, Byggeri", "55 36 24 50 · byg@vordingborg.dk", "vor_byg")],
                           "vp":  [("Vordingborg Forsyning", "55 35 37 00 · kontakt@vordingborgforsyning.dk", "vf_nyraad")]}

# keyword-backlog 9/11 2026: 'energirenovering silkeborg'
S.update({
 "sil_groen": ("Silkeborg Kommune: sammen om grøn omstilling – energirenoveringer (læst 9/11 2026)", "https://silkeborg.dk/borger/klima-og-energi/sammen-om-groen-omstilling"),
 "se_raad": ("SparEnergi: gratis og uvildig energirådgivning til private (læst 9/11 2026)", "https://sparenergi.dk/privat/raadgivningen"),
})

# ---------- daglig by-rutine 10. nov. 2026: København (DK2) og Vejen (DK1) ----------
S.update({
 "kbh_sol": ("Københavns Kommune: solceller og byggetilladelse (læst 10/11 2026)", "https://www.kk.dk/borger/bolig-og-byggeri/byggetilladelse/byggetilladelse-trin-for-trin/solceller-og-byggetilladelse"),
 "kbh_solret": ("Københavns Kommune: arkitektoniske retningslinjer og gode eksempler på solceller (PDF, juli 2026)", "https://www.kk.dk/sites/default/files/2026-07/retningslinjer-eksempler-for-solcellerpdf-_1049.pdf"),
 "kbh_serv": ("Københavns Kommune: hvad er en servitut? (læst 10/11 2026)", "https://www.kk.dk/borger/bolig-og-byggeri/byggetilladelse/byggetilladelse-trin-for-trin/hvad-er-en-servitut"),
 "kbh_tilsl": ("Københavns Kommune: tilslutningspligt til fjernvarme og dispensationsmuligheder (læst 10/11 2026)", "https://www.kk.dk/borger/affald-og-miljoe/vand-varme-og-solceller/tilslutningspligt-til-fjernvarme-og-dispensationsmuligheder"),
 "hofor_vk": ("HOFOR: spørgsmål og svar om at blive varmeklar (læst 10/11 2026)", "https://www.hofor.dk/baeredygtige-byer/fremtidens-fjernvarme/bliv-varmeklar/spoergsmaal-og-svar-til-at-blive-varmeklar/"),
 "hofor_sk": ("HOFOR: stor varmepumpe i Sundkrogsgade (læst 10/11 2026)", "https://www.hofor.dk/baeredygtige-byer/fremtidens-fjernvarme/store-varmepumper/stor-varmepumpe-i-sundkrogsgade/"),
 "vjn_byg": ("Vejen Kommune: søg byggetilladelse – solenergi (læst 10/11 2026)", "https://vejen.dk/borger/bolig-byggeri-og-flytning/byggeri/soeg-byggetilladelse"),
 "vjn_fv": ("Vejen Kommune: fjernvarmeforsyning – værkerne i kommunen (læst 10/11 2026)", "https://vejen.dk/kontakt/akut-hjaelp/fjernvarmeforsyning"),
 "vjn_jels": ("Vejen Kommune, Økonomiudvalget 2/12 2025: Jels Varmes ansøgning om kommunegaranti (gengivet af Monrad)", "https://www.monrad.app/agenda_items/27089"),
 "vjn_jels2": ("Mig og Vejen 8/9 2026: Må droppe fjernvarmen (Jels)", "https://www.migogvejen.dk/byer/rodding/14229-ma-droppe-fjernvarmen"),
 "vjn_lands": ("Mig og Vejen 9/11 2022: Landsbyer skal selv", "https://www.migogvejen.dk/byer/holsted/7768-landsbyer-skal-selv"),
 "vjn_2035": ("Mig og Vejen 13/7 2022: Hvor skal varmen komme fra (Vejen Kommunes pressemeddelelse)", "https://migogvejen.dk/byer/vejen/7235-hvor-skal-varmen-komme-fra"),
})
CITIES["koebenhavn"] = {
  "name": "København", "kommune": "Københavns Kommune", "updated": ("10. november 2026", "2026-11-10"),
  # 94 % fjernvarme: ingen selvstændig varmepumpe-byside (som Aarhus)
  "vp_page": False,
  "sol_intro": "Solceller i København: på huse, carporte, garager og udhuse kan anlægget ofte sættes op uden byggetilladelse – men ikke hvis grunden er omfattet af lokalplan eller servitutter, eller huset er fredet eller bevaringsværdigt. Mange af byens villaområder har servitutter fra starten af 1900-tallet. Her er reglerne, priserne og vejen til et tilbud.",
  "sol_facts": [
    ("Byggetilladelse kræves, hvis anlægget ikke overholder bygningsreglementets <strong>højde- og afstandskrav</strong>, påvirker brand- eller konstruktionsforhold eller udløser en fornyet helhedsvurdering.", ["kbh_sol"]),
    ("Er grunden omfattet af <strong>lokalplan eller servitutter</strong>, eller er ejendommen fredet eller bevaringsværdig, skal du også have byggetilladelse.", ["kbh_sol"]),
    ("Mange af Københavns <strong>villaområder har servitutter</strong>, der blev tinglyst i starten af 1900-tallet for at holde områderne åbne og ensartede.", ["kbh_serv"]),
    ("Kommunens retningslinjer: panelerne skal så vidt muligt have <strong>samme farve som taget</strong>, være refleksfrie og holde afstand til tagkip og tagkant.", ["kbh_solret"]),
  ],
  "sol_faq": [
    ("Skal jeg søge byggetilladelse til solceller på mit hus i København?", "Ikke altid. Københavns Kommune kræver byggetilladelse, hvis anlægget bryder bygningsreglementets højde- og afstandskrav, påvirker brand- eller konstruktionsforhold, hvis grunden er omfattet af lokalplan eller servitutter, eller hvis huset er fredet eller bevaringsværdigt. Tjek din ejendom, før du bestiller.", ["kbh_sol"]),
    ("Hvem kontakter jeg om solceller i Københavns Kommune?", "Område for Bygninger, Njalsgade 13, på telefon 33 66 52 00 (hverdage kl. 9-16). Når anlægget er sat op, skal kommunen også have besked, så det kan registreres i BBR.", ["kbh_sol"]),
  ],
  "vp_intro": "Varmepumpe eller fjernvarme i København? 94 % af parcel- og rækkehusene i kommunen har fjernvarme. Enfamiliehuse må frit vælge en varmepumpe, men betaler stadig effektbidrag til HOFOR, hvis matriklen har tilslutningspligt. Her er priserne, HOFORs planer og regnestykket.",
  "vp_facts": [
    ("I København er der <strong>tilslutningspligt til fjernvarme</strong>. Enfamiliehuse og ejendomme med et varmebehov under 250 kW skal dog ikke aftage fjernvarmen og kan frit vælge fx en varmepumpe.", ["kbh_tilsl"]),
    ("Har matriklen tinglyst tilslutningspligt, skal du fortsat <strong>betale effektbidrag</strong> til HOFOR, også når du ikke aftager fjernvarme. Et nyt lavenergihus kan søge dispensation.", ["kbh_tilsl"]),
    ("HOFOR sænker gradvist temperaturen i fjernvarmenettet og forventer at være færdig i <strong>2033</strong>, så store eldrevne varmepumper kan bruges. Fremtidens net kører med 65 grader det meste af tiden og højst 75 grader på meget kolde dage.", ["hofor_vk"]),
    ("HOFOR vurderer, at ca. 70 % af de ca. 32.000 fjernvarmeanlæg fungerer fint efter en mindre justering, mens ca. 5 % – især i ejendomme fra før 1950 – kan få brug for større opgraderinger.", ["hofor_vk"]),
  ],
  "vp_faq": [
    ("Må jeg skifte fjernvarmen ud med en varmepumpe i København?", "Ja, hvis du har et enfamiliehus eller en ejendom med et varmebehov under 250 kW. Københavns Kommune skriver, at du frit kan vælge fx en varmepumpe. Har matriklen tinglyst tilslutningspligt, skal du dog stadig betale effektbidrag til HOFOR.", ["kbh_tilsl"]),
    ("Skal mit fjernvarmeanlæg skiftes, når HOFOR sænker temperaturen?", "Ikke nødvendigvis. HOFOR tester fra 2026 og sænker gradvist temperaturen bydel for bydel fra 2027. Kan anlægget varme huset op med 55 graders fremløb, når det er 0 grader udenfor, tegner det godt. Ellers anbefaler HOFOR en VVS'er med fjernvarmeordning. Ejeren betaler selv.", ["hofor_vk"]),
  ],
}
CITIES["vejen"] = {
  "name": "Vejen", "kommune": "Vejen Kommune", "updated": ("10. november 2026", "2026-11-10"),
  "sol_intro": "Solceller i Vejen: et anlæg til én familie på det eksisterende tag af en bolig kræver som udgangspunkt hverken byggetilladelse eller landzonetilladelse. Lokalplaner, fredninger eller naturbeskyttelsesloven kan dog kræve dispensation, og anlæg på terræn kræver byggetilladelse. Her er reglerne, priserne og vejen til et tilbud.",
  "sol_facts": [
    ("Solceller til brug for én familie på <strong>det eksisterende tag af en bolig</strong> kræver som udgangspunkt hverken byggetilladelse eller landzonetilladelse.", ["vjn_byg"]),
    ("<strong>Lokalplan, fredninger eller naturbeskyttelsesloven</strong> kan betyde, at du skal søge dispensation.", ["vjn_byg"]),
    ("Et <strong>fritstående anlæg på terræn</strong> eller på en erhvervs- eller landbrugsbygning kræver byggetilladelse, og kommunen kan stille vilkår om farve og refleksion.", ["vjn_byg"]),
    ("Solanlæg skal <strong>altid registreres i BBR</strong>.", ["vjn_byg"]),
  ],
  "sol_faq": [
    ("Skal jeg søge om lov til solceller på mit hus i Vejen?", "Som udgangspunkt ikke, når anlægget er til én familie og sidder på det eksisterende tag af en bolig. Lokalplan, fredning eller naturbeskyttelsesloven kan dog kræve dispensation, og anlæg på terræn kræver byggetilladelse.", ["vjn_byg"]),
    ("Hvordan søger jeg, hvis mine solceller kræver tilladelse i Vejen Kommune?", "Ansøgningen sendes via Byg & Miljø, hvor du også kan se, hvilke regler der gælder for din adresse. Vejen Kommunes hovednummer er 79 96 50 00.", ["vjn_byg", "vjn_fv"]),
  ],
  "vp_intro": "Luft til vand-varmepumpe i Vejen: kun 45 % af husene i kommunen har fjernvarme, og næsten hvert femte hus har stadig naturgas. I Jels er planerne om et nyt fjernvarmeselskab opgivet, så mange husejere i landsbyerne står med en individuel løsning. Her er status, priserne og tilskudsreglerne.",
  "vp_facts": [
    ("Fjernvarmen i kommunen leveres af fire værker: <strong>Varmega (tidl. Vejen Varmeværk), Holsted Varmeværk, Brørup Fjernvarme og Rødding Varmecentral</strong>.", ["vjn_fv"]),
    ("<strong>Jels Varme</strong> søgte om en kommunegaranti på op til 128,8 mio. kr. til fjernvarme i Jels. Økonomiudvalget anbefalede 2. december 2025 at afvise ansøgningen.", ["vjn_jels"]),
    ("En ny ansøgning blev ikke sendt til politisk behandling, og Jels Varme indkaldte til ekstraordinær generalforsamling 23. september 2026 med det formål at <strong>nedlægge selskabet</strong>.", ["vjn_jels2"]),
    ("Allerede i 2022 meldte kommunen ud, at <strong>13 landsbyer</strong>, der primært opvarmes med naturgas, ikke skal forvente kommunal hjælp til at skifte: ni af dem har mulighed for en fælles løsning, resten er for små.", ["vjn_lands"]),
  ],
  "vp_faq": [
    ("Kommer der fjernvarme til Jels?", "Ikke som det ser ud nu. Økonomiudvalget anbefalede i december 2025 at afvise kommunegarantien, en ny ansøgning blev ikke sendt videre til politisk behandling, og Jels Varme indkaldte i september 2026 til generalforsamling for at nedlægge selskabet. Husejerne står dermed med individuelle løsninger som varmepumpe.", ["vjn_jels", "vjn_jels2"]),
    ("Hvem leverer fjernvarme i Vejen Kommune?", "Varmega (tidl. Vejen Varmeværk) på 69 15 39 00, Holsted Varmeværk på 75 39 26 60, Brørup Fjernvarme på 75 38 13 20 og Rødding Varmecentral på 74 84 16 70.", ["vjn_fv"]),
  ],
}
CONTACTS["koebenhavn"] = {"sol": [("Københavns Kommune, Område for Bygninger", "33 66 52 00", "kbh_sol")],
                          "vp":  [("HOFOR, kundeservice", "33 95 33 95 · kundeservice@hofor.dk", "hofor_vk")]}
CONTACTS["vejen"] = {"sol": [("Vejen Kommune", "79 96 50 00", "vjn_byg")],
                     "vp":  [("Varmega (tidl. Vejen Varmeværk)", "69 15 39 00", "vjn_fv")]}

# ---------- daglig by-rutine 11. nov. 2026: Varde (DK1) og Faxe (DK2) ----------
S.update({
 "var_byg": ("Varde Kommune: byggeri – solceller og solfangere (læst 11/11 2026)", "https://vardekommune.dk/borger/bolig-og-byggeri/byggeri/"),
 "var_vpl": ("Varde Kommune: Varmeplan for Varde Kommune 2023-2030, vedtaget 6/12 2022 (PDF)", "https://vardekommune.dk/wp-content/uploads/2023/01/Varmeplan-for-Varde-Kommune-2023-2030.pdf"),
 "var_helle": ("Dansk Fjernvarme 18/7 2025: Fjernvarme til attraktiv pris på vej til Helle Energis forbrugere", "https://danskfjernvarme.dk/aktuelt/nyheder/2025/fjernvarme-til-attraktiv-pris-paa-vej-til-helle-energis-forbrugere"),
 "var_oks": ("Dansk Fjernvarme 16/6 2026: 30 år i fjernvarmen var ikke planlagt (Oksbøl Varmeværk)", "https://danskfjernvarme.dk/aktuelt/nyheder/2026/30-aar-i-fjernvarmen-var-ikke-planlagt"),
 "fax_sol": ("Faxe Kommune: solceller og solfangeranlæg (læst 11/11 2026)", "https://faxekommune.dk/da/borger/byggeri-bbr/solceller-solfangeranlaeg"),
 "fax_vp": ("Faxe Kommune: varmepumpe (læst 11/11 2026)", "https://faxekommune.dk/da/borger/byggeri-bbr/varmepumpe-0"),
 "fax_haslev": ("Faxe Kommune, Teknik- og Miljøudvalget: status på konvertering til fjernvarme i Haslev (2026, gengivet af Monrad)", "https://www.monrad.app/agenda_items/150739"),
 "fax_fl": ("Faxe Kommune, Byrådet 2026: omprioritering af midler fra fjernvarme i Faxe Ladeplads (gengivet af Monrad)", "https://www.monrad.app/agenda_items/114593"),
 "fax_es": ("Energy Supply 5/12 2023: Forsyning dropper fjernvarmeprojekter i tre gasbyer", "https://www.energy-supply.dk/article/view/1068779/forsyning_dropper_fjernvarmeprojekter_i_tre_gasbyer_fjerde_by_far_ny_chance"),
})
CITIES["varde"] = {
  "name": "Varde", "kommune": "Varde Kommune", "updated": ("11. november 2026", "2026-11-11"),
  "sol_intro": "Solceller i Varde: på enfamilie-, tofamilie-, række- og sommerhuse kan du som udgangspunkt sætte solceller op uden byggetilladelse og uden at anmelde det til kommunen – men anlægget tæller med i bygningshøjden, og lokalplaner og tinglyste deklarationer kan sætte grænser. Her er reglerne, priserne og vejen til et tilbud.",
  "sol_facts": [
    ("Solceller på <strong>enfamilie-, tofamilie-, række- og sommerhuse</strong> og tilhørende småbygninger kræver hverken byggetilladelse eller anmeldelse, når byggeloven er overholdt.", ["var_byg"]),
    ("Anlægget skal <strong>medregnes i bygningshøjden</strong>, som stadig skal overholdes.", ["var_byg"]),
    ("<strong>Lokalplaner, byplanvedtægter og tinglyste deklarationer</strong> kan regulere eller forbyde solceller.", ["var_byg"]),
    ("Kommunen anbefaler, at panelerne får <strong>samme hældning som taget</strong> og placeres harmonisk i forhold til kviste, tagvinduer og skorstene.", ["var_byg"]),
  ],
  "sol_faq": [
    ("Skal jeg søge byggetilladelse til solceller på mit hus i Varde?", "Som udgangspunkt ikke. Varde Kommune skriver, at solceller på enfamilie-, tofamilie-, række- og sommerhuse kan sættes op uden byggetilladelse eller anmeldelse, hvis byggeloven er overholdt – og anlægget tæller med i bygningshøjden. Tjek også lokalplan og tinglyste deklarationer.", ["var_byg"]),
    ("Hvad med solceller på jorden i Varde Kommune?", "Kommunen afgør selv, om et anlæg på terræn kræver byggetilladelse, så du skal altid sende projektmateriale til vurdering. Varde Kommune har telefon 79 94 68 00.", ["var_byg"]),
  ],
  "vp_intro": "Luft til vand-varmepumpe i Varde: Varde Kommune vil have alle olie- og naturgasfyr til privat opvarmning udfaset i 2030, og 8 % af husene har stadig oliefyr. Nogle landsbyer får fjernvarme, men resten skal finde en individuel løsning. Her er status, priserne og tilskudsreglerne.",
  "vp_facts": [
    ("Ifølge varmeplanen var der ca. <strong>4.100 oliefyr og 2.700 gasfyr</strong> i Varde Kommune, og ambitionen er, at alle olie- og naturgasfyr til privat opvarmning er udfaset i <strong>2030</strong>.", ["var_vpl"]),
    ("Områder, der hverken har fjernvarme eller er udpeget til kollektiv varme, anbefales at skifte til en <strong>individuel løsning som varmepumper</strong>.", ["var_vpl"]),
    ("<strong>Helle Energi</strong> skal levere fjernvarme til Nordenskov, Agerbæk, Fåborg, Næsbjerg, Årre og Starup-Tofterup fra seks små varmecentraler; ca. 1.300 husstande kan få fjernvarme i løbet af 2026 og 2027.", ["var_helle"]),
    ("Når et område er udpeget til kollektiv varme, og et projektforslag er godkendt, kan man ikke længere få tilskud fra Bygningspuljen til en varmepumpe.", ["var_vpl"]),
  ],
  "vp_faq": [
    ("Får min landsby fjernvarme i Varde Kommune?", "Det afhænger af byen. Oksbøl Varmeværk har konverteret Billum og Janderup, og Helle Energi bygger varmecentraler til seks byer i den gamle Helle Kommune. Varmeplanen anbefaler individuelle løsninger som varmepumper i de områder, der er for små eller ligger for langt fra et fjernvarmenet.", ["var_vpl", "var_oks", "var_helle"]),
    ("Hvor mange oliefyr er der i Varde Kommune?", "Varmeplanen fra 2022 nævner ca. 4.100 oliefyr og 2.700 gasfyr. Danmarks Statistik registrerer i 2026 oliefyr i ca. 8 % af de beboede parcel- og rækkehuse.", ["var_vpl", "dst_bol102"]),
  ],
}
CITIES["faxe"] = {
  "name": "Faxe", "kommune": "Faxe Kommune", "updated": ("11. november 2026", "2026-11-11"),
  "sol_intro": "Solceller i Faxe: et anlæg på taget kræver ikke tilladelse fra Faxe Kommune, når det sidder mere end 2,5 meter fra skel (5 meter i sommerhusområder). Lokalplaner, deklarationer og grundejerforeninger kan dog stille krav, og kommunen er åben for dispensation. Her er reglerne, priserne og vejen til et tilbud.",
  "sol_facts": [
    ("Solceller på bygninger kræver ikke tilladelse fra kommunen, når anlægget er <strong>mere end 2,5 m fra skel</strong> (5,0 m i sommerhusområde).", ["fax_sol"]),
    ("<strong>Byplanvedtægter, lokalplaner, deklarationer, grundejerforeningsvedtægter</strong>, fredning og beskyttelseslinjer kan forhindre et anlæg.", ["fax_sol"]),
    ("Flere lokalplaner kræver, at solceller er <strong>nedfældet i tagfladen</strong>, men kommunen vil se på dispensation ud fra konkrete ansøgninger.", ["fax_sol"]),
    ("Anlægget skal <strong>anmeldes til BBR</strong> med antal paneler, m² og kW, også når det ikke kræver tilladelse.", ["fax_sol"]),
  ],
  "sol_faq": [
    ("Skal jeg søge om lov til solceller på mit hus i Faxe Kommune?", "Ikke når anlægget sidder på bygningen mere end 2,5 m fra skel (5 m i sommerhusområder) og overholder bygningsreglementets højde- og afstandskrav. Lokalplan, deklarationer eller grundejerforeningens vedtægter kan dog kræve dispensation.", ["fax_sol"]),
    ("Hvem kontakter jeg om solceller i Faxe Kommune?", "Byg på byg@faxekommune.dk eller 56 20 30 30. Dispensation fra en lokalplan søges på plan@faxekommune.dk, og BBR har telefon 56 20 30 10.", ["fax_sol"]),
  ],
  "vp_intro": "Luft til vand-varmepumpe i Faxe: kun hvert femte hus i kommunen har fjernvarme, og næsten hvert tredje har naturgas. Fjernvarmeprojekterne i Faxe Ladeplads, Karise, Dalby og Rønnede er opgivet, så for de fleste gaskunder er en varmepumpe vejen væk fra gassen. Her er status, priserne og reglerne.",
  "vp_facts": [
    ("<strong>Faxe Ladeplads</strong> er ikke længere udlagt som muligt fjernvarmeområde. Kun 23 % af det opvarmede areal havde skrevet kontrakt, og målet var ca. 60-75 %.", ["fax_fl"]),
    ("Fjernvarmeprojekterne i <strong>Rønnede/Kongsted, Karise og Dalby</strong> blev droppet i 2023 på grund af for lille interesse.", ["fax_es"]),
    ("I Haslev er to af syv fjernvarmeprojekter gennemført, to har ikke nået de krævede <strong>60 % tilslutning</strong>, og tre venter på en tilslutningsundersøgelse.", ["fax_haslev"]),
    ("En luft til luft- eller luft til vand-varmepumpe kræver som regel ikke tilladelse, men i <strong>rækkehuse</strong>, bevaringsværdige huse og ved jordvarme skal du kontakte kommunen først.", ["fax_vp"]),
  ],
  "vp_faq": [
    ("Kræver en varmepumpe tilladelse i Faxe Kommune?", "Som regel ikke. Du skal dog kontakte kommunens byggesagsafdeling, hvis det er jordvarme, hvis huset er bevaringsværdigt eller ligger i en bevarende lokalplan, hvis du bor i en rækkehusbebyggelse, eller hvis varmepumpen skal stå inden for en beskyttelseslinje.", ["fax_vp"]),
    ("Hvor meget må en varmepumpe støje i Faxe?", "Faxe Kommune skriver, at støjen højst må være 35 dB ved skel til naboen om natten. Kommer der klager, kan kommunen give påbud om at dæmpe støjen.", ["fax_vp"]),
  ],
}
CONTACTS["varde"] = {"sol": [("Varde Kommune", "79 94 68 00 · vardekommune@varde.dk", "var_byg")],
                     "vp":  [("Varde Kommune", "79 94 68 00 · vardekommune@varde.dk", "var_byg")]}
CONTACTS["faxe"] = {"sol": [("Faxe Kommune, Byg", "56 20 30 30 · byg@faxekommune.dk", "fax_sol")],
                    "vp":  [("Faxe Kommune, Byg", "56 20 30 30 · byg@faxekommune.dk", "fax_sol")]}

# ---------- daglig by-rutine 12. nov. 2026: Kalundborg (DK2) og Skive (DK1) ----------
S.update({
 "kal_byg": ("Kalundborg Kommune: byggetilladelser (læst 12/11 2026)", "https://www.kalundborg.dk/service-and-selvbetjening/bolig-and-byggeri/byggeri/byggetilladelser"),
 "kal_sbt": ("Kalundborg Kommune: sagsbehandlingstider for byggeansøgninger (læst 12/11 2026)", "https://www.kalundborg.dk/service-and-selvbetjening/bolig-and-byggeri/byggeri/byggetilladelser/sagsbehandlingstider"),
 "kal_lp": ("Kalundborg Kommune: lokalplaner og byplanvedtægter (læst 12/11 2026)", "https://www.kalundborg.dk/demokrati/planer-politikker-og-strategier/lokalplaner-og-byplanvedtaegter"),
 "kal_jv": ("Kalundborg Kommune: jordvarme (læst 12/11 2026)", "https://www.kalundborg.dk/service-and-selvbetjening/bolig-and-byggeri/bygningsvedligehold/jordvarme"),
 "kal_tv": ("TV-Kalundborg: Hvem skal betale for kuldsejlet projekt? (fjernvarme i Gørlev og Kirke Helsinge)", "https://tv-kalundborg.dk/nyheder/hvem-skal-betale-for-kuldsejlet-projekt/"),
 "kal_ff": ("Kalundborg Forsyning: om fjernvarme (læst 12/11 2026)", "https://kalfor.dk/fjernvarme/om-fjernvarme"),
 "kal_tf": ("Kalundborg Forsyning: tilslutning til fjernvarme (læst 12/11 2026)", "https://kalfor.dk/selvbetjening/tilslutning-fjernvarme"),
 "ski_sol": ("Skive Kommune: opsætning af solenergianlæg (læst 12/11 2026)", "https://skive.dk/erhverv/erhvervsaffald-forsyning-og-miljoe/forsyning/solenergianlaeg/"),
 "ski_ind": ("Skive Kommune: individuel varmeforsyning (læst 12/11 2026)", "https://skive.dk/borger/natur-miljoe-og-klima/varmeforsyning/individuel-varmeforsyning/"),
 "ski_kol": ("Skive Kommune: kollektiv varmeforsyning og termonet (læst 12/11 2026)", "https://skive.dk/borger/natur-miljoe-og-klima/varmeforsyning/kollektiv-varmeforsyning/"),
 "ski_lok": ("Skive Kommune: lokale initiativer om kollektiv varme (læst 12/11 2026)", "https://skive.dk/borger/natur-miljoe-og-klima/varmeforsyning/lokale-initiativer/"),
 "ski_gl": ("Skive Kommune: overskudsvarme fra GreenLab Skive (læst 12/11 2026)", "https://skive.dk/borger/natur-miljoe-og-klima/varmeforsyning/overskudsvarme-fra-greenlab-skive/"),
 "ski_jv": ("Skive Kommune: jordvarme (læst 12/11 2026)", "https://skive.dk/erhverv/erhvervsaffald-forsyning-og-miljoe/forsyning/jordvarme/"),
 "ski_sf": ("Skive Fjernvarme: ny kunde, udvidelsesområde og tidsplan (læst 12/11 2026)", "https://www.skivefjernvarme.dk/ny-kunde"),
})
CITIES["kalundborg"] = {
  "name": "Kalundborg", "kommune": "Kalundborg Kommune", "updated": ("12. november 2026", "2026-11-12"),
  "vp_title": "Varmepumpe Kalundborg: luft til vand, tilskud, pris | Energitjekket",
  "fv_title": "Fjernvarme eller varmepumpe i Kalundborg? Pris 2026 | Energitjekket",
  "sol_intro": "Solceller i Kalundborg: PVGIS beregner en af de højeste solcelleproduktioner af alle byerne på dette site. Ligger panelerne plant på taget af et enfamiliehus, og overholder huset byggeretten i bygningsreglementet, kræver det som udgangspunkt ikke byggetilladelse – men lokalplaner og servitutter kan sætte grænser. Her er reglerne, priserne og vejen til et tilbud.",
  "sol_facts": [
    ("Solceller, der ligger <strong>plant på taget af et enfamiliehus</strong> og overholder bygningsreglementets højde- og afstandskrav, kræver som udgangspunkt ikke byggetilladelse.", ["se_sol"]),
    ("Kalundborg Kommune skriver, at du <strong>altid skal søge byggetilladelse</strong>, hvis byggeretten efter BR18 kapitel 8 ikke overholdes – uanset undtagelserne.", ["kal_byg"]),
    ("En <strong>lokalplan eller byplanvedtægt</strong> kan bestemme, hvordan bebyggelsen skal se ud. Afvigelser kræver dispensation, og kun mindre væsentlige lempelser kan godkendes.", ["kal_lp"]),
    ("For småhusbyggeri lover kommunen en <strong>maksimal sagsbehandlingstid på 65 dage</strong>, når ansøgningen er indsendt efter 1. september 2026 og er fuldt oplyst.", ["kal_sbt"]),
  ],
  "sol_faq": [
    ("Skal jeg søge byggetilladelse til solceller på mit hus i Kalundborg?", "Som regel ikke, hvis panelerne ligger plant på taget af et enfamiliehus, og bygningsreglementets højde- og afstandskrav er overholdt. Kalundborg Kommune skriver dog, at du altid skal søge, hvis byggeretten efter BR18 kapitel 8 ikke overholdes. Tjek også lokalplan og tinglyste servitutter.", ["se_sol", "kal_byg"]),
    ("Hvordan kontakter jeg Kalundborg Kommune om byggeri?", "Byggesagsområdet kan ikke ringes op direkte. Du kan bestille et telefonmøde på 15 minutter på kommunens hjemmeside eller skrive til dto@kalundborg.dk. Handler vejledningen om en konkret byggesag, opkræves der gebyr for tiden.", ["kal_byg"]),
  ],
  "vp_intro": "Luft til vand-varmepumpe i Kalundborg: mere end hvert tiende hus i kommunen har elvarme, og fjernvarmeprojektet i Gørlev og Kirke Helsinge er opgivet. For de fleste uden for fjernvarmenettene er en varmepumpe derfor vejen væk fra olie, gas og elpaneler. Her er status, priserne og reglerne.",
  "vp_facts": [
    ("Kalundborg Forsyning har indstillet fjernvarmeprojektet i <strong>Gørlev og Kirke Helsinge</strong>: kun 60 % af de potentielle kunder viste interesse, og der krævedes 70 %.", ["kal_tv"]),
    ("<strong>Sæby og Reerslev</strong> havde ifølge Kalundborg Forsyning ikke volumen nok til at gøre en central varmeløsning rentabel.", ["kal_tv"]),
    ("Et <strong>jordvarmeanlæg</strong> skal anmeldes eller have tilladelse hos kommunen. Ved en anmeldelse kan du etablere anlægget, hvis du ikke har hørt fra kommunen inden 4 uger.", ["kal_jv"]),
    ("Erstatter jordvarmen fx et oliefyr, kan du søge <strong>Kalundborg Varmeforsyning A/S om tilskud</strong>, før projektet sættes i gang.", ["kal_jv"]),
  ],
  "vp_faq": [
    ("Kommer der fjernvarme til Gørlev og Kirke Helsinge?", "Nej, ikke som det ser ud nu. Kalundborg Forsyning har indstillet projektet, fordi kun 60 % af de potentielle kunder havde vist interesse mod de nødvendige 70 %. Boligernes spredte placering og stigende anlægsomkostninger trak også ned, og forsyningen havde brugt knap 3,1 mio. kr. på projektet.", ["kal_tv"]),
    ("Hvor ofte skal et jordvarmeanlæg kontrolleres i Kalundborg Kommune?", "Mindst én gang om året af en jordvarmesagkyndig. Finder kontrollen fejl, skal du inden 14 dage sende en skriftlig redegørelse til kommunen, og resultatet af kontrollen skal gemmes i mindst 10 år.", ["kal_jv"]),
  ],
}
CITIES["skive"] = {
  "name": "Skive", "kommune": "Skive Kommune", "updated": ("12. november 2026", "2026-11-12"),
  "sol_intro": "Solceller i Skive: på enfamiliehuse, sommerhuse, udhuse, carporte og garager kræver et anlæg på taget ikke byggetilladelse, så længe byggeretten er overholdt, og anlægget ikke ændrer bygningens højde- og afstandsforhold. Anlægget skal altid registreres i BBR. Her er reglerne, priserne og vejen til et tilbud.",
  "sol_facts": [
    ("Solenergianlæg på taget af <strong>enfamiliehuse og sommerhuse</strong> kræver hverken byggetilladelse, VVM-screening eller landzonetilladelse, når byggeretten er overholdt.", ["ski_sol"]),
    ("Gør anlægget fx en garage højere end <strong>2,5 m inden for 2,5 m fra naboskel</strong>, eller påvirker det bygningens bærende konstruktion, kræver det byggetilladelse.", ["ski_sol"]),
    ("Har du søgt om et anlæg <strong>under 50 kW</strong> og ikke fået svar inden for en måned, betragtes tilladelsen som givet.", ["ski_sol"]),
    ("Anlæg uden tilladelse skal registreres i <strong>BBR</strong>: send areal og ydelse til tek@skivekommune.dk.", ["ski_sol"]),
  ],
  "sol_faq": [
    ("Skal jeg søge byggetilladelse til solceller på mit hus i Skive?", "Ikke på enfamiliehuse og sommerhuse, når byggeretten er overholdt, og anlægget hverken ændrer højde- og afstandsforhold eller påvirker bygningens bæreevne. Lokalplaner, byplanvedtægter og servitutter kan dog stille krav til tagets udseende, og så skal du søge dispensation først.", ["ski_sol"]),
    ("Hvad gælder for solceller på jorden i Skive Kommune?", "Et anlæg på terræn kræver byggetilladelse, VVM-screening og landzonetilladelse – også når det hører til en bolig eller et sommerhus.", ["ski_sol"]),
  ],
  "vp_intro": "Luft til vand-varmepumpe i Skive: hvert femte hus i kommunen har naturgas, og 8 % har stadig oliefyr. Skive Fjernvarme udvider i byen frem mod 2028, men i mange landsbyer er en varmepumpe eller et fælles termonet vejen væk fra fyret. Her er status, priserne og reglerne.",
  "vp_facts": [
    ("Skive Fjernvarme tilbyder nu og frem mod 2028 fjernvarme til områder med <strong>næsten 2.500 boliger</strong> i Skive. Udvidelsen forudsætter, at helst op imod halvdelen i området tilmelder sig.", ["ski_sf"]),
    ("Kan du ikke få fjernvarme, anbefaler kommunen en <strong>varmepumpe</strong>. I områder, hvor der på sigt kommer fjernvarme, anbefaler den at <strong>lease</strong> varmepumpen.", ["ski_ind"]),
    ("<strong>Jordvarme</strong> kræver ifølge kommunen en grund på mindst 300 m², og anlægget skal anmeldes eller have tilladelse.", ["ski_ind", "ski_jv"]),
    ("I landsbyer langt fra fjernvarmen kan et <strong>termonet</strong> – mindre fælles jordvarme – være et alternativ til individuelle løsninger.", ["ski_kol"]),
  ],
  "vp_faq": [
    ("Hvornår kommer der fjernvarme i Skive?", "Skive Fjernvarme oplyser, at områder med næsten 2.500 boliger får tilbudt fjernvarme nu og frem mod 2028, og at udvidelsen forudsætter, at helst op imod halvdelen i området tilmelder sig. Du kan tjekke din adresse hos Skive Fjernvarme på 97 52 09 66.", ["ski_sf"]),
    ("Skal jordvarme anmeldes i Skive Kommune?", "Ja. Ligger anlægget uden for områder med særlige drikkevandsinteresser og indvindingsoplande, og bruges ethanol eller IPA-sprit som frostvæske, er en anmeldelse nok – har kommunen ikke gjort indsigelse inden 4 uger, kan anlægget etableres. Øvrige anlæg kræver tilladelse.", ["ski_jv"]),
  ],
}
CONTACTS["kalundborg"] = {"sol": [("Kalundborg Kommune, byggesag", "dto@kalundborg.dk · telefonmøde bookes på kalundborg.dk", "kal_byg")],
                          "vp":  [("Kalundborg Forsyning", "59 57 17 00 · kundecenter@kalfor.dk", "kal_ff")]}
CONTACTS["skive"] = {"sol": [("Skive Kommune, Teknik", "tek@skivekommune.dk", "ski_sol")],
                     "vp":  [("Skive Fjernvarme", "97 52 09 66 · skivefjernvarme@skivefjernvarme.dk", "ski_sf")]}

# ---------- daglig by-rutine 13. nov. 2026: Gladsaxe (DK2) og Kongens Lyngby (DK2, Lyngby-Taarbæk Kommune) ----------
S.update({
 "gla_byg": ("Gladsaxe Kommune: før du bygger – solvarme- og solcelleanlæg (læst 13/11 2026)", "https://gladsaxe.dk/borger/bolig-vand-og-varme/byggeri/foer-du-bygger"),
 "gla_sol": ("Gladsaxe Kommune: solceller (læst 13/11 2026)", "https://gladsaxe.dk/borger/bolig-vand-og-varme/varme-og-energi/solceller"),
 "gla_fv": ("Gladsaxe Kommune: fjernvarme og udbygningsplaner (læst 13/11 2026)", "https://gladsaxe.dk/borger/bolig-vand-og-varme/varme-og-energi/fjernvarme"),
 "gla_vp30": ("Gladsaxe Kommune: Varmeplan 2030 (læst 13/11 2026)", "https://gladsaxe.dk/politik/planer-politikker-og-visioner/miljoe-og-klima/varmeplan-2030"),
 "gla_ggf": ("Gladsaxe Kommune, Klima- og Miljøudvalget: afrapportering på driftsaftale for Gentofte Gladsaxe Fjernvarme 2025-2026 (via Monrad, læst 13/11 2026)", "https://www.monrad.app/agenda_items/77211"),
 "gla_kort": ("Gladsaxe Fjernvarme: se, om og hvornår du kan få fjernvarme (læst 13/11 2026)", "https://gladsaxefjernvarme.dk/privat/jeg-overvejer-at-faa-fjernvarme/se-straks-om-dit-hus-kan-faa-fjernvarme/"),
 "lyn_kp": ("Lyngby-Taarbæk Kommuneplan 2025: generelle rammer (solceller, bevaringsværdig bebyggelse, tagmateriale; læst 13/11 2026)", "https://ltk.cowiplan.dk/kommuneplan-2025/hvad-gaelder/generelle-rammer/"),
 "lyn_byg": ("Lyngby-Taarbæk Kommune: ansøg om byggetilladelse (læst 13/11 2026)", "https://www.ltk.dk/borger/bolig-og-byggeri/byggeri/ansoeg-om-byggetilladelse"),
 "lyn_disp": ("Lyngby-Taarbæk Kommune: dispensation (læst 13/11 2026)", "https://www.ltk.dk/borger/bolig-og-byggeri/byggeri/dispensation"),
 "lyn_fvng": ("Lyngby-Taarbæk Kommune: fjernvarme og naturgas, Varmeplan 2022-2030 (læst 13/11 2026)", "https://www.fjernvarme.ltk.dk/fjernvarme-og-naturgas"),
 "lyn_info": ("Lyngby-Taarbæk Kommune: Vestforbrændings informationsmøder 2026 om graveopstart (læst 13/11 2026)", "https://fjernvarme.ltk.dk/informationsmoeder-2026-om-graveopstart-i-lyngby-taarbaek"),
 "lyn_pdf": ("Vestforbrænding: informationsmøde om graveopstart i Lyngby-Taarbæk 26. januar 2026 (pdf)", "https://www.fjernvarme.ltk.dk/media/2gdhlg4e/informationsmoede-om-graveopstart-26-januar-lyngby-taarbaek.pdf"),
 "lyn_vf": ("Vestforbrænding: fjernvarme i Lyngby-Taarbæk (læst 13/11 2026)", "https://vestfor.dk/privat/fjernvarme/fjernvarme-lyngby-taarbaek-kommune"),
})
CITIES["gladsaxe"] = {
  "name": "Gladsaxe", "kommune": "Gladsaxe Kommune", "updated": ("13. november 2026", "2026-11-13"),
  "sol_intro": "Solceller i Gladsaxe: på et fritliggende enfamiliehus kræver solceller ikke byggetilladelse, når de sidder på det eksisterende tag i flugt med taghældningen, og huset ikke har bevaringsværdi 1-4. Bor du i rækkehus eller dobbelthus, skal du kontakte Byggesag først – og halvdelen af husene i kommunen er række-, kæde- eller dobbelthuse. Her er reglerne, priserne og vejen til et tilbud.",
  "sol_facts": [
    ("På et <strong>fritliggende enfamiliehus</strong> med bevaringsværdi 5 eller mere kræver solceller ikke byggetilladelse, når de sidder på det eksisterende tag og i flugt med taghældningen.", ["gla_byg"]),
    ("Har huset <strong>bevaringsværdi 1-4</strong> (slå det op hos Slots- og Kulturstyrelsen), skal du kontakte Byggesag, før du går i gang.", ["gla_byg"]),
    ("Ved <strong>dobbelt- og rækkehuse</strong> skal du altid kontakte Byggesag, fordi deklarationer og lokalplaner kan have særlige regler.", ["gla_byg"]),
    ("Når anlægget er sat op, skal elinstallatøren registrere det hos netselskabet, og du skal selv indberette det i <strong>BBR</strong>.", ["gla_sol"]),
  ],
  "sol_faq": [
    ("Skal jeg søge byggetilladelse til solceller på min villa i Gladsaxe?", "Ikke hvis villaen er fritliggende, har bevaringsværdi 5 eller mere, og solcellerne sidder på det eksisterende tag i flugt med taghældningen. Har huset bevaringsværdi 1-4, skal du kontakte Byggesag på byggesag@gladsaxe.dk eller 39 57 59 05.", ["gla_byg"]),
    ("Hvor meget af strømmen i Gladsaxe kan komme fra solceller?", "Ifølge en analyse, kommunen henviser til, kan ca. en tredjedel af strømforbruget i Gladsaxe produceres på tagene i kommunen, og ca. halvdelen af det potentiale ligger på private tage.", ["gla_sol"]),
  ],
  "vp_intro": "Luft til vand-varmepumpe i Gladsaxe: næsten halvdelen af husene i kommunen har stadig naturgas, men fjernvarmen er på vej til stort set hele kommunen frem mod 2029. Før du vælger en varmepumpe, er det vigtigste derfor, hvornår fjernvarmen når din vej. Her er status, priserne og reglerne.",
  "vp_facts": [
    ("Der er godkendt projektforslag for udbygning af fjernvarmen til <strong>stort set hele Gladsaxe Kommune</strong>: ca. 5.000 bygninger hos Gentofte Gladsaxe Fjernvarme og ca. 4.000 hos Vestforbrænding.", ["gla_ggf"]),
    ("Den samlede tidsplan blev opdateret i efteråret 2025 med forventet afslutning af de sidste etaper i <strong>2029</strong>.", ["gla_ggf"]),
    ("Der er <strong>ingen tilslutningspligt</strong> til fjernvarme i Gladsaxe – du må selv vælge opvarmning.", ["gla_fv"]),
    ("Falder tilslutningen i et udbygningsområde under <strong>40 %</strong>, vil kommunen og fjernvarmeselskabet genoverveje udbygningen. Samlet ligger tilslutningen i Gladsaxe på 82 %.", ["gla_fv", "gla_ggf"]),
  ],
  "vp_faq": [
    ("Hvornår får jeg fjernvarme i Gladsaxe?", "Det afhænger af, om du bor i Gentofte Gladsaxe Fjernvarmes område i den sydlige del af kommunen eller i Vestforbrændings område nord for Motorring 3 og vest for Stengårds Allé. Begge selskaber har kort, hvor du kan slå din adresse op. Kommunen skriver, at det er selskabernes tidsplan, der gælder.", ["gla_fv", "gla_kort"]),
    ("Hvad gør jeg, hvis mit gasfyr går i stykker, før fjernvarmen kommer?", "Gladsaxe Kommune nævner, at du kan reparere fyret, udskifte det med et brugt eller købe en midlertidig varmepumpe. Tal med en VVS'er om mulighederne.", ["gla_fv"]),
  ],
}
CITIES["kongens-lyngby"] = {
  "name": "Kongens Lyngby", "kommune": "Lyngby-Taarbæk Kommune", "cross_name": "Lyngby-Taarbæk", "updated": ("13. november 2026", "2026-11-13"),
  "sol_title": "Solceller Kongens Lyngby 2026: regler og pris | Energitjekket",
  "vp_title": "Varmepumpe Kongens Lyngby: luft til vand, pris 2026 | Energitjekket",
  "fv_title": "Fjernvarme eller varmepumpe i Kongens Lyngby? 2026 | Energitjekket",
  "reg_title": "Solceller i Lyngby-Taarbæk: regler og tilladelse | Energitjekket",
  "sol_intro": "Solceller i Kongens Lyngby: Lyngby-Taarbæks kommuneplan tillader solceller på alle bygninger – men ikke på bevaringsværdige huse, hvis det påvirker bevaringsværdien, og i rækkehus- og dobbelthusområder kun efter ensartede retningslinjer. Mere end halvdelen af husene har tegltag. Her er reglerne, priserne og vejen til et tilbud.",
  "sol_facts": [
    ("Kommuneplanens generelle rammer siger, at der <strong>må opsættes solceller på alle bygninger</strong> – med undtagelse for bevaringsværdig bebyggelse.", ["lyn_kp"]),
    ("Ejendomme med <strong>høj bevaringsværdi (SAVE 1-3)</strong> er udpeget som bevaringsværdige. Her må solceller kun sættes op, hvis det ikke påvirker bevaringsværdien.", ["lyn_kp", "lyn_byg"]),
    ("I områder med <strong>rækkehuse og dobbelthuse</strong> må solceller kun sættes op efter ensartede retningslinjer.", ["lyn_kp"]),
    ("Kommunen har en <strong>byggesagsvagt</strong> på 45 97 38 87 alle hverdage, og en forhåndsdialog på 30 minutter er gratis.", ["lyn_byg"]),
  ],
  "sol_faq": [
    ("Må jeg sætte solceller på mit hus i Kongens Lyngby?", "Som udgangspunkt ja: kommuneplanen tillader solceller på alle bygninger. Er huset bevaringsværdigt (SAVE 1-3), må de kun sættes op, hvis det ikke påvirker bevaringsværdien, og i rækkehus- og dobbelthusområder skal de følge ensartede retningslinjer. Tjek også lokalplan og tinglyste servitutter.", ["lyn_kp", "lyn_byg"]),
    ("Hvor lang tid tager en byggesag i Lyngby-Taarbæk?", "Kommunen skriver, at du i øjeblikket skal forvente ca. 3 måneders køtid, før din sag får en byggesagsbehandler. Kræver sagen naboorientering, høring eller politisk behandling, tager det længere tid.", ["lyn_byg", "lyn_disp"]),
  ],
  "vp_intro": "Luft til vand-varmepumpe i Kongens Lyngby: to ud af tre huse i Lyngby-Taarbæk Kommune har naturgas – den højeste andel af byerne på dette site – men Vestforbrænding ruller fjernvarme ud til ca. 8.625 adresser frem mod 2030. Bor du uden for fjernvarmeområderne, er en varmepumpe vejen væk fra gassen. Her er status, priserne og reglerne.",
  "vp_facts": [
    ("Vestforbrændings udrulning i Lyngby-Taarbæk startede i oktober 2023 og skal være færdig i <strong>december 2030</strong>: 17 energidistrikter og ca. 8.625 adresser.", ["lyn_pdf"]),
    ("<strong>Spring Forbi, Raadvad, Bakken, Frederiksdal og Ny Frederiksdal</strong> samt spredt bebyggelse i det østlige Virum ved Mølleåen får ikke tilbudt fjernvarme. Her peger kommunen på varmepumpe eller termonet.", ["lyn_fvng"]),
    ("Selv om et område er udpeget til fjernvarme, må du godt installere <strong>jordvarme eller solceller</strong>. Et jordvarmeanlæg kræver altid tilladelse.", ["lyn_fvng"]),
    ("I Vestforbrændings kampagneperiode koster en fjernvarmetilslutning <strong>15.000 kr.</strong> (op til 50 m stikledning); uden for kampagnen 45.000 kr.", ["lyn_pdf"]),
  ],
  "vp_faq": [
    ("Hvilke områder i Lyngby-Taarbæk får ikke fjernvarme?", "Ifølge kommunen boliger i Spring Forbi, Raadvad, Bakken, Frederiksdal og Ny Frederiksdal (Marienborg/Sophienholm) samt spredt bebyggelse i det østlige Virum, der grænser op til Mølleåen. Her kan en varmepumpe – eller i samråd med kommunen et termonet – være løsningen.", ["lyn_fvng"]),
    ("Skal jordvarme have tilladelse i Lyngby-Taarbæk?", "Ja. Lyngby-Taarbæk Kommune skriver, at opsætning af et jordvarmeanlæg altid kræver tilladelse – også hvis dit område er udpeget til fjernvarme.", ["lyn_fvng"]),
  ],
}
CONTACTS["gladsaxe"] = {"sol": [("Gladsaxe Kommune, Byggesag", "39 57 59 05 · byggesag@gladsaxe.dk", "gla_byg")],
                        "vp":  [("Gladsaxe Fjernvarme (Gentofte Gladsaxe Fjernvarme)", "70 20 58 50 · info@ggfjernvarme.dk", "gla_kort")]}
CONTACTS["kongens-lyngby"] = {"sol": [("Lyngby-Taarbæk Kommune, byggesagsvagt", "45 97 38 87 (alle hverdage)", "lyn_byg")],
                              "vp":  [("Lyngby-Taarbæk Kommune, Klima og Forsyning – Varme", "45 97 35 00", "lyn_fvng")]}

# ---------- daglig by-rutine 16. nov. 2026: Holstebro (DK1) og Fredensborg (DK2) ----------
S.update({
 "hol_byg": ("Holstebro Kommune: byggeri – solcelleanlæg (læst 16/11 2026)", "https://www.holstebro.dk/byggeri"),
 "hol_varme": ("Holstebro Kommune: varmeforsyning (læst 16/11 2026)", "https://www.holstebro.dk/borger/bolig-og-byggeri/boligejer/el-og-varme/varme"),
 "hol_vfomr": ("Vestforsyning: forsyningsområde for varme (læst 16/11 2026)", "https://www.vestforsyning.dk/varme/forsyningsomraade/"),
 "hol_vfkan": ("Vestforsyning: kan jeg få fjernvarme? (læst 16/11 2026)", "https://www.vestforsyning.dk/varme/kan-jeg-faa-fjernvarme/"),
 "hol_vfjern": ("Vestforsyning: Vi presser lige nu varmen under jernbanen (27/8 2026)", "https://www.vestforsyning.dk/nyheder/nyheder/vi-presser-lige-nu-varmen-under-jernbanen/"),
 "fre_sol": ("Fredensborg Kommune: solceller (læst 16/11 2026)", "https://fredensborg.dk/borger/klima-og-energi/elektricitet/solceller"),
 "fre_fv": ("Fredensborg Kommune: fjernvarme (læst 16/11 2026)", "https://fredensborg.dk/borger/klima-og-energi/varme/fjernvarme"),
 "fre_vp": ("Fredensborg Kommune: varmepumpe – regler, støj og placering (læst 16/11 2026)", "https://fredensborg.dk/borger/klima-og-energi/varme/varmepumpe"),
 "fre_nf": ("Norfors: fjernvarme i Fredensborg Kommune (læst 16/11 2026)", "https://norfors.dk/borger/fjernvarme/fredensborg-kommune"),
 "fre_monrad": ("Fredensborg Kommune, Udvalget for Natur, Miljø og Bæredygtig udvikling 11/11 2025: orientering om status på fjernvarmeudbygning (via Monrad)", "https://www.monrad.app/agenda_items/5991"),
 "fre_nivaa": ("Norfors: Fremtidens fjernvarme rykker ind i Nivå Bymidte (læst 16/11 2026)", "https://norfors.dk/fremtidens-fjernvarme-rykker-ind-i-nivaa-bymidte"),
 "fre_es": ("Energy Supply 29/10 2026: Efter fem års ventetid: Fjernvarmeplaner falder til jorden", "https://www.energy-supply.dk/article/view/1253741/efter_fem_ars_ventetid_fjernvarmeplaner_falder_til_jorden"),
 "fre_humle": ("Humleborg Online: Byrådet annullerer fjernvarmeprojekter i Fredensborg (læst 16/11 2026)", "https://humleborg.dk/kanaler/lokale-nyheder/byradet-annullerer-fjernvarmeprojekter-i-fredensborg"),
})
CITIES["holstebro"] = {
  "name": "Holstebro", "kommune": "Holstebro Kommune", "updated": ("16. november 2026", "2026-11-16"),
  "sol_intro": "Solceller i Holstebro: et anlæg på taget kræver som udgangspunkt ingen tilladelse fra Holstebro Kommune – men du har selv ansvaret for, at fredning, lokalplan og reglerne ved skel er overholdt. Står panelerne tættere end 2,5 m på skel, må intet blive højere end 2,5 m. Her er reglerne, priserne og vejen til et tilbud.",
  "sol_facts": [
    ("Et solcelleanlæg på taget kræver som udgangspunkt <strong>ikke tilladelse</strong> fra kommunen, men ejeren har ansvaret for, at lovgivningen er overholdt.", ["hol_byg"]),
    ("Sidder solcellerne på en bygning tættere end <strong>2,5 m fra skel</strong>, må ingen højde inkl. solceller overstige 2,5 m – ellers skal der søges byggetilladelse og dispensation.", ["hol_byg"]),
    ("Et <strong>fritstående anlæg på jorden</strong> kræver byggetilladelse, i det åbne land også landzonetilladelse, og det skal stå tæt på de eksisterende bygninger.", ["hol_byg"]),
    ("Kommunen beder dig tjekke, om huset er <strong>fredet eller bevaringsværdigt</strong>, om der er kirkezone eller kystbeskyttelseslinje, og om en lokalplan eller byplanvedtægt gælder.", ["hol_byg"]),
  ],
  "sol_faq": [
    ("Skal jeg søge tilladelse til solceller på taget i Holstebro?", "Som udgangspunkt nej. Holstebro Kommune skriver, at et solcelleanlæg på taget ikke kræver tilladelse, men at du selv har ansvaret for, at fredning, lokalplan eller byplanvedtægt og højdegrænsen ved skel er overholdt. Er du i tvivl, kan du sende en ansøgning med tegninger til kommunen.", ["hol_byg"]),
    ("Må jeg sætte solceller på jorden ved min landejendom?", "Ja, men et fritstående anlæg kræver både landzonetilladelse og byggetilladelse, og det skal placeres tæt på de eksisterende bygninger. Ansøgningen skal have en situationsplan med placering og mål samt data på panelernes og stativets størrelse. På taget af en landejendom skal der ikke søges byggetilladelse.", ["hol_byg"]),
  ],
  "vp_intro": "Luft til vand-varmepumpe i Holstebro: fire ud af fem huse i Holstebro Kommune har fjernvarme, og kun 1 % har naturgas. En varmepumpe er derfor mest aktuel for de godt 1.000 huse med oliefyr og for husene i landsbyer og det åbne land uden for værkernes net. Her er tallene, priserne og reglerne.",
  "vp_facts": [
    ("Der er <strong>seks fjernvarmeselskaber</strong> i Holstebro Kommune: Vestforsyning Varme (Holstebro by og omegnsbyerne) samt værkerne i Ulfborg, Vemb, Thorsminde, Vinderup og Ejsing.", ["hol_varme"]),
    ("I mange fjernvarmeområder, der er planlagt før januar 2019, er der <strong>tilslutnings- og forblivelsespligt</strong> til fjernvarme. Områderne kan ses på Plandata.dk.", ["hol_varme"]),
    ("Vestforsyning har <strong>mere end 12.000 forbrugere</strong>, 306 km hovedledninger og vekslerstationer i Holstebro, Mejrup og Tvis.", ["hol_vfomr"]),
    ("Vestforsyning udvider ved <strong>Sønderlundvej</strong>, hvor to fjernvarmerør presses under jernbanen; de skal efter planen være på plads ved nytår.", ["hol_vfjern"]),
  ],
  "vp_faq": [
    ("Er der tilslutningspligt til fjernvarme i Holstebro?", "I mange fjernvarmeområder, der er planlagt før januar 2019, har Holstebro Kommune pålagt tilslutnings- og forblivelsespligt. Fjernvarmeområderne kan ses på Plandata.dk. Ligger dit hus i et sådant område, så afklar det med kommunen, før du køber varmepumpe.", ["hol_varme"]),
    ("Hvor kommer Vestforsynings fjernvarme fra?", "Ifølge Vestforsyning primært fra MEC – BioHeat & Power, som laver varme af lokale energikilder som affald, halm og flis. Varmecentraler dækker varmebehovet i kolde perioder og ved udfald på kraftvarmeværket.", ["hol_vfomr"]),
  ],
}
CITIES["fredensborg"] = {
  "name": "Fredensborg", "kommune": "Fredensborg Kommune", "updated": ("16. november 2026", "2026-11-16"),
  "vp_title": "Varmepumpe Fredensborg: luft til vand og pris 2026 | Energitjekket",
  "fv_title": "Fjernvarme eller varmepumpe i Fredensborg? 2026 | Energitjekket",
  "sol_intro": "Solceller i Fredensborg: et anlæg på dit private tag kræver som udgangspunkt ingen byggetilladelse, men på bevaringsværdige huse (SAVE 1-4) giver kommunen som udgangspunkt ikke lov, og nogle lokalplaner kræver dispensation. Over halvdelen af husene i kommunen er række-, kæde- eller dobbelthuse. Her er reglerne, priserne og vejen til et tilbud.",
  "sol_facts": [
    ("Et solcelleanlæg på dit <strong>private tag</strong> kræver som udgangspunkt ikke byggetilladelse, men skal overholde bygningsreglementets afstandskrav til skel (BR18 § 179).", ["fre_sol"]),
    ("På <strong>bevaringsværdige bygninger (SAVE 1-4)</strong> gives der som udgangspunkt ikke tilladelse til solceller på taget.", ["fre_sol"]),
    ("Står lokalplanen i vejen, kan du søge <strong>dispensation</strong>. Kommunen anbefaler matte, antirefleksbehandlede paneler i sort eller tagets farve, som følger tagfladens hældning.", ["fre_sol"]),
    ("Er ejendommen <strong>fredet</strong>, kan kommunen ikke dispensere – det kræver tilladelse fra Slots- og Kulturstyrelsen.", ["fre_sol"]),
  ],
  "sol_faq": [
    ("Kræver solceller byggetilladelse i Fredensborg Kommune?", "Som udgangspunkt ikke på et privat tag. Lokalplaner, byplanvedtægter og tinglyste deklarationer kan dog kræve dispensation, og anlægget skal altid overholde afstandskravene til skel i BR18 § 179. Afdelingen Byg svarer på byggesager@fredensborg.dk.", ["fre_sol"]),
    ("Kan jeg få dispensation fra lokalplanen til solceller i Fredensborg?", "Ofte. Kommunen skriver, at den er positivt indstillet og så vidt muligt imødekommer ansøgningerne, hvis dispensationen ikke strider mod planens principper. Der lægges vægt på, at panelerne passer til bygningen og kvarteret og ikke generer naboerne. Ansøgningen sendes via Byg og Miljø.", ["fre_sol"]),
  ],
  "vp_intro": "Luft til vand-varmepumpe i Fredensborg: knap fire ud af ti huse i Fredensborg Kommune har stadig naturgas, og i oktober 2026 annullerede byrådet de planlagte fjernvarmeprojekter i Fredensborg By og Fredensborg Øst. Mange står derfor igen med valget mellem varmepumpe og gas. Her er status, priserne og kommunens regler for støj og placering.",
  "vp_facts": [
    ("Byrådet har annulleret fjernvarmeprojekterne i <strong>Fredensborg By og Fredensborg Øst</strong> med 316 bygninger, efter Norfors' beregninger viste, at de ville blive 10,2 mio. kr. dyrere end individuelle luft til vand-varmepumper over 20 år.", ["fre_es", "fre_humle"]),
    ("Med annulleringen kan de berørte boligejere igen <strong>søge tilskud</strong> til individuelle varmepumper.", ["fre_humle"]),
    ("Varmepumpens udedel skal stå mindst <strong>2,5 m fra skel</strong> og overholde <strong>35 dB</strong> om natten i skel til naboen i villa- og rækkehusområder.", ["fre_vp"]),
    ("Står flere varmepumper tæt, fx i en rækkehusbebyggelse, kan den samlede støj blive kraftigere (<strong>cikadeeffekten</strong>). Et jordvarmeanlæg kræver altid tilladelse fra kommunen først.", ["fre_vp"]),
  ],
  "vp_faq": [
    ("Hvad sker der nu med fjernvarmen i Fredensborg by?", "Byrådet godkendte i oktober 2026 at annullere de to projekter fra 2021 og 2022, fordi fjernvarmen ikke længere var den samfundsøkonomisk bedste løsning. Norfors arbejder ifølge borgmesteren videre med et nyt, mere sammenhængende projekt, men der er ingen tidsplan, og flere byrådsmedlemmer opfordrede borgerne til ikke at vente med at undersøge andre løsninger.", ["fre_humle", "fre_es"]),
    ("Skal jeg søge tilladelse til en varmepumpe i Fredensborg?", "Som udgangspunkt ikke i enfamiliehuse, dobbelthuse, rækkehuse og sommerhuse. Varmepumpen skal overholde bygningsreglementets afstandskrav og 35 dB om natten i skel, og du skal selv registrere skiftet i BBR. Kræver placeringen dispensation fra lokalplanen, søger du via Byg og Miljø.", ["fre_vp"]),
  ],
}
CONTACTS["holstebro"] = {"sol": [("Holstebro Kommune, Teknik og Miljø", "tm@holstebro.dk", "hol_varme")],
                         "vp":  [("Vestforsyning", "96 12 73 00 · kundeservice@vestforsyning.dk", "hol_vfkan")]}
CONTACTS["fredensborg"] = {"sol": [("Fredensborg Kommune, Byg", "byggesager@fredensborg.dk", "fre_sol")],
                           "vp":  [("Norfors", "45 16 05 00 · norfors@norfors.dk", "fre_nf")]}

# ---------- daglig by-rutine 17. nov. 2026: Nakskov (DK2, Lolland Kommune) og Assens (DK1) ----------
S.update({
 "nak_sol": ("Lolland Kommune: solcelleanlæg (læst 17/11 2026)", "https://www.lolland.dk/borger/bolig-og-byggeri/varme-energi-og-energibesparelse/solcelleanlaeg"),
 "nak_byg": ("Lolland Kommune: generelt om byggeri (læst 17/11 2026)", "https://www.lolland.dk/borger/bolig-og-byggeri/byggeri/generelt-om-byggeri"),
 "nak_jord": ("Lolland Kommune: jordvarme (læst 17/11 2026)", "https://www.lolland.dk/borger/bolig-og-byggeri/varme-energi-og-energibesparelse/jordvarme"),
 "nak_lf": ("Lolland Forsyning: din varme – forsyningsområde (læst 17/11 2026)", "https://lollandforsyning.dk/kunde/varme/din-varme/"),
 "nak_lfvv": ("Lolland Forsyning: varmeværker (læst 17/11 2026)", "https://lollandforsyning.dk/kunde/varme/varmevaerker/"),
 "nak_lft": ("Lolland Forsyning: tilslutning til fjernvarme (læst 17/11 2026)", "https://lollandforsyning.dk/kunde/varme/tilslutning-til-fjernvarme/"),
 "nak_elk": ("Lolland Kommune, Økonomi- og Erhvervsudvalget 18/11 2026: 40 MW elkedel i Nakskov (sagsfremstilling via Sagsvagt, læst 17/11 2026)", "https://sagsvagt.dk/sag/lolland-2026-11-18-oekonomi-og-erhvervsudvalget-8.html"),
 "nak_syd": ("Dansk Fjernvarme: Sydhavsvarme har set dagens lys på Lolland (24/2 2026)", "https://danskfjernvarme.dk/aktuelt/nyheder/2026/sydhavsvarme-har-set-dagens-lys-paa-lolland"),
 "ass_sol": ("Assens Kommune: solceller (læst 17/11 2026)", "https://www.assens.dk/borger/bolig-og-byggeri/jeg-skal-bygge/solceller"),
 "ass_vplan": ("Assens Kommune: varmeplan og status på fjernvarme (læst 17/11 2026)", "https://www.assens.dk/borger/bolig-og-byggeri/varme/varmeplan"),
 "ass_vp": ("Assens Kommune: varmepumpe (læst 17/11 2026)", "https://www.assens.dk/borger/bolig-og-byggeri/varme/opvarmningsformer/varmepumpe"),
 "ass_tilsk": ("Assens Kommune: tilskudsordninger til varme (læst 17/11 2026)", "https://www.assens.dk/borger/bolig-og-byggeri/varme/tilskudsordninger"),
 "ass_af900": ("Assens Fjernvarme: over 900 ejendomme i Aarup-området har nu fået fjernvarme (læst 17/11 2026)", "https://assensfjernvarme.dk/nyheder/over-900-ejendomme-i-aarup-omraadet-har-nu-faaet-fjernvarme"),
 "ass_aftid": ("Assens Fjernvarme: tidsplan for Aarup og landsbyer (læst 17/11 2026)", "https://assensfjernvarme.dk/aarup-og-landsbyer/tidsplan"),
 "ass_nb": ("NB-Forsyning & Klima: Assens Fjernvarme reducerede forsyningsområde (2/6 2026)", "https://www.nb-forsyning.dk/2026/06/02/assens-fjernvarme-reducerede-forsyningsomraade-fjernvarmen-var-for-dyr"),
})
CITIES["nakskov"] = {
  "name": "Nakskov", "kommune": "Lolland Kommune", "updated": ("17. november 2026", "2026-11-17"),
  "sol_intro": "Solceller i Nakskov: Lolland Kommune skriver, at det afhænger af monteringen, om du skal have tilladelse – og at panelerne bør følge tagets hældning og tage hensyn til kviste, skorstene og husets udtryk. Nakskov har samtidig den næsthøjeste solproduktion pr. kWp af byerne på dette site – kun Rønne på Bornholm ligger højere. Her er reglerne, tallene og vejen til et tilbud.",
  "sol_facts": [
    ("Om du skal have <strong>tilladelse</strong>, afhænger ifølge kommunen af, hvordan anlægget monteres på taget.", ["nak_sol"]),
    ("Anlægget bør placeres med <strong>samme hældning som taget</strong> eller som en integreret del af tagbelægningen.", ["nak_sol"]),
    ("Tjek krav i <strong>deklarationer og byplanvedtægter</strong>, og om huset er bevaringsværdigt eller fredet. Anlægget skal indberettes til BBR.", ["nak_sol"]),
    ("I <strong>landzone</strong> kan det være nødvendigt at søge både landzone- og byggetilladelse.", ["nak_sol"]),
  ],
  "sol_faq": [
    ("Skal jeg søge tilladelse til solceller i Nakskov?", "Det afhænger af monteringen. Lolland Kommune skriver, at du i visse tilfælde skal have tilladelse, og kommunens generelle byggeside nævner solcelleanlæg blandt de tekniske anlæg, der kræver byggetilladelse. Spørg derfor Teknik og Miljø, før du bestiller – især hvis panelerne ikke følger tagets hældning.", ["nak_sol", "nak_byg"]),
    ("Hvad skal en ansøgning om solceller i Lolland Kommune indeholde?", "Tegninger, der viser anlæggets placering, afstanden til skel, totalhøjden over terræn og anlæggets størrelse i m². Ansøgningen sendes digitalt via Byg og Miljø; papir og mail behandles ikke.", ["nak_sol", "nak_byg"]),
  ],
  "vp_intro": "Varmepumpe i Nakskov: lidt over halvdelen af husene i Lolland Kommune har fjernvarme, men andelen med oliefyr er den højeste af byerne på dette site, og ingen huse er registreret med naturgas. Uden for Lolland Varmes net i Nakskov, Søllested og Midtlolland er en luft til vand-varmepumpe det oplagte skifte fra olie og elvarme. Her er tallene, priserne og reglerne.",
  "vp_facts": [
    ("Lolland Varme forsyner ca. <strong>4.500 kunder i Nakskov</strong>, ca. 500 i Søllested og ca. 525 på Midtlolland (Bandholm, Reersnæs, Nørreballe, Østofte og Stokkemarke).", ["nak_lf"]),
    ("Ligger ejendommen i forsyningsområdet, kan du som udgangspunkt få fjernvarme, medmindre varmeplanen eller tekniske og økonomiske hensyn er til hinder.", ["nak_lft"]),
    ("Et <strong>jordvarmeanlæg kræver tilladelse</strong> fra Lolland Kommune og må ikke ligge nærmere end 300 m fra en almen drikkevandsboring og 50 m fra andre vandindvindingsanlæg.", ["nak_jord"]),
    ("Lolland Kommune nævner, at et jordvarmeanlæg også kan kræve <strong>dispensation fra tilslutning til kollektiv varme</strong>.", ["nak_jord"]),
  ],
  "vp_faq": [
    ("Kræver jordvarme tilladelse i Lolland Kommune?", "Ja. Du skal søge tilladelse hos Lolland Kommune med en målfast tegning af slangernes placering. Anlægget skal efterses af en sagkyndig mindst én gang om året, og det skal anmeldes til kommunens miljøafdeling, når det tages i brug.", ["nak_jord"]),
    ("Kan jeg få fjernvarme i Nakskov?", "Ligger huset i Lolland Varmes forsyningsområde, kan du som udgangspunkt få fjernvarme, medmindre den kommunale varmeplan eller tekniske og økonomiske hensyn er til hinder. Du ansøger om et fjernvarmestik hos Lolland Forsyning.", ["nak_lft"]),
  ],
}
CITIES["assens"] = {
  "name": "Assens", "kommune": "Assens Kommune", "updated": ("17. november 2026", "2026-11-17"),
  "sol_intro": "Solceller i Assens: følger panelerne tagets hældning, kræver det ikke byggetilladelse fra Assens Kommune. På flade tage, på terræn og på erhvervs- og etagebygninger skal du søge. Lokalplaner og beskyttelseslinjer kan stadig kræve dispensation. Her er reglerne, priserne og vejen til et tilbud.",
  "sol_facts": [
    ("Solceller, der lægges i <strong>samme hældning som taget</strong>, kræver ikke byggetilladelse.", ["ass_sol"]),
    ("På et <strong>fladt tag</strong> skal der søges byggetilladelse, så kommunen kan vurdere anlægget.", ["ass_sol"]),
    ("Et anlæg på <strong>terræn</strong> kræver altid byggetilladelse – i landzone også landzonetilladelse.", ["ass_sol"]),
    ("Selv uden byggetilladelse kan der kræves <strong>dispensation</strong> fra skov-, å- og søbeskyttelseslinjer, lokalplaner eller tinglyste bestemmelser.", ["ass_sol"]),
  ],
  "sol_faq": [
    ("Skal jeg søge byggetilladelse til solceller i Assens?", "Ikke hvis panelerne lægges i samme hældning som taget på din bolig eller dit udhus. På et fladt tag, på terræn og på erhvervs- og etagebygninger skal du søge. Tjek også lokalplanen for din adresse på kommunens kort.", ["ass_sol"]),
    ("Hvad skal jeg registrere i BBR?", "Assens Kommune skriver, at solceller skal registreres i BBR med areal, anlæggets størrelse i kW og årstal for opsætning – også når der ikke skal søges byggetilladelse.", ["ass_sol"]),
  ],
  "vp_intro": "Varmepumpe i Assens: lidt over halvdelen af husene i Assens Kommune har fjernvarme, og Assens Fjernvarme er ved at afslutte udrulningen i Aarup og landsbyerne. Men en etape langs transmissionsledningen mod Aarup blev droppet, fordi fjernvarmen ville blive dyrere end varmepumper. Her er status, priserne og tilskudsreglerne.",
  "vp_facts": [
    ("Assens Kommune <strong>anbefaler varmepumpe</strong>, hvis ejendommen ligger i et område, der ikke vil blive forsynet med fjernvarme.", ["ass_vp"]),
    ("Varmepumpepuljen kræver bl.a., at huset <strong>ikke ligger i et område med fjernvarme eller planlagt fjernvarme</strong>, og at du ikke allerede har et bindende tilbud.", ["ass_tilsk"]),
    ("Assens Fjernvarme droppede i 2026 en etape med ca. <strong>40 ejendomme langs transmissionsledningen</strong> mod Aarup; her ville fjernvarmen være 24 % dyrere end individuelle varmepumper.", ["ass_nb"]),
    ("Kommunens kort viser for hver adresse, om fjernvarme er vedtaget, undersøges, eller om der <strong>ingen planer</strong> er.", ["ass_vplan"]),
  ],
  "vp_faq": [
    ("Kan jeg få tilskud til varmepumpe i Assens Kommune?", "Fra Varmepumpepuljen, hvis du ejer og bor i en helårsbolig med olie-, gas-, el- eller biokedel, og huset ikke ligger i et område med fjernvarme eller planlagt fjernvarme. Puljen dækker luft til vand og jordvarme, og du skal søge, før du indhenter et bindende tilbud.", ["ass_tilsk"]),
    ("Hvorfor fik husene langs transmissionsledningen ikke fjernvarme?", "Ifølge Assens Fjernvarme opnåede etapen ikke de krævede over 60 % tilslutning, og beregningerne viste, at fjernvarmen ville være 24 % dyrere end individuelle varmepumper. Kommunen godkendte reduktionen af forsyningsområdet i maj 2026, så borgerne kan søge midler til varmepumpe.", ["ass_nb"]),
  ],
}
CONTACTS["nakskov"] = {"sol": [("Lolland Kommune, Bolig og Byggeri", "54 67 64 50 · byggeri@lolland.dk", "nak_sol")],
                       "vp":  [("Lolland Forsyning (Lolland Varme)", "72 30 11 11 · forsyning@lollandforsyning.dk", "nak_lf")]}
CONTACTS["assens"] = {"sol": [("Assens Kommune, Byggesag", "64 74 75 19", "ass_sol")],
                      "vp":  [("Assens Fjernvarme", "64 71 10 24 · post@assensfjernvarme.dk", "ass_af900")]}

# ---------- daglig by-rutine 18. nov. 2026: Hinnerup (DK1, Favrskov Kommune) og Helsinge (DK2, Gribskov Kommune) ----------
S.update({
 "hin_byg": ("Favrskov Kommune: byggeri (læst 18/11 2026)", "https://favrskov.dk/borger/flyt-byg-og-bolig/byggeri"),
 "hin_skift": ("Favrskov Kommune: skift varmekilde (læst 18/11 2026)", "https://favrskov.dk/borger/flyt-byg-og-bolig/skift-varmekilde"),
 "hin_jord": ("Favrskov Kommune: jordvarme (læst 18/11 2026)", "https://favrskov.dk/borger/flyt-byg-og-bolig/jordvarme"),
 "hin_land": ("Favrskov Kommune: landzonetilladelser (læst 18/11 2026)", "https://favrskov.dk/borger/flyt-byg-og-bolig/landzonetilladelser"),
 "hin_ve": ("Favrskov Kommune: planlægning for vedvarende energianlæg (læst 18/11 2026)", "https://favrskov.dk/borger/fysisk-planlaegning/planlaegning-vedvarende-energianlaeg"),
 "hin_ber": ("Hinnerup Fjernvarme: bestyrelsens beretning til generalforsamlingen 28/5 2026 (PDF)", "https://www.hinnerupfjernvarme.dk/p/Hinnerup%20Fjernvarme/%C3%85rsregnskaber%20og%20budgetter/Bestyrelsens_beretning_2026.pdf"),
 "hin_elk": ("Hinnerup Fjernvarme: ny elkedel og akkumuleringstank på vej (4/2 2026)", "https://www.hinnerupfjernvarme.dk/nyheder/ny-elkedel-og-akkumuleringstank-paa-vej"),
 "hin_pris": ("Hinnerup Fjernvarme: samme priser som i 2025 (læst 18/11 2026)", "https://www.hinnerupfjernvarme.dk/nyheder/samme-priser-som-i-2025"),
 "hin_soef": ("Hinnerup Fjernvarme: nedlægning af fjernvarmerør under Ølstedvej i Søften (læst 18/11 2026)", "https://www.hinnerupfjernvarme.dk/nyheder/nedlaegning-af-fjernvarmeroer-under-oelstedvej-i-soeften"),
 "hel_byg": ("Gribskov Kommune: praktisk information ved byggeri (læst 18/11 2026)", "https://gribskov.dk/borger/flyt-bolig-og-byg/byggeri/praktisk-information-ved-byggeri"),
 "hel_trin": ("Gribskov Kommune: byggetilladelse trin for trin (læst 18/11 2026)", "https://gribskov.dk/borger/flyt-bolig-og-byg/byggeri/byggetilladelse-trin-for-trin"),
 "hel_kp": ("Gribskov Kommune: Kommuneplan 2025-37, vedtaget 9/9 2025 (læst 18/11 2026)", "https://gribskov.dk/om-kommunen/byudvikling-og-planlaegning/kommuneplan-2025-37"),
 "hel_kpmv": ("Gribskov Kommune: miljørapport for forslag til Kommuneplan 2025-37, afsnit 7.2.1 Solceller (PDF)", "https://gribskov.viewer.dkplan.niras.dk/media/ev4d3ccx/miljoevurdering-af-forslag-til-kommuneplan-2025.pdf"),
 "hel_vplan": ("Gribskov Kommune: varmeplanlægning – Varmeplan 2022 (læst 18/11 2026)", "https://gribskov.dk/borger/natur-miljoe-klima-og-trafik/varmeplanlaegning"),
 "hel_fj": ("Gribskov Kommune: kan jeg få fjernvarme i min bolig? (læst 18/11 2026)", "https://gribskov.dk/borger/natur-miljoe-klima-og-trafik/varmeplanlaegning/kan-jeg-faa-fjernvarme-i-min-bolig"),
 "hel_varme": ("Gribskov Kommune: varme (læst 18/11 2026)", "https://gribskov.dk/borger/natur-miljoe-klima-og-trafik/varme"),
 "hel_ber": ("Helsinge Fjernvarme: beretning 2025 (læst 18/11 2026)", "https://www.helsingefjernvarme.dk/nyheder/beretning-2025"),
 "hel_fo": ("Helsinge Fjernvarme: forbrugerorientering 2025 (læst 18/11 2026)", "https://www.helsingefjernvarme.dk/nyheder/forbrugerorientering-2025"),
})
CITIES["hinnerup"] = {
  "name": "Hinnerup", "kommune": "Favrskov Kommune", "updated": ("18. november 2026", "2026-11-18"),
  "sol_intro": "Solceller i Hinnerup: Favrskov Kommune har ingen særskilt solcelleside, så det er bygningsreglementets byggeret, din lokalplan og eventuelle deklarationer, der afgør, om du skal søge. Anlægget skal under alle omstændigheder meldes til BBR. Her er reglerne, tallene og vejen til et tilbud.",
  "sol_facts": [
    ("Etablerer du <strong>solceller eller solvarme</strong>, skal du give Favrskov Kommune besked, så det kan blive rettet i BBR – via Byg og Miljø eller Digital Post.", ["hin_skift"]),
    ("En <strong>lokalplan, deklaration</strong> eller retningslinjer for samlede bebyggelser kan begrænse dine valg af tagmaterialer og udvendige farver.", ["hin_byg"]),
    ("Kræver projektet byggetilladelse, søges den via <strong>Byg og Miljø</strong>, og du må først gå i gang, når tilladelsen er givet.", ["hin_byg"]),
    ("Ligger ejendommen i <strong>landzone</strong>, kan der også kræves landzonetilladelse.", ["hin_byg", "hin_land"]),
  ],
  "sol_faq": [
    ("Skal jeg melde mine solceller til kommunen i Hinnerup?", "Ja. Favrskov Kommune skriver, at du skal give besked, når du etablerer solceller eller solvarme, så BBR kan blive rettet. Det er ejerens ansvar, at BBR-meddelelsen er opdateret.", ["hin_skift"]),
    ("Hvor finder jeg lokalplanen for min adresse i Favrskov?", "På Favrskov Kommunes webkort 'Lokalplaner i Favrskov Kommune' eller på Plandata.dk. Kommunen beder dig orientere dig i kommuneplan, lokalplan og byplanvedtægt, før du bygger.", ["hin_byg"]),
  ],
  "vp_intro": "Varmepumpe i Hinnerup: to ud af tre huse i Favrskov Kommune har fjernvarme, og Hinnerup Fjernvarme er blandt de billigste værker i landet. Varmepumpen er derfor mest relevant uden for fjernvarmenettene og for de godt 1.000 huse, der stadig har naturgas. Her er tallene, reglerne for jordvarme og priserne.",
  "vp_facts": [
    ("Varmeforsyningen i Favrskov Kommune kommer fra <strong>fjernvarme, naturgas eller individuel varme</strong> som olie-, pille- og halmfyr.", ["hin_skift"]),
    ("Du kan skifte fra fjernvarme eller naturgas til individuel varme, hvis ejendommen <strong>ikke har tilslutningspligt</strong>, du har fået dispensation, eller du bygger et nyt lavenergihus.", ["hin_skift"]),
    ("Et <strong>jordvarmeanlæg</strong> kræver anmeldelse eller tilladelse fra Favrskov Kommune og må ikke ligge inden for 300 m fra et alment vandværks boringer eller 50 m fra en privat drikkevandsboring.", ["hin_jord"]),
    ("Byrådet godkendte en revideret <strong>Strategisk Varmeplan 2022-2030</strong> den 30. maj 2023.", ["hin_skift"]),
  ],
  "vp_faq": [
    ("Skal jeg søge om jordvarme i Favrskov Kommune?", "Et terrænnært anlæg uden for områder med særlige drikkevandsinteresser og vandværksoplande, med IPA-sprit eller ethanol som frostsikring, kan anmeldes via Byg og Miljø; hører du ikke fra kommunen inden for 4 uger, må du gå i gang. Dybe anlæg (over 5 m) og anlæg i drikkevandsområder kræver tilladelse.", ["hin_jord"]),
    ("Fritager en jordvarmetilladelse for tilslutningspligt til fjernvarme?", "Nej. Favrskov Kommune skriver, at en tilladelse til jordvarme ikke fritager ejendommen fra tilslutningspligt; bestemmelserne står i lokalplanen for området. Dispensation kan gives til nybyggeri i lavenergiklasse.", ["hin_jord"]),
  ],
}
CITIES["helsinge"] = {
  "name": "Helsinge", "kommune": "Gribskov Kommune", "updated": ("18. november 2026", "2026-11-18"),
  "sol_intro": "Solceller i Helsinge: Gribskov Kommune har ingen særskilt solcelleside, men byggeretten i bygningsreglementets kapitel 8 og din lokalplan afgør, om du skal søge. Kommuneplan 2025-37 giver mulighed for solenergi på tagarealer. Her er reglerne, tallene og vejen til et tilbud.",
  "sol_facts": [
    ("Gribskov Kommune henviser til <strong>byggeretten</strong> i bygningsreglementets kapitel 8, som beskriver, hvad man oftest kan få lov til uden tilladelse.", ["hel_byg"]),
    ("Er ejendommen omfattet af en <strong>lokalplan eller byplanvedtægt</strong>, skal den overholdes – ellers skal du søge dispensation.", ["hel_byg"]),
    ("Kræver dit anlæg byggetilladelse, koster sagsbehandlingen <strong>904 kr. pr. time</strong> for sager oprettet i 2026.", ["hel_byg"]),
    ("<strong>Kommuneplan 2025-37</strong>, vedtaget 9. september 2025, giver mulighed for solenergi på tagarealer og i andre multifunktionelle sammenhænge.", ["hel_kp", "hel_kpmv"]),
  ],
  "sol_faq": [
    ("Skal jeg søge byggetilladelse til solceller i Helsinge?", "Det afhænger af, om anlægget holder sig inden for byggeretten i bygningsreglementets kapitel 8 og din lokalplan. Kan det ikke det, skal Gribskov Kommune foretage en helhedsvurdering, og du skal søge via Byg og Miljø.", ["hel_byg", "hel_trin"]),
    ("Hvor længe gælder en byggetilladelse i Gribskov Kommune?", "I 1 år. Du skal påbegynde arbejdet, inden tilladelsen udløber, og anmelde til kommunen, at du går i gang.", ["hel_trin"]),
  ],
  "vp_intro": "Varmepumpe i Helsinge: kun hvert tredje hus i Gribskov Kommune har fjernvarme, og andelen med varmepumpe og med elvarme er den højeste af alle byerne på dette site. I gasområderne Helsinge Øst og Helsinge Vest planlægges fjernvarme, mens resten af kommunen uden for nettene er udlagt til individuel varme. Her er tallene, planerne og priserne.",
  "vp_facts": [
    ("Varmeplan 2022, godkendt af byrådet <strong>13. december 2022</strong>, viser hvilke dele af kommunen der har kollektiv varme; resten er udlagt til individuel forsyning som fx varmepumpe.", ["hel_vplan"]),
    ("I <strong>Helsinge Øst</strong> (Fuglekvarteret og Nejlinge) og <strong>Helsinge Vest</strong> (Tofte og Skærød) er der planer om at konvertere gasområderne til fjernvarme.", ["hel_fj"]),
    ("I <strong>Annisse Nord og Ramløse</strong> undersøges det, om der kan etableres byvarme (ø-varme).", ["hel_fj"]),
    ("Er der et <strong>godkendt projektforslag</strong> i dit område, kan du ikke søge tilskud til varmepumpe.", ["hel_varme"]),
  ],
  "vp_faq": [
    ("Må jeg installere en varmepumpe i et område, hvor fjernvarmen er på vej?", "Ja, men Gribskov Kommune opfordrer dig til at overveje, om det er værd at vente, til fjernvarmen er udrullet. Og er der et godkendt projektforslag i området, kan du ikke søge tilskud til varmepumpe.", ["hel_fj", "hel_varme"]),
    ("Hvad gør jeg, hvis der ikke kommer fjernvarme i mit område?", "Ligger din bolig ikke i et markeret område på kommunens kort, er der ingen umiddelbare planer om fjernvarme eller ø-varme. Så er en individuel løsning som en varmepumpe det typiske valg – og du kan søge tilskud, hvis du opfylder kravene.", ["hel_fj", "hel_varme", "se_vpp"]),
  ],
}
CONTACTS["hinnerup"] = {"sol": [("Favrskov Kommune, Byggeri", "89 64 10 10 · byg@favrskov.dk", "hin_byg")],
                        "vp":  [("Hinnerup Fjernvarme", "86 98 53 40 · info@hinnerupfjernvarme.dk", "hin_ber")]}
CONTACTS["helsinge"] = {"sol": [("Gribskov Kommune, Center for Teknik og Borgerservice", "72 49 60 00", "hel_byg")],
                        "vp":  [("Helsinge Fjernvarme", "48 79 52 25 · kontor@helsingefjernvarme.dk", "hel_ber")]}

# keyword-backlog 18/11 2026: 'fjernvarmeanlæg vejle' (GSC 16 visninger, pos. 52,7) -> tilslutningspriser fra Vejle Fjernvarmes takstblad på FV-siden
S["vf_takst"] = ("Vejle Fjernvarme: takster og regler for tilslutning pr. 1. januar 2026 (PDF, læst 18/11 2026)", "https://vejlefjernvarme.dk/p/Vejle%20Fjernvarme/Filer/Takster%20og%20regler%20for%20tilslutning%20pr.%201.%20januar%202026.pdf/Takster-og-regler-for-tilslutning-pr.-1.-januar-2026.pdf")
CITIES["vejle"]["fv_title"] = "Fjernvarme i Vejle: tilslutning, pris og varmepumpe | Energitjekket"
CITIES["vejle"]["updated"] = ("18. november 2026", "2026-11-18")

# keyword-backlog 18/11 2026: 'solceller københavn' (GSC 15 visninger, pos. 39,7) -> mere af Københavns Kommunes arkitektoniske retningslinjer (PDF juli 2026) på /solceller/koebenhavn/
CITIES["koebenhavn"]["updated"] = ("18. november 2026", "2026-11-18")
CITIES["koebenhavn"]["sol_facts"] = CITIES["koebenhavn"]["sol_facts"] + [
    ("Af hensyn til arkitekturen kan solceller i nogle tilfælde <strong>kun sættes op mod gård- eller bagsiden</strong>, og i områder med høje bevaringsværdier som Indre By kan det være vanskeligt at indpasse dem.", ["kbh_solret"]),
]
CITIES["koebenhavn"]["sol_faq"] = [
    ("Hvordan skal solceller se ud på et hus i København?", "Københavns Kommunes retningslinjer siger bl.a., at panelerne så vidt muligt skal have samme farve som tagmaterialet, passe til tagets form, rytme og linjer og være refleksfrie. Inddækninger og blændstykker skal have samme farve som solcellerne, rør og kabler må ikke være synlige, og der skal være afstand til tagkip, tagkanter, hjørner og gesims.", ["kbh_solret"]),
] + CITIES["koebenhavn"]["sol_faq"] + [
    ("Kan jeg kombinere solceller med et grønt tag i København?", "Ja. Kommunens retningslinjer opfordrer dig til at overveje, om solcellerne kan kombineres med andre bæredygtige tiltag som et grønt tag, og viser som eksempel standardmoduler på stativ på den flade del af et københavnertag med grønt tag.", ["kbh_solret"]),
]

# ---------- daglig by-rutine 19. nov. 2026: Middelfart (DK1, Middelfart Kommune) og Tønder (DK1, Tønder Kommune) ----------
S.update({
 "mid_byg": ("Middelfart Kommune: byggetilladelser – solceller, jordvarme og gebyrer (læst 19/11 2026)", "https://middelfart.dk/bolig/byggetilladelser"),
 "mid_vplan": ("Middelfart Kommune: Varmeplan Middelfart 2022 og FAQ (læst 19/11 2026)", "https://middelfart.dk/bolig/varmeplan"),
 "mid_baer": ("Middelfart Kommune, Klima-, Natur- og Genbrugsudvalget 7/10 2026: individuel forsyning af Båring-Asperup (via Sagsvagt)", "https://sagsvagt.dk/sag/middelfart-2026-10-07-klima-natur-og-genbrugsudvalget-3.html"),
 "mf_takst": ("Middelfart Fjernvarme: takstblad gældende pr. 1. januar 2026 (PDF)", "https://middelfartfjernvarme.dk/p/Middelfart%20Fjernvarme/Filer/Takstblad/Takstblad-2026---G%C3%A6ldende-fra-01-01-2026--endelig-.pdf"),
 "mf_tilsl": ("Middelfart Fjernvarme: pris for tilslutning 2026 (læst 19/11 2026)", "https://middelfartfjernvarme.dk/priser/pris-for-tilslutning"),
 "ton_sol": ("Tønder Kommune: solenergianlæg (opdateret 3/7 2026, læst 19/11 2026)", "https://www.toender.dk/service-og-selvbetjening/bolig-byggeri-og-affald/byggeri/solenergianlaeg/"),
 "ton_byg": ("Tønder Kommune: byggetilladelse og byggesagsgebyr (opdateret 15/9 2026, læst 19/11 2026)", "https://www.toender.dk/service-og-selvbetjening/bolig-byggeri-og-affald/byggeri/byggetilladelse/"),
 "ton_olie": ("Tønder Kommune: olietanke (opdateret 3/7 2026, læst 19/11 2026)", "https://www.toender.dk/service-og-selvbetjening/bolig-byggeri-og-affald/affald-og-miljoe/olietanke/"),
 "ton_kp": ("Tønder Kommune: Kommuneplan 2017-2029, varmeforsyning", "https://toender.cowiplan.dk/kommuneplan17/hovedstruktur/energi-og-klima/varmeforsyning/"),
 "tf_fakta": ("Tønder Fjernvarmeselskab: fakta (læst 19/11 2026)", "https://tonder-fjernvarme.dk/om-os-2/fakta"),
 "tf_priser": ("Tønder Fjernvarmeselskab: priser 1/1-31/12 2026 (læst 19/11 2026)", "https://tonder-fjernvarme.dk/oekonomi/priser"),
 "tf_rosin": ("Tønder Dagblad: 45 huse på Rosinfeltvej kan få fjernvarme (6/11 2026)", "https://tonderdagblad.dk/article/45-huse-paa-rosinfeltvej-kan-faa-fjernvarme---projekt-til-8-millioner-kr-56644"),
})
CITIES["middelfart"] = {
  "name": "Middelfart", "kommune": "Middelfart Kommune", "updated": ("19. november 2026", "2026-11-19"),
  "sol_intro": "Solceller i Middelfart: Middelfart Kommune vil have en redegørelse, før du lægger solceller på taget – både for den ekstra last på tagkonstruktionen og for brandvæsenets adgang. Øges lasten med mere end 5 %, kræver anlægget byggetilladelse. Her er reglerne, tallene og vejen til et tilbud.",
  "sol_facts": [
    ("Ved solceller på tag skal du sende en <strong>redegørelse</strong> til teknik@middelfart.dk om, hvorvidt anlægget øger lastpåvirkningen på bygningen med mere eller mindre end <strong>5 %</strong>.", ["mid_byg"]),
    ("Øges lasten med mere end 5 %, kræver anlægget <strong>byggetilladelse</strong>, som søges via Byg og Miljø.", ["mid_byg"]),
    ("Du skal også redegøre for, om <strong>brandvæsenets indsatsmuligheder</strong> ændres; kommunen sender redegørelsen videre til TrekantBrand.", ["mid_byg"]),
    ("Byggesager koster <strong>800 kr. pr. time</strong> for private, og Middelfart Kommune opkræver ikke gebyr, hvis du får afslag.", ["mid_byg"]),
  ],
  "sol_faq": [
    ("Skal jeg søge byggetilladelse til solceller i Middelfart?", "Kun hvis anlægget øger lastpåvirkningen på bygningen med mere end 5 %. Men du skal under alle omstændigheder sende en redegørelse om lasten og om brandvæsenets indsatsmuligheder til teknik@middelfart.dk, før anlægget sættes op.", ["mid_byg"]),
    ("Hvorfor skal brandvæsenet vurdere mine solceller i Middelfart?", "Solceller på tag og facade kan påvirke adgangen til taget ved brand, muligheden for at ventilere eller slukke oppefra, risikoen for brandspredning og give elektriske farer for redningsfolkene. Middelfart Kommune sender derfor redegørelsen til TrekantBrand.", ["mid_byg"]),
  ],
  "vp_intro": "Varmepumpe i Middelfart: lidt over halvdelen af husene i Middelfart Kommune har fjernvarme, mens knap hvert femte stadig har naturgas. I Båring-Asperup er et planlagt fjernvarmeområde netop aflyst, så husene dér skal have individuel varme. Her er tallene, planerne og priserne.",
  "vp_facts": [
    ("Kortet i <strong>Varmeplan Middelfart 2022</strong> viser godkendte fjernvarmeområder, og hvor forsyningsselskaberne planlægger at udvide.", ["mid_vplan"]),
    ("Bor du i et område, der er <strong>godkendt til fjernvarme</strong>, kan du ikke få tilskud til en varmepumpe, og kommunen anbefaler at vente på fjernvarmen.", ["mid_vplan"]),
    ("Den 7. oktober 2026 godkendte kommunen, at et tidligere godkendt fjernvarmeområde i <strong>Båring-Asperup med ca. 373 ejendomme</strong> i stedet overgår til individuel opvarmning, fx varmepumper.", ["mid_baer"]),
    ("Et <strong>jordvarmeanlæg</strong> skal anmeldes eller have tilladelse fra kommunen, før du etablerer det.", ["mid_byg"]),
  ],
  "vp_faq": [
    ("Hvorfor blev fjernvarmen i Båring-Asperup droppet?", "En ny gennemregning i august 2026 viste, at fjernvarme ikke længere var den bedste løsning – bl.a. fordi færre end ventet ville tilsluttes. Individuel opvarmning er ifølge beregningerne ca. 11,5 mio. kr. billigere for samfundet over 20 år og giver knap 80 % lavere CO2-udledning med nutidens tal.", ["mid_baer"]),
    ("Skal jeg søge om jordvarme i Middelfart Kommune?", "Ja. Middelfart Kommune skriver, at et jordvarmeanlæg først skal anmeldes eller have tilladelse, og at du også skal kontakte kommunen, når anlægget færdigmeldes eller sløjfes.", ["mid_byg"]),
  ],
}
CITIES["toender"] = {
  "name": "Tønder", "kommune": "Tønder Kommune", "updated": ("19. november 2026", "2026-11-19"),
  "sol_intro": "Solceller i Tønder: på taget eller facaden af et enfamiliehus, rækkehus eller sommerhus kræver solceller som udgangspunkt ikke byggetilladelse i Tønder Kommune – medmindre byggeretten overskrides, huset er fredet eller bevaringsværdigt, eller en lokalplan eller servitut siger andet. Her er reglerne, tallene og vejen til et tilbud.",
  "sol_facts": [
    ("Solceller og solfangere <strong>på eller i tagfladen eller facaden</strong> af et enfamiliehus, sommerhus, rækkehus eller udhus kræver ikke byggetilladelse, medmindre byggeretten overskrides.", ["ton_sol"]),
    ("Er huset <strong>fredet eller bevaringsværdigt</strong>, eller kræver en lokalplan eller servitut det, skal du søge tilladelse.", ["ton_sol"]),
    ("Anlæg <strong>direkte på terræn</strong> regnes som en selvstændig konstruktion og kræver byggetilladelse – og i landzone også landzonetilladelse.", ["ton_sol"]),
    ("Kræver anlægget byggetilladelse, koster sagsbehandlingen <strong>783 kr. pr. time</strong>, og servicemålet er 4-8 uger.", ["ton_byg"]),
  ],
  "sol_faq": [
    ("Skal jeg søge om solceller på taget i Tønder?", "Normalt ikke, hvis anlægget sidder på eller i tagfladen eller facaden af et enfamiliehus, rækkehus, sommerhus eller udhus og holder sig inden for byggeretten. Er huset fredet eller bevaringsværdigt, eller kræver lokalplanen eller en servitut det, skal du søge.", ["ton_sol"]),
    ("Hvornår kræver solceller landzonetilladelse i Tønder Kommune?", "Når anlægget står på jorden i landzone, sidder på landbrugs-, industri- eller erhvervsbygninger, eller overskrider byggeretten – fx tæt på skel med en højde over 2,5 m.", ["ton_sol"]),
  ],
  "vp_intro": "Varmepumpe i Tønder: Tønder Kommune har en af de højeste andele huse med elvarme og med oliefyr blandt byerne på dette site, og meget få huse er bygget efter år 2000. Her er tallene, fjernvarmeplanerne i Tønder by og priserne – så du kan se, om varmepumpen er det rigtige valg for dit hus.",
  "vp_facts": [
    ("Ifølge Kommuneplan 2017-2029 forsynede de <strong>fem større varmeværker</strong> – Bredebro, Løgumkloster, Skærbæk, Toftlund og Tønder – 7.324 husstande med fjernvarme medio 2018.", ["ton_kp"]),
    ("Kommuneplanen har som mål at <strong>udbrede individuelle og kollektive varmepumpeløsninger</strong> i områder uden kollektiv varmeforsyning.", ["ton_kp"]),
    ("Skifter du oliefyret ud, skal <strong>sløjfning af olietanken</strong> meddeles kommunen senest 4 uger efter via Byg og Miljø.", ["ton_olie"]),
    ("Kender du ikke alderen på en <strong>overjordisk olietank</strong>, skal den ifølge Tønder Kommune sløjfes nu.", ["ton_olie"]),
  ],
  "vp_faq": [
    ("Hvad skal jeg gøre med olietanken, når jeg får varmepumpe i Tønder?", "Sløjfningen skal meddeles Tønder Kommune skriftligt via Byg og Miljø senest 4 uger efter, at den er sket. Tjek samtidig, at oplysningerne om tanken i BBR er rigtige – det er dit ansvar som grundejer.", ["ton_olie"]),
    ("Kan jeg få fjernvarme i stedet for varmepumpe i Tønder by?", "Måske. Tønder Fjernvarme vil fx lægge rør ud til 45 ejendomme på Rosinfeltvej, hvis nok husejere skriver kontrakt – ingen kan tvinges til at tilslutte sig. Bor du uden for nettene, er en varmepumpe det typiske valg. Kontakt Tønder Fjernvarme for status på din adresse.", ["tf_rosin"]),
  ],
}
CONTACTS["middelfart"] = {"sol": [("Middelfart Kommune, Teknik- og Miljøforvaltningen", "88 88 55 00 · teknik@middelfart.dk", "mid_byg")],
                          "vp":  [("Middelfart Fjernvarme", "64 41 03 42 · post@middelfartfjernvarme.dk", "mf_tilsl")]}
CONTACTS["toender"] = {"sol": [("Tønder Kommune, Byggeri", "74 92 92 92 · toender@toender.dk", "ton_byg")],
                       "vp":  [("Tønder Fjernvarmeselskab", "74 72 28 01 · e-mail@tonder-fjernvarme.dk", "tf_priser")]}

# keyword-backlog 19/11 2026: 'jordvarme silkeborg' (GSC 13 visninger, pos. 71,5) -> jordvarme-regler på /varmepumpe/silkeborg/
S.update({"sil_jord": ("Silkeborg Kommune: jordvarmeanlæg (læst 19/11 2026)", "https://silkeborg.dk/borger/klima-og-energi/jordvarmeanlaeg")})
CITIES["silkeborg"]["vp_intro"] = "Varmepumpe i Silkeborg: Silkeborg Forsyning lægger fjernvarme ud i en række byer uden for Silkeborg, bl.a. Virklund, Sejs-Svejbæk, Them og Salten. Bor du dér, skal du nok ikke have varmepumpe. Bor du uden for projekterne, er en luft til vand-varmepumpe eller jordvarme et oplagt valg. Her er status, reglerne for jordvarme i Silkeborg Kommune, priserne og tallene."
CITIES["silkeborg"]["vp_facts"] = CITIES["silkeborg"]["vp_facts"] + [
    ("<strong>Jordvarme i Silkeborg:</strong> du skal søge tilladelse eller anmelde anlægget hos Silkeborg Kommune via Byg og Miljø, før du etablerer det. Et vandret, ikke-industrielt anlæg uden for særlige drikkevandsområder kan anmeldes – hører du ikke fra kommunen inden for 4 uger, må du gå i gang.", ["sil_jord"]),
    ("Jordvarmeslanger og installationer skal ligge mindst <strong>50 m fra en drikkevandsbrønd eller -boring</strong>, og der er normalt 100 m beskyttelseszone om gravhøje. Anlægget skal tæthedsprøves, færdigmeldes og efterses af en sagkyndig efter et år.", ["sil_jord"]),
]
CITIES["middelfart"]["vp_title"] = "Varmepumpe Middelfart: luft til vand, tilskud, pris | Energitjekket"
CITIES["middelfart"]["fv_title"] = "Fjernvarme eller varmepumpe i Middelfart? Pris 2026 | Energitjekket"

# ---------- daglig by-rutine 20. nov. 2026: Rønne (DK2, Bornholms Regionskommune) og Hobro (DK1, Mariagerfjord Kommune) ----------
S.update({
 "brk_sol": ("Bornholms Regionskommune: solcelleanlæg, husstandsvindmøller, jordvarme (læst 20/11 2026)", "https://bornholm.dk/service-og-selvbetjening/by-og-bolig/byggeri-og-nedrivning/solcelleanlaeg-hustandsvindmoeller-jordvarme"),
 "brk_gebyr": ("Bornholms Regionskommune: sagsbehandlingstider og gebyrer for byggesager (læst 20/11 2026)", "https://bornholm.dk/service-og-selvbetjening/by-og-bolig/byggeri-og-nedrivning/skal-du-bygge/sagsbehandlingstider-og-gebyrer"),
 "rvv_priser": ("Rønne Varme A/S: varmepriser 1/1-31/12 2026 (læst 20/11 2026)", "https://rvv.dk/fjernvarme/varmepriser/"),
 "rvv_fv": ("Rønne Varme A/S: fjernvarme – hvor varmen produceres (læst 20/11 2026)", "https://rvv.dk/fjernvarme/"),
 "beof_tilsl": ("Bornholms Energi & Forsyning: sådan får du fjernvarme – priser for tilslutning (læst 20/11 2026)", "https://beof.dk/vores-varme/saadan-faar-du-fjernvarme/"),
 "beof_takst": ("Bornholms Energi & Forsyning: takster og gebyrer pr. 1/7 2026 (læst 20/11 2026)", "https://beof.dk/vores-varme/priser-og-gebyrer/"),
 "bnu_rvv": ("Bornholm.nu: RVV – høje indkøbspriser presser fjernvarmeprisen (28/1 2026)", "https://bornholm.nu/nyheder/rvv-hoeje-indkoebspriser-presser-fjernvarmeprisen/134985"),
 "mfk_sol": ("Mariagerfjord Kommune: solcelle- og solfangeranlæg (opdateret 1/7 2026, læst 20/11 2026)", "https://www.mariagerfjord.dk/by-land-og-bolig/byggeri/solcelle-og-solfangeranlaeg"),
 "mfk_solgr": ("Mariagerfjord Kommune: administrationsgrundlag for etablering af solcelleanlæg (PDF)", "https://www.mariagerfjord.dk/media/igihmdd2/solcelle-administrationsgrundlag-hjemmeside_final_tilg_a.pdf"),
 "mfk_gebyr": ("Mariagerfjord Kommune: sagsbehandlingstid og gebyr for byggesager (læst 20/11 2026)", "https://www.mariagerfjord.dk/by-land-og-bolig/byggeri/sagsbehandlingstid-og-gebyr"),
 "mfk_vplan": ("Mariagerfjord Kommune: varmeplan (opdateret 3/3 2026, læst 20/11 2026)", "https://www.mariagerfjord.dk/by-land-og-bolig/klima-og-forsyning/varmeplan"),
 "mfk_vp22": ("Mariagerfjord Kommune: Varmeplan december 2022 (PDF)", "https://www.mariagerfjord.dk/media/anvownjr/varmeplan-december-2022-tilg-a.pdf"),
 "mfk_status": ("Mariagerfjordposten: status på udrulning af grøn varme – orientering til Udvalget for Klima og Landdistrikter 4/12 2025", "https://mariagerfjordposten.dk/status-paa-groen-varme/"),
 "mfk_fyr": ("Mariagerfjord Kommune: har du et gammelt gas- eller oliefyr? (læst 20/11 2026)", "https://www.mariagerfjord.dk/by-land-og-bolig/klima-og-forsyning/har-du-et-gammelt-gas-eller-oliefyr"),
 "hv_faq": ("Hobro Varmeværk: spørgsmål og svar om tilslutning (læst 20/11 2026)", "https://www.hobrovarme.dk/fjernvarme/spoergsmaal-og-svar/"),
 "hv_home": ("Hobro Varmeværk: forside – varmens oprindelse (læst 20/11 2026)", "https://hobrovarme.dk/"),
 "df_hobro": ("Dansk Fjernvarme: Varmepumper får nyt liv hos Hobro Varmeværk i 2026 (9/12 2025)", "https://danskfjernvarme.dk/aktuelt/nyheder/2025/varmepumper-faar-nyt-liv-hos-hobro-varmevaerk-i-2026"),
})
CITIES["roenne"] = {
  "name": "Rønne", "kommune": "Bornholms Regionskommune", "updated": ("20. november 2026", "2026-11-20"),
  "sol_intro": "Solceller i Rønne og på resten af Bornholm: Bornholms Regionskommune vurderer, at ca. halvdelen af de bornholmske husejere skal have en tilladelse, før de må sætte solceller op – ofte på grund af lokalplaner, deklarationer eller beskyttelseslinjer. Her er reglerne, tallene og vejen til et tilbud.",
  "sol_facts": [
    ("Skønsmæssigt skal <strong>ca. halvdelen af de bornholmske husejere</strong> have en tilladelse, før de må sætte solceller eller solfangere op på huset, skriver kommunen.", ["brk_sol"]),
    ("På et <strong>enfamiliehus eller sommerhus</strong> skal du ikke søge, så længe BR18's højde- og skelregler, lokalplaner, deklarationer, servitutter og beskyttelseslinjerne i naturbeskyttelsesloven er overholdt.", ["brk_sol"]),
    ("Anlæg <strong>på terræn</strong> kræver altid byggetilladelse – det samme gælder erhvervsejendomme, etageboliger og institutioner.", ["brk_sol"]),
    ("Byggesagsgebyret er <strong>993 kr. pr. time</strong> i 2026, og det kan opkræves, selv om du får afslag.", ["brk_gebyr"]),
  ],
  "sol_faq": [
    ("Skal jeg søge om solceller på mit hus i Rønne?", "Ikke hvis det er et enfamiliehus eller sommerhus, og anlægget overholder BR18's regler om højde og skrå højdegrænseplan, lokalplan eller byplanvedtægt, tinglyste deklarationer og beskyttelseslinjer. Så skal du blot selv melde anlægget til BBR via kommunens skema. Strider anlægget mod en af reglerne, skal du søge dispensation via Byg og Miljø.", ["brk_sol"]),
    ("Gælder der særlige regler for svenskehuse på Bornholm?", "Ja. Bornholms Regionskommune skriver, at alle svenskehusene er omfattet af deklarationer, som kan begrænse valget af byggematerialer. Undersøg deklarationen, før du bestiller solceller.", ["brk_sol"]),
  ],
  "vp_intro": "Varmepumpe i Rønne og på Bornholm: næsten ingen huse har naturgas, men næsten hvert ottende hus har stadig elvarme, og fjernvarmen hos Bornholms Varme er blandt de dyreste i landet. Her er tallene, fjernvarmepriserne og reglerne for jordvarme – så du kan se, om varmepumpen er det rigtige valg for dit hus.",
  "vp_facts": [
    ("Rønne forsynes af <strong>Rønne Varme</strong>, der køber varmen fra kraftvarmeværket Bornholms Elproduktion og affaldsforbrændingen BOFA. Resten af øens fjernvarmebyer forsynes af <strong>Bornholms Varme</strong> (BEOF).", ["rvv_fv", "beof_tilsl"]),
    ("Et standardhus betaler <strong>17.526 kr. om året</strong> hos Rønne Varme og <strong>22.669 kr.</strong> hos Bornholms Varme ifølge Forsyningstilsynet (januar 2026) – mod et landsgennemsnit på 16.953 kr.", ["ft_pris"]),
    ("Et <strong>jord- eller bjergvarmeanlæg</strong> skal anmeldes til eller have tilladelse fra kommunen. Ved en anmeldelse må du gå i gang, hvis kommunen ikke gør indsigelse inden 4 uger.", ["brk_sol"]),
    ("Et jordvarmeanlæg skal <strong>efterses én gang om året</strong> af en sagkyndig, og rapporten skal gemmes i 10 år.", ["brk_sol"]),
  ],
  "vp_faq": [
    ("Kan jeg få bjergvarme på Bornholm?", "Ja, det er muligt. Bornholms Regionskommune beskriver både jordvarme med nedgravede slanger og bjergvarme, hvor slangerne sænkes ned i en boring i klippen. Begge dele etableres efter jordvarmebekendtgørelsen og kræver anmeldelse eller tilladelse fra Center for Miljø, Plan og Kultur, før du går i gang.", ["brk_sol"]),
    ("Hvorfor er fjernvarmen dyr i Rønne?", "Ifølge direktøren for Rønne Vand & Varme skyldes det primært høje indkøbspriser på varmen fra BEOF og BOFA, og selskabet har i flere år haft en prisstrid med BEOF (Bornholm.nu, januar 2026). Rønne Varmes pris for et standardhus var uændret fra januar 2025 til januar 2026.", ["bnu_rvv", "ft_pris"]),
  ],
}
CITIES["hobro"] = {
  "name": "Hobro", "kommune": "Mariagerfjord Kommune", "updated": ("20. november 2026", "2026-11-20"),
  "sol_intro": "Solceller i Hobro: i Mariagerfjord Kommune kræver et solcelleanlæg, der følger tagets hældning, som udgangspunkt ikke byggetilladelse – men en lokalplan, en servitut eller en beskyttelseslinje ved fjorden, en å eller en kirke kan ændre det. Her er reglerne, tallene og vejen til et tilbud.",
  "sol_facts": [
    ("Et anlæg på taget, der <strong>følger tagets hældning</strong>, kræver som udgangspunkt ikke byggetilladelse i Mariagerfjord Kommune – men det skal registreres i BBR.", ["mfk_sol"]),
    ("Ligger huset inden for <strong>strand-, sø- eller å-beskyttelseslinjen</strong>, kirkebyggelinjen (bygninger over 8,5 m), fortidsmindebeskyttelseslinjen, et Natura 2000-område eller visse fredninger, kan du skulle søge dispensation.", ["mfk_sol"]),
    ("Anlæg <strong>på terræn</strong> kræver altid byggetilladelse, og i landzone kan der også kræves landzonetilladelse.", ["mfk_sol"]),
    ("Byggesager koster <strong>768 kr. pr. time</strong> i 2026, og den aktuelle ventetid er ca. 8 uger.", ["mfk_gebyr"]),
  ],
  "sol_faq": [
    ("Skal jeg søge om solceller på taget i Hobro?", "Normalt ikke, hvis anlægget følger tagets hældning og ikke går ud over tagets afgrænsning. Tjek dog lokalplan, servitutter og beskyttelseslinjer. Er du i tvivl, kan du skrive til Byggesagsteamet på byg@mariagerfjord.dk. Husk at registrere anlægget i BBR.", ["mfk_sol", "mfk_solgr"]),
    ("Kræver solceller på et fladt tag byggetilladelse i Mariagerfjord?", "Ja. Ifølge kommunens administrationsgrundlag kræver anlæg, der ikke følger tagets hældning eller afgrænsning – fx på stativ på et fladt tag – byggetilladelse, og kommunen lægger vægt på, at naboerne ikke får væsentlige visuelle gener eller skyggegener.", ["mfk_solgr"]),
  ],
  "vp_intro": "Varmepumpe i Hobro og Mariagerfjord: lidt over halvdelen af husene har fjernvarme, men ca. 2.200 boliger med olie eller gas ligger uden for fjernvarmeområderne og kan ikke få fjernvarme, oplyser kommunen. Her er tallene, planerne og priserne – så du kan se, om varmepumpen er det rigtige valg for dit hus.",
  "vp_facts": [
    ("I starten af 2025 blev <strong>ca. 2.850 boliger</strong> i Mariagerfjord Kommune opvarmet med olie eller gas (sommerhuse fraregnet). <strong>Ca. 2.200</strong> af dem ligger uden for fjernvarmeområdet.", ["mfk_status"]),
    ("Varmeplanen deler kommunen i tre områdetyper. I <strong>områdetype 3</strong> forventes der ikke at komme fjernvarme, så her skal husejerne se på individuelle løsninger som varmepumper eller lokale fællesløsninger.", ["mfk_vp22"]),
    ("Varmeplanen er <strong>ikke retsgyldig</strong> og giver ingen tilslutningspligt – udvidelserne afhænger af, at nok husejere tilslutter sig.", ["mfk_vplan"]),
    ("Fjernvarmen til <strong>Hørby Kirkeby og Valsgaard</strong> (ca. 500 boliger) afventer, fordi etableringsprisen er høj og gasprisen forholdsvis lav, og projektet til Falslev og Norup er standset.", ["mfk_status"]),
  ],
  "vp_faq": [
    ("Kommer der fjernvarme til mit hus i Hobro?", "Det afhænger af adressen. Hobro Syd er konverteret, og projektforslaget for Bærkvarteret (Hobro Vest) blev godkendt i juni 2025, mens Hørby Kirkeby og Valsgaard afventer. Se kortet i Mariagerfjord Kommunes varmeplan, eller spørg Hobro Varmeværk. Ligger du i områdetype 3, kommer der ikke fjernvarme foreløbig.", ["mfk_status", "mfk_vplan", "df_hobro"]),
    ("Hvor kan jeg få gratis råd om at skifte oliefyr i Mariagerfjord?", "Mariagerfjord Kommune henviser til Energistyrelsens SparEnergi, der har gratis privat energirådgivning, information om tilskud og om de forskellige typer varmepumper. Kommunen kan ikke selv give individuel sparring.", ["mfk_fyr"]),
  ],
}
CONTACTS["roenne"] = {"sol": [("Bornholms Regionskommune", "56 92 00 00 · post@brk.dk", "brk_sol")],
                      "vp":  [("Rønne Varme A/S (RVV)", "56 91 04 04 · rvv@rvv.dk", "rvv_priser")]}
CONTACTS["hobro"] = {"sol": [("Mariagerfjord Kommune, Byg", "97 11 41 60 · byg@mariagerfjord.dk", "mfk_sol")],
                     "vp":  [("Hobro Varmeværk", "98 52 18 25 · info@hobrovarme.dk", "hv_faq")]}
CITIES["roenne"]["vp_title"] = "Varmepumpe Rønne & Bornholm: elvarme og pris | Energitjekket"
CITIES["roenne"]["reg_title"] = "Solceller Bornholm: regler og byggetilladelse | Energitjekket"
CITIES["hobro"]["reg_title"] = "Solceller Mariagerfjord: regler og tilladelse | Energitjekket"
CITIES["roenne"]["fv_title"] = "Fjernvarme eller varmepumpe i Rønne? Priser 2026 | Energitjekket"

# keyword-backlog 20/11 2026: 'byggetilladelse silkeborg' -> titel på /solceller/silkeborg/regler-og-byggetilladelse/
CITIES["silkeborg"]["reg_title"] = "Byggetilladelse Silkeborg: solceller, gebyr, regler | Energitjekket"

# ---------- daglig by-rutine 23. nov. 2026: Ebeltoft (DK1, Syddjurs Kommune) og Thisted (DK1, Thisted Kommune) ----------
S.update({
 "syd_sol": ("Syddjurs Kommune: solceller og solvarme (læst 23/11 2026)", "https://www.syddjurs.dk/borger/bolig-byggeri-og-flytning/byggeri/naar-du-vil-bygge/solceller-og-solvarme"),
 "syd_gebyr": ("Syddjurs Kommune: sagsbehandling og gebyr på byggesager (opdateret 8/7 2026, læst 23/11 2026)", "https://www.syddjurs.dk/borger/bolig-byggeri-og-flytning/byggeri/naar-du-vil-bygge/sagsbehandling-og-gebyr-paa-byggesager"),
 "syd_fv": ("Syddjurs Kommune: fjernvarme og tilslutningspligt (læst 23/11 2026)", "https://www.syddjurs.dk/borger/bolig-byggeri-og-flytning/bolig/opvarmning-af-bolig/fjernvarme"),
 "syd_energi": ("Syddjurs Kommune: Syddjurs sætter retning for fremtidens energianlæg (byrådsmødet 24/6 2026)", "https://www.syddjurs.dk/nyheder/pressemeddelelser/syddjurs-saetter-retning-for-fremtidens-energianlaeg"),
 "ef_priser": ("Ebeltoft Fjernvarme: priser 2026 inkl. moms (læst 23/11 2026)", "https://www.ebeltoftfjernvarme.dk/oekonomi/priser/"),
 "ef_2026": ("Ebeltoft Fjernvarme: prisstigning i 2026 (25/11 2025)", "https://www.ebeltoftfjernvarme.dk/nyheder/prisstigning-i-2026/"),
 "ef_2025": ("Ebeltoft Fjernvarme: eget elværk i 2025 (18/12 2024)", "https://www.ebeltoftfjernvarme.dk/nyheder/eget-elvaerk-i-2025/"),
 "thi_sol": ("Thisted Kommune: vejledning om solcelleanlæg, version 2.0 (3/9 2025, PDF)", "https://cdn2.gopublic.dk/thistedkommune/Media/638962055650214021/Vejledning_Solceller.pdf"),
 "thi_byg": ("Thisted Kommune: byggeri og nedrivning – byggesagsgebyr 2026 (læst 23/11 2026)", "https://www.thisted.dk/service-and-selvbetjening/bolig-byggeri-and-flytning/byggeri-og-nedrivning"),
 "thi_varme": ("Thisted Kommune: miljøvenlig varmeforsyning – fjernvarme, jordvarme og varmepumper (læst 23/11 2026)", "https://www.thisted.dk/service-and-selvbetjening/bolig-byggeri-and-flytning/min-bolig/miljoevenlig-varmeforsyning"),
 "tvf_2026": ("Thisted Varmeforsyning: varsling af prisstigning 2026 (læst 23/11 2026)", "https://thisted-varmeforsyning.dk/nyheder/varsling-af-prisstigning-2026"),
 "tvf_prod": ("Thisted Varmeforsyning: produktion – anlæg og adresser (læst 23/11 2026)", "https://www.thisted-varmeforsyning.dk/profil/produktion/"),
 "kun_snedsted": ("KunThy: Fjernvarme-planer i Midtthy stilles i bero (13/10 2026)", "https://kunmedierne.dk/thy/fjernvarme-planer-i-midtthy-stilles-i-bero-varmepumperne-har-holdt-deres-indtog/"),
 "dbt_vest": ("Dagbladet Thisted: Varmepumper og ny tank ved Vestervig Fjernvarme (20/11 2026)", "https://dagbladetthisted.dk/article/varmepumper-og-ny-tank-ved-vestervig-fjernvarme---okonomiudvalget-anbefaler-kommunalbestyrelsen-har-sidste-ord-62959"),
})
CITIES["ebeltoft"] = {
  "name": "Ebeltoft", "kommune": "Syddjurs Kommune", "updated": ("23. november 2026", "2026-11-23"),
  "sol_intro": "Solceller i Ebeltoft og resten af Syddjurs: på et parcelhus, rækkehus eller sommerhus kræver solceller som udgangspunkt hverken byggetilladelse eller anmeldelse – men anlægget tæller med i bygningshøjden, og lokalplaner og deklarationer kan sætte grænser. Her er reglerne, tallene og vejen til et tilbud.",
  "sol_facts": [
    ("Solceller på <strong>enfamilie-, tofamilie-, række- og sommerhuse</strong> og deres småbygninger kan sættes op uden byggetilladelse eller anmeldelse efter byggeloven, skriver Syddjurs Kommune.", ["syd_sol"]),
    ("Anlægget skal <strong>medregnes i bygningshøjden</strong>, som stadig skal være overholdt, hvis du vil undgå en byggetilladelse.", ["syd_sol"]),
    ("Ved anlæg <strong>på terræn</strong> afgør kommunen, om der kræves tilladelse – du skal derfor altid sende projektmateriale ind.", ["syd_sol"]),
    ("Byggesagsgebyret er <strong>731 kr. pr. time</strong> i 2026, og ved afslag opkræves samme gebyr – dog højst 10.000 kr.", ["syd_gebyr"]),
  ],
  "sol_faq": [
    ("Skal jeg søge om solceller på mit hus i Ebeltoft?", "Normalt ikke, hvis det er et enfamilie-, tofamilie-, række- eller sommerhus, og anlægget holder sig inden for bygningshøjden. Men lokalplaner, byplanvedtægter og tinglyste deklarationer kan regulere eller ligefrem forbyde solceller, så tjek dem først. Nederst på kommunens side kan du se, om din ejendom er omfattet af en lokalplan.", ["syd_sol"]),
    ("Hvad skal jeg sende til Syddjurs Kommune ved solceller på terræn?", "En målfast situationsplan med terrænkoter, panelernes mål og placering og afstanden til vej-, sti- og naboskel og eksisterende bygninger. Er du ikke selv ejer, skal der også være en fuldmagt fra ejeren. Kommunen afgør derefter, om anlægget kræver byggetilladelse.", ["syd_sol"]),
  ],
  "vp_intro": "Varmepumpe i Ebeltoft og Syddjurs: ingen huse i kommunen har naturgas, men hvert niende har stadig elvarme – og næsten hvert femte har allerede en varmepumpe. Her er tallene, fjernvarmepriserne og planerne – så du kan se, om varmepumpen er det rigtige valg for dit hus.",
  "vp_facts": [
    ("Hos Ebeltoft Fjernvarme kan et hus <strong>uden vandbåret anlæg</strong> (fx med elpaneler) tilsluttes for et samlet tilslutningsbidrag på <strong>12.500 kr.</strong> inkl. 10 m stikledning.", ["ef_priser"]),
    ("Ebeltoft Fjernvarme hævede det faste bidrag fra 19,94 til <strong>24,75 kr. pr. m²</strong> i 2026 – ca. 67 kr. mere om måneden for et standardhus på 125 m².", ["ef_2026"]),
    ("Byrådet besluttede 24. juni 2026 at prioritere en <strong>udvidelse af Rønde Fjernvarmeværk</strong> som det første projekt i den videre energiplanlægning.", ["syd_energi"]),
    ("Tilslutningspligt til fjernvarme gælder kun, hvor kommunen pålagde den <strong>før 1. januar 2019</strong> – nye pligter kan ikke længere pålægges.", ["syd_fv"]),
  ],
  "vp_faq": [
    ("Kan jeg få fjernvarme i Ebeltoft, hvis jeg har elvarme?", "Ebeltoft Fjernvarme har en særlig tilslutningspris for ejendomme uden vandbåret anlæg: 12.500 kr. i samlet tilslutningsbidrag inkl. 10 m stikledning. Længere stik faktureres ekstra. Prislisten dækker tilslutningen – ikke installationen inde i huset.", ["ef_priser"]),
    ("Har jeg pligt til at tilslutte mig fjernvarme i Syddjurs?", "Kun hvis kommunen pålagde din ejendom tilslutningspligt før 1. januar 2019. Folkepensionister, der har ejet og boet i huset siden beslutningen, kan søge dispensation, og nye lavenergihuse kan søge fritagelse for både tilslutnings- og forblivelsespligt.", ["syd_fv"]),
  ],
}
CITIES["thisted"] = {
  "name": "Thisted", "kommune": "Thisted Kommune", "updated": ("23. november 2026", "2026-11-23"),
  "sol_intro": "Solceller i Thisted og Thy: Thisted Kommune kræver som udgangspunkt ikke byggetilladelse til solceller på et parcelhus, rækkehus eller sommerhus – men kun hvis panelerne ligger helt plant med tagfladen. Over halvdelen af husene har fibercementtag. Her er reglerne, tallene og vejen til et tilbud.",
  "sol_facts": [
    ("Solceller på <strong>enfamiliehuse, dobbelthuse, rækkehuse og sommerhuse</strong> og deres garager, carporte og udhuse kræver som udgangspunkt ikke byggetilladelse i Thisted Kommune.", ["thi_sol"]),
    ("Det forudsætter, at anlægget ligger <strong>helt plant med tagfladen</strong>, overholder skelafstanden og ikke strider mod lokalplan, deklarationer eller andre tinglysninger – fx et krav om rød tegl.", ["thi_sol"]),
    ("Anlæg <strong>på terræn</strong> kræver altid byggetilladelse, og i landzone også landzonetilladelse.", ["thi_sol"]),
    ("Byggesagsgebyret er <strong>699 kr. pr. time</strong> i 2026 (677 kr. i 2025).", ["thi_byg"]),
  ],
  "sol_faq": [
    ("Må jeg vinkle solcellerne op på taget i Thisted?", "Så kræver det som regel en byggetilladelse. Kommunens vejledning gør det til en betingelse for undtagelsen, at anlægget ligger helt plant med den eksisterende tagflade – vinkles panelerne ud fra taget, ændrer det bygningens højde.", ["thi_sol"]),
    ("Skal jeg have landzonetilladelse til solceller i Thy?", "Ikke til solceller på selve boligen. Et anlæg på terræn i landzone kræver både byggetilladelse og landzonetilladelse. Kommunen giver normalt landzonetilladelse til anlæg til privat brug, hvis det ikke virker skæmmende eller reflekterende i landskabet og ikke er til gene for naboerne.", ["thi_sol"]),
  ],
  "vp_intro": "Varmepumpe i Thisted og Thy: seks ud af ti huse har fjernvarme, men 1.477 huse har stadig oliefyr, og fjernvarmeplanerne for fem landsbyer i Midtthy er trukket tilbage, fordi mange har valgt varmepumpe. Her er tallene, priserne og planerne – så du kan se, om varmepumpen er det rigtige valg for dit hus.",
  "vp_facts": [
    ("Thisted Varmeforsyning hævede forbrugsprisen fra 570 til <strong>656,25 kr. pr. MWh</strong> 1. januar 2026 på grund af højere brændsels- og CO₂-omkostninger. Abonnement og effektbidrag er uændrede.", ["tvf_2026"]),
    ("Et standardhus betaler <strong>15.228 kr. om året</strong> hos Thisted Varmeforsyning – <strong>3.278 kr. (27,4 %) mere</strong> end i januar 2025 ifølge Forsyningstilsynet.", ["ft_pris"]),
    ("Fjernvarmeprojektet for <strong>Vilsund, Sundby, Koldby, Hørdum og Hundborg</strong> fra værket i Snedsted er trukket tilbage på grund af for lille interesse – mange har i stedet installeret varmepumper.", ["kun_snedsted"]),
    ("Et <strong>jordvarmeanlæg</strong> skal anmeldes eller søges hos Thisted Kommune, før det etableres, og færdigmeldes senest 14 dage efter tæthedsprøvningen.", ["thi_varme"]),
  ],
  "vp_faq": [
    ("Kræver en luft til vand-varmepumpe tilladelse i Thisted Kommune?", "Nej. Kommunen skriver, at en luftvarmepumpe ikke kræver tilladelse, men den skal overholde Miljøstyrelsens vejledende støjgrænser ved skel. Energistyrelsens støjberegner kan hjælpe dig med at finde den bedste placering, før du køber.", ["thi_varme"]),
    ("Hvad sker der med fjernvarmen i Vestervig?", "Økonomiudvalget anbefaler, at der sættes en lokalplan i gang, så Vestervig Fjernvarme kan få varmepumper, energioptagere og en ekstra akkumuleringstank på nabogrunden. Kommunalbestyrelsen træffer den endelige beslutning 24. november 2026.", ["dbt_vest"]),
  ],
}
CONTACTS["ebeltoft"] = {"sol": [("Syddjurs Kommune, Byggeri", "87 53 50 00", "syd_sol")],
                        "vp":  [("Ebeltoft Fjernvarme", "86 34 26 55 · mail@ebeltoftfjernvarme.dk", "ef_priser")]}
CONTACTS["thisted"] = {"sol": [("Thisted Kommune, Team Byg", "99 17 21 44 · byggesag@thisted.dk", "thi_byg")],
                       "vp":  [("Thisted Varmeforsyning", "97 92 66 66 · post@t-vf.dk", "tvf_2026")]}

# keyword-backlog 23/11 2026: 'jordvarme holbæk' (GSC 9 visninger, pos. 73,3) -> jordvarme-regler på /varmepumpe/holbaek/
S.update({"hol_jord": ("Holbæk Kommune: jordvarmeanlæg (læst 23/11 2026)", "https://holbaek.dk/service-og-selvbetjening/bolig-og-byggeri/byggeri/jordvarmeanlaeg"),
          "hol_udenfor": ("Holbæk Kommune: opvarmning uden for fjernvarmeområder (læst 23/11 2026)", "https://holbaek.dk/service-og-selvbetjening/teknik-og-miljoe/klima-og-energi-/opvarmning-/opvarmning-udenfor-fjernvarmeomraader")})
CITIES["holbaek"]["vp_title"] = "Varmepumpe Holbæk: luft til vand, jordvarme, tilskud | Energitjekket"
CITIES["holbaek"]["vp_intro"] = CITIES["holbaek"]["vp_intro"].replace("Her er status, priserne og tilskudsreglerne.", "Her er status, priserne, tilskudsreglerne og reglerne for jordvarme i Holbæk Kommune.")
CITIES["holbaek"]["vp_facts"] = CITIES["holbaek"]["vp_facts"] + [
    ("<strong>Jordvarme i Holbæk:</strong> meget store dele af Holbæk Kommune er udpeget som område med særlige drikkevandsinteresser eller indvindingsopland, så de fleste skal <strong>søge om tilladelse</strong> via Byg og Miljø. Uden for de områder kan et vandret anlæg anmeldes mindst 4 uger før etableringen.", ["hol_jord"]),
    ("Kommunen kalder jordvarme en <strong>oplagt erstatning for oliefyr</strong> i et helårshus, men skriver også, at det kræver plads og koster en del at anlægge jordslangerne.", ["hol_udenfor"]),
]
# keyword-backlog 23/11 2026: 'fjernvarme haderslev' -> kilde til Haderslev Fjernvarmes priser 2026/2027 (FV-siden, data_sub.py)
S.update({"hfv_priser": ("Haderslev Fjernvarme: priser pr. 1/1 2026 og 1/1 2027 (læst 23/11 2026)", "https://www.haderslev-fjernvarme.dk/oekonomi/priser/")})
CITIES["haderslev"]["fv_title"] = "Fjernvarme Haderslev: priser 2026-2027 og udvidelse | Energitjekket"
# ---------- dry-run 25. nov. 2026: Frederiksberg (DK2, Frederiksberg Kommune, vp_page False) ----------
S.update({
 "frb_sol": ("Frederiksberg Kommune: Miljø og energi – solceller (læst 25/11 2026)", "https://www.frederiksberg.dk/by-bolig-og-miljoe/byggeri/miljoe-og-energi"),
 "frb_gebyr": ("Frederiksberg Kommune: Sagsbehandlingstid og gebyr (timepris 1.411 kr., læst 25/11 2026)", "https://www.frederiksberg.dk/by-bolig-og-miljoe/byggeri/sagsbehandlingstid-og-gebyr"),
 "frb_bev": ("Frederiksberg Kommune: Fredede og bevaringsværdige bygninger – tag (læst 25/11 2026)", "https://www.frederiksberg.dk/by-bolig-og-miljoe/byggeri/fredede-og-bevaringsvaerdige-bygninger"),
 "frb_baeredygtig": ("Frederiksberg Kommune: Solceller på tage – Bæredygtig Frederiksberg (læst 25/11 2026)", "https://baeredygtig.frederiksberg.dk/solceller-paa-tagene"),
 "frb_fv_priser": ("Frederiksberg Forsyning: Priser på fjernvarme 2026 inkl. moms (læst 25/11 2026)", "https://www.frb-forsyning.dk/priser/varme"),
 "frb_fv_2026": ("Frederiksberg Forsyning: Dine priser i 2026 (29/12 2025)", "https://www.frb-forsyning.dk/dine-priser-i-2026"),
 "frb_fv_varme": ("Frederiksberg Forsyning: Fordele ved fjernvarme – CTR og fossilfrie brændsler (læst 25/11 2026)", "https://www.frb-forsyning.dk/varme"),
 "frb_fv_miljoe": ("Frederiksberg Forsyning: Miljødeklarationer (læst 25/11 2026)", "https://www.frb-forsyning.dk/om-os/baeredygtighed-i-forsyningen/miljoedeklarationer"),
 "frb_fv_kontakt": ("Frederiksberg Forsyning: Kontakt kundeservice (læst 25/11 2026)", "https://www.frb-forsyning.dk/om-os/kontakt"),
})
CITIES["frederiksberg"] = {
  "name": "Frederiksberg", "kommune": "Frederiksberg Kommune", "updated": ("25. november 2026", "2026-11-25"),
  "vp_page": False, "price_area": "DK2",
  "reg_title": "Solceller Frederiksberg: regler og tilladelse | Energitjekket",
  "fv_title": "Fjernvarme eller varmepumpe på Frederiksberg? 2026 | Energitjekket",
  "sol_intro": "Solceller på Frederiksberg: i Frederiksberg Kommune skal du søge byggetilladelse, før du sætter solceller op – uanset om det er et parcelhus, rækkehus eller en etageejendom. Ni ud af ti huse er fra før 1960, og kommunen vurderer bevaringsværdi og arkitektur i hver enkelt sag. Her er reglerne, tallene og vejen til et tilbud.",
  "sol_facts": [
    ("I Frederiksberg Kommune skal du altid <strong>søge byggetilladelse</strong>, hvis du vil etablere et solcelleanlæg.", ["frb_sol"]),
    ("På skrå tage skal paneler integreres nænsomt i arkitekturen – fx <strong>nedfældet i tagfladen</strong> – og anlæg ovenpå et tag skal følge tagets kanter med afskårne plader.", ["frb_sol"]),
    ("Sagsbehandlingstiden er ca. <strong>7 uger</strong> (ned til 2 uger i enkle sager), og byggesagsgebyret er <strong>1.411 kr. pr. time</strong> (opkræves i to rater).", ["frb_gebyr"]),
    ("På bevaringsværdige bygninger peger kommunen på, at solceller kan integreres i tagfladen mod <strong>gård- eller haveside</strong>, så synlige tagflader mod gaden ikke brydes.", ["frb_bev"]),
  ],
  "sol_faq": [
    ("Skal jeg søge byggetilladelse til solceller på Frederiksberg?", "Ja. Frederiksberg Kommune skriver, at du skal søge byggetilladelse, hvis du vil etablere solcelleanlæg. Med ansøgningen skal du bl.a. vedlægge situationsplan samt målfast tagplan og snittegning af både eksisterende og ønskede forhold.", ["frb_sol"]),
    ("Hvad koster byggetilladelse til solceller på Frederiksberg?", "Timeprisen for byggesagsbehandling er 1.411 kr. pr. time for ansøgninger modtaget efter 1. januar 2024, opkrævet i to rater – og gebyret betales også ved afslag eller tilbagetrækning. Forvent ca. 7 ugers sagsbehandlingstid (ned til 2 uger ved ikke-komplekse sager).", ["frb_gebyr"]),
  ],
  "vp_intro": "Varmepumpe eller fjernvarme på Frederiksberg? Næsten alle parcel- og rækkehuse (97,6 %) har fjernvarme fra Frederiksberg Forsyning, og Danmarks Statistik registrerer ingen huse med naturgas. Her er priserne, varmekilderne og regnestykket.",
  "vp_facts": [
    ("Frederiksberg Forsynings vægtede fjernvarmepris faldt 2,5 % i 2026 til <strong>624,26 kr. pr. MWh</strong> inkl. moms, plus en fast belastningsbetaling på <strong>26,25 kr. pr. m²</strong> etageareal om året.", ["frb_fv_priser", "frb_fv_2026"]),
    ("Varmeprisen skifter måned for måned fra <strong>454,14 kr. pr. MWh i august</strong> til <strong>728,64 kr. pr. MWh i januar</strong> inkl. moms.", ["frb_fv_priser"]),
    ("Fjernvarmen leveres via <strong>CTR</strong> fra hovedstadsområdets kraftvarmeværker og affaldsanlæg, og mindst 85 % stammer fra fossilfrie brændsler.", ["frb_fv_varme"]),
    ("Tilslutning af et nyt matrikelstik koster <strong>8.500 kr. inkl. moms</strong> plus 2,69 kr. pr. m² for de første 10 meter rør.", ["frb_fv_priser"]),
  ],
  "vp_faq": [
    ("Hvad koster fjernvarme på Frederiksberg i 2026?", "Ifølge Frederiksberg Forsynings prisliste er den vægtede årspris 624,26 kr. pr. MWh inkl. moms plus 26,25 kr. pr. m² i årlig belastningsbetaling. For en 125 m² villa med 13,4 MWh svarer det i forsyningens eksempel til 11.646 kr. om året inkl. moms.", ["frb_fv_priser", "frb_fv_2026"]),
    ("Kan det betale sig at skifte til varmepumpe på Frederiksberg?", "For huse, der allerede har fjernvarme, er det sjældent rentabelt, fordi Frederiksberg Forsyning ligger under landsgennemsnittet i Forsyningstilsynets statistik. En varmepumpe er primært relevant for de få boliger med elvarme eller oliefyr.", ["frb_fv_priser", "ft_pris"]),
  ],
}
CONTACTS["frederiksberg"] = {
  "sol": [("Frederiksberg Kommune, By, Byggeri og Ejendomme", "Personlig kontakt kun efter forudgående aftale · frederiksberg.dk", "frb_sol")],
  "vp": [("Frederiksberg Forsyning, kundeservice", "38 18 50 00 · ff@frb-forsyning.dk", "frb_fv_kontakt")],
}

# ---------- daglig by-rutine 25. nov. 2026: Gentofte (DK2, Gentofte Kommune, vp_page True) ----------
S.update({
 "gen_sol_byg": ("Gentofte Kommune: Kræver dit byggeri en byggetilladelse? (læst 25/11 2026)", "https://gentofte.dk/bolig-og-by/byggeri-og-byplanlaegning/kraever-dit-byggeri-en-byggetilladelse/"),
 "gen_ansoeg": ("Gentofte Kommune: Ansøgning om byggetilladelse via Byg- og Miljøportalen (læst 25/11 2026)", "https://gentofte.dk/bolig-og-by/byggeri-og-byplanlaegning/ansoegning-om-byggetilladelse/"),
 "gen_kontakt_byg": ("Gentofte Kommune: Kontakt og vejledning om byggeri – gebyr 888 kr./time inkl. moms og ventetid (læst 25/11 2026)", "https://gentofte.dk/bolig-og-by/byggeri-og-byplanlaegning/kontakt-og-vejledning-om-byggeri/"),
 "gen_bev": ("Gentofte Kommune: Bevaringsværdige bygninger (læst 25/11 2026)", "https://gentofte.dk/bolig-og-by/byggeri-og-byplanlaegning/bevaringsvaerdige-bygninger/"),
 "gen_energi_pdf": ("Gentofte & Frederiksberg Kommune: Kom i gang med energiforbedringer (1/2 2026, PDF)", "https://klima.gentofte.dk/media/pofdgaek/kom-igang-med-energiforbedringer-tgl.pdf"),
 "gen_forsyning": ("Gentofte Kommune: Forsyning – fjernvarmebeslutning 22/6 2026 og jordvarme (læst 25/11 2026)", "https://gentofte.dk/bolig-og-by/miljoe-forsyning-og-klima/forsyning/"),
 "gen_niras": ("Gentofte Kommune / NIRAS: Aflysning af otte udbygningsområder for fjernvarme (4/3 2026, PDF)", "https://gentofte.dk/media/pvnp1d4c/niras-samfundsoekonomiske-analyse.pdf"),
 "gen_fv_takst": ("Gentofte Fjernvarme: Takstblad 2026 inkl. moms (gældende 1/1 2026, PDF)", "https://gentoftefjernvarme.dk/wp-content/uploads/2025/12/Takstblad-for-Gentofte-Fjernvarme-2026.pdf"),
 "gen_fv_tilslut": ("Gentofte Fjernvarme: Takst for tilslutningsbidrag 2026 (PDF)", "https://gentoftefjernvarme.dk/wp-content/uploads/2025/12/Gentofte-Fjernvarme-Takst-for-tilslutningsbidrag-2026.pdf"),
 "gen_fv_2026": ("Gentofte Fjernvarme: Varmeregningen bliver lidt mindre i 2026 (læst 25/11 2026)", "https://gentoftefjernvarme.dk/varmeregningen-bliver-lidt-mindre-i-2026/"),
 "gen_fv_miljoe": ("Gentofte Fjernvarme: Fjernvarmedeklaration 2024 – 94 % fossilfrie brændsler (PDF)", "https://gentoftefjernvarme.dk/wp-content/uploads/2025/11/Miljoedeklaration-2024-for-Gentofte-Fjernvarme-1.0.pdf"),
 "gen_fv_kontakt": ("Gentofte Gladsaxe Fjernvarme: Kontakt kundeservice (læst 25/11 2026)", "https://gentoftefjernvarme.dk/privat/om-os/kontakt/"),
 "ft_pris_aug26": ("Forsyningstilsynet: Statistik om fjernvarmepriser pr. 31/8 2026 (læst 25/11 2026)", "https://forsyningstilsynet.dk/analyser-og-tal/forbrugerpriser/fjernvarmepriser"),
})
CITIES["gentofte"] = {
  "name": "Gentofte", "kommune": "Gentofte Kommune", "updated": ("25. november 2026", "2026-11-25"),
  "vp_page": True, "price_area": "DK2",
  "sol_intro": "Solceller i Gentofte: på en almindelig villa kræver solceller normalt ikke byggetilladelse, medmindre lokalplan eller bevaringsværdi siger andet – og over otte ud af ti huse i kommunen er fra før 1960. Her er reglerne, byggetal og vejen til tilbud.",
  "sol_facts": [
    ("På et <strong>almindeligt hus</strong> kræver solceller som udgangspunkt ikke byggetilladelse, når arbejdet ikke udløser andre tilladelseskrævende ændringer og overholder lokalplanen.", ["gen_sol_byg"]),
    ("Er huset udpeget som <strong>bevaringsværdigt</strong>, skal du søge tilladelse til alle udvendige ændringer – herunder solceller – via Byg- og Miljøportalen som en planmæssig forespørgsel.", ["gen_sol_byg", "gen_bev"]),
    ("<strong>Byggesagsgebyret</strong> afregnes efter tidsforbrug til <strong>888 kr. pr. time inkl. moms</strong>; plansager er gebyrfrie, og det første 30-minutters vejledningsmøde er gratis.", ["gen_kontakt_byg"]),
    ("Når en byggesag er fuldt oplyst, er den forventede <strong>ventetid cirka 2 måneder</strong> til fordeling til sagsbehandler.", ["gen_kontakt_byg"]),
  ],
  "sol_faq": [
    ("Skal man søge byggetilladelse til solceller i Gentofte?", "Normalt ikke på et almindeligt enfamiliehus, hvis lokalplanen er overholdt. Men er huset bevaringsværdigt eller underlagt særlige lokalplanbestemmelser for tagmateriale, skal du søge om tilladelse i Byg- og Miljøportalen.", ["gen_sol_byg", "gen_bev", "gen_ansoeg"]),
    ("Hvad koster sagsbehandling hos Plan og Byg i Gentofte?", "Timeprisen er 888 kr. inkl. moms for projekter omfattet af byggeloven, mens rene plansager er gratis. Både det første 30-minutters vejledningsmøde og det første sagsforberedende møde er uden beregning.", ["gen_kontakt_byg"]),
  ],
  "vp_intro": "Varmepumpe i Gentofte: hvert fjerde parcel- og rækkehus har stadig naturgas, og den 22. juni 2026 besluttede kommunalbestyrelsen at stoppe fjernvarmeudbygningen i otte delområder til fordel for individuelle varmepumper. Her er status, fjernvarmepriser og regler.",
  "vp_facts": [
    ("<strong>Otte fjernvarmeområder aflyst:</strong> den 22. juni 2026 godkendte Gentofte Kommune et projektforslag om at stoppe udrulningen i otte ikke-igangsatte delområder (4.6–4.8 og 5.4–5.8), så boligerne i stedet omlægges til individuelle luft til vand-varmepumper.", ["gen_forsyning", "gen_niras"]),
    ("<strong>Gentofte Fjernvarme 2026:</strong> variabelt bidrag er 334,36 kr./MWh, fast bidrag 575,39 kr./MWh og administrationsbidrag 1.143,01 kr./år inkl. moms – samlet <strong>13.330 kr./år</strong> for et nyt 125 m² standardhus (13,4 MWh).", ["gen_fv_takst", "gen_fv_2026"]),
    ("<strong>Tilslutning til fjernvarme:</strong> standardtilslutningsbidraget i eksisterende områder steg pr. 1. januar 2026 til <strong>90.000 kr. inkl. moms</strong> for effektbehov op til 80 kW (0 kr. i særlige kampagneområder).", ["gen_fv_tilslut"]),
    ("<strong>Jordvarme:</strong> bor du uden for fjernvarmeområdet, kan du søge tilladelse via Byg- og Miljøportalen; anlæg med dybe boringer kræver også VVM-screening.", ["gen_forsyning"]),
  ],
  "vp_faq": [
    ("Får mit område i Gentofte fjernvarme eller skal jeg vælge varmepumpe?", "Kommunalbestyrelsen stoppede 22. juni 2026 den endnu ikke igangsatte fjernvarmeudbygning i otte delområder (4.6, 4.7, 4.8 samt 5.4–5.8), hvor luft til vand-varmepumper var ca. 277 mio. kr. billigere samfundsøkonomisk. Tjek din adresse på Gentofte Gladsaxe Fjernvarmes kort, før du beslutter dig.", ["gen_forsyning", "gen_niras"]),
    ("Hvad koster fjernvarme i Gentofte i 2026?", "I Gentofte Fjernvarmes takstblad for 2026 faldt den samlede pris ca. 2,2 % til 13.330 kr. inkl. moms for et 125 m² standardhus (13,4 MWh). I Forsyningstilsynets statistik for et 130 m² hus med 18,1 MWh er årsprisen 17.609 kr.", ["gen_fv_takst", "gen_fv_2026", "ft_pris_aug26"]),
  ],
}
CONTACTS["gentofte"] = {
  "sol": [("Gentofte Kommune, Plan og Byg", "39 98 37 01 · Plan-byg@gentofte.dk", "gen_kontakt_byg")],
  "vp": [("Gentofte Gladsaxe Fjernvarme, kundeservice", "70 20 58 50 · info@ggfjernvarme.dk", "gen_fv_kontakt")],
}
# ---------- daglig by-rutine 26. nov. 2026: Hvidovre (DK2, Hvidovre Kommune, vp_page True) ----------
S.update({
 "hvi_sol": ("Hvidovre Kommune: Solceller og solfangere (læst 26/11 2026)", "https://www.hvidovre.dk/borger/by-bolig-og-byggeri/varme-og-energi/solceller-og-solfangere"),
 "hvi_bygg": ("Hvidovre Kommune: Ansøg om byggetilladelse – gebyr 1.163 kr. i 2026 og sagsbehandlingstid (læst 26/11 2026)", "https://www.hvidovre.dk/borger/by-bolig-og-byggeri/byggeri-og-byggetilladelse/ansoeg-om-byggetilladelse"),
 "hvi_bev": ("Hvidovre Kommune: Bevaringsværdige bygninger (læst 26/11 2026)", "https://www.hvidovre.dk/borger/by-bolig-og-byggeri/byplanlaegning/bevaringsvaerdige-bygninger"),
 "hvi_lokalplan": ("Hvidovre Kommune: Lokalplaner og byplanvedtægter (læst 26/11 2026)", "https://www.hvidovre.dk/borger/by-bolig-og-byggeri/byplanlaegning/lokalplaner-og-byplanvedtaegter"),
 "hvi_tid": ("Hvidovre Kommune: Kortere ventetid på byggesager i Hvidovre (19/3 2026)", "https://www.hvidovre.dk/om-kommunen/presse/pressemeddelelser/2026/mar/kortere-ventetid-paa-byggesager-i-hvidovre"),
 "hvi_varmeplan": ("Hvidovre Kommune: Varmeplan, vedtaget december 2022 (læst 26/11 2026)", "https://www.hvidovre.dk/borger/by-bolig-og-byggeri/varme-og-energi/varmeplan"),
 "hvi_groen": ("Hvidovre Kommune: Skift til grøn opvarmning (læst 26/11 2026)", "https://www.hvidovre.dk/borger/by-bolig-og-byggeri/varme-og-energi/skift-til-groen-opvarmning"),
 "hvi_fv": ("Hvidovre Fjernvarme: forside med udbygningsområder (læst 26/11 2026)", "https://www.hvidovrefjernvarme.dk/"),
 "hvi_fdh": ("FD Hvidovre: Takstblad 2026, priser gældende fra 1/1 2026 (PDF)", "https://www.hvidovrefjernvarme.dk/wp-content/uploads/2025/12/takstblad-2026_FDH.pdf"),
 "hvi_ave": ("Avedøre Fjernvarme: Takstblad 2026, priser gældende fra 1/1 2026 (PDF)", "https://www.hvidovrefjernvarme.dk/wp-content/uploads/2025/12/Bilag-2.4-Takstblad-2026.pdf"),
 "hvi_ave_om": ("Avedøre Fjernvarme: om selskabet og miljødeklarationer (læst 26/11 2026)", "https://www.hvidovrefjernvarme.dk/avedoere-fjernvarme/"),
 "hvi_hfs": ("Hvidovre Fjernvarmeselskab: om selskabet (læst 26/11 2026)", "https://www.hvidovrefjernvarme.dk/hvidovre-fjernvarmeselskab/"),
})
CITIES["hvidovre"] = {
  "name": "Hvidovre", "kommune": "Hvidovre Kommune", "updated": ("26. november 2026", "2026-11-26"),
  "vp_page": True, "price_area": "DK2",
  "sol_intro": "Solceller i Hvidovre: de fleste anlæg kan sættes op uden tilladelse fra kommunen, men næsten alle ejendomme ligger under en lokalplan eller byplanvedtægt, og over fire ud af ti huse er fra før 1960. Her er reglerne, byggetal og vejen til tilbud.",
  "sol_facts": [
    ("Solceller kan i de fleste tilfælde <strong>opsættes uden tilladelse fra kommunen</strong>, fordi de hverken udvider etagearealet eller giver en væsentlig anvendelsesændring.", ["hvi_sol"]),
    ("Tjek altid <strong>lokalplan eller byplanvedtægt</strong> og om huset er <strong>bevaringsværdigt</strong> – næsten alle ejendomme i Hvidovre Kommune er omfattet af en lokalplan eller byplanvedtægt.", ["hvi_sol", "hvi_bygg"]),
    ("Anlægget bliver en del af bygningen og skal derfor overholde <strong>højde- og afstandskravene</strong> i bygningsreglementets kapitel 8. Kommunen anbefaler, at du bagefter opdaterer BBR.", ["hvi_sol"]),
    ("Skal du alligevel søge byggetilladelse, er gebyret et <strong>fast beløb på 1.163 kr. pr. sag</strong> i 2026, og sagsbehandlingen tager i gennemsnit 2–3 måneder fra sagen er fuldt oplyst.", ["hvi_bygg"]),
  ],
  "sol_faq": [
    ("Skal man søge byggetilladelse til solceller i Hvidovre?", "I de fleste tilfælde ikke, ifølge kommunen, fordi solceller hverken udvider etagearealet eller ændrer anvendelsen. Men er der en lokalplan eller byplanvedtægt med regler om solceller, eller er huset bevaringsværdigt, bør du undersøge reglerne for din adresse, før du bestiller anlægget.", ["hvi_sol", "hvi_lokalplan"]),
    ("Hvad koster byggesagsbehandling i Hvidovre?", "Et fast gebyr på 1.163 kr. pr. sag for ansøgninger indsendt i 2026 (samme beløb som i 2025). Kommunen arbejder efter enkeltsagsprincippet, så flere sagstyper på samme grund – fx nybyggeri, lovliggørelse og nedrivning – giver hver deres gebyr.", ["hvi_bygg"]),
  ],
  "vp_intro": "Varmepumpe i Hvidovre: kun 37 % af parcel- og rækkehusene har fjernvarme, mens næsten halvdelen stadig fyrer med naturgas. Kommunen anbefaler grøn fjernvarme frem for individuelle varmepumper i den tætte, lave bebyggelse. Her er status, priser og regler.",
  "vp_facts": [
    ("<strong>Kommunens anbefaling:</strong> i områder med tæt, lav bebyggelse som villaer og rækkehuse anbefaler Hvidovre Kommune grøn fjernvarme, blandt andet fordi kommunen oplever en del støjklager fra naboer til varmepumper.", ["hvi_groen"]),
    ("<strong>Varmeplan 2022:</strong> kommunalbestyrelsen vedtog i december 2022 en varmeplan for udbredelse af fjernvarmen. Et udbygningsprojekt tager typisk 1–2 år fra start til fjernvarmen er i drift.", ["hvi_varmeplan", "hvi_groen"]),
    ("<strong>Udbygningsområder:</strong> Hvidovre Fjernvarme nævner på sin forside Nymarken og Mågeparken, Strandmark Nord og Avedøre Landsby som områder, hvor der endnu skal lægges rør.", ["hvi_fv"]),
    ("<strong>Varmepumpe alligevel?</strong> Kommunen henviser til Energistyrelsens vejledning om varmepumper og dens støjberegner, før du vælger placering.", ["hvi_groen"]),
  ],
  "vp_faq": [
    ("Kan jeg få fjernvarme i Hvidovre?", "Det afhænger af din adresse. I eksisterende fjernvarmeområder kan du tilsluttes; i udbygningsområderne (nu Nymarken og Mågeparken, Strandmark Nord og Avedøre Landsby) skal nettet først bygges, og et projekt tager typisk 1–2 år fra start. Spørg Hvidovre Fjernvarme, før du vælger en anden løsning.", ["hvi_fv", "hvi_groen", "hvi_hfs"]),
    ("Anbefaler Hvidovre Kommune varmepumper?", "I tæt, lav bebyggelse anbefaler kommunen grøn fjernvarme frem for individuelle varmepumper, bl.a. på grund af støjklager. Vil du alligevel have en varmepumpe, peger kommunen på Energistyrelsens vejledning og støjberegner.", ["hvi_groen"]),
  ],
}
CONTACTS["hvidovre"] = {
  "sol": [("Hvidovre Kommune, Byggesagsteamet (telefonvagt)", "36 39 35 70 · pom@hvidovre.dk", "hvi_bygg")],
  "vp": [("Hvidovre Fjernvarme, kundeservice", "36 38 38 00", "hvi_fv")],
}
# ---------- daglig by-rutine 26. nov. 2026: Hørsholm (DK2, Hørsholm Kommune, vp_page True) ----------
S.update({
 "hsm_sol": ("Hørsholm Kommune: Solceller og varmepumper (læst 26/11 2026)", "https://www.horsholm.dk/borger/bolig-byggeri-og-veje/byggeri/jeg-skal-bygge/solceller-og-varmepumper"),
 "hsm_gebyr": ("Hørsholm Kommune: Byggesagsgebyr – 920 kr. pr. time i 2026 (læst 26/11 2026)", "https://www.horsholm.dk/borger/bolig-byggeri-og-veje/byggeri/jeg-skal-bygge/byggesagsgebyr"),
 "hsm_tid": ("Hørsholm Kommune: Sagsbehandlingstider (læst 26/11 2026)", "https://www.horsholm.dk/borger/bolig-byggeri-og-veje/byggeri/jeg-skal-bygge/sagsbehandlingstider"),
 "hsm_bev": ("Hørsholm Kommune: Bevaringsværdig eller fredet bygning (læst 26/11 2026)", "https://www.horsholm.dk/borger/bolig-byggeri-og-veje/byggeri/jeg-skal-bygge/bevaringsvaerdig-eller-fredet-bygning"),
 "hsm_disp": ("Hørsholm Kommune: Dispensationer og helhedsvurdering (læst 26/11 2026)", "https://www.horsholm.dk/borger/bolig-byggeri-og-veje/byggeri/jeg-skal-bygge/dispensationer"),
 "hsm_kontakt": ("Hørsholm Kommune: Kontakt byggesagsvagten (læst 26/11 2026)", "https://www.horsholm.dk/borger/bolig-byggeri-og-veje/byggeri/kontakt-byggesagsvagten"),
 "hsm_varme": ("Hørsholm Kommune: Varmeforsyning – Norfors og fjernvarme (læst 26/11 2026)", "https://www.horsholm.dk/borger/klima-og-energi/varmeforsyning"),
 "hsm_nf": ("Norfors: Fjernvarme – tilslutning og takster (læst 26/11 2026)", "https://norfors.dk/borger/fjernvarme"),
})
CITIES["hoersholm"] = {
  "name": "Hørsholm", "kommune": "Hørsholm Kommune", "updated": ("26. november 2026", "2026-11-26"),
  "vp_page": True, "price_area": "DK2",
  "sol_intro": "Solceller i Hørsholm: solceller kræver som udgangspunkt ikke byggetilladelse, men næsten hvert andet hus har tegltag, og bevaringsværdige huse skal have kommunens godkendelse til ydre ændringer. Her er reglerne, byggetal og vejen til tilbud.",
  "sol_facts": [
    ("Solceller kræver <strong>som udgangspunkt ikke byggetilladelse</strong>, hvis byggeretten i bygningsreglementets kapitel 8 er overholdt, og anlægget udføres efter de præ-accepterede brandløsninger og bygningsreglementets tekniske kapitler.", ["hsm_sol"]),
    ("Lokalplan, byplanvedtægt eller servitut kan stille krav til solcellers fremtoning – kommunen nævner fx, at anlægget skal være en integreret del af tagfladen med en glansgrad på højst 30.", ["hsm_sol"]),
    ("På huse udpeget som <strong>bevaringsværdige</strong> i Temalokalplan 143 eller en anden lokalplan skal kommunen godkende ændringer af husets ydre; dispensationsansøgningen sendes separat til bom-post@horsholm.dk.", ["hsm_bev"]),
    ("Byggesagsgebyret er <strong>920 kr. pr. time</strong> i 2026 efter faktisk tidsforbrug. Kommunen oplyser 4–5 måneders gennemsnitlig sagsbehandlingstid og 2–3 måneder for enfamiliehuse, der følger plangrundlaget og byggeretten.", ["hsm_gebyr", "hsm_tid"]),
  ],
  "sol_faq": [
    ("Kræver solceller byggetilladelse i Hørsholm Kommune?", "Som udgangspunkt nej, hvis byggeretten er overholdt, og anlægget følger de præ-accepterede løsninger og bygningsreglementets tekniske krav. Kan byggeretten ikke overholdes – fx solceller på et garagetag tæt på skel, der allerede er 2,5 m højt – skal kommunen lave en helhedsvurdering, og du skal søge byggetilladelse.", ["hsm_sol"]),
    ("Hvad koster byggesagsbehandling i Hørsholm?", "Taksten er 920 kr. pr. time i 2026, beregnet efter faktisk tidsforbrug med mindste enhed på ét minut – også ved afslag eller tilbagetrukket ansøgning. Kræver sagen færdigmelding eller ibrugtagningstilladelse, opkræves gebyret i to rater.", ["hsm_gebyr"]),
  ],
  "vp_intro": "Varmepumpe i Hørsholm: over halvdelen af parcel- og rækkehusene fyrer med naturgas, og kun 24 % har fjernvarme fra Norfors. Norfors har trukket projektforslaget om nye fjernvarmeområder tilbage, så mange gasfyrsejere må finde en anden løsning. Her er status, priser og regler.",
  "vp_facts": [
    ("<strong>Nye fjernvarmeområder trukket tilbage:</strong> kommunalbestyrelsen godkendte i september 2024 et fjernvarmeprojekt fra Norfors til høring, men efter Energistyrelsens afgørelse i december 2024 om Usserødværket trak Norfors projektforslaget tilbage.", ["hsm_varme"]),
    ("<strong>Usserødværket og stævning af staten:</strong> Norfors stævnede i slutningen af maj 2026 staten på grund af ændret lovgivning på affaldsområdet. Kommunen oplyser, at kunder med fjernvarme ikke risikerer at stå uden varme, fordi Norfors har forsyningspligt.", ["hsm_varme"]),
    ("<strong>Ingen ny tilslutningspligt:</strong> som udgangspunkt er der ikke tilslutningspligt i Hørsholm Kommune, og der kan ikke pålægges ny tilslutningspligt i nye fjernvarmeområder.", ["hsm_varme"]),
    ("<strong>Varmepumpe:</strong> det kræver ikke byggetilladelse at opsætte en varmepumpe, men anlægget skal overholde bygningsreglementet, og lokalplaner kan regulere placering og afskærmning. Jordvarme kræver tilladelse via Byg og Miljø.", ["hsm_sol", "hsm_varme"]),
  ],
  "vp_faq": [
    ("Kan jeg få fjernvarme i Hørsholm?", "Kun hvis din adresse ligger i et eksisterende fjernvarmeområde hos Norfors. Kommunens varmeplanskort viser, om dit område er udlagt til fjernvarme, og i eksisterende områder kan du bede Norfors om et uforpligtende tilbud. Nye områder venter, efter at projektforslaget blev trukket tilbage.", ["hsm_varme", "hsm_nf"]),
    ("Må jeg beholde mit gasfyr i Hørsholm?", "Ja, ifølge kommunen kan du fortsat varme op med olie- og gasfyr. Regeringens ønske er, at gas er udfaset af rumopvarmning i 2035, men der er endnu ikke taget stilling til, om eller hvornår gasnettet lukkes.", ["hsm_varme"]),
  ],
}
CONTACTS["hoersholm"] = {
  "sol": [("Hørsholm Kommune, byggesagsvagten", "48 49 00 24 · bom-post@horsholm.dk", "hsm_kontakt")],
  "vp": [("Norfors, kundeservice", "45 16 05 00 · norfors@norfors.dk", "hsm_nf")],
}
# ---------- daglig by-rutine 27. nov. 2026: Rødovre (DK2, Rødovre Kommune, vp_page True) ----------
S.update({
 "rod_sol": ("Rødovre Kommune: Vejledning til opsætning af solenergianlæg (læst 27/11 2026)", "https://rk.dk/borger/bolig-og-by/byggeri-og-byplanlaegning/byggeri/vejledning-til-opsaetning-af-solenergianlaeg"),
 "rod_gebyr": ("Rødovre Kommune: Gebyr – byggesagsbehandling, takster 2025 og 2026 (læst 27/11 2026)", "https://rk.dk/borger/bolig-og-by/byggeri-og-byplanlaegning/byggeri/foer-du-bygger/gebyr-byggesagsbehandling"),
 "rod_mal": ("Rødovre Kommune: Servicemål for byggesagsbehandling (læst 27/11 2026)", "https://rk.dk/borger/bolig-og-by/byggeri-og-byplanlaegning/byggeri/foer-du-bygger/servicemaal-for-byggesagsbehandling"),
 "rod_bev": ("Rødovre Kommune: Kulturhistoriske kvaliteter – SAVE-registrering og bevaringsværdige bygninger (læst 27/11 2026)", "https://rk.dk/borger/bolig-og-by/byggeri-og-byplanlaegning/fysisk-planlaegning-i-roedovre-kommune/kulturhistoriske-kvaliteter"),
 "rod_varme": ("Rødovre Kommune: Varmekilder – elvarme, varmepumper og fjernvarme (læst 27/11 2026)", "https://rk.dk/borger/bolig-og-by/grund-og-ejendom/varmekilder"),
 "rkf_om": ("Rødovre Kommunale Fjernvarmeforsyning: Om os og tidslinje (læst 27/11 2026)", "https://www.rodovrefjernvarme.dk/om-os"),
 "rkf_faq": ("Rødovre Kommunale Fjernvarmeforsyning: Spørgsmål og svar om udrulningen (læst 27/11 2026)", "https://www.rodovrefjernvarme.dk/vil-du-have-fjernvarme/spoergsmaal-og-svar"),
 "rkf_ny": ("Rødovre Kommunale Fjernvarmeforsyning: Ændret tidsplan for udrulning af fjernvarme i Rødovre (læst 27/11 2026)", "https://www.rodovrefjernvarme.dk/nyheder/aendret-tidsplan-for-udrulning-af-fjernvarme-i-roedovre"),
 "rkf_takst": ("Rødovre Kommunale Fjernvarmeforsyning: Takstblad 2026 inkl. moms, revision 18. august 2026 (PDF)", "https://www.rodovrefjernvarme.dk/p/R%C3%B8dovre%20Kommunale%20Fjernvarme/PDF/Takster/Takster-2026-med-moms--pr-1-januar-2026--med-udbygningstill%C3%A6g--revision-18-august-2026.pdf"),
 "rkf_forside": ("Rødovre Kommunale Fjernvarmeforsyning: forside – varmen fra VEKS og vedvarende energi (læst 27/11 2026)", "https://www.rodovrefjernvarme.dk/"),
 "rkf_pris": ("Rødovre Kommunale Fjernvarmeforsyning: Information om prisstigninger – varmekilder hos VEKS (læst 27/11 2026)", "https://www.rodovrefjernvarme.dk/nyheder/information-om-prisstigninger"),
 "rkf_fors": ("Rødovre Kommunale Fjernvarmeforsyning: Forsyningsområder og kontakt (læst 27/11 2026)", "https://www.rodovrefjernvarme.dk/om-os/forsyningsomraader"),
})
CITIES["roedovre"] = {
  "name": "Rødovre", "kommune": "Rødovre Kommune", "updated": ("27. november 2026", "2026-11-27"),
  "vp_page": True, "price_area": "DK2",
  "sol_intro": "Solceller i Rødovre: de fleste boligområder er dækket af en lokalplan eller byplanvedtægt, nyere planer kan kræve refleksfri og integrerede anlæg, og over seks ud af ti huse er fra før 1960. Her er reglerne, byggetal og vejen til tilbud.",
  "sol_facts": [
    ("Kommunen beder dig tjekke tre ting, før du sætter solenergianlæg op: om huset er omfattet af <strong>lokalplan, deklaration eller byplanvedtægt</strong>, om det er <strong>bevaringsværdigt eller ligger i et kulturmiljø</strong>, og om anlægget <strong>kræver byggetilladelse</strong>.", ["rod_sol"]),
    ("De fleste boligområder i Rødovre er dækket af en lokalplan eller byplanvedtægt. Nyere planer indeholder typisk bestemmelser om, at <strong>anlæg ikke må være blanke eller reflekterende</strong>, ikke må ses fra vejen og skal godkendes af kommunen.", ["rod_sol"]),
    ("Kommunens otte retningslinjer beder om <strong>refleksfri anlæg</strong>, der følger tagfladens hældning, sættes op som én samlet firkantet flade med mindst en halv meters afstand til kip og kanter, har samme farve som tagmaterialet og har skjulte rør og kabler.", ["rod_sol"]),
    ("Skal du søge byggetilladelse til noget andet end en simpel konstruktion, er gebyret i 2026 <strong>999 kr. pr. medgået time</strong>. Servicemålet for énfamiliehuse er 40 dage fra sagen er tilstrækkeligt oplyst, og den første forhåndsdialog er gratis.", ["rod_gebyr", "rod_mal"]),
  ],
  "sol_faq": [
    ("Skal man søge byggetilladelse til solceller i Rødovre?", "Kommunen opfordrer dig til selv at afklare det sammen med to andre ting: om huset er omfattet af lokalplan, deklaration eller byplanvedtægt, og om det er bevaringsværdigt eller ligger i et kulturmiljø. Eftersom de fleste boligområder har en lokalplan eller byplanvedtægt, bør du kontakte Byggesagsafdelingen på 36 37 70 00, før du bestiller anlægget.", ["rod_sol"]),
    ("Hvad koster byggesagsbehandling i Rødovre?", "I 2026 koster øvrige bygningstyper som énfamiliehuse 999 kr. pr. medgået time, og simple konstruktioner som garager og carporte 1.229 kr. pr. bygning. Kommunen tager ikke gebyr for den første forhåndsdialog.", ["rod_gebyr"]),
  ],
  "vp_intro": "Varmepumpe i Rødovre: 55 % af parcel- og rækkehusene fyrer stadig med naturgas, og kun 29 % har fjernvarme – men kommunen udbygger fjernvarmen frem mod 2032, og elvarme er som hovedregel forbudt, mens varmepumper er undtaget. Her er status, priser og regler.",
  "vp_facts": [
    ("<strong>Elvarmeforbud, men ikke for varmepumper:</strong> i Rødovre er der generelt forbud mod at etablere elvarme, men varmepumper er undtaget. De kræver ikke byggetilladelse, men skal overholde bygningsreglementet og placeres, så du undgår støjgener for dig selv og naboen.", ["rod_varme"]),
    ("<strong>Lokalplan og synlighed:</strong> en lokalplan kan fastlægge varmepumpens placering, og kommunen anbefaler, at den ikke er synlig fra vejen, og at afskærmningen tilpasses husets arkitektur og farver.", ["rod_varme"]),
    ("<strong>Fjernvarmeudbygning:</strong> arbejdet syd for Roskildevej ventes afsluttet i 2027 og nord for Roskildevej i 2028, mens Islev og områderne nord og syd for Jyllingevej udrulles i 2026–2032 efter interesse og teknisk mulighed.", ["rkf_faq", "rkf_om"]),
    ("<strong>Kampagnerabat:</strong> underskriver du en tilmeldingsaftale inden fristen i et udbygningsområde, føres stikledningen ind uden omkostning; efter fristen koster tilslutningen 31.250 kr. inkl. moms.", ["rkf_faq", "rkf_takst"]),
  ],
  "vp_faq": [
    ("Kan jeg få fjernvarme i Rødovre?", "Det afhænger af din adresse. Rødovre Kommunale Fjernvarmeforsyning har fem separate ledningsnet og udbygger frem mod 2032. Du skal selv tilmelde dig, når tilmeldingen åbner i dit område, og du kan godt tilmelde dig, selvom området først kobles på senere. Tilmelding kan påvirke rækkefølgen i udrulningen.", ["rkf_om", "rkf_faq"]),
    ("Må jeg få en varmepumpe i Rødovre?", "Ja. Der er generelt forbud mod elvarme i kommunen, men varmepumper er undtaget og kræver ikke byggetilladelse. Du skal overholde bygningsreglementet, undgå støjgener og følge eventuelle lokalplanbestemmelser om placering.", ["rod_varme"]),
  ],
}
CONTACTS["roedovre"] = {
  "sol": [("Rødovre Kommune, Byggesag og Erhverv", "36 37 70 00", "rod_sol")],
  "vp": [("Rødovre Kommunale Fjernvarmeforsyning, kundeservice", "36 37 72 50 · fjernvarme@rk.dk", "rkf_fors")],
}
# ---------- daglig by-rutine 27. nov. 2026: Ballerup (DK2, Ballerup Kommune, vp_page True) ----------
S.update({
 "bal_bygg": ("Ballerup Kommune: Spørgsmål & svar om byggeri – byggetilladelse og byggesagsgebyr (læst 27/11 2026)", "https://ballerup.dk/borger/bolig-vand-varme/byggeri/spoergsmaal-svar"),
 "bal_bev": ("Ballerup Kommune: Fredede & bevaringsværdige bygninger (læst 27/11 2026)", "https://ballerup.dk/borger/bolig-vand-varme/skal-du-bygge/fredede-bevaringsvaerdige-bygninger"),
 "bal_skov": ("Ballerup Kommune: Bevaring i Gl. Skovlunde – vejledning til Lokalplan 104 (udgivet januar 2009, læst 27/11 2026)", "https://ballerup.dk/sites/default/files/2021-06/bevaringsvejledning_for_skovlunde_landsby.pdf"),
 "bal_lp204": ("Ballerup Kommune: Lokalplan 204 for en del af boligbebyggelsen Bispevangen (januar 2025)", "https://ballerup.dk/sites/default/files/2025-01/LP%20204%20ENDELIG%20m.%20bilag%20-%2027jan25.pdf"),
 "bal_sol": ("Ballerup Kommune: Solceller – gratis beregningsværktøj og solcelle-hotline (læst 27/11 2026)", "https://ballerup.dk/borger/natur-klima-miljoe/klima/solceller"),
 "bal_tid": ("Ballerup Avis: Gennemsnitlig ventetid på byggetilladelse falder fra 82 til 75 dage (24/11 2026)", "https://ballerupavis.dk/article/gennemsnitlig-ventetid-paa-byggetilladelse-falder-fra-82-til-75-dage-64128"),
 "bal_fv": ("Ballerup Kommune: Fjernvarme – plan for udrulning i to etaper (læst 27/11 2026)", "https://ballerup.dk/fjernvarme"),
 "bal_vp": ("Ballerup Kommune: Varmeforsyning – plan, handlinger og anbefalinger (oplæg 30/5 2024)", "https://fugb.dk/Fil%20arkiv/Temam%C3%B8der/2024/Ball%20K%20Varmeforsyning%20opl%C3%A6g%20for%20FU%202024-05-30.pdf"),
 "vf_bal": ("Vestforbrænding: Fjernvarme i Ballerup – plan for udbygning (læst 27/11 2026)", "https://vestfor.dk/privat/fjernvarme/fjernvarme-ballerup-kommune"),
 "vf_pris": ("Vestforbrænding: Priser og gebyrer – takstblad (læst 27/11 2026)", "https://vestfor.dk/privat/har-fjernvarme/priser-og-gebyrer"),
 "vf_beregn": ("Vestforbrænding: Se din fjernvarmepris – model A og B (læst 27/11 2026)", "https://vestfor.dk/privat/fjernvarme/se-din-fjernvarmepris"),
 "vf_dekl": ("Vestforbrænding: Fjernvarmedeklaration 2025 – fjernvarme til eget net (rev. 18/6 2026, PDF)", "https://cms.vestfor.dk/media/zuvl5jy2/vestforbraending-fjernvarmedeklaration-eget-net-2025.pdf"),
 "vf_nyhed": ("Vestforbrænding: Ved Gershøj siger farvel til gas (24/2 2025)", "https://vestfor.dk/bliv-klogere/nyheder/nyhedsoverblik/farvel-til-gas"),
})
CITIES["ballerup"] = {
  "name": "Ballerup", "kommune": "Ballerup Kommune", "updated": ("27. november 2026", "2026-11-27"),
  "vp_page": True, "price_area": "DK2",
  "sol_intro": "Solceller i Ballerup: kommunen tager intet byggesagsgebyr, flere lokalplaner stiller krav til solceller, og over halvdelen af husene er fra 1960'erne og 70'erne. Her er reglerne, byggetal og vejen til tilbud.",
  "sol_facts": [
    ("Ballerup Kommune har <strong>afskaffet byggesagsgebyret</strong> for både private og virksomheder, så det koster ikke noget at søge byggetilladelse eller anmelde et byggeri.", ["bal_bygg"]),
    ("Kommunens oversigt over byggeri, der kræver byggetilladelse, nævner nye huse, tilbygninger, inddragelse af tagetage og småbygninger over 50 m². <strong>Solceller står ikke på listen</strong>, men tjek lokalplan, byplanvedtægt og tinglyste deklarationer for din adresse.", ["bal_bygg"]),
    ("I <strong>Gl. Skovlunde</strong> fastslår vejledningen til Lokalplan 104, at solfangere og solceller ikke må placeres på bevaringsværdige bygninger, og at anlæg skal placeres uden for syne fra sti, vej og fællesarealer. Vejledningen er fra 2009.", ["bal_skov"]),
    ("Gennemsnitlig sagsbehandlingstid for byggesager var <strong>75 dage i oktober 2026</strong> (82 i marts). Kommunen følger nu servicemålet på 40 dage for énfamiliehuse.", ["bal_tid"]),
    ("Kommunen tilbyder et <strong>gratis beregningsværktøj</strong> og en solcelle-hotline på 61 31 51 90 (mandag-torsdag kl. 15-17), hvor en uvildig rådgiver svarer på spørgsmål om solceller og batterier.", ["bal_sol"]),
  ],
  "sol_faq": [
    ("Skal man søge byggetilladelse til solceller i Ballerup?", "Kommunens liste over byggeri, der kræver byggetilladelse, nævner ikke solceller blandt eksemplerne. Er huset fredet eller bevaringsværdigt, henviser kommunen til at søge byggetilladelse via Bygogmiljø.dk. Kontakt Center for By og Miljø på 44 77 63 70, hvis du er i tvivl om din adresse.", ["bal_bygg", "bal_bev"]),
    ("Hvad koster en byggesag i Ballerup?", "Ingenting i gebyr. Kommunen har afskaffet byggesagsgebyret for private og virksomheder, så det er gratis at søge byggetilladelse eller anmelde byggeri.", ["bal_bygg"]),
    ("Hvor lang tid tager en byggesag i Ballerup?", "I oktober 2026 tog en sag i gennemsnit 75 dage, mod 82 dage i marts. Kommunen følger nu de fælles servicemål, herunder 40 dage for énfamiliehuse.", ["bal_tid"]),
  ],
  "vp_intro": "Varmepumpe i Ballerup: 63 % af parcel- og rækkehusene fyrer med naturgas, og kun 21 % har fjernvarme – men Vestforbrænding udruller fjernvarme i to etaper frem mod 2030, og kommunen peger på varmepumper i de områder, der ikke får fjernvarme. Her er status, priser og regler.",
  "vp_facts": [
    ("<strong>Kommunens plan:</strong> fjernvarme udrulles til områderne i varmeplanen, og individuelle varmepumper skal være i de områder, hvor Vestforbrænding ikke kan komme ud med fjernvarme. Kommunen har som mål at udfase naturgas og oliefyr.", ["bal_vp"]),
    ("<strong>To etaper:</strong> etape 1 giver ca. 3.300 kunder tilbud om fjernvarme frem til 2028, og etape 2 omfatter 12 energidistrikter med ca. 4.000 kunder; graveriet i etape 2 starter i andet halvår af 2026 og slutter i 2030.", ["vf_nyhed", "bal_fv"]),
    ("<strong>Områder uden fjernvarme:</strong> kommunen skriver, at der er enkelte områder, hvor der ikke er god samfundsøkonomi i fjernvarme. Her kan du overveje at udskifte olie- eller gasfyret med en individuel løsning, og kommunen har oplevet støjklager over varmepumper og anbefaler at undersøge kølemiddel og placering.", ["bal_fv", "bal_vp"]),
    ("<strong>Smørum Kraftvarmeværk:</strong> Bjørnekær, Smørumvej og Baneskrænten tilbydes fjernvarme fra Smørum Kraftvarmeværk senest i 2030.", ["bal_fv"]),
  ],
  "vp_faq": [
    ("Kan jeg få fjernvarme i Ballerup?", "Se på Vestforbrændings adressekort, om dit energidistrikt er med i etape 1 eller etape 2. Etape 1 løber til 2028 (Skovlunde 2026-2027), etape 2 fra 2026 til 2030. Er du i et område uden udbygningsplan, kan du overveje en individuel løsning.", ["vf_bal", "bal_fv"]),
    ("Anbefaler Ballerup Kommune varmepumper?", "Kommunens anbefaling er fjernvarme, hvor Vestforbrænding kommer. Varmepumper hører til i områder uden fjernvarme, og kommunen råder til at undersøge kølemiddel og placere varmepumpen, så naboer ikke generes af støj.", ["bal_vp", "bal_fv"]),
  ],
}
CONTACTS["ballerup"] = {
  "sol": [("Ballerup Kommune, Center for By og Miljø", "44 77 63 70 · byggesag@balk.dk", "bal_bev")],
  "vp": [("Vestforbrænding, fjernvarme", "70 25 70 60", "bal_fv")],
}
