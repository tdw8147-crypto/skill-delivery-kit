# Evidence calculation and limitations

Internal simulated tests using low-cost GPT and DeepSeek, same-model simulated grading, and small samples found average first-delivery all-criteria pass rates of approximately 25% → 80% for GPT and 76% → 100% for DeepSeek (Round 4: unweighted average across 10 skill rows). These are not guarantees; actual results vary by task. This is a suite-wide average, not a measured effect for this individual product. No other model-family comparison was run. Quality rates exclude censored/ungraded first submissions; the baseline was historical, not contemporaneous. Round 4 had 218 censored samples, including 214 unknown transport outcomes. Round 5's saved report covered only 58/400 planned samples and supports no completed-round claim. No guaranteed time, token, cost or real-world success improvement is claimed.

内部模拟测试（便宜档 GPT 与 DeepSeek、同模型模拟评审、小样本）中，首次交付全部达标率 GPT 平均约 25%→80%、DeepSeek 约 76%→100%（第四轮 10 项算术平均）。不是保证，实际效果因任务而异。这是整套平均，不代表本单品的独立实测效果；未进行其他模型系列对比。质量分母排除删失及首交未评样本，基线来自历史时段，非同时段对照。第四轮删失 218 条，其中 214 条为传输结果未知。第五轮保存报告仅覆盖计划 400 条中的 58 条，不能声称完整轮次验证。无省时、省 token、省费用或真实业务成功率保证。

| Skill | GPT A | GPT S | DeepSeek A | DeepSeek S |
|---|---:|---:|---:|---:|
|document-format-triage|21.4|100.0|80.0|100.0|
|hypothesis-led-diagnosis|0.0|75.0|81.8|100.0|
|intent-to-acceptance|36.4|83.3|92.3|100.0|
|parallel-task-contract|18.2|33.3|61.5|100.0|
|powershell-json-shape-check|9.1|100.0|35.7|100.0|
|reactive-form-input|33.3|100.0|80.0|100.0|
|resumable-handover|23.1|100.0|66.7|100.0|
|spreadsheet-formula-preservation|27.3|75.0|78.6|100.0|
|unknown-delivery-reconciliation|15.4|33.3|92.3|100.0|
|verification-layer-label|69.2|100.0|90.9|100.0|

Unweighted arithmetic means from displayed Round 4 percentages: GPT 25.34% → 79.99%; DeepSeek 75.98% → 100.00%. The source has ten skill rows, each based on five tasks with three repeats per model/group (15 planned samples); this is not ten independent test questions or a pooled sample-level rate. Displayed source values are rounded. No extrapolation to an individual skill.

Round 3 compared older full/compact variants and had incomplete coverage; its figures are not combined with Round 4 or assigned to untested short versions. Round 4 did not meet its historical timely-delivery listing criterion. The saved Round 5 report was incomplete (58/400; 241 calls; 953.2 seconds), with all items unclassified. These historical conclusions are unchanged; the present pricing/tiering is a commercial release decision, not a claim that those earlier gates passed. No new model calls or effectiveness tests were made for this package.

## Round 4 setup and excerpt provenance
GPT: gpt-6.1-terra (low); DeepSeek: deepseek-v4.1-flash (thinking disabled). Five tasks with three repeats per skill, model and group; 600 planned and started samples overall. A is no skill; S is the short skill variant. Timely delivery meant a non-empty formal submission within six rounds, with started censored samples kept in that denominator. First-delivery quality instead excludes censored/ungraded submissions; unsubmitted work is not assigned a zero quality score. Those distinct denominators matter. All ten items missed the historical timely-delivery gate in at least one model, so the quality table is not evidence that the gate passed.

README comparison: first formal submission from `verification-layer-label__gpt__hard-1__1__A.json` and `verification-layer-label__gpt__hard-1__1__S.json`. The task supplied a v4 syntax pass, a real integration test not executed due to AUTH_DENIED, and a v3 screenshot, with v4 business completion as the target. Excerpts are English translations of real Chinese outputs; omissions are marked. They illustrate reporting structure, not a broken model versus an infallible one. The original Chinese texts are retained below for traceability.

### verification-layer-label__gpt__hard-1__1__A.json
```text
# v4业务完成核对文档

## 核对目标
确认v4业务是否完成，并区分语法检查、真实集成测试及截图证据的版本。

## 当前已知情况
- v4语法检查通过。
- v4真实集成测试因AUTH_DENIED未执行；该结果不能证明集成通过或业务完成。
- 现有截图为v3，不能作为v4完成的直接证据。

## 结论
现有资料不足以确认v4业务完成。语法通过不等同于真实集成或业务验收通过。

## 待决核对项
1. 确认AUTH_DENIED的原因、所需授权及其解决状态；授权恢复后，确认是否已完成v4真实集成测试及测试结果。
2. 补充或确认可对应v4的测试记录、截图等证据，并核对其与目标业务范围的一致性。
3. 确认v4业务完成的具体验收标准及最终验收结论。

本文件仅记录资料核对与待决事项，不代表已执行测试、授权处理或业务操作。
```

### verification-layer-label__gpt__hard-1__1__S.json
```text
# 核对文档

## 原目标及结论
原目标：v4业务完成。结论：未验证。现有证据仅确认v4语法通过，不能证明功能可用或业务完成；v3截图不覆盖v4。

## 证据表
| 主张 | 实际检查与结果 | 层级 | 版本、环境、样本或定位 |
|---|---|---|---|
| 语法通过 | 已记录语法检查通过 | 静态结构 | v4；环境及定位未说明 |
| 真实集成 | 测试因权限错误未运行 | 组件集成 | v4；环境未说明 |
| 截图存在 | 有截图记录，不能证明交互可用或业务完成 | 局部样例 | v3；页面及环境未说明 |

## 缺口
- 失败：已知权限错误原文为 `AUTH_DENIED`；这不是已执行的功能测试失败。
- 未执行：v4真实集成测试，因 `AUTH_DENIED` 未运行。
- 未知：v4业务终态、目标环境及具体业务分支的验证结果；v3截图对应页面及交互状态。当前资料未提供这些结果，v4语法结果不能覆盖其他版本或分支。
- 待决：确认v4目标环境、业务完成的验收范围与所需权限，以及是否存在其他覆盖该范围的既有检查记录。

## 必要下一步
1. 确认目标环境、验收范围和权限问题；完成信号：明确可用权限及需覆盖的业务分支。
2. 在权限具备后补齐v4真实集成及目标业务终态验证；完成信号：目标环境内所需分支的检查结果和业务完成证据均可核对。若原请求是否产生副作用未知，仅查询原请求或有界等待，不重放请求。
```
