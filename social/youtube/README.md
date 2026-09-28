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
*(Tracks job IDs in `users/olga/data/youtube/sarvam-jobs.json` by default)*

#### Step B: Wait and download outputs
```bash
uv run python social/youtube/cli.py transcribe --wait
```
*(Polls job status, downloads raw diarized JSONs to the selected YouTube data directory, and compiles YAML transcripts)*

#### Step C: Rebuild clean YAML transcripts only (offline)
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
├── olga.yaml                    # Master video manifest
├── transcripts/                 # Formatted YAML transcripts (used by TrainerTwin pipeline)
│   ├── 01.yaml
│   ├── 02.yaml
│   └── ...
users/olga/audios/               # Downloaded audio MP3s
users/olga/data/youtube/sarvam-json/  # Raw Sarvam diarized JSON outputs
users/olga/data/youtube/sarvam-jobs.json  # State tracker for batch job IDs
```

### Transcript Schema (`transcripts/*.yaml`)

Directly ingested by `pipeline/`:

```yaml
id: '01'
title: 2025 Dubai Real Estate Market Correction...
source: 2025 Dubai Real Estate Market Correction...
audio_file: 2025 Dubai Real Estate Market Correction.mp3
duration: "00:21:44"
model: saaras:v3
raw_speaker_ids:
  - '0'
  - '1'
counts:
  raw_entries: 75
turns:
  - t: "00:00:08"
    speaker: '1'
    text: >-
      Okay, we are on uh property monitor platform and this platform as I mentioned
      available only for real estate professionals...
```

---

## CLI Options Reference

| Argument | Description | Default |
| :--- | :--- | :--- |
| `command` | Subcommand: `list`, `download`, `transcribe`, `all` | *required* |
| `url` | YouTube video, playlist, or channel URL | *required for list/download/all* |
| `--slug` | Manifest filename slug | `channel` / `youtube` |
| `--data-dir` | Output base directory | `users/olga/data/youtube` |
| `--audios-dir` | Directory containing audio files | `users/olga/audios` |
| `--max-videos` | Limit number of videos | `None` (all) |
| `--api-key` | Sarvam AI API key override | `SARVAM_API_KEY` from `.env` |
| `-o`, `--output` | Explicit custom manifest output path | Auto-generated in `--data-dir` |
