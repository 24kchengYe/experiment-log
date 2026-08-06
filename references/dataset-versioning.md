# Dataset and model versioning

Use this reference when an experiment creates training, test, annotation, prediction, or model artifacts.

## Version README contract

Every consumable version should answer:

1. What is this version for, and what is its status?
2. Which run(s), input version(s), code, prompt/rule, model, and label process produced it?
3. Which records were included, excluded, repaired, deduplicated, or reverted?
4. What does each output field mean? Include one compact structural example when the schema is not obvious.
5. How many cases, versions, units, labels/issues, pairs, and rows exist? Keep units separate.
6. How were train/validation/test splits created or preserved?
7. Which leakage keys were checked: case ID, group ID, exact input hash, near-duplicate key, or other project unit?
8. What validation, summary, manifest, and checksum files accompany it?
9. What should downstream consumers read, and which files are analysis-only?
10. Which earlier version does it supersede, and what changed?

Use [DATA_VERSION_TEMPLATE.md](../assets/DATA_VERSION_TEMPLATE.md) when creating a new version.

## Preserve identity and lineage

- Never overwrite an existing version. A schema, label, cleaning, split, prompt, or selection change creates a new version.
- Preserve the previous split when the research question does not require resampling. Record why a new split is necessary.
- Keep excluded, unresolved, or partial records in a separate artifact with exclusion reasons when they may support later review.
- Store a manifest that maps every training/evaluation row to its source unit, case/version identity, split, label provenance, and pairing metadata.
- Store prompt snapshots used to generate labels and prompts embedded in training examples separately when they serve different purposes.

## Label quality

Distinguish label sources such as deterministic conversion, single review, multi-review vote, adjudicated label, model proxy Gold, and human Gold. Do not collapse them into one “GT” field without provenance.

If a label is hierarchical or partial, record the released depth explicitly. For example, a unit may be stable at problem presence or category but unresolved at fine label. Do not export partial labels as complete targets merely to preserve dataset size.

## Count conservation

At minimum verify:

```text
source_total = included_total + excluded_total
total_rows = train_rows + validation_rows + test_rows
```

When one unit may contain multiple labels, report both affected units and label instances. When paired data is used, report complete pairs, broken pairs, and whether pairs cross splits.

## Model artifact identity

For trained models record base model, training dataset version/hash, training prompt/schema, job ID, checkpoint/global step, endpoint, training config, and evaluation dataset version. A friendly model name alone is insufficient.
