# -*- coding: utf-8 -*-
"""v4: ekstra lokalt indhold pr. by. Tal kommer fra data_local_gen.py (PVGIS + Danmarks Statistik, hentet 24/10 2026),
tekster er skrevet pr. by. Alle fakta har en kilde i LOCAL_S (flettes ind i S i build.py)."""
from data_local_gen import PV, HEAT, STOCK, ROOF, ROOF_LABELS, TOWNS

def tal(n): return f"{int(round(n)):,}".replace(",", ".")
def pct(part, whole, d=0):
    v = 100 * part / whole
    return (f"{v:.{d}f}".replace(".", ",")) + " %"
def hs(c): return sum(HEAT[c].values())            # beboede parcel- og rækkehuse i alt
def hp(c, k, d=0): return pct(HEAT[c][k], hs(c), d)
def rp(c, k, d=0): return pct(ROOF[c]["T"][k], ROOF[c]["tot"], d)
def town(c, name): return dict(TOWNS[c])[name]
_NUMW = {6: "seks", 7: "syv", 8: "otte", 9: "ni", 10: "ti", 11: "elleve", 12: "tolv", 13: "tretten", 14: "fjorten"}
def nw(k=0): return _NUMW[len(NAMES) - k]          # "ni" for 9 byer, nw(1) = "otte" (de andre)
def top(f, rev=False):
    """By med højeste (eller laveste, rev=True) værdi blandt sitets byer. Bruges til at tjekke sammenlignende udsagn."""
    return sorted(NAMES, key=f, reverse=not rev)[0]
def rank(f, c): return sorted(NAMES, key=f, reverse=True).index(c) + 1
_ORDP = {1: "", 2: "næst", 3: "tredje", 4: "fjerde", 5: "femte", 6: "sjette", 7: "syvende", 8: "ottende"}
def rk(f, c, word, art="den", rev=False):
    """Rangord, fx 'den højeste', 'den næsthøjeste' (rev=True tæller fra bunden). Holder sammenlignende udsagn sande, når nye byer kommer til."""
    r = sorted(NAMES, key=f, reverse=not rev).index(c) + 1
    return f"{art} {_ORDP[r]}{word}"
def above(f, c):
    """Navne på byer med højere værdi end c (til 'Kun X og Y har en højere andel')."""
    a = [NAMES[x] for x in sorted(NAMES, key=f, reverse=True)[:rank(f, c) - 1]]
    return a[0] if len(a) == 1 else ", ".join(a[:-1]) + " og " + a[-1]

NAMES = {"kolding": "Kolding", "vejle": "Vejle", "esbjerg": "Esbjerg", "odense": "Odense", "aalborg": "Aalborg", "randers": "Randers", "horsens": "Horsens", "aarhus": "Aarhus", "viborg": "Viborg", "naestved": "Næstved", "silkeborg": "Silkeborg"}
LOCAL_S = {
 "dst_bol102": ("Danmarks Statistik: BOL102, boliger efter område og opvarmning (2026)", "https://www.statistikbanken.dk/BOL102"),
 "dst_bol101": ("Danmarks Statistik: BOL101, boliger efter opførelsesår og udlejningsforhold (2026)", "https://www.statistikbanken.dk/BOL101"),
 "dst_bygb50": ("Danmarks Statistik: BYGB50, bygninger efter tagdækningsmateriale (2026)", "https://www.statistikbanken.dk/BYGB50"),
 "dst_by3": ("Danmarks Statistik: BY3, folketal i byområder 1. januar 2026", "https://www.statistikbanken.dk/BY3"),
 "pvgis": ("PVGIS 5.3, EU-Kommissionens Joint Research Centre", "https://re.jrc.ec.europa.eu/pvg_tools/en/"),
 "bolius_mont": ("Bolius: placering og montering af solceller", "https://www.bolius.dk/placering-og-montering-af-solceller-27566"),
 "bolius_asb": ("Bolius: pas på asbest i taget (ajourført 10/2 2025)", "https://www.bolius.dk/pas-paa-asbest-i-taget-3412"),
 "se_moeder": ("SparEnergi: gratis rådgivning om varmepumper, efteråret 2026 (opdateret 22/10 2026)", "https://sparenergi.dk/privat/overvejer-du-skifte-dit-gamle-fyr-ud-med-en-varmepumpe"),
 "vej_elm": ("Vejle Kommune: energivenlig bolig, lån en elmåler (opdateret 9/10 2026)", "https://www.vejle.dk/da/groent-liv/dine-groenne-valg/energivenlig-bolig/"),
 "vej_varme": ("Vejle Kommune: varme (9 fjernvarmeværker og 1 naturgasselskab)", "https://www.vejle.dk/da/service-og-selvbetjening/borger/bolig-byggeri-og-forsyning/forsyning-og-energi/varme/"),
 "ran_bolig": ("Randers Kommune: bæredygtige boliger (BedreBolig-rådgivere)", "https://www.randers.dk/udvikling-by-og-land/klima-og-energi/klimaliga/borgere-i-klimaliga/baeredygtige-boliger/"),
 "trefor_v": ("TREFOR/EWII: fjernvarme i Kolding", "https://www.trefor.dk/varme"),
 "tvis_kol": ("TVIS: fjernvarmeprojekt i Kolding (Almind, Vester Nebel, Viuf m.fl.)", "https://www.tvis.net/kolding/"),
 "ffyn_kul": ("Dansk Fjernvarme 23/4 2024: Fjernvarme Fyn lukker et af landets sidste kulværker", "https://danskfjernvarme.dk/aktuelt/nyheder/2024/fjernvarme-fyn-lukker-et-af-landets-sidste-kulvaerker"),
 "ramboll_meta": ("Rambøll: overskudsvarme fra Metas datacenter i Odense", "https://www.ramboll.com/da-dk/projekter/energi/meta-surplus-heat-to-district-heating"),
 "verdo_fv": ("Verdo: fjernvarme i Randers og Herning", "https://www.verdo.com/dk/privat/fjernvarme/"),
 "fjho": ("Fjernvarme Horsens: nøgletal", "https://fjernvarmehorsens.dk/"),
}
for c, p in PV.items():
    LOCAL_S[f"pv_{c}"] = (f"PVGIS 5.3-beregning for {NAMES[c]} (syd, 35°, 14 % tab)", p["url_syd"])
    LOCAL_S[f"pvo_{c}"] = (f"PVGIS 5.3-beregning for {NAMES[c]} (øst, 35°)", p["url_oest"])
    LOCAL_S[f"pvv_{c}"] = (f"PVGIS 5.3-beregning for {NAMES[c]} (vest, 35°)", p["url_vest"])

# Rækkefølge af sektioner pr. by (varieres, så siderne ikke er bygget ens)
SOL_ORDER = {
 "kolding": ["lokalt", "produktion", "tage", "boliger", "guides", "faq"],
 "vejle":   ["lokalt", "boliger", "produktion", "tage", "guides", "faq"],
 "esbjerg": ["lokalt", "tage", "produktion", "boliger", "faq", "guides"],
 "odense":  ["lokalt", "boliger", "tage", "produktion", "faq", "guides"],
 "aalborg": ["tage", "lokalt", "produktion", "boliger", "guides", "faq"],
 "randers": ["lokalt", "tage", "boliger", "produktion", "faq", "guides"],
 "horsens": ["produktion", "lokalt", "tage", "boliger", "guides", "faq"],
}
VP_ORDER = {
 "kolding": ["lokalt", "opvarmning", "lokale-byer", "pris", "guides", "faq"],
 "vejle":   ["lokalt", "lokale-byer", "opvarmning", "pris", "faq", "guides"],
 "esbjerg": ["opvarmning", "lokalt", "pris", "lokale-byer", "guides", "faq"],
 "odense":  ["opvarmning", "lokalt", "lokale-byer", "pris", "faq", "guides"],
 "aalborg": ["lokalt", "pris", "opvarmning", "lokale-byer", "guides", "faq"],
 "randers": ["lokale-byer", "lokalt", "opvarmning", "pris", "faq", "guides"],
 "horsens": ["pris", "opvarmning", "lokalt", "lokale-byer", "guides", "faq"],
}
FV_ORDER = {
 "kolding": ["status", "varmekilder", "priser", "andel", "billigst", "faq"],
 "vejle":   ["status", "andel", "priser", "billigst", "varmekilder", "faq"],
 "esbjerg": ["varmekilder", "status", "priser", "billigst", "andel", "faq"],
 "odense":  ["andel", "varmekilder", "priser", "status", "billigst", "faq"],
 "aalborg": ["status", "priser", "varmekilder", "billigst", "andel", "faq"],
 "randers": ["status", "priser", "billigst", "andel", "varmekilder", "faq"],
 "horsens": ["priser", "billigst", "varmekilder", "andel", "status", "faq"],
}

# ---------- solceller: produktion (PVGIS) ----------
def _pv(c):
    p = PV[c]; return p, p["syd"] * 6, p["months"][5] * 6, p["months"][11] * 6
