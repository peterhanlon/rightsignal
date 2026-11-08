---
date: 2026-11-08
slot: llm-open-weight
type: changed
title: DeepSeek-V4.1-Flash-1017 replaces GLM-5.3 as best open-weight LLM
old: GLM-5.3
new: DeepSeek-V4.1-Flash-1017
sources:
- https://artificialanalysis.ai/models
- https://huggingface.co/zai-org/GLM-5.3
- https://huggingface.co/moonshotai/Kimi-K3.1-Pro
- https://huggingface.co/OBLITERATUS/DeepSeek-V4.1-Flash-1017-obliterated
- https://huggingface.co/ISTA-DASLab/DeepSeek-V4.1-Flash-1017-GSQ-RCO-Coder-GGUF
---
Artificial Analysis retired Intelligence Index v4.3 and published v5.0 on 27 October 2026, re-basing every score and cost figure this slot relied on. On the live table, GLM-5.3 (max) now reads 32 — level with, not clear of, DeepSeek V4.1 Flash 1017 (max), the two being joint best among models whose weights are actually released. Kimi K3.1 Pro scores 46 but has not shipped weights (a repo is trending on Hugging Face, though its status is unverified), and MiMo-V2.6-Pro's 46 sits only on the retired v4.3.2 scale.

With benchmark quality tied, the other criteria decide it. On serving cost GLM-5.3 (max) is $5.01 per Index task, ranked last of 21 comparable open-weight models, against roughly $0.60 for DeepSeek — about an eighth. On licence, DeepSeek ships under MIT, while GLM-5.3 uses Z.ai's own glm-5.3 terms, under which providers above $10bn revenue need a security review before commercial use. Both have weights out; DeepSeek is widely served in vLLM and SGLang, with GGUF and derivative builds already circulating.

This is not a single preliminary reading: AA also benchmarked DeepSeek independently on 19 October, scoring it 45 on v4.3.2, equal second among open weights and level with GLM-5.3. GLM-5.3 keeps an edge on raw throughput (75.8 output tokens/sec on AA's live page), which is a secondary measure here, and remains a reasonable pick where cost is not binding. Watch Kimi K3.1 Pro: if those weights are confirmed released, it takes the quality lead outright.
