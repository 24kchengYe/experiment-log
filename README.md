# experiment-log

一个用于维护**同一套实验事实、不同表达视图**的研究文档技能。

它解决的核心问题是：实验的真实记录、面向读者的研究叙事和论文写作需要不同的表达方式，但不能各自形成互相矛盾的“事实”。

能力本质上分为两类：

1. **真实记录**：保存实验事实，目标是可复现、可定位、可审计。
2. **研究叙事**：从事实中组织问题、证据和结论，目标是让读者看懂。

论文写作不是第三套事实，也不是默认模式；它只是“研究叙事”在论文场景下的显式输出形式。

## 中文主规范与英文兼容层

- `SKILL.zh-CN.md` 是当前中文主规范，集中定义 Record、Synthesis、实验包生命周期和证据组织规则。
- `references/*.zh-CN.md` 与 `assets/*.zh-CN.md` 是对应的中文专项规则和模板。
- `SKILL.md` 及未带语言后缀的英文文件作为跨设备兼容层保留；技能触发后会先完整读取中文主规范。双语内容如有差异，以中文主规范为准，并将差异视为需要修复的版本漂移。
- 原 `evidence-forward-paper-writing` 中有价值的贡献主线、claim–evidence map、hostile-review、必要限制和跨论文表面一致性规则，已经并入 Synthesis 与显式出版材料模式。

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

每个实验包中的 `EXPERIMENT_LOG.md` 和机器可读产物共同构成事实源。项目级索引只链接实验包，不复制全部事实。Guide 和 Paper 都必须能追溯到 Experiment ID、分析表或原始产物。

## 默认行为

- 用户说“记录这个实验”：只更新 Record，并报告是否会实质影响 Guide；只有用户要求 `guide`/`sync` 或已授权自动同步时才改 Guide。
- 用户说“整理目前的实验结论”：读取 Log，更新 Guide，不重写事实。
- 用户说“检查实验记录是否矛盾”：审计数字、版本、路径、指标口径和跨文档结论。
- 用户明确说“写论文 / manuscript / paper”：才进入 Paper 模式。

因此，这个技能只有两种工作模式：Record 保存事实，Synthesis 组织证据。论文写作是 Synthesis 的显式输出，不是第三套事实或默认副作用。

## 实验记录覆盖完整生命周期

Record 模式不仅负责补写一段日志，还负责建立和维护实验包：

```text
提出问题 → 分配 Experiment ID → 冻结输入与分析合同
        → fixture / 技术闸门 → append-only 正式执行
        → 失败与恢复保留 → 冻结分析 → 完成审计
        → 判断是否需要更新 Guide
```

正式运行前冻结统计单位、登记分母、条件、排除与重试规则、提示词、模型/路线要求和分析方法。续跑时跳过已有终态记录，只调用未登记完成的 Attempt ID。`complete` 必须同时有可核验产物和完成审计，不能只因为脚本正常退出。

实验状态分为三条轴：

- **Procedural status**：是否按登记协议完成；
- **Evidentiary result**：结果支持、部分支持、混合、零结果、反驳或不确定；
- **Claim eligibility**：可进入正文、SI、诊断记录、仅作 pilot，或不得形成主张。

这样可以避免把“接口额度停止”写成科学失败，也避免把“400次调用完成”写成假设得到支持。

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

### 每个实验都有稳定的 Experiment ID

新建分阶段研究项目时，推荐：

```text
P<stage>-<DOMAIN>-<TASK>-<NN>
```

- `P0`：数据、模型、接口、统计和冻结协议等准备闸门；
- `P1`：数据合成、实证比较和敏感性分析；
- `P2`：行为层或模型外部受控干预；
- `P3`：内部表征与机制分析。

例如 `P0-MODEL-01`、`P1-VIT-SIZE-01`、`P2-PER-EXT-02`、`P3-DIST-REP-01`。Experiment ID 表示科学问题和设计家族；模型、路线、条件、重复、时间和版本放入 Attempt ID、run version 和 analysis version。已有项目继续保留自己的编号，不强制迁移。

### 实验包目录

```text
<EXPERIMENT-ID>/
├── README.md
├── EXPERIMENT_LOG.md
├── inputs/<design-version>/       # spec、analysis contract、attempt plan、freeze manifest
├── code/                          # build、run、analyze、audit、plot
├── outputs/<run-version>/         # immutable attempts、canonical outputs、failure ledger、run manifest
├── analysis/<analysis-version>/   # estimands、summary、source tables、completion audit
└── ops/                           # 可选的启动、续跑和监视脚本
```

图片、文本生成和 hidden-state 实验可以使用不同文件名，但冻结输入、不可变输出、失败账本、分析结果和完成审计这些职责保持不变。

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

一项实验只在自己的 package Log 中完整记录一次，其他位置通过 Experiment ID 引用，避免多个版本互相漂移。

## 多实验项目的产物怎么组织

技能不会强制项目改目录名，但会先区分这些角色：

