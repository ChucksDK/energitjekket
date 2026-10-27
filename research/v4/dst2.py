import json,urllib.request
def q(table,vars_):
    body=json.dumps({"table":table,"format":"JSONSTAT","lang":"da","variables":vars_}).encode()
    r=urllib.request.Request("https://api.statbank.dk/v1/data",data=body,headers={"Content-Type":"application/json"})
    return json.load(urllib.request.urlopen(r))
K=["000","461","561","621","630","615","730","851"]
d=q("BOL101",[{"code":"OMRÅDE","values":K},{"code":"BEBO","values":["1000"]},{"code":"ANVENDELSE","values":["125","130"]},{"code":"UDLFORH","values":["*"]},{"code":"OPFØRELSESÅR","values":["*"]},{"code":"Tid","values":["2026"]}])
json.dump(d,open("bol101_2026.json","w"),ensure_ascii=False)
ds=d["dataset"]; dm=ds["dimension"]; ids=dm["id"]; size=dm["size"]; v=ds["value"]
import itertools
cats=[list(dm[i]["category"]["index"]) for i in ids]
res={}
for idx,combo in enumerate(itertools.product(*cats)): res[combo]=v[idx] or 0
lab=dm["OMRÅDE"]["category"]["label"]
def bucket(y):
    s=y[:4] if y[0]!='-' else '1899'
    y=int(s)
    return 'før 1960' if y<1960 else ('1960-1979' if y<1980 else ('1980-1999' if y<2000 else '2000+'))
out={}
for a in cats[0]:
    tot=0; ej=0; B={}
    for combo,val in res.items():
        if combo[0]!=a: continue
        tot+=val
        if combo[3]=='EJ': ej+=val
        b=bucket(combo[4]); B[b]=B.get(b,0)+val
    out[a]={"name":lab[a],"tot":tot,"ej":ej,"B":B}
    print(lab[a],tot,f"ejer {ej/tot:.0%}",{k:f"{x/tot:.0%}" for k,x in B.items()})
json.dump(out,open("bol101_summary.json","w"),ensure_ascii=False,indent=1)
