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
  "svc": "varmepumpe", "crumb": "Pris",
  "kw": "luft til vand varmepumpe pris / pris inkl montering",
  "evidence": "Autocomplete 'luft til vand varmepumpe pris': 10 forslag (bl.a. 'inkl montering', 'inkl montering jylland', '200m2', '250 m2', '300 m2'). PAA: 'Hvad koster en varmepumpe til et hus på 150 m2?', 'Kan det betale sig at få en luft til vand varmepumpe?', 'Hvad koster en luft til vand varmepumpe om året?'. Bylokale varianter ('luft til vand varmepumpe pris odense' osv.) gav INGEN forslag i de 7 byer, så der er ingen pris-side pr. by.",
  "title": "Luft til vand-varmepumpe pris 2026 inkl. montering",
  "desc": "En luft til vand-varmepumpe koster typisk 90.000-150.000 kr. inkl. montering. Se driftsudgift, tilskud, ekstraposter og hvad tilbuddet skal vise.",
  "h1": "Hvad koster en luft til vand-varmepumpe i 2026?",
  "intro": "Prisen på en luft til vand-varmepumpe afhænger af husets varmebehov, dit varmesystem og hvor meget ekstra arbejde der skal til. Vi har ikke fundet kilder, der viser regionale prisforskelle i Jylland eller på Fyn. Her er prisspændene fra to kilder, hvad varmen koster om året, og hvordan tilskuddet påvirker regnestykket.",
  "sections": [
   ("Pris inkl. montering", [
     ("table", ["Type", "Pris inkl. montering", "Kilde"],
      [["Luft til vand", "typisk 100.000-130.000 kr.", "SparEnergi"], ["Luft til vand", "ca. 90.000-150.000 kr.", "Energisparer.dk"], ["Jordvarme", "ca. 120.000-180.000 kr.", "Energisparer.dk"], ["Luft til luft (supplement)", "ca. 12.000-25.000 kr.", "Energisparer.dk"]], ["se_vp", "es_vp"]),
     ("p", "Energisparer.dk omregner til ca. 9.000-15.000 kr. pr. kW, fra ca. 90.000 kr. for 6 kW til ca. 150.000 kr. for 16 kW. Hvor mange kW dit hus skal bruge, afhænger af varmetabet, ikke kun af antallet af kvadratmeter. Derfor bør installatøren dimensionere anlægget.", ["es_vp"]),
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
   ("Hvad koster en varmepumpe til et hus på 150 m²?", "Vi har ikke fundet en pålidelig kilde til priser pr. m². Effekten skal passe til husets varmetab, og prisen ligger typisk inden for ca. 90.000-150.000 kr. Bed installatøren om en beregning af varmebehovet.", ["es_vp"]),
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
