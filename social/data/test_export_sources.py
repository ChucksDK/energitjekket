import json
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(REPO / "src"))

import export_sources  # noqa: E402
import data_local_gen  # noqa: E402

FIXTURE = REPO / "social" / "test" / "fixtures" / "elpris_data.json"


class RegisterTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.reg = export_sources.build_register(REPO, elpris_path=FIXTURE)
        cls.facts = cls.reg["facts"]

    def test_pv_syd(self):
        f = self.facts["pv.aalborg.syd"]
        self.assertEqual(f["unit"], "kwh_per_kwp")
        self.assertEqual(f["value"], data_local_gen.PV["aalborg"]["syd"])
        self.assertEqual(f["source"]["name"], "PVGIS 5.3 (EU JRC)")
        self.assertEqual(f["source"]["url"], data_local_gen.PV["aalborg"]["url_syd"])

    def test_pv_months(self):
        keys = [k for k in self.facts if k.startswith("pv.kolding.month.")]
        self.assertEqual(len(keys), 12)

    def test_heat_pct(self):
        h = data_local_gen.HEAT["odense"]
        tot = sum(h.values())
        self.assertAlmostEqual(self.facts["heat.odense.fjernvarme_pct"]["value"], h["FJ"] / tot * 100)
        self.assertAlmostEqual(self.facts["heat.odense.varmepumpe_pct"]["value"], h["VP"] / tot * 100)
        self.assertEqual(self.facts["heat.odense.varmepumpe_pct"]["unit"], "pct")

    def test_elpris(self):
        self.assertEqual(self.facts["elpris.2026-10-27.DK1.billigste_time"]["value"], 6)
        self.assertEqual(self.facts["elpris.2026-10-27.DK1.billigste_time"]["unit"], "hour")
        hrs = self.reg["elpris"]["2026-10-27"]["DK1"]["hours"]
        self.assertEqual(len(hrs), 24)
        self.assertAlmostEqual(self.facts["elpris.2026-10-27.DK1.billigste_pris"]["value"], min(hrs))
        self.assertAlmostEqual(self.facts["elpris.2026-10-27.DK1.dyreste_pris"]["value"], max(hrs))
        self.assertAlmostEqual(self.facts["elpris.2026-10-27.DK1.gns_pris"]["value"], sum(hrs) / 24)

    def test_manual(self):
        f = self.facts["bolius.oliefyr"]
        self.assertEqual(f["value"], 32388)
        self.assertIn("bolius.dk", f["source"]["url"])
        self.assertEqual(self.facts["beregner.scop"]["unit"], "scop")

    def _tmp_repo(self, t, entry, html="<p>hej 32.388 kr.</p>"):
        t = Path(t)
        (t / "social" / "data").mkdir(parents=True)
        (t / "site").mkdir()
        (t / "site" / "a.html").write_text(html)
        base = {"id": "x.y", "value": 32388, "unit": "kr", "label": "l",
                "source_key": "bolius_varme", "site_text": "32.388 kr.", "page": "a.html"}
        base.update(entry)
        (t / "social" / "data" / "manual_facts.json").write_text(json.dumps([base]))
        return t

    def _build(self, entry, **kw):
        with tempfile.TemporaryDirectory() as t:
            t = self._tmp_repo(t, entry, **kw)
            return export_sources.build_register(t, elpris_path=FIXTURE, src_dir=REPO / "src")

    def test_valid_temp_fact(self):
        self.assertEqual(self._build({})["facts"]["x.y"]["value"], 32388)

    def test_missing_site_text_raises(self):
        with self.assertRaises(ValueError) as cm:
            self._build({"site_text": "findes ikke"})
        self.assertIn("x.y", str(cm.exception))

    def test_value_text_mismatch_raises(self):
        with self.assertRaises(ValueError) as cm:
            self._build({"value": 99999})
        self.assertIn("x.y", str(cm.exception))

    def test_text_on_other_page_raises(self):
        with self.assertRaises(ValueError) as cm:
            self._build({"page": "b.html"})
        self.assertIn("x.y", str(cm.exception))

    def test_raw_attribute_value_ok(self):
        r = self._build({"value": 3.5, "unit": "scop", "site_text": 'value="3.5"'}, html='<input value="3.5">')
        self.assertEqual(r["facts"]["x.y"]["value"], 3.5)

    def test_unknown_source_key_raises(self):
        with self.assertRaises(ValueError) as cm:
            self._build({"source_key": "findes_ikke"})
        self.assertIn("x.y", str(cm.exception))

    def test_format_da(self):
        self.assertEqual(export_sources.format_da(32388, "kr"), "32.388 kr.")
        self.assertEqual(export_sources.format_da(1.45, "kr_per_kwh"), "1,45 kr.")
        self.assertEqual(export_sources.format_da(6, "hour"), "kl. 06")

    def test_quarter_guard(self):
        raw = json.loads(FIXTURE.read_text())
        day = next(iter(raw["days"].values()))
        day["areas"]["DK1"]["spot"] = day["areas"]["DK1"]["spot"][:95]
        with tempfile.TemporaryDirectory() as t:
            f = Path(t) / "e.json"
            f.write_text(json.dumps(raw))
            with self.assertRaises(ValueError):
                export_sources.build_register(REPO, elpris_path=f)



class AtomicWriteTest(unittest.TestCase):
    def test_main_writes_via_temp_file_and_os_replace(self):
        import os
        from unittest import mock
        calls = []
        real = os.replace

        def spy(src, dst):
            calls.append((str(src), str(dst)))
            # Midt i skrivningen må målfilen ikke findes halvt skrevet: kun temp-filen findes.
            self.assertFalse(Path(dst).exists())
            self.assertTrue(json.loads(Path(src).read_text(encoding="utf-8"))["facts"])
            real(src, dst)

        with tempfile.TemporaryDirectory() as t:
            out = Path(t) / "sources.json"
            with mock.patch.object(export_sources.os, "replace", side_effect=spy):
                export_sources.main(["--elpris", str(FIXTURE), "--out", str(out)])
            self.assertEqual(len(calls), 1)
            self.assertEqual(Path(calls[0][0]).parent, out.parent)
            self.assertEqual(calls[0][1], str(out))
            self.assertTrue(json.loads(out.read_text(encoding="utf-8"))["facts"])
            self.assertEqual(sorted(p.name for p in Path(t).iterdir()), ["sources.json"])


if __name__ == "__main__":
    unittest.main()
