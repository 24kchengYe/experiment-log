# Guide / research-narrative mode

The Guide helps a reader understand the study without reading every package or execution ledger. It is derived from the Record, not a second source of truth. It should read like a concise map of the eventual main text and SI, not like a project diary.

## Recommended structure

1. Research objective and overall answer
2. Data sources, empirical references, and unit definitions
3. Experiment framework and the paths compared
4. Findings grouped by research question
5. Retained interpretation and method
6. Evidence boundaries and unresolved questions
7. SI experiments, sensitivity analyses, and traceability index

## Finding structure

Use the smallest structure that makes the comparison interpretable. A repeated label block is optional, not mandatory. A common pattern is:

```markdown
### {Research question or scoped result}

{What was generated, compared, or changed; the baseline and alternative path; and the statistical unit.}

| Indicator | Definition and unit | Empirical reference or baseline | Alternative or treatment |
|---|---|---|---|
| ... | ... | ... | ... |

{One concise conclusion stating what changed or was learned. Add a scope boundary only if it changes interpretation.}
```

Adapt the columns to the study. For generation experiments, a useful sequence is: what was generated; baseline prompt logic; complete conditioning/blueprint logic; result table; conclusion. Put component ablations and alternative settings in the SI section unless they are central to the main answer. For interventions, state the manipulated condition, comparison, outcome, and estimand in parallel language across benchmarks.

## Narrative rules

- Open with the research objective and overall answer only when they help orient the reader; do not add a ceremonial overview paragraph that merely repeats the table of contents.
- Lead each section with the result or comparison the reader needs, then give only the method needed to interpret it.
- Organize by question and evidence chain, not by a diary of tool calls.
- Explain why an experiment existed only when that rationale helps interpret its evidence.
- Include negative evidence when it changes the retained design.
- Preserve meaningful tensions; do not force inconsistent experiments into one conclusion.
- Distinguish a measured result from a proposed explanation.
- Define every metric, parameter, and physical unit at first use, then reuse one stable, readable name. Do not leave conclusions in parameter shorthand that a domain reader cannot interpret.
- Name the dataset, Gold/reference-label protocol, and tested method separately. When several datasets share one Gold protocol, state the common protocol once and distinguish datasets by source, sampling, size, or purpose.
- Before comparing absolute metrics across datasets, explain their composition and purpose. Do not narrate cross-dataset differences as chronological method improvement or regression.
- Keep paths and operational commands in the Log; the Guide links to them.
- Omit routine execution counts such as HTTP 200 totals when they do not affect the denominator, missingness, or claim boundary.
- Avoid work-log prose, ceremonial transitions, generic “future work,” unsupported novelty claims, and meta-commentary such as “本轮”, “为与原文对齐”, or statements about what the team chose not to do.
- Do not end with empty statements such as “the complete estimates jointly characterize the relationship.” State the observable pattern, comparison, and implication.
- Use evidence-strength labels only where the status is genuinely unclear or decision-relevant. Repeating `Strength`, `Meaning`, and `Boundary` after every result creates defensive boilerplate.
- A result table should expose missing empirical-reference or complete-treatment columns instead of hiding them in prose.

## What belongs where

| Content | Log | Guide |
|---|---:|---:|
| Commands, endpoints, configs, raw paths | Full | Usually omit; link through traceability index |
| Every run, including failures | Full | Only decision-relevant failures |
| Full metric tables | Full | Decision-relevant subset |
| Research story and retained design | Traceable notes | Primary |
| Open contradictions | Full evidence | Concise explanation |
| Next tasks | Exact experiment plan | Prioritized unresolved question or SI experiment |
