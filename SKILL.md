---
name: exp-log
description: |
  Write and maintain structured experiment logs for ML/scientific research projects.
  Ensures every experiment is recorded with motivation, method (with formulas),
  results (with baseline comparison), analysis, and artifact paths.

  Use this skill when the user mentions:
  - "/exp-log", "/experiment-log", "记录实验", "写实验日志", "experiment log", "实验记录"
  - "记录一下这个实验", "把结果记下来", "log this experiment", "record results"
  - "更新实验日志", "update experiment log", "add to log"
  - "实验失败了记录一下", "log the failure", "记录失败原因"
  - "整理实验记录", "organize experiment log", "重构日志"
  - "从日志里提取论文素材", "extract for paper", "论文素材"

  Also trigger when the user completes a training run, evaluation, or ablation study
  and needs the results systematically recorded.
---

# Experiment Log — Structured Research Experiment Recording

A skill for writing and maintaining ML/scientific experiment logs that serve three purposes:
1. **Daily R&D**: quickly locate what was done, what worked, what failed
2. **Advisor reporting**: extract key progress and decisions for presentations
3. **Paper writing**: directly copy formulas, result tables, and analysis into manuscripts

## Core Principles

### 1. Every experiment gets an EXP-ID

```markdown
### EXP-{section}.{number}: {one-line title}

**Date**: YYYY-MM-DD
**Git**: {commit hash(es)}
**Status**: complete / failed / in_progress / planned

#### Motivation
2-3 sentences: What problem from the previous experiment motivated this one?
What is the hypothesis being tested?

#### Method
- Key formulas (LaTeX, paper-grade precision)
- Algorithm description or pseudocode
- Hyperparameters table
- Diff vs previous version (only list changes, don't repeat)
- **Data**: split method (by city/image/patch?), sizes, version
- **Changed variables**: list EXACTLY what changed vs baseline (single-variable?)
- **Train-test gap**: note if training and inference use different procedures

#### Results
- Quantitative results table (MUST include baseline comparison column)
- **Uncertainty**: mean +/- std, CI, or N runs (single-run results must be flagged)
- **Fair comparison check**: same data, same thresholds, same post-processing?
- Figure/plot paths: `output/figures/xxx.png`
- Bold the key numbers

#### Analysis
- Did results match the hypothesis?
- If failed: root cause, what hypothesis was ruled out, what constraint was established
- **Conclusion strength**: mark each claim as one of:
  - **Established**: supported by controlled experiment + statistical test
  - **Supported**: consistent evidence but missing some controls
  - **Preliminary**: single run, limited data, or confounded variables
  - **Hypothesis**: reasonable guess, needs verification
- Impact on next steps (→ points to next EXP-ID)

#### Artifacts
- Model weights: `model/trained/xxx.pth`
- Output data: `data/xxx/`
- Visualizations: `output/figures/xxx/`
```

### 2. Failed experiments use decision trees, not flat lists

Each failure must explicitly record:

```markdown
- **Excluded hypothesis**: What did this failure disprove?
- **Established constraint**: What must future attempts satisfy?
- **→ Next step**: How this directly led to the next attempt (→ EXP-X.Y.Z)
```

When multiple failures form a chain, add an ASCII decision tree summary:

```
EXP-A failed (reason) ──→ constraint: must do X
    ↓
EXP-B failed (reason) ──→ constraint: must also do Y
    ↓
EXP-C failed (reason) ──→ constraint: must also do Z
    ↓
Conclusion: need approach W ──→ EXP-D
```

### 3. Reference old experiments precisely

Never write "旧方法" or "old model". Always specify:

```markdown
# Bad
Used the old HRNet model results...

# Good
Used HRNet v1 (2025-03, epoch=49, Dice=0.783,
Git: `e3f1a2b`, weights: `model/trained_archive/best_model.pth`)
```

First mention of any model/method requires: **version name + date + key metric + git hash + artifact path**. Subsequent references use the version name only.

### 4. Formulas on first occurrence

Every quantitative metric must have a formula definition on first use:

```markdown
$$\text{jaccard} = \frac{n_{stable}}{n_{hist} + n_{mod} - n_{stable}}$$
```

Later references: "jaccard (defined in §X.Y)"

### 5. Cross-references, not duplication

- Each experiment is detailed in exactly ONE place
- Other sections use `(§EXP-X.Y.Z)` or `(see EXP-X.Y.Z)` to reference
- Summary/index tables (like §9) link to detailed sections, don't repeat content

