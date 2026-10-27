# -*- coding: utf-8 -*-
"""v7 (25. okt. 2026): nye emnesider med høj købsintention + kilder.
Samme blokformat som data_sub.NATIONAL. Alle tal har en kilde; vores egne omregninger er markeret som sådan.
Nøglen "updated" styrer den synlige 'Opdateret'-dato og dateModified i JSON-LD."""
UPD = ("25. oktober 2026", "2026-10-25")

TOPIC_S = {
 "se_l2l": ("SparEnergi: skift til luft til luft-varmepumpe (opdateret 14/4 2026)", "https://sparenergi.dk/privat/tid-til-skifte-varmekilde/bliv-klogere-paa-luft-til-luft-varmepumpen"),
 "se_l2l_pdf": ("SparEnergi: energiløsning, luft-luft-varmepumpe (PDF, jan. 2024)", "https://sparenergi.dk/sites/default/files/media/documents/2024-01/Luft-luftvarmepumpe_OK.pdf"),
 "mst_jv": ("Miljøstyrelsen: jordvarmeanlæg (tilladelse og anmeldelse)", "https://mst.dk/erhverv/groen-produktion-og-affald/industri/regulering-af-saerlige-brancher-og-aktiviteter/jordvarmeanlaeg"),
 "mst_olie": ("Miljøstyrelsen: olietanke (sløjfning)", "https://mst.dk/borger/hjem-og-have/haven-og-udendoers-miljoe/olietanke"),
 "naes_fv": ("TV2 Øst: Næstved Fjernvarme dropper fjernvarme i Holsted Syd", "https://www.tv2east.dk/naestved/fjernvarme-droppes-efter-for-lav-tilmelding-8e89b"),
 "ran_olie": ("Randers Kommune: sløjfning af olietank (opdateret 13/3 2026)", "https://www.randers.dk/erhverv/affald-og-miljoe/miljoe/olie-og-kemikalier/olietanke/sloejfning/"),
 "be_guide": ("Byggeri og Energi: Solcelleguide (april 2026, PDF)", "https://byggeriogenergi.dk/sites/default/files/2026-04/Solcelleguide_ByggeriogEnergi.pdf"),
 "aar_sol": ("Aarhus Kommune: solceller på grunde med énfamiliehus, rækkehuse mv.", "https://aarhus.dk/borger/bolig-byggeri-og-miljoe/byggeri/solceller-grunde-med-enfamiliehus-raekkehuse-mv/"),
 "vor_sol": ("Vordingborg Kommune: solceller og vindmøller", "https://www.vordingborg.dk/borger/bolig-og-byggeri/byggeri-og-bbr/solceller-og-vindmoeller"),
 "installator": ("Installatør 14/10 2026: 19.000 har fået tilskud til varmepumpe, nu er puljen næsten tømt", "https://www.installator.dk/19000-har-faet-tilskud-til-varmepumpe-nu-er-puljen-naesten-tomt"),
 "cvr_virk": ("CVR (Erhvervsstyrelsen): ANGU ApS, CVR 40086560", "https://datacvr.virk.dk/enhed/virksomhed/40086560"),
}

T = {}

