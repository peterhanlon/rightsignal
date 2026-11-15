---
date: 2026-11-15
slot: tts-open-weight
type: challenged
title: Fish Audio Drama 3 challenges BreezeBlue Breeze TTS 2 Open Weights for best
  open-weight tts
old: null
new: Fish Audio Drama 3
sources:
- https://artificialanalysis.ai/text-to-speech/arena
- https://huggingface.co/BreezeBlue/Breeze-TTS-2
- https://fish.audio/
---
Fish Audio Drama 3 would take this title on today's evidence, but the case has not yet cleared our bar for a change, so it is recorded as the challenger for now. The adjudicator's reasoning:

Breeze TTS 2 took this slot in September on the strength of being the top open-weight entry on the Artificial Analysis provider-voice board. That is no longer true on the live board. Breeze now reads 1228 Elo, 14th overall and only third among open-weight models, behind Fish Audio Drama 3 (1275) and Drama 3 Preview (1241). On the controlled-voice arena Breeze sits at 1019, fourth among open-weight models behind Drama 3 (1073), Ming-3.0-tts (1067) and Drama 3 Preview (1060). Drama 3 leads on both arenas, and Artificial Analysis names it the #1 open-weights model on both; our own standings snapshot puts it 7th overall at 1275 with Breeze outside the top ten. That is a lead on the slot's principal quality criterion, corroborated across two boards, so the title moves.

Two things to weigh before you deploy it. Licence: the Fish Audio Community Licence v1.0 is free commercially below US$500k annual revenue, but it grants no rights to offer Drama 3 as a hosted service to third parties at any revenue level, so an API product needs a separate written agreement. Hardware: it is a 35B-parameter mixture-of-experts model with roughly 3B active per token and FP8 experts, and launch-day self-hosting reports cluster around 39-48 GB of VRAM, or about 32 GB on community 4-bit builds. Breeze, by comparison, fits in roughly 7.7 GiB eager (12 GB practical floor), so it stays listed as the small-card challenger despite the restrictive weights licence. Latency for Drama 3 is not independently documented in our sources. If you need unconditional commercial terms, MIT-licensed Ming-3.0-tts (1187) and Apache-2.0 Step Audio EditX (1101) remain the fallbacks.
