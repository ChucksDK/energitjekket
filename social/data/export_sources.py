#!/usr/bin/env python3
"""Byg kilderegisteret social/data/sources.json ud fra repoets egne data."""
import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

PV_SOURCE = "PVGIS 5.3 (EU JRC)"
HEAT_SOURCE = {"name": "Danmarks Statistik BOL102 (2026)", "url": "https://www.statbank.dk/BOL102"}
ELPRIS_SOURCE = {"name": "Energi Data Service (Energinet), spotpris", "url": "https://www.energidataservice.dk/"}


def _load_src_modules(src_dir):
    sys.path.insert(0, str(src_dir))
    try:
        import data_local_gen
        import data
    finally:
        sys.path.remove(str(src_dir))
    return data_local_gen, data


def _fact(value, unit, label, source):
    return {"value": value, "unit": unit, "label": label, "source": source}


def _pv_facts(PV):
    facts = {}
    for city, d in PV.items():
        src = {"name": PV_SOURCE, "url": d["url_syd"]}
        facts[f"pv.{city}.syd"] = _fact(d["syd"], "kwh_per_kwp", f"Solcelleproduktion pr. kWp pr. år, {city}, sydvendt", src)
        for i, v in enumerate(d["months"], start=1):
            facts[f"pv.{city}.month.{i}"] = _fact(v, "kwh_per_kwp", f"Solcelleproduktion pr. kWp i måned {i}, {city}", src)
    return facts


def _heat_facts(HEAT):
    facts = {}
    for city, codes in HEAT.items():
        total = sum(codes.values())
        facts[f"heat.{city}.fjernvarme_pct"] = _fact(codes["FJ"] / total * 100, "pct", f"Andel boliger med fjernvarme, {city}", HEAT_SOURCE)
        facts[f"heat.{city}.varmepumpe_pct"] = _fact(codes["VP"] / total * 100, "pct", f"Andel boliger med varmepumpe, {city}", HEAT_SOURCE)
    return facts


def _elpris(elpris_path):
    raw = json.loads(Path(elpris_path).read_text(encoding="utf-8"))
    facts, hours_out = {}, {}
    for date, day in raw["days"].items():
        hours_out[date] = {}
        for area, a in day["areas"].items():
            spot = a["spot"]
            if len(spot) != 96:
                raise ValueError(f"elpris {date} {area}: forventede 96 kvartersværdier, fik {len(spot)}")
            hrs = [round(sum(spot[h * 4:h * 4 + 4]) / 4, 6) for h in range(24)]
            hours_out[date][area] = {"hours": hrs}
            lo, hi = min(hrs), max(hrs)
            base = f"elpris.{date}.{area}"
            lbl = f"{date}, {area}"
            facts[f"{base}.billigste_time"] = _fact(hrs.index(lo), "hour", f"Billigste time, {lbl}", ELPRIS_SOURCE)
            facts[f"{base}.billigste_pris"] = _fact(lo, "kr_per_kwh", f"Billigste spotpris pr. time, {lbl}", ELPRIS_SOURCE)
            facts[f"{base}.dyreste_time"] = _fact(hrs.index(hi), "hour", f"Dyreste time, {lbl}", ELPRIS_SOURCE)
            facts[f"{base}.dyreste_pris"] = _fact(hi, "kr_per_kwh", f"Dyreste spotpris pr. time, {lbl}", ELPRIS_SOURCE)
            facts[f"{base}.gns_pris"] = _fact(sum(hrs) / 24, "kr_per_kwh", f"Gennemsnitlig spotpris, {lbl}", ELPRIS_SOURCE)
    return facts, hours_out


_DA_RULES = {
    "kr": (0, " kr."), "kr_per_kwh": (2, " kr."), "kwh": (0, " kWh"), "kwh_per_kwp": (0, " kWh"),
    "pct": (0, " %"), "m2": (0, " m²"), "kwp": (0, " kWp"), "count": (0, ""), "scop": (1, ""),
}


def format_da(value, unit):
    """Samme danske formatering som social/lib/format.js formatFact."""
    if unit == "hour":
        return f"kl. {int(value):02d}"
    if unit not in _DA_RULES:
        raise ValueError(f"format_da: ukendt enhed {unit!r}")
    decimals, suffix = _DA_RULES[unit]
    s = f"{value:,.{decimals}f}".replace(",", "_").replace(".", ",").replace("_", ".")
    return s + suffix


def _value_matches(value, unit, text):
    """Værdien skal stå i teksten: dansk formateret, eller som rå value="..."-attribut."""
    formatted = format_da(value, unit)
    if re.search(r"(?<![\d.,])" + re.escape(formatted), text):
        return True
    return f'value="{value}"' in text


def _manual_facts(repo_root, S):
    items = json.loads((Path(repo_root) / "social" / "data" / "manual_facts.json").read_text(encoding="utf-8"))
    site = Path(repo_root) / "site"
    facts = {}
    for m in items:
        page = site / m["page"]
        if not page.is_file():
            raise ValueError(f"{m['id']}: siden {m['page']} findes ikke")
        if m["site_text"] not in page.read_text(encoding="utf-8", errors="replace"):
            raise ValueError(f"{m['id']}: site_text {m['site_text']!r} findes ikke i site/{m['page']}")
        if not _value_matches(m["value"], m["unit"], m["site_text"]):
            raise ValueError(f"{m['id']}: værdien {m['value']!r} ({m['unit']}) står ikke i site_text {m['site_text']!r}")
        if m["source_key"] not in S:
            raise ValueError(f"{m['id']}: ukendt source_key {m['source_key']!r}")
        name, url = S[m["source_key"]]
        facts[m["id"]] = _fact(m["value"], m["unit"], m["label"], {"name": name, "url": url})
    return facts


def build_register(repo_root, elpris_path=None, src_dir=None):
    repo_root = Path(repo_root)
    gen, data = _load_src_modules(src_dir or repo_root / "src")
    elpris_path = elpris_path or repo_root / "src" / "elpris_data.json"
    facts = {}
    facts.update(_pv_facts(gen.PV))
    facts.update(_heat_facts(gen.HEAT))
    ef, hours = _elpris(elpris_path)
    facts.update(ef)
    facts.update(_manual_facts(repo_root, data.S))
    return {"generated": datetime.now(timezone.utc).isoformat(timespec="seconds"), "facts": facts, "elpris": hours}


def main(argv=None):
    repo_root = Path(__file__).resolve().parent.parent.parent
    ap = argparse.ArgumentParser()
    ap.add_argument("--elpris", default=None)
    ap.add_argument("--out", default=str(repo_root / "social" / "data" / "sources.json"))
    a = ap.parse_args(argv)
    reg = build_register(repo_root, elpris_path=a.elpris)
    out = Path(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(reg, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"skrev {out} ({len(reg['facts'])} fakta)")


if __name__ == "__main__":
    main()