SOL_PROD = {
 "kolding": ("Så meget strøm giver solceller i Kolding",
   lambda: f"Ved Kolding Fjord giver et sydvendt anlæg med 35° hældning ca. <strong>{tal(PV['kolding']['syd'])} kWh pr. kWp om året</strong> ifølge PVGIS. Et typisk 6 kWp-anlæg på et parcelhus i Kolding ender dermed på omkring {tal(PV['kolding']['syd']*6)} kWh, så længe taget ikke ligger i skygge."),
 "vejle": ("Solceller i Vejle: syd, øst eller vest?",
   lambda: f"Vender dit tag ikke mod syd? PVGIS viser, hvad retningen betyder i Vejle: syd giver ca. {tal(PV['vejle']['syd'])} kWh pr. kWp om året, mens øst og vest giver omkring {tal(PV['vejle']['oest'])}-{tal(PV['vejle']['vest'])} kWh. Det er en nedgang på ca. {round(100*(1-PV['vejle']['oest']/PV['vejle']['syd']))} %, men øst-vest fordeler til gengæld produktionen over flere timer af dagen."),
 "esbjerg": ("Mere sol ved Vestkysten: produktion i Esbjerg",
   lambda: f"Esbjerg har {rk(lambda x: PV[x]['syd'], 'esbjerg', 'højeste')} beregnede produktion af de {nw()} byer på dette site: ca. <strong>{tal(PV['esbjerg']['syd'])} kWh pr. kWp om året</strong> for et sydvendt anlæg på 35° (PVGIS). For et 6 kWp-anlæg svarer det til ca. {tal(PV['esbjerg']['syd']*6)} kWh. Husk dog Esbjerg Kommunes krav til, hvordan anlægget skal ligge på taget."),
 "odense": ("Solcellernes produktion i Odense måned for måned",
   lambda: f"I Odense beregner PVGIS ca. {tal(PV['odense']['syd'])} kWh pr. kWp om året for et sydvendt tag med 35° hældning. Men fordelingen over året er skæv: et 6 kWp-anlæg giver ca. <strong>{tal(PV['odense']['months'][5]*6)} kWh i juni</strong>, men kun ca. {tal(PV['odense']['months'][11]*6)} kWh i december. Med fjernvarme, som næsten alle i Odense har, bruges solstrømmen ikke til varme, men til husholdning, elbil eller et batteri."),
 "aalborg": ("Giver solceller mindre strøm i Aalborg end sydpå?",
   lambda: f"Nej, ikke målbart. PVGIS giver Aalborg ca. {tal(PV['aalborg']['syd'])} kWh pr. kWp om året for et sydvendt anlæg på 35°. Det er mere end i Kolding ({tal(PV['kolding']['syd'])} kWh) og Vejle ({tal(PV['vejle']['syd'])} kWh). Nordjylland har lange sommerdage, og juni giver her {rk(lambda x: PV[x]['months'][5], 'aalborg', 'højeste')} månedsproduktion af de {nw()} byer: ca. {tal(PV['aalborg']['months'][5]*6)} kWh fra 6 kWp."),
 "randers": ("Forventet elproduktion fra solceller i Randers",
   lambda: f"For et sydvendt tag i Randers beregner PVGIS ca. {tal(PV['randers']['syd'])} kWh pr. kWp om året. PVGIS' optimale hældning i Randers er {PV['randers']['opt_angle']}°, men den giver kun {PV['randers']['opt']-PV['randers']['syd']} kWh mere pr. kWp end 35°. Det er altså ikke værd at vinkle panelerne op på stativer for at jagte de sidste kilowatttimer."),
 "horsens": ("Hvad producerer 6 kWp i Horsens om året?",
   lambda: f"Ca. <strong>{tal(PV['horsens']['syd']*6)} kWh</strong>, hvis taget vender mod syd med 35° hældning. Det viser en PVGIS-beregning for Horsens ({tal(PV['horsens']['syd'])} kWh pr. kWp). Vender taget mod øst, er tallet ca. {tal(PV['horsens']['oest']*6)} kWh. Brug Horsens Kommunes gratis SolarSim til at regne på netop dit tag, før du sammenligner tilbud."),
}

# ---------- solceller: tage (DST BYGB50 + Bolius) ----------
SOL_ROOF = {
 "kolding": ("Tagene i Kolding: betontagsten er mest udbredt",
   lambda: f"Betontagsten (cementsten) ligger på {rp('kolding','08')} af parcel- og rækkehusene i Kolding Kommune mod {rp('dk','08')} i hele landet. Bolius beskriver, at beslag på tegl- og betontegltage fastgøres i lægter eller spær med ansatsskruer eller tagkroge, og at stenene skal tilpasses, så taget forbliver tæt.",
   ["dst_bygb50", "bolius_mont"]),
 "vejle": ("Hvilke tage har husene i Vejle?",
   lambda: f"Hvert tredje parcel- og rækkehus i Vejle Kommune har betontagsten ({rp('vejle','08')}), og kun {rp('vejle','10')} har tegl, mod {rp('dk','10')} på landsplan. Bolius anbefaler at få vurderet tagets stand og bæreevne, før panelerne kommer op.",
   ["dst_bygb50", "dst_bol101", "bolius_mont"]),
 "esbjerg": ("Tegl, beton og eternit: tagene i Esbjerg",
   lambda: f"Tre tagtyper deler næsten husene i Esbjerg Kommune mellem sig: tegl ({rp('esbjerg','10')}), betontagsten ({rp('esbjerg','08')}) og fibercement/eternit ({rp('esbjerg','06')}). På tegl og skifer kræver kommuneplanen, at rækker af sten ved top, bund og sider holdes fri, så kend din tagtype, før du får tilbud.",
   ["dst_bygb50", "esb_sol"]),
 "odense": ("Tegltage dominerer i Odense",
   lambda: f"{rp('odense','10')} af parcel- og rækkehusene i Odense Kommune har tegltag. Det er den højeste andel af de {nw()} byer og langt over landsgennemsnittet på {rp('dk','10')}. Bolius beskriver to måder at montere på tegl: tagkroge, der går ind under stenene, eller ansatsskruer gennem tagbeklædningen. Tagkroge tager længere tid, fordi teglene skal tilpasses for at holde tæt.",
   ["dst_bygb50", "bolius_mont"]),
 "aalborg": ("Eternittage i Aalborg: det skal du vide før solceller",
   lambda: f"Aalborg Kommune har flest fibercementtage af de {nw()} byer: {rp('aalborg','06')} af parcel- og rækkehusene har et tag, som Danmarks Statistik registrerer som fibercement inkl. asbest. Dansk Eternit havde fabrik i Aalborg, og ifølge Bolius indeholder bølge- og kunstskiferplader fra før 1984 næsten altid asbest. Det er tilladt at montere solceller på et asbesttag, hvis monteringen kun kræver, at der bores huller i pladerne.",
   ["dst_bygb50", "bolius_asb"]),
 "randers": ("Fibercement er det mest almindelige tag i Randers",
   lambda: f"{rp('randers','06')} af parcel- og rækkehusene i Randers Kommune har tag af fibercement (eternit), mod {rp('dk','06')} i hele landet. Bølgetage er lette konstruktioner, og Bolius skriver, at lægter og spær derfor måske skal forstærkes. Få leverandøren eller en ingeniør til at regne på det, og husk, at plader fra før 1984 næsten altid indeholder asbest.",
   ["dst_bygb50", "bolius_mont", "bolius_asb"]),
 "horsens": ("Tagene i Horsens Kommune",
   lambda: f"I Horsens Kommune er fibercement ({rp('horsens','06')}), betontagsten ({rp('horsens','08')}) og tegl ({rp('horsens','10')}) de tre store tagtyper. Har dit hus tagpap med hældning, som {rp('horsens','04')} har, skal gennembrydningerne tætnes ekstra omhyggeligt ifølge Bolius. Skal taget alligevel skiftes inden for 10-15 år, anbefaler Bolius at overveje at gøre det først.",
   ["dst_bygb50", "bolius_mont"]),
}

