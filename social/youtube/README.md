# YouTube Ingestion & Transcription CLI (`social/youtube/cli.py`)

A unified CLI tool to extract YouTube channel metadata, download audio MP3s, and run batch diarized speech-to-text transcription with Sarvam AI (`saaras:v3`) for TrainerTwin persona development.

---

## Prerequisites

1. Set your `SARVAM_API_KEY` in `olga/.env`:
   ```bash
   SARVAM_API_KEY=sk_10d1wop5_...
   ```
2. System tools: `yt-dlp` and `ffprobe` (for duration extraction).
3. Python dependencies: `sarvamai`, `pyyaml`, `python-dotenv` (managed via `uv`).

---

## Quick Start

Run commands from the `olga` project root:

```bash
cd ~/Developers/Github/foreverlearning/olga
```

### 1. List Channel Videos & Metadata (`list`)

Extracts video IDs, titles, durations, and view counts without downloading media:

```bash
# Channel or playlist URL:
uv run python social/youtube/cli.py list "https://www.youtube.com/@olgasinenko" --slug olga --max-videos 50
```

Saves the master video index to `users/olga/data/youtube/{slug}.yaml` by default.

---

### 2. Download Video Audio as MP3 (`download`)

Downloads the highest quality audio stream converted to MP3:

```bash
# Single video:
uv run python social/youtube/cli.py download "https://www.youtube.com/watch?v=VIDEO_ID"

# Full channel / playlist:
uv run python social/youtube/cli.py download "https://www.youtube.com/@olgasinenko"
```

Files default to `users/olga/audios/` (or specify `--audios-dir users/<slug>/audios`).

---

### 3. Transcribe with Sarvam AI (`transcribe`)

The Sarvam workflow batches up to 20 files per API job with speaker diarization (`with_diarization=True`) and word timestamps.

#### Step A: Submit batch jobs
```bash
uv run python social/youtube/cli.py transcribe --submit
```
*(Tracks job IDs in `users/olga/audios/sarvam-jobs.json` by default.)*

#### Step B: Wait and download outputs
```bash
uv run python social/youtube/cli.py transcribe --wait
```
*(Polls job status, downloads raw diarized JSONs under `audios/`, and compiles Markdown transcripts.)*

#### Step C: Rebuild Markdown transcripts only (offline)
Re-runs chunk restitching (joining sentences split at 30-second model boundaries) without making API calls:
```bash
uv run python social/youtube/cli.py transcribe --build
```

---

### 4. End-to-End Pipeline (`all`)

Runs the entire workflow sequentially (list -> download -> submit -> wait -> build):

```bash
uv run python social/youtube/cli.py all "https://www.youtube.com/@olgasinenko" --max-videos 10 --slug olga
```

---

## Output Structure

Outputs default to `users/olga/data/youtube/` and `users/olga/audios/`. For another person, pass both `--data-dir users/<slug>/data/youtube` and `--audios-dir users/<slug>/audios` to every relevant command:

```text
users/olga/data/youtube/
├── olga.yaml                    # Master video manifest (including descriptions when available)
└── video/
    └── YYYY-MM-DD-title-pQCLpcXSx2s.md
users/olga/audios/               # Audio, uploads, Sarvam jobs/raw JSON, date cache
users/olga/audios/runs/<since>/  # Date-bounded collection job state
```

### Transcript Schema (`video/*.md`)

Directly ingested by `pipeline/`; description stays in frontmatter, not spoken evidence. Existing YAML transcripts are **not** moved automatically: migrate and rebuild their workspace manifests before ingesting new Markdown copies of the same videos.

```markdown
---
id: pQCLpcXSx2s
title: 4 Questions That Kill Your Dubai Real Estate Deals in 2026
date: '2026-08-13'
url: https://www.youtube.com/watch?v=pQCLpcXSx2s
description: Video description, if available
duration: 00:17:48
model: saaras:v3
transcript: true
---

# 4 Questions That Kill Your Dubai Real Estate Deals in 2026

## Transcript

### 00:00:08 · Speaker 1

Spoken transcript text...
```

---

## CLI Options Reference

| Argument | Description | Default |
| :--- | :--- | :--- |
| `command` | Subcommand: `list`, `download`, `transcribe`, `all` | *required* |
| `url` | YouTube video, playlist, or channel URL | *required for list/download/all* |
| `--slug` | Manifest filename slug | User directory name |
| `--data-dir` | Output base directory | `users/olga/data/youtube` |
| `--audios-dir` | Directory containing audio files | `users/olga/audios` |
| `--max-videos` | Limit number of videos | `None` (all) |
| `--api-key` | Sarvam AI API key override | `SARVAM_API_KEY` from `.env` |
| `-o`, `--output` | Explicit custom manifest output path | Auto-generated in `--data-dir` |
