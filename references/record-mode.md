# Record mode

The experiment package is the factual source of truth. Do not smooth contradictions or hide failed attempts to improve the narrative. Read [experiment-package.md](experiment-package.md) before creating a package or assigning an identifier.

## Required experiment entry

```markdown
### {EXPERIMENT-ID}: {one-line scientific question or test}

**Date**: YYYY-MM-DD

**Procedural status**: planned / frozen / running / stopped / complete / failed
**Evidentiary result**: not_analyzed / supports / partly_supports / mixed / null / contradicts / inconclusive
**Claim eligibility**: main_text / SI / diagnostic / pilot_only / no_claim
**Git / versions**: {commit, design, dataset, prompt, model receipt, route, analysis}

#### Motivation and hypothesis
What question is tested, why now, and what result would support or reject it?

#### Method and data
- Baseline and all changed variables
- Data source, version, split rule, registered denominator, and evaluation unit
- Prompt/model/config and fair-comparison controls
- Attempt IDs, missing-data policy, exclusions, and retry policy
- Frozen input and analysis-contract versions

#### Execution and integrity
- Fixture or technical-gate result
- Called, terminal, successful, failed, and uncalled attempt counts
- Resume or recovery actions and whether existing terminal records were immutable
- Run-manifest and failure-ledger status

#### Results
- Metric definitions on first use
- Numerator, denominator, sample size, uncertainty or number of runs
- Exact comparison table and exceptions
- Unit-level estimand and summary/source-table paths

#### Analysis
- Observation
- Interpretation
- Alternative explanations or confounders
- Evidence strength: Established / Supported / Preliminary / Hypothesis
- Decision and next EXP-ID

#### Artifacts
- Code, frozen inputs, prompt, data, model/route evidence, raw outputs, failure ledger, run manifest, parsed data, analysis, completion audit, source tables, and figures
```

## Lifecycle updates

A package Log is updated throughout the lifecycle; it is not written only after success.

1. **Planned**: record the question, dependency, proposed ID, and unresolved design choices.
2. **Frozen**: record the registered denominator, estimand, controls, retry/exclusion policy, versions, and freeze manifest before formal outputs.
3. **Running or stopped**: report exact called/terminal/remaining counts. Distinguish quota, credential, provider, executor, parser, and scientific failures.
4. **Complete**: link analysis and completion audit; report the three status axes separately.
5. **Amended**: identify whether the change is scientific or technical, which version supersedes which, and whether formal units ran before the amendment.

## Precision rules

- Use exact paths, prompt versions, model/endpoint IDs or receipts, hashes, and timestamps when available. Put long launch commands in logs or `ops/` rather than bloating the narrative entry.
- Define terms such as Review Unit, Issue, Clean, Verdict, positive/negative sample, pair, case, and trajectory at first use.
- State whether counts are cases, versions, domain units, issues, or rubric labels. Never mix them in one column.
- Name the exact baseline. Replace “旧版本” with version/date/key metric/path.
- List every changed variable. Do not present a multi-variable experiment as a single-factor ablation.
- State whether train/test prompts and schemas match, whether the test set was reused for development, and whether labels were reviewed.
- Separate model prediction, historical Judge output, rule mapping, agent review, and human/strong-model Gold.
- If a proxy metric is used, state its relationship to the end objective.
- Distinguish a replayable run from a promoted data/model version. Link both when a run produces a downstream version.
- If the same IDs have revised labels, name the label/GT version every time a result is reported.
- Preserve `superseded` and `invalid` experiments with the reason and replacement pointer; exclude their numbers from current conclusions.
- Record partial completion, checkpoint recovery, and whether resumed work reran completed units.
- Do not call content-bearing HTTP responses “valid data” before parsing and schema checks.
- Do not call a provider-limit stop an experiment failure or a null result.
- Do not report an analysis as formal when the fixed denominator has not been accounted for, unless the frozen contract defines an interim analysis.

## Failed experiments

For failures, additionally record:

- observed failure and affected scope;
- excluded hypothesis;
- established constraint;
- unresolved alternatives;
- next experiment linked by `EXP-ID`.

Use a short decision chain when several failures lead to the same retained design.

## Organization

- Keep one detailed Log in each experiment package. Use a project-level registry only as an index of package IDs, statuses, results, and primary artifacts.
- Organize package summaries by research question; order packages chronologically only within a question.
- Describe an experiment in one package and cross-reference it elsewhere.
- Keep engineering fixes separate from research conclusions.
- Maintain a compact experiment index with `EXP-ID`, question, status, key result, and artifact link.
- Keep machine-readable summaries beside prose when the experiment has nontrivial counts or distributions.
