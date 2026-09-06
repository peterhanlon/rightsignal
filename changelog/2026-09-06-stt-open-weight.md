---
date: 2026-09-06
slot: stt-open-weight
type: challenged
title: Qwen3.5 Omni enters the Artificial Analysis STT top five; ARK-ASR-3B holds
old: null
new: Qwen3.5 Omni Flash / Plus
sources:
- https://artificialanalysis.ai/speech-to-text
- https://huggingface.co/Audio8/ARK-ASR-3B
---
Artificial Analysis' speech-to-text board reshuffled on 6 September 2026, with Qwen3.5 Omni Flash listed at #1 and Qwen3.5 Omni Plus at #2, ahead of Nova 2 Pro, Amazon Transcribe and Universal-3 Pro. Three of those five are hosted commercial services, so they are out of scope for this slot; the two Qwen3.5 Omni entries are the only plausible open-weight challengers in the listing.

They do not clear the bar. The listing gives us a rank and a percentage and nothing else: no licence, no confirmation that weights are downloadable, no throughput figure and no language coverage. The percentages as recorded are also hard to read as error rates — the #1 entry is shown at 13.5% while the #5 entry is shown at 3.1% — so whatever the board is ordering on, it is not a straight word error rate, and we will not restate those numbers as WER.

Crucially, this slot is judged on the Open ASR Leaderboard harness, where ARK-ASR-3B still holds at 4.76 mean WER with RTFx 490.98 under Apache-2.0. Nothing in today's evidence scores a Qwen3.5 Omni variant on that harness, so there is no like-for-like comparison to act on.

ARK-ASR-3B therefore keeps the title. Qwen3.5 Omni goes on the challenger list pending three things: confirmation that the weights are published under a usable licence, an Open ASR Leaderboard entry run with the leaderboard's own scorer, and a throughput number. If those land and beat 4.76, this becomes a change.
