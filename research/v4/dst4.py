import json,urllib.request,itertools
def q(table,vars_):
    body=json.dumps({"table":table,"format":"JSONSTAT","lang":"da","variables":vars_}).encode()
    r=urllib.request.Request("https://api.statbank.dk/v1/data",data=body,headers={"Content-Type":"application/json"})
    return json.load(urllib.request.urlopen(r))
K=["000","461","561","621","630","615","730","851"]
d=q("BYGB50",[{"code":"OMRÅDE","values":K},{"code":"MÆNGDE4","values":["45"]},{"code":"TAGMAT","values":["*"]},{"code":"ANVEND","values":["120","130"]},{"code":"OPFØRELSESÅR","values":["*"]},{"code":"Tid","values":["2026"]}])
ds=d["dataset"]; dm=ds["dimension"]; ids=dm["id"]; v=ds["value"]
cats=[list(dm[i]["category"]["index"]) for i in ids]
res={combo:(v[n] or 0) for n,combo in enumerate(itertools.product(*cats))}
lab=dm["OMRÅDE"]["category"]["label"]; tl=dm["TAGMAT"]["category"]["label"]
out={}
for a in cats[0]:
    T={}
    for combo,val in res.items():
        if combo[0]==a: T[combo[2]]=T.get(combo[2],0)+val
    tot=sum(T.values()); out[a]={"name":lab[a],"tot":tot,"T":T}
    print(lab[a],tot,' | '.join(f"{tl[k][:18]} {x/tot:.1%}" for k,x in sorted(T.items(),key=lambda r:-r[1])[:6]))
json.dump({"labels":tl,"data":out},open("bygb50_2026.json","w"),ensure_ascii=False,indent=1)
