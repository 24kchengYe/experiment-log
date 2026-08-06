# Extracting a skill from experiments

Use this reference when a repeated experimental workflow should become a reusable skill.

## Extraction gate

Create a skill when most of these are true:

- the workflow has been executed more than once or is costly/error-prone to reconstruct;
- inputs, outputs, success criteria, and failure states are stable enough to describe;
- at least one experiment verifies the intended path, and known failures have changed the procedure;
- reusable scripts, prompts, schemas, patches, or templates exist;
- the procedure benefits future work beyond one dated run.

Do not extract a skill from a one-off analysis, an unstable candidate Rubric, an unverified script, or a narrative conclusion with no executable workflow.

## Extraction workflow

1. **Choose one capability**
   - Name the user task, not the project history.
   - Write realistic trigger phrases and non-goals.
2. **Collect evidence anchors**
   - Link verified `EXP-ID`s, fixed datasets, expected outputs, failure cases, and known environment constraints.
   - Treat these as regression anchors, not universal performance claims.
3. **Separate stable procedure from experiment constants**
   - Stable workflow belongs in `SKILL.md`, scripts, and references.
   - Dataset IDs, endpoints, commits, thresholds, and profiles belong in versioned config or verified-experiment references.
4. **Promote canonical entrypoints**
   - Move reusable logic out of dated run directories.
   - The skill must not depend on a historical run's working directory.
   - Reuse maintained project code when appropriate; pin version/commit and document patches.
5. **Package progressive disclosure**
   - `SKILL.md`: routing and required workflow.
   - `references/`: contracts, variants, verified experiments, failure modes.
   - `scripts/`: deterministic repeated operations.
   - `assets/`: templates, fixtures, diagrams, and patches used in output.
   - `agents/openai.yaml`: human-facing metadata and invocation policy.
6. **Externalize configuration safely**
   - Commit example config, never API keys, sessions, tokens, or private credentials.
   - Define environment-variable names and preflight checks.
7. **Validate**
   - Add self-test/smoke test for the main path.
   - Test missing inputs, resume behavior, schema validation, and path discovery where relevant.
   - Forward-test on an artifact not used to write the instructions when possible.
8. **Establish ownership and sync**
   - Choose one canonical source directory or repository.
   - If the skill is mirrored into a project `data/skills/` folder and GitHub, document which side is authoritative and how to sync changes.

## Skill evidence record

Maintain a small `references/verified-experiments.md` when behavior depends on empirical anchors. For each anchor record the input version, environment/runtime, command/profile, output, result, known mismatch, and source artifact.

When a new experiment changes the stable procedure, update the Experiment Log first, then the skill, its tests, and the verified-experiment reference. Do not edit the skill based only on a preferred story.

## Retirement and replacement

Retire an older skill only after the replacement covers its triggers, required workflows, assets, and validation. Prefer a deprecation pointer before archive/delete so other devices and projects can migrate safely.
