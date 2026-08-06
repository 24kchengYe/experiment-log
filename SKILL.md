---
name: exp-log
description: Design, freeze, run, resume, record, promote, audit, and synthesize reproducible scientific experiments, experiment packages, dataset/model versions, evaluations, and research narratives from one traceable evidence base; also extract verified repeated workflows into reusable skills. Use whenever a task involves 实验记录、实验日志、实验包、实验编号、冻结协议、失败账本、运行清单、完成审计、实验指南、研究叙事、数据版本说明、评测报告、从实验提取技能、结果整理、论文实验部分, experiment logs, experiment packages, experiment guides, ablations, evaluations, failed or interrupted runs, artifact lineage, multi-stage pipeline traces, rubric-version provenance, or evidence-backed paper writing. Supports record and synthesis modes plus record, failure, update, guide, sync, audit, promote, extract-skill, extract, and explicit paper routes while preserving /exp-log and /experiment-log compatibility.
---

# Experiment Log

Maintain one evidence base through two working modes.

1. **Record mode** preserves what was planned, frozen, executed, returned, analyzed, and audited. Its unit is an experiment package with immutable identifiers and traceable artifacts.
2. **Synthesis mode** explains what the accumulated experiments show. Its default artifact is an Experiment Guide; a paper, manuscript section, response, or presentation is an explicitly requested publication output of the same mode.

The modes have different information density. Record mode may include operational failures, commands, hashes, and exact paths. Synthesis mode keeps only the evidence needed to understand the research question, comparison, result, meaning, and boundary.

## Route the request

| User intent | Route | Working mode | Primary output |
|---|---|---|---|
| Plan or freeze a new experiment | `record` | Record | Experiment package and frozen inputs |
| Continue, resume, or monitor a run | `update` | Record | Run manifest, response ledger, status update |
| Record a completed or failed run | `record` / `failure` | Record | Package `EXPERIMENT_LOG.md` and artifacts |
| Check completeness, arithmetic, paths, or contradictions | `audit` | Record | Audit findings or completion audit |
| Explain what the experiments now show | `guide` | Synthesis | Experiment Guide |
| Align factual and reader-facing views | `sync` | Record, then synthesis | Log update and authorized Guide update |
| Locate or repackage evidence | `extract` | Either | Requested index, table, or summary |
| Promote validated Run output to an immutable Version | `promote` | Record | Version bundle and lineage contract |
| Turn a verified repeated workflow into a reusable skill | `extract-skill` | Record | Skill package with tests and evidence anchors |
| Write a paper, response, abstract, or named section | `paper` | Synthesis | Explicitly requested publication artifact |

A request to run or record an experiment does not authorize a Guide or paper rewrite. After a material result, report whether the Guide would change. Update it only when the user requested `guide`/`sync` or has already authorized automatic synchronization. If the project requires confirmation, propose the affected claims and wait.

## Select the governing references

- For experiment identity, P0–P3 stages, package layout, versions, run states, freezing, execution, and completion audits, read [experiment-package.md](references/experiment-package.md).
- For factual experiment records, read [record-mode.md](references/record-mode.md).
- For Experiment Guides and research narratives, read [guide-mode.md](references/guide-mode.md).
- For an explicitly requested publication artifact, also read [paper-mode.md](references/paper-mode.md).
- For cross-document consistency or audits, read [sync-audit.md](references/sync-audit.md).

When a filesystem-backed experiment package is available, use `scripts/validate_experiment_package.py <path> --phase planned|frozen|running|complete` as a structural check. Treat its output as an audit aid, not a substitute for reading scientific contracts and results.

## Record-mode workflow

1. **Discover the current contract**
   - Inspect existing package IDs, stage legend, logs, manifests, prompts, configs, data, code, raw outputs, analysis, and project instructions.
   - Map inputs, runs, promoted versions, analysis, prompts, and shared artifacts before treating similarly named files as equivalent.
   - Preserve an established naming system. Do not mass-rename historical experiments unless explicitly requested.
