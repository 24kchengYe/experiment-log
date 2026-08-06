# Record 模式

实验包是事实来源。不得为了叙事顺畅而抹平矛盾或隐藏失败尝试。创建包或编号前，先读 [experiment-package.zh-CN.md](experiment-package.zh-CN.md)。

## 必备实验条目

```markdown
### {EXPERIMENT-ID}: {一句话科学问题}

**日期**：YYYY-MM-DD
**程序状态**：planned / frozen / running / stopped / complete / failed
**证据结果**：not_analyzed / supports / partly_supports / mixed / null / contradicts / inconclusive
**主张资格**：main_text / SI / diagnostic / pilot_only / no_claim
**Git / 版本**：{commit、design、dataset、prompt、model receipt、route、analysis}

#### 动机与假设
检验什么、为何现在检验、什么结果支持或反驳假设。

#### 方法与数据
- 基线及全部改变变量
- 数据来源、版本、切分、登记分母和评测单位
- 提示词/模型/配置与公平比较控制
- Attempt ID、缺失、排除和重试规则
- 冻结输入与分析合同版本

#### 执行与完整性
- fixture/技术闸门结果
- called、terminal、successful、failed和uncalled数量
- 续跑/恢复及既有终态记录是否不可变
- 运行清单和失败账本状态

#### 结果
- 指标定义、分子分母、样本量与不确定性
- 比较表、例外、单位级估计量和source table路径

#### 分析
- 观察、解释、替代解释、证据强度、决策和下一Experiment ID

#### 产物
- 代码、冻结输入、提示词、数据、模型/路线证据、原始输出、账本、分析、完成审计、source table和图
```

## 生命周期

1. **Planned**：问题、依赖、拟用编号和未决设计。
2. **Frozen**：正式输出前记录分母、估计量、控制、重试/排除、版本和冻结清单。
3. **Running / stopped**：精确报告called、terminal、remaining；区分额度、凭据、provider、执行器、解析器和科学失败。
4. **Complete**：链接分析与完成审计，分开报告三条状态轴。
5. **Amended**：说明科学变化或技术修正、版本替代关系及受影响正式单元。

## 精确规则

- 有条件时记录路径、提示词版本、模型/端点ID或receipt、哈希和时间戳；长命令放入日志或 `ops/`。
- 术语首次出现时定义，计数单位不得混用。
- 写明精确基线和全部改变变量；多变量实验不能伪装成单因素消融。
- 说明训练/测试Schema、测试集复用和标签复核情况。
- 区分模型预测、历史Judge、规则映射、Agent复核及human/strong-model Gold。
- 使用代理指标时说明与最终目标的关系。
- 区分Run和提升后的Version；同一ID更换标签时明确label/GT version。
- 保存 `superseded`、`invalid`、部分完成、恢复及是否重做既有终态。
- HTTP响应含内容不等于数据有效，须经解析与Schema检查。
- provider额度停止不是科学失败；固定分母未核对时不得称为正式分析，除非预设中期分析。

## 失败实验与组织

失败另记录影响范围、排除假设、建立约束、未决解释和下一Experiment ID。每个实验只在一个包中详细记录，项目registry只做索引；工程修复与科学结论分开，复杂计数旁保留机器可读汇总。
