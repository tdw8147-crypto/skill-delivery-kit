# 可续办交接（中文版）

暂停或转交工作时，交付一份标明证据版本、接手后可以直接续办的断点单。

这是 [`resumable-handover`](../resumable-handover/) 的中文独立版，内容与该目录下的 `SKILL.zh.md` 相同，单独成文件夹是为了能用安装工具直接装。中文版和英文版装一个就够。

## 安装

```bash
npx skills add tdw8147-crypto/skill-delivery-kit --skill resumable-handover-zh
```

或手动把本文件夹复制到 `~/.claude/skills/`（Claude Code）或 `~/.agents/skills/`（Codex）。聊天应用直接粘贴 `SKILL.md` 的内容。

## 更多

- 完整的真实测试对比（输入、两份输出、评分项）：[EXAMPLES.md](../resumable-handover/EXAMPLES.md)
- 测试数据和局限：[EVIDENCE.md](../EVIDENCE.md)
- 许可：MIT
