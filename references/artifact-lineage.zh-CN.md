# 产物布局与血缘

项目含多次Run、派生数据集、提示词、报告或模型输出时使用。

## 区分产物角色

```text
inputs/      不可变源输入
runs/        可重放执行现场和中间状态
versions/    经验证、供下游消费的不可变产物
analysis/    派生解释，不能成为唯一数据源
prompts/     当前源文件及归档/冻结快照
assets/      可编辑视觉源和渲染导出
references/  冻结Rubric、协议、Registry和Schema
skills/      从已验证实验提炼的可复用流程
```

这些是语义角色，不是强制目录名。重组前先把既有项目映射到这些角色。

### Run

Run是执行现场，可以不完整、探索、失败、续跑或被替代。适用时共同保存输入、配置、Prompt快照、中间状态、原始/标准化输出、日志和实验记录。

```text
runs/YYYY-MM-DD_<scope>_<experiment>/
├── EXPERIMENT.md
├── input/ 或冻结输入清单
├── prompt_snapshot/ 或config快照
├── stages/ 或outputs/
├── summary.json
└── validation/integrity report
```

日期前置便于检索；dataset/model/profile只在用于区分时加入。不要因同日运行就把无关实验塞入同一Run。

### Version

Version是由一个或多个Run提升、供下游消费的快照。必须有稳定Schema、血缘、统计、验证和不可变身份；不是每个Run都要提升。

```text
versions/vNN_YYYY-MM-DD_<purpose>_<size>/
├── README.md 或 VERSION.md
├── 下游消费的数据/模型
├── manifest
├── summary
├── validation
├── checksums
└── 需要时的冻结prompt/config
```

发布后不得原位修改Version。

### Analysis

Analysis可汇总多个Run或Version，但数字必须回到机器可读汇总或主要输出。报告不能替代原始预测和清单。

## 事实源规则

- 便捷链接、`active`目录、复制Prompt、渲染图或分享包只是视图，不自动成为事实源。
- 历史复现使用Run的冻结快照或哈希，不用当前active配置反推。
- 同时记录易读版本名与不可变身份：git commit、SHA-256、endpoint/checkpoint或dataset manifest hash。
- 源文件未提交时如实说明，以冻结快照和checksum为准，不虚构commit关联。
- 保存被替代或无效输出，明确状态与替代指针，不静默覆盖或删除证据。

## 命名与提升闸门

推荐命名：Run为 `YYYY-MM-DD_<scope>_<experiment>`，Version为 `vNN_YYYY-MM-DD_<label>`，Analysis为 `YYYY-MM-DD_<topic>.md`。状态可含 `planned`、`running`、`completed`、`failed`、`data_ready`、`superseded`、`invalid`、`archived`。

只有以下信息均明确时才把Run提升为Version：精确输入与转换、输出Schema、纳入/排除/fallback/去重规则、数量守恒、切分与泄漏规则、Prompt/模型/规则身份、验证与checksum、预定下游消费者、产生该版本的Run和代码。
