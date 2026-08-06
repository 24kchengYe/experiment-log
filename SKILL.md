---
name: exp-log
description: Write, update, synchronize, and audit reproducible Experiment Logs, evidence-backed Experiment Guides or research narratives, dataset/model version records, evaluation reports, multi-stage pipeline traces, and explicitly requested paper drafts from one traceable evidence base. Use for “实验记录”, “实验日志”, “实验指南”, “研究叙事”, “数据版本说明”, “评测报告”, “记录这个实验”, “整理实验结论”, “同步记录和指南”, “写论文”, “experiment log”, “experiment guide”, completed training/evaluation/ablation runs, failed experiments, artifact lineage, or turning accumulated experiments into defensible findings. Supports record, guide, sync, audit, failure, update, extract, and explicit paper modes while preserving /exp-log and /experiment-log compatibility.
---

# Experiment Log + Guide

Maintain several views of the same evidence without confusing their purposes.

- **Experiment Log** (`EXPERIMENT_LOG.md`) is the factual source of truth: what ran, why, with which data, code, prompt, model, metrics, outputs, and failures.
- **Experiment Guide / Research Narrative** (`EXPERIMENT_GUIDE.md`) explains the research problem, evidence chain, retained decisions, limitations, and next questions to a reader.
- **Paper draft** is a publication-oriented transformation of the same evidence. Enter this mode only when the user explicitly requests a paper, manuscript, or paper section.

The Guide may tell a coherent story. It must not invent continuity, certainty, causality, or contributions that the Log does not support. Paper mode is never inferred from a request to record or summarize experiments.

## Route the request

| User intent | Mode | Primary output |
|---|---|---|
| Record a completed or failed run | `record` / `failure` | Experiment Log |
| Update status, metrics, paths, or conclusions | `update` | Experiment Log |
| Explain what the experiments now show | `guide` | Experiment Guide |
| Keep factual and narrative views aligned | `sync` | Log first, then Guide if material |
| Check correctness, traceability, or contradictions | `audit` | Audit findings and corrections |
| Locate or repackage existing evidence | `extract` | Requested index, table, or summary |
| Write a paper or manuscript section | `paper` | Explicitly requested paper artifact |

After a substantive experiment, default to `sync`: record the experiment first, then apply the Guide impact gate. For a small metadata/path correction, update only the Log unless the correction changes a claim.

## Shared workflow

1. **Discover the evidence**
   - Inspect the current Log, Guide, manifests, configs, prompts, datasets, evaluation outputs, and code.
   - Prefer primary artifacts over old narrative summaries.
   - Map inputs, runs, versions, analysis, prompts, and share artifacts before treating similarly named files as equivalent.
2. **Identify the unit of record**
   - Assign or preserve an `EXP-ID`.
   - State the research question, baseline, changed variables, evaluation unit, and data split.
3. **Write the factual record first**
   - Follow [record-mode.md](references/record-mode.md).
   - Record exact paths, versions, denominators, failures, and comparison conditions.
4. **Classify evidence strength**
   - `Established`: controlled evidence with the needed statistical support.
   - `Supported`: consistent evidence with relevant controls, but not definitive.
   - `Preliminary`: limited runs/data or remaining confounders.
   - `Hypothesis`: plausible explanation awaiting a direct test.
5. **Run the Guide impact gate**
   - Follow [guide-mode.md](references/guide-mode.md) only when new evidence materially changes the reader-facing account.
6. **Audit the views**
   - Follow [sync-audit.md](references/sync-audit.md).
   - A Guide or paper claim must resolve to an `EXP-ID`, table, metric, or artifact in the Log.

## Load specialized rules only when needed

- For a project with many runs, versions, prompts, reports, symlinks, or copied artifacts, read [artifact-lineage.md](references/artifact-lineage.md).
- When creating or revising a training/test/annotation/model version, read [dataset-versioning.md](references/dataset-versioning.md) and use [DATA_VERSION_TEMPLATE.md](assets/DATA_VERSION_TEMPLATE.md).
- For evaluation, ablation, reviewer-stability, semantic review, or root-cause analysis, read [evaluation-reporting.md](references/evaluation-reporting.md) and use [EVALUATION_REPORT_TEMPLATE.md](assets/EVALUATION_REPORT_TEMPLATE.md).
- For multi-stage model/tool pipelines with retries, checkpoints, or partial release states, read [pipeline-traceability.md](references/pipeline-traceability.md) and use [RUN_EXPERIMENT_TEMPLATE.md](assets/RUN_EXPERIMENT_TEMPLATE.md).

## Guide impact gate

Update the Guide when new evidence changes at least one of:

- the main finding or its evidence strength;
- the retained/default model, prompt, dataset, pipeline, or evaluation method;
- dataset scale, composition, split, or version;
- the research framework or causal explanation;
- an important limitation, trade-off, or evidence boundary;
- next-step priority.

If none changes, leave the Guide untouched and report: `Guide: no material change`.

## Document contracts

### Experiment Log

The Log is appendable, reproducible, and exact. It may contain negative results, operational details, and unresolved contradictions. Use [EXPERIMENT_LOG_TEMPLATE.md](assets/EXPERIMENT_LOG_TEMPLATE.md) for the project ledger and [RUN_EXPERIMENT_TEMPLATE.md](assets/RUN_EXPERIMENT_TEMPLATE.md) for a standalone run record.

Each experiment requires:

- `EXP-ID`, date, status, and relevant git/version identifiers;
- motivation and falsifiable hypothesis;
- data source, split, sample counts, and evaluation unit;
- method and every variable changed from the named baseline;
- results with metric definitions and denominators;
- interpretation separated from observation;
- evidence strength and comparison limitations;
- exact code, prompt, config, data, model, report, and output paths.

### Experiment Guide

The Guide is concise, evidence-forward, and organized by research question rather than execution date. Use [EXPERIMENT_GUIDE_TEMPLATE.md](assets/EXPERIMENT_GUIDE_TEMPLATE.md). Each important claim includes its scope, evidence and denominator, supporting `EXP-ID` or artifact, evidence strength, and practical implication or uncertainty.

### Paper

Use [paper-mode.md](references/paper-mode.md) only after an explicit paper request. Paper mode may organize a contribution narrative, but all quantitative claims, comparisons, and limitations remain traceable to the Log. If venue, section, or audience is unclear, produce a neutral research-paper draft rather than assuming a venue.

## Commands

- `/exp-log record` — add a completed experiment.
- `/exp-log failure` — record a failed run and the constraint learned.
- `/exp-log update` — update an existing experiment.
- `/exp-log guide` — refresh the reader-facing Guide from the Log.
- `/exp-log sync` — update the Log, run the impact gate, then audit both views.
- `/exp-log audit` — check missing evidence, arithmetic, paths, versions, and contradictions.
- `/exp-log extract` — produce a path index, comparison table, timeline, slides outline, or requested view.
- `/exp-log paper` — draft or revise a paper artifact; explicit user request required.

## Completion check

- Verify every new number against its source; make units and denominators explicit.
- Name the exact baseline and changed variables.
- Distinguish observation, interpretation, and hypothesis.
- Ensure file links and artifact paths resolve.
- Ensure Guide and paper claims do not exceed Log evidence.
- Report which views changed and which did not.
