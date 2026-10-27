"""Elpris: hentning, beregning og validering (bruges af build.py og refresh_elpris.py).

Kilder (kun åbne, gratis):
- Energi Data Service, datasæt DayAheadPrices (Energinet). Day-ahead-priser i 15-minutters opløsning siden 1/10 2025
  (det gamle datasæt Elspotprices sluttede 30/9 2025).
- Energi Data Service, datasæt DatahubPricelist: netselskabernes nettarif C (husstande på 0,4 kV-nettet) samt
  Energinets transmissionsnettarif, systemtarif og elafgiften (kode EA-001).
- Elafgiften 2026-2027 på 0,8 øre/kWh ekskl. moms er tjekket hos Skattestyrelsen (se data.py: "elafgift_skat").

Intet her opfinder tal: alt beregnes fra de hentede data. Fejler hentningen, bruges den sidst gode datafil.
"""
import json, os, datetime as dt, urllib.request, urllib.parse
from zoneinfo import ZoneInfo

CPH = ZoneInfo("Europe/Copenhagen")
HERE = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(HERE, "elpris_data.json")
API = "https://api.energidataservice.dk/dataset/"
MOMS = 0.25
ENERGINET_GLN = "5790000432752"
FEE_CODES = {"transmission": "40000", "system": "41000", "elafgift": "EA-001"}
FEE_LABELS = {"transmission": "Energinets transmissionsnettarif", "system": "Energinets systemtarif", "elafgift": "Elafgift"}
# Netselskaber, vi viser som eksempler. Kun selskaber, hvis prisområde er entydigt. Første selskab er standard.
# (visningsnavn, ChargeOwner i DatahubPricelist, ChargeTypeCodes der lægges sammen: nettarif C + evt. rabat)
NET = {
    "DK1": [("N1", "N1 A/S - 131", ["CD"]),
            ("Konstant", "Konstant Net A/S - 151", ["C_FBTNTR_B", "C_FBTNTR_R"]),
            ("TREFOR El-net", "TREFOR El-net A/S", ["C"]),
            ("Vores Elnet", "Vores Elnet A/S", ["TNT1009"])],
    "DK2": [("Radius", "Radius Elnet A/S", ["DT_C_01"]),
            ("Cerius", "Cerius A/S", ["30TR_C_ET", "30RE_C_ET"])],
}
AREAS = ("DK1", "DK2")
AREA_NAME = {"DK1": "Vestdanmark (DK1)", "DK2": "Østdanmark (DK2)"}
AREA_SHORT = {"DK1": "Jylland og Fyn", "DK2": "Sjælland, øerne og Bornholm"}
REGION_AREA = {"Region Nordjylland": "DK1", "Region Midtjylland": "DK1", "Region Syddanmark": "DK1",
               "Region Sjælland": "DK2", "Region Hovedstaden": "DK2"}

