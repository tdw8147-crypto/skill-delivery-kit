# Skill Delivery Kit
Make Codex, ChatGPT and DeepSeek deliver a usable first draft — fewer clarification loops, less boilerplate, clearer next actions.

![License: MIT](https://img.shields.io/badge/license-MIT-green) ![Skills: 10](https://img.shields.io/badge/skills-10-blue) ![Models: GPT / DeepSeek](https://img.shields.io/badge/models-GPT%20%7C%20DeepSeek-purple)

Ten compact skills for getting concrete artifacts out of messy tasks: handovers, diagnosis cards, acceptance specs and evidence-backed reports. Start with three free skills; each includes English and Chinese versions.

## Before / After
Same task: report v4 business completion from a passing v4 syntax check, an integration test blocked by `AUTH_DENIED`, and a v3 screenshot. The change: a general checklist becomes a version-scoped evidence table that distinguishes not-run from failed.

**Before — A, no skill**
```text
# v4 business completion check document
## Check goal
Confirm whether v4 business work is complete, distinguishing versions of syntax checks, real integration tests and screenshot evidence.
## Currently known
- v4 syntax check passed.
- v4 real integration test was not executed due to AUTH_DENIED; this cannot prove integration passed or business work is complete.
- The existing screenshot is v3 and cannot directly prove v4 completion.
…
1. Confirm the cause of AUTH_DENIED, the required authorization and whether it is resolved; after access returns, confirm whether v4 real integration tests ran and their results.
2. Supplement or confirm test records, screenshots and other evidence corresponding to v4, and check consistency with the target business scope.
3. Confirm the specific acceptance criteria and final acceptance conclusion for v4 business completion.
```

**After — S, with `verification-layer-label`**
```text
# Check document
## Original goal and conclusion
Original goal: v4 business completion. Conclusion: unverified. Existing evidence confirms only v4 syntax passed; it cannot prove functionality or business completion; the v3 screenshot does not cover v4.
## Evidence table
| Claim | Actual check and result | Layer | Version, environment, sample or location |
|---|---|---|---|
| Syntax passed | Syntax check recorded as passed | Static structure | v4; environment and location not stated |
| Real integration | Test did not run due to a permission error | Component integration | v4; environment not stated |
| Screenshot exists | A screenshot is recorded; it cannot prove usable interaction or business completion | Local sample | v3; page and environment not stated |
…
- Not executed: v4 real integration test did not run due to `AUTH_DENIED`.
```
Real output from our internal test run, model GPT (`gpt-6.1-terra`, low), translated from Chinese; excerpts from the first formal submissions, with omissions marked `…`.

## Quick start
Install all three free skills in one line (Bash, Git Bash or WSL):
```bash
git clone https://github.com/tdw8147-crypto/skill-delivery-kit.git && mkdir -p ~/.agents/skills && cp -R skill-delivery-kit/{resumable-handover,unknown-delivery-reconciliation,reactive-form-input} ~/.agents/skills/
```
In ChatGPT or DeepSeek, paste a skill's `SKILL.md` into your instructions or the start of a chat.
Then paste the task and its evidence; use the trigger example below to ask for the artifact.
For Chinese instructions, paste `SKILL.zh.md` instead.

## Free skills
| Skill | What it solves | Trigger example |
|---|---|---|
| `resumable-handover` | Resume work without rediscovering the context | Hand this task over with one clear next action. |
| `unknown-delivery-reconciliation` | Find the original receipt without sending twice | Reconcile this timed-out send without retrying it. |
| `reactive-form-input` | Tell displayed text from app-accepted input | Check whether this field input actually took effect. |

## Paid skills
| Skill | What it solves | Trigger example |
|---|---|---|
| `hypothesis-led-diagnosis` | Turn an unclear failure into a testable diagnosis | Give me a diagnosis card with one discriminating experiment. |
| `intent-to-acceptance` | Turn a vague request into observable acceptance | Turn this request into a per-item acceptance spec. |
| `powershell-json-shape-check` | Catch JSON that parses but breaks the consumer | Check zero, one and many items against this JSON contract. |
| `spreadsheet-formula-preservation` | Check formula preservation separately from values | Audit the original formulas against this edited workbook. |
| `verification-layer-label` | Say exactly what your checks actually prove | Label this release evidence by verification layer. |
| `document-format-triage` | Choose the right path for every document page | Triage this document into native, field and OCR paths. |
| `parallel-task-contract` | Give another executor a brief they can use alone | Write a self-contained task brief with an acceptance example. |

**Single skill: US$4.90 · Complete bundle (all 10): US$14.90.**
[Get the complete bundle](https://claudemodeskills.lemonsqueezy.com/checkout/buy/fb481b12-0fa4-4e0d-a856-128f28ad4eb1) · [Browse single skills](https://claudemodeskills.lemonsqueezy.com)
Each download includes English and Chinese skill files plus a short install guide.

## Results
Fourth-round internal test: first-delivery all-criteria pass rate (unweighted mean across ten skills).

| Model | No skill (A) | With skill (S) |
|---|---:|---:|
| GPT | ≈25% | ≈80% |
| DeepSeek | ≈76% | 100% |

Cheap-tier models, model-graded, small sample — details in [EVIDENCE.md](EVIDENCE.md).

## FAQ
**What client do I need?** A client that loads `SKILL.md`, such as Codex, or any chat client where you can paste instructions, including ChatGPT and DeepSeek; these are text instructions, not plugins.

**Does this change tool permissions?** No; skills organize the output and next steps using the access your client already has.

**What about refunds?** Check the refund terms shown at checkout before buying; use the free skills to try the format first.

**Which languages are included?** Every skill comes in English (`SKILL.md`) and Chinese (`SKILL.zh.md`); load one version at a time.

## License
The public repository and its three free skills are [MIT licensed](LICENSE).

## 中文
10 个精简技能，把任务整理成可用文档与明确下一步，减少反复追问和空泛声明。
公开仓库含 3 个免费技能，另有 7 个付费技能；每份均提供英文和中文。
单品 US$4.90；10 个合集 US$14.90。安装命令见上；聊天客户端可直接粘贴技能正文。
前后对比来自第四轮真实内部输出；测试方法与完整限制见 EVIDENCE.md。
