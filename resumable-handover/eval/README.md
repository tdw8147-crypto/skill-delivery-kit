# How the handover test works

1. `scenarios.json` — 6 scenarios: the facts each conversation hides, and the follow-up questions with expected answers.
2. `transcripts/` — the long conversations (generated once by GPT from those facts, then frozen; all fictional).
3. `handover_bench.py` — for each group (no skill / this skill / competitor / older editions) and model: the model reads the transcript and writes a handover; a fresh window sees only the handover and answers the questions; a blind grader (GPT) scores each answer against the original transcript.
   `--naive` = the user only says "summarize this". It calls our own model gateway (`fast_client`); swap `call()` for your own API client to rerun.
4. `summary_plain_wording.txt`, `summary_careful_prompt.txt` — the results. Group names: `none` no skill, `pwf` planning-with-files, `ours` compact v3, `live` previous published edition, `v4` this edition (Chinese), `v4en` this edition (English).
