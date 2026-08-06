# Sync and audit

## Sync order

1. Update the Experiment Log from primary artifacts.
2. Recalculate affected summaries and indices.
3. Run the Guide impact gate in `SKILL.md`.
4. If material, update the Guide's affected claims, evidence strength, decisions, and traceability links.
5. Update paper artifacts only when the user explicitly requested paper work.
6. Run the audit below and report changed/unchanged views.

## Audit checklist

### Traceability

- Every Guide or paper number resolves to a Log entry and primary artifact.
- Every retained recommendation names its supporting `EXP-ID`s.
- Paths exist or are clearly marked unavailable/remote.

### Arithmetic and units

- Totals equal subgroup sums when they are meant to.
- Percentages use the stated numerator and denominator.
- Case, version, Review Unit, Issue, pair, and rubric counts are not conflated.
- Precision, Recall, F1, accuracy, exact match, Jaccard, and pass rate are defined once and used consistently.
- Source, included, excluded, and split counts obey conservation equations.

### Version consistency

- Prompt, rubric, dataset, label, model, endpoint, and evaluation-script versions match the actual run.
- Training and test schemas are identified.
- Reviewed GT is distinguished from original labels and predictions.
- Active symlinks or current prompts are not cited as historical run snapshots.

### Comparison validity

- Baselines use comparable data, thresholds, prompts, post-processing, and evaluation units.
- Same input IDs, same GT, same prompt/schema, and same evaluation code are checked as separate conditions.
- Reused test sets and multiple comparisons are disclosed.
- Single runs are not presented as stable improvements.
- Causal attribution matches the variables controlled.

### Narrative consistency

- The Guide does not omit a failure that invalidates its recommendation.
- Evidence-strength labels match the Log.
- “Current,” “best,” and “default” refer to one identified version.
- Next steps respond to unresolved evidence rather than repeating completed work.

## Audit output

Return findings in three groups:

1. **Must correct** — wrong numbers, broken provenance, version mismatch, or contradicted claims.
2. **Must clarify** — ambiguous units, metrics, baselines, or evidence strength.
3. **Optional strengthening** — additional controls or evidence that would improve confidence.