# ---------- solceller: boligerne (DST BOL101/BY3) ----------
def _st(c): return STOCK[c]
SOL_HOMES = {
 "kolding": lambda: f"I Kolding Kommune er der {tal(STOCK['kolding']['parcel'])} beboede parcel- og stuehuse og {tal(STOCK['kolding']['raekke'])} række-, kæde- og dobbelthuse. {pct(STOCK['kolding']['ejer'],STOCK['kolding']['tot'])} bebos af ejeren. Ud over Kolding by gælder siden også Vamdrup, Christiansfeld, Lunderskov, Sønder Bjert og Vester Nebel, der alle hører under Kolding Kommunes regler for solceller.",
 "vejle": lambda: f"Vejle Kommune har {tal(STOCK['vejle']['tot'])} beboede parcel- og rækkehuse, og {pct(STOCK['vejle']['B']['2000+'],STOCK['vejle']['tot'])} er bygget i 2000 eller senere. Kun {above(lambda x: STOCK[x]['B']['2000+'] / STOCK[x]['tot'], 'vejle')} har en højere andel af nyere huse blandt de {nw()} byer på dette site. Kommunens regler gælder også i Børkop, Give, Jelling, Brejning og Egtved.",
 "esbjerg": lambda: f"{pct(STOCK['esbjerg']['B']['1960-1979'],STOCK['esbjerg']['tot'])} af de {tal(STOCK['esbjerg']['tot'])} beboede parcel- og rækkehuse i Esbjerg Kommune er opført 1960-1979, den største andel af de {nw()} byer. Bolius anbefaler at sikre, at taget har tilstrækkelig restlevetid, før solcellerne monteres. Siden gælder også Ribe, Bramming, Tjæreborg, Gørding og Tarp.",
 "odense": lambda: f"Odense skiller sig ud ved de mange rækkehuse: {tal(STOCK['odense']['raekke'])} af kommunens {tal(STOCK['odense']['tot'])} beboede parcel- og rækkehuse er række-, kæde- eller dobbelthuse ({pct(STOCK['odense']['raekke'],STOCK['odense']['tot'])}). Odense Kommune kræver tilladelse eller dispensation, hvis en lokalplan, byplanvedtægt eller servitut regulerer solceller eller tagets udseende. Siden gælder også Bellinge, Sankt Klemens, Fraugde og Over Holluf.",
 "aalborg": lambda: f"Aalborg Kommune har {tal(STOCK['aalborg']['tot'])} beboede parcel- og rækkehuse, næstflest af de {nw()} kommuner på dette site efter Aarhus. Siden gælder hele kommunen: Aalborg og Nørresundby ({tal(town('aalborg','Nørresundby'))} indbyggere) og forstæder som Svenstrup, Klarup, Vodskov og Gistrup samt Nibe.",
 "randers": lambda: f"I Randers Kommune er {pct(STOCK['randers']['ejer'],STOCK['randers']['tot'])} af de {tal(STOCK['randers']['tot'])} beboede parcel- og rækkehuse ejerboliger, og {pct(STOCK['randers']['B']['før 1960'],STOCK['randers']['tot'])} er bygget før 1960. Har huset bevaringsværdi 1-3 i et kulturmiljø, giver Randers Kommune som udgangspunkt ikke tilladelse til solceller. Siden gælder også Assentoft, Langå, Stevnstrup og Spentrup.",
 "horsens": lambda: f"Horsens har den højeste andel ejerboliger af de {nw()} kommuner: {pct(STOCK['horsens']['ejer'],STOCK['horsens']['tot'])} af de {tal(STOCK['horsens']['tot'])} beboede parcel- og rækkehuse bebos af ejeren. {pct(STOCK['horsens']['B']['2000+'],STOCK['horsens']['tot'])} er bygget i 2000 eller senere. Siden gælder også Brædstrup, Lund, Egebjerg, Østbirk og Gedved.",
}
SOL_HOMES_H = {
 "kolding": "Boliger og byer i Kolding Kommune", "vejle": "Nyere huse i Vejle Kommune", "esbjerg": "Huse fra 60'erne og 70'erne i Esbjerg",
 "odense": "Rækkehuse og parcelhuse i Odense", "aalborg": "Fra Nørresundby til Nibe", "randers": "Ejerboliger i Randers Kommune", "horsens": "Ejerboliger i Horsens Kommune",
}
# ekstra, datadrevne FAQ (solceller)
SOL_XFAQ = {
 "kolding": [("Hvor meget strøm giver et 6 kWp-anlæg i Kolding?", lambda: f"Ca. {tal(PV['kolding']['syd']*6)} kWh om året på et sydvendt tag med 35° hældning ifølge PVGIS. På et øst- eller vestvendt tag er det ca. {tal(PV['kolding']['oest']*6)}-{tal(PV['kolding']['vest']*6)} kWh.", ["pv_kolding", "pvo_kolding"]),
             ("Kan man sætte solceller på betontagsten?", lambda: "Ja. Bolius beskriver, at beslag på tegl- og betontegltage fastgøres i taglægter eller spær med ansatsskruer eller tagkroge. Det er det mest udbredte tag i Kolding Kommune.", ["bolius_mont", "dst_bygb50"])],
 "vejle": [("Kan det betale sig med solceller på et øst-vest-tag i Vejle?", lambda: f"Øst og vest giver ca. {tal(PV['vejle']['oest'])}-{tal(PV['vejle']['vest'])} kWh pr. kWp om året i Vejle mod {tal(PV['vejle']['syd'])} kWh mod syd (PVGIS). Bolius skriver, at øst- eller vestvendt kan gå an, mens nordvendt er udelukket.", ["pvo_vejle", "pv_vejle", "bolius_mont"])],
 "esbjerg": [("Hvor meget producerer solceller i Esbjerg?", lambda: f"PVGIS beregner ca. {tal(PV['esbjerg']['syd'])} kWh pr. kWp om året for et sydvendt anlæg på 35°, svarende til ca. {tal(PV['esbjerg']['syd']*6)} kWh for 6 kWp.", ["pv_esbjerg"])],
 "odense": [("Hvor meget strøm giver solceller i Odense om vinteren?", lambda: f"Meget lidt. Et sydvendt 6 kWp-anlæg giver ca. {tal(PV['odense']['months'][11]*6)} kWh i december og ca. {tal(PV['odense']['months'][0]*6)} kWh i januar, mod ca. {tal(PV['odense']['months'][5]*6)} kWh i juni (PVGIS).", ["pv_odense"]),
            ("Kan man få solceller på et tegltag i Odense?", lambda: "Ja. Ifølge Bolius monteres beslagene med tagkroge under stenene eller med ansatsskruer, og teglene skal tilpasses, så taget holder tæt. Tjek også Odense Kommunes regler, hvis huset har bevaringsværdi.", ["bolius_mont", "ode_sol"])],
 "aalborg": [("Må jeg sætte solceller på et eternittag med asbest i Aalborg?", lambda: "Ja, hvis monteringen kun kræver, at der bores huller i pladerne. Du må ikke skære, ridse eller knække pladerne. Bølgetage kan desuden kræve, at lægter og spær forstærkes.", ["bolius_asb", "bolius_mont"])],
 "randers": [("Hvordan ved jeg, om mit eternittag i Randers indeholder asbest?", lambda: "Bolius skriver, at plader fra før 1984 næsten altid indeholder asbest, at plader fra 1984-1990 kan gøre det, og at plader fra efter 1990 er asbestfri. Nummeret på pladens yderside kan også afsløre det.", ["bolius_asb"])],
 "horsens": [("Hvor meget strøm giver solceller i Horsens?", lambda: f"PVGIS beregner ca. {tal(PV['horsens']['syd'])} kWh pr. kWp om året for et sydvendt tag med 35° hældning. Et 6 kWp-anlæg giver dermed omkring {tal(PV['horsens']['syd']*6)} kWh.", ["pv_horsens"])],
}

