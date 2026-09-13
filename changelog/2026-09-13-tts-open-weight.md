---
date: 2026-09-13
slot: tts-open-weight
type: challenged
title: 'Breeze TTS 2 slips to #9 as StepAudio 2.5 TTS edges ahead'
old: null
new: StepFun StepAudio 2.5 TTS (Aug 2026)
sources:
- https://huggingface.co/BreezeBlue/Breeze-TTS-2
- https://huggingface.co/tencent/AuK
---
The pick has lost ground. On the Artificial Analysis provider-voice board (fetched 13 September) BreezeBlue Breeze TTS 2 Open Weights reads 1202 Elo at #9, down from the 1215 and 7th place that won it the title on 9 September. Sitting just above it at 1207 is StepFun StepAudio 2.5 TTS (Aug 2026), with the rest of the top ten — Cartesia Sonic 3.6 (1276), Inworld Realtime TTS-2 (1243), Speechify Simba 3.2 (1237), Qwen-Audio-3.0-TTS-Plus (1234), VUI Luna (1228), Gemini 3.1 Flash TTS, ElevenLabs v3 — either hosted-only or unconfirmed for downloadable weights.

StepFun is the obvious challenger: the Step-Audio line already appears in this slot's caveats as the Apache-2.0-coded option self-hosters fall back on. But we have nothing in front of us confirming that checkpoints for the 2.5 TTS release have actually shipped, nor its licence terms, time-to-first-audio or VRAM footprint — all stated criteria here. A five-point Elo gap on one board at one refresh is also thin corroboration. That is a challenge, not a handover.

Also newly ingested: tencent/AuK is trending on Hugging Face as a text-to-speech pipeline with zero-shot cloning, editing and separation tags, but carries no independent quality or latency measurement yet, so it changes nothing today.

Breeze TTS 2 keeps the title on its verified package — sub-40ms first audio, 0.32 RTF on a warmed H100, ~7.7 GiB eager inference — with the standing caveat that the weights remain research/non-commercial. We will revisit as soon as StepAudio 2.5's weights and licence are pinned down or the board reading holds.
