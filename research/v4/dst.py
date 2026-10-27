import json,urllib.request
def q(table,vars_):
    body=json.dumps({"table":table,"format":"JSONSTAT","lang":"da","variables":vars_}).encode()
    r=urllib.request.Request("https://api.statbank.dk/v1/data",data=body,headers={"Content-Type":"application/json"})
    return json.load(urllib.request.urlopen(r))
K=["000","461","561","621","630","615","730","851"]
d=q("BOL102",[{"code":"AMT","values":K},{"code":"BEBO","values":["1000"]},{"code":"ANVENDELSE","values":["125","130"]},{"code":"OPVARMNING","values":["*"]},{"code":"Tid","values":["2026"]}])
json.dump(d,open("bol102_2026.json","w"),ensure_ascii=False)
ds=d["dataset"]; dims=ds["dimension"]; ids=ds["dimension"]["id"]; size=ds["dimension"]["size"]
print(ids,size)