T["/varmepumpe/jordvarme-pris/"] = {
  "svc": "varmepumpe", "crumb": "Jordvarme pris", "updated": UPD,
  "kw": "jordvarme pris / jordvarme pris inkl montering",
  "title": "Jordvarme pris 2026: hvad koster jordvarme inkl. montering?",
  "desc": "Jordvarme koster typisk 120.000-200.000 kr. inkl. montering. Se drift pr. år, tilskud på 27.000 kr., krav til grunden og tilladelse fra kommunen.",
  "h1": "Jordvarme pris 2026: hvad koster det at få jordvarme?",
  "intro": "Jordvarme er den dyreste varmepumpe at etablere, fordi der skal graves jordslanger ned eller bores. Til gengæld har den den laveste driftsudgift. Her er prisspændene fra to kilder, hvad grunden skal kunne, og hvilken tilladelse du skal have fra kommunen.",
  "sections": [
   ("Hvad koster jordvarme inkl. montering?", [
     ("table", ["Kilde", "Jordvarme inkl. montering", "Til sammenligning: luft til vand"],
      [["SparEnergi", "typisk 130.000-200.000 kr.", "typisk 100.000-130.000 kr."], ["Energisparer.dk (okt. 2026)", "ca. 120.000-180.000 kr.", "ca. 90.000-150.000 kr."]], ["se_vp", "es_vp"]),
     ("p", "Energisparer.dk forklarer prisforskellen med, at der skal graves eller bores til jordslangen. En vandret jordslange kræver et stort haveareal, mens lodrette boringer er dyrere, men fylder mindre.", ["es_vp"]),
     ("p", "Med 27.000 kr. fra Varmepumpepuljen giver Energisparer.dk's eksempel på et jordvarmeanlæg til ca. 150.000 kr. en nettopris på ca. 123.000 kr.", ["es_vp"]),
   ]),
   ("Hvad koster jordvarme om året?", [
     ("table", ["Opvarmning af 130 m² hus", "Drift pr. år"],
      [["Jordvarme med gulvvarme", "6.960 kr."], ["Luft til vand med gulvvarme", "7.288 kr."], ["Jordvarme med radiatorer", "8.725 kr."], ["Luft til vand med radiatorer", "9.386 kr."], ["Fjernvarme (vægtet gennemsnit)", "16.953 kr."], ["Gasfyr", "18.433 kr."], ["Oliefyr", "32.388 kr."]], ["es_vp", "bolius_varme"]),
     ("p", "Tallene er Bolius' driftsudgifter for et standardhus på 130 m² med et varmebehov på 18.100 kWh (ajourført 9. september 2026). Det er driften alene. Med afskrivning, service og rente regner Bolius 19.530-20.750 kr. om året for jordvarme, fordi anlægget er dyrt at etablere.", ["bolius_varme"]),
   ]),
   ("Kan din grund bruges til jordvarme?", [
     ("ul", [("SparEnergi skriver, at jordvarme kræver mindst 300 m² ubebygget grund, medmindre du får vertikal jordvarme (boringer).", ["se_vp"]),
             ("Jordvarme giver både rumvarme og varmt vand og kræver radiatorer eller gulvvarme med vand, ligesom en luft til vand-varmepumpe.", ["se_vp"]),
             ("Anlægget må ikke overdækkes, så det bliver svært at komme til jordslangerne, fx med bygninger eller faste installationer.", ["mst_jv"])]),
   ]),
   ("Tilladelse fra kommunen", [
     ("p", "Jordslangerne indeholder frostsikringsvæske og kan forurene jord og grundvand, hvis de bliver utætte. Derfor skal kommunen give tilladelse, før du etablerer et jordvarmeanlæg.", ["mst_jv"]),
     ("p", "Ikke-industrielle, terrænnære anlæg uden for områder med særlige drikkevandsinteresser og indvindingsoplande skal kun anmeldes, hvis de bruger de frostsikringsmidler, bekendtgørelsen tillader. Det sker via Byg og Miljø. Dybe boringer på 10 meter eller mere vil almindeligvis kræve en VVM-screening.", ["mst_jv"]),
     ("note", "Jordslangerne skal efterses efter første driftsår. Har varmepumpen mere end 1 kg kølemiddel, kræver Arbejdstilsynet desuden et årligt eftersyn.", ["mst_jv"]),
   ]),
   ("Tilskud og fradrag", [
     ("p", "Varmepumpepuljen giver 27.000 kr. til jordvarme, det samme som til luft til vand, hvis du skifter olie, gas, elvarme eller biokedel ud i en helårsbolig uden for fjernvarme. Puljen lukker senest 30. november 2026 eller når pengene er brugt. Du kan ikke få håndværkerfradrag for samme varmepumpe, når du får tilskud.", ["se_vpp", "vpp_faq"]),
   ]),
  ],
  "faq": [
   ("Hvad koster jordvarme inkl. montering?", "SparEnergi angiver typisk 130.000-200.000 kr., og Energisparer.dk ca. 120.000-180.000 kr. Boringer er dyrere end vandrette jordslanger.", ["se_vp", "es_vp"]),
   ("Er jordvarme billigere i drift end luft til vand?", "Med Bolius' tal for et 130 m² hus koster jordvarme 8.725 kr. om året mod 9.386 kr. for luft til vand med radiatorer og 7.288 kr. med gulvvarme. Forskellen afhænger mest af dit varmesystem.", ["es_vp", "bolius_varme"]),
   ("Skal jeg søge tilladelse til jordvarme?", "Ja. Kommunen skal give tilladelse, men ikke-industrielle terrænnære anlæg uden for særlige drikkevandsområder skal kun anmeldes. Det sker via Byg og Miljø.", ["mst_jv"]),
   ("Hvor stor skal grunden være?", "SparEnergi skriver mindst 300 m² ubebygget grund, medmindre du vælger vertikal jordvarme med boringer.", ["se_vp"]),
  ],
}

