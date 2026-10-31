---
date: 2026-10-31
slot: llm-open-weight
type: challenged
title: DeepSeek-V4.1-Flash challenges GLM-5.3 on licence and serving support, not
  yet on scores
old: null
new: DeepSeek-V4.1-Flash-1017
sources:
- https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017
- https://github.com/sgl-project/sglang/releases/tag/v0.5.21
- https://github.com/vllm-project/vllm/releases/tag/v0.32.0rc2
- https://artificialanalysis.ai/models
- https://huggingface.co/mistralai/Mistral-Large-4-1T-A52B
- https://huggingface.co/zai-org/GLM-5.3
---
GLM-5.3 keeps the title, but there is now a credible challenger worth naming.

DeepSeek released V4.1-Flash-1017 on 17 October under MIT, with weights on the official repo and FP8 checkpoints in-tree ([Hugging Face](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017)). The serving stack has moved fast: SGLang v0.5.21 ships it as a supported LLM/VLM with its own cookbook entry ([release notes](https://github.com/sgl-project/sglang/releases/tag/v0.5.21)), and vLLM v0.32.0rc2 has a pinned CI eval for the NVFP4 build ([release](https://github.com/vllm-project/vllm/releases/tag/v0.32.0rc2)). Third-party mixed-precision GGUF conversions are already trending, which usually indicates real deployment demand rather than curiosity.

On two of this slot's four criteria it is plainly ahead of the incumbent. MIT beats Z.ai's custom glm-5.3 licence, which still requires a security review for providers above $10bn in revenue, and the weights are unambiguously out. What is missing is the bit that actually decides the title: no independent evaluation in this cycle puts it ahead of GLM-5.3 on Intelligence Index or on cost per task. Artificial Analysis's visible top five this week — Gemini 4 Carbon (High) at 59, Claude Opus 5.5 at 58, GPT-6 Astra at 57 — is the overall table and contains no open-weight entries at all ([aa-models](https://artificialanalysis.ai/models)), so it tells us nothing about where DeepSeek sits against GLM-5.3.

Until an open-weights index reading lands, this stays a challenge. Mistral-Large-4-1T-A52B is in the same position: released, multilingual, but unmeasured here. If you are picking today on licence clarity alone, DeepSeek is the easier legal read.
