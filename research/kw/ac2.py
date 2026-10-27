import urllib.request, urllib.parse, json, sys, time
def ac(q):
    u="https://suggestqueries.google.com/complete/search?client=firefox&hl=da&gl=dk&q="+urllib.parse.quote(q)
    try: return json.loads(urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=10).read().decode('utf-8','replace'))[1]
    except Exception as e: return ['ERR '+str(e)]
seeds=[l.strip() for l in open(sys.argv[1]) if l.strip()]
out={}
for s in seeds:
    out[s]=ac(s); time.sleep(0.25)
json.dump(out,open(sys.argv[2],'w'),ensure_ascii=False,indent=0)
for k,v in out.items(): print(k,'=>',v)
