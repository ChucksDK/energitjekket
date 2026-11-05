# -*- coding: utf-8 -*-
"""Undersider: lokale guides (regler for solceller, fjernvarme eller varmepumpe) og nationale emnesider.
Hver side har ét søgeord (kw) og dokumentation (evidence) fra Google autocomplete / PAA / relaterede søgninger 23/10 2026.
Blokke: ("p", tekst, kilder) | ("ul", [(tekst, kilder)]) | ("table", [kolonner], [rækker], kilder) | ("note"|"example", tekst, kilder)
"""
FV_AVG = "16.953"
# Forsyningstilsynet, standardhus 130 m², 18,1 MWh, inkl. moms, pr. 31/1 2026: (værk, postnr, årspris, kr/MWh)
FV_PRICES = {
 "kolding": [("TREFOR Varme, Kolding", "6000", "17.496", "811"), ("Christiansfeld Fjernvarmeselskab", "6070", "16.791", "668"), ("Vamdrup Fjernvarme", "6580", "16.066", "662")],
 "vejle":   [("Vejle Fjernvarme", "7100", "14.911", "618"), ("Jelling Varmeværk", "7300", "15.366", "590"), ("Give Fjernvarme", "7323", "20.800", "730"), ("Egtved Varmeværk", "6040", "22.010", "975")],
 "esbjerg": [("DIN Forsyning Varme", "6715", "18.249", "817"), ("Ribe Fjernvarme", "6760", "15.327", "627"), ("Bramming Fjernvarme", "6740", "16.232", "662"), ("Gørding Varmeværk", "6690", "15.323", "612"), ("Hunderup-Sejstrup Fællesvarme", "6740", "30.459", "892")],
 "odense":  [("Fjernvarme Fyn Distribution", "5000", "15.076", "710")],
 "aalborg": [("Aalborg Varme", "9000", "20.348", "956"), ("Nibe Varmeværk", "9240", "14.388", "568"), ("Kongerslev Fjernvarme", "9293", "16.428", "662"), ("Sønderholm Varmeværk", "9240", "18.276", "643")],
 "randers": [("Verdo Varme", "8920", "14.541", "703"), ("Langå Varmeværk", "8870", "18.995", "705"), ("Havndal Fjernvarme", "8970", "17.911", "579"), ("Mellerup Fjernvarme", "8930", "23.766", "913")],
 "horsens": [("Fjernvarme Horsens", "8700", "13.254", "685"), ("Brædstrup Fjernvarme", "8740", "9.855", "300"), ("Østbirk Varmeværk", "8752", "14.643", "437"), ("Hovedgård Fjernvarme", "8732", "16.446", "587")],
 # 26/10 2026: Kredsløb + de 6 mindre værker i Varmeplan Aarhus (aar_mr); Viborg: værker fra kommunens liste over 14 selskaber (vib_strat)
 "aarhus":  [("Kredsløb Fjernvarme", "8220", "16.229", "667"), ("Lystrup Fjernvarme", "8520", "18.751", "825"), ("Løgten-Skødstrup Fjernvarmeværk", "8541", "17.097", "787"), ("Malling Varmeværk", "8340", "17.297", "745"), ("Tranbjerg Varmeværk", "8310", "19.549", "921"), ("Holme-Lundshøj Fjernvarmeværk", "8270", "19.338", "913"), ("Rundhøj Fjernvarme", "8270", "17.028", "761")],
 "viborg":  [("Viborg Varme", "8800", "18.854", "791"), ("Gudenådalens Energiselskab (Bjerringbro)", "8850", "22.102", "700"), ("Stoholm Fjernvarmeværk", "7850", "16.190", "656"), ("Karup Varmeværk", "7470", "13.410", "475"), ("Løgstrup Varmeværk", "8831", "14.668", "437"), ("Ørum Varmeværk", "8830", "14.837", "625"), ("Hammershøj Fjernvarmeværk", "8830", "22.565", "1.031")],
}
FV_COMPARE_ROWS = [
 ("Luft til vand-varmepumpe med gulvvarme", "7.288 kr.", "18.463 kr."),
 ("Luft til vand-varmepumpe med radiatorer", "9.386 kr.", "20.561 kr."),
 ("Fjernvarme (landsgennemsnit)", "16.953 kr.", "20.050 kr."),
 ("Gasfyr", "18.433 kr.", "23.743 kr."),
 ("Oliefyr", "32.388 kr.", "38.153 kr."),
]
SOL_REG = {}
FV_PAGE = {}
NATIONAL = {}

SOL_REG["kolding"] = {
  "kw": "solceller kolding kommune",
  "evidence": "Autocomplete: 'solceller kolding' → 'solceller kolding kommune'; 'kolding kommune solceller'. PAA på 'solceller kolding kommune': 'Skal jeg søge byggetilladelse til solceller?'. Top-resultat er kolding.dk.",
  "intro": "Kolding Kommune lader som regel parcel-, række- og sommerhusejere sætte solceller op på taget uden tilladelse, men der er seks situationer, hvor du skal henvende dig først. Kommunen giver desuden gratis adgang til et uvildigt solcelletjek frem til september 2027.",
  "sections": [
   ("Hvornår skal du kontakte Kolding Kommune?", [
     ("p", "Kommunen skriver, at solceller og solfangere på den eksisterende tagflade af enfamiliehuse, sommerhuse og rækkehuse <strong>ofte kan sættes op uden tilladelse</strong>. Du skal dog henvende dig, og eventuelt søge tilladelse, hvis ét af disse punkter gælder:", ["kol_sol"]),
     ("ul", [("Ejendommen er omfattet af en lokalplan, byplanvedtægt eller tinglyst deklaration med regler om solceller, tagmaterialer eller refleksioner.", ["kol_sol"]),
             ("Bygningen er bevaringsværdig eller fredet, eller ejendommen ligger inden for bygge- og naturbeskyttelseslinjer.", ["kol_sol"]),
             ("Panelerne skal sidde på stativer eller beslag, der vinkler dem væk fra tagfladen.", ["kol_sol"]),
             ("Anlægget skal stå på stativer på jorden.", ["kol_sol"]),
             ("Anlægget overholder ikke bygningsreglementets højde- og afstandskrav. Ved et parcelhus er kravet bl.a. mindst 2,5 m til skel mod nabo, sti og vej.", ["kol_sol", "br18_179"]),
             ("Anlægget skal på andre bygninger end boliger og tilhørende garager og udhuse, fx driftsbygninger på en landbrugsejendom. Så skal der altid søges byggetilladelse, og der kræves også miljøscreening.", ["kol_sol"])]),
   ]),
   ("Landzone omkring Kolding", [
     ("p", "Bor du i landzone, fx uden for Christiansfeld, Vamdrup eller Lunderskov, gælder de samme punkter. Kræver anlægget byggetilladelse, skal du <strong>også have landzonetilladelse</strong> efter planlovens § 35. Anlægget skal som hovedregel stå i tilknytning til eksisterende bebyggelse, og byggesagen behandles først, når landzonetilladelsen er givet, og offentlighedsfasen er udløbet.", ["kol_sol"]),
   ]),
   ("Sådan gør du i praksis", [
     ("ul", [("<strong>Regn først:</strong> Kolding Kommune samarbejder med SolarSim og giver alle borgere gratis adgang til et uvildigt solcelletjek frem til <strong>15. september 2027</strong>. Værktøjet regner på tagets hældning, skygge, dit elforbrug og elpriser.", ["kol_sol"]),
             ("<strong>Tjek planerne:</strong> Slå ejendommen op i lokalplan, byplanvedtægt og kommuneplanramme, før du indhenter tilbud.", ["kol_sol"]),
             ("<strong>Kræver det tilladelse:</strong> Søg via Byg & Miljø med en projektbeskrivelse, en tegning af placering og størrelse og ansøgningsskemaet.", ["kol_sol"]),
             ("<strong>Kræver det ikke tilladelse:</strong> Send anlæggets areal og ydelse til byggesag@kolding.dk, når det er sat op, så det kan komme i BBR.", ["kol_sol"]),
             ("<strong>Taget:</strong> Kommunen gør opmærksom på, at ikke alle tagkonstruktioner kan bære anlæggene, og anbefaler en vurdering af en bygningssagkyndig. Anlægget må heller ikke give generende reflekser.", ["kol_sol"])]),
   ]),
  ],
  "faq": [
   ("Skal jeg søge byggetilladelse til solceller på mit hus i Kolding?", "Som regel ikke, når panelerne ligger på den eksisterende tagflade af et enfamiliehus, rækkehus eller sommerhus. Du skal henvende dig til kommunen ved lokalplan- eller deklarationskrav, bevaringsværdi, stativer, anlæg på jorden eller hvis bygningsreglementets højde- og afstandskrav ikke overholdes.", ["kol_sol"]),
   ("Hvad er SolarSim i Kolding?", "Et uvildigt digitalt solcelletjek, som Kolding Kommune giver alle borgere gratis adgang til frem til 15. september 2027. Det beregner potentialet for dit tag ud fra hældning, skygge, elforbrug og elpriser.", ["kol_sol"]),
   ("Hvem kontakter jeg i Kolding Kommune om solceller?", "Byggesag på 79 79 60 40 eller byggesag@kolding.dk, Nytorv 11, 6000 Kolding.", ["kol_sol"]),
   ("Gælder reglerne også for solceller på en landbrugsejendom?", "Ikke for driftsbygninger. Kommunen skriver, at anlæg på fx driftsbygninger altid kræver byggetilladelse og miljøscreening, og i landzone også landzonetilladelse.", ["kol_sol"]),
  ],
}
SOL_REG["vejle"] = {
  "kw": "solceller vejle kommune",
  "evidence": "Autocomplete: 'solceller vejle' → 'solceller vejle kommune'; 'vejle kommune solceller'; 'solcelleanlæg vejle'.",
  "intro": "Vejle Kommunes egne retningslinjer for solenergi handler mest om store solcelleparker. For dit parcelhus gælder de nationale regler, men kommunen tilbyder en gratis forhåndsdialog, hvis du er i tvivl. Her er, hvad du skal vide.",
  "sections": [
   ("Solceller på taget af et parcelhus i Vejle", [
     ("p", "Vejle Kommune har ikke en særskilt side om solceller på parcelhustage, så de generelle regler gælder. Kommunen skal godkende placeringen, hvis lokalplaner, fredninger eller servitutter regulerer den, og anlæg på jorden skal altid godkendes.", ["se_sol", "vej_sol"]),
     ("p", "Bygningsreglementet kræver, at solcelleanlæg ved fritliggende enfamiliehuse, tofamiliehuse, dobbelthuse og rækkehuse holder <strong>mindst 2,5 m til skel</strong> mod nabo, sti og vej. Ved sommerhuse er kravet 5 m.", ["br18_179"]),
     ("p", "Tjek derfor lokalplanen for dit område først. Vejle Kommunes byggeside henviser til de gældende lokalplaner og kommuneplanen.", ["vej_byg"]),
   ]),
   ("Gratis forhåndsdialog og gebyrer i 2026", [
     ("ul", [("Vejle Kommune tilbyder en <strong>gratis forhåndsdialog på 30 minutter</strong> med en byggesagsbehandler. Her får du at vide, hvilke krav og tilladelser der gælder for dit projekt.", ["vej_byg"]),
             ("Kræver dit anlæg byggetilladelse, betaler du for sagsbehandlingen efter tid: <strong>826 kr. pr. time</strong> fra 1. januar 2026. Enkle konstruktioner har en fast pris på 1.230 kr.", ["vej_byg"]),
             ("Alle ansøgninger skal sendes via Byg & Miljø. BBR opdateres automatisk, når sagen afsluttes.", ["vej_byg"])]),
   ]),
   ("Solceller på jorden og i landzone", [
     ("p", "Et mindre solcelleanlæg i landzonen kræver landzonetilladelse efter planlovens § 35 og kan efter almindelig praksis kun tillades i tilknytning til eksisterende bebyggelse. Store anlæg, der producerer mere end til eget forbrug, er som udgangspunkt lokalplanpligtige. Skillelinjen er typisk 1 ha.", ["vej_sol"]),
     ("p", "Til store anlæg stiller kommunen bl.a. krav om højst 4 m høje paneler. Det er ikke et krav til dit tag, men det viser, hvad kommunen lægger vægt på.", ["vej_sol"]),
   ]),
  ],
  "faq": [
   ("Kræver solceller på mit hus i Vejle byggetilladelse?", "Typisk ikke, hvis de ligger på taget og overholder bygningsreglementet og lokalplanen. Er du i tvivl, kan du bruge Vejle Kommunes gratis forhåndsdialog på 30 minutter.", ["vej_byg", "se_sol"]),
   ("Hvad koster en byggetilladelse til solceller i Vejle?", "Vejle Kommune afregner byggesager efter tid med 826 kr. pr. time fra 1. januar 2026. Enkle konstruktioner har en fast pris på 1.230 kr., og forhåndsdialogen på 30 minutter er gratis.", ["vej_byg"]),
   ("Må jeg sætte solceller op på jorden ved mit hus i landzone?", "Kun med landzonetilladelse, og normalt kun i tilknytning til eksisterende bebyggelse.", ["vej_sol"]),
   ("Hvor tæt på skel må solceller sidde?", "Ved parcel-, række- og dobbelthuse mindst 2,5 m fra skel mod nabo, sti og vej. Ved sommerhuse 5 m.", ["br18_179"]),
  ],
}
SOL_REG["esbjerg"] = {
  "kw": "solceller esbjerg kommune",
  "evidence": "Autocomplete: 'solceller esbjerg' → 'solceller esbjerg kommune'; 'solcelleanlæg esbjerg kommune'; 'esbjerg kommune solceller'.",
  "intro": "Esbjerg Kommune har nogle af de mest konkrete regler i landet for, hvordan et solcelleanlæg skal se ud på taget. De står i kommuneplanens retningslinjer for vedvarende energi. Her er de oversat til almindeligt dansk.",
  "sections": [
   ("Sådan skal anlægget se ud på taget", [
     ("ul", [("Anlægget skal samles i <strong>én rektangulær eller kvadratisk form</strong> og følge tagets hældning.", ["esb_sol"]),
             ("På flade tage skal det skjules bag murkronen.", ["esb_sol"]),
             ("På <strong>tegl- og skifertage</strong> bør to rækker tagsten ved top og bund og tre rækker langs siderne holdes fri. På andre tage bør der være mindst 50 cm til top, bund og sider.", ["esb_sol"]),
             ("Stråtage, kviste og valme skal holdes fri.", ["esb_sol"])]),
   ]),
   ("Bevaringsværdige huse og kulturmiljøer", [
     ("p", "Bygninger med <strong>SAVE 1-3</strong> inden for et udpeget kulturmiljø kan som udgangspunkt ikke få solceller. Det samme gælder ejendomme med en bevarende lokalplan.", ["esb_sol"]),
     ("p", "Det er særligt relevant i Ribe og andre ældre bymiljøer i kommunen. Tjek din bygnings SAVE-værdi, før du beder om tilbud.", ["esb_sol"]),
   ]),
   ("Genskin og lufthavnen", [
     ("p", "Kommunen kræver antirefleksbehandling, hvor der er risiko for genskin for naboer og trafikanter. Det kan også være relevant tæt på <strong>Esbjerg Lufthavn</strong>.", ["esb_sol"]),
   ]),
   ("Solceller på jorden", [
     ("p", "Små anlæg på terræn under 1 ha kræver ofte landzonetilladelse, mens anlæg over 1 ha kræver lokalplan. Esbjerg Kommune foretrækker generelt, at anlæg placeres på tage frem for på jorden. Kommunens eneste kollektive solvarmeanlæg ligger ved Gørding Varmeværk.", ["esb_sol"]),
   ]),
  ],
  "faq": [
   ("Hvor meget af taget skal holdes fri for solceller i Esbjerg?", "På tegl og skifer to rækker sten ved top og bund og tre rækker langs siderne. På andre tage mindst 50 cm til top, bund og sider.", ["esb_sol"]),
   ("Må jeg få solceller på stråtag i Esbjerg Kommune?", "Nej. Kommuneplanen siger, at stråtage, kviste og valme skal holdes fri.", ["esb_sol"]),
   ("Kan jeg få solceller på et bevaringsværdigt hus i Ribe?", "Er huset SAVE 1-3 i et udpeget kulturmiljø, eller er der en bevarende lokalplan, kan der som udgangspunkt ikke gives tilladelse.", ["esb_sol"]),
   ("Hvem kontakter jeg i Esbjerg Kommune?", "Teknik & Miljø på 76 16 16 16, Torvegade 74. Åbent mandag-onsdag kl. 10-15, torsdag kl. 10-17 og fredag kl. 10-12.30.", ["esb_sol"]),
  ],
}

SOL_REG["odense"] = {
  "kw": "solceller odense kommune",
  "evidence": "Autocomplete: 'solceller odense' → 'solceller odense kommune' (første forslag); 'odense kommune solceller'; 'solcelleanlæg odense'.",
  "intro": "Odense Kommune har en af de klareste tommelfingerregler: ligger solcellerne plant på taget af et enfamilie- eller rækkehus uden stativ, skal du ikke søge byggetilladelse. Men der er tre spørgsmål, du skal kunne svare nej til først.",
  "sections": [
   ("De tre spørgsmål, du skal svare nej til", [
     ("ul", [("Er din ejendom omfattet af en lokalplan eller byplanvedtægt, der siger noget om solceller eller tagets udseende?", ["ode_sol"]),
             ("Er der en tinglyst servitut, der siger noget om solceller eller tagets udseende?", ["ode_sol"]),
             ("Er din ejendom udpeget som bevaringsværdig i kategori 4 eller lavere?", ["ode_sol"])]),
     ("p", "Svarer du ja til ét af dem, skal du søge byggetilladelse eller dispensation. Odense Kommunes undtagelse gælder kun solceller, der ligger <strong>plant på taget uden stativ</strong>.", ["ode_sol"]),
   ]),
   ("Naboer og genskin", [
     ("p", "Kommunen anbefaler, at du orienterer de naboer, der kan blive generet af genskin. Overvej derfor placeringen og antirefleksbehandlede paneler, hvis taget vender ud mod naboernes vinduer.", ["ode_sol"]),
   ]),
   ("BBR, afstand til skel og kontakt", [
     ("ul", [("Anlægget skal registreres i BBR.", ["ode_sol"]),
             ("Bygningsreglementets afstandskrav gælder altid: mindst 2,5 m til skel ved parcel-, række- og dobbelthuse.", ["br18_179"]),
             ("Byggesag har telefontid mandag-torsdag kl. 10-12 på 65 51 24 62. Brug Digital Post til personfølsomme oplysninger. Personligt fremmøde sker efter aftale.", ["ode_sol"])]),
   ]),
  ],
  "faq": [
   ("Skal jeg søge byggetilladelse til solceller i Odense?", "Ikke hvis du bor i enfamilie- eller rækkehus, panelerne ligger plant på taget uden stativ, og hverken lokalplan, byplanvedtægt, servitut eller bevaringsværdi (kategori 4 eller lavere) regulerer det.", ["ode_sol"]),
   ("Må jeg bruge stativ på et fladt tag i Odense?", "Undtagelsen gælder kun paneler, der ligger plant uden stativ. Med stativ bør du kontakte Byggesag, før du går i gang.", ["ode_sol"]),
   ("Skal jeg fortælle naboerne, at jeg får solceller?", "Odense Kommune anbefaler, at du orienterer de naboer, der kan blive generet af genskin.", ["ode_sol"]),
   ("Hvornår kan jeg ringe til Odense Kommune om solceller?", "Byggesag har telefontid mandag-torsdag kl. 10-12 på 65 51 24 62.", ["ode_sol"]),
  ],
}
SOL_REG["aalborg"] = {
  "kw": "solceller aalborg kommune",
  "evidence": "Autocomplete: 'solceller aalborg' → 'solceller aalborg kommune'; 'aalborg kommune solceller'; 'solcelleanlæg aalborg'.",
  "intro": "Aalborg Kommune har ikke en særskilt side om solceller på parcelhuse. Til gengæld har kommunen en hurtig STRAKS-ansøgning, hvis dit anlæg kræver tilladelse, og klare regler for anlæg på jorden. Her er overblikket.",
  "sections": [
   ("Start med lokalplanen", [
     ("p", "Aalborg Kommune beder dig først finde ud af, hvad der gælder på din ejendom: lokalplan eller byplanvedtægt, ellers kommuneplanen og bygningsreglementet. Du skal også tjekke tinglyste servitutter.", ["aal_byg"]),
     ("p", "Kommunen understreger, at alt byggeri skal overholde bygningsreglementet, lokalplanen og servitutterne, også når det ikke kræver tilladelse. For solceller ved et parcelhus betyder bygningsreglementet bl.a. mindst 2,5 m til skel.", ["aal_byg", "br18_179"]),
   ]),
   ("Når det kræver tilladelse: STRAKS-ansøgning og dispensation", [
     ("ul", [("Med en <strong>STRAKS-ansøgning</strong> for enfamiliehuse og sommerhuse giver kommunen tilladelse <strong>senest 3 uger</strong> efter, at sagen er oprettet, hvis ansøgningen er fyldestgørende og lovlig.", ["aal_byg"]),
             ("Skal du afvige fra lokalplanen, skal du søge dispensation. Det kan kræve, at kommunen hører naboerne først, så det tager længere tid.", ["aal_byg"]),
             ("Du har selv ansvaret for, at BBR har de rigtige oplysninger om din ejendom.", ["aal_byg"])]),
   ]),
   ("Solceller på jorden og nye energiparker", [
     ("p", "Solenergianlæg <strong>under 2 hektar</strong> behandles som landzonesager. Anlæg over 2 hektar kræver kommuneplantillæg, lokalplan og miljøvurdering.", ["aal_ve"]),
     ("p", "Stae og Nørrekær Enge er udpeget som statslige energiparker ved bekendtgørelse af 7. juli 2026. For Storvorde og Gåser har der været høring fra 29. september 2026 i 8 uger. Bor du i nærheden, kan der komme store anlæg i dit område.", ["aal_ve"]),
   ]),
  ],
  "faq": [
   ("Hvor hurtigt kan jeg få tilladelse til solceller i Aalborg?", "Med en fyldestgørende STRAKS-ansøgning giver Aalborg Kommune tilladelse senest 3 uger efter, at sagen er oprettet.", ["aal_byg"]),
   ("Kræver solceller på jorden tilladelse i Aalborg Kommune?", "Ja. Anlæg under 2 hektar behandles som landzonesager, og anlæg over 2 hektar kræver lokalplan og miljøvurdering.", ["aal_ve"]),
   ("Hvor kan jeg ringe til Aalborg Kommune om byggeri?", "Byggeri på 99 82 82 00, mandag-fredag kl. 10-14. Adressen er Stigsborg Brygge 105, 9400 Nørresundby.", ["aal_byg"]),
   ("Kommer der solcelleparker ved Storvorde?", "Storvorde og Gåser er foreslået som statslige energiparker, og forslaget har været i høring fra 29. september 2026 i 8 uger.", ["aal_ve"]),
  ],
}
SOL_REG["randers"] = {
  "kw": "solceller randers kommune",
  "evidence": "Autocomplete: 'solceller randers' → 'solceller randers kommune'; 'randers kommune solceller'.",
  "intro": "Randers Kommune skriver, at solceller stort set altid kræver byggetilladelse. I praksis er de fleste anlæg på parcelhuse undtaget, men kun hvis du kender de præcise grænser. Her er de.",
  "sections": [
   ("Hvornår kræver solceller byggetilladelse i Randers?", [
     ("ul", [("Anlægget kommer <strong>tættere på skel end 2,50 m</strong>.", ["ran_sol"]),
             ("Anlægget står på terræn og er højere end 1,80 m og/eller større end 35 m².", ["ran_sol"]),
             ("Anlægget sidder på erhvervsbygninger o.l., og lasten øges mere end 5 %.", ["ran_sol"]),
             ("Anlægget sidder på et parcelhus, dobbelthus, rækkehus, sommerhus eller en sekundær bygning, og byggeretten i bygningsreglementets kapitel 8 overskrides.", ["ran_sol"])]),
     ("p", "Omvendt kræver anlæg på parcelhuse <strong>ikke</strong> byggetilladelse, når byggeretten i kapitel 8 overholdes, og terrænanlæg under 1,80 m og 35 m² er også undtaget.", ["ran_sol"]),
   ]),
   ("Lokalplaner: fire bestemmelser du skal kigge efter", [
     ("ul", [("Forbud mod blanke og reflekterende overflader.", ["ran_sol"]), ("Krav om bestemte tagmaterialer, fx tegl eller skifer.", ["ran_sol"]),
             ("Særlige bevaringsbestemmelser.", ["ran_sol"]), ("Krav om, at anlægget skal bygges ind i taget.", ["ran_sol"])]),
     ("p", "Kan du ikke overholde lokalplanen, skal du søge dispensation. Det tager længere tid, fordi naboerne kan blive orienteret først.", ["ran_sol"]),
   ]),
   ("Ansøgning, fredede huse og natur", [
     ("ul", [("En ansøgning skal mindst indeholde en kort beskrivelse af anlæggets størrelse, effekt og antal celler, en tegning af placeringen og en fuldmagt, hvis du ikke selv ejer huset.", ["ran_sol"]),
             ("På <strong>fredede bygninger</strong> tillades solceller ikke. På bygninger med bevaringsværdi 1-3 i kulturmiljøer gives der som udgangspunkt ikke tilladelse. Andre huse med bevaringsværdi 1-3 vurderes konkret. Spørgsmål sendes til plan@randers.dk.", ["ran_sol"]),
             ("Nær beskyttet natur kan det kræve dispensation. Spørgsmål sendes til naturbeskyttelse@randers.dk. I fredskov afgør Styrelsen for Grøn Arealomlægning og Vandmiljø sagen.", ["ran_sol"]),
             ("Randers Kommune har telefon 89 15 15 15, Laksetorvet 1.", ["ran_sol"])]),
   ]),
  ],
  "faq": [
   ("Kræver solceller byggetilladelse i Randers?", "Kommunen skriver, at det stort set altid gør. Anlæg på parcel-, række- og dobbelthuse er dog undtaget, når byggeretten i BR18 kapitel 8 overholdes, og anlægget holder mindst 2,50 m til skel.", ["ran_sol"]),
   ("Hvor stort må et solcelleanlæg på jorden være uden tilladelse i Randers?", "Under 1,80 m højt og under 35 m². Er det højere eller større, kræver det byggetilladelse.", ["ran_sol"]),
   ("Kan jeg få solceller på et fredet hus i Randers Kommune?", "Nej. Randers Kommune tillader ikke solceller på fredede bygninger. Ved bevaringsværdi 1-3 i kulturmiljøer gives der som udgangspunkt heller ikke tilladelse.", ["ran_sol"]),
   ("Hvad skal en ansøgning om solceller i Randers indeholde?", "En kort beskrivelse af størrelse, effekt og antal celler, en tegning af placeringen og en fuldmagt, hvis du ikke selv ejer huset.", ["ran_sol"]),
  ],
}
SOL_REG["horsens"] = {
  "kw": "solceller horsens kommune",
  "evidence": "Autocomplete: 'solceller horsens' → 'solceller horsens kommune'; 'horsens kommune solceller'. PAA på 'solceller horsens kommune': 'Kan det betale sig at få solceller i 2026?', 'Hvad koster solceller inkl. montering?'.",
  "intro": "Horsens Kommune giver gratis adgang til et uvildigt beregningsværktøj frem til februar 2027 og forklarer reglerne mere teknisk end de fleste kommuner. Her får du begge dele samlet.",
  "sections": [
   ("Gratis beregning med SolarSim til 15. februar 2027", [
     ("p", "Horsens Kommune giver gratis adgang til SolarSim frem til <strong>15. februar 2027</strong>. Det tager under 5 minutter i fire trin: indtast adresse, oplys elforbrug, tegn tagfladerne, og få anlægsstørrelse, pris, tilbagebetalingstid og en vurdering af, om et batteri kan betale sig.", ["hor_sol"]),
     ("p", "Værktøjet spørger ikke efter kontaktoplysninger. Brug resultatet som pejlemærke, når du sammenligner tilbud.", ["hor_sol"]),
   ]),
   ("Hvornår kræver solceller byggetilladelse?", [
     ("ul", [("Hvis anlægget <strong>øger lasten på taget med mere end 5 %</strong> (BR18 § 5, pkt. 4).", ["hor_sol"]),
             ("På andre bygningstyper kræver det ikke tilladelse, hvis anlægget holdes inden for tagets vandrette udbredelse, og den samlede højde ikke overstiger 8,5 m (BR18 § 176).", ["hor_sol"]),
             ("På flade tage kræver anlæg, der står <strong>mere end 1 m over tagfladen</strong>, tilladelse.", ["hor_sol"])]),
     ("note", "For parcel-, række-, dobbelt- og sommerhuse gælder byggeretten i bygningsreglementets kapitel 8, bl.a. mindst 2,5 m til skel.", ["br18_179"]),
   ]),
   ("Bevaringsværdi, fredning og BBR", [
     ("ul", [("Er ejendommen optaget i kommuneplanen med <strong>bevaringsværdi 1-4</strong>, kan du ikke forvente tilladelse.", ["hor_sol"]),
             ("Ændringer på fredede bygninger skal godkendes af Slots- og Kulturstyrelsen.", ["hor_sol"]),
             ("Du skal altid anmelde anlægget til BBR med adresse, areal og samlet effekt i kW. Ansøgninger sendes via Byg og Miljø.", ["hor_sol"]),
             ("Har du et stort tag på over 250 m², nævner kommunen en screening af store tage via Klimapartnerskabet. På sologvind.dk kan du se kortlag med solindstråling.", ["hor_sol"])]),
   ]),
  ],
  "faq": [
   ("Er SolarSim gratis i Horsens?", "Ja. Horsens Kommune giver gratis adgang frem til 15. februar 2027, og værktøjet beder ikke om kontaktoplysninger.", ["hor_sol"]),
   ("Må solceller stå mere end 1 m over et fladt tag?", "Ifølge Horsens Kommune kræver anlæg mere end 1 m over tagfladen byggetilladelse.", ["hor_sol"]),
   ("Kan jeg få solceller på et bevaringsværdigt hus i Horsens?", "Har ejendommen bevaringsværdi 1-4 i kommuneplanen, kan du ifølge kommunen ikke forvente tilladelse.", ["hor_sol"]),
   ("Hvornår har Horsens Kommune telefontid?", "Mandag-onsdag kl. 9-15, torsdag kl. 9-17 og fredag kl. 9-13 på 76 29 29 29.", ["hor_sol"]),
  ],
}

