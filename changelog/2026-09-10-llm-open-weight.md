---
date: 2026-09-10
slot: llm-open-weight
type: changed
title: GLM-5.3 replaces Kimi K3 as best open-weight LLM
old: Kimi K3
new: GLM-5.3
sources:
- https://artificialanalysis.ai/leaderboards/models
- https://artificialanalysis.ai/models/open-source
- https://huggingface.co/zai-org/GLM-5.3
- https://huggingface.co/moonshotai/Kimi-K3
- https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash
---
Kimi K3 held this slot on a one-point lead over GLM-5.3 on Artificial Analysis's Intelligence Index v4.2. That scale has been retired. On v4.3 the lead is gone: AA's leaderboard fetched on 9 September has GLM-5.3 (max) at 45 and Kimi K3 (max) at 44, while AA's open-weights page on 7 September names the two as level at 44 at the top of the open field. On the most favourable reading for the incumbent, quality is now a tie.

The slot's other criteria then decide it. The pick's own card already conceded that GLM-5.3 costs roughly $0.9 per Index task against K3's $2.3 and runs at about 84 tokens per second against K3's 41 — K3 is rack-scale to self-host and slow even on Moonshot's hosted API. Both models have weights genuinely released on Hugging Face (K3 on 27 July, GLM-5.3 on 28 August) and both ship under vendor-specific licences rather than a standard open one, so neither wins on licence. GLM-5.3 is therefore ahead or level on quality and clearly ahead on serving cost.

Two caveats. GLM-5.3 on Hugging Face is a text-generation model under Z.ai's custom glm-5.3 licence — check its terms before commercial use, and note it does not match K3's native vision, though vision is not a criterion here. GLM-5.3-Flash (MIT, 26 August) scores 42 and is the cheaper Flash-class option. DeepSeek-V4.1-Flash appeared on Hugging Face trending on 10 September under MIT with an FP8 checkpoint, but carries no independent score yet.
