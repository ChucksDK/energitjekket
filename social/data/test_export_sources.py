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

    def test_missing_site_text_raises(self):
        with tempfile.TemporaryDirectory() as t:
            t = Path(t)
            (t / "social" / "data").mkdir(parents=True)
            (t / "site").mkdir()
            (t / "site" / "a.html").write_text("<p>hej</p>")
            (t / "social" / "data" / "manual_facts.json").write_text(json.dumps([
                {"id": "x.y", "value": 1, "unit": "kr", "label": "l",
                 "source_key": "bolius_varme", "site_text": "findes ikke"}]))
            with self.assertRaises(ValueError) as cm:
                export_sources.build_register(t, elpris_path=FIXTURE, src_dir=REPO / "src")
            self.assertIn("x.y", str(cm.exception))


if __name__ == "__main__":
    unittest.main()
