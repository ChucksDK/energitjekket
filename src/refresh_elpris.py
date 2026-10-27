#!/usr/bin/env python3
"""Daglig elpris-opdatering: hent -> valider -> byg -> check.py -> klargør deploy-pakke.

Kør fra projektroden eller src/:
    python3 src/refresh_elpris.py                  # normal kørsel (13:45-rutinen og 08:00-by-rutinen)
    python3 src/refresh_elpris.py --verify-live    # efter deploy: tjek energitjekket.dk
    python3 src/refresh_elpris.py --mark-deployed dpl_xxx   # efter godkendt live-tjek: gem som baseline

Selve uploadet sker via Vercel MCP (der er ingen Vercel-token på boksen): se README, "Elpris-rutinen".
Exit-koder: 0 = klar til deploy (eller intet ændret), 2 = data ugyldige/forældede (deploy ikke),
3 = morgendagens priser mangler efter kl. 13:30 (prøv igen senere), 4 = build eller check.py fejlede.
Idempotent: kan køres igen når som helst. Fejler hentningen, bruges den sidst gode datafil (src/elpris_data.json).
"""
import argparse, base64, fcntl, hashlib, http.server, json, os, shutil, socketserver, subprocess, sys, threading, urllib.request, functools, re
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import elpris as EL
SITE = os.path.join(ROOT, "site"); DEP = os.path.join(ROOT, "deploy"); B64 = os.path.join(DEP, "b64")
LIVE = "https://energitjekket.dk"

def log(*a): print(*a, flush=True)

def files_manifest():
    out = []
    for dp, _, fs in os.walk(SITE):
        for f in fs:
            p = os.path.join(dp, f); b = open(p, "rb").read()
            out.append({"file": os.path.relpath(p, SITE).replace(os.sep, "/"), "sha": hashlib.sha1(b).hexdigest(), "size": len(b)})
    return sorted(out, key=lambda x: x["file"])

def run_check():
    class H(http.server.SimpleHTTPRequestHandler):
        def log_message(self, *a): pass
    class S(socketserver.ThreadingMixIn, http.server.HTTPServer):
        daemon_threads = True
        def handle_error(self, *a): pass  # check.py lukker forbindelser tidligt; støj, ikke fejl
    srv = S(("127.0.0.1", 0), functools.partial(H, directory=SITE)); port = srv.server_address[1]
    t = threading.Thread(target=srv.serve_forever, daemon=True); t.start()
    try:
        env = dict(os.environ, CHECK_BASE=f"http://127.0.0.1:{port}")
        r = subprocess.run([sys.executable, os.path.join(ROOT, "verify", "check.py")], capture_output=True, text=True, env=env, timeout=900)
    finally:
        srv.shutdown()
    open(os.path.join(ROOT, "verify", "check-output-elpris-latest.txt"), "w").write(r.stdout + r.stderr)
    gate = [l for l in r.stdout.splitlines() if l.startswith("GATE:")]
    return r.returncode == 0, (gate[-1] if gate else (r.stderr.strip().splitlines() or ["check.py gav intet output"])[-1])

def prepare_deploy():
    files = files_manifest()
    base = {}
    bp = os.path.join(DEP, "deployed.json")
    if os.path.exists(bp): base = {f["file"]: f["sha"] for f in json.load(open(bp))["files"]}
    up = [f for f in files if base.get(f["file"]) != f["sha"]]
    shutil.rmtree(B64, ignore_errors=True); os.makedirs(B64)
    for f in up:
        with open(os.path.join(SITE, f["file"]), "rb") as src, open(os.path.join(B64, f["sha"] + ".b64"), "w") as dst:
            dst.write(base64.b64encode(src.read()).decode())
    removed = sorted(set(base) - {f["file"] for f in files})
    json.dump(files, open(os.path.join(DEP, "files.json"), "w"), separators=(",", ":"))
    json.dump([{**f, "b64": os.path.join(B64, f["sha"] + ".b64")} for f in up], open(os.path.join(DEP, "upload.json"), "w"), indent=0)
    return files, up, removed

def verify_live():
    data = EL.load(); days = sorted(data["days"]); today = EL.now_cph().date().isoformat()
    errs = []
    def get(u):
        req = urllib.request.Request(u, headers={"User-Agent": "energitjekket-verify", "Cache-Control": "no-cache"})
        with urllib.request.urlopen(req, timeout=30) as r: return r.status, r.read().decode("utf-8", "replace")
    st, h = get(LIVE + "/elpris/?v=" + data["fetched"][:16].replace(":", ""))
    if st != 200: errs.append(f"/elpris/ gav {st}")
    want = [d for d in days if d >= today][:2] or days[-1:]
    for d in want:
        if f'data-d="{d}"' not in h: errs.append(f"/elpris/ mangler {d} i HTML")
    if today not in days: errs.append(f"datafilen har ikke {today}")
    sm = get(LIVE + "/sitemap.xml")[1]
    bad = []
    for u in re.findall(r"<loc>([^<]+)</loc>", sm):
        try:
            s, body = get(u)
            if s != 200: bad.append((u, s))
        except Exception as e: bad.append((u, str(e)))
    if bad: errs.append(f"{len(bad)} sitemap-URL'er fejler: {bad[:5]}")
    for p in ("/assets/elpris.js", "/og/elpris.png"):
        try: get(LIVE + p)
        except Exception as e: errs.append(f"{p}: {e}")
    log(json.dumps({"live_ok": not errs, "errors": errs, "days_in_html": want, "sitemap_urls_checked": len(re.findall('<loc>', sm))}, ensure_ascii=False))
    return 0 if not errs else 1

