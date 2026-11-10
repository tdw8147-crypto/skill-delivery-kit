# Reactive Form Input

The field can look right and still be empty where the application makes decisions.

## The problem

A profile page has a visible contact email field and a hidden email field. A DOM write makes the address appear, but the application model is empty. The submit button stays disabled, and the team needs a record of what actually took effect. Submitting the form is not part of that check.

## Before / After

**Before — GPT, A (no skill), internal simulated test.** Original Chinese excerpt:

> ## 当前结论
> 已报告状态同步与提交受阻现象；原因和验证结果待确认，不能宣称检查完成或通过。

**After — GPT with an earlier full-length version of this skill, internal simulated test.** Original Chinese excerpt:

> - 资料记载：DOM 赋值后显示值正确，但 React state 为空，提交按钮禁用。资料未说明具体观察时点、校验提示或异步校验是否结束。
> - 显示值与应用状态不一致，不能仅凭 DOM 值判定输入已生效；当前只能记录为未确认生效，亦不能据此断言最终失败。上述状态均为资料记载，未由本次实际验证。
> …

The after response separates what was displayed from what the application accepted.
It also names the missing validation evidence without implying a live test ran.

Source: `reactive-form-input__gpt__hard-1__1__A.json` and `reactive-form-input__gpt__hard-1__1__C.json`, `last_draft`. The saved archive has no compact-version sample for this task, so the excerpt comes from the earlier full-length variant.

## Evidence

First-delivery all-criteria pass rate (A → S): **GPT 33.3% → 100.0%; DeepSeek 80.0% → 100.0%** (`EVIDENCE.md`; internal simulated test, small sample). These are historical compact-version results, not results for the excerpt above or for this expanded edition.

## Trigger phrases

- “The field looks filled, but the app hasn't picked it up.”
- “Check the visible contact field, not the hidden duplicate.”
- “Is this input accepted, still validating, or unverified?”
- “Check the form state without submitting it.”

## Install

- **Claude Code:** Put `reactive-form-input/SKILL.md` under `~/.claude/skills/`.
- **Codex:** Put `reactive-form-input/SKILL.md` under `~/.agents/skills/`.
- **Cursor:** Create `.cursor/rules/reactive-form-input.mdc` and paste the skill body into the rule.
- **ChatGPT / DeepSeek:** Paste the skill and the page or interaction notes into the chat.

## What's inside

- `SKILL.md` — English workflow, template, examples and checklist.
- `SKILL.zh.md` — Complete Chinese version.
- `README.md` — This page: the problem, a real before/after, numbers and install steps.

## 中文简介

表单明明显示了值，应用却可能没接收。这个技能让代理认准目标字段、分开记录显示值与应用信号，区分已生效、未生效、校验中和未验证；不靠提交业务表单来试。
