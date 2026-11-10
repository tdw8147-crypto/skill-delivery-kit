# Unknown Delivery Reconciliation

When a receipt is unclear, settle what you can without sending the request twice.

## The problem

An attachment upload times out, but a matching read-only receipt says it arrived. A newer note refers to a different identifier and says only that it was sent. The operator needs to know whether the two records describe the same request before closing the case. Clicking upload again would add another attempt without settling the first.

## Before / After

**Before — GPT, A (no skill), internal simulated test.** Original Chinese excerpt:

> 待决：确认q7与att-901是否为同一对象、09:02查询是否覆盖q7，以及q7是否已有delivered证据。若q7属于验收范围且尚无送达证据，整体验收暂不能宣称完成；建议仅针对原q7进行只读状态核实，或在有界期限内等待其delivered，再依据证据判定。等待期限及到期后的处置方向待确认，不擅自重发。
> …

**After — GPT, S (short skill), internal simulated test.** Original Chinese excerpt:

> 下一步：建议仅对原q7进行最多一次只读正式状态查询，核对目标、提交时间及原附件hash以确认其是否属于att-901。若匹配原身份的最新可信回执为delivered，即达到送达验收并结案，无需等待已读；若查询不可用、身份仍无法归属或未达到送达，则保留待决，不再自动查询。不得重投、换标识重投或再次点击测试。

Both avoid resending; the after response sets a concrete cap and names what to match.
It defines when to close and when to preserve the unresolved state without further polling.

Source: `unknown-delivery-reconciliation__gpt__hard-1__1__A.json` and `unknown-delivery-reconciliation__gpt__hard-1__1__S.json`, `last_draft`.

## Evidence

First-delivery all-criteria pass rate (A → S): **GPT 15.4% → 33.3%; DeepSeek 92.3% → 100.0%** (`EVIDENCE.md`; internal simulated test, small sample). Historical short-skill results, not a test of this expanded edition.

## Trigger phrases

- “It timed out after submit. Did it go through?”
- “Does this receipt belong to the original attachment?”
- “Sent isn't enough; confirm whether it was delivered.”
- “Write the status record without resending.”

## Install

- **Claude Code:** Put `unknown-delivery-reconciliation/SKILL.md` under `~/.claude/skills/`.
- **Codex:** Put `unknown-delivery-reconciliation/SKILL.md` under `~/.agents/skills/`.
- **Cursor:** Create `.cursor/rules/unknown-delivery-reconciliation.mdc` and paste the skill body into the rule.
- **ChatGPT / DeepSeek:** Paste the skill and the existing request and receipt evidence into the chat.

## What's inside

- `SKILL.md` — English workflow, template, examples and checklist.
- `SKILL.zh.md` — Complete Chinese version.
- `README.md` — This page: the problem, a real before/after, numbers and install steps.

## 中文简介

超时或回执冲突时，按原请求标识、目标、提交时间和内容指纹核对。只报告证据支持的层级；达标就结案，缺证据也先交记录，只留一个有界查询，不重发。