# ---------- varmepumpe: opvarmning (DST BOL102) ----------
VP_HEAT = {
 "kolding": ("Sådan varmes husene op i Kolding Kommune",
   lambda: f"{hp('kolding','FJ')} af de beboede parcel- og rækkehuse i Kolding Kommune har fjernvarme. Naturgas er næststørst med {tal(HEAT['kolding']['CN'])} huse ({hp('kolding','CN',1)}). I Christiansfeld er udvidelsen af fjernvarmen til naturgaskunderne opgivet. {tal(HEAT['kolding']['VP'])} huse har allerede en varmepumpe."),
 "vejle": ("Vejle har den største andel varmepumper på sitet",
   lambda: f"{tal(HEAT['vejle']['VP'])} beboede parcel- og rækkehuse i Vejle Kommune varmes op med varmepumpe. Det er {hp('vejle','VP',1)} og den højeste andel af de {nw()} byer, mod {hp('dk','VP',1)} på landsplan. Samtidig har {tal(HEAT['vejle']['CN']+HEAT['vejle']['CO'])} huse stadig gas- eller oliefyr, og det er dem, kommunens fjernvarmeudrulning frem mod 2028 handler om."),
 "esbjerg": ("Fire ud af fem huse har fjernvarme i Esbjerg Kommune",
   lambda: f"{hp('esbjerg','FJ')} af de beboede parcel- og rækkehuse i Esbjerg Kommune har fjernvarme. Tilbage står ca. {tal(HEAT['esbjerg']['CO']+HEAT['esbjerg']['CN']+HEAT['esbjerg']['ELV'])} huse med olie, naturgas eller elvarme. Det er dem, en luft til vand-varmepumpe og Varmepumpepuljen er relevant for."),
 "odense": ("Næsten alle huse i Odense har fjernvarme",
   lambda: f"I Odense Kommune har {hp('odense','FJ',1)} af de beboede parcel- og rækkehuse fjernvarme, den højeste andel af de {nw()} byer. Kun {tal(HEAT['odense']['CO'])} huse har oliefyr, {tal(HEAT['odense']['CN'])} har naturgas, og {tal(HEAT['odense']['VP'])} har varmepumpe. En luft til vand-varmepumpe er derfor kun aktuel for få huse i Odense, primært uden for fjernvarmenettet."),
 "aalborg": ("Opvarmning i Aalborg Kommune i tal",
   lambda: f"{hp('aalborg','FJ')} af de beboede parcel- og rækkehuse i Aalborg Kommune har fjernvarme. {tal(HEAT['aalborg']['CO'])} huse har stadig oliefyr, flere end naturgas ({tal(HEAT['aalborg']['CN'])}). Kommunen udbygger ikke fjernvarmen yderligere lige nu og peger selv på varmepumper i områderne uden for nettet."),
 "randers": ("Randers har mange gas- og oliefyr tilbage",
   lambda: f"Kun {hp('randers','FJ')} af de beboede parcel- og rækkehuse i Randers Kommune har fjernvarme, {rk(lambda x: HEAT[x]['FJ'] / hs(x), 'randers', 'laveste', rev=True)} andel af de {nw()} byer. {tal(HEAT['randers']['CN'])} huse har naturgas, og {tal(HEAT['randers']['CO'])} har oliefyr ({hp('randers','CO',1)}, kun Viborg har en højere andel blandt byerne på sitet). Verdo udbygger lige nu i Assentoft, Harridslev, Stevnstrup og Spentrup. Uden for de byer er en varmepumpe alternativet."),
 "horsens": ("Opvarmningen af husene i Horsens Kommune",
   lambda: f"{hp('horsens','FJ')} af de beboede parcel- og rækkehuse i Horsens Kommune har fjernvarme efter Fjernvarme Horsens' store udbygning. {tal(HEAT['horsens']['VP'])} huse har varmepumpe, mens {tal(HEAT['horsens']['CN'])} stadig har naturgas og {tal(HEAT['horsens']['CO'])} oliefyr."),
}
VP_HEAT_ROWS = [("FJ", "Fjernvarme"), ("CN", "Naturgas (centralvarme)"), ("CO", "Oliefyr (centralvarme)"), ("VP", "Varmepumpe"), ("CA", "Centralvarme, anden kilde (fx træpiller)"), ("ELV", "Elvarme")]
# Lokale rådgivningstilbud, kun hvor kommunen eller Energistyrelsen har et konkret tilbud
VP_ADVICE = {
 "kolding": ("Energistyrelsens rådgivere holder et online møde om varmepumper for Kolding Kommune den <strong>3. november 2026</strong>. Tidspunkt og tilmelding offentliggøres på SparEnergi.", ["se_moeder"]),
 "vejle": ("Vejle Kommune låner en gratis elmåler ud (1 uge, 1 pr. husstand) hos Teknik og Miljø, så du kan måle dit forbrug, før du regner på en varmepumpe. Kommunen har 9 lokale fjernvarmeværker og 1 naturgasselskab.", ["vej_elm", "vej_varme"]),
 "randers": ("Randers Kommune henviser til Energistyrelsens BedreBolig-rådgivere, som kan gennemgå dit hus, før du vælger varmekilde. Foldere ligger på Randers Bibliotek og i Borgerservice.", ["ran_bolig"]),
}
# By for by: kun byer, hvor fjernvarmestatus står i en kilde. (by, status, kilder)
VP_TOWNS = {
 "kolding": [("Kolding", "Fjernvarme fra TREFOR Varme", ["trefor_v", "ft_pris"]),
             ("Vamdrup", "Eget værk: Vamdrup Fjernvarme", ["ft_pris"]),
             ("Christiansfeld", "Eget værk, men udvidelsen til naturgaskunderne er opgivet", ["kol_chr"]),
             ("Vester Nebel", "Fik fjernvarme via TVIS og TREFOR i 2024", ["tvis_kol"]),
             ("Almind", "Fik fjernvarme via TVIS og TREFOR i 2024", ["tvis_kol"]),
             ("Viuf", "Fik fjernvarme via TVIS og TREFOR i 2024", ["tvis_kol"])],
 "vejle":   [("Vejle", "Vejle Fjernvarme, primært overskudsvarme fra TVIS", ["vej_fv", "ft_pris"]),
             ("Give", "Eget værk: Give Fjernvarme", ["ft_pris"]),
             ("Jelling", "Eget værk: Jelling Varmeværk", ["ft_pris"]),
             ("Egtved", "Eget værk: Egtved Varmeværk", ["ft_pris"])],
 "esbjerg": [("Esbjerg", "DIN Forsyning", ["esb_fv"]),
             ("Ribe", "Eget værk: Ribe Fjernvarme", ["ft_pris"]),
             ("Bramming", "Eget værk: Bramming Fjernvarme", ["ft_pris"]),
             ("Tjæreborg", "DIN Forsyning", ["esb_fv"]),
             ("Gørding", "Eget værk: Gørding Varmeværk", ["ft_pris"]),
             ("Tarp", "DIN Forsyning", ["esb_fv"])],
 "odense":  [("Odense", "Fjernvarme Fyn", ["ode_fv", "ft_pris"])],
 "aalborg": [("Aalborg", "Aalborg Varme (Aalborg Forsyning)", ["aal_forsyning", "ft_pris"]),
             ("Nibe", "Eget værk: Nibe Varmeværk", ["ft_pris"])],
 "randers": [("Randers", "Verdo Varme", ["verdo_fv", "ft_pris"]),
             ("Assentoft", "Verdo udbygger, åben for tilmelding", ["verdo_omr"]),
             ("Langå", "Eget værk: Langå Varmeværk", ["ft_pris"]),
             ("Stevnstrup", "Verdo udbygger, åben for tilmelding", ["verdo_omr"]),
             ("Spentrup", "Under udbygning, over 580 tilmeldt", ["ran_fv", "verdo_omr"]),
             ("Harridslev", "Verdo udbygger, åben for tilmelding", ["verdo_omr"])],
 "horsens": [("Horsens", "Fjernvarme Horsens", ["fjho", "ft_pris"]),
             ("Brædstrup", "Eget værk: Brædstrup Fjernvarme", ["ft_pris"]),
             ("Østbirk", "Eget værk: Østbirk Varmeværk", ["ft_pris"]),
             ("Hovedgård", "Eget værk: Hovedgård Fjernvarme", ["ft_pris"])],
}
VP_TOWNS_NOTE = {
 "kolding": "Bor du i en af de mindre byer som Lunderskov eller Sønder Bjert, så tjek adressen på Kolding Kommunes kort over fjernvarme- og naturgasområder.",
 "vejle": "Bor du i fx Børkop, Brejning eller Bredsten, så tjek kommunens fjernvarmekort med de gule, blå og grønne områder.",
 "esbjerg": "Andrup og Egebæk ligger tæt på Esbjerg by. Tjek adressen hos DIN Forsyning eller på Plandata.dk.",
 "odense": "Bor du i Bellinge, Sankt Klemens, Fraugde eller en af landsbyerne, så tjek adressen hos Fjernvarme Fyn. Selskabet skriver, at de fleste store bebyggede områder er ved at være forbundne.",
 "aalborg": "I varmeplanen blev Hostrup, St. Restrup og Nr. Kongerslev screenet, men kun Ajstrup konverteres. Bor du i fx Svenstrup, Klarup eller Vodskov, så tjek adressen hos Aalborg Forsyning.",
 "randers": "Fårup, Øster Bjerregrav og de mindre landsbyer står ikke på Verdos liste over nye områder pr. oktober 2026.",
 "horsens": "Lund, Egebjerg, Gedved og Hatting: tjek adressen hos Fjernvarme Horsens eller på Plandata.dk.",
}
VP_XFAQ = {
 "kolding": [("Hvor mange huse i Kolding Kommune har stadig gasfyr?", lambda: f"Ifølge Danmarks Statistik havde {tal(HEAT['kolding']['CN'])} beboede parcel- og rækkehuse naturgas som opvarmning i 2026, og {tal(HEAT['kolding']['CO'])} havde oliefyr.", ["dst_bol102"])],
 "vejle": [("Hvor mange i Vejle har varmepumpe?", lambda: f"{tal(HEAT['vejle']['VP'])} beboede parcel- og rækkehuse i Vejle Kommune er registreret med varmepumpe ({hp('vejle','VP',1)}) ifølge Danmarks Statistik, 2026.", ["dst_bol102"])],
 "esbjerg": [("Hvor mange huse i Esbjerg Kommune har ikke fjernvarme?", lambda: f"Ca. {tal(hs('esbjerg')-HEAT['esbjerg']['FJ'])} af {tal(hs('esbjerg'))} beboede parcel- og rækkehuse ({pct(hs('esbjerg')-HEAT['esbjerg']['FJ'],hs('esbjerg'))}) ifølge Danmarks Statistik, 2026. Heraf har {tal(HEAT['esbjerg']['VP'])} allerede varmepumpe.", ["dst_bol102"])],
 "odense": [("Er der stadig oliefyr i Odense?", lambda: f"Kun få. Danmarks Statistik registrerer {tal(HEAT['odense']['CO'])} beboede parcel- og rækkehuse med oliefyr i Odense Kommune i 2026, ud af {tal(hs('odense'))}.", ["dst_bol102"])],
 "aalborg": [("Hvor mange huse i Aalborg Kommune har oliefyr?", lambda: f"{tal(HEAT['aalborg']['CO'])} beboede parcel- og rækkehuse ifølge Danmarks Statistik, 2026. {tal(HEAT['aalborg']['CN'])} har naturgas.", ["dst_bol102"])],
 "randers": [("Kan jeg skifte gas- eller oliefyret ud med fjernvarme i Randers?", lambda: f"Fjernvarmen dækker {hp('randers','FJ')} af husene i kommunen, mod {hp('dk','FJ')} på landsplan (Danmarks Statistik, 2026). Verdo har pr. oktober 2026 Assentoft, Harridslev, Stevnstrup og Spentrup åbne for tilmelding.", ["dst_bol102", "verdo_omr"])],
 "horsens": [("Hvor mange huse i Horsens Kommune har varmepumpe?", lambda: f"{tal(HEAT['horsens']['VP'])} beboede parcel- og rækkehuse ({hp('horsens','VP',1)}) ifølge Danmarks Statistik, 2026.", ["dst_bol102"])],
}

