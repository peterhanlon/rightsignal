---
date: 2026-11-15
slot: llm-coding
type: changed
title: Claude Opus 5.5 replaces GPT-6 Astra as best LLM for coding
old: GPT-6 Astra
new: Claude Opus 5.5
sources:
- https://benchlm.ai/benchmarks/swe-bench-verified
- https://developers.openai.com/api/docs/models/gpt-6-astra
- https://www.anthropic.com/claude/opus
---
GPT-6 Astra no longer leads the main independent agentic-coding run. On Vals' Terminal-Bench 4.0 board, updated 5 November 2026, Astra is fifth at 59.60%, behind Claude Opus 5.5 (65.15%), Claude Sonnet 5.5 (64.14%), Kimi K3.1 Pro (63.64%) and Gemini 4 Carbon (63.13%). The same evaluator had Opus 5.5 ahead of Astra a month earlier on the now-archived Terminal-Bench 2.1 table, 87.64% to 87.27%, so this is a result that has held across two runs and two scales rather than a single preliminary reading. Of the models ahead of Astra, Opus 5.5 leads them all, which is why it takes the title rather than Sonnet 5.5 or Kimi K3.1 Pro.

Astra's remaining claim is the official Terminal-Bench board, where it is still #1 at 87.4% as of 15 November 2026. But Opus 5.5 is absent from that board, so it is an unscored gap rather than a win: no published run anywhere has Astra ahead of Opus 5.5. On repo-scale work, Astra is not in benchlm's SWE-bench Verified top ten at all, which is topped by Claude Opus 5 at 96%.

Two caveats for practitioners. Opus 5.5 has no score on the official Terminal-Bench board or on SWE-bench Verified, so its repo-scale evidence is thinner than its agentic-terminal evidence. And the earlier rationale for Astra cited an Artificial Analysis launch run from 9 September 2026 that predates both Opus 5.5 and Sonnet 5.5; treat any AA figures from that article as stale. If your workload is terminal-shaped agentic coding, Opus 5.5 is the current pick.