T["/varmepumpe/luft-til-luft-pris/"] = {
  "svc": "varmepumpe", "crumb": "Luft til luft pris", "updated": UPD,
  "kw": "luft til luft varmepumpe pris",
  "title": "Luft til luft-varmepumpe pris 2026 inkl. montering",
  "desc": "En luft til luft-varmepumpe koster typisk 12.000-40.000 kr. inkl. montering. Se hvad den kan erstatte, hvad du sparer, og hvorfor der ikke er tilskud.",
  "h1": "Luft til luft-varmepumpe: pris, besparelse og begrænsninger",
  "intro": "En luft til luft-varmepumpe er den billigste varmepumpe, men den varmer kun luften i de rum, den kan nå, og giver ikke varmt vand. Den passer bedst til huse og sommerhuse med elvarme. Her er priserne, hvad du kan spare, og hvornår en luft til vand-varmepumpe er det bedre valg.",
  "sections": [
   ("Hvad koster en luft til luft-varmepumpe?", [
     ("table", ["Kilde", "Pris inkl. montering"],
      [["SparEnergi (side om luft til luft, april 2026)", "15.000-30.000 kr."], ["SparEnergi (sammenligning af varmepumpetyper, august 2026)", "typisk 30.000-40.000 kr."], ["Energisparer.dk (okt. 2026)", "ca. 12.000-25.000 kr."]], ["se_l2l", "se_vp", "es_vp"]),
     ("p", "Kilderne er ikke enige, og spændet afhænger især af, om du får én indedel eller flere (multisplit). Bed om en pris med montering, rørføring og eventuel ny gruppe i eltavlen.", ["se_l2l", "se_vp", "es_vp"]),
   ]),
   ("Hvad kan den, og hvad kan den ikke?", [
     ("ul", [("Den giver 4-6 gange mere varme for pengene end traditionel elvarme.", ["se_l2l"]),
             ("Den kræver ikke radiatorer eller gulvvarme med vand, og derfor er den et alternativ til elpaneler.", ["se_l2l"]),
             ("Den varmer kun det rum, den er sat op i. Varmen spreder sig mest, hvis der er åbne døre og direkte forbindelse til andre rum.", ["se_l2l"]),
             ("Den kan ikke opvarme dit brugsvand.", ["se_l2l"]),
             ("Udedelen må højst støje 35 dB i skellet til naboerne.", ["se_l2l"])]),
   ]),
   ("Hvad sparer du?", [
     ("p", "SparEnergi skriver, at du kan spare op til 40 % på regningen i forhold til opvarmning med el eller gas. Til sammenligning kan luft til vand og jordvarme spare op til 70 %.", ["se_vp"]),
     ("example", "<strong>SparEnergis regneeksempel:</strong> Et hus på 130 m² fra 1970'erne med elvarme og et samlet forbrug til varme og varmt vand på 19.200 kWh. Varmepumpen (SCOP 3,8) dækker 70 % af rumvarmen, og resten klares med elradiatorer. Forbruget falder til 10.432 kWh, og med en elpris på 1,65 kr. og 1.500 kr. i service sparer huset 12.967 kr. om året. Eksemplet er fra januar 2024, før elafgiften blev sat ned.", ["se_l2l_pdf"]),
     ("p", "I 2026 og 2027 er elafgiften nede på 0,8 øre pr. kWh (ekskl. moms) for alle. Det gør både elvarme og varmepumpe billigere at køre, så besparelsen i kroner er mindre end i eksemplet, mens forholdet mellem dem er det samme.", ["elafgift", "se_sol"]),
   ]),
   ("Ingen tilskud fra Varmepumpepuljen", [
     ("p", "Varmepumpepuljen giver kun tilskud til luft til vand og væske til vand (jordvarme). En luft til luft-varmepumpe er ikke omfattet.", ["se_vpp"]),
     ("p", "Har du radiatorer eller gulvvarme med vand og varmer op med olie eller gas, kan en luft til vand-varmepumpe overtage både rumvarme og varmt vand. Den er dyrere, men kan give 27.000 kr. i tilskud, hvis du opfylder kravene.", ["se_vp", "se_vpp"]),
   ]),
   ("Krav til selve varmepumpen", [
     ("ul", [("Energimærke A+ opfylder EU's ecodesignkrav. Har kølemidlet en lav klimapåvirkning (GWP under 150), er energimærke A tilladt. SparEnergi anbefaler A+++ for den største besparelse.", ["se_l2l"]),
             ("Skal den holde et sommerhus frostfrit, skal den kunne indstilles til en fast temperatur på 8-12 °C.", ["se_l2l", "se_l2l_pdf"]),
             ("Har varmepumpen mere end 1 kg kølemiddel, skal kølekredsen efterses mindst én gang om året af en fagperson.", ["se_l2l"])]),
   ]),
  ],
  "faq": [
   ("Hvad koster en luft til luft-varmepumpe inkl. montering?", "SparEnergi angiver 15.000-30.000 kr. på sin side om luft til luft og typisk 30.000-40.000 kr. i sin sammenligning af typer. Energisparer.dk angiver ca. 12.000-25.000 kr.", ["se_l2l", "se_vp", "es_vp"]),
   ("Kan man få tilskud til luft til luft-varmepumpe?", "Nej. Varmepumpepuljen gælder kun luft til vand og jordvarme.", ["se_vpp"]),
   ("Kan en luft til luft-varmepumpe varme hele huset?", "Sjældent. Den varmer det rum, den står i, og SparEnergi regner i sit eksempel med, at den dækker 70 % af rumvarmen. Resten klares med elvarme.", ["se_l2l", "se_l2l_pdf"]),
   ("Giver luft til luft varmt vand?", "Nej. Brugsvandet skal stadig opvarmes på anden vis, fx med en elvandvarmer.", ["se_l2l"]),
  ],
}