def mark_deployed(dpl):
    files = json.load(open(os.path.join(DEP, "files.json")))
    json.dump({"deployment": dpl, "marked": EL.now_cph().isoformat(timespec="minutes"), "files": files}, open(os.path.join(DEP, "deployed.json"), "w"), indent=0)
    st = os.path.join(DEP, "status.json")
    if os.path.exists(st):
        s = json.load(open(st)); s["deployed"] = dpl; json.dump(s, open(st, "w"), ensure_ascii=False, indent=1)
    log(f"Baseline gemt: {dpl} ({len(files)} filer)")
    return 0

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--verify-live", action="store_true"); ap.add_argument("--mark-deployed")
    ap.add_argument("--skip-fetch", action="store_true", help="byg med den sidst gode datafil")
    ap.add_argument("--allow-missing-tomorrow", action="store_true")
    a = ap.parse_args()
    os.makedirs(DEP, exist_ok=True)
    lock = open(os.path.join(DEP, ".lock"), "w")
    try: fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except OSError: log("En anden kørsel er i gang."); return 4
    if a.mark_deployed: return mark_deployed(a.mark_deployed)
    if a.verify_live: return verify_live()

    now = EL.now_cph(); status = {"started": now.isoformat(timespec="minutes"), "ready": False}
    old = EL.load(); fresh = None; fetch_err = None
    if not a.skip_fetch:
        try:
            fresh = EL.compute(EL.fetch(now.date()), now)
        except Exception as e:
            fetch_err = f"{type(e).__name__}: {e}"
    data = None
    if fresh:
        errs, warns = EL.validate(fresh, now, need_tomorrow=False if a.allow_missing_tomorrow else None)
        status.update(fetch="ok", errors=errs, warnings=warns)
        if old and not errs and EL.trim(dict(fresh), now.date().isoformat())["days"] == old.get("days"):
            fresh["fetched"] = old["fetched"]  # samme data som sidst: behold tidsstemplet, så en genkørsel giver identisk build
        if not errs:
            data = EL.trim(fresh, now.date().isoformat()); EL.save(data)
        elif any("mangler data for" in e and e.endswith((now.date() + EL.dt.timedelta(days=1)).isoformat()) for e in errs) and len(errs) == 1:
            # i dag er fin, kun i morgen mangler: gem i dag, men meld "prøv igen"
            data = EL.trim(fresh, now.date().isoformat()); EL.save(data); status["tomorrow_missing"] = True
    else:
        status.update(fetch="fejl" if fetch_err else "sprunget over", fetch_error=fetch_err)
    if data is None:
        data = old
        if not data or now.date().isoformat() not in data["days"]:
            status["result"] = "Ingen gyldige data for i dag. Siden bygges ikke om, intet deployes."
            json.dump(status, open(os.path.join(DEP, "status.json"), "w"), ensure_ascii=False, indent=1); log(json.dumps(status, ensure_ascii=False, indent=1)); return 2
        status["used_cached_data"] = data["fetched"]
    r = subprocess.run([sys.executable, os.path.join(HERE, "build.py")], cwd=HERE, capture_output=True, text=True)
    if r.returncode != 0:
        status["result"] = "build.py fejlede: " + r.stderr[-800:]
        json.dump(status, open(os.path.join(DEP, "status.json"), "w"), ensure_ascii=False, indent=1); log(json.dumps(status, ensure_ascii=False, indent=1)); return 4
    ok, gate = run_check(); status["check"] = gate
    if not ok:
        status["result"] = "check.py fejlede (se verify/check-output-elpris-latest.txt). Intet deployes."
        json.dump(status, open(os.path.join(DEP, "status.json"), "w"), ensure_ascii=False, indent=1); log(json.dumps(status, ensure_ascii=False, indent=1)); return 4
    files, up, removed = prepare_deploy()
    status.update(ready=True, data_days=sorted(data["days"]), data_fetched=data["fetched"], files=len(files), upload=len(up), removed_since_baseline=removed,
                  files_json=os.path.join(DEP, "files.json"), upload_json=os.path.join(DEP, "upload.json"), nothing_changed=not up)
    code = 0
    if status.get("tomorrow_missing"):
        status["result"] = "Bygget med i dag. Morgendagens priser mangler stadig: kør igen om 15-30 min, før der deployes (eller deploy med --allow-missing-tomorrow)."
        status["ready"] = False; code = 3
    else:
        status["result"] = "Intet ændret siden sidste deploy." if not up else f"Klar: upload {len(up)} filer og opret produktions-deploy med {len(files)} filer."
    json.dump(status, open(os.path.join(DEP, "status.json"), "w"), ensure_ascii=False, indent=1)
    log(json.dumps(status, ensure_ascii=False, indent=1))
    return code

if __name__ == "__main__": sys.exit(main())