FV_PAGE["kolding"] = {
  "kw": "fjernvarme kolding / varmepumpe eller fjernvarme",
  "evidence": "Autocomplete 'fjernvarme kolding': 10 forslag (bl.a. 'fjernvarme kolding pris', 'fjernvarme kolding kommune', 'trefor fjernvarme kolding'). 'fjernvarme christiansfeld' → 'christiansfeld fjernvarme pris'; 'fjernvarme vamdrup' → 'vamdrup fjernvarme priser'. National: 'fjernvarme eller varmepumpe' (PAA: 'Hvad kan bedst betale sig, fjernvarme eller varmepumpe?').",
  "intro": "I Kolding by leverer TREFOR Varme fjernvarmen, og Christiansfeld og Vamdrup har egne værker. Uden for nettet er en varmepumpe typisk løsningen. Her er de lokale priser, status for udbygningen og reglerne for, hvornår du må vælge en varmepumpe.",
  "status": [
   ("Kolding Kommunes kort viser, om din ejendom ligger i et fjernvarme- eller naturgasområde, har <strong>tilslutningspligt</strong> eller er omfattet af forbud mod elvarme.", ["kol_fv"]),
   ("Forbuddet mod elvarme gælder elvarme som primær opvarmning i fjernvarmeområder. Kommunen oplyser, at der er undtagelser og mulighed for dispensation, bl.a. for eldrevne varmepumper.", ["kol_fv"]),
   ("Tilslutningspligt betyder, at du skal betale tilslutningsafgift og en årlig afgift, men ikke at du skal aftage varmen. I nye områder pålægges der ikke længere tilslutningspligt.", ["kol_fv"]),
   ("I <strong>Christiansfeld</strong> er udvidelsen af fjernvarmen til naturgaskunderne opgivet, fordi der ved fristen i december 2025 var langt fra nok bindende tilsagn.", ["kol_chr"]),
  ],
  "local_take": "TREFOR Varme i Kolding ligger lidt over landsgennemsnittet for et standardhus, mens Christiansfeld og Vamdrup ligger lidt under. Har du gasfyr i Christiansfeld, er en varmepumpe det realistiske alternativ, nu hvor udvidelsen er opgivet.",
  "contact": ("Kolding Kommune, Team Energi", "79 79 79 79 · energi@kolding.dk", "kol_fv"),
  "faq": [
   ("Hvad koster fjernvarme i Kolding?", "Ifølge Forsyningstilsynets prisstatistik pr. 31. januar 2026 koster det 17.496 kr. om året inkl. moms for et standardhus på 130 m² hos TREFOR Varme, Kolding. Landsgennemsnittet er 16.953 kr.", ["ft_pris", "wg_pris"]),
   ("Kommer der fjernvarme til gaskunderne i Christiansfeld?", "Nej, ikke foreløbig. Udvidelsen blev opgivet, fordi der ved fristen i december 2025 var langt fra nok bindende tilsagn.", ["kol_chr"]),
   ("Må jeg få varmepumpe i et område med forbud mod elvarme i Kolding?", "Kolding Kommune oplyser, at der er undtagelser og mulighed for dispensation, bl.a. for eldrevne varmepumper. Kontakt Team Energi, før du bestiller.", ["kol_fv"]),
  ],
}
FV_PAGE["vejle"] = {
  "kw": "fjernvarme vejle / varmepumpe eller fjernvarme vejle",
  "evidence": "Autocomplete 'fjernvarme vejle': 10 forslag (bl.a. 'fjernvarme vejle kommune', 'fjernvarme vejle pris', 'vejle fjernvarme priser'). 'fjernvarme give' → 'give fjernvarme priser'; 'fjernvarme jelling' → 'jelling fjernvarme priser'; 'fjernvarme egtved'. 'luft til vand varmepumpe vejle' findes også som forslag.",
  "intro": "Vejle Kommune er midt i en stor udrulning af fjernvarme med frist i 2028, og kommunen beder dig selv overveje at vente, hvis dit område er på kortet. Her er status, de lokale priser og hvornår en varmepumpe alligevel er det rigtige valg.",
  "status": [
   ("Kommunens fjernvarmekort har tre farver: <strong>gul</strong> = fjernvarme i dag, <strong>blå</strong> = udrulning i gang eller forventet ved nok tilmeldte, <strong>grøn</strong> = potentiale, der regnes på.", ["vej_fv"]),
   ("Kommunen har skrevet til alle med olie- eller gasfyr i BBR. Selskaberne har <strong>frem til 2028</strong> til at udrulle. Et projektforslag tager 3-6 måneder at godkende, og selve udrulningen op til 18 måneder.", ["vej_fv"]),
   ("Er der et godkendt projektforslag i dit område, kan du ikke få tilskud fra Varmepumpepuljen. Står dit område ikke på kortet, er der ingen umiddelbare planer om fjernvarme.", ["vej_fv"]),
   ("Størstedelen af fjernvarmen i Vejle Kommune er overskudsvarme leveret af TVIS.", ["vej_fv"]),
  ],
  "local_take": "Vejle Fjernvarme og Jelling Varmeværk ligger under landsgennemsnittet, mens Give og Egtved ligger over. Bor du i et gult eller blåt område i Vejle by, taler meget for at vente på fjernvarmen. I Give eller Egtved, eller uden for kortet, bør du regne på en varmepumpe.",
  "contact": ("Vejle Kommune, Team Varme", "51 68 60 95 · jordogvarme@vejle.dk", "vej_fv"),
  "faq": [
   ("Hvad koster fjernvarme i Vejle?", "Hos Vejle Fjernvarme koster et standardhus på 130 m² 14.911 kr. om året inkl. moms ifølge Forsyningstilsynets statistik pr. 31. januar 2026. Give Fjernvarme ligger på 20.800 kr. og Egtved Varmeværk på 22.010 kr.", ["ft_pris", "wg_pris"]),
   ("Skal jeg vente på fjernvarme eller købe varmepumpe nu i Vejle?", "Tjek din adresse på kommunens kort. Er området gult, blåt eller grønt, anbefaler kommunen, at du overvejer nøje, om det er værd at vente. Står det ikke på kortet, er der ingen umiddelbare planer.", ["vej_fv"]),
   ("Hvor kommer fjernvarmen i Vejle fra?", "Størstedelen er overskudsvarme leveret af TVIS ifølge Vejle Kommune.", ["vej_fv"]),
  ],
}
FV_PAGE["esbjerg"] = {
  "kw": "fjernvarme esbjerg / esbjerg fjernvarme varmepumpe",
  "evidence": "Autocomplete 'fjernvarme esbjerg': 10 forslag (bl.a. 'fjernvarme esbjerg pris', 'esbjerg fjernvarme varmepumpe', 'fjernvarme pris esbjerg 2026'). PAA: 'Hvor får Esbjerg fjernvarme fra?'. Også 'fjernvarme ribe' og 'fjernvarme bramming' med prisforslag.",
  "intro": "I Esbjerg kommer fjernvarmen fra DIN Forsyning, som selv kører store havvandsvarmepumper på havnen. Prisen er dog over landsgennemsnittet, og i kommunen spænder værkerne fra ca. 15.000 til over 30.000 kr. om året. Her er tallene.",
  "status": [
   ("DIN Forsyning leverer fjernvarme til Esbjerg by, bl.a. Sædding, Hjerting, Tarp og Tjæreborg, samt til Varde, Alslev og Nordby på Fanø. Det er <strong>ca. 25.500 husstande</strong>.", ["esb_fv"]),
   ("Det kulfyrede Esbjergværk blev taget ud af drift i sommeren 2024. Siden december 2024 har to <strong>havvandsvarmepumper</strong> på op til 70 MW leveret grundlast sammen med en elkedel og en fliskedel.", ["esb_fv"]),
   ("Uden for DIN Forsynings net har bl.a. Ribe, Bramming og Gørding egne værker med egne priser.", ["ft_pris", "wg_pris"]),
  ],
  "local_take": "DIN Forsyning ligger ca. 1.300 kr. over landsgennemsnittet for et standardhus. Hunderup-Sejstrup Fællesvarme (postnr. 6740) er et af de dyreste værker i statistikken. Står du uden for nettet med olie, gas eller elvarme, er en luft til vand-varmepumpe det oplagte valg, og så kan du søge tilskud.",
  "contact": ("DIN Forsyning (fjernvarme)", "74 74 74 74 · post@dinforsyning.dk", "esb_fv"),
  "faq": [
   ("Hvad koster fjernvarme i Esbjerg?", "Hos DIN Forsyning Varme koster et standardhus på 130 m² 18.249 kr. om året inkl. moms ifølge Forsyningstilsynets statistik pr. 31. januar 2026. Landsgennemsnittet er 16.953 kr.", ["ft_pris", "wg_pris"]),
   ("Hvor får Esbjerg sin fjernvarme fra?", "Siden december 2024 fra bl.a. to havvandsvarmepumper på op til 70 MW på Esbjerg Havn samt en elkedel og en fliskedel. Esbjergværket lukkede i sommeren 2024.", ["esb_fv"]),
   ("Kan jeg få tilskud til varmepumpe i Esbjerg Kommune?", "Kun hvis boligen ligger uden for fjernvarme og planlagt fjernvarme, og du skifter olie, gas, el eller biokedel ud. Tjek din adresse hos DIN Forsyning og på Plandata.dk.", ["se_vpp", "plandata"]),
  ],
}
FV_PAGE["odense"] = {
  "kw": "fjernvarme odense / varmepumpe odense",
  "evidence": "Autocomplete 'fjernvarme odense': 10 forslag (bl.a. 'fjernvarme odense kommune', 'odense fjernvarme prisstigninger'). 'fjernvarme årslev' → 'fjernvarme fyn årslev'. 'varmepumpe odense' → 'varmepumpe service odense'.",
  "intro": "I Odense er fjernvarmen så udbredt, at en luft til vand-varmepumpe især er relevant for huse uden for nettet i landsbyerne og i landzone. Her er Fjernvarme Fyns pris, området, der stadig udbygges, og hvad det koster at forlade fjernvarmen.",
  "status": [
   ("Fjernvarme Fyn skriver, at de fleste store bebyggede områder er ved at være forbundne, og at antallet af nye områder og kunder derfor er stabilt.", ["ode_fv"]),
   ("Pr. oktober 2026 står <strong>Lundsmarken i Årslev</strong> som det område, der er åbent for tilmelding.", ["ode_fv"]),
   ("Varmepumpepuljen giver kun tilskud uden for fjernvarmeområder og områder med planlagt fjernvarme. Tjek din adresse hos Fjernvarme Fyn og på Plandata.dk.", ["se_vpp", "plandata", "ode_fv"]),
  ],
  "local_take": "Fjernvarme Fyn ligger under landsgennemsnittet. Har du allerede fjernvarme i Odense, er det sjældent økonomisk oplagt at skifte. Står du uden for nettet med olie, gas eller elvarme, er luft til vand det typiske valg.",
  "contact": ("Fjernvarme Fyn", "65 47 30 00 · kontakt@fjernvarmefyn.dk", "ode_fv"),
  "faq": [
   ("Hvad koster fjernvarme i Odense?", "Hos Fjernvarme Fyn Distribution koster et standardhus på 130 m² 15.076 kr. om året inkl. moms ifølge Forsyningstilsynets statistik pr. 31. januar 2026. Landsgennemsnittet er 16.953 kr.", ["ft_pris", "wg_pris"]),
   ("Kan jeg få fjernvarme i Årslev?", "Fjernvarme Fyn har pr. oktober 2026 Lundsmarken i Årslev åben for tilmelding.", ["ode_fv"]),
   ("Kan det betale sig at skifte fjernvarme ud med varmepumpe i Odense?", "Sjældent, når fjernvarmeprisen er under landsgennemsnittet. Værket kan også kræve udtrædelsesgodtgørelse, som ifølge Energiankenævnet erfaringsmæssigt ligger på 10.000-100.000 kr.", ["ft_pris", "ean_udtr"]),
  ],
}
FV_PAGE["aalborg"] = {
  "kw": "varmepumpe aalborg fjernvarme / fjernvarme aalborg pris",
  "evidence": "Autocomplete 'varmepumpe aalborg' → 'varmepumpe aalborg fjernvarme', 'varmepumpe aalborg kommune'. 'fjernvarme aalborg': 10 forslag (bl.a. 'fjernvarme aalborg pris', 'aalborg fjernvarme pris 2026'). PAA på 'varmepumpe aalborg fjernvarme': 'Må man installere en varmepumpe, når man har fjernvarme?'. Relaterede: 'Havvandsvarmepumpe Aalborg', 'Norbis Park'.",
  "intro": "Aalborg Kommune har meldt klart ud: der kommer ikke mere fjernvarme ud over Ajstrup foreløbig. Samtidig er Aalborg Varmes pris blandt de højere i landet, og fjernvarmen er midt i et skifte væk fra kul. Her er, hvad det betyder for dit valg.",
  "status": [
   ("I varmeplanen fra 2022 blev <strong>21 områder</strong> screenet. Fire havde potentiale (Ajstrup, Hostrup, St. Restrup og Nr. Kongerslev), men ved udgangen af 2025 gennemføres kun konverteringen af Ajstrup.", ["aal_fv"]),
   ("Kommunen skriver, at der lige nu ikke er mulighed for yderligere udbygning, og at borgere i områderne bør overveje andre grønne opvarmningsformer, fx varmepumper.", ["aal_fv"]),
   ("Nordjyllandsværket skal udfases som kulfyret værk <strong>senest i 2028</strong>. Aalborg Forsyning bygger derfor i Norbis Park en havvandsvarmepumpe, tre elkedler og et varmelager på 200.000 m³.", ["aal_ve", "aal_forsyning"]),
  ],
  "local_take": "Aalborg Varme ligger ca. 3.400 kr. over landsgennemsnittet for et standardhus, mens fx Nibe Varmeværk ligger under. Bor du uden for fjernvarmen, peger kommunen selv på varmepumper. Har du fjernvarme, så tjek tilslutningspligt og udtrædelsesvilkår, før du regner på et skifte.",
  "contact": ("Aalborg Forsyning", "99 82 82 99", "aal_forsyning"),
  "faq": [
   ("Hvad koster fjernvarme fra Aalborg Varme?", "Et standardhus på 130 m² koster 20.348 kr. om året inkl. moms ifølge Forsyningstilsynets statistik pr. 31. januar 2026. Landsgennemsnittet er 16.953 kr.", ["ft_pris", "wg_pris"]),
   ("Må man installere en varmepumpe, når man har fjernvarme i Aalborg?", "Tjek først, om din ejendom har tilslutningspligt. I så fald skal de faste bidrag betales, selv om du ikke bruger varmen. Melder du dig helt ud, kan værket kræve udtrædelsesgodtgørelse.", ["ean_fast", "ean_udtr"]),
   ("Kommer der fjernvarme til Hostrup, St. Restrup eller Nr. Kongerslev?", "Ikke efter den nuværende varmeplan. Kun Ajstrup konverteres, og kommunen ser ikke mulighed for yderligere udbygning lige nu.", ["aal_fv"]),
  ],
}
FV_PAGE["randers"] = {
  "kw": "fjernvarme randers / fjernvarme spentrup / varmepumpe randers",
  "evidence": "Autocomplete 'fjernvarme randers': 9 forslag (bl.a. 'verdo fjernvarme randers', 'tilslutning fjernvarme randers'). 'fjernvarme spentrup' → 'tilmelding fjernvarme spentrup'. 'fjernvarme assentoft' → 'fjernvarme assentoft pris'. PAA på 'fjernvarme spentrup': 'Kan man blive tvunget til fjernvarme?'. Relaterede: 'Verdo fjernvarme Assentoft', 'Fjernvarme Stevnstrup', 'Fjernvarme Harridslev'.",
  "intro": "Verdo udbygger fjernvarmen i fire byer i Randers Kommune lige nu. Bor du i en af dem, bør du tjekke fjernvarmen, før du køber varmepumpe, også fordi du ikke kan få tilskud i planlagte fjernvarmeområder. Her er status og priserne.",
  "status": [
   ("Verdo har pr. oktober 2026 <strong>Assentoft, Harridslev, Stevnstrup og Spentrup</strong> åbne for tilmelding.", ["verdo_omr"]),
   ("I <strong>Spentrup</strong> er gravearbejdet i gang. Over 580 husstande, ca. 60 % af byen, har tilmeldt sig. De første boliger ventes tilsluttet i november, og transmissionsledningen ventes færdig i efteråret 2027.", ["ran_fv"]),
   ("Verdo anbefaler, at du ikke opsiger din gasaftale, før du har en fast dato for tilslutningen. Der går typisk et par måneder fra bindende tilmelding, og selve omlægningen i huset tager 1-2 dage.", ["verdo_omr"]),
  ],
  "local_take": "Verdo Varme i Randers ligger under landsgennemsnittet, mens fx Langå og Mellerup ligger over. I Verdos udbygningsbyer taler prisen for fjernvarme. Uden for dem er luft til vand det typiske valg, og så kan du søge tilskud.",
  "contact": ("Verdo", "70 10 02 30", "verdo_omr"),
  "faq": [
   ("Hvad koster fjernvarme hos Verdo i Randers?", "Hos Verdo Varme koster et standardhus på 130 m² 14.541 kr. om året inkl. moms ifølge Forsyningstilsynets statistik pr. 31. januar 2026. Landsgennemsnittet er 16.953 kr.", ["ft_pris", "wg_pris"]),
   ("Kan man blive tvunget til fjernvarme?", "Tilslutningspligt betyder, at du skal betale de faste bidrag, ikke at du skal bruge varmen. I nye områder pålægges der ifølge bl.a. Kolding Kommune ikke længere tilslutningspligt.", ["ean_fast", "kol_fv"]),
   ("Kan jeg få varmepumpetilskud i Spentrup?", "Næppe. Varmepumpepuljen giver ikke tilskud i områder med fjernvarme eller planlagt fjernvarme, og Spentrup er under udbygning.", ["se_vpp", "ran_fv"]),
  ],
}
FV_PAGE["horsens"] = {
  "kw": "fjernvarme horsens / varmepumpe horsens",
  "evidence": "Autocomplete 'fjernvarme horsens': 9 forslag. 'fjernvarme brædstrup' → 'brædstrup fjernvarme priser'; 'fjernvarme østbirk'. 'luft til vand varmepumpe horsens' og 'varmepumpe installation horsens' findes som forslag.",
  "intro": "Horsens-området har noget af landets billigste fjernvarme. Brædstrup Fjernvarme er blandt de ti billigste værker i Danmark, og Fjernvarme Horsens ligger også under gennemsnittet. Det gør regnestykket for en varmepumpe anderledes her end mange andre steder.",
  "status": [
   ("Fjernvarme Horsens er gået fra <strong>8.200 til 22.400 kunder</strong> fra 2015 til 2025 og har lagt 470 km nye ledninger. De sidste kunder i det store udbygningsprojekt kunne tilslutte sig i 2023.", ["hor_fv"]),
   ("Selskabet forventer at nå 25.000 kunder i 2030, heriblandt flere erhvervskunder.", ["hor_fv"]),
   ("Brædstrup Fjernvarme er blandt de ti billigste værker i Forsyningstilsynets statistik med 9.855 kr. for et standardhus.", ["wg_pris"]),
  ],
  "local_take": "Har du fjernvarme i Horsens eller Brædstrup, er der sjældent penge at hente ved at skifte til varmepumpe. Bor du uden for nettet med olie, gas eller elvarme, er luft til vand det typiske valg, og så kan du søge tilskud.",
  "contact": ("Horsens Kommune", "76 29 29 29", "hor_sol"),
  "faq": [
   ("Hvad koster fjernvarme i Horsens?", "Hos Fjernvarme Horsens koster et standardhus på 130 m² 13.254 kr. om året inkl. moms ifølge Forsyningstilsynets statistik pr. 31. januar 2026. Landsgennemsnittet er 16.953 kr.", ["ft_pris", "wg_pris"]),
   ("Er fjernvarme billig i Brædstrup?", "Ja. Brædstrup Fjernvarme er blandt de ti billigste værker i statistikken med 9.855 kr. om året for et standardhus.", ["wg_pris"]),
   ("Kan jeg stadig få fjernvarme i Horsens?", "Fjernvarme Horsens forventer at nå 25.000 kunder i 2030. Kontakt selskabet eller tjek Plandata.dk for at se, om din adresse ligger i et fjernvarmeområde.", ["hor_fv", "plandata"]),
  ],
}

# ---------- daglig by-rutine 26. okt. 2026 ----------
SOL_REG["aarhus"] = {
  "kw": "solceller aarhus kommune",
  "evidence": "Autocomplete 26/10 2026: 'solceller aarhus' → 'solceller aarhus kommune' (første forslag); 'aarhus kommune solceller'. Top-resultat er aarhus.dk.",
  "intro": "Aarhus Kommune skriver sine regler for solceller ud med tal: 2,5 meter til skel, 1 meter over et fladt tag, 1,8 meter for anlæg på jorden i byzone og 20 meter fra stuehuset i landzone. Her er de samlet, så du kan se, om dit anlæg kræver tilladelse.",
  "sections": [
   ("Hus, garage og carport: afstand og højde", [
     ("ul", [("Solcelleanlæg må ikke placeres på bygninger, der står <strong>tættere end 2,5 meter på skel</strong>, eller 5 meter ved nabo- og stiskel i sommerhusområder (BR18 § 179). Vil du tættere på, skal du søge byggetilladelse.", ["aar_sol", "br18_179"]),
             ("Anlægget skal også overholde bygningsreglementets maksimale højder: §§ 176-178 for selve huset og §§ 181-183 for garager, carporte, udhuse, drivhuse og overdækkede terrasser.", ["aar_sol"]),
             ("Står panelerne <strong>mere end 1 meter over et fladt tag</strong>, er anlægget en bygningslignende konstruktion, der kræver byggetilladelse.", ["aar_sol"]),
             ("Du har selv ansvaret for, at tagkonstruktionen kan bære vægten, og at anlægget er fastgjort forsvarligt. Er du i tvivl, anbefaler kommunen en professionel rådgiver.", ["aar_sol"])]),
   ]),
   ("Lokalplaner: solceller tæller ikke som reflekterende", [
     ("p", "Mange lokalplaner forbyder reflekterende materialer. I Aarhus Kommune betragtes solceller <strong>ikke</strong> som reflekterende materialer, så de bestemmelser rammer dem ikke.", ["aar_sol"]),
     ("p", "Står der i lokalplanen, at anlæg til solenergi skal indgå som en del af tagfladen, betyder det i Aarhus, at panelerne på et eksisterende hus skal sidde parallelt med tagfladen og <strong>højst 15 cm over den</strong>. Ved nybyggeri skal de integreres i tagdækningen.", ["aar_sol"]),
     ("p", "Kommunen henviser til sin digitale planportal for lokalplaner og byplanvedtægter og til tinglysning.dk for servitutter. Vil du afvige fra en plan eller servitut, kræver det tilladelse.", ["aar_sol"]),
   ]),
   ("Solceller i haven og i landzone", [
     ("ul", [("Et anlæg på terræn er en selvstændig konstruktion og kræver som udgangspunkt byggetilladelse.", ["aar_sol"]),
             ("Undtaget er anlæg i byzone og sommerhuszone, der er <strong>højst 1,8 meter høje</strong>. De skal stadig holde 2,5 meter til skel.", ["aar_sol"]),
             ("I landzone kræver et anlæg på jorden både byggetilladelse og landzonetilladelse. Kommunen giver ofte tilladelse, når anlægget står inden for ca. <strong>20 meter fra stuehuset</strong>, men sjældent i det åbne land.", ["aar_sol"])]),
   ]),
   ("Bevaringsværdi, BBR og gebyr", [
     ("ul", [("Har huset bevaringsværdi 1-4 i kommuneplanen, kan du ikke forvente tilladelse. På fredede bygninger må der som udgangspunkt ikke sættes solceller op, og ændringer skal godkendes af Slots- og Kulturstyrelsen.", ["aar_sol"]),
             ("Ligger ejendommen i et fredet område eller inden for en beskyttelseslinje ved sø, å, skov eller strand, kan det kræve dispensation.", ["aar_sol"]),
             ("Anlægget skal altid anmeldes til BBR med adresse, areal og samlet effekt i kW. Ansøgninger sendes via Byg og Miljø.", ["aar_sol"]),
             ("Søger du til et eksisterende hus eller et anlæg på terræn, opkræver kommunen et selvstændigt gebyr. Søger du sammen med byggetilladelsen til et nyt hus, gør den ikke.", ["aar_sol"])]),
   ]),
  ],
  "faq": [
   ("Skal jeg søge byggetilladelse til solceller på mit hus i Aarhus?", "Normalt ikke, når huset står mindst 2,5 meter fra skel og højdekravene overholdes. Du skal søge, hvis anlægget står mere end 1 meter over et fladt tag, eller hvis du vil afvige fra lokalplan, byplanvedtægt eller servitut.", ["aar_sol"]),
   ("Hvad betyder det, at solceller skal indgå i tagfladen?", "Aarhus Kommune læser kravet sådan, at panelerne på et eksisterende hus skal monteres parallelt med tagfladen og højst 15 cm over den. Ved nybyggeri skal de integreres direkte i tagdækningen.", ["aar_sol"]),
   ("Må jeg sætte solceller på jorden i min have i Aarhus?", "I byzone og sommerhuszone ja, uden byggetilladelse, hvis anlægget er højst 1,8 meter højt og står mindst 2,5 meter fra skel. I landzone kræver det både byggetilladelse og landzonetilladelse.", ["aar_sol"]),
   ("Hvem kontakter jeg i Aarhus Kommune om solceller?", "Byggeri, Karen Blixens Boulevard 7, 8220 Brabrand, på 89 40 22 13 (mandag-fredag kl. 9.30-11.30) eller byggesag@mtm.aarhus.dk. Møder med en sagsbehandler kræver forudgående aftale.", ["aar_sol"]),
  ],
}
SOL_REG["viborg"] = {
  "kw": "solceller viborg kommune",
  "evidence": "Autocomplete 26/10 2026: 'solceller viborg' → 'solceller viborg', 'solceller viborg kommune'. Top-resultat er viborg.dk.",
  "intro": "Viborg Kommune har én hovedregel: følger panelerne tagbeklædningen, og overholder huset bygningsreglementets højde- og afstandskrav, skal du ikke søge. Stativer og anlæg på jorden kræver altid tilladelse. Her er resten af reglerne.",
  "sections": [
   ("Hovedreglen for solceller på taget", [
     ("p", "Kan bygningen med solcelleanlægget placeret <strong>parallelt med tagbeklædningen</strong> overholde højde- og afstandskravene i bygningsreglementet eller lokalplanen, kræver det ingen byggetilladelse.", ["vib_sol"]),
     ("p", "Afviger bygningen fra kravene, når anlægget kommer op, eller skal panelerne sidde på <strong>stativ</strong>, skal du have byggetilladelse, før anlægget sættes op. For parcel-, række- og dobbelthuse er afstandskravet bl.a. mindst 2,5 meter til skel.", ["vib_sol", "br18_179"]),
     ("note", "Viborg Kommune skriver, at anlægget ikke må være reflekterende, og at placeringen bør tilpasses, så den ikke generer naboerne. Kan anlægget ikke overholde reglerne, vurderer kommunen sagen konkret, og det kan føre til en høring i området.", ["vib_sol"]),
   ]),
   ("Landbrug, erhverv og anlæg på jorden", [
     ("p", "Anlæg på erhvervsvirksomheder, avls- og driftsbygninger, industribygninger og på terræn kræver <strong>altid byggetilladelse</strong>. Står anlægget på jorden eller på en driftsbygning i landzone, kan det også kræve landzonetilladelse.", ["vib_sol"]),
   ]),
   ("Lokalplan, deklarationer og fredning", [
     ("ul", [("Er ejendommen omfattet af en lokalplan eller byplanvedtægt, skal du tjekke, om planen forhindrer solceller. I så fald skal du søge dispensation, og det kan føre til en høring.", ["vib_sol"]),
             ("Deklarationer og servitutter på ejendommen kan du se på tinglysning.dk. Naturbeskyttelsesloven og planloven kan også begrænse, hvor anlægget må stå.", ["vib_sol"]),
             ("Er huset fredet eller registreret som bevaringsværdigt, skal du kontakte kommunen, før du går i gang.", ["vib_sol"])]),
   ]),
   ("Forhåndsdialog, ansøgning og BBR", [
     ("ul", [("Viborg Kommune tilbyder en <strong>forhåndsdialog</strong>, før du søger, så du kan undgå typiske fejl i ansøgningen.", ["vib_byg"]),
             ("Ansøgningen sendes via Byg og Miljø. Den skal bl.a. indeholde en fuldmagt fra ejeren og oplysning om, hvorvidt projektet kræver dispensation fra lokalplanen. Kommunen screener ansøgningen, før sagsbehandlingen begynder.", ["vib_ans"]),
             ("Når anlægget er færdigt, skal det registreres i BBR via kommunens selvbetjening for tekniske anlæg.", ["vib_sol"])]),
   ]),
  ],
  "faq": [
   ("Kræver solceller byggetilladelse i Viborg Kommune?", "Ikke når panelerne ligger parallelt med tagbeklædningen, og huset overholder højde- og afstandskravene. Stativer, anlæg på jorden og anlæg på landbrugs- og erhvervsbygninger kræver altid tilladelse.", ["vib_sol"]),
   ("Må jeg sætte solceller op på stativ i Viborg?", "Ja, men det kræver byggetilladelse, før anlægget sættes op. Det gælder også, hvis bygningen ellers ville afvige fra bygningsreglementets højde- og afstandskrav.", ["vib_sol"]),
   ("Kræver solceller på en driftsbygning tilladelse i Viborg?", "Ja. Anlæg på avls- og driftsbygninger kræver altid byggetilladelse, og i landzone kan der også kræves landzonetilladelse.", ["vib_sol"]),
   ("Hvornår kan jeg ringe til Viborg Kommune om solceller?", "Teknik & Miljø, Byggeri, på 87 87 52 52: mandag-onsdag kl. 9-14, torsdag kl. 9-17 og fredag kl. 9-13. Du kan også skrive til byggeri@viborg.dk.", ["vib_sol"]),
  ],
}
FV_PAGE["aarhus"] = {
  "kw": "fjernvarme aarhus / fjernvarme aarhus pris / varmepumpe aarhus",
  "evidence": "Autocomplete 26/10 2026 'fjernvarme aarhus': 10 forslag (bl.a. 'fjernvarme aarhus pris', 'fjernvarme aarhus kommune', 'kredsløb fjernvarme aarhus', 'fremtidens fjernvarme aarhus'). 'varmepumpe aarhus' → 'varmepumpe pris aarhus'. 'luft til vand varmepumpe aarhus' gav INGEN forslag, så Aarhus har ingen selvstændig varmepumpe-byside (93 % fjernvarme).",
  "intro": "I Aarhus Kommune har ni ud af ti huse fjernvarme, de fleste fra Kredsløb, og seks mindre værker er med i Varmeplan Aarhus. En luft til vand-varmepumpe er derfor kun aktuel for huse uden for nettet. Her er de lokale priser, planerne for fjernvarmen og tilskudsreglerne.",
  "status": [
   ("Kredsløbs planforslag <strong>Fremtidens Fjernvarme</strong> skal erstatte varmen fra Studstrupværket og indebærer nye investeringer for 2,8 mia. kr. Forslaget blev opdateret i marts 2026 og var i høring.", ["aar_ff", "aar_geo"]),
   ("Det opdaterede forslag lægger op til <strong>nye transmissionsledninger til og fra Sabro og Harlev</strong>, mens varmeforsyningen af Odder og Hørning fra Aarhus udgår senest i 2030.", ["aar_ff"]),
   ("Luft til vand-varmepumperne i planen øges fra 100 til 130 MW, geotermien samles på 3 lokaliteter med ca. 110 MW, og overskudsvarme fra et CO₂-fangstanlæg udskydes fra 2030 til 2035.", ["aar_ff"]),
   ("Kommunens forslag til Energiplan 2025-2045 regner med ca. 45.000 nye boliger i kommunen over de næste 20 år.", ["aar_mr"]),
  ],
  "local_take": "Kredsløb ligger ca. 700 kr. under landsgennemsnittet for et standardhus, mens alle seks mindre værker ligger over. Har du fjernvarme i Aarhus, er der sjældent penge i at skifte til varmepumpe. Varmepumpen er relevant for de få huse uden for nettet, fx i landsbyer som Lillering, Hørret og Fårup.",
  "contact": ("Kredsløb, kundeservice fjernvarme", "77 88 10 10 (hverdage kl. 9-14)", "kredslob"),
  "faq": [
   ("Hvad koster fjernvarme i Aarhus?", "Hos Kredsløb Fjernvarme koster et standardhus på 130 m² 16.229 kr. om året inkl. moms ifølge Forsyningstilsynets statistik pr. 31. januar 2026. Lystrup Fjernvarme ligger på 18.751 kr. og Tranbjerg Varmeværk på 19.549 kr. Landsgennemsnittet er 16.953 kr.", ["ft_pris", "wg_pris"]),
   ("Hvor kommer fjernvarmen i Aarhus fra?", "I dag bl.a. fra Studstrupværket, Kredsløbs eget halmfyrede kraftvarmeværk og affaldsforbrænding. Aftalen om træpillevarme fra Studstrupværket udløber i 2030, og siden oktober 2025 har Kredsløb fået 20 MW geotermisk varme fra Innargi i Skejby, som skal øges til 111 MW frem mod 2030.", ["aar_geo"]),
   ("Hvem kontakter jeg om fjernvarme på min adresse i Aarhus?", "Kredsløbs kundeservice for fjernvarme på 77 88 10 10 på hverdage kl. 9-14. Bor du i Lystrup, Løgten, Malling, Tranbjerg eller et andet område med eget værk, så kontakt værket direkte.", ["kredslob", "ft_pris"]),
  ],
}
FV_PAGE["viborg"] = {
  "kw": "fjernvarme viborg / fjernvarme viborg pris / varmepumpe viborg",
  "evidence": "Autocomplete 26/10 2026 'fjernvarme viborg': 10 forslag (bl.a. 'fjernvarme viborg kommune', 'fjernvarme viborg pris', 'viborg fjernvarme tilslutning'). 'fjernvarme bjerringbro' → 'bjerringbro fjernvarme priser'; 'fjernvarme stoholm' → 'stoholm fjernvarme priser'. 'luft til vand varmepumpe viborg' findes som forslag.",
  "intro": "I Viborg Kommune leverer 14 fjernvarmeselskaber varme, og priserne spænder fra ca. 13.400 til over 22.000 kr. om året. Samtidig har hvert sjette hus stadig naturgas, og Viborg Varme konverterer gasområder i byen et kvarter ad gangen. Her er status og tallene.",
  "status": [
   ("Kommunens varmeplan er et kort over <strong>potentielle nye fjernvarmeområder</strong> på Minimap. Den bliver til virkelighed gennem konkrete projektforslag.", ["vib_vp"]),
   ("Viborg Varme er i gang i <strong>Planetkvarteret</strong> (Merkurvej, Neptunvej og Saturnvej i Overlund) fra marts 2026 til februar 2027. <strong>Liseborgvej etape 1</strong> med op til 138 forbrugere starter i november 2026, og Gråmejsevej og Sortmejsevej følger i februar 2027.", ["vib_slip", "vib_lise"]),
   ("Senere er Engbakkevej/Nørresøvej Nord (oktober 2027), Engelsborg og Lupinmarken (2028) og Engelsborg etape B (2030) planlagt. Bor du i et af områderne, kan du ikke få tilskud fra Varmepumpepuljen.", ["vib_slip", "se_vpp"]),
   ("Byrådets mål er, at alle olie- og naturgasfyr er omstillet til vedvarende energi i 2030. Kommunen skriver til boligejere med olie- og gasfyr i områder, der ikke forventes at få fjernvarme, og som kan få tilskud.", ["vib_strat"]),
  ],
  "local_take": "Viborg Varme ligger ca. 1.900 kr. over landsgennemsnittet i Forsyningstilsynets standardhus, mens Karup og Løgstrup ligger langt under. Har du gasfyr i et af Viborg Varmes konverteringsområder, taler meget for at vente på fjernvarmen. Ligger du uden for kortet, fx i en landsby med oliefyr, er en luft til vand-varmepumpe med tilskud det oplagte valg.",
  "contact": ("Viborg Varme", "87 27 58 00 · post@viborgvarme.dk", "vib_slip"),
  "faq": [
   ("Hvad koster fjernvarme i Viborg?", "Hos Viborg Varme koster et standardhus på 130 m² med 18,1 MWh 18.854 kr. om året inkl. moms ifølge Forsyningstilsynets statistik pr. 31. januar 2026. Viborg Varme oplyser selv 15.855 kr. i 2026 for et parcelhus på 140 m² med et forbrug på 14.000 kWh.", ["ft_pris", "wg_pris", "vib_budget"]),
   ("Hvornår kommer overskudsvarmen fra Apple til Viborg?", "Ifølge Dansk Fjernvarme begynder Viborg Varme at modtage overskudsvarme fra Apples datacenter og Energinets transformerstation i Tjele i andet halvår 2027, først 12 MW og forhåbentlig 24,5 MW inden 2030.", ["vib_df"]),
   ("Kan jeg få varmepumpetilskud, hvis mit gasområde får fjernvarme?", "Nej. Varmepumpepuljen giver ikke tilskud i områder med fjernvarme eller planlagt fjernvarme. Tjek Viborg Varmes projektliste og kommunens varmeplan, før du søger.", ["se_vpp", "vib_slip", "vib_vp"]),
  ],
}

