# Experiment identity and package contract

Use this contract for new experiment families. When a project already has a documented contract, preserve it and record deviations instead of silently replacing it.

## 1. Separate four identifiers

1. **Experiment ID** identifies one scientific question and design family. It remains stable across reruns and analysis revisions.
2. **Design version** identifies frozen inputs, prompts, schemas, estimands, and analysis rules, for example `formal_v01`.
3. **Attempt ID** identifies one registered sampling or evaluation unit, condition, and replicate. It is assigned before the attempt runs.
4. **Run/analysis version** identifies a concrete execution route and a concrete readout, for example `formal_gpt4o_v01` and `formal_v01`.

Do not place a model name, seed, timestamp, completion status, or words such as `final` and `latest` in the Experiment ID. Those describe an execution or version, not the scientific question.

## 2. Stage–domain–task Experiment IDs

For a new staged research program, prefer:

```text
P<stage>-<DOMAIN>-<TASK>-<NN>
```

- `P<stage>` is the project stage.
- `DOMAIN` is a stable uppercase subject tag such as `MODEL`, `SCL`, `DIST`, `VIT`, or `PER`.
- `TASK` is an optional but useful family tag such as `SIZE`, `BPA`, `EXT`, `REP`, `DATA`, or `RULE`.
- `NN` is a two-digit sequence within the stage/domain/task family.

Recommended default stage legend:

| Stage | Purpose | Typical contents |
|---|---|---|
| `P0` | Readiness and design gates | assets, data readiness, model/interface smoke, technical PoC, power/precision, frozen specifications |
| `P1` | Data synthesis and empirical comparison | generation, reconstruction, benchmark construction, prompt/size sensitivity, distribution comparison |
| `P2` | Behavioral or external controlled intervention | matched input changes, image edits, counterfactual prompts, specificity and dose controls |
| `P3` | Internal representation or mechanism analysis | probes, representation transfer, activation interventions, mechanistic controls |

Examples:

- `P0-MODEL-01`: model and interface readiness smoke;
- `P1-VIT-SIZE-01`: Vitality generation-size sensitivity;
- `P2-PER-EXT-02`: Perception theme-level external intervention;
- `P3-DIST-REP-01`: Distance Decay representation and internal-intervention chain.

The stage legend is a project contract, not a universal scientific law. If a project uses different stage meanings, define them once and keep them stable. Preserve historical `EXP-3.5` or other identifiers when already established; add an alias/index rather than renaming artifacts in place.

## 3. Experiment package layout

```text
<EXPERIMENT-ID>/
├── README.md                 # one-screen scope and current entry points
├── EXPERIMENT_LOG.md         # factual lifecycle record for this package
├── RESULTS.md                # optional reader-facing result note, derived from analysis
├── inputs/
│   └── <design-version>/
│       ├── spec.json
│       ├── analysis_contract.json
│       ├── attempt_plan.csv|json
│       ├── prompts/ or prompt files
│       └── input_freeze_manifest.json
├── code/
│   ├── build_design.*
│   ├── run_formal.*
│   ├── analyze_formal.*
│   ├── audit_completion.*
│   └── plot_*.*              # when the figure belongs to this package
├── outputs/
│   └── <run-version>/
│       ├── attempts/ or attempt_ledger.jsonl
│       ├── canonical_responses.jsonl or immutable raw artifacts
│       ├── failure_ledger.csv|json|md
│       └── run_manifest.json
├── analysis/
│   └── <analysis-version>/
│       ├── unit_estimands.csv
│       ├── summary.csv|json
│       ├── source tables and QC tables
│       └── completion_audit.json
└── ops/                      # optional launch, resume, scheduler, and watcher scripts
```

Names may vary with modality, but responsibilities should not. For images, `outputs` may contain an image manifest and hashes rather than `canonical_responses.jsonl`. For hidden-state experiments, inputs should include direction metadata and discovery/confirmation splits. Do not manufacture empty directories merely to resemble the template.

A project-level experiment index may link packages, statuses, and primary artifacts. It should not duplicate each package's full factual record.

## 4. Freeze contract

Before the first formal output, freeze and version:

- scientific question, hypothesis, allowed and forbidden claims;
- baseline, conditions, changed variables, controls, and sampling unit;
- registered denominator, split rule, exclusions, missing-data handling, and retry policy;
- model/route requirements, prompts, schemas, parameters, and parsing rules;
- primary estimand, uncertainty method, multiplicity family, and sensitivity analyses;
- code and input hashes needed to establish pre-output provenance.

Use fixture or pilot outputs only for technical validation or predeclared precision estimation. Do not merge them into the formal denominator.

Scientific design changes after formal output require a new design version or experiment package. A compatibility fix that does not change mathematical operations may be a versioned technical amendment; record its scope and verify no formal unit ran before the amended gate passed.

## 5. Append-only execution

- Assign every Attempt ID before execution.
- Preserve successful responses and failures as immutable records.
- On resume, skip every Attempt ID that already has a terminal record.
- Distinguish an uncalled attempt from a called failure.
- Stop safely when credentials, quota, model receipts, schemas, or technical gates do not meet the contract.
- Keep provider, network, copying, parsing, and executor failures; do not select outputs by visual quality or result direction.
- Record whether retries are forbidden, technical-only, or predeclared. Never retry a successful attempt merely to obtain a more favorable result.

The run manifest should state the fixed denominator, terminal records, successful outputs, retained failures, uncalled attempts, route/model evidence, start/end time, and current procedural status.

## 6. Analysis and completion audit

Analysis should be reproducible from frozen inputs and immutable outputs. Keep unit-level estimands separate from summaries. Store the table used by each figure or manuscript number as a versioned source table.

Before marking a package procedurally complete, verify:

- every registered Attempt ID is accounted for;
- no unknown, duplicate, missing, orphaned, or path-mismatched artifact exists;
- hashes or byte-level identities match the manifest where required;
- the intended statistical unit, fixed denominator, exclusions, and sensitivity populations were used;
- all technical failures remain in the ledger;
- analysis code and result files are versioned and present;
- the completion audit reports checks individually rather than only returning `complete`.

## 7. Three status axes

Record three axes separately:

| Axis | Example values |
|---|---|
| Procedural | `planned`, `frozen`, `running`, `provider_limit_stop`, `registered_calls_complete_outputs_incomplete`, `complete`, `failed` |
| Evidentiary | `not_analyzed`, `supports`, `partly_supports`, `mixed`, `null`, `contradicts`, `inconclusive` |
| Claim eligibility | `main_text`, `SI`, `diagnostic`, `pilot_only`, `no_claim` |

Use exact compound procedural states when a single word would hide an important distinction. For example, all calls may be terminal while some registered outputs are missing; this is not the same as a complete output set.

## 8. Version and file naming

- Prefer `formal_v01`, `formal_gpt4o_v01`, `readout_v01`, and `figure_v01`.
- Use zero-padded replicate identifiers such as `R001`.
- Encode condition and sampling unit in Attempt IDs when useful, for example `VIT-SIZE-N050-R006`.
- Keep timestamps in manifests and logs, not as substitutes for semantic versions.
- Avoid `final`, `latest`, `new`, `new2`, `fixed`, and silent overwrite.
- When correcting a frozen artifact, create a new version and retain the replaced version with a clear status.
