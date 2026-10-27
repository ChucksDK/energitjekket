"""Henter rådata for nye byer (daglig by-rutine) og fletter ind i research/v4/*.json. Brug: python3 fetch_new.py 751:aarhus:56.1572:10.2107 791:viborg:56.4532:9.4020"""
import json,urllib.request,itertools,sys,time,os
V4=os.path.join(os.path.dirname(__file__),"..","v4")
def q(table,vars_):
    body=json.dumps({"table":table,"format":"JSONSTAT","lang":"da","variables":vars_}).encode()
    r=urllib.request.Request("https://api.statbank.dk/v1/data",data=body,headers={"Content-Type":"application/json"})
    return json.load(urllib.request.urlopen(r,timeout=60))
def info(t): return json.load(urllib.request.urlopen(f"https://api.statbank.dk/v1/tableinfo/{t}?lang=da&format=JSON",timeout=60))
args=[a.split(":") for a in sys.argv[1:]]
K=[a[0] for a in args]; SL={a[0]:a[1] for a in args}
# BOL102 (merge into dataset: rebuild full file with all codes)
old=json.load(open(f"{V4}/bol102_2026.json"))["dataset"]["dimension"]["AMT"]["category"]["index"]
allk=list(old)+[k for k in K if k not in old]
d=q("BOL102",[{"code":"AMT","values":allk},{"code":"BEBO","values":["1000"]},{"code":"ANVENDELSE","values":["125","130"]},{"code":"OPVARMNING","values":["*"]},{"code":"Tid","values":["2026"]}])
json.dump(d,open(f"{V4}/bol102_2026.json","w"),ensure_ascii=False); print("BOL102 ok")
# BOL101
d=q("BOL101",[{"code":"OMRÅDE","values":K},{"code":"BEBO","values":["1000"]},{"code":"ANVENDELSE","values":["125","130"]},{"code":"UDLFORH","values":["*"]},{"code":"OPFØRELSESÅR","values":["*"]},{"code":"Tid","values":["2026"]}])
ds=d["dataset"]; dm=ds["dimension"]; ids=dm["id"]; v=ds["value"]
cats=[list(dm[i]["category"]["index"]) for i in ids]
res={combo:(v[n] or 0) for n,combo in enumerate(itertools.product(*cats))}
lab=dm["OMRÅDE"]["category"]["label"]
def bucket(y):
    if not y[0].isdigit(): return 'før 1960' if y[0]=='-' else 'uoplyst'
    y=int(y[:4]); return 'før 1960' if y<1960 else ('1960-1979' if y<1980 else ('1980-1999' if y<2000 else '2000+'))
summ=json.load(open(f"{V4}/bol101_summary.json"))
for a in cats[0]:
    tot=ej=0; B={}; P={}
    for combo,val in res.items():
        if combo[0]!=a: continue
        tot+=val; P[combo[2]]=P.get(combo[2],0)+val
        if combo[3]=='EJ': ej+=val
        b=bucket(combo[4]); B[b]=B.get(b,0)+val
    B.setdefault("uoplyst",0)
    summ[a]={"name":lab[a],"tot":tot,"ej":ej,"B":B,"P":P}; print(lab[a],tot,ej,B,P)
json.dump(summ,open(f"{V4}/bol101_summary.json","w"),ensure_ascii=False,indent=1)
# BYGB50
d=q("BYGB50",[{"code":"OMRÅDE","values":K},{"code":"MÆNGDE4","values":["45"]},{"code":"TAGMAT","values":["*"]},{"code":"ANVEND","values":["120","130"]},{"code":"OPFØRELSESÅR","values":["*"]},{"code":"Tid","values":["2026"]}])
ds=d["dataset"]; dm=ds["dimension"]; ids=dm["id"]; v=ds["value"]
cats=[list(dm[i]["category"]["index"]) for i in ids]
res={combo:(v[n] or 0) for n,combo in enumerate(itertools.product(*cats))}
lab=dm["OMRÅDE"]["category"]["label"]
r=json.load(open(f"{V4}/bygb50_2026.json"))
for a in cats[0]:
    T={}
    for combo,val in res.items():
        if combo[0]==a: T[combo[2]]=T.get(combo[2],0)+val
    r["data"][a]={"name":lab[a],"tot":sum(T.values()),"T":T}; print(lab[a],sum(T.values()),T)
json.dump(r,open(f"{V4}/bygb50_2026.json","w"),ensure_ascii=False,indent=1)
# BY3
bi=info("BY3"); byer=[x for v_ in bi["variables"] if v_["id"]=="BYER" for x in v_["values"]]
ids_=[x["id"] for x in byer if x["id"][:3] in K and not x["id"].endswith(("99999","99997"))]
d=q("BY3",[{"code":"BYER","values":ids_},{"code":"FOLKARTAET","values":["FOLKETAL"]},{"code":"Tid","values":["2026"]}])
ds=d["dataset"]; lab=ds["dimension"]["BYER"]["category"]["label"]; idx=ds["dimension"]["BYER"]["category"]["index"]; vals=ds["value"]
t=json.load(open(f"{V4}/by3_2026.json"))
new={}
for i,k in enumerate(idx): new.setdefault(SL[k[:3]],[]).append((lab[k],vals[i]))
for c in new: new[c].sort(key=lambda x:-(x[1] or 0)); t[c]=new[c]; print(c,new[c][:12])
json.dump(t,open(f"{V4}/by3_2026.json","w"),ensure_ascii=False,indent=1)
# PVGIS
pv=json.load(open(f"{V4}/pvgis.json"))
for a in args:
    c,la,lo=a[1],float(a[2]),float(a[3]); res={}
    for name,extra in (("syd35","angle=35&aspect=0"),("oest_vest","angle=35&aspect=-90"),("vest","angle=35&aspect=90"),("opt","optimalangles=1")):
        u=f"https://re.jrc.ec.europa.eu/api/v5_3/PVcalc?lat={la}&lon={lo}&peakpower=1&loss=14&{extra}&outputformat=json"
        dd=json.load(urllib.request.urlopen(u,timeout=60))
        res[name]={"url":u,"E_y":dd["outputs"]["totals"]["fixed"]["E_y"],"H_y":dd["outputs"]["totals"]["fixed"]["H(i)_y"],
                   "months":[m["E_m"] for m in dd["outputs"]["monthly"]["fixed"]],"angle":dd["inputs"]["mounting_system"]["fixed"]["slope"]["value"],"db":dd["inputs"]["meteo_data"]["radiation_db"]}
        time.sleep(0.5)
    pv[c]=res; print(c,{k:(round(v_["E_y"]),v_["angle"]) for k,v_ in res.items()},res["syd35"]["db"])
json.dump(pv,open(f"{V4}/pvgis.json","w"),indent=1)
