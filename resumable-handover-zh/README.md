<p align="center"><img src="../media/ruoxi-handover-banner.png" alt="若溪的交接纸条：换窗口不失忆" width="100%"></p>

# 换窗口交接纸条（中文版）

对话太长要开新窗口、上下文要被压缩时用。把它贴给 AI，再随口说一句“总结一下，我要开新对话”，AI 就会写出一张**交接纸条**：新窗口只看这张纸条，就能接着干——名字、数字、确认号原样保留，你否掉的方案不会再冒出来，还没定的事不会被它擅自决定，结果不明的操作不会被重做。

适合：DeepSeek 提示“达到对话长度上限”、ChatGPT/豆包/Kimi 聊久了忘事、Claude Code `/compact` 后丢规矩。

## 实测（2026-11，自己测，方法和脚本公开）

6 个真实场景（写小说、改简历、家庭旅行、修 bug、定时发视频、批量改名），每个都藏着改口、作废、没定、结果不明的坑。新窗口只看交接，回答 6～7 个像真人一样的追问，盲评对照原对话打分。GPT + DeepSeek 各跑 2 次。

用户只说“总结一下”时：

| | 平均分 | 全部答对 |
|---|---|---|
| 不装 Skill | 0.95 | 16/24 |
| planning-with-files（热门竞品，只测技能正文和模板，没测它的 Claude Code 插件） | 0.95 | 18/24 |
| 我们上一版 | 0.94 | 18/24 |
| **这一版** | **0.98** | **21/24** |

说实话：样本不大；如果你本来就会写很讲究的交接提示词，装不装差别不大（0.96 对 0.95）。它帮的是不会写提示词的人——随口一句，效果不输精心写的提示词。

## 怎么用

- **DeepSeek / ChatGPT / 豆包 / Kimi（网页或 App）**：把 `SKILL.md` 全文贴进对话，再说“总结一下，我要开新对话”。把它写的纸条复制到新窗口第一条。
- **Claude Code**：把本文件夹复制到 `~/.claude/skills/`。
- **Codex**：复制到 `~/.agents/skills/`。

```bash
npx skills add tdw8147-crypto/skill-delivery-kit --skill resumable-handover-zh
```

## 更多

- 英文版和测试说明：[resumable-handover](../resumable-handover/)
- 许可：MIT