2. **Define the experiment unit**
   - Assign one stable Experiment ID to one scientific question and design family.
   - Separate package identity from model, route, condition, replicate, timestamp, and analysis version.
3. **Freeze before formal outputs**
   - Freeze the question, estimand, unit, fixed denominator, conditions, exclusions, retry policy, analysis contract, and claim boundary.
   - Hash or otherwise version the design inputs and code needed to reconstruct the run.
4. **Validate with a fixture or technical gate**
   - Test schemas, parsers, hooks, model loading, file paths, and no-op behavior without consuming formal units.
   - Keep technical amendments versioned and distinguish them from scientific design changes.
5. **Execute append-only**
   - Preserve every registered attempt, successful output, technical failure, and recovery action.
   - Do not retry, regenerate, exclude, or select outputs based on observed scientific results unless the frozen policy permits it.
6. **Analyze from the frozen contract**
   - Keep raw outputs, parsed data, unit-level estimands, summary tables, and figures separable.
   - Define metrics, units, denominators, uncertainty, baselines, and changed variables.
7. **Audit completion**
   - Account for the fixed denominator and verify missing, duplicate, unknown, or orphaned artifacts.
   - Record procedural status, evidentiary result, and claim eligibility separately.
8. **Update the factual record**
   - Write observation before interpretation and link every claim to its primary artifact.

## Synthesis-mode workflow

1. Establish the evidence boundary from completed or explicitly labeled preliminary packages.
2. Write one sentence stating the research question and strongest supported answer.
3. Build a claim–evidence map before prose: claim, comparison, result, denominator, uncertainty, Experiment ID, and scope.
4. Organize by research question and evidence chain, not by execution date or tool history.
5. Prefer a compact result table when the same fields repeat across conditions, indicators, theories, or datasets.
6. Explain physical meaning and units before parameter names. A conclusion must say what changed or was learned, not merely that estimates were produced.
7. Include a limitation only when it changes interpretation, applicability, or the next decision. Preserve mandatory disclosures without appending a generic weakness inventory.
8. Keep commands, endpoints, retry history, local paths, and routine HTTP counts in Record mode unless they alter the evidence boundary.
9. Run a hostile-review pass: narrow claims that exceed the measured sample, model, route, protocol, or comparison, while retaining the scientific value that remains supported.

## Evidence strength and status

Use evidence labels when they help a decision or resolve ambiguity; do not repeat them mechanically after every paragraph.

- `Established`: controlled evidence with the required statistical and procedural support.
- `Supported`: consistent evidence with relevant controls but a remaining limitation.
- `Preliminary`: incomplete denominator, limited run, pilot, or unresolved confounder.
- `Hypothesis`: proposed explanation awaiting a direct test.

Never collapse the following into one status:

- **Procedural status**: whether the registered work completed as specified.
- **Evidentiary result**: whether the result supports, partly supports, contradicts, or leaves the hypothesis unresolved.
- **Claim eligibility**: whether the result belongs in the main text, SI, diagnostic record, or no-claim archive.

A null result is not a run failure. A completed API run is not evidence for the hypothesis. A provider-limit stop is procedural and does not define a scientific result.

## Load specialized rules only when needed

- For a project with many runs, versions, prompts, reports, symlinks, or copied artifacts, read [artifact-lineage.md](references/artifact-lineage.md).
- When creating or revising a training/test/annotation/model version, read [dataset-versioning.md](references/dataset-versioning.md) and use [DATA_VERSION_TEMPLATE.md](assets/DATA_VERSION_TEMPLATE.md).
- For evaluation, ablation, reviewer-stability, semantic review, or root-cause analysis, read [evaluation-reporting.md](references/evaluation-reporting.md) and use [EVALUATION_REPORT_TEMPLATE.md](assets/EVALUATION_REPORT_TEMPLATE.md).
- For multi-stage model/tool pipelines with retries, checkpoints, or partial release states, read [pipeline-traceability.md](references/pipeline-traceability.md) and use [RUN_EXPERIMENT_TEMPLATE.md](assets/RUN_EXPERIMENT_TEMPLATE.md).
- When an experiment consumes a Rubric, record its version, registry/prompt paths, manifest, and hashes. Use a dedicated Rubric-engineering skill to construct, calibrate, freeze, or migrate the rules themselves.
- When a verified experimental method should become a reusable skill, read [skill-extraction.md](references/skill-extraction.md). Use the environment's skill-creation workflow to package and validate it.

