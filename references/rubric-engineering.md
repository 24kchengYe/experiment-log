# Rubric engineering

Use this reference when experiments require constructing, revising, freezing, auditing, or migrating an evaluation rubric.

## Hierarchy

```text
Domain → Category → Rubric → Mode → Severity / decision effect
```

- **Domain**: independently reviewed object or capability area.
- **Category**: navigation and reporting group; it should help readers and models narrow the search space.
- **Rubric**: one judgment object, evidence source, and responsibility path.
- **Mode**: a concrete violation pattern under that Rubric.
- **Severity / effect**: fixed consequence of the Mode; do not let the reviewer improvise it.

Split Rubrics when the judgment object, required evidence, or ownership path differs. Do not mechanically split several illegal scenarios when they share the same object, evidence, severity, and repair direction. Conversely, do not merge different root causes merely to reduce label count.

## Construction workflow

1. **Build the evidence pool**
   - Product/specification constraints and deterministic checker rules.
   - Historical evaluator issues with exact input and evidence.
   - Unresolved cases, reviewer disagreements, model errors, and repair regressions.
   - Existing rules and their observed frequency.
2. **Normalize issue facts**
   - Separate symptom, violated constraint, root cause, severity, and suggested repair.
   - Rewrite examples into domain-independent violation facts before clustering.
3. **Create the hierarchy**
   - Group by Domain and Category.
   - Define Rubrics by judgment object/evidence/ownership.
   - Define Modes only for operationally distinct violation conditions.
4. **Write the decision contract**
   - Judgment object, scope, standard, applicability, exclusions, evidence requirements, anti-false-positive rules, counting unit, Modes, fixed severity, and calibration examples.
5. **Run overlap and atomicity audits**
   - One Issue should describe one independent violation fact.
   - Add precedence or exclusion rules for likely double hits.
   - A Mode name must match its actual violation condition.
   - Keep repair suggestions and concrete examples outside the core definition when they encourage overfitting.
6. **Generate machine-readable registry and prompt views**
   - Full Guide: evidence requirements, exclusions, calibration cases.
   - Review Prompt: full decision contract for labeling.
   - Training/online Prompt: concise rules with the same registry and output contract.
   - Registry: stable IDs, hierarchy, severity, and allowed values.
7. **Pilot and calibrate**
   - Sample common, long-tail, clean, multi-issue, and boundary cases.
   - Measure existence, Category, Rubric, Mode, multi-label, and reason stability separately.
   - Review disagreements per case before editing rules.
8. **Freeze a version**
   - Freeze Guide, prompts, registry, builder, counts, manifest, and SHA-256.
   - Record which evaluator/data experiments support the version.

Use [RUBRIC_VERSION_TEMPLATE.md](../assets/RUBRIC_VERSION_TEMPLATE.md) for the frozen bundle.

## Quality checks

- Every Mode has exactly one Rubric and one fixed severity/effect.
- Every emitted label exists in the registry; no duplicate `rubric_id + mode`.
- Applicability and exclusion rules prevent obvious overreach.
- Evidence requirements can be checked from the evaluator input.
- Counting rules distinguish one root cause from repeated manifestations.
- Multi-issue examples demonstrate zero, one, and several independent issues.
- Long-tail and zero-frequency Modes are listed. Low frequency is not proof that a rule is invalid; inspect applicability and available data.
- Rubric count reflects decision boundaries, not a desire for either maximal detail or minimal labels.

## Version migration

Classify every old label as unchanged, pure rename, split, merge, semantic change, removed, or new. Only unchanged labels and true renames are safe for deterministic migration. Splits, merges, severity changes, and semantic boundary changes require targeted or full re-review.

Before replacing a frozen version:

- calculate affected historical labels and Review Units;
- publish an old→new migration table with evidence;
- identify validators, prompts, datasets, and reports tied to the old registry;
- compare old and candidate rules on fixed inputs with the same evaluator when testing rule quality;
- preserve the old bundle and label version.

Do not call a candidate “the new version” until structure, semantics, migration cost, and fixed-set behavior have been reviewed.