T["/varmepumpe/skift-oliefyr/"] = {
  "svc": "varmepumpe", "crumb": "Skift oliefyr", "updated": UPD,
  "kw": "skift oliefyr til varmepumpe / udskiftning af oliefyr",
  "title": "Skift oliefyr til varmepumpe: pris, tilskud og olietank",
  "desc": "Sådan skifter du oliefyret ud med en varmepumpe: hvad du sparer om året, tilskud på 27.000 kr. (frist 30/11 2026), og hvad du skal gøre med olietanken.",
  "h1": "Skift oliefyr til varmepumpe: økonomi, tilskud og olietanken",
  "intro": "Oliefyret er den dyreste måde at varme et hus op på i Bolius' sammenligning. Derfor er skiftet til en varmepumpe ofte det, der tjener sig hurtigst hjem. Her er tallene, rækkefølgen du skal gøre tingene i, og reglerne for den gamle olietank.",
  "sections": [
   ("Hvad sparer du ved at skifte?", [
     ("table", ["130 m² hus, 18.100 kWh varme", "Drift pr. år", "Inkl. afskrivning, service og rente"],
      [["Oliefyr", "32.388 kr.", "38.153 kr."], ["Luft til vand med radiatorer", "9.386 kr.", "20.561 kr."], ["Luft til vand med gulvvarme", "7.288 kr.", "18.463 kr."]], ["bolius_varme"]),
     ("p", "Energisparer.dk regner en tilbagebetalingstid på ca. 3-5 år fra olie efter tilskud for en luft til vand-varmepumpe med en nettopris på 68.000-113.000 kr. Det er et regneeksempel med 2026-elpriser, ikke et løfte, og service, renter og den højere elafgift fra 2028 er ikke med.", ["es_vp"]),
   ]),
   ("Rækkefølgen: tilbud, tilsagn, kontrakt", [
     ("ul", [("Indhent gerne uforpligtende tilbud først. Du må bare ikke indgå en bindende aftale, før du har tilsagn om tilskud.", ["vpp_ens", "vpp_faq"]),
             ("Søg Varmepumpepuljen på SparEnergi.dk med MitID. Tilskuddet er 27.000 kr. til luft til vand eller jordvarme.", ["se_vpp"]),
             ("Boligen skal være en helårsbolig, du selv ejer, og den må ikke ligge i et område med fjernvarme eller planlagt fjernvarme.", ["se_vpp"]),
             ("Når varmepumpen er installeret, skal du selv søge om udbetaling, senest 1 år efter tilsagnet.", ["vpp_faq"])]),
     ("note", "Puljen lukker senest 30. november 2026 eller tidligere, hvis pengene slipper op. Se <a href=\"/varmepumpe/tilskud/\">status på Varmepumpepuljen</a>.", ["vpp_faq"]),
   ]),
   ("Hvad skal der ske med olietanken?", [
     ("p", "Når olietanken tages varigt ud af brug, fx fordi du får en varmepumpe, skal den sløjfes. Tanken tømmes for restindhold og fjernes helt, eller påfyldningsstuds og udluftningsrør afmonteres, så den er afblændet og ikke kan fyldes igen.", ["mst_olie"]),
     ("p", "Du skal give kommunen besked om, at tanken er sløjfet, og hvordan det er sket. Husk også at afmelde en eventuel automatisk oliepåfyldning. Randers Kommune kræver fx, at anmeldelsen sendes senest 4 uger efter sløjfningen via Byg og Miljø.", ["mst_olie", "ran_olie"]),
     ("p", "Miljøstyrelsen fortolker reglerne sådan, at tanken skal sløjfes umiddelbart efter, at den er taget varigt ud af brug, dvs. inden for højst et par måneder. Randers Kommune advarer om, at forsikringen kan afvise at dække oprensning efter et oliespild, hvis anlægget ikke overholder reglerne.", ["mst_olie", "ran_olie"]),
   ]),
   ("Det skal tilbuddet indeholde", [
     ("ul", [("Nedtagning og bortskaffelse af det gamle fyr og eventuelt olietanken.", ["es_vp"]),
             ("Dimensionering ud fra husets varmebehov og dine radiatorer eller gulvvarme.", ["es_vp"]),
             ("Eventuel opgradering af eltavlen, buffertank, ny varmtvandsbeholder og fundament til udedelen.", ["es_vp"]),
             ("Hvem der søger tilskuddet. Mange installatører hjælper, men ansvaret for at søge i tide er dit.", ["es_vp"])]),
   ]),
  ],
  "faq": [
   ("Hvor meget sparer jeg ved at skifte oliefyr til varmepumpe?", "Med Bolius' tal for et 130 m² hus koster olie 32.388 kr. om året i drift, mens luft til vand med radiatorer koster 9.386 kr.", ["bolius_varme"]),
   ("Kan jeg få tilskud til at skifte oliefyret?", "Ja, 27.000 kr. fra Varmepumpepuljen til luft til vand eller jordvarme, hvis boligen opfylder de 5 krav, og du har tilsagn, før du skriver under. Puljen lukker senest 30. november 2026.", ["se_vpp", "vpp_faq"]),
   ("Skal olietanken fjernes?", "Den skal sløjfes: tømmes og enten fjernes eller afblændes, så den ikke kan fyldes igen. Du skal give kommunen besked.", ["mst_olie"]),
   ("Hvem kan sløjfe olietanken?", "Randers Kommune nævner fx kloakservicefirmaer og vognmænd med speciale i tømning og rensning af olietanke, autoriserede VVS-installatører, smedemestre, oliefyrsmontører og entreprenører.", ["ran_olie"]),
  ],
}

