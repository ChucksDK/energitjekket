import json,urllib.request,time
C={"kolding":(55.4904,9.4722),"vejle":(55.7113,9.5357),"esbjerg":(55.4765,8.4594),"odense":(55.4038,10.4024),"aalborg":(57.0488,9.9217),"randers":(56.4607,10.0364),"horsens":(55.8607,9.8503)}
out={}
for c,(la,lo) in C.items():
    res={}
    for name,extra in (("syd35","angle=35&aspect=0"),("oest_vest","angle=35&aspect=-90"),("vest","angle=35&aspect=90"),("opt","optimalangles=1")):
        u=f"https://re.jrc.ec.europa.eu/api/v5_3/PVcalc?lat={la}&lon={lo}&peakpower=1&loss=14&{extra}&outputformat=json"
        d=json.load(urllib.request.urlopen(u,timeout=60))
        res[name]={"url":u.replace("&outputformat=json","&outputformat=json"),"E_y":d["outputs"]["totals"]["fixed"]["E_y"],"H_y":d["outputs"]["totals"]["fixed"]["H(i)_y"],
                   "months":[m["E_m"] for m in d["outputs"]["monthly"]["fixed"]],"angle":d["inputs"]["mounting_system"]["fixed"]["slope"]["value"],"db":d["inputs"]["meteo_data"]["radiation_db"]}
        time.sleep(0.5)
    out[c]=res
    print(c,{k:(round(v["E_y"]),v["angle"]) for k,v in res.items()},res["syd35"]["db"])
json.dump(out,open("pvgis.json","w"),indent=1)
