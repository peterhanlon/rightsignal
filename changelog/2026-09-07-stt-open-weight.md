---
date: 2026-09-07
slot: stt-open-weight
type: challenged
title: Microsoft's VibeVoice-ASR-Streaming-7B logged as an unverified challenger;
  ARK-ASR-3B holds
old: null
new: microsoft/VibeVoice-ASR-Streaming-7B
sources:
- https://huggingface.co/microsoft/VibeVoice-ASR-Streaming-7B
- https://huggingface.co/Audio8/ARK-ASR-3B
- https://arxiv.org/abs/2609.04404
- https://arxiv.org/abs/2609.04260
- https://arxiv.org/abs/2609.04225
---
No change this week. The bulk of the incoming evidence is literature rather than evaluation: papers on ASR hallucination under environmental degradation, a word-level backdoor attack (GhostWord), turn-aware streaming supervision, a trilingual spoken-dialogue fact-checking benchmark, and a Mandarin-English code-switching dataset. Interesting reading, but none of it scores a model against the criteria this slot is judged on, so none of it moves ARK-ASR-3B.

The one item worth recording is microsoft/VibeVoice-ASR-Streaming-7B, which appeared on Hugging Face's trending list on 2 September 2026. From the listing we can see it is an automatic-speech-recognition pipeline tagged for streaming and for four languages (en, zh, es, pt). That is the whole of the public signal. There is no independent leaderboard result, no reported throughput, and the listing surfaces no licence — and without a licence you cannot even confirm it belongs in an open-weight slot, let alone whether it beats a 4.76 mean WER at RTFx 490.98.

A streaming 7B from Microsoft is plausibly relevant to voice-agent workloads where latency, not batch WER, decides the design. But this slot ranks on independent WER first, and until the model is scored with the Open ASR Leaderboard's own harness there is nothing to compare. It joins the existing challenger list on the same terms as Orze-ASR-3Way: a repo exists, a claim does not. Check the card yourself for licence terms before building against it.
