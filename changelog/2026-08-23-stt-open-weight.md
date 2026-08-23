---
date: 2026-08-23
slot: stt-open-weight
type: challenged
title: 'Orze-ASR-3Way takes #1 on Open ASR; ARK-ASR-3B holds the title pending licence
  checks'
old: null
new: bosonai/Orze-ASR-3Way
sources:
- https://huggingface.co/datasets/hf-audio/open-asr-leaderboard
- https://artificialanalysis.ai/speech-to-text
- https://huggingface.co/Audio8/ARK-ASR-3B
---
The Open ASR leaderboard has a new leader: bosonai/Orze-ASR-3Way at 3.81 mean WER, ahead of ARK-ASR-3B on 4.76, MOSS-Transcribe-preview-2B on 4.87, MOSS-Transcribe-Diarize on 5.17 and Cohere Transcribe on 5.42 ([Open ASR](https://huggingface.co/datasets/hf-audio/open-asr-leaderboard)). That is close to a full WER point over the current pick, measured by an independent scorer rather than a vendor card, so it is a serious challenge on the slot's first criterion.

It is not yet enough to take the title. This slot judges licence and language coverage alongside WER, and we have no confirmation of Orze's licence terms, weight release or language list, nor any throughput figure. ARK's case here was never a single number — it was Apache-2.0 plus 19 languages plus competitive accuracy — and swapping it out on a leaderboard row alone would be the sort of move this tracker exists to avoid. We will revisit once the model card and an independent throughput run are available.

One useful correction in the same update: ARK-ASR-3B now appears on the leaderboard in its own right at 4.76, which retires the standing caveat that its numbers were card-derived rather than board-verified. The figure sits between the card's claimed 5.04% and AutoArk's rerun at 5.13%, and slightly ahead of both.

The Artificial Analysis speech-to-text movement this week — Fun-Realtime-ASR-preview at 1.7%, Scribe v2, the Azure MAI-Transcribe pair and Smallest AI Pulse Pro ([AA](https://artificialanalysis.ai/speech-to-text)) — is all commercial API territory and does not bear on an open-weight slot.
