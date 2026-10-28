"""Genererer src/data_local_gen.py ud fra rådata hentet 24/10 2026 (PVGIS 5.3 og Danmarks Statistik)."""
import json, itertools, pprint
CODE={"461":"odense","561":"esbjerg","621":"kolding","630":"vejle","615":"horsens","730":"randers","851":"aalborg","751":"aarhus","791":"viborg","370":"naestved","740":"silkeborg","316":"holbaek","330":"slagelse","000":"dk"}
pv=json.load(open("pvgis.json"))
PV={c:{"syd":round(v["syd35"]["E_y"]),"oest":round(v["oest_vest"]["E_y"]),"vest":round(v["vest"]["E_y"]),
       "opt":round(v["opt"]["E_y"]),"opt_angle":v["opt"]["angle"],"months":[round(m) for m in v["syd35"]["months"]],
       "url_syd":v["syd35"]["url"],"url_oest":v["oest_vest"]["url"],"url_vest":v["vest"]["url"],"db":v["syd35"]["db"]} for c,v in pv.items()}
# BOL102: opvarmning
d=json.load(open("bol102_2026.json"))["dataset"]; dm=d["dimension"]; ids=dm["id"]
cats=[list(dm[i]["category"]["index"]) for i in ids]
res={combo:(d["value"][n] or 0) for n,combo in enumerate(itertools.product(*cats))}
HEAT={}
for a in cats[0]:
    H={}
    for combo,val in res.items():
        if combo[0]==a: H[combo[3]]=H.get(combo[3],0)+val
    HEAT[CODE[a]]=H
# BOL101: bestand
b=json.load(open("bol101_summary.json"))
STOCK={CODE[a]:{"tot":v["tot"],"parcel":v["P"]["125"],"raekke":v["P"]["130"],"ejer":v["ej"],"B":v["B"]} for a,v in b.items()}
# BYGB50: tag
r=json.load(open("bygb50_2026.json")); tl=r["labels"]
ROOF={CODE[a]:{"tot":v["tot"],"T":v["T"]} for a,v in r["data"].items()}
# BY3: byer
t=json.load(open("by3_2026.json"))
TOWNS={c:[(n.split(" ",1)[1].replace(" (del af flere kommuner)",""),p) for n,p in lst if p] for c,lst in t.items()}
with open("../../src/data_local_gen.py","w",encoding="utf-8") as f:
    f.write('# -*- coding: utf-8 -*-\n"""GENERERET af research/v4/make_local.py (data hentet 24/10 2026). Redigér ikke i hånden.\n'
            'PV: PVGIS 5.3 (SARAH3), kWh pr. kWp pr. år, 35° hældning, 14 % systemtab. HEAT: DST BOL102 2026, beboede parcel/stuehuse + række/kæde/dobbelthuse.\n'
            'STOCK: DST BOL101 2026 (samme boligtyper). ROOF: DST BYGB50 2026, antal parcel- og rækkehusbygninger efter tagmateriale. TOWNS: DST BY3 folketal 1/1 2026."""\n')
    for name,obj in (("PV",PV),("HEAT",HEAT),("STOCK",STOCK),("ROOF",ROOF),("ROOF_LABELS",tl),("TOWNS",TOWNS)):
        f.write(f"{name} = "+pprint.pformat(obj,width=200,sort_dicts=False)+"\n")
print("ok", {c:PV[c]["syd"] for c in PV})
