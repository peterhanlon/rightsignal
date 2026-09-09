---
date: 2026-09-09
slot: tts-open-weight
type: challenged
title: Breeze TTS 2 Open Weights replaces Fish Audio S2 Pro as best open-weight TTS
old: null
new: BreezeBlue Breeze TTS 2 Open Weights
sources:
- https://artificialanalysis.ai/text-to-speech
- https://huggingface.co/fishaudio/s2-pro
---
The Artificial Analysis provider-voice arena has settled the question. BreezeBlue Breeze TTS 2 Open Weights now sits at #7 overall on 1215 Elo — the highest-placed open-weights model on the board — while Fish Audio S2 Pro has fallen out of the top ten altogether. That is not a one-off reading: the same board had Breeze at 1,220 against 1,125 for S2 Pro shortly after the weights went up on Hugging Face on 25 August 2026, and the gap has held through today's fetch.

Breeze also takes the two engineering criteria. BreezeBlue quotes under 40ms time-to-first-audio on an H100 with roughly 7.7GiB for eager inference, a 12GB GPU minimum and 24GB for the fast path; S2 Pro's quoted ~100ms first audio and 0.195 RTF assume an H200-class card. On licence there is nothing to choose between them: Breeze ships Apache-2.0 inference code but puts weights, derivatives and self-hosted outputs under the BreezeBlue Research and Non-Commercial Licence, needing written authorisation from RESONIA — the same blocker as the Fish Audio Research License.

Two caveats stay on the record. Breeze is English and Chinese only, a sharp narrowing from S2 Pro's 80+ languages; if you need broad multilingual coverage, the old pick is still the one to reach for. And if you need to ship commercially from self-hosted weights, neither of these helps you — Step-Audio-EditX, at 1104 Elo and Apache-2.0 on the repository code (though with no licence file on the weights repo), remains the least restrictive on paper and runs in 12GB of VRAM.