# ---------- fjernvarme-undersider ----------
FV_SOURCES = {
 "kolding": [("TREFOR Varme (i dag under EWII) leverer fjernvarmen i Kolding blandt andet ved at udnytte <strong>overskudsvarme fra raffinaderiet i Fredericia</strong> og varme fra affaldsforbrænding i Kolding.", ["trefor_v"]),
             ("I 2024 lagde TVIS en 4,7 km transmissionsledning fra Lyshøj Allé til Kokbjerg. Dermed kunne ca. <strong>1.900 boliger og virksomheder</strong> i Almind, Gravens, Ågård, Vester Nebel, Viuf og ved Kokbjerg få fjernvarme gennem TREFOR. Varmen blev leveret fra 10. september.", ["tvis_kol"])],
 "vejle": [("Den kollektive varme i Vejle Kommune leveres af <strong>9 lokale fjernvarmeværker</strong> og ét naturgasselskab.", ["vej_varme"]),
           ("Størstedelen af fjernvarmen er overskudsvarme leveret af TVIS, transmissionsselskabet i Trekantområdet.", ["vej_fv"])],
 "esbjerg": [("Det kulfyrede Esbjergværk blev taget ud af drift i sommeren 2024. Siden december 2024 har to <strong>havvandsvarmepumper</strong> på Esbjerg Havn (op til 70 MW) leveret grundlasten sammen med en elkedel og en fliskedel.", ["esb_fv"]),
             ("DIN Forsyning leverer til ca. 25.500 husstande i Esbjerg by, Varde, Alslev og Nordby på Fanø.", ["esb_fv"])],
 "odense": [("Fjernvarme Fyn slukkede for kullet på Fynsværket i <strong>april 2024</strong>. Blok 7 bygges om til gas og bruges kun på særligt kolde dage. Den fossile CO₂-udledning faldt fra ca. 900.000 tons i 2018 til ca. 400.000 tons i 2023.", ["ffyn_kul"]),
            ("En del af varmen kommer fra <strong>Metas datacenter i Tietgenbyen</strong>. Store ammoniakvarmepumper på ca. 45 MW hæver overskudsvarmen til 70-75 °C og sender den ud i Odenses fjernvarmenet.", ["ramboll_meta"])],
 "aalborg": [("Nordjyllandsværket skal udfases som kulfyret værk <strong>senest i 2028</strong>.", ["aal_ve"]),
             ("Aalborg Forsyning bygger derfor i Norbis Park en havvandsvarmepumpe, tre elkedler og et varmelager på 200.000 m³.", ["aal_forsyning"])],
 "randers": [("Verdo producerer fjernvarmen i Randers på <strong>Randers Kraftvarmeværk</strong>, der bruger certificeret bæredygtig biomasse i form af træflis og træpiller og laver el og varme på samme tid.", ["verdo_fv"]),
             ("I 2022 var produktionen i Randers baseret på 99,2 % vedvarende energi. Verdo undersøger blandt andet store varmepumper, overskudsvarme og geotermi til fremtiden.", ["verdo_fv"])],
 "horsens": [("Fjernvarme Horsens kalder sig Danmarks største forbrugerejede fjernvarmeselskab og producerede <strong>520.000 MWh varme i 2024</strong>.", ["fjho"]),
             ("Varmen kommer fra affaldsforbrænding og gasturbiner (45 MW varme), fire biomassekedler (60 MW), en elkedel og en varmepumpe (15 MW hver) samt overskudsvarme fra industri. Gascentraler dækker spids- og reservelast.", ["fjho"])],
}
FV_SHARE = {
 "kolding": lambda: f"{hp('kolding','FJ')} af de beboede parcel- og rækkehuse i Kolding Kommune har fjernvarme, mod {hp('dk','FJ')} i hele landet. Det efterlader {tal(hs('kolding')-HEAT['kolding']['FJ'])} huse med anden opvarmning, heraf {tal(HEAT['kolding']['CN'])} med naturgas.",
 "vejle": lambda: f"Vejle ligger præcis på landsgennemsnittet: {hp('vejle','FJ')} af de beboede parcel- og rækkehuse har fjernvarme. Til gengæld har {hp('vejle','VP',1)} varmepumpe, mere end i nogen af de andre {nw(1)} kommuner på dette site.",
 "esbjerg": lambda: f"{hp('esbjerg','FJ')} af husene i Esbjerg Kommune har fjernvarme. {tal(HEAT['esbjerg']['CO']+HEAT['esbjerg']['CN'])} huse har stadig olie- eller gasfyr, og {tal(HEAT['esbjerg']['VP'])} har varmepumpe.",
 "odense": lambda: f"I Odense Kommune har {hp('odense','FJ',1)} af de beboede parcel- og rækkehuse fjernvarme. Kun {tal(hs('odense')-HEAT['odense']['FJ'])} huse i hele kommunen varmes op på anden måde, og {tal(HEAT['odense']['VP'])} af dem har varmepumpe.",
 "aalborg": lambda: f"{hp('aalborg','FJ')} af husene i Aalborg Kommune har fjernvarme. Når prisen hos Aalborg Varme er over gennemsnittet, rammer det derfor rigtig mange husstande.",
 "randers": lambda: f"Kun {hp('randers','FJ')} af husene i Randers Kommune har fjernvarme, {rk(lambda x: HEAT[x]['FJ'] / hs(x), 'randers', 'laveste', rev=True)} andel blandt de {nw()} byer på dette site. {tal(HEAT['randers']['CN']+HEAT['randers']['CO'])} huse har gas- eller oliefyr.",
 "horsens": lambda: f"{hp('horsens','FJ')} af de beboede parcel- og rækkehuse i Horsens Kommune har fjernvarme. {tal(HEAT['horsens']['VP'])} har varmepumpe, og {tal(HEAT['horsens']['CN']+HEAT['horsens']['CO'])} har stadig gas- eller oliefyr.",
}
FV_SOURCES_H = {
 "kolding": "Hvor kommer fjernvarmen i Kolding fra?", "vejle": "Vejles fjernvarme: TVIS og 9 lokale værker",
 "esbjerg": "Havvandsvarmepumper i stedet for kul", "odense": "Fra kul til datacentervarme i Odense",
 "aalborg": "Aalborgs fjernvarme efter kullet", "randers": "Biomasse fra Randers Kraftvarmeværk", "horsens": "Sådan laver Fjernvarme Horsens varmen",
}
# Hvilken bys reg-side får en note om ældre huse (DST BOL101)
def reg_age_note(c, kommune):
    """Returnerer (tekst, kildenøgler)."""
    s = STOCK[c]; B = s["B"]; t = s["tot"]
    notes = {
        "kolding": (f"Godt hvert fjerde hus i kommunen ({pct(B['før 1960'], t)}) er fra før 1960. Står dit hus i en gammel bydel, så spørg om bevaringsværdi, før du bestiller.", []),
        "vejle": (f"{tal(B['2000+'])} af kommunens beboede huse er opført i 2000 eller senere. Bor du i en nyere udstykning, så tjek, om områdets lokalplan har krav til tage og facader.", []),
        "esbjerg": (f"Esbjerg Kommune har {tal(B['1960-1979'])} huse fra 1960-1979, {pct(B['1960-1979'], t)} af alle beboede parcel- og rækkehuse. Ifølge Bolius har mange parcelhuse fra 1960'erne og 1970'erne asbestholdige bølgeplade- eller kunstskifertage, så få taget vurderet, før panelerne skrues fast.", ["bolius_asb"]),
        "odense": (f"Odense har {tal(s['raekke'])} beboede række-, kæde- og dobbelthuse. Bor du i et af dem, så tjek også ejer- eller grundejerforeningens regler, ikke kun lokalplanen.", []),
        "aalborg": (f"Aalborg Kommune har {tal(t)} beboede parcel- og rækkehuse, og {pct(B['1960-1979'], t)} af dem er fra 1960-1979. Er dit tag fra den tid, så få det vurderet, før du bestiller.", []),
        "randers": (f"{pct(B['før 1960'], t)} af husene i Randers Kommune er bygget før 1960. Bor du i et ældre kvarter, så slå adressen op i kommunens lokalplaner.", []),
        "horsens": (f"Horsens har den største ejerandel blandt de {nw()} kommuner på sitet: {pct(s['ejer'], t)} af de beboede huse er ejerboliger. Som lejer skal du altid have udlejers accept først.", []),
    }
    return notes[c]

