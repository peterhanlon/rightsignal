---
date: 2026-09-03
slot: llm-coding
type: challenged
title: 'Claude Fable 5.1 Max takes Arena WebDev #1 by a wide margin; logged as challenger'
old: null
new: Claude Fable 5.1 Max
sources:
- https://arena.ai/leaderboard/code/webdev
- https://arxiv.org/abs/2609.02272
---
Anthropic's claude-fable-5.1-max has entered the Arena WebDev board straight at #1 with 1765 Elo, ahead of qwen3.8-max-0902 (1688), claude-opus-5-max (1687), kimi-k3-max (1674) and qwen3.8-max (1669). Unlike the Qwen3.8-Max result we logged previously — a four-point gap that was a tie in practice — this is a 77-point lead over the next entry and a 78-point lead over the incumbent's Arena variant, which is not noise.

It is still not enough to move the title. Arena WebDev is a human-preference board for web front-end work; it does not measure any of this slot's stated criteria — agentic coding benchmarks, repo-scale task performance, or tool-calling reliability. Fable 5.1 has no independent SWE-bench Verified or Terminal-Bench 2.1 run in the evidence to date, and the earlier Fable 5 terminal figures already came with a disclosed harness caveat (Vals reports Opus 4.8 used as a refusal fallback in both Fable 5's and Opus 5's runs).

Claude Opus 5 therefore holds, on the strength of its independent SWE-bench Verified result and its price position. The existing caveats stand: GPT-5.6 Sol leads Opus 5 on vals.ai's Terminal-Bench 2.1 table, and DeepSeek V4 Pro is within a point on SWE-bench Verified as an open-weight option. We will revisit if an independent agentic or repo-scale run for Fable 5.1 appears.

Also noted but not decision-relevant: PaperCompiler, a new arXiv method for repository-level paper-to-code generation, which reports no model ranking bearing on this slot.
