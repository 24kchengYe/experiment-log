# 从实验提炼技能

重复实验流程需要沉淀为可复用技能时使用。

## 提炼闸门

多数条件成立时才创建技能：流程已执行多次或重建成本高；输入、输出、成功和失败状态足够稳定；至少一项实验验证主路径，已知失败确实改变流程；已有可复用脚本/Prompt/Schema/patch/template；流程能服务于日期Run之外的未来任务。

一次性分析、不稳定候选Rubric、未验证脚本或没有可执行流程的叙事结论，不应过早包装为技能。

## 提炼流程

1. **选择单一能力**：以用户任务命名，写真实触发语和非目标。
2. **收集证据锚点**：链接验证过的Experiment ID、固定数据、预期输出、失败case和环境约束；它们是回归锚点，不是普遍性能主张。
3. **区分稳定流程与实验常量**：稳定流程进 `SKILL.md`、scripts和references；dataset ID、endpoint、commit、threshold和profile进版本化config或verified-experiment reference。
4. **提升规范入口**：把可复用逻辑移出日期Run；技能不依赖历史工作目录。复用维护中的项目代码时固定版本/commit并记录patch。
5. **渐进披露打包**：`SKILL.md`保存路由和必需工作流，`references/`保存合同与变体，`scripts/`保存确定性重复操作，`assets/`保存模板/fixture/patch，`agents/openai.yaml`保存人类可见元数据。
6. **安全外置配置**：只提交example config，不提交API key、session、token或私密凭据；定义环境变量名和preflight。
7. **验证**：主路径有smoke/self-test；测试缺失输入、续跑、Schema和路径发现；适用时用未参与写规则的产物做forward test。
8. **建立所有权与同步**：明确唯一源目录/仓库，以及项目镜像和GitHub的同步方式。

## 技能证据记录

行为依赖实证锚点时维护 `references/verified-experiments.md`，记录输入版本、环境、命令/profile、输出、结果、已知不匹配和源产物。新实验改变稳定流程时，先更新Experiment Log，再更新技能、测试和证据引用；不能只因偏好某种故事就修改技能。

## 停用与替代

只有替代技能覆盖原触发范围、必需工作流、assets和验证后才停用旧技能。优先保留deprecation pointer并移出活跃技能根目录，便于其他设备迁移和恢复。