# ---------- daglig by-rutine 26. okt. 2026: Aarhus (93 % fjernvarme, ingen varmepumpe-byside) og Viborg ----------
SOL_ORDER.update({
 "aarhus": ["boliger", "lokalt", "tage", "produktion", "guides", "faq"],
 "viborg": ["lokalt", "produktion", "boliger", "tage", "faq", "guides"],
})
VP_ORDER.update({"viborg": ["lokale-byer", "opvarmning", "lokalt", "pris", "guides", "faq"]})
# Aarhus: varmepumpe-blokkene (lokalt, opvarmning, lokale-byer) bor på fjernvarmesiden
FV_ORDER.update({
 "aarhus": ["andel", "status", "priser", "lokalt", "opvarmning", "lokale-byer", "varmekilder", "billigst", "faq"],
 "viborg": ["status", "billigst", "priser", "varmekilder", "andel", "faq"],
})
def _flat(c): return ROOF[c]["T"]["02"] + ROOF[c]["T"]["04"]
SOL_PROD.update({
 "aarhus": ("Solceller i Aarhus: produktion fra forår til efterår",
   lambda: f"PVGIS beregner ca. {tal(PV['aarhus']['syd'])} kWh pr. kWp om året for et sydvendt tag med 35° hældning i Aarhus. Fra april til august giver hvert kWp mindst {min(PV['aarhus']['months'][3:8])} kWh om måneden, mens november til februar tilsammen kun giver ca. {sum(PV['aarhus']['months'][i] for i in (10, 11, 0, 1))} kWh. Ligger panelerne på et fladt tag, må de ikke stå mere end 1 meter over tagfladen uden byggetilladelse."),
 "viborg": ("Giver solceller mindre i Viborg end ved kysten?",
   lambda: f"Lidt. Viborg får ca. {tal(PV['viborg']['syd'])} kWh pr. kWp om året for et sydvendt anlæg på 35° (PVGIS), {rk(lambda x: PV[x]['syd'], 'viborg', 'laveste', art='det', rev=True)} af de {nw()} byer på dette site. Esbjerg ved Vestkysten får {tal(PV['esbjerg']['syd'])} kWh. Forskellen er ca. {round(100*(1-PV['viborg']['syd']/PV['esbjerg']['syd']))} %, svarende til ca. {tal((PV['esbjerg']['syd']-PV['viborg']['syd'])*6)} kWh om året for et 6 kWp-anlæg. Tagets retning og skygge betyder mere end beliggenheden."),
})
SOL_PROD_SRC_NEW = {"aarhus": ["pv_aarhus", "aar_sol"], "viborg": ["pv_viborg", "pv_esbjerg"]}
SOL_ROOF.update({
 "aarhus": ("Mange flade tage og tagpaptage i Aarhus",
   lambda: f"Tegl er det mest udbredte tag i Aarhus Kommune ({rp('aarhus','10')}), men {pct(_flat('aarhus'), ROOF['aarhus']['tot'])} af parcel- og rækkehusene har fladt tag eller tagpap, mod {pct(_flat('dk'), ROOF['dk']['tot'])} på landsplan. På et fladt tag sættes panelerne typisk på stativ, og Aarhus Kommune kræver byggetilladelse, hvis anlægget står mere end 1 meter over tagfladen. Bolius skriver, at gennembrydninger i tagpap skal tætnes omhyggeligt.",
   ["dst_bygb50", "aar_sol", "bolius_mont"]),
 "viborg": ("Eternittage og ældre huse i Viborg",
   lambda: f"Fibercement (eternit) er det mest udbredte tag i Viborg Kommune: {rp('viborg','06')} af parcel- og rækkehusene mod {rp('dk','06')} i hele landet. {pct(STOCK['viborg']['B']['før 1960'] + STOCK['viborg']['B']['1960-1979'], STOCK['viborg']['tot'])} af husene er bygget før 1980, og ifølge Bolius indeholder bølge- og kunstskiferplader fra før 1984 næsten altid asbest. Få derfor tagets alder og stand vurderet, før leverandøren skruer beslagene fast.",
   ["dst_bygb50", "dst_bol101", "bolius_asb"]),
})
SOL_HOMES.update({
 "aarhus": lambda: f"Aarhus Kommune har {tal(STOCK['aarhus']['tot'])} beboede parcel- og rækkehuse, flest af de {nw()} kommuner på dette site, og {pct(STOCK['aarhus']['raekke'],STOCK['aarhus']['tot'])} af dem er række-, kæde- eller dobbelthuse. Bor du i et rækkehus, så tjek både lokalplanen og ejer- eller grundejerforeningens regler. Siden gælder hele kommunen, også Lystrup, Beder-Malling, Løgten, Mårslet og Solbjerg.",
 "viborg": lambda: f"{pct(STOCK['viborg']['B']['før 1960'],STOCK['viborg']['tot'])} af de {tal(STOCK['viborg']['tot'])} beboede parcel- og rækkehuse i Viborg Kommune er bygget før 1960, {rk(lambda x: STOCK[x]['B']['før 1960'] / STOCK[x]['tot'], 'viborg', 'største')} andel af de {nw()} byer. Er huset fredet eller registreret som bevaringsværdigt, skal du kontakte kommunen, før du går i gang. Siden gælder også Bjerringbro, Stoholm, Karup, Løgstrup og Frederiks.",
})
SOL_HOMES_SRC_NEW = {"viborg": ["vib_sol"]}
SOL_HOMES_H.update({"aarhus": "Rækkehuse og parcelhuse i Aarhus Kommune", "viborg": "Ældre huse i Viborg Kommune"})
SOL_XFAQ.update({
 "aarhus": [("Kan jeg sætte solceller på et fladt tag i Aarhus?", lambda: f"Ja. Står panelerne højst 1 meter over tagfladen, og overholder huset afstanden på 2,5 meter til skel, kræver det som udgangspunkt ikke byggetilladelse. {pct(_flat('aarhus'), ROOF['aarhus']['tot'])} af husene i kommunen har fladt tag eller tagpap.", ["aar_sol", "dst_bygb50"])],
 "viborg": [("Kan det betale sig med solceller på et øst-vest-tag i Viborg?", lambda: f"Et østvendt tag giver ca. {tal(PV['viborg']['oest'])} kWh pr. kWp om året i Viborg og et vestvendt ca. {tal(PV['viborg']['vest'])} kWh, mod {tal(PV['viborg']['syd'])} kWh mod syd (PVGIS). Det er ca. {round(100*(1-PV['viborg']['oest']/PV['viborg']['syd']))} % mindre, men produktionen fordeles over flere af dagens timer.", ["pvo_viborg", "pvv_viborg", "pv_viborg"])],
})
VP_HEAT.update({
 "aarhus": ("Fjernvarme dominerer i Aarhus Kommune",
   lambda: f"{hp('aarhus','FJ',1)} af de {tal(hs('aarhus'))} beboede parcel- og rækkehuse i Aarhus Kommune har fjernvarme. Kun {tal(HEAT['aarhus']['VP'])} har varmepumpe og {tal(HEAT['aarhus']['CO'])} oliefyr, og naturgas er stort set væk: Danmarks Statistik registrerer {tal(HEAT['aarhus']['CN'])} {'hus' if HEAT['aarhus']['CN'] == 1 else 'huse'} med naturgas."),
 "viborg": ("Viborg har den største andel oliefyr på sitet",
   lambda: f"{tal(HEAT['viborg']['CO'])} beboede parcel- og rækkehuse i Viborg Kommune ({hp('viborg','CO',1)}) varmes stadig op med oliefyr, den højeste andel af de {nw()} byer, og {tal(HEAT['viborg']['CN'])} ({hp('viborg','CN',1)}) har naturgas. {hp('viborg','FJ',1)} har fjernvarme, tæt på landsgennemsnittet på {hp('dk','FJ',1)}. Det er olie- og gasfyrene uden for fjernvarmeplanerne, som Varmepumpepuljen er rettet mod."),
})
VP_HEAT_SRC_NEW = {"viborg": ["se_vpp"]}
VP_ADVICE.update({
 "viborg": ("Energistyrelsens rådgivere holder et gratis møde om varmepumper i Viborg Kommune <strong>torsdag 29. oktober 2026 kl. 17-19</strong> i Østfjendshallen, Kalkværksvej 18, Mønsted.", ["se_moeder"]),
})
VP_TOWNS.update({
 "aarhus": [("Aarhus", "Kredsløb Fjernvarme", ["kredslob", "ft_pris"]),
            ("Lystrup", "Eget værk: Lystrup Fjernvarme", ["ft_pris"]),
            ("Løgten", "Eget værk: Løgten-Skødstrup Fjernvarmeværk", ["ft_pris"]),
            ("Sabro", "Ny transmissionsledning i Kredsløbs planforslag", ["aar_ff"]),
            ("Harlev", "Ny transmissionsledning i Kredsløbs planforslag", ["aar_ff"]),
            ("Lillering", "Undersøgt af Kredsløb, for lidt tilslutning: ikke varmeplansområde", ["aar_mr"]),
            ("Hørret", "Undersøgt af Kredsløb, for lidt tilslutning: ikke varmeplansområde", ["aar_mr"]),
            ("Fårup", "Undersøgt af Kredsløb, for lidt tilslutning: ikke varmeplansområde", ["aar_mr"])],
 "viborg": [("Viborg", "Viborg Varme, konverterer gasområder kvarter for kvarter", ["vib_slip", "ft_pris"]),
            ("Bjerringbro", "Gudenådalens Energiselskab", ["vib_strat", "ft_pris"]),
            ("Stoholm", "Eget værk: Stoholm Fjernvarmeværk", ["ft_pris"]),
            ("Karup", "Eget værk: Karup Varmeværk", ["ft_pris"]),
            ("Løgstrup", "Eget værk: Løgstrup Varmeværk", ["ft_pris"]),
            ("Ørum", "Eget værk: Ørum Varmeværk", ["ft_pris"]),
            ("Hammershøj", "Eget værk: Hammershøj Fjernvarmeværk", ["ft_pris"])],
})
VP_TOWNS_NOTE.update({
 "aarhus": "Bor du i Mårslet, Solbjerg, Hjortshøj eller Trige, så tjek adressen hos Kredsløb eller på Plandata.dk, før du søger tilskud.",
 "viborg": "Bor du i en mindre landsby uden eget værk, så tjek Viborg Kommunes varmeplan på Minimap og Viborg Varmes projektliste, før du vælger varmepumpe.",
})
VP_XFAQ.update({
 "aarhus": [("Hvor mange huse i Aarhus Kommune har ikke fjernvarme?", lambda: f"Ca. {tal(hs('aarhus')-HEAT['aarhus']['FJ'])} af {tal(hs('aarhus'))} beboede parcel- og rækkehuse ({pct(hs('aarhus')-HEAT['aarhus']['FJ'],hs('aarhus'),1)}) ifølge Danmarks Statistik, 2026. Heraf har {tal(HEAT['aarhus']['VP'])} allerede varmepumpe, og {tal(HEAT['aarhus']['CO'])} har oliefyr.", ["dst_bol102"])],
 "viborg": [("Hvor mange huse i Viborg Kommune har olie- eller gasfyr?", lambda: f"Danmarks Statistik registrerer {tal(HEAT['viborg']['CO'])} beboede parcel- og rækkehuse med oliefyr og {tal(HEAT['viborg']['CN'])} med naturgas i 2026, ud af {tal(hs('viborg'))}. {tal(HEAT['viborg']['VP'])} har allerede varmepumpe.", ["dst_bol102"])],
})
FV_SOURCES.update({
 "aarhus": [("Aftalen om træpillevarme fra <strong>Studstrupværket</strong> udløber i 2030, og Kredsløb mister dermed 500 MW varmekapacitet. Kredsløbs eget halmfyrede kraftvarmeværk og affaldsforbrændingen skal fremover dække 45-50 % af varmen, resten skal være elbaseret.", ["aar_geo"]),
            ("Siden oktober 2025 har Kredsløb fået <strong>20 MW geotermisk varme</strong> fra Innargis anlæg i Skejby. I 2030 skal Innargi levere 111 MW fra tre anlæg: Skejby, Bautavej og Halmstadsgade.", ["aar_geo"]),
            ("Ved <strong>Egå Renseanlæg</strong> skal en spildevandsvarmepumpe på 8 MW anlægges fra november 2026 til februar 2028. En større spildevandsvarmepumpe på 23 MW ved Aarhus ReWater er udskudt til 2037.", ["aar_egaa", "aar_ff"])],
 "viborg": [("Viborg Varme har ca. 12.500 kunder. Varmen kommer i dag bl.a. fra en luft til vand-varmepumpe på 15 MW, en grundvands- og søvarmepumpe på 6 MW, en elkedel på 50 MW og gaskedler på 90 MW.", ["vib_df"]),
            ("Fra andet halvår 2027 begynder Viborg Varme at modtage <strong>overskudsvarme fra Apples datacenter</strong> og Energinets transformerstation i Tjele, først 12 MW og forventet 24,5 MW inden 2030. Varmen sendes 4,5 km til Taphede.", ["vib_df"])],
})
FV_SHARE.update({
 "aarhus": lambda: f"{hp('aarhus','FJ',1)} af de beboede parcel- og rækkehuse i Aarhus Kommune har fjernvarme. Kun Odense har en højere andel blandt de {nw()} byer på dette site. Det efterlader ca. {tal(hs('aarhus')-HEAT['aarhus']['FJ'])} huse med anden opvarmning, heraf {tal(HEAT['aarhus']['VP'])} med varmepumpe.",
 "viborg": lambda: f"{hp('viborg','FJ',1)} af de beboede parcel- og rækkehuse i Viborg Kommune har fjernvarme, mod {hp('dk','FJ',1)} i hele landet. {tal(HEAT['viborg']['CN']+HEAT['viborg']['CO'])} huse har gas- eller oliefyr, og {tal(HEAT['viborg']['VP'])} har varmepumpe.",
})
FV_SOURCES_H.update({"aarhus": "Aarhus efter Studstrupværket: geotermi og varmepumper", "viborg": "Overskudsvarme fra Apple og Tjele til Viborg"})
_reg_age_old = reg_age_note
def reg_age_note(c, kommune):
    s = STOCK[c]; B = s["B"]; t = s["tot"]
    if c == "aarhus":
        return (f"Aarhus Kommune har {tal(s['raekke'])} beboede række-, kæde- og dobbelthuse ({pct(s['raekke'], t)} af alle parcel- og rækkehuse). Bor du i et af dem, så tjek også bebyggelsens lokalplan og ejer- eller grundejerforeningens regler for tagene.", [])
    if c == "viborg":
        return (f"{pct(B['før 1960'], t)} af husene i Viborg Kommune er bygget før 1960, {rk(lambda x: STOCK[x]['B']['før 1960'] / STOCK[x]['tot'], 'viborg', 'største')} andel af de {nw()} byer på sitet. Er dit hus registreret som bevaringsværdigt, så kontakt kommunen, før du går i gang.", ["vib_sol"])
    return _reg_age_old(c, kommune)


