# unknown-delivery-reconciliation

Reconcile the original submission before treating a timeout as non-delivery.

**Use cases:** Status reconciliation after message or attachment submission.

**Input → output:** Original submission identifier, target, fingerprint, time and status → reconciliation record.

中文：提交结果不明时先核对原记录，避免把超时当成未发送。
适用：消息或附件提交后的状态核对。

## Installation / 安装
The supplied SKILL.md bodies are in Simplified Chinese; the product documentation is bilingual. Use one relevant skill at a time. These are text workflows, not plugins, automation scripts or model weights. Tool access and the host application's rules remain unchanged.

- **Codex:** copy the entire `<skill-name>` folder into `~/.agents/skills/` (user scope) or `.agents/skills/` in your project. Open/reload the session and ask to use the skill by name. If your installed version uses a different skills location, use its documented directory.
- **Claude Code:** copy the entire folder into `~/.claude/skills/` (user scope) or `.claude/skills/` in the project. Reload and invoke `/<skill-name>` or ask for it by name.
- **ChatGPT:** open SKILL.md, copy its full text, and paste it into Custom Instructions. If the field limit is too small, paste the complete text into a new conversation before your task; do not truncate the rules silently. No automatic skill discovery is implied.
- **DeepSeek:** paste the full SKILL.md into the system prompt if your client supports it. Otherwise paste it as the first message of a new chat; this is conversation context, not a platform-level system prompt.

Then provide the task, available evidence and desired deliverable. The skill produces a structured artifact from the supplied context; it does not itself repair systems, edit workbooks, send messages or submit business forms. Remove its folder or pasted instructions to uninstall.

中文：Codex 放入用户级 `~/.agents/skills/` 或项目 `.agents/skills/`；Claude Code 放入 `~/.claude/skills/` 或项目 `.claude/skills/`，重开会话并按名称调用。ChatGPT 将全文粘贴到自定义指令，超出长度时改为新对话首条完整粘贴；DeepSeek 使用支持系统提示的客户端，否则在新会话首条粘贴。一次选一个相关技能，附任务与已有资料。技能正文为中文，产出结构化文档，不自动执行情境中的业务动作。客户端目录可能随版本变化，请以所装版本文档为准。

## Evidence / 效果说明
Internal simulated tests using low-cost GPT and DeepSeek, same-model simulated grading, and small samples found average first-delivery all-criteria pass rates of approximately 25% → 80% for GPT and 76% → 100% for DeepSeek (Round 4: unweighted average across 10 skill rows). These are not guarantees; actual results vary by task. This is a suite-wide average, not a measured effect for this individual product. No Claude comparison was run. Quality rates exclude censored/ungraded first submissions; the baseline was historical, not contemporaneous. Round 4 had 218 censored samples, including 214 unknown transport outcomes. Round 5's saved report covered only 58/400 planned samples and supports no completed-round claim. No guaranteed time, token, cost or real-world success improvement is claimed.

内部模拟测试（便宜档 GPT 与 DeepSeek、同模型模拟评审、小样本）中，首次交付全部达标率 GPT 平均约 25%→80%、DeepSeek 约 76%→100%（第四轮 10 项算术平均）。不是保证，实际效果因任务而异。这是整套平均，不代表本单品的独立实测效果；未进行 Claude 对比。质量分母排除删失及首交未评样本，基线来自历史时段，非同时段对照。第四轮删失 218 条，其中 214 条为传输结果未知。第五轮保存报告仅覆盖计划 400 条中的 58 条，不能声称完整轮次验证。无省时、省 token、省费用或真实业务成功率保证。

License: MIT. See LICENSE.
