---
date: 2023-09-12
slot: embeddings
type: changed
title: bge-large-en-v1.5 takes best text embeddings
old: OpenAI text-embedding-ada-002
new: bge-large-en-v1.5
sources:
- https://huggingface.co/BAAI/bge-large-en-v1.5
---
The first open model you could swap in for ada-002 and simply win: MTEB average 64.23 against 60.99, retrieval 54.29 against 49.25, at 335M parameters under MIT — one cheap GPU, no per-token bill. The era of the default OpenAI embedding ends here.

*Recorded retrospectively in the August 2026 backfill.*