NATIONAL["/solceller/pris/"] = {
  "svc": "solceller", "crumb": "Pris",
  "kw": "solceller pris / solceller pris inkl montering",
  "evidence": "Autocomplete 'solceller pris': 'inkl montering', 'pr m2', 'med batteri', '2026', 'pr kwh'. PAA: 'Hvad koster solceller inkl. montering?', 'Kan det betale sig at få solceller i 2026?', 'Hvad koster 10m2 solceller?', 'Kan private solceller betale sig?'. Bylokale varianter ('solceller pris kolding' osv.) gav INGEN forslag i nogen af de 7 byer, så der er ingen pris-side pr. by.",
  "title": "Solceller pris 2026: hvad koster et anlæg inkl. montering?",
  "desc": "Solceller pris 2026: typisk 50.000-135.000 kr. inkl. montering. Pris pr. kWp og m², ekstraposter, tilbagebetaling og elafgift med kilder.",
  "h1": "Solceller pris 2026: hvad koster et anlæg inkl. montering?",
  "intro": "Der findes ingen officiel pris på solceller, og vi har ikke fundet kilder, der viser, at prisen afhænger af, om du bor i Kolding eller Aalborg. Det er tag, anlægsstørrelse og installatør, der flytter prisen. Her er de typiske priser for 2026 med kilder, og hvad du skal tjekke i et tilbud.",
  "sections": [
   ("Typiske priser inkl. montering", [
     ("table", ["Anlæg", "Pris inkl. montering", "Produktion pr. år", "Pris pr. kWp"],
      [["4 kWp (ca. 9-10 paneler)", "ca. 50.000-55.000 kr.", "ca. 3.800-4.200 kWh", "ca. 12.500-14.000 kr."],
       ["6 kWp (typisk parcelhus)", "ca. 90.000-95.000 kr.", "ca. 5.700-6.300 kWh", "ca. 15.000-16.000 kr."],
       ["10 kWp (stort forbrug/elbil)", "ca. 125.000-135.000 kr.", "ca. 9.500-10.500 kWh", "ca. 12.500-13.500 kr."]], ["es_sol"]),
     ("p", "Pr. m² panel svarer det til ca. 2.150-3.300 kr., fordi et anlæg fylder ca. 4,7-6 m² pr. kWp. SparEnergi skriver, at et solcelleanlæg typisk fylder 15-40 m².", ["es_sol", "se_sol"]),
     ("p", "Energisparer.dk ser typisk 20-40 % forskel mellem tilbud på det samme anlæg og anbefaler at få mindst tre tilbud.", ["es_sol"]),
   ]),
   ("Poster, der kan komme oveni", [
     ("ul", [("Stillads: typisk 4.000-12.000 kr.", ["es_sol"]), ("Ny eltavle: typisk 5.000-15.000 kr., hvis tavlen skal opgraderes.", ["es_sol"]),
             ("Inverter: typisk 8.000-18.000 kr. SparEnergi skriver, at den normalt skal udskiftes efter ca. 10 år, mens panelerne holder ca. 25 år.", ["es_sol", "se_sol"]),
             ("Løbende udgifter: omkring 500 kr. om året til netselskabet.", ["se_sol"])]),
   ]),
   ("Kan det betale sig i 2026?", [
     ("p", "Det afhænger mest af, hvor meget af strømmen du selv bruger. SparEnergi angiver en samlet besparelse på typisk 2.500-7.000 kr. om året. Salg af overskudsstrøm op til 7.000 kr. om året er skattefrit pr. ejer.", ["se_sol"]),
     ("table", ["Anlæg ved 4.000 kWh årligt forbrug", "Simpel tilbagebetalingstid"], [["2 kWp", "12 år"], ["4 kWp", "15 år"], ["6 kWp", "17 år"]], ["se_sol"]),
     ("p", "SparEnergis tabel viser, at et for stort anlæg i forhold til forbruget tjener sig langsommere hjem. Energisparer.dk regner med ca. 16 års tilbagebetaling for et 6 kWp-anlæg og en pris på ca. 0,77 kr. pr. produceret kWh over levetiden.", ["se_sol", "es_sol"]),
     ("note", "Elafgiften er nede på 0,8 øre pr. kWh (ekskl. moms) i 2026 og 2027, så den strøm, du selv bruger, sparer dig mindre i de to år. Efter gældende lov stiger afgiften igen fra 2028.", ["elafgift", "elafgift_lov"]),
   ]),
   ("Fradrag og afgifter", [
     ("ul", [("Håndværkerfradrag: op til 9.000 kr. pr. person i 2026 for arbejdslønnen, hvis betingelserne er opfyldt.", ["hvfradrag", "hvbeting"]),
             ("Har du både solceller og elbil, kan du fra 1. januar 2026 søge refusion af elafgift.", ["se_sol"]),
             ("Anlægget skal installeres af en VE-godkendt installatør og registreres hos netselskabet.", ["se_sol"])]),
   ]),
  ],
  "faq": [
   ("Hvad koster solceller inkl. montering?", "Ifølge Energisparer.dk (oktober 2026) typisk ca. 50.000-55.000 kr. for 4 kWp, 90.000-95.000 kr. for 6 kWp og 125.000-135.000 kr. for 10 kWp.", ["es_sol"]),
   ("Hvad koster 10 m² solceller?", "Med ca. 2.150-3.300 kr. pr. m² er det omkring 21.500-33.000 kr. for 10 m² panel. 10 m² svarer dog kun til ca. 2 kWp, og små anlæg er dyrere pr. kWp. Det er vores omregning, ikke en pris fra en installatør.", ["es_sol"]),
   ("Kan private solceller betale sig?", "Ofte, hvis du bruger en stor del af strømmen selv. SparEnergi angiver en samlet besparelse på typisk 2.500-7.000 kr. om året og en simpel tilbagebetalingstid på 12-17 år afhængigt af anlæggets størrelse.", ["se_sol"]),
   ("Er prisen anderledes i Jylland end på Fyn?", "Vi har ikke fundet kilder, der viser regionale prisforskelle. Prisen afhænger af tag, adgangsforhold, anlæg og installatør, så sammenlign flere tilbud.", []),
  ],
}
NATIONAL["/solceller/med-batteri/"] = {
  "svc": "solceller", "crumb": "Med batteri",
  "kw": "solceller med batteri / solceller med batteri pris",
  "evidence": "Autocomplete 'solceller med batteri': 'pris', 'inkl montering', '10 kwh', 'tilbud'. 'solceller pris' → 'solceller pris med batteri'. PAA: 'Kan det betale sig at købe solceller med batteri?', 'Hvad koster et 5 kW solcelleanlæg med batteri?', 'Hvad koster det at få solceller og batteri?', 'Hvilke solceller med batteri er bedst?'. Bylokale varianter gav ingen forslag.",
  "title": "Solceller med batteri: pris og om det kan betale sig (2026)",
  "desc": "Et batteri til solceller koster typisk 35.000-80.000 kr. ekstra. Se hvornår det kan betale sig, hvad det gør for selvforsyningen, og hvad tilbuddet skal vise.",
  "h1": "Solceller med batteri: pris og om det kan betale sig",
  "intro": "Et batteri gemmer dagens solstrøm til aftenen. Det hæver din selvforsyning markant, men det koster mange penge og holder kortere end panelerne. Her er tallene for 2026, og hvornår et batteri giver mening.",
  "sections": [
   ("Hvad koster et batteri til solceller?", [
     ("table", ["Opsætning (6 kWp)", "Typisk samlet pris", "Selvforsyning", "Tilbagebetaling"],
      [["Uden batteri", "ca. 90.000-95.000 kr.", "ca. 30-40 %", "ca. 16 år"],
       ["Med batteri (ca. 10 kWh)", "ca. 137.000-152.000 kr.", "ca. 60-80 %", "ca. 15-16 år, men batteriet holder 10-15 år"]], ["es_sol"]),
     ("p", "Energisparer.dk angiver, at et batteri typisk lægger 35.000-80.000 kr. oven i prisen, afhængigt af kapaciteten, som oftest er 5-15 kWh.", ["es_sol"]),
   ]),
   ("Kan det betale sig?", [
     ("p", "SparEnergi skriver, at et batteri ofte er en god idé, men at batterier kan være dyre, og at du bør spørge installatøren, om det kan betale sig for dig.", ["se_sol"]),
     ("p", "Med Energisparer.dk's tal er tilbagebetalingstiden omtrent den samme med og uden batteri. Men batteriet skal typisk skiftes efter 10-15 år, mens panelerne holder ca. 25 år. Det trækker regnestykket i retning af anlægget uden batteri.", ["es_sol", "se_sol"]),
     ("ul", [("<strong>Taler for et batteri:</strong> stort forbrug om aftenen og natten, fx elbil, der lader om aftenen, eller ønsket om højere selvforsyning.", ["es_sol"]),
             ("<strong>Taler imod:</strong> lavt aftenforbrug, eller at du kan flytte forbruget til dagtimerne, fx opvask og tøjvask. Det bedste for økonomien er at bruge så meget solstrøm som muligt selv.", ["se_sol"])]),
   ]),
   ("Regn på dit eget hus gratis", [
     ("p", "I to af vores byer kan du få en gratis, uvildig beregning med SolarSim: <strong>Horsens Kommune</strong> frem til 15. februar 2027 og <strong>Kolding Kommune</strong> frem til 15. september 2027. Horsens Kommune skriver, at værktøjet også vurderer, om et batteri kan betale sig.", ["hor_sol", "kol_sol"]),
   ]),
   ("Det skal tilbuddet vise", [
     ("ul", [("Batteriets brugbare kapacitet i kWh og garantien.", []),
             ("Om inverteren kan styre et batteri (hybridinverter), eller om der skal mere udstyr til.", []),
             ("Hvor stor en del af din produktion batteriet forventes at flytte fra salg til eget forbrug.", ["es_sol"]),
             ("Prisen på batteriet for sig, så du kan sammenligne med og uden.", [])]),
     ("note", "Punkterne uden kildehenvisning er vores egne anbefalinger til, hvordan tilbud kan sammenlignes.", []),
   ]),
  ],
  "faq": [
   ("Kan det betale sig at købe solceller med batteri?", "Det afhænger af dit aftenforbrug. Med Energisparer.dk's tal er tilbagebetalingen omtrent den samme med og uden batteri, men batteriet holder kun 10-15 år, så anlæg uden batteri er ofte den bedste forretning samlet set.", ["es_sol"]),
   ("Hvad koster det at få solceller og batteri?", "For et 6 kWp-anlæg med ca. 10 kWh batteri angiver Energisparer.dk typisk 137.000-152.000 kr.", ["es_sol"]),
   ("Hvad koster et 5 kW solcelleanlæg med batteri?", "Vi har ikke fundet en kilde med netop 5 kWp. Energisparer.dk angiver ca. 50.000-55.000 kr. for 4 kWp og 90.000-95.000 kr. for 6 kWp, plus typisk 35.000-80.000 kr. for et batteri. Få et konkret tilbud.", ["es_sol"]),
   ("Hvilke solceller med batteri er bedst?", "Vi rangerer ikke mærker. Sammenlign kapacitet, garanti, inverter og forventet effekt på dit eget forbrug, og bed flere installatører om tilbud på samme grundlag.", []),
  ],
}

NATIONAL["/varmepumpe/pris/"] = {
  "svc": "varmepumpe", "crumb": "Pris", "updated": ("3. november 2026", "2026-11-03"),
  "kw": "luft til vand varmepumpe pris / pris inkl montering",
  "evidence": "Autocomplete 'luft til vand varmepumpe pris': 10 forslag (bl.a. 'inkl montering', 'inkl montering jylland', '200m2', '250 m2', '300 m2'). PAA: 'Hvad koster en varmepumpe til et hus på 150 m2?', 'Kan det betale sig at få en luft til vand varmepumpe?', 'Hvad koster en luft til vand varmepumpe om året?'. Bylokale varianter ('luft til vand varmepumpe pris odense' osv.) gav INGEN forslag i de 7 byer, så der er ingen pris-side pr. by.",
  "title": "Luft til vand-varmepumpe pris 2026 inkl. montering",
  "desc": "En luft til vand-varmepumpe koster typisk 90.000-150.000 kr. inkl. montering. Se driftsudgift, tilskud, ekstraposter og hvad tilbuddet skal vise.",
  "h1": "Hvad koster en luft til vand-varmepumpe i 2026?",
  "intro": "Prisen på en luft til vand-varmepumpe afhænger af husets varmebehov, dit varmesystem og hvor meget ekstra arbejde der skal til. Vi har ikke fundet kilder, der viser regionale prisforskelle i Nordjylland, resten af Jylland, på Fyn eller på Sjælland. Her er prisspændene fra to kilder, hvad varmen koster om året, og hvordan tilskuddet påvirker regnestykket.",
  "sections": [
   ("Pris inkl. montering", [
     ("table", ["Type", "Pris inkl. montering", "Kilde"],
      [["Luft til vand", "typisk 100.000-130.000 kr.", "SparEnergi"], ["Luft til vand", "ca. 90.000-150.000 kr.", "Energisparer.dk"], ["Jordvarme", "ca. 120.000-180.000 kr.", "Energisparer.dk"], ["Luft til luft (supplement)", "ca. 12.000-25.000 kr.", "Energisparer.dk"]], ["se_vp", "es_vp"]),
     ("p", "Energisparer.dk omregner til ca. 9.000-15.000 kr. pr. kW, fra ca. 90.000 kr. for 6 kW til ca. 150.000 kr. for 16 kW. Hvor mange kW dit hus skal bruge, afhænger af varmetabet, ikke kun af antallet af kvadratmeter. Derfor bør installatøren dimensionere anlægget. Se typiske priser for et hus på 150 og 200 m² i guiden til <a href=\"/varmepumpe/luft-til-vand/\">luft til vand varmepumpe</a>.", ["es_vp", "es_l2v"]),
   ]),
   ("Pris inkl. montering i Nordjylland og på Sjælland", [
     ("p", "Prisspændene ovenfor er landsdækkende. Vi har ikke fundet offentlige kilder, der viser, at montering koster mere eller mindre i Nordjylland eller på Sjælland. Forskellen ligger i driften: Energisparer.dk regner med ca. 7.500 kr. om året i Vestdanmark og ca. 8.000 kr. i Østdanmark ved en SCOP på 3,5, fordi elprisen er forskellig i de to prisområder.", ["es_vp"]),
     ("p", "Lokale regler, fjernvarme og tilskud i Nordjylland: <a href=\"/varmepumpe/aalborg/\">Aalborg</a> og <a href=\"/varmepumpe/hjoerring/\">Hjørring</a>. På Sjælland: <a href=\"/varmepumpe/roskilde/\">Roskilde</a>, <a href=\"/varmepumpe/koege/\">Køge</a>, <a href=\"/varmepumpe/holbaek/\">Holbæk</a>, <a href=\"/varmepumpe/slagelse/\">Slagelse</a> og <a href=\"/varmepumpe/naestved/\">Næstved</a>.", []),
   ]),
   ("Poster, du skal spørge ind til", [
     ("ul", [("Opgradering af eltavlen.", ["es_vp"]), ("Buffertank.", ["es_vp"]), ("Fundament til udedelen.", ["es_vp"]),
             ("Bortskaffelse af det gamle olie- eller gasfyr.", ["es_vp"]),
             ("Afkobling fra gasnettet, hvis du har gas. Gebyret kan dækkes af Evidas afkoblingspulje i 2026.", ["evida_afk"])]),
   ]),
   ("Hvad koster varmen om året?", [
     ("table", ["Opvarmning af 130 m² hus", "Årlig udgift til varme", "Inkl. afskrivning, service og rente"],
      [["Luft til vand med gulvvarme", "7.288 kr.", "18.463 kr."], ["Luft til vand med radiatorer", "9.386 kr.", "20.561 kr."], ["Fjernvarme (landsgennemsnit)", "16.953 kr.", "20.050 kr."], ["Gasfyr", "18.433 kr.", "23.743 kr."], ["Oliefyr", "32.388 kr.", "38.153 kr."], ["Elradiatorer", "30.974 kr.", "31.991 kr."]], ["bolius_varme"]),
     ("p", "Bolius' tal bygger på et hus på 130 m² med et forbrug på 18.100 kWh og gennemsnitspriser for de seneste 12 måneder. Energisparer.dk regner med en driftsudgift på ca. 7.500 kr. om året i Vestdanmark og ca. 8.000 kr. i Østdanmark ved en SCOP på 3,5.", ["bolius_varme", "es_vp"]),
   ]),
   ("Tilskud eller håndværkerfradrag", [
     ("p", "Du kan søge <strong>27.000 kr.</strong> fra Varmepumpepuljen, når en helårsbolig uden for fjernvarme skifter olie, gas, el eller biokedel ud. Puljen lukker senest 30. november 2026 eller når midlerne er brugt. Får du tilskud, kan du <strong>ikke</strong> også få håndværkerfradrag for samme varmepumpe.", ["vpp_faq"]),
     ("example", "<strong>Regneeksempel (vores illustration, ikke et tilbud):</strong> En luft til vand-varmepumpe til 115.000 kr. (midt i SparEnergis spænd) minus 27.000 kr. i tilskud giver 88.000 kr. Det forudsætter, at boligen opfylder puljens krav, og at du har tilsagn, før du skriver under. Håndværkerfradrag kan ikke lægges oveni.", ["se_vp", "vpp_faq"]),
   ]),
  ],
  "faq": [
   ("Hvad koster en luft til vand-varmepumpe inkl. montering?", "SparEnergi angiver typisk 100.000-130.000 kr., og Energisparer.dk ca. 90.000-150.000 kr. Prisen afhænger af husets varmebehov og hvor meget ekstra arbejde der skal til.", ["se_vp", "es_vp"]),
   ("Hvad koster en varmepumpe til et hus på 150 m²?", "Energisparer.dk angiver som tommelfingerregel 110.000-135.000 kr. inkl. installation for et hus på 130-180 m² (8-12 kW). Effekten skal passe til husets varmetab, så bed installatøren om en beregning af varmebehovet.", ["es_l2v"]),
   ("Hvad koster en luft til vand-varmepumpe om året?", "Bolius regner med 9.386 kr. om året i varmeudgift for et 130 m² hus med radiatorer og 7.288 kr. med gulvvarme.", ["bolius_varme"]),
   ("Kan jeg få både tilskud og håndværkerfradrag?", "Nej, ikke for samme varmepumpe. SparEnergi skriver, at du ikke må få støtte fra andre offentlige ordninger, herunder det grønne håndværkerfradrag, når du får tilskud fra Varmepumpepuljen.", ["vpp_faq"]),
  ],
}
NATIONAL["/varmepumpe/tilskud/"] = {
  "svc": "varmepumpe", "crumb": "Tilskud", "updated": ("25. oktober 2026", "2026-10-25"),
  "kw": "varmepumpepuljen 2026 / varmepumpe tilskud",
  "evidence": "Autocomplete 'varmepumpepuljen': '2026', '2027', 'status', 'opbrugt', 'ansøgning', 'udbetaling'. 'varmepumpe tilskud': '2026', '2027', 'og håndværkerfradrag'. PAA: 'Er varmepumpepuljen 2026 opbrugt?', 'Hvornår kan man søge varmepumpepuljen?', 'Er varmepumpepuljen stadig åben?', 'Er der stadig midler i varmepumpepuljen?'. Også 'udfasning af gasfyr' og 'gasfyr til varmepumpe'.",
  "title": "Varmepumpepuljen 2026: status, krav og frist 30. november",
  "desc": "Varmepumpepuljen 2026 giver 27.000 kr. til luft til vand og jordvarme. Status 25/10: puljen er åben, lukker senest 30/11. Se de 5 krav og afkoblingspuljen.",
  "h1": "Varmepumpepuljen 2026: status, krav og frist",
  "intro": "Varmepumpepuljen giver 27.000 kr. til at skifte olie, gas, el eller biokedel ud med en luft til vand-varmepumpe eller jordvarme. Pengene er ved at slippe op, og puljens fremtid efter 2026 er uafklaret. Her er status, kravene og hvad det betyder lokalt.",
  "sections": [
   ("Status pr. 25. oktober 2026", [
     ("note", "<strong>Puljen er åben, men lukker senest mandag 30. november 2026</strong>, og tidligere, hvis pengene slipper op inden. Når der er søgt for alle midlerne, lukker SparEnergi ansøgningsportalen. Der er ingen garanti for en ny pulje i 2027, så vent ikke til sidste uge.", ["vpp_faq", "se_vpp", "vpp_tekniq"]),
     ("ul", [("SparEnergi skriver (siden er sidst opdateret 23. oktober 2026), at puljen er åben og lukker, når der er ansøgt for alle midlerne, dog senest 30. november 2026. Tilskud gives efter først til mølle.", ["se_vpp", "vpp_faq"]),
             ("Der var afsat 116,9 mio. kr. i 2026, og puljen fik tilført 200 mio. kr. ekstra. Ansøgningsvinduerne i 2026 er 5. februar-11. maj og 2. juli-30. november.", ["vpp_puljer"]),
             ("Det seneste offentlige beløb, vi har fundet, er fra TEKNIQ 13. oktober 2026: over 19.000 havde fået tilsagn for i alt 460 mio. kr., og der var <strong>knap 44 mio. kr. tilbage</strong>. Installatør bragte samme tal 14. oktober. Med 27.000 kr. pr. tilsagn svarede det til omkring 1.600 tilsagn mere (vores omregning). Der er søgt siden, så det reelle restbeløb er lavere.", ["vpp_tekniq", "installator"]),
             ("Regeringens finanslovsudspil for 2027 lægger op til at omprioritere de 185 mio. kr. om året, der var afsat til varmepumper i 2027-2029, til en bredere elektrificeringsramme. Det er derfor uvist, om der kommer en pulje i 2027.", ["vpp_tekniq"])]),
     ("p", "Status ændrer sig fra dag til dag. Tjek altid SparEnergi.dk, før du regner med tilskuddet. Vi har senest tjekket kilderne 25. oktober 2026.", ["se_vpp"]),
   ]),
   ("De 5 krav", [
     ("ul", [("Huset er en helårsbolig, og du ejer det selv.", ["se_vpp"]), ("Det opvarmes i dag med oliefyr, gasfyr, elvarme eller biokedel.", ["se_vpp"]),
             ("Det ligger <strong>ikke</strong> i et område med fjernvarme eller planlagt fjernvarme.", ["se_vpp"]),
             ("Du er ikke allerede i gang. Du må fx ikke have indgået en bindende aftale.", ["se_vpp"]), ("Du skifter til luft til vand eller jordvarme.", ["se_vpp"])]),
     ("p", "Tilskuddet er 27.000 kr. Er du momsregistreret og trækker momsen fra, er det 21.600 kr. Tilskuddet er skattefrit for private boligejere.", ["vpp_faq", "vpp_puljer"]),
     ("p", "En hyppig grund til afslag er forkerte oplysninger i BBR eller Plandata.dk. Plandata kan kun rettes af kommunen, så tjek dine oplysninger, før du søger.", ["vpp_faq"]),
   ]),
   ("Fra ansøgning til udbetaling", [
     ("ul", [("Du må gerne indhente tilbud før ansøgningen, men ikke indgå en bindende aftale eller gå i gang, før du har tilsagn.", ["vpp_ens", "vpp_faq"]),
             ("De fleste ansøgninger forventes at få svar inden for en uge. Sager, der behandles manuelt, kan tage op til 3 måneder.", ["vpp_puljer"]),
             ("Du skal søge om udbetaling senest 1 år efter tilsagnet og senest 30 dage efter, at varmepumpen er installeret. Behandlingen af udbetalingen kan tage op til 4 måneder.", ["vpp_faq"]),
             ("Du kan ikke få håndværkerfradrag for den samme varmepumpe, når du får tilskud.", ["vpp_faq"])]),
   ]),
   ("Hvor gælder puljen? Fjernvarmen i vores byer", [
     ("p", "Det afgørende krav er, at boligen ligger uden for fjernvarme og planlagt fjernvarme. Status er meget forskellig fra by til by, fx udbygger Vejle frem til 2028 og Verdo i fire byer ved Randers, mens Aalborg Kommune ikke ser mulighed for mere fjernvarme ud over Ajstrup. Se din by under <em>Fjernvarme eller varmepumpe</em> nedenfor.", ["vej_fv", "verdo_omr", "aal_fv"]),
   ]),
   ("Skifter du fra gas? Afkoblingspuljen 2026", [
     ("p", "Afkoblingspuljen dækker Evidas gebyr for at blive koblet af gasnettet, hvis du har et årligt gasforbrug på 100-6.000 m³. 2026-puljen er den sidste. Det er datoen for din opsigelse, der tæller, og midlerne fordeles efter først til mølle.", ["evida_afk"]),
   ]),
  ],
  "faq": [
   ("Er Varmepumpepuljen 2026 opbrugt?", "Ikke pr. 25. oktober 2026, hvor SparEnergi stadig skrev, at puljen er åben. 13. oktober var der ifølge TEKNIQ knap 44 mio. kr. tilbage. Puljen lukker, når midlerne er søgt, og senest 30. november 2026.", ["se_vpp", "vpp_tekniq", "vpp_faq"]),
   ("Hvornår lukker Varmepumpepuljen?", "Senest 30. november 2026, eller før, hvis der er ansøgt for alle midlerne.", ["vpp_faq"]),
   ("Kommer der en varmepumpepulje i 2027?", "Det er uvist. Regeringens finanslovsudspil for 2027 lægger op til at omprioritere de 185 mio. kr. om året, der var afsat til varmepumper i 2027-2029.", ["vpp_tekniq"]),
   ("Kan jeg få tilskud, hvis der kommer fjernvarme i mit område?", "Nej. Boligen må hverken ligge i et område med fjernvarme eller planlagt fjernvarme.", ["se_vpp"]),
   ("Hvor lang tid går der, før jeg får svar?", "De fleste forventes at få svar inden for en uge. Manuelle sager kan tage op til 3 måneder.", ["vpp_puljer"]),
  ],
}

