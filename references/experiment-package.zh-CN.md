# 实验编号与实验包合同

本合同用于新的实验家族。项目已有明确合同时，保留既有规则并记录偏离，不得静默替换。

## 四类标识必须分开

1. **Experiment ID**：标识一个科学问题与设计家族；续跑和分析修订不改变该编号。
2. **Design version**：标识冻结的输入、提示词、Schema、估计量和分析规则，如 `formal_v01`。
3. **Attempt ID**：标识一个预先登记的采样/评测单位、条件和重复。
4. **Run / analysis version**：标识一次具体执行路线和一次具体读出，如 `formal_gpt4o_v01` 与 `formal_v01`。

Experiment ID 中不要写模型名、seed、时间戳、完成状态或 `final`、`latest`。这些属于执行或版本，不属于科学问题。

## Stage–domain–task 编号

新的分阶段研究计划优先使用：

```text
P<stage>-<DOMAIN>-<TASK>-<NN>
```

- `P<stage>`：项目阶段。
- `DOMAIN`：稳定的大写主题标签，如 `MODEL`、`SCL`、`DIST`、`VIT`、`PER`。
- `TASK`：可选但推荐的实验家族标签，如 `SIZE`、`BPA`、`EXT`、`REP`、`DATA`、`RULE`。
- `NN`：该阶段/主题/任务内两位序号。

| 阶段 | 目的 | 常见内容 |
|---|---|---|
| `P0` | 准备与设计闸门 | 数据/素材准备、模型与接口smoke、技术PoC、功效/精度、冻结规范 |
| `P1` | 数据合成与实证比较 | 生成、关系重建、benchmark、提示词/规模敏感性、分布比较 |
| `P2` | 行为层或模型外部受控干预 | 匹配输入改变、图像编辑、反事实提示、特异性和剂量控制 |
| `P3` | 内部表征与机制分析 | probe、表征迁移、激活干预和机制控制 |

示例：`P0-MODEL-01`、`P1-VIT-SIZE-01`、`P2-PER-EXT-02`、`P3-DIST-REP-01`。

阶段定义是项目合同，不是普遍科学规律。已有 `EXP-3.5` 等编号时保留历史编号，用别名或索引衔接，不在原位批量改名。

## 实验包结构

```text
<EXPERIMENT-ID>/
├── README.md                 # 一屏范围与当前入口
├── EXPERIMENT_LOG.md         # 包级事实记录
├── RESULTS.md                # 可选读者结果说明，由分析派生
├── inputs/<design-version>/
│   ├── spec.json
│   ├── analysis_contract.json
│   ├── attempt_plan.csv|json
│   ├── prompts/
│   └── input_freeze_manifest.json
├── code/
│   ├── build_design.*
│   ├── run_formal.*
│   ├── analyze_formal.*
│   ├── audit_completion.*
│   └── plot_*.*
├── outputs/<run-version>/
│   ├── attempts/ 或 attempt_ledger.jsonl
│   ├── canonical_responses.jsonl 或不可变原始产物
│   ├── failure_ledger.csv|json|md
│   └── run_manifest.json
├── analysis/<analysis-version>/
│   ├── unit_estimands.csv
│   ├── summary.csv|json
│   ├── source tables 与 QC tables
│   └── completion_audit.json
└── ops/                      # 可选启动、续跑、调度和watcher脚本
```

文件名可随模态变化，但职责不变。图片实验可用image manifest和哈希，hidden-state实验应保存方向元数据与发现/确认切分。不要为模仿模板而制造空目录。

## 冻结合同

第一次正式输出前冻结并版本化：

- 科学问题、假设、允许和禁止的主张；
- 基线、条件、改变变量、控制和采样单位；
- 登记分母、切分、排除、缺失处理和重试规则；
- 模型/路线要求、提示词、Schema、参数和解析规则；
- 主要估计量、不确定性、多重比较族和敏感性分析；
- 建立前置来源所需的代码与输入哈希。

fixture/pilot只用于技术验证或预设精度估计，不并入正式分母。正式输出后改变科学设计需要新design version或新实验包；不改变数学操作的兼容修正可作为技术amendment，但要记录范围，并验证修正闸门前是否已有正式单元运行。

## 只增不改的执行

- 运行前分配全部Attempt ID。
- 成功响应和失败均作为不可变记录保存。
- 续跑时跳过已有终态记录，只处理真正未完成的Attempt ID。
- 区分未调用与已调用失败。
- 凭据、额度、模型receipt、Schema或技术闸门不符合合同时安全停止。
- 保存provider、网络、复制、解析和执行器失败；不得根据结果方向或观感选取输出。
- 明确重试是禁止、仅技术失败，还是按预设规则允许；成功尝试不得为获取更有利结果而重试。

运行清单应记录固定分母、终态记录、成功输出、保留失败、未调用项、路线/模型证据、开始结束时间和程序状态。

## 分析与完成审计

分析必须可由冻结输入和不可变输出重现。单位级估计量与汇总分开；每个图或论文数字对应的表应作为版本化source table保存。

标记程序完成前核对：

- 每个登记Attempt ID均有交代；
- 不存在未知、重复、缺失、孤立或路径不匹配产物；
- 需要时哈希或字节身份与清单一致；
- 使用了预定统计单位、固定分母、排除和敏感性人群；
- 所有技术失败仍在账本中；
- 分析代码和结果文件已版本化并存在；
- 完成审计逐项报告检查，而非只返回 `complete`。

## 三条状态轴

| 轴 | 示例 |
|---|---|
| 程序状态 | `planned`、`frozen`、`running`、`provider_limit_stop`、`registered_calls_complete_outputs_incomplete`、`complete`、`failed` |
| 证据结果 | `not_analyzed`、`supports`、`partly_supports`、`mixed`、`null`、`contradicts`、`inconclusive` |
| 主张资格 | `main_text`、`SI`、`diagnostic`、`pilot_only`、`no_claim` |

单个词会掩盖重要区别时使用复合程序状态。例如调用均终态但部分登记输出缺失，不等于完整输出集。

## 版本和命名

- 优先使用 `formal_v01`、`formal_gpt4o_v01`、`readout_v01`、`figure_v01`。
- 重复使用补零编号，如 `R001`。
- Attempt ID可编码条件和单位，如 `VIT-SIZE-N050-R006`。
- 时间戳放在清单和日志中，不替代语义版本。
- 避免 `final`、`latest`、`new`、`new2`、`fixed` 和静默覆盖。
- 修正冻结产物时创建新版本，并保留被替代版本及状态。
