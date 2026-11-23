---
date: 2026-11-22
slot: llm-open-weight
type: changed
title: Kimi K3.1 Pro takes best open-weight LLM from DeepSeek-V4.1-Flash-1017
old: DeepSeek-V4.1-Flash-1017
new: Kimi K3.1 Pro
sources:
- https://artificialanalysis.ai/models
- https://huggingface.co/moonshotai/Kimi-K3.1-Pro
- https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017
---
The thing that kept DeepSeek-V4.1-Flash-1017 in this slot was that Kimi K3.1 Pro's weights were hypothetical. They are not any more. Moonshot published moonshotai/Kimi-K3.1-Pro on Hugging Face on 4 November 2026, ungated, at roughly 1.56TB, with vLLM and SGLang recipes on the card, so it now clears the "weights actually released" criterion.

On benchmark quality the gap is wide and it has held. Artificial Analysis's Intelligence Index v5.0.1 puts Kimi K3.1 Pro at 46 against DeepSeek V4.1 Flash 1017 (max) at 33, and AA's live board names Kimi the top open-weights model; that reading was the same when this slot was last written on 8 November and again at our 22 November fetch. For the record, the outgoing card's claim of a joint-best 32 level with GLM-5.3 is stale: on v5.0.1 the pick reads 33 and GLM-5.3 (max) 32, and neither is the best released-weight score.

DeepSeek keeps two things. Serving cost: $0.60 per Index task against Kimi's $3.68. And licence: plain MIT with no commercial review clause, where Kimi ships a bespoke licence requiring a separate Moonshot agreement for model-as-a-service businesses above $20m revenue, plus attribution above 100m MAU. At 2.8T parameters Kimi is a multi-node serve, so most teams will rent it rather than host it.

That is a secondary-measure win, not a block. If your constraint is budget or a clean licence, DeepSeek remains the sensible self-host; if it is capability, Kimi is now the open-weight leader.