T["/varmepumpe/skift-gasfyr/"] = {
  "svc": "varmepumpe", "crumb": "Skift gasfyr", "updated": UPD,
  "kw": "skift gasfyr til varmepumpe / gasfyr til varmepumpe",
  "title": "Skift gasfyr til varmepumpe: tjek fjernvarme, tilskud og pris",
  "desc": "Før du skifter gasfyret ud: tjek kommunens varmeplan for fjernvarme, tilskud på 27.000 kr. og gratis afkobling fra gasnettet i 2026. Se pris og besparelse.",
  "h1": "Skift gasfyr til varmepumpe: start med varmeplanen",
  "intro": "Mange gasområder skal have fjernvarme i de kommende år. Ligger dit hus i et af dem, kan du ikke få tilskud til en varmepumpe, og fjernvarmen kan være det billigste valg. Derfor er det første skridt at tjekke kommunens varmeplan. Her er rækkefølgen, tallene og afkoblingen fra gasnettet.",
  "sections": [
   ("Trin 1: Kommer der fjernvarme til din adresse?", [
     ("p", "Varmepumpepuljen kræver, at huset hverken ligger i et område med fjernvarme eller i et område, der er besluttet udlagt til fjernvarme. Status afhænger af kommunens varmeplan og ses på Plandata.dk.", ["vpp_puljer", "plandata"]),
     ("p", "SparEnergi har et adresseopslag, der giver et vejledende svar ud fra BBR og Plandata. Du kan først være sikker, når din ansøgning er behandlet. Forkerte oplysninger i Plandata kan kun rettes af kommunen.", ["se_vpp", "vpp_faq"]),
     ("p", "Et planlagt projekt kan også blive opgivet. Næstved Fjernvarme droppede Holsted Syd, da kun 13 % af ejerne havde tilmeldt sig mod et krav på mindst 60 % tilslutning pr. kvadratmeter. Beboerne der må derfor finde en anden varmekilde. Se status for <a href=\"/varmepumpe/vejle/\">Vejle</a>, <a href=\"/varmepumpe/randers/\">Randers</a> og vores andre byer.", ["naes_fv"]),
   ]),
   ("Trin 2: Hvad er billigst for dig?", [
     ("table", ["130 m² hus, 18.100 kWh varme", "Drift pr. år"],
      [["Gasfyr", "18.433 kr."], ["Fjernvarme (vægtet landsgennemsnit)", "16.953 kr."], ["Luft til vand med radiatorer", "9.386 kr."], ["Luft til vand med gulvvarme", "7.288 kr."]], ["bolius_varme", "ft_pris"]),
     ("p", "Energisparer.dk regner med en tilbagebetalingstid på ca. 6-11 år fra gas for luft til vand med en nettopris efter tilskud på 68.000-113.000 kr. Fjernvarmeprisen svinger meget mellem værkerne, så se prisen hos dit lokale værk.", ["es_vp", "ft_pris"]),
   ]),
   ("Trin 3: Tilskud og afkobling fra gasnettet", [
     ("ul", [("Varmepumpepuljen giver 27.000 kr. til luft til vand eller jordvarme. Du skal have tilsagn, før du indgår en bindende aftale. Puljen lukker senest 30. november 2026.", ["se_vpp", "vpp_faq"]),
             ("Afkoblingspuljen dækker Evidas gebyr for at blive koblet af gasnettet, hvis du har et årligt forbrug på 100-6.000 m³. 2026-puljen er den sidste i ordningen.", ["evida_afk"]),
             ("Det er datoen, hvor Evida modtager din opsigelse, der tæller, og opsigelsen er bindende. Du kan ikke få andel i puljen med tilbagevirkende kraft.", ["evida_afk"])]),
     ("note", "Overvej rækkefølgen: få tilsagn om tilskud, skriv kontrakt med installatøren, og opsig gassen, mens Afkoblingspuljen stadig har penge.", ["vpp_faq", "evida_afk"]),
   ]),
   ("Det skal tilbuddet indeholde", [
     ("ul", [("Nedtagning af gasfyret og hvem der tager sig af afkoblingen hos Evida.", ["es_vp", "evida_afk"]),
             ("Dimensionering ud fra husets varmebehov og dine radiatorer eller gulvvarme.", ["es_vp"]),
             ("Eltavle, buffertank, varmtvandsbeholder og fundament til udedelen, hvis det er nødvendigt.", ["es_vp"])]),
   ]),
  ],
  "faq": [
   ("Kan jeg få tilskud til at skifte gasfyr til varmepumpe?", "Ja, 27.000 kr., hvis huset ligger uden for fjernvarme og planlagt fjernvarme, og du har tilsagn, før du skriver under. Puljen lukker senest 30. november 2026.", ["se_vpp", "vpp_faq"]),
   ("Hvad koster det at blive koblet af gasnettet?", "I 2026 kan Afkoblingspuljen dække Evidas gebyr for private husholdninger med et årligt forbrug på 100-6.000 m³. Det er den sidste pulje.", ["evida_afk"]),
   ("Hvordan ser jeg, om der kommer fjernvarme?", "Se kommunens varmeplan på Plandata.dk, eller brug SparEnergis adresseopslag, som bygger på BBR og Plandata.", ["plandata", "se_vpp"]),
   ("Er en varmepumpe billigere end gas?", "Med Bolius' tal koster gas 18.433 kr. om året for et 130 m² hus, mens luft til vand med radiatorer koster 9.386 kr. i drift.", ["bolius_varme"]),
  ],
}

