# Multi-stage pipeline traceability

Use this reference when an experiment calls models/tools repeatedly, supports retries or resume, or produces labels through several stages.

## Stage contract

For each stage record:

- stage purpose and allowed inputs/outputs;
- exact prompt/config/schema/model identity;
- deterministic ID for each logical call or task;
- raw request and raw response;
- normalized result after parser/schema/registry validation;
- attempt number, error, retry decision, usage, latency, and timestamp;
- checkpoint/completion state.

Do not preserve hidden chain-of-thought. Preserve auditable facts, selected evidence, structured decisions, and externally visible reasoning summaries needed to reproduce the outcome.

## Raw versus normalized

Never overwrite raw responses with corrected results. Store normalization and repair actions separately. A deterministic repair may fix formatting or recompute a derived field, but must not silently change the model's substantive label.

## Retry and resume

- Keep one stable `call_id` or task ID across attempts.
- Resume by identifying missing or invalid logical calls, not by rerunning an entire completed stage.
- Record changed retry parameters such as timeout or output budget.
- Retain historical error ledgers after successful recovery.
- Audit for missing calls, duplicate canonical results, ID mismatches, illegal labels, and incomplete stages before release.

## Hierarchical release

If a pipeline can resolve different samples to different depths, record a release state per unit, such as complete, coarse-only, presence-only, or unresolved. Downstream exports must select compatible release states explicitly.

## Cost and efficiency

Report at least:

- successful and attempted calls by stage;
- calls per input unit;
- input/output/total tokens when available;
- wall-clock time and effective concurrency;
- retries and recovered failures;
- cost estimate and pricing assumptions;
- coverage or release rate.

An efficiency optimization is only validated when output quality is compared under the same input and reference. A counterfactual replay on saved calls is evidence for projected cost, not held-out quality.

## Final integrity audit

Before declaring completion, verify input conservation, stage completeness, prompt/config hashes, schema validity, unique IDs, legal label registry, release counts, excluded records, and checksum coverage. Link this audit from the experiment record.
