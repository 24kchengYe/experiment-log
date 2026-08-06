# experiment-log

一个用于维护**同一套实验事实、不同表达视图**的研究文档技能。

它解决的核心问题是：实验的真实记录、面向读者的研究叙事和论文写作需要不同的表达方式，但不能各自形成互相矛盾的“事实”。

能力本质上分为两类：

1. **真实记录**：保存实验事实，目标是可复现、可定位、可审计。
2. **研究叙事**：从事实中组织问题、证据和结论，目标是让读者看懂。

论文写作不是第三套事实，也不是默认模式；它只是“研究叙事”在论文场景下的显式输出形式。

```text
原始产物（代码、配置、数据、预测、评测报告）
                    │
                    ▼
        EXPERIMENT_LOG.md
        唯一事实底座，可复现、可定位
                    │
                    ▼
        EXPERIMENT_GUIDE.md
        研究问题、证据链与当前结论
                    │
            用户明确要求写论文
                    ▼
            Paper / Manuscript
```

## 三种产物分别解决什么问题

| 产物 | 主要用途 | 保留什么 | 不应该做什么 |
|---|---|---|---|
| `EXPERIMENT_LOG.md` | 真实记录、复现、定位产物 | 每次实验的动机、数据、版本、变量、指标、失败、路径 | 为了故事顺畅而省略矛盾或失败 |
| `EXPERIMENT_GUIDE.md` | 项目指南、研究汇报、阶段性总结 | 研究问题、证据链、当前结论、边界、保留方案 | 复制所有命令和运行流水账 |
| Paper / Manuscript | 论文、摘要、贡献陈述 | 经过选择的贡献叙事、方法、实验和限制 | 在没有明确请求时自动进入论文写作 |

`EXPERIMENT_LOG.md` 是唯一事实源。Guide 和 Paper 都必须能追溯到 Log 中的 `EXP-ID`、指标或原始产物。

## 默认行为

- 用户说“记录这个实验”：先更新 Log；若结论、默认方案或下一步发生实质变化，再同步 Guide。
- 用户说“整理目前的实验结论”：读取 Log，更新 Guide，不重写事实。
- 用户说“检查实验记录是否矛盾”：审计数字、版本、路径、指标口径和跨文档结论。
- 用户明确说“写论文 / manuscript / paper”：才进入 Paper 模式。

因此，这个技能既能写“真实记录”，也能组织“研究故事”；论文写作是显式选择，不是默认副作用。

### `sync` 不是每次都重写 Guide

一次新实验只有在改变以下内容时，才同步修改 Guide：

- 主要结论或证据强度；
- 当前推荐的模型、Prompt、数据集或链路；
- 数据规模、组成、切分或版本；
- 重要限制、取舍或下一步优先级。

如果只是补路径、修日期或增加一个不改变结论的运行，技能只更新 Log，并明确返回 `Guide: no material change`。

## 同一个实验在三种产物中怎么写

假设一次消融实验发现 Split Prompt 没有提升 Category F1：

- **Log**：记录两个模型、两套 Prompt、训练/测试样本数、评测脚本、每项指标、原始预测路径，以及本次同时改变了哪些变量。
- **Guide**：写成“在当前固定测试集上，Split 未显示出相对 Full 的稳定收益，因此暂不作为默认方案”，并链接对应 `EXP-ID`。
- **Paper**：只有用户要求写论文时，才把该结果组织成消融表和方法选择依据；不会把固定测试集结论扩大为普遍规律。

## Log 如何保证可复现

### 每个实验都有 EXP-ID

每个实验使用唯一编号，例如 `EXP-3.5`、`EXP-5.7.4a`。Guide 和 Paper 使用该编号回指事实来源。

### 失败实验也保留决策价值

失败实验需要说明排除了什么假设、建立了什么约束，以及它如何导向下一次实验：

```
Mode A failed (synthetic gap) ──→ constraint: must use real pairs
    ↓
Mode B v1 failed (changed regions) ──→ constraint: must filter changes
    ↓
Conclusion: need change detection first ──→ EXP-5.7.8
```

