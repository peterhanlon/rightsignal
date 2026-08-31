---
date: 2026-08-31
slot: llm-open-weight
type: challenged
title: DeepSeek-V4-Flash-Vision-Exp lands under MIT; Kimi K3 keeps the open-weight
  title
old: null
new: DeepSeek-V4-Flash-Vision-Exp
sources:
- https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-Vision-Exp
- https://huggingface.co/orcarouter/Qwen3.8-Flash-Next-Uncensored-GGUF
---
An experimental member of the DeepSeek V4 family, `deepseek-ai/DeepSeek-V4-Flash-Vision-Exp`, appeared on the Hugging Face trending list on 31 August with safetensors weights, fp8 and 8-bit variants, an image-text-to-text pipeline, eval-results tags and — notably — an MIT licence ([model card](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-Vision-Exp)). On licence and "weights actually released", that is stronger than the incumbent: Kimi K3 ships under Moonshot's own custom terms with attribution and MaaS conditions above certain thresholds.

It does not take the title. This is a Flash-class, explicitly experimental checkpoint, and nothing in the current evidence gives it an independent head-to-head score against K3 or against the GLM-5.3 weights already logged as a challenger. Flash-tier releases from every lab so far trade quality for serving cost, and serving cost is only one of four criteria here. We would want an Artificial Analysis-style Intelligence Index placement, or another third-party evaluation, on the downloadable weights before treating a V4 checkpoint as the frontier open-weight model.

Also in the dossier and not moving the needle: `orcarouter/Qwen3.8-Flash-Next-Uncensored-GGUF`, a community abliterated quantisation of an existing Flash-class Qwen rather than a new model ([listing](https://huggingface.co/orcarouter/Qwen3.8-Flash-Next-Uncensored-GGUF)).

Kimi K3 therefore holds the slot, still on the strength of being the highest-scoring thing you can download, and still with the same caveats: enormous to self-host and slow in practice. The interesting question for the next few weeks is whether a full, non-experimental DeepSeek V4 arrives under the same MIT terms.
