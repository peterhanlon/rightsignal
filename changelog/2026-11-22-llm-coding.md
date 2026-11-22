---
date: 2026-11-22
slot: llm-coding
type: changed
title: Claude Opus 5.5 replaces GPT-6 Astra as best LLM for coding
old: GPT-6 Astra
new: Claude Opus 5.5
sources:
- https://benchlm.ai/benchmarks/swe-bench-verified
- https://openai.com/index/introducing-gpt-6-2-astra-sol
- https://www.tbench.ai/leaderboard
- https://www.vals.ai/benchmarks/terminal-bench
- https://artificialanalysis.ai/
---
GPT-6 Astra has lost the lead on every board this slot tracks. On the benchmark owners' own Terminal-Bench 4.1 table, Claude Opus 5.5 is first at 65.76% (Claude Code, max) with Astra fourth at 60.30%. Vals' live 11 November Terminal-Bench 4.0 board has Opus 5.5 joint-first at 65.15% with Claude Fable 5.2, ahead of Sonnet 5.5 (64.14%), Kimi K3.1 Pro (63.64%) and Gemini 4 Carbon (63.13%), with Astra sixth at 59.60%. Artificial Analysis superseded its Coding Agent Index v2.0 with v2.1 on 14 November, where Fable 5.2 and Opus 5.5 again share the lead at 58.

Two challengers split the boards. Kimi K3.1 Pro, run through Kimi Code CLI, tops AA's Terminal-Bench 4.1 harness run at 68% (Claude Code with Sonnet 5.5 at 66%, Opus 5.5 and Gemini 4 Carbon at 65%), and beat Astra 67.2% to 59.1% on AA's earlier 4.0 run. But that is one board; Opus 5.5 is first or joint-first on three, across two independent evaluators, holding from 11 to 14 November. It takes the title on that balance.

Two cautions. Vals publishes fallback-adjusted figures: counting fallback-assisted tasks as failures takes Opus 5.5 from 65.15% to 53.54% on 4.0 and from 87.64% to 79.77% on the archived 2.1 run. And SWE-bench Verified still belongs to Claude Opus 5 at 96% on benchlm's aggregate — a saturated board Astra was never run on. OpenAI announced GPT-6.2 Astra and Sol on 17 November; no independent coding runs yet.