# ---------- daglig by-rutine 27. okt. 2026: Næstved og Silkeborg ----------
# Forsyningstilsynet, prisstatistik januar 2026 (CSV), alle værker i de to kommuner, der indgår i statistikken
FV_PRICES["naestved"] = [("Næstved Fjernvarme", "4700", "16.745", "699"), ("Fensmark Fjernvarmeværk", "4684", "18.287", "750"), ("Fuglebjerg Fjernvarmeværk", "4250", "19.125", "625"), ("Sandved-Tornemark Kraftvarmeværk", "4262", "24.124", "962")]
FV_PRICES["silkeborg"] = [("Silkeborg Varme", "8600", "18.000", "800"), ("Kjellerup Fjernvarme", "8620", "16.615", "676"), ("Ans Fjernvarmeværk", "8643", "24.643", "1.090")]
SOL_REG["naestved"] = {
  "kw": "solceller næstved kommune / solceller byggetilladelse næstved",
  "evidence": "Næstved Kommunes byggeside har et selvstændigt afsnit 'Krav til opsætning af solcelleanlæg' (tjekket 27/10 2026), og to klagesager ved Planklagenævnet om solceller i Næstved (lokalplan 101 og 102) er offentliggjort.",
  "intro": "Næstved Kommune lader dig sætte solceller op uden ansøgning på enfamilie-, sommer- og dobbelthuse, så længe panelerne følger tagets hældning. Undtagelserne er få, men klare: fredning og bevaringsværdi, krav til tagets udseende i lokalplanen og fortidsminder. Her er reglerne og to klagesager fra kommunen.",
  "sections": [
   ("Uden ansøgning: fire betingelser", [
     ("ul", [("Anlægget <strong>følger tagets hældning</strong>, enten lagt oven på det eksisterende tag eller nedfældet i taget.", ["nae_byg"]),
             ("Du har selv tjekket tinglyste servitutter, lokalplaner og andre tinglyste dokumenter for forbud mod anlægget.", ["nae_byg"]),
             ("Du har selv tjekket, at de konstruktionsmæssige regler kan overholdes.", ["nae_byg"]),
             ("Du anmelder anlægget til BBR med oplysning om effekt og størrelse.", ["nae_byg"])]),
     ("note", "Reglen gælder for enfamiliehuse, sommerhuse og dobbelthuse. Andet byggeri kræver altid ansøgning om byggetilladelse.", ["nae_byg"]),
   ]),
   ("Her kræves altid byggetilladelse", [
     ("p", "Fredede og bevaringsværdige bygninger, ejendomme hvor plangrundlaget stiller <strong>krav til tagets udseende eller farve</strong>, og arealer eller bygninger inden for <strong>fortidsmindebeskyttelseslinjen</strong>. Fritstående anlæg, fx på jorden i haven, kræver også altid tilladelse.", ["nae_byg"]),
   ]),
   ("Det skal ansøgningen indeholde", [
     ("ul", [("En beskrivelse af anlægget: fabrikat og type, effekt i kW, antal paneler og areal i m².", ["nae_byg"]),
             ("En situationsplan med anlæggets afstand til skel og en facadetegning med højde over terræn og panelernes hældning.", ["nae_byg"]),
             ("Hvis anlægget står på stativ: en redegørelse for placeringen på tag eller jord. Desuden produktdatablad.", ["nae_byg"]),
             ("Ansøgningen sendes via Byg & Miljø. I 2024 var den gennemsnitlige sagsbehandlingstid for enfamiliehuse 41 kalenderdage.", ["nae_byg"])]),
   ]),
   ("To klagesager om solceller i Næstved", [
     ("p", "<strong>Lokalplan nr. 101:</strong> Næstved Kommune gav i marts 2024 afslag på dispensation til solceller, der lå 8-10 cm over betontagstenene, fordi kommunen læste lokalplanen som et krav om nedfældning. Planklagenævnet ophævede afslaget: solcellerne flugtede med tagets geometri og stod ikke på stativ, så der krævedes ingen dispensation.", ["nae_pkn101"]),
     ("p", "<strong>Lokalplan nr. 102 (Appenæs):</strong> Lokalplanen forbyder solcellepaneler og kræver røde vingetegl. Planklagenævnet stadfæstede i februar 2026 kommunens afslag på solcelletagsten i stedet for et stråtag, fordi solcelletagsten også er omfattet af forbuddet.", ["nae_pkn102"]),
     ("note", "Læs din lokalplans præcise ordlyd, før du bestiller. Det er ordlyden, der afgør, om du skal søge.", ["nae_pkn101"]),
   ]),
  ],
  "faq": [
   ("Kræver solceller byggetilladelse i Næstved Kommune?", "Ikke på enfamilie-, sommer- og dobbelthuse, når anlægget følger tagets hældning, og servitutter og lokalplan tillader det. Fredede og bevaringsværdige bygninger, tage med krav til udseende eller farve og arealer ved fortidsminder kræver altid tilladelse.", ["nae_byg"]),
   ("Må jeg sætte solceller på jorden i haven i Næstved?", "Kun med byggetilladelse. Næstved Kommune skriver, at fritstående anlæg altid kræver ansøgning. Ansøgningen skal bl.a. have en situationsplan med afstand til skel og en redegørelse for stativet.", ["nae_byg"]),
   ("Må solcellerne ligge oven på tagstenene, hvis lokalplanen siger, de skal flugte taget?", "I en klagesag om lokalplan nr. 101 i Næstved fandt Planklagenævnet, at solceller 8-10 cm over betontagstenene flugtede med tagets geometri, fordi de ikke stod på stativ. Det afhænger dog af ordlyden i netop din lokalplan.", ["nae_pkn101"]),
   ("Hvem kontakter jeg om solceller i Næstved Kommune?", "Center for Teknik og Miljø på 55 88 61 10 eller byggesag@naestved.dk. Du kan også bestille tid til et møde med Byggesag via kommunens hjemmeside.", ["nae_byg"]),
  ],
}
SOL_REG["silkeborg"] = {
  "kw": "solceller silkeborg kommune / byggetilladelse solceller silkeborg",
  "evidence": "Silkeborg Kommunes side 'Ansøg om byggetilladelse' har et selvstændigt afsnit 'Skal jeg ansøge om opsætning af solceller?' med regler, gebyr og BBR (tjekket 27/10 2026).",
  "intro": "Silkeborg Kommune lister præcis, hvornår solceller kræver byggetilladelse, og tager 700 kr. i timen for at behandle sagen. For de fleste parcelhuse er det lokalplanen, der afgør det. Her er de fire tilfælde, gebyret, sagsbehandlingstiden og et eksempel fra Planklagenævnet.",
  "sections": [
   ("De fire tilfælde, der kræver byggetilladelse", [
     ("ul", [("Anlægget sættes op på <strong>terræn</strong>.", ["sil_byg"]),
             ("Anlægget sættes på bygninger som erhvervsbygninger, skoler, ridehaller og etageboliger, der ikke er undtaget i bygningsreglementet.", ["sil_byg"]),
             ("Anlægget er placeret <strong>for højt i forhold til afstanden til naboskel</strong>. For parcel-, række- og dobbelthuse gælder bl.a. 2,5 meter til skel.", ["sil_byg", "br18_179"]),
             ("Opsætningen kræver en <strong>ændring af tagkonstruktionen</strong>, fx fordi lasten øges. Det bør en rådgiver vurdere.", ["sil_byg"])]),
   ]),
   ("Lokalplan, byplanvedtægt og servitutter", [
     ("p", "Silkeborg Kommune beder dig undersøge, om ejendommen er omfattet af en lokalplan, byplanvedtægt eller tinglyste servitutter med bestemmelser om materialer og udseende af tagbeklædningen. Er den det, skal du søge dispensation. Planerne finder du på Silkeborglokalplaner.dk.", ["sil_byg"]),
     ("example", "Eksempel: Lokalplan nr. 132.20 for boligområdet ved Øster Bordingvej siger, at solceller kun må sættes op med tilladelse i hvert enkelt tilfælde, og at de ikke må give blændingsgener. Kommunen gav dispensation til et anlæg i 2022, og Planklagenævnet gav ikke naboen medhold i klagen.", ["sil_pkn"]),
   ]),
   ("Gebyr og sagsbehandlingstid i 2026", [
     ("ul", [("Fra 1. januar 2026 er gebyret <strong>700 kr. pr. time</strong>. Det gælder også forespørgsler, forhåndsdialoger og telefonopkald om konkrete sager. Søger du solceller sammen med et nyt hus, er der intet særskilt gebyr.", ["sil_byg"]),
             ("Kommunen oplyser en forøget sagsbehandlingstid på ca. <strong>12-14 uger</strong> for enfamiliehuse, sommerhuse og rækkehuse på grund af ekstraordinært mange ansøgninger. Servicemålet er 40 dage.", ["sil_byg"]),
             ("Du søger via Byg og Miljø og kan booke en samtale på 20 minutter med en byggesagsbehandler, før du sender.", ["sil_byg"])]),
   ]),
   ("BBR", [
     ("p", "Silkeborg Kommune skriver, at <strong>solfangere</strong> (vandbaserede anlæg) altid skal anmeldes til BBR med adresse og areal. Du retter selv BBR-oplysningerne på bbr.dk.", ["sil_byg"]),
   ]),
  ],
  "faq": [
   ("Skal jeg søge byggetilladelse til solceller på mit hus i Silkeborg?", "Kun hvis anlægget står på terræn, står for højt i forhold til naboskel eller kræver ændring af tagkonstruktionen. Anlæg på bygninger som skoler, erhverv og etageboliger kræver også tilladelse. Tjek desuden lokalplan og servitutter på Silkeborglokalplaner.dk.", ["sil_byg"]),
   ("Hvad koster det at søge om solceller i Silkeborg Kommune?", "Fra 1. januar 2026 opkræver Silkeborg Kommune 700 kr. pr. time for byggesagsbehandling, også for solceller på et eksisterende hus og for anlæg på terræn. Gebyret opkræves i to rater. Søger du sammen med et nyt hus, er der intet særskilt gebyr for solcellerne.", ["sil_byg"]),
   ("Hvor lang tid tager en byggetilladelse til solceller i Silkeborg?", "Kommunen oplyser lige nu ca. 12-14 uger for enfamiliehuse og lignende på grund af mange ansøgninger. Det nationale servicemål er 40 dage. Mangler ansøgningen oplysninger, bliver det længere.", ["sil_byg"]),
   ("Hvem kontakter jeg om solceller i Silkeborg Kommune?", "Team Byg i Teknik- og Miljøafdelingen på 89 70 14 14 eller byg@silkeborg.dk.", ["sil_byg"]),
  ],
}
FV_PAGE["naestved"] = {
  "kw": "fjernvarme næstved / næstved fjernvarme pris / varmepumpe næstved",
  "evidence": "Næstved Kommune har en egen spørgsmål og svar-side om fjernvarme, og Næstved Fjernvarme offentliggør ugentligt tilslutningsprocenten for Holsted Nord (tjekket 27/10 2026).",
  "intro": "I Næstved Kommune har under en tredjedel af husene fjernvarme, og knap lige så mange har naturgas. Flere udbygninger i Næstved by er faldet, fordi for få tilmeldte sig, og Holsted Nord har frist 30. november 2026. Her er status, de fire værkers priser og regnestykket mod en varmepumpe.",
  "status": [
   ("Næstved Kommunes status for Varmeplan 2022-2030: fjernvarme er godkendt i <strong>Næstved by, Glumsø og Karrebæk</strong>. I Fensmark er den godkendt i den sydlige del, mens to gasområder er under afklaring. I <strong>Mogenstrup</strong> kan det ikke lade sig gøre.", ["nae_fv"]),
   ("<strong>Holsted Vest</strong> (ca. 1.300 ejendomme) nåede 51 % tilmelding og <strong>Holsted Syd</strong> (ca. 270 ejendomsejere) 13 %. Begge projekter er droppet, fordi kravet er 60 % målt pr. kvadratmeter.", ["nae_vest", "nae_syd"]),
   ("I <strong>Holsted Nord</strong> (område 50), det sidste område i Næstved Fjernvarmes masterplan, var tilslutningen 8 % den 21. oktober 2026. Fristen er 30. november 2026.", ["nae_nord", "nae_syd"]),
   ("I Lille Næstved Nord nåede de to områder 35 % og 43 % og fik ikke fjernvarme. Kun Fodbygårdsvej, Marie Bregendahls Vej og Leif Panduros Vej (95 ejendomme) i den vestlige del af Lille Næstved nåede 60 %.", ["nae_lnn"]),
  ],
  "local_take": "Næstved Fjernvarme ligger lige under landsgennemsnittet, mens Sandved-Tornemark hører til de 10 % dyreste værker i landet. Har du fjernvarme, er der sjældent penge i at skifte. Har du gasfyr i et af de opgivne Holsted-områder eller i Mogenstrup, kommer fjernvarmen ikke foreløbig, og en luft til vand-varmepumpe med tilskud er det oplagte alternativ. Bor du i Holsted Nord, så vent på udfaldet efter 30. november.",
  "contact": ("Næstved Fjernvarme", "55 72 56 65 · info@naestvedfjernvarme.dk (man-tors kl. 9-15, fre kl. 9-13)", "nae_nord"),
  "faq": [
   ("Hvad koster fjernvarme i Næstved?", "Hos Næstved Fjernvarme koster et standardhus på 130 m² med 18,1 MWh 16.745 kr. om året inkl. moms ifølge Forsyningstilsynets statistik pr. 31. januar 2026. Fensmark ligger på 18.287 kr., Fuglebjerg på 19.125 kr. og Sandved-Tornemark på 24.124 kr. Landsgennemsnittet er 16.953 kr.", ["ft_pris"]),
   ("Hvor kommer fjernvarmen i Næstved fra?", "Næstved Fjernvarme oplyser, at ca. 87 % af varmen kommer fra affaldsforbrænding, og at planen er 99,5 % fra vedvarende energikilder i 2028. Affaldsvarmen har værket fået fra det fælleskommunale anlæg, i dag AffaldPlus, siden 1983.", ["nae_om"]),
   ("Hvor lang tid går der, fra fjernvarme er godkendt, til jeg kan blive tilsluttet?", "Næstved Kommune skriver, at fjernvarmeselskabet har 5 år fra godkendelsen til at nå frem til den sidste ejendom i området. Du skal selv tilmelde dig hos selskabet.", ["nae_fv"]),
  ],
}
FV_PAGE["silkeborg"] = {
  "kw": "fjernvarme silkeborg / silkeborg forsyning fjernvarme / varmepumpe silkeborg",
  "evidence": "Silkeborg Forsyning har projektsider for Silkeborg Syd, Voel og andre nye områder samt en spørgsmål og svar-side om fjernvarme (tjekket 27/10 2026).",
  "intro": "Silkeborg Forsyning er i gang med at lægge fjernvarme ud til Virklund, Sejs-Svejbæk, Them, Salten og Voel, og et nyt varmepumpe- og biomasseanlæg blev indviet i september 2026. Hvert femte hus i kommunen har stadig naturgas. Her er status, priserne og hvornår en varmepumpe giver mening.",
  "status": [
   ("<strong>Silkeborg Syd</strong> (Virklund, Sejs-Svejbæk, Them og Salten): projektet blev sendt i EU-udbud med frist til slutningen af august 2026. Gravearbejdet i byerne forventes at begynde i slutningen af 2026, og alt ventes færdigt i første halvår af 2029. Omkring 2.500 husstande har tilmeldt sig.", ["sil_syd", "sil_voel"]),
   ("<strong>Voel</strong> nåede 59 % tilslutning i februar 2026 (målet var 55 %). Gravearbejdet forventes at begynde i andet halvår af 2026 og vare ca. to år.", ["sil_voel"]),
   ("<strong>Resenbro og Skærbæk</strong> sagde ja med 68 % i august 2024 og er under etablering. I Høje Kejlstrup kørte der tilmeldingskampagne i 2025/2026. Knudlund er udgået af Silkeborg Syd på grund af lav tilmelding.", ["sil_faq"]),
   ("Bor du i et projektområde, kan du ikke få tilskud fra Varmepumpepuljen, fordi fjernvarmen er planlagt.", ["se_vpp"]),
  ],
  "local_take": "Silkeborg Varme ligger lidt over landsgennemsnittet, Kjellerup lidt under, og Ans hører til de 10 % dyreste værker i landet. Har du gasfyr i Silkeborg Syd eller Voel, er fjernvarmen på vej, og kampagneprisen gælder kun, til gravemaskinerne er forbi din adresse. Ligger du uden for projekterne, fx i en landsby med oliefyr, er en luft til vand-varmepumpe med tilskud det oplagte valg.",
  "contact": ("Silkeborg Forsyning", "89 20 64 00 · Tietgensvej 3, 8600 Silkeborg", "sil_kontakt"),
  "faq": [
   ("Hvad koster fjernvarme i Silkeborg?", "Hos Silkeborg Varme koster et standardhus på 130 m² med 18,1 MWh 18.000 kr. om året inkl. moms ifølge Forsyningstilsynets statistik pr. 31. januar 2026. Kjellerup Fjernvarme ligger på 16.615 kr. og Ans Fjernvarmeværk på 24.643 kr. Landsgennemsnittet er 16.953 kr.", ["ft_pris"]),
   ("Hvor kommer fjernvarmen i Silkeborg fra?", "Fra bl.a. biomasse, solvarme, varmepumper og kraftvarme. Solvarmeanlægget på Sejling Hede, der kom i drift i slutningen af 2016, dækker ca. 20 % af varmebehovet i Silkeborg, og i september 2026 blev et nyt varmepumpeanlæg og et biomasseanlæg til have- og parkaffald indviet.", ["sil_faq", "sil_df"]),
   ("Hvad sparer jeg ved at tilmelde mig fjernvarme i Voel til kampagnepris?", "Silkeborg Forsyning skriver, at kampagneprisen i Voel sparer 19.800 kr., og at tilbuddet bortfalder, når gravemaskinerne har gravet forbi ejendommen.", ["sil_voel"]),
  ],
}

# ---------- daglig by-rutine 28. okt. 2026: Holbæk og Slagelse ----------
# Forsyningstilsynet, prisstatistik januar 2026 (CSV): værker i de to kommuner (navne og postnr. som i statistikken)
FV_PRICES["holbaek"] = [("Mørkøv Varmeværk", "4440", "17.411", "533"), ("FORS Varme Holbæk, Jyderup", "4300", "20.181", "793"), ("FORS Varme Holbæk St. Merløse", "4370", "22.751", "935"), ("Fors Varme Holbæk Have", "4300", "23.070", "952")]
FV_PRICES["slagelse"] = [("Hashøj Kraftvarmeforsyning", "4261", "14.505", "437"), ("SK Varme", "4200", "18.283", "671")]
SOL_REG["holbaek"] = {
  "kw": "solceller holbæk kommune / byggetilladelse solceller holbæk",
  "evidence": "Holbæk Kommune har en selvstændig side om solcelle- og solfangeranlæg (opdateret 5/7 2026) og vedtog i 2011 retningslinjer for dispensation til solceller fra lokalplaner. En klagesag ved Planklagenævnet om solceller i Holbæk er offentliggjort.",
  "intro": "Holbæk Kommune skelner skarpt: solceller, der følger tagets hældning, kræver som udgangspunkt ikke byggetilladelse, mens anlæg på stativ eller på jorden altid gør. Lokalplaner om tagets udseende kan kræve dispensation. Her er reglerne, kommunens retningslinjer og en klagesag fra Holbæk.",
  "sections": [
   ("Uden byggetilladelse: panelerne følger taget", [
     ("ul", [("Anlægget sidder på taget af en <strong>privat bolig eller sekundær bygning</strong> og følger tagets hældning.", ["hol_sol"]),
             ("Du har tjekket byplanvedtægt, lokalplan, tinglyste deklarationer, grundejerforeningens vedtægter, fredning, bevaringsværdi og beskyttelseslinjer efter naturbeskyttelsesloven.", ["hol_sol"]),
             ("Panelerne giver ikke generende refleksioner hos naboerne.", ["hol_sol"]),
             ("Du sender antal paneler, areal i m² og ydelse i kW til byggesag@holb.dk til registrering i BBR.", ["hol_sol"])]),
   ]),
   ("Her kræves altid byggetilladelse", [
     ("p", "Anlæg på <strong>stativ på taget</strong> og anlæg <strong>på jorden</strong>, som kommunen regner for tekniske anlæg. I landzone skal et jordanlæg også have landzonetilladelse. På driftsbygninger kan det kræve tilladelse, selv om anlægget flugter med taget, afhængigt af størrelsen og om produktionen væsentligt overstiger eget forbrug. På visse bygninger kræves også tilladelse, hvis lasten på konstruktionen stiger mere end 5 %.", ["hol_sol"]),
   ]),
   ("Dispensation fra lokalplanen", [
     ("p", "Mange lokalplaner i Holbæk kræver matte tegl eller forbyder blanke og reflekterende materialer. Udvalget for Klima og Miljø besluttede i 2011, at kommunen kan dispensere fra den slags krav og fra arealgrænser efter en konkret vurdering og naboorientering, evt. på betingelse af antirefleksbehandlede paneler.", ["hol_disp"]),
     ("example", "Eksempel: Holbæk Kommune afslog i november 2022 27 m² solceller integreret i taget på et bevaringsværdigt hus i lokalplan nr. 3.14, der kræver røde tegltagsten. Planklagenævnet ophævede afslaget, fordi kommunen fejlagtigt mente, at den slet ikke kunne dispensere, og sendte sagen tilbage til ny behandling.", ["hol_pkn"]),
   ]),
   ("Solceller på jorden i landzone", [
     ("p", "Holbæk Kommune giver normalt landzonetilladelse til mindre solcelleanlæg til privat brug, når de står i tilknytning til de eksisterende bygninger på egen ejendom og ikke er skæmmende eller til gene for naboer. Kommunen kan stille krav om afskærmende beplantning.", ["hol_sol"]),
   ]),
  ],
  "faq": [
   ("Kræver solceller byggetilladelse i Holbæk Kommune?", "Ikke som udgangspunkt, hvis de følger tagets hældning på en privat bolig eller sekundær bygning. Anlæg på stativ på taget og anlæg på jorden kræver altid byggetilladelse, som du søger via Byg og Miljø.", ["hol_sol"]),
   ("Må jeg sætte solceller op, hvis lokalplanen kræver matte tegl?", "Det kræver dispensation. Holbæk Kommune kan efter retningslinjer fra 2011 dispensere fra krav om matte eller ikke-reflekterende tagmaterialer efter en konkret vurdering og naboorientering, evt. mod at panelerne er antirefleksbehandlede.", ["hol_disp"]),
   ("Kan jeg få solceller på et bevaringsværdigt hus i Holbæk?", "Det kræver en konkret vurdering. I en sag om lokalplan nr. 3.14 fandt Planklagenævnet, at kommunen godt kunne dispensere fra kravet om røde tegltagsten, og sendte et afslag tilbage til ny behandling.", ["hol_pkn"]),
   ("Hvem kontakter jeg om solceller i Holbæk Kommune?", "Byggesag på byggesag@holb.dk eller kommunens hovednummer 72 36 36 36. Ansøgninger og dispensationer søges via Byg og Miljø.", ["hol_sol"]),
  ],
}
SOL_REG["slagelse"] = {
  "kw": "solceller slagelse kommune / byggetilladelse solceller slagelse",
  "evidence": "Slagelse Kommune har en side om solcelleanlæg og et administrationsgrundlag for solfangere og solcelleanlæg (rev. 19/9 2022) med regler for lokalplaner, bevarende lokalplaner og landzone (tjekket 28/10 2026).",
  "intro": "Slagelse Kommune har sit eget administrationsgrundlag for solceller. Uden lokalplan er det byggeretten i bygningsreglementet, der afgør, om du skal søge. Med lokalplan eller i de bevarende bykerner kræver det ofte dispensation. Her er reglerne, SAVE-vurderingerne og hvordan du søger.",
  "sections": [
   ("Uden lokalplan: byggeretten afgør det", [
     ("ul", [("På et tag i by- eller landzone uden lokalplan skal du ikke søge, hvis anlægget <strong>overholder byggeretten</strong> i BR18 kap. 8, bl.a. kravet om mindst 2,5 meter til skel.", ["slg_adm", "br18_179"]),
             ("Du skal selv sikre, at ingen tinglyst deklaration forhindrer anlægget, og at de konstruktive krav overholdes.", ["slg_adm"]),
             ("I sommerhusområder gælder samme princip, men skelafstanden er mindst 5 meter.", ["slg_adm"]),
             ("Anlægget skal indberettes til BBR, når det er sat op. Har det krævet byggetilladelse, sker det automatisk.", ["slg_adm", "slg_sol"])]),
   ]),
   ("Lokalplaner med krav til taget", [
     ("p", "Står der kun, at <strong>blanke eller reflekterende tagmaterialer</strong> ikke må bruges, vurderer kommunen ikke, at solceller i sig selv strider mod det, men ser på størrelse, omfang og taghældning i forhold til naboerne, normalt efter naboorientering. Kræver lokalplanen en <strong>bestemt tagdækning</strong>, fx røde teglsten, skal du søge dispensation.", ["slg_adm"]),
     ("note", "Kommunen vil have anlægget placeret symmetrisk, så tagmaterialet kan ses hele vejen rundt om det. Flere mindre felter vurderes normalt pænere end én stor flade.", ["slg_adm"]),
   ]),
   ("Bevarende lokalplaner og SAVE-værdier", [
     ("ul", [("<strong>SAVE 1-2:</strong> bygningen er fredet eller særligt bevaringsværdig, og dispensation kan normalt ikke komme på tale.", ["slg_adm"]),
             ("<strong>SAVE 3-4:</strong> kræver en helt særskilt konkret vurdering, og anlægget skal gribe mindst muligt ind i arkitekturen.", ["slg_adm"]),
             ("<strong>SAVE 5-10:</strong> der skal tages hensyn til bevaringsområdet, og der kan evt. dispenseres på visse betingelser, fx placering mod gårdrummet.", ["slg_adm"])]),
   ]),
   ("Terræn, strand og skov", [
     ("ul", [("Anlæg på terræn i <strong>landzone</strong> kræver altid landzonetilladelse.", ["slg_adm"]),
             ("Inden for <strong>strandbeskyttelseslinjen</strong> kræver det tilladelse eller dispensation efter naturbeskyttelsesloven.", ["slg_adm"]),
             ("Inden for <strong>skovbyggelinjen</strong> afgøres det konkret, om der skal dispenseres.", ["slg_adm"])]),
   ]),
   ("Sådan søger du", [
     ("p", "Byggetilladelse søges på Byg og Miljø med målfast situationsplan med afstand til skel, plan og snit med målsatte højder og en beskrivelse af anlægget. Dispensation fra en lokalplan søges på teknik@slagelse.dk. Regn med mindst 6 ugers sagsbehandling.", ["slg_adm"]),
   ]),
  ],
  "faq": [
   ("Kræver solceller byggetilladelse i Slagelse Kommune?", "Ikke på et tag uden lokalplan, hvis anlægget overholder byggeretten i bygningsreglementet og ingen deklaration forbyder det. Kræver lokalplanen en bestemt tagdækning, eller overholdes byggeretten ikke, skal du søge.", ["slg_adm"]),
   ("Kan jeg få solceller på et hus i Skælskørs eller Korsørs gamle bydel?", "Det afhænger af bygningens SAVE-værdi og den bevarende lokalplan. Ved SAVE 1-2 kan der normalt ikke dispenseres, ved SAVE 3-10 vurderer kommunen hver sag konkret.", ["slg_adm"]),
   ("Må jeg sætte solceller på jorden i haven i Slagelse?", "I byzone uden lokalplan ja, hvis byggeretten er overholdt, herunder 2,5 meter til skel. I landzone kræver alle anlæg på terræn landzonetilladelse.", ["slg_adm"]),
   ("Hvem kontakter jeg om solceller i Slagelse Kommune?", "Byggeri i Slagelse Kommune på 58 57 37 37 eller teknik@slagelse.dk. Spørgsmål om dispensation fra lokalplaner sendes også til teknik@slagelse.dk.", ["slg_byg", "slg_adm"]),
  ],
}
FV_PAGE["holbaek"] = {
  "kw": "fjernvarme holbæk / fors fjernvarme holbæk / varmepumpe holbæk",
  "evidence": "Holbæk Kommune har en side om fjernvarmeplaner (opdateret 25/3 2026), og Fors offentliggør tilslutningsprocenten for etape 1 i Holbæk by (senest 4/8 2026).",
  "intro": "I Holbæk Kommune har under hvert tiende hus fjernvarme, langt den laveste andel på dette site. Fjernvarmen til Holbæk by venter på flere tilmeldinger frem til 1. maj 2027, og der er ingen planer om nye områder. Her er status, de fire værkers priser og regnestykket mod en varmepumpe.",
  "status": [
   ("<strong>Holbæk by, etape 1</strong> blev godkendt i marts 2024, men gennemføres kun, hvis mindst 70 % af varmegrundlaget (m²) tilmelder sig. Tilslutningen var 12,09 % den 4. august 2026.", ["hol_fv", "fors_hol"]),
   ("Kommunalbestyrelsen besluttede 17. juni 2026 at forlænge arbejdet til <strong>1. maj 2027</strong> med fokus på boligselskaber, Holbæk Sygehus og andre store varmeforbrugere.", ["hol_ext", "fors_hol"]),
   ("I <strong>Jyderup</strong> godkendte kommunen i november 2023 et anlæg med eldreven varmepumpe og solpaneler. I <strong>Mørkøv</strong> er der fjernvarme, og ledningsnettet udvides. I <strong>St. Merløse</strong> er der fjernvarme i dele af byen.", ["hol_fv"]),
   ("Holbæk Kommune skriver, at der ikke er planer om flere muligheder for fjernvarme i kommunen.", ["hol_fv"]),
  ],
  "local_take": "Mørkøv Varmeværk ligger lidt over landsgennemsnittet, mens Fors Varme Holbæk Have hører til de 10 % dyreste værker i landet. Har du gasfyr uden for de fire fjernvarmebyer, kommer fjernvarmen ikke, og en luft til vand-varmepumpe med tilskud er det oplagte valg. Bor du i etape 1 i Holbæk by, afgøres projektet senest 1. maj 2027.",
  "contact": ("Holbæk Kommune", "72 36 36 36 · Kanalstræde 2, 4300 Holbæk", "hol_fv"),
  "faq": [
   ("Hvad koster fjernvarme i Holbæk?", "Ifølge Forsyningstilsynets statistik pr. 31. januar 2026 koster et standardhus på 130 m² med 18,1 MWh 23.070 kr. om året inkl. moms hos Fors Varme Holbæk Have, 20.181 kr. hos Fors i Jyderup, 22.751 kr. i St. Merløse og 17.411 kr. hos Mørkøv Varmeværk. Landsgennemsnittet er 16.953 kr.", ["ft_pris"]),
   ("Hvor kommer fjernvarmen i Holbæk Kommune fra?", "Holbæk Kommune skriver, at fjernvarmen primært kommer fra eldrevne varmepumper. Fjernvarmen til Holbæk by skal komme fra et stort varmepumpeanlæg ved Omfartsvejen, kaldet Energibyen.", ["hol_fv"]),
   ("Hvad koster det at blive tilsluttet fjernvarme i Holbæk by?", "Fors skriver, at tilslutning koster 25.000 kr. til kampagnepris, indtil gravemaskinerne har været forbi huset, og derefter 50.000 kr. Projektet gennemføres kun, hvis 70 % af varmegrundlaget tilmelder sig.", ["fors_hol"]),
  ],
}
FV_PAGE["slagelse"] = {
  "kw": "fjernvarme slagelse / envafors fjernvarme / varmepumpe slagelse",
  "evidence": "Slagelse Kommune har en statusside om fjernvarme for hvert lokalområde, og Envafors beskriver varmeproduktionen i Slagelse og Korsør (tjekket 28/10 2026).",
  "intro": "I Slagelse Kommune bliver fjernvarmen udbygget i Slagelse by, mens projekterne i Skælskør, Vemmelev og Forlev er annulleret. Knap hvert tredje hus har fjernvarme, og næsten lige så mange har naturgas. Her er status by for by, priserne og regnestykket mod en varmepumpe.",
  "status": [
   ("<strong>Slagelse NV</strong> er udrullet i 2025, og nye kunder kan stadig koble sig på. <strong>Slagelse SV</strong> nåede 61 % tilslutning og bliver realiseret.", ["slg_fv"]),
   ("<strong>Slagelse Øst</strong> (øst for Klosterbanken) er planlagt til 2027 og kræver 60 % tilslutning. De gasforsynede områder i den nordøstlige del af byen kan først få fjernvarme omkring 2029/30.", ["slg_fv"]),
   ("På <strong>Halsskov</strong> er fjernvarmen udrullet. For <strong>Svenstrup</strong> ventes en endelig afgørelse i 2029/30, dog ikke for husene langs Stibjergvej.", ["slg_fv"]),
   ("Projekterne i det centrale <strong>Skælskør</strong> (maj 2025) og i <strong>Vemmelev og Forlev</strong> (august 2025) er annulleret. I Slots Bjergby afventer udrulningen, fordi prisen fortsat er høj.", ["slg_fv"]),
  ],
  "local_take": "Hashøj Kraftvarmeforsyning i Dalmose hører til de 20 % billigste værker i landet, mens SK Varme ligger ca. 1.300 kr. over landsgennemsnittet for et standardhus. Bor du i Slagelse SV eller Øst, er fjernvarmen tæt på. I Skælskør, Vemmelev, Forlev og Sørbymagle er projekterne droppet, og en luft til vand-varmepumpe med tilskud er det oplagte valg.",
  "contact": ("Envafors", "58 36 25 00 · kontakt@envafors.dk (man-tors kl. 8-17, fre kl. 8-13)", "env_ve"),
  "faq": [
   ("Hvad koster fjernvarme i Slagelse?", "Hos SK Varme koster et standardhus på 130 m² med 18,1 MWh 18.283 kr. om året inkl. moms ifølge Forsyningstilsynets statistik pr. 31. januar 2026. Hashøj Kraftvarmeforsyning i Dalmose ligger på 14.505 kr. Landsgennemsnittet er 16.953 kr.", ["ft_pris"]),
   ("Hvor kommer fjernvarmen i Slagelse og Korsør fra?", "Envafors skriver, at fjernvarmen primært produceres på halm og flis samt solvarme, og at flere store varmepumper i Slagelse og Korsør leverer en voksende del. Omkring 95 % af varmen er baseret på vedvarende energi.", ["env_ve"]),
   ("Hvornår kommer der fjernvarme i det nordøstlige Slagelse?", "Ifølge Slagelse Kommune oplyser Envafors, at de gasforsynede områder i den nordøstlige del af Slagelse by først kan få fjernvarme omkring 2029/30, fordi det kræver et større forsyningsrør.", ["slg_fv"]),
  ],
}