## Guide impact gate

Update the Guide when new evidence changes at least one of:

- the main finding or its evidence strength;
- the retained/default model, prompt, dataset, pipeline, or evaluation method;
- dataset scale, composition, split, or version;
- the research framework or causal explanation;
- an important limitation, trade-off, or evidence boundary;
- next-step priority.

If none changes, report `Guide: no material change`. If change is material but authorization is absent, report the affected section and proposed claim without editing it.

## Document contracts

### Experiment Log

The package Log is appendable, reproducible, and exact. It may contain negative results, operational details, and unresolved contradictions. Use [EXPERIMENT_LOG_TEMPLATE.md](assets/EXPERIMENT_LOG_TEMPLATE.md) for a package or project ledger and [RUN_EXPERIMENT_TEMPLATE.md](assets/RUN_EXPERIMENT_TEMPLATE.md) for a standalone run record. A project-level index may link package IDs and primary artifacts but should not duplicate every package entry.

Each experiment requires:

- Experiment ID, date, the three status axes, and relevant git/version identifiers;
- motivation and falsifiable hypothesis;
- data source, split, sample counts, and evaluation unit;
- method and every variable changed from the named baseline;
- results with metric definitions and denominators;
- interpretation separated from observation;
- evidence strength and comparison limitations;
- exact code, prompt, config, data, model, report, and output paths;
- frozen input manifest, immutable attempt/output ledger, failure ledger, run manifest, and completion audit when applicable.

### Experiment Guide

The Guide is concise and organized by research question rather than execution date. Use [EXPERIMENT_GUIDE_TEMPLATE.md](assets/EXPERIMENT_GUIDE_TEMPLATE.md). Repeated comparisons belong in interpretable tables with definitions and units. Evidence-strength labels are optional when scope and support are already clear; do not turn them into repetitive boilerplate.

### Publication outputs

Use [paper-mode.md](references/paper-mode.md) only after an explicit paper request. Paper writing is a synthesis output, not a third factual mode. It may organize a contribution narrative, but all quantitative claims, comparisons, and limitations remain traceable to the package evidence. If venue, section, or audience is unclear, produce a neutral research-paper draft rather than assuming a venue.

## Commands

- `/exp-log record` — plan, freeze, or record an experiment package.
- `/exp-log failure` — preserve a failed or interrupted attempt and the constraint learned.
- `/exp-log update` — update progress, metrics, paths, or status.
- `/exp-log guide` — synthesize the evidence into an Experiment Guide.
- `/exp-log sync` — update the Record, apply the impact gate, then update the Guide if authorized.
- `/exp-log audit` — check package completeness, provenance, arithmetic, versions, and cross-document claims.
- `/exp-log extract` — produce an index, comparison table, timeline, source table, slides outline, or requested view.
- `/exp-log promote` — promote validated Run output to a frozen data/model Version.
- `/exp-log extract-skill` — extract a stable, tested workflow from verified experiments.
- `/exp-log paper` — draft or revise an explicitly requested publication artifact.

## Completion check

- Every new number resolves to a primary artifact; units and denominators are explicit.
- Experiment ID, Attempt ID, run version, and analysis version are not conflated.
- The baseline and every changed variable are named.
- Formal inputs were frozen before formal outputs, or the deviation is disclosed.
- Registered attempts, failures, retries, and exclusions follow the frozen policy.
- Observation, interpretation, explanation, and hypothesis remain distinct.
- Package paths resolve and completion status is auditable.
- Guide or paper claims do not exceed the Record evidence.
- Report which record, guide, paper, or repository surfaces changed and which did not.
