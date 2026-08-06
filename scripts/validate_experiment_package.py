from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


ID_PATTERN = re.compile(r"^P\d-[A-Z0-9]+(?:-[A-Z0-9]+)*-\d{2}$")
PHASES = ("planned", "frozen", "running", "complete")


def any_match(root: Path, patterns: tuple[str, ...]) -> list[str]:
    matches: set[str] = set()
    if not root.exists():
        return []
    for pattern in patterns:
        for path in root.rglob(pattern):
            if path.is_file():
                matches.add(path.relative_to(root).as_posix())
    return sorted(matches)


def validate(package: Path, phase: str) -> dict:
    package = package.resolve()
    errors: list[str] = []
    warnings: list[str] = []
    found: dict[str, list[str] | bool] = {}

    if not package.is_dir():
        return {
            "package": str(package),
            "phase": phase,
            "errors": ["package path is not a directory"],
            "warnings": [],
            "found": {},
            "ok": False,
        }

    experiment_id = package.name
    if not ID_PATTERN.fullmatch(experiment_id):
        warnings.append(
            "package name does not match P<stage>-<DOMAIN>-<TASK?>-<NN>; "
            "preserve it if the project has an established alternative"
        )

    required_root = {
        "experiment_log": package / "EXPERIMENT_LOG.md",
        "inputs": package / "inputs",
        "code": package / "code",
    }
    for key, path in required_root.items():
        present = path.exists()
        found[key] = present
        if not present:
            errors.append(f"missing required package surface: {path.name}")

    found["readme"] = (package / "README.md").exists()
    if not found["readme"]:
        warnings.append("README.md is absent; add a one-screen scope and entry-point index")

    input_root = package / "inputs"
    code_root = package / "code"
    output_root = package / "outputs"
    analysis_root = package / "analysis"

    freeze = any_match(input_root, ("*freeze*manifest*.json", "*input*manifest*.json"))
    contracts = any_match(input_root, ("*spec*.json", "*contract*.json"))
    builders = any_match(code_root, ("build_*.*", "*design*.*"))
    runners = any_match(code_root, ("run_*.*",))
    found.update(freeze_manifests=freeze, contracts=contracts, builders=builders, runners=runners)

    if phase in {"frozen", "running", "complete"}:
        if not freeze:
            errors.append("no frozen input manifest found")
        if not contracts:
            errors.append("no specification or analysis contract found")
        if not runners:
            errors.append("no formal runner found under code/")

    if phase in {"running", "complete"}:
        found["outputs"] = output_root.exists()
        if not output_root.exists():
            errors.append("outputs/ is absent for a running or complete package")
        run_manifests = any_match(output_root, ("*run*manifest*.json",))
        failure_ledgers = any_match(output_root, ("*failure*ledger*",))
        attempt_ledgers = any_match(
            output_root,
            ("*attempt*ledger*", "canonical_responses.jsonl", "*event*ledger*.jsonl", "*image*manifest*.json"),
        )
        found.update(
            run_manifests=run_manifests,
            failure_ledgers=failure_ledgers,
            attempt_or_output_ledgers=attempt_ledgers,
        )
        if not run_manifests:
            warnings.append("no run manifest found under outputs/")
        if not failure_ledgers:
            warnings.append("no failure ledger found under outputs/")
        if not attempt_ledgers:
            warnings.append("no canonical attempt/output ledger found under outputs/")

    if phase == "complete":
        found["analysis"] = analysis_root.exists()
        if not analysis_root.exists():
            errors.append("analysis/ is absent for a complete package")
        summaries = any_match(analysis_root, ("*summary*.csv", "*summary*.json", "RESULTS.md"))
        audits = any_match(package, ("*completion*audit*.json", "*integrity*audit*.json"))
        analyzers = any_match(code_root, ("analy*.*",))
        found.update(analysis_summaries=summaries, completion_audits=audits, analyzers=analyzers)
        if not summaries:
            errors.append("no analysis summary found")
        if not audits:
            errors.append("no completion or integrity audit found")
        if not analyzers:
            errors.append("no analysis code found under code/")

    prohibited = []
    for path in package.rglob("*"):
        if not path.is_file():
            continue
        stem = path.stem.lower()
        if re.search(r"(^|[_-])(final|latest|new2?)([_-]|$)", stem):
            prohibited.append(path.relative_to(package).as_posix())
    found["unstable_names"] = sorted(prohibited)
    if prohibited:
        warnings.append("files use unstable names such as final/latest/new; prefer semantic versions")

    return {
        "experiment_id": experiment_id,
        "package": str(package),
        "phase": phase,
        "errors": errors,
        "warnings": warnings,
        "found": found,
        "ok": not errors,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit an experiment package without modifying it.")
    parser.add_argument("package", type=Path)
    parser.add_argument("--phase", choices=PHASES, default="complete")
    parser.add_argument("--output", type=Path, help="Optional JSON report path")
    args = parser.parse_args()

    report = validate(args.package, args.phase)
    payload = json.dumps(report, ensure_ascii=False, indent=2)
    print(payload)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(payload + "\n", encoding="utf-8")
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
