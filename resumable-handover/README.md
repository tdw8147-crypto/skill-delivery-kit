# Resumable Handover

Give the next shift a starting point, not a transcript to reread.

## The problem

A four-page manual has been exported and its body checked, but nobody has opened the latest PDF. A new revision changed only the cover. The next operator needs to know what the older review still covers, what to open first, and when to restore the cover. A long list of things to reconfirm obscures that decision.

## Before / After

**Before — GPT, A (no skill), internal simulated test.** Original Chinese excerpt:

> ## 待确认
> - v3 的准确路径、恢复封面的具体操作，以及复核后由谁确认交付。
> …

**After — GPT, S (short skill), internal simulated test.** Original Chinese excerpt:

> 第一动作：定位并打开最新v3文件；完成信号为实际看到v3预览。若暂无法定位，等待提供v3文件位置。
> …

The after response puts the concrete resume action and visible completion signal together.
It also names the exact missing input instead of making the entire handoff wait.

Source: `resumable-handover__gpt__hard-1__1__A.json` and `resumable-handover__gpt__hard-1__1__S.json`, `last_draft`.

## Evidence

First-delivery all-criteria pass rate (A → S): **GPT 23.1% → 100.0%; DeepSeek 66.7% → 100.0%** (`EVIDENCE.md`; internal simulated test, small sample). Historical short-skill results, not a test of this expanded edition.

## Trigger phrases

- “Leave a handover for the next shift.”
- “What is the first action when we resume?”
- “This revision changed only the cover. What still needs checking?”
- “Capture the pending request without trying it again.”

## Install

- **Claude Code:** Put `resumable-handover/SKILL.md` under `~/.claude/skills/`.
- **Codex:** Put `resumable-handover/SKILL.md` under `~/.agents/skills/`.
- **Cursor:** Create `.cursor/rules/resumable-handover.mdc` and paste the skill body into the rule.
- **ChatGPT / DeepSeek:** Paste the English or Chinese skill and the current notes into the chat.

## What's inside

- `SKILL.md` — English workflow, template, examples and checklist.
- `SKILL.zh.md` — Complete Chinese version.
- `README.md` — This page: the problem, a real before/after, numbers and install steps.

## 中文简介

暂停、换班或转交时，用现有资料直接产出断点单：写清已完成证据支持哪个版本、下一步做什么、看到什么才算做完。资料不全也先交，未完成的业务动作不代做。
