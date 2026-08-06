# 多阶段管线可追溯性

实验反复调用模型/工具、支持重试/续跑，或通过多阶段生成标签时使用。

## 阶段合同

每阶段记录：目的及允许输入/输出、精确Prompt/config/Schema/model身份、每个逻辑调用的确定性ID、原始请求和响应、经parser/Schema/Registry验证后的标准化结果、attempt number、error、retry decision、usage、latency、timestamp及checkpoint/completion state。

不得保存隐藏chain-of-thought；保存复现所需的可审计事实、选定证据、结构化决策和外显推理摘要。

## 原始与标准化结果

不得用修正结果覆盖原始响应。标准化和修复动作另存。确定性修复可调整格式或重算派生字段，但不能静默改变模型实质标签。

## 重试与续跑

- 各attempt沿用稳定call_id或task ID。
- 根据缺失或无效逻辑调用续跑，不重做完整阶段。
- 记录timeout、output budget等重试参数变化。
- 成功恢复后仍保留历史error ledger。
- 发布前审计缺失调用、重复canonical结果、ID错配、非法标签和未完成阶段。

## 分层发布

管线若可把不同样本解析到不同深度，为每个unit记录release state，如complete、coarse-only、presence-only、unresolved；下游导出必须显式选择兼容状态。

## 成本与效率

至少报告各阶段成功/尝试调用、每input unit调用数、可得时的输入/输出/总token、wall-clock、有效并发、重试与恢复失败、价格假设和成本估计、覆盖或发布率。效率优化只有在相同输入与reference下比较质量才算验证；对已保存调用的反事实重放只能证明预计成本，不能证明held-out质量。

## 最终完整性审计

完成前核对输入守恒、阶段完整性、Prompt/config hash、Schema有效性、唯一ID、合法label registry、release counts、排除记录和checksum覆盖，并从实验记录链接审计。