# ---------- daglig by-rutine 29. okt. 2026: Roskilde og Sønderborg ----------
# Forsyningstilsynet, prisstatistik januar 2026 (CSV): værker i de to kommuner (navne og postnr. som i statistikken)
FV_PRICES["roskilde"] = [("Svogerslev Fjernvarmecentral", "4000", "14.575", "735"), ("Fors Varme Roskilde A/S", "4000", "18.367", "704")]
FV_PRICES["soenderborg"] = [("Sønderborg Varme A/S", "6400", "14.760", "580"), ("SONFOR Varme A/S", "6400", "23.694", "845")]
SOL_REG["roskilde"] = {
  "kw": "solceller roskilde kommune / byggetilladelse solceller roskilde",
  "evidence": "Roskilde Kommune beskriver reglerne for solceller og solfangere på enfamiliehuse på sin byggeside, solcelleanlæg på terræn i Landzonestrategien (2021) og større anlæg på en særskilt side (opdateret 26/5 2026).",
  "intro": "Roskilde Kommune kræver som udgangspunkt ingen tilladelse til solceller på det eksisterende tag på et enfamiliehus. Det er bygningsreglementets højde- og afstandsregler, lokalplanen og bevaringshensyn, der sætter grænserne. Her er reglerne, kravene til anlæg på jorden i landzone og hvordan du søger.",
  "sections": [
   ("På taget af et enfamiliehus", [
     ("ul", [("Solceller og solfangere på det <strong>eksisterende bygningstag</strong> kræver som udgangspunkt ikke tilladelse efter byggeloven.", ["ros_byg"]),
             ("Anlægget skal overholde bygningsreglementets regler om <strong>højde og afstand</strong>, bl.a. til skel.", ["ros_byg", "br18_179"]),
             ("Solceller og solfangere behandles ens: de samme regler gælder for begge.", ["ros_byg"]),
             ("Anlæg på <strong>erhvervsbygninger</strong> kræver altid byggetilladelse.", ["ros_byg"])]),
   ]),
   ("Tjek dette, før du bestiller", [
     ("p", "Roskilde Kommune beder dig gennemgå fire ting: bestemmelser i en eventuel <strong>lokalplan</strong>, <strong>tinglyste deklarationer</strong>, regler om <strong>fredning eller bevaring</strong> af bygningen og regler om <strong>naturbeskyttelse</strong>. Rammer en af dem dit hus, kan anlægget kræve tilladelse eller dispensation efter anden lovgivning.", ["ros_byg"]),
   ]),
   ("Solceller på terræn i landzone", [
     ("p", "Et mindre solcelleanlæg på jorden i landzone kræver landzonetilladelse, og større anlæg kan udløse lokalplanpligt. Kommunen lægger især vægt på, at anlægget ikke påvirker landskab, udsigter, natur eller kulturmiljøer negativt, ikke er til gene for naboer, er visuelt afskærmet og ligger i tilknytning til ejendommens øvrige bebyggelse.", ["ros_lz"]),
     ("note", "Anlæg på over 1 hektar kræver lokalplan, kommuneplantillæg og miljøvurdering, og ansøgningerne behandles i to runder om året med frist 1. marts og 1. september. Det er for solcelleparker, ikke for et anlæg i haven.", ["ros_ve"]),
   ]),
   ("Sådan søger du", [
     ("p", "Kræver anlægget tilladelse, søger du via Byg & Miljø. Skal du have dispensation fra en lokalplan, vedlægger du en dispensationsansøgning med begrundelse og ejers underskrift, og facadetegningerne skal vise eventuelle solcelleanlæg.", ["ros_tjek"]),
   ]),
  ],
  "faq": [
   ("Kræver solceller byggetilladelse i Roskilde Kommune?", "Ikke som udgangspunkt på det eksisterende tag på et enfamiliehus, hvis højde- og afstandsreglerne i bygningsreglementet overholdes. På erhvervsbygninger kræver det altid byggetilladelse, og lokalplan, deklarationer og bevaring kan kræve dispensation.", ["ros_byg"]),
   ("Hvad lægger Roskilde Kommune vægt på ved solceller på jorden i landzone?", "At anlægget ikke påvirker landskab, udsigter, natur eller kulturmiljøer negativt, ikke generer naboerne, er visuelt afskærmet og ligger i tilknytning til ejendommens øvrige bebyggelse. Det fremgår af kommunens landzonestrategi.", ["ros_lz"]),
   ("Hvad skal jeg vedlægge, hvis jeg skal have dispensation til solceller i Roskilde?", "En dispensationsansøgning med begrundelse og ejers underskrift, som sendes sammen med ansøgningen i Byg & Miljø. Facadetegningerne skal vise solcelleanlægget.", ["ros_tjek"]),
   ("Hvem kontakter jeg om solceller i Roskilde Kommune?", "Byggesag i Roskilde Kommune på byggesag@roskilde.dk eller kommunens hovednummer 46 31 30 00.", ["ros_varme"]),
  ],
}
SOL_REG["soenderborg"] = {
  "kw": "solceller sønderborg kommune / tilladelse solceller sønderborg",
  "evidence": "Sønderborg Kommune beskriver på sin side om varmekilder og energi, hvornår solceller kræver tilladelse, hvilke korttemaer man skal tjekke, og hvad en ansøgning skal indeholde (tjekket 29/10 2026).",
  "intro": "Sønderborg Kommune skelner mellem solceller direkte på tagfladen, som ikke kræver byggetilladelse, og anlæg på stativ, som altid kræver tilladelse. Om dit hus er berørt af lokalplan, bevaring, fredning, beskyttelseslinjer eller kirkelandskab, kan du se på kommunens kort. Her er reglerne og hvordan du søger.",
  "sections": [
   ("Direkte på tagfladen: ingen byggetilladelse", [
     ("ul", [("Solceller og solfangere direkte på tagfladen af et hus kræver <strong>ikke byggetilladelse</strong>.", ["sk_sol"]),
             ("Undtaget er <strong>erhvervsbygninger, landbrugsbygninger og etageejendomme</strong>, hvor det altid kræver kommunens tilladelse.", ["sk_sol"]),
             ("Anlægget skal stadig overholde bygningsreglementet, lokalplaner og tinglyste deklarationer.", ["sk_sol"]),
             ("Er ejendommen ikke berørt af kommunens korttemaer, skal du ikke søge, men anlægget skal indberettes til BBR.", ["sk_sol"])]),
   ]),
   ("På stativ: altid tilladelse", [
     ("p", "Placerer du solcellerne eller solfangerne på <strong>stativ</strong>, fritstående eller på taget, kræver det altid kommunens tilladelse. I landzone er det en landzonetilladelse, i byzone en byggetilladelse.", ["sk_sol"]),
   ]),
   ("Tjek kortet: fem forhold kræver tilladelse", [
     ("ul", [("<strong>Fredet bygning:</strong> kræver tilladelse fra Kulturstyrelsen, og normalt kan der ikke sættes solceller op.", ["sk_sol"]),
             ("<strong>Bevaringsværdig bygning:</strong> kontakt kommunen, så bevaringsværdien ikke ødelægges.", ["sk_sol"]),
             ("<strong>Lokalplan eller byplanvedtægt:</strong> der kan være forbud, og så skal du søge dispensation. Ukomplicerede sager forsøger kommunen at svare på inden for 2 uger.", ["sk_sol"]),
             ("<strong>Arealfredning eller beskyttelseslinje:</strong> kræver en konkret ansøgning.", ["sk_sol"]),
             ("<strong>Kirkelandskab:</strong> kræver tilladelse fra Haderslev Stift. Skal sagen også have kommunens tilladelse, tilbyder kommunen at sende den videre til stiftet.", ["sk_sol"])]),
   ]),
   ("Sådan søger du", [
     ("p", "Ansøgningen skal indeholde adresse, anlæggets størrelse i m², effekt, en begrundelse for placeringen og en tegning af placeringen med angivelse af højde. Tegningen kan laves på kommunens digitale kort og sendes som pdf til byg-bolig@sonderborg.dk.", ["sk_sol"]),
   ]),
  ],
  "faq": [
   ("Kræver solceller byggetilladelse i Sønderborg Kommune?", "Ikke når de sidder direkte på tagfladen af et hus. På stativ kræver det altid tilladelse, og på erhvervsbygninger, landbrugsbygninger og etageejendomme kræver det også kommunens tilladelse.", ["sk_sol"]),
   ("Må jeg sætte solceller op, hvis mit hus ligger i et kirkelandskab?", "Det kræver tilladelse fra Haderslev Stift. Kræver anlægget også tilladelse eller dispensation fra Sønderborg Kommune, tilbyder kommunen at sende sagen videre til stiftet.", ["sk_sol"]),
   ("Hvor hurtigt får jeg dispensation fra en lokalplan til solceller i Sønderborg?", "Ved ukomplicerede sager forsøger kommunen at give svar inden for 2 uger.", ["sk_sol"]),
   ("Hvem kontakter jeg om solceller i Sønderborg Kommune?", "Byg i Sønderborg Kommune (Kvik-Caféen) på 88 72 40 82. Ansøgninger kan sendes til byg-bolig@sonderborg.dk.", ["sk_sol"]),
  ],
}
FV_PAGE["roskilde"] = {
  "kw": "fjernvarme roskilde / fors fjernvarme roskilde / varmepumpe roskilde",
  "evidence": "Roskilde Kommune har en side om varmeforsyning (opdateret 28/9 2026) med status for Himmelev, Veddelev, Vindinge og de fire aflyste projekter, og Fors offentliggør projektstatus for Veddelev (senest 23/10 2026).",
  "intro": "I Roskilde Kommune har 44 % af husene fjernvarme, og nettet bliver udbygget i Veddelev, Himmelev og Vindinge. I Jyllinge, Viby-Dåstrup, Gadstrup-Snoldelev og Store Valby-Ågerup er projekterne aflyst. Her er status, de to værkers priser og regnestykket mod en varmepumpe.",
  "status": [
   ("<strong>Himmelev:</strong> udrulningen er i sin afsluttende fase og ventes færdig i løbet af 2026.", ["ros_varme"]),
   ("<strong>Veddelev:</strong> gravearbejdet er i gang. Fors forventer at koble etape 1 på i varmesæsonen 2026/27 og etape 4 i foråret 2027.", ["fors_ved", "ros_varme"]),
   ("<strong>Vindinge:</strong> projektet fortsætter efter skift af entreprenør, og arbejdet genoptages, når den nye entreprenør er på plads.", ["ros_varme"]),
   ("<strong>Jyllinge, Viby-Dåstrup, Gadstrup-Snoldelev og Store Valby-Ågerup:</strong> projektgodkendelserne er bortfaldet, og områderne er tilbage på naturgas.", ["ros_varme", "ros_jyl"]),
  ],
  "local_take": "Svogerslev Fjernvarmecentral hører til de 20 % billigste værker i landet, mens Fors Varme Roskilde ligger ca. 1.400 kr. over landsgennemsnittet for et standardhus. Bor du i Jyllinge, Viby, Gadstrup eller Store Valby, kommer fjernvarmen ikke foreløbig, og en luft til vand-varmepumpe med tilskud er det oplagte valg. I Veddelev er fjernvarmen på vej.",
  "contact": ("Fors", "70 20 20 66 · fors@fors.dk", "fors_ved"),
  "faq": [
   ("Hvad koster fjernvarme i Roskilde?", "Ifølge Forsyningstilsynets statistik pr. 31. januar 2026 koster et standardhus på 130 m² med 18,1 MWh 18.367 kr. om året inkl. moms hos Fors Varme Roskilde og 14.575 kr. hos Svogerslev Fjernvarmecentral. Landsgennemsnittet er 16.953 kr.", ["ft_pris"]),
   ("Hvor kommer fjernvarmen i Roskilde fra?", "Ifølge Fors Varme Roskildes årsrapport for 2025 leveres varmen fra VEKS, primært som overskudsvarme fra kraftvarmeværket i Avedøre og fra affaldsforbrændingen hos ARGO i Roskilde. Fors producerer selv varme med en varmepumpe, der udnytter spildevand fra Bjergmarken Renseanlæg.", ["fors_aar"]),
   ("Hvad koster det at få fjernvarme i Veddelev?", "Fors skriver, at tilslutning koster 25.000 kr. til kampagnepris, hvis du tilmelder dig, før der graves på din vej, og 50.000 kr. bagefter.", ["fors_ved"]),
  ],
}
FV_PAGE["soenderborg"] = {
  "kw": "fjernvarme sønderborg / sønderborg varme / varmepumpe sønderborg",
  "evidence": "ProjectZero viser varmekilde og forsyningsselskab for hver by i Sønderborg Kommune, og Sønderborg Varme og SONFOR beskriver udbygningen mod vest og på Nordals (tjekket 29/10 2026).",
  "intro": "I Sønderborg Kommune har tre ud af fem huse fjernvarme, og Sønderborg Varme udbygger mod vest til Nybøl, Vester Sottrup, Avnbøl, Ullerup og Blans. På Nordals leverer SONFOR varmen. Her er status by for by, de to selskabers priser og regnestykket mod en varmepumpe.",
  "status": [
   ("<strong>Nybøl og Vester Sottrup:</strong> fjernvarmen lægges ud i etaper, og de sidste etaper er planlagt til 2026.", ["sv_nyb"]),
   ("<strong>Avnbøl, Ullerup og Blans:</strong> Sønderborg Varme ventes at levere varme i Avnbøl og Ullerup i 2027 og i Blans i 2028. I Blans blev tilslutningskravet sænket fra 75 til 65 %, og 67 % er tilmeldt.", ["df_blans", "sn_blans"]),
   ("<strong>Skodsbøl:</strong> Sønderborg Varme arbejder på et projektforslag, men det afhænger af lokal opbakning.", ["pz_varme"]),
   ("<strong>Nordals:</strong> SONFOR forsyner fra Nordborg til Guderup. Projektet i Dyndved blev ikke gennemført, og i Oksbøl, Broballe, Mjels og Elstrup var tilslutningen for lav.", ["sonfor_na", "sonfor_halm"]),
  ],
  "local_take": "Sønderborg Varme hører til den billigste fjerdedel af landets værker, mens SONFOR Varme på Nordals er blandt de 10 % dyreste. Bor du i Sønderborg Varmes område eller i en af de nye byer mod vest, er fjernvarmen svær at slå. Bor du i en landsby uden fjernvarmeplaner, fx Oksbøl, Broballe eller Elstrup, er en luft til vand-varmepumpe med tilskud det oplagte valg.",
  "contact": ("Sønderborg Varme", "73 43 50 00 · post@sfjv.dk", "pz_varme"),
  "faq": [
   ("Hvad koster fjernvarme i Sønderborg?", "Ifølge Forsyningstilsynets statistik pr. 31. januar 2026 koster et standardhus på 130 m² med 18,1 MWh 14.760 kr. om året inkl. moms hos Sønderborg Varme og 23.694 kr. hos SONFOR Varme. Landsgennemsnittet er 16.953 kr.", ["ft_pris"]),
   ("Hvor kommer fjernvarmen i Sønderborg fra?", "Sønderborg Varme bygger et system med tre ben: elbaseret varme, biomasse og affaldsenergi. En elkedel på 25 MW ved kraftvarmeværket i Sønderborg ventes i drift i 2026, og værket i Gråsten får en luft-vand-varmepumpe på 13 MW i 2027. Selskabet stræber efter at være CO2-neutralt i 2029.", ["df_sv29"]),
   ("Hvor kommer fjernvarmen på Nordals fra?", "Sønderborg Forsyning (SONFOR) skrev i 2023, at fjernvarmeanlægget i Nordborg udelukkende fyrer med halm. Nettet løber fra Nordborg til Guderup.", ["sonfor_halm", "sonfor_na"]),
  ],
}

# ---------- daglig by-rutine 30. okt. 2026: Køge og Svendborg ----------
# Forsyningstilsynet, prisstatistik januar 2026 (CSV): værker i de to kommuner (navne og postnr. som i statistikken). Køge Fjernvarme (VEKS) indgår ikke i statistikken.
FV_PRICES["koege"] = [("Borup Varmeværk", "4140", "13.892", "510"), ("Køge Varme A/S", "4600", "23.912", "678")]
FV_PRICES["svendborg"] = [("Svendborg Fjernvarme", "5700", "16.486", "735"), ("Stenstrup Fjernvarme", "5771", "14.097", "570"), ("Skårup Fjernvarme", "5881", "26.627", "1.150")]
SOL_REG["koege"] = {
  "kw": "solceller køge kommune / tilladelse solceller køge",
  "evidence": "Køge Kommune beskriver reglerne for solceller og solfangere på enfamiliehuse på siden om energikilder og opvarmning, og dispensation og landzone på særskilte sider (tjekket 30/10 2026).",
  "intro": "Køge Kommune kræver som udgangspunkt ingen tilladelse til solceller eller solfangere på taget af et enfamiliehus. Det er lokalplanen og bygningsreglementet, der sætter grænserne, og ligger huset i landzone, kan det kræve landzonetilladelse. Her er reglerne og hvordan du søger.",
  "sections": [
   ("På taget af et enfamiliehus", [
     ("ul", [("Solcelle- og solfangeranlæg på taget af et <strong>enfamiliehus</strong> kræver som udgangspunkt ikke tilladelse fra kommunen.", ["koe_energi"]),
             ("Anlægget skal overholde bestemmelserne i <strong>lokalplanen</strong> og bygningsreglementet, bl.a. om højde og afstand.", ["koe_energi", "br18_179"]),
             ("Solfangere (varme) og solceller (strøm) er omfattet af de samme regler.", ["koe_energi"])]),
   ]),
   ("Når lokalplanen siger nej", [
     ("p", "Kommunalbestyrelsen kan kun <strong>i mindre grad</strong> dispensere fra en lokalplan, og der kan ikke dispenseres fra planens principper, som typisk står under formål og anvendelse. Du kan søge dispensation sammen med en ansøgning om byggetilladelse eller sende en begrundet ansøgning til tmf@koege.dk.", ["koe_disp"]),
   ]),
   ("Huse i landzone", [
     ("p", "Ligger ejendommen i landzone, kan anlægget kræve <strong>landzonetilladelse</strong>. Du kan slå op på kommunens kort, om din ejendom ligger i landzone. En ansøgning skal bl.a. indeholde en beskrivelse, et luftfoto med placering og en situationsplan.", ["koe_lz", "koe_energi"]),
     ("note", "Skal projektet kun anmeldes, har Køge Kommune 14 dage til at vurdere, om det er undtaget fra kravet om landzonetilladelse. Fristen løber først, når kommunen har alle oplysninger.", ["koe_lz"]),
   ]),
  ],
  "faq": [
   ("Kræver solceller byggetilladelse i Køge Kommune?", "Som udgangspunkt ikke på taget af et enfamiliehus. Anlægget skal dog overholde lokalplanen og bygningsreglementet, og særlige forhold kan kræve dispensation eller landzonetilladelse.", ["koe_energi"]),
   ("Kan Køge Kommune dispensere fra en lokalplan, der forbyder solceller?", "Kun i mindre grad. Der kan ikke dispenseres fra lokalplanens principper. Du søger sammen med byggeansøgningen eller med en begrundet ansøgning til tmf@koege.dk.", ["koe_disp"]),
   ("Hvad skal en ansøgning om landzonetilladelse i Køge indeholde?", "En beskrivelse af projektet, et luftfoto med placering, en situationsplan, tegninger før og efter og eventuelt fotos. Søger du for en anden, skal du vedlægge fuldmagt.", ["koe_lz"]),
   ("Hvem kontakter jeg om solceller i Køge Kommune?", "Byggesag på byg@koege.dk eller 56 67 24 55. Spørgsmål om lokalplaner går til Plan på plan@koege.dk eller 56 67 21 11.", ["koe_energi"]),
  ],
}
SOL_REG["svendborg"] = {
  "kw": "solceller svendborg kommune / byggetilladelse solceller svendborg",
  "evidence": "Svendborg Kommune beskriver på siden 'Overvejer du solceller?', hvornår anlæg på tag, landbrugsbygninger og terræn kræver bygge- eller landzonetilladelse (tjekket 30/10 2026).",
  "intro": "Svendborg Kommune kræver umiddelbart hverken byggetilladelse eller landzonetilladelse til solceller på et almindeligt parcelhus. Anlæg på terræn og på landbrugsbygninger har egne regler med grænser for areal, højde og last. Her er reglerne og hvordan du søger.",
  "sections": [
   ("På et almindeligt parcelhus", [
     ("ul", [("Solceller på et almindeligt parcelhus kræver <strong>umiddelbart ikke byggetilladelse eller landzonetilladelse</strong>.", ["svb_sol"]),
             ("Tjek om ejendommen har en <strong>lokalplan, byplanvedtægt eller tinglyste deklarationer</strong> med særlige regler for tagmateriale eller solceller.", ["svb_sol"]),
             ("På tag af andre bygninger end driftsbygninger kræver det ikke landzonetilladelse, så længe panelerne følger tagets hældning og ikke står på stativ.", ["svb_sol"])]),
   ]),
   ("Solceller i haven: grænsen går ved 40 m²", [
     ("ul", [("Et anlæg på terræn kræver ikke byggetilladelse, hvis det er <strong>under 40 m²</strong> og højst <strong>1,8 m</strong> højt på stativ.", ["svb_sol"]),
             ("Det må ikke stride mod deklarationer eller lokalplan og skal overholde naturbeskyttelseslovens afstandslinjer.", ["svb_sol"]),
             ("For at undgå landzonetilladelse skal det også ligge i nær tilknytning til bebyggelsen, højst 20 m fra hovedbygningen.", ["svb_sol"])]),
   ]),
   ("Landbrugs- og erhvervsbygninger", [
     ("p", "På eksisterende erhvervs- og landbrugsbygninger kræver solceller ikke byggetilladelse, hvis de bærende konstruktioner ikke belastes med mere end <strong>5 %</strong> ekstra, brandforholdene er uændrede, og lokalplan, deklarationer og fredning ikke er til hinder. Kommunen skriver, at de fleste anlæg på landbrugsbygninger øger lasten med mere end 5 % og derfor kræver byggetilladelse.", ["svb_sol"]),
   ]),
  ],
  "faq": [
   ("Kræver solceller byggetilladelse i Svendborg Kommune?", "Umiddelbart ikke på et almindeligt parcelhus. Lokalplan, byplanvedtægt og tinglyste deklarationer kan dog have særlige regler for tagmateriale eller solceller.", ["svb_sol"]),
   ("Hvor store solceller må jeg sætte op i haven uden tilladelse i Svendborg?", "Under 40 m² og højst 1,8 m høje på stativ, uden at stride mod deklarationer, lokalplan og naturbeskyttelseslovens afstandslinjer. I landzone skal anlægget også ligge højst 20 m fra hovedbygningen.", ["svb_sol"]),
   ("Kræver solceller på en landbrugsbygning tilladelse i Svendborg?", "Ofte. Øger anlægget lasten på de bærende konstruktioner med mere end 5 %, kræver det byggetilladelse, og det gør de fleste anlæg på landbrugsbygninger ifølge kommunen.", ["svb_sol"]),
   ("Hvem kontakter jeg om solceller i Svendborg Kommune?", "Byg og BBR i Svendborg Kommune på 62 23 33 33.", ["svb_sol"]),
  ],
}
FV_PAGE["koege"] = {
  "kw": "fjernvarme køge / køge fjernvarme / varmepumpe køge",
  "evidence": "Køge Fjernvarme meldte 5/10 2026 ud, at projektforslaget for K05, K06 og K08 skal annulleres (FAQ opdateret 26/10 2026), og Dansk Fjernvarme beskrev 1/10 2026 det nye værk i Bjæverskov.",
  "intro": "Kun 14 % af husene i Køge Kommune har fjernvarme, og halvdelen har naturgas. Omkring Nylandsvej bliver nettet udbygget, mens projektet for kvartererne omkring midtbyen skal regnes om. I Bjæverskov er et helt nyt værk åbnet. Her er status, værkernes priser og regnestykket mod en varmepumpe.",
  "status": [
   ("<strong>Omkring Nylandsvej (K02):</strong> gravearbejdet ved Ølsemaglevej Øst og Strandlodsvej er i gang. Forsythiavej, Tranholmsvej og Stevnsbovej er sendt i nyt udbud.", ["kfv_grav", "kfv_nyl"]),
   ("<strong>Kvartererne omkring midtbyen (K05, K06 og K08):</strong> Køge Fjernvarme vil have projektforslaget annulleret på grund af stigende renter og omkostninger og venter et nyt forslag i løbet af 2027.", ["kfv_pm"]),
   ("<strong>Bjæverskov:</strong> byens første varmeværk blev indviet 19. september 2026. 850 husstande er tilmeldt, ca. 80 % af byen, og de sidste ventes koblet på i begyndelsen af 2027.", ["df_bjae"]),
   ("<strong>Borup:</strong> Køge Kommune har VVM-screenet en ny elkedel ved Borup Varmeværk på Bækgårdsvej og vurderet, at den ikke kræver miljøvurdering.", ["koe_borup"]),
  ],
  "local_take": "Borup Varmeværk hører til de 15 % billigste værker i landet, mens Køge Varme A/S, der forsyner et mindre område i Køge, er blandt de 10 % dyreste. Køge Fjernvarme indgår ikke i Forsyningstilsynets statistik. Bor du i K05, K06 eller K08, er du fortsat i et fjernvarmeområde uden adgang til Varmepumpepuljen, så vent på det nye projektforslag, før du vælger. Uden for fjernvarmeplanerne er en luft til vand-varmepumpe det oplagte alternativ til gasfyret.",
  "contact": ("Køge Fjernvarme", "43 64 44 00 · koegefjernvarme@veks.dk", "kfv_pm"),
  "faq": [
   ("Hvad koster fjernvarme i Køge?", "Ifølge Forsyningstilsynets statistik pr. 31. januar 2026 koster et standardhus på 130 m² med 18,1 MWh 13.892 kr. om året inkl. moms hos Borup Varmeværk og 23.912 kr. hos Køge Varme A/S. Landsgennemsnittet er 16.953 kr. Køge Fjernvarme indgår ikke i statistikken.", ["ft_pris"]),
   ("Hvad koster det at blive tilsluttet fjernvarme omkring Nylandsvej?", "Køge Fjernvarme skriver, at tilmeldte er omfattet af kampagneprisen på 10.000 kr. inkl. moms for 20 meter stikledning (normalpris 56.000 kr.) og sparer 50 % på effektbidraget de første 5 år.", ["kfv_nyl"]),
   ("Hvor kommer fjernvarmen i Bjæverskov fra?", "Fra Energinets transformerstation lige vest for byen. Værket henter ca. 40 °C varmt vand fra stationens køling, og to varmepumper løfter det til ca. 70 °C. En gaskedel på 6 MW er backup.", ["df_bjae"]),
  ],
}
FV_PAGE["svendborg"] = {
  "kw": "fjernvarme svendborg / svendborg fjernvarme / varmepumpe svendborg",
  "evidence": "Svendborg Kommune beskriver fjernvarmen og Varmeplan 2030 på sin side om fjernvarme, og Svendborg Fjernvarme viser planen for nye områder (tjekket 30/10 2026). Dansk Fjernvarme beskrev 8/5 2026 selskabets nye produktion.",
  "intro": "I Svendborg Kommune har kun hvert fjerde hus fjernvarme, som produceres på værkerne i Svendborg, Skårup og Stenstrup. Svendborg Fjernvarme vil udbygge i flere bydele, men først skal en ny stor varmepumpe i drift. Her er status, de tre værkers priser og regnestykket mod en varmepumpe.",
  "status": [
   ("<strong>Ny produktion på Bodøvej:</strong> en 25 MW varmepumpe, en 25 MW elkedel og en ny akkumuleringstank ventes i fuld drift fra midten af 2028. Svendborg Fjernvarme skriver, at det er en forudsætning for at udbrede fjernvarmen.", ["df_svb"]),
   ("<strong>Svendborg by:</strong> planen omfatter boliger i Nordøst (ca. 576), Sydøst (ca. 432), Tved (ca. 411), Øst og Christiansminde (ca. 445) samt Ryttermarken, Frederiksø og Kogtved. Selskabet regner med omkring fem år i alt.", ["sfv_ud"]),
   ("<strong>Ollerup, Vester Skerninge og Ulbølle:</strong> ikke længere udlagt til fjernvarme, fordi projektet blev langt dyrere end ventet. Området er nu individuel varmeforsyning.", ["svb_oll"]),
   ("<strong>Lundeborg:</strong> fjernvarmeprojektet fra maj 2024 blev annulleret i november 2025, og området er udlagt til individuel varmeforsyning.", ["svb_lund"]),
  ],
  "local_take": "Stenstrup Fjernvarme hører til de 20 % billigste værker i landet, og Svendborg Fjernvarme ligger under landsgennemsnittet, mens Skårup Fjernvarme er blandt de 5 % dyreste. Bor du i en af de bydele, Svendborg Fjernvarme vil udbygge til, kan det betale sig at vente på tilbuddet. Bor du i Ollerup, Vester Skerninge, Ulbølle eller Lundeborg, er en luft til vand-varmepumpe med tilskud det oplagte valg.",
  "contact": ("Svendborg Fjernvarme", "62 21 33 21 · info@svendborgfjernvarme.dk", "sfv_ud"),
  "faq": [
   ("Hvad koster fjernvarme i Svendborg?", "Ifølge Forsyningstilsynets statistik pr. 31. januar 2026 koster et standardhus på 130 m² med 18,1 MWh 16.486 kr. om året inkl. moms hos Svendborg Fjernvarme, 14.097 kr. hos Stenstrup Fjernvarme og 26.627 kr. hos Skårup Fjernvarme. Landsgennemsnittet er 16.953 kr.", ["ft_pris"]),
   ("Hvor kommer fjernvarmen i Svendborg fra?", "Svendborg Fjernvarme har i dag en 16 MW ammoniak-varmepumpe, en 25 MW elkedel, tre gasmotorer og gaskedler. Cirka en tredjedel af varmen kommer fra gas, og selskabet vil nedbringe gasandelen fra ca. 35 til ca. 5 %.", ["df_svb"]),
   ("Hvorfor kan Svendborg Fjernvarme ikke bare udvide nu?", "Selskabet forklarer, at projektbekendtgørelsen hidtil har stået i vejen, fordi fossile brændsler har udgjort for stor en del af produktionen. De nye elektriske anlæg er en forudsætning for at udbrede fjernvarmen til nye områder.", ["df_svb"]),
  ],
}

