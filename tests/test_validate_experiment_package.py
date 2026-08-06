from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts.validate_experiment_package import validate


class ValidateExperimentPackageTests(unittest.TestCase):
    def test_complete_package_passes(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            package = Path(temp) / "P2-PER-EXT-02"
            for directory in (
                package / "inputs" / "formal_v01",
                package / "code",
                package / "outputs" / "formal_v01",
                package / "analysis" / "formal_v01",
            ):
                directory.mkdir(parents=True, exist_ok=True)
            (package / "README.md").write_text("scope", encoding="utf-8")
            (package / "EXPERIMENT_LOG.md").write_text("record", encoding="utf-8")
            (package / "inputs" / "formal_v01" / "analysis_contract.json").write_text("{}", encoding="utf-8")
            (package / "inputs" / "formal_v01" / "input_freeze_manifest.json").write_text("{}", encoding="utf-8")
            (package / "code" / "build_design.py").write_text("", encoding="utf-8")
            (package / "code" / "run_formal.py").write_text("", encoding="utf-8")
            (package / "code" / "analyze_formal.py").write_text("", encoding="utf-8")
            (package / "outputs" / "formal_v01" / "attempt_ledger.jsonl").write_text("", encoding="utf-8")
            (package / "outputs" / "formal_v01" / "failure_ledger.csv").write_text("", encoding="utf-8")
            (package / "outputs" / "formal_v01" / "run_manifest.json").write_text("{}", encoding="utf-8")
            (package / "analysis" / "formal_v01" / "summary.json").write_text("{}", encoding="utf-8")
            (package / "analysis" / "formal_v01" / "completion_audit.json").write_text("{}", encoding="utf-8")

            report = validate(package, "complete")
            self.assertTrue(report["ok"], report)

    def test_running_package_requires_freeze_and_outputs(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            package = Path(temp) / "P1-VIT-SIZE-01"
            (package / "inputs").mkdir(parents=True)
            (package / "code").mkdir()
            (package / "EXPERIMENT_LOG.md").write_text("record", encoding="utf-8")

            report = validate(package, "running")
            self.assertFalse(report["ok"])
            self.assertIn("no frozen input manifest found", report["errors"])
            self.assertIn("outputs/ is absent for a running or complete package", report["errors"])

    def test_historical_identifier_is_warning_not_error(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            package = Path(temp) / "EXP-3.5"
            (package / "inputs").mkdir(parents=True)
            (package / "code").mkdir()
            (package / "EXPERIMENT_LOG.md").write_text("record", encoding="utf-8")

            report = validate(package, "planned")
            self.assertTrue(report["ok"], report)
            self.assertTrue(any("does not match" in item for item in report["warnings"]))


if __name__ == "__main__":
    unittest.main()
