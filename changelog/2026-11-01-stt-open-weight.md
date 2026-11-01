---
date: 2026-11-01
slot: stt-open-weight
type: challenged
title: Voxtral Small Transcribe 3 enters the Artificial Analysis top three; ARK-ASR-3B
  holds the title
old: null
new: Voxtral Small Transcribe 3
sources:
- https://artificialanalysis.ai/speech-to-text
- https://huggingface.co/spaces/hf-audio/open_asr_leaderboard
- https://huggingface.co/Audio8/ARK-ASR-3B
---
Artificial Analysis added two Voxtral Transcribe 3 entries on 1 November 2026: Voxtral Small Transcribe 3 at #3 (2.1%) and Voxtral Mini Transcribe 3 at #5 (2.2%), behind Fun-Realtime-ASR-preview (1.7%) and MAI-Transcribe-2 (2.0%). That is the only movement in this cycle, and it does not shift the title.

Two reasons. First, the Artificial Analysis listing is tracked here as a complement covering closed models, and its percentages do not line up with Open ASR Leaderboard WER — the same problem already noted for the Qwen3.5 Omni entries, where #1 and #5 sit at 13.5% and 3.1%. You cannot read a Voxtral number against ARK's 4.76 and call it a lead.

Second, nothing in the dossier states a licence, confirms downloadable weights, or gives throughput or language coverage for either Voxtral variant. This slot requires open weights and judges on licence and language coverage, so the entry cannot be assessed against the criteria at all yet.

Meanwhile the Open ASR Leaderboard fetch of 1 November 2026 still has Edge0/ARK-ASR-3B at #1 on 4.76 mean WER, ahead of MOSS-Transcribe-preview-2B (4.87), MOSS-Transcribe-Diarize (5.17), moondream/parakeet-ultra (5.32) and Cohere Transcribe (5.42). That is the same ordering the title was awarded on, holding across five months.

The existing caveats stand: Parakeet-TDT-0.6B-v3 remains the throughput choice at 6.34% average WER under CC BY 4.0, and AutoArk's own rerun on 8x RTX 4090 lands ARK at 5.13% WER and RTFx 197, well below the board's 490.98.
