# Skill Delivery Kit

Three skills for the moments when an agent reports "done" and nobody can tell what was actually checked. Each skill covers one failure pattern and gives the agent a short workflow, a fill-in output template, worked examples and a pre-delivery checklist.

## Skills

| Skill | Use it when | What you get |
|---|---|---|
| `resumable-handover` | You pause a task or hand it to another session or person | A handover note that says which version each finished check covers, what is left in order, and the first action to take when work resumes |
| `unknown-delivery-reconciliation` | A send, upload or submit timed out and you cannot tell whether it went through | A record of what happened to the original request, the evidence still missing, and one bounded next step. It does not resend |
| `reactive-form-input` | A web form shows the value you typed but validation or dependent fields disagree | A layer-by-layer report on whether the application accepted the input. It does not submit the form to find out |

Claude loads a skill on its own when the task matches the description. You can also call one by name, for example `/skill-delivery-kit:resumable-handover`.

## What the plugin contains

Plain-text instructions only. There are no scripts, hooks, MCP servers or commands. The plugin does not run code, call the network, or read or store personal data. You can read every line before you enable it.

Each skill folder holds:

- `SKILL.md`: the skill in English.
- `SKILL.zh.md`: the same skill in Chinese, for pasting into a chat when you work in Chinese.
- `EXAMPLES.md`: one complete test pair with the task inputs, the output without the skill, the output with it, and how each was graded.

## Install

```
/plugin marketplace add tdw8147-crypto/skill-delivery-kit
/plugin install skill-delivery-kit@skill-delivery-kit
```

## Evidence and limits

The numbers quoted in `EXAMPLES.md` come from an internal simulated test with a small sample and model grading. The method, the full tables and the limits are in [EVIDENCE.md](https://github.com/tdw8147-crypto/skill-delivery-kit/blob/main/EVIDENCE.md). Treat them as an indication, and try the skills on your own tasks.

## License

MIT. See `LICENSE`.
