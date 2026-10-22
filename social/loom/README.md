# Loom

Loom uses the same audio-to-turns flow as YouTube:

1. Download/extract audio with yt-dlp into an OS temporary directory.
2. Upload to AssemblyAI through the central `social/transcribe.py` module.
3. Transcribe/diarize with `universal-3-5-pro`, using automatic language detection and source metadata as context (no keyterms or LLM rewrite).
4. Save validated JSON, speaker-labeled Markdown, and `speaker_count`; clean temporary downloads and delete completed provider transcripts after export. Failed jobs retain checkpoints for resume; see [cleanup limits](../README.md).

The export contract remains untimed. Publication dates are source metadata.

Loom's built-in captions/transcription API is **not used**. No GPU is needed.

## Unified collector

Run from the `olga` repository root. Publication dates are filtered from `--since` through today's UTC date.

```sh
# One share link
uv run python -m social --user olga --since 2020-01-01 \
  --loom 'https://www.loom.com/share/5912cd3e872a4a1f890a56983f4c9583'

# Existing YAML manifest, or a text file containing share URLs
uv run python -m social --user olga --since 2020-01-01 \
  --loom users/olga/data/loom/loom.yaml

# Metadata only: no audio download or paid transcription/naming calls
uv run python -m social --user olga --since 2020-01-01 \
  --loom users/olga/data/loom/loom.yaml --no-transcribe
```

`--loom` can be combined with `--youtube`, `--linkedin`, `--twitter`, and `--instagram`.

## Standalone tool

```sh
uv run python -m social.loom.cli --user olga --since 2020-01-01 \
  --source users/olga/data/loom/loom.yaml
```

Requires `yt-dlp`, `ffmpeg`, and `ASSEMBLYAI_API_KEY`. No OpenRouter key or separate speaker-naming call is used. Only accessible share links are supported; Loom folder discovery is not supported.

## Output

- Transcripts: `users/<user>/data/loom/videos/*.md`.
- Discovered metadata: `users/<user>/data/loom/collected.yaml`. The input manifest is left untouched.
- Validated provider JSON: `users/<user>/data/loom/assemblyai-json/<video-id>.json`.
- Speaker count and labels: transcript frontmatter and `collected.yaml`.

Existing complete transcripts are skipped regardless of provider. Paths and categories are preserved when rebuilding incomplete transcripts. An empty result cannot overwrite an existing transcript. Files outside the selected date window are not modified. Interrupted exports reuse saved AssemblyAI JSON; interrupted polling resumes from `assemblyai-json/<video-id>.job.json` rather than starting another paid job. Old Gemini caches are not relabeled.

Speaker separation remains a model prediction, not human-verified ground truth. Labels are generic, not guessed names. Long recordings use the batch endpoint (not Dictation's 20-minute-limited endpoint). Provider failures, model fallback, and missing/partial diarization fail explicitly instead of saving a successful transcript.
