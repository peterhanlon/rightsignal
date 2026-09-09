---
date: 2026-09-09
slot: llm-open-weight
type: challenged
title: GLM-5.3 replaces Kimi K3 as best open-weight LLM
old: null
new: GLM-5.3
sources:
- https://artificialanalysis.ai/models
---
Artificial Analysis now lists GLM-5.3 (max) at 45 on its Intelligence Index, one point ahead of Kimi K3 (max) at 44 — the reverse of the 50-vs-49 reading that put K3 in this slot in July ([AA models](https://artificialanalysis.ai/models)).

Treat the quality gap as a tie: one point, in opposite directions across the two readings, is inside the noise. What settles it is the rest of the slot's criteria. GLM-5.3's full weights went public on Hugging Face between 25 and 28 August, so the availability objection that kept it as a challenger is gone. On cost and speed it is not close: roughly $0.9 per Index task against K3's $2.3, and about 84 tokens per second against K3's 41. K3 keeps the bigger context window and native vision, and it remains a serious model, but paying more than twice as much for half the throughput to score level is no longer defensible.

Licence is a wash rather than a win. GLM-5.3 is tagged 'other' on Hugging Face, not MIT; K3 shipped under Moonshot's own custom terms with attribution and MaaS conditions attached. Both need reading before commercial deployment.

The other open-weight contenders stay behind. DeepSeek-V4-Flash-Vision-Exp scores 42 and is an explicitly experimental Flash-class checkpoint, though its ~168GB FP8/FP4 footprint makes it much the easiest to self-host. GLM-5.3-Flash also sits at 42, MIT-licensed, and is the sensible pick if you need something small and permissive.

Self-hosting GLM-5.3 is still rack-scale work: reported local serving needs 8x H200 or 10-12x H100 at FP8.
