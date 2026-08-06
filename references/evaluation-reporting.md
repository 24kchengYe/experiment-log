# Evaluation and comparison reporting

Use this reference for model evaluation, ablations, reviewer stability, label audits, and root-cause reports.

## Define the evaluation contract

Before results, state:

- evaluation unit and sample count;
- positive class and clean/problem/pass/fail semantics;
- GT source and review status;
- model, checkpoint/endpoint, prompt, user-input schema, decoding config, and evaluation code;
- whether the dataset was reused during development;
- which factors are fixed and which changed.

Define every metric at first use. Accuracy, pass rate, issue presence, verdict, category, exact set match, Jaccard, Precision, Recall, and F1 are not interchangeable.

## Comparable does not mean identical

- Same input IDs do not imply same GT.
- Same GT does not imply same System/User Prompt or output schema.
- Same metric name does not imply the same positive class, unit, averaging, or denominator.
- A common intersection enables a scoped comparison; it does not replace full-set results.

When two training/review methods create different label sets for the same inputs, use a 2×2 evaluation where appropriate: evaluate both models against both label sources. Report diagonal fit and cross-label generalization separately.

## Report several layers separately

For structured predictions, report only applicable layers, for example:

1. problem existence or clean detection;
2. top-level verdict;
3. category;
4. rubric/class ID;
5. fine mode/subtype;
6. single-label versus multi-label exactness;
7. reason/description semantic quality.

State whether counts are units or label instances. For multi-label tasks, include micro/macro method and exact-set criteria.

## Semantic review

When exact string or ID matching is insufficient, create a structured review dataset containing input, GT, prediction, judgment, and rationale. Define categories before review, such as exact, partial/subset, and incorrect/conflicting. Preserve the reviewed rows, not only aggregate percentages.

## Root-cause analysis

- Analyze per-case evidence, then aggregate causes; do not infer causes from metrics alone.
- Separate label/rubric ambiguity, reviewer instability, prompt-context failure, model capability, parsing/schema failure, and data coverage.
- Include representative cases for major error modes and point to the full machine-readable review set.
- Correct GT before recomputing metrics; keep the original label version archived and name the reviewed GT version.

## Share bundle

A portable evaluation bundle should include raw predictions, GT/manifest, metric JSON, config, validation summary, main report, detailed case review, and a manifest explaining which model was evaluated against which GT. A standalone HTML is a view, not the only artifact.
