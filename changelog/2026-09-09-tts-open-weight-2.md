---
date: 2026-09-09
slot: tts-open-weight
type: changed
title: Breeze TTS 2 Open Weights takes best open-weight TTS from Fish Audio S2 Pro
old: Fish Audio S2 Pro
new: BreezeBlue Breeze TTS 2 Open Weights
sources:
- https://artificialanalysis.ai/text-to-speech/arena?tab=leaderboard
- https://huggingface.co/BreezeBlue/Breeze-TTS-2
- https://huggingface.co/fishaudio/s2-pro
---
Fish Audio S2 Pro has held this slot since March, but the Artificial Analysis provider-voice board no longer supports it. In the 9 September standings the pick sits at 1128 Elo in 25th place and is out of the top ten, while BreezeBlue's Breeze TTS 2 Open Weights is 7th at 1215 and the highest-placed open-weight model on the board. That is an 87-point gap on the slot's principal quality measure, not a rounding error, and the weights have been public on Hugging Face since 25 August 2026.

Breeze also wins the remaining criteria. BreezeBlue quotes under 40ms time-to-first-audio and 0.32 RTF on a warmed-up H100, against roughly 100ms first audio and 0.195 RTF on an H200 for S2 Pro, and it needs about 7.7 GiB for eager inference, so a 12GB card will do rather than H200-class kit. On licence there is no gain and no loss: Breeze's inference code is Apache 2.0 but the checkpoints carry a research-and-non-commercial licence, exactly as restrictive as the Fish Audio Research License. Commercial deployment still needs a separate agreement in both cases.

Two caveats worth weighing before you swap. Breeze covers English and Chinese only, where S2 Pro spans 80-plus languages; if you need broad language coverage the old pick remains the better tool despite the Elo gap. And Step-Audio-EditX, at 1104 Elo, is behind both but keeps the loosest code licensing, so it stays the fallback for self-hosters who must ship commercially.
