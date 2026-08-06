# 数据与模型版本

实验生成训练、测试、标注、预测或模型产物时使用。

## Version README合同

每个可消费版本应回答：

1. 用途与状态是什么？
2. 哪些Run、输入版本、代码、Prompt/规则、模型和标签流程产生它？
3. 哪些记录被纳入、排除、修复、去重或回退？
4. 每个输出字段含义是什么？Schema不直观时给一个紧凑例子。
5. case、version、unit、label/issue、pair和row各有多少？单位分开报告。
6. train/validation/test如何创建或保留？
7. 检查了哪些泄漏键：case ID、group ID、精确输入hash、近重复键或其他项目单位？
8. 附带哪些验证、汇总、manifest和checksum？
9. 下游应读取哪些文件，哪些只用于分析？
10. 替代哪个旧版本，实质变化是什么？

创建版本时使用 [DATA_VERSION_TEMPLATE.zh-CN.md](../assets/DATA_VERSION_TEMPLATE.zh-CN.md)。

## 身份与血缘

- 不覆盖既有Version；Schema、标签、清洗、切分、Prompt或选择改变均产生新版本。
- 研究问题无需重采样时保留原切分；新切分必须说明理由。
- 可能用于后续复核的排除、未决或部分记录另存，并保留排除原因。
- manifest把每个训练/评测行映射到源unit、case/version、split、label provenance和pair metadata。
- 用于生成标签的Prompt快照与嵌入训练样本的Prompt若用途不同，应分开保存。

## 标签质量与数量守恒

区分确定性转换、单人复核、多评审投票、仲裁标签、模型代理Gold和human Gold；不得无来源地合并成一个“GT”。层级或部分标签应记录发布深度，不为保留数据量而把部分标签导出为完整target。

至少验证：

```text
source_total = included_total + excluded_total
total_rows = train_rows + validation_rows + test_rows
```

一个unit可含多个label时，同时报告受影响unit与label instance；paired data报告完整pair、破损pair及pair是否跨split。

## 模型产物身份

训练模型记录base model、训练数据版本/hash、训练Prompt/Schema、job ID、checkpoint/global step、endpoint、训练配置和评测数据版本；易读模型名不足以唯一定位。