```text
inputs/      不可变原始输入
runs/        每次实验现场：配置、快照、中间状态、原始输出
versions/    从 Run 提升出的可消费版本，只增不改
analysis/    跨实验分析和读者报告
prompts/     当前源文件与历史冻结快照
assets/      可编辑图源与渲染文件
references/  冻结 Rubric、协议、Registry 和 Schema
skills/      从已验证实验中提炼的可复用流程
```

关键约束：

- `run` 可以失败、暂停或被替代；只有通过来源、Schema、统计、切分、校验和哈希检查后，才提升为 `version`。
- 历史实验使用当时冻结的 Prompt/Config 或哈希复现，不能拿当前 `active/` 入口反推。
- 数据清洗、标签变化、重新切分或输出 Schema 变化都产生新版本，不覆盖旧文件。
- 多阶段 API 链路保留稳定 `call_id`、原始请求/响应、标准化结果、重试账本和断点；成功恢复后也不删除失败记录。
- 测试 ID 相同不代表 GT 相同。标签来源不同的实验需要明确同 GT 比较、交叉比较或 2×2 评测。

数据版本可直接使用 `assets/DATA_VERSION_TEMPLATE.md`；独立 Run 使用 `assets/RUN_EXPERIMENT_TEMPLATE.md`。

## 实验资产如何继续沉淀

```text
冻结的数据、Prompt、Rubric 与分析合同
                    │
                    ▼
           按日期保存的 Runs
                    │
             验证、审计、冻结
                    ▼
            数据/模型 Versions
                    │
           重复验证且流程稳定
                    ▼
              Reusable Skill
```

Rubric 构造属于独立的 Judge Rubric Engineering 能力。`experiment-log` 只记录实验实际使用的 Rubric 版本、Prompt/Registry 路径、Manifest、哈希和迁移状态，不在实验记录内部修改规则。

### 什么时候从实验提取 Skill

一条链路被重复执行、输入输出稳定、失败模式已知，并且有脚本或固定协议时，可以从 Run 中提取成 Skill：

- 把可复用代码移出带日期的 Run，不再依赖历史工作目录；
- 将主流程放进 `SKILL.md`，变体和验证锚点放进 `references/`；
- 将重复操作变成脚本，并增加 smoke/self-test；
- 固定运行时版本和配置合同，但不提交 Key、Session 或 Token；
- 在 `verified-experiments.md` 中保留支撑该技能的实验、数据和已知限制；
- 明确项目内 `data/skills/` 与外部 GitHub 仓库哪一边是唯一源码，以及如何同步。

只有一次运行、规则仍在频繁变化或没有通过验证的流程，不应提前包装成 Skill。

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
/exp-log record   # 设计、冻结或记录一个实验包
/exp-log failure  # 记录失败实验及其建立的约束
/exp-log guide    # 从 Log 更新研究叙事
/exp-log sync     # 先更新 Log，再按影响门槛同步 Guide
/exp-log audit    # 审计溯源、数字、版本和结论
/exp-log extract  # 提取索引、对比表、时间线或摘要
/exp-log paper    # 显式生成论文或审稿回复等出版产物
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
├── SKILL.md                         # 两种工作模式、路由和主工作流
├── SKILL.zh-CN.md                   # 中文主规范
├── references/
│   ├── experiment-package.md       # 编号、目录、冻结、执行、状态和审计
│   ├── experiment-package.zh-CN.md # 中文实验包合同
│   ├── record-mode.md              # 真实记录规则
│   ├── guide-mode.md               # 研究叙事规则
│   ├── paper-mode.md               # 显式论文模式
│   ├── artifact-lineage.md         # Run、Version 与产物血缘
│   ├── dataset-versioning.md       # 数据/模型版本合同
│   ├── evaluation-reporting.md     # 评测、消融与根因分析
│   ├── pipeline-traceability.md    # 多阶段调用、断点与成本
│   ├── rubric-engineering.md       # 兼容入口：转交独立 Rubric Skill
│   ├── skill-extraction.md         # 从实验提取可复用 Skill
│   ├── sync-audit.md               # 同步与审计规则
│   └── *.zh-CN.md                  # 上述各专项规则的中文版本
├── assets/
│   ├── EXPERIMENT_LOG_TEMPLATE.md
│   ├── EXPERIMENT_GUIDE_TEMPLATE.md
│   ├── RUN_EXPERIMENT_TEMPLATE.md
│   ├── DATA_VERSION_TEMPLATE.md
│   ├── EVALUATION_REPORT_TEMPLATE.md
│   ├── RUBRIC_VERSION_TEMPLATE.md  # 兼容入口，不再维护规则模板
│   └── *.zh-CN.md                  # 上述各模板的中文版本
├── scripts/
│   └── validate_experiment_package.py # 只读检查编号、冻结、输出和完成审计
├── tests/
│   └── test_validate_experiment_package.py
├── evals/
│   └── evals.json                   # Record、编号/包结构和 Guide 三类回归场景
└── agents/openai.yaml
```

## License

MIT
