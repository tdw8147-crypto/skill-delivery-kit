# Skill Delivery Kit

Help ChatGPT/Codex and DeepSeek deliver directly, more like Claude, with fewer unnecessary follow-up questions and disclaimers.

Ten compact text skills turn existing context into concrete handovers, specifications, diagnosis cards and evidence-bounded reports. They preserve necessary questions and accurate limits. The supplied skill bodies are in Chinese; this README is bilingual.

## Free, complete samples (MIT)
- [resumable-handover](./resumable-handover/SKILL.md) — Turn task state into a checkpoint someone can resume directly.
- [unknown-delivery-reconciliation](./unknown-delivery-reconciliation/SKILL.md) — Reconcile the original submission before treating a timeout as non-delivery.
- [reactive-form-input](./reactive-form-input/SKILL.md) — Distinguish a visible field value from form state actually accepted by the application.

These are complete, usable skills, not deliberately weakened trials.

## Installation / 安装
The supplied SKILL.md bodies are in Simplified Chinese; the product documentation is bilingual. Use one relevant skill at a time. These are text workflows, not plugins, automation scripts or model weights. Tool access and the host application's rules remain unchanged.

- **Codex:** copy the entire `<skill-name>` folder into `~/.agents/skills/` (user scope) or `.agents/skills/` in your project. Open/reload the session and ask to use the skill by name. If your installed version uses a different skills location, use its documented directory.
- **Claude Code:** copy the entire folder into `~/.claude/skills/` (user scope) or `.claude/skills/` in the project. Reload and invoke `/<skill-name>` or ask for it by name.
- **ChatGPT:** open SKILL.md, copy its full text, and paste it into Custom Instructions. If the field limit is too small, paste the complete text into a new conversation before your task; do not truncate the rules silently. No automatic skill discovery is implied.
- **DeepSeek:** paste the full SKILL.md into the system prompt if your client supports it. Otherwise paste it as the first message of a new chat; this is conversation context, not a platform-level system prompt.

Then provide the task, available evidence and desired deliverable. The skill produces a structured artifact from the supplied context; it does not itself repair systems, edit workbooks, send messages or submit business forms. Remove its folder or pasted instructions to uninstall.

中文：Codex 放入用户级 `~/.agents/skills/` 或项目 `.agents/skills/`；Claude Code 放入 `~/.claude/skills/` 或项目 `.claude/skills/`，重开会话并按名称调用。ChatGPT 将全文粘贴到自定义指令，超出长度时改为新对话首条完整粘贴；DeepSeek 使用支持系统提示的客户端，否则在新会话首条粘贴。一次选一个相关技能，附任务与已有资料。技能正文为中文，产出结构化文档，不自动执行情境中的业务动作。客户端目录可能随版本变化，请以所装版本文档为准。

## Paid collection
Seven paid skills at **US$4.9 each**; the complete **US$14.9 bundle** includes all seven plus the three MIT samples (10 skills total). The free files in the bundle remain free under MIT.

- **hypothesis-led-diagnosis** — Organize diagnosis around falsifiable hypotheses rather than guessed causes.
- **intent-to-acceptance** — Turn informal requests into acceptance specifications that retain counts and constraints.
- **powershell-json-shape-check** — Check JSON root types and empty, single and multiple-item shapes, not just parsing.
- **spreadsheet-formula-preservation** — Compare formula expressions instead of treating unchanged numbers as proof of preservation.
- **verification-layer-label** — Keep completion wording within the verification layer actually supported by evidence.
- **document-format-triage** — Identify document structure before choosing field, native-editing or image-based processing.
- **parallel-task-contract** — Create a self-contained task contract without relying on the main conversation.

[Buy a skill or the complete bundle]({{BUY_URL}})

Purchase link pending; checkout is not live in this draft. Prices are listed in USD; final checkout tax handling must be specified by the storefront. Paid content is not licensed by this repository's MIT license.

## Evidence and limits
In internal simulated tests (low-cost GPT and DeepSeek models, model-graded, small samples), the share of tasks fully correct on the first delivery rose from about 25% to 80% for GPT and from 76% to 100% for DeepSeek, averaged across the 10 skills. Results vary by task; this is not a guarantee.

## 中文说明
让 ChatGPT/Codex、DeepSeek 像 Claude 一样直接交付、少反问少免责。三份免费样品完整可用；七份付费技能各 $4.9，十份合集 $14.9。技能把已有资料组织成可用交付物，不代替执行或授权；保留必要澄清和真实限制。购买入口：{{BUY_URL}}（待填）。

内部模拟测试（便宜档 GPT 与 DeepSeek、同模型模拟评审、小样本）中，首次交付全部达标率 GPT 平均约 25%→80%、DeepSeek 约 76%→100%（10 个技能平均）。实际效果因任务而异，不作保证。
