# 评测与比较报告

用于模型评测、消融、评分稳定性、标签审计和根因分析。

## 定义评测合同

结果前说明：评测单位与样本数、正类及clean/problem/pass/fail语义、GT来源与复核状态、模型/checkpoint/endpoint、System/User Prompt与输入Schema、解码配置、评测代码、数据是否用于开发，以及哪些因素固定、哪些改变。

指标首次出现时定义。Accuracy、pass rate、issue presence、verdict、category、exact set match、Jaccard、Precision、Recall和F1不可互换。

## 可比不等于相同

- 相同输入ID不代表相同GT。
- 相同GT不代表相同Prompt或输出Schema。
- 相同指标名不代表相同正类、单位、平均方式或分母。
- 公共交集只支持有边界比较，不能替代全量结果。

两种训练/复核方法为同一输入产生不同标签集时，适用时进行2×2评测：两模型分别对两种标签源评测，分开报告对角拟合与跨标签泛化。

## 分层报告

结构化预测只报告适用层级，例如问题存在/clean检测、顶层verdict、category、rubric/class ID、细mode/subtype、单/多标签精确性及reason语义质量。说明数量是unit还是label instance；多标签任务写明micro/macro和exact-set标准。

## 语义复核与根因

字符串或ID精确匹配不足时，建立含input、GT、prediction、judgment和rationale的结构化复核集，事先定义exact、partial/subset、incorrect/conflicting等类别，并保存逐行结果。

- 先分析case证据，再汇总原因；不能仅从指标推断根因。
- 区分标签/Rubric歧义、Reviewer不稳定、Prompt上下文、模型能力、解析/Schema和数据覆盖。
- 主要错误模式提供代表case，并链接完整机器可读复核集。
- 修正GT后再重算指标；归档原标签并命名复核后的GT版本。

## 分享包

可移植评测包包括原始预测、GT/manifest、metrics JSON、config、validation summary、主报告、逐case复核及说明模型—GT对应关系的manifest。HTML只是视图，不能成为唯一产物。
