---
date: 2026-09-09
slot: llm-coding
type: challenged
title: GPT-6 Astra challenges Claude Opus 5 for best LLM for coding
old: null
new: GPT-6 Astra Max
sources:
- https://arena.ai/leaderboard/code/webdev
- https://www.anthropic.com/claude/opus
- https://openai.com/index/codex-quantum-computing-experiments
---
GPT-6 Astra would take this title on today's evidence, but the case has not yet cleared our bar for a change, so it is recorded as the challenger for now. The adjudicator's reasoning:

The title moves to GPT-6 Astra Max. On the agentic side, vals.ai's Terminal-Bench 2.1 now has Astra first at 87.27%, ahead of GPT-5.6 Sol (85.77%), Claude Fable 5.1 (85.02%) and Opus 5 in fourth at 84.64% — and Opus 5's own figure falls to 81.27% once its server-side fallbacks to Opus 4.8 on refused tasks are counted as failures. Astra also tops vals' Code Migration table, which is the nearest thing on that board to repo-scale work. That is not a one-board reading: Arena WebDev has had Astra at #1 across both fetches in this cycle, 1,796 on 9 September against claude-fable-5.1-max at 1,764 and claude-opus-5-max at 1,688, with our outgoing pick third.

Opus 5 keeps #1 on the independent SWE-bench Verified aggregate at 96%, but the top three there sit within a point of each other and vals has dropped that benchmark from its coding index as saturated, so it no longer carries the weight it did when Opus 5 took the title in July.

Claude Fable 5.1 Max is the other contender and leads the Vals Index overall, but it trails Astra on both boards this slot tracks and its refusals on bio- and cyber-adjacent tasks remain an operational cost. Astra is dearer at $10/$50 per million tokens against Opus 5's $5/$25, and there is still no independent SWE-bench Verified run for it — that is the main reason for medium rather than high confidence. Teams already happy with Opus 5's cost profile have no urgent reason to switch; new agentic setups should default to Astra.
