---
date: 2026-10-31
slot: embeddings
type: challenged
title: EmbeddingGemma 2 logged as a challenger; Nemotron-3-Embed-8B holds the embeddings
  title
old: null
new: EmbeddingGemma 2
sources:
- https://deepmind.google/blog/embeddinggemma-2-an-open-lightweight-multimodal-embedding-model/
- https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B
- https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-4GB
- https://huggingface.co/nvidia/Nemotron-3-Embed-8B-BF16
---
Nemotron-3-Embed-8B keeps the title. Nothing in this round's evidence puts a named rival ahead of it on the slot's principal criteria — RTEB/MTEB retrieval.

The one item worth recording is Google DeepMind's announcement of **EmbeddingGemma 2**, published on 6 October 2026 and billed as an open, lightweight multimodal embedding model ([DeepMind blog](https://deepmind.google/blog/embeddinggemma-2-an-open-lightweight-multimodal-embedding-model/)). An open-weight release from that lab is relevant here, and the "lightweight" framing speaks directly to our dimension/cost criterion. But the post is vendor material and the dossier carries no RTEB or MTEB retrieval numbers for it, no task counts and no independent board placing. That is a single, non-independent source: enough to list as a challenger, nowhere near enough to move a title. We will pull the live RTEB(beta) and MTEB tables once it appears on them and revisit.

The other two items ingested against this slot are not embedding models at all: [Nemotron-3.5-Transcribe-30B-A4B](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B) is speech recognition and translation, and [Nemotron-3.5-Bolt-E4B-4GB](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-4GB) is text generation. Neither bears on retrieval quality.

The standing caveats on the incumbent still apply. Its 78.46 RTEB average comes from a vendor snapshot of a 16-task open view, while the live RTEB(beta) multilingual board lists 30 tasks across 22 languages and ranks by Borda count, with the private column removed since January 2026. Quote the basis, not just the number.
