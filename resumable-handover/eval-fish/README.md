# Long-chat handover test (DeepSeek, two window moves)

[中文说明在下面](#中文)

## Why a second test

Our first test ([../eval](../eval)) used short chats and one window move. DeepSeek scored about the same with and without the skill there, because the task was too easy. Real chat users talk much longer, change their minds often, move windows more than once, and only say "summarize this". So we rebuilt the test around that.

## Method (`fish_bench.py`)

- 4 scenarios rewritten from our own real projects: planning a video episode (many changed decisions), publishing a short video, listing a product for sale, and rules for replying to comments. The comments scenario was added **after** the skill was written, to check we did not just tune to the questions.
- Each scenario: a frozen ~23k-character Chinese conversation (3 parts) plus a ~5k-character continuation in the new window.
- Move 1: DeepSeek reads the long conversation, the user says only "总结一下我们刚才聊的内容，我要开个新对话。" ("summarize what we discussed, I'm starting a new chat") → handover 1.
- Move 2: a new window sees only handover 1 + the continuation; the user says the same sentence again → handover 2.
- A third window sees only handover 2 and answers 9–10 realistic follow-ups ("what's the partner's nickname?", "the upscaled file isn't back — can I upload the raw one?"). GPT grades each answer against the full original conversation.
- Model: deepseek-v4.1-flash, thinking off. 10 runs per scenario per condition. Condition "with" = the Chinese edition `resumable-handover-zh` (v4, same text as in this repo).

## Results

| | No skill | With skill (v4) |
|---|---|---|
| All 4 scenarios, follow-ups correct | 233/370 = **63%** | 289/370 = **78%** |
| Video episode plan | 78% | 81% |
| Short video publishing | 64% | 67% |
| Product listing | 57% | 78% |
| Comment rules (added after the skill) | 51% | **87%** |
| Runs with every question right | 0/40 | 2/40 |

- A draft v5 (copy every old item forward, also record attempted results) scored 73% over 18 runs — worse than v4, so it was **not** released.
- Most common misses: which option was cancelled and which one stayed (the model swaps them), attempts that already failed, and time-zone conversions.

## Limits

- The conversations were written by GPT from our real project notes, not raw chat logs. They contain private project details, so the transcripts and scenario files are not published; the script is, for anyone who wants to build their own scenarios.
- Graded by a model. 10 runs per cell — a small sample.
- After two moves, almost no run is perfect even with the skill. It loses less; it does not lose nothing.

`fish_bench.py` imports `../eval/handover_bench.py` and expects your API settings there. Subcommands: `gen` (build frozen conversations from a `scenarios.json`), `run` (moves + questions + grading), `sum` (totals). Example: `python fish_bench.py run --reps 10 --conds none,v4`.

---

## 中文

### 为什么又测一轮
第一轮（[../eval](../eval)）对话短、只换一次窗口，DeepSeek 装不装差不多——题太简单。真实用户是：聊得很长、改口很多、换好几次窗口、只会说“总结一下”。所以照这个重做。

### 测法
- 4 个场景都是我们自己项目里的真事改写：一期视频怎么做（改口很多次）、短视频发布、商品上架、评论区回复规矩（这个是技能写好**之后**才加的“没见过的题”）。
- 每段约 2.3 万字长对话 + 新窗口续聊约 5 千字，冻结不变。
- 第 1 次换窗口：用户只说“总结一下我们刚才聊的内容，我要开个新对话。”→ 纸条 1；第 2 次：新窗口只看纸条 1 + 续聊，再说一遍 → 纸条 2。
- 第三个窗口只看纸条 2，回答 9～10 个真人会问的追问；GPT 对照完整原对话判对错。
- deepseek-v4.1-flash（不开思考），每个场景装/不装各 10 次；“装”的是中文版 `resumable-handover-zh`（v4，和仓库里一字不差）。

### 结果
370 道追问答对：不装 **63%** → 装上 **78%**；没见过的评论区规矩 **51% → 87%**；全部答对的次数 0/40 vs 2/40。草稿 v5 跑了 18 次平均 73%，比 v4 差，没有上线。

### 说实话
- 对话是 GPT 按我们的真事写的，不是原始聊天记录；里面有项目私事，所以对话和场景文件不公开，脚本公开。
- 模型评分，每格 10 次，小样本。
- 换两次窗口后，装上也会丢东西——新窗口第一件事，请自己扫一眼纸条。
