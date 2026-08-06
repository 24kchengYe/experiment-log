# Artifact layout and lineage

Use this reference when a project contains multiple runs, derived datasets, prompts, reports, or model outputs.

## Separate artifact roles

```text
inputs/      immutable source inputs
runs/        replayable execution sites and intermediate state
versions/    immutable, validated artifacts consumed downstream
analysis/    derived interpretation; never the sole source of data
prompts/     active source plus archived/frozen snapshots
assets/      editable visual source plus rendered exports
```

These roles are semantic, not mandatory directory names. Map an existing project to them before reorganizing anything.

### Run

A run is an execution site. It may be incomplete, exploratory, failed, resumed, or superseded. Keep inputs, configuration, prompt snapshot, intermediate state, raw outputs, normalized outputs, logs, and the experiment record together when practical.

### Version

A version is a downstream-consumable snapshot promoted from one or more runs. It must have a stable schema, lineage, statistics, validation, and immutable identity. Do not promote every run to a version.

### Analysis

Analysis can aggregate many runs or versions. Its numbers must link back to machine-readable summaries or primary outputs. A report is not a replacement for raw predictions or manifests.

## Source-of-truth rules

- A convenience symlink, “active” directory, copied prompt, rendered image, or share bundle is a view, not automatically the source of truth.
- Historical reproduction uses the run's frozen snapshot or recorded hash, never the current active prompt/config.
- Record both the human-friendly version label and immutable identity: git commit, SHA-256, endpoint/checkpoint, or dataset manifest hash.
- When source files are uncommitted, say so and rely on frozen snapshots plus checksums; do not invent a commit association.
- Preserve superseded or invalid outputs with an explicit status and replacement pointer. Do not silently overwrite or delete evidence.

## Naming and status

Recommended names:

- run: `YYYY-MM-DD_<scope>_<experiment>`;
- version: `vNN_YYYY-MM-DD_<label>`;
- analysis: `YYYY-MM-DD_<topic>.md`;
- portable deliverable outside a dated directory: include version or date in the filename.

Useful statuses include `planned`, `running`, `completed`, `failed`, `data_ready`, `superseded`, `invalid`, and `archived`. Define project-specific values at first use.

## Promotion gate: run to version

Promote a run only when all of the following are known:

- exact source inputs and transformations;
- output schema and field meanings;
- inclusion, exclusion, fallback, and deduplication rules;
- row counts and count conservation;
- split and leakage policy, if relevant;
- prompt/model/rule identity;
- validation results and checksums;
- intended downstream consumer;
- pointer back to the producing run and code.
