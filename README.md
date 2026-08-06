# experiment-log

A reusable research-documentation skill that keeps several views aligned with one evidence base:

- `EXPERIMENT_LOG.md`: exact, reproducible experiment record and factual source of truth.
- `EXPERIMENT_GUIDE.md`: evidence-backed project guide or research narrative.
- Paper artifacts: publication-oriented writing, only when explicitly requested.

## What it does

The skill preserves `/exp-log` and `/experiment-log` compatibility while adding `guide`, `sync`, `audit`, and explicit `paper` modes. It records:
- **Motivation**: Why was this experiment attempted?
- **Method**: Exact formulas, algorithms, prompts, configs, and changed variables
- **Results**: Quantitative tables with baseline comparison
- **Analysis**: What worked, what failed, decision trees for failures
- **Artifacts**: Code paths, model weights, output data, figures

## Why

The Log and Guide solve different problems. The Log retains paths, versions, failures, counts, and comparison conditions. The Guide helps a reader understand the research question, evidence chain, retained choices, and limitations. Keeping the Log as the source of truth prevents a cleaner narrative from silently changing the evidence.

Paper writing is opt-in. A request to record an experiment or summarize a project does not automatically trigger manuscript-style writing.

## Key features

### EXP-ID format
Every experiment gets a unique ID (`EXP-3.5`, `EXP-5.7.4a`) with standardized sections.

### Decision trees for failures
Failed experiments explicitly record what hypothesis was excluded, what constraint was established, and how it led to the next attempt:

```
Mode A failed (synthetic gap) ──→ constraint: must use real pairs
    ↓
Mode B v1 failed (changed regions) ──→ constraint: must filter changes
    ↓
Conclusion: need change detection first ──→ EXP-5.7.8
```

### Precise references
Never "the old model" — always "HRNet v1 (2025-03, Dice=0.783, Git: `e3f1a2b`)".

### Cross-references, not duplication
Each experiment detailed in one place, referenced elsewhere with `(§EXP-X.Y.Z)`.

## Install

```bash
# Shared agent-skills location
git clone https://github.com/24kchengYe/experiment-log.git ~/.agents/skills/experiment-log

# Codex-only alternative
git clone https://github.com/24kchengYe/experiment-log.git ~/.codex/skills/experiment-log
```

## Usage

In any Claude Code conversation:

```
/exp-log record   # Record a completed experiment
/exp-log failure  # Record a failed experiment and learned constraint
/exp-log guide    # Refresh the reader-facing research narrative
/exp-log sync     # Update the Log, then update the Guide if material
/exp-log audit    # Audit provenance, arithmetic, versions, and claims
/exp-log extract  # Produce an index, table, timeline, or summary
/exp-log paper    # Write a paper artifact; explicit request required
```

Natural-language triggers such as “记录一下这个实验”, “更新实验指南”, and “同步实验记录和结论” are supported.

## License

MIT
