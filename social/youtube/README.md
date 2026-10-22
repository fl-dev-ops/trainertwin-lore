# YouTube collection and AssemblyAI transcription

Requires `ASSEMBLYAI_API_KEY` in `.env`, `yt-dlp`, and `ffmpeg`. Every media download and transcription delegates to **`social/transcribe.py`**, using AssemblyAI Universal-3.5 Pro via HTTP. No Google SDK or OpenRouter key is needed for transcription.

## Commands

```sh
# Metadata only (channel, playlist, or single video)
uv run python social/youtube/cli.py list 'https://www.youtube.com/@olgasinenko' --max-videos 50 --slug olga

# Full collection: discovery, temporary audio, AssemblyAI, Markdown
uv run python social/youtube/cli.py all 'https://www.youtube.com/@olgasinenko' --max-videos 10 --slug olga

# One video
uv run python social/youtube/cli.py transcribe 'https://www.youtube.com/watch?v=VIDEO_ID'

# Rebuild Markdown from saved AssemblyAI JSON offline
uv run python social/youtube/cli.py transcribe --build

# Date-bounded collector; parallel transcription jobs
uv run python -m social --user olga --since 2020-01-01 \
  --youtube 'https://www.youtube.com/@olgasinenko' --workers 10
```

The old `download`, `--audios-dir`, `--submit`, and `--wait` workflow is removed. Downloads live only in OS temporary directories, cleaned after processing even on failure. Completed AssemblyAI transcripts are deleted remotely after validation/cache export; failures retain checkpoints for resume. See [the shared transcription contract](../README.md) for failure/cleanup limits.

For login/bot-blocked videos, explicitly opt into your local browser cookies for a run:

```sh
YT_DLP_COOKIES_FROM_BROWSER=safari uv run python social/youtube/cli.py transcribe 'https://www.youtube.com/watch?v=VIDEO_ID'
```

This lets yt-dlp read Safari cookies without exporting a cookie jar. `YT_DLP_COOKIES` (an existing jar) takes precedence if both are set. macOS may require granting access to Safari's cookie store; no permission bypass is attempted.

## Output

Defaults to `users/olga/data/youtube/`; override with `--data-dir`. `--api-key` overrides `ASSEMBLYAI_API_KEY`; `-o/--output` overrides the manifest path.

- `<slug>.yaml`: video metadata and, once transcribed, `model`, `speakers`, `speaker_count`.
- `assemblyai-json/<video-id>.json`: validated speaker turns; reused on export interruptions.
- `assemblyai-json/<video-id>.job.json`: pending job ID/settings/media hash, used to resume polling without another paid submission.
- `video/YYYY-MM-DD-title-<video-id>.md`: spoken text, numeric speaker IDs/labels, and source metadata.

`universal-3-5-pro` does recognition and diarization, with automatic language detection and contextual `prompt` from source metadata. No hand-authored keyterms, separate speaker-naming calls, or LLM rewrite are used. Unsupported/model-fallback results are rejected, not silently labeled as Universal-3.5 Pro.

The existing export contract stays untimed. Speaker count is derived from IDs, not inferred identities. Generic `Speaker 1`, `Speaker 2`, etc. are used; names are not guessed from metadata. Markdown still goes through the existing transcript normalizer; the JSON cache retains provider turn text before that formatting step.

Existing complete Markdown stays unchanged regardless of model, including bracketed legacy filenames. Old Gemini caches are not rebuilt as AssemblyAI output. To deliberately re-transcribe, back up/remove the Markdown and corresponding AssemblyAI cache/checkpoint. Explicit silent results save `speaker_count: 0`; empty output cannot overwrite an existing transcript. Missing or partial diarization fails without overwriting speech. Speaker accuracy and speech coverage remain model predictions, not verified ground truth.