# ---------- daglig by-rutine 31. okt. 2026: Faaborg og Aabenraa ----------
# Forsyningstilsynet, prisstatistik januar 2026 (CSV): værker i de to kommuner (navne og postnr. som i statistikken).
FV_PRICES["faaborg"] = [("Kværndrup Fjernvarme", "5772", "9.256", "468"), ("Midtfyns Fjernvarme (Ringe)", "5750", "15.766", "731"), ("FFV Varme A/S", "5750", "18.548", "862")]
FV_PRICES["aabenraa"] = [("Aabenraa - Rødekro Fjernvarme", "6200", "11.624", "511"), ("Hjordkær Fjernvarmeværk", "6230", "15.881", "660"), ("Padborg Fjernvarme", "6330", "16.318", "687"), ("Løjt Kirkeby Fjernvarmeselskab", "6200", "18.119", "766"), ("Genner, Hellevad og Hovslund Forenede Kraftvarmeværker", "6230", "19.129", "695")]
SOL_REG["faaborg"] = {
  "kw": "solceller faaborg-midtfyn kommune / byggetilladelse solceller faaborg",
  "evidence": "Faaborg-Midtfyn Kommune beskriver på siden 'El og varme', hvilke solcelleanlæg der kræver byggetilladelse, hvornår en lokalplan kræver dispensation, og hvad der skal meldes til BBR (tjekket 31/10 2026).",
  "intro": "Faaborg-Midtfyn Kommune kræver ikke byggetilladelse til solceller på den eksisterende tagkonstruktion af et parcelhus, dobbelthus, rækkehus eller sommerhus, når byggeretten er overholdt. Anlæg på terræn kræver altid tilladelse, og en lokalplan kan kræve dispensation. Her er reglerne og hvordan du søger.",
  "sections": [
   ("På taget af dit hus: ingen byggetilladelse", [
     ("ul", [("Solceller på den <strong>eksisterende tagkonstruktion</strong> af et enfamiliehus, dobbelthus, rækkehus eller sommerhus kræver ikke byggetilladelse.", ["fmk_elv"]),
             ("På <strong>flade tage</strong> på boliger må anlægget være op til 1,5 m højt uden byggetilladelse.", ["fmk_elv"]),
             ("Anlægget skal overholde byggeretten, fx det skrå højdegrænseplan og mindst 2,5 m til skel ved enfamiliehuse. Kan det ikke overholdes, kræver det byggetilladelse.", ["fmk_elv", "br18_179"])]),
   ]),
   ("Det kræver altid byggetilladelse", [
     ("ul", [("Solceller på <strong>terræn</strong>, fx i haven.", ["fmk_elv"]),
             ("Solceller på taget af <strong>erhvervsbygninger, etageboliger og landbrugsbygninger</strong>.", ["fmk_elv"]),
             ("I landzone kræver et anlæg på terræn også <strong>landzonetilladelse</strong>, og det skal normalt placeres i tilknytning til ejendommens bebyggelse.", ["fmk_elv"])]),
   ]),
   ("Lokalplan: dispensation ved mere end 75 % af tagfladen", [
     ("p", "Lokalplaner og byplanvedtægter har ofte regler om tagets materiale, farve og refleksioner. Du skal søge dispensation, hvis planen er bevarende, skal sikre et ensartet arkitektonisk udtryk, eller kræver bestemte tagmaterialer eller farver og anlægget fylder <strong>mere end 75 % af den enkelte tagflade</strong>. Ansøgningen sendes via Byg og Miljø med en begrundelse, oplysninger om anlægget og en tegning af placeringen.", ["fmk_elv"]),
   ]),
   ("Servitutter, fredning og kysten", [
     ("ul", [("Tjek at der ikke er <strong>tinglyste servitutter</strong>, som forhindrer solceller. Ved servitutter kontakter du den påtaleberettigede.", ["fmk_elv"]),
             ("En <strong>fredet bygning</strong> kræver tilladelse fra Kulturstyrelsen, og en bevaringsværdig bygning kræver en konkret vurdering hos BYG.", ["fmk_elv"]),
             ("Inden for <strong>strandbeskyttelseslinjen</strong> kræver solceller altid tilladelse fra Kystdirektoratet.", ["fmk_elv"])]),
   ]),
  ],
  "faq": [
   ("Kræver solceller byggetilladelse i Faaborg-Midtfyn Kommune?", "Ikke på den eksisterende tagkonstruktion af et enfamiliehus, dobbelthus, rækkehus eller sommerhus, når byggeretten er overholdt. Solceller på terræn og på erhverv, etageboliger og landbrugsbygninger kræver byggetilladelse.", ["fmk_elv"]),
   ("Hvornår skal jeg søge dispensation fra lokalplanen til solceller i Faaborg-Midtfyn?", "Bl.a. hvis lokalplanen er bevarende, skal sikre et ensartet udtryk, eller kræver bestemte tagmaterialer eller farver og anlægget fylder mere end 75 % af tagfladen. Du søger via Byg og Miljø.", ["fmk_elv"]),
   ("Må jeg sætte solceller op på et hus tæt ved kysten i Faaborg?", "Ligger ejendommen inden for strandbeskyttelseslinjen, kræver det altid tilladelse fra Kystdirektoratet, før du sætter solceller op.", ["fmk_elv"]),
   ("Hvem kontakter jeg om solceller i Faaborg-Midtfyn Kommune?", "BYG i Faaborg-Midtfyn Kommune på byg@fmk.dk eller 72 53 21 04.", ["fmk_byg"]),
  ],
}
SOL_REG["aabenraa"] = {
  "kw": "solceller aabenraa kommune / tilladelse solceller aabenraa",
  "evidence": "Aabenraa Kommune beskriver på siden om solenergianlæg og siden om byggetilladelse, hvordan man undersøger reglerne og søger via Byg og Miljø (tjekket 31/10 2026). Kommunens vejledning til Byg og Miljø viser, hvilke forhold på grunden portalen tjekker.",
  "intro": "Aabenraa Kommune beder husejere undersøge byggelovgivningen og en eventuel lokalplan, før de sætter solceller op, og henviser til vejledningen 'Gode råd inden du opsætter solenergianlæg'. Kræver anlægget tilladelse, søger du i Byg og Miljø, som også viser bindinger på din grund. Her er reglerne og hvordan du søger.",
  "sections": [
   ("Tjek byggelovgivning og lokalplan først", [
     ("ul", [("Når du vil sætte et solenergianlæg op, skal du være opmærksom på de forhold i <strong>byggelovgivningen og en eventuel lokalplan</strong>, som skal overholdes.", ["abr_sol"]),
             ("Kommunens vejledning <strong>'Gode råd inden du opsætter solenergianlæg'</strong> samler de generelle retningslinjer, byggeloven og lokalplanforhold.", ["abr_sol"]),
             ("Bygningsreglementet kræver, at solceller ved parcel-, række- og dobbelthuse holder <strong>mindst 2,5 m til skel</strong> mod nabo, sti og vej.", ["br18_179"])]),
   ]),
   ("Byg og Miljø viser bindinger på din grund", [
     ("p", "Under <strong>Forhold på projektstedet</strong> i Byg og Miljø kan du klikke dig gennem fire faner: lokal- og kommuneplaner, bygge- og beskyttelseslinjer, fredning og forurening. Her ser du fx, om projektet kræver dispensation fra en lokalplan, og kommunen skriver, at det kan have stor betydning for både sagsbehandlingstiden og afgørelsen.", ["abr_bom"]),
   ]),
   ("Når anlægget kræver tilladelse", [
     ("ul", [("Ansøgningen sendes digitalt via <strong>Byg og Miljø</strong>, hvor du også får oplyst, hvilke bilag der skal med.", ["abr_byg"]),
             ("Alle bilag skal være i pdf-format, gemt enkeltvis og navngivet efter indholdet, fx situationsplan eller facade.", ["abr_byg"]),
             ("Søger en installatør for dig, giver du fuldmagt i Byg og Miljø. Kommunen opkræver et <strong>byggesagsgebyr efter tidsforbrug</strong>.", ["abr_byg"])]),
   ]),
   ("Sikkerhed og installation", [
     ("p", "Elinstallationen skal altid udføres af en <strong>autoriseret elinstallatør</strong>. Kommunen gør desuden opmærksom på Sikkerhedsstyrelsens advarsel fra 2013 om brandfare ved solcellesystemet Scheuten Solar Multisol (typerne P6-48, P6-54, P6-60 og P6-66).", ["abr_sol"]),
   ]),
  ],
  "faq": [
   ("Kræver solceller byggetilladelse i Aabenraa Kommune?", "Det afhænger af byggelovgivningen og en eventuel lokalplan for ejendommen. Kommunen henviser til vejledningen 'Gode råd inden du opsætter solenergianlæg', og i Byg og Miljø kan du se, om der er en lokalplan eller andre bindinger.", ["abr_sol", "abr_byg"]),
   ("Hvordan ser jeg, om min grund i Aabenraa har en lokalplan eller fredning?", "Start en ansøgning i Byg og Miljø og vælg adressen. Under 'Forhold på projektstedet' viser portalen lokal- og kommuneplaner, bygge- og beskyttelseslinjer, fredning og forurening.", ["abr_bom"]),
   ("Hvad koster det at søge om tilladelse til solceller i Aabenraa?", "Kommunen opkræver et byggesagsgebyr efter den tid, der bliver brugt på sagen. Taksterne står i kommunens gebyrvedtægt.", ["abr_byg"]),
   ("Hvem kontakter jeg om solceller i Aabenraa Kommune?", "Team Byg i Aabenraa Kommune på 73 76 73 47 eller byg@aabenraa.dk.", ["abr_sol"]),
  ],
}
FV_PAGE["faaborg"] = {
  "kw": "fjernvarme faaborg / ffv varme faaborg / varmepumpe faaborg",
  "evidence": "FFV Varme beskriver status for Faaborg nordvest, landsbyerne og Korinth på sin side om fjernvarmeprojekter (tjekket 31/10 2026), og Faaborg-Midtfyn Kommune godkendte 10/12 2025 aflysningen af projektet i Korinth.",
  "intro": "Kun hvert tredje hus i Faaborg-Midtfyn Kommune har fjernvarme, som leveres af FFV Varme, Midtfyns Fjernvarme, Kværndrup Fjernvarme og Fjernvarme Fyn. Flere udvidelser er sat på pause eller aflyst, fordi for få har tilmeldt sig. Her er status, værkernes priser og regnestykket mod en varmepumpe.",
  "status": [
   ("<strong>Faaborg by:</strong> FFV Varme lægger en ny fjernvarmeledning på Rugagervej fra Råmosevej til området ved Røde Kro som led i moderniseringen af nettet. Arbejdet ventes færdigt i slutningen af november 2026.", ["ffv_rug"]),
   ("<strong>Faaborg nordvest</strong> (bl.a. Saugstedgårdsvej, Bjernevej, Kildevej og Frydensbergvej): udvidelsen er sat midlertidigt på pause, fordi de lave gaspriser gør det svært at nå den nødvendige tilslutning.", ["ffv_proj"]),
   ("<strong>Brobyværk, Vester Åby, Horne, Falsled og Millinge/Svanninge:</strong> projekterne er sat på pause i ca. et år. I <strong>Espe</strong> nåede FFV omkring 86 % af de nødvendige tilslutninger, og projektet er afsluttet.", ["ffv_pause", "ffv_proj"]),
   ("<strong>Korinth:</strong> kun 126 forhåndstilmeldinger mod de 348, projektet krævede. Kommunen godkendte 10. december 2025, at projektet aflyses.", ["fmk_kor"]),
  ],
  "local_take": "Kværndrup Fjernvarme hører til de 2 % billigste værker i landet, og Midtfyns Fjernvarme i Ringe ligger under landsgennemsnittet, mens FFV Varme, der forsyner Faaborg, ligger over. Bor du i Korinth eller Espe, er en luft til vand-varmepumpe med tilskud det oplagte valg. Bor du i en af de landsbyer, hvor projektet er sat på pause, så følg FFV's udmeldinger: tilskuddet til en varmepumpe bortfalder først, hvis et fjernvarmeprojekt bliver godkendt og sat i gang.",
  "contact": ("FFV Varme A/S", "62 61 16 66 · ffv@ffv.dk", "ffv_proj"),
  "faq": [
   ("Hvad koster fjernvarme i Faaborg-Midtfyn?", "Ifølge Forsyningstilsynets statistik pr. 31. januar 2026 koster et standardhus på 130 m² med 18,1 MWh 18.548 kr. om året inkl. moms hos FFV Varme, 15.766 kr. hos Midtfyns Fjernvarme og 9.256 kr. hos Kværndrup Fjernvarme. Landsgennemsnittet er 16.953 kr.", ["ft_pris"]),
   ("Hvorfor blev fjernvarmen i Korinth aflyst?", "Projektet krævede mindst 348 tilslutninger ud af 487 bygninger, men i sensommeren 2025 havde kun 126 meldt sig. En ny beregning viste et samfundsøkonomisk underskud på ca. 40 mio. kr. i forhold til luft til vand-varmepumper over 20 år.", ["fmk_kor"]),
   ("Hvad tilbød Midtfyns Energi i Ringe i 2026?", "Boligejere i Ringe, Ryslinge, Fjellerup og Gislev, der tilmeldte sig senest 1. juni 2026, fik 10.000 kr. i rabat, så tilslutningen kostede 21.250 kr.", ["df_mfe"]),
  ],
}
FV_PAGE["aabenraa"] = {
  "kw": "fjernvarme aabenraa / aabenraa fjernvarme / varmepumpe aabenraa",
  "evidence": "Aabenraa Fjernvarme viser tidsplaner for Bolderslev (opdateret 21/10 2026) og Varnæs (20/8 2026) og priser og konverteringsbidrag for 2026 på sin hjemmeside (tjekket 31/10 2026).",
  "intro": "Halvdelen af husene i Aabenraa Kommune har fjernvarme, og Aabenraa Fjernvarme er blandt de billigste værker i landet. Nettet bliver lige nu udbygget til Bolderslev og Varnæs, men i de nye områder kommer et årligt konverteringsbidrag oven i prisen. Her er status, værkernes priser og regnestykket mod en varmepumpe.",
  "status": [
   ("<strong>Bolderslev:</strong> første spadestik på transmissionsledningen blev taget 4. maj 2026, og ledningen ventes færdig i december 2026. De første forbrugere ventes at få fjernvarme i 1. kvartal 2027, og en ny fjernvarmecentral er under opførelse.", ["afv_bol", "afv_bol_op"]),
   ("<strong>Varnæs:</strong> den sydlige del er færdig, og arbejdet i den nordlige del begyndte 6. juli 2026. Kommende kunder får en sms, når de kan koble på.", ["afv_var"]),
   ("<strong>Varnæs, Bovrup og Bolderslev</strong> betaler et konverteringsbidrag på 3.700 kr. om året, og <strong>Tinglev</strong> et transmissionsbidrag på 22,50 kr. pr. opvarmet m². Hvornår bidragene udfases, kan værket ikke love på forhånd.", ["afv_pris"]),
   ("<strong>Tumbøl og Felsted:</strong> overskudsvarme fra gasmotorerne på en biogasgård i Tumbøl bliver nu sendt ud i fjernvarmenettet.", ["afv_gylle"]),
  ],
  "local_take": "Aabenraa - Rødekro Fjernvarme er nr. 15 af 374 værker i Forsyningstilsynets statistik regnet fra det billigste, og Hjordkær og Padborg ligger under landsgennemsnittet, mens Løjt Kirkeby og Genner, Hellevad og Hovslund ligger over. I Varnæs, Bovrup og Bolderslev skal konverteringsbidraget med i regnestykket. Uden for fjernvarmeområderne er en luft til vand-varmepumpe det oplagte alternativ til gasfyret, men vælg en støjsvag model og placér udedelen med omtanke.",
  "contact": ("Aabenraa Fjernvarme", "74 62 40 98 · info@aabenraa-fjernvarme.dk", "afv_pris"),
  "faq": [
   ("Hvad koster fjernvarme i Aabenraa?", "Ifølge Forsyningstilsynets statistik pr. 31. januar 2026 koster et standardhus på 130 m² med 18,1 MWh 11.624 kr. om året inkl. moms hos Aabenraa - Rødekro Fjernvarme, 15.881 kr. hos Hjordkær, 16.318 kr. hos Padborg og 18.119 kr. hos Løjt Kirkeby. Landsgennemsnittet er 16.953 kr.", ["ft_pris"]),
   ("Hvad betaler et hus på 125 m² hos Aabenraa Fjernvarme?", "Værkets eget eksempel for 2026: 13,4 MWh til 511 kr. pr. MWh (6.847 kr.), fastbidrag 12,50 kr. pr. m² (1.563 kr.) og abonnement 750 kr., i alt 9.160 kr. om året inkl. moms. I konverteringsområderne kommer konverteringsbidraget oveni.", ["afv_pris"]),
   ("Hvornår får Bolderslev fjernvarme?", "Aabenraa Fjernvarme venter, at de første forbrugere i Bolderslev får fjernvarme i 1. kvartal 2027. Tidsplanen for gravearbejdet i byen opdateres løbende.", ["afv_bol"]),
  ],
}

# ---------- daglig by-rutine 1. nov. 2026: Herning og Greve ----------
# Forsyningstilsynet, prisstatistik januar 2026 (CSV): værker i de to kommuner (navne og postnr. som i statistikken).
FV_PRICES["herning"] = [("Vildbjerg Varme A/S", "7480", "9.255", "300"), ("Verdo Varme Herning", "8920", "13.045", "462"), ("Kibæk Varmeværk", "6933", "13.096", "368"), ("Sunds Vand- og Varmeværk", "7451", "13.996", "593"), ("Aulum Fjernvarme", "7490", "15.312", "375"), ("Ørnhøj-Grønbjerg Kraftvarmeværk", "6973", "20.377", "718")]
FV_PRICES["greve"] = [("Greve Fjernvarme A.m.b.a.", "2670", "14.432", "522"), ("Mosede Fjernvarmeværk a.m.b.a.", "2670", "21.594", "1028")]
SOL_REG["herning"] = {
  "kw": "solceller herning kommune / byggetilladelse solceller herning",
  "evidence": "Herning Kommune beskriver på siden 'Solceller, jordvarme og vindmøller', hvornår solceller kræver tilladelse, hvad der gælder for anlæg på terræn og i landzone, og hvordan man søger (tjekket 1/11 2026).",
  "intro": "Herning Kommune kræver ikke tilladelse efter byggeloven til solceller, der monteres fladt på den eksisterende tagkonstruktion, hvis anlægget højst øger lasten med 5 %. Anlæg på jorden kræver altid tilladelse, og i landzone også landzonetilladelse. Her er reglerne og hvordan du søger.",
  "sections": [
   ("Fladt på taget: højst 5 % ekstra last", [
     ("ul", [("Paneler, der monteres <strong>fladt på en eksisterende tagkonstruktion</strong>, kræver ikke tilladelse efter byggeloven, hvis anlæggets samlede vægt højst er 5 % af tagkonstruktionens nuværende last.", ["her_sol"]),
             ("Kan det eftervises, hører projektet ikke under en konstruktionsklasse, og så er byggetilladelse ikke nødvendig.", ["her_sol"]),
             ("Kommunen anbefaler altid at sende <strong>skitser og en beregning</strong> af påvirkningen via Byg og Miljø, så den kan vurdere, om anlægget kræver tilladelse.", ["her_sol"])]),
   ]),
   ("Regler, du stadig skal overholde", [
     ("ul", [("Anlægget må ikke stride mod <strong>bygningsreglementet, lokalplaner eller byplanvedtægter</strong>.", ["her_sol"]),
             ("Tjek også <strong>tinglyste deklarationer</strong>, fredede bygninger og lokale grundejervedtægter.", ["her_sol"]),
             ("Kræver et byggearbejde ikke tilladelse, er det ejerens eget ansvar, at det overholder bygningsreglementet og anden lovgivning.", ["her_br18"]),
             ("Bygningsreglementet kræver, at solceller ved parcel-, række- og dobbelthuse holder <strong>mindst 2,5 m til skel</strong> mod nabo, sti og vej.", ["br18_179"])]),
   ]),
   ("Solceller på jorden og i landzone", [
     ("p", "Et anlæg på terræn kræver tilladelse fra kommunen og må højst stå <strong>20 m fra ejendommens samlede bygninger</strong>. Det gælder kun mindre anlæg til eget forbrug. I landzone skal anlæg til eget forbrug som udgangspunkt placeres på tagflader, og et mindre anlæg på terræn kræver <strong>landzonetilladelse</strong>. Du søger i Byg og Miljø under ansøgningstypen 'Planmæssig forespørgsel'.", ["her_sol"]),
   ]),
   ("Genskin og naboer", [
     ("p", "Solen kan reflekteres fra blanke flader på panelerne og genere naboerne. Herning Kommune anbefaler, at du lader <strong>leverandøren vurdere risikoen for genskin</strong>. Er du i tvivl, om et anlæg må sættes op, kan du ringe til kommunen på 96 28 80 15.", ["her_sol"]),
   ]),
  ],
  "faq": [
   ("Kræver solceller byggetilladelse i Herning Kommune?", "Ikke når panelerne monteres fladt på den eksisterende tagkonstruktion og højst øger lasten med 5 %. Solceller på terræn kræver tilladelse, og i landzone også landzonetilladelse.", ["her_sol"]),
   ("Hvordan søger jeg om solceller på jorden i Herning?", "I Byg og Miljø under 'Planmæssig forespørgsel'. Anlægget må højst stå 20 m fra bygningerne og kun levere strøm til eget forbrug.", ["her_sol"]),
   ("Hvad skal en ansøgning om solceller i Herning indeholde?", "Relevant tegningsmateriale i pdf-format, der viser anlæggets størrelse og placering. Søger du for en anden, skal ejeren give fuldmagt i Byg og Miljø.", ["her_sol", "her_soeg"]),
   ("Hvem kontakter jeg om solceller i Herning Kommune?", "Byggesag i Herning Kommune på 96 28 80 15 eller byggesag@herning.dk.", ["her_sol"]),
  ],
}
SOL_REG["greve"] = {
  "kw": "solceller greve kommune / byggetilladelse solceller greve",
  "evidence": "Greve Kommunes 'Tjekliste før opsætning af solceller' (rev. 21.11.2019) og siden 'Skal du søge byggetilladelse?' beskriver, hvornår solceller kræver tilladelse, hvad lokalplanen betyder, og hvad der skal meldes til BBR (tjekket 1/11 2026).",
  "intro": "Greve Kommune kræver ikke byggetilladelse til solceller på et skråt tag eller en facade af et enfamilie- eller rækkehus, når bygningsreglementets højder og afstande holdes. Anlæg på terræn og på erhverv kræver altid tilladelse, og over ca. 75 % af en tagflade skal sagen behandles efter lokalplanen. Her er reglerne og hvordan du søger.",
  "sections": [
   ("Skråt tag på parcel- og rækkehuse: ingen byggetilladelse", [
     ("ul", [("Anlæg på <strong>facaden eller et tag, der ikke er fladt</strong>, på et enfamilie- eller rækkehus kræver ikke tilladelse eller anmeldelse efter byggeloven.", ["gre_tjek"]),
             ("Anlægget skal holde sig inden for <strong>BR18 § 177</strong> om højder og afstande.", ["gre_tjek"]),
             ("Anlæg på <strong>terræn</strong> og på erhvervsbyggeri kræver altid byggetilladelse.", ["gre_tjek"])]),
   ]),
   ("Lokalplan: over 75 % af en tagflade skal behandles", [
     ("p", "Greve Kommune vurderer, at solceller på op til ca. 75 % af en enkelt tagflade ikke er et nyt tag. Fylder anlægget mere, skal sagen som udgangspunkt behandles efter lokalplanen, og du sender en underskrevet ansøgning til byg@greve.dk med en <strong>målfast facadetegning</strong> og anlæggets størrelse i m². Afgørelsen træffes <strong>uden gebyr</strong>, fordi sagen behandles efter planloven.", ["gre_tjek"]),
   ]),
   ("Antirefleks, bevarende lokalplaner og fredning", [
     ("ul", [("Kommunen anbefaler <strong>antirefleksbehandlede</strong> paneler. Forbyder lokalplanen blanke og reflekterende tagmaterialer, er antirefleks et krav.", ["gre_tjek"]),
             ("Er du omfattet af en <strong>bevarende lokalplan</strong>, skal du sende en ansøgning til byg@greve.dk, og kommunen vurderer den konkret.", ["gre_tjek"]),
             ("Er bygningen <strong>bevaringsværdig eller fredet</strong>, eller ændrer anlægget bygningens udseende væsentligt, kræver det tilladelse.", ["gre_byg"])]),
   ]),
   ("Meld anlægget til BBR", [
     ("p", "Solceller og solfangere skal meldes til Bygnings- og Boligregistret på <strong>bbrteam@greve.dk</strong>. Mailen skal indeholde anlæggets størrelse (antal paneler og m²) og ydelsen i kWp.", ["gre_tjek"]),
   ]),
  ],
  "faq": [
   ("Kræver solceller byggetilladelse i Greve Kommune?", "Ikke på et skråt tag eller en facade af et enfamilie- eller rækkehus, når BR18's højder og afstande holdes. Solceller på terræn og på erhvervsbyggeri kræver altid byggetilladelse.", ["gre_tjek"]),
   ("Hvad hvis solcellerne dækker næsten hele taget i Greve?", "Over ca. 75 % af en enkelt tagflade skal sagen som udgangspunkt behandles efter lokalplanen. Send ansøgning, facadetegning og anlæggets størrelse til byg@greve.dk. Afgørelsen er uden gebyr.", ["gre_tjek"]),
   ("Skal mine solceller være antirefleks i Greve?", "Kommunen anbefaler det altid for at undgå gener for naboerne, og det er et krav, hvis lokalplanen forbyder blanke og reflekterende tagmaterialer.", ["gre_tjek"]),
   ("Hvem kontakter jeg om solceller i Greve Kommune?", "Byggesagsbehandlingen i Greve Kommune på 43 97 91 96. Spørgsmål om lokalplaner og ansøgninger kan sendes til byg@greve.dk.", ["gre_byg", "gre_tjek"]),
  ],
}
FV_PAGE["herning"] = {
  "kw": "fjernvarme herning / verdo herning / varmepumpe herning",
  "evidence": "Verdo oplyser priser pr. 1/4 2026, prisen fra 1/1 2027 og tilslutningsbidrag i Herning på sin hjemmeside, og Herning Kommune beskriver puljen til fælles varmeløsninger (tjekket 1/11 2026).",
  "intro": "Næsten fire ud af fem huse i Herning Kommune har fjernvarme, og Verdo Varme Herning hører til de 10 % billigste fjernvarmeværker i landet. I landsbyer uden fjernvarme støtter kommunen i stedet fælles varmeløsninger med rådgivning. Her er status, værkernes priser og regnestykket mod en varmepumpe.",
  "status": [
   ("<strong>Herning by:</strong> Verdo leverer fjernvarme til 35.000 adresser i Herning og omegn, og 90 % af varmen produceres på biomasse.", ["verdo_her"]),
   ("<strong>Pris fra 1. januar 2027:</strong> varmeregningen for et standardhus i Herning stiger med 215 kr. om året. Prisen bliver 46,12 øre pr. kWh, og et standardhus på 125 m² med 13.400 kWh kommer til at betale 9.989 kr. om året.", ["verdo_her_pris"]),
   ("<strong>Tilslutning:</strong> et almindeligt enfamiliehus betaler 25.000 kr. inkl. 20 m stikledning, når stikket blev ført ind ved byggemodningen, ellers 40.000 kr. Ekstra stikledning koster 675 kr. pr. meter.", ["verdo_her_pris"]),
   ("<strong>Landsbyer uden fjernvarme:</strong> kommunen øremærkede 600.000 kr. i 2024 og 2025 til rådgivning om fælles varmeløsninger for mindst 10 boliger, hvor mindst halvdelen har olie- eller gasfyr.", ["her_faelles"]),
  ],
  "local_take": "Vildbjerg Varme er nr. 6 af 374 værker i Forsyningstilsynets statistik regnet fra det billigste, og Verdo Varme Herning, Kibæk, Sunds og Aulum ligger alle under landsgennemsnittet, mens Ørnhøj-Grønbjerg ligger over. Har du fjernvarme fra et af de billige værker, er der sjældent penge i at skifte til varmepumpe. Bor du i en landsby uden fjernvarme, er en luft til vand-varmepumpe eller en fælles varmeløsning med naboerne de oplagte alternativer til olie- og gasfyret.",
  "contact": ("Verdo, fjernvarme Herning", "70 10 02 30 · varmeherning@verdo.com", "verdo_her"),
  "faq": [
   ("Hvad koster fjernvarme i Herning?", "Ifølge Forsyningstilsynets statistik pr. 31. januar 2026 koster et standardhus på 130 m² med 18,1 MWh 13.045 kr. om året inkl. moms hos Verdo Varme Herning, 9.255 kr. hos Vildbjerg Varme, 13.996 kr. hos Sunds Vand- og Varmeværk og 20.377 kr. hos Ørnhøj-Grønbjerg Kraftvarmeværk. Landsgennemsnittet er 16.953 kr.", ["ft_pris"]),
   ("Hvad koster det at blive tilsluttet fjernvarme i Herning?", "Hos Verdo koster et almindeligt enfamiliehus 25.000 kr. inkl. 20 m stikledning, hvis stikket blev ført ind ved byggemodningen, og ellers 40.000 kr. Hertil kommer en fjernvarmeunit og VVS-arbejde.", ["verdo_her_pris"]),
   ("Stiger fjernvarmen i Herning i 2027?", "Ja, lidt. Fra 1. januar 2027 stiger regningen for et standardhus på 125 m² med 13.400 kWh med 215 kr. til 9.989 kr. om året, og kWh-prisen bliver 46,12 øre inkl. moms.", ["verdo_her_pris"]),
  ],
}
FV_PAGE["greve"] = {
  "kw": "fjernvarme greve / greve fjernvarme / varmepumpe greve",
  "evidence": "Greve Fjernvarme viser udbygningsfaser og tilmeldingsstatus på siden 'Kan du få fjernvarme?' og priser på siden 'Hvad koster det at få fjernvarme?' (tjekket 1/11 2026), og Greve Kommune meldte aflysningen i Tune ud i 2026.",
  "intro": "Kun hvert fjerde hus i Greve Kommune har fjernvarme, og over halvdelen har stadig naturgas. Greve Fjernvarme udbygger nettet øst for motorvejen i fem faser frem mod 2038, mens Tune ikke får fjernvarme. Her er status, værkernes priser og regnestykket mod en varmepumpe.",
  "status": [
   ("<strong>Udbygningsfaser:</strong> Greve Fjernvarme udbygger i fem faser: fase 1 (2023-2026), fase 2 (2025-2030) og fase 3-5 (2028-2038), hvor projektforslagene endnu afventer.", ["gfv_kan"]),
   ("<strong>Åsager, Firhøj, Rugager, Græsager, Egedal, Hørager og Hirseager:</strong> 63 % har tilmeldt sig, så kravet på 60 % er nået. Gravearbejdet ventes at begynde i starten af 2027, og alle boliger ventes tilsluttet i løbet af 2027. Fugleparken er endnu ikke nået op på 60 %.", ["gfv_kan"]),
   ("<strong>Eriksmindekvarteret:</strong> Greve Fjernvarme forbereder projektet, og boligejerne kan forvente information i løbet af november 2026.", ["gfv_kan"]),
   ("<strong>Tune:</strong> Høje Taastrup Fjernvarme har aflyst projektet, fordi tilslutningen faldt fra 60 % til 46 %. Husejerne kan igen søge tilskud til en varmepumpe.", ["gre_tune"]),
  ],
  "local_take": "Greve Fjernvarme ligger under landsgennemsnittet i Forsyningstilsynets statistik, mens Mosede Fjernvarmeværk ligger et godt stykke over. Greve Fjernvarmes projektforslag for fase 1 fra 2022 regnede med en årlig besparelse på knap 6.000 kr. for en gennemsnitlig villakunde ved fjernvarme frem for en luft til vand-varmepumpe. Bor du i Tune, Greve Landsby, Kildebrønde eller Karlslunde Landsby, er der ingen fjernvarme på vej fra Greve Fjernvarme, og så er en luft til vand-varmepumpe det oplagte alternativ til gasfyret.",
  "contact": ("Greve Fjernvarme", "35 29 41 35 · projekt@grevefjernvarme.dk", "gfv_kan"),
  "faq": [
   ("Hvad koster fjernvarme i Greve?", "Ifølge Forsyningstilsynets statistik pr. 31. januar 2026 koster et standardhus på 130 m² med 18,1 MWh 14.432 kr. om året inkl. moms hos Greve Fjernvarme og 21.594 kr. hos Mosede Fjernvarmeværk. Landsgennemsnittet er 16.953 kr. Tranegilde Fjernvarme indgår ikke i statistikken.", ["ft_pris"]),
   ("Hvad koster det at blive tilsluttet Greve Fjernvarme?", "Skifter du fra olie, naturgas, varmepumpe eller elvarme, er kampagneprisen 34.995 kr., så længe kampagnen i dit område løber. Derefter er prisen 116.250 kr. Hertil kommer et etableringsbidrag på 30 kr. pr. m² om året i 30 år.", ["gfv_pris"]),
   ("Hvad koster fjernvarme om året for et hus i Greve?", "Greve Fjernvarmes eget eksempel med et hus på 136 m² og et forbrug på 14,7 MWh giver 17.992 kr. om året inkl. etableringsbidrag.", ["gfv_pris"]),
  ],
}

