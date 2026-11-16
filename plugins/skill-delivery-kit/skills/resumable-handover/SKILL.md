---
name: resumable-handover
description: Use when a chat is too long and the user must open a new window, when context is about to be compacted or cleared, or when work is paused or passed to someone else. Writes a "handover note" that lets the new window pick up seamlessly from the note alone - no forgotten settings, no revived cancelled ideas, no repeating actions whose outcome is unknown. Trigger on "summarize so I can start a new chat", "we're near the limit", "write a handover", "context is about to compact".
---

# Handover note for a new window

The AI in the new window sees nothing from before - **only this note**. So write conclusions, not history; write the exact names and numbers, not "the one we mentioned earlier".

## Step 1: which kind of session is this
- **Chat**: writing, planning, a CV, studying, advice... the output lives in the conversation.
- **Agent**: the AI is calling tools, editing files, publishing, running commands.
Both use the format below; Agent sessions must also fill section 7.

## Note format (copy the headings; write "none" for empty sections)

```
[HANDOVER | <one line: what we are doing>]
To the new window: you are taking over; you cannot see the earlier chat, so this note is the source of truth. After reading, restate the goal and the next step in two or three sentences and wait for my OK before acting. If something is not in this note, ask me - do not guess.

1. Goal: what must be delivered, for whom, and what "done" looks like.
2. Final facts: names, numbers, dates, budget, IDs, confirmation numbers, file paths, versions - copied exactly. If the user changed their mind, write only the new value and add "(old X is void)".
3. Rules: the user's requirements and prohibitions, in their own words where possible.
4. Locked (do not change): parts the user has signed off. Quote short ones; say where long ones are.
5. Void / cancelled: rejected ideas, deleted plot points, dropped stops, approaches that failed (with why). The new window must not propose these again.
6. Undecided / waiting on someone: anything the user said "let me think", "not yet", or "waiting for X to reply" about. The new window must not decide for the user or invent content to fill the gap.
7. Actions with unknown outcome (required for Agent): anything sent but not confirmed (publish, submit, migration, payment, upload). Say where to check and what to look for; do not repeat it until checked.
8. Next step: the first concrete action (verb + object + what done looks like), then the following steps in order.
```

## While writing
- **Final state only.** If the user changed their mind three times, keep the last; old versions go into section 5 or brackets.
- **Copy proper nouns and numbers exactly**: character names, company names, confirmation and order numbers, commands, paths, banned words. Never compress them into "details confirmed".
- **Leave out only secrets**: passwords, one-time codes, card numbers, API keys, ID numbers. Order numbers, booking/confirmation numbers, file paths and versions **must be included** - the next person needs them.
- Do not copy small talk, trial-and-error, or long passages the AI wrote; keep the conclusions.
- Length: usually 600-2000 words. Prefer one more of the user's hard rules over one more paragraph of history.
- Plain language the user can read. No jargon like "evidence locator", "breakpoint", "side effect".

## Self-check before sending
- [ ] Reading only the note, can the new window name its first action?
- [ ] For everything the user changed, does only the new version remain?
- [ ] Is everything the user rejected or cancelled in section 5?
- [ ] Did anything undecided get written as decided?
- [ ] Is any unknown-outcome action written as "done" or "not started"? (Both are wrong - it is "to be checked".)
- [ ] Are names, numbers and IDs exact? Did a confirmation number get dropped as "private"?

## Example (chat)
```
[HANDOVER | Planning a small wedding on 18 May: running order and budget]
To the new window: ... (as above)
1. Goal: a running-order sheet and a budget sheet to send to the planner and both families.
2. Final facts: date 18 May (old 11 May is void); 60 guests (old 80 is void); venue "Lakeside Lawn", deposit paid, contract no. HP-0518.
3. Rules: no prank games; total budget at most 60,000; the bride's mother does not eat beef.
4. Locked: entrance music; the vows text (written by the user - do not edit).
5. Void: the indoor backup venue; drone filming (too expensive).
6. Undecided: whether to hire a band - waiting for the groom to get a quote from a friend; do not decide for him.
7. Unknown outcome: none.
8. Next step: recalculate catering for 60 guests and update the budget sheet.
```

## Example (Agent)
```
7. Unknown outcome: ran deploy.sh to release v2.3 to staging; SSH dropped, result unknown. First open /health and check the version is 2.3; do not run deploy.sh again until checked.
8. Next step: check /health version; then set the expiry in config/cache.yml to 600 and run npm test -- cache.
```
