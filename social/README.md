# Social collection

Run from the repository root. Give one or more **profile/channel HTTPS URLs**, a person's folder slug, and an **absolute inclusive UTC publication date**. The upper bound is today's UTC date. Choose yesterday's date for roughly a day, a date seven days ago for a week, etc.; use an explicit calendar date for a month or year. There is no rolling-duration flag.

```sh
uv run python -m social --user jane-doe --since 2026-08-01 \
  --linkedin 'https://www.linkedin.com/in/janedoe/' \
  --twitter 'https://x.com/janedoe' \
  --instagram 'https://www.instagram.com/janedoe/' \
  --youtube 'https://www.youtube.com/@janedoe'

uv run python -m pipeline --user jane-doe index --model openai/gpt-oss-120b --provider Cerebras
```

You can omit unavailable platforms. Requires the corresponding keys in `.env`: `HARVEST_API_KEY`, `TWITTER_API_KEY`, `APIFY_API_KEY`, and **`ASSEMBLYAI_API_KEY` for all audio/video transcription**. Audio extraction needs `yt-dlp` and `ffmpeg`. **`social/transcribe.py` is the only transcription implementation**, including downloads, upload/polling, validation, caching, concurrency, and transcript export. It uses AssemblyAI `universal-3-5-pro` with speaker labels, automatic language detection, and a context `prompt` derived from source titles/descriptions/captions. No keyterms or LLM rewriting are used. A provider fallback to another model fails explicitly rather than being mislabeled. Gemini remains only in `social/gemini.py` for image OCR (OpenRouter primary, direct Google fallback), and in the separate text/indexing pipeline.

Exports keep the existing untimed speaker-turn format; `speaker_count` comes from distinct IDs (0 for explicit no-speech results). Media downloads live only in OS temporary directories and are cleaned up after processing; local file inputs are never deleted. Completed provider transcripts are deleted after validation/cache export (deletion failures warn without losing saved text). Failures keep job checkpoints for inspection/resume; they may leave a provider-side job until resumed or explicitly deleted. Validated JSON goes to `assemblyai-json/<video-id>.json`, with in-flight IDs in `<video-id>.job.json`. Re-running after interrupted polling reuses that ID and verifies media/settings instead of submitting again. A timeout during the initial paid POST cannot be automatically reconciled; check the provider dashboard before resubmitting. Existing complete Markdown—including old providers—is preserved, but old Gemini JSON is not reused or relabeled as AssemblyAI output. To deliberately re-transcribe, back up/remove the Markdown and the matching AssemblyAI cache/checkpoint. Collection costs money.

LinkedIn comments on selected posts and Instagram's provided latest comments are included. X followers/following, mentions, standalone thread context and articles are not included in the unified date-bound run; use the standalone X CLI for those extras. YouTube video metadata is checked per selected video for descriptions and missing dates; transcripts go to `data/youtube/video/*.md` and the manifest to `data/youtube/<slug>.yaml`. `--no-transcribe` saves only the dated YouTube/Loom video index (not transcript evidence).

For a local audio **or video** file, use the same central module (original preserved):

```sh
uv run python -m social.transcribe recording.mp4 --context 'A sales coaching conversation.' \
  --output users/jane-doe/data/assemblyai-json/recording.json
```

The cutoff governs **newly collected dated content**, not undated profile fields. Existing files from an earlier/wider run are **not deleted**; use a fresh slug/workspace if you need an isolated window for analysis. A provider's pagination/history limit or unavailable publication dates may prevent full coverage. Invalid/missing dates stop the bounded run rather than silently accepting an unbounded post. Review source counts before claiming completeness.

## Loom audio transcripts

Loom shares the YouTube transcription flow: **temporary audio → AssemblyAI → speaker-labeled text**. It does not use Loom's built-in captions.

```sh
uv run python -m social --user olga --since 2020-01-01 \
  --loom 'https://www.loom.com/share/5912cd3e872a4a1f890a56983f4c9583'

uv run python -m social --user olga --since 2020-01-01 \
  --loom users/olga/data/loom/loom.yaml
```

`--loom` accepts a share URL or a text/YAML file containing share links, and can be combined with the other platform flags. Transcripts go to `data/loom/videos/`. Existing complete transcripts, including legacy providers, are skipped; remove a transcript and its cached JSON deliberately if you want a new paid transcription. `--no-transcribe` saves metadata only. See [the Loom tool](loom/README.md) for limits and the standalone command.

## Parallelism

YouTube/Loom transcription jobs (download + upload + AssemblyAI job) run in parallel, N videos at a time with `--workers` (default: 2). Each job downloads into its own OS temp directory, so per-video failures never block the others; all failures are reported and the command then exits nonzero. Rate-limit `--workers` to match your AssemblyAI concurrency quota.

## Progress output

Selected platforms run concurrently (one worker per platform); each still writes only its own data directory. Terminals show a fixed `tqdm` row for each platform's completed stages, with a separate item-level row for its current work. Redirected output and background runs use newline-only progress updates (first item, every 10 items or after 15 seconds between completed items, and a final summary). Everything goes to stderr, leaving stdout available for YAML/JSON output.

Stages include profile discovery, post collection, enrichment/export, and YouTube/Loom metadata/download/transcription. Item-level counts show **items processed**, not successful downloads or transcriptions; the stage percentage is not a time estimate. Waiting on a provider is explicitly labeled; no fabricated percentage is shown while AssemblyAI or Apify processes a request. A failure in one platform does not cancel the others, but the overall command exits unsuccessfully once all workers finish.

For single-platform operations such as comments on an individual post, thread context, or standalone AssemblyAI transcription, the standalone tools remain available at `social/{linkedin,twitter,instagram,youtube,loom}/cli.py` (each has its own `README.md`).
