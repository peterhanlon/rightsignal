---
date: 2024-09-05
slot: inference-serving
type: milestone
title: 'vLLM v0.6.0: the performance overhaul'
old: null
new: null
sources:
- https://vllm.ai/blog/2024-09-05-perf-update
---
The CPU-side bottlenecks get attacked — API server split from the engine over ZMQ, multi-step scheduling, async output processing — for 2.7x throughput and 5x faster time-per-output-token on Llama 3 8B.

*Recorded retrospectively in the August 2026 backfill.*