T["/solceller/kan-det-betale-sig/"] = {
  "svc": "solceller", "crumb": "Kan det betale sig?", "updated": UPD,
  "kw": "kan solceller betale sig / kan solceller betale sig 2026",
  "title": "Kan solceller betale sig i 2026? Tilbagebetaling med tal",
  "desc": "Kan solceller betale sig? Se tilbagebetalingstid, hvad strømmen er værd brugt selv og solgt, elafgiften 2026-2028, og hvorfor egetforbruget betyder mest.",
  "h1": "Kan solceller betale sig i 2026?",
  "intro": "Svaret afhænger mest af, hvor meget af strømmen du selv bruger. Strøm, du bruger selv, er værd omtrent dobbelt så meget som strøm, du sælger. Her er regnestykket med kilder, hvad elafgiften betyder i 2026-2028, og hvordan du selv kan regne på dit hus.",
  "sections": [
   ("Kort svar", [
     ("p", "SparEnergi angiver, at et solcelleanlæg typisk sparer 2.500-7.000 kr. om året samlet set, når udgifterne er trukket fra, og at levetiden er ca. 25 år. Energisparer.dk regner med ca. 16 års tilbagebetaling for et 6 kWp-anlæg til ca. 92.000 kr.", ["se_sol", "es_sol"]),
     ("table", ["Anlæg ved 4.000 kWh årligt forbrug", "Simpel tilbagebetalingstid"], [["2 kWp", "12 år"], ["4 kWp", "15 år"], ["6 kWp", "17 år"]], ["se_sol"]),
     ("p", "SparEnergis tabel viser, at et anlæg, der er stort i forhold til forbruget, tjener sig langsommere hjem.", ["se_sol"]),
   ]),
   ("Hvad er en kWh solstrøm værd?", [
     ("table", ["Strømmen bruges", "Værdi pr. kWh (DK1)"],
      [["Selv, i 2026-2027", "ca. 1,13 kr."], ["Selv, fra 2028", "ca. 2,03 kr."], ["Solgt til nettet", "ca. 0,52 kr."]], ["es_sol"]),
     ("p", "Energisparer.dk har regnet med timepriser vægtet efter solproduktion. Forskellen mellem 2027 og 2028 skyldes elafgiften, som er nede på 0,8 øre pr. kWh i 2026 og 2027 og efter gældende lov stiger igen fra 2028.", ["es_sol", "elafgift", "elafgift_lov"]),
     ("example", "<strong>Energisparer.dk's regneeksempel (6 kWp, DK1):</strong> 5.700 kWh om året, heraf 35 % brugt selv. Det giver ca. 2.250 kr. i sparet køb og ca. 1.930 kr. for solgt strøm, i alt ca. 4.200 kr. om året i 2026-2027 og ca. 6.000 kr. fra 2028. Med 50 % egetforbrug er tilbagebetalingen ca. 13-14 år.", ["es_sol"]),
   ]),
   ("Det trækker regnestykket op eller ned", [
     ("ul", [("<strong>Op:</strong> elbil, varmepumpe eller andet forbrug i dagtimerne, fordi strømmen så bruges selv.", ["se_sol", "es_sol"]),
             ("<strong>Op:</strong> et sydvendt tag uden skygge. Hver kWp giver ca. 950-1.050 kWh om året mod syd.", ["es_sol"]),
             ("<strong>Ned:</strong> inverteren skal normalt udskiftes efter ca. 10 år, og den koster typisk 8.000-18.000 kr.", ["se_sol", "es_sol"]),
             ("<strong>Ned:</strong> løbende udgifter til netselskabet på typisk omkring 500 kr. om året.", ["se_sol"]),
             ("<strong>Skat:</strong> salg af overskudsstrøm er skattefrit op til 7.000 kr. om året pr. ejer.", ["se_sol"])]),
   ]),
   ("Regn på dit eget hus", [
     ("p", "Brug vores <a href=\"/beregner/#solceller\">solcelleberegner</a>, hvor du selv kan ændre pris, produktion, egetforbrug og elpriser. Standardværdierne er de tal, der står ovenfor, med kilder.", []),
     ("p", "Bor du i Horsens eller Kolding Kommune, giver kommunen gratis adgang til et uvildigt beregningsværktøj (SolarSim). Se <a href=\"/solceller/horsens/\">Horsens</a> og <a href=\"/solceller/kolding/\">Kolding</a>.", ["hor_sol", "kol_sol"]),
   ]),
  ],
  "faq": [
   ("Hvor lang er tilbagebetalingstiden på solceller?", "SparEnergi angiver 12-17 år ved et forbrug på 4.000 kWh afhængigt af anlæggets størrelse. Energisparer.dk regner med ca. 16 år for 6 kWp og ca. 13-14 år med 50 % egetforbrug.", ["se_sol", "es_sol"]),
   ("Kan solceller betale sig med den lave elafgift?", "Den lave elafgift i 2026-2027 gør den strøm, du selv bruger, mindre værd i de to år. Energisparer.dk regner med ca. 1,13 kr. pr. kWh i 2026-2027 og ca. 2,03 kr. fra 2028.", ["es_sol", "elafgift"]),
   ("Skal jeg betale skat af solgt strøm?", "Først når du sælger for mere end 7.000 kr. om året pr. ejer.", ["se_sol"]),
   ("Kan det betale sig med batteri?", "Ifølge Energisparer.dk er tilbagebetalingen omtrent den samme med og uden batteri, men batteriet holder typisk 10-15 år. Se vores side om solceller med batteri.", ["es_sol"]),
  ],
}

