---
date: 2026-09-09
slot: llm-open-weight
type: changed
title: GLM-5.3 replaces Kimi K3 as best open-weight LLM
old: Kimi K3
new: GLM-5.3
sources:
- https://huggingface.co/moonshotai/Kimi-K3
- https://artificialanalysis.ai/models
- https://huggingface.co/zai-org/GLM-5.3
---
The Artificial Analysis open-weights table has flipped. Today's standings put GLM-5.3 (max) at 45 on the AA Intelligence Index against Kimi K3 (max) at 44 — a reversal of the 50-to-49 reading the slot card was built on, and the same ordering this slot already recorded when GLM-5.3 was listed as challenger. One board, one point, but it has held across readings rather than appearing today for the first time.

The rest of the criteria are not close. GLM-5.3's weights went public on 28 August, so availability is settled. On serving cost it runs at roughly $0.9 per Index task against K3's $2.3, and at about 84 tokens per second against K3's 41. K3 is rack-scale to self-host — 2.8T parameters, 104B active — and slow even on Moonshot's own API, and its licence is a custom Moonshot one requiring attribution above 100M MAU or $20M monthly revenue and a separate agreement for large model-as-a-service use.

So the title moves. Caveats worth holding: the quality lead is a single point from a single tracked board, and we have not independently verified GLM-5.3's full licence terms — GLM-5.3-Flash is MIT, but that does not automatically carry to the max checkpoint. Check the model card before you build on it. Kimi K3 stays as the nearest challenger, and DeepSeek-V4-Flash-Vision-Exp remains the lightest self-host at roughly 168GB, but at 42 on the Index it is a cost-and-speed pick, not a quality one.