# ---------- daglig by-rutine 2. nov. 2026: Hjørring og Holte (Rudersdal) ----------
# Forsyningstilsynet, prisstatistik januar 2026 (CSV): værker i de to kommuner (Hjørring: de 11 værker, som Hjørring Kommune selv lister; Rudersdal: Norfors, som ejer og driver Holte Fjernvarme).
FV_PRICES["hjoerring"] = [("Hjørring Varmeforsyning", "9800", "12.876", "506"), ("Løkken Varmeværk", "9480", "13.450", "443"), ("Tversted Kraftvarmeværk a.m.b.a.", "9881", "13.956", "500"), ("Hirtshals Fjernvarme", "9850", "14.358", "410"), ("Bindslev Fjernvarme a.m.b.a.", "9881", "15.966", "543"), ("Vrå Varmeværk AMBA", "9760", "16.249", "618"), ("Sindal Varmeforsyning Amba", "9870", "18.365", "781"), ("Tårs Varmeværk", "9830", "18.522", "725"), ("Lønstrup Varmeforsyning AMBA", "9800", "21.523", "830"), ("Løkkensvejens Kraftvarmeværk Amba", "9480", "23.962", "875"), ("Lørslev Fjernvarmeforsyning Amba", "9800", "28.072", "698")]
FV_PRICES["holte"] = [("I/S Norfors - Norfors Fjernvarme", "2970", "25.084", "937")]
SOL_REG["hjoerring"] = {
  "kw": "solceller hjørring kommune / byggetilladelse solceller hjørring",
  "evidence": "Hjørring Kommunes side 'Solceller (individuelle anlæg)' beskriver, hvornår solceller på tag, facade og terræn kræver tilladelse, hvordan man søger dispensation, og hvad der gælder for batterier (tjekket 2/11 2026).",
  "intro": "Hjørring Kommune kræver ikke byggetilladelse til private solceller, der følger tagets hældning eller sidder parallelt med facaden. Lokalplan, servitutter og kommuneplanens rammer for solenergi skal dog overholdes, og anlæg på terræn kræver både byggetilladelse og landzonetilladelse. Her er reglerne og hvordan du søger.",
  "sections": [
   ("Tag og facade: ingen byggetilladelse", [
     ("ul", [("Private anlæg, der <strong>følger tagets hældning</strong> eller opsættes parallelt med facaden, kræver ikke byggetilladelse.", ["hjo_sol"]),
             ("På <strong>flade tage</strong> kan solenergianlæg eventuelt stå på stativer eller bærebeslag, der vinkler panelerne.", ["hjo_sol"]),
             ("Anlægget skal <strong>indberettes til BBR</strong>, når det er sat op (log på med MitID).", ["hjo_sol"])]),
   ]),
   ("Lokalplan, servitutter og kommuneplanens rammer", [
     ("p", "Anlægget skal overholde byggeretten i bygningsreglementet, den gældende lokalplan og tinglyste servitutter, og det skal udformes og placeres efter <strong>kommuneplanens generelle rammer for solenergianlæg</strong>. Strider det mod lokalplan eller servitut, sender du en begrundet ansøgning om dispensation via en <strong>planmæssig forespørgsel i Byg og Miljø</strong> eller på byggeri@hjoerring.dk.", ["hjo_sol"]),
     ("p", "Bygningsreglementet kræver, at solceller ved parcel-, række- og dobbelthuse holder <strong>mindst 2,5 m til skel</strong> mod nabo, sti og vej.", ["br18_179"]),
   ]),
   ("Solceller på terræn", [
     ("ul", [("Anlæg på jorden kræver <strong>byggetilladelse og landzonetilladelse</strong>.", ["hjo_sol"]),
             ("Det skal stå inden for ejendommens bebyggelsesareal, dvs. <strong>op til ca. 20 m</strong> fra den eksisterende hovedbygning, og tage hensyn til naboerne.", ["hjo_sol"]),
             ("Panelerne skal være <strong>antirefleksbehandlede</strong> og må ikke virke skæmmende i landskabet. Ansøgningen skal have kort med afstande til skel, tegninger med areal og totalhøjde og et datablad.", ["hjo_sol"])]),
   ]),
   ("Batteri over 20 kWh", [
     ("p", "Er der koblet et <strong>batterianlæg på over 20 kWh</strong> til solcellerne, kan det være omfattet af beredskabslovens § 34, stk. 2, og skal i høring hos Nordjyllands Beredskab. Hjørring Kommune står for høringen, så kontakt Team Byggeri eller skriv tydeligt i ansøgningen, at der er et batteri.", ["hjo_sol"]),
   ]),
  ],
  "faq": [
   ("Kræver solceller byggetilladelse i Hjørring Kommune?", "Ikke på et privat hus, når panelerne følger tagets hældning eller sidder parallelt med facaden. Solceller på terræn kræver både byggetilladelse og landzonetilladelse.", ["hjo_sol"]),
   ("Hvordan søger jeg dispensation fra lokalplanen til solceller i Hjørring?", "Send en begrundet ansøgning via en planmæssig forespørgsel i Byg og Miljø eller en mail til byggeri@hjoerring.dk. Kommunen tager stilling til, om der kan dispenseres.", ["hjo_sol"]),
   ("Må jeg sætte solcellerne på stativ på et fladt tag i Hjørring?", "Ja, ifølge kommunen kan solenergianlæg på flade tage eventuelt stå på stativer eller bærebeslag, der vinkler anlægget. Lokalplanen og bygningsreglementets højder og afstande gælder stadig.", ["hjo_sol"]),
   ("Hvem kontakter jeg om solceller i Hjørring Kommune?", "Team Byggeri i Hjørring Kommune på 72 33 65 70 eller byggeri@hjoerring.dk.", ["hjo_sol"]),
  ],
}
SOL_REG["holte"] = {
  "kw": "solceller rudersdal kommune / solceller holte tilladelse",
  "evidence": "Rudersdal Kommunes side 'Hvis du vil have solceller eller varmepumpe' beskriver, hvornår solceller kræver tilladelse fra Byplan, hvilke ældre lokalplaner der kan regulere solanlæg, og hvad en ansøgning skal indeholde (tjekket 2/11 2026).",
  "intro": "I Rudersdal Kommune, som Holte hører under, kræver solceller ikke tilladelse fra Byplan, når huset ikke er fredet eller bevaringsværdigt med værdi 1-3, og anlægget overholder lokalplan, servitutter og bygningsreglementet. Ældre lokalplaner fra før 2000 kan dog regulere solanlæg. Her er reglerne og hvordan du søger.",
  "sections": [
   ("Hvornår kræver solceller ikke tilladelse?", [
     ("ul", [("Bygningen er <strong>ikke fredet eller bevaringsværdig</strong> med værdien 1-3 og ligger ikke inden for en fredning.", ["rud_solvp"]),
             ("Anlægget overholder <strong>lokalplan eller byplanvedtægt</strong>, deklarationer og servitutter.", ["rud_solvp"]),
             ("Anlægget overholder bygningsreglementet, bl.a. <strong>BR18 § 177 og § 179</strong> om højder og afstande til vej- og naboskel.", ["rud_solvp", "br18_179"])]),
   ]),
   ("Ældre lokalplaner fra Søllerød og Birkerød", [
     ("p", "Kommunen gør opmærksom på ældre lokalplaner fra før 2000, fx <strong>nr. 10, 31 og 49 fra tidligere Søllerød</strong> og nr. 81 fra tidligere Birkerød. Flere af dem regulerer bygningernes ydre, fx tagbelægning eller solanlæg, og så skal du søge dispensation på byplan@rudersdal.dk. Er ejendommen omfattet af en bevarende lokalplan, en ensartet bebyggelse eller en bebyggelse med værdifuld karakter, så skriv til Byplan først.", ["rud_solvp"]),
   ]),
   ("Det skal en ansøgning om dispensation indeholde", [
     ("ul", [("En <strong>situationsplan</strong>, der viser tagfladen, hvor meget anlægget fylder, og panelernes afstand til skel med mål.", ["rud_solvp"]),
             ("<strong>Facadetegninger</strong> med eksisterende og fremtidige forhold, samlet højde over terræn og det skrå højdegrænseplan.", ["rud_solvp"]),
             ("Om panelerne ligger oven på, er indfældet i taget eller står på stativ, samt <strong>datablad</strong>, farver og om panelerne giver generende reflekser.", ["rud_solvp"])]),
   ]),
   ("Bevaringsværdige huse og BBR", [
     ("p", "Har huset <strong>bevaringsværdi 1-3</strong> eller er det fredet, skal du søge Byplan om tilladelse. Kommunens Arkitektur- og Byplanudvalg vedtog i august 2024 principper for solceller på bevaringsværdige bygninger, ensartede bebyggelser og bygninger i landzone. Huse opført efter 31.12.2011 registreres ikke med bevaringsværdi. Når anlægget er sat op, anmelder du det til BBR på BBR@rudersdal.dk.", ["rud_solvp"]),
   ]),
  ],
  "faq": [
   ("Kræver solceller tilladelse i Rudersdal Kommune?", "Ikke fra Byplan, når huset ikke er fredet eller bevaringsværdigt med værdi 1-3, ikke ligger i en fredning, og anlægget overholder lokalplan, servitutter og bygningsreglementet.", ["rud_solvp"]),
   ("Hvordan finder jeg ud af, om mit hus i Holte er bevaringsværdigt?", "Slå adressen op via kommunens side. Oplysninger om fredning ligger under Rudersdal SAVE. Bevaringsværdien -1 betyder, at ejendommen ikke er registreret.", ["rud_solvp"]),
   ("Hvor søger jeg dispensation til solceller i Rudersdal?", "Send en mail til byplan@rudersdal.dk med begrundelse, lokalplanens nummer og paragraf, situationsplan, facadetegninger og datablad på panelerne.", ["rud_solvp"]),
   ("Hvem kontakter jeg om solceller i Holte?", "Byplan i Rudersdal Kommune, Øverødvej 2 i Holte, på 46 11 25 00 (via Kontaktcenter) eller byplan@rudersdal.dk.", ["rud_solvp"]),
  ],
}
FV_PAGE["hjoerring"] = {
  "kw": "fjernvarme hjørring / hjørring varmeforsyning / varmepumpe hjørring",
  "evidence": "Hjørring Varmeforsyning oplyser varmepris 2026, tilslutningsafgift og status for fjernvarme til landsbyerne på sin hjemmeside, og Hjørring Kommune lister de lokale varmeværker på siden om varmeplan og varmebreve (tjekket 2/11 2026).",
  "intro": "Næsten to ud af tre huse i Hjørring Kommune har fjernvarme, og Hjørring Varmeforsyning hører til de billigste værker i landet. Til landsbyerne omkring Hjørring kommer der ikke fjernvarme foreløbig, fordi værket vurderer, at en varmepumpe er billigere for husejeren. Her er status, værkernes priser og regnestykket mod en varmepumpe.",
  "status": [
   ("<strong>Hjørring by:</strong> forbrugsprisen hos Hjørring Varmeforsyning er 506,25 kr. pr. MWh inkl. moms i 2026 mod 461,25 kr. i 2025.", ["hjv_pris"]),
   ("<strong>Tilslutning:</strong> et standardhus på op til ca. 125 m² betaler normalt 14.562,50 kr. inkl. moms plus 1.056,25 kr. pr. meter stikledning. I udstykninger fra før 1.1.2009 er prisen højere.", ["hjv_tilslut"]),
   ("<strong>Hjørring Syd:</strong> en stor varmepumpe ved renseanlægget i Hæstrup skal levere overskudsvarme til 2.500 husstande fra fyringssæsonen 2027-28.", ["df_haestrup"]),
   ("<strong>Landsbyerne:</strong> arbejdet med fjernvarme til Skibsby, Vidstrup, Harken/Hæstrup Mølleby, Bjergby, Tornby, Horne og Ilbro er indstillet.", ["hjv_status"]),
  ],
  "local_take": "Hjørring Varmeforsyning er nr. 26 af 374 værker i Forsyningstilsynets statistik regnet fra det billigste, og Løkken, Tversted og Hirtshals ligger også i den billige ende. Har du fjernvarme fra et af dem, er der sjældent penge i at skifte til varmepumpe. Lønstrup, Løkkensvejens Kraftvarmeværk og Lørslev ligger derimod blandt de dyreste i landet. Bor du i en af landsbyerne, hvor Hjørring Varmeforsyning har opgivet fjernvarmen, peger værket selv på varmepumpen som den billigste løsning.",
  "contact": ("Hjørring Varmeforsyning", "96 24 15 00 · hv@hjvarme.dk", "hjv_tilslut"),
  "faq": [
   ("Hvad koster fjernvarme i Hjørring?", "Ifølge Forsyningstilsynets statistik pr. 31. januar 2026 koster et standardhus på 130 m² med 18,1 MWh 12.876 kr. om året inkl. moms hos Hjørring Varmeforsyning, 14.358 kr. hos Hirtshals Fjernvarme, 16.249 kr. hos Vrå Varmeværk og 18.365 kr. hos Sindal Varmeforsyning. Landsgennemsnittet er 16.953 kr.", ["ft_pris"]),
   ("Hvad koster det at blive tilsluttet fjernvarme i Hjørring?", "Hos Hjørring Varmeforsyning er tilslutningsafgiften for et standardhus på op til ca. 125 m² normalt 14.562,50 kr. inkl. moms plus 1.056,25 kr. pr. meter stikledning. Værket skal bruge tegninger eller en opmåling for at give en præcis pris.", ["hjv_tilslut"]),
   ("Hvorfor steg fjernvarmen i Hjørring i 2026?", "Hjørring Varmeforsyning forklarede stigningen på ca. 9,7 % med, at affaldsvarmen fra Nordværk Affaldsenergi var blevet markant dyrere. Værkets eget standardhus steg fra 12.137 til 13.303 kr. om året.", ["df_hjv2026"]),
  ],
}
FV_PAGE["holte"] = {
  "kw": "fjernvarme holte / fjernvarme rudersdal / varmepumpe holte",
  "evidence": "Rudersdal Kommunes side 'Status på fjernvarme i Rudersdal' beskriver aflysningen af projekterne i Holte, Øverød, Gl. Holte, Nærum, Søllerød, Trørød og Skodsborg og status i Birkerød og Vedbæk, og Norfors oplyser takster for 2026 (tjekket 2/11 2026).",
  "intro": "Kun 15 % af husene i Rudersdal Kommune har fjernvarme, og seks ud af ti har naturgas. I juni 2026 blev fjernvarmeprojekterne for Holte, Øverød, Gl. Holte, Nærum, Søllerød, Trørød og Skodsborg aflyst, mens Birkerød, Bistrup og Vedbæk stadig er i spil. Her er status, Norfors' priser og regnestykket mod en varmepumpe.",
  "status": [
   ("<strong>Holte og Øverød:</strong> projektforslaget er trukket tilbage, fordi der ikke er fundet placeringer til nye lokale varmepumpeanlæg.", ["rud_fjv"]),
   ("<strong>Gl. Holte, Trørød, Nærum, Søllerød og Skodsborg:</strong> projektforslaget er også trukket tilbage og formelt aflyst efter kommunalbestyrelsens møde 24. juni 2026.", ["rud_fjv"]),
   ("<strong>Birkerød og Bistrup:</strong> Norfors fortsætter med et projekt for ca. 4.700 kunder og en luft-til-vand-varmepumpe på Blokken. Lokalplanen behandles efteråret 2026 og forår 2027.", ["rud_fjv"]),
   ("<strong>Vedbæk:</strong> E.ON's projekt med overskudsvarme fra spildevandet for ca. 530 kunder er forsinket, og E.ON vil præsentere en mere detaljeret tidsplan inden udgangen af 2026.", ["rud_fjv"]),
  ],
  "local_take": "Norfors ligger med 25.084 kr. for et standardhus i Forsyningstilsynets statistik blandt de dyreste værker i landet, nr. 361 af 374 regnet fra det billigste. For de mange gasfyr i Holte, Øverød, Nærum og Trørød er fjernvarme ikke længere på vej, og kommunen peger selv på varmepumpe og jordvarme som alternativer. Bor du i Birkerød, Bistrup eller Vedbæk, kan det betale sig at vente på tidsplanen og et konkret tilbud, før du vælger.",
  "contact": ("Norfors", "45 16 05 00 · norfors@norfors.dk", "rud_fjv"),
  "faq": [
   ("Hvad koster fjernvarme i Rudersdal?", "Norfors, der ejer og driver Holte Fjernvarme, opkræver 937,58 kr. pr. MWh inkl. moms i 2026 plus en fast målerafgift på 1.269,35 kr. og en arealafgift på 52,66 kr. pr. m². Norfors' eget standardhus på 125 m² med 13,4 MWh betaler 20.414,96 kr. om året, 1.839,02 kr. mere end i 2025.", ["nf_takst26", "nf_just26"]),
   ("Hvem leverer fjernvarme i Holte?", "Holte Fjernvarme overdrog 1. juli 2023 alle aktiver og aktiviteter til I/S Norfors. Afdelingen hedder stadig Holte Fjernvarme, men det er Norfors, der ejer, driver og opkræver betaling.", ["nf_holte"]),
   ("Skal jeg søge dispensation fra tilslutningspligten for at få varmepumpe i Rudersdal?", "Ikke hvis du kun skifter olie- eller gasfyret ud med en varmepumpe. Dispensation skal kun søges ved nybyggeri, væsentlige ombygninger samtidig med nyt varmeanlæg eller lavenergibyggeri i områder med fjernvarme. Husk at få BBR rettet på bbr@rudersdal.dk bagefter.", ["rud_fjv"]),
  ],
}

# ---------- daglig by-rutine 3. nov. 2026: Nykøbing Falster (Guldborgsund) og Haderslev ----------
# Forsyningstilsynet, prisstatistik januar 2026 (CSV): værker med postnumre i Guldborgsund og Haderslev kommuner (standardhus 130 m², 18,1 MWh, inkl. moms; MWh-pris).
FV_PRICES["nykoebing-falster"] = [("Sakskøbing Fjernvarmeselskab", "4990", "13.256", "521"), ("Sydfalster Varmeværk", "4873", "14.660", "466"), ("Øster Toreby, Sundby og Nagelsti Varmeværk", "4800", "15.518", "521"), ("Guldborgsund Varme", "4800", "15.774", "639"), ("Nysted Varmeværk", "4880", "16.240", "493"), ("Nr. Alslev Fjernvarmeværk", "4840", "17.061", "535"), ("REFA Stubbekøbing Fjernvarme", "4800", "18.867", "503"), ("REFA Horbelev Varmeværk", "4871", "20.082", "643"), ("REFA Gedser Fjernvarme", "4874", "21.314", "740")]
FV_PRICES["haderslev"] = [("Haderslev Fjernvarme", "6100", "15.187", "665"), ("Vojens Fjernvarme", "6500", "19.063", "846"), ("Gram Fjernvarme", "6510", "21.010", "850")]
SOL_REG["nykoebing-falster"] = {
  "kw": "solceller guldborgsund kommune / byggetilladelse solceller nykøbing falster",
  "evidence": "Guldborgsund Kommunes side med ofte stillede spørgsmål om byggetilladelse beskriver, hvornår solceller kræver byggetilladelse og landzonetilladelse, og hvilke betingelser der gælder for parcel-, række-, dobbelt- og sommerhuse (tjekket 3/11 2026).",
  "intro": "Guldborgsund Kommune, som Nykøbing Falster hører under, kræver ikke byggetilladelse til solceller på et parcel-, række-, dobbelt- eller sommerhus, når panelerne følger tagets hældning og lasten holdes under 5 %. Fladt tag, terræn og landzone kræver derimod tilladelse. Her er reglerne og hvordan du søger.",
  "sections": [
   ("Tre betingelser for at slippe for byggetilladelse", [
     ("ul", [("Solcellerne <strong>følger tagets hældning</strong>.", ["gul_faq"]),
             ("<strong>Lastvirkningen</strong> fra solcellerne holdes under 5 % i forhold til husets eksisterende dokumentation.", ["gul_faq"]),
             ("Anlægget overholder bygningsreglementets krav til <strong>afstand og højde</strong> samt lokalplaner og tinglyste servitutter.", ["gul_faq", "br18_179"])]),
   ]),
   ("Her kræver solceller byggetilladelse", [
     ("ul", [("Solceller på <strong>fladt tag</strong>, også på et parcelhus.", ["gul_faq"]),
             ("Solceller på <strong>terræn</strong>, altså på jorden.", ["gul_faq"]),
             ("Solceller på erhvervs-, etage-, kontor- og lagerbygninger, og anlæg, der <strong>ikke overholder bygningsreglementets</strong> krav til højde og afstand.", ["gul_faq"])]),
   ]),
   ("Landzone: også landzonetilladelse", [
     ("p", "Ligger ejendommen i <strong>landzone</strong>, kræver solcelleanlægget også en landzonetilladelse. Kommunen skriver, at sagsbehandlingen så tager længere tid: sagen skal i høring, tilladelsen annonceres på guldborgsund.dk, og først når den <strong>4 uger lange klagefrist</strong> er udløbet, kan der gives byggetilladelse.", ["gul_faq", "gul_lz"]),
   ]),
   ("BBR og hvem du kontakter", [
     ("p", "Kræver anlægget ikke byggetilladelse, skal du <strong>selv sørge for at registrere det i BBR</strong>. Er du i tvivl, om dit anlæg kræver tilladelse, kan du ringe til Bolig & Byggesag på 54 73 20 95. Ansøgninger sendes digitalt via Byg og Miljø med MitID.", ["gul_faq"]),
   ]),
  ],
  "faq": [
   ("Kræver solceller byggetilladelse i Guldborgsund Kommune?", "Ikke på et enfamilie-, række-, dobbelt- eller sommerhus, når panelerne følger tagets hældning, lasten holdes under 5 %, og bygningsreglementet, lokalplanen og servitutterne overholdes. På fladt tag og på terræn kræver det byggetilladelse.", ["gul_faq"]),
   ("Må jeg sætte solceller på mit flade tag i Nykøbing Falster uden tilladelse?", "Nej. Guldborgsund Kommune kræver byggetilladelse til solceller på fladt tag.", ["gul_faq"]),
   ("Skal jeg have landzonetilladelse til solceller på taget?", "Ja, hvis ejendommen ligger i landzone. Så kræver solcelleanlægget også en landzonetilladelse, og der er 4 ugers klagefrist, før der kan gives byggetilladelse.", ["gul_faq", "gul_lz"]),
   ("Hvem kontakter jeg om solceller i Guldborgsund Kommune?", "Bolig & Byggesag i Center for Teknik & Miljø på 54 73 20 95, mandag-onsdag kl. 9-11, torsdag kl. 14-16 og fredag kl. 9-11.", ["gul_faq"]),
  ],
}
SOL_REG["haderslev"] = {
  "kw": "solceller haderslev kommune / byggetilladelse solceller haderslev",
  "evidence": "Haderslev Kommunes side 'Solceller' beskriver, hvornår solceller kræver byggetilladelse eller landzonetilladelse, krav til BBR, konstruktion og brand og hvornår et anlæg skal VVM-screenes (tjekket 3/11 2026).",
  "intro": "Haderslev Kommune kræver ikke byggetilladelse til private solceller på et enfamilie-, tofamilie-, række- eller sommerhus, når panelerne følger tagets hældning, står mindst 2,5 m fra skel og holder sig inden for bygningshøjden. Fredede og bevaringsværdige huse og anlæg på terræn kræver tilladelse. Her er reglerne og hvordan du søger.",
  "sections": [
   ("Uden byggetilladelse: tag på dit eget hus", [
     ("ul", [("Gælder private anlæg på <strong>enfamilie-, tofamilie-, række- og sommerhuse</strong> og småbygninger som carport og garage ved dem.", ["had_sol"]),
             ("Panelerne skal <strong>følge tagets hældning</strong> og stå mindst 2,5 m fra skel.", ["had_sol", "br18_179"]),
             ("Solcellerne <strong>tæller med i bygningshøjden</strong>, som stadig skal overholdes.", ["had_sol"])]),
   ]),
   ("Her kræver det byggetilladelse", [
     ("ul", [("Huset er <strong>fredet eller bevaringsværdigt</strong>.", ["had_sol"]),
             ("Anlægget står på <strong>terræn</strong> eller ændrer husets brand- eller konstruktionsforhold, fx på arealer, der skal holdes fri til redningsberedskabet.", ["had_sol"]),
             ("Anlægget sidder på erhvervsbygninger, etageejendomme, kontor- eller lagerbygninger.", ["had_sol"])]),
     ("p", "Står anlægget på stativ på jorden i <strong>landzone</strong>, kræver det landzonetilladelse uanset størrelse.", ["had_sol"]),
   ]),
   ("Tag, vægt og placering", [
     ("p", "Kommunen anbefaler, at en <strong>professionel rådgiver</strong> gennemgår, om tagkonstruktionen kan bære den ekstra vægt. Hører taget til konstruktionsklasse 2 eller højere, skal en certificeret rådgiver tilknyttes. Placér panelerne harmonisk i forhold til kviste, tagvinduer og skorstene, og tjek lokalplanen, som fx kan bestemme tagets farve og materiale.", ["had_sol"]),
   ]),
   ("Husk BBR", [
     ("p", "Opsætningen skal <strong>altid registreres i BBR</strong> på bbr@haderslev.dk, uanset om anlægget kræver byggetilladelse eller ej. Tinglyste servitutter for din grund finder du på Tinglysning.dk.", ["had_sol"]),
   ]),
  ],
  "faq": [
   ("Kræver solceller byggetilladelse i Haderslev Kommune?", "Ikke på et privat enfamilie-, tofamilie-, række- eller sommerhus, når panelerne følger tagets hældning, står mindst 2,5 m fra skel og bygningshøjden overholdes. Lokalplaner og deklarationer kan dog forbyde solceller.", ["had_sol"]),
   ("Skal mit bevaringsværdige hus i Haderslev have tilladelse til solceller?", "Ja. Er ejendommen fredet eller bevaringsværdig, kræver solceller byggetilladelse i Haderslev Kommune.", ["had_sol"]),
   ("Skal solceller på jorden have landzonetilladelse i Haderslev?", "Ja. Et solcelleanlæg på stativ på jorden i landzone kræver landzonetilladelse uanset størrelse, og det kræver også byggetilladelse.", ["had_sol"]),
   ("Hvem kontakter jeg om solceller i Haderslev Kommune?", "Teknik og Klima i Haderslev Kommune, Christian X's Vej 39, på 74 34 34 34. BBR-registreringen sendes til bbr@haderslev.dk.", ["had_sol"]),
  ],
}
FV_PAGE["nykoebing-falster"] = {
  "kw": "fjernvarme nykøbing falster / guldborgsund varme / varmepumpe nykøbing falster",
  "evidence": "Guldborgsund Forsyning oplyser forsyningsområde, takster for 2026 og fjernvarmedeklaration for 2025, og Guldborgsund Kommune beskriver forslaget til Varmeplan 2025 på sin høringsside (tjekket 3/11 2026).",
  "intro": "57 % af husene i Guldborgsund Kommune har fjernvarme, og der er ingen naturgas i husene. Til gengæld har flere end hvert tiende hus elvarme, og næsten lige så mange har oliefyr. Her er status for fjernvarmen, de ni værkers priser og regnestykket mod en varmepumpe.",
  "status": [
   ("<strong>Nykøbing F. og omegn:</strong> Guldborgsund Varme forsyner ca. 7.000 kunder i Nykøbing F., Ønslev, Eskilstrup, Ovstrup, Gundslevmagle og Systofte.", ["gfo_varme"]),
   ("<strong>Pris 2026:</strong> 0,562 kr. pr. kWh inkl. moms plus fast målerbidrag (260,67 kr. for de fleste huse) og arealbidrag på 30,27 kr. pr. m² efter BBR.", ["gfo_takst26"]),
   ("<strong>Tilslutning:</strong> investeringsbidraget for et enfamilie-, kæde- eller rækkehus er 24.940,54 kr. inkl. moms plus 853,99 kr. pr. meter stikledning (PEX op til 40 mm).", ["gfo_takst26"]),
   ("<strong>Varmeplan 2025:</strong> fjernvarmen i de fleste byer og større landsbyer skal bevares og udbygges, mens oliefyrene uden for fjernvarmen skal udfases.", ["gul_vpl"]),
  ],
  "local_take": "Sakskøbing Fjernvarmeselskab er nr. 35 af 374 værker i Forsyningstilsynets statistik regnet fra det billigste, og Guldborgsund Varme ligger som nr. 116 under landsgennemsnittet. REFA's værker i Stubbekøbing, Horbelev og Gedser ligger derimod over gennemsnittet. Har du fjernvarme i Nykøbing F., er der sjældent penge i at skifte. Har du oliefyr eller elvarme i en landsby uden fjernvarme, er en varmepumpe den løsning, kommunen selv peger på, hvis der ikke kommer en fælles løsning.",
  "contact": ("Guldborgsund Forsyning", "72 44 12 12 · forbrug@guldborgsundforsyning.dk", "gfo_varme"),
  "faq": [
   ("Hvad koster fjernvarme i Nykøbing Falster?", "Ifølge Forsyningstilsynets statistik pr. 31. januar 2026 koster et standardhus på 130 m² med 18,1 MWh 15.774 kr. om året inkl. moms hos Guldborgsund Varme, 13.256 kr. hos Sakskøbing Fjernvarmeselskab og 18.867 kr. hos REFA Stubbekøbing Fjernvarme. Landsgennemsnittet er 16.953 kr.", ["ft_pris"]),
   ("Hvad koster det at blive tilsluttet fjernvarme i Nykøbing Falster?", "Guldborgsund Varmes investeringsbidrag for et enfamilie-, kæde- eller rækkehus er 24.940,54 kr. inkl. moms i 2026. Dertil kommer stikledningen, der koster 853,99 kr. pr. meter for de almindelige PEX-rør.", ["gfo_takst26"]),
   ("Hvad laves fjernvarmen i Nykøbing Falster af?", "I 2025 kom 47,5 % af Guldborgsund Varmes brændsel fra overskudsvarme, 47,4 % fra træ og 5,1 % fra bioolie. Ifølge fjernvarmedeklarationen er andelen af vedvarende energi inkl. el 100 %.", ["gfo_dekl25"]),
  ],
}
FV_PAGE["haderslev"] = {
  "kw": "fjernvarme haderslev / haderslev fjernvarme udvidelse / varmepumpe haderslev",
  "evidence": "Haderslev Kommune beskriver fjernvarmeudrulningen og lokalbyerne på sin side om fjernvarme og i Varmeplan for gasområder 2022, og Haderslev Fjernvarme oplyser kampagnepriser og status for udvidelsen (tjekket 3/11 2026).",
  "intro": "Fire ud af ti huse i Haderslev Kommune har fjernvarme, og hvert fjerde har naturgas. Haderslev Fjernvarme har gravet færdigt i sine udvidelsesområder, Vojens Fjernvarme skulle efter planen være færdig i 2026, mens lokalbyerne med naturgas ikke får fjernvarme. Her er status, værkernes priser og regnestykket mod en varmepumpe.",
  "status": [
   ("<strong>Haderslev by:</strong> Haderslev Fjernvarme skriver, at gravearbejdet er afsluttet i alle udvidelsesområder. Ved udgangen af 2024 var 2.537 nye kunder tilsluttet, og tilslutningen lå på 83,4 %.", ["hfv_tid", "hfv_gf25"]),
   ("<strong>Vojens:</strong> projektet for ca. 867 forbrugere i 9 delområder forventes udrullet inden udgangen af 2026.", ["had_fjv", "had_vpl"]),
   ("<strong>Gram:</strong> fjernvarmen forventedes udrullet inden udgangen af 2023.", ["had_fjv"]),
   ("<strong>Lokalbyer med naturgas:</strong> fjernvarmeselskaberne ser ikke mulighed for at tilbyde fjernvarme. Undtagelsen er Marstrup, hvor 85 % skulle tilslutte sig frivilligt.", ["had_fjv"]),
  ],
  "local_take": "Haderslev Fjernvarme er nr. 93 af 374 værker i Forsyningstilsynets statistik regnet fra det billigste og ligger under landsgennemsnittet, mens Vojens Fjernvarme og Gram Fjernvarme ligger over. Bor du i Haderslev by og har fået tilbudt fjernvarme, er det sjældent en varmepumpe kan konkurrere. Har du gasfyr i en af lokalbyerne, peger kommunens varmeplan på varmepumpe, jordvarme eller biomasse, medmindre I selv går sammen om en fælles løsning.",
  "contact": ("Haderslev Fjernvarme", "74 52 21 88 · info@haderslev-fjernvarme.dk", "hfv_tid"),
  "faq": [
   ("Hvad koster fjernvarme i Haderslev?", "Ifølge Forsyningstilsynets statistik pr. 31. januar 2026 koster et standardhus på 130 m² med 18,1 MWh 15.187 kr. om året inkl. moms hos Haderslev Fjernvarme, 19.063 kr. hos Vojens Fjernvarme og 21.010 kr. hos Gram Fjernvarme. Landsgennemsnittet er 16.953 kr.", ["ft_pris"]),
   ("Hvad koster det at komme på fjernvarme i Haderslevs udvidelsesområder?", "Haderslev Fjernvarmes kampagnepris er et engangsbeløb på 20.000 kr. og 267 kr. om måneden med Komplet-abonnement, eller 55.000 kr. kontant. Da gravearbejdet er afsluttet, kommer et genopgravningsgebyr på 10.000 kr. oveni, og kampagnen gælder kun indtil et år efter, at gravearbejdet startede på din vej.", ["hfv_tid"]),
   ("Hvorfor får lokalbyerne i Haderslev Kommune ikke fjernvarme?", "Fjernvarmeselskaberne i Haderslev, Vojens og Gram har vurderet, at områderne ligger for langt fra et eksisterende net eller har for få ejendomme med olie eller gas. Kommunen anbefaler i stedet individuelle varmepumper, jordvarme, biomasse eller lokale fælles løsninger som termonet.", ["had_fjv", "had_vpl"]),
  ],
}

