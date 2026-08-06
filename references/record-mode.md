# Record mode

The Experiment Log is the factual source of truth. Do not smooth contradictions or hide failed attempts to improve the narrative.

## Required experiment entry

```markdown
### EXP-{section}.{number}: {one-line title}

**Date**: YYYY-MM-DD

**Status**: planned / in_progress / complete / failed
**Git / version**: {commit, dataset, prompt, model, endpoint}

#### Motivation and hypothesis
What question is tested, why now, and what result would support or reject it?

#### Method and data
- Baseline and all changed variables
- Data source, version, split rule, sizes, and evaluation unit
- Prompt/model/config/command and fair-comparison controls

#### Results
- Metric definitions on first use
- Numerator, denominator, sample size, uncertainty or number of runs
- Exact comparison table and exceptions

#### Analysis
- Observation
- Interpretation
- Alternative explanations or confounders
- Evidence strength: Established / Supported / Preliminary / Hypothesis
- Decision and next EXP-ID

#### Artifacts
- Code, config, prompt, data, model, raw outputs, report, figures
```

## Precision rules

- Use exact paths, commands, prompt versions, model/endpoint IDs, hashes, and timestamps when available.
- Define terms such as Review Unit, Issue, Clean, Verdict, positive/negative sample, pair, case, and trajectory at first use.
- State whether counts are cases, versions, domain units, issues, or rubric labels. Never mix them in one column.
- Name the exact baseline. Replace “旧版本” with version/date/key metric/path.
- List every changed variable. Do not present a multi-variable experiment as a single-factor ablation.
- State whether train/test prompts and schemas match, whether the test set was reused for development, and whether labels were reviewed.
- Separate model prediction, historical Judge output, rule mapping, agent review, and human/strong-model Gold.
- If a proxy metric is used, state its relationship to the end objective.

## Failed experiments

For failures, additionally record:

- observed failure and affected scope;
- excluded hypothesis;
- established constraint;
- unresolved alternatives;
- next experiment linked by `EXP-ID`.

Use a short decision chain when several failures lead to the same retained design.

## Organization

- Organize detailed entries by research question; order experiments chronologically within a question.
- Describe an experiment in one place and cross-reference it elsewhere.
- Keep engineering fixes separate from research conclusions.
- Maintain a compact experiment index with `EXP-ID`, question, status, key result, and artifact link.
