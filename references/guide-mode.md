# Guide / research-narrative mode

The Guide helps a reader understand the project without reading every run. It is derived from the Log, not a second source of truth.

## Recommended structure

1. Objective and decision context
2. Data sources and unit definitions
3. Research framework or pipeline
4. Current data/experiment state
5. Findings grouped by research question
6. Retained method and why it was retained
7. Evidence boundaries, trade-offs, and unresolved questions
8. Current decisions and next experiments
9. Traceability index to `EXP-ID`s and artifacts

## Claim–evidence block

For each important finding, write:

```markdown
### {Scoped finding}

**Evidence**: {metric, numerator/denominator, comparison, EXP-ID or artifact}

**Strength**: Established / Supported / Preliminary / Hypothesis

**Meaning**: {decision enabled by this evidence}
**Boundary**: {where the conclusion may not hold}
```

Prefer “On the fixed 124-unit test set, A improved Category F1 from X to Y” over “A is better than B.”

## Narrative rules

- Lead with the strongest supported result and the decision it enables.
- Organize by question and evidence chain, not by a diary of tool calls.
- Explain why an experiment existed only when that rationale helps interpret its evidence.
- Include negative evidence when it changes the retained design.
- Preserve meaningful tensions; do not force inconsistent experiments into one conclusion.
- Distinguish a measured result from a proposed explanation.
- Define every metric at first use, then reuse one stable name.
- Keep paths and operational commands in the Log; the Guide links to them.
- Avoid work-log prose, ceremonial transitions, generic “future work,” and unsupported novelty claims.

## What belongs where

| Content | Log | Guide |
|---|---:|---:|
| Commands, endpoints, configs, raw paths | Full | Link only |
| Every run, including failures | Full | Only decision-relevant failures |
| Full metric tables | Full | Decision-relevant subset |
| Research story and retained design | Traceable notes | Primary |
| Open contradictions | Full evidence | Concise explanation |
| Next tasks | Exact experiment plan | Prioritized research direction |
