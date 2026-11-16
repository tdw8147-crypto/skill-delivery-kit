<p align="center"><img src="../media/ruoxi-handover-banner.png" alt="Ruoxi's handover note: a new window that remembers" width="100%"></p>

# Resumable Handover

Chat too long? Context about to compact? Paste this skill in, say "summarize so I can start a new chat", and the new window picks up exactly where you left off — same names, same rules, nothing you cancelled coming back.

## The problem

Every long chat hits the wall: DeepSeek's "conversation length limit", ChatGPT drifting away from the original goal, Claude Code forgetting your rules after `/compact`. The usual fix is "ask the AI for a summary and paste it into a new chat". That summary quietly drops the things that matter: the booking number, the rule you set in message 3, the plot twist you killed, the deploy that may or may not have gone through.

This skill gives the AI one fixed shape for that note — final facts, rules, locked parts, **void ideas**, **undecided items**, **actions with unknown outcome**, next step — and a self-check before it hands it over.

## Before / After

Same model (GPT), same 25,000-character family-trip chat, user just says "summarize this, I'm opening a new chat". Then, in the new window: *"What's the Chengdu hotel confirmation number?"*

**Without the skill**

> The handover doesn't include the confirmation number; you'll need to check your booking. Check-in 2 Oct, check-out 4 Oct.

**With the skill**

> Confirmation number **CD8841**, check-in 2 Oct, check-out **4 Oct**.

Same test, a publishing-agent chat where the user had said "no external links". New window is asked: *"Add a cloud-drive link to the description?"*

- Without: *"Not for now; check the link and platform rules first."* — the rule has become a maybe.
- With: *"No. We agreed: no external links in the description or comments."*

## Evidence (Nov 2026, our own test, method and scripts public)

6 realistic scenarios — 3 chat (co-writing a novel, CV rewrite, family trip) and 3 agent (bug fix with an unknown DB migration, scheduled video publishing, a 1,000-photo batch rename stopped halfway). Each conversation hides changed minds, cancelled items, undecided items and an action with unknown outcome. A fresh window sees **only** the handover and answers 6–7 follow-up questions phrased like a real user ("just book me a hotel then"). A blind grader checks every answer against the original conversation. GPT-6.1 and DeepSeek-v4.1, 2 runs each.

User says only "summarize this":

| | Avg score | All questions right |
|---|---|---|
| No skill | 0.95 | 16/24 |
| planning-with-files (Chinese skill text + templates only; its Claude Code hooks are not tested here) | 0.95 | 18/24 |
| Our previous edition | 0.94 | 18/24 |
| **This edition** | **0.98** | **21/24** |

Honest limits: small sample; modern models already write decent handovers when asked carefully (with a carefully written prompt, no-skill scored 0.96 and this edition 0.95 — no real difference). The gain is for people who don't know how to ask: one casual sentence gets you a handover at least as good as a well-crafted prompt.

## Install

- **ChatGPT / DeepSeek / Doubao / Kimi (web or app):** paste the contents of `SKILL.zh.md` (Chinese) or `SKILL.md` (English) at the start of a chat, or right before you ask for the summary.
- **Claude Code:** copy this folder to `~/.claude/skills/`.
- **Codex:** copy this folder to `~/.agents/skills/`.
- **Cursor:** create `.cursor/rules/resumable-handover.mdc` and paste the skill body.

## Trigger phrases

- "Summarize this, I'm starting a new chat."
- "We're near the limit — write a handover."
- "Context is about to compact."
- "Pause here; someone else will continue."

## What's inside

- `SKILL.md` — English skill: the 8-part note, writing rules, self-check, two examples.
- `SKILL.zh.md` — Chinese skill (the one tested above).
- `EXAMPLES.md` — a complete before/after from the **previous** edition's test.