T["/solceller/fladt-tag-og-carport/"] = {
  "svc": "solceller", "crumb": "Fladt tag og carport", "updated": UPD,
  "kw": "solceller på fladt tag / solceller på carport",
  "title": "Solceller på fladt tag og carport: regler og montering",
  "desc": "Solceller på fladt tag eller carport: hvornår kræver det byggetilladelse, afstand til skel, montering med ballast eller beslag, og hvad du skal tjekke først.",
  "h1": "Solceller på fladt tag og carport: regler og montering",
  "intro": "Et fladt tag eller en carport kan være en god plads til solceller, hvis husets tag vender forkert eller ikke kan bære. Men det er netop her, reglerne om byggetilladelse oftest slår til. Her er, hvad der gælder, med kilder fra kommuner og branchen.",
  "sections": [
   ("Hvornår kræver det byggetilladelse?", [
     ("p", "Solceller kræver som udgangspunkt ikke byggetilladelse. Byggeri og Energis solcelleguide nævner dog bl.a. disse undtagelser: anlæg på stativ på taget, anlæg der kræver ændring af tagkonstruktionen, og fritstående anlæg på jorden.", ["be_guide"]),
     ("ul", [("Vordingborg Kommune skriver, at anlæg på stativ på fladt tag altid kræver byggetilladelse, mens anlæg på carporte og udhuse kan sættes op uden ansøgning, når de følger tagets hældning.", ["vor_sol"]),
             ("Aarhus Kommune vurderer anlæg på flade tage, der er højere end 1 meter over tagfladen, som en bygningslignende konstruktion, der kræver byggetilladelse.", ["aar_sol"]),
             ("Kommunerne formulerer reglerne forskelligt, så tjek din egen kommunes side. Se fx <a href=\"/solceller/kolding/regler-og-byggetilladelse/\">reglerne i Kolding</a> eller <a href=\"/solceller/randers/regler-og-byggetilladelse/\">Randers</a>.", ["vor_sol", "aar_sol"])]),
   ]),
   ("Afstand til skel gælder også carporten", [
     ("p", "Bygningsreglementets § 179 kræver mindst 2,5 meter til skel mod nabo, sti og vej for boliger. I sommerhusområder er det 5 meter mod nabo og sti.", ["be_guide", "br18_179"]),
     ("p", "Bolius skriver, at det også gælder solceller på garage og carport. Står bygningen tættere på skel, skal du ifølge Aarhus Kommune søge byggetilladelse.", ["bolius_mont", "aar_sol"]),
   ]),
   ("Montering på fladt tag", [
     ("ul", [("Konsolsystemer: plader af rustfrit stål skrues fast i underlaget, og der svejses tagpap over for at holde tæt.", ["bolius_mont"]),
             ("Ballast: systemer holdes nede af sand, sten eller lignende i stedet for skruer. Så bliver tagfladen ikke gennembrudt, og risikoen for utætheder mindskes.", ["bolius_mont"]),
             ("Uanset tagtype anbefaler Bolius en vurdering af tagkonstruktionens tilstand, gerne med beregninger fra en ingeniør. Aarhus Kommune minder om, at du selv skal sikre, at taget kan bære den ekstra vægt.", ["bolius_mont", "aar_sol"])]),
     ("note", "SparEnergi anbefaler, at du beder installatøren om en garanti for, at taget kan bære anlægget. Vil installatøren ikke stå inde for det, så få en bygningsingeniør til at regne på det.", ["se_sol"]),
   ]),
   ("Retning og hældning", [
     ("p", "Bolius skriver, at sydvendt er bedst, øst og vest kan gå an, og at hældningen bør være mellem 15 og 60 grader alt efter retningen. På et fladt tag får panelerne derfor ofte et stativ, og det er netop stativet, der kan udløse krav om byggetilladelse.", ["bolius_mont", "be_guide"]),
     ("p", "Du kan se, hvad et anlæg giver i din by mod syd, øst og vest, på vores bysider. Tallene er beregnet i PVGIS, fx for <a href=\"/solceller/aalborg/\">Aalborg</a> og <a href=\"/solceller/esbjerg/\">Esbjerg</a>.", ["pvgis"]),
   ]),
   ("Husk BBR", [
     ("p", "Solcelleanlæg skal anmeldes til BBR med adresse, areal og samlet effekt i kW, også når de ikke kræver byggetilladelse.", ["aar_sol", "vor_sol"]),
   ]),
  ],
  "faq": [
   ("Kræver solceller på carport byggetilladelse?", "Som regel ikke, hvis panelerne følger tagets hældning og carporten overholder afstanden til skel. Står carporten tættere end 2,5 meter på skel, skal du søge.", ["vor_sol", "aar_sol"]),
   ("Kræver solceller på fladt tag byggetilladelse?", "Ofte, hvis de står på stativ. Vordingborg Kommune kræver altid tilladelse til stativer på fladt tag, og Aarhus Kommune ved anlæg højere end 1 meter over tagfladen.", ["vor_sol", "aar_sol", "be_guide"]),
   ("Kan solceller monteres uden at bore i taget?", "Ja, på flade tage findes ballastsystemer, der holdes nede af sand eller sten. Taget skal kunne bære den ekstra vægt.", ["bolius_mont"]),
   ("Hvor tæt på skel må solceller være?", "Mindst 2,5 meter for boliger og 5 meter mod nabo og sti i sommerhusområder.", ["be_guide"]),
  ],
}

T["/solceller/tilbud/"] = {
  "svc": "solceller", "crumb": "Tilbud", "updated": UPD, "checklist": True,
  "kw": "tilbud på solceller / solceller tilbud",
  "title": "Tilbud på solceller: få et uforpligtende tilbud",
  "desc": "Få et uforpligtende tilbud på solceller fra en installatør i dit område. Se hvad tilbuddet skal indeholde, prisniveauet pr. kWp, og hvordan du sammenligner.",
  "h1": "Få tilbud på solceller",
  "intro": "Udfyld formularen, så sender vi din forespørgsel til én udvalgt installatør, der dækker dit område. Nedenfor kan du se, hvad et godt tilbud skal indeholde, og hvilket prisniveau du kan holde det op imod.",
  "sections": [
   ("Hvad koster det typisk?", [
     ("p", "Energisparer.dk ser i 2026 et prisniveau på ca. 12.500-16.000 kr. pr. kWp for et færdigmonteret anlæg. Et typisk 6 kWp-anlæg koster ca. 90.000-95.000 kr. inkl. montering.", ["es_sol"]),
     ("p", "Ligger et tilbud markant over 16.000 kr. pr. kWp, bør du bede om en forklaring. Ligger det langt under 11.000 kr. pr. kWp, så tjek, om montering, stillads og nettilslutning reelt er med.", ["es_sol"]),
     ("p", "Se alle priser, ekstraposter og tilbagebetaling i <a href=\"/solceller/pris/\">guiden til solceller pris 2026</a>, og regn selv på økonomien i <a href=\"/beregner/#solceller\">beregneren</a>.", []),
   ]),
   ("Sådan sammenligner du tilbud", [
     ("ul", [("Giv alle installatører samme grundlag: dit årlige elforbrug i kWh og tagets type.", ["es_sol"]),
             ("Sammenlign totalprisen og prisen pr. kWp, ikke kun panelprisen.", ["es_sol"]),
             ("Tjek, hvilken elpris installatøren har brugt i økonomiberegningen, og hvilke faktorer der ligger bag den forventede produktion.", ["se_sol"]),
             ("Få arbejdslønnen opgjort for sig, så du kan bruge håndværkerfradraget på op til 9.000 kr. pr. person i 2026.", ["es_sol", "hvfradrag"]),
             ("Find dit forbrug time for time på Eloverblik.dk, så installatøren kan foreslå et anlæg, du selv kan bruge strømmen fra.", ["se_sol"])]),
   ]),
  ],
  "faq": [
   ("Er tilbuddet gratis og uforpligtende?", "Ja. Du bestemmer selv, om du vil sige ja til installatørens tilbud. Vi er en formidlingstjeneste og ikke selv installatør.", []),
   ("Hvor mange installatører får mine oplysninger?", "Én. Vi sender din forespørgsel til én udvalgt installatør i dit område, og du får en e-mail med firmaets navn og CVR-nummer, så snart det er sket.", []),
   ("Hvad skal et tilbud på solceller indeholde?", "SparEnergi anbefaler som minimum størrelse og placering, samlet pris, forventet produktion, garantier, forsikringsmuligheder og et overslag over økonomien.", ["se_sol"]),
   ("Hvor meget svinger priserne?", "Energisparer.dk ser typisk 20-40 % forskel mellem to montører på samme anlæg.", ["es_sol"]),
  ],
}