# ---------- daglig by-rutine 27. okt. 2026: Næstved (første by øst for Storebælt, DK2) og Silkeborg ----------
_FJ = lambda x: HEAT[x]["FJ"] / hs(x); _CN = lambda x: HEAT[x]["CN"] / hs(x); _EL = lambda x: HEAT[x]["ELV"] / hs(x)
_PVY = lambda x: PV[x]["syd"]; _NEW = lambda x: STOCK[x]["B"]["2000+"] / STOCK[x]["tot"]; _OLD = lambda x: STOCK[x]["B"]["før 1960"] / STOCK[x]["tot"]
SOL_ORDER.update({
 "naestved": ["produktion", "lokalt", "boliger", "tage", "faq", "guides"],
 "silkeborg": ["lokalt", "tage", "boliger", "produktion", "guides", "faq"],
})
VP_ORDER.update({
 "naestved": ["opvarmning", "lokale-byer", "lokalt", "pris", "faq", "guides"],
 "silkeborg": ["lokale-byer", "lokalt", "pris", "opvarmning", "faq", "guides"],
})
FV_ORDER.update({
 "naestved": ["andel", "status", "billigst", "priser", "varmekilder", "faq"],
 "silkeborg": ["varmekilder", "status", "andel", "billigst", "priser", "faq"],
})
SOL_PROD.update({
 "naestved": ("Mere sol på Sydsjælland: produktion i Næstved",
   lambda: f"PVGIS beregner ca. <strong>{tal(PV['naestved']['syd'])} kWh pr. kWp om året</strong> for et sydvendt tag med 35° hældning i Næstved, {rk(_PVY, 'naestved', 'højeste')} af de {nw()} byer på dette site. Et 6 kWp-anlæg giver dermed ca. {tal(PV['naestved']['syd']*6)} kWh. Maj og juni giver hver ca. {tal(PV['naestved']['months'][5]*6)} kWh fra 6 kWp, mens december kun giver ca. {tal(PV['naestved']['months'][11]*6)} kWh."),
 "silkeborg": ("Søhøjlandet og solen: produktion i Silkeborg",
   lambda: f"For et sydvendt tag med 35° hældning i Silkeborg beregner PVGIS ca. {tal(PV['silkeborg']['syd'])} kWh pr. kWp om året, {rk(_PVY, 'silkeborg', 'laveste', rev=True)} af de {nw()} byer på dette site. Et 6 kWp-anlæg ender på omkring {tal(PV['silkeborg']['syd']*6)} kWh. Ligger huset ved skov eller skrænt, betyder skyggen mere end den beregnede forskel mellem byerne, så få installatøren til at måle på netop dit tag."),
})
SOL_PROD_SRC_NEW.update({"naestved": ["pv_naestved"], "silkeborg": ["pv_silkeborg"]})
SOL_ROOF.update({
 "naestved": ("Stråtage og eternit i Næstved Kommune",
   lambda: f"Fibercement er det mest udbredte tag på parcel- og rækkehusene i Næstved Kommune ({rp('naestved','06')} mod {rp('dk','06')} i hele landet). {tal(ROOF['naestved']['T']['14'])} huse har <strong>stråtag</strong> ({rp('naestved','14',1)}), {rk(lambda x: ROOF[x]['T']['14'] / ROOF[x]['tot'], 'naestved', 'højeste')} andel af de {nw()} kommuner på sitet. Står et stråtagshus i et bevaringsværdigt kulturmiljø, kan lokalplanen helt forbyde solceller: i Appenæs stadfæstede Planklagenævnet i 2026 et afslag på solcelletagsten i stedet for stråtag.",
   ["dst_bygb50", "nae_pkn102"]),
 "silkeborg": ("Betontagsten, eternit og flade tage i Silkeborg",
   lambda: f"I Silkeborg Kommune er betontagsten og fibercement næsten lige udbredt: {rp('silkeborg','08')} og {rp('silkeborg','06')} af parcel- og rækkehusene. {pct(_flat('silkeborg'), ROOF['silkeborg']['tot'])} har fladt tag eller tagpap, mod {pct(_flat('dk'), ROOF['dk']['tot'])} på landsplan. Kræver anlægget, at tagkonstruktionen forstærkes, fx på grund af øget last, skal du ifølge kommunen søge byggetilladelse.",
   ["dst_bygb50", "sil_byg"]),
})
SOL_HOMES.update({
 "naestved": lambda: f"{pct(STOCK['naestved']['B']['før 1960'],STOCK['naestved']['tot'])} af de {tal(STOCK['naestved']['tot'])} beboede parcel- og rækkehuse i Næstved Kommune er bygget før 1960, {rk(_OLD, 'naestved', 'største')} andel af de {nw()} byer. Næstved Kommune kræver altid byggetilladelse til solceller på fredede og bevaringsværdige bygninger. Siden gælder også Fensmark, Fuglebjerg, Glumsø, Mogenstrup og Karrebæksminde.",
 "silkeborg": lambda: f"Silkeborg Kommune har {tal(STOCK['silkeborg']['tot'])} beboede parcel- og rækkehuse, og {pct(STOCK['silkeborg']['B']['2000+'],STOCK['silkeborg']['tot'])} er bygget i 2000 eller senere, {rk(_NEW, 'silkeborg', 'højeste')} andel af de {nw()} byer. I nyere udstykninger regulerer lokalplanen ofte tagene, så slå adressen op på Silkeborglokalplaner.dk. Siden gælder også Kjellerup, Sejs-Svejbæk, Virklund, Them og Bryrup.",
})
SOL_HOMES_SRC_NEW.update({"naestved": ["nae_byg"], "silkeborg": ["sil_byg"]})
SOL_HOMES_H.update({"naestved": "Gamle huse i Næstved Kommune", "silkeborg": "Nyere huse i Silkeborg Kommune"})
SOL_XFAQ.update({
 "naestved": [("Giver solceller mere i Næstved end i de jyske byer?", lambda: f"PVGIS' strålingsdata giver Næstved ca. {tal(PV['naestved']['syd'])} kWh pr. kWp om året mod fx {tal(PV['aarhus']['syd'])} kWh i Aarhus og {tal(PV['viborg']['syd'])} kWh i Viborg, for samme sydvendte tag på 35°. Forskellen er ca. {round(100*(PV['naestved']['syd']/PV['viborg']['syd']-1))} % i forhold til Viborg. Tagets retning og skygge betyder stadig mest.", ["pv_naestved", "pv_aarhus", "pv_viborg"])],
 "silkeborg": [("Hvor meget mindre giver et øst- eller vestvendt tag i Silkeborg?", lambda: f"Ca. {tal(PV['silkeborg']['oest'])} kWh pr. kWp om året mod øst og {tal(PV['silkeborg']['vest'])} kWh mod vest, mod {tal(PV['silkeborg']['syd'])} kWh mod syd (PVGIS, 35°). Det er ca. {round(100*(1-PV['silkeborg']['oest']/PV['silkeborg']['syd']))} % mindre, men produktionen fordeles over flere timer af dagen.", ["pvo_silkeborg", "pvv_silkeborg", "pv_silkeborg"])],
})
VP_HEAT.update({
 "naestved": ("Næstved har flest gasfyr på sitet",
   lambda: f"{tal(HEAT['naestved']['CN'])} beboede parcel- og rækkehuse i Næstved Kommune ({hp('naestved','CN',1)}) varmes op med naturgas, {rk(_CN, 'naestved', 'højeste')} andel af de {nw()} byer og næsten lige så mange som dem med fjernvarme ({hp('naestved','FJ',1)}, {rk(_FJ, 'naestved', 'laveste', rev=True)} andel). {tal(HEAT['naestved']['ELV'])} huse har elvarme ({hp('naestved','ELV',1)} mod {hp('dk','ELV',1)} på landsplan). Det er netop olie-, gas- og elvarme uden for fjernvarmen, som Varmepumpepuljen er rettet mod."),
 "silkeborg": ("Naturgas fylder stadig meget i Silkeborg Kommune",
   lambda: f"{hp('silkeborg','FJ',1)} af de {tal(hs('silkeborg'))} beboede parcel- og rækkehuse i Silkeborg Kommune har fjernvarme, mens {tal(HEAT['silkeborg']['CN'])} ({hp('silkeborg','CN',1)}) har naturgas og {tal(HEAT['silkeborg']['VP'])} ({hp('silkeborg','VP',1)}) allerede har varmepumpe. Ifølge Silkeborg Forsyning har de fleste i Silkeborg Syd i dag gasfyr, og det er dér, fjernvarmen nu lægges ud."),
})
VP_HEAT_SRC_NEW.update({"naestved": ["se_vpp"], "silkeborg": ["sil_syd"]})
VP_TOWNS.update({
 "naestved": [("Næstved", "Næstved Fjernvarme. Godkendt i byen, men Holsted Vest og Syd er droppet, og Holsted Nord har frist 30/11 2026", ["nae_fv", "nae_vest", "nae_nord"]),
              ("Fensmark", "Eget værk. Godkendt i den sydlige del, to gasområder under afklaring", ["nae_fv", "ft_pris"]),
              ("Fuglebjerg", "Eget værk: Fuglebjerg Fjernvarmeværk", ["ft_pris", "nae_fv"]),
              ("Glumsø", "Fjernvarme er godkendt", ["nae_fv"]),
              ("Mogenstrup", "Fjernvarme er undersøgt og kan ikke lade sig gøre", ["nae_fv"]),
              ("Karrebæksminde", "Fjernvarme er godkendt (Karrebæk)", ["nae_fv"]),
              ("Sandved", "Eget værk: Sandved-Tornemark Kraftvarmeværk", ["ft_pris", "nae_fv"])],
 "silkeborg": [("Silkeborg", "Silkeborg Forsyning (Silkeborg Varme)", ["sil_faq", "ft_pris"]),
               ("Kjellerup", "Eget værk: Kjellerup Fjernvarme", ["ft_pris"]),
               ("Sejs-Svejbæk", "Silkeborg Syd: gravearbejde fra slutningen af 2026", ["sil_syd"]),
               ("Virklund", "Silkeborg Syd: gravearbejde fra slutningen af 2026", ["sil_syd"]),
               ("Them", "Silkeborg Syd: gravearbejde fra slutningen af 2026", ["sil_syd"]),
               ("Voel", "59 % tilmeldt, gravearbejde fra andet halvår 2026", ["sil_voel"]),
               ("Ans", "Eget værk: Ans Fjernvarmeværk", ["ft_pris"])],
})
VP_TOWNS_NOTE.update({
 "naestved": "Bor du i Tappernøje, Herlufmagle, Holme-Olstrup eller en af landsbyerne, så slå adressen op på Næstved Kommunes fjernvarmekort, før du søger tilskud.",
 "silkeborg": "Bor du i Bryrup, Gjern, Fårvang eller en mindre landsby, så tjek adressen hos Silkeborg Forsyning og på Plandata.dk. Resenbro og Skærbæk er også ved at få fjernvarme.",
})
VP_XFAQ.update({
 "naestved": [("Hvor mange huse i Næstved Kommune har gasfyr eller elvarme?", lambda: f"Danmarks Statistik registrerer {tal(HEAT['naestved']['CN'])} beboede parcel- og rækkehuse med naturgas, {tal(HEAT['naestved']['ELV'])} med elvarme og {tal(HEAT['naestved']['CO'])} med oliefyr i 2026, ud af {tal(hs('naestved'))}. {tal(HEAT['naestved']['VP'])} har allerede varmepumpe.", ["dst_bol102"])],
 "silkeborg": [("Hvor mange i Silkeborg Kommune har allerede varmepumpe?", lambda: f"{tal(HEAT['silkeborg']['VP'])} beboede parcel- og rækkehuse ({hp('silkeborg','VP',1)}) ifølge Danmarks Statistik, 2026, mod {hp('dk','VP',1)} på landsplan. Ifølge Silkeborg Forsyning har kun 8 % af dem med varmepumpe i Silkeborg Syd tilmeldt sig fjernvarme.", ["dst_bol102", "sil_syd"])],
})
FV_SOURCES.update({
 "naestved": [("Ca. <strong>87 % af fjernvarmen</strong> fra Næstved Fjernvarme kommer fra affaldsforbrænding. Værket har fået overskudsvarme fra det fælleskommunale forbrændingsanlæg, i dag AffaldPlus, siden 1983.", ["nae_om"]),
              ("Næstved Fjernvarmes plan er, at <strong>99,5 % af varmen</strong> skal komme fra vedvarende energikilder i 2028. Værket blev stiftet i 1965 og er et andelsselskab ejet af kunderne.", ["nae_om"])],
 "silkeborg": [("Solvarmeanlægget på <strong>Sejling Hede</strong> kom i drift i slutningen af 2016 og dækker ca. 20 % af varmebehovet i Silkeborg. Siden 2019 har et røggaskøleanlæg udnyttet energien i naturgassen fra kraftværket bedre.", ["sil_faq"]),
               ("Et nyt <strong>varmepumpeanlæg</strong> og et <strong>biomasseanlæg</strong>, der bruger have- og parkaffald, blev taget i drift og officielt indviet 4. september 2026. Fra 2014 til 2024 faldt CO₂-udledningen fra varmen fra 196 til 66,6 kg pr. MWh.", ["sil_df"])],
})
FV_SHARE.update({
 "naestved": lambda: f"Kun {hp('naestved','FJ',1)} af de beboede parcel- og rækkehuse i Næstved Kommune har fjernvarme, {rk(_FJ, 'naestved', 'laveste', rev=True)} andel af de {nw()} byer på dette site, mod {hp('dk','FJ',1)} i hele landet. {tal(HEAT['naestved']['CN']+HEAT['naestved']['CO']+HEAT['naestved']['ELV'])} huse har gas, olie eller elvarme.",
 "silkeborg": lambda: f"{hp('silkeborg','FJ',1)} af de beboede parcel- og rækkehuse i Silkeborg Kommune har fjernvarme, mod {hp('dk','FJ',1)} i hele landet. {tal(HEAT['silkeborg']['CN'])} huse har naturgas, {tal(HEAT['silkeborg']['CO'])} oliefyr og {tal(HEAT['silkeborg']['VP'])} varmepumpe.",
})
FV_SOURCES_H.update({"naestved": "Affaldsvarme fra AffaldPlus i Næstved", "silkeborg": "Solvarme, varmepumper og biomasse i Silkeborg"})
_reg_age_old2 = reg_age_note
def reg_age_note(c, kommune):
    s = STOCK[c]; B = s["B"]; t = s["tot"]
    if c == "naestved":
        return (f"{tal(B['før 1960'])} af de beboede huse i Næstved Kommune ({pct(B['før 1960'], t)}) er bygget før 1960. Er dit hus fredet eller bevaringsværdigt, skal du altid søge, uanset hvordan panelerne monteres.", ["nae_byg"])
    if c == "silkeborg":
        return (f"{tal(B['2000+'])} af kommunens beboede huse er opført i 2000 eller senere. Mange nyere udstykninger har lokalplaner med krav til tagene, så tjek Silkeborglokalplaner.dk, før du bestiller.", ["sil_byg"])
    return _reg_age_old2(c, kommune)