def _get(dataset, params, timeout=40):
    q = urllib.parse.urlencode(params)
    req = urllib.request.Request(API + dataset + "?" + q, headers={"User-Agent": "energitjekket.dk elpris-build"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.load(r)["records"]

def now_cph():
    return dt.datetime.now(CPH)

def fetch(today=None):
    """Henter rå data for i går..i overmorgen (vi bruger kun i dag og i morgen)."""
    today = today or now_cph().date()
    start = (today - dt.timedelta(days=1)).isoformat()
    end = (today + dt.timedelta(days=2)).isoformat()
    spot = _get("DayAheadPrices", {"start": start, "end": end, "filter": json.dumps({"PriceArea": list(AREAS)}),
                                   "sort": "TimeUTC asc", "limit": 0})
    owners = [o for a in AREAS for _, o, _ in NET[a]]
    net = _get("DatahubPricelist", {"filter": json.dumps({"ChargeOwner": owners}), "limit": 0})
    fees = _get("DatahubPricelist", {"filter": json.dumps({"GLN_Number": [ENERGINET_GLN]}), "limit": 0})
    return {"spot": spot, "net": net, "fees": fees}

def _valid_on(rec, day):
    d0 = day.isoformat() + "T00:00:00"
    return rec["ValidFrom"] <= d0 and (rec["ValidTo"] is None or rec["ValidTo"] > d0)

def _hourly(rec):
    if rec.get("ResolutionDuration") == "PT1H":
        return [float(rec[f"Price{i}"]) for i in range(1, 25)]
    return [float(rec["Price1"])] * 24  # P1D: samme pris hele døgnet

def compute(raw, fetched_at=None):
    fetched_at = fetched_at or now_cph()
    by_day = {}
    for r in raw["spot"]:
        if r.get("DayAheadPriceDKK") is None: continue
        d, t = r["TimeDK"][:10], r["TimeDK"][11:16]
        by_day.setdefault(d, {}).setdefault(r["PriceArea"], []).append((r["TimeUTC"], t, round(r["DayAheadPriceDKK"] / 1000, 5)))
    days = {}
    for d, areas in sorted(by_day.items()):
        day = dt.date.fromisoformat(d)
        fees = {}
        for k, code in FEE_CODES.items():
            recs = sorted((x for x in raw["fees"] if x["ChargeTypeCode"] == code and x["ChargeType"] == "D03" and _valid_on(x, day)), key=lambda x: x["ValidFrom"])
            if recs: fees[k] = round(float(recs[-1]["Price1"]), 6)
        net = {}
        for a in AREAS:
            net[a] = {}
            for label, owner, codes in NET[a]:
                def pick(code):  # kun tariffer (D03), nyeste gyldige post
                    v = sorted((x for x in raw["net"] if x["ChargeOwner"] == owner and x["ChargeTypeCode"] == code
                                and x["ChargeType"] == "D03" and _valid_on(x, day)), key=lambda x: x["ValidFrom"])
                    return v[-1] if v else None
                base = pick(codes[0])
                if not base: continue
                h = _hourly(base)
                for extra in codes[1:]:
                    x = pick(extra)
                    if x: h = [p + q for p, q in zip(h, _hourly(x))]
                net[a][label] = [round(p, 6) for p in h]
        days[d] = {"areas": {a: {"t": [t for _, t, _ in sorted(v)], "spot": [p for _, _, p in sorted(v)]} for a, v in areas.items()},
                   "fees": fees, "net": net}
    return {"fetched": fetched_at.isoformat(timespec="minutes"), "dataset": "DayAheadPrices", "days": days}

def validate(data, now=None, need_tomorrow=None):
    """Returnerer (fejl, advarsler). need_tomorrow=None: kræv i morgen efter kl. 13:30."""
    now = now or now_cph()
    today, tomorrow = now.date().isoformat(), (now.date() + dt.timedelta(days=1)).isoformat()
    if need_tomorrow is None: need_tomorrow = (now.hour, now.minute) >= (13, 30)
    errs, warns = [], []
    for d in (today, tomorrow):
        if d not in data["days"]:
            if d == today or need_tomorrow: errs.append(f"mangler data for {d}")
            else: warns.append(f"{d} er ikke offentliggjort endnu")
            continue
        D = data["days"][d]
        for a in AREAS:
            A = D["areas"].get(a)
            if not A: errs.append(f"{d} {a}: ingen spotpriser"); continue
            n = len(A["spot"])
            if n not in (92, 96, 100) and n not in (23, 24, 25): errs.append(f"{d} {a}: {n} perioder (forventet 96 kvarterer eller 24 timer)")
            if any(not (-5 <= p <= 15) for p in A["spot"]): errs.append(f"{d} {a}: urealistisk spotpris (uden for -5..15 kr./kWh)")
            if len(set(A["spot"])) < 3: errs.append(f"{d} {a}: næsten ens priser hele døgnet")
            if not D["net"].get(a): errs.append(f"{d} {a}: ingen nettarif C fundet")
            else:
                for lab, h in D["net"][a].items():
                    if not all(-0.5 <= x <= 5 for x in h): errs.append(f"{d} {a} {lab}: urealistisk nettarif")
                miss = [lab for lab, _, _ in NET[a] if lab not in D["net"][a]]
                if miss: warns.append(f"{d} {a}: ingen gyldig tarif for {', '.join(miss)}")
        for k in FEE_CODES:
            if k not in D["fees"]: errs.append(f"{d}: mangler {FEE_LABELS[k]}")
            elif not (0 <= D["fees"][k] <= 2): errs.append(f"{d}: urealistisk {FEE_LABELS[k]}")
    return errs, warns

def load():
    if not os.path.exists(DATA_FILE): return None
    with open(DATA_FILE, encoding="utf-8") as f: return json.load(f)

def save(data):
    tmp = DATA_FILE + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f: json.dump(data, f, ensure_ascii=False, separators=(",", ":"))
    os.replace(tmp, DATA_FILE)

def trim(data, keep_from):
    data["days"] = {d: v for d, v in data["days"].items() if d >= keep_from}
    return data

# ---------- beregninger til visning ----------
def total(spot, net_h, fees):
    """Anslået pris inkl. moms for én periode: (spot + nettarif + Energinet + elafgift) x 1,25."""
    return (spot + net_h + fees["transmission"] + fees["system"] + fees["elafgift"]) * (1 + MOMS)

def series(data, d, a, net_label=None):
    D = data["days"][d]; A = D["areas"][a]
    net_label = net_label or default_net(data, d, a)
    nh = D["net"][a][net_label]
    tot = [total(p, nh[int(t[:2])], D["fees"]) for t, p in zip(A["t"], A["spot"])]
    return A["t"], A["spot"], tot

def default_net(data, d, a):
    for lab, _, _ in NET[a]:
        if lab in data["days"][d]["net"][a]: return lab
    raise KeyError(a)

def hourly(ts, vals):
    out = {}
    for t, v in zip(ts, vals): out.setdefault(t[:2], []).append(v)
    return [(h, sum(v) / len(v)) for h, v in out.items()]

def stats(data, d, a, net_label=None):
    ts, spot, tot = series(data, d, a, net_label)
    hs, ht = hourly(ts, spot), hourly(ts, tot)
    i_min, i_max = min(range(len(spot)), key=spot.__getitem__), max(range(len(spot)), key=spot.__getitem__)
    ch = min(ht, key=lambda x: x[1]); ex = max(ht, key=lambda x: x[1])
    chs = min(hs, key=lambda x: x[1]); exs = max(hs, key=lambda x: x[1])
    best3 = None  # billigste sammenhængende 3 timer (samlet pris)
    for i in range(len(ht) - 2):
        s = sum(x[1] for x in ht[i:i + 3]) / 3
        if best3 is None or s < best3[1]: best3 = (ht[i][0], s, ht[i + 2][0])
    return {"spot_avg": sum(spot) / len(spot), "tot_avg": sum(tot) / len(tot),
            "spot_min": (ts[i_min], spot[i_min]), "spot_max": (ts[i_max], spot[i_max]),
            "cheap_h": ch, "exp_h": ex, "cheap_h_spot": chs, "exp_h_spot": exs, "best3": best3,
            "hours_spot": hs, "hours_tot": ht, "n": len(ts), "res": "15 min" if len(ts) > 30 else "1 time"}

SOURCES = {
    "eds_dap": ("Energi Data Service (Energinet): Day-Ahead Prices, DK1 og DK2", "https://www.energidataservice.dk/tso-electricity/DayAheadPrices"),
    "eds_tarif": ("Energi Data Service (Energinet): DatahubPricelist, tariffer og elafgift", "https://www.energidataservice.dk/tso-electricity/DatahubPricelist"),
    "elafgift_skat": ("Skattestyrelsen: midlertidig nedsættelse af elafgiften i 2026 og 2027", "https://skat.dk/erhverv/afgifter-paa-varer-og-ydelser-punktafgifter/nyhedsbrev-afgifter/midlertidig-nedsaettelse-af-elafgiften-i-2026-og-2027"),
}
