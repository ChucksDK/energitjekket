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
  "vp_intro": "Luft til vand-varmepumpe i Horsens: fjernvarmen er vokset voldsomt i Horsens de seneste ti år, så start med at tjekke, om din adresse er dækket. Ligger du udenfor, er her priser, tilskud og tilbud.",
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
  "name": "Silkeborg", "kommune": "Silkeborg Kommune", "updated": ("27. oktober 2026", "2026-10-27"),
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
  "vp_intro": "Luft til vand-varmepumpe i Silkeborg: Silkeborg Forsyning lægger fjernvarme ud i en række byer uden for Silkeborg, bl.a. Virklund, Sejs-Svejbæk, Them, Salten og Voel. Bor du dér, skal du nok ikke have varmepumpe. Bor du uden for projekterne, er den et oplagt valg. Her er status og tallene.",
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
  "name": "Slagelse", "kommune": "Slagelse Kommune", "updated": ("28. oktober 2026", "2026-10-28"),
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
  "vp_intro": "Luft til vand-varmepumpe i Slagelse: fjernvarmen bliver udbygget i Slagelse by, men i Skælskør, Vemmelev, Forlev og Sørbymagle er fjernvarmeprojekterne droppet. Dér skal husene have en individuel løsning, fx en varmepumpe. Her er status, priserne og tilskudsreglerne.",
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
