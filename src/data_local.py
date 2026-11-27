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
_NUMW = {6: "seks", 7: "syv", 8: "otte", 9: "ni", 10: "ti", 11: "elleve", 12: "tolv", 13: "tretten", 14: "fjorten", 15: "femten", 16: "seksten", 17: "sytten", 18: "atten", 19: "nitten", 20: "tyve", 21: "enogtyve", 22: "toogtyve", 23: "treogtyve", 24: "fireogtyve", 25: "femogtyve", 26: "seksogtyve", 27: "syvogtyve", 28: "otteogtyve", 29: "niogtyve", 30: "tredive", 31: "enogtredive", 32: "toogtredive", 33: "treogtredive", 34: "fireogtredive", 35: "femogtredive", 36: "seksogtredive", 37: "syvogtredive", 38: "otteogtredive", 39: "niogtredive", 40: "fyrre", 41: "enogfyrre", 42: "toogfyrre", 43: "treogfyrre", 44: "fireogfyrre", 45: "femogfyrre", 46: "seksogfyrre", 47: "syvogfyrre", 48: "otteogfyrre", 49: "niogfyrre", 50: "halvtreds", 51: "enoghalvtreds", 52: "tooghalvtreds", 53: "treoghalvtreds", 54: "fireoghalvtreds", 55: "femoghalvtreds", 56: "seksoghalvtreds", 57: "syvoghalvtreds", 58: "otteoghalvtreds", 59: "nioghalvtreds", 60: "tres", 61: "enogtres", 62: "toogtres", 63: "treogtres", 64: "fireogtres", 65: "femogtres", 66: "seksogtres", 67: "syvogtres", 68: "otteogtres", 69: "niogtres", 70: "halvfjerds", 71: "enoghalvfjerds", 72: "tooghalvfjerds", 73: "treoghalvfjerds", 74: "fireoghalvfjerds", 75: "femoghalvfjerds", 76: "seksoghalvfjerds", 77: "syvoghalvfjerds", 78: "otteoghalvfjerds", 79: "nioghalvfjerds", 80: "firs", 81: "enogfirs", 82: "toogfirs", 83: "treogfirs", 84: "fireogfirs", 85: "femogfirs", 86: "seksogfirs", 87: "syvogfirs", 88: "otteogfirs", 89: "niogfirs", 90: "halvfems", 91: "enoghalvfems", 92: "tooghalvfems", 93: "treoghalvfems", 94: "fireoghalvfems", 95: "femoghalvfems", 96: "seksoghalvfems", 97: "syvoghalvfems", 98: "otteoghalvfems", 99: "nioghalvfems", 100: "hundrede", 101: "ethundredeogen", 102: "ethundredeogto", 103: "ethundredeogtre", 104: "ethundredeogfire", 105: "ethundredeogfem"}
def nw(k=0): return _NUMW[len(NAMES) - k]          # "ni" for 9 byer, nw(1) = "otte" (de andre)
def top(f, rev=False):
    """By med højeste (eller laveste, rev=True) værdi blandt sitets byer. Bruges til at tjekke sammenlignende udsagn."""
    return sorted(NAMES, key=f, reverse=not rev)[0]
def rank(f, c): return sorted(NAMES, key=f, reverse=True).index(c) + 1
_ORDP = {1: "", 2: "næst", 3: "tredje", 4: "fjerde", 5: "femte", 6: "sjette", 7: "syvende", 8: "ottende", 9: "niende", 10: "tiende", 11: "ellevte", 12: "tolvte", 13: "trettende", 14: "fjortende", 15: "femtende", 16: "sekstende", 17: "syttende", 18: "attende", 19: "nittende", 20: "tyvende", 21: "enogtyvende", 22: "toogtyvende", 23: "treogtyvende", 24: "fireogtyvende", 25: "femogtyvende", 26: "seksogtyvende", 27: "syvogtyvende", 28: "otteogtyvende", 29: "niogtyvende", 30: "tredivte", 31: "enogtredivte", 32: "toogtredivte", 33: "treogtredivte", 34: "fireogtredivte", 35: "femogtredivte", 36: "seksogtredivte", 37: "syvogtredivte", 38: "otteogtredivte", 39: "niogtredivte", 40: "fyrretyvende", 41: "enogfyrretyvende", 42: "toogfyrretyvende", 43: "treogfyrretyvende", 44: "fireogfyrretyvende", 45: "femogfyrretyvende", 46: "seksogfyrretyvende", 47: "syvogfyrretyvende", 48: "otteogfyrretyvende", 49: "niogfyrretyvende", 50: "halvtredsindstyvende", 51: "enoghalvtredsindstyvende", 52: "tooghalvtredsindstyvende", 53: "treoghalvtredsindstyvende", 54: "fireoghalvtredsindstyvende", 55: "femoghalvtredsindstyvende", 56: "seksoghalvtredsindstyvende", 57: "syvoghalvtredsindstyvende", 58: "otteoghalvtredsindstyvende", 59: "nioghalvtredsindstyvende", 60: "tresindstyvende", 61: "enogtresindstyvende", 62: "toogtresindstyvende", 63: "treogtresindstyvende", 64: "fireogtresindstyvende", 65: "femogtresindstyvende", 66: "seksogtresindstyvende", 67: "syvogtresindstyvende", 68: "otteogtresindstyvende", 69: "niogtresindstyvende", 70: "halvfjerdsindstyvende", 71: "enoghalvfjerdsindstyvende", 72: "tooghalvfjerdsindstyvende", 73: "treoghalvfjerdsindstyvende", 74: "fireoghalvfjerdsindstyvende", 75: "femoghalvfjerdsindstyvende", 76: "seksoghalvfjerdsindstyvende", 77: "syvoghalvfjerdsindstyvende", 78: "otteoghalvfjerdsindstyvende", 79: "nioghalvfjerdsindstyvende", 80: "firsindstyvende", 81: "enogfirsindstyvende", 82: "toogfirsindstyvende", 83: "treogfirsindstyvende", 84: "fireogfirsindstyvende", 85: "femogfirsindstyvende", 86: "seksogfirsindstyvende", 87: "syvogfirsindstyvende", 88: "otteogfirsindstyvende", 89: "niogfirsindstyvende", 90: "halvfemsindstyvende", 91: "enoghalvfemsindstyvende", 92: "tooghalvfemsindstyvende", 93: "treoghalvfemsindstyvende", 94: "fireoghalvfemsindstyvende", 95: "femoghalvfemsindstyvende", 96: "seksoghalvfemsindstyvende", 97: "syvoghalvfemsindstyvende", 98: "otteoghalvfemsindstyvende", 99: "nioghalvfemsindstyvende", 100: "hundredende", 101: "ethundredeogførste", 102: "ethundredeoganden", 103: "ethundredeogtredje", 104: "ethundredeogfjerde", 105: "ethundredeogfemte"}
def rk(f, c, word, art="den", rev=False):
    """Rangord, fx 'den højeste', 'den næsthøjeste' (rev=True tæller fra bunden). Holder sammenlignende udsagn sande, når nye byer kommer til."""
    r = sorted(NAMES, key=f, reverse=not rev).index(c) + 1
    return f"{art} {_ORDP[r]}{word}"
_EJ = lambda x: STOCK[x]["ejer"] / STOCK[x]["tot"]
def above(f, c):
    """Navne på byer med højere værdi end c (til 'Kun X og Y har en højere andel')."""
    a = [NAMES[x] for x in sorted(NAMES, key=f, reverse=True)[:rank(f, c) - 1]]
    return a[0] if len(a) == 1 else ", ".join(a[:-1]) + " og " + a[-1]

NAMES = {"kolding": "Kolding", "vejle": "Vejle", "esbjerg": "Esbjerg", "odense": "Odense", "aalborg": "Aalborg", "randers": "Randers", "horsens": "Horsens", "aarhus": "Aarhus", "viborg": "Viborg", "naestved": "Næstved", "silkeborg": "Silkeborg", "holbaek": "Holbæk", "slagelse": "Slagelse", "roskilde": "Roskilde", "soenderborg": "Sønderborg", "koege": "Køge", "svendborg": "Svendborg", "faaborg": "Faaborg", "aabenraa": "Aabenraa", "herning": "Herning", "greve": "Greve", "hjoerring": "Hjørring", "holte": "Holte", "nykoebing-falster": "Nykøbing Falster", "haderslev": "Haderslev", "frederikshavn": "Frederikshavn", "hedensted": "Hedensted", "ringkoebing": "Ringkøbing", "helsingoer": "Helsingør", "stenloese": "Stenløse", "frederikssund": "Frederikssund", "skanderborg": "Skanderborg", "vordingborg": "Vordingborg", "koebenhavn": "København", "vejen": "Vejen", "varde": "Varde", "faxe": "Faxe", "kalundborg": "Kalundborg", "skive": "Skive", "gladsaxe": "Gladsaxe", "kongens-lyngby": "Kongens Lyngby", "holstebro": "Holstebro", "fredensborg": "Fredensborg", "nakskov": "Nakskov", "assens": "Assens", "hinnerup": "Hinnerup", "helsinge": "Helsinge", "middelfart": "Middelfart", "toender": "Tønder", "roenne": "Rønne", "hobro": "Hobro", "ebeltoft": "Ebeltoft", "thisted": "Thisted", "frederiksberg": "Frederiksberg", "gentofte": "Gentofte", "hvidovre": "Hvidovre", "hoersholm": "Hørsholm", "roedovre": "Rødovre", "ballerup": "Ballerup"}
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
   lambda: f"{rp('odense','10')} af parcel- og rækkehusene i Odense Kommune har tegltag. Det er {rk(lambda x: ROOF[x]['T']['10'] / ROOF[x]['tot'], 'odense', 'højeste')} andel af de {nw()} byer og langt over landsgennemsnittet på {rp('dk','10')}. Bolius beskriver to måder at montere på tegl: tagkroge, der går ind under stenene, eller ansatsskruer gennem tagbeklædningen. Tagkroge tager længere tid, fordi teglene skal tilpasses for at holde tæt.",
   ["dst_bygb50", "bolius_mont"]),
 "aalborg": ("Eternittage i Aalborg: det skal du vide før solceller",
   lambda: f"Aalborg Kommune har {rk(lambda x: ROOF[x]['T']['06'] / ROOF[x]['tot'], 'aalborg', 'største')} andel af fibercementtage blandt de {nw()} byer: {rp('aalborg','06')} af parcel- og rækkehusene har et tag, som Danmarks Statistik registrerer som fibercement inkl. asbest. Dansk Eternit havde fabrik i Aalborg, og ifølge Bolius indeholder bølge- og kunstskiferplader fra før 1984 næsten altid asbest. Det er tilladt at montere solceller på et asbesttag, hvis monteringen kun kræver, at der bores huller i pladerne.",
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
 "esbjerg": lambda: f"{pct(STOCK['esbjerg']['B']['1960-1979'],STOCK['esbjerg']['tot'])} af de {tal(STOCK['esbjerg']['tot'])} beboede parcel- og rækkehuse i Esbjerg Kommune er opført 1960-1979, {rk(lambda x: STOCK[x]['B']['1960-1979'] / STOCK[x]['tot'], 'esbjerg', 'største')} andel af de {nw()} byer. Bolius anbefaler at sikre, at taget har tilstrækkelig restlevetid, før solcellerne monteres. Siden gælder også Ribe, Bramming, Tjæreborg, Gørding og Tarp.",
 "odense": lambda: f"Odense skiller sig ud ved de mange rækkehuse: {tal(STOCK['odense']['raekke'])} af kommunens {tal(STOCK['odense']['tot'])} beboede parcel- og rækkehuse er række-, kæde- eller dobbelthuse ({pct(STOCK['odense']['raekke'],STOCK['odense']['tot'])}). Odense Kommune kræver tilladelse eller dispensation, hvis en lokalplan, byplanvedtægt eller servitut regulerer solceller eller tagets udseende. Siden gælder også Bellinge, Sankt Klemens, Fraugde og Over Holluf.",
 "aalborg": lambda: f"Aalborg Kommune har {tal(STOCK['aalborg']['tot'])} beboede parcel- og rækkehuse, næstflest af de {nw()} kommuner på dette site efter Aarhus. Siden gælder hele kommunen: Aalborg og Nørresundby ({tal(town('aalborg','Nørresundby'))} indbyggere) og forstæder som Svenstrup, Klarup, Vodskov og Gistrup samt Nibe.",
 "randers": lambda: f"I Randers Kommune er {pct(STOCK['randers']['ejer'],STOCK['randers']['tot'])} af de {tal(STOCK['randers']['tot'])} beboede parcel- og rækkehuse ejerboliger, og {pct(STOCK['randers']['B']['før 1960'],STOCK['randers']['tot'])} er bygget før 1960. Har huset bevaringsværdi 1-3 i et kulturmiljø, giver Randers Kommune som udgangspunkt ikke tilladelse til solceller. Siden gælder også Assentoft, Langå, Stevnstrup og Spentrup.",
 "horsens": lambda: f"Horsens har {rk(_EJ, 'horsens', 'højeste')} andel ejerboliger af de {nw()} kommuner: {pct(STOCK['horsens']['ejer'],STOCK['horsens']['tot'])} af de {tal(STOCK['horsens']['tot'])} beboede parcel- og rækkehuse bebos af ejeren. {pct(STOCK['horsens']['B']['2000+'],STOCK['horsens']['tot'])} er bygget i 2000 eller senere. Siden gælder også Brædstrup, Lund, Egebjerg, Østbirk og Gedved.",
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
 "vejle": ("Mange varmepumper i Vejle Kommune",
   lambda: f"{tal(HEAT['vejle']['VP'])} beboede parcel- og rækkehuse i Vejle Kommune varmes op med varmepumpe. Det er {hp('vejle','VP',1)} og {rk(lambda x: HEAT[x]['VP'] / hs(x), 'vejle', 'højeste')} andel af de {nw()} byer, mod {hp('dk','VP',1)} på landsplan. Samtidig har {tal(HEAT['vejle']['CN']+HEAT['vejle']['CO'])} huse stadig gas- eller oliefyr, og det er dem, kommunens fjernvarmeudrulning frem mod 2028 handler om."),
 "esbjerg": ("Fire ud af fem huse har fjernvarme i Esbjerg Kommune",
   lambda: f"{hp('esbjerg','FJ')} af de beboede parcel- og rækkehuse i Esbjerg Kommune har fjernvarme. Tilbage står ca. {tal(HEAT['esbjerg']['CO']+HEAT['esbjerg']['CN']+HEAT['esbjerg']['ELV'])} huse med olie, naturgas eller elvarme. Det er dem, en luft til vand-varmepumpe og Varmepumpepuljen er relevant for."),
 "odense": ("Luft til vand-varmepumpe i Odense: kun få huse uden fjernvarme",
   lambda: f"I Odense Kommune har {hp('odense','FJ',1)} af de beboede parcel- og rækkehuse fjernvarme, {rk(lambda x: HEAT[x]['FJ'] / hs(x), 'odense', 'højeste')} andel af de {nw()} byer. Kun {tal(HEAT['odense']['CO'])} huse har oliefyr, {tal(HEAT['odense']['CN'])} har naturgas, og {tal(HEAT['odense']['VP'])} har varmepumpe. En luft til vand-varmepumpe er derfor kun aktuel for få huse i Odense, primært uden for fjernvarmenettet."),
 "aalborg": ("Opvarmning i Aalborg Kommune i tal",
   lambda: f"{hp('aalborg','FJ')} af de beboede parcel- og rækkehuse i Aalborg Kommune har fjernvarme. {tal(HEAT['aalborg']['CO'])} huse har stadig oliefyr, flere end naturgas ({tal(HEAT['aalborg']['CN'])}). Kommunen udbygger ikke fjernvarmen yderligere lige nu og peger selv på varmepumper i områderne uden for nettet."),
 "randers": ("Randers har mange gas- og oliefyr tilbage",
   lambda: f"Kun {hp('randers','FJ')} af de beboede parcel- og rækkehuse i Randers Kommune har fjernvarme, {rk(lambda x: HEAT[x]['FJ'] / hs(x), 'randers', 'laveste', rev=True)} andel af de {nw()} byer. {tal(HEAT['randers']['CN'])} huse har naturgas, og {tal(HEAT['randers']['CO'])} har oliefyr ({hp('randers','CO',1)}, kun {above(lambda x: HEAT[x]['CO'] / hs(x), 'randers')} har en højere andel blandt byerne på sitet). Verdo udbygger lige nu i Assentoft, Harridslev, Stevnstrup og Spentrup. Uden for de byer er en varmepumpe alternativet."),
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
 "odense": [("Er der stadig oliefyr i Odense?", lambda: f"Kun få. Danmarks Statistik registrerer {tal(HEAT['odense']['CO'])} beboede parcel- og rækkehuse med oliefyr i Odense Kommune i 2026, ud af {tal(hs('odense'))}.", ["dst_bol102"]),
            ("Hvad koster en luft til vand-varmepumpe i Odense?", lambda: "SparEnergi angiver typisk 100.000-130.000 kr. inkl. montering, og Energisparer.dk ca. 90.000-150.000 kr. Vi har ikke fundet kilder med en særlig Odense-pris. Med så høj fjernvarmeandel er en luft til vand-varmepumpe mest relevant uden for fjernvarmenettet; tjek Fjernvarme Fyns kort, før du køber.", ["se_vp", "es_vp", "ode_fv"])],
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
        "horsens": (f"Horsens har {rk(_EJ, 'horsens', 'største')} ejerandel blandt de {nw()} kommuner på sitet: {pct(s['ejer'], t)} af de beboede huse er ejerboliger. Som lejer skal du altid have udlejers accept først.", []),
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
 "viborg": ("Mange oliefyr i Viborg: her passer en luft til vand-varmepumpe",
   lambda: f"{tal(HEAT['viborg']['CO'])} beboede parcel- og rækkehuse i Viborg Kommune ({hp('viborg','CO',1)}) varmes stadig op med oliefyr, {rk(lambda x: HEAT[x]['CO'] / hs(x), 'viborg', 'højeste')} andel af de {nw()} byer, og {tal(HEAT['viborg']['CN'])} ({hp('viborg','CN',1)}) har naturgas. {hp('viborg','FJ',1)} har fjernvarme, tæt på landsgennemsnittet på {hp('dk','FJ',1)}. Det er olie- og gasfyrene uden for fjernvarmeplanerne, som Varmepumpepuljen er rettet mod."),
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
 "viborg": [("Hvor mange huse i Viborg Kommune har olie- eller gasfyr?", lambda: f"Danmarks Statistik registrerer {tal(HEAT['viborg']['CO'])} beboede parcel- og rækkehuse med oliefyr og {tal(HEAT['viborg']['CN'])} med naturgas i 2026, ud af {tal(hs('viborg'))}. {tal(HEAT['viborg']['VP'])} har allerede varmepumpe.", ["dst_bol102"]),
  ("Hvad koster en luft til vand-varmepumpe i Viborg?", lambda: "SparEnergi angiver typisk 100.000-130.000 kr. inkl. montering, og Energisparer.dk ca. 90.000-150.000 kr. Vi har ikke fundet kilder, der viser en særlig Viborg-pris. Skifter du olie, gas, el eller biokedel ud uden for fjernvarme og planlagt fjernvarme, kan du søge 27.000 kr. fra Varmepumpepuljen, senest 30. november 2026.", ["se_vp", "es_vp", "vpp_faq"])],
})
FV_SOURCES.update({
 "aarhus": [("Aftalen om træpillevarme fra <strong>Studstrupværket</strong> udløber i 2030, og Kredsløb mister dermed 500 MW varmekapacitet. Kredsløbs eget halmfyrede kraftvarmeværk og affaldsforbrændingen skal fremover dække 45-50 % af varmen, resten skal være elbaseret.", ["aar_geo"]),
            ("Siden oktober 2025 har Kredsløb fået <strong>20 MW geotermisk varme</strong> fra Innargis anlæg i Skejby. I 2030 skal Innargi levere 111 MW fra tre anlæg: Skejby, Bautavej og Halmstadsgade.", ["aar_geo"]),
            ("Ved <strong>Egå Renseanlæg</strong> skal en spildevandsvarmepumpe på 8 MW anlægges fra november 2026 til februar 2028. En større spildevandsvarmepumpe på 23 MW ved Aarhus ReWater er udskudt til 2037.", ["aar_egaa", "aar_ff"])],
 "viborg": [("Viborg Varme har ca. 12.500 kunder. Varmen kommer i dag bl.a. fra en luft til vand-varmepumpe på 15 MW, en grundvands- og søvarmepumpe på 6 MW, en elkedel på 50 MW og gaskedler på 90 MW.", ["vib_df"]),
            ("Fra andet halvår 2027 begynder Viborg Varme at modtage <strong>overskudsvarme fra Apples datacenter</strong> og Energinets transformerstation i Tjele, først 12 MW og forventet 24,5 MW inden 2030. Varmen sendes 4,5 km til Taphede.", ["vib_df"])],
})
FV_SHARE.update({
 "aarhus": lambda: f"{hp('aarhus','FJ',1)} af de beboede parcel- og rækkehuse i Aarhus Kommune har fjernvarme. Kun {above(_hf('FJ'), 'aarhus')} har en højere andel blandt de {nw()} byer på dette site. Det efterlader ca. {tal(hs('aarhus')-HEAT['aarhus']['FJ'])} huse med anden opvarmning, heraf {tal(HEAT['aarhus']['VP'])} med varmepumpe.",
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
 "naestved": ("Næsten lige så mange gasfyr som fjernvarme i Næstved",
   lambda: f"{tal(HEAT['naestved']['CN'])} beboede parcel- og rækkehuse i Næstved Kommune ({hp('naestved','CN',1)}) varmes op med naturgas, {rk(_CN, 'naestved', 'højeste')} andel af de {nw()} byer og næsten lige så mange som dem med fjernvarme ({hp('naestved','FJ',1)}, {rk(_FJ, 'naestved', 'laveste', rev=True)} andel). {tal(HEAT['naestved']['ELV'])} huse har elvarme ({hp('naestved','ELV',1)} mod {hp('dk','ELV',1)} på landsplan). Det er netop olie-, gas- og elvarme uden for fjernvarmen, som Varmepumpepuljen er rettet mod."),
 "silkeborg": ("Varmepumpe i Silkeborg: naturgas fylder stadig meget",
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

# ---------- daglig by-rutine 28. okt. 2026: Holbæk og Slagelse (DK2, Region Sjælland) ----------
_VP = lambda x: HEAT[x]["VP"] / hs(x); _TEGL = lambda x: ROOF[x]["T"]["10"] / ROOF[x]["tot"]
SOL_ORDER.update({
 "holbaek": ["lokalt", "boliger", "tage", "produktion", "faq", "guides"],
 "slagelse": ["produktion", "tage", "lokalt", "boliger", "guides", "faq"],
})
VP_ORDER.update({
 "holbaek": ["opvarmning", "lokalt", "lokale-byer", "pris", "guides", "faq"],
 "slagelse": ["lokalt", "lokale-byer", "opvarmning", "pris", "faq", "guides"],
})
FV_ORDER.update({
 "holbaek": ["status", "andel", "priser", "billigst", "varmekilder", "faq"],
 "slagelse": ["status", "varmekilder", "andel", "priser", "billigst", "faq"],
})
SOL_PROD.update({
 "holbaek": ("Solproduktion ved Holbæk Fjord",
   lambda: f"For et sydvendt tag med 35° hældning i Holbæk beregner PVGIS ca. {tal(PV['holbaek']['syd'])} kWh pr. kWp om året, {rk(_PVY, 'holbaek', 'højeste')} af de {nw()} byer på dette site. Et 6 kWp-anlæg giver dermed ca. {tal(PV['holbaek']['syd']*6)} kWh. Vender taget mod øst eller vest, falder det til ca. {tal(PV['holbaek']['oest'])} og {tal(PV['holbaek']['vest'])} kWh pr. kWp."),
 "slagelse": ("Solceller i Slagelse: produktion på Vestsjælland",
   lambda: f"PVGIS beregner ca. <strong>{tal(PV['slagelse']['syd'])} kWh pr. kWp om året</strong> for et sydvendt tag med 35° hældning i Slagelse, {rk(_PVY, 'slagelse', 'højeste')} af de {nw()} byer på dette site. Et 6 kWp-anlæg giver ca. {tal(PV['slagelse']['syd']*6)} kWh om året, heraf ca. {tal(PV['slagelse']['months'][5]*6)} kWh i juni og kun ca. {tal(PV['slagelse']['months'][11]*6)} kWh i december."),
})
SOL_PROD_SRC_NEW.update({"holbaek": ["pv_holbaek", "pvo_holbaek", "pvv_holbaek"], "slagelse": ["pv_slagelse"]})
SOL_ROOF.update({
 "holbaek": ("Eternit, tegl og lokalplaner i Holbæk Kommune",
   lambda: f"Fibercement er det mest udbredte tag på parcel- og rækkehusene i Holbæk Kommune ({rp('holbaek','06')}), fulgt af tegl ({rp('holbaek','10')}) og cementsten ({rp('holbaek','08')}). Kræver lokalplanen matte tegl eller forbyder den reflekterende materialer, kan kommunen dispensere efter en konkret vurdering, evt. på betingelse af, at panelerne er antirefleksbehandlede.",
   ["dst_bygb50", "hol_disp"]),
 "slagelse": ("Tegl og eternit i Slagelse Kommune",
   lambda: f"{rp('slagelse','06')} af parcel- og rækkehusene i Slagelse Kommune har fibercement og {rp('slagelse','10')} tegl, {rk(_TEGL, 'slagelse', 'højeste')} tegl-andel af de {nw()} kommuner på sitet. Kræver lokalplanen røde teglsten, skal du søge dispensation, og kommunen vil have anlægget placeret, så tagmaterialet kan ses hele vejen rundt om det.",
   ["dst_bygb50", "slg_adm"]),
})
SOL_HOMES.update({
 "holbaek": lambda: f"Holbæk Kommune har {tal(STOCK['holbaek']['tot'])} beboede parcel- og rækkehuse, og {pct(STOCK['holbaek']['B']['før 1960'],STOCK['holbaek']['tot'])} er bygget før 1960, {rk(_OLD, 'holbaek', 'største')} andel af de {nw()} byer. Søger du dispensation fra en lokalplan til solceller, orienterer kommunen naboerne, før den træffer afgørelse. Siden gælder også Jyderup, Tølløse, Svinninge, Vipperød og Mørkøv.",
 "slagelse": lambda: f"{pct(STOCK['slagelse']['B']['før 1960'],STOCK['slagelse']['tot'])} af de {tal(STOCK['slagelse']['tot'])} beboede parcel- og rækkehuse i Slagelse Kommune er bygget før 1960, {rk(_OLD, 'slagelse', 'største')} andel af de {nw()} byer. I de bevarende lokalplaner i Slagelse, Korsør og Skælskør vurderer kommunen hver solcellesag konkret. Siden gælder også Korsør, Skælskør, Forlev, Svenstrup og Dalmose.",
})
SOL_HOMES_SRC_NEW.update({"holbaek": ["hol_disp"], "slagelse": ["slg_adm"]})
SOL_HOMES_H.update({"holbaek": "Huse og lokalplaner i Holbæk Kommune", "slagelse": "Gamle bykerner i Slagelse, Korsør og Skælskør"})
SOL_XFAQ.update({
 "holbaek": [("Må solcellerne stå på stativ på mit tag i Holbæk?", lambda: f"Kun med byggetilladelse. Holbæk Kommune kræver altid tilladelse til anlæg på stativ på taget. Følger panelerne tagets hældning, giver et sydvendt tag ca. {tal(PV['holbaek']['syd'])} kWh pr. kWp om året og et østvendt ca. {tal(PV['holbaek']['oest'])} kWh (PVGIS, 35°).", ["hol_sol", "pv_holbaek", "pvo_holbaek"])],
 "slagelse": [("Hvor meget giver solceller i Slagelse om vinteren?", lambda: f"PVGIS beregner ca. {tal(PV['slagelse']['months'][11]*6)} kWh i december og {tal(PV['slagelse']['months'][0]*6)} kWh i januar fra et 6 kWp-anlæg mod syd, mod ca. {tal(PV['slagelse']['months'][5]*6)} kWh i juni. Over hele året giver det ca. {tal(PV['slagelse']['syd']*6)} kWh.", ["pv_slagelse"]),
            ("Hvad koster solceller i Slagelse?", lambda: "Energisparer.dk ser i 2026 ca. 12.500-16.000 kr. pr. kWp for et færdigmonteret anlæg, så et typisk 6 kWp-anlæg ligger omkring 75.000-96.000 kr. inkl. montering. Vi har ikke fundet en særlig Slagelse-pris. Kræver lokalplanen røde teglsten, kan dispensation og ekstra montage påvirke prisen.", ["es_sol", "slg_adm"])],
})
VP_HEAT.update({
 "holbaek": ("Mange gasfyr og færrest med fjernvarme på sitet i Holbæk",
   lambda: f"{tal(HEAT['holbaek']['CN'])} beboede parcel- og rækkehuse i Holbæk Kommune ({hp('holbaek','CN',1)}) har naturgas, {rk(_CN, 'holbaek', 'højeste')} andel af de {nw()} byer, og kun {hp('holbaek','FJ',1)} har fjernvarme. Samtidig har {tal(HEAT['holbaek']['VP'])} huse ({hp('holbaek','VP',1)}) allerede varmepumpe, {rk(_VP, 'holbaek', 'højeste')} andel på sitet, mod {hp('dk','VP',1)} på landsplan."),
 "slagelse": ("Gas, olie og elvarme i Slagelse Kommune",
   lambda: f"{hp('slagelse','FJ',1)} af de {tal(hs('slagelse'))} beboede parcel- og rækkehuse i Slagelse Kommune har fjernvarme, mens {tal(HEAT['slagelse']['CN'])} ({hp('slagelse','CN',1)}) har naturgas, {tal(HEAT['slagelse']['CO'])} oliefyr og {tal(HEAT['slagelse']['ELV'])} elvarme. {tal(HEAT['slagelse']['VP'])} huse ({hp('slagelse','VP',1)}) har allerede varmepumpe, {rk(_VP, 'slagelse', 'højeste')} andel af de {nw()} byer."),
})
VP_HEAT_SRC_NEW.update({"holbaek": ["hol_fv"], "slagelse": ["slg_fv"]})
VP_TOWNS.update({
 "holbaek": [("Holbæk", "Etape 1 godkendt, men 12 % tilmeldt mod krav på 70 %. Afgøres senest 1/5 2027", ["fors_hol", "hol_ext"]),
             ("Jyderup", "Fors. Varmepumpeanlæg godkendt i 2023, tilslutningspligt", ["hol_fv", "ft_pris"]),
             ("Tølløse", "Ikke med i kommunens fjernvarmeplaner", ["hol_fv"]),
             ("Svinninge", "Ikke med i kommunens fjernvarmeplaner", ["hol_fv"]),
             ("Vipperød", "Ikke med i kommunens fjernvarmeplaner", ["hol_fv"]),
             ("Mørkøv", "Mørkøv Varmeværk. Ledningsnettet udvides", ["hol_fv", "ft_pris"]),
             ("Store Merløse", "Fors. Fjernvarme i dele af byen", ["hol_fv", "ft_pris"])],
 "slagelse": [("Slagelse", "SV realiseres (61 %), Øst planlagt til 2027, nordøst tidligst 2029/30", ["slg_fv"]),
              ("Korsør", "Fjernvarme. Halsskov udrullet, Svenstrup afgøres 2029/30", ["slg_fv"]),
              ("Skælskør", "Projektet annulleret i maj 2025", ["slg_fv"]),
              ("Forlev", "Projektet (Vemmelev-Forlev) annulleret i august 2025", ["slg_fv"]),
              ("Sørbymagle", "Ingen udsigt til fællesvarme", ["slg_fv"]),
              ("Slots Bjergby", "Planlagt fra Slagelse, men afventer pga. høj pris", ["slg_fv"]),
              ("Dalmose", "Eget værk: Hashøj Kraftvarmeforsyning", ["ft_pris", "slg_fv"])],
})
VP_TOWNS_NOTE.update({
 "holbaek": "Bor du i Ugerløse, Gislinge, Tuse, Regstrup eller en af landsbyerne, så slå adressen op på Plandata.dk, før du søger tilskud.",
 "slagelse": "Bor du i Vemmelev, Boeslunde, Kirke Stillinge eller en af landsbyerne, så tjek adressen på Slagelse Kommunes fjernvarmekort, før du søger tilskud.",
})
VP_XFAQ.update({
 "holbaek": [("Hvor mange huse i Holbæk Kommune har gasfyr?", lambda: f"Danmarks Statistik registrerer {tal(HEAT['holbaek']['CN'])} beboede parcel- og rækkehuse med naturgas i 2026, ud af {tal(hs('holbaek'))}. {tal(HEAT['holbaek']['CO'])} har oliefyr og {tal(HEAT['holbaek']['ELV'])} elvarme, mens {tal(HEAT['holbaek']['FJ'])} har fjernvarme.", ["dst_bol102"])],
 "slagelse": [("Hvor mange i Slagelse Kommune har allerede varmepumpe?", lambda: f"{tal(HEAT['slagelse']['VP'])} beboede parcel- og rækkehuse ({hp('slagelse','VP',1)}) ifølge Danmarks Statistik, 2026, mod {hp('dk','VP',1)} på landsplan. {tal(HEAT['slagelse']['CN'] + HEAT['slagelse']['CO'])} har stadig gas- eller oliefyr.", ["dst_bol102"])],
})
FV_SOURCES.update({
 "holbaek": [("Holbæk Kommune skriver, at fjernvarmen i kommunen primært kommer fra <strong>eldrevne varmepumper</strong>, og at størstedelen af strømmen til dem med tiden skal komme fra solceller og vindmøller.", ["hol_fv"]),
             ("Fjernvarmen til Holbæk by skal komme fra et stort varmepumpeanlæg ved Omfartsvejen, kaldet <strong>Energibyen</strong>. I Jyderup godkendte kommunen i november 2023 et anlæg med eldreven varmepumpe og solpaneler, der afløser naturgas.", ["hol_fv"])],
 "slagelse": [("Envafors skriver, at fjernvarmen i Slagelse og Korsør primært produceres på <strong>halm og flis</strong> samt solvarme, og at flere store varmepumper leverer en voksende del. Omkring <strong>95 %</strong> af varmen er vedvarende energi.", ["env_ve"]),
              ("Slagelse Kraftvarmeværk producerer 40-50 mio. kWh el om året, og en ny stor akkumuleringstank gør det muligt at lave varme med el, når elprisen er lav.", ["env_ve"])],
})
FV_SHARE.update({
 "holbaek": lambda: f"Kun {hp('holbaek','FJ',1)} af de beboede parcel- og rækkehuse i Holbæk Kommune har fjernvarme, {rk(_FJ, 'holbaek', 'laveste', rev=True)} andel af de {nw()} byer på dette site, mod {hp('dk','FJ',1)} i hele landet. {tal(HEAT['holbaek']['CN']+HEAT['holbaek']['CO']+HEAT['holbaek']['ELV'])} huse har gas, olie eller elvarme.",
 "slagelse": lambda: f"{hp('slagelse','FJ',1)} af de beboede parcel- og rækkehuse i Slagelse Kommune har fjernvarme, mod {hp('dk','FJ',1)} i hele landet. {tal(HEAT['slagelse']['CN'])} huse har naturgas, {tal(HEAT['slagelse']['CO'])} oliefyr og {tal(HEAT['slagelse']['ELV'])} elvarme.",
})
FV_SOURCES_H.update({"holbaek": "Varmepumper i Holbæk, Jyderup og Energibyen", "slagelse": "Halm, flis og varmepumper i Slagelse og Korsør"})
_reg_age_old3 = reg_age_note
def reg_age_note(c, kommune):
    s = STOCK[c]; B = s["B"]; t = s["tot"]
    if c == "holbaek":
        return (f"{tal(B['før 1960'])} af de beboede huse i Holbæk Kommune ({pct(B['før 1960'], t)}) er bygget før 1960. Er huset fredet eller bevaringsværdigt, kan det kræve dispensation, også selv om panelerne følger taget.", ["hol_sol"])
    if c == "slagelse":
        return (f"{tal(B['før 1960'])} af kommunens beboede huse ({pct(B['før 1960'], t)}) er bygget før 1960. Ligger dit hus i en bevarende lokalplan, afhænger svaret af bygningens SAVE-værdi.", ["slg_adm"])
    return _reg_age_old3(c, kommune)

# ---------- daglig by-rutine 29. okt. 2026: Roskilde (DK2, Region Sjælland) og Sønderborg (DK1, Region Syddanmark) ----------
_FIB = lambda x: ROOF[x]["T"]["06"] / ROOF[x]["tot"]
SOL_ORDER.update({
 "roskilde": ["boliger", "produktion", "lokalt", "tage", "faq", "guides"],
 "soenderborg": ["tage", "lokalt", "produktion", "boliger", "faq", "guides"],
})
VP_ORDER.update({
 "roskilde": ["lokale-byer", "lokalt", "opvarmning", "pris", "guides", "faq"],
 "soenderborg": ["opvarmning", "lokale-byer", "lokalt", "pris", "faq", "guides"],
})
FV_ORDER.update({
 "roskilde": ["status", "priser", "andel", "varmekilder", "billigst", "faq"],
 "soenderborg": ["andel", "status", "varmekilder", "priser", "billigst", "faq"],
})
SOL_PROD.update({
 "roskilde": ("Solproduktion ved Roskilde Fjord",
   lambda: f"PVGIS beregner ca. {tal(PV['roskilde']['syd'])} kWh pr. kWp om året for et sydvendt tag med 35° hældning i Roskilde, {rk(_PVY, 'roskilde', 'højeste')} af de {nw()} byer på dette site. Ved den optimale hældning på {PV['roskilde']['opt_angle']}° bliver det ca. {tal(PV['roskilde']['opt'])} kWh. Et 6 kWp-anlæg mod syd giver ca. {tal(PV['roskilde']['syd']*6)} kWh om året."),
 "soenderborg": ("Sol over Als: produktion i Sønderborg",
   lambda: f"For et sydvendt tag med 35° hældning i Sønderborg beregner PVGIS ca. <strong>{tal(PV['soenderborg']['syd'])} kWh pr. kWp om året</strong>, {rk(_PVY, 'soenderborg', 'højeste')} af de {nw()} byer på dette site. Fra april til august giver et 6 kWp-anlæg ca. {tal(sum(PV['soenderborg']['months'][3:8])*6)} kWh, mens november, december og januar tilsammen kun giver ca. {tal((PV['soenderborg']['months'][10]+PV['soenderborg']['months'][11]+PV['soenderborg']['months'][0])*6)} kWh."),
})
SOL_PROD_SRC_NEW.update({"roskilde": ["pv_roskilde", "pvgis"], "soenderborg": ["pv_soenderborg"]})
SOL_ROOF.update({
 "roskilde": ("Tegl, eternit og cementsten i Roskilde Kommune",
   lambda: f"Tagene på parcel- og rækkehusene i Roskilde Kommune er ret ligeligt fordelt: {rp('roskilde','10')} har tegl, {rp('roskilde','06')} fibercement og {rp('roskilde','08')} cementsten. {rp('roskilde','04')} har tagpap med hældning og {rp('roskilde','02')} fladt tag. Sidder panelerne på det eksisterende tag, kræver det som udgangspunkt ikke tilladelse, hvis højde- og afstandsreglerne er overholdt.",
   ["dst_bygb50", "ros_byg"]),
 "soenderborg": ("Eternit og tegl i Sønderborg Kommune",
   lambda: f"{rp('soenderborg','06')} af parcel- og rækkehusene i Sønderborg Kommune har fibercement, og {rp('soenderborg','10')} har tegl. {rp('soenderborg','08')} har cementsten. Er taget af ældre fibercement, så få det vurderet, før panelerne skrues fast: ifølge Bolius kan det indeholde asbest.",
   ["dst_bygb50", "bolius_asb"]),
})
SOL_HOMES.update({
 "roskilde": lambda: f"{pct(STOCK['roskilde']['ejer'],STOCK['roskilde']['tot'])} af de {tal(STOCK['roskilde']['tot'])} beboede parcel- og rækkehuse i Roskilde Kommune er ejerboliger, {rk(_EJ, 'roskilde', 'højeste')} andel af de {nw()} kommuner på sitet, og {pct(STOCK['roskilde']['B']['1960-1979'],STOCK['roskilde']['tot'])} er bygget i 1960-1979. Siden gælder også Jyllinge, Viby, Svogerslev, Vindinge og Gundsømagle.",
 "soenderborg": lambda: f"{pct(STOCK['soenderborg']['B']['før 1960'],STOCK['soenderborg']['tot'])} af de {tal(STOCK['soenderborg']['tot'])} beboede parcel- og rækkehuse i Sønderborg Kommune er bygget før 1960, {rk(_OLD, 'soenderborg', 'største')} andel af de {nw()} byer. Er huset registreret som bevaringsværdigt, skal du kontakte kommunen, før du sætter solceller op. Siden gælder også Nordborg, Gråsten, Broager, Augustenborg og Høruphav.",
})
SOL_HOMES_SRC_NEW.update({"roskilde": [], "soenderborg": ["sk_sol"]})
SOL_HOMES_H.update({"roskilde": "Ejerboliger fra Roskilde til Jyllinge", "soenderborg": "Ældre huse fra Gråsten til Nordborg"})
SOL_XFAQ.update({
 "roskilde": [("Hvor meget giver solceller i Roskilde om sommeren?", lambda: f"PVGIS beregner ca. {tal(PV['roskilde']['months'][5]*6)} kWh i juni og {tal(PV['roskilde']['months'][6]*6)} kWh i juli fra et 6 kWp-anlæg mod syd. Over hele året giver det ca. {tal(PV['roskilde']['syd']*6)} kWh.", ["pv_roskilde"])],
 "soenderborg": [("Hvor meget mister jeg med et østvendt tag i Sønderborg?", lambda: f"PVGIS beregner ca. {tal(PV['soenderborg']['oest'])} kWh pr. kWp om året mod øst og {tal(PV['soenderborg']['vest'])} kWh mod vest, mod {tal(PV['soenderborg']['syd'])} kWh mod syd ved 35° hældning. Et østvendt 6 kWp-anlæg giver dermed ca. {tal((PV['soenderborg']['syd']-PV['soenderborg']['oest'])*6)} kWh mindre om året end et sydvendt.", ["pvo_soenderborg", "pvv_soenderborg", "pv_soenderborg"])],
})
VP_HEAT.update({
 "roskilde": ("Naturgas i mere end hvert fjerde hus i Roskilde Kommune",
   lambda: f"{tal(HEAT['roskilde']['CN'])} beboede parcel- og rækkehuse i Roskilde Kommune ({hp('roskilde','CN',1)}) har naturgas, {rk(_CN, 'roskilde', 'højeste')} andel af de {nw()} byer, mens {hp('roskilde','FJ',1)} har fjernvarme. {tal(HEAT['roskilde']['VP'])} huse ({hp('roskilde','VP',1)}) har allerede varmepumpe, mod {hp('dk','VP',1)} på landsplan."),
 "soenderborg": ("Tre ud af fem huse har fjernvarme i Sønderborg Kommune",
   lambda: f"{hp('soenderborg','FJ',1)} af de {tal(hs('soenderborg'))} beboede parcel- og rækkehuse i Sønderborg Kommune har fjernvarme, mod {hp('dk','FJ',1)} på landsplan. {tal(HEAT['soenderborg']['CN'])} har naturgas, {tal(HEAT['soenderborg']['CO'])} oliefyr og {tal(HEAT['soenderborg']['CA'])} anden centralvarme end olie og gas. Kun {hp('soenderborg','VP',1)} har varmepumpe, {rk(_VP, 'soenderborg', 'laveste', rev=True)} andel af de {nw()} byer."),
})
VP_HEAT_SRC_NEW.update({"roskilde": ["ros_varme"], "soenderborg": ["pz_varme"]})
VP_TOWNS.update({
 "roskilde": [("Roskilde", "Fjernvarme fra Fors. Himmelev afsluttes i 2026", ["ros_varme", "fors_aar"]),
              ("Jyllinge", "Fjernvarmeprojektet bortfaldet i 2026. Naturgasområde igen", ["ros_jyl", "ros_varme"]),
              ("Viby", "Projektet (Viby-Dåstrup) bortfaldet i 2026", ["ros_varme"]),
              ("Svogerslev", "Eget værk: Svogerslev Fjernvarmecentral", ["ros_varme", "ft_pris"]),
              ("Vindinge", "Fjernvarme under udrulning. Arbejdet genoptages med ny entreprenør", ["ros_varme"]),
              ("Gadstrup", "Projektet (Gadstrup-Snoldelev) bortfaldet i 2026", ["ros_varme"]),
              ("Veddelev", "Fjernvarme under etablering. Første tilkoblinger i 2026/27", ["fors_ved"])],
 "soenderborg": [("Sønderborg", "Fjernvarme fra Sønderborg Varme", ["pz_varme"]),
                 ("Nordborg", "Fjernvarme fra SONFOR (halm)", ["pz_varme", "sonfor_halm"]),
                 ("Gråsten", "Sønderborg Varme. Ny varmepumpe på 13 MW ventes i 2027", ["pz_varme", "df_sv29"]),
                 ("Augustenborg", "Fjernvarme fra Sønderborg Varme", ["pz_varme"]),
                 ("Guderup", "Fjernvarme fra SONFOR via ledning fra Nordborg", ["pz_varme", "sonfor_na"]),
                 ("Vester Sottrup", "Fjernvarme under udrulning. Sidste etape i 2026", ["sv_nyb"]),
                 ("Blans", "Fjernvarme på vej. Varme ventes i 2028", ["df_blans", "pz_varme"])],
})
VP_TOWNS_NOTE.update({
 "roskilde": "Bor du i Store Valby, Ågerup, Gundsømagle eller en af landsbyerne, så slå adressen op på kommunens varmeplankort eller Plandata.dk, før du søger tilskud.",
 "soenderborg": "Bor du i Oksbøl, Broballe, Mjels, Elstrup eller en anden landsby, så tjek din by på ProjectZeros kort, før du søger tilskud.",
})
VP_XFAQ.update({
 "roskilde": [("Hvor mange huse i Roskilde Kommune har allerede varmepumpe?", lambda: f"{tal(HEAT['roskilde']['VP'])} beboede parcel- og rækkehuse ({hp('roskilde','VP',1)}) ifølge Danmarks Statistik, 2026, mod {hp('dk','VP',1)} på landsplan. {tal(HEAT['roskilde']['CN'])} har stadig naturgas og {tal(HEAT['roskilde']['CO'])} oliefyr.", ["dst_bol102"])],
 "soenderborg": [("Hvor mange huse i Sønderborg Kommune har stadig olie- eller gasfyr?", lambda: f"Danmarks Statistik registrerer {tal(HEAT['soenderborg']['CO'])} beboede parcel- og rækkehuse med oliefyr og {tal(HEAT['soenderborg']['CN'])} med naturgas i 2026, ud af {tal(hs('soenderborg'))}. {tal(HEAT['soenderborg']['ELV'])} har elvarme og {tal(HEAT['soenderborg']['VP'])} varmepumpe.", ["dst_bol102"])],
})
FV_SOURCES.update({
 "roskilde": [("Fors Varme Roskilde får varmen fra <strong>VEKS</strong>, primært som overskudsvarme fra kraftvarmeværket i Avedøre og fra affaldsforbrændingen hos <strong>ARGO</strong> i Roskilde. I perioder med spidsbelastning suppleres med egen produktion.", ["fors_aar"]),
              ("Fors producerer selv fjernvarme på et <strong>varmepumpeanlæg</strong>, der udnytter overskudsvarme fra spildevand på Bjergmarken Renseanlæg. Selskabet har ca. 10.328 kunder i Roskilde by og omegn.", ["fors_aar"])],
 "soenderborg": [("Sønderborg Varme bygger et system med tre ben: <strong>elbaseret varme, biomasse og affaldsenergi</strong>. En elkedel på 25 MW ved kraftvarmeværket i Sønderborg ventes i drift i 2026, og værket i Gråsten får en luft-vand-varmepumpe på 13 MW i 2027.", ["df_sv29"]),
                 ("På Nordals fyrer SONFORs anlæg i Nordborg ifølge selskabet <strong>udelukkende med halm</strong>, og nettet løber fra Nordborg til Guderup.", ["sonfor_halm", "sonfor_na"])],
})
FV_SHARE.update({
 "roskilde": lambda: f"{hp('roskilde','FJ',1)} af de beboede parcel- og rækkehuse i Roskilde Kommune har fjernvarme, mod {hp('dk','FJ',1)} i hele landet. {tal(HEAT['roskilde']['CN'])} huse har naturgas, {tal(HEAT['roskilde']['ELV'])} elvarme og {tal(HEAT['roskilde']['CO'])} oliefyr.",
 "soenderborg": lambda: f"{hp('soenderborg','FJ',1)} af de beboede parcel- og rækkehuse i Sønderborg Kommune har fjernvarme, {rk(_FJ, 'soenderborg', 'højeste')} andel af de {nw()} byer på dette site, mod {hp('dk','FJ',1)} i hele landet. {tal(HEAT['soenderborg']['CN']+HEAT['soenderborg']['CO']+HEAT['soenderborg']['ELV'])} huse har gas, olie eller elvarme.",
})
FV_SOURCES_H.update({"roskilde": "Avedøre, ARGO og spildevand i Roskilde", "soenderborg": "Elkedel, varmepumpe og halm i Sønderborg og på Nordals"})
_reg_age_old4 = reg_age_note
def reg_age_note(c, kommune):
    s = STOCK[c]; B = s["B"]; t = s["tot"]
    if c == "roskilde":
        return (f"{tal(B['1960-1979'])} af de beboede huse i Roskilde Kommune ({pct(B['1960-1979'], t)}) er bygget i 1960-1979. Uanset alder skal du tjekke lokalplan og tinglyste deklarationer, før du bestiller.", ["ros_byg"])
    if c == "soenderborg":
        return (f"{tal(B['før 1960'])} af kommunens beboede huse ({pct(B['før 1960'], t)}) er bygget før 1960. Er bygningen fredet, kræver solceller tilladelse fra Kulturstyrelsen, og normalt kan det ikke lade sig gøre.", ["sk_sol"])
    return _reg_age_old4(c, kommune)


# ---------- daglig by-rutine 30. okt. 2026: Køge (DK2, Region Sjælland) og Svendborg (DK1, Region Syddanmark) ----------
SOL_ORDER.update({
 "koege": ["lokalt", "boliger", "tage", "produktion", "faq", "guides"],
 "svendborg": ["produktion", "boliger", "lokalt", "tage", "guides", "faq"],
})
VP_ORDER.update({
 "koege": ["opvarmning", "lokalt", "lokale-byer", "pris", "guides", "faq"],
 "svendborg": ["lokale-byer", "opvarmning", "pris", "lokalt", "faq", "guides"],
})
FV_ORDER.update({
 "koege": ["andel", "status", "priser", "varmekilder", "billigst", "faq"],
 "svendborg": ["status", "varmekilder", "andel", "priser", "billigst", "faq"],
})
SOL_PROD.update({
 "koege": ("Solproduktion ved Køge Bugt",
   lambda: f"PVGIS beregner ca. {tal(PV['koege']['syd'])} kWh pr. kWp om året for et sydvendt tag med 35° hældning i Køge. Et vestvendt tag giver ca. {tal(PV['koege']['vest'])} kWh og et østvendt ca. {tal(PV['koege']['oest'])} kWh pr. kWp. Med et 6 kWp-anlæg mod syd bliver det ca. {tal(PV['koege']['syd']*6)} kWh om året, heraf ca. {tal(PV['koege']['months'][4]*6)} kWh i maj alene."),
 "svendborg": ("Sydfyn har sol: produktion i Svendborg",
   lambda: f"For et sydvendt tag med 35° hældning i Svendborg beregner PVGIS ca. <strong>{tal(PV['svendborg']['syd'])} kWh pr. kWp om året</strong>, {rk(_PVY, 'svendborg', 'højeste')} af de {nw()} byer på dette site. Ved den optimale hældning på {PV['svendborg']['opt_angle']}° bliver det ca. {tal(PV['svendborg']['opt'])} kWh. Maj er den bedste måned med ca. {tal(PV['svendborg']['months'][4]*6)} kWh fra et 6 kWp-anlæg, december den svageste med ca. {tal(PV['svendborg']['months'][11]*6)} kWh."),
})
SOL_PROD_SRC_NEW.update({"koege": ["pv_koege", "pvo_koege", "pvv_koege"], "svendborg": ["pv_svendborg", "pvgis"]})
SOL_ROOF.update({
 "koege": ("Fibercement og tegl i Køge Kommune",
   lambda: f"{rp('koege','06')} af parcel- og rækkehusene i Køge Kommune har tag af fibercement, og {rp('koege','10')} har tegl. {rp('koege','08')} har cementsten og {rp('koege','02')} fladt tag. Sidder panelerne på taget af et enfamiliehus, kræver det som udgangspunkt ikke kommunens tilladelse, men lokalplanen kan stille krav.",
   ["dst_bygb50", "koe_energi"]),
 "svendborg": ("Stråtag og eternit i Svendborg Kommune",
   lambda: f"{rp('svendborg','06')} af parcel- og rækkehusene i Svendborg Kommune har fibercement og {rp('svendborg','10')} tegl. {tal(ROOF['svendborg']['T']['14'])} huse har <strong>stråtag</strong> ({rp('svendborg','14',1)}), mod {rp('dk','14',1)} i hele landet. Er taget af ældre fibercement, så få det vurderet, før panelerne skrues fast: ifølge Bolius kan det indeholde asbest.",
   ["dst_bygb50", "bolius_asb"]),
})
SOL_HOMES.update({
 "koege": lambda: f"Køge Kommune har {tal(STOCK['koege']['tot'])} beboede parcel- og rækkehuse, og {pct(STOCK['koege']['ejer'],STOCK['koege']['tot'])} er ejerboliger. {pct(STOCK['koege']['B']['1960-1979'],STOCK['koege']['tot'])} er bygget i 1960-1979. Siden gælder også Borup ({tal(town('koege','Borup'))} indbyggere), Bjæverskov, Ejby, Lellinge og Lille Skensved.",
 "svendborg": lambda: f"{pct(STOCK['svendborg']['B']['før 1960'],STOCK['svendborg']['tot'])} af de {tal(STOCK['svendborg']['tot'])} beboede parcel- og rækkehuse i Svendborg Kommune er bygget før 1960, {rk(_OLD, 'svendborg', 'største')} andel af de {nw()} byer. Tjek lokalplan, byplanvedtægt og deklarationer, før du bestiller. Siden gælder også Thurø, Tåsinge (Vindeby og Troense), Stenstrup, Skårup og Gudme.",
})
SOL_HOMES_SRC_NEW.update({"koege": [], "svendborg": ["svb_sol"]})
SOL_HOMES_H.update({"koege": "Huse fra Køge til Borup og Bjæverskov", "svendborg": "Ældre huse på Sydfyn og Tåsinge"})
SOL_XFAQ.update({
 "koege": [("Hvor meget mindre giver et østvendt tag i Køge?", lambda: f"PVGIS beregner ca. {tal(PV['koege']['oest'])} kWh pr. kWp om året mod øst og {tal(PV['koege']['vest'])} kWh mod vest, mod {tal(PV['koege']['syd'])} kWh mod syd ved 35° hældning. Et østvendt 6 kWp-anlæg giver dermed ca. {tal((PV['koege']['syd']-PV['koege']['oest'])*6)} kWh mindre om året.", ["pvo_koege", "pvv_koege", "pv_koege"])],
 "svendborg": [("Hvor meget giver solceller i Svendborg om sommeren?", lambda: f"PVGIS beregner ca. {tal(PV['svendborg']['months'][5]*6)} kWh i juni og {tal(PV['svendborg']['months'][6]*6)} kWh i juli fra et 6 kWp-anlæg mod syd. Over hele året giver det ca. {tal(PV['svendborg']['syd']*6)} kWh.", ["pv_svendborg"])],
})
VP_HEAT.update({
 "koege": ("Halvdelen af husene i Køge Kommune har naturgas",
   lambda: f"{tal(HEAT['koege']['CN'])} beboede parcel- og rækkehuse i Køge Kommune ({hp('koege','CN',1)}) har naturgas, {rk(_CN, 'koege', 'højeste')} andel af de {nw()} byer, mod {hp('dk','CN',1)} på landsplan. Kun {hp('koege','FJ',1)} har fjernvarme. {tal(HEAT['koege']['VP'])} huse ({hp('koege','VP',1)}) har allerede varmepumpe, og {tal(HEAT['koege']['CO'])} har stadig oliefyr."),
 "svendborg": ("Gas, varmepumper og fjernvarme i Svendborg Kommune",
   lambda: f"{hp('svendborg','CN',1)} af de {tal(hs('svendborg'))} beboede parcel- og rækkehuse i Svendborg Kommune har naturgas, og {hp('svendborg','FJ',1)} har fjernvarme. {tal(HEAT['svendborg']['VP'])} huse ({hp('svendborg','VP',1)}) har allerede varmepumpe, {rk(_VP, 'svendborg', 'højeste')} andel af de {nw()} byer, mod {hp('dk','VP',1)} på landsplan."),
})
VP_HEAT_SRC_NEW.update({"koege": ["koe_energi"], "svendborg": ["svb_vp2030"]})
VP_TOWNS.update({
 "koege": [("Køge (Nylandsvej, K02)", "Fjernvarme under udbygning. Gravning ved Ølsemaglevej Øst og Strandlodsvej", ["kfv_grav"]),
           ("Køge (K05, K06, K08)", "Projektforslaget søges annulleret. Nyt forslag ventes i 2027", ["kfv_pm"]),
           ("Borup", "Eget værk: Borup Varmeværk", ["ft_pris", "koe_borup"]),
           ("Bjæverskov", "Nyt værk indviet 19/9 2026. Overskudsvarme fra Energinet", ["df_bjae"]),
           ("Ejby", "Tjek adressen i kommunens varmeplan", ["koe_energi"]),
           ("Lille Skensved", "Tjek adressen i kommunens varmeplan", ["koe_energi"])],
 "svendborg": [("Svendborg", "Svendborg Fjernvarme. Nye områder efter ny varmepumpe (2028)", ["sfv_ud", "df_svb"]),
               ("Stenstrup", "Eget værk: Stenstrup Fjernvarme", ["svb_fv", "ft_pris"]),
               ("Skårup", "Eget værk: Skårup Fjernvarme", ["svb_fv", "ft_pris"]),
               ("Ollerup", "Ikke længere fjernvarmeområde. Tilskud til varmepumpe muligt", ["svb_oll"]),
               ("Vester Skerninge", "Ikke længere fjernvarmeområde. Tilskud til varmepumpe muligt", ["svb_oll"]),
               ("Lundeborg", "Fjernvarmeprojektet annulleret 2025. Individuel varme", ["svb_lund"])],
})
VP_TOWNS_NOTE.update({
 "koege": "Bor du i Ejby, Lille Skensved, Vemmedrup eller en af landsbyerne, så slå adressen op i kommunens varmeplan, før du søger tilskud. Har du tilslutningspligt til naturgas, skal du søge dispensation hos Plan.",
 "svendborg": "Bor du på Thurø, Tåsinge eller i en landsby, så slå adressen op på kommunens varmeplanskort, før du søger tilskud. Kortet viser vedtaget fjernvarme, fjernvarmepotentiale og områder til individuel opvarmning.",
})
VP_XFAQ.update({
 "koege": [("Hvor mange huse i Køge Kommune har stadig gas- eller oliefyr?", lambda: f"Danmarks Statistik registrerer {tal(HEAT['koege']['CN'])} beboede parcel- og rækkehuse med naturgas og {tal(HEAT['koege']['CO'])} med oliefyr i 2026, ud af {tal(hs('koege'))}. {tal(HEAT['koege']['ELV'])} har elvarme og {tal(HEAT['koege']['VP'])} varmepumpe.", ["dst_bol102"])],
 "svendborg": [("Hvor mange huse i Svendborg Kommune har allerede varmepumpe?", lambda: f"{tal(HEAT['svendborg']['VP'])} beboede parcel- og rækkehuse ({hp('svendborg','VP',1)}) ifølge Danmarks Statistik, 2026, mod {hp('dk','VP',1)} på landsplan. {tal(HEAT['svendborg']['CN'])} har stadig naturgas og {tal(HEAT['svendborg']['CO'])} oliefyr.", ["dst_bol102"])],
})
FV_SOURCES.update({
 "koege": [("Det nye værk i <strong>Bjæverskov</strong> henter ca. 40 °C varmt vand fra kølingen af Energinets transformerstation vest for byen, og to varmepumper løfter det til ca. 70 °C. En gaskedel på 6 MW og et lager på 4.500 m³ er backup.", ["df_bjae"]),
           ("Til <strong>Borup Varmeværk</strong> er en ny elkedel ved værket på Bækgårdsvej VVM-screenet. Køge Kommune vurderede, at projektet ikke vil påvirke miljøet væsentligt.", ["koe_borup"])],
 "svendborg": [("<strong>Svendborg Fjernvarme</strong> har i dag en 16 MW ammoniak-varmepumpe, en 25 MW elkedel, tre gasmotorer og gaskedler. Cirka en tredjedel af varmen kommer fra gas, efter at affaldsforbrændingen lukkede i 2023.", ["df_svb"]),
               ("Med en ny 25 MW varmepumpe og en ny 25 MW elkedel skal gasandelen ned fra ca. 35 til ca. 5 %, og 80-90 % af varmen skal komme fra el. Anlæggene ventes i fuld drift fra midten af 2028.", ["df_svb"])],
})
FV_SHARE.update({
 "koege": lambda: f"Kun {hp('koege','FJ',1)} af de beboede parcel- og rækkehuse i Køge Kommune har fjernvarme, mod {hp('dk','FJ',1)} i hele landet. {tal(HEAT['koege']['CN'])} huse ({hp('koege','CN',1)}) har naturgas, {tal(HEAT['koege']['CO'])} oliefyr og {tal(HEAT['koege']['ELV'])} elvarme.",
 "svendborg": lambda: f"{hp('svendborg','FJ',1)} af de beboede parcel- og rækkehuse i Svendborg Kommune har fjernvarme, mod {hp('dk','FJ',1)} i hele landet. Svendborg Kommune opgør selv 7.757 gasopvarmede og 1.939 olieopvarmede bygninger og har som mål, at 90 % af oliefyrene og 65 % af gasfyrene er skiftet ud senest i 2030.",
})
FV_SOURCES_H.update({"koege": "Overskudsvarme i Bjæverskov og elkedel i Borup", "svendborg": "Varmepumper, elkedler og gas i Svendborg"})
_reg_age_old5 = reg_age_note
def reg_age_note(c, kommune):
    s = STOCK[c]; B = s["B"]; t = s["tot"]
    if c == "koege":
        return (f"{tal(B['1960-1979'])} af de beboede huse i Køge Kommune ({pct(B['1960-1979'], t)}) er bygget i 1960-1979. Tjek lokalplanen for dit kvarter, før du bestiller: kommunen kan kun i mindre grad dispensere.", ["koe_disp"])
    if c == "svendborg":
        return (f"{tal(B['før 1960'])} af kommunens beboede huse ({pct(B['før 1960'], t)}) er bygget før 1960. Bor du i et ældre kvarter, så tjek byplanvedtægt og deklarationer for regler om tagmateriale.", ["svb_sol"])
    return _reg_age_old5(c, kommune)

# ---------- daglig by-rutine 31. okt. 2026: Faaborg (DK1, Faaborg-Midtfyn Kommune) og Aabenraa (DK1, Region Syddanmark) ----------
_CA = lambda x: HEAT[x]["CA"] / hs(x); _STR = lambda x: ROOF[x]["T"]["14"] / ROOF[x]["tot"]; _MET = lambda x: ROOF[x]["T"]["12"] / ROOF[x]["tot"]
SOL_ORDER.update({
 "faaborg": ["boliger", "lokalt", "produktion", "tage", "faq", "guides"],
 "aabenraa": ["tage", "lokalt", "boliger", "produktion", "guides", "faq"],
})
VP_ORDER.update({
 "faaborg": ["lokale-byer", "lokalt", "opvarmning", "pris", "faq", "guides"],
 "aabenraa": ["lokalt", "opvarmning", "pris", "lokale-byer", "guides", "faq"],
})
FV_ORDER.update({
 "faaborg": ["status", "andel", "priser", "billigst", "varmekilder", "faq"],
 "aabenraa": ["priser", "status", "andel", "varmekilder", "billigst", "faq"],
})
SOL_PROD.update({
 "faaborg": ("Solproduktion på Sydfyn: Faaborg",
   lambda: f"PVGIS beregner ca. <strong>{tal(PV['faaborg']['syd'])} kWh pr. kWp om året</strong> for et sydvendt tag med 35° hældning i Faaborg, {rk(_PVY, 'faaborg', 'højeste')} af de {nw()} byer på dette site. Et 6 kWp-anlæg mod syd giver dermed ca. {tal(PV['faaborg']['syd']*6)} kWh om året. Maj er den bedste måned med ca. {tal(PV['faaborg']['months'][4]*6)} kWh, mens december kun giver ca. {tal(PV['faaborg']['months'][11]*6)} kWh."),
 "aabenraa": ("Øst, vest eller syd: produktion i Aabenraa",
   lambda: f"For et sydvendt tag med 35° hældning i Aabenraa beregner PVGIS ca. {tal(PV['aabenraa']['syd'])} kWh pr. kWp om året. Vender taget mod vest, bliver det ca. {tal(PV['aabenraa']['vest'])} kWh, og mod øst ca. {tal(PV['aabenraa']['oest'])} kWh pr. kWp. Ved den optimale hældning på {PV['aabenraa']['opt_angle']}° når et sydvendt anlæg ca. {tal(PV['aabenraa']['opt'])} kWh pr. kWp."),
})
SOL_PROD_SRC_NEW.update({"faaborg": ["pv_faaborg", "pvgis"], "aabenraa": ["pv_aabenraa", "pvo_aabenraa", "pvv_aabenraa"]})
SOL_ROOF.update({
 "faaborg": ("Stråtag og cementsten i Faaborg-Midtfyn",
   lambda: f"{tal(ROOF['faaborg']['T']['14'])} parcel- og rækkehuse i Faaborg-Midtfyn Kommune har <strong>stråtag</strong> ({rp('faaborg','14',1)}), {rk(_STR, 'faaborg', 'største')} andel af de {nw()} byer og mod {rp('dk','14',1)} i hele landet. {rp('faaborg','08')} har cementsten, {rp('faaborg','06')} fibercement og {rp('faaborg','10')} tegl. Er taget af ældre fibercement, så få det vurderet, før panelerne skrues fast: ifølge Bolius kan det indeholde asbest.",
   ["dst_bygb50", "bolius_asb"]),
 "aabenraa": ("Metaltage, eternit og tegl i Aabenraa Kommune",
   lambda: f"{rp('aabenraa','12',1)} af parcel- og rækkehusene i Aabenraa Kommune har tag af <strong>metalplader</strong>, {rk(_MET, 'aabenraa', 'største')} andel af de {nw()} byer. {rp('aabenraa','06')} har fibercement, {rp('aabenraa','08')} cementsten og {rp('aabenraa','10')} tegl, mens {rp('aabenraa','02',1)} har fladt tag. Monteringen afhænger af tagtypen, så få installatøren til at se taget, før du får et tilbud.",
   ["dst_bygb50", "bolius_mont"]),
})
SOL_HOMES.update({
 "faaborg": lambda: f"{pct(STOCK['faaborg']['B']['før 1960'],STOCK['faaborg']['tot'])} af de {tal(STOCK['faaborg']['tot'])} beboede parcel- og rækkehuse i Faaborg-Midtfyn Kommune er bygget før 1960, {rk(_OLD, 'faaborg', 'største')} andel af de {nw()} byer. Kommunens største by er Ringe med {tal(town('faaborg','Ringe'))} indbyggere, tæt fulgt af Faaborg med {tal(town('faaborg','Faaborg'))}. Siden gælder også Årslev, Nørre Lyndelse, Ryslinge og Kværndrup.",
 "aabenraa": lambda: f"Aabenraa Kommune har {tal(STOCK['aabenraa']['tot'])} beboede parcel- og rækkehuse, og {pct(STOCK['aabenraa']['ejer'],STOCK['aabenraa']['tot'])} er ejerboliger. {pct(STOCK['aabenraa']['B']['1960-1979'],STOCK['aabenraa']['tot'])} er bygget i 1960-1979. Siden gælder også Rødekro ({tal(town('aabenraa','Rødekro'))} indbyggere), Padborg, Tinglev, Løjt Kirkeby og Kruså.",
})
SOL_HOMES_SRC_NEW.update({"faaborg": ["fmk_elv"], "aabenraa": []})
SOL_HOMES_H.update({"faaborg": "Ældre huse fra Faaborg til Ringe", "aabenraa": "Huse fra Aabenraa til Padborg og Tinglev"})
SOL_XFAQ.update({
 "faaborg": [("Hvor meget giver solceller i Faaborg om sommeren?", lambda: f"PVGIS beregner ca. {tal(PV['faaborg']['months'][5]*6)} kWh i juni og {tal(PV['faaborg']['months'][6]*6)} kWh i juli fra et 6 kWp-anlæg mod syd. Over hele året giver det ca. {tal(PV['faaborg']['syd']*6)} kWh.", ["pv_faaborg"])],
 "aabenraa": [("Kan det betale sig med solceller på et vestvendt tag i Aabenraa?", lambda: f"Et vestvendt tag giver ifølge PVGIS ca. {tal(PV['aabenraa']['vest'])} kWh pr. kWp om året mod {tal(PV['aabenraa']['syd'])} kWh mod syd. Et vestvendt 6 kWp-anlæg giver dermed ca. {tal(PV['aabenraa']['vest']*6)} kWh om året, og mere af strømmen kommer sidst på eftermiddagen.", ["pvv_aabenraa", "pv_aabenraa"])],
})
VP_HEAT.update({
 "faaborg": ("Gas, træpiller og varmepumper i Faaborg-Midtfyn",
   lambda: f"Kun {hp('faaborg','FJ',1)} af de {tal(hs('faaborg'))} beboede parcel- og rækkehuse i Faaborg-Midtfyn Kommune har fjernvarme, mod {hp('dk','FJ',1)} på landsplan. {tal(HEAT['faaborg']['CN'])} ({hp('faaborg','CN',1)}) har naturgas, og {tal(HEAT['faaborg']['CA'])} ({hp('faaborg','CA',1)}) har centralvarme med en anden kilde end olie og gas, fx træpiller, {rk(_CA, 'faaborg', 'største')} andel af de {nw()} byer. {tal(HEAT['faaborg']['VP'])} huse ({hp('faaborg','VP',1)}) har allerede varmepumpe."),
 "aabenraa": ("Elvarme i hvert ellevte hus i Aabenraa Kommune",
   lambda: f"{tal(HEAT['aabenraa']['ELV'])} beboede parcel- og rækkehuse i Aabenraa Kommune ({hp('aabenraa','ELV',1)}) har elvarme, {rk(_EL, 'aabenraa', 'højeste')} andel af de {nw()} byer, mod {hp('dk','ELV',1)} på landsplan. {hp('aabenraa','FJ',1)} har fjernvarme, {tal(HEAT['aabenraa']['CN'])} naturgas og {tal(HEAT['aabenraa']['CO'])} oliefyr. Elvarme er en af de varmekilder, Varmepumpepuljen giver tilskud til at skifte ud."),
})
VP_HEAT_SRC_NEW.update({"faaborg": ["fmk_vp"], "aabenraa": ["se_vpp"]})
VP_TOWNS.update({
 "faaborg": [("Faaborg", "FFV Varme. Udvidelsen i Faaborg nordvest er sat på pause", ["ffv_proj"]),
             ("Ringe", "Midtfyns Fjernvarme", ["ft_pris", "df_mfe"]),
             ("Kværndrup", "Eget værk: Kværndrup Fjernvarme", ["fmk_elv", "ft_pris"]),
             ("Korinth", "Fjernvarmeprojektet aflyst 10/12 2025. Tilskud til varmepumpe muligt", ["fmk_kor"]),
             ("Espe", "Fjernvarmeprojektet afsluttet uden fjernvarme", ["ffv_proj"]),
             ("Brobyværk, Horne, Vester Åby", "Fjernvarmeprojekterne sat på pause i ca. et år", ["ffv_pause"])],
 "aabenraa": [("Aabenraa og Rødekro", "Aabenraa Fjernvarme", ["afv_pris", "ft_pris"]),
              ("Bolderslev", "Fjernvarme på vej. De første forbrugere ventes i 1. kvartal 2027", ["afv_bol"]),
              ("Varnæs og Bovrup", "Fjernvarme under udrulning. Konverteringsbidrag 3.700 kr. om året", ["afv_var", "afv_pris"]),
              ("Tinglev", "Aabenraa Fjernvarme med transmissionsbidrag", ["afv_pris"]),
              ("Padborg", "Eget værk: Padborg Fjernvarme", ["ft_pris"]),
              ("Tumbøl og Felsted", "Overskudsvarme fra en biogasgård i Tumbøl", ["afv_gylle"])],
})
VP_TOWNS_NOTE.update({
 "faaborg": "Bor du i en af de mange landsbyer uden for fjernvarmen, så tjek kommunens varmeplan, før du søger tilskud. Planen er kun vejledende, men tilskuddet bortfalder, når et konkret fjernvarmeprojekt er godkendt og sat i gang.",
 "aabenraa": "Bor du uden for byerne med fjernvarme, så slå adressen op i kommunens varmeplanlægning, før du søger tilskud. Områder, hvor fjernvarmen ikke kan nå ud, udpeges til individuel opvarmning.",
})
VP_XFAQ.update({
 "faaborg": [("Hvor mange huse i Faaborg-Midtfyn har stadig gas- eller oliefyr?", lambda: f"Danmarks Statistik registrerer {tal(HEAT['faaborg']['CN'])} beboede parcel- og rækkehuse med naturgas og {tal(HEAT['faaborg']['CO'])} med oliefyr i 2026, ud af {tal(hs('faaborg'))}. {tal(HEAT['faaborg']['ELV'])} har elvarme og {tal(HEAT['faaborg']['VP'])} varmepumpe.", ["dst_bol102"])],
 "aabenraa": [("Hvor mange huse i Aabenraa Kommune har allerede varmepumpe?", lambda: f"{tal(HEAT['aabenraa']['VP'])} beboede parcel- og rækkehuse ({hp('aabenraa','VP',1)}) ifølge Danmarks Statistik, 2026, mod {hp('dk','VP',1)} på landsplan. {tal(HEAT['aabenraa']['ELV'])} har elvarme og {tal(HEAT['aabenraa']['CN'])} naturgas.", ["dst_bol102"])],
})
FV_SOURCES.update({
 "faaborg": [("Faaborg-Midtfyn Kommune beskriver forsyningen som <strong>et net af små og mellemstore kraftvarmeværker</strong>, og den kollektive varmeforsyning dækkes af fjernvarmeselskaberne.", ["fmk_elv"]),
             ("Ifølge varmeplanen skal ny fjernvarme hovedsageligt bygge på <strong>lokal spildvarme og varmepumper</strong>. Hvor fjernvarme ikke er muligt, peger kommunen overvejende på individuelle varmepumper.", ["fmk_vp"])],
 "aabenraa": [("På en gård i <strong>Tumbøl</strong> kører gasmotorer på biogas fra gylle. Om sommeren ventes overskudsvarmen at kunne forsyne både Tumbøl og Felsted via Aabenraa Fjernvarmes net.", ["afv_gylle"]),
              ("Kommunens varmeplan fra 2022 åbner for <strong>ø-løsninger</strong>, hvor nye varmekilder forsyner et lukket net i byer langt fra det eksisterende fjernvarmenet.", ["abr_vp22"])],
})
FV_SHARE.update({
 "faaborg": lambda: f"{hp('faaborg','FJ',1)} af de beboede parcel- og rækkehuse i Faaborg-Midtfyn Kommune har fjernvarme, mod {hp('dk','FJ',1)} i hele landet. Kommunens varmeplan regnede med, at ca. 12.675 af kommunens 25.992 ejendomme ville have fjernvarme, når de besluttede udbygninger var færdige, og at 2.813 ejendomme allerede havde egen varmepumpe.",
 "aabenraa": lambda: f"{hp('aabenraa','FJ',1)} af de beboede parcel- og rækkehuse i Aabenraa Kommune har fjernvarme, tæt på landsgennemsnittet på {hp('dk','FJ',1)}. {tal(HEAT['aabenraa']['CN'])} huse ({hp('aabenraa','CN',1)}) har naturgas og {tal(HEAT['aabenraa']['ELV'])} ({hp('aabenraa','ELV',1)}) elvarme.",
})
FV_SOURCES_H.update({"faaborg": "Kraftvarme, spildvarme og varmepumper i Faaborg-Midtfyn", "aabenraa": "Biogas i Tumbøl og nye net i Aabenraa"})
_reg_age_old6 = reg_age_note
def reg_age_note(c, kommune):
    s = STOCK[c]; B = s["B"]; t = s["tot"]
    if c == "faaborg":
        return (f"{tal(B['før 1960'])} af kommunens beboede huse ({pct(B['før 1960'], t)}) er bygget før 1960. Ligger dit hus i en bevarende lokalplan eller byplanvedtægt, skal du søge dispensation, før du sætter solceller op.", ["fmk_elv"])
    if c == "aabenraa":
        return (f"{tal(B['1960-1979'])} af de beboede huse i Aabenraa Kommune ({pct(B['1960-1979'], t)}) er bygget i 1960-1979. Tjek fanen med lokal- og kommuneplaner i Byg og Miljø for dit kvarter, før du bestiller.", ["abr_bom"])
    return _reg_age_old6(c, kommune)

# ---------- daglig by-rutine 1. nov. 2026: Herning (DK1, Region Midtjylland) og Greve (DK2, Region Sjælland) ----------
_B6079 = lambda x: STOCK[x]["B"]["1960-1979"] / STOCK[x]["tot"]; _CEM = lambda x: ROOF[x]["T"]["08"] / ROOF[x]["tot"]; _FLAD = lambda x: ROOF[x]["T"]["02"] / ROOF[x]["tot"]
_GSTR = "Greve Strand (del af Hovedstadsområdet)"
SOL_ORDER.update({
 "herning": ["lokalt", "tage", "produktion", "boliger", "faq", "guides"],
 "greve": ["lokalt", "tage", "produktion", "boliger", "faq", "guides"],
})
VP_ORDER.update({
 "herning": ["opvarmning", "lokale-byer", "lokalt", "pris", "guides", "faq"],
 "greve": ["lokalt", "lokale-byer", "opvarmning", "pris", "faq", "guides"],
})
FV_ORDER.update({
 "herning": ["andel", "priser", "status", "billigst", "varmekilder", "faq"],
 "greve": ["status", "priser", "andel", "billigst", "varmekilder", "faq"],
})
SOL_PROD.update({
 "herning": ("Sol i Midtjylland: juni vs. december i Herning",
   lambda: f"Et sydvendt 6 kWp-anlæg i Herning giver ifølge PVGIS ca. {tal(PV['herning']['months'][5]*6)} kWh i juni, men kun ca. {tal(PV['herning']['months'][11]*6)} kWh i december. Over hele året lander et anlæg med 35° hældning på ca. <strong>{tal(PV['herning']['syd']*6)} kWh</strong> ({tal(PV['herning']['syd'])} kWh pr. kWp) – {rk(_PVY, 'herning', 'laveste', rev=True)} blandt de {nw()} byer her på sitet. Ved optimal hældning ({PV['herning']['opt_angle']}°) stiger årsudbyttet til ca. {tal(PV['herning']['opt']*6)} kWh."),
 "greve": ("Syd, øst eller vest: produktion i Greve",
   lambda: f"For et sydvendt tag med 35° hældning i Greve beregner PVGIS ca. {tal(PV['greve']['syd'])} kWh pr. kWp om året. Et tag mod øst giver ca. {tal(PV['greve']['oest'])} kWh og mod vest ca. {tal(PV['greve']['vest'])} kWh pr. kWp, altså ca. {pct(PV['greve']['vest'], PV['greve']['syd'])} af et sydvendt tag. Maj og juni er de bedste måneder med ca. {tal(PV['greve']['months'][4]*6)} og {tal(PV['greve']['months'][5]*6)} kWh fra et 6 kWp-anlæg mod syd."),
})
SOL_PROD_SRC_NEW.update({"herning": ["pv_herning", "pvgis"], "greve": ["pv_greve", "pvo_greve", "pvv_greve"]})
SOL_ROOF.update({
 "herning": ("Få tegltage: cementsten dominerer i Herning",
   lambda: f"Danmarks Statistik viser, at {rp('herning','08',1)} af parcel- og rækkehusene i Herning Kommune har <strong>cementsten</strong> – {rk(_CEM, 'herning', 'største')} andel af de {nw()} byer. Fibercement dækker {rp('herning','06')}, mens tegl kun sidder på {rp('herning','10')} (landsplan {rp('dk','10')}). Bolius advarer om, at ældre fibercementplader fra før 1984 næsten altid indeholder asbest, så få taget tjekket før montage.",
   ["dst_bygb50", "bolius_asb"]),
 "greve": ("Flade tage og fibercement i Greve",
   lambda: f"{rp('greve','02',1)} af parcel- og rækkehusene i Greve Kommune har <strong>fladt tag</strong>, {rk(_FLAD, 'greve', 'højeste')} andel af de {nw()} byer, mod {rp('dk','02',1)} i hele landet. {rp('greve','06')} har fibercement, {rp('greve','08')} cementsten og {rp('greve','10')} tegl. Greve Kommunes tjekliste for anlæg uden byggetilladelse gælder kun tage, der ikke er flade, så har du fladt tag, så kontakt kommunen, før du bestiller.",
   ["dst_bygb50", "gre_tjek"]),
})
SOL_HOMES.update({
 "herning": lambda: f"Fra Herning by ({tal(town('herning','Herning'))} indbyggere) til Sunds ({tal(town('herning','Sunds'))}) og Vildbjerg ({tal(town('herning','Vildbjerg'))}) tæller kommunen {tal(STOCK['herning']['tot'])} beboede parcel- og rækkehuse. {pct(STOCK['herning']['B']['1960-1979'],STOCK['herning']['tot'])} er fra 1960-1979 – {rk(_B6079, 'herning', 'største')} andel blandt de {nw()} byer. Aulum, Kibæk og Sønder Felding er også dækket af siden.",
 "greve": lambda: f"{pct(STOCK['greve']['ejer'],STOCK['greve']['tot'])} af de {tal(STOCK['greve']['tot'])} beboede parcel- og rækkehuse i Greve Kommune er ejerboliger, {rk(_EJ, 'greve', 'højeste')} andel af de {nw()} kommuner, og {pct(STOCK['greve']['B']['1960-1979'],STOCK['greve']['tot'])} er bygget i 1960-1979, {rk(_B6079, 'greve', 'største')} andel på sitet. Byområdet Greve Strand har {tal(town('greve',_GSTR))} indbyggere ifølge Danmarks Statistik. Siden gælder også Tune ({tal(town('greve','Tune'))}), Greve Landsby og Kildebrønde.",
})
SOL_HOMES_SRC_NEW.update({"herning": [], "greve": []})
SOL_HOMES_H.update({"herning": "Fra Herning by til Sunds, Vildbjerg og Aulum", "greve": "Ejerboliger fra Greve Strand til Tune"})
SOL_XFAQ.update({
 "herning": [("Hvor meget giver solceller i Herning om vinteren?", lambda: f"PVGIS beregner ca. {tal(PV['herning']['months'][11]*6)} kWh i december og {tal(PV['herning']['months'][0]*6)} kWh i januar fra et 6 kWp-anlæg mod syd i Herning, mod ca. {tal(PV['herning']['months'][4]*6)} kWh i maj.", ["pv_herning"])],
 "greve": [("Kan solceller betale sig på et øst-vest-tag i Greve?", lambda: f"Et østvendt tag giver ifølge PVGIS ca. {tal(PV['greve']['oest'])} kWh og et vestvendt ca. {tal(PV['greve']['vest'])} kWh pr. kWp om året i Greve, mod {tal(PV['greve']['syd'])} kWh mod syd. Et 6 kWp-anlæg mod vest giver dermed ca. {tal(PV['greve']['vest']*6)} kWh om året, og mere af strømmen kommer sidst på dagen.", ["pvo_greve", "pvv_greve", "pv_greve"])],
})
VP_HEAT.update({
 "herning": ("Næsten fire ud af fem huse har fjernvarme i Herning Kommune",
   lambda: f"{hp('herning','FJ',1)} af de {tal(hs('herning'))} beboede parcel- og rækkehuse i Herning Kommune har fjernvarme, mod {hp('dk','FJ',1)} på landsplan. Kun {tal(HEAT['herning']['CN'])} ({hp('herning','CN',1)}) har naturgas og {tal(HEAT['herning']['CO'])} oliefyr, mens {tal(HEAT['herning']['CA'])} ({hp('herning','CA',1)}) har centralvarme med en anden kilde, fx træpiller, {rk(_CA, 'herning', 'største')} andel af de {nw()} byer. {tal(HEAT['herning']['VP'])} huse ({hp('herning','VP',1)}) har allerede varmepumpe."),
 "greve": ("Over halvdelen af husene i Greve har naturgas",
   lambda: f"{tal(HEAT['greve']['CN'])} beboede parcel- og rækkehuse i Greve Kommune ({hp('greve','CN',1)}) har naturgas, {rk(_CN, 'greve', 'højeste')} andel af de {nw()} byer, mod {hp('dk','CN',1)} på landsplan. Kun {hp('greve','FJ',1)} har fjernvarme. {tal(HEAT['greve']['VP'])} huse ({hp('greve','VP',1)}) har allerede varmepumpe, og {tal(HEAT['greve']['ELV'])} har elvarme."),
})
VP_HEAT_SRC_NEW.update({"herning": [], "greve": []})
VP_TOWNS.update({
 "herning": [("Herning", "Verdo. Tilslutning 25.000-40.000 kr. for et enfamiliehus", ["verdo_her_pris"]),
             ("Vildbjerg", "Eget værk: Vildbjerg Varme", ["ft_pris"]),
             ("Sunds", "Eget værk: Sunds Vand- og Varmeværk", ["ft_pris"]),
             ("Aulum", "Eget værk: Aulum Fjernvarme", ["ft_pris"]),
             ("Kibæk", "Eget værk: Kibæk Varmeværk", ["ft_pris"]),
             ("Landsbyer uden fjernvarme", "Kommunens pulje til rådgivning om fælles varmeløsninger", ["her_faelles"])],
 "greve": [("Greve Strand og Hundige", "Greve Fjernvarme. Udbygges i faser frem mod 2038", ["gfv_kan", "gre_vpl"]),
           ("Åsager, Firhøj m.fl.", "60 %-kravet nået. Gravearbejdet ventes at begynde i starten af 2027", ["gfv_kan"]),
           ("Mosede", "Mosede Fjernvarmeværk", ["gre_varme", "ft_pris"]),
           ("Tune", "Fjernvarmeprojektet aflyst i 2026. Tilskud til varmepumpe muligt igen", ["gre_tune"]),
           ("Greve Landsby og Kildebrønde", "Uden for Greve Fjernvarmes forsyningsområde", ["gfv_kan"]),
           ("Vest for motorvejen", "Tranegilde Fjernvarme", ["gfv_kan", "gre_varme"])],
})
VP_TOWNS_NOTE.update({
 "herning": "Bor du i en landsby uden fjernvarme, så tal med naboerne om en fælles varmeløsning. Kommunens pulje kræver mindst 10 boliger, hvoraf mindst halvdelen i dag har olie- eller gasfyr.",
 "greve": "Bor du øst for motorvejen, så tjek Greve Fjernvarmes udbygningsfaser, før du vælger varmepumpe. I Tune kan du igen søge tilskud fra statens varmepumpepulje, efter at fjernvarmeprojektet er aflyst.",
})
VP_XFAQ.update({
 "herning": [("Hvor mange huse i Herning Kommune har stadig olie- eller gasfyr?", lambda: f"Danmarks Statistik registrerer {tal(HEAT['herning']['CO'])} beboede parcel- og rækkehuse med oliefyr og {tal(HEAT['herning']['CN'])} med naturgas i 2026, ud af {tal(hs('herning'))}. {tal(HEAT['herning']['ELV'])} har elvarme og {tal(HEAT['herning']['VP'])} varmepumpe.", ["dst_bol102"])],
 "greve": [("Hvor mange huse i Greve Kommune har allerede varmepumpe?", lambda: f"{tal(HEAT['greve']['VP'])} beboede parcel- og rækkehuse ({hp('greve','VP',1)}) ifølge Danmarks Statistik, 2026, mod {hp('dk','VP',1)} på landsplan. {tal(HEAT['greve']['CN'])} har stadig naturgas og {tal(HEAT['greve']['CO'])} oliefyr.", ["dst_bol102"])],
})
FV_SOURCES.update({
 "herning": [("Verdo skriver, at 90 % af fjernvarmen til de 35.000 adresser i Herning og omegn produceres på vedvarende energi i form af <strong>biomasse</strong>.", ["verdo_her"]),
             ("Herning Kommunes pulje til <strong>fælles varmeløsninger</strong> betaler rådgivning om fx jordvarme eller en fælles luft-vand-varmepumpe i lokalområder uden fjernvarme, men ikke selve anlægget.", ["her_faelles"])],
 "greve": [("Fjernvarmen i Greve produceres i hovedtræk ved <strong>affaldsforbrænding og biomasse</strong> og en smule fossile brændsler i spidsbelastede perioder, og varmen kommer fra VEKS (Vestegnens Kraftvarmeselskab).", ["gre_varme"]),
           ("Greve er en del af <strong>hovedstadsområdets sammenhængende fjernvarmesystem</strong>, hvor varmen leveres via store transmissionsrør tæt ved Køge Bugt-motorvejen.", ["gfv_kan"])],
})
FV_SHARE.update({
 "herning": lambda: f"{hp('herning','FJ',1)} af de beboede parcel- og rækkehuse i Herning Kommune har fjernvarme, mod {hp('dk','FJ',1)} i hele landet. Kun {tal(HEAT['herning']['CN'])} huse ({hp('herning','CN',1)}) har naturgas og {tal(HEAT['herning']['CO'])} oliefyr.",
 "greve": lambda: f"Kun {hp('greve','FJ',1)} af de beboede parcel- og rækkehuse i Greve Kommune har fjernvarme, mod {hp('dk','FJ',1)} i hele landet. {tal(HEAT['greve']['CN'])} huse ({hp('greve','CN',1)}) har naturgas, {rk(_CN, 'greve', 'højeste')} andel af de {nw()} byer.",
})
FV_SOURCES_H.update({"herning": "Biomasse i Herning og fælles varme i landsbyerne", "greve": "Affald og biomasse fra VEKS i Greve"})
_reg_age_old7 = reg_age_note
def reg_age_note(c, kommune):
    s = STOCK[c]; B = s["B"]; t = s["tot"]
    if c == "herning":
        return (f"{tal(B['1960-1979'])} af de beboede huse i Herning Kommune ({pct(B['1960-1979'], t)}) er bygget i 1960-1979. Er du i tvivl om, hvad taget kan bære, så send skitser og en beregning af lasten via Byg og Miljø, som kommunen anbefaler.", ["her_sol"])
    if c == "greve":
        return (f"{tal(B['1960-1979'])} af de beboede huse i Greve Kommune ({pct(B['1960-1979'], t)}) er bygget i 1960-1979. Find lokalplanen for dit kvarter og tjek, om den forbyder blanke og reflekterende tagmaterialer: så skal panelerne være antirefleksbehandlede.", ["gre_tjek"])
    return _reg_age_old7(c, kommune)

# ---------- daglig by-rutine 2. nov. 2026: Hjørring (DK1, Region Nordjylland) og Holte (Rudersdal Kommune, DK2, Region Hovedstaden) ----------
_FIB = lambda x: ROOF[x]["T"]["06"] / ROOF[x]["tot"]; _TEGL = lambda x: ROOF[x]["T"]["10"] / ROOF[x]["tot"]; _CO = lambda x: HEAT[x]["CO"] / hs(x)
_RHOV = "Rudersdal (del af Hovedstadsområdet)"
SOL_ORDER.update({
 "hjoerring": ["tage", "produktion", "lokalt", "boliger", "faq", "guides"],
 "holte": ["boliger", "lokalt", "tage", "produktion", "guides", "faq"],
})
VP_ORDER.update({
 "hjoerring": ["lokale-byer", "opvarmning", "pris", "lokalt", "faq", "guides"],
 "holte": ["opvarmning", "lokalt", "pris", "lokale-byer", "guides", "faq"],
})
FV_ORDER.update({
 "hjoerring": ["priser", "status", "billigst", "andel", "faq", "varmekilder"],
 "holte": ["status", "andel", "varmekilder", "priser", "billigst", "faq"],
})
SOL_PROD.update({
 "hjoerring": ("Lyse sommernætter, mørk vinter: produktion i Hjørring",
   lambda: f"PVGIS beregner ca. {tal(PV['hjoerring']['syd'])} kWh pr. kWp om året for et sydvendt tag med 35° hældning i Hjørring. Juni giver ca. {tal(PV['hjoerring']['months'][5]*6)} kWh fra et 6 kWp-anlæg mod syd, {rk(lambda x: PV[x]['months'][5], 'hjoerring', 'højeste')} junital af de {nw()} byer, mens december kun giver ca. {tal(PV['hjoerring']['months'][11]*6)} kWh. Ved den optimale hældning på {PV['hjoerring']['opt_angle']}° bliver det ca. {tal(PV['hjoerring']['opt']*6)} kWh om året."),
 "holte": ("Hvor meget giver solceller i Holte?",
   lambda: f"For et sydvendt tag med 35° hældning i Holte beregner PVGIS ca. <strong>{tal(PV['holte']['syd'])} kWh pr. kWp om året</strong>. Et 6 kWp-anlæg giver dermed ca. {tal(PV['holte']['syd']*6)} kWh om året mod syd og ca. {tal(PV['holte']['oest']*6)} kWh mod øst. Har du fladt tag, så husk, at stativer kan ændre husets udseende, og at ældre lokalplaner i Rudersdal kan regulere det."),
})
SOL_PROD_SRC_NEW.update({"hjoerring": ["pv_hjoerring", "pvgis"], "holte": ["pv_holte", "pvo_holte", "rud_solvp"]})
SOL_ROOF.update({
 "hjoerring": ("Næsten halvdelen af tagene i Hjørring er fibercement",
   lambda: f"{rp('hjoerring','06',1)} af parcel- og rækkehusene i Hjørring Kommune har tag af <strong>fibercement</strong>, {rk(_FIB, 'hjoerring', 'højeste')} andel af de {nw()} byer, mod {rp('dk','06',1)} i hele landet. {rp('hjoerring','10')} har tegl og {rp('hjoerring','08')} cementsten. Ifølge Bolius indeholder bølge- og kunstskiferplader fra før 1984 næsten altid asbest, så få taget vurderet, før panelerne skrues fast.",
   ["dst_bygb50", "bolius_asb"]),
 "holte": ("Tegl og flade tage i Rudersdal",
   lambda: f"{rp('holte','10')} af parcel- og rækkehusene i Rudersdal Kommune har <strong>tegltag</strong>, {rk(_TEGL, 'holte', 'højeste')} andel af de {nw()} byer, og {rp('holte','02',1)} har <strong>fladt tag</strong>, {rk(lambda x: ROOF[x]['T']['02'] / ROOF[x]['tot'], 'holte', 'højeste')} andel på sitet, mod {rp('dk','02',1)} i hele landet. Kun {rp('holte','06')} har fibercement. Kommunen beder dig oplyse, om panelerne ligger oven på taget, er indfældet eller står på stativ, hvis du skal søge dispensation.",
   ["dst_bygb50", "rud_solvp"]),
})
SOL_HOMES.update({
 "hjoerring": lambda: f"Hjørring Kommune har {tal(STOCK['hjoerring']['tot'])} beboede parcel- og rækkehuse, og kun {pct(STOCK['hjoerring']['B']['2000+'],STOCK['hjoerring']['tot'])} er bygget i 2000 eller senere, {rk(_NEW, 'hjoerring', 'laveste', rev=True)} andel af de {nw()} byer. {pct(STOCK['hjoerring']['B']['før 1960'],STOCK['hjoerring']['tot'])} er fra før 1960. Hjørring by har {tal(town('hjoerring','Hjørring'))} indbyggere, og siden gælder også Hirtshals ({tal(town('hjoerring','Hirtshals'))}), Sindal ({tal(town('hjoerring','Sindal'))}), Vrå, Tårs og Løkken.",
 "holte": lambda: f"{pct(STOCK['holte']['ejer'],STOCK['holte']['tot'])} af de {tal(STOCK['holte']['tot'])} beboede parcel- og rækkehuse i Rudersdal Kommune er ejerboliger, {rk(_EJ, 'holte', 'højeste')} andel af de {nw()} kommuner, og {pct(STOCK['holte']['B']['1960-1979'],STOCK['holte']['tot'])} er bygget i 1960-1979. Ifølge Danmarks Statistik bor {tal(town('holte',_RHOV))} i den del af Hovedstadsområdet, der ligger i kommunen, og {tal(town('holte','Birkerød'))} i Birkerød. Siden gælder hele Rudersdal Kommune, hvis rådhus ligger i Holte.",
})
SOL_HOMES_SRC_NEW.update({"hjoerring": [], "holte": ["rud_fjv"]})
SOL_HOMES_H.update({"hjoerring": "Ældre huse fra Hjørring til Hirtshals og Løkken", "holte": "Ejerboliger i Holte og resten af Rudersdal"})
SOL_XFAQ.update({
 "hjoerring": [("Hvor meget giver solceller i Hjørring om sommeren og vinteren?", lambda: f"PVGIS beregner ca. {tal(PV['hjoerring']['months'][5]*6)} kWh i juni og {tal(PV['hjoerring']['months'][6]*6)} kWh i juli fra et 6 kWp-anlæg mod syd i Hjørring, men kun ca. {tal(PV['hjoerring']['months'][11]*6)} kWh i december og {tal(PV['hjoerring']['months'][0]*6)} kWh i januar.", ["pv_hjoerring"])],
 "holte": [("Hvor meget giver et øst- eller vestvendt tag i Holte?", lambda: f"Ca. {tal(PV['holte']['oest'])} kWh pr. kWp om året mod øst og {tal(PV['holte']['vest'])} kWh mod vest, mod {tal(PV['holte']['syd'])} kWh mod syd (PVGIS, 35°). Et 6 kWp-anlæg mod vest giver dermed ca. {tal(PV['holte']['vest']*6)} kWh om året.", ["pvo_holte", "pvv_holte", "pv_holte"])],
})
VP_HEAT.update({
 "hjoerring": ("Næsten to ud af tre huse har fjernvarme i Hjørring Kommune",
   lambda: f"{hp('hjoerring','FJ',1)} af de {tal(hs('hjoerring'))} beboede parcel- og rækkehuse i Hjørring Kommune har fjernvarme, mod {hp('dk','FJ',1)} på landsplan. {tal(HEAT['hjoerring']['CO'])} huse ({hp('hjoerring','CO',1)}) har stadig oliefyr, {rk(_CO, 'hjoerring', 'højeste')} andel af de {nw()} byer, og {tal(HEAT['hjoerring']['CA'])} har centralvarme med en anden kilde, fx træpiller. Kun {tal(HEAT['hjoerring']['CN'])} har naturgas, og {tal(HEAT['hjoerring']['VP'])} ({hp('hjoerring','VP',1)}) har allerede varmepumpe."),
 "holte": ("Seks ud af ti huse i Rudersdal har naturgas",
   lambda: f"{tal(HEAT['holte']['CN'])} beboede parcel- og rækkehuse i Rudersdal Kommune ({hp('holte','CN',1)}) har naturgas, {rk(_CN, 'holte', 'højeste')} andel af de {nw()} byer, mod {hp('dk','CN',1)} på landsplan. Kun {hp('holte','FJ',1)} har fjernvarme. {tal(HEAT['holte']['VP'])} huse ({hp('holte','VP',1)}) har allerede varmepumpe, og {tal(HEAT['holte']['CO'])} har oliefyr."),
})
VP_HEAT_SRC_NEW.update({"hjoerring": [], "holte": []})
VP_TOWNS.update({
 "hjoerring": [("Hjørring", "Hjørring Varmeforsyning. Tilslutning 14.562,50 kr. + stikledning for et standardhus", ["hjv_tilslut"]),
               ("Hirtshals", "Eget værk: Hirtshals Fjernvarme", ["hjo_vpl", "ft_pris"]),
               ("Sindal", "Eget værk: Sindal Varmeforsyning", ["hjo_vpl", "ft_pris"]),
               ("Vrå", "Eget værk: Vrå Varmeværk", ["hjo_vpl", "ft_pris"]),
               ("Løkken", "Eget værk: Løkken Varmeværk", ["hjo_vpl", "ft_pris"]),
               ("Tornby, Horne, Bjergby m.fl.", "Hjørring Varmeforsyning har indstillet arbejdet med fjernvarme", ["hjv_status"])],
 "holte": [("Holte og Øverød", "Fjernvarmeprojektet aflyst i juni 2026", ["rud_fjv"]),
           ("Gl. Holte, Nærum, Trørød, Søllerød", "Fjernvarmeprojektet aflyst i juni 2026", ["rud_fjv"]),
           ("Skodsborg", "Med i det aflyste projekt for Gl. Holte m.fl.", ["rud_fjv"]),
           ("Birkerød", "Norfors' projekt for ca. 4.700 kunder i Birkerød og Bistrup fortsætter", ["rud_fjv"]),
           ("Vedbæk", "E.ON's projekt for ca. 530 kunder er forsinket", ["rud_fjv"]),
           ("Eksisterende net i Holte", "Holte Fjernvarme, ejet og drevet af Norfors siden 1. juli 2023", ["nf_holte"])],
})
VP_TOWNS_NOTE.update({
 "hjoerring": "Bor du i en af landsbyerne, hvor Hjørring Varmeforsyning har opgivet fjernvarmen, peger værket selv på varmepumpen som den billigste løsning for husejeren. Har du fået et varmebrev, så brug linket til boliganalysen i brevet.",
 "holte": "Bor du i Holte, Øverød, Gl. Holte, Nærum, Trørød, Søllerød eller Skodsborg, kommer fjernvarmen ikke foreløbig. Skifter du kun gasfyret ud med en varmepumpe, udløser det ikke tilslutningspligt, og du kan søge Varmepumpepuljen.",
})
VP_XFAQ.update({
 "hjoerring": [("Hvor mange huse i Hjørring Kommune har stadig oliefyr?", lambda: f"Danmarks Statistik registrerer {tal(HEAT['hjoerring']['CO'])} beboede parcel- og rækkehuse med oliefyr og {tal(HEAT['hjoerring']['CN'])} med naturgas i 2026, ud af {tal(hs('hjoerring'))}. {tal(HEAT['hjoerring']['ELV'])} har elvarme og {tal(HEAT['hjoerring']['VP'])} varmepumpe.", ["dst_bol102"])],
 "holte": [("Hvor mange huse i Rudersdal Kommune har gasfyr?", lambda: f"{tal(HEAT['holte']['CN'])} af de {tal(hs('holte'))} beboede parcel- og rækkehuse ({hp('holte','CN',1)}) har naturgas ifølge Danmarks Statistik, 2026. {tal(HEAT['holte']['VP'])} har allerede varmepumpe, og {tal(HEAT['holte']['FJ'])} har fjernvarme.", ["dst_bol102"])],
})
FV_SOURCES.update({
 "hjoerring": [("Affaldsvarme har i flere år udgjort ca. <strong>60 % af Hjørring Varmeforsynings</strong> varmeproduktion, og prisen på affaldsvarmen fra Nordværk er steget.", ["hjv_status", "df_hjv2026"]),
               ("Værket bygger en stor <strong>varmepumpe på overskudsvarme fra renseanlægget i Hæstrup</strong> til 2.500 husstande i Hjørring Syd, og næste skridt er en varmepumpe ved vandværket i Bagterp til ca. 200 huse.", ["df_haestrup"])],
 "holte": [("Norfors har <strong>ikke kapacitet</strong> til at levere mere varme fra Usserødværket til nye fjernvarmeområder i Rudersdal.", ["rud_fjv"]),
           ("I Vedbæk vil E.ON bruge <strong>overskudsvarme fra spildevandet</strong> fra en energicentral ved rensningsanlægget på Gøngehusvej, og kommunen undersøger fortsat geotermi.", ["rud_fjv"])],
})
FV_SHARE.update({
 "hjoerring": lambda: f"{hp('hjoerring','FJ',1)} af de beboede parcel- og rækkehuse i Hjørring Kommune har fjernvarme, mod {hp('dk','FJ',1)} i hele landet. {tal(HEAT['hjoerring']['CO'])} huse har oliefyr og {tal(HEAT['hjoerring']['CN'])} naturgas.",
 "holte": lambda: f"Kun {hp('holte','FJ',1)} af de beboede parcel- og rækkehuse i Rudersdal Kommune har fjernvarme, mod {hp('dk','FJ',1)} i hele landet. {tal(HEAT['holte']['CN'])} huse ({hp('holte','CN',1)}) har naturgas, {rk(_CN, 'holte', 'højeste')} andel af de {nw()} byer.",
})
FV_SOURCES_H.update({"hjoerring": "Affaldsvarme og overskudsvarme fra renseanlægget", "holte": "Usserødværket og overskudsvarme fra spildevand"})
_reg_age_old8 = reg_age_note
def reg_age_note(c, kommune):
    s = STOCK[c]; B = s["B"]; t = s["tot"]
    if c == "hjoerring":
        return (f"{tal(B['før 1960'])} af de beboede huse i Hjørring Kommune ({pct(B['før 1960'], t)}) er bygget før 1960. Tjek lokalplanen og eventuelle servitutter i Tingbogen for din grund, før du bestiller, som kommunen anbefaler.", ["hjo_sol"])
    if c == "holte":
        return (f"{tal(B['1960-1979'])} af de beboede huse i Rudersdal Kommune ({pct(B['1960-1979'], t)}) er bygget i 1960-1979. Er dit kvarter omfattet af en ældre lokalplan fra tidligere Søllerød eller Birkerød, så tjek reglerne for tag og solanlæg, før du bestiller.", ["rud_solvp"])
    return _reg_age_old8(c, kommune)

# ---------- daglig by-rutine 3. nov. 2026: Nykøbing Falster (Guldborgsund Kommune, DK2, Region Sjælland) og Haderslev (DK1, Region Syddanmark) ----------
_ELVs = lambda x: HEAT[x]["ELV"] / hs(x); _OLDs = lambda x: STOCK[x]["B"]["før 1960"] / STOCK[x]["tot"]; _CAs = lambda x: HEAT[x]["CA"] / hs(x)
SOL_ORDER.update({
 "nykoebing-falster": ["produktion", "boliger", "tage", "lokalt", "faq", "guides"],
 "haderslev": ["lokalt", "tage", "boliger", "produktion", "faq", "guides"],
})
VP_ORDER.update({
 "nykoebing-falster": ["opvarmning", "pris", "lokale-byer", "lokalt", "guides", "faq"],
 "haderslev": ["lokalt", "lokale-byer", "opvarmning", "pris", "faq", "guides"],
})
FV_ORDER.update({
 "nykoebing-falster": ["andel", "varmekilder", "priser", "status", "faq", "billigst"],
 "haderslev": ["status", "priser", "andel", "billigst", "varmekilder", "faq"],
})
SOL_PROD.update({
 "nykoebing-falster": ("Blandt de solrigeste byer på sitet: produktion i Nykøbing Falster",
   lambda: f"PVGIS beregner ca. <strong>{tal(PV['nykoebing-falster']['syd'])} kWh pr. kWp om året</strong> for et sydvendt tag med 35° hældning i Nykøbing Falster, {rk(_PVY, 'nykoebing-falster', 'højeste')} af de {nw()} byer på dette site. Et 6 kWp-anlæg giver dermed ca. {tal(PV['nykoebing-falster']['syd']*6)} kWh om året mod syd, ca. {tal(PV['nykoebing-falster']['vest']*6)} kWh mod vest og ca. {tal(PV['nykoebing-falster']['oest']*6)} kWh mod øst. Maj er den bedste måned med ca. {tal(PV['nykoebing-falster']['months'][4]*6)} kWh, tæt fulgt af juni med ca. {tal(PV['nykoebing-falster']['months'][5]*6)} kWh."),
 "haderslev": ("Hvor meget giver solceller i Haderslev?",
   lambda: f"For et sydvendt tag med 35° hældning i Haderslev beregner PVGIS ca. {tal(PV['haderslev']['syd'])} kWh pr. kWp om året, og ved den optimale hældning på {PV['haderslev']['opt_angle']}° ca. {tal(PV['haderslev']['opt'])} kWh. Et 6 kWp-anlæg giver ca. {tal(PV['haderslev']['syd']*6)} kWh om året. Mod vest falder det til ca. {tal(PV['haderslev']['vest']*6)} kWh og mod øst til ca. {tal(PV['haderslev']['oest']*6)} kWh, ca. {round(100*(1-PV['haderslev']['oest']/PV['haderslev']['syd']))} % mindre end mod syd."),
})
SOL_PROD_SRC_NEW.update({"nykoebing-falster": ["pv_nykoebing-falster", "pvo_nykoebing-falster", "pvv_nykoebing-falster"], "haderslev": ["pv_haderslev", "pvo_haderslev", "pvv_haderslev"]})
SOL_ROOF.update({
 "nykoebing-falster": ("Fibercement og tegl dominerer tagene i Guldborgsund",
   lambda: f"{rp('nykoebing-falster','06')} af parcel- og rækkehusene i Guldborgsund Kommune har tag af <strong>fibercement</strong>, {rk(_FIB, 'nykoebing-falster', 'højeste')} andel af de {nw()} byer, og {rp('nykoebing-falster','10')} har <strong>tegl</strong>. Kun {rp('nykoebing-falster','02',1)} har fladt tag, og det er værd at vide, fordi Guldborgsund Kommune kræver byggetilladelse til solceller på fladt tag. Ifølge Bolius indeholder bølge- og kunstskiferplader fra før 1984 næsten altid asbest.",
   ["dst_bygb50", "gul_faq", "bolius_asb"]),
 "haderslev": ("Tre tagtyper deler husene i Haderslev",
   lambda: f"I Haderslev Kommune er tagene delt mellem <strong>fibercement</strong> ({rp('haderslev','06')}), <strong>tegl</strong> ({rp('haderslev','10')}) og <strong>cementsten</strong> ({rp('haderslev','08')}) af parcel- og rækkehusene, mod {rp('dk','08')} cementsten i hele landet. Haderslev Kommune anbefaler, at en rådgiver tjekker, om tagkonstruktionen kan bære den ekstra vægt, og hører taget til konstruktionsklasse 2 eller højere, skal en certificeret rådgiver med.",
   ["dst_bygb50", "had_sol"]),
})
SOL_HOMES.update({
 "nykoebing-falster": lambda: f"{pct(STOCK['nykoebing-falster']['B']['før 1960'],STOCK['nykoebing-falster']['tot'])} af de {tal(STOCK['nykoebing-falster']['tot'])} beboede parcel- og rækkehuse i Guldborgsund Kommune er bygget før 1960, {rk(_OLDs, 'nykoebing-falster', 'højeste')} andel af de {nw()} byer, og kun {pct(STOCK['nykoebing-falster']['B']['2000+'],STOCK['nykoebing-falster']['tot'])} er fra 2000 eller senere. Nykøbing F. har {tal(town('nykoebing-falster','Nykøbing F'))} indbyggere, og siden gælder også Sakskøbing ({tal(town('nykoebing-falster','Sakskøbing'))}), Sundby ({tal(town('nykoebing-falster','Sundby'))}), Nørre Alslev, Stubbekøbing og Nysted.",
 "haderslev": lambda: f"Haderslev Kommune har {tal(STOCK['haderslev']['tot'])} beboede parcel- og rækkehuse. {pct(STOCK['haderslev']['B']['før 1960'],STOCK['haderslev']['tot'])} er bygget før 1960 og {pct(STOCK['haderslev']['B']['1960-1979'],STOCK['haderslev']['tot'])} i 1960-1979, mens kun {pct(STOCK['haderslev']['B']['2000+'],STOCK['haderslev']['tot'])} er fra 2000 eller senere. Haderslev by har {tal(town('haderslev','Haderslev'))} indbyggere, og siden gælder også Vojens ({tal(town('haderslev','Vojens'))}), Starup ({tal(town('haderslev','Starup'))}), Gram ({tal(town('haderslev','Gram'))}) og Marstrup.",
})
SOL_HOMES_SRC_NEW.update({"nykoebing-falster": [], "haderslev": []})
SOL_HOMES_H.update({"nykoebing-falster": "Ældre huse fra Nykøbing F. til Sakskøbing og Nysted", "haderslev": "Huse i Haderslev, Vojens og Gram"})
SOL_XFAQ.update({
 "nykoebing-falster": [("Giver solceller mere i Nykøbing Falster end i Jylland?", lambda: f"Lidt. PVGIS giver Nykøbing Falster ca. {tal(PV['nykoebing-falster']['syd'])} kWh pr. kWp om året mod fx {tal(PV['aarhus']['syd'])} kWh i Aarhus og {tal(PV['herning']['syd'])} kWh i Herning, for samme sydvendte tag på 35°. For et 6 kWp-anlæg er forskellen til Herning ca. {tal((PV['nykoebing-falster']['syd']-PV['herning']['syd'])*6)} kWh om året. Tagets retning og skygge betyder stadig mest.", ["pv_nykoebing-falster", "pv_aarhus", "pv_herning"])],
 "haderslev": [("Hvor meget giver solceller i Haderslev om vinteren?", lambda: f"PVGIS beregner ca. {tal(PV['haderslev']['months'][11]*6)} kWh i december og {tal(PV['haderslev']['months'][0]*6)} kWh i januar fra et 6 kWp-anlæg mod syd i Haderslev, mod ca. {tal(PV['haderslev']['months'][4]*6)} kWh i maj.", ["pv_haderslev"])],
})
VP_HEAT.update({
 "nykoebing-falster": ("Ingen naturgas, men mange oliefyr og elvarme i Guldborgsund",
   lambda: f"Danmarks Statistik registrerer ingen beboede parcel- og rækkehuse med naturgas i Guldborgsund Kommune. {hp('nykoebing-falster','FJ',1)} har fjernvarme, men {tal(HEAT['nykoebing-falster']['ELV'])} huse ({hp('nykoebing-falster','ELV',1)}) har <strong>elvarme</strong> og {tal(HEAT['nykoebing-falster']['CO'])} ({hp('nykoebing-falster','CO',1)}) har <strong>oliefyr</strong> – {rk(_ELVs, 'nykoebing-falster', 'højeste')} elvarmeandel og {rk(_hf('CO'), 'nykoebing-falster', 'højeste')} olieandel af de {nw()} byer, mod {hp('dk','ELV',1)} og {hp('dk','CO',1)} på landsplan. {tal(HEAT['nykoebing-falster']['VP'])} huse har allerede varmepumpe."),
 "haderslev": ("Fire ud af ti huse har fjernvarme, og hvert fjerde har naturgas",
   lambda: f"{hp('haderslev','FJ',1)} af de {tal(hs('haderslev'))} beboede parcel- og rækkehuse i Haderslev Kommune har fjernvarme, mod {hp('dk','FJ',1)} på landsplan, og {tal(HEAT['haderslev']['CN'])} ({hp('haderslev','CN',1)}) har naturgas. {tal(HEAT['haderslev']['CA'])} huse ({hp('haderslev','CA',1)}) har centralvarme med en anden kilde, fx træpiller, {rk(_CAs, 'haderslev', 'højeste')} andel af de {nw()} byer. {tal(HEAT['haderslev']['VP'])} har allerede varmepumpe."),
})
VP_HEAT_SRC_NEW.update({"nykoebing-falster": [], "haderslev": []})
VP_TOWNS.update({
 "nykoebing-falster": [("Nykøbing F., Ønslev, Eskilstrup", "Guldborgsund Varme, ca. 7.000 kunder (også Ovstrup, Gundslevmagle, Systofte)", ["gfo_varme"]),
                       ("Sakskøbing", "Eget værk: Sakskøbing Fjernvarmeselskab", ["ft_pris"]),
                       ("Nysted", "Eget værk: Nysted Varmeværk", ["ft_pris"]),
                       ("Nørre Alslev", "Eget værk: Nr. Alslev Fjernvarmeværk", ["ft_pris"]),
                       ("Stubbekøbing, Horbelev, Gedser", "REFA's tre fjernvarmeværker", ["ft_pris"]),
                       ("Mindre landsbyer", "Varmeplanen åbner for lokale energifællesskaber, ellers individuelle grønne løsninger", ["gul_vpl"])],
 "haderslev": [("Haderslev", "Haderslev Fjernvarme: gravearbejdet i udvidelsesområderne er afsluttet", ["hfv_tid"]),
               ("Starup", "Med i Haderslev Fjernvarmes udvidelse, 81 % tilslutning", ["hfv_gf25"]),
               ("Marstrup", "Fjernvarme betinget af 85 % frivillig tilslutning", ["had_fjv", "hfv_gf25"]),
               ("Vojens", "Vojens Fjernvarme: ca. 867 forbrugere, udrulning inden udgangen af 2026", ["had_vpl"]),
               ("Gram", "Gram Fjernvarme: udrulning forventet inden udgangen af 2023", ["had_fjv"]),
               ("Øvrige lokalbyer med naturgas", "Ingen fjernvarme fra de tre selskaber", ["had_fjv"])],
})
VP_TOWNS_NOTE.update({
 "nykoebing-falster": "Har du oliefyr eller elvarme i en landsby uden fjernvarme, så hør først, om der er et energifællesskab på vej. Ellers anbefaler kommunen en individuel grøn løsning, og Varmepumpepuljen kan give tilskud til at skifte oliefyr eller elvarme ud.",
 "haderslev": "Bor du i en lokalby med gasfyr, kommer fjernvarmen ikke. Ligger du derimod i et af udvidelsesområderne i Haderslev, Vojens eller Gram, så tal med fjernvarmeselskabet, før du køber varmepumpe. Kommunen advarer om, at for mange varmepumper kan forhindre fjernvarmen.",
})
VP_XFAQ.update({
 "nykoebing-falster": [("Hvor mange huse i Guldborgsund Kommune har elvarme eller oliefyr?", lambda: f"Danmarks Statistik registrerer {tal(HEAT['nykoebing-falster']['ELV'])} beboede parcel- og rækkehuse med elvarme og {tal(HEAT['nykoebing-falster']['CO'])} med oliefyr i 2026, ud af {tal(hs('nykoebing-falster'))}. {tal(HEAT['nykoebing-falster']['CA'])} har centralvarme med en anden kilde, og ingen har naturgas.", ["dst_bol102"])],
 "haderslev": [("Hvor mange huse i Haderslev Kommune har gasfyr?", lambda: f"{tal(HEAT['haderslev']['CN'])} af de {tal(hs('haderslev'))} beboede parcel- og rækkehuse ({hp('haderslev','CN',1)}) har naturgas ifølge Danmarks Statistik, 2026. {tal(HEAT['haderslev']['CO'])} har oliefyr, {tal(HEAT['haderslev']['ELV'])} elvarme og {tal(HEAT['haderslev']['VP'])} varmepumpe.", ["dst_bol102"])],
})
FV_SOURCES.update({
 "nykoebing-falster": [("I 2025 kom <strong>47,5 % af Guldborgsund Varmes brændsel fra overskudsvarme</strong>, 47,4 % fra træ og 5,1 % fra bioolie.", ["gfo_dekl25"]),
                       ("Andelen af <strong>vedvarende energi inkl. el</strong> var 100 % ifølge værkets fjernvarmedeklaration for 2025.", ["gfo_dekl25"])],
 "haderslev": [("Haderslev Fjernvarme startede i slutningen af 2024 <strong>prøvedrift på en varmepumpe, elkedler og en varmeakkumuleringstank</strong> ved Industri Langkær.", ["hfv_gf25"]),
               ("Udvidelsesprojektet blev godkendt i 2021 sammen med en <strong>11 MW varmepumpe</strong>, og det oprindelige budget lå på 272,6 mio. kr. plus ca. 80 mio. kr. til varmepumpen.", ["had_vpl", "hfv_gf25"])],
})
FV_SHARE.update({
 "nykoebing-falster": lambda: f"{hp('nykoebing-falster','FJ',1)} af de beboede parcel- og rækkehuse i Guldborgsund Kommune har fjernvarme, mod {hp('dk','FJ',1)} i hele landet. Der er ingen huse med naturgas, men {tal(HEAT['nykoebing-falster']['ELV'])} har elvarme og {tal(HEAT['nykoebing-falster']['CO'])} oliefyr.",
 "haderslev": lambda: f"{hp('haderslev','FJ',1)} af de beboede parcel- og rækkehuse i Haderslev Kommune har fjernvarme, mod {hp('dk','FJ',1)} i hele landet. {tal(HEAT['haderslev']['CN'])} huse har naturgas og {tal(HEAT['haderslev']['CO'])} oliefyr.",
})
FV_SOURCES_H.update({"nykoebing-falster": "Overskudsvarme og træ", "haderslev": "Varmepumpe, elkedler og akkumuleringstank i Langkær"})
_reg_age_old9 = reg_age_note
def reg_age_note(c, kommune):
    s = STOCK[c]; B = s["B"]; t = s["tot"]
    if c == "nykoebing-falster":
        return (f"{tal(B['før 1960'])} af de beboede huse i Guldborgsund Kommune ({pct(B['før 1960'], t)}) er bygget før 1960. Har dit ældre hus fladt tag eller ligger det i landzone, kræver solcellerne tilladelse, så tjek det, før du bestiller.", ["gul_faq"])
    if c == "haderslev":
        return (f"{tal(B['1960-1979'])} af de beboede huse i Haderslev Kommune ({pct(B['1960-1979'], t)}) er bygget i 1960-1979. Tjek lokalplanen for dit kvarter, som fx kan bestemme tagets farve og materiale, før du bestiller.", ["had_sol"])
    return _reg_age_old9(c, kommune)

# ---------- daglig by-rutine 4. nov. 2026: Frederikshavn (DK1, Region Nordjylland) og Hedensted (DK1, Region Midtjylland) ----------
_CEMs = lambda x: ROOF[x]["T"]["08"] / ROOF[x]["tot"]; _VPs = lambda x: HEAT[x]["VP"] / hs(x); _S6079 = lambda x: STOCK[x]["B"]["1960-1979"] / STOCK[x]["tot"]
SOL_ORDER.update({
 "frederikshavn": ["tage", "lokalt", "produktion", "boliger", "guides", "faq"],
 "hedensted": ["boliger", "produktion", "lokalt", "tage", "faq", "guides"],
})
VP_ORDER.update({
 "frederikshavn": ["lokale-byer", "opvarmning", "lokalt", "pris", "faq", "guides"],
 "hedensted": ["opvarmning", "lokalt", "pris", "lokale-byer", "faq", "guides"],
})
FV_ORDER.update({
 "frederikshavn": ["priser", "billigst", "status", "andel", "varmekilder", "faq"],
 "hedensted": ["status", "andel", "priser", "varmekilder", "billigst", "faq"],
})
SOL_PROD.update({
 "frederikshavn": ("Solproduktion i Frederikshavn: maj, juni og juli næsten lige gode",
   lambda: f"PVGIS beregner ca. {tal(PV['frederikshavn']['syd'])} kWh pr. kWp om året for et sydvendt tag med 35° hældning i Frederikshavn og ca. {tal(PV['frederikshavn']['opt'])} kWh ved den optimale hældning på {PV['frederikshavn']['opt_angle']}°. Et 6 kWp-anlæg giver ca. {tal(PV['frederikshavn']['syd']*6)} kWh om året. Maj, juni og juli giver ca. {tal(PV['frederikshavn']['months'][4]*6)}, {tal(PV['frederikshavn']['months'][5]*6)} og {tal(PV['frederikshavn']['months'][6]*6)} kWh, mens december kun giver ca. {tal(PV['frederikshavn']['months'][11]*6)} kWh."),
 "hedensted": ("Hvor meget giver solceller i Hedensted?",
   lambda: f"For et sydvendt tag med 35° hældning i Hedensted beregner PVGIS ca. {tal(PV['hedensted']['syd'])} kWh pr. kWp om året, og et 6 kWp-anlæg giver dermed ca. {tal(PV['hedensted']['syd']*6)} kWh. Vender taget mod øst eller vest, falder det til ca. {tal(PV['hedensted']['oest']*6)} og {tal(PV['hedensted']['vest']*6)} kWh, ca. {round(100*(1-PV['hedensted']['oest']/PV['hedensted']['syd']))} % mindre end mod syd. Den bedste måned er maj med ca. {tal(PV['hedensted']['months'][4]*6)} kWh."),
})
SOL_PROD_SRC_NEW.update({"frederikshavn": ["pv_frederikshavn", "pvo_frederikshavn", "pvv_frederikshavn"], "hedensted": ["pv_hedensted", "pvo_hedensted", "pvv_hedensted"]})
SOL_ROOF.update({
 "frederikshavn": ("Over fire ud af ti tage i Frederikshavn er fibercement",
   lambda: f"{rp('frederikshavn','06')} af parcel- og rækkehusene i Frederikshavn Kommune har tag af <strong>fibercement</strong>, {rk(_FIB, 'frederikshavn', 'højeste')} andel af de {nw()} byer, og {rp('frederikshavn','10')} har <strong>tegl</strong>. Ifølge Bolius indeholder bølge- og kunstskiferplader fra før 1984 næsten altid asbest, så få taget vurderet, før panelerne monteres. Har dit kvarter en lokalplan eller deklaration med regler om tagmaterialer eller refleksioner, kan solcellerne kræve dispensation.",
   ["dst_bygb50", "bolius_asb", "fre_sol"]),
 "hedensted": ("Cementsten er det mest udbredte tag i Hedensted",
   lambda: f"{rp('hedensted','08')} af parcel- og rækkehusene i Hedensted Kommune har tag af <strong>cementsten</strong>, {rk(_CEMs, 'hedensted', 'højeste')} andel af de {nw()} byer og mod {rp('dk','08')} i hele landet. {rp('hedensted','06')} har <strong>fibercement</strong> og {rp('hedensted','10')} <strong>tegl</strong>. Kommunen kræver, at panelerne følger tagets hældning og ikke er af reflekterende materiale, hvis du vil slippe for tilladelse.",
   ["dst_bygb50", "hed_sol"]),
})
SOL_HOMES.update({
 "frederikshavn": lambda: f"{pct(STOCK['frederikshavn']['B']['1960-1979'],STOCK['frederikshavn']['tot'])} af de {tal(STOCK['frederikshavn']['tot'])} beboede parcel- og rækkehuse i Frederikshavn Kommune er bygget i 1960-1979, {rk(_S6079, 'frederikshavn', 'højeste')} andel af de {nw()} byer, og kun {pct(STOCK['frederikshavn']['B']['2000+'],STOCK['frederikshavn']['tot'])} er fra 2000 eller senere. Frederikshavn by har {tal(town('frederikshavn','Frederikshavn'))} indbyggere, og siden gælder også Sæby ({tal(town('frederikshavn','Sæby'))}), Skagen ({tal(town('frederikshavn','Skagen'))}), Strandby ({tal(town('frederikshavn','Strandby'))}) og Ålbæk.",
 "hedensted": lambda: f"Hedensted Kommune har {tal(STOCK['hedensted']['tot'])} beboede parcel- og rækkehuse, og {pct(STOCK['hedensted']['B']['2000+'],STOCK['hedensted']['tot'])} af dem er bygget i 2000 eller senere, {rk(_NEW, 'hedensted', 'højeste')} andel af de {nw()} byer, mod {pct(STOCK['dk']['B']['2000+'],STOCK['dk']['tot'])} i hele landet. Hedensted by har {tal(town('hedensted','Hedensted'))} indbyggere, og siden gælder også Juelsminde ({tal(town('hedensted','Juelsminde'))}), Tørring ({tal(town('hedensted','Tørring'))}), Hornsyld ({tal(town('hedensted','Hornsyld'))}) og Uldum.",
})
SOL_HOMES_SRC_NEW.update({"frederikshavn": [], "hedensted": []})
SOL_HOMES_H.update({"frederikshavn": "Huse fra 1960'erne og 70'erne fra Frederikshavn til Skagen og Sæby", "hedensted": "Mange nyere huse i Hedensted, Juelsminde og Tørring"})
SOL_XFAQ.update({
 "frederikshavn": [("Hvor meget giver solceller i Frederikshavn om vinteren?", lambda: f"PVGIS beregner ca. {tal(PV['frederikshavn']['months'][11]*6)} kWh i december og {tal(PV['frederikshavn']['months'][0]*6)} kWh i januar fra et 6 kWp-anlæg mod syd i Frederikshavn, mod ca. {tal(PV['frederikshavn']['months'][4]*6)} kWh i maj.", ["pv_frederikshavn"])],
 "hedensted": [("Kan et øst-vest-tag betale sig i Hedensted?", lambda: f"Det giver mindre end et sydvendt tag: PVGIS beregner ca. {tal(PV['hedensted']['oest'])} kWh pr. kWp mod øst og {tal(PV['hedensted']['vest'])} kWh mod vest i Hedensted, mod {tal(PV['hedensted']['syd'])} kWh mod syd. Øst og vest giver næsten det samme, så panelerne kan deles på begge tagflader.", ["pv_hedensted", "pvo_hedensted", "pvv_hedensted"])],
})
VP_HEAT.update({
 "frederikshavn": ("Næsten to ud af tre huse i Frederikshavn har fjernvarme",
   lambda: f"{hp('frederikshavn','FJ',1)} af de {tal(hs('frederikshavn'))} beboede parcel- og rækkehuse i Frederikshavn Kommune har fjernvarme, mod {hp('dk','FJ',1)} på landsplan. {tal(HEAT['frederikshavn']['CN'])} huse ({hp('frederikshavn','CN',1)}) har naturgas, især i de byer, kommunen har udlagt til naturgas, og {tal(HEAT['frederikshavn']['CO'])} ({hp('frederikshavn','CO',1)}) har oliefyr. {tal(HEAT['frederikshavn']['VP'])} har allerede varmepumpe."),
 "hedensted": ("Hvert femte hus har varmepumpe, og hvert femte har naturgas",
   lambda: f"{tal(HEAT['hedensted']['VP'])} af de {tal(hs('hedensted'))} beboede parcel- og rækkehuse i Hedensted Kommune ({hp('hedensted','VP',1)}) har allerede varmepumpe, {rk(_VPs, 'hedensted', 'højeste')} andel af de {nw()} byer, mod {hp('dk','VP',1)} på landsplan. {tal(HEAT['hedensted']['CN'])} ({hp('hedensted','CN',1)}) har naturgas og kun {hp('hedensted','FJ',1)} fjernvarme. {tal(HEAT['hedensted']['CA'])} huse har centralvarme med en anden kilde, fx træpiller."),
})
VP_HEAT_SRC_NEW.update({"frederikshavn": ["fre_scr"], "hedensted": []})
VP_TOWNS.update({
 "frederikshavn": [("Frederikshavn og Kilden", "Frederikshavn Varme; ringledningen kan også forsyne Gærum (drift ultimo 2026)", ["fre_scr", "ffv_aar25"]),
                   ("Skagen", "Skagen Varmeværk; havnen, Højen og en stor del af nordbyen var naturgasområder i 2022", ["fre_scr"]),
                   ("Sæby", "Sæby Varmeværk; hele byen er fjernvarmeområde undtagen et erhvervsområde", ["fre_scr"]),
                   ("Strandby og Elling", "Strandby Varmeværk; projektforslag om fjernvarme til Elling godkendt i 2022", ["fre_scr"]),
                   ("Østervrå, Thorshøj, Hørby, Dybvad, Voerså", "Egne varmeværker", ["fre_scr"]),
                   ("Ålbæk, Jerup, Kvissel, Ravnshøj", "Naturgas-byer uden fjernvarmeplaner i 2022; omstilling senest i 2035", ["fre_scr"])],
 "hedensted": [("Hedensted og Daugård", "Hedensted Fjernvarme; Daugård-projektet med 330 nye forbrugere", ["hed_fjv", "df_daug"]),
               ("Hornsyld", "Hornsyld Klimavarme", ["hed_fjv"]),
               ("Løsning", "Løsning Fjernvarme", ["hed_fjv"]),
               ("Rask Mølle og Uldum", "Rask Mølle Uldum Forsyning", ["hed_fjv"]),
               ("Tørring og Ølholm", "Tørring Kraftvarmeværk", ["hed_fjv", "ft_pris"]),
               ("Øvrige byer og landområder", "Tre af fire byområder fra varmeplanen 2022 er taget ud; borgerne kan selv arbejde for fjernvarme", ["hed_red"])],
})
VP_TOWNS_NOTE.update({
 "frederikshavn": "Bor du i en af naturgas-byerne som Ålbæk eller Jerup, kommer fjernvarmen efter kommunens screening ikke foreløbig, og gasfyret skal senest i 2035 erstattes. Bor du i Gærum, så hør Frederikshavn Forsyning om ringledningen, før du køber varmepumpe.",
 "hedensted": "Har du gasfyr i en by uden fjernvarmeprojekt, er en varmepumpe den løsning, flest i kommunen allerede har valgt. Bor du nær et af de fem fjernvarmeselskaber, så spørg først, om dit område er udlagt eller planlagt til fjernvarme, fordi det også afgør, om du kan få tilskud fra Varmepumpepuljen.",
})
VP_XFAQ.update({
 "frederikshavn": [("Hvor mange huse i Frederikshavn Kommune har gasfyr?", lambda: f"{tal(HEAT['frederikshavn']['CN'])} af de {tal(hs('frederikshavn'))} beboede parcel- og rækkehuse ({hp('frederikshavn','CN',1)}) har naturgas ifølge Danmarks Statistik, 2026. {tal(HEAT['frederikshavn']['CO'])} har oliefyr, {tal(HEAT['frederikshavn']['ELV'])} elvarme og {tal(HEAT['frederikshavn']['VP'])} varmepumpe.", ["dst_bol102"])],
 "hedensted": [("Hvor mange huse i Hedensted Kommune har varmepumpe?", lambda: f"Danmarks Statistik registrerer {tal(HEAT['hedensted']['VP'])} beboede parcel- og rækkehuse med varmepumpe i 2026, ud af {tal(hs('hedensted'))}. {tal(HEAT['hedensted']['CN'])} har naturgas, {tal(HEAT['hedensted']['CO'])} oliefyr og {tal(HEAT['hedensted']['FJ'])} fjernvarme.", ["dst_bol102"])],
})
FV_SOURCES.update({
 "frederikshavn": [("<strong>Affaldskraftvarmeværket</strong> står for ca. 30 % af varmen til Frederikshavn Varmes kunder og <strong>varmepumpen</strong> på Vendsysselvej for ca. 35 %.", ["ffv_varme"]),
                   ("I 2025 blev en <strong>20 MW elkedel</strong> og en akkumuleringstank på 7.400 m³ færdige, så billig strøm kan lagres som varme og naturgaskedlerne bruges mindre.", ["ffv_aar25"])],
 "hedensted": [("En <strong>4 MW spildevandsvarmepumpe</strong> skal fra 2027 levere ca. 20.000 MWh om året, mere end en fjerdedel af den varme, Hedensted Fjernvarme leverer.", ["hfj_spild"]),
               ("Træflis og træpiller skal komme fra <strong>ansvarligt skovbrug</strong> og overholde Energistyrelsens bæredygtighedskrav.", ["hfj_miljo"])],
})
FV_SHARE.update({
 "frederikshavn": lambda: f"{hp('frederikshavn','FJ',1)} af de beboede parcel- og rækkehuse i Frederikshavn Kommune har fjernvarme, mod {hp('dk','FJ',1)} i hele landet. {tal(HEAT['frederikshavn']['CN'])} huse har naturgas og {tal(HEAT['frederikshavn']['CO'])} oliefyr.",
 "hedensted": lambda: f"{hp('hedensted','FJ',1)} af de beboede parcel- og rækkehuse i Hedensted Kommune har fjernvarme, mod {hp('dk','FJ',1)} i hele landet. {tal(HEAT['hedensted']['CN'])} huse har naturgas, og {tal(HEAT['hedensted']['VP'])} har allerede varmepumpe.",
})
FV_SOURCES_H.update({"frederikshavn": "Affaldsvarme, varmepumpe og ny elkedel", "hedensted": "Spildevandsvarmepumpe fra 2027"})
_reg_age_old10 = reg_age_note
def reg_age_note(c, kommune):
    s = STOCK[c]; B = s["B"]; t = s["tot"]
    if c == "frederikshavn":
        return (f"{tal(B['1960-1979'])} af de beboede huse i Frederikshavn Kommune ({pct(B['1960-1979'], t)}) er bygget i 1960-1979. Tjek, om lokalplanen eller en tinglyst deklaration for dit kvarter har regler om tagmaterialer eller refleksioner, før du bestiller.", ["fre_sol"])
    if c == "hedensted":
        return (f"{tal(B['2000+'])} af de beboede huse i Hedensted Kommune ({pct(B['2000+'], t)}) er bygget i 2000 eller senere. Tjek servitutterne og lokalplanen for dit kvarter, før du bestiller, fordi de kan sætte andre regler end kommunens hovedregel.", ["hed_sol"])
    return _reg_age_old10(c, kommune)

# ---------- keyword-backlog 4. nov. 2026 (GSC 25.-31.10): 'luft til luft varmepumpe vejle' og 'varmepumpe horsens' ----------
VP_HEAT.update({
 "vejle": ("Varmepumpe i Vejle: luft til vand eller luft til luft?",
   lambda: f"{tal(HEAT['vejle']['VP'])} beboede parcel- og rækkehuse i Vejle Kommune varmes op med varmepumpe. Det er {hp('vejle','VP',1)} og {rk(lambda x: HEAT[x]['VP'] / hs(x), 'vejle', 'højeste')} andel af de {nw()} byer, mod {hp('dk','VP',1)} på landsplan. Samtidig har {tal(HEAT['vejle']['CN']+HEAT['vejle']['CO'])} huse stadig gas- eller oliefyr, og det er dem, kommunens fjernvarmeudrulning frem mod 2028 handler om. {tal(HEAT['vejle']['ELV'])} huse har elvarme: har du elpaneler og ingen radiatorer med vand, er en <a href=\"/varmepumpe/luft-til-luft/\">luft til luft-varmepumpe</a> det billigste sted at starte, ca. 12.000-25.000 kr. ifølge Energisparer.dk, men den giver ikke tilskud fra Varmepumpepuljen."),
 "horsens": ("Luft til vand-varmepumpe i Horsens: hvem står uden for fjernvarmen?",
   lambda: f"{hp('horsens','FJ')} af de beboede parcel- og rækkehuse i Horsens Kommune har fjernvarme efter Fjernvarme Horsens' store udbygning. {tal(HEAT['horsens']['VP'])} huse har allerede varmepumpe, mens {tal(HEAT['horsens']['CN'])} stadig har naturgas, {tal(HEAT['horsens']['CO'])} oliefyr og {tal(HEAT['horsens']['ELV'])} elvarme. Det er de ca. {tal(HEAT['horsens']['CN']+HEAT['horsens']['CO']+HEAT['horsens']['ELV'])} huse, en luft til vand-varmepumpe i Horsens er mest relevant for, hvis de ligger uden for fjernvarmeområdet."),
})
VP_HEAT_SRC_NEW.update({"vejle": ["es_vp", "se_l2l", "se_vpp"], "horsens": ["hor_fv"]})
VP_XFAQ["vejle"] = VP_XFAQ["vejle"] + [("Hvad koster en luft til luft-varmepumpe i Vejle?", lambda: "Vi har ikke fundet kilder med en særlig Vejle-pris. Energisparer.dk angiver ca. 12.000-25.000 kr. inkl. montering, og SparEnergi 15.000-30.000 kr. Prisen afhænger især af antallet af indedele. Der er ikke tilskud fra Varmepumpepuljen til luft til luft, men du kan få håndværkerfradrag for arbejdslønnen.", ["es_vp", "se_l2l", "se_vpp", "hvfradrag"])]
VP_XFAQ["horsens"] = VP_XFAQ["horsens"] + [("Hvornår giver en varmepumpe mening i Horsens?", lambda: f"Når huset ligger uden for fjernvarmeområdet og i dag varmes op med olie, gas eller elvarme. Det gælder ca. {tal(HEAT['horsens']['CN']+HEAT['horsens']['CO']+HEAT['horsens']['ELV'])} beboede parcel- og rækkehuse i Horsens Kommune ifølge Danmarks Statistik. Tjek først din adresse hos Fjernvarme Horsens eller på Plandata.dk.", ["dst_bol102", "hor_fv", "plandata"])]

# ---------- daglig by-rutine 5. nov. 2026: Ringkøbing (DK1, Ringkøbing-Skjern Kommune) og Helsingør (DK2, Region Hovedstaden) ----------
_COs = lambda x: HEAT[x]["CO"] / hs(x); _CNs = lambda x: HEAT[x]["CN"] / hs(x); _RKs = lambda x: STOCK[x]["raekke"] / STOCK[x]["tot"]; _FLs = lambda x: (ROOF[x]["T"]["02"] + ROOF[x]["T"]["04"]) / ROOF[x]["tot"]; _FIBs = lambda x: ROOF[x]["T"]["06"] / ROOF[x]["tot"]
SOL_ORDER.update({
 "ringkoebing": ["lokalt", "tage", "boliger", "produktion", "faq", "guides"],
 "helsingoer": ["boliger", "lokalt", "tage", "produktion", "guides", "faq"],
})
VP_ORDER.update({
 "ringkoebing": ["lokalt", "opvarmning", "lokale-byer", "pris", "guides", "faq"],
 "helsingoer": ["lokale-byer", "lokalt", "opvarmning", "faq", "pris", "guides"],
})
FV_ORDER.update({
 "ringkoebing": ["billigst", "priser", "varmekilder", "status", "andel", "faq"],
 "helsingoer": ["andel", "status", "billigst", "priser", "faq", "varmekilder"],
})
SOL_PROD.update({
 "ringkoebing": ("Vestkystsol: hvad giver et anlæg i Ringkøbing?",
   lambda: f"PVGIS beregner ca. {tal(PV['ringkoebing']['syd'])} kWh pr. kWp om året for et sydvendt tag med 35° hældning i Ringkøbing og ca. {tal(PV['ringkoebing']['opt'])} kWh ved den optimale hældning på {PV['ringkoebing']['opt_angle']}°. Et 6 kWp-anlæg giver dermed ca. {tal(PV['ringkoebing']['syd']*6)} kWh om året, heraf ca. {tal(sum(PV['ringkoebing']['months'][3:8])*6)} kWh i april-august. Kommuneplanen kræver, at panelerne har samme hældning som taget, så det er tagets egen vinkel, der afgør produktionen."),
 "helsingoer": ("Hvor meget strøm giver solceller i Helsingør?",
   lambda: f"I Helsingør beregner PVGIS ca. {tal(PV['helsingoer']['syd'])} kWh pr. kWp om året for et sydvendt tag med 35° hældning, så et 6 kWp-anlæg giver ca. {tal(PV['helsingoer']['syd']*6)} kWh. Mod øst giver det samme anlæg ca. {tal(PV['helsingoer']['oest']*6)} kWh og mod vest ca. {tal(PV['helsingoer']['vest']*6)} kWh. Fra november til januar falder produktionen til ca. {tal((PV['helsingoer']['months'][10]+PV['helsingoer']['months'][11]+PV['helsingoer']['months'][0])*6)} kWh i alt."),
})
SOL_PROD_SRC_NEW.update({"ringkoebing": ["pv_ringkoebing", "rks_kp"], "helsingoer": ["pv_helsingoer", "pvo_helsingoer", "pvv_helsingoer"]})
SOL_ROOF.update({
 "ringkoebing": ("Fibercement, cementsten og tegl: tagene i Ringkøbing-Skjern",
   lambda: f"{rp('ringkoebing','06')} af parcel- og rækkehusene i Ringkøbing-Skjern Kommune har tag af <strong>fibercement</strong>, {rk(_FIBs, 'ringkoebing', 'højeste')} andel af de {nw()} byer, mens {rp('ringkoebing','08')} har <strong>cementsten</strong> og {rp('ringkoebing','10')} <strong>tegl</strong>. Ifølge Bolius indeholder bølge- og kunstskiferplader fra før 1984 næsten altid asbest, så få taget vurderet, før panelerne skal nedfældes i tagfladen, som kommuneplanen kræver.",
   ["dst_bygb50", "bolius_asb", "rks_kp"]),
 "helsingoer": ("Mange flade tage og tagpap i Helsingør",
   lambda: f"{pct(ROOF['helsingoer']['T']['02'] + ROOF['helsingoer']['T']['04'], ROOF['helsingoer']['tot'])} af parcel- og rækkehusene i Helsingør Kommune har fladt tag eller tagpap, {rk(_FLs, 'helsingoer', 'højeste')} andel af de {nw()} byer, mod {pct(ROOF['dk']['T']['02'] + ROOF['dk']['T']['04'], ROOF['dk']['tot'])} på landsplan. {rp('helsingoer','10')} har <strong>tegl</strong> og {rp('helsingoer','06')} <strong>fibercement</strong>. På et fladt tag kommer panelerne typisk på stativ, og så skal anlægget stadig overholde byggerettens højde- og afstandsbestemmelser for at være undtaget for byggetilladelse.",
   ["dst_bygb50", "hel_sol"]),
})
SOL_HOMES.update({
 "ringkoebing": lambda: f"Ringkøbing-Skjern Kommune har {tal(STOCK['ringkoebing']['tot'])} beboede parcel- og rækkehuse, og {pct(STOCK['ringkoebing']['B']['før 1960'],STOCK['ringkoebing']['tot'])} af dem er bygget før 1960, mod {pct(STOCK['dk']['B']['før 1960'],STOCK['dk']['tot'])} i hele landet. Byerne er spredt: Ringkøbing har {tal(town('ringkoebing','Ringkøbing'))} indbyggere, Skjern {tal(town('ringkoebing','Skjern'))}, Videbæk {tal(town('ringkoebing','Videbæk'))}, Tarm {tal(town('ringkoebing','Tarm'))} og Hvide Sande {tal(town('ringkoebing','Hvide Sande'))}, og siden gælder hele kommunen.",
 "helsingoer": lambda: f"{pct(STOCK['helsingoer']['raekke'],STOCK['helsingoer']['tot'])} af de {tal(STOCK['helsingoer']['tot'])} beboede parcel- og rækkehuse i Helsingør Kommune er række-, kæde- eller dobbelthuse, {rk(_RKs, 'helsingoer', 'højeste')} andel af de {nw()} byer, og {pct(STOCK['helsingoer']['ejer'],STOCK['helsingoer']['tot'])} bebos af ejeren. Helsingør-byområdet har {tal(town('helsingoer','Helsingør-byområdet (inkl. Espergærde)'))} indbyggere, og siden gælder også Hellebæk ({tal(town('helsingoer','Hellebæk'))}), Hornbæk-Dronningmølle ({tal(town('helsingoer','Hornbæk-Dronningmølle'))}), Saunte og Kvistgård.",
})
SOL_HOMES_SRC_NEW.update({"ringkoebing": [], "helsingoer": []})
SOL_HOMES_H.update({"ringkoebing": "Ældre huse fra Ringkøbing og Skjern til Hvide Sande", "helsingoer": "Mange rækkehuse i Helsingør, Espergærde og Hornbæk"})
SOL_XFAQ.update({
 "ringkoebing": [("Hvor meget giver solceller i Ringkøbing om sommeren?", lambda: f"PVGIS beregner ca. {tal(PV['ringkoebing']['months'][4]*6)} kWh i maj, {tal(PV['ringkoebing']['months'][5]*6)} kWh i juni og {tal(PV['ringkoebing']['months'][6]*6)} kWh i juli fra et 6 kWp-anlæg mod syd i Ringkøbing, mod ca. {tal(PV['ringkoebing']['months'][11]*6)} kWh i december.", ["pv_ringkoebing"])],
 "helsingoer": [("Kan solceller på et rækkehus i Helsingør kræve tilladelse?", lambda: "Rækkehuse er omfattet af samme undtagelse som enfamiliehuse, når byggerettens højde- og afstandsbestemmelser og de brandmæssige løsninger er overholdt. Ligger rækkehusene i en bebyggelse med lokalplan eller deklaration, kan den kræve ikke-reflekterende paneler, så tjek den først, og spørg evt. grundejerforeningen.", ["hel_sol"])],
})
VP_HEAT.update({
 "ringkoebing": ("Tre ud af fem huse har fjernvarme, men oliefyrene er mange",
   lambda: f"{hp('ringkoebing','FJ',1)} af de {tal(hs('ringkoebing'))} beboede parcel- og rækkehuse i Ringkøbing-Skjern Kommune har fjernvarme, mod {hp('dk','FJ',1)} på landsplan. {tal(HEAT['ringkoebing']['CO'])} huse ({hp('ringkoebing','CO',1)}) har stadig oliefyr, {rk(_COs, 'ringkoebing', 'højeste')} andel af de {nw()} byer, og {tal(HEAT['ringkoebing']['CN'])} har naturgas. {tal(HEAT['ringkoebing']['VP'])} har allerede varmepumpe, og {tal(HEAT['ringkoebing']['CA'])} har centralvarme med en anden kilde, fx træpiller."),
 "helsingoer": ("Flere huse har naturgas end fjernvarme i Helsingør",
   lambda: f"{tal(HEAT['helsingoer']['CN'])} af de {tal(hs('helsingoer'))} beboede parcel- og rækkehuse i Helsingør Kommune ({hp('helsingoer','CN',1)}) har naturgas, {rk(_CNs, 'helsingoer', 'højeste')} andel af de {nw()} byer og mod {hp('dk','CN',1)} på landsplan. Kun {hp('helsingoer','FJ',1)} har fjernvarme. {tal(HEAT['helsingoer']['ELV'])} huse har elvarme og {tal(HEAT['helsingoer']['VP'])} varmepumpe."),
})
VP_HEAT_SRC_NEW.update({"ringkoebing": [], "helsingoer": ["fh_nye"]})
VP_TOWNS.update({
 "ringkoebing": [("Ringkøbing", "Ringkøbing Fjernvarme; nyt flisværk med absorptionsvarmepumpe", ["df_rfv"]),
                 ("Hvide Sande", "Hvide Sande Fjernvarme; egne vindmøller, landets laveste varmepris", ["df_hsfv"]),
                 ("Skjern, Tarm, Videbæk, Lem, Spjald, Tim", "Egne værker med vidt forskellige priser", ["ft_pris"]),
                 ("Fjelstervang", "Taget ud som muligt fjernvarmeområde i juni 2026", ["rks_fjel"]),
                 ("Hee, Stauning, Ølstrup, No, Vorgod-Barde m.fl.", "Kommunens varmescreeninger af landsbyerne", ["rks_varme"]),
                 ("Det åbne land", "Ingen fjernvarme; individuelle løsninger eller små fællesanlæg", ["rks_svp"])],
 "helsingoer": [("Søhelte-kvarteret", "Konverteret fra gas til fjernvarme; færdigt", ["fh_status"]),
                ("Marienlyst-kvarteret", "Anlægsarbejdet under afslutning (sep. 2026)", ["fh_status"]),
                ("Helsingør Bykerne og Yderområder", "Anlæg i gang; Yderområde 3 projekteres, 4 har fået tilbud i 2026", ["fh_status"]),
                ("Espergærde C", "Udbygning 2023-2028, kræver mindst 60 % tilslutning", ["fh_esp"]),
                ("Hornbæk", "Hornbæk Fjernvarme", ["ft_pris"]),
                ("Snekkersten og øvrige dele af Helsingør og Espergærde", "Kommende planer, tidligst efter 2028", ["fh_nye"])],
})
VP_TOWNS_NOTE.update({
 "ringkoebing": "Har du oliefyr i en landsby eller i det åbne land, er en luft til vand-varmepumpe det typiske valg, fordi kommunens varmeplan ikke peger på fjernvarme dér. Bor du i en af de landsbyer, kommunen har screenet, så læs screeningen for din by og hør borgerforeningen, før du køber, fordi det også afgør, om du kan få tilskud fra Varmepumpepuljen.",
 "helsingoer": "Har du gasfyr i et af de fem godkendte områder, så tjek først tilbuddet fra Forsyning Helsingør. Ligger huset uden for både de godkendte og de kommende områder, er en luft til vand-varmepumpe det realistiske alternativ, når gasfyret skal skiftes.",
})
VP_XFAQ.update({
 "ringkoebing": [("Hvor mange huse i Ringkøbing-Skjern Kommune har oliefyr?", lambda: f"{tal(HEAT['ringkoebing']['CO'])} af de {tal(hs('ringkoebing'))} beboede parcel- og rækkehuse ({hp('ringkoebing','CO',1)}) har oliefyr ifølge Danmarks Statistik, 2026. {tal(HEAT['ringkoebing']['CN'])} har naturgas, {tal(HEAT['ringkoebing']['ELV'])} elvarme og {tal(HEAT['ringkoebing']['VP'])} varmepumpe.", ["dst_bol102"])],
 "helsingoer": [("Hvor mange huse i Helsingør Kommune har gasfyr?", lambda: f"Danmarks Statistik registrerer {tal(HEAT['helsingoer']['CN'])} beboede parcel- og rækkehuse med naturgas i 2026, ud af {tal(hs('helsingoer'))}. {tal(HEAT['helsingoer']['FJ'])} har fjernvarme, {tal(HEAT['helsingoer']['ELV'])} elvarme og {tal(HEAT['helsingoer']['VP'])} varmepumpe.", ["dst_bol102"])],
})
FV_SOURCES.update({
 "ringkoebing": [("Hvide Sande Fjernvarme laver <strong>95 % af varmen</strong> med solvarme, elkedler og varmepumper, og strømmen kommer det meste af tiden fra værkets tre egne vindmøller på havnen.", ["df_hsfv"]),
                 ("Ringkøbing Fjernvarmes nye <strong>fliskedel og absorptionsvarmepumpe</strong> skal ifølge værket få naturgassens andel af el- og varmeproduktionen ned på ca. 8 %. Om sommeren kører værket kun på solvarme.", ["df_rfv"])],
 "helsingoer": [("Forsyning Helsingør oplyser, at <strong>88 % af varmen</strong> kommer fra vedvarende energi.", ["fh_nye"]),
                ("Prisen hos Forsyning Helsingør er ifølge selskabet selv, med inflationen regnet med, <strong>lavere end for ti år siden</strong>.", ["fh_pris"])],
})
FV_SHARE.update({
 "ringkoebing": lambda: f"{hp('ringkoebing','FJ',1)} af de beboede parcel- og rækkehuse i Ringkøbing-Skjern Kommune har fjernvarme, mod {hp('dk','FJ',1)} i hele landet. {tal(HEAT['ringkoebing']['CO'])} huse har oliefyr og {tal(HEAT['ringkoebing']['CN'])} naturgas.",
 "helsingoer": lambda: f"Kun {hp('helsingoer','FJ',1)} af de beboede parcel- og rækkehuse i Helsingør Kommune har fjernvarme, mod {hp('dk','FJ',1)} i hele landet, mens {hp('helsingoer','CN',1)} har naturgas. Det er de huse, Forsyning Helsingørs udbygning handler om.",
})
FV_SOURCES_H.update({"ringkoebing": "Vindmøller, solvarme og nyt flisværk", "helsingoer": "88 % vedvarende energi"})
_reg_age_old11 = reg_age_note
def reg_age_note(c, kommune):
    s = STOCK[c]; B = s["B"]; t = s["tot"]
    if c == "ringkoebing":
        return (f"{tal(B['før 1960'])} af de beboede huse i Ringkøbing-Skjern Kommune ({pct(B['før 1960'], t)}) er bygget før 1960. Ligger dit hus i Ringkøbings indre by eller ved Vedersø Klit, så tjek den bevarende lokalplan, før du bestiller.", ["rks_kp"])
    if c == "helsingoer":
        return (f"{tal(s['raekke'])} af de beboede huse i Helsingør Kommune ({pct(s['raekke'], t)}) er række-, kæde- eller dobbelthuse. Tjek lokalplanen eller deklarationen for din bebyggelse, fordi den kan kræve ikke-reflekterende paneler.", ["hel_sol"])
    return _reg_age_old11(c, kommune)

# ---------- daglig by-rutine 6. nov. 2026: Stenløse (DK2, Egedal) og Frederikssund (DK2) ----------
SOL_ORDER.update({
 "stenloese": ["lokalt", "boliger", "tage", "produktion", "faq", "guides"],
 "frederikssund": ["produktion", "lokalt", "boliger", "tage", "guides", "faq"],
})
VP_ORDER.update({
 "stenloese": ["lokalt", "opvarmning", "lokale-byer", "pris", "faq", "guides"],
 "frederikssund": ["opvarmning", "lokalt", "lokale-byer", "pris", "guides", "faq"],
})
FV_ORDER.update({
 "stenloese": ["status", "priser", "andel", "billigst", "varmekilder", "faq"],
 "frederikssund": ["andel", "status", "priser", "billigst", "faq", "varmekilder"],
})
SOL_PROD.update({
 "stenloese": ("Hvor meget strøm giver solceller i Stenløse?",
   lambda: f"I Stenløse beregner PVGIS ca. {tal(PV['stenloese']['syd'])} kWh pr. kWp om året for et sydvendt tag med 35° hældning, så et 6 kWp-anlæg giver ca. {tal(PV['stenloese']['syd']*6)} kWh. Mod øst giver det samme anlæg ca. {tal(PV['stenloese']['oest']*6)} kWh og mod vest ca. {tal(PV['stenloese']['vest']*6)} kWh. Fra november til januar falder produktionen til ca. {tal((PV['stenloese']['months'][10]+PV['stenloese']['months'][11]+PV['stenloese']['months'][0])*6)} kWh i alt."),
 "frederikssund": ("Solcellernes produktion i Frederikssund måned for måned",
   lambda: f"PVGIS beregner ca. {tal(PV['frederikssund']['syd'])} kWh pr. kWp om året for et sydvendt tag med 35° hældning i Frederikssund. Et 6 kWp-anlæg giver ca. {tal(PV['frederikssund']['syd']*6)} kWh om året, heraf ca. {tal(PV['frederikssund']['months'][5]*6)} kWh i juni og kun ca. {tal(PV['frederikssund']['months'][11]*6)} kWh i december."),
})
SOL_PROD_SRC_NEW.update({"stenloese": ["pv_stenloese", "pvo_stenloese", "pvv_stenloese"], "frederikssund": ["pv_frederikssund", "pvgis"]})
SOL_ROOF.update({
 "stenloese": ("Fibercement og cementsten: tagene i Egedal",
   lambda: f"{rp('stenloese','06')} af parcel- og rækkehusene i Egedal Kommune har tag af <strong>fibercement</strong>, og {rp('stenloese','08')} har <strong>cementsten</strong> – de to største tagtyper. {rp('stenloese','10')} har tegl. Ifølge Bolius indeholder bølge- og kunstskiferplader fra før 1984 næsten altid asbest, så få taget vurderet, før panelerne monteres.",
   ["dst_bygb50", "bolius_asb"]),
 "frederikssund": ("Fibercement, cementsten og tegl i Frederikssund",
   lambda: f"{rp('frederikssund','06')} af parcel- og rækkehusene i Frederikssund Kommune har <strong>fibercement</strong>, {rp('frederikssund','08')} <strong>cementsten</strong> og {rp('frederikssund','10')} <strong>tegl</strong>. De tre typer dækker tilsammen over fire ud af fem tage. Få tagets restlevetid vurderet, før du monterer solceller.",
   ["dst_bygb50", "bolius_asb"]),
})
SOL_HOMES.update({
 "stenloese": lambda: f"Egedal Kommune har {tal(STOCK['stenloese']['tot'])} beboede parcel- og rækkehuse, og {pct(STOCK['stenloese']['B']['1960-1979'],STOCK['stenloese']['tot'])} af dem er bygget 1960-1979 – mere end hvert andet hus. Ølstykke-Stenløse har {tal(town('stenloese','Ølstykke-Stenløse'))} indbyggere, Smørumnedre {tal(town('stenloese','Smørumnedre'))}, Ganløse {tal(town('stenloese','Ganløse'))} og Veksø {tal(town('stenloese','Veksø'))}. Siden gælder hele kommunen.",
 "frederikssund": lambda: f"Frederikssund Kommune har {tal(STOCK['frederikssund']['tot'])} beboede parcel- og rækkehuse, og {pct(STOCK['frederikssund']['ejer'],STOCK['frederikssund']['tot'])} bebos af ejeren. Frederikssund by har {tal(town('frederikssund','Frederikssund'))} indbyggere, Slangerup {tal(town('frederikssund','Slangerup'))}, Jægerspris {tal(town('frederikssund','Jægerspris'))} og Skibby {tal(town('frederikssund','Skibby'))}. Siden gælder hele kommunen.",
})
SOL_HOMES_SRC_NEW.update({"stenloese": [], "frederikssund": []})
SOL_HOMES_H.update({"stenloese": "Mange huse fra 1960'erne og 1970'erne i Egedal", "frederikssund": "Fra Frederikssund by til Slangerup og Skibby"})
SOL_XFAQ.update({
 "stenloese": [("Hvor meget giver solceller i Stenløse om sommeren?", lambda: f"PVGIS beregner ca. {tal(PV['stenloese']['months'][4]*6)} kWh i maj, {tal(PV['stenloese']['months'][5]*6)} kWh i juni og {tal(PV['stenloese']['months'][6]*6)} kWh i juli fra et 6 kWp-anlæg mod syd, mod ca. {tal(PV['stenloese']['months'][11]*6)} kWh i december.", ["pv_stenloese"])],
 "frederikssund": [("Skal solceller på et hus i landzone ved Jægerspris have tilladelse?", lambda: "På hustaget gælder samme BR18-regler som i byen, men lokalplan, servitut og beskyttelseslinjer kan kræve dispensation. Fritstående anlæg i landzone kan også kræve landzonetilladelse. Tjek kommunens digitale kort.", ["frs_sol"])],
})
VP_HEAT.update({
 "stenloese": ("Flere huse har naturgas end fjernvarme i Egedal",
   lambda: f"{tal(HEAT['stenloese']['CN'])} af de {tal(hs('stenloese'))} beboede parcel- og rækkehuse i Egedal Kommune ({hp('stenloese','CN',1)}) har naturgas – flere end dem med fjernvarme ({hp('stenloese','FJ',1)}). {tal(HEAT['stenloese']['VP'])} har allerede varmepumpe, {tal(HEAT['stenloese']['ELV'])} elvarme og {tal(HEAT['stenloese']['CO'])} oliefyr."),
 "frederikssund": ("Næsten fire ud af ti huse har gasfyr i Frederikssund",
   lambda: f"{tal(HEAT['frederikssund']['CN'])} beboede parcel- og rækkehuse i Frederikssund Kommune ({hp('frederikssund','CN',1)}) har naturgas, mens kun {hp('frederikssund','FJ',1)} har fjernvarme. {tal(HEAT['frederikssund']['VP'])} har varmepumpe ({hp('frederikssund','VP',1)}), {tal(HEAT['frederikssund']['ELV'])} elvarme og {tal(HEAT['frederikssund']['CO'])} oliefyr."),
})
VP_HEAT_SRC_NEW.update({"stenloese": ["ege_fv"], "frederikssund": ["frs_klima"]})
VP_TOWNS.update({
 "stenloese": [("Ølstykke-Stenløse", "Egedal Fjernvarme udbygger i etape 11-20; kampagnepris ved tidlig tilmelding", ["ege_fv"]),
               ("Smørumnedre", "Smørum Kraftvarme blandt landets billigste værker", ["ft_pris"]),
               ("Slagslunde", "Eget fjernvarmeværk i Forsyningstilsynets statistik", ["ft_pris"]),
               ("Ganløse / Veksø", "Tjek om din adresse er med i udbygningen; ellers er varmepumpe alternativet", ["ege_fv"])],
 "frederikssund": [("Frederikssund by", "Vestforbrænding: fjernvarme forventet senest 2030; energicentral 2028", ["frs_klima", "vf_energi"]),
                   ("Græse Bakkeby / Vinge / St. Rørbæk", "Samme 2030-forventning som byen", ["frs_klima"]),
                   ("Jægerspris", "Eget kraftvarmeværk; allerede elkedler og varmepumper i produktionen", ["frs_klima"]),
                   ("Skibby / Slangerup", "Usikkert; tidligst 2032 hvis projekterne fortsætter", ["frs_klima"])],
})
VP_TOWNS_NOTE.update({
 "stenloese": "Har du gasfyr i et udvidelsesområde i Ølstykke eller Stenløse, så tjek Egedal Fjernvarmes kampagnepris, før du køber varmepumpe. Ligger huset uden for udbygningen, er en luft til vand-varmepumpe det typiske valg, når gasfyret skal skiftes.",
 "frederikssund": "Har du gasfyr i Frederikssund by, Græse Bakkeby, Vinge eller St. Rørbæk, så følg Vestforbrændings tidsplan. Bor du i Skibby, Slangerup eller uden for planerne, peger kommunen selv på individuelle varmepumper.",
})
VP_XFAQ.update({
 "stenloese": [("Hvor mange huse i Egedal Kommune har gasfyr?", lambda: f"Danmarks Statistik registrerer {tal(HEAT['stenloese']['CN'])} beboede parcel- og rækkehuse med naturgas i 2026, ud af {tal(hs('stenloese'))}. {tal(HEAT['stenloese']['FJ'])} har fjernvarme, {tal(HEAT['stenloese']['VP'])} varmepumpe og {tal(HEAT['stenloese']['ELV'])} elvarme.", ["dst_bol102"])],
 "frederikssund": [("Hvor mange huse i Frederikssund Kommune har gasfyr?", lambda: f"{tal(HEAT['frederikssund']['CN'])} af de {tal(hs('frederikssund'))} beboede parcel- og rækkehuse ({hp('frederikssund','CN',1)}) har naturgas ifølge Danmarks Statistik, 2026. {tal(HEAT['frederikssund']['FJ'])} har fjernvarme og {tal(HEAT['frederikssund']['VP'])} varmepumpe.", ["dst_bol102"])],
})
FV_SOURCES.update({
 "stenloese": [("Egedal Fjernvarme har solfangere og fliskedel ved Maglevad og forsyner kunder i Stenløse og Ølstykke. Udbygningen i etape 11-20 fortsætter i 2026-2027.", ["ege_fv"]),
               ("Smørum Kraftvarme er nr. 3 af 374 værker i Forsyningstilsynets statistik januar 2026.", ["ft_pris"])],
 "frederikssund": [("Vestforbrænding bygger energicentral med 19 MW elkedel i Frederikssund; drift forventes forår 2028.", ["vf_energi"]),
                   ("Jægerspris Kraftvarme har sat elkedler og varmepumper ind, så produktionen kan køre næsten gasfrit.", ["frs_klima"])],
})
FV_SHARE.update({
 "stenloese": lambda: f"Kun {hp('stenloese','FJ',1)} af de beboede parcel- og rækkehuse i Egedal Kommune har fjernvarme, mens {hp('stenloese','CN',1)} har naturgas. Det er de gasfyr, Egedal Fjernvarmes udbygning handler om.",
 "frederikssund": lambda: f"Kun {hp('frederikssund','FJ',1)} af de beboede parcel- og rækkehuse i Frederikssund Kommune har fjernvarme, mod {hp('dk','FJ',1)} i hele landet, mens {hp('frederikssund','CN',1)} har naturgas.",
})
FV_SOURCES_H.update({"stenloese": "Solfangere, flis og udbygning i Ølstykke-Stenløse", "frederikssund": "Energicentral og Vestforbrænding"})
_reg_age_old12 = reg_age_note
def reg_age_note(c, kommune):
    s = STOCK[c]; B = s["B"]; t = s["tot"]
    if c == "stenloese":
        return (f"{tal(B['1960-1979'])} af de beboede huse i Egedal Kommune ({pct(B['1960-1979'], t)}) er bygget 1960-1979. Tjek lokalplanen eller deklarationen for din ejendom, før du bestiller solceller.", ["ege_sol"])
    if c == "frederikssund":
        return (f"{tal(B['før 1960'])} af de beboede huse i Frederikssund Kommune ({pct(B['før 1960'], t)}) er bygget før 1960. Tjek lokalplan, servitut og evt. beskyttelseslinjer på kommunens digitale kort.", ["frs_sol"])
    return _reg_age_old12(c, kommune)

# ---------- daglig by-rutine 9. nov. 2026: Skanderborg (DK1) og Vordingborg (DK2) ----------
SOL_ORDER.update({
 "skanderborg": ["boliger", "lokalt", "produktion", "faq", "tage", "guides"],
 "vordingborg": ["produktion", "boliger", "lokalt", "tage", "faq", "guides"],
})
VP_ORDER.update({
 "skanderborg": ["lokale-byer", "lokalt", "opvarmning", "faq", "pris", "guides"],
 "vordingborg": ["opvarmning", "lokale-byer", "lokalt", "faq", "pris", "guides"],
})
FV_ORDER.update({
 "skanderborg": ["priser", "billigst", "status", "andel", "faq", "varmekilder"],
 "vordingborg": ["status", "andel", "varmekilder", "priser", "billigst", "faq"],
})
SOL_PROD.update({
 "skanderborg": ("Solceller i Skanderborg: produktion året rundt",
   lambda: f"For et sydvendt tag med 35° hældning i Skanderborg beregner PVGIS ca. {tal(PV['skanderborg']['syd'])} kWh pr. kWp om året; den bedste hældning er {PV['skanderborg']['opt_angle']}° med ca. {tal(PV['skanderborg']['opt'])} kWh. Et 6 kWp-anlæg giver ca. {tal(PV['skanderborg']['syd']*6)} kWh, heraf ca. {tal(sum(PV['skanderborg']['months'][3:8])*6)} kWh fra april til august. Mod øst eller vest falder det til ca. {tal(PV['skanderborg']['oest'])}-{tal(PV['skanderborg']['vest'])} kWh pr. kWp."),
 "vordingborg": ("Meget sol ved Storstrømmen: produktion i Vordingborg",
   lambda: f"PVGIS beregner ca. {tal(PV['vordingborg']['syd'])} kWh pr. kWp om året for et sydvendt tag med 35° hældning i Vordingborg – {rk(_PVY, 'vordingborg', 'højeste')} af de {nw()} byer på dette site. Et 6 kWp-anlæg giver ca. {tal(PV['vordingborg']['syd']*6)} kWh om året og ca. {tal(PV['vordingborg']['months'][5]*6)} kWh i juni. Vender taget mod vest, giver det ca. {tal(PV['vordingborg']['vest'])} kWh pr. kWp, mod øst ca. {tal(PV['vordingborg']['oest'])}."),
})
SOL_PROD_SRC_NEW.update({"skanderborg": ["pv_skanderborg", "pvo_skanderborg", "pvv_skanderborg"], "vordingborg": ["pv_vordingborg", "pvv_vordingborg", "pvo_vordingborg"]})
SOL_ROOF.update({
 "skanderborg": ("Fibercement, tegl og cementsten i Skanderborg",
   lambda: f"Tagene i Skanderborg Kommune er delt næsten ligeligt: {rp('skanderborg','06')} af parcel- og rækkehusene har <strong>fibercement</strong>, {rp('skanderborg','10')} <strong>tegl</strong> og {rp('skanderborg','08')} <strong>cementsten</strong>. På et fladt tag må solcellerne højst hæves 1 m over tagfladen uden ansøgning. Bølge- og skiferplader fra før 1984 kan indeholde asbest, så få taget vurderet før montering.",
   ["dst_bygb50", "skb_sol", "bolius_asb"]),
 "vordingborg": ("Fire ud af ti tage er fibercement i Vordingborg",
   lambda: f"{rp('vordingborg','06')} af parcel- og rækkehusene i Vordingborg Kommune har tag af <strong>fibercement</strong>, mod {rp('dk','06')} på landsplan. {rp('vordingborg','10')} har tegl og {rp('vordingborg','08')} cementsten. Med mange ældre huse er det værd at få tagets alder og et evt. asbestindhold vurderet, før panelerne kommer op.",
   ["dst_bygb50", "bolius_asb"]),
})
SOL_HOMES.update({
 "skanderborg": lambda: f"Skanderborg Kommune har {tal(STOCK['skanderborg']['tot'])} beboede parcel- og rækkehuse, og {pct(STOCK['skanderborg']['B']['2000+'],STOCK['skanderborg']['tot'])} er bygget i 2000 eller senere – {rk(lambda x: STOCK[x]['B']['2000+'] / STOCK[x]['tot'], 'skanderborg', 'højeste')} andel af de {nw()} byer, mod {pct(STOCK['dk']['B']['2000+'],STOCK['dk']['tot'])} på landsplan. {pct(STOCK['skanderborg']['ejer'],STOCK['skanderborg']['tot'])} bebos af ejeren. Skanderborg by har {tal(town('skanderborg','Skanderborg'))} indbyggere, Galten {tal(town('skanderborg','Galten'))}, Hørning {tal(town('skanderborg','Hørning'))} og Ry {tal(town('skanderborg','Ry'))}. Siden gælder hele kommunen.",
 "vordingborg": lambda: f"Vordingborg Kommune har {tal(STOCK['vordingborg']['tot'])} beboede parcel- og rækkehuse, og {pct(STOCK['vordingborg']['B']['før 1960'],STOCK['vordingborg']['tot'])} er bygget før 1960 – næsten hvert andet hus og {rk(lambda x: STOCK[x]['B']['før 1960'] / STOCK[x]['tot'], 'vordingborg', 'højeste')} andel af de {nw()} byer. Vordingborg by har {tal(town('vordingborg','Vordingborg'))} indbyggere, Præstø {tal(town('vordingborg','Præstø'))}, Stege {tal(town('vordingborg','Stege'))} og Nyråd {tal(town('vordingborg','Nyråd'))}. Siden gælder hele kommunen, også Møn.",
})
SOL_HOMES_SRC_NEW.update({"skanderborg": [], "vordingborg": []})
SOL_HOMES_H.update({"skanderborg": "Mange nye huse fra Skanderborg til Galten, Hørning og Ry", "vordingborg": "Ældre huse fra Vordingborg til Præstø og Stege"})
SOL_XFAQ.update({
 "skanderborg": [("Må solceller stå på jorden i haven i Skanderborg?", lambda: "Ja, men de skal som udgangspunkt holde 2,5 m til skel (5 m i sommerhusområder), og er anlægget over 1,8 m højt, kræver det byggetilladelse.", ["skb_sol"])],
 "vordingborg": [("Hvor meget giver solceller i Vordingborg om vinteren?", lambda: f"PVGIS beregner ca. {tal((PV['vordingborg']['months'][10]+PV['vordingborg']['months'][11]+PV['vordingborg']['months'][0])*6)} kWh i alt fra november til januar for et 6 kWp-anlæg mod syd, mod ca. {tal(sum(PV['vordingborg']['months'][4:7])*6)} kWh fra maj til juli.", ["pv_vordingborg"])],
})
VP_HEAT.update({
 "skanderborg": ("To ud af tre huse har fjernvarme i Skanderborg",
   lambda: f"{hp('skanderborg','FJ')} af de {tal(hs('skanderborg'))} beboede parcel- og rækkehuse i Skanderborg Kommune har fjernvarme, mod {hp('dk','FJ')} på landsplan. {tal(HEAT['skanderborg']['VP'])} har allerede varmepumpe ({hp('skanderborg','VP',1)}), mens {tal(HEAT['skanderborg']['CN'])} har naturgas, {tal(HEAT['skanderborg']['CO'])} oliefyr og {tal(HEAT['skanderborg']['ELV'])} elvarme – de fleste i landsbyerne uden for nettet."),
 "vordingborg": ("Mange med elvarme og oliefyr: opvarmning i Vordingborg",
   lambda: f"{tal(HEAT['vordingborg']['CO'])} beboede parcel- og rækkehuse i Vordingborg Kommune ({hp('vordingborg','CO',1)}) har oliefyr – {rk(_hf('CO'), 'vordingborg', 'højeste')} andel – og {tal(HEAT['vordingborg']['ELV'])} ({hp('vordingborg','ELV',1)}) elvarme – {rk(_hf('ELV'), 'vordingborg', 'højeste')} andel af de {nw()} byer. {tal(HEAT['vordingborg']['VP'])} har allerede varmepumpe ({hp('vordingborg','VP',1)}), {rk(_hf('VP'), 'vordingborg', 'højeste')} andel, og kun {hp('vordingborg','FJ',1)} har fjernvarme."),
})
VP_HEAT_SRC_NEW.update({"skanderborg": ["skb_varme"], "vordingborg": ["vor_varme"]})
VP_TOWNS.update({
 "skanderborg": [("Skanderborg / Hørning", "Skanderborg-Hørning Fjernvarme; Mesing afventer vindmølle og tilskud", ["skb_varme", "skb_mesing"]),
                 ("Galten / Skovby / Stjær", "Galten Varmeværk og Kredsløb; Galten syd og Skovby syd stoppet", ["skb_varme"]),
                 ("Herskind / Låsby", "Fjernvarme forsøgt, stoppet pga. for få tilmeldinger", ["skb_varme"]),
                 ("Sjelle / Skjørring / Dørup", "Ikke potentielle til fjernvarme: varmepumpe eller fælles løsning", ["skb_varme"])],
 "vordingborg": [("Nyråd", "Fjernvarme omkring efteråret 2026; ingen varmepumpetilskud", ["vf_nyraad_faq"]),
                 ("Stensved / Præstø", "Forventet fjernvarmeudbygning frem mod 2028", ["vor_varme"]),
                 ("Ørslev", "Fjernvarme etableret 2021-2024", ["vf_oerslev"]),
                 ("Øvrige gas- og olieområder", "Forventes primært individuel opvarmning, fx varmepumpe", ["vor_varme"])],
})
VP_TOWNS_NOTE.update({
 "skanderborg": "Bor du i en landsby, hvor fjernvarmen er stoppet eller ikke er potentiel, er en luft til vand-varmepumpe det typiske valg, når olie- eller gasfyret skal skiftes. Kommunen har også en pulje til fælles varmeløsninger i landsbyer.",
 "vordingborg": "Bor du i Nyråd, Stensved eller Præstø, så tjek fjernvarmen først. I resten af kommunen forventer varmeplanen individuel opvarmning, og her er en luft til vand-varmepumpe det oplagte alternativ til olie, gas og elvarme.",
})
VP_XFAQ.update({
 "skanderborg": [("Hvor mange huse i Skanderborg Kommune har varmepumpe?", lambda: f"{tal(HEAT['skanderborg']['VP'])} af de {tal(hs('skanderborg'))} beboede parcel- og rækkehuse ({hp('skanderborg','VP',1)}) ifølge Danmarks Statistik, 2026. {tal(HEAT['skanderborg']['CN'])} har naturgas og {tal(HEAT['skanderborg']['CO'])} oliefyr.", ["dst_bol102"])],
 "vordingborg": [("Hvor mange huse i Vordingborg Kommune har elvarme eller oliefyr?", lambda: f"Danmarks Statistik registrerer {tal(HEAT['vordingborg']['ELV'])} beboede parcel- og rækkehuse med elvarme og {tal(HEAT['vordingborg']['CO'])} med oliefyr i 2026, ud af {tal(hs('vordingborg'))}. {tal(HEAT['vordingborg']['CN'])} har naturgas.", ["dst_bol102"])],
})
FV_SOURCES.update({
 "skanderborg": [("Alle fjernvarmeselskaber i Skanderborg Kommune er forbrugerejede; kommunen har ikke sit eget selskab, men Kredsløb fra Aarhus forsyner bl.a. Galten nord og Skovby.", ["skb_varme"]),
                 ("Skanderborg-Hørning Fjernvarmes projekt i Mesing bygger på strøm fra en planlagt vindmølle på 4,5 MW med direkte linje til værket.", ["skb_mesing"])],
 "vordingborg": [("Vordingborg Fjernvarme har bl.a. halmfyr og en elkedel på 30 MW; Stege Fjernvarme halmfyr og solvarme.", ["vor_ep"]),
                 ("Præstø Fjernvarme har bl.a. varmepumpe, træpillekedel og solvarme.", ["vor_ep"])],
})
FV_SHARE.update({
 "skanderborg": lambda: f"{hp('skanderborg','FJ',1)} af de beboede parcel- og rækkehuse i Skanderborg Kommune har fjernvarme, mod {hp('dk','FJ',1)} i hele landet. Kun {hp('skanderborg','CN',1)} har naturgas.",
 "vordingborg": lambda: f"Kun {hp('vordingborg','FJ',1)} af de beboede parcel- og rækkehuse i Vordingborg Kommune har fjernvarme, mod {hp('dk','FJ',1)} i hele landet. Til gengæld har {hp('vordingborg','VP',1)} allerede varmepumpe.",
})
FV_SOURCES_H.update({"skanderborg": "Forbrugerejede værker og vindmølle ved Mesing", "vordingborg": "Halm, elkedel og solvarme"})
_reg_age_old13 = reg_age_note
def reg_age_note(c, kommune):
    s = STOCK[c]; B = s["B"]; t = s["tot"]
    if c == "skanderborg":
        return (f"{tal(B['2000+'])} af de beboede huse i Skanderborg Kommune ({pct(B['2000+'], t)}) er bygget i 2000 eller senere. I nyere udstykninger har lokalplanen ofte regler om tagets udseende, så tjek den i kommunens lokalplanportal.", ["skb_sol"])
    if c == "vordingborg":
        return (f"{tal(B['før 1960'])} af de beboede huse i Vordingborg Kommune ({pct(B['før 1960'], t)}) er bygget før 1960. Er huset fredet eller bevaringsværdigt, kræver solceller altid byggetilladelse.", ["vor_sol"])
    return _reg_age_old13(c, kommune)

# keyword-backlog 9/11 2026: 'energirenovering silkeborg' (GSC 12 visninger) -> FAQ på /varmepumpe/silkeborg/
VP_XFAQ["silkeborg"] = VP_XFAQ["silkeborg"] + [("Hvor får jeg hjælp til energirenovering i Silkeborg?", lambda: "Silkeborg Kommune peger på energirenoveringer af tag og loft, vinduer og døre, terrændæk og ydervægge og anbefaler at få en energirådgiver til at vurdere, hvad der giver mening for dit hus. Energistyrelsens gratis, uvildige rådgivning hos SparEnergi har telefon 31 15 90 00 og mail info@sparenergi.dk. Et hus med lavere varmetab kan klare sig med en mindre varmepumpe.", ["sil_groen", "se_raad"])]

# ---------- daglig by-rutine 10. nov. 2026: København (DK2, vp_page False) og Vejen (DK1) ----------
SOL_ORDER.update({
 "koebenhavn": ["boliger", "tage", "lokalt", "faq", "produktion", "guides"],
 "vejen": ["tage", "produktion", "boliger", "faq", "lokalt", "guides"],
})
VP_ORDER.update({
 "vejen": ["lokalt", "opvarmning", "faq", "lokale-byer", "pris", "guides"],
})
# København: varmepumpe-blokkene (lokalt, opvarmning, lokale-byer) bor på fjernvarmesiden
FV_ORDER.update({
 "koebenhavn": ["status", "opvarmning", "priser", "lokalt", "andel", "billigst", "lokale-byer", "faq", "varmekilder"],
 "vejen": ["billigst", "priser", "andel", "status", "faq", "varmekilder"],
})
SOL_PROD.update({
 "koebenhavn": ("Solceller i København: mod syd, øst eller vest",
   lambda: f"PVGIS beregner ca. {tal(PV['koebenhavn']['syd'])} kWh pr. kWp om året for et sydvendt tag med 35° hældning i København – {rk(_PVY, 'koebenhavn', 'højeste')} af de {nw()} byer på dette site. Et 6 kWp-anlæg giver ca. {tal(PV['koebenhavn']['syd']*6)} kWh om året. Mod øst giver det ca. {tal(PV['koebenhavn']['oest'])} og mod vest ca. {tal(PV['koebenhavn']['vest'])} kWh pr. kWp – værd at kende, fordi kommunen skriver, at solceller af hensyn til arkitekturen nogle gange kun kan sidde mod gård- eller bagsiden."),
 "vejen": ("Solceller i Vejen: sommer og vinter",
   lambda: f"PVGIS beregner ca. {tal(PV['vejen']['syd'])} kWh pr. kWp om året for et sydvendt tag med 35° hældning i Vejen og ca. {tal(PV['vejen']['opt'])} kWh ved den bedste hældning på {PV['vejen']['opt_angle']}°. Et 6 kWp-anlæg giver ca. {tal(PV['vejen']['syd']*6)} kWh om året, men november til januar giver tilsammen kun ca. {tal((PV['vejen']['months'][10]+PV['vejen']['months'][11]+PV['vejen']['months'][0])*6)} kWh. Mod øst eller vest er det ca. {tal(PV['vejen']['oest'])}-{tal(PV['vejen']['vest'])} kWh pr. kWp."),
})
SOL_PROD_SRC_NEW.update({"koebenhavn": ["pv_koebenhavn", "pvo_koebenhavn", "pvv_koebenhavn", "kbh_solret"], "vejen": ["pv_vejen", "pvo_vejen", "pvv_vejen"]})
SOL_ROOF.update({
 "koebenhavn": ("Tegl og flade tage i København",
   lambda: f"{rp('koebenhavn','10')} af parcel- og rækkehusene i Københavns Kommune har <strong>tegltag</strong>, mod {rp('dk','10')} på landsplan, og {pct(_flat('koebenhavn'), ROOF['koebenhavn']['tot'])} har fladt tag eller tagpap. Kommunens retningslinjer siger, at panelerne skal passe til tagets form og så vidt muligt have samme farve som tagmaterialet, og at inddækninger skal have samme farve som solcellerne.",
   ["dst_bygb50", "kbh_solret"]),
 "vejen": ("Fibercement og cementsten på tagene i Vejen",
   lambda: f"{rp('vejen','06')} af parcel- og rækkehusene i Vejen Kommune har tag af <strong>fibercement</strong> og {rp('vejen','08')} <strong>cementsten</strong> – {rk(_rt('08'), 'vejen', 'højeste')} andel cementsten af de {nw()} byer. {rp('vejen','10')} har tegl. Bølgeplader fra før 1984 kan indeholde asbest, så få taget vurderet, før panelerne monteres.",
   ["dst_bygb50", "bolius_asb"]),
})
SOL_HOMES.update({
 "koebenhavn": lambda: f"Københavns Kommune har {tal(STOCK['koebenhavn']['tot'])} beboede parcel- og rækkehuse, og {pct(STOCK['koebenhavn']['B']['før 1960'],STOCK['koebenhavn']['tot'])} er bygget før 1960 – {rk(lambda x: STOCK[x]['B']['før 1960'] / STOCK[x]['tot'], 'koebenhavn', 'højeste')} andel af de {nw()} byer, mod {pct(STOCK['dk']['B']['før 1960'],STOCK['dk']['tot'])} på landsplan. {pct(STOCK['koebenhavn']['raekke'],STOCK['koebenhavn']['tot'])} er række-, kæde- eller dobbelthuse. Mange villaområder har servitutter fra starten af 1900-tallet, så tjek tingbogen, før du bestiller.",
 "vejen": lambda: f"Vejen Kommune har {tal(STOCK['vejen']['tot'])} beboede parcel- og rækkehuse, og {pct(STOCK['vejen']['B']['1960-1979'],STOCK['vejen']['tot'])} er bygget 1960-1979, mod {pct(STOCK['dk']['B']['1960-1979'],STOCK['dk']['tot'])} på landsplan. {pct(STOCK['vejen']['ejer'],STOCK['vejen']['tot'])} bebos af ejeren. Vejen by har {tal(town('vejen','Vejen'))} indbyggere, Brørup {tal(town('vejen','Brørup'))}, Holsted {tal(town('vejen','Holsted'))}, Rødding {tal(town('vejen','Rødding'))} og Jels {tal(town('vejen','Jels'))}. Siden gælder hele kommunen.",
})
SOL_HOMES_SRC_NEW.update({"koebenhavn": ["kbh_serv"], "vejen": []})
SOL_HOMES_H.update({"koebenhavn": "Ældre villaer og rækkehuse i København", "vejen": "Huse fra Vejen til Brørup, Holsted, Rødding og Jels"})
SOL_XFAQ.update({
 "koebenhavn": [("Kan jeg få hjælp til at vurdere solceller i København?", lambda: "Københavns Kommune henviser til Solcellepuljen, hvor ejendomme kan søge støtte til en professionel teknisk rådgiver, der screener, om ejendommen er velegnet til solceller. Se betingelserne på kommunens side om byfornyelsespuljer.", ["kbh_sol"])],
 "vejen": [("Kræver solceller på jorden tilladelse i Vejen Kommune?", lambda: "Ja. Vejen Kommune skriver, at et fritstående anlæg på terræn kræver byggetilladelse, og at kommunen kan stille vilkår om anlæggets farve og refleksion.", ["vjn_byg"])],
})
VP_HEAT.update({
 "koebenhavn": ("Over ni ud af ti huse har fjernvarme i København",
   lambda: f"{hp('koebenhavn','FJ',1)} af de {tal(hs('koebenhavn'))} beboede parcel- og rækkehuse i Københavns Kommune har fjernvarme, mod {hp('dk','FJ')} på landsplan. Kun {tal(HEAT['koebenhavn']['VP'])} har varmepumpe, {tal(HEAT['koebenhavn']['ELV'])} elvarme og {tal(HEAT['koebenhavn']['CO'])} oliefyr, og Danmarks Statistik registrerer {tal(HEAT['koebenhavn']['CN'])} {'hus' if HEAT['koebenhavn']['CN'] == 1 else 'huse'} med naturgas."),
 "vejen": ("Næsten hvert femte hus har naturgas i Vejen",
   lambda: f"{tal(HEAT['vejen']['CN'])} af de {tal(hs('vejen'))} beboede parcel- og rækkehuse i Vejen Kommune ({hp('vejen','CN',1)}) har naturgas, mod {hp('dk','CN',1)} på landsplan, og {tal(HEAT['vejen']['CO'])} har oliefyr. Kun {hp('vejen','FJ')} har fjernvarme. {tal(HEAT['vejen']['VP'])} har allerede varmepumpe ({hp('vejen','VP',1)}) – {rk(_hf('VP'), 'vejen', 'højeste')} andel af de {nw()} byer."),
})
VP_HEAT_SRC_NEW.update({"koebenhavn": ["kbh_tilsl"], "vejen": ["vjn_fv"]})
VP_TOWNS.update({
 "koebenhavn": [("Hele kommunen", "Tilslutningspligt; enfamiliehuse må vælge varmepumpe, men betaler effektbidrag", ["kbh_tilsl"]),
                ("Nordhavn", "HOFORs 24 MW havvandsvarmepumpe i drift vinteren 2027/28", ["hofor_sk"]),
                ("Midtbyen", "Højeste fremløbstemperatur i dag; ældre anlæg kan kræve opgradering", ["hofor_vk"]),
                ("Brønshøj", "Yderst i nettet med de laveste temperaturer i dag", ["hofor_vk"])],
 "vejen": [("Vejen", "Varmega (tidl. Vejen Varmeværk)", ["vjn_fv", "ft_pris"]),
           ("Brørup", "Brørup Fjernvarme, blandt landets billigste", ["vjn_fv", "ft_pris"]),
           ("Holsted / Rødding", "Holsted Varmeværk og Rødding Varmecentral", ["vjn_fv"]),
           ("Jels", "Fjernvarmeprojekt opgivet 2026: individuel løsning", ["vjn_jels2"])],
})
VP_TOWNS_NOTE.update({
 "koebenhavn": "Har du fjernvarme i København, er første skridt at tjekke, om anlægget er klar til lavere temperatur. En varmepumpe er mest relevant for de få huse med olie, elvarme eller anden opvarmning – og husk effektbidraget, hvis matriklen har tilslutningspligt.",
 "vejen": "Bor du i Vejen, Brørup, Holsted eller Rødding, så spørg værket, om din adresse kan få fjernvarme. I Jels og de mindre landsbyer med naturgas er en luft til vand-varmepumpe det typiske valg, når gasfyret skal skiftes.",
})
VP_XFAQ.update({
 "koebenhavn": [("Hvor mange huse i København har ikke fjernvarme?", lambda: f"Ca. {tal(hs('koebenhavn')-HEAT['koebenhavn']['FJ'])} af {tal(hs('koebenhavn'))} beboede parcel- og rækkehuse ({pct(hs('koebenhavn')-HEAT['koebenhavn']['FJ'],hs('koebenhavn'),1)}) ifølge Danmarks Statistik, 2026. Heraf har {tal(HEAT['koebenhavn']['VP'])} varmepumpe, {tal(HEAT['koebenhavn']['ELV'])} elvarme og {tal(HEAT['koebenhavn']['CO'])} oliefyr.", ["dst_bol102"])],
 "vejen": [("Hvor mange huse i Vejen Kommune har naturgas?", lambda: f"{tal(HEAT['vejen']['CN'])} af de {tal(hs('vejen'))} beboede parcel- og rækkehuse ({hp('vejen','CN',1)}) ifølge Danmarks Statistik, 2026. {tal(HEAT['vejen']['VP'])} har allerede varmepumpe, og {tal(HEAT['vejen']['CO'])} har oliefyr.", ["dst_bol102"])],
})
FV_SOURCES.update({
 "koebenhavn": [("HOFOR installerer en <strong>24 MW havvandsvarmepumpe</strong> i energicentralen i Nordhavn, som skal kunne forsyne ca. 12.500 husstande. Den skal i drift i løbet af vinteren 2027/2028.", ["hofor_sk"]),
                ("Fjernvarmen kommer i dag fra affaldsforbrænding, kraftvarmeværker, varmepumper, spidslastanlæg og vekslerstationer. Varmen fra bl.a. Amagerværket føres op i tunnelen i Adelgade og ved Fredens Park.", ["hofor_vk"])],
 "vejen": [("Vejen Varmeværk hedder nu <strong>Varmega</strong>.", ["vjn_fv"]),
           ("Jels Varmes projekt skulle primært producere varme med varmepumper suppleret med biomasse og naturgas; i de seneste beregninger indgik briketter af overskudstræ og savsmuld.", ["vjn_jels2"])],
})
FV_SHARE.update({
 "koebenhavn": lambda: f"{hp('koebenhavn','FJ',1)} af de beboede parcel- og rækkehuse i Københavns Kommune har fjernvarme, mod {hp('dk','FJ',1)} i hele landet. Det efterlader ca. {tal(hs('koebenhavn')-HEAT['koebenhavn']['FJ'])} huse med anden opvarmning, heraf {tal(HEAT['koebenhavn']['VP'])} med varmepumpe.",
 "vejen": lambda: f"{hp('vejen','FJ',1)} af de beboede parcel- og rækkehuse i Vejen Kommune har fjernvarme, mod {hp('dk','FJ',1)} i hele landet. {hp('vejen','CN',1)} har naturgas og {hp('vejen','VP',1)} varmepumpe.",
})
FV_SOURCES_H.update({"koebenhavn": "Havvand, affald og Amagerværket", "vejen": "Fire værker og et opgivet projekt i Jels"})
_reg_age_old14 = reg_age_note
def reg_age_note(c, kommune):
    s = STOCK[c]; B = s["B"]; t = s["tot"]
    if c == "koebenhavn":
        return (f"{tal(B['før 1960'])} af de beboede huse i Københavns Kommune ({pct(B['før 1960'], t)}) er bygget før 1960. Mange villaområder har servitutter fra starten af 1900-tallet, og er grunden omfattet af servitut eller lokalplan, kræver solceller byggetilladelse.", ["kbh_serv", "kbh_sol"])
    if c == "vejen":
        return (f"{tal(B['1960-1979'])} af de beboede huse i Vejen Kommune ({pct(B['1960-1979'], t)}) er bygget 1960-1979. Er huset omfattet af en lokalplan eller fredning, kan solceller kræve dispensation – tjek reglerne for din adresse i Byg & Miljø.", ["vjn_byg"])
    return _reg_age_old14(c, kommune)

# keyword-backlog 10/11 2026: 'luft til vand varmepumpe aabenraa' (GSC 40 visninger, pos. 79,4) -> FAQ om pris og elvarme på /varmepumpe/aabenraa/
VP_XFAQ["aabenraa"] = VP_XFAQ.get("aabenraa", []) + [("Hvad koster en luft til vand-varmepumpe i Aabenraa?", lambda: f"SparEnergi angiver typisk 100.000-130.000 kr. for en luft til vand-varmepumpe, og Energisparer.dk ca. 90.000-150.000 kr. afhængigt af husets størrelse. Har huset elvarme med paneler – det gælder {tal(HEAT['aabenraa']['ELV'])} af de {tal(hs('aabenraa'))} beboede parcel- og rækkehuse i Aabenraa Kommune – skal der også etableres radiatorer eller gulvvarme, før en luft til vand-varmepumpe kan bruges. Ellers er en luft til luft-varmepumpe det billigere valg.", ["se_vp", "es_vp", "es_l2v", "dst_bol102"])]

# ---------- daglig by-rutine 11. nov. 2026: Varde (DK1) og Faxe (DK2) ----------
SOL_ORDER.update({
 "varde": ["produktion", "lokalt", "tage", "faq", "boliger", "guides"],
 "faxe": ["lokalt", "boliger", "produktion", "tage", "faq", "guides"],
})
VP_ORDER.update({
 "varde": ["opvarmning", "lokale-byer", "lokalt", "pris", "faq", "guides"],
 "faxe": ["lokalt", "lokale-byer", "opvarmning", "faq", "pris", "guides"],
})
FV_ORDER.update({
 "varde": ["priser", "status", "billigst", "andel", "faq", "varmekilder"],
 "faxe": ["status", "andel", "priser", "faq", "billigst", "varmekilder"],
})
SOL_PROD.update({
 "varde": ("Solceller i Varde: vestkyst og hældning",
   lambda: f"PVGIS beregner ca. {tal(PV['varde']['syd'])} kWh pr. kWp om året for et sydvendt tag med 35° hældning i Varde og ca. {tal(PV['varde']['opt'])} kWh ved den bedste hældning på {PV['varde']['opt_angle']}°. Et 6 kWp-anlæg giver ca. {tal(PV['varde']['syd']*6)} kWh om året. Juni alene giver ca. {tal(PV['varde']['months'][5]*6)} kWh, december kun ca. {tal(PV['varde']['months'][11]*6)} kWh. Mod øst er det ca. {tal(PV['varde']['oest'])} og mod vest ca. {tal(PV['varde']['vest'])} kWh pr. kWp."),
 "faxe": ("Solceller i Faxe: blandt de solrigeste på sitet",
   lambda: f"PVGIS beregner ca. {tal(PV['faxe']['syd'])} kWh pr. kWp om året for et sydvendt tag med 35° hældning i Faxe – {rk(_PVY, 'faxe', 'højeste')} af de {nw()} byer på dette site. Et 6 kWp-anlæg giver ca. {tal(PV['faxe']['syd']*6)} kWh om året. Mod øst giver det ca. {tal(PV['faxe']['oest'])} og mod vest ca. {tal(PV['faxe']['vest'])} kWh pr. kWp, så et øst-vest-tag giver ca. en femtedel mindre end et sydvendt."),
})
SOL_PROD_SRC_NEW.update({"varde": ["pv_varde", "pvo_varde", "pvv_varde"], "faxe": ["pv_faxe", "pvo_faxe", "pvv_faxe"]})
SOL_ROOF.update({
 "varde": ("Fibercement, cementsten og tegl på tagene i Varde",
   lambda: f"{rp('varde','06')} af parcel- og rækkehusene i Varde Kommune har tag af <strong>fibercement</strong>, {rp('varde','08')} <strong>cementsten</strong> og {rp('varde','10')} <strong>tegl</strong>. Bølgeplader fra før 1984 kan indeholde asbest, og Varde Kommune råder dig til at få en professionel rådgiver til at vurdere, om tagkonstruktionen kan bære den ekstra vægt fra solcellerne.",
   ["dst_bygb50", "bolius_asb", "var_byg"]),
 "faxe": ("Få tegltage og mange cementsten i Faxe",
   lambda: f"Kun {rp('faxe','10')} af parcel- og rækkehusene i Faxe Kommune har <strong>tegltag</strong> – {rk(_rt('10'), 'faxe', 'laveste', rev=True)} andel af de {nw()} byer – mod {rp('dk','10')} på landsplan. {rp('faxe','06')} har <strong>fibercement</strong> og {rp('faxe','08')} <strong>cementsten</strong>. Flere lokalplaner i kommunen kræver, at solceller er nedfældet i tagfladen, så tjek lokalplanen, før du vælger montering.",
   ["dst_bygb50", "fax_sol"]),
})
SOL_HOMES.update({
 "varde": lambda: f"Varde Kommune har {tal(STOCK['varde']['tot'])} beboede parcel- og rækkehuse, og {pct(STOCK['varde']['B']['før 1960'],STOCK['varde']['tot'])} er bygget før 1960, mod {pct(STOCK['dk']['B']['før 1960'],STOCK['dk']['tot'])} på landsplan. {pct(STOCK['varde']['ejer'],STOCK['varde']['tot'])} bebos af ejeren. Varde by har {tal(town('varde','Varde'))} indbyggere, Ølgod {tal(town('varde','Ølgod'))}, Oksbøl {tal(town('varde','Oksbøl'))}, Tistrup {tal(town('varde','Tistrup'))} og Nørre Nebel {tal(town('varde','Nørre Nebel'))}. Siden gælder hele kommunen.",
 "faxe": lambda: f"Faxe Kommune har {tal(STOCK['faxe']['tot'])} beboede parcel- og rækkehuse, og {pct(STOCK['faxe']['raekke'],STOCK['faxe']['tot'])} er række-, kæde- eller dobbelthuse. {pct(STOCK['faxe']['B']['2000+'],STOCK['faxe']['tot'])} er bygget i 2000 eller senere, mod {pct(STOCK['dk']['B']['2000+'],STOCK['dk']['tot'])} på landsplan. Haslev er kommunens største by med {tal(town('faxe','Haslev'))} indbyggere, Faxe har {tal(town('faxe','Faxe'))}, Rønnede {tal(town('faxe','Rønnede'))}, Dalby {tal(town('faxe','Dalby'))}, Faxe Ladeplads {tal(town('faxe','Faxe Ladeplads'))} og Karise {tal(town('faxe','Karise'))}. Siden gælder hele kommunen.",
})
SOL_HOMES_SRC_NEW.update({"varde": [], "faxe": []})
SOL_HOMES_H.update({"varde": "Huse fra Varde til Ølgod, Oksbøl og Tistrup", "faxe": "Huse i Haslev, Faxe og de mindre byer"})
SOL_XFAQ.update({
 "varde": [("Skal solceller registreres i BBR i Varde Kommune?", lambda: "Ja. Varde Kommune skriver, at anlægget altid skal registreres i Bygnings- og Boligregistret (BBR), uanset om det kræver byggetilladelse eller ej.", ["var_byg"])],
 "faxe": [("Kræver solceller på jorden tilladelse i Faxe Kommune?", lambda: "Ja. Et anlæg på jorden er et teknisk anlæg og kræver byggetilladelse, og i landzone også landzonetilladelse. Mindre anlæg til privat brug ved eksisterende bebyggelse får normalt tilladelse, men i områder med særlige natur- eller landskabshensyn gives der normalt afslag.", ["fax_sol"])],
})
VP_HEAT.update({
 "varde": ("Mange oliefyr tilbage i Varde",
   lambda: f"{tal(HEAT['varde']['CO'])} af de {tal(hs('varde'))} beboede parcel- og rækkehuse i Varde Kommune ({hp('varde','CO',1)}) har oliefyr – {rk(_hf('CO'), 'varde', 'højeste')} andel af de {nw()} byer og mod {hp('dk','CO',1)} på landsplan. {tal(HEAT['varde']['CN'])} har naturgas, og {tal(HEAT['varde']['VP'])} har allerede varmepumpe ({hp('varde','VP',1)}). {hp('varde','FJ')} har fjernvarme."),
 "faxe": ("Næsten hvert tredje hus har naturgas i Faxe",
   lambda: f"{tal(HEAT['faxe']['CN'])} af de {tal(hs('faxe'))} beboede parcel- og rækkehuse i Faxe Kommune ({hp('faxe','CN',1)}) har naturgas, mod {hp('dk','CN',1)} på landsplan, og kun {hp('faxe','FJ')} har fjernvarme. {tal(HEAT['faxe']['VP'])} har allerede varmepumpe ({hp('faxe','VP',1)}) – {rk(_hf('VP'), 'faxe', 'højeste')} andel af de {nw()} byer – og {tal(HEAT['faxe']['ELV'])} har elvarme."),
})
VP_HEAT_SRC_NEW.update({"varde": ["var_vpl"], "faxe": ["fax_fl", "fax_es"]})
VP_TOWNS.update({
 "varde": [("Varde / Alslev", "DIN Forsyning Varme via transmissionsledning", ["var_vpl", "ft_pris"]),
           ("Ølgod / Outrup / Ansager / Oksbøl", "Egne værker, alle under landsgennemsnittet i pris", ["var_vpl", "ft_pris"]),
           ("Billum / Janderup", "Konverteret til fjernvarme fra Oksbøl", ["var_oks"]),
           ("Agerbæk, Årre, Næsbjerg m.fl.", "Helle Energi: fjernvarme i løbet af 2026-2027", ["var_helle"])],
 "faxe": [("Faxe", "Faxe Fjernvarmeselskab, under landsgennemsnittet i pris", ["ft_pris"]),
          ("Haslev", "Haslev Fjernvarme; tre udbygningsprojekter afventer", ["fax_haslev", "ft_pris"]),
          ("Faxe Ladeplads", "Ikke længere muligt fjernvarmeområde (2025)", ["fax_fl"]),
          ("Rønnede, Karise, Dalby", "Fjernvarmeprojekter droppet 2023", ["fax_es"])],
})
VP_TOWNS_NOTE.update({
 "varde": "Bor du i en af Helle-byerne eller tæt på et af de ni værker, så spørg først, om din adresse kan få fjernvarme – i et udpeget område kan du ikke få tilskud til varmepumpe. I de mindste landsbyer anbefaler varmeplanen individuelle løsninger som en luft til vand-varmepumpe.",
 "faxe": "Har du gasfyr i Faxe Ladeplads, Karise, Dalby eller Rønnede, er fjernvarme ikke på vej, og en luft til vand-varmepumpe er det typiske valg. Bor du i et af Haslevs projektområder, så spørg kommunen om status, før du søger tilskud.",
})
VP_XFAQ.update({
 "varde": [("Hvor mange huse i Varde Kommune har oliefyr?", lambda: f"{tal(HEAT['varde']['CO'])} af de {tal(hs('varde'))} beboede parcel- og rækkehuse ({hp('varde','CO',1)}) ifølge Danmarks Statistik, 2026. {tal(HEAT['varde']['CN'])} har naturgas, og {tal(HEAT['varde']['VP'])} har allerede varmepumpe.", ["dst_bol102"])],
 "faxe": [("Hvor mange huse i Faxe Kommune har naturgas?", lambda: f"{tal(HEAT['faxe']['CN'])} af de {tal(hs('faxe'))} beboede parcel- og rækkehuse ({hp('faxe','CN',1)}) ifølge Danmarks Statistik, 2026. {tal(HEAT['faxe']['VP'])} har allerede varmepumpe, og {tal(HEAT['faxe']['CO'])} har oliefyr.", ["dst_bol102"])],
})
FV_SOURCES.update({
 "varde": [("Varde by og Alslev får varmen fra DIN Forsyning via en <strong>transmissionsledning fra Esbjerg</strong>, hvor affaldsforbrændingen Energnist ifølge varmeplanen fortsat skal levere ca. halvdelen af varmen.", ["var_vpl"]),
           ("Oksbøl Varmeværk har et solvarmeanlæg på 15.000 m², en 8 MW elkedel og siden 2023 en 8,5 MW fliskedel, så størstedelen af varmen i Oksbøl i dag laves på bæredygtig energi.", ["var_oks"])],
 "faxe": [("Haslev Fjernvarmes udbygning skal bidrage til Faxe Kommunes mål om at udfase gas- og oliefyr i <strong>2030</strong>.", ["fax_haslev"]),
          ("Faxe Kommune skriver, at fjernvarme typisk giver færre lokale støjgener end individuelle varmepumper og mindre vedligeholdelse for den enkelte.", ["fax_haslev"])],
})
FV_SHARE.update({
 "varde": lambda: f"{hp('varde','FJ',1)} af de beboede parcel- og rækkehuse i Varde Kommune har fjernvarme, mod {hp('dk','FJ',1)} i hele landet. {hp('varde','CO',1)} har oliefyr og {hp('varde','VP',1)} varmepumpe.",
 "faxe": lambda: f"{hp('faxe','FJ',1)} af de beboede parcel- og rækkehuse i Faxe Kommune har fjernvarme, mod {hp('dk','FJ',1)} i hele landet. {hp('faxe','CN',1)} har naturgas og {hp('faxe','VP',1)} varmepumpe.",
})
FV_SOURCES_H.update({"varde": "Ni værker fra Esbjerg-ledningen til flis i Oksbøl", "faxe": "Haslevs projekter og målet for 2030"})
_reg_age_old15 = reg_age_note
def reg_age_note(c, kommune):
    s = STOCK[c]; B = s["B"]; t = s["tot"]
    if c == "varde":
        return (f"{tal(B['før 1960'])} af de beboede huse i Varde Kommune ({pct(B['før 1960'], t)}) er bygget før 1960. Bygninger med SAVE-bevaringsværdi 1-4 er optaget som bevaringsværdige i kommuneplanen, og lokalplaner eller tinglyste deklarationer kan regulere solceller – tjek din ejendom først.", ["var_byg"])
    if c == "faxe":
        return (f"{tal(B['før 1960'])} af de beboede huse i Faxe Kommune ({pct(B['før 1960'], t)}) er bygget før 1960. I bevarende lokalplaner ser Faxe Kommune på husets arkitektur, bevaringsværdi og synlighed fra vej, sti eller fællesareal, før solceller kan godkendes.", ["fax_sol"])
    return _reg_age_old15(c, kommune)


# keyword-backlog 11/11 2026: 'luft til vand varmepumpe svendborg' (GSC 32 visninger, pos. 36,6) -> FAQ om luft til vand-pris og gas/olie på /varmepumpe/svendborg/
VP_XFAQ["svendborg"] = VP_XFAQ["svendborg"] + [("Hvad koster en luft til vand-varmepumpe i Svendborg?", lambda: f"SparEnergi angiver typisk 100.000-130.000 kr. for en luft til vand-varmepumpe, og Energisparer.dk ca. 90.000-150.000 kr. inkl. installation afhængigt af husets størrelse og varmetab. I Svendborg Kommune har {tal(HEAT['svendborg']['CN'])} beboede parcel- og rækkehuse naturgas og {tal(HEAT['svendborg']['CO'])} oliefyr – huse, der typisk allerede har radiatorer, så en luft til vand-varmepumpe kan overtage både rumvarme og varmt vand.", ["se_vp", "es_vp", "es_l2v", "dst_bol102"])]
# keyword-backlog 11/11 2026: 'luft til luft varmepumpe aabenraa' (GSC 30 visninger, pos. 84,1) -> FAQ om luft til luft på /varmepumpe/aabenraa/
VP_XFAQ["aabenraa"] = VP_XFAQ.get("aabenraa", []) + [("Hvad koster en luft til luft-varmepumpe i Aabenraa?", lambda: f"SparEnergi angiver 15.000-30.000 kr. på sin side om luft til luft og typisk 30.000-40.000 kr. i sin sammenligning af typer; Energisparer.dk ca. 12.000-25.000 kr. Den passer bedst til huse med elvarme – det gælder {tal(HEAT['aabenraa']['ELV'])} af de {tal(hs('aabenraa'))} beboede parcel- og rækkehuse i Aabenraa Kommune – men den varmer kun de rum, den kan nå, giver ikke varmt vand og er ikke omfattet af Varmepumpepuljen.", ["se_l2l", "se_vp", "es_vp", "se_vpp", "dst_bol102"])]

# keyword-backlog 12/11 2026: 'luft til luft varmepumpe svendborg' (GSC 20 visninger, pos. 36,9) -> FAQ om luft til luft på /varmepumpe/svendborg/
VP_XFAQ["svendborg"] = VP_XFAQ["svendborg"] + [("Hvad koster en luft til luft-varmepumpe i Svendborg?", lambda: f"SparEnergi angiver 15.000-30.000 kr. på sin side om luft til luft og typisk 30.000-40.000 kr. i sin sammenligning af typer; Energisparer.dk ca. 12.000-25.000 kr. Den passer bedst til huse med elvarme – det gælder {tal(HEAT['svendborg']['ELV'])} af de {tal(hs('svendborg'))} beboede parcel- og rækkehuse i Svendborg Kommune – men den varmer kun de rum, den kan nå, giver ikke varmt vand og er ikke omfattet af Varmepumpepuljen. Har du gas- eller oliefyr med radiatorer, er en luft til vand-varmepumpe som regel det rigtige valg.", ["se_l2l", "se_vp", "es_vp", "se_vpp", "dst_bol102"])]
# keyword-backlog 12/11 2026: 'luft til vand varmepumpe aalborg' (GSC 20 visninger, pos. 85,2) -> ny H2 + FAQ om luft til vand på /varmepumpe/aalborg/
VP_HEAT["aalborg"] = ("Luft til vand-varmepumpe i Aalborg: hvem står uden for fjernvarmen?", VP_HEAT["aalborg"][1])
VP_XFAQ["aalborg"] = VP_XFAQ["aalborg"] + [("Hvad koster en luft til vand-varmepumpe i Aalborg?", lambda: f"SparEnergi angiver typisk 100.000-130.000 kr. for en luft til vand-varmepumpe, og Energisparer.dk ca. 90.000-150.000 kr. inkl. installation afhængigt af husets størrelse og varmetab. Vi har ikke fundet kilder med en særlig Aalborg-pris. Det er især de {tal(HEAT['aalborg']['CO'])} huse med oliefyr og {tal(HEAT['aalborg']['CN'])} med naturgas i Aalborg Kommune, der typisk allerede har radiatorer, så en luft til vand-varmepumpe kan overtage både rumvarme og varmt vand.", ["se_vp", "es_vp", "es_l2v", "dst_bol102"])]

# ---------- daglig by-rutine 12. nov. 2026: Kalundborg (DK2) og Skive (DK1) ----------
SOL_ORDER.update({
 "kalundborg": ["produktion", "tage", "lokalt", "boliger", "faq", "guides"],
 "skive": ["lokalt", "tage", "faq", "produktion", "boliger", "guides"],
})
VP_ORDER.update({
 "kalundborg": ["opvarmning", "lokalt", "pris", "lokale-byer", "faq", "guides"],
 "skive": ["lokale-byer", "opvarmning", "faq", "lokalt", "pris", "guides"],
})
FV_ORDER.update({
 "kalundborg": ["status", "priser", "andel", "billigst", "faq", "varmekilder"],
 "skive": ["priser", "andel", "status", "billigst", "varmekilder", "faq"],
})
SOL_PROD.update({
 "kalundborg": ("Blandt de solrigeste byer på sitet: produktion i Kalundborg",
   lambda: f"PVGIS beregner ca. <strong>{tal(PV['kalundborg']['syd'])} kWh pr. kWp om året</strong> for et sydvendt tag med 35° hældning i Kalundborg – {rk(_PVY, 'kalundborg', 'højeste')} af de {nw()} byer på dette site. Et 6 kWp-anlæg giver ca. {tal(PV['kalundborg']['syd']*6)} kWh om året, og ved den bedste hældning på {PV['kalundborg']['opt_angle']}° ca. {tal(PV['kalundborg']['opt']*6)} kWh. Maj giver ca. {tal(PV['kalundborg']['months'][4]*6)} kWh og juni ca. {tal(PV['kalundborg']['months'][5]*6)} kWh, december kun ca. {tal(PV['kalundborg']['months'][11]*6)} kWh."),
 "skive": ("Hvor meget giver solceller i Skive?",
   lambda: f"For et sydvendt tag med 35° hældning i Skive beregner PVGIS ca. {tal(PV['skive']['syd'])} kWh pr. kWp om året. Et 6 kWp-anlæg giver dermed ca. {tal(PV['skive']['syd']*6)} kWh om året. Skive ligger i den nordlige del af landet, og PVGIS giver {rk(_PVY, 'skive', 'laveste', rev=True)} produktion af de {nw()}. Mod vest falder det til ca. {tal(PV['skive']['vest'])} og mod øst til ca. {tal(PV['skive']['oest'])} kWh pr. kWp, så sydvendte tagflader betaler sig bedst."),
})
SOL_PROD_SRC_NEW.update({"kalundborg": ["pv_kalundborg", "pvo_kalundborg", "pvv_kalundborg"], "skive": ["pv_skive", "pvo_skive", "pvv_skive"]})
SOL_ROOF.update({
 "kalundborg": ("Mange fibercement-tage i Kalundborg",
   lambda: f"{rp('kalundborg','06')} af parcel- og rækkehusene i Kalundborg Kommune har tag af <strong>fibercement</strong> – {rk(_rt('06'), 'kalundborg', 'højeste')} andel af de {nw()} byer og mod {rp('dk','06')} på landsplan. {rp('kalundborg','10')} har <strong>tegl</strong> og {rp('kalundborg','08')} <strong>cementsten</strong>. Bølgeplader fra før 1984 kan indeholde asbest, så få tagets tilstand vurderet, før der monteres solceller.",
   ["dst_bygb50", "bolius_asb"]),
 "skive": ("Hvert andet hus har fibercement-tag i Skive",
   lambda: f"{rp('skive','06')} af parcel- og rækkehusene i Skive Kommune har tag af <strong>fibercement</strong> – {rk(_rt('06'), 'skive', 'højeste')} andel af de {nw()} byer og mod {rp('dk','06')} på landsplan. Kun {rp('skive','10')} har <strong>tegl</strong> og {rp('skive','08')} <strong>cementsten</strong>. Skive Kommune beder dig undersøge, om tagkonstruktionen kan klare den øgede belastning, og bølgeplader fra før 1984 kan indeholde asbest.",
   ["dst_bygb50", "ski_sol", "bolius_asb"]),
})
SOL_HOMES.update({
 "kalundborg": lambda: f"Kalundborg Kommune har {tal(STOCK['kalundborg']['tot'])} beboede parcel- og rækkehuse, og {pct(STOCK['kalundborg']['B']['før 1960'],STOCK['kalundborg']['tot'])} er bygget før 1960, mod {pct(STOCK['dk']['B']['før 1960'],STOCK['dk']['tot'])} på landsplan. {pct(STOCK['kalundborg']['ejer'],STOCK['kalundborg']['tot'])} bebos af ejeren. Kalundborg by har {tal(town('kalundborg','Kalundborg'))} indbyggere, Høng {tal(town('kalundborg','Høng'))}, Gørlev {tal(town('kalundborg','Gørlev'))}, Svebølle {tal(town('kalundborg','Svebølle'))} og Ubby {tal(town('kalundborg','Ubby'))}. Siden gælder hele kommunen.",
 "skive": lambda: f"Skive Kommune har {tal(STOCK['skive']['tot'])} beboede parcel- og rækkehuse, og {pct(STOCK['skive']['ejer'],STOCK['skive']['tot'])} bebos af ejeren, mod {pct(STOCK['dk']['ejer'],STOCK['dk']['tot'])} på landsplan. Kun {pct(STOCK['skive']['B']['2000+'],STOCK['skive']['tot'])} er bygget i 2000 eller senere, mod {pct(STOCK['dk']['B']['2000+'],STOCK['dk']['tot'])} i hele landet. Skive by har {tal(town('skive','Skive'))} indbyggere, Højslev Stationsby {tal(town('skive','Højslev Stationsby'))}, Glyngøre {tal(town('skive','Glyngøre'))}, Roslev {tal(town('skive','Roslev'))} og Balling {tal(town('skive','Balling'))}. Siden gælder hele kommunen.",
})
SOL_HOMES_SRC_NEW.update({"kalundborg": [], "skive": []})
SOL_HOMES_H.update({"kalundborg": "Huse fra Kalundborg til Høng, Gørlev og Svebølle", "skive": "Huse i Skive, Højslev, Glyngøre og Roslev"})
SOL_XFAQ.update({
 "kalundborg": [("Hvad gør jeg, hvis lokalplanen ikke tillader solceller i Kalundborg?", lambda: "Du kan søge Kalundborg Kommune om dispensation, men kommunen kan kun give dispensation til mindre væsentlige lempelser, der ikke strider mod lokalplanens hovedprincipper. Ellers kræver det en ny lokalplan.", ["kal_lp"])],
 "skive": [("Skal jeg bruge refleksfri solpaneler i Skive?", lambda: "Det er ikke et krav, men Skive Kommune anbefaler altid refleksbehandlede paneler, så genskin ikke generer naboerne.", ["ski_sol"])],
})
VP_HEAT.update({
 "kalundborg": ("Mange huse med elvarme i Kalundborg",
   lambda: f"{tal(HEAT['kalundborg']['ELV'])} af de {tal(hs('kalundborg'))} beboede parcel- og rækkehuse i Kalundborg Kommune ({hp('kalundborg','ELV',1)}) har elvarme – {rk(_hf('ELV'), 'kalundborg', 'højeste')} andel af de {nw()} byer og mod {hp('dk','ELV',1)} på landsplan. {tal(HEAT['kalundborg']['CO'])} har oliefyr og kun {tal(HEAT['kalundborg']['CN'])} naturgas. {tal(HEAT['kalundborg']['VP'])} har allerede varmepumpe ({hp('kalundborg','VP',1)}), og {hp('kalundborg','FJ')} har fjernvarme."),
 "skive": ("Hvert femte hus har naturgas i Skive",
   lambda: f"{tal(HEAT['skive']['CN'])} af de {tal(hs('skive'))} beboede parcel- og rækkehuse i Skive Kommune ({hp('skive','CN',1)}) har naturgas, og {tal(HEAT['skive']['CO'])} ({hp('skive','CO',1)}) har oliefyr – {rk(_hf('CO'), 'skive', 'højeste')} olieandel af de {nw()} byer og mod {hp('dk','CO',1)} på landsplan. {tal(HEAT['skive']['VP'])} har allerede varmepumpe ({hp('skive','VP',1)}), og {hp('skive','FJ')} har fjernvarme."),
})
VP_HEAT_SRC_NEW.update({"kalundborg": ["kal_tv"], "skive": ["ski_sf"]})
VP_TOWNS.update({
 "kalundborg": [("Kalundborg", "Kalundborg Forsyning, varme fra Asnæsværket", ["kal_ff", "ft_pris"]),
                ("Høng / Svebølle / Ubby-Jerslev", "Egne værker: Høng, Svebølle-Viskinge og Hvidebæk", ["ft_pris"]),
                ("Gørlev / Kirke Helsinge", "Fjernvarmeprojekt indstillet (for lav tilslutning)", ["kal_tv"]),
                ("Sæby / Reerslev", "For lille volumen til central varme", ["kal_tv"])],
 "skive": [("Skive", "Skive Fjernvarme udvider frem mod 2028", ["ski_sf", "ft_pris"]),
           ("Roslev / Glyngøre / Durup / Højslev", "Egne værker, Roslev og Glyngøre under landsgennemsnittet", ["ski_kol", "ft_pris"]),
           ("Oddense / Jebjerg / Breum / Hem", "Naturgasbyer; overskudsvarme fra GreenLab undersøges", ["ski_gl"]),
           ("Fur / Ramsing-Lem-Lihme", "Egne værker, blandt de dyreste i landet", ["ft_pris"])],
})
VP_TOWNS_NOTE.update({
 "kalundborg": "Har du gasfyr i Gørlev, Kirke Helsinge, Sæby eller Reerslev, er fjernvarme ikke på vej, og en luft til vand-varmepumpe er det typiske valg. Har du elvarme med paneler, skal der først etableres radiatorer eller gulvvarme – ellers er en luft til luft-varmepumpe det billigere valg.",
 "skive": "Bor du i et af Skive Fjernvarmes udvidelsesområder, så tjek din adresse først. Kommunen anbefaler at lease en varmepumpe i områder, hvor der på sigt kommer fjernvarme. I landsbyer langt fra et net kan et termonet eller en luft til vand-varmepumpe være løsningen.",
})
VP_XFAQ.update({
 "kalundborg": [("Hvor mange huse i Kalundborg Kommune har elvarme?", lambda: f"{tal(HEAT['kalundborg']['ELV'])} af de {tal(hs('kalundborg'))} beboede parcel- og rækkehuse ({hp('kalundborg','ELV',1)}) ifølge Danmarks Statistik, 2026. {tal(HEAT['kalundborg']['CO'])} har oliefyr, og {tal(HEAT['kalundborg']['VP'])} har allerede varmepumpe.", ["dst_bol102"])],
 "skive": [("Hvor mange huse i Skive Kommune har naturgas?", lambda: f"{tal(HEAT['skive']['CN'])} af de {tal(hs('skive'))} beboede parcel- og rækkehuse ({hp('skive','CN',1)}) ifølge Danmarks Statistik, 2026. {tal(HEAT['skive']['CO'])} har oliefyr, og {tal(HEAT['skive']['VP'])} har allerede varmepumpe.", ["dst_bol102"])],
})
FV_SOURCES.update({
 "kalundborg": [("Kalundborg Forsynings fjernvarme kommer fra <strong>Asnæsværket</strong>, hvor varmen laves sammen med el og damp, så brændslet – flis – udnyttes bedst muligt.", ["kal_ff"]),
                ("En <strong>akkumuleringstank på over 60 meter</strong> ved Asnæsværket rummer varmt fjernvarmevand til en uges forbrug om sommeren.", ["kal_ff"])],
 "skive": [("GreenLab Skive forventer at kunne levere store mængder <strong>overskudsvarme fra brintproduktion</strong>, som kan bruges til at konvertere naturgasbyer i Skive og Morsø Kommune.", ["ski_gl"]),
           ("Overskudsvarmen kan ikke dække de koldeste perioder alene, så et nærliggende værk eller lokale enheder som varmepumper eller elkedler skal også producere varme.", ["ski_gl"])],
})
FV_SHARE.update({
 "kalundborg": lambda: f"{hp('kalundborg','FJ',1)} af de beboede parcel- og rækkehuse i Kalundborg Kommune har fjernvarme, mod {hp('dk','FJ',1)} i hele landet. {hp('kalundborg','ELV',1)} har elvarme og {hp('kalundborg','VP',1)} varmepumpe.",
 "skive": lambda: f"{hp('skive','FJ',1)} af de beboede parcel- og rækkehuse i Skive Kommune har fjernvarme, mod {hp('dk','FJ',1)} i hele landet. {hp('skive','CN',1)} har naturgas og {hp('skive','CO',1)} oliefyr.",
})
FV_SOURCES_H.update({"kalundborg": "Flis på Asnæsværket og en 60 meter høj varmetank", "skive": "Overskudsvarme fra GreenLab og lokale værker"})
_reg_age_old16 = reg_age_note
def reg_age_note(c, kommune):
    s = STOCK[c]; B = s["B"]; t = s["tot"]
    if c == "kalundborg":
        return (f"{tal(B['før 1960'])} af de beboede huse i Kalundborg Kommune ({pct(B['før 1960'], t)}) er bygget før 1960. Ældre kvarterer er ofte omfattet af lokalplaner eller byplanvedtægter med krav til, hvordan husene skal se ud – søg din adresse på kommunens kort, før du bestiller.", ["kal_lp"])
    if c == "skive":
        return (f"{tal(B['før 1960'])} af de beboede huse i Skive Kommune ({pct(B['før 1960'], t)}) er bygget før 1960. Lokalplaner, byplanvedtægter og deklarationer kan stille krav til farve, materiale og blankhed på taget, og strider anlægget mod dem, skal du søge dispensation, før du går i gang.", ["ski_sol"])
    return _reg_age_old16(c, kommune)


# ---------- daglig by-rutine 13. nov. 2026: Gladsaxe og Kongens Lyngby (hovedstadsområdet, DK2) ----------
VP_XFAQ["silkeborg"] = VP_XFAQ["silkeborg"] + [("Hvad koster en varmepumpe i Silkeborg?", lambda: "SparEnergi angiver typisk 100.000-130.000 kr. inkl. montering for en luft til vand-varmepumpe, og Energisparer.dk ca. 90.000-150.000 kr. afhængigt af husets størrelse. Vi har ikke fundet kilder med en særlig Silkeborg-pris. Ligger huset i Silkeborg Syd eller et andet område med planlagt fjernvarme, så tjek tidsplanen hos Silkeborg Forsyning, før du køber.", ["se_vp", "es_vp", "es_l2v", "sil_syd"])]
_GLA_T = "Gladsaxe (kommunens del af hovedstadsområdet)"; _LYN_T = "Lyngby-Taarbæk (kommunens del af hovedstadsområdet)"
_RK = lambda c: STOCK[c]["raekke"] / STOCK[c]["tot"]
SOL_ORDER.update({"gladsaxe": ["boliger", "lokalt", "tage", "produktion", "faq", "guides"],
                  "kongens-lyngby": ["tage", "lokalt", "faq", "boliger", "produktion", "guides"]})
VP_ORDER.update({"gladsaxe": ["lokalt", "opvarmning", "faq", "pris", "lokale-byer", "guides"],
                 "kongens-lyngby": ["opvarmning", "lokale-byer", "lokalt", "faq", "pris", "guides"]})
FV_ORDER.update({"gladsaxe": ["status", "andel", "priser", "faq", "billigst", "varmekilder"],
                 "kongens-lyngby": ["andel", "status", "varmekilder", "priser", "billigst", "faq"]})
SOL_PROD.update({
 "gladsaxe": ("Solceller i Gladsaxe: produktion pr. måned",
   lambda: f"PVGIS beregner ca. {tal(PV['gladsaxe']['syd'])} kWh pr. kWp om året for et sydvendt tag med 35° hældning i Gladsaxe. Den bedste hældning er {PV['gladsaxe']['opt_angle']}°, hvor det giver ca. {tal(PV['gladsaxe']['opt'])} kWh. Et 6 kWp-anlæg på et sydvendt tag giver ca. {tal(PV['gladsaxe']['syd']*6)} kWh om året – ca. {tal(PV['gladsaxe']['months'][4]*6)} kWh i maj, men kun {tal(PV['gladsaxe']['months'][11]*6)} kWh i december. På et øst-vest-tag, som mange rækkehuse har, giver hver side ca. {tal(PV['gladsaxe']['oest'])}-{tal(PV['gladsaxe']['vest'])} kWh pr. kWp."),
 "kongens-lyngby": ("Hvor meget giver solceller i Kongens Lyngby?",
   lambda: f"For et sydvendt tag med 35° hældning i Kongens Lyngby beregner PVGIS ca. {tal(PV['kongens-lyngby']['syd'])} kWh pr. kWp om året, så et 6 kWp-anlæg giver ca. {tal(PV['kongens-lyngby']['syd']*6)} kWh. Mod øst falder det til ca. {tal(PV['kongens-lyngby']['oest'])} og mod vest til ca. {tal(PV['kongens-lyngby']['vest'])} kWh pr. kWp. Juni giver ca. {tal(PV['kongens-lyngby']['months'][5]*6)} kWh fra et 6 kWp-anlæg og januar ca. {tal(PV['kongens-lyngby']['months'][0]*6)} kWh."),
})
SOL_PROD_SRC_NEW.update({"gladsaxe": ["pv_gladsaxe", "pvo_gladsaxe", "pvv_gladsaxe"], "kongens-lyngby": ["pv_kongens-lyngby", "pvo_kongens-lyngby", "pvv_kongens-lyngby"]})
SOL_ROOF.update({
 "gladsaxe": ("Tegl og fibercement på Gladsaxes tage",
   lambda: f"{rp('gladsaxe','10')} af parcel- og rækkehusene i Gladsaxe Kommune har <strong>tegltag</strong> – {rk(_rt('10'), 'gladsaxe', 'højeste')} andel af de {nw()} byer og mod {rp('dk','10')} på landsplan. {rp('gladsaxe','06')} har <strong>fibercement</strong>, og {pct(_flat('gladsaxe'), ROOF['gladsaxe']['tot'])} har fladt tag eller tagpap. På et fladt tag monteres panelerne på et stativ, og bølgeplader fra før 1984 kan indeholde asbest.",
   ["dst_bygb50", "bolius_asb", "bolius_mont"]),
 "kongens-lyngby": ("Over halvdelen tegltage: tagene i Kongens Lyngby",
   lambda: f"{rp('kongens-lyngby','10')} af parcel- og rækkehusene i Lyngby-Taarbæk Kommune har <strong>tegltag</strong> – {rk(_rt('10'), 'kongens-lyngby', 'højeste')} andel af de {nw()} byer på dette site og mod {rp('dk','10')} på landsplan. {pct(_flat('kongens-lyngby'), ROOF['kongens-lyngby']['tot'])} har fladt tag eller tagpap, og kun {rp('kongens-lyngby','06')} har fibercement. Kommuneplanen kræver, at tagmateriale højst har glansværdi 15.",
   ["dst_bygb50", "lyn_kp", "bolius_mont"]),
})
SOL_HOMES.update({
 "gladsaxe": lambda: f"Gladsaxe Kommune har {tal(STOCK['gladsaxe']['tot'])} beboede parcel- og rækkehuse, og {tal(STOCK['gladsaxe']['raekke'])} af dem ({pct(STOCK['gladsaxe']['raekke'],STOCK['gladsaxe']['tot'])}) er række-, kæde- eller dobbelthuse – {rk(_RK, 'gladsaxe', 'højeste')} andel af de {nw()} byer og mod {pct(STOCK['dk']['raekke'],STOCK['dk']['tot'])} på landsplan. Netop her skal du kontakte Byggesag, før du sætter solceller op. {pct(STOCK['gladsaxe']['B']['før 1960'],STOCK['gladsaxe']['tot'])} af husene er bygget før 1960. Gladsaxe-delen af hovedstadsområdet har {tal(town('gladsaxe', _GLA_T))} indbyggere, og siden gælder hele kommunen, også Søborg, Buddinge, Mørkhøj og Bagsværd.",
 "kongens-lyngby": lambda: f"Lyngby-Taarbæk Kommune har {tal(STOCK['kongens-lyngby']['tot'])} beboede parcel- og rækkehuse, og {pct(STOCK['kongens-lyngby']['ejer'],STOCK['kongens-lyngby']['tot'])} bebos af ejeren – {rk(_EJ, 'kongens-lyngby', 'højeste')} andel af de {nw()} byer. {pct(STOCK['kongens-lyngby']['B']['før 1960'],STOCK['kongens-lyngby']['tot'])} er bygget før 1960, mod {pct(STOCK['dk']['B']['før 1960'],STOCK['dk']['tot'])} på landsplan, og en del af dem har høj bevaringsværdi. Kommunens del af hovedstadsområdet har {tal(town('kongens-lyngby', _LYN_T))} indbyggere, og siden gælder hele kommunen, også Virum, Sorgenfri, Lundtofte og Taarbæk.",
})
SOL_HOMES_SRC_NEW.update({"gladsaxe": ["gla_byg"], "kongens-lyngby": ["lyn_kp"]})
SOL_HOMES_H.update({"gladsaxe": "Rækkehuse og villaer i Gladsaxe Kommune", "kongens-lyngby": "Ældre ejerboliger i Lyngby-Taarbæk"})
SOL_XFAQ.update({
 "gladsaxe": [("Hvor mange huse i Gladsaxe er rækkehuse?", lambda: f"{tal(STOCK['gladsaxe']['raekke'])} af de {tal(STOCK['gladsaxe']['tot'])} beboede parcel- og rækkehuse i Gladsaxe Kommune er række-, kæde- eller dobbelthuse ifølge Danmarks Statistik, 2026. Ved dobbelt- og rækkehuse skal du kontakte Byggesag, før du sætter solceller op.", ["dst_bol101", "gla_byg"])],
 "kongens-lyngby": [("Kan jeg få en gratis snak med kommunen om solceller i Lyngby?", lambda: "Ja. Lyngby-Taarbæk Kommune tilbyder en forhåndsdialog på 30 minutter, som er gratis. Den kan bookes, når kommunen har kapacitet, og byggesagsvagten kan også kontaktes alle hverdage på 45 97 38 87.", ["lyn_byg"])],
})
VP_HEAT.update({
 "gladsaxe": ("Næsten hvert andet hus har naturgas i Gladsaxe",
   lambda: f"{tal(HEAT['gladsaxe']['CN'])} af de {tal(hs('gladsaxe'))} beboede parcel- og rækkehuse i Gladsaxe Kommune ({hp('gladsaxe','CN',1)}) har naturgas, mod {hp('dk','CN',1)} på landsplan, og {tal(HEAT['gladsaxe']['FJ'])} ({hp('gladsaxe','FJ',1)}) har fjernvarme. Kun {tal(HEAT['gladsaxe']['VP'])} ({hp('gladsaxe','VP',1)}) har varmepumpe. Kommunen skriver, at fjernvarmen i dag dækker ca. 60 % af varmebehovet og skal op på næsten 100 % i 2030."),
 "kongens-lyngby": ("Flest gasfyr på sitet: varmen i Kongens Lyngby",
   lambda: f"{tal(HEAT['kongens-lyngby']['CN'])} af de {tal(hs('kongens-lyngby'))} beboede parcel- og rækkehuse i Lyngby-Taarbæk Kommune ({hp('kongens-lyngby','CN',1)}) har naturgas – {rk(_hf('CN'), 'kongens-lyngby', 'højeste')} andel af de {nw()} byer og mod {hp('dk','CN',1)} på landsplan. Kun {hp('kongens-lyngby','FJ',1)} har fjernvarme, og {tal(HEAT['kongens-lyngby']['VP'])} ({hp('kongens-lyngby','VP',1)}) har allerede varmepumpe."),
})
VP_HEAT_SRC_NEW.update({"gladsaxe": ["gla_fv"], "kongens-lyngby": []})
VP_TOWNS.update({
 "gladsaxe": [("Syd i kommunen", "Gentofte Gladsaxe Fjernvarme, ca. 5.000 bygninger", ["gla_ggf", "ft_pris"]),
              ("Nord for Motorring 3 / vest for Stengårds Allé", "Vestforbrænding, ca. 4.000 bygninger", ["gla_fv", "gla_ggf", "ft_pris"]),
              ("Høje Gladsaxe", "Fællesdriften af Høje Gladsaxe", ["ft_pris"]),
              ("Nybrovej (spredte bygninger)", "Endnu ikke omfattet af projektforslag", ["gla_ggf"])],
 "kongens-lyngby": [("Virum / Sorgenfri (C1)", "Vestforbrænding, alle tilbudt senest 2025", ["lyn_fvng"]),
                    ("Lyngby / Lundtofte / Jægersborg", "Vestforbrænding etape 2, graveopstart 2026", ["lyn_info", "lyn_pdf"]),
                    ("Åbrinken", "Norfors", ["lyn_fvng", "ft_pris"]),
                    ("Spring Forbi / Raadvad / Frederiksdal", "Ingen fjernvarme – varmepumpe eller termonet", ["lyn_fvng"])],
})
VP_TOWNS_NOTE.update({
 "gladsaxe": "Fjernvarmen er planlagt til stort set hele kommunen, så for de fleste gasfyr handler valget om timing. Går fyret i stykker, før fjernvarmen kommer, nævner kommunen en midlertidig varmepumpe som en mulighed. Er huset ikke omfattet af et projektforslag, er en luft til vand-varmepumpe det typiske valg.",
 "kongens-lyngby": "Har du gasfyr i Spring Forbi, Raadvad, Bakken, Frederiksdal, Ny Frederiksdal eller det østlige Virum ved Mølleåen, kommer der ikke fjernvarme, og kommunen peger på varmepumpe eller termonet. Vælger du jordvarme, kræver anlægget altid tilladelse.",
})
VP_XFAQ.update({
 "gladsaxe": [("Hvor mange huse i Gladsaxe Kommune har naturgas?", lambda: f"{tal(HEAT['gladsaxe']['CN'])} af de {tal(hs('gladsaxe'))} beboede parcel- og rækkehuse ({hp('gladsaxe','CN',1)}) ifølge Danmarks Statistik, 2026. {tal(HEAT['gladsaxe']['FJ'])} har fjernvarme, og {tal(HEAT['gladsaxe']['VP'])} har allerede varmepumpe.", ["dst_bol102"])],
 "kongens-lyngby": [("Hvor mange huse i Lyngby-Taarbæk har naturgas?", lambda: f"{tal(HEAT['kongens-lyngby']['CN'])} af de {tal(hs('kongens-lyngby'))} beboede parcel- og rækkehuse ({hp('kongens-lyngby','CN',1)}) ifølge Danmarks Statistik, 2026. {tal(HEAT['kongens-lyngby']['FJ'])} har fjernvarme, og {tal(HEAT['kongens-lyngby']['VP'])} har allerede varmepumpe.", ["dst_bol102"]),
                    ("Hvad koster en luft til vand-varmepumpe i Kongens Lyngby?", lambda: "SparEnergi angiver typisk 100.000-130.000 kr. inkl. montering, og Energisparer.dk ca. 90.000-150.000 kr. afhængigt af husets størrelse. Vi har ikke fundet kilder med en særlig Lyngby-pris. Ligger din adresse i et af Vestforbrændings udrulningsområder, så sammenlign med fjernvarmetilslutningen, der koster 15.000 kr. i kampagneperioden.", ["se_vp", "es_vp", "lyn_pdf"])],
})
FV_SOURCES.update({
 "gladsaxe": [("Omtrent <strong>80 %</strong> af fjernvarmens energi i Gladsaxe Kommune kommer fra halm, flis, affald og samproduktion med el, og andelen stiger år for år.", ["gla_fv"]),
              ("Vestforbrændings fjernvarme nord for Motorring 3 stammer primært fra <strong>affaldsforbrænding</strong>.", ["gla_fv"])],
 "kongens-lyngby": [("Der arbejdes på et <strong>geotermianlæg</strong>, som skal forsyne 10.000 kunder i Virum-området, og i etape 2 ses der på overskudsvarme fra Mølleåværket.", ["lyn_fvng"]),
                    ("Vestforbrænding vil gøre fjernvarmen klimaneutral i 2030, bl.a. med CO2-fangst på affaldsforbrændingsanlægget i Glostrup.", ["lyn_fvng"])],
})
FV_SHARE.update({
 "gladsaxe": lambda: f"{hp('gladsaxe','FJ',1)} af de beboede parcel- og rækkehuse i Gladsaxe Kommune har fjernvarme, mod {hp('dk','FJ',1)} i hele landet. {hp('gladsaxe','CN',1)} har naturgas, så udbygningen frem mod 2029 rammer mange huse.",
 "kongens-lyngby": lambda: f"{hp('kongens-lyngby','FJ',1)} af de beboede parcel- og rækkehuse i Lyngby-Taarbæk Kommune har fjernvarme, mod {hp('dk','FJ',1)} i hele landet. {hp('kongens-lyngby','CN',1)} har naturgas.",
})
FV_SOURCES_H.update({"gladsaxe": "Halm, flis, affald og samproduktion", "kongens-lyngby": "Geotermi i Virum og affaldsvarme"})
_reg_age_old17 = reg_age_note
def reg_age_note(c, kommune):
    s = STOCK[c]; B = s["B"]; t = s["tot"]
    if c == "gladsaxe":
        return (f"{tal(B['før 1960'])} af de beboede huse i Gladsaxe Kommune ({pct(B['før 1960'], t)}) er bygget før 1960. Slå husets bevaringsværdi op hos Slots- og Kulturstyrelsen: ved værdi 1-4 skal du kontakte Byggesag, før du går i gang.", ["gla_byg"])
    if c == "kongens-lyngby":
        return (f"{tal(B['før 1960'])} af de beboede huse i Lyngby-Taarbæk Kommune ({pct(B['før 1960'], t)}) er bygget før 1960. Ejendomme med høj bevaringsværdi (SAVE 1-3) er udpeget som bevaringsværdige i kommuneplanen, og kommunen vil gerne se projektet, før du går i gang.", ["lyn_kp", "lyn_byg"])
    return _reg_age_old17(c, kommune)

# ---------- daglig by-rutine 16. nov. 2026: Holstebro (DK1) og Fredensborg (DK2) ----------
_FRE_K = "Hørsholm-byområdet (delen i Fredensborg Kommune, Kokkedal)"
SOL_ORDER.update({"holstebro": ["lokalt", "produktion", "boliger", "faq", "tage", "guides"],
                  "fredensborg": ["boliger", "tage", "lokalt", "produktion", "faq", "guides"]})
VP_ORDER.update({"holstebro": ["opvarmning", "lokalt", "lokale-byer", "pris", "faq", "guides"],
                 "fredensborg": ["lokalt", "lokale-byer", "opvarmning", "faq", "pris", "guides"]})
FV_ORDER.update({"holstebro": ["priser", "andel", "status", "varmekilder", "faq", "billigst"],
                 "fredensborg": ["status", "priser", "billigst", "andel", "varmekilder", "faq"]})
SOL_PROD.update({
 "holstebro": ("Hvad giver solceller i Holstebro?",
   lambda: f"PVGIS beregner ca. {tal(PV['holstebro']['syd'])} kWh pr. kWp om året for et sydvendt tag med 35° hældning i Holstebro – {rk(lambda x: PV[x]['syd'], 'holstebro', 'laveste', rev=True)} værdi af de {nw()} byer. Et 6 kWp-anlæg giver dermed ca. {tal(PV['holstebro']['syd']*6)} kWh om året, heraf ca. {tal(PV['holstebro']['months'][5]*6)} kWh i juni og kun {tal(PV['holstebro']['months'][11]*6)} kWh i december. Vender taget mod vest, giver det ca. {tal(PV['holstebro']['vest'])} kWh pr. kWp, mod øst ca. {tal(PV['holstebro']['oest'])}."),
 "fredensborg": ("Solproduktion i Fredensborg Kommune",
   lambda: f"I Fredensborg giver et sydvendt tag med 35° hældning ca. {tal(PV['fredensborg']['syd'])} kWh pr. kWp om året ifølge PVGIS, og ved den bedste hældning på {PV['fredensborg']['opt_angle']}° ca. {tal(PV['fredensborg']['opt'])} kWh. Et 6 kWp-anlæg giver ca. {tal(PV['fredensborg']['syd']*6)} kWh om året. Mange rækkehuse har tagflader mod øst og vest; her giver hver kWp ca. {tal(PV['fredensborg']['oest'])}-{tal(PV['fredensborg']['vest'])} kWh, og kommunen nævner selv, at øst-vest-tage passer godt til forbruget morgen og aften."),
})
SOL_PROD_SRC_NEW.update({"holstebro": ["pv_holstebro", "pvo_holstebro", "pvv_holstebro"], "fredensborg": ["pv_fredensborg", "pvo_fredensborg", "pvv_fredensborg", "fre_sol"]})
SOL_ROOF.update({
 "holstebro": ("Fibercement og cementsten dominerer tagene i Holstebro",
   lambda: f"{rp('holstebro','06')} af parcel- og rækkehusene i Holstebro Kommune har <strong>fibercement</strong> og {rp('holstebro','08')} <strong>cementsten</strong>, mens kun {rp('holstebro','10')} har tegltag – {rk(_rt('10'), 'holstebro', 'laveste', rev=True)} andel af de {nw()} byer og mod {rp('dk','10')} på landsplan. Bølgeplader fra før 1984 kan indeholde asbest, så få taget vurderet, før der monteres solceller.",
   ["dst_bygb50", "bolius_asb", "bolius_mont"]),
 "fredensborg": ("Tegl, tagpap og flade tage i Fredensborg",
   lambda: f"{rp('fredensborg','10')} af parcel- og rækkehusene i Fredensborg Kommune har <strong>tegltag</strong>, og {pct(_flat('fredensborg'), ROOF['fredensborg']['tot'])} har fladt tag eller tagpap. Kun {rp('fredensborg','06')} har fibercement – {rk(_rt('06'), 'fredensborg', 'laveste', rev=True)} andel af de {nw()} byer og mod {rp('dk','06')} på landsplan. På flade tage monteres panelerne på stativ, og ved dispensation anbefaler kommunen matte paneler, der følger tagfladen.",
   ["dst_bygb50", "fre_sol", "bolius_mont"]),
})
SOL_HOMES.update({
 "holstebro": lambda: f"Holstebro Kommune har {tal(STOCK['holstebro']['tot'])} beboede parcel- og rækkehuse, og {pct(STOCK['holstebro']['B']['2000+'],STOCK['holstebro']['tot'])} af dem er bygget i 2000 eller senere – {rk(_sb('2000+'), 'holstebro', 'højeste')} andel af de {nw()} byer og mod {pct(STOCK['dk']['B']['2000+'],STOCK['dk']['tot'])} på landsplan. {pct(STOCK['holstebro']['ejer'],STOCK['holstebro']['tot'])} bebos af ejeren. Holstebro by har {tal(town('holstebro','Holstebro'))} indbyggere, Vinderup {tal(town('holstebro','Vinderup'))} og Ulfborg {tal(town('holstebro','Ulfborg'))}.",
 "fredensborg": lambda: f"Fredensborg Kommune har {tal(STOCK['fredensborg']['tot'])} beboede parcel- og rækkehuse, og {tal(STOCK['fredensborg']['raekke'])} af dem ({pct(STOCK['fredensborg']['raekke'],STOCK['fredensborg']['tot'])}) er række-, kæde- eller dobbelthuse – {rk(_RK, 'fredensborg', 'højeste')} andel af de {nw()} byer og mod {pct(STOCK['dk']['raekke'],STOCK['dk']['tot'])} på landsplan. {pct(STOCK['fredensborg']['B']['1960-1979'],STOCK['fredensborg']['tot'])} er bygget 1960-1979. De største byområder er Kokkedal-delen af Hørsholm-byområdet ({tal(town('fredensborg', _FRE_K))} indbyggere), Humlebæk ({tal(town('fredensborg','Humlebæk'))}), Fredensborg ({tal(town('fredensborg','Fredensborg'))}) og Nivå ({tal(town('fredensborg','Nivå'))}).",
})
SOL_HOMES_SRC_NEW.update({"holstebro": ["dst_by3"], "fredensborg": ["dst_by3"]})
SOL_HOMES_H.update({"holstebro": "Mange nyere huse i Holstebro Kommune", "fredensborg": "Flest rækkehuse på sitet: boligerne i Fredensborg Kommune"})
SOL_XFAQ.update({
 "holstebro": [("Hvor meget strøm giver et 6 kWp-anlæg i Holstebro?", lambda: f"Ca. {tal(PV['holstebro']['syd']*6)} kWh om året på et sydvendt tag med 35° hældning ifølge PVGIS 5.3. Vender taget mod vest, er det ca. {tal(PV['holstebro']['vest']*6)} kWh, og mod øst ca. {tal(PV['holstebro']['oest']*6)} kWh.", ["pv_holstebro", "pvo_holstebro", "pvv_holstebro"])],
 "fredensborg": [("Gælder der særlige regler for solceller på rækkehuse i Fredensborg?", lambda: "Tjek lokalplan, byplanvedtægt og tinglyste deklarationer for din bebyggelse: indeholder de bestemmelser om tagmaterialer eller anlæg til vedvarende energi, kan det kræve dispensation. Kommunen går gerne i dialog med grundejerforeninger i områder, hvor der opleves barrierer for solceller.", ["fre_sol"])],
})
VP_HEAT.update({
 "holstebro": ("Fjernvarme i fire ud af fem huse i Holstebro",
   lambda: f"{tal(HEAT['holstebro']['FJ'])} af de {tal(hs('holstebro'))} beboede parcel- og rækkehuse i Holstebro Kommune ({hp('holstebro','FJ',1)}) har fjernvarme – {rk(_hf('FJ'), 'holstebro', 'højeste')} andel af de {nw()} byer. Kun {tal(HEAT['holstebro']['CN'])} ({hp('holstebro','CN',1)}) har naturgas, mens {tal(HEAT['holstebro']['CO'])} ({hp('holstebro','CO',1)}) stadig har oliefyr og {tal(HEAT['holstebro']['VP'])} ({hp('holstebro','VP',1)}) varmepumpe, mod {hp('dk','VP',1)} på landsplan."),
 "fredensborg": ("Gas og fjernvarme næsten lige store i Fredensborg",
   lambda: f"{tal(HEAT['fredensborg']['CN'])} af de {tal(hs('fredensborg'))} beboede parcel- og rækkehuse i Fredensborg Kommune ({hp('fredensborg','CN',1)}) har naturgas og {tal(HEAT['fredensborg']['FJ'])} ({hp('fredensborg','FJ',1)}) fjernvarme. {tal(HEAT['fredensborg']['VP'])} ({hp('fredensborg','VP',1)}) har allerede varmepumpe, og {tal(HEAT['fredensborg']['ELV'])} ({hp('fredensborg','ELV',1)}) har elvarme – {rk(_hf('ELV'), 'fredensborg', 'højeste')} andel af de {nw()} byer."),
})
VP_HEAT_SRC_NEW.update({"holstebro": ["hol_varme"], "fredensborg": ["fre_fv"]})
VP_TOWNS.update({
 "holstebro": [("Holstebro", "Vestforsyning Varme", ["hol_varme", "hol_vfomr", "ft_pris"]),
               ("Vinderup", "Vinderup Varmeværk", ["hol_varme", "ft_pris"]),
               ("Ulfborg", "Ulfborg Fjernvarmeværk", ["hol_varme", "ft_pris"]),
               ("Tvis", "Vestforsyning (vekslerstation i Tvis)", ["hol_vfomr"]),
               ("Vemb", "Vemb Varmeværk", ["hol_varme"]),
               ("Thorsminde", "Thorsminde Varmeværk", ["hol_varme", "ft_pris"]),
               ("Ejsing", "Ejsing Fjernvarme", ["hol_varme", "ft_pris"])],
 "fredensborg": [(_FRE_K, "Norfors; områder godkendt 2024 venter på nye varmeanlæg", ["fre_monrad"]),
                 ("Humlebæk", "Norfors; nye områder fra 2024 forsynes fra Helsingør", ["fre_monrad"]),
                 ("Fredensborg", "Projekterne i byen og Fredensborg Øst annulleret okt. 2026", ["fre_es", "fre_humle"]),
                 ("Nivå", "Norfors; kun Nivå Bymidte udbygges", ["fre_monrad", "fre_nivaa"])],
})
VP_TOWNS_NOTE.update({
 "holstebro": "Holstebro by og de større omegnsbyer har fjernvarme fra Vestforsyning, og fem mindre byer har egne værker. Varmepumpen er derfor især relevant i de mindre landsbyer og i det åbne land, hvor der hverken er fjernvarme eller gas – og for de huse, der stadig har oliefyr.",
 "fredensborg": "I Fredensborg by er der efter byrådets beslutning ingen fjernvarme på vej, og i Nivå udbygges kun bymidten. Her er en luft til vand-varmepumpe det oplagte skifte fra gas. Bor du i rækkehus, så husk kommunens støjgrænse på 35 dB i skel om natten – flere varmepumper tæt på hinanden kan give cikadeeffekt.",
})
VP_XFAQ.update({
 "holstebro": [("Hvor mange huse i Holstebro har oliefyr?", lambda: f"{tal(HEAT['holstebro']['CO'])} af de {tal(hs('holstebro'))} beboede parcel- og rækkehuse i Holstebro Kommune ({hp('holstebro','CO',1)}) ifølge Danmarks Statistik, 2026. Hertil kommer {tal(HEAT['holstebro']['ELV'])} med elvarme. Det er især disse huse uden for fjernvarmenettet, hvor en varmepumpe kan give mening.", ["dst_bol102"]),
               ("Hvad koster en luft til vand-varmepumpe i Holstebro?", lambda: "SparEnergi angiver typisk 100.000-130.000 kr. inkl. montering, og Energisparer.dk ca. 90.000-150.000 kr. afhængigt af husets størrelse. Vi har ikke fundet kilder med en særlig Holstebro-pris. Til sammenligning koster et standardhus 14.846 kr. om året i fjernvarme hos Vestforsyning ifølge Forsyningstilsynet.", ["se_vp", "es_vp", "ft_pris"])],
 "fredensborg": [("Hvor mange huse i Fredensborg Kommune har naturgas?", lambda: f"{tal(HEAT['fredensborg']['CN'])} af de {tal(hs('fredensborg'))} beboede parcel- og rækkehuse ({hp('fredensborg','CN',1)}) ifølge Danmarks Statistik, 2026. {tal(HEAT['fredensborg']['FJ'])} har fjernvarme, og {tal(HEAT['fredensborg']['VP'])} har allerede varmepumpe.", ["dst_bol102"]),
                 ("Hvad koster en luft til vand-varmepumpe i Fredensborg?", lambda: "SparEnergi angiver typisk 100.000-130.000 kr. inkl. montering, og Energisparer.dk ca. 90.000-150.000 kr. afhængigt af husets størrelse. Vi har ikke fundet kilder med en særlig Fredensborg-pris. Norfors' beregning for Fredensborg By og Fredensborg Øst viste, at fjernvarmen samlet ville blive 10,2 mio. kr. (3,2 %) dyrere end individuelle luft til vand-varmepumper over 20 år.", ["se_vp", "es_vp", "fre_es"])],
})
FV_SOURCES.update({
 "holstebro": [("Varmen kommer primært fra <strong>MEC – BioHeat & Power</strong>, der producerer varme af lokale energikilder som affald, halm og flis.", ["hol_vfomr"]),
               ("Varmen fordeles via fem vekslerstationer i Holstebro og stationer i <strong>Mejrup og Tvis</strong>; varmecentraler dækker vinterbehovet og udfald på kraftvarmeværket.", ["hol_vfomr"])],
 "fredensborg": [("Der kan ikke produceres mere varme på <strong>Usserødværket</strong>, og den nye affaldslov har gjort værkets fremtid uafklaret, så udvidelser er sat midlertidigt på pause.", ["fre_monrad"]),
                 ("Norfors undersøger <strong>geotermi og store varmepumper</strong> og forbereder et større ledningsnet, der kan føre varme rundt i forsyningsområdet.", ["fre_monrad"])],
})
FV_SHARE.update({
 "holstebro": lambda: f"{hp('holstebro','FJ',1)} af de beboede parcel- og rækkehuse i Holstebro Kommune har fjernvarme, mod {hp('dk','FJ',1)} i hele landet. Kun {hp('holstebro','CN',1)} har naturgas.",
 "fredensborg": lambda: f"{hp('fredensborg','FJ',1)} af de beboede parcel- og rækkehuse i Fredensborg Kommune har fjernvarme, mod {hp('dk','FJ',1)} i hele landet. {hp('fredensborg','CN',1)} har naturgas.",
})
FV_SOURCES_H.update({"holstebro": "Affald, halm og flis fra Måbjerg", "fredensborg": "Usserødværket på pause og nye varmekilder"})
# Keyword 16/11 2026: 'varmepumpe slagelse' (GSC 1.-7/11)
VP_XFAQ["slagelse"] = VP_XFAQ.get("slagelse", []) + [("Hvad koster en varmepumpe i Slagelse?", lambda: "SparEnergi angiver typisk 100.000-130.000 kr. inkl. montering for en luft til vand-varmepumpe, og Energisparer.dk ca. 90.000-150.000 kr. afhængigt af husets størrelse. Vi har ikke fundet kilder med en særlig Slagelse-pris. Bor du i Skælskør, Vemmelev, Forlev eller Sørbymagle, hvor fjernvarmeprojekterne er droppet, er en varmepumpe det typiske alternativ til gas og olie.", ["se_vp", "es_vp"])]
_reg_age_old18 = reg_age_note
def reg_age_note(c, kommune):
    s = STOCK[c]; B = s["B"]; t = s["tot"]
    if c == "holstebro":
        return (f"{tal(B['før 1960'])} af de beboede huse i Holstebro Kommune ({pct(B['før 1960'], t)}) er bygget før 1960. Kommunen henviser til kulturarv.dk, hvor du kan se, om huset er fredet eller bevaringsværdigt, og til Plandata.dk for lokalplaner og byplanvedtægter.", ["hol_byg"])
    if c == "fredensborg":
        return (f"Kun {tal(B['før 1960'])} af de beboede huse i Fredensborg Kommune ({pct(B['før 1960'], t)}) er bygget før 1960 – {rk(_sb('før 1960'), 'fredensborg', 'laveste', rev=True)} andel af de {nw()} byer. Bevaringsværdige bygninger kan ses på kommunens kort, og ved SAVE 1-4 gives der som udgangspunkt ikke tilladelse til solceller.", ["fre_sol"])
    return _reg_age_old18(c, kommune)

# ---------- daglig by-rutine 17. nov. 2026: Nakskov (DK2, Lolland Kommune) og Assens (DK1) ----------
SOL_ORDER.update({"nakskov": ["produktion", "lokalt", "tage", "boliger", "faq", "guides"],
                  "assens": ["lokalt", "boliger", "produktion", "tage", "faq", "guides"]})
VP_ORDER.update({"nakskov": ["opvarmning", "faq", "lokalt", "lokale-byer", "pris", "guides"],
                 "assens": ["lokalt", "opvarmning", "pris", "lokale-byer", "faq", "guides"]})
FV_ORDER.update({"nakskov": ["priser", "status", "varmekilder", "billigst", "andel", "faq"],
                 "assens": ["status", "andel", "priser", "faq", "varmekilder", "billigst"]})
SOL_PROD.update({
 "nakskov": ("Næsten mest sol af byerne på sitet",
   lambda: f"PVGIS beregner ca. {tal(PV['nakskov']['syd'])} kWh pr. kWp om året for et sydvendt tag med 35° hældning i Nakskov – {rk(lambda x: PV[x]['syd'], 'nakskov', 'højeste')} værdi af de {nw()} byer. Et 6 kWp-anlæg giver dermed ca. {tal(PV['nakskov']['syd']*6)} kWh om året, heraf ca. {tal(PV['nakskov']['months'][4]*6)} kWh i maj og kun {tal(PV['nakskov']['months'][11]*6)} kWh i december. Mod vest giver hver kWp ca. {tal(PV['nakskov']['vest'])} kWh, mod øst ca. {tal(PV['nakskov']['oest'])}."),
 "assens": ("Hvad giver solceller i Assens?",
   lambda: f"I Assens giver et sydvendt tag med 35° hældning ca. {tal(PV['assens']['syd'])} kWh pr. kWp om året ifølge PVGIS, og ved den bedste hældning på {PV['assens']['opt_angle']}° ca. {tal(PV['assens']['opt'])} kWh. Et 6 kWp-anlæg giver ca. {tal(PV['assens']['syd']*6)} kWh om året – {tal(PV['assens']['months'][5]*6)} kWh i juni og {tal(PV['assens']['months'][0]*6)} kWh i januar. Et øst- eller vestvendt tag giver ca. {tal(PV['assens']['oest'])}-{tal(PV['assens']['vest'])} kWh pr. kWp."),
})
SOL_PROD_SRC_NEW.update({"nakskov": ["pv_nakskov", "pvo_nakskov", "pvv_nakskov"], "assens": ["pv_assens", "pvo_assens", "pvv_assens"]})
SOL_ROOF.update({
 "nakskov": ("Fibercement på to ud af fem tage i Lolland Kommune",
   lambda: f"{rp('nakskov','06')} af parcel- og rækkehusene i Lolland Kommune har <strong>fibercement</strong>, {rp('nakskov','10')} tegl og {rp('nakskov','08')} cementsten. Kun {pct(_flat('nakskov'), ROOF['nakskov']['tot'])} har fladt tag eller tagpap – {rk(lambda x: _flat(x) / ROOF[x]['tot'], 'nakskov', 'laveste', rev=True)} andel af de {nw()} byer. Mange huse er gamle, og bølgeplader fra før 1984 kan indeholde asbest, så få taget vurderet – kommunen beder dig også tjekke, om taget kan bære vægten.",
   ["dst_bygb50", "nak_sol", "bolius_asb"]),
 "assens": ("Fibercement og cementsten på tre ud af fem tage i Assens",
   lambda: f"{rp('assens','06')} af parcel- og rækkehusene i Assens Kommune har <strong>fibercement</strong> og {rp('assens','08')} <strong>cementsten</strong>, mens {rp('assens','10')} har tegl. {pct(_flat('assens'), ROOF['assens']['tot'])} har fladt tag eller tagpap; her kræver Assens Kommune, at du søger, fordi panelerne ikke følger en taghældning.",
   ["dst_bygb50", "ass_sol", "bolius_mont"]),
})
SOL_HOMES.update({
 "nakskov": lambda: f"Lolland Kommune har {tal(STOCK['nakskov']['tot'])} beboede parcel- og rækkehuse, og {pct(STOCK['nakskov']['B']['før 1960'],STOCK['nakskov']['tot'])} er bygget før 1960 – {rk(_sb('før 1960'), 'nakskov', 'højeste')} andel af de {nw()} byer og mod {pct(STOCK['dk']['B']['før 1960'],STOCK['dk']['tot'])} på landsplan. Kun {pct(STOCK['nakskov']['B']['2000+'],STOCK['nakskov']['tot'])} er fra 2000 eller senere. Nakskov har {tal(town('nakskov','Nakskov'))} indbyggere, Maribo {tal(town('nakskov','Maribo'))} og Rødby {tal(town('nakskov','Rødby'))}.",
 "assens": lambda: f"Assens Kommune har {tal(STOCK['assens']['tot'])} beboede parcel- og rækkehuse, og {pct(STOCK['assens']['ejer'],STOCK['assens']['tot'])} bebos af ejeren. {pct(STOCK['assens']['B']['før 1960'],STOCK['assens']['tot'])} er bygget før 1960 mod {pct(STOCK['dk']['B']['før 1960'],STOCK['dk']['tot'])} på landsplan. Kommunen har ingen stor by: Assens har {tal(town('assens','Assens'))} indbyggere, Glamsbjerg {tal(town('assens','Glamsbjerg'))}, Vissenbjerg {tal(town('assens','Vissenbjerg'))} og Aarup {tal(town('assens','Aarup'))}.",
})
SOL_HOMES_SRC_NEW.update({"nakskov": ["dst_by3"], "assens": ["dst_by3"]})
SOL_HOMES_H.update({"nakskov": "Mange gamle huse: boligerne i Lolland Kommune", "assens": "Mange små byer: boligerne i Assens Kommune"})
SOL_XFAQ.update({
 "nakskov": [("Hvor meget strøm giver et 6 kWp-anlæg i Nakskov?", lambda: f"Ca. {tal(PV['nakskov']['syd']*6)} kWh om året på et sydvendt tag med 35° hældning ifølge PVGIS 5.3. Mod vest er det ca. {tal(PV['nakskov']['vest']*6)} kWh og mod øst ca. {tal(PV['nakskov']['oest']*6)} kWh.", ["pv_nakskov", "pvo_nakskov", "pvv_nakskov"])],
 "assens": [("Hvor meget strøm giver et 6 kWp-anlæg i Assens?", lambda: f"Ca. {tal(PV['assens']['syd']*6)} kWh om året på et sydvendt tag med 35° hældning ifølge PVGIS 5.3. Mod vest er det ca. {tal(PV['assens']['vest']*6)} kWh og mod øst ca. {tal(PV['assens']['oest']*6)} kWh.", ["pv_assens", "pvo_assens", "pvv_assens"])],
})
VP_HEAT.update({
 "nakskov": ("Flest oliefyr på sitet: opvarmningen i Lolland Kommune",
   lambda: f"{tal(HEAT['nakskov']['CO'])} af de {tal(hs('nakskov'))} beboede parcel- og rækkehuse i Lolland Kommune ({hp('nakskov','CO',1)}) har stadig oliefyr – {rk(_hf('CO'), 'nakskov', 'højeste')} andel af de {nw()} byer og mod {hp('dk','CO',1)} på landsplan. {tal(HEAT['nakskov']['ELV'])} ({hp('nakskov','ELV',1)}) har elvarme, {tal(HEAT['nakskov']['FJ'])} ({hp('nakskov','FJ',1)}) fjernvarme og {tal(HEAT['nakskov']['VP'])} ({hp('nakskov','VP',1)}) varmepumpe. Ingen er registreret med naturgas."),
 "assens": ("Fjernvarme i lidt over halvdelen af husene i Assens",
   lambda: f"{tal(HEAT['assens']['FJ'])} af de {tal(hs('assens'))} beboede parcel- og rækkehuse i Assens Kommune ({hp('assens','FJ',1)}) har fjernvarme, {tal(HEAT['assens']['VP'])} ({hp('assens','VP',1)}) varmepumpe og {tal(HEAT['assens']['CN'])} ({hp('assens','CN',1)}) naturgas. {tal(HEAT['assens']['CO'])} ({hp('assens','CO',1)}) har stadig oliefyr, og {tal(HEAT['assens']['CA'])} ({hp('assens','CA',1)}) fyrer med træ, træpiller eller anden biomasse."),
})
VP_HEAT_SRC_NEW.update({"nakskov": ["nak_lf"], "assens": ["ass_vp"]})
VP_TOWNS.update({
 "nakskov": [("Nakskov", "Lolland Varme (ca. 4.500 kunder)", ["nak_lf", "ft_pris"]),
             ("Maribo", "Sydhavsvarme (tidl. Maribo Varmeværk)", ["nak_syd"]),
             ("Rødby", "Rødby Varmeværk", ["ft_pris"]),
             ("Rødbyhavn", "Rødbyhavn Fjernvarme", ["ft_pris"]),
             ("Holeby", "Holeby Fjernvarme", ["ft_pris"]),
             ("Søllested", "Lolland Varme (halm og solfangere)", ["nak_lf"]),
             ("Bandholm, Nørreballe, Stokkemarke", "Lolland Varme Midtlolland (varme fra Sakskøbing via Maribo)", ["nak_lf"])],
 "assens": [("Assens", "Assens Fjernvarme", ["ass_af900", "ft_pris"]),
            ("Aarup", "Assens Fjernvarme (udrulning 2023-2026)", ["ass_af900", "ass_aftid"]),
            ("Glamsbjerg og Haarby", "Glamsbjerg-Haarby Varmeværk", ["ft_pris"]),
            ("Tommerup og Tommerup Stationsby", "Tommerup Bys Fjernvarmeforsyning / Tommerup St. Varmeforsyning", ["ft_pris"]),
            ("Langs transmissionsledningen Assens-Aarup", "Ingen fjernvarme – etapen droppet 2026", ["ass_nb"])],
})
VP_TOWNS_NOTE.update({
 "nakskov": "Fjernvarmen dækker Nakskov, Maribo, Rødby, Rødbyhavn, Holeby, Søllested og en række landsbyer på Midtlolland. Uden for nettene – og i de mange ældre huse med oliefyr eller elvarme – er en luft til vand-varmepumpe det typiske alternativ. Vil du have jordvarme, kræver det tilladelse fra kommunen.",
 "assens": "Assens, Aarup, Glamsbjerg, Haarby og Tommerup har fjernvarme. Langs transmissionsledningen fra Assens mod Aarup blev en etape droppet, fordi varmepumper var billigere. Kommunen anbefaler varmepumpe, hvor der ikke kommer fjernvarme – tjek din adresse på kommunens kort.",
})
VP_XFAQ.update({
 "nakskov": [("Hvor mange huse i Lolland Kommune har oliefyr?", lambda: f"{tal(HEAT['nakskov']['CO'])} af de {tal(hs('nakskov'))} beboede parcel- og rækkehuse ({hp('nakskov','CO',1)}) ifølge Danmarks Statistik, 2026 – mod {hp('dk','CO',1)} på landsplan. Hertil kommer {tal(HEAT['nakskov']['ELV'])} med elvarme.", ["dst_bol102"]),
             ("Hvad koster en luft til vand-varmepumpe i Nakskov?", lambda: "SparEnergi angiver typisk 100.000-130.000 kr. inkl. montering, og Energisparer.dk ca. 90.000-150.000 kr. afhængigt af husets størrelse. Vi har ikke fundet kilder med en særlig Nakskov-pris. Til sammenligning koster et standardhus 13.723 kr. om året i fjernvarme hos Lolland Varme ifølge Forsyningstilsynet.", ["se_vp", "es_vp", "ft_pris"])],
 "assens": [("Hvad koster en luft til vand-varmepumpe i Assens?", lambda: "SparEnergi angiver typisk 100.000-130.000 kr. inkl. montering, og Energisparer.dk ca. 90.000-150.000 kr. afhængigt af husets størrelse. Vi har ikke fundet kilder med en særlig Assens-pris. Langs transmissionsledningen mod Aarup viste Assens Fjernvarmes beregning, at fjernvarme ville være 24 % dyrere end individuelle varmepumper.", ["se_vp", "es_vp", "ass_nb"]),
            ("Hvor mange huse i Assens Kommune har varmepumpe?", lambda: f"{tal(HEAT['assens']['VP'])} af de {tal(hs('assens'))} beboede parcel- og rækkehuse ({hp('assens','VP',1)}) ifølge Danmarks Statistik, 2026, mod {hp('dk','VP',1)} på landsplan. {tal(HEAT['assens']['CN'])} har stadig naturgas og {tal(HEAT['assens']['CO'])} oliefyr.", ["dst_bol102"])],
})
FV_SOURCES.update({
 "nakskov": [("Varmen i Nakskov kommer fra <strong>flisværket på Savnsøvej</strong> (2 kedler, 19 MW) og <strong>halmværket på Drammenvej</strong> (3 kedler, 22,5 MW).", ["nak_lfvv"]),
             ("Produktionen er ca. 135.000 MWh om året på ca. 14.000 tons flis og op mod 60.000 bigballer; en planlagt <strong>40 MW elkedel</strong> skal skære op til 40 % af halmen.", ["nak_lf", "nak_elk"])],
 "assens": [("Fjernvarmen til Aarup og landsbyerne sendes fra Assens gennem en <strong>18 km lang transmissionsledning</strong>; flere kunder giver et større aftræk og en mere stabil forsyning.", ["ass_af900"]),
            ("Kommunens kollektive varmeforsyning består af <strong>fem lokale fjernvarmeselskaber</strong> og et naturgasselskab.", ["ass_nb"])],
})
FV_SHARE.update({
 "nakskov": lambda: f"{hp('nakskov','FJ',1)} af de beboede parcel- og rækkehuse i Lolland Kommune har fjernvarme, mod {hp('dk','FJ',1)} i hele landet. Ingen er registreret med naturgas, men {hp('nakskov','CO',1)} har oliefyr.",
 "assens": lambda: f"{hp('assens','FJ',1)} af de beboede parcel- og rækkehuse i Assens Kommune har fjernvarme, mod {hp('dk','FJ',1)} i hele landet. {hp('assens','CN',1)} har naturgas.",
})
FV_SOURCES_H.update({"nakskov": "Flis, halm og snart en elkedel i Nakskov", "assens": "Fra Assens til Aarup i én ledning"})
_reg_age_old19 = reg_age_note
def reg_age_note(c, kommune):
    s = STOCK[c]; B = s["B"]; t = s["tot"]
    if c == "nakskov":
        return (f"{tal(B['før 1960'])} af de beboede huse i Lolland Kommune ({pct(B['før 1960'], t)}) er bygget før 1960 – {rk(_sb('før 1960'), 'nakskov', 'højeste')} andel af de {nw()} byer. Kommunen beder dig tjekke, om huset er bevaringsværdigt eller fredet, og om taget kan bære den ekstra vægt.", ["nak_sol"])
    if c == "assens":
        return (f"{tal(B['før 1960'])} af de beboede huse i Assens Kommune ({pct(B['før 1960'], t)}) er bygget før 1960. Find lokalplanen for din adresse på kommunens kort: lokalplaner kan kræve dispensation, selv når solcellerne følger taghældningen.", ["ass_sol"])
    return _reg_age_old19(c, kommune)

# keyword-backlog 17/11 2026: 'luft til vand varmepumpe slagelse' (GSC 18 visninger, pos. 27,1) -> luft til vand-H2 + FAQ på /varmepumpe/slagelse/
VP_HEAT["slagelse"] = ("Luft til vand-varmepumpe i Slagelse: gas, olie og elvarme i kommunen", VP_HEAT["slagelse"][1])
VP_XFAQ["slagelse"] = VP_XFAQ["slagelse"] + [("Hvem i Slagelse Kommune kan få tilskud til en luft til vand-varmepumpe?", lambda: f"Byrådet annullerede i 2025 fjernvarmeprojekterne i det centrale Skælskør og i Vemmelev og Forlev, så boligejerne dér igen kan søge tilskud til varmepumpe. Varmepumpepuljen giver 27.000 kr. ved skift til luft til vand-varmepumpe, når huset ikke ligger i et område med fjernvarme eller planlagt fjernvarme. Danmarks Statistik registrerer {tal(HEAT['slagelse']['CN'])} huse med naturgas og {tal(HEAT['slagelse']['CO'])} med oliefyr i Slagelse Kommune – typisk huse med radiatorer, hvor en luft til vand-varmepumpe kan overtage både rumvarme og varmt vand.", ["slg_fv", "se_vpp", "dst_bol102", "es_l2v"])]


# ---------- daglig by-rutine 18. nov. 2026: Hinnerup (DK1, Favrskov Kommune) og Helsinge (DK2, Gribskov Kommune) ----------
SOL_ORDER.update({"hinnerup": ["boliger", "produktion", "lokalt", "faq", "tage", "guides"],
                  "helsinge": ["tage", "lokalt", "produktion", "faq", "boliger", "guides"]})
VP_ORDER.update({"hinnerup": ["lokale-byer", "opvarmning", "lokalt", "faq", "pris", "guides"],
                 "helsinge": ["opvarmning", "lokalt", "pris", "faq", "lokale-byer", "guides"]})
FV_ORDER.update({"hinnerup": ["andel", "priser", "status", "faq", "billigst", "varmekilder"],
                 "helsinge": ["status", "priser", "varmekilder", "faq", "andel", "billigst"]})
SOL_PROD.update({
 "hinnerup": ("Solcelleproduktion i Hinnerup og Favrskov",
   lambda: f"Et sydvendt tag med 35° hældning i Hinnerup giver ca. {tal(PV['hinnerup']['syd'])} kWh pr. kWp om året ifølge PVGIS 5.3. Et 6 kWp-anlæg ender på ca. {tal(PV['hinnerup']['syd']*6)} kWh – fra ca. {tal(PV['hinnerup']['months'][0]*6)} kWh i januar til ca. {tal(PV['hinnerup']['months'][5]*6)} kWh i juni. Øst- og vestvendte tage giver begge ca. {tal(PV['hinnerup']['oest'])}-{tal(PV['hinnerup']['vest'])} kWh pr. kWp, og den bedste hældning er {PV['hinnerup']['opt_angle']}° med ca. {tal(PV['hinnerup']['opt'])} kWh."),
 "helsinge": ("Nordkystens sol: produktion i Helsinge",
   lambda: f"PVGIS beregner ca. {tal(PV['helsinge']['syd'])} kWh pr. kWp om året for et sydvendt tag med 35° hældning i Helsinge – {rk(lambda x: PV[x]['syd'], 'helsinge', 'højeste')} værdi af de {nw()} byer. Et 6 kWp-anlæg giver dermed ca. {tal(PV['helsinge']['syd']*6)} kWh om året, heraf ca. {tal(PV['helsinge']['months'][6]*6)} kWh i juli. Mod vest giver hver kWp ca. {tal(PV['helsinge']['vest'])} kWh og mod øst ca. {tal(PV['helsinge']['oest'])} kWh."),
})
SOL_PROD_SRC_NEW.update({"hinnerup": ["pv_hinnerup", "pvo_hinnerup", "pvv_hinnerup"], "helsinge": ["pv_helsinge", "pvo_helsinge", "pvv_helsinge"]})
SOL_ROOF.update({
 "hinnerup": ("Fibercement og cementsten dominerer i Favrskov",
   lambda: f"{rp('hinnerup','06')} af parcel- og rækkehusene i Favrskov Kommune har <strong>fibercement</strong>, {rp('hinnerup','08')} cementsten og {rp('hinnerup','10')} tegl. {pct(_flat('hinnerup'), ROOF['hinnerup']['tot'])} har fladt tag eller tagpap. Favrskov Kommune skriver, at en lokalplan eller deklaration kan begrænse valget af tagmaterialer og farver – tjek den, før du lægger solceller på, og få et ældre fibercementtag vurderet for asbest.",
   ["dst_bygb50", "hin_byg", "bolius_asb"]),
 "helsinge": ("Mange stråtage i Gribskov",
   lambda: f"{rp('helsinge','06')} af parcel- og rækkehusene i Gribskov Kommune har <strong>fibercement</strong>, {rp('helsinge','10')} tegl og {rp('helsinge','08')} cementsten. {tal(ROOF['helsinge']['T']['14'])} huse ({rp('helsinge','14',1)}) har <strong>stråtag</strong> – {rk(_rt('14'), 'helsinge', 'højeste')} andel af de {nw()} byer – og {pct(_flat('helsinge'), ROOF['helsinge']['tot'])} har fladt tag eller tagpap. Gribskov Kommune skriver, at en lokalplan eller byplanvedtægt skal overholdes – tjek din, før du bestiller.",
   ["dst_bygb50", "hel_byg", "bolius_mont"]),
})
SOL_HOMES.update({
 "hinnerup": lambda: f"Favrskov Kommune har {tal(STOCK['hinnerup']['tot'])} beboede parcel- og rækkehuse, og {pct(STOCK['hinnerup']['B']['2000+'],STOCK['hinnerup']['tot'])} er bygget i 2000 eller senere – {rk(_sb('2000+'), 'hinnerup', 'højeste')} andel af de {nw()} byer og mod {pct(STOCK['dk']['B']['2000+'],STOCK['dk']['tot'])} på landsplan. {pct(STOCK['hinnerup']['ejer'],STOCK['hinnerup']['tot'])} bebos af ejeren. Hinnerup har {tal(town('hinnerup','Hinnerup'))} indbyggere, Hadsten {tal(town('hinnerup','Hadsten'))}, Hammel {tal(town('hinnerup','Hammel'))} og Søften {tal(town('hinnerup','Søften'))}.",
 "helsinge": lambda: f"Gribskov Kommune har {tal(STOCK['helsinge']['tot'])} beboede parcel- og rækkehuse. {pct(STOCK['helsinge']['B']['1960-1979'],STOCK['helsinge']['tot'])} er bygget 1960-1979 – {rk(_sb('1960-1979'), 'helsinge', 'højeste')} andel af de {nw()} byer – og {pct(STOCK['helsinge']['ejer'],STOCK['helsinge']['tot'])} bebos af ejeren. Helsinge har {tal(town('helsinge','Helsinge'))} indbyggere, Gilleleje {tal(town('helsinge','Gilleleje'))} og Græsted {tal(town('helsinge','Græsted'))}.",
})
SOL_HOMES_SRC_NEW.update({"hinnerup": ["dst_by3"], "helsinge": ["dst_by3"]})
SOL_HOMES_H.update({"hinnerup": "Nye huse og tre jævnstore byer i Favrskov", "helsinge": "Huse fra 60'erne og 70'erne: boligerne i Gribskov"})
SOL_XFAQ.update({
 "hinnerup": [("Hvor meget strøm giver et 6 kWp-anlæg i Hinnerup?", lambda: f"Ca. {tal(PV['hinnerup']['syd']*6)} kWh om året på et sydvendt tag med 35° hældning ifølge PVGIS 5.3. Mod øst er det ca. {tal(PV['hinnerup']['oest']*6)} kWh og mod vest ca. {tal(PV['hinnerup']['vest']*6)} kWh.", ["pv_hinnerup", "pvo_hinnerup", "pvv_hinnerup"])],
 "helsinge": [("Hvor meget strøm giver et 6 kWp-anlæg i Helsinge?", lambda: f"Ca. {tal(PV['helsinge']['syd']*6)} kWh om året på et sydvendt tag med 35° hældning ifølge PVGIS 5.3. Mod vest er det ca. {tal(PV['helsinge']['vest']*6)} kWh og mod øst ca. {tal(PV['helsinge']['oest']*6)} kWh.", ["pv_helsinge", "pvo_helsinge", "pvv_helsinge"])],
})
VP_HEAT.update({
 "hinnerup": ("To ud af tre huse har fjernvarme i Favrskov",
   lambda: f"{tal(HEAT['hinnerup']['FJ'])} af de {tal(hs('hinnerup'))} beboede parcel- og rækkehuse i Favrskov Kommune ({hp('hinnerup','FJ',1)}) har fjernvarme, mod {hp('dk','FJ',1)} på landsplan. {tal(HEAT['hinnerup']['VP'])} ({hp('hinnerup','VP',1)}) har varmepumpe, {tal(HEAT['hinnerup']['CN'])} ({hp('hinnerup','CN',1)}) naturgas, {tal(HEAT['hinnerup']['CA'])} ({hp('hinnerup','CA',1)}) træ, piller eller anden biomasse og {tal(HEAT['hinnerup']['CO'])} ({hp('hinnerup','CO',1)}) oliefyr."),
 "helsinge": ("Højeste andel med varmepumpe og elvarme: opvarmningen i Gribskov",
   lambda: f"{tal(HEAT['helsinge']['VP'])} af de {tal(hs('helsinge'))} beboede parcel- og rækkehuse i Gribskov Kommune ({hp('helsinge','VP',1)}) har varmepumpe – {rk(_hf('VP'), 'helsinge', 'højeste')} andel af de {nw()} byer og mod {hp('dk','VP',1)} på landsplan. {tal(HEAT['helsinge']['ELV'])} ({hp('helsinge','ELV',1)}) har elvarme, også {rk(_hf('ELV'), 'helsinge', 'højeste')} andel, og {tal(HEAT['helsinge']['CO'])} ({hp('helsinge','CO',1)}) har oliefyr – {rk(_hf('CO'), 'helsinge', 'højeste')} andel. Kun {hp('helsinge','FJ',1)} har fjernvarme."),
})
VP_HEAT_SRC_NEW.update({"hinnerup": ["hin_skift"], "helsinge": ["hel_vplan"]})
VP_TOWNS.update({
 "hinnerup": [("Hinnerup", "Hinnerup Fjernvarme (5.405 forbrugere i 2025)", ["hin_ber", "ft_pris"]),
              ("Søften", "Hinnerup Fjernvarme – nettet udvides under Ølstedvej", ["hin_soef"]),
              ("Grundfør og Norring/Foldby", "Hinnerup Fjernvarme – nye boliger og projektforslag", ["hin_ber"]),
              ("Hadsten", "Hadsten Varmeværk", ["ft_pris"]),
              ("Hammel", "Hammel Fjernvarme", ["ft_pris"]),
              ("Thorsø", "Thorsø Fjernvarmeværk", ["ft_pris"])],
 "helsinge": [("Helsinge", "Helsinge Fjernvarme (over 2.059 husstande)", ["hel_ber", "ft_pris"]),
              ("Helsinge Øst og Vest (gasområder)", "Planlagt konvertering til fjernvarme", ["hel_fj"]),
              ("Gilleleje", "Gilleleje Fjernvarme", ["ft_pris"]),
              ("Græsted", "Græsted Fjernvarme", ["ft_pris"]),
              ("Vejby og Tisvilde", "Vejby-Tisvilde Fjernvarme", ["ft_pris", "hel_varme"]),
              ("Annisse Nord og Ramløse", "Byvarme (ø-varme) undersøges", ["hel_fj"])],
})
VP_TOWNS_NOTE.update({
 "hinnerup": "Hinnerup, Søften, Hadsten, Hammel og Thorsø har fjernvarme, og Hinnerup Fjernvarmes net vokser. Uden for nettene – og for de huse, der stadig har naturgas eller olie – er en luft til vand-varmepumpe det typiske alternativ. Jordvarme kræver anmeldelse eller tilladelse fra Favrskov Kommune.",
 "helsinge": "Helsinge, Gilleleje, Græsted, Vejby og Tisvilde har fjernvarme, og gasområderne i Helsinge Øst og Vest skal efter planen over på fjernvarme. Resten af Gribskov Kommune er udlagt til individuel varme – her har mange allerede valgt varmepumpe. Tjek din adresse på kommunens kort, før du vælger.",
})
VP_XFAQ.update({
 "hinnerup": [("Hvor mange huse i Favrskov Kommune har stadig naturgas?", lambda: f"{tal(HEAT['hinnerup']['CN'])} af de {tal(hs('hinnerup'))} beboede parcel- og rækkehuse ({hp('hinnerup','CN',1)}) ifølge Danmarks Statistik, 2026 – mod {hp('dk','CN',1)} på landsplan. Hertil kommer {tal(HEAT['hinnerup']['CO'])} med oliefyr.", ["dst_bol102"]),
              ("Hvad koster en luft til vand-varmepumpe i Hinnerup?", lambda: "SparEnergi angiver typisk 100.000-130.000 kr. inkl. montering, og Energisparer.dk ca. 90.000-150.000 kr. afhængigt af husets størrelse. Vi har ikke fundet kilder med en særlig Hinnerup-pris. Til sammenligning koster et standardhus 13.326 kr. om året i fjernvarme hos Hinnerup Fjernvarme ifølge Forsyningstilsynet.", ["se_vp", "es_vp", "ft_pris"])],
 "helsinge": [("Hvor mange huse i Gribskov Kommune har elvarme?", lambda: f"{tal(HEAT['helsinge']['ELV'])} af de {tal(hs('helsinge'))} beboede parcel- og rækkehuse ({hp('helsinge','ELV',1)}) ifølge Danmarks Statistik, 2026 – mod {hp('dk','ELV',1)} på landsplan. Har huset elpaneler uden radiatorer, er en luft til luft-varmepumpe ofte det billigste skifte.", ["dst_bol102", "se_vp"]),
              ("Hvad koster en luft til vand-varmepumpe i Helsinge?", lambda: "SparEnergi angiver typisk 100.000-130.000 kr. inkl. montering, og Energisparer.dk ca. 90.000-150.000 kr. afhængigt af husets størrelse. Vi har ikke fundet kilder med en særlig Helsinge-pris. Bor du i Helsinge Øst eller Vest, hvor fjernvarmen er planlagt, kan du ikke få tilskud, hvis der er et godkendt projektforslag i området.", ["se_vp", "es_vp", "hel_varme"])],
})
FV_SOURCES.update({
 "hinnerup": [("Ca. <strong>72 % af varmen</strong> blev i 2025 produceret på halm, 21 % på flis, 7 % var overskudsvarme og 0,1 % naturgas; en absorptionsvarmepumpe på halmkedel 2 øger kedlens virkningsgrad med 12-15 %.", ["hin_ber"]),
              ("En ny <strong>elkedel og akkumuleringstank</strong> i Søften Erhverv skal producere varme, når strømmen er billigst, og give adgang til overskudsvarme fra virksomheder.", ["hin_elk", "hin_ber"])],
 "helsinge": [("Helsinge Fjernvarme kører <strong>gasmotorer</strong>, der laver el og varme, når elprisen er høj, og en <strong>elkedel med akkumuleringstanke</strong>, når elprisen er lav eller negativ.", ["hel_ber"]),
              ("Værket har også <strong>solvarme</strong>, og bestyrelsen undersøger eldrevne varmepumper eller endnu en elkedel. Naturgas dækkede i 2020 ca. 27 % af fjernvarmeproduktionen i Gribskov Kommune og skal udfases.", ["hel_fo", "hel_ber", "hel_varme"])],
})
FV_SHARE.update({
 "hinnerup": lambda: f"{hp('hinnerup','FJ',1)} af de beboede parcel- og rækkehuse i Favrskov Kommune har fjernvarme, mod {hp('dk','FJ',1)} i hele landet. {hp('hinnerup','CN',1)} har stadig naturgas.",
 "helsinge": lambda: f"Kun {hp('helsinge','FJ',1)} af de beboede parcel- og rækkehuse i Gribskov Kommune har fjernvarme, mod {hp('dk','FJ',1)} i hele landet, mens {hp('helsinge','VP',1)} har varmepumpe.",
})
FV_SOURCES_H.update({"hinnerup": "Halm, flis og snart en elkedel i Søften", "helsinge": "Gasmotorer, elkedel og solvarme i Helsinge"})
_reg_age_old20 = reg_age_note
def reg_age_note(c, kommune):
    s = STOCK[c]; B = s["B"]; t = s["tot"]
    if c == "hinnerup":
        return (f"{tal(B['2000+'])} af de beboede huse i Favrskov Kommune ({pct(B['2000+'], t)}) er bygget i 2000 eller senere – mange i nyere udstykninger med lokalplaner, der kan stille krav til tage og farver. Tjek lokalplanen for din adresse på kommunens webkort.", ["hin_byg"])
    if c == "helsinge":
        return (f"{tal(B['1960-1979'])} af de beboede huse i Gribskov Kommune ({pct(B['1960-1979'], t)}) er bygget 1960-1979. Er huset omfattet af en lokalplan eller byplanvedtægt, skal den overholdes, ellers skal du søge dispensation.", ["hel_byg"])
    return _reg_age_old20(c, kommune)

# ---------- daglig by-rutine 19. nov. 2026: Middelfart (DK1, Middelfart Kommune) og Tønder (DK1, Tønder Kommune) ----------
SOL_ORDER.update({"middelfart": ["lokalt", "tage", "produktion", "boliger", "faq", "guides"],
                  "toender": ["boliger", "tage", "faq", "produktion", "lokalt", "guides"]})
VP_ORDER.update({"middelfart": ["lokalt", "lokale-byer", "pris", "opvarmning", "faq", "guides"],
                 "toender": ["opvarmning", "faq", "lokalt", "lokale-byer", "pris", "guides"]})
FV_ORDER.update({"middelfart": ["status", "faq", "priser", "andel", "varmekilder", "billigst"],
                 "toender": ["priser", "varmekilder", "status", "andel", "faq", "billigst"]})
SOL_PROD.update({
 "middelfart": ("Solcelleproduktion ved Lillebælt",
   lambda: f"PVGIS 5.3 beregner ca. {tal(PV['middelfart']['syd'])} kWh pr. kWp om året for et sydvendt tag med 35° hældning i Middelfart. Et anlæg på 6 kWp giver dermed ca. {tal(PV['middelfart']['syd']*6)} kWh om året – ca. {tal(PV['middelfart']['months'][4]*6)} kWh i maj og kun ca. {tal(PV['middelfart']['months'][11]*6)} kWh i december. Et vestvendt tag giver ca. {tal(PV['middelfart']['vest'])} kWh pr. kWp, et østvendt ca. {tal(PV['middelfart']['oest'])} kWh."),
 "toender": ("Solcelleproduktion i Tønder og marsken",
   lambda: f"Et sydvendt tag med 35° hældning i Tønder giver ca. {tal(PV['toender']['syd'])} kWh pr. kWp om året ifølge PVGIS 5.3, og den bedste hældning er {PV['toender']['opt_angle']}° med ca. {tal(PV['toender']['opt'])} kWh. Et 6 kWp-anlæg ender på ca. {tal(PV['toender']['syd']*6)} kWh om året. Mod vest giver hver kWp ca. {tal(PV['toender']['vest'])} kWh og mod øst ca. {tal(PV['toender']['oest'])} kWh."),
})
SOL_PROD_SRC_NEW.update({"middelfart": ["pv_middelfart", "pvo_middelfart", "pvv_middelfart"], "toender": ["pv_toender", "pvo_toender", "pvv_toender"]})
SOL_ROOF.update({
 "middelfart": ("Mange cementstenstage i Middelfart",
   lambda: f"{rp('middelfart','08')} af parcel- og rækkehusene i Middelfart Kommune har tag af <strong>cementsten</strong> – {rk(_rt('08'), 'middelfart', 'højeste')} andel af de {nw()} byer. {rp('middelfart','10')} har tegl og {rp('middelfart','06')} fibercement. Middelfart Kommune vil have en redegørelse for, om solcellerne øger lasten på bygningen med mere end 5 % – få derfor installatøren til at vurdere tagkonstruktionen, inden du får et tilbud.",
   ["dst_bygb50", "mid_byg", "bolius_mont"]),
 "toender": ("Fibercement og stråtage i Tønder Kommune",
   lambda: f"{rp('toender','06')} af parcel- og rækkehusene i Tønder Kommune har <strong>fibercement</strong>, {rp('toender','08')} cementsten og {rp('toender','10')} tegl. {tal(ROOF['toender']['T']['14'])} huse ({rp('toender','14',1)}) har <strong>stråtag</strong> – {rk(_rt('14'), 'toender', 'højeste')} andel af de {nw()} byer. Er huset fredet eller bevaringsværdigt, skal du søge Tønder Kommune om tilladelse, og et ældre fibercementtag bør vurderes for asbest, før der monteres solceller.",
   ["dst_bygb50", "ton_sol", "bolius_asb"]),
})
SOL_HOMES.update({
 "middelfart": lambda: f"Middelfart Kommune har {tal(STOCK['middelfart']['tot'])} beboede parcel- og rækkehuse. {pct(STOCK['middelfart']['B']['før 1960'],STOCK['middelfart']['tot'])} er bygget før 1960, men {pct(STOCK['middelfart']['B']['2000+'],STOCK['middelfart']['tot'])} er fra 2000 eller senere – {rk(_sb('2000+'), 'middelfart', 'højeste')} andel af de {nw()} byer. {pct(STOCK['middelfart']['ejer'],STOCK['middelfart']['tot'])} bebos af ejeren. Middelfart har {tal(town('middelfart','Middelfart'))} indbyggere, Strib {tal(town('middelfart','Strib'))}, Nørre Aaby {tal(town('middelfart','Nørre Aaby'))} og Ejby {tal(town('middelfart','Ejby'))}.",
 "toender": lambda: f"Tønder Kommune har {tal(STOCK['toender']['tot'])} beboede parcel- og rækkehuse, og kun {pct(STOCK['toender']['B']['2000+'],STOCK['toender']['tot'],1)} er bygget i 2000 eller senere – {rk(_sb('2000+'), 'toender', 'laveste', rev=True)} andel af de {nw()} byer. {pct(STOCK['toender']['B']['før 1960'],STOCK['toender']['tot'])} er fra før 1960. Tønder har {tal(town('toender','Tønder'))} indbyggere, Løgumkloster {tal(town('toender','Løgumkloster'))}, Toftlund {tal(town('toender','Toftlund'))} og Skærbæk {tal(town('toender','Skærbæk'))}.",
})
SOL_HOMES_SRC_NEW.update({"middelfart": ["dst_by3"], "toender": ["dst_by3"]})
SOL_HOMES_H.update({"middelfart": "Gamle bykerner og nye kvarterer: boligerne i Middelfart", "toender": "Ældre huse og fire mindre byer: boligerne i Tønder Kommune"})
SOL_XFAQ.update({
 "middelfart": [("Hvor meget strøm giver et 6 kWp-anlæg i Middelfart?", lambda: f"Ca. {tal(PV['middelfart']['syd']*6)} kWh om året på et sydvendt tag med 35° hældning ifølge PVGIS 5.3. Mod vest er det ca. {tal(PV['middelfart']['vest']*6)} kWh og mod øst ca. {tal(PV['middelfart']['oest']*6)} kWh.", ["pv_middelfart", "pvo_middelfart", "pvv_middelfart"])],
 "toender": [("Hvor meget strøm giver et 6 kWp-anlæg i Tønder?", lambda: f"Ca. {tal(PV['toender']['syd']*6)} kWh om året på et sydvendt tag med 35° hældning ifølge PVGIS 5.3. Mod vest er det ca. {tal(PV['toender']['vest']*6)} kWh og mod øst ca. {tal(PV['toender']['oest']*6)} kWh.", ["pv_toender", "pvo_toender", "pvv_toender"])],
})
VP_HEAT.update({
 "middelfart": ("Fjernvarme i byerne, gas i resten: opvarmningen i Middelfart",
   lambda: f"{tal(HEAT['middelfart']['FJ'])} af de {tal(hs('middelfart'))} beboede parcel- og rækkehuse i Middelfart Kommune ({hp('middelfart','FJ',1)}) har fjernvarme, mod {hp('dk','FJ',1)} på landsplan. {tal(HEAT['middelfart']['CN'])} ({hp('middelfart','CN',1)}) har naturgas, {tal(HEAT['middelfart']['VP'])} ({hp('middelfart','VP',1)}) varmepumpe og {tal(HEAT['middelfart']['CO'])} ({hp('middelfart','CO',1)}) oliefyr. Kun {hp('middelfart','ELV',1)} har elvarme."),
 "toender": ("Mange med elvarme og oliefyr: opvarmningen i Tønder",
   lambda: f"{tal(HEAT['toender']['ELV'])} af de {tal(hs('toender'))} beboede parcel- og rækkehuse i Tønder Kommune ({hp('toender','ELV',1)}) har elvarme – {rk(_hf('ELV'), 'toender', 'højeste')} andel af de {nw()} byer – og {tal(HEAT['toender']['CO'])} ({hp('toender','CO',1)}) har oliefyr, {rk(_hf('CO'), 'toender', 'højeste')} andel. {tal(HEAT['toender']['VP'])} ({hp('toender','VP',1)}) har allerede varmepumpe, {tal(HEAT['toender']['CN'])} ({hp('toender','CN',1)}) naturgas, og {hp('toender','FJ',1)} har fjernvarme."),
})
VP_HEAT_SRC_NEW.update({"middelfart": ["mid_vplan"], "toender": ["ton_kp"]})
VP_TOWNS.update({
 "middelfart": [("Middelfart", "Middelfart Fjernvarme", ["mf_takst", "ft_pris"]),
                ("Strib", "Middelfart Fjernvarme (eget grundbidrag)", ["mf_takst"]),
                ("Nørre Aaby og Ejby", "Middelfart Fjernvarme", ["mf_takst"]),
                ("Gelsted", "Gelsted Fjernvarmecentral", ["ft_pris"]),
                ("Føns", "Føns Nærvarme", ["ft_pris"]),
                ("Båring og Asperup", "Fjernvarmeområde aflyst – individuel opvarmning", ["mid_baer"])],
 "toender": [("Tønder", "Tønder Fjernvarmeselskab (ca. 3.200 forbrugere)", ["tf_fakta", "ft_pris"]),
             ("Løgumkloster", "Løgumkloster Fjernvarme", ["ft_pris"]),
             ("Toftlund", "Toftlund Fjernvarme", ["ft_pris"]),
             ("Skærbæk", "Skærbæk Fjernvarme", ["ft_pris"]),
             ("Bredebro", "Bredebro Varmeværk", ["ft_pris"]),
             ("Havneby (Rømø)", "Havneby Varmeværk", ["ft_pris", "ton_kp"])],
})
VP_TOWNS_NOTE.update({
 "middelfart": "Middelfart, Strib, Nørre Aaby og Ejby forsynes af Middelfart Fjernvarme, mens Gelsted og Føns har egne, dyrere værker. I Båring og Asperup er fjernvarmen droppet, så her er en luft til vand-varmepumpe det typiske valg. Tjek din adresse i Varmeplan Middelfart 2022, før du vælger.",
 "toender": "Tønder, Løgumkloster, Toftlund, Skærbæk og Bredebro har hver deres fjernvarmeværk, og der er mindre værker i bl.a. Havneby på Rømø. I landsbyerne og det åbne land er en varmepumpe det typiske alternativ til olie, gas og elvarme – kommuneplanen har netop som mål at udbrede varmepumper i områder uden kollektiv varme.",
})
VP_XFAQ.update({
 "middelfart": [("Hvor mange huse i Middelfart Kommune har stadig naturgas?", lambda: f"{tal(HEAT['middelfart']['CN'])} af de {tal(hs('middelfart'))} beboede parcel- og rækkehuse ({hp('middelfart','CN',1)}) ifølge Danmarks Statistik, 2026 – mod {hp('dk','CN',1)} på landsplan. Hertil kommer {tal(HEAT['middelfart']['CO'])} med oliefyr. Middelfart Kommune har sendt varmebreve til alle bygningsejere med olie- eller gasfyr om mulighederne for at skifte.", ["dst_bol102", "mid_vplan"]),
                ("Hvad koster en luft til vand-varmepumpe i Middelfart?", lambda: "SparEnergi angiver typisk 100.000-130.000 kr. inkl. montering, og Energisparer.dk ca. 90.000-150.000 kr. afhængigt af husets størrelse. Vi har ikke fundet kilder med en særlig Middelfart-pris. Til sammenligning koster et standardhus 15.860 kr. om året i fjernvarme hos Middelfart Fjernvarme ifølge Forsyningstilsynet.", ["se_vp", "es_vp", "ft_pris"])],
 "toender": [("Hvor mange huse i Tønder Kommune har oliefyr eller elvarme?", lambda: f"{tal(HEAT['toender']['CO'])} har oliefyr og {tal(HEAT['toender']['ELV'])} elvarme af de {tal(hs('toender'))} beboede parcel- og rækkehuse ifølge Danmarks Statistik, 2026 – tilsammen {pct(HEAT['toender']['CO']+HEAT['toender']['ELV'], hs('toender'))}. Har huset elpaneler uden radiatorer, er en luft til luft-varmepumpe ofte det billigste skifte; med radiatorer er det typisk en luft til vand-varmepumpe.", ["dst_bol102", "se_vp"]),
             ("Hvad koster en luft til vand-varmepumpe i Tønder?", lambda: "SparEnergi angiver typisk 100.000-130.000 kr. inkl. montering, og Energisparer.dk ca. 90.000-150.000 kr. afhængigt af husets størrelse. Vi har ikke fundet kilder med en særlig Tønder-pris. Tønder Dagblad skriver, at en luft til vand-varmepumpe i projektforslaget for Rosinfeltvej koster 246.000 kr. over 10 år for en villa på 181 m².", ["se_vp", "es_vp", "tf_rosin"])],
})
FV_SOURCES.update({
 "middelfart": [("Middelfart Fjernvarme opkræver en <strong>motivationstarif</strong>: 1 % rabat på forbruget pr. grad, returtemperaturen er lavere end forventet, og 1 % tillæg pr. grad, den er højere – højst 20 % hver vej.", ["mf_takst"]),
                ("I nyere forsyningsområder og i Strib er <strong>grundbidraget</strong> 30 kr. pr. m² mod 20 kr. i de ældre områder i Middelfart, Nr. Aaby og Ejby (inkl. moms, 2026).", ["mf_takst"])],
 "toender": [("Tønder Fjernvarmeselskab producerer på <strong>to fliskedler</strong> (3,75 og 10 MW), en <strong>elkedel på 15 MW</strong> og <strong>varmepumper på 3,6 MW</strong>, med en akkumuleringstank på 4.400 m³.", ["tf_fakta"]),
             ("Tre <strong>gaskedler</strong> på Energivej, Østergade og Grønnevej bruges kun som supplement i spidsbelastningsperioder.", ["tf_fakta"])],
})
FV_SHARE.update({
 "middelfart": lambda: f"{hp('middelfart','FJ',1)} af de beboede parcel- og rækkehuse i Middelfart Kommune har fjernvarme, mod {hp('dk','FJ',1)} i hele landet. {hp('middelfart','CN',1)} har stadig naturgas.",
 "toender": lambda: f"{hp('toender','FJ',1)} af de beboede parcel- og rækkehuse i Tønder Kommune har fjernvarme, mod {hp('dk','FJ',1)} i hele landet, mens {hp('toender','ELV',1)} har elvarme og {hp('toender','CO',1)} oliefyr.",
})
FV_SOURCES_H.update({"middelfart": "Returtemperatur og grundbidrag hos Middelfart Fjernvarme", "toender": "Flis, elkedel og varmepumper i Tønder"})
_reg_age_old21 = reg_age_note
def reg_age_note(c, kommune):
    s = STOCK[c]; B = s["B"]; t = s["tot"]
    if c == "middelfart":
        return (f"{tal(B['før 1960'])} af de beboede huse i Middelfart Kommune ({pct(B['før 1960'], t)}) er bygget før 1960. Kommunen har et kort over bevaringsværdige bygninger – og et hus kan også være bevaringsværdigt via lokalplan eller tinglyst deklaration. Tjek det, før du bestiller solceller.", ["mid_byg"])
    if c == "toender":
        return (f"{tal(B['før 1960'])} af de beboede huse i Tønder Kommune ({pct(B['før 1960'], t)}) er bygget før 1960. Er dit hus fredet eller bevaringsværdigt, skal du søge kommunen om tilladelse til solceller – også på taget.", ["ton_sol"])
    return _reg_age_old21(c, kommune)

# keyword-backlog 19/11 2026: 'jordvarme silkeborg' (GSC 13 visninger, pos. 71,5) -> FAQ om jordvarme på /varmepumpe/silkeborg/
VP_XFAQ["silkeborg"] = [("Skal jeg søge om jordvarme i Silkeborg Kommune?", lambda: "Ja. Silkeborg Kommune skriver, at du skal søge tilladelse eller anmelde jordvarmeanlægget via Byg og Miljø, før du etablerer det. Du kan nøjes med en anmeldelse, hvis anlægget er vandret, ikke-industrielt, ligger uden for områder med særlige drikkevandsinteresser og indvindingsoplande og kun bruger de frostsikringsmidler, jordvarmebekendtgørelsen tillader. Hører du ikke fra kommunen inden for 4 uger, må du gå i gang. Måske skal du også have byggetilladelse.", ["sil_jord"]),
                        ("Hvad koster jordvarme i Silkeborg?", lambda: "Vi har ikke fundet kilder med en særlig Silkeborg-pris. Energisparer.dk angiver ca. 120.000-180.000 kr. inkl. montering for jordvarme og ca. 93.000-153.000 kr. efter Varmepumpepuljens 27.000 kr. – som kun gælder uden for områder med fjernvarme eller planlagt fjernvarme. Har din ejendom tilslutningspligt i lokalplanen, kan du kun få dispensation til jordvarme, hvis huset opføres som lavenergibyggeri.", ["es_vp", "se_vpp", "sil_jord"])] + VP_XFAQ["silkeborg"]

# ---------- daglig by-rutine 20. nov. 2026: Rønne (DK2, Bornholms Regionskommune) og Hobro (DK1, Mariagerfjord Kommune) ----------
SOL_ORDER.update({"roenne": ["produktion", "lokalt", "boliger", "tage", "faq", "guides"],
                  "hobro": ["tage", "lokalt", "faq", "boliger", "produktion", "guides"]})
VP_ORDER.update({"roenne": ["opvarmning", "lokalt", "faq", "lokale-byer", "pris", "guides"],
                 "hobro": ["lokale-byer", "lokalt", "opvarmning", "pris", "faq", "guides"]})
FV_ORDER.update({"roenne": ["priser", "status", "varmekilder", "faq", "andel", "billigst"],
                 "hobro": ["andel", "status", "priser", "varmekilder", "billigst", "faq"]})
SOL_PROD.update({
 "roenne": ("Mest sol på sitet: solcelleproduktion på Bornholm",
   lambda: f"PVGIS 5.3 beregner ca. {tal(PV['roenne']['syd'])} kWh pr. kWp om året for et sydvendt tag med 35° hældning i Rønne – {rk(_PVs, 'roenne', 'højeste')} af de {nw()} byer på dette site. Et anlæg på 6 kWp giver dermed ca. {tal(PV['roenne']['syd']*6)} kWh om året – ca. {tal(PV['roenne']['months'][4]*6)} kWh i maj og kun ca. {tal(PV['roenne']['months'][11]*6)} kWh i december. Mod vest giver hver kWp ca. {tal(PV['roenne']['vest'])} kWh og mod øst ca. {tal(PV['roenne']['oest'])} kWh."),
 "hobro": ("Solcelleproduktion ved Mariager Fjord",
   lambda: f"Et sydvendt tag med 35° hældning i Hobro giver ca. {tal(PV['hobro']['syd'])} kWh pr. kWp om året ifølge PVGIS 5.3, og den bedste hældning er {PV['hobro']['opt_angle']}° med ca. {tal(PV['hobro']['opt'])} kWh. Et 6 kWp-anlæg ender på ca. {tal(PV['hobro']['syd']*6)} kWh om året, heraf ca. {tal(PV['hobro']['months'][5]*6)} kWh i juni. Mod vest giver hver kWp ca. {tal(PV['hobro']['vest'])} kWh og mod øst ca. {tal(PV['hobro']['oest'])} kWh."),
})
SOL_PROD_SRC_NEW.update({"roenne": ["pv_roenne", "pvo_roenne", "pvv_roenne"], "hobro": ["pv_hobro", "pvo_hobro", "pvv_hobro"]})
SOL_ROOF.update({
 "roenne": ("Tegltage og fibercement på Bornholm",
   lambda: f"{rp('roenne','10')} af parcel- og rækkehusene i Bornholms Regionskommune har tag af <strong>tegl</strong> – {rk(_rt('10'), 'roenne', 'højeste')} andel af de {nw()} byer. {rp('roenne','06')} har fibercement og {rp('roenne','08')} cementsten. Ligger huset i en bevarende lokalplan, kan den være meget specifik om tagdækningen, skriver kommunen – tjek den, før du vælger panelernes udseende. Et ældre fibercementtag bør vurderes for asbest, før der monteres solceller.",
   ["dst_bygb50", "brk_sol", "bolius_asb"]),
 "hobro": ("Næsten hvert andet tag er fibercement i Mariagerfjord",
   lambda: f"{rp('hobro','06')} af parcel- og rækkehusene i Mariagerfjord Kommune har tag af <strong>fibercement</strong> – {rk(_rt('06'), 'hobro', 'højeste')} andel af de {nw()} byer. {rp('hobro','08')} har cementsten og {rp('hobro','10')} tegl. Følger anlægget tagets hældning og afgrænsning, kræver det som udgangspunkt ikke byggetilladelse – men et ældre fibercementtag bør vurderes for asbest og bæreevne, før der monteres solceller.",
   ["dst_bygb50", "mfk_solgr", "bolius_asb"]),
})
SOL_HOMES.update({
 "roenne": lambda: f"Bornholms Regionskommune har {tal(STOCK['roenne']['tot'])} beboede parcel- og rækkehuse. {pct(STOCK['roenne']['B']['før 1960'],STOCK['roenne']['tot'])} er bygget før 1960, og kun {pct(STOCK['roenne']['B']['2000+'],STOCK['roenne']['tot'],1)} er fra 2000 eller senere – {rk(_sb('2000+'), 'roenne', 'laveste', rev=True)} andel af de {nw()} byer. {pct(STOCK['roenne']['ejer'],STOCK['roenne']['tot'])} bebos af ejeren. Rønne har {tal(town('roenne','Rønne'))} indbyggere, Nexø {tal(town('roenne','Nexø'))}, Aakirkeby {tal(town('roenne','Aakirkeby'))} og Hasle {tal(town('roenne','Hasle'))}.",
 "hobro": lambda: f"Mariagerfjord Kommune har {tal(STOCK['hobro']['tot'])} beboede parcel- og rækkehuse, og {pct(STOCK['hobro']['parcel'],STOCK['hobro']['tot'])} er parcelhuse. {pct(STOCK['hobro']['B']['før 1960'],STOCK['hobro']['tot'])} er bygget før 1960 og {pct(STOCK['hobro']['B']['2000+'],STOCK['hobro']['tot'])} i 2000 eller senere. Hobro har {tal(town('hobro','Hobro'))} indbyggere, Hadsund {tal(town('hobro','Hadsund'))}, Mariager {tal(town('hobro','Mariager'))} og Arden {tal(town('hobro','Arden'))}.",
})
SOL_HOMES_SRC_NEW.update({"roenne": ["dst_by3"], "hobro": ["dst_by3"]})
SOL_HOMES_H.update({"roenne": "Gamle huse og fire købstæder: boligerne på Bornholm", "hobro": "Parcelhuse ved fjorden: boligerne i Mariagerfjord"})
SOL_XFAQ.update({
 "roenne": [("Hvor meget strøm giver et 6 kWp-anlæg i Rønne?", lambda: f"Ca. {tal(PV['roenne']['syd']*6)} kWh om året på et sydvendt tag med 35° hældning ifølge PVGIS 5.3. Mod vest er det ca. {tal(PV['roenne']['vest']*6)} kWh og mod øst ca. {tal(PV['roenne']['oest']*6)} kWh.", ["pv_roenne", "pvo_roenne", "pvv_roenne"])],
 "hobro": [("Hvor meget strøm giver et 6 kWp-anlæg i Hobro?", lambda: f"Ca. {tal(PV['hobro']['syd']*6)} kWh om året på et sydvendt tag med 35° hældning ifølge PVGIS 5.3. Mod vest er det ca. {tal(PV['hobro']['vest']*6)} kWh og mod øst ca. {tal(PV['hobro']['oest']*6)} kWh.", ["pv_hobro", "pvo_hobro", "pvv_hobro"])],
})
VP_HEAT.update({
 "roenne": ("Ingen gas, men meget elvarme: opvarmningen på Bornholm",
   lambda: f"{tal(HEAT['roenne']['ELV'])} af de {tal(hs('roenne'))} beboede parcel- og rækkehuse i Bornholms Regionskommune ({hp('roenne','ELV',1)}) har elvarme – {rk(_hf('ELV'), 'roenne', 'højeste')} andel af de {nw()} byer – mod {hp('dk','ELV',1)} på landsplan. {tal(HEAT['roenne']['FJ'])} ({hp('roenne','FJ',1)}) har fjernvarme, {tal(HEAT['roenne']['VP'])} ({hp('roenne','VP',1)}) varmepumpe, {tal(HEAT['roenne']['CA'])} anden centralvarme som fx træpiller og {tal(HEAT['roenne']['CO'])} oliefyr. Kun {tal(HEAT['roenne']['CN'])} hus har naturgas."),
 "hobro": ("Olie, træpiller og gas uden for byerne: opvarmningen i Mariagerfjord",
   lambda: f"{tal(HEAT['hobro']['FJ'])} af de {tal(hs('hobro'))} beboede parcel- og rækkehuse i Mariagerfjord Kommune ({hp('hobro','FJ',1)}) har fjernvarme. {tal(HEAT['hobro']['CN'])} ({hp('hobro','CN',1)}) har naturgas, {tal(HEAT['hobro']['CO'])} ({hp('hobro','CO',1)}) oliefyr og {tal(HEAT['hobro']['CA'])} ({hp('hobro','CA',1)}) anden centralvarme som fx træpiller – {rk(_hf('CA'), 'hobro', 'højeste')} andel af de {nw()} byer. {tal(HEAT['hobro']['VP'])} ({hp('hobro','VP',1)}) har allerede varmepumpe."),
})
VP_HEAT_SRC_NEW.update({"roenne": ["rvv_fv"], "hobro": ["mfk_status"]})
VP_TOWNS.update({
 "roenne": [("Rønne", "Rønne Varme A/S (varme fra Bornholms Elproduktion og BOFA)", ["rvv_fv", "ft_pris"]),
            ("Nexø og Aakirkeby", "Bornholms Varme (BEOF)", ["beof_tilsl", "ft_pris"]),
            ("Hasle og Allinge-Sandvig", "Bornholms Varme (BEOF)", ["beof_tilsl"]),
            ("Svaneke og Gudhjem", "Bornholms Varme (BEOF)", ["beof_tilsl"]),
            ("Pedersker", "Bornholms Varme – overgangstakster frem til 2030", ["beof_takst"])],
 "hobro": [("Hobro", "Hobro Varmeværk (ca. 3.500 forbrugere)", ["df_hobro", "ft_pris"]),
           ("Hadsund", "Hadsund Fjernvarmeværk (flis og overskudsvarme)", ["mfk_vp22", "ft_pris"]),
           ("Mariager", "Mariager Fjernvarme (biomasse)", ["mfk_vp22", "ft_pris"]),
           ("Arden", "Arden Varmeværk (mest overskudsvarme fra Rockwool)", ["mfk_vp22", "ft_pris"]),
           ("Assens og Als", "Assens Fjernvarme og Als Fjernvarme", ["mfk_vp22", "ft_pris"]),
           ("Valsgaard og Hørby Kirkeby", "Fjernvarmeprojekt afventer – forventning om for lav tilslutning", ["mfk_status"])],
})
VP_TOWNS_NOTE.update({
 "roenne": "Rønne har sit eget fjernvarmeselskab, mens Bornholms Varme forsyner over 6.800 adresser i de øvrige byer fra Allinge til Aakirkeby. Landsbyer og sommerhusområder uden fjernvarme har hverken naturgas eller fjernvarme som alternativ – her er en varmepumpe det typiske skifte fra elvarme, olie eller træpiller.",
 "hobro": "Hobro, Hadsund, Mariager, Arden, Assens og Als har hver deres fjernvarmeværk. Uden for byerne ligger ca. 2.200 boliger med olie eller gas, som ifølge kommunen ikke kan tilkobles fjernvarme – her er en varmepumpe det oplagte alternativ. Tjek din adresse i varmeplanen, før du vælger.",
})
VP_XFAQ.update({
 "roenne": [("Hvor mange huse på Bornholm har elvarme?", lambda: f"{tal(HEAT['roenne']['ELV'])} af de {tal(hs('roenne'))} beboede parcel- og rækkehuse ({hp('roenne','ELV',1)}) ifølge Danmarks Statistik, 2026 – mod {hp('dk','ELV',1)} på landsplan. Har huset elpaneler uden radiatorer, er en luft til luft-varmepumpe ofte det billigste skifte; med radiatorer er det typisk en luft til vand-varmepumpe.", ["dst_bol102", "se_vp"]),
            ("Hvad koster en luft til vand-varmepumpe i Rønne?", lambda: "SparEnergi angiver typisk 100.000-130.000 kr. inkl. montering, og Energisparer.dk ca. 90.000-150.000 kr. afhængigt af husets størrelse. Vi har ikke fundet kilder med en særlig Bornholm-pris. Til sammenligning koster et standardhus 17.526 kr. om året i fjernvarme hos Rønne Varme og 22.669 kr. hos Bornholms Varme ifølge Forsyningstilsynet.", ["se_vp", "es_vp", "ft_pris"])],
 "hobro": [("Hvor mange huse i Mariagerfjord Kommune har oliefyr eller naturgas?", lambda: f"{tal(HEAT['hobro']['CO'])} har oliefyr og {tal(HEAT['hobro']['CN'])} naturgas af de {tal(hs('hobro'))} beboede parcel- og rækkehuse ifølge Danmarks Statistik, 2026. Kommunen har opgjort, at ca. 2.200 boliger med olie eller gas ligger uden for fjernvarmeområdet.", ["dst_bol102", "mfk_status"]),
           ("Hvad koster en luft til vand-varmepumpe i Hobro?", lambda: "SparEnergi angiver typisk 100.000-130.000 kr. inkl. montering, og Energisparer.dk ca. 90.000-150.000 kr. afhængigt af husets størrelse. Vi har ikke fundet kilder med en særlig Hobro-pris. Til sammenligning koster et standardhus 16.236 kr. om året i fjernvarme hos Hobro Varmeværk ifølge Forsyningstilsynet.", ["se_vp", "es_vp", "ft_pris"])],
})
FV_SOURCES.update({
 "roenne": [("Rønne Varme producerer ikke selv varmen til daglig: den købes hos <strong>kraftvarmeværket Bornholms Elproduktion</strong> og <strong>affaldsforbrændingen BOFA</strong>, og selskabet driver kun en reserve- og spidsbelastningscentral.", ["rvv_fv"]),
            ("Bornholms Varmes fjernvarme er ifølge BEOF <strong>99,98 % vedvarende</strong> og produceres primært på lokal halm og træflis.", ["beof_tilsl"])],
 "hobro": [("Hobro Varmeværk får i 2026 ca. <strong>15 % af varmen fra overskudsvarme</strong>, resten fra flis, en <strong>elkedel på 40 MW</strong> og fire varmepumper på i alt <strong>7,2 MW</strong>, der skulle i drift fra uge 35 i 2026.", ["df_hobro"]),
           ("Arden Varmeværk får størstedelen af varmen som <strong>overskudsvarme fra Rockwool</strong>, og Hadsund Fjernvarme modtager overskudsvarme fra Mariagerfjord Vand.", ["mfk_vp22"])],
})
FV_SHARE.update({
 "roenne": lambda: f"{hp('roenne','FJ',1)} af de beboede parcel- og rækkehuse i Bornholms Regionskommune har fjernvarme, mod {hp('dk','FJ',1)} i hele landet, mens {hp('roenne','ELV',1)} har elvarme.",
 "hobro": lambda: f"{hp('hobro','FJ',1)} af de beboede parcel- og rækkehuse i Mariagerfjord Kommune har fjernvarme, mod {hp('dk','FJ',1)} i hele landet. {hp('hobro','CN',1)} har stadig naturgas og {hp('hobro','CO',1)} oliefyr.",
})
FV_SOURCES_H.update({"roenne": "Kraftvarme, affald og halm: her kommer varmen fra", "hobro": "Overskudsvarme, flis og elkedel i Hobro"})
_reg_age_old22 = reg_age_note
def reg_age_note(c, kommune):
    s = STOCK[c]; B = s["B"]; t = s["tot"]
    if c == "roenne":
        return (f"{tal(B['før 1960'])} af de beboede huse i Bornholms Regionskommune ({pct(B['før 1960'], t)}) er bygget før 1960. Mange ældre huse ligger i bevarende lokalplaner, og alle svenskehusene er omfattet af deklarationer – tjek begge dele, før du bestiller solceller.", ["brk_sol"])
    if c == "hobro":
        return (f"{tal(B['før 1960'])} af de beboede huse i Mariagerfjord Kommune ({pct(B['før 1960'], t)}) er bygget før 1960. Lokalplaner, byplanvedtægter og servitutter kan have krav til farve, materiale og blankhed på taget – også for solceller, der følger taghældningen.", ["mfk_sol"])
    return _reg_age_old22(c, kommune)

# ---------- daglig by-rutine 23. nov. 2026: Ebeltoft (DK1, Syddjurs Kommune) og Thisted (DK1, Thisted Kommune) ----------
SOL_ORDER.update({"ebeltoft": ["lokalt", "tage", "produktion", "faq", "boliger", "guides"],
                  "thisted": ["tage", "produktion", "lokalt", "boliger", "faq", "guides"]})
VP_ORDER.update({"ebeltoft": ["opvarmning", "pris", "lokalt", "lokale-byer", "faq", "guides"],
                 "thisted": ["lokalt", "lokale-byer", "opvarmning", "faq", "pris", "guides"]})
FV_ORDER.update({"ebeltoft": ["status", "priser", "varmekilder", "andel", "faq", "billigst"],
                 "thisted": ["varmekilder", "priser", "status", "billigst", "andel", "faq"]})
SOL_PROD.update({
 "ebeltoft": ("Solcelleproduktion på Djursland",
   lambda: f"PVGIS 5.3 beregner ca. {tal(PV['ebeltoft']['syd'])} kWh pr. kWp om året for et sydvendt tag med 35° hældning i Ebeltoft – {rk(_PVs, 'ebeltoft', 'højeste')} værdi af de {nw()} byer på dette site. Ved den bedste hældning på {PV['ebeltoft']['opt_angle']}° bliver det ca. {tal(PV['ebeltoft']['opt'])} kWh. Et 6 kWp-anlæg giver ca. {tal(PV['ebeltoft']['syd']*6)} kWh om året, heraf ca. {tal(PV['ebeltoft']['months'][6]*6)} kWh i juli og ca. {tal(PV['ebeltoft']['months'][0]*6)} kWh i januar. Mod vest giver hver kWp ca. {tal(PV['ebeltoft']['vest'])} kWh og mod øst ca. {tal(PV['ebeltoft']['oest'])} kWh."),
 "thisted": ("Solceller ved Vesterhavet: produktion i Thy",
   lambda: f"Et sydvendt tag med 35° hældning i Thisted giver ca. {tal(PV['thisted']['syd'])} kWh pr. kWp om året ifølge PVGIS 5.3. Et anlæg på 6 kWp ender på ca. {tal(PV['thisted']['syd']*6)} kWh om året – ca. {tal(PV['thisted']['months'][5]*6)} kWh i juni, men kun ca. {tal(PV['thisted']['months'][11]*6)} kWh i december. Et vestvendt tag giver ca. {tal(PV['thisted']['vest'])} kWh pr. kWp og et østvendt ca. {tal(PV['thisted']['oest'])} kWh, så vest er det bedste alternativ, hvis du ikke har et sydvendt tag."),
})
SOL_PROD_SRC_NEW.update({"ebeltoft": ["pv_ebeltoft", "pvo_ebeltoft", "pvv_ebeltoft"], "thisted": ["pv_thisted", "pvo_thisted", "pvv_thisted"]})
SOL_ROOF.update({
 "ebeltoft": ("Fibercement, tegl og cementsten i Syddjurs",
   lambda: f"{rp('ebeltoft','06')} af parcel- og rækkehusene i Syddjurs Kommune har tag af <strong>fibercement</strong>, {rp('ebeltoft','10')} <strong>tegl</strong> og {rp('ebeltoft','08')} cementsten, og {rp('ebeltoft','12',1)} har metalplader – {rk(_rt('12'), 'ebeltoft', 'højeste')} andel af de {nw()} byer. Kommunen anbefaler paneler med antirefleksbelægning, så naboer og trafikanter ikke generes af genskin, og at du får en rådgiver til at vurdere, om tagkonstruktionen kan bære vægten. Et ældre fibercementtag bør også vurderes for asbest.",
   ["dst_bygb50", "syd_sol", "bolius_asb"]),
 "thisted": ("Flest fibercementtage på sitet: Thisted Kommune",
   lambda: f"{rp('thisted','06')} af parcel- og rækkehusene i Thisted Kommune har tag af <strong>fibercement</strong> – {rk(_rt('06'), 'thisted', 'højeste')} andel af de {nw()} byer – mens kun {rp('thisted','10')} har tegl, {rk(_rt('10'), 'thisted', 'laveste', rev=True)} andel. {rp('thisted','08')} har cementsten. Fibercementtage fra før 1984 kan indeholde asbest, så få taget vurderet, før der monteres solceller – og husk, at panelerne skal ligge plant med tagfladen, hvis du vil undgå en byggetilladelse.",
   ["dst_bygb50", "thi_sol", "bolius_asb"]),
})
SOL_HOMES.update({
 "ebeltoft": lambda: f"Syddjurs Kommune har {tal(STOCK['ebeltoft']['tot'])} beboede parcel- og rækkehuse. {pct(STOCK['ebeltoft']['B']['2000+'],STOCK['ebeltoft']['tot'])} er bygget i 2000 eller senere – {rk(_sb('2000+'), 'ebeltoft', 'højeste')} andel af de {nw()} byer – og {pct(STOCK['ebeltoft']['B']['før 1960'],STOCK['ebeltoft']['tot'])} før 1960. {pct(STOCK['ebeltoft']['ejer'],STOCK['ebeltoft']['tot'])} bebos af ejeren. Ebeltoft har {tal(town('ebeltoft','Ebeltoft'))} indbyggere, Hornslet {tal(town('ebeltoft','Hornslet'))}, Rønde {tal(town('ebeltoft','Rønde'))} og Ryomgård {tal(town('ebeltoft','Ryomgård'))}.",
 "thisted": lambda: f"Thisted Kommune har {tal(STOCK['thisted']['tot'])} beboede parcel- og rækkehuse, og {pct(STOCK['thisted']['parcel'],STOCK['thisted']['tot'])} er parcelhuse. {pct(STOCK['thisted']['B']['før 1960'],STOCK['thisted']['tot'])} er bygget før 1960 og {pct(STOCK['thisted']['B']['1960-1979'],STOCK['thisted']['tot'])} i 1960-1979, mens kun {pct(STOCK['thisted']['B']['2000+'],STOCK['thisted']['tot'])} er fra 2000 eller senere. Thisted har {tal(town('thisted','Thisted'))} indbyggere, Hurup {tal(town('thisted','Hurup'))}, Hanstholm {tal(town('thisted','Hanstholm'))} og Klitmøller {tal(town('thisted','Klitmøller'))}.",
})
SOL_HOMES_SRC_NEW.update({"ebeltoft": ["dst_by3"], "thisted": ["dst_by3"]})
SOL_HOMES_H.update({"ebeltoft": "Mange nyere huse: boligerne i Syddjurs", "thisted": "Ældre parcelhuse i Thy: boligerne i Thisted Kommune"})
SOL_XFAQ.update({
 "ebeltoft": [("Hvor meget strøm giver et 6 kWp-anlæg i Ebeltoft?", lambda: f"Ca. {tal(PV['ebeltoft']['syd']*6)} kWh om året på et sydvendt tag med 35° hældning ifølge PVGIS 5.3. Mod vest er det ca. {tal(PV['ebeltoft']['vest']*6)} kWh og mod øst ca. {tal(PV['ebeltoft']['oest']*6)} kWh.", ["pv_ebeltoft", "pvo_ebeltoft", "pvv_ebeltoft"])],
 "thisted": [("Hvor meget strøm giver et 6 kWp-anlæg i Thisted?", lambda: f"Ca. {tal(PV['thisted']['syd']*6)} kWh om året på et sydvendt tag med 35° hældning ifølge PVGIS 5.3. Mod vest er det ca. {tal(PV['thisted']['vest']*6)} kWh og mod øst ca. {tal(PV['thisted']['oest']*6)} kWh.", ["pv_thisted", "pvo_thisted", "pvv_thisted"])],
})
VP_HEAT.update({
 "ebeltoft": ("Ingen naturgas, men meget elvarme: opvarmningen i Syddjurs",
   lambda: f"Danmarks Statistik registrerer ingen beboede parcel- og rækkehuse med naturgas i Syddjurs Kommune. {tal(HEAT['ebeltoft']['FJ'])} af de {tal(hs('ebeltoft'))} huse ({hp('ebeltoft','FJ',1)}) har fjernvarme, {tal(HEAT['ebeltoft']['VP'])} ({hp('ebeltoft','VP',1)}) har allerede varmepumpe – {rk(_hf('VP'), 'ebeltoft', 'højeste')} andel af de {nw()} byer – og {tal(HEAT['ebeltoft']['ELV'])} ({hp('ebeltoft','ELV',1)}) har <strong>elvarme</strong>, mod {hp('dk','ELV',1)} på landsplan. {tal(HEAT['ebeltoft']['CO'])} ({hp('ebeltoft','CO',1)}) har oliefyr og {tal(HEAT['ebeltoft']['CA'])} anden centralvarme som fx træpiller."),
 "thisted": ("Seks ud af ti med fjernvarme – men mange oliefyr i Thy",
   lambda: f"{tal(HEAT['thisted']['FJ'])} af de {tal(hs('thisted'))} beboede parcel- og rækkehuse i Thisted Kommune ({hp('thisted','FJ',1)}) har fjernvarme. {tal(HEAT['thisted']['CO'])} ({hp('thisted','CO',1)}) har <strong>oliefyr</strong> – {rk(_hf('CO'), 'thisted', 'højeste')} andel af de {nw()} byer og mod {hp('dk','CO',1)} på landsplan – og {tal(HEAT['thisted']['CA'])} ({hp('thisted','CA',1)}) anden centralvarme som fx træpiller. {tal(HEAT['thisted']['CN'])} har naturgas, og {tal(HEAT['thisted']['VP'])} ({hp('thisted','VP',1)}) har allerede varmepumpe."),
})
VP_HEAT_SRC_NEW.update({"ebeltoft": ["syd_fv"], "thisted": ["thi_varme"]})
VP_TOWNS.update({
 "ebeltoft": [("Ebeltoft", "Ebeltoft Fjernvarmeværk (primært flis)", ["ef_2026", "ft_pris"]),
              ("Rønde", "Rønde Fjernvarmeværk – udvidelse prioriteret af byrådet i 2026", ["syd_energi", "ft_pris"]),
              ("Hornslet", "Hornslet Fjernvarmeselskab", ["ft_pris"]),
              ("Ryomgård og Kolind", "Ryomgård Fjernvarmeværk og Kolind Fjernvarmeværk", ["ft_pris"]),
              ("Mørke og Thorsager", "Mørke Fjernvarmeselskab og Thorsager Fjernvarmeværk", ["ft_pris"]),
              ("Knebel og Mols", "Intet fjernvarmeværk i Forsyningstilsynets prisstatistik", ["ft_pris"])],
 "thisted": [("Thisted og Klitmøller", "Thisted Varmeforsyning (affald, halm og geotermi)", ["tvf_prod", "ft_pris"]),
             ("Hanstholm", "Hanstholm Varmeværk", ["ft_pris"]),
             ("Hurup", "Hurup Fjernvarme", ["ft_pris"]),
             ("Snedsted", "Snedsted Varmeværk", ["ft_pris", "kun_snedsted"]),
             ("Vestervig", "Vestervig Fjernvarme – planer om varmepumper og ny tank", ["dbt_vest", "ft_pris"]),
             ("Vilsund, Sundby, Koldby, Hørdum og Hundborg", "Fjernvarmeprojekt trukket tilbage", ["kun_snedsted"])],
})
VP_TOWNS_NOTE.update({
 "ebeltoft": "Syddjurs har mange små fjernvarmeværker, men intet naturgasnet. Uden for byerne – fx på Mols – er alternativet til elvarme, olie eller træpiller derfor typisk en varmepumpe. Spørg dit lokale værk, om din adresse kan tilsluttes, før du vælger.",
 "thisted": "Thisted Kommune har en række fjernvarmeværker fra Hanstholm til Hurup. I landsbyerne i Midtthy, hvor fjernvarmeprojektet er trukket tilbage, er en varmepumpe det oplagte alternativ til olie- og gasfyret. Spørg dit lokale værk, om din adresse kan tilsluttes, før du vælger.",
})
VP_XFAQ.update({
 "ebeltoft": [("Hvor mange huse i Syddjurs har elvarme?", lambda: f"{tal(HEAT['ebeltoft']['ELV'])} af de {tal(hs('ebeltoft'))} beboede parcel- og rækkehuse ({hp('ebeltoft','ELV',1)}) ifølge Danmarks Statistik, 2026 – mod {hp('dk','ELV',1)} på landsplan. Har huset elpaneler uden radiatorer, er en luft til luft-varmepumpe ofte det billigste skifte; med radiatorer er det typisk en luft til vand-varmepumpe.", ["dst_bol102", "se_vp"]),
              ("Hvad koster en luft til vand-varmepumpe i Ebeltoft?", lambda: "SparEnergi angiver typisk 100.000-130.000 kr. inkl. montering, og Energisparer.dk ca. 90.000-150.000 kr. afhængigt af husets størrelse. Vi har ikke fundet kilder med en særlig Ebeltoft-pris. Til sammenligning koster et standardhus 14.566 kr. om året i fjernvarme hos Ebeltoft Fjernvarmeværk ifølge Forsyningstilsynet.", ["se_vp", "es_vp", "ft_pris"])],
 "thisted": [("Hvor mange huse i Thisted Kommune har oliefyr?", lambda: f"{tal(HEAT['thisted']['CO'])} af de {tal(hs('thisted'))} beboede parcel- og rækkehuse ({hp('thisted','CO',1)}) ifølge Danmarks Statistik, 2026, og {tal(HEAT['thisted']['CN'])} har naturgas. Ligger huset uden for et fjernvarmeområde, er en luft til vand-varmepumpe det typiske skifte.", ["dst_bol102"]),
             ("Hvad koster en luft til vand-varmepumpe i Thisted?", lambda: "SparEnergi angiver typisk 100.000-130.000 kr. inkl. montering, og Energisparer.dk ca. 90.000-150.000 kr. afhængigt af husets størrelse. Vi har ikke fundet kilder med en særlig Thisted-pris. Til sammenligning koster et standardhus 15.228 kr. om året i fjernvarme hos Thisted Varmeforsyning ifølge Forsyningstilsynet.", ["se_vp", "es_vp", "ft_pris"])],
})
FV_SOURCES.update({
 "ebeltoft": [("Ebeltoft Fjernvarme producerer i dag <strong>hovedparten af varmen på flis</strong>, men omstiller dele af produktionen til el og forventer investeringer for omkring <strong>80 mio. kr.</strong> over fem år – bl.a. fordi en fliskedel på 35-40 år ikke kan overholde kravene fra 2030.", ["ef_2026"]),
              ("I 2025 investerede værket i en <strong>absorptionsvarmepumpe</strong>, der genbruger varmen i røggassen, samt et solcelleanlæg og en ORC-turbine, som tilsammen forventes at dække op til 70 % af værkets eget elforbrug.", ["ef_2025"])],
 "thisted": [("Kraftvarmeværk Thisted brænder ca. <strong>50.000 tons affald</strong> om året og producerer ca. 130.000 MWh varme og 20.000 MWh el.", ["tvf_prod"]),
             ("Thisted Varmeforsyning har desuden et <strong>geotermianlæg</strong> med en boring på 1.243 m og halmvarmeanlæg, og centralerne i Hillerslev og Klitmøller er fusioneret ind i selskabet.", ["tvf_prod"])],
})
FV_SHARE.update({
 "ebeltoft": lambda: f"{hp('ebeltoft','FJ',1)} af de beboede parcel- og rækkehuse i Syddjurs Kommune har fjernvarme, mod {hp('dk','FJ',1)} i hele landet. Ingen har naturgas, mens {hp('ebeltoft','ELV',1)} har elvarme og {hp('ebeltoft','VP',1)} varmepumpe.",
 "thisted": lambda: f"{hp('thisted','FJ',1)} af de beboede parcel- og rækkehuse i Thisted Kommune har fjernvarme, mod {hp('dk','FJ',1)} i hele landet. {hp('thisted','CO',1)} har oliefyr og {hp('thisted','CN',1)} naturgas.",
})
FV_SOURCES_H.update({"ebeltoft": "Flis, røggas og egen strøm: her kommer varmen fra", "thisted": "Affald, halm og geotermi i Thisted"})
_reg_age_old23 = reg_age_note
def reg_age_note(c, kommune):
    s = STOCK[c]; B = s["B"]; t = s["tot"]
    if c == "ebeltoft":
        return (f"{tal(B['før 1960'])} af de beboede huse i Syddjurs Kommune ({pct(B['før 1960'], t)}) er bygget før 1960. Lokalplaner, byplanvedtægter og tinglyste deklarationer kan regulere eller forbyde solceller – også på et parcelhus, hvor der ellers ikke kræves byggetilladelse.", ["syd_sol"])
    if c == "thisted":
        return (f"{tal(B['før 1960'])} af de beboede huse i Thisted Kommune ({pct(B['før 1960'], t)}) er bygget før 1960. Er dit hus fredet eller bevaringsværdigt, gælder undtagelsen for solceller ikke – og en lokalplan kan fx kræve, at taget fremstår med rød tegl.", ["thi_sol"])
    return _reg_age_old23(c, kommune)


# ---------- dry-run 25. nov. 2026: Frederiksberg ----------
SOL_ORDER.update({
 "frederiksberg": ["boliger", "tage", "lokalt", "faq", "produktion", "guides"],
})
FV_ORDER.update({
 "frederiksberg": ["status", "opvarmning", "priser", "lokalt", "andel", "billigst", "lokale-byer", "faq", "varmekilder"],
})
SOL_PROD.update({
 "frederiksberg": ("Solceller på Frederiksberg: mod syd, øst eller vest",
   lambda: f"PVGIS 5.3 beregner ca. {tal(PV['frederiksberg']['syd'])} kWh pr. kWp om året for et sydvendt tag med 35° hældning på Frederiksberg (et 6 kWp-anlæg giver ca. {tal(PV['frederiksberg']['syd']*6)} kWh/år). Mod øst giver det ca. {tal(PV['frederiksberg']['oest'])} og mod vest ca. {tal(PV['frederiksberg']['vest'])} kWh pr. kWp – vigtigt, fordi kommunen på bevaringsværdige bygninger peger på placering mod gård- eller havesiden."),
})
SOL_PROD_SRC_NEW.update({"frederiksberg": ["pv_frederiksberg", "pvo_frederiksberg", "pvv_frederiksberg", "frb_bev"]})
SOL_ROOF.update({
 "frederiksberg": ("Tegltage dominerer på Frederiksberg",
   lambda: f"{rp('frederiksberg','10')} af parcel- og rækkehusene i Frederiksberg Kommune har <strong>tegltag</strong> ({rk(lambda x: ROOF[x]['T']['10'] / ROOF[x]['tot'], 'frederiksberg', 'højeste')} andel af de {nw()} byer, mod {rp('dk','10')} på landsplan), mens {rp('frederiksberg','06')} har fibercement og {pct(_flat('frederiksberg'), ROOF['frederiksberg']['tot'])} fladt tag eller tagpap. Kommunen stiller krav om, at solceller integreres nænsomt i tagfladen – fx nedfældet på skrå tage.",
   ["dst_bygb50", "frb_sol"]),
})
SOL_HOMES.update({
 "frederiksberg": lambda: f"Frederiksberg Kommune har {tal(STOCK['frederiksberg']['tot'])} beboede parcel- og rækkehuse, og {pct(STOCK['frederiksberg']['B']['før 1960'], STOCK['frederiksberg']['tot'])} er bygget før 1960 ({rk(lambda x: STOCK[x]['B']['før 1960'] / STOCK[x]['tot'], 'frederiksberg', 'højeste')} andel af de {nw()} byer, mod {pct(STOCK['dk']['B']['før 1960'], STOCK['dk']['tot'])} på landsplan). {pct(STOCK['frederiksberg']['raekke'], STOCK['frederiksberg']['tot'])} er række-, kæde- eller dobbelthuse, og kommunen vurderer bevaringsværdi og arkitektur i hver enkelt byggesag.",
})
SOL_HOMES_SRC_NEW.update({"frederiksberg": ["frb_sol", "frb_bev"]})
SOL_HOMES_H.update({"frederiksberg": "Ældre villaer og rækkehuse på Frederiksberg"})
SOL_XFAQ.update({
 "frederiksberg": [("Hvor mange huse på Frederiksberg har tegltag?", lambda: f"{tal(ROOF['frederiksberg']['T']['10'])} af de {tal(ROOF['frederiksberg']['tot'])} parcel- og rækkehuse med oplyst tagdækning ({rp('frederiksberg','10')}) har tegltag ifølge Danmarks Statistik (BYGB50, 2026), og {pct(STOCK['frederiksberg']['B']['før 1960'], STOCK['frederiksberg']['tot'])} af husene er bygget før 1960.", ["dst_bygb50", "dst_bol101"])],
})
VP_HEAT.update({
 "frederiksberg": ("97,6 % af husene på Frederiksberg har fjernvarme",
   lambda: f"{hp('frederiksberg','FJ',1)} af de {tal(hs('frederiksberg'))} beboede parcel- og rækkehuse i Frederiksberg Kommune har fjernvarme, mod {hp('dk','FJ')} på landsplan. Kun {tal(HEAT['frederiksberg']['CO'])} har oliefyr, {tal(HEAT['frederiksberg']['ELV'])} elvarme og {tal(HEAT['frederiksberg']['VP'])} varmepumpe, og Danmarks Statistik registrerer 0 huse med naturgas."),
})
VP_HEAT_SRC_NEW.update({"frederiksberg": ["frb_fv_varme"]})
VP_TOWNS.update({
 "frederiksberg": [("Hele kommunen", "99 % af alle boliger på Frederiksberg har fjernvarme via Frederiksberg Forsyning", ["frb_fv_varme"]),
                   ("Større ejendomme og nybyggeri", "CTR-fjernvarme med mindst 85 % fossilfri produktion", ["frb_fv_varme"])],
})
VP_TOWNS_NOTE.update({
 "frederiksberg": "Når 97,6 % af parcel- og rækkehusene allerede har fjernvarme og prisen ligger under landsgennemsnittet, er en varmepumpe sjældent rentabel som erstatning – den er primært relevant for de få boliger med elvarme eller oliefyr.",
})
VP_XFAQ.update({
 "frederiksberg": [("Hvor mange huse på Frederiksberg har ikke fjernvarme?", lambda: f"Kun {tal(hs('frederiksberg') - HEAT['frederiksberg']['FJ'])} af {tal(hs('frederiksberg'))} beboede parcel- og rækkehuse ({pct(hs('frederiksberg') - HEAT['frederiksberg']['FJ'], hs('frederiksberg'), 1)}) ifølge Danmarks Statistik, 2026. Heraf har {tal(HEAT['frederiksberg']['CO'])} oliefyr, {tal(HEAT['frederiksberg']['ELV'])} elvarme og {tal(HEAT['frederiksberg']['VP'])} varmepumpe.", ["dst_bol102"])],
})
FV_SOURCES.update({
 "frederiksberg": [("<strong>CTR-transmissionsnettet:</strong> Frederiksberg Forsyning køber fjernvarme via Centralkommunernes Transmissionsselskab fra hovedstadsområdets kraftvarmeværker og affaldsanlæg.", ["frb_fv_varme"]),
                   ("<strong>Mindst 85 % fossilfri:</strong> produktionen er baseret på bl.a. træpiller, halmpiller, affald og geotermi; målet i forsyningens miljødeklaration er løbende udfasning af fossile brændsler.", ["frb_fv_varme", "frb_fv_miljoe"])],
})
FV_SHARE.update({
 "frederiksberg": lambda: f"{hp('frederiksberg','FJ',1)} af de beboede parcel- og rækkehuse i Frederiksberg Kommune har fjernvarme, mod {hp('dk','FJ',1)} i hele landet. Det efterlader kun {tal(hs('frederiksberg') - HEAT['frederiksberg']['FJ'])} huse med anden opvarmning, heraf {tal(HEAT['frederiksberg']['VP'])} med varmepumpe.",
})
FV_SOURCES_H.update({"frederiksberg": "CTR-fjernvarme fra fossilfrie brændsler"})
_reg_age_old24 = reg_age_note
def reg_age_note(c, kommune):
    s = STOCK[c]; B = s["B"]; t = s["tot"]
    if c == "frederiksberg":
        return (f"{tal(B['før 1960'])} af de beboede parcel- og rækkehuse i Frederiksberg Kommune ({pct(B['før 1960'], t)}) er bygget før 1960. På Frederiksberg skal du altid søge byggetilladelse til solceller, og kommunen vurderer bevaringsværdi og tagfladens arkitektur i hver enkelt sag.", ["frb_sol", "frb_bev"])
    return _reg_age_old24(c, kommune)


# ---------- daglig by-rutine 25. nov. 2026: Gentofte ----------
SOL_ORDER.update({
 "gentofte": ["tage", "boliger", "produktion", "lokalt", "faq", "guides"],
})
VP_ORDER.update({
 "gentofte": ["opvarmning", "lokale-byer", "pris", "lokalt", "faq", "guides"],
})
FV_ORDER.update({
 "gentofte": ["status", "varmekilder", "priser", "andel", "billigst", "faq"],
})
SOL_PROD.update({
 "gentofte": ("Solindstråling i Gentofte: syd, øst og vest",
  lambda: f"PVGIS 5.3 beregner ca. {tal(PV['gentofte']['syd'])} kWh pr. kWp om året på et sydvendt 35°-tag i Gentofte – ca. {tal(PV['gentofte']['syd']*6)} kWh om året for et 6 kWp-anlæg, toppende med ca. {tal(PV['gentofte']['months'][4]*6)} kWh i maj og {tal(PV['gentofte']['months'][5]*6)} kWh i juni. Et vestvendt tag giver ca. {tal(PV['gentofte']['vest'])} kWh pr. kWp og et østvendt ca. {tal(PV['gentofte']['oest'])} kWh pr. kWp, mens optimal hældning på {PV['gentofte']['opt_angle']}° mod syd giver ca. {tal(PV['gentofte']['opt'])} kWh."),
})
SOL_PROD_SRC_NEW.update({"gentofte": ["pv_gentofte", "pvo_gentofte", "pvv_gentofte"]})
SOL_ROOF.update({
 "gentofte": ("Næsten to ud af tre huse i Gentofte har tegltag",
  lambda: f"{rp('gentofte','10')} af parcel- og rækkehusene i Gentofte Kommune har <strong>tegltag</strong> – {rk(lambda x: ROOF[x]['T']['10'] / ROOF[x]['tot'], 'gentofte', 'højeste')} andel af de {nw()} byer, mod {rp('dk','10')} på landsplan – mens {rp('gentofte','04')} har tagpap med hældning og kun {rp('gentofte','06')} fibercement ({rk(lambda x: ROOF[x]['T']['06'] / ROOF[x]['tot'], 'gentofte', 'laveste', rev=True)} andel på sitet). På bevaringsværdige huse kræver solceller altid tilladelse via en planmæssig forespørgsel.",
  ["dst_bygb50", "gen_sol_byg", "gen_bev"]),
})
SOL_HOMES.update({
 "gentofte": lambda: f"Gentofte Kommune tæller {tal(STOCK['gentofte']['tot'])} beboede parcel- og rækkehuse, hvoraf {pct(STOCK['gentofte']['B']['før 1960'], STOCK['gentofte']['tot'])} er opført før 1960 ({rk(lambda x: STOCK[x]['B']['før 1960'] / STOCK[x]['tot'], 'gentofte', 'højeste')} andel af de {nw()} byer, mod {pct(STOCK['dk']['B']['før 1960'], STOCK['dk']['tot'])} i hele landet). {pct(STOCK['gentofte']['ejer'], STOCK['gentofte']['tot'])} er ejerboliger, og {pct(STOCK['gentofte']['raekke'], STOCK['gentofte']['tot'])} er række-, kæde- eller dobbelthuse.",
})
SOL_HOMES_SRC_NEW.update({"gentofte": ["gen_bev"]})
SOL_HOMES_H.update({"gentofte": "Klassiske villaer før 1960 i Gentofte"})
SOL_XFAQ.update({
 "gentofte": [("Hvor mange villaer i Gentofte har tegltag?", lambda: f"{tal(ROOF['gentofte']['T']['10'])} af de {tal(ROOF['gentofte']['tot'])} parcel- og rækkehuse med oplyst tag ({rp('gentofte','10')}) har tegltag ifølge Danmarks Statistik (BYGB50, 2026), og {pct(STOCK['gentofte']['B']['før 1960'], STOCK['gentofte']['tot'])} af husene er bygget før 1960.", ["dst_bygb50", "dst_bol101"])],
})
VP_HEAT.update({
 "gentofte": ("Hvert fjerde hus i Gentofte har stadig naturgas",
  lambda: f"{tal(HEAT['gentofte']['FJ'])} af de {tal(hs('gentofte'))} beboede parcel- og rækkehuse i Gentofte Kommune ({hp('gentofte','FJ',1)}) har fjernvarme, men {tal(HEAT['gentofte']['CN'])} huse ({hp('gentofte','CN',1)}) varmer stadig med <strong>naturgas</strong>, {tal(HEAT['gentofte']['CO'])} med oliefyr og {tal(HEAT['gentofte']['ELV'])} med elvarme. {tal(HEAT['gentofte']['VP'])} huse ({hp('gentofte','VP',1)}) har allerede varmepumpe."),
})
VP_HEAT_SRC_NEW.update({"gentofte": ["gen_forsyning", "gen_niras"]})
VP_TOWNS.update({
 "gentofte": [("Eksisterende fjernvarmeområder", "Gentofte Gladsaxe Fjernvarme (tilslutningsbidrag 90.000 kr. inkl. moms i 2026)", ["gen_forsyning", "gen_fv_tilslut"]),
              ("Delområder 4.6, 4.7, 4.8 og 5.4–5.8", "Fjernvarmeudbygning aflyst 22. juni 2026; omklassificeret til luft til vand-varmepumper", ["gen_forsyning", "gen_niras"]),
              ("Igangværende udbygningsområder", "Gentofte Gladsaxe Fjernvarme (kampagnetilslutning 0 kr. i særlige områder)", ["gen_fv_tilslut"])],
})
VP_TOWNS_NOTE.update({
 "gentofte": "Efter kommunalbestyrelsens beslutning den 22. juni 2026 om at stoppe fjernvarme i otte ikke-igangsatte delområder skal husejere dér som udgangspunkt skifte fra gasfyr til individuel varmepumpe. Bor du i et igangværende eller eksisterende område, kan du slå din adresse op hos Gentofte Gladsaxe Fjernvarme.",
})
VP_XFAQ.update({
 "gentofte": [("Hvor mange huse i Gentofte har naturgas i dag?", lambda: f"{tal(HEAT['gentofte']['CN'])} af {tal(hs('gentofte'))} beboede parcel- og rækkehuse ({hp('gentofte','CN',1)}) ifølge Danmarks Statistik, 2026. Desuden har {tal(HEAT['gentofte']['CO'])} huse oliefyr og {tal(HEAT['gentofte']['ELV'])} elvarme.", ["dst_bol102"])],
})
FV_SOURCES.update({
 "gentofte": [("<strong>CTR og 94 % fossilfri brændsler:</strong> Gentofte Fjernvarme køber varmen gennem Centralkommunernes Transmissionsselskab. I miljødeklarationen for 2024 kom 37,2 % fra træpiller, 30,3 % fra flis, 23,0 % fra bioaffald, 2,3 % fra halm og 1,9 % fra biogas.", ["gen_fv_miljoe"]),
              ("<strong>Store centrale varmepumper på vej:</strong> Gentofte Gladsaxe Fjernvarme arbejder sammen med CTR om yderligere vedvarende kilder, herunder store varmepumper.", ["gen_fv_miljoe", "gen_forsyning"])],
})
FV_SHARE.update({
 "gentofte": lambda: f"{hp('gentofte','FJ',1)} af de beboede parcel- og rækkehuse i Gentofte Kommune har fjernvarme, mod {hp('dk','FJ',1)} på landsplan, mens {hp('gentofte','CN',1)} stadig fyrer med naturgas.",
})
FV_SOURCES_H.update({"gentofte": "CTR-varme og 94 % fossilfrie brændsler i Gentofte"})
_reg_age_old25 = reg_age_note
def reg_age_note(c, kommune):
    s = STOCK[c]; B = s["B"]; t = s["tot"]
    if c == "gentofte":
        return (f"{tal(B['før 1960'])} af de beboede parcel- og rækkehuse i Gentofte Kommune ({pct(B['før 1960'], t)}) er bygget før 1960. På almindelige huse kræver solceller normalt ikke tilladelse, men på bevaringsværdige bygninger skal du altid søge som en planmæssig forespørgsel i Byg- og Miljøportalen.", ["gen_sol_byg", "gen_bev"])
    return _reg_age_old25(c, kommune)

# ---------- daglig by-rutine 26. nov. 2026: Hvidovre og Hørsholm ----------
SOL_ORDER.update({
 "hvidovre": ["produktion", "tage", "boliger", "lokalt", "faq", "guides"],
 "hoersholm": ["boliger", "tage", "produktion", "lokalt", "faq", "guides"],
})
VP_ORDER.update({
 "hvidovre": ["lokale-byer", "opvarmning", "pris", "lokalt", "faq", "guides"],
 "hoersholm": ["opvarmning", "pris", "lokale-byer", "lokalt", "faq", "guides"],
})
FV_ORDER.update({
 "hvidovre": ["status", "priser", "varmekilder", "andel", "billigst", "faq"],
 "hoersholm": ["status", "varmekilder", "andel", "priser", "billigst", "faq"],
})
SOL_PROD.update({
 "hvidovre": ("Hvidovres solindstråling: sydtag, øst-vest og optimal hældning",
  lambda: f"I Hvidovre giver et sydvendt tag med 35° hældning ifølge PVGIS 5.3 ca. {tal(PV['hvidovre']['syd'])} kWh pr. kWp om året. Et 6 kWp-anlæg når dermed ca. {tal(PV['hvidovre']['syd']*6)} kWh, med ca. {tal(PV['hvidovre']['months'][4]*6)} kWh i maj og {tal(PV['hvidovre']['months'][5]*6)} kWh i juni. Vender taget mod vest, falder udbyttet til ca. {tal(PV['hvidovre']['vest'])} kWh pr. kWp, og mod øst er det ca. {tal(PV['hvidovre']['oest'])} kWh. Den optimale hældning på {PV['hvidovre']['opt_angle']}° mod syd giver ca. {tal(PV['hvidovre']['opt'])} kWh pr. kWp."),
 "hoersholm": ("Solindstråling i Hørsholm: hvad et sydtag og et østvesttag giver",
  lambda: f"PVGIS 5.3 beregner for Hørsholm ca. {tal(PV['hoersholm']['syd'])} kWh pr. kWp om året på et sydvendt 35°-tag, altså ca. {tal(PV['hoersholm']['syd']*6)} kWh om året for 6 kWp. Produktionen topper i maj (ca. {tal(PV['hoersholm']['months'][4]*6)} kWh) og juni (ca. {tal(PV['hoersholm']['months'][5]*6)} kWh). Et vestvendt tag giver ca. {tal(PV['hoersholm']['vest'])} kWh pr. kWp, et østvendt ca. {tal(PV['hoersholm']['oest'])} kWh, og den optimale hældning på {PV['hoersholm']['opt_angle']}° mod syd ca. {tal(PV['hoersholm']['opt'])} kWh pr. kWp."),
})
SOL_PROD_SRC_NEW.update({"hvidovre": ["pv_hvidovre", "pvo_hvidovre", "pvv_hvidovre"], "hoersholm": ["pv_hoersholm", "pvo_hoersholm", "pvv_hoersholm"]})
SOL_ROOF.update({
 "hvidovre": ("Mere end hvert fjerde hus i Hvidovre har fibercementtag",
  lambda: f"{rp('hvidovre','06')} af parcel- og rækkehusene i Hvidovre Kommune har <strong>fibercementtag inkl. asbest</strong> mod {rp('dk','06')} på landsplan, mens {rp('hvidovre','10')} har tegl, {rp('hvidovre','08')} cementsten, {rp('hvidovre','04')} tagpap med hældning og {rp('hvidovre','02')} built-up. Har taget asbestholdig fibercement, kræver monteringen forsigtighed.",
  ["dst_bygb50", "bolius_asb"]),
 "hoersholm": ("Næsten hvert andet hus i Hørsholm har tegltag",
  lambda: f"{rp('hoersholm','10')} af parcel- og rækkehusene i Hørsholm Kommune har <strong>tegltag</strong> mod {rp('dk','10')} på landsplan, {rp('hoersholm','06')} har fibercement inkl. asbest, {rp('hoersholm','02')} built-up og {rp('hoersholm','04')} tagpap med hældning. Kræver en lokalplan, at solceller er integreret i tagfladen, er tagtypen afgørende for monteringen.",
  ["dst_bygb50", "hsm_sol"]),
})
SOL_HOMES.update({
 "hvidovre": lambda: f"Hvidovre Kommune tæller {tal(STOCK['hvidovre']['tot'])} beboede parcel- og rækkehuse, hvoraf {pct(STOCK['hvidovre']['B']['før 1960'], STOCK['hvidovre']['tot'])} er opført før 1960 og {pct(STOCK['hvidovre']['B']['1960-1979'], STOCK['hvidovre']['tot'])} i 1960–79. {pct(STOCK['hvidovre']['ejer'], STOCK['hvidovre']['tot'])} er ejerboliger, og {pct(STOCK['hvidovre']['raekke'], STOCK['hvidovre']['tot'])} er række-, kæde- eller dobbelthuse mod {pct(STOCK['dk']['raekke'], STOCK['dk']['tot'])} på landsplan.",
 "hoersholm": lambda: f"Hørsholm Kommune har {tal(STOCK['hoersholm']['tot'])} beboede parcel- og rækkehuse. {pct(STOCK['hoersholm']['B']['1960-1979'], STOCK['hoersholm']['tot'])} er opført i 1960–79, {pct(STOCK['hoersholm']['B']['før 1960'], STOCK['hoersholm']['tot'])} før 1960 og {pct(STOCK['hoersholm']['B']['1980-1999'], STOCK['hoersholm']['tot'])} i 1980–99. {pct(STOCK['hoersholm']['ejer'], STOCK['hoersholm']['tot'])} er ejerboliger, og {pct(STOCK['hoersholm']['raekke'], STOCK['hoersholm']['tot'])} er række-, kæde- eller dobbelthuse.",
})
SOL_HOMES_SRC_NEW.update({"hvidovre": ["hvi_bev"], "hoersholm": ["hsm_bev"]})
SOL_HOMES_H.update({"hvidovre": "Parcel- og rækkehuse i Hvidovre: bevaringsværdi og alder", "hoersholm": "Parcelhuse fra 1960'erne og 70'erne i Hørsholm"})
SOL_XFAQ.update({
 "hvidovre": [("Hvor mange huse i Hvidovre har fibercementtag?", lambda: f"{tal(ROOF['hvidovre']['T']['06'])} af de {tal(ROOF['hvidovre']['tot'])} parcel- og rækkehuse med oplyst tag ({rp('hvidovre','06')}) har fibercement inkl. asbest ifølge Danmarks Statistik (BYGB50, 2026).", ["dst_bygb50"])],
 "hoersholm": [("Hvor mange huse i Hørsholm har tegltag?", lambda: f"{tal(ROOF['hoersholm']['T']['10'])} af de {tal(ROOF['hoersholm']['tot'])} parcel- og rækkehuse med oplyst tag ({rp('hoersholm','10')}) har tegltag ifølge Danmarks Statistik (BYGB50, 2026).", ["dst_bygb50"])],
})
VP_HEAT.update({
 "hvidovre": ("Næsten halvdelen af husene i Hvidovre varmes stadig med naturgas",
  lambda: f"{tal(HEAT['hvidovre']['FJ'])} af de {tal(hs('hvidovre'))} beboede parcel- og rækkehuse i Hvidovre Kommune ({hp('hvidovre','FJ',1)}) har fjernvarme, mens {tal(HEAT['hvidovre']['CN'])} huse ({hp('hvidovre','CN',1)}) varmer med <strong>naturgas</strong>, {tal(HEAT['hvidovre']['VP'])} ({hp('hvidovre','VP',1)}) med varmepumpe, {tal(HEAT['hvidovre']['ELV'])} med elvarme og {tal(HEAT['hvidovre']['CO'])} med oliefyr."),
 "hoersholm": ("Over halvdelen af husene i Hørsholm har stadig naturgas",
  lambda: f"{tal(HEAT['hoersholm']['CN'])} af de {tal(hs('hoersholm'))} beboede parcel- og rækkehuse i Hørsholm Kommune ({hp('hoersholm','CN',1)}) varmer med <strong>naturgas</strong>, mens {tal(HEAT['hoersholm']['FJ'])} ({hp('hoersholm','FJ',1)}) har fjernvarme, {tal(HEAT['hoersholm']['VP'])} ({hp('hoersholm','VP',1)}) varmepumpe, {tal(HEAT['hoersholm']['ELV'])} elvarme og {tal(HEAT['hoersholm']['CO'])} oliefyr."),
})
VP_HEAT_SRC_NEW.update({"hvidovre": ["hvi_varmeplan", "hvi_groen"], "hoersholm": ["hsm_varme"]})
VP_TOWNS.update({
 "hvidovre": [("Hvidovre (kommunens del af hovedstadsområdet)", "Fjernvarme fra FD Hvidovre og Avedøre Fjernvarme; flere områder udbygges", ["hvi_fv", "hvi_hfs"]),
              ("Nymarken og Mågeparken", "Udbygningsområde hos Hvidovre Fjernvarme (nyhedsbreve november 2026)", ["hvi_fv"]),
              ("Strandmark Nord", "Udbygningsområde hos Hvidovre Fjernvarme (nyhedsbrev november 2026)", ["hvi_fv"]),
              ("Avedøre Landsby", "Udbygningsområde hos Hvidovre Fjernvarme", ["hvi_fv"])],
 "hoersholm": [("Hørsholm-byområdet (delen i Hørsholm Kommune)", "Norfors; nye områder ikke længere på vej – kommunen arbejder for at konvertere gasområder til fjernvarme inden 2035", ["hsm_varme"]),
               ("Eksisterende Norfors-områder", "Uforpligtende tilbud hos Norfors for adresser i områder med fjernvarme", ["hsm_nf"]),
               ("Områder uden fjernvarme", "Projektforslaget om nye områder er trukket tilbage; varmepumpe er den vej, kommunen peger på", ["hsm_varme"])],
})
VP_TOWNS_NOTE.update({
 "hvidovre": "Hvidovre Kommune har kun ét byområde i Danmarks Statistiks opgørelse, så indbyggertallet gælder byområdet og opvarmningstallene hele kommunen. Hvilke veje der får fjernvarme først, afgør udbygningsplanen hos Hvidovre Fjernvarme – spørg dem, før du vælger anden varmekilde.",
 "hoersholm": "Hørsholm-byområdet strækker sig ind i Rudersdal og Fredensborg Kommune. Danmarks Statistik opgør 48.797 indbyggere i alt, hvoraf 24.833 bor i Hørsholm Kommune. Opvarmningstallene gælder hele Hørsholm Kommune. Om din adresse er udlagt til fjernvarme, ser du på kommunens varmeplanskort.",
})
VP_XFAQ.update({
 "hvidovre": [("Hvor mange huse i Hvidovre har varmepumpe?", lambda: f"{tal(HEAT['hvidovre']['VP'])} af {tal(hs('hvidovre'))} beboede parcel- og rækkehuse ({hp('hvidovre','VP',1)}) har varmepumpe ifølge Danmarks Statistik, 2026, mens {tal(HEAT['hvidovre']['CN'])} ({hp('hvidovre','CN',1)}) har naturgas.", ["dst_bol102"])],
 "hoersholm": [("Hvor mange huse i Hørsholm har varmepumpe?", lambda: f"{tal(HEAT['hoersholm']['VP'])} af {tal(hs('hoersholm'))} beboede parcel- og rækkehuse ({hp('hoersholm','VP',1)}) har varmepumpe ifølge Danmarks Statistik, 2026, og {tal(HEAT['hoersholm']['CN'])} ({hp('hoersholm','CN',1)}) har naturgas.", ["dst_bol102"])],
})
FV_SOURCES.update({
 "hvidovre": [("<strong>Fordelingsselskab:</strong> Hvidovre Fjernvarmeselskab, stiftet i 1984 og ejet af kommunen og distributionsselskaberne, tager sig af nyanlæg, finansiering og køb og salg af varme. Planen er, at hele Hvidovre konverteres til fjernvarmeområde.", ["hvi_hfs"]),
              ("<strong>Spidslastcentral i Avedøre:</strong> Avedøre Fjernvarmes kedler på Rebslagerporten sættes i drift, når der er behov, og centralen har status som spidslastcentral for vestegnens fjernvarmeforsyning.", ["hvi_ave_om"]),
              ("<strong>Miljødeklarationer:</strong> Avedøre Fjernvarme har offentliggjort miljødeklarationer for 2022–2025, og Hvidovre Fjernvarmeselskab har en miljødeklaration på sin side.", ["hvi_ave_om", "hvi_hfs"])],
 "hoersholm": [("<strong>Usserødværket:</strong> værket leverer varmen til Norfors' fjernvarmeområder, og usikkerheden om værkets fremtid påvirker udrulningen af fjernvarme i Hørsholm og nabokommunerne.", ["hsm_varme"]),
               ("<strong>Fire forsyningsområder:</strong> Norfors Fjernvarme består af sammenhængende områder i Hørsholm, Rudersdal, Fredensborg og Allerød Kommune.", ["hsm_nf"])],
})
FV_SHARE.update({
 "hvidovre": lambda: f"Fjernvarme findes i {hp('hvidovre','FJ',1)} af de beboede parcel- og rækkehuse i Hvidovre Kommune (landet: {hp('dk','FJ',1)}), og {hp('hvidovre','CN',1)} fyrer stadig med naturgas.",
 "hoersholm": lambda: f"I Hørsholm Kommune har {hp('hoersholm','FJ',1)} af de beboede parcel- og rækkehuse fjernvarme mod {hp('dk','FJ',1)} på landsplan, og {hp('hoersholm','CN',1)} bruger naturgas.",
})
FV_SOURCES_H.update({"hvidovre": "Fordelingsselskab og spidslast: sådan leveres varmen i Hvidovre", "hoersholm": "Usserødværket og Norfors' fire forsyningsområder"})
_reg_age_old26 = reg_age_note
def reg_age_note(c, kommune):
    s = STOCK[c]; B = s["B"]; t = s["tot"]
    if c == "hvidovre":
        return (f"{tal(B['før 1960'])} af de beboede parcel- og rækkehuse i Hvidovre Kommune ({pct(B['før 1960'], t)}) er bygget før 1960. Næsten alle ejendomme er omfattet af en lokalplan eller byplanvedtægt, så tjek planen for din adresse og om huset er bevaringsværdigt, før du bestiller solceller.", ["hvi_bygg", "hvi_bev"])
    if c == "hoersholm":
        return (f"{tal(B['før 1960'])} af de beboede parcel- og rækkehuse i Hørsholm Kommune ({pct(B['før 1960'], t)}) er bygget før 1960. På huse udpeget som bevaringsværdige i Temalokalplan 143 skal kommunen godkende ændringer af husets ydre, så spørg kommunen, før solceller kommer på et sådant tag.", ["hsm_bev"])
    return _reg_age_old26(c, kommune)

# ---------- daglig by-rutine 27. nov. 2026: Rødovre og Ballerup ----------
SOL_ORDER.update({
 "roedovre": ["tage", "boliger", "produktion", "lokalt", "faq", "guides"],
 "ballerup": ["boliger", "produktion", "tage", "lokalt", "faq", "guides"],
})
VP_ORDER.update({
 "roedovre": ["opvarmning", "lokale-byer", "pris", "lokalt", "faq", "guides"],
 "ballerup": ["pris", "opvarmning", "lokale-byer", "lokalt", "faq", "guides"],
})
FV_ORDER.update({
 "roedovre": ["status", "andel", "priser", "varmekilder", "billigst", "faq"],
 "ballerup": ["priser", "status", "varmekilder", "andel", "billigst", "faq"],
})
SOL_PROD.update({
 "roedovre": ("Solindstråling i Rødovre: sydtag, øst-vest og optimal vinkel",
  lambda: f"PVGIS 5.3 giver for Rødovre ca. {tal(PV['roedovre']['syd'])} kWh pr. kWp om året på et sydvendt tag med 35° hældning, så et 6 kWp-anlæg når ca. {tal(PV['roedovre']['syd']*6)} kWh. Maj giver ca. {tal(PV['roedovre']['months'][4]*6)} kWh og juni ca. {tal(PV['roedovre']['months'][5]*6)} kWh, mens december kun giver ca. {tal(PV['roedovre']['months'][11]*6)} kWh. Et vestvendt tag giver ca. {tal(PV['roedovre']['vest'])} kWh pr. kWp, et østvendt ca. {tal(PV['roedovre']['oest'])} kWh, og den optimale hældning på {PV['roedovre']['opt_angle']}° mod syd giver ca. {tal(PV['roedovre']['opt'])} kWh pr. kWp."),
 "ballerup": ("Hvad giver solen i Ballerup? Syd, øst-vest og optimal hældning",
  lambda: f"Ifølge PVGIS 5.3 producerer et sydvendt 35°-tag i Ballerup ca. {tal(PV['ballerup']['syd'])} kWh pr. kWp om året. Med 6 kWp bliver det ca. {tal(PV['ballerup']['syd']*6)} kWh, heraf ca. {tal(PV['ballerup']['months'][4]*6)} kWh i maj og ca. {tal(PV['ballerup']['months'][5]*6)} kWh i juni. Vest giver ca. {tal(PV['ballerup']['vest'])} kWh pr. kWp, øst ca. {tal(PV['ballerup']['oest'])} kWh, og med den optimale hældning på {PV['ballerup']['opt_angle']}° mod syd ca. {tal(PV['ballerup']['opt'])} kWh pr. kWp."),
})
SOL_PROD_SRC_NEW.update({"roedovre": ["pv_roedovre", "pvo_roedovre", "pvv_roedovre"], "ballerup": ["pv_ballerup", "pvo_ballerup", "pvv_ballerup"]})
SOL_ROOF.update({
 "roedovre": ("Mere end fire ud af ti huse i Rødovre har tegltag",
  lambda: f"{rp('roedovre','10')} af parcel- og rækkehusene i Rødovre Kommune har <strong>tegltag</strong> mod {rp('dk','10')} på landsplan, {rp('roedovre','06')} har fibercement inkl. asbest, {rp('roedovre','08')} cementsten, {rp('roedovre','04')} tagpap med hældning og {rp('roedovre','02')} built-up. Kommunens retningslinjer vil have anlæg, der følger tagfladens hældning og har tagets farve, så tagtypen har betydning for, hvordan anlægget skal se ud.",
  ["dst_bygb50", "rod_sol"]),
 "ballerup": ("Næsten hvert tredje hus i Ballerup har fibercementtag",
  lambda: f"{rp('ballerup','06')} af parcel- og rækkehusene i Ballerup Kommune har <strong>fibercementtag inkl. asbest</strong> mod {rp('dk','06')} på landsplan, {rp('ballerup','10')} har tegl, {rp('ballerup','08')} cementsten, {rp('ballerup','04')} tagpap med hældning og {rp('ballerup','02')} built-up. Har taget asbestholdig fibercement, kræver monteringen forsigtighed.",
  ["dst_bygb50", "bolius_asb"]),
})
SOL_HOMES.update({
 "roedovre": lambda: f"Rødovre Kommune tæller {tal(STOCK['roedovre']['tot'])} beboede parcel- og rækkehuse, hvoraf {pct(STOCK['roedovre']['B']['før 1960'], STOCK['roedovre']['tot'])} er opført før 1960 og {pct(STOCK['roedovre']['B']['1960-1979'], STOCK['roedovre']['tot'])} i 1960–79. {pct(STOCK['roedovre']['ejer'], STOCK['roedovre']['tot'])} er ejerboliger, og {pct(STOCK['roedovre']['raekke'], STOCK['roedovre']['tot'])} er række-, kæde- eller dobbelthuse mod {pct(STOCK['dk']['raekke'], STOCK['dk']['tot'])} på landsplan.",
 "ballerup": lambda: f"Ballerup Kommune har {tal(STOCK['ballerup']['tot'])} beboede parcel- og rækkehuse. {pct(STOCK['ballerup']['B']['1960-1979'], STOCK['ballerup']['tot'])} er opført i 1960–79, {pct(STOCK['ballerup']['B']['1980-1999'], STOCK['ballerup']['tot'])} i 1980–99 og kun {pct(STOCK['ballerup']['B']['før 1960'], STOCK['ballerup']['tot'])} før 1960. {pct(STOCK['ballerup']['ejer'], STOCK['ballerup']['tot'])} er ejerboliger, og {pct(STOCK['ballerup']['raekke'], STOCK['ballerup']['tot'])} er række-, kæde- eller dobbelthuse.",
})
SOL_HOMES_SRC_NEW.update({"roedovre": ["rod_bev"], "ballerup": ["bal_bev"]})
SOL_HOMES_H.update({"roedovre": "Rækkehuse og SAVE-værdier i Rødovre", "ballerup": "Over halvdelen af husene i Ballerup er fra 1960'erne og 70'erne"})
SOL_XFAQ.update({
 "roedovre": [("Hvor mange huse i Rødovre har tegltag?", lambda: f"{tal(ROOF['roedovre']['T']['10'])} af de {tal(ROOF['roedovre']['tot'])} parcel- og rækkehuse med oplyst tag ({rp('roedovre','10')}) har tegltag ifølge Danmarks Statistik (BYGB50, 2026).", ["dst_bygb50"])],
 "ballerup": [("Hvor mange huse i Ballerup har fibercementtag?", lambda: f"{tal(ROOF['ballerup']['T']['06'])} af de {tal(ROOF['ballerup']['tot'])} parcel- og rækkehuse med oplyst tag ({rp('ballerup','06')}) har fibercement inkl. asbest ifølge Danmarks Statistik (BYGB50, 2026).", ["dst_bygb50"])],
})
VP_HEAT.update({
 "roedovre": ("Over halvdelen af husene i Rødovre varmes med naturgas",
  lambda: f"{tal(HEAT['roedovre']['CN'])} af de {tal(hs('roedovre'))} beboede parcel- og rækkehuse i Rødovre Kommune ({hp('roedovre','CN',1)}) varmer med <strong>naturgas</strong>, mens {tal(HEAT['roedovre']['FJ'])} ({hp('roedovre','FJ',1)}) har fjernvarme, {tal(HEAT['roedovre']['VP'])} ({hp('roedovre','VP',1)}) varmepumpe, {tal(HEAT['roedovre']['ELV'])} elvarme og {tal(HEAT['roedovre']['CO'])} oliefyr."),
 "ballerup": ("Næsten to tredjedele af husene i Ballerup fyrer med naturgas",
  lambda: f"{tal(HEAT['ballerup']['CN'])} af de {tal(hs('ballerup'))} beboede parcel- og rækkehuse i Ballerup Kommune ({hp('ballerup','CN',1)}) varmer med <strong>naturgas</strong>, mens {tal(HEAT['ballerup']['FJ'])} ({hp('ballerup','FJ',1)}) har fjernvarme, {tal(HEAT['ballerup']['VP'])} ({hp('ballerup','VP',1)}) varmepumpe, {tal(HEAT['ballerup']['ELV'])} elvarme og {tal(HEAT['ballerup']['CO'])} oliefyr."),
})
VP_HEAT_SRC_NEW.update({"roedovre": ["rod_varme"], "ballerup": ["bal_vp"]})
VP_TOWNS.update({
 "roedovre": [("Rødovre (kommunens del af hovedstadsområdet)", "Fjernvarme fra Rødovre Kommunale Fjernvarmeforsyning (varme fra VEKS) i fem separate ledningsnet", ["rkf_om"]),
              ("Nord og syd for Roskildevej", "Udbygning ventes afsluttet i 2028 (nord) og 2027 (syd); tilmelding er åben", ["rkf_faq", "rkf_om"]),
              ("Islev og nord og syd for Jyllingevej", "Udrulning 2026–2032 efter interesse og teknisk mulighed", ["rkf_ny", "rkf_faq"])],
 "ballerup": [("Ballerup (kommunens del af hovedstadsområdet)", "Fjernvarme fra Vestforbrænding; etape 1 til 2028 og etape 2 2026–2030", ["bal_fv", "vf_bal"]),
              ("Skovlunde", "Etape 1: Skovlunde Ø, V og N forventes tilsluttet 2026–2027", ["bal_fv"]),
              ("Måløv og Egebjerg", "Gershøj og Egebjerg V afsluttet; Måløv S og Ø i etape 2 (2027–2030)", ["bal_fv"]),
              ("Bjørnekær, Smørumvej og Baneskrænten", "Fjernvarme fra Smørum Kraftvarmeværk senest 2030", ["bal_fv"])],
})
VP_TOWNS_NOTE.update({
 "roedovre": "Rødovre Kommune har kun ét byområde i Danmarks Statistiks opgørelse, så indbyggertallet gælder byområdet og opvarmningstallene hele kommunen. Om din adresse allerede har fjernvarme eller kommer med i udbygningen, afgør Rødovre Kommunale Fjernvarmeforsyning, som skriver til dig, når der er en tidsplan for dit område.",
 "ballerup": "Ballerup-byområdet er kommunens del af Hovedstadsområdet, mens Smørumnedre-byområdet (8.663 indbyggere i alt) går på tværs af flere kommuner, så kun en del bor i Ballerup Kommune. Opvarmningstallene gælder hele Ballerup Kommune. På Vestforbrændings kort kan du slå din adresse op.",
})
VP_XFAQ.update({
 "roedovre": [("Hvor mange huse i Rødovre har varmepumpe?", lambda: f"{tal(HEAT['roedovre']['VP'])} af {tal(hs('roedovre'))} beboede parcel- og rækkehuse ({hp('roedovre','VP',1)}) har varmepumpe ifølge Danmarks Statistik, 2026, mens {tal(HEAT['roedovre']['CN'])} ({hp('roedovre','CN',1)}) har naturgas.", ["dst_bol102"])],
 "ballerup": [("Hvor mange huse i Ballerup har varmepumpe?", lambda: f"{tal(HEAT['ballerup']['VP'])} af {tal(hs('ballerup'))} beboede parcel- og rækkehuse ({hp('ballerup','VP',1)}) har varmepumpe ifølge Danmarks Statistik, 2026, mens {tal(HEAT['ballerup']['CN'])} ({hp('ballerup','CN',1)}) har naturgas.", ["dst_bol102"])],
})
FV_SOURCES.update({
 "roedovre": [("<strong>Distributionsselskab:</strong> Rødovre Kommunale Fjernvarmeforsyning producerer ikke selv varme, men køber den hos transmissionsselskabet VEKS og leverer den videre i fem separate ledningsnet, som hver forsynes fra en vekslerstation.", ["rkf_om"]),
              ("<strong>VEKS' kilder:</strong> VEKS køber varme fra flere kilder, herunder Køge Kraftvarme, ARGO (affaldsforbrænding i Roskilde) og Avedøreværket. Ifølge RKF blev 94 % af fjernvarmen i 2024 produceret med vedvarende energikilder.", ["rkf_pris", "rkf_forside"]),
              ("<strong>Nonprofit:</strong> både VEKS og RKF arbejder efter hvile-i-sig-selv-princippet, så indtægter og omkostninger skal balancere, og eventuelle overskud går tilbage til forbrugerne.", ["rkf_pris"])],
 "ballerup": [("<strong>Brændselsmix 2025:</strong> Vestforbrændings deklaration for eget net viser 40,35 % bioaffald, 35,92 % fossilt affald, 14,65 % naturgas, 6,97 % elektricitet og 2,10 % gasolie. Andelen af vedvarende energi er 83,2 %.", ["vf_dekl"]),
              ("<strong>CO2 og rangering:</strong> udledningen er 11,78 kg CO2-ækvivalenter pr. GJ (42,4 kg pr. MWh), hvilket giver Energistyrelsens gule rangering – mindre udledning end et gasfyr, men mere end en luft-til-vand-varmepumpe.", ["vf_dekl"]),
              ("<strong>Varmeplan 2030:</strong> det første hus i Ballerup blev koblet på i februar 2025. Udbygningen kan frem mod 2030 koble 39.000 husstande i syv kommuner på og lægger 450 km fjernvarmerør.", ["vf_nyhed"])],
})
FV_SHARE.update({
 "roedovre": lambda: f"Fjernvarme findes i {hp('roedovre','FJ',1)} af de beboede parcel- og rækkehuse i Rødovre Kommune (landet: {hp('dk','FJ',1)}), og {hp('roedovre','CN',1)} fyrer med naturgas.",
 "ballerup": lambda: f"I Ballerup Kommune har {hp('ballerup','FJ',1)} af de beboede parcel- og rækkehuse fjernvarme mod {hp('dk','FJ',1)} på landsplan, og {hp('ballerup','CN',1)} bruger naturgas.",
})
FV_SOURCES_H.update({"roedovre": "Distributionsselskab og VEKS-varme: sådan leveres varmen i Rødovre", "ballerup": "Vestforbrændings brændselsmix og deklaration 2025"})
_reg_age_old27 = reg_age_note
def reg_age_note(c, kommune):
    s = STOCK[c]; B = s["B"]; t = s["tot"]
    if c == "roedovre":
        return (f"{tal(B['før 1960'])} af de beboede parcel- og rækkehuse i Rødovre Kommune ({pct(B['før 1960'], t)}) er bygget før 1960. Kommunen har SAVE-registreret huse i 31 bykvarterer, og bygninger med bevaringsværdi 1-3 (rækkehuse 1-4) er omfattet af bevaringshensyn i Kommuneplan 2022, så tjek husets SAVE-værdi og lokalplanen, før du bestiller solceller.", ["rod_bev"])
    if c == "ballerup":
        return (f"{tal(B['før 1960'])} af de beboede parcel- og rækkehuse i Ballerup Kommune ({pct(B['før 1960'], t)}) er bygget før 1960, mens {tal(B['1960-1979'])} ({pct(B['1960-1979'], t)}) er fra 1960–79. Står huset som fredet eller bevaringsværdigt, henviser kommunen til byggetilladelse via Bygogmiljø.dk, og i Gl. Skovlunde forbyder vejledningen til Lokalplan 104 solceller på bevaringsværdige bygninger.", ["bal_bev", "bal_skov"])
    return _reg_age_old27(c, kommune)

# ---------- tjek af sammenlignende udsagn: bygget fejler, hvis en ny by gør et udsagn forkert ----------
_PVs = lambda c: PV[c]["syd"]; _rt = lambda k: (lambda c: ROOF[c]["T"][k] / ROOF[c]["tot"]); _hf = lambda k: (lambda c: HEAT[c][k] / hs(c)); _sb = lambda k: (lambda c: STOCK[c]["B"][k] / STOCK[c]["tot"])
CLAIMS = [
 ("Esbjerg top 18 PV (dynamisk tekst; løsnet 17/11 efter Nakskov/Assens)", rank(_PVs, "esbjerg") <= 27),  # løsnet 27/11 efter Rødovre/Ballerup; løsnet 20/11 efter Rønne/Hobro, 23/11 efter Ebeltoft/Thisted
 ("Aalborg top 17 juni (dynamisk tekst; løsnet 17/11)", rank(lambda c: PV[c]["months"][5], "aalborg") <= 25),  # løsnet 23/11
 ("Odense top 4 tegl (dynamisk tekst; løsnet 13/11 efter Gladsaxe/Lyngby, 27/11 efter Rødovre)", rank(_rt("10"), "odense") <= 9), ("Aalborg top 5 fibercement (dynamisk tekst)", rank(_rt("06"), "aalborg") <= 7),  # løsnet 23/11 efter Thisted
 ("Vejle ikke nr. 1 nyere huse", rank(_sb("2000+"), "vejle") > 1),
 ("Esbjerg top 6 1960-79 (dynamisk tekst; løsnet 26/11 efter Hørsholm, 27/11 efter Ballerup)", rank(_sb("1960-1979"), "esbjerg") <= 7),
 ("Aarhus flest huse", top(lambda c: STOCK[c]["tot"]) == "aarhus"), ("Aalborg nr. 2 huse", rank(lambda c: STOCK[c]["tot"], "aalborg") == 2),
 ("Horsens top 12 ejerandel (dynamisk tekst; løsnet 13/11, 25/11 efter Gentofte, 26/11 efter Hørsholm)", rank(_EJ, "horsens") <= 12),
 ("Odense top 3 FJ (dynamisk tekst; løsnet 25/11 efter Frederiksberg)", rank(_hf("FJ"), "odense") <= 3), ("Aarhus top 5 FJ (dynamisk tekst; løsnet 25/11 efter Frederiksberg)", rank(_hf("FJ"), "aarhus") <= 5),

 ("Viborg top 9 olie, Randers top 14 (dynamisk tekst; løsnet 17/11)", rank(_hf("CO"), "viborg") <= 14 and rank(_hf("CO"), "randers") <= 21),  # løsnet 19/11 efter Middelfart/Tønder, 23/11 efter Ebeltoft/Thisted
 ("Næstved gas tæt på fjernvarme (overskrift)", abs(HEAT["naestved"]["CN"] - HEAT["naestved"]["FJ"]) / HEAT["naestved"]["FJ"] < 0.05),
 ("Sønderborg tre ud af fem FJ (overskrift)", 0.58 <= HEAT["soenderborg"]["FJ"] / hs("soenderborg") <= 0.62),
 ("Roskilde mere end hvert fjerde gas (overskrift)", HEAT["roskilde"]["CN"] / hs("roskilde") > 0.25),
 ("Holbæk top 10 gasfyr (overskrift 'Mange gasfyr' og dynamisk tekst; løsnet 26/11 efter Hørsholm/Hvidovre, 27/11 efter Ballerup/Rødovre) og laveste FJ (overskrift)", rank(_hf("CN"), "holbaek") <= 10 and top(_hf("FJ"), rev=True) == "holbaek"),
 ("Køge halvdelen gas, top 5 gasfyr (overskrift, dynamisk tekst)", 0.47 <= HEAT["koege"]["CN"] / hs("koege") <= 0.53 and rank(_hf("CN"), "koege") <= 7),  # løsnet 26/11 efter Hørsholm, 27/11 efter Ballerup/Rødovre
 ("Svendborg hvert fjerde FJ (overskrift)", 0.23 <= HEAT["svendborg"]["FJ"] / hs("svendborg") <= 0.27),
 ("Svendborg top 6 PV (dynamisk tekst; løsnet 17/11)", rank(_PVs, "svendborg") <= 7),
 ("Faaborg hvert tredje FJ (tekst)", 0.32 <= HEAT["faaborg"]["FJ"] / hs("faaborg") <= 0.36),
 ("Aabenraa halvdelen FJ (tekst)", 0.48 <= HEAT["aabenraa"]["FJ"] / hs("aabenraa") <= 0.54),
 ("Aabenraa hvert ellevte elvarme (overskrift)", 0.085 <= HEAT["aabenraa"]["ELV"] / hs("aabenraa") <= 0.096),
 ("Aabenraa FJ tæt på landsgennemsnit (tekst)", abs(HEAT["aabenraa"]["FJ"] / hs("aabenraa") - HEAT["dk"]["FJ"] / hs("dk")) < 0.04),
 ("Herning næsten fire ud af fem FJ (overskrift)", 0.76 <= HEAT["herning"]["FJ"] / hs("herning") < 0.80),
 ("Greve over halvdelen gas (overskrift)", HEAT["greve"]["CN"] / hs("greve") > 0.50),
 ("Greve hvert fjerde FJ (tekst)", 0.22 <= HEAT["greve"]["FJ"] / hs("greve") <= 0.27),
 ("Hjørring næsten to ud af tre FJ (overskrift)", 0.60 <= HEAT["hjoerring"]["FJ"] / hs("hjoerring") < 0.667),
 ("Hjørring næsten halvdelen fibercement (overskrift)", 0.45 <= ROOF["hjoerring"]["T"]["06"] / ROOF["hjoerring"]["tot"] < 0.50),
 ("Holte/Rudersdal seks ud af ti gas (overskrift)", 0.57 <= HEAT["holte"]["CN"] / hs("holte") <= 0.63),
 ("Holte/Rudersdal 15 pct. FJ (tekst)", round(100 * HEAT["holte"]["FJ"] / hs("holte")) == 15),
 ("Nykøbing F. top 3 PV (overskrift 'blandt de solrigeste', dynamisk tekst; løsnet 17/11)", rank(_PVs, "nykoebing-falster") <= 4),
 ("Guldborgsund ingen gas, ELV og olie top 3 (overskrift, dynamisk tekst)", HEAT["nykoebing-falster"]["CN"] == 0 and rank(_hf("ELV"), "nykoebing-falster") <= 8 and rank(_hf("CO"), "nykoebing-falster") <= 5),  # løsnet 19/11 efter Tønder, 23/11 efter Ebeltoft
 ("Guldborgsund mere end hvert tiende elvarme, næsten lige så mange olie (tekst)", HEAT["nykoebing-falster"]["ELV"] / hs("nykoebing-falster") > 0.10 and 0.85 <= HEAT["nykoebing-falster"]["CO"] / HEAT["nykoebing-falster"]["ELV"] < 1),
 ("Guldborgsund 57 pct. FJ (tekst)", round(100 * HEAT["nykoebing-falster"]["FJ"] / hs("nykoebing-falster")) == 57),
 ("Guldborgsund fibercement og tegl de to største tagtyper (overskrift)", sorted(ROOF["nykoebing-falster"]["T"], key=lambda k: -ROOF["nykoebing-falster"]["T"][k])[:2] == ["06", "10"]),
 ("Haderslev fire ud af ti FJ, hvert fjerde gas (overskrift)", 0.38 <= HEAT["haderslev"]["FJ"] / hs("haderslev") <= 0.42 and 0.23 <= HEAT["haderslev"]["CN"] / hs("haderslev") <= 0.27),
 ("Haderslev tre tagtyper 25-30 pct. (overskrift)", all(0.25 <= ROOF["haderslev"]["T"][k] / ROOF["haderslev"]["tot"] <= 0.30 for k in ("06", "10", "08"))),
 ("Frederikshavn næsten to ud af tre FJ (overskrift/intro)", 0.62 <= HEAT["frederikshavn"]["FJ"] / hs("frederikshavn") <= 0.665),
 ("Frederikshavn over fire ud af ti fibercement (overskrift)", 0.40 < ROOF["frederikshavn"]["T"]["06"] / ROOF["frederikshavn"]["tot"] < 0.50),
 ("Frederikshavn maj/juni/juli næsten lige (overskrift)", max(PV["frederikshavn"]["months"][4:7]) / min(PV["frederikshavn"]["months"][4:7]) < 1.08),
 ("Hedensted hvert femte VP og hvert femte gas (overskrift/intro)", all(0.18 <= HEAT["hedensted"][k] / hs("hedensted") <= 0.22 for k in ("VP", "CN"))),
 ("Hedensted cementsten mest udbredte tag (overskrift)", sorted(ROOF["hedensted"]["T"], key=lambda k: -ROOF["hedensted"]["T"][k])[0] == "08"),
 ("Hedensted 36 pct. FJ (intro)", round(100 * HEAT["hedensted"]["FJ"] / hs("hedensted")) == 36),
 ("Hedensted øst og vest næsten ens (FAQ)", abs(PV["hedensted"]["oest"] - PV["hedensted"]["vest"]) / PV["hedensted"]["syd"] < 0.03),
 ("Ringkøbing oliefyr over landsgennemsnit (overskrift)", HEAT["ringkoebing"]["CO"] / hs("ringkoebing") > HEAT["dk"]["CO"] / hs("dk")),
 ("Ringkøbing tre ud af fem FJ (overskrift/intro)", 0.58 <= HEAT["ringkoebing"]["FJ"] / hs("ringkoebing") <= 0.62),
 ("Ringkøbing fibercement, cementsten og tegl de tre største tagtyper (overskrift)", sorted(ROOF["ringkoebing"]["T"], key=lambda k: -ROOF["ringkoebing"]["T"][k])[:3] == ["06", "08", "10"]),
 ("Helsingør flere naturgas end FJ (overskrift/intro)", HEAT["helsingoer"]["CN"] > HEAT["helsingoer"]["FJ"]),
 ("Helsingør næsten fire ud af ti naturgas (intro)", 0.35 <= HEAT["helsingoer"]["CN"] / hs("helsingoer") < 0.40),
 ("Helsingør 36 pct. FJ (FV-intro)", round(100 * HEAT["helsingoer"]["FJ"] / hs("helsingoer")) == 36),
 ("Helsingør mange flade tage: over landsgennemsnit (overskrift)", _FLs("helsingoer") > _FLs("dk")),
 ("Helsingør mange rækkehuse: over landsgennemsnit (overskrift)", _RKs("helsingoer") > STOCK["dk"]["raekke"] / STOCK["dk"]["tot"]),
 ("Ringkøbing ældre huse: før 1960 over landsgennemsnit (overskrift)", STOCK["ringkoebing"]["B"]["før 1960"] / STOCK["ringkoebing"]["tot"] > STOCK["dk"]["B"]["før 1960"] / STOCK["dk"]["tot"]),
 ("Stenløse/Egedal flere naturgas end FJ (overskrift/intro)", HEAT["stenloese"]["CN"] > HEAT["stenloese"]["FJ"]),
 ("Stenløse/Egedal næsten fire ud af ti naturgas (intro)", 0.37 <= HEAT["stenloese"]["CN"] / hs("stenloese") < 0.42),
 ("Stenløse/Egedal 35 pct. FJ (FV-intro)", round(100 * HEAT["stenloese"]["FJ"] / hs("stenloese")) == 35),
 ("Stenløse/Egedal over halvdelen bygget 1960-79 (overskrift)", STOCK["stenloese"]["B"]["1960-1979"] / STOCK["stenloese"]["tot"] > 0.50),
 ("Stenløse fibercement og cementsten de to største tagtyper (overskrift)", sorted(ROOF["stenloese"]["T"], key=lambda k: -ROOF["stenloese"]["T"][k])[:2] == ["06", "08"]),
 ("Frederikssund næsten fire ud af ti gas (overskrift/intro)", 0.35 <= HEAT["frederikssund"]["CN"] / hs("frederikssund") < 0.40),
 ("Frederikssund 24 pct. FJ (FV-intro)", round(100 * HEAT["frederikssund"]["FJ"] / hs("frederikssund")) == 24),
 ("Frederikssund flere naturgas end FJ (intro)", HEAT["frederikssund"]["CN"] > HEAT["frederikssund"]["FJ"]),
 ("Frederikssund fibercement, cementsten og tegl top 3 (overskrift)", sorted(ROOF["frederikssund"]["T"], key=lambda k: -ROOF["frederikssund"]["T"][k])[:3] == ["06", "08", "10"]),
 ("Skanderborg to ud af tre FJ (overskrift/intro)", 0.64 <= HEAT["skanderborg"]["FJ"] / hs("skanderborg") <= 0.70),
 ("Skanderborg fibercement/tegl/cementsten næsten ligeligt (overskrift)", sorted(ROOF["skanderborg"]["T"], key=lambda k: -ROOF["skanderborg"]["T"][k])[:3] == ["06", "10", "08"]),
 ("Vordingborg højeste elvarme, olie top 3 (overskrift/intro; ændret 17/11 efter Nakskov)", rank(_hf("ELV"), "vordingborg") <= 2 and rank(_hf("CO"), "vordingborg") <= 3),
 ("Vordingborg hvert tredje FJ (intro)", 0.30 <= HEAT["vordingborg"]["FJ"] / hs("vordingborg") <= 0.36),
 ("Vordingborg fire ud af ti fibercement (overskrift)", 0.38 <= ROOF["vordingborg"]["T"]["06"] / ROOF["vordingborg"]["tot"] < 0.43),
 ("Vordingborg næsten hvert andet hus før 1960 (tekst)", 0.45 <= STOCK["vordingborg"]["B"]["før 1960"] / STOCK["vordingborg"]["tot"] < 0.50),
 ("København 94 pct. FJ (intro/FV-intro)", round(100 * HEAT["koebenhavn"]["FJ"] / hs("koebenhavn")) == 94),
 ("København over ni ud af ti FJ (overskrift)", HEAT["koebenhavn"]["FJ"] / hs("koebenhavn") > 0.90),
 ("København tegl største tagtype (tekst)", max(ROOF["koebenhavn"]["T"], key=lambda k: ROOF["koebenhavn"]["T"][k]) == "10"),
 ("Vejen fibercement, cementsten, tegl top 3 (overskrift)", sorted(ROOF["vejen"]["T"], key=lambda k: -ROOF["vejen"]["T"][k])[:3] == ["06", "08", "10"]),
 ("Vejen 45 pct. FJ (intro/FV-intro)", round(100 * HEAT["vejen"]["FJ"] / hs("vejen")) == 45),
 ("Vejen næsten hvert femte naturgas (overskrift/intro)", 0.17 <= HEAT["vejen"]["CN"] / hs("vejen") < 0.20),
 ("Varde 56 pct. FJ (FV-intro)", round(100 * HEAT["varde"]["FJ"] / hs("varde")) == 56),
 ("Varde 8 pct. olie (intro/FAQ)", round(100 * HEAT["varde"]["CO"] / hs("varde")) == 8),
 ("Varde mange oliefyr top 6 (overskrift; løsnet 17/11)", rank(_hf("CO"), "varde") <= 11),  # løsnet 19/11 efter Tønder, 23/11 efter Ebeltoft/Thisted
 ("Faxe hvert femte FJ (intro)", 0.18 <= HEAT["faxe"]["FJ"] / hs("faxe") < 0.22),
 ("Faxe næsten hvert tredje naturgas (overskrift/intro)", 0.29 <= HEAT["faxe"]["CN"] / hs("faxe") < 0.334),
 ("Faxe få tegltage (overskrift)", rank(_rt("10"), "faxe", ) >= len(NAMES) - 2),
 ("Faxe solrig top 12 (overskrift; løsnet 25/11 efter Frederiksberg)", rank(_PVs, "faxe") <= 12),
 ("Faxe øst-vest ca. en femtedel mindre (tekst)", 0.17 <= 1 - (PV["faxe"]["oest"] + PV["faxe"]["vest"]) / 2 / PV["faxe"]["syd"] <= 0.25),

 ("Kalundborg top 3 PV (intro/overskrift)", rank(_PVs, "kalundborg") <= 3),
 ("Kalundborg mere end hvert tiende ELV (intro)", 0.10 < HEAT["kalundborg"]["ELV"] / hs("kalundborg") < 0.125),
 ("Kalundborg mange ELV top 3 (overskrift)", rank(_hf("ELV"), "kalundborg") <= 6),  # løsnet 19/11 efter Tønder
 ("Kalundborg mange fibercement top 4 (overskrift)", rank(_rt("06"), "kalundborg") <= 5),  # løsnet 23/11 efter Thisted (dynamisk tekst)
 ("Kalundborg 47 pct. FJ (FV-intro)", round(100 * HEAT["kalundborg"]["FJ"] / hs("kalundborg")) == 47),
 ("Skive hvert femte naturgas (overskrift/intro)", 0.19 <= HEAT["skive"]["CN"] / hs("skive") < 0.21),
 ("Skive 8 pct. olie (intro)", round(100 * HEAT["skive"]["CO"] / hs("skive")) == 8),
 ("Skive hvert andet fibercement (overskrift)", 0.48 <= ROOF["skive"]["T"]["06"] / ROOF["skive"]["tot"] < 0.53),
 ("Skive lav PV, nordligere (tekst)", rank(_PVs, "skive") >= len(NAMES) - 4),
 ("Skive 45 pct. FJ (FV-intro)", round(100 * HEAT["skive"]["FJ"] / hs("skive")) == 45),
 ("Gladsaxe næsten halvdelen gas (overskrift/intro)", 0.46 <= HEAT["gladsaxe"]["CN"] / hs("gladsaxe") < 0.50),
 ("Gladsaxe halvdelen række/dobbelt (sol-intro)", 0.47 <= STOCK["gladsaxe"]["raekke"] / STOCK["gladsaxe"]["tot"] < 0.53),
 ("Gladsaxe 37 pct. FJ (FV-intro)", round(100 * HEAT["gladsaxe"]["FJ"] / hs("gladsaxe")) == 37),
 ("Lyngby højeste gas (overskrift/intro)", top(_hf("CN")) == "kongens-lyngby"),
 ("Lyngby to ud af tre gas (intro)", 0.64 <= HEAT["kongens-lyngby"]["CN"] / hs("kongens-lyngby") < 0.69),
 ("Lyngby over halvdelen tegl (overskrift; rettet 25/11 efter Frederiksberg)", ROOF["kongens-lyngby"]["T"]["10"] / ROOF["kongens-lyngby"]["tot"] > 0.50),
 ("Lyngby 18 pct. FJ (FV-intro)", round(100 * HEAT["kongens-lyngby"]["FJ"] / hs("kongens-lyngby")) == 18),
 ("Lyngby mere end halvdelen tegl (sol-intro)", ROOF["kongens-lyngby"]["T"]["10"] / ROOF["kongens-lyngby"]["tot"] > 0.5),
 ("Holstebro fire ud af fem FJ (overskrift/intro)", 0.78 <= HEAT["holstebro"]["FJ"] / hs("holstebro") < 0.82),
 ("Holstebro 1 pct. gas (intro)", round(100 * HEAT["holstebro"]["CN"] / hs("holstebro")) == 1),
 ("Holstebro godt 1.000 oliefyr (intro)", 1000 <= HEAT["holstebro"]["CO"] < 1100),
 ("Holstebro fibercement+cementsten dominerer (overskrift)", (ROOF["holstebro"]["T"]["06"] + ROOF["holstebro"]["T"]["08"]) / ROOF["holstebro"]["tot"] > 0.55),
 ("Fredensborg flest rækkehuse (overskrift)", top(_RK) == "fredensborg"),
 ("Fredensborg over halvdelen række (sol-intro)", STOCK["fredensborg"]["raekke"] / STOCK["fredensborg"]["tot"] > 0.5),
 ("Fredensborg knap fire ud af ti gas (intro)", 0.36 <= HEAT["fredensborg"]["CN"] / hs("fredensborg") < 0.40),
 ("Fredensborg gas og FJ næsten lige store, lidt flere gas (overskrift/FV-intro)", 0 < (HEAT["fredensborg"]["CN"] - HEAT["fredensborg"]["FJ"]) / hs("fredensborg") < 0.05),
 ("Fredensborg 36 pct. FJ (FV-intro)", round(100 * HEAT["fredensborg"]["FJ"] / hs("fredensborg")) == 36),
 ("Nakskov næsthøjeste PV efter Rønne (overskrift/intro; ændret 20/11)", rank(_PVs, "nakskov") == 2 and top(_PVs) == "roenne"),
 ("Nakskov højeste andel oliefyr (overskrift/intro)", top(_hf("CO")) == "nakskov"),
 ("Nakskov 0 naturgas (tekst)", HEAT["nakskov"]["CN"] == 0),
 ("Nakskov lidt over halvdelen FJ (intro)", 0.50 < HEAT["nakskov"]["FJ"] / hs("nakskov") < 0.56),
 ("Nakskov fibercement to ud af fem (overskrift)", 0.37 <= ROOF["nakskov"]["T"]["06"] / ROOF["nakskov"]["tot"] <= 0.42),
 ("Nakskov mange gamle huse, over halvdelen før 1960 (overskrift)", STOCK["nakskov"]["B"]["før 1960"] / STOCK["nakskov"]["tot"] > 0.50 and rank(_sb("før 1960"), "nakskov") <= 8),
 ("Assens lidt over halvdelen FJ (overskrift/intro)", 0.50 < HEAT["assens"]["FJ"] / hs("assens") < 0.56),
 ("Assens fibercement+cementsten ca. halvdelen (overskrift)", 0.55 <= (ROOF["assens"]["T"]["06"] + ROOF["assens"]["T"]["08"]) / ROOF["assens"]["tot"] <= 0.65),
 ("Hinnerup to ud af tre FJ (overskrift/intro)", 0.63 <= HEAT["hinnerup"]["FJ"] / hs("hinnerup") <= 0.70),
 ("Hinnerup godt 1.000 naturgas (intro/local_take)", 1000 < HEAT["hinnerup"]["CN"] < 1200),
 ("Hinnerup fibercement og cementsten dominerer (overskrift)", ROOF["hinnerup"]["T"]["06"] + ROOF["hinnerup"]["T"]["08"] > ROOF["hinnerup"]["tot"] / 2),
 ("Hinnerup by: Hinnerup størst (overskrift 'tre jævnstore byer')", TOWNS["hinnerup"][0][0] == "Hinnerup"),
 ("Helsinge højeste andel VP (overskrift/intro/FV)", top(_hf("VP")) == "helsinge"),
 ("Helsinge højeste andel elvarme (overskrift/intro)", top(_hf("ELV")) == "helsinge"),
 ("Helsinge hvert tredje hus FJ (intro)", 0.30 <= HEAT["helsinge"]["FJ"] / hs("helsinge") <= 0.36),
 ("Helsinge mange stråtage, top 3 (overskrift)", rank(_rt("14"), "helsinge") <= 3),
 ("Helsinge 60'erne/70'erne, top 10 (overskrift)", rank(_sb("1960-1979"), "helsinge") <= 10),
 ("Middelfart lidt over halvdelen FJ (VP-intro)", 0.50 < HEAT["middelfart"]["FJ"] / hs("middelfart") < 0.56),
 ("Middelfart knap hver femte gas (VP-intro)", 0.16 <= HEAT["middelfart"]["CN"] / hs("middelfart") < 0.20),
 ("Middelfart mange cementsten, top 5 (overskrift)", rank(_rt("08"), "middelfart") <= 5),
 ("Toender elvarme top 6 (VP-intro 'en af de højeste')", rank(_hf("ELV"), "toender") <= 6),
 ("Toender oliefyr top 6 (VP-intro/overskrift)", rank(_hf("CO"), "toender") <= 6),
 ("Toender meget få nye huse, bund 5 (dynamisk tekst; løsnet 25/11 efter Frederiksberg)", rank(_sb("2000+"), "toender") >= len(NAMES) - 4),
 ("Toender stråtag top 8 (overskrift)", rank(_rt("14"), "toender") <= 8),
 ("Roenne højeste PV (overskrift 'Mest sol på sitet')", top(_PVs) == "roenne"),
 ("Roenne næsten hvert ottende elvarme (VP-intro)", 0.105 <= HEAT["roenne"]["ELV"] / hs("roenne") < 0.125),
 ("Roenne næsten ingen naturgas (VP-intro/overskrift)", HEAT["roenne"]["CN"] < 10),
 ("Roenne mange tegltage, top 7 (dynamisk tekst; neutral overskrift; løsnet 26/11 efter Hørsholm)", rank(_rt("10"), "roenne") <= 7),
 ("Hobro lidt over halvdelen FJ (VP-intro)", 0.50 < HEAT["hobro"]["FJ"] / hs("hobro") < 0.56),
 ("Hobro næsten hvert andet tag fibercement (overskrift)", 0.42 <= ROOF["hobro"]["T"]["06"] / ROOF["hobro"]["tot"] < 0.50),
 ("Ebeltoft hvert niende elvarme (VP-intro)", 0.105 <= HEAT["ebeltoft"]["ELV"] / hs("ebeltoft") < 0.118),
 ("Ebeltoft næsten hvert femte VP (VP-intro)", 0.18 <= HEAT["ebeltoft"]["VP"] / hs("ebeltoft") < 0.20),
 ("Ebeltoft ingen naturgas (VP-intro/overskrift/FV-andel)", HEAT["ebeltoft"]["CN"] == 0),
 ("Ebeltoft mange nyere huse, top 15 2000+ (overskrift)", rank(_sb("2000+"), "ebeltoft") <= 15),
 ("Thisted seks ud af ti FJ (VP-intro/overskrift)", 0.57 <= HEAT["thisted"]["FJ"] / hs("thisted") < 0.63),
 ("Thisted 1.477 oliefyr (VP-intro)", HEAT["thisted"]["CO"] == 1477),
 ("Thisted mange oliefyr, top 10 (overskrift)", rank(_hf("CO"), "thisted") <= 10),
 ("Thisted højeste andel fibercement (overskrift 'Flest fibercementtage')", top(_rt("06")) == "thisted"),
 ("Thisted over halvdelen fibercement (sol-intro)", ROOF["thisted"]["T"]["06"] / ROOF["thisted"]["tot"] > 0.5),
 ("Thisted ældre huse, top 15 før 1960 (overskrift)", rank(_sb("før 1960"), "thisted") <= 15),
# 27/11 2026: Rødovre og Ballerup
 ("Roedovre over seks ud af ti huse før 1960 (sol-intro)", STOCK["roedovre"]["B"]["før 1960"] / STOCK["roedovre"]["tot"] > 0.6),
 ("Roedovre over halvdelen naturgas, 55 % (VP-intro, overskrift)", 0.54 <= HEAT["roedovre"]["CN"] / hs("roedovre") < 0.56),
 ("Roedovre 29 % fjernvarme (VP-intro)", 0.285 <= HEAT["roedovre"]["FJ"] / hs("roedovre") < 0.30),
 ("Roedovre mere end fire ud af ti tegltag (overskrift)", 0.40 <= ROOF["roedovre"]["T"]["10"] / ROOF["roedovre"]["tot"] < 0.50),
 ("Ballerup over halvdelen opført 1960-79 (sol-intro, overskrift)", STOCK["ballerup"]["B"]["1960-1979"] / STOCK["ballerup"]["tot"] > 0.5),
 ("Ballerup næsten hvert tredje tag fibercement (overskrift)", 0.29 <= ROOF["ballerup"]["T"]["06"] / ROOF["ballerup"]["tot"] < 0.333),
 ("Ballerup næsten to tredjedele naturgas, 63 % (overskrift, VP-intro)", 0.625 <= HEAT["ballerup"]["CN"] / hs("ballerup") < 0.635),
 ("Ballerup 21 % fjernvarme (VP-intro)", 0.205 <= HEAT["ballerup"]["FJ"] / hs("ballerup") < 0.215),
]
_bad = [n for n, ok in CLAIMS if not ok]
assert not _bad, f"Sammenlignende udsagn passer ikke længere: {_bad}"

# keyword-backlog 23/11 2026: 'jordvarme holbæk' (GSC 9 visninger, pos. 73,3) -> FAQ om jordvarme på /varmepumpe/holbaek/
VP_XFAQ["holbaek"] = [("Skal jeg søge om jordvarme i Holbæk Kommune?", lambda: "Ja, i de fleste tilfælde. Et vandret jordvarmeanlæg kan kun anmeldes, hvis det er ikke-industrielt, ligger uden for områder med særlige drikkevandsinteresser og indvindingsoplande og kun bruger de tilladte frostsikringsmidler – og anmeldelsen skal ske mindst 4 uger før. Men meget store dele af Holbæk Kommune ligger i netop de områder, så de fleste skal søge om tilladelse via Byg og Miljø. Kommunen har et kort, der viser, hvor du kan nøjes med at anmelde. Lodrette anlæg med dybe boringer kræver desuden boretilladelse og VVM-screening.", ["hol_jord"]),
                      ("Hvad koster jordvarme i Holbæk?", lambda: "Vi har ikke fundet kilder med en særlig Holbæk-pris. Energisparer.dk angiver ca. 120.000-180.000 kr. inkl. montering for jordvarme og ca. 93.000-153.000 kr. efter Varmepumpepuljens 27.000 kr. – som kun gælder uden for områder med fjernvarme eller planlagt fjernvarme, og altså ikke i etape 1 i Holbæk by. Når anlægget er installeret, skal det færdigmeldes med ledningsplan og tæthedsprøvning og efterses af en sagkyndig efter første driftsår.", ["es_vp", "se_vpp", "hol_jord"])] + VP_XFAQ["holbaek"]