### 6. Artifact paths are mandatory

Every experiment must list its outputs:

```markdown
#### Artifacts
- Code: `code/05_change_detection/25f_finetune_roma.py`
- Data: `data/07_roma_finetune_change_aware/` (6072 train, 653 val)
- Figures: `output/figures/roma_grid_search/results.csv`
- Weights: `model/trained/roma_finetuned/best.pth`
```

### 7. Section organization

- Organize by **research question**, not by time
- Within a question, experiments are chronologically ordered with EXP-IDs
- A "Conclusions" section contains only cross-question insights
- An "Index" section provides a quick-lookup table with EXP-ID links
- "Engineering/Bug fixes" are separated from research experiments
- "Next steps" section is always kept current

## Commands

### `/experiment-log record`
Record a new experiment. Will prompt for:
- Which section/question it belongs to
- Previous experiment it builds on (for motivation)
- Method, results, analysis

### `/experiment-log failure`
Record a failed experiment with decision tree format.

### `/experiment-log update`
Update an existing experiment's status or add new results.

### `/experiment-log audit`
Scan the experiment log for:
- Missing git hashes
- Vague references ("旧方法", "old model")
- Missing artifact paths
- Experiments without motivation sections
- Duplicated content across sections
- **Missing data split description** (how was train/val/test divided?)
- **Single-run results without uncertainty** (no mean±std, no CI)
- **Multi-variable changes** claimed as single-factor conclusions
- **Conclusions marked as "established" without statistical tests**
- **Proxy metrics** used without linking to end-goal metrics
- **Missing fair comparison conditions** (different thresholds, data, post-processing)
- **Train-test mismatch** not documented (e.g., training uses mask X but inference doesn't)

### `/experiment-log extract`
Extract material for a specific purpose:
- `extract paper §X` — extract formulas + result tables for paper section X
- `extract slides` — extract key findings as bullet points for presentation
- `extract timeline` — generate chronological progress summary

## File Structure

The experiment log is a single markdown file (typically `EXPERIMENT_LOG.md`) at the project root. Structure:

```
# Project Experiment Log
> Author, affiliation, advisor
> Last updated: YYYY-MM-DD

## 1. Project Overview
### 1.1 Research Goal
### 1.2 Core Questions
### 1.3 Solution Narratives (problem → hypothesis → process → references)

## 2-N. Experiments by Research Question
### EXP-X.Y.Z: Title
(following the template above)

## N+1. Conclusions (cross-question insights only)

## N+2. Engineering & Bug Fixes (non-research)

## N+3. Next Steps (always current)

## N+4. Experiment Index (quick-lookup table → EXP-IDs)

## Appendices
### A. Code Index
### B. Model Weights
### C. Data Paths
### D. Output Paths
### E. References
```

## Anti-patterns to Avoid

1. **Flat chronological log**: "April 15: tried X. April 16: tried Y." — No structure, no decision logic.
2. **Results without analysis**: Tables of numbers without explaining what they mean or what to do next.
3. **Vague references**: "the old model", "previous results", "as before" — uninterpretable after 2 weeks.
4. **Duplicate content**: Same experiment described in both §5 and §7 — creates inconsistency.
5. **Missing motivation**: Jumping straight to method without explaining WHY this experiment was attempted.
6. **Prose-only failures**: "It didn't work because X" — missing the decision tree (what was excluded, what constraint was learned, what comes next).
7. **Multi-variable changes claimed as single-factor**: Changed data + code + hyperparams simultaneously, then attributed improvement to one factor. Must list ALL changed variables.
8. **Overconfident conclusions from single runs**: "Method A is better" based on 0.008 Dice difference without confidence intervals. Flag single-run results explicitly.
9. **Proxy metrics mistaken for end-goal**: Optimizing Dice/SSIM/right-angle-rate without verifying that the actual research objective (e.g., tracking quality) improved.
10. **Unfair comparisons**: Comparing methods with different thresholds, data splits, post-processing, or evaluation scripts. Every comparison table must state what was held constant.
11. **Test set hacking**: Repeatedly viewing test results and adjusting methods → test set becomes dev set. Note which datasets have been used for development vs final evaluation.
12. **Missing data split description**: Not stating whether train/val/test are split by city, image, or random patch — critical for spatial data where adjacent patches leak information.