### 引用必须能定位

不写“旧模型”，而写成“HRNet v1（2025-03，Dice=0.783，Git: `e3f1a2b`，权重路径：…）”。

### 交叉引用，不复制实验

一项实验只在 Log 中完整记录一次，其他位置通过 `EXP-ID` 引用，避免多个版本互相漂移。

## 多实验项目的产物怎么组织

技能不会强制项目改目录名，但会先区分这些角色：

```text
inputs/      不可变原始输入
runs/        每次实验现场：配置、快照、中间状态、原始输出
versions/    从 Run 提升出的可消费版本，只增不改
analysis/    跨实验分析和读者报告
prompts/     当前源文件与历史冻结快照
assets/      可编辑图源与渲染文件
```

关键约束：

- `run` 可以失败、暂停或被替代；只有通过来源、Schema、统计、切分、校验和哈希检查后，才提升为 `version`。
- 历史实验使用当时冻结的 Prompt/Config 或哈希复现，不能拿当前 `active/` 入口反推。
- 数据清洗、标签变化、重新切分或输出 Schema 变化都产生新版本，不覆盖旧文件。
- 多阶段 API 链路保留稳定 `call_id`、原始请求/响应、标准化结果、重试账本和断点；成功恢复后也不删除失败记录。
- 测试 ID 相同不代表 GT 相同。标签来源不同的实验需要明确同 GT 比较、交叉比较或 2×2 评测。

数据版本可直接使用 `assets/DATA_VERSION_TEMPLATE.md`；独立 Run 使用 `assets/RUN_EXPERIMENT_TEMPLATE.md`。

## 安装与更新

```bash
# Claude Code / 多 Agent 共用位置
git clone https://github.com/24kchengYe/experiment-log.git ~/.agents/skills/experiment-log

# 仅供 Codex 使用的位置
git clone https://github.com/24kchengYe/experiment-log.git ~/.codex/skills/experiment-log
```

已经安装时，在技能目录执行：

```bash
git pull
```

## 使用方式

可以直接使用命令：

```
/exp-log record   # 记录一次完成的实验
/exp-log failure  # 记录失败实验及其建立的约束
/exp-log guide    # 从 Log 更新研究叙事
/exp-log sync     # 先更新 Log，再按影响门槛同步 Guide
/exp-log audit    # 审计溯源、数字、版本和结论
/exp-log extract  # 提取索引、对比表、时间线或摘要
/exp-log paper    # 显式进入论文写作模式
```

也可以直接使用自然语言，例如：

- “记录一下刚刚的模型评测，补全数据路径和指标定义。”
- “根据实验记录更新项目实验指南，只改实质变化的结论。”
- “检查训练集、测试集数量和报告里的统计是否一致。”
- “基于 EXP-3.2 和 EXP-3.4 写论文的消融实验小节。”

`/experiment-log` 旧命令仍然兼容。

## 仓库结构

```text
experiment-log/
├── SKILL.md                         # 模式选择与主工作流
├── references/
│   ├── record-mode.md              # 真实记录规则
│   ├── guide-mode.md               # 研究叙事规则
│   ├── paper-mode.md               # 显式论文模式
│   ├── artifact-lineage.md         # Run、Version 与产物血缘
│   ├── dataset-versioning.md       # 数据/模型版本合同
│   ├── evaluation-reporting.md     # 评测、消融与根因分析
│   ├── pipeline-traceability.md    # 多阶段调用、断点与成本
│   └── sync-audit.md               # 同步与审计规则
├── assets/
│   ├── EXPERIMENT_LOG_TEMPLATE.md
│   ├── EXPERIMENT_GUIDE_TEMPLATE.md
│   ├── RUN_EXPERIMENT_TEMPLATE.md
│   ├── DATA_VERSION_TEMPLATE.md
│   └── EVALUATION_REPORT_TEMPLATE.md
└── agents/openai.yaml
```

## License

MIT
