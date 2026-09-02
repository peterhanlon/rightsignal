---
date: 2026-09-02
slot: llm-coding
type: challenged
title: 'Qwen3.8-Max-0902 takes #1 on Arena WebDev, joining the challenger list behind
  Claude Opus 5'
old: null
new: Qwen3.8-Max-0902
sources:
- https://arena.ai/leaderboard/code/webdev
---
Alibaba's new checkpoint, qwen3.8-max-0902, has moved to #1 on the Arena WebDev coding board at 1,691 Elo, displacing claude-opus-5-max, which now sits second at 1,687. The rest of the top five is kimi-k3-max at 1,674, the earlier qwen3.8-max at 1,669 and claude-opus-5-high at 1,661 ([Arena WebDev](https://arena.ai/leaderboard/code/webdev)).

A 4-point Elo gap is not a result. On a board of this size that margin is comfortably inside the usual confidence interval, and the two models are best read as tied. More importantly, Arena WebDev measures human preference between generated web front-ends. It tells you little about the three things this slot is judged on: agentic coding benchmarks, repo-scale task completion and tool-calling reliability. Kimi K3 has been sitting in the same neighbourhood on this board for weeks without shifting the title, for the same reason.

So Qwen3.8-Max goes on the challenger list rather than into the pick. What would move it: an independent agentic run — SWE-bench Verified or Terminal-Bench 2.1 on a third-party harness such as vals.ai — showing it at or above Opus 5's 97.0% and 84.64%. Nothing in this cycle provides that.

The existing caveats stand unchanged. Opus 5's terminal lead remains genuinely contested against GPT-5.6 Sol, and its Terminal-Bench figure still depends on how you score server-side fallbacks to Opus 4.8. Claude Opus 5 holds the title.