# ---------- daglig by-rutine 4. nov. 2026: Frederikshavn og Hedensted ----------
# Forsyningstilsynet, prisstatistik januar 2026 (CSV): Frederikshavn = de 9 værker, kommunens varmescreening 2022 nævner (postnr. 9900/9300/9990/9970/9750/9352).
# Hedensted = de 5 selskaber på kommunens fjernvarmeside + Tørring-Ølholm og Daugård Fællesvarme (postnr. 8721). Annasminde Varmeforsyning (7160) udeladt: kommunetilhør ikke verificeret.
FV_PRICES["frederikshavn"] = [("Skagen Varmeværk", "9990", "12.635", "450"), ("Sæby Varmeværk", "9300", "14.032", "520"), ("Østervrå Varmeværk", "9750", "18.381", "687"), ("Frederikshavn Varme", "9900", "18.419", "798"), ("Strandby Varmeværk", "9970", "18.887", "750"), ("Voerså Kraftvarmeværk", "9300", "20.212", "875"), ("Thorshøj Kraftvarmeværk", "9750", "21.111", "793"), ("Hørby Varmeværk", "9300", "21.600", "812"), ("Dybvad Varmeværk", "9352", "23.350", "1.000")]
FV_PRICES["hedensted"] = [("RMU Forsyning (Rask Mølle, Uldum)", "7171", "18.121", "775"), ("Hornsyld Klimavarme", "8783", "20.178", "718"), ("Hedensted Fjernvarme", "8722", "20.397", "850"), ("Daugård Fællesvarme", "8721", "21.607", "627"), ("Tørring Kraftvarmeværk", "7160", "22.086", "247"), ("Løsning Fjernvarme", "8723", "22.581", "812"), ("Tørring Kraftvarmeværk, Ølholm", "7160", "27.242", "247")]
SOL_REG["frederikshavn"] = {
  "kw": "solceller frederikshavn kommune / byggetilladelse solceller frederikshavn",
  "evidence": "Frederikshavn Kommunes side 'Grøn energi' beskriver, hvornår solcelle- og solfangeranlæg kræver byggetilladelse eller dispensation, krav om BBR-registrering og ansøgningstyper i Byg og Miljø (tjekket 4/11 2026).",
  "intro": "Frederikshavn Kommune kræver som udgangspunkt ikke byggetilladelse til solceller på taget af dit hus, når anlægget overholder bygningsreglementets højde- og afstandskrav. Stativer på jorden, bevaringsværdige og fredede huse og ejendomme inden for bygge- og naturbeskyttelseslinjer kræver tilladelse. Her er reglerne og hvordan du søger.",
  "sections": [
   ("Her kræver solceller byggetilladelse", [
     ("ul", [("Anlæg på <strong>stativer på jorden</strong>.", ["fre_sol"]),
             ("Anlæg, der ikke overholder bygningsreglementets <strong>højde- og afstandskrav</strong>, fx fordi stativer eller bærebeslag vinkler panelerne op fra tagfladen.", ["fre_sol", "br18_179"]),
             ("Anlæg på etageboliger, erhvervsbygninger og landbrugets avls- og driftsbygninger med dyrehold.", ["fre_sol"]),
             ("Anlæg på en <strong>bevaringsværdig eller fredet</strong> ejendom eller på ejendomme omfattet af bygge- og naturbeskyttelseslinjer.", ["fre_sol"])]),
   ]),
   ("Lokalplan og deklaration: måske dispensation", [
     ("p", "Er dit hus omfattet af en lokalplan, byplanvedtægt eller tinglyst deklaration med regler om solceller, <strong>tagmaterialer eller refleksioner</strong>, kan det kræve dispensation eller byggetilladelse. Kommunen skriver, at nogle bestemmelser gør det helt umuligt at sætte solceller op. Du spørger via Byg og Miljø med ansøgningstypen 'Planmæssig forespørgsel'.", ["fre_sol"]),
   ]),
   ("Blænding og naboer", [
     ("p", "Som ejer har du ansvaret for, at anlægget ikke skærmer for eller generer naboer eller trafikanter, fx ved <strong>spejling eller blænding</strong>, og for at følge leverandørens forskrifter.", ["fre_sol"]),
   ]),
   ("BBR og hvem du kontakter", [
     ("p", "Kræver anlægget ikke tilladelse, skal du sende <strong>areal og ydelse til BBR</strong>, når det er sat op. Skal du søge, vælger du 'Faste konstruktioner, som ikke er en bygning' i Byg og Miljø. Byg i Center for Teknik og Miljø har telefon 98 45 63 98.", ["fre_sol"]),
   ]),
  ],
  "faq": [
   ("Kræver solceller byggetilladelse i Frederikshavn Kommune?", "Som udgangspunkt ikke på taget af dit hus, når anlægget overholder bygningsreglementets højde- og afstandskrav. Stativer på jorden, etageboliger, erhverv, bevaringsværdige og fredede ejendomme og ejendomme inden for bygge- og naturbeskyttelseslinjer kræver byggetilladelse.", ["fre_sol"]),
   ("Må jeg vinkle solcellerne op fra taget i Frederikshavn?", "Det kan kræve byggetilladelse. Kommunen nævner netop stativer og bærebeslag, der vinkler solcellerne fra tagfladen, som et eksempel på anlæg, der ikke overholder højde- og afstandskravene.", ["fre_sol"]),
   ("Skal mine solceller registreres i BBR?", "Ja. Også når anlægget ikke kræver tilladelse, skal du sende oplysninger om areal og ydelse til BBR, når det er sat op.", ["fre_sol"]),
   ("Hvem kontakter jeg om solceller i Frederikshavn Kommune?", "Byg i Center for Teknik og Miljø på 98 45 63 98.", ["fre_sol"]),
  ],
}
SOL_REG["hedensted"] = {
  "kw": "solceller hedensted kommune / byggetilladelse solceller hedensted",
  "evidence": "Hedensted Kommunes side 'Solceller' beskriver reglerne for solceller på tag og på stativ/terræn i by- og landzone, hvad ansøgningen skal indeholde og hvem man kontakter (tjekket 4/11 2026).",
  "intro": "Hedensted Kommune kræver hverken byggetilladelse eller landzonetilladelse til solceller på taget af dit hus, når de følger tagets hældning uden stativ, ikke reflekterer, overholder byggeretten og kun forsyner din egen ejendom. Anlæg på stativ på jorden kræver tilladelse. Her er reglerne og hvordan du søger.",
  "sections": [
   ("Fem betingelser for solceller på taget uden tilladelse", [
     ("ul", [("Solcellerne <strong>følger tagets hældning</strong> og monteres ikke på stativ.", ["hed_sol"]),
             ("Panelerne er <strong>ikke af reflekterende materiale</strong>.", ["hed_sol"]),
             ("Anlægget overholder <strong>byggeretten</strong>.", ["hed_sol", "br18_179"]),
             ("Anlægget forsyner <strong>kun din egen ejendom</strong>.", ["hed_sol"]),
             ("Servitutter og lokalplan siger ikke noget andet. Er bygningen bevaringsværdig eller fredet, så kontakt plan@hedensted.dk.", ["hed_sol"])]),
   ]),
   ("Solceller på stativ eller terræn", [
     ("p", "Et anlæg på <strong>stativ på jorden</strong> kræver byggetilladelse og i landzone også landzonetilladelse. I landzone skal anlægget placeres i tilknytning til boligen, dvs. <strong>højst 20 meter</strong> fra den og i samme terrænhøjde, det må ikke ligge i områder med særlige landskabelige udpegninger, og det må kun forsyne din egen ejendom.", ["hed_sol"]),
   ]),
   ("Det skal stå i ansøgningen", [
     ("p", "Søger du i Byg og Miljø, skal du krydse af ved landzone og begrunde ansøgningen med <strong>farve, højde, længde og bredde</strong>, afstande til skel og byggelinjer og, for anlæg på terræn, afstanden til husets øvrige bygninger. På kommunens webkort kan du se, om ejendommen er omfattet af fredning, naturbeskyttelse eller landskabelige udpegninger.", ["hed_sol"]),
   ]),
   ("BBR og hvem du kontakter", [
     ("p", "Når anlægget er sat op, sender du areal og ydeevne til <strong>BBR@Hedensted.dk</strong>. Spørgsmål om byggetilladelse: byg@hedensted.dk eller 79 75 56 05. Landzone: landskab@hedensted.dk. Lokalplan: plan@hedensted.dk eller 79 75 56 06.", ["hed_sol"]),
   ]),
  ],
  "faq": [
   ("Kræver solceller byggetilladelse i Hedensted Kommune?", "Ikke på taget, når panelerne følger tagets hældning uden stativ, ikke reflekterer, overholder byggeretten og kun forsyner din egen ejendom, og servitutter og lokalplan ikke siger andet.", ["hed_sol"]),
   ("Skal jeg have landzonetilladelse til solceller på taget i Hedensted?", "Nej, ikke når betingelserne for solceller på taget er opfyldt. Står anlægget på stativ på jorden i landzone, kræver det både byggetilladelse og landzonetilladelse.", ["hed_sol"]),
   ("Hvor langt fra huset må et jordanlæg stå i landzone?", "Højst 20 meter fra boligen og i samme terrænhøjde, ifølge Hedensted Kommune.", ["hed_sol"]),
   ("Hvem kontakter jeg om solceller i Hedensted Kommune?", "Byggesager: byg@hedensted.dk eller 79 75 56 05. Lokalplaner og bevaringsværdige huse: plan@hedensted.dk.", ["hed_sol"]),
  ],
}
FV_PAGE["frederikshavn"] = {
  "kw": "fjernvarme frederikshavn / frederikshavn forsyning varme pris / varmepumpe frederikshavn",
  "evidence": "Frederikshavn Forsyning oplyser priser for 2026, tilslutningspris og varmekilder, Frederikshavn Varmes årsrapport 2025 beskriver ringledningen, og kommunens varmescreening fra 2022 gennemgår værkerne og naturgas-byerne (tjekket 4/11 2026).",
  "intro": "Næsten to ud af tre huse i Frederikshavn Kommune har fjernvarme fra ni varmeværker fra Skagen til Dybvad. Prisforskellen er stor: et standardhus betaler 12.635 kr. om året i Skagen og 23.350 kr. i Dybvad. Her er status for fjernvarmen, værkernes priser og regnestykket mod en varmepumpe.",
  "status": [
   ("<strong>Pris 2026 i Frederikshavn by:</strong> 873,75 kr. pr. MWh inkl. moms plus arealbidrag på 23,75 kr. pr. m² i BBR og et målerabonnement fra 875 kr. om året.", ["ffv_pris"]),
   ("<strong>Tilslutning:</strong> 27.500 kr. inkl. moms for private med op til 15 meter stikledning. Forsyningen oplyser erfaringsmæssigt ca. 30.000 kr. for de indvendige installationer.", ["ffv_faa"]),
   ("<strong>Ringledning:</strong> Frederikshavn Varmes 4,8 km ringledning, der også kan forsyne Gærum, ventes sat i drift ultimo 2026.", ["ffv_aar25"]),
   ("<strong>Naturgas-byerne:</strong> Ålbæk, Jerup, Kvissel, Ravnshøj og Haldbjerg/Vangen havde ingen fjernvarmeplaner i screeningen fra 2022, og her skal ejendommene senest i 2035 have en anden varmeforsyning.", ["fre_scr"]),
  ],
  "local_take": "Skagen Varmeværk er nr. 23 og Sæby Varmeværk nr. 54 af 374 værker i Forsyningstilsynets statistik regnet fra det billigste, mens Frederikshavn Varme som nr. 224 ligger over landsgennemsnittet, og Dybvad Varmeværk er nr. 346. Har du fjernvarme i Skagen eller Sæby, er der sjældent penge i at skifte. Har du gasfyr i en af naturgas-byerne, peger kommunens egen screening på individuel opvarmning eller en fælles løsning, og så er en varmepumpe det oplagte alternativ.",
  "contact": ("Frederikshavn Forsyning, Varme", "98 29 90 00 · varme@forsyningen.dk", "ffv_faa"),
  "faq": [
   ("Hvad koster fjernvarme i Frederikshavn?", "Ifølge Forsyningstilsynets statistik pr. 31. januar 2026 koster et standardhus på 130 m² med 18,1 MWh 18.419 kr. om året inkl. moms hos Frederikshavn Varme, 12.635 kr. hos Skagen Varmeværk og 14.032 kr. hos Sæby Varmeværk. Landsgennemsnittet er 16.953 kr.", ["ft_pris"]),
   ("Hvad koster det at blive tilsluttet fjernvarme i Frederikshavn?", "Frederikshavn Forsyning tager 27.500 kr. inkl. moms for private med op til 15 meter stikledning. Graver du selv renden, får du 318,75 kr. i rabat pr. meter. Dertil kommer den indvendige installation, som forsyningen erfaringsmæssigt anslår til ca. 30.000 kr.", ["ffv_faa"]),
   ("Hvorfor får Ålbæk ikke fjernvarme?", "Ålbæk ligger ca. 20 km fra både Skagen Varmeværk og Frederikshavn Varme, og kommunens screening fra 2022 vurderede, at det ikke er økonomisk fordelagtigt at føre en ledning dertil. Med 497 ejendomme med naturgas og 68 med oliefyr bør det ifølge screeningen afklares, om der er interesse for en fælles løsning.", ["fre_scr"]),
  ],
}
FV_PAGE["hedensted"] = {
  "kw": "fjernvarme hedensted / hedensted fjernvarme pris 2026 / varmepumpe hedensted",
  "evidence": "Hedensted Fjernvarme oplyser priser og prisstigningen pr. 1/11 2026 og planerne for en spildevandsvarmepumpe, Dansk Fjernvarme beskriver Daugård-projektet, og Hedensted Kommune beskriver fjernvarmeselskaberne og status for varmeplanen (tjekket 4/11 2026).",
  "intro": "36 % af husene i Hedensted Kommune har fjernvarme, og hvert femte har naturgas. Fjernvarmen er dyr her: alle de værker i kommunen, vi har fundet i Forsyningstilsynets statistik, ligger over landsgennemsnittet, og Hedensted Fjernvarme har hævet prisen fra 1. november 2026. Her er status, værkernes priser og regnestykket mod en varmepumpe.",
  "status": [
   ("<strong>Pris fra 1/11 2026:</strong> Hedensted Fjernvarme hæver det variable bidrag fra 850 til 931,25 kr. pr. MWh og det faste bidrag fra 32,50 til 33,75 kr. pr. m² inkl. moms. Priserne gælder også pr. 1. januar 2027.", ["hfj_pris"]),
   ("<strong>Daugård:</strong> 330 nye forbrugere kobles på fra Hedensted. Med over 100 % tilmeldte blev tilslutningen gratis, og projektet ventedes færdigt i 2. kvartal 2026.", ["df_daug"]),
   ("<strong>Spildevandsvarmepumpe:</strong> en 4 MW varmepumpe ved Hedensted Spildevand i Daugård skal fra efteråret 2027 levere ca. 20.000 MWh om året og skære naturgassens andel af produktionen fra 20 til 4 %.", ["hfj_spild"]),
   ("<strong>Varmeplanen:</strong> tre af de fire byområder, som varmeplanen fra 2022 pegede på til fjernvarme, er taget ud igen.", ["hed_red"]),
  ],
  "local_take": "RMU Forsyning i Rask Mølle og Uldum er det billigste af værkerne i kommunen i Forsyningstilsynets statistik, men som nr. 203 af 374 ligger det stadig over landsgennemsnittet, og Hedensted Fjernvarme var nr. 295 allerede før prisstigningen i november. Har du gasfyr uden for fjernvarmeområderne, er en luft til vand-varmepumpe det oplagte valg. Bor du i et fjernvarmeområde, så regn begge løsninger igennem, og husk at et tilbud om fjernvarme altid er frivilligt.",
  "contact": ("Hedensted Fjernvarme", "75 89 10 12 · admin@hedensted-fjernvarme.dk", "hfj_pris"),
  "faq": [
   ("Hvad koster fjernvarme i Hedensted?", "Ifølge Forsyningstilsynets statistik pr. 31. januar 2026 koster et standardhus på 130 m² med 18,1 MWh 20.397 kr. om året inkl. moms hos Hedensted Fjernvarme, 18.121 kr. hos RMU Forsyning og 22.581 kr. hos Løsning Fjernvarme. Landsgennemsnittet er 16.953 kr. Hedensted Fjernvarme har siden hævet prisen pr. 1. november 2026.", ["ft_pris", "hfj_pris"]),
   ("Hvor meget naturgas bruger Hedensted Fjernvarme?", "Hedensted Fjernvarme forventer, at den nye spildevandsvarmepumpe fra 2027 kan reducere naturgassens andel af fjernvarmeproduktionen fra 20 til 4 %. Projektet koster knap 41 mio. kr.", ["hfj_spild"]),
   ("Kan jeg blive tvunget på fjernvarme i Hedensted Kommune?", "Nej. Kommunen skriver, at et tilbud om fjernvarme altid er frivilligt. Ligger din bolig i et område, der er udlagt eller planlagt til fjernvarme, har fjernvarmeselskabet til gengæld ret og pligt til at forsyne dig, hvis du ønsker det.", ["hed_fjv"]),
  ],
}

# ---------- daglig by-rutine 5. nov. 2026: Ringkøbing og Helsingør ----------
# Forsyningstilsynet, prisstatistik januar 2026 (CSV): Ringkøbing-Skjern = værkerne med postnumre i kommunen (6880/6893/6900/6920/6940/6950/6960/6971/6980).
# Kibæk (6933, Herning), Ørnhøj (6973, Herning) og værkerne på 6990 (Holstebro) er udeladt. Helsingør = Forsyning Helsingør Varme (3000) og Hornbæk Fjernvarme (3100).
FV_PRICES["ringkoebing"] = [("Hvide Sande Fjernvarme", "6960", "3.478", "56"), ("Tim Kraftvarmeværk", "6980", "12.093", "437"), ("Skjern Fjernvarme", "6900", "12.390", "531"), ("Videbæk Varme", "6920", "12.754", "543"), ("Lem Varmeværk", "6940", "14.106", "650"), ("Ringkøbing Fjernvarmeværk", "6950", "14.415", "562"), ("Tarm Varmeværk", "6880", "16.855", "707"), ("Troldhede Kraftvarmeværk", "6920", "20.292", "925"), ("Hemmet Varmeværk", "6893", "20.604", "793"), ("Spjald Fjernvarme- og Vandværk", "6971", "24.736", "993")]
FV_PRICES["helsingoer"] = [("Forsyning Helsingør Varme", "3000", "16.628", "567"), ("Hornbæk Fjernvarme", "3100", "18.310", "728")]
SOL_REG["ringkoebing"] = {
  "kw": "solceller ringkøbing-skjern kommune / tilladelse solceller ringkøbing",
  "evidence": "Ringkøbing-Skjern Kommunes gældende retningslinjer for mindre solcelleanlæg i Kommuneplan 2021-2033 (gengivet uændret i forslaget til tillæg nr. 46 fra 2024) og kommunens side om byggetilladelse (tjekket 5/11 2026).",
  "intro": "Ringkøbing-Skjern Kommune kræver som udgangspunkt ikke tilladelse til mindre solcelleanlæg på taget, men kommuneplanen stiller krav om, at panelerne har samme hældning som taget. I områder med bevarende lokalplan, fx Ringkøbings indre by og Vedersø Klit, kan solceller på bygningen være udelukket. Her er reglerne og hvem du kontakter.",
  "sections": [
   ("Solceller på taget: kommuneplanens krav", [
     ("ul", [("Mindre anlæg på <strong>tagflader</strong> kræver som udgangspunkt ikke tilladelse hos kommunen.", ["rks_kp"]),
             ("Solceller og solfangere skal have <strong>samme hældning som taget</strong> og nedfældes i tagfladen.", ["rks_kp"]),
             ("Er panelets højde <strong>under 100 cm</strong>, må det dog anbringes oven på tagfladen.", ["rks_kp"]),
             ("Panelerne kan også bygges ind i facade og tag som en del af arkitekturen.", ["rks_kp"])]),
   ]),
   ("Bevarende lokalplaner: indre by og Vedersø Klit", [
     ("p", "Nogle bygninger er omfattet af en <strong>bevarende lokalplan</strong> eller lignende, hvor solceller på bygningen ikke er en mulighed. Kommunen nævner selv bygninger i den indre by i Ringkøbing og ved Vedersø Klit. Find lokalplanen for din ejendom, før du bestiller.", ["rks_kp"]),
   ]),
   ("Solceller på jorden og i sommerhusområder", [
     ("p", "Det kræver tilladelse at sætte solceller op på <strong>terræn</strong>. I sommerhusområder gives der som udgangspunkt ikke tilladelse til anlæg på terræn, og i landzone skal anlægget helst ligge i tilknytning til de eksisterende bygninger og haven.", ["rks_kp"]),
   ]),
   ("Hvem du kontakter", [
     ("p", "Land, By og Kultur, Smed Sørensens Vej 1 i Ringkøbing, på 99 74 15 15 eller land.by.kultur@rksk.dk. På byggesags- og landzoneområdet har kommunen midlertidigt telefontid om mandagen kl. 10-17.", ["rks_byg"]),
   ]),
  ],
  "faq": [
   ("Kræver solceller tilladelse i Ringkøbing-Skjern Kommune?", "Ikke som udgangspunkt for mindre anlæg på taget. Anlæg på terræn kræver tilladelse, og bevarende lokalplaner kan udelukke solceller på bygningen.", ["rks_kp"]),
   ("Må solcellerne stå på stativ på mit tag i Ringkøbing?", "Kommuneplanen siger, at panelerne skal have samme hældning som taget og nedfældes i tagfladen. Kun paneler under 100 cm i højden må anbringes oven på tagfladen. Vil du vinkle panelerne op, så spørg kommunen først.", ["rks_kp"]),
   ("Kan jeg få solceller på jorden ved mit sommerhus ved Vestkysten?", "Som udgangspunkt ikke. Ringkøbing-Skjern Kommune giver ifølge kommuneplanen som udgangspunkt ikke tilladelse til solcelleanlæg på terræn i sommerhusområder.", ["rks_kp"]),
   ("Hvem kontakter jeg om solceller i Ringkøbing-Skjern Kommune?", "Land, By og Kultur på 99 74 15 15 eller land.by.kultur@rksk.dk.", ["rks_byg"]),
  ],
}
SOL_REG["helsingoer"] = {
  "kw": "solceller helsingør kommune / byggetilladelse solceller helsingør",
  "evidence": "Helsingør Kommunes vejledning 'Energiløsninger' beskriver reglerne for solceller på enfamiliehuse, etageboliger og erhverv i by- og landzone samt solcelleparker på jorden (tjekket 5/11 2026).",
  "intro": "Helsingør Kommune skriver, at solceller på enfamiliehuse, dobbelthuse, rækkehuse og sommerhuse er undtaget for byggetilladelse efter BR18, når byggerettens højde- og afstandsbestemmelser og de brandmæssige løsninger er overholdt. En lokalplan kan kræve ikke-reflekterende paneler, og anlæg på jorden kræver altid tilladelse. Her er reglerne og hvem du kontakter.",
  "sections": [
   ("Huse: undtaget for byggetilladelse på betingelser", [
     ("ul", [("Gælder <strong>enfamiliehuse</strong>, herunder stuehuse i landzone, dobbelthuse, rækkehuse og sommerhuse.", ["hel_sol"]),
             ("Anlægget skal overholde byggerettens <strong>højde- og afstandsbestemmelser</strong> i BR18 §§ 166-195.", ["hel_sol", "br18_179"]),
             ("Anlægget skal følge de brandmæssige <strong>præ-accepterede løsninger</strong>.", ["hel_sol"])]),
   ]),
   ("Lokalplan: ikke-reflekterende paneler", [
     ("p", "En lokalplan kan regulere, om der må sættes <strong>reflekterende materialer</strong> på husene. Så kan du kun bruge solceller, der ikke reflekterer. Kommunens lokalplanportal viser de gældende lokalplaner og byplanvedtægter.", ["hel_sol"]),
   ]),
   ("Etageboliger, erhverv og anlæg på jorden", [
     ("p", "På etageboliger og erhverv i byzone er solceller undtaget for byggetilladelse, hvis anlægget ikke øger lasten på tagkonstruktionen med <strong>mere end 5 %</strong>, dokumenteret ved en beregning. I landzone kræver de landzonetilladelse. Solcelleanlæg på jorden kræver altid byggetilladelse, og fritstående anlæg i landzone kan som udgangspunkt ikke forvente landzonetilladelse.", ["hel_sol"]),
   ]),
   ("Hvem du kontakter", [
     ("p", "Center for By, Land og Vand, Stengade 59 i Helsingør, på 49 28 28 28 eller blv@helsingor.dk. Kommunens vejledning dækker kun bygge- og planloven, ikke afregningen af strømmen.", ["hel_sol"]),
   ]),
  ],
  "faq": [
   ("Kræver solceller byggetilladelse i Helsingør Kommune?", "Ikke på et enfamiliehus, dobbelthus, rækkehus eller sommerhus, når anlægget overholder byggerettens højde- og afstandsbestemmelser og de brandmæssige løsninger. Anlæg på jorden kræver altid byggetilladelse.", ["hel_sol"]),
   ("Må jeg bruge almindelige solcellepaneler, hvis min lokalplan forbyder reflekterende materialer?", "Nej. Regulerer lokalplanen reflekterende materialer, skal du bruge solceller, der ikke reflekterer, ifølge Helsingør Kommune.", ["hel_sol"]),
   ("Gælder reglerne også for sommerhuse i Hornbæk og Dronningmølle?", "Ja, kommunens undtagelse gælder også sommerhuse, når højde-, afstands- og brandkravene er overholdt. Tjek lokalplanen for dit område.", ["hel_sol"]),
   ("Hvem kontakter jeg om solceller i Helsingør Kommune?", "Center for By, Land og Vand på 49 28 28 28 eller blv@helsingor.dk.", ["hel_sol"]),
  ],
}
FV_PAGE["ringkoebing"] = {
  "kw": "fjernvarme ringkøbing / fjernvarme ringkøbing-skjern pris / varmepumpe ringkøbing",
  "evidence": "Forsyningstilsynets prisstatistik januar 2026 for de ti værker i kommunen, Dansk Fjernvarmes artikler om Ringkøbing Fjernvarmes flisværk og Hvide Sande Fjernvarmes priser, og kommunens strategiske varmeplan og varmeinfo (tjekket 5/11 2026).",
  "intro": "Tre ud af fem huse i Ringkøbing-Skjern Kommune har fjernvarme, og prisforskellen mellem værkerne er enorm: i Forsyningstilsynets statistik fra januar 2026 betalte et standardhus 3.478 kr. om året i Hvide Sande og 24.736 kr. i Spjald. Her er status for fjernvarmen, de ti værkers priser og regnestykket mod en varmepumpe.",
  "status": [
   ("<strong>Hvide Sande:</strong> fra 1. april 2026 er varmeprisen 12,50 kr. pr. MWh, og det faste bidrag er nul resten af året. Et standardhus på 125 m² med 13,4 MWh betaler dermed 1.284 kr. for 2026.", ["hsfv_ned", "df_hsfv"]),
   ("<strong>Ringkøbing:</strong> Ringkøbing Fjernvarme har bygget en 10,5 MW fliskedel og en absorptionsvarmepumpe, der skal fjerne mindst 3 mio. m³ naturgas om året. Naturgas udgjorde 41 % af energimixet før.", ["df_rfv"]),
   ("<strong>Strategisk varmeplan:</strong> kommunen er delt i områder med fjernvarme, godkendt udrulning, potentiale for fjernvarme og områder med individuelle løsninger. I det åbne land kommer der ikke fjernvarme.", ["rks_varme", "rks_svp"]),
   ("<strong>Fjelstervang:</strong> taget ud som muligt fjernvarmeområde i juni 2026 efter for lidt tilslutning.", ["rks_fjel"]),
  ],
  "local_take": "Hvide Sande Fjernvarme er nr. 1 af 374 værker i Forsyningstilsynets statistik, og Tim, Skjern og Videbæk ligger alle i top 25. Har du fjernvarme fra et af dem, er der sjældent penge i en varmepumpe. Spjald Fjernvarme er derimod nr. 360, og Troldhede og Hemmet ligger også et godt stykke over landsgennemsnittet. Har du oliefyr i en landsby eller i det åbne land, peger kommunens egen varmeplan på individuelle løsninger, og så er en luft til vand-varmepumpe det oplagte valg.",
  "contact": ("Ringkøbing-Skjern Kommune, varmeplan", "varme@rksk.dk", "rks_varme"),
  "faq": [
   ("Hvad koster fjernvarme i Ringkøbing-Skjern Kommune?", "Ifølge Forsyningstilsynets statistik pr. 31. januar 2026 koster et standardhus på 130 m² med 18,1 MWh 14.415 kr. om året inkl. moms hos Ringkøbing Fjernvarmeværk, 12.390 kr. hos Skjern Fjernvarme og 16.855 kr. hos Tarm Varmeværk. Landsgennemsnittet er 16.953 kr.", ["ft_pris"]),
   ("Hvorfor er fjernvarmen så billig i Hvide Sande?", "Hvide Sande Fjernvarme ejer tre vindmøller på havnen og laver i dag 95 % af varmen med solvarme, elkedler og varmepumper. Indtægter fra elmarkedet og systemydelser gjorde det muligt at sætte prisen ned til 12,50 kr. pr. MWh fra 1. april 2026, hvilket værket selv kalder under produktionsprisen.", ["df_hsfv", "hsfv_ned"]),
   ("Hvad gør jeg, hvis min landsby ikke får fjernvarme?", "Kommunen henviser til individuelle løsninger som varmepumper eller mindre fællesanlæg. Anlæg under 250 kW indfyret effekt er ikke omfattet af varmeforsyningsloven og er derfor lettere at etablere, og borger- og sogneforeninger kan søge kommunens pulje til borgermøder om fælles varme.", ["rks_varme"]),
  ],
}
FV_PAGE["helsingoer"] = {
  "kw": "fjernvarme helsingør / forsyning helsingør fjernvarme pris / varmepumpe helsingør",
  "evidence": "Forsyning Helsingør oplyser de godkendte og kommende fjernvarmeområder, status for udbygningen i september 2026, tilslutningspris og priseksempel, og Forsyningstilsynets prisstatistik januar 2026 viser prisen hos Forsyning Helsingør og Hornbæk Fjernvarme (tjekket 5/11 2026).",
  "intro": "Kun 36 % af husene i Helsingør Kommune har fjernvarme, og næsten lige så mange har naturgas. Forsyning Helsingør udbygger i fem godkendte områder frem til 2028, så for mange gasfyr-ejere er spørgsmålet, om fjernvarmen kommer i tide. Her er status, priserne og regnestykket mod en varmepumpe.",
  "status": [
   ("<strong>Godkendte områder:</strong> Søhelte-kvarteret (færdigt), Marienlyst-kvarteret (under afslutning), Helsingør Bykerne og Yderområde 1 og 2 (i gang), Yderområde 3 (projekteres efteråret 2026), Yderområde 4 (tilbud i 2026) og Espergærde C (2023-2028).", ["fh_status", "fh_esp"]),
   ("<strong>Efter 2028:</strong> yderligere dele af Helsingør, Espergærde og Snekkersten er med i de kommende planer, hvis økonomien er sund og tilslutningen stor nok.", ["fh_nye", "fh_status"]),
   ("<strong>Tilslutning:</strong> 33.750 kr. for et enfamiliehus inkl. gravearbejde og stikledning, eller 687,50 kr. om måneden i fem år. Fjernvarmeenheden koster typisk 40.000-45.000 kr. eller 350 kr. om måneden i abonnement.", ["fh_pris"]),
   ("<strong>Espergærde C:</strong> udbygningen kræver, at mindst 60 % i området tilslutter sig.", ["fh_esp"]),
  ],
  "local_take": "Forsyning Helsingør er nr. 153 af 374 værker i Forsyningstilsynets statistik og ligger lidt under landsgennemsnittet, mens Hornbæk Fjernvarme som nr. 215 ligger over. Har du gasfyr i et af de fem godkendte områder, er fjernvarme det oplagte første tjek. Ligger dit hus uden for både de godkendte og de kommende områder, har Forsyning Helsingør ikke meldt nogen plan ud for dig, og så er en luft til vand-varmepumpe det realistiske alternativ, når gasfyret skal skiftes.",
  "contact": ("Forsyning Helsingør", "48 40 50 50", "fh_nye"),
  "faq": [
   ("Hvad koster fjernvarme i Helsingør?", "Ifølge Forsyningstilsynets statistik pr. 31. januar 2026 koster et standardhus på 130 m² med 18,1 MWh 16.628 kr. om året inkl. moms hos Forsyning Helsingør og 18.310 kr. hos Hornbæk Fjernvarme. Landsgennemsnittet er 16.953 kr. Forsyning Helsingør oplyser selv 13.623,18 kr. om året for en gennemsnitsfamilie i et standardparcelhus.", ["ft_pris", "fh_pris"]),
   ("Hvor mange har fået fjernvarme i Helsingør siden 2022?", "Forsyning Helsingør havde ved udgangen af juli 2026 registreret 1.146 nye fjernvarmestik siden 2022. Ét stik kan dække mange husstande, fx en boligforening med 50-200 boliger.", ["fh_status"]),
   ("Hvor meget sparer jeg ved at skifte fra gas til fjernvarme i Helsingør?", "Forsyning Helsingør skriver, at de fleste huse kan spare 5-25 % på varmeregningen ved at skifte fra naturgas til fjernvarme. Regn også en varmepumpe igennem, hvis dit område ikke står på planen.", ["fh_nye"]),
  ],
}