T["/varmepumpe/tilbud/"] = {
  "svc": "varmepumpe", "crumb": "Tilbud", "updated": UPD, "checklist": True,
  "kw": "tilbud på varmepumpe / varmepumpe tilbud / luft til vand tilbud",
  "title": "Tilbud på varmepumpe: få et uforpligtende tilbud",
  "desc": "Få et uforpligtende tilbud på en luft til vand-varmepumpe fra en installatør i dit område. Se hvad tilbuddet skal vise, og hvornår du må skrive under.",
  "h1": "Få tilbud på luft til vand-varmepumpe",
  "intro": "Udfyld formularen, så sender vi din forespørgsel til én udvalgt installatør, der dækker dit område. Søger du tilskud, må du gerne få tilbud nu, men du må ikke skrive under, før du har tilsagn.",
  "sections": [
   ("Tilbud før tilskud: sådan gør du", [
     ("ul", [("Du må gerne indhente tilbud, før du søger Varmepumpepuljen, men ikke indgå en bindende aftale eller gå i gang, før du har tilsagn.", ["vpp_ens", "vpp_faq"]),
             ("Tilskuddet er 27.000 kr. til luft til vand og jordvarme. Puljen lukker senest 30. november 2026 eller når midlerne er brugt.", ["se_vpp", "vpp_faq"]),
             ("Ligger huset i et område med fjernvarme eller planlagt fjernvarme, kan du ikke få tilskud. Se status i <a href=\"/varmepumpe/\">din by</a>.", ["se_vpp"])]),
   ]),
   ("Hvad koster det typisk?", [
     ("p", "SparEnergi angiver typisk 100.000-130.000 kr. for en luft til vand-varmepumpe, og Energisparer.dk ca. 90.000-150.000 kr. inkl. montering. Energisparer.dk ser 20-40 % prisforskel mellem installatører på samme opgave.", ["se_vp", "es_vp"]),
     ("p", "Se alle priser og driftsudgifter i <a href=\"/varmepumpe/pris/\">prisguiden</a>, og regn på din egen tilbagebetalingstid i <a href=\"/beregner/#varmepumpe\">beregneren</a>.", []),
   ]),
   ("Sådan sammenligner du tilbud", [
     ("ul", [("Sammenlign på totalpris, ikke fra-pris, og bed om en specificeret pris med el-arbejde og ekstraarbejde.", ["es_vp"]),
             ("Få anlæggets SCOP og garanti oplyst. Et lidt dyrere anlæg med højere SCOP kan være billigst over levetiden.", ["es_vp"]),
             ("Spørg, hvad det årlige eftersyn koster, og hvor hurtigt du kan få service og reservedele.", ["es_vp"])]),
   ]),
  ],
  "faq": [
   ("Må jeg få et tilbud, før jeg søger tilskud?", "Ja. Du må bare ikke skrive under på en bindende aftale, før du har tilsagn om tilskud.", ["vpp_ens", "vpp_faq"]),
   ("Er tilbuddet gratis og uforpligtende?", "Ja. Du bestemmer selv, om du vil sige ja. Vi er en formidlingstjeneste og ikke selv installatør.", []),
   ("Hvor mange installatører får mine oplysninger?", "Én. Du får en e-mail med firmaets navn og CVR-nummer, så snart vi har sendt din forespørgsel.", []),
   ("Hvad skal et tilbud på varmepumpe indeholde?", "Model og energimærke, dimensionering, samlet pris med arbejdsløn for sig, placering af udedelen, hvad der sker med det gamle fyr, og hvem der søger tilskud.", ["se_vp", "vpp_faq"]),
  ],
}

# Navigation: (sti, kort titel, teaser, ikon)
NAV = {
 "solceller": [("/solceller/kan-det-betale-sig/", "Kan solceller betale sig?", "Tilbagebetaling, værdi pr. kWh og elafgiften.", "scale"),
               ("/solceller/fladt-tag-og-carport/", "Solceller på fladt tag og carport", "Byggetilladelse, skel og montering.", "building"),
               ("/solceller/tilbud/", "Tilbud på solceller", "Få et uforpligtende tilbud, og se hvad det skal indeholde.", "doc")],
 "varmepumpe": [("/varmepumpe/skift-oliefyr/", "Skift oliefyr til varmepumpe", "Besparelse, tilskud og olietanken.", "flame"),
                ("/varmepumpe/skift-gasfyr/", "Skift gasfyr til varmepumpe", "Varmeplan, tilskud og afkobling.", "flame"),
                ("/varmepumpe/jordvarme-pris/", "Jordvarme pris", "Pris, drift, grund og tilladelse.", "pump"),
                ("/varmepumpe/luft-til-luft-pris/", "Luft til luft-varmepumpe pris", "Pris, besparelse og begrænsninger.", "pump"),
                ("/varmepumpe/tilbud/", "Tilbud på varmepumpe", "Få et uforpligtende tilbud før fristen.", "doc")],
}
