import json,urllib.request,itertools
def info(t): return json.load(urllib.request.urlopen(f"https://api.statbank.dk/v1/tableinfo/{t}?lang=da&format=JSON"))
def q(table,vars_):
    body=json.dumps({"table":table,"format":"JSONSTAT","lang":"da","variables":vars_}).encode()
    r=urllib.request.Request("https://api.statbank.dk/v1/data",data=body,headers={"Content-Type":"application/json"})
    return json.load(urllib.request.urlopen(r))
K={"461":"odense","561":"esbjerg","621":"kolding","630":"vejle","615":"horsens","730":"randers","851":"aalborg"}
bi=info("BY3"); byer=[v for v in bi["variables"] if v["id"]=="BYER"][0]["values"]
ids=[x["id"] for x in byer if x["id"][:3] in K and not x["id"].endswith(("99999","99997"))]
d=q("BY3",[{"code":"BYER","values":ids},{"code":"FOLKARTAET","values":["FOLKETAL"]},{"code":"Tid","values":["2026"]}])
ds=d["dataset"]; lab=ds["dimension"]["BYER"]["category"]["label"]; idx=ds["dimension"]["BYER"]["category"]["index"]
vals=ds["value"]; out={}
for i,k in enumerate(idx):
    out.setdefault(K[k[:3]],[]).append((lab[k],vals[i]))
for c in out: out[c].sort(key=lambda x:-(x[1] or 0)); print(c,out[c][:10])
json.dump(out,open("by3_2026.json","w"),ensure_ascii=False,indent=1)
# BYGB50 roof material
bi=info("BYGB50")
for v in bi["variables"]: print(v["id"],[(x["id"],x["text"]) for x in v["values"]][:30] if v["id"]!="OMRÅDE" else "")