# ---------- tjek af sammenlignende udsagn: bygget fejler, hvis en ny by gør et udsagn forkert ----------
_PVs = lambda c: PV[c]["syd"]; _rt = lambda k: (lambda c: ROOF[c]["T"][k] / ROOF[c]["tot"]); _hf = lambda k: (lambda c: HEAT[c][k] / hs(c)); _sb = lambda k: (lambda c: STOCK[c]["B"][k] / STOCK[c]["tot"])
CLAIMS = [
 ("Esbjerg top 2 PV", rank(_PVs, "esbjerg") <= 2),
 ("Aalborg top 2 juni", rank(lambda c: PV[c]["months"][5], "aalborg") <= 2),
 ("Odense flest tegl", top(_rt("10")) == "odense"), ("Aalborg flest fibercement", top(_rt("06")) == "aalborg"),
 ("Vejle ikke nr. 1 nyere huse", rank(_sb("2000+"), "vejle") > 1),
 ("Esbjerg flest 1960-79", top(_sb("1960-1979")) == "esbjerg"), ("Viborg top 2 før 1960", rank(_sb("før 1960"), "viborg") <= 2),
 ("Aarhus flest huse", top(lambda c: STOCK[c]["tot"]) == "aarhus"), ("Aalborg nr. 2 huse", rank(lambda c: STOCK[c]["tot"], "aalborg") == 2),
 ("Horsens højeste ejerandel", top(lambda c: STOCK[c]["ejer"] / STOCK[c]["tot"]) == "horsens"),
 ("Vejle højeste VP-andel", top(_hf("VP")) == "vejle"), ("Odense højeste FJ", top(_hf("FJ")) == "odense"), ("Aarhus nr. 2 FJ", rank(_hf("FJ"), "aarhus") == 2),

 ("Viborg højeste olie, Randers nr. 2", top(_hf("CO")) == "viborg" and rank(_hf("CO"), "randers") == 2),
 ("Næstved flest gasfyr (overskrift)", top(_hf("CN")) == "naestved"),
]
_bad = [n for n, ok in CLAIMS if not ok]
assert not _bad, f"Sammenlignende udsagn passer ikke længere: {_bad}"
