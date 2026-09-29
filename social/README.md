# Social collection

Run from the repository root. Give one or more **profile/channel HTTPS URLs**, a person's folder slug, and an **absolute inclusive UTC publication date**. The upper bound is today's UTC date. Choose yesterday's date for roughly a day, a date seven days ago for a week, etc.; use an explicit calendar date for a month or year. There is no rolling-duration flag.

```sh
uv run python -m social --user jane-doe --since 2026-08-01 \
  --linkedin 'https://www.linkedin.com/in/janedoe/' \
  --twitter 'https://x.com/janedoe' \
  --instagram 'https://www.instagram.com/janedoe/' \
  --youtube 'https://www.youtube.com/@janedoe'

uv run python -m pipeline --user jane-doe ingest --model openai/gpt-4o
uv run python -m pipeline --user jane-doe build --model openai/gpt-4o
uv run python -m pipeline --user jane-doe analyze
uv run python -m pipeline --user jane-doe lint
```

You can omit unavailable platforms. Requires the corresponding API keys in `.env` (`HARVEST_API_KEY`, `TWITTER_API_KEY`, `APIFY_API_KEY`, and `SARVAM_API_KEY` when transcribing YouTube), plus `yt-dlp` and `ffprobe` for YouTube. The collector saves profile snapshots and **dated posts/tweets/video transcripts** under `users/<slug>/data/<channel>/`; YouTube audio is under `users/<slug>/audios/<since>/<channel-hash>/`. LinkedIn comments on selected posts and Instagram's provided latest comments are included. X followers/following, mentions, standalone thread context and articles are not included in the unified date-bound run; use the standalone X CLI for those extras. YouTube video metadata is checked per selected video for descriptions, and for missing publication dates; transcripts go to `data/youtube/video/*.md` and the manifest to `data/youtube/<slug>.yaml`. `--no-transcribe` saves only the dated YouTube video index (not usable as transcript evidence). Collection/transcription can be slow and cost money.

The cutoff governs **newly collected dated content**, not undated profile fields. Existing files from an earlier/wider run are **not deleted**; use a fresh slug/workspace if you need an isolated window for analysis. A provider's pagination/history limit or unavailable publication dates may prevent full coverage. Invalid/missing dates stop the bounded run rather than silently accepting an unbounded post. Review source counts before claiming completeness.

For single-platform operations such as comments on an individual post, thread context, or manual Sarvam jobs, the standalone tools remain available at `social/{linkedin,twitter,instagram,youtube}/cli.py` (each has its own `README.md`).
