---
date: 2026-09-06
slot: llm-coding
type: challenged
title: 'gpt-6-astra-max takes #1 on Arena WebDev, but no agentic evidence yet'
old: null
new: gpt-6-astra-max
sources:
- https://arena.ai/leaderboard/code/webdev
---
A new model, gpt-6-astra-max, has entered the Arena WebDev board at #1 with 1797, ahead of claude-fable-5.1-max at 1762, claude-opus-5-max at 1688, qwen3.8-max-0902 at 1686 and kimi-k3-max at 1674. That is a 35-point margin over the previous leader and a clear gap over the Opus line — larger than the four-point shuffles we have logged on this board over the past few weeks, so it is worth registering rather than filing as noise.

It does not move the title. Arena WebDev is a human-preference board scoring web front-end output; none of this slot's criteria — agentic coding benchmarks, repo-scale task performance, tool-calling reliability — are measured by it. We have seen the same pattern twice already: claude-fable-5.1-max and qwen3.8-max-0902 both topped this board without a single independent agentic run appearing afterwards, and neither displaced Opus 5.

What would change our mind is an independent SWE-bench Verified or Terminal-Bench 2.1 run on a third-party harness. Opus 5 holds the pick on vals.ai's SWE-bench Verified board at 97.0% and sits second on their Terminal-Bench 2.1 table at 84.64%. Those numbers are already under pressure — GPT-5.6 Sol leads Terminal-Bench 2.1 at 85.77%, DeepSeek V4 Pro is within 0.6 points on SWE-bench Verified, and Opus 5's terminal figure drops to 81.27% if its server-side fallbacks to Opus 4.8 count as failures. A genuinely strong agentic showing from the new model would likely settle it. Until one is published, Opus 5 stays.
