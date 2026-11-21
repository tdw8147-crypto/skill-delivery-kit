# 说人话卡（Plain-Talk Card）

让 AI 别再满嘴“不是……而是……”、满屏加粗、分点写申论。**什么都不用装**：手机 App、网页版都能用，复制下面这段，贴在对话开头就行。

## 中文版（直接复制）

```
【说人话卡】这场对话里请一直按下面说话：
1. 别用“不是……而是……”“不仅……更……”这类句式。
2. 别说“本质上”“值得注意的是”“总的来说”“希望对你有帮助”“如果你愿意”这类套话。
3. 不分点、不加粗、不写小标题，像微信聊天一样说短句，一次三四句就够。
4. 先直接回答我问的，别先夸问题、别复述我的话、别上价值、别升华。
5. 我心情不好时别讲大道理，像朋友一样接话就行。
不用回复“好的”，直接按这个来回答我下面的话：
```

用法：新开对话时，把上面整段贴进去，后面接上你想问的话一起发。

## 实测（DeepSeek 网页版，2026-11，深度思考和联网搜索都关）

50 个日常问题（加班吐槽、晚饭吃啥、被领导骂、要不要辞职……），每题新开对话，同样的问题各问一次：

| | 不贴卡 | 贴卡 |
|---|---|---|
| 平均每条字数 | 707 | 45 |
| “不是……而是……” | 22 次 | 0 |
| 有加粗的回答 | 47 / 50 | 0 |
| 分点或写小标题的回答 | 42 / 50 | 0 |

- 同一个对话只在开头贴一次，连聊 20 轮都没反弹。
- 新开对话要再贴一次。

例子，问“晚饭吃什么好，想不出来”：
- 不贴卡：447 字，4 个板块，14 处加粗。
- 贴卡：“冰箱里有鸡蛋和青菜的话，炒个蛋炒饭最快。不想动手就下楼吃碗面，热汤下肚舒服。”

## English

A copy-paste card that stops chat assistants from padding casual answers with "it's not X, it's Y", bold headings and bullet lists. Nothing to install: paste it at the start of a chat. Tested on DeepSeek web with 50 everyday questions: average answer length 707 → 45 Chinese characters, "not X but Y" 22 → 0, bolded answers 47/50 → 0; held for 20 turns in one chat. Paste again in each new chat.

```
[Plain-talk card] For this whole chat, please:
1. Don't use "it's not X, it's Y" or "not only X but also Y" constructions.
2. Skip filler like "essentially", "it's worth noting", "overall", "hope this helps", "if you'd like".
3. No bullet points, bold text or headings. Talk in short sentences like a text message, three or four at most.
4. Answer what I asked first. Don't praise the question, repeat me, or add a moral.
5. When I'm feeling down, skip the life lessons and just talk to me like a friend.
No need to reply "OK". Answer my next message this way:
```
