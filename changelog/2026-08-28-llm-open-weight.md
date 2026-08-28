---
date: 2026-08-28
slot: llm-open-weight
type: challenged
title: GLM-5.3 weights land on Hugging Face, drawing level with Kimi K3 but not past
  it
old: null
new: GLM-5.3
sources:
- https://huggingface.co/zai-org/GLM-5.3
- https://x.com/kimmonismus/status/2093354978534477956
- https://x.com/kimmonismus/status/2093295691221156346
---
Z.ai's full GLM-5.3 is now downloadable: the `zai-org/GLM-5.3` repository appeared on Hugging Face's trending list on 25 August, and its public release was confirmed on 28 August alongside practical serving notes — roughly 10–12x H100 (or 8x H200) for FP8, about 390–430GB at 4-bit/NVFP4, and 230–250GB under aggressive 2-bit quantisation with quality and context trade-offs.

That closes the gap this slot flagged a month ago, when GLM-5.3 matched Kimi K3's score of 60 on the Artificial Analysis Intelligence Index but had no released weights. The "weights actually released" criterion is now satisfied. What has not changed is the quality picture: matching K3 is not beating it, and nothing in this cycle's evidence is an independent head-to-head evaluation putting GLM-5.3 ahead on the slot's stated criteria. Our bar for a title change is an independent result showing the challenger wins, so K3 keeps the slot.

Two cautions for anyone planning around this. The Hugging Face model card tags GLM-5.3 as `license:other`, not MIT — the MIT terms noted previously applied to the smaller GLM-5.3-Flash checkpoint, and the flagship's licence should be read directly before commercial use. And the local-hardware figures above come from a single social-media summary, not a measured serving benchmark, so treat them as an order-of-magnitude guide rather than a costed comparison against K3's 2.8T-parameter, 104B-active footprint.

We will revisit as soon as a third-party board publishes a separated score, or a like-for-like throughput and cost comparison, for the released GLM-5.3 checkpoint against K3.
