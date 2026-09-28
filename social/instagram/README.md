# Instagram Ingestion CLI (`social/instagram/cli.py`)

A lightweight CLI tool to extract Instagram profiles, posts, carousels, and reels via Apify into structured YAML manifests and Markdown files for TrainerTwin persona development.

---

## Prerequisites

1. Set your `APIFY_API_KEY` in `olga/.env`:
   ```bash
   APIFY_API_KEY=apify_api_...
   ```
2. Python dependencies (`httpx`, `pyyaml`, `python-dotenv`) run via `uv`.

---

## Quick Start

Run commands from the `olga` project root:

```bash
cd ~/Developers/Github/foreverlearning/olga
```

### 1. Extract Profile + Posts Balanced by Content Type

Fetches the profile and selects up to 5 posts of each type (`reel`, `carousel`, `image`):

```bash
uv run python social/instagram/cli.py all olga_sinenko.official --slug olga --max-per-type 5
```

---

### 2. Extract Profile Only

Fetches trainer identity, bio, follower stats, and link in bio:

```bash
uv run python social/instagram/cli.py profile olga_sinenko.official --slug olga
```

---

### 3. Extract Latest Posts Only

Extracts recent posts without re-fetching profile:

```bash
# Fetch latest 20 posts regardless of type:
uv run python social/instagram/cli.py posts olga_sinenko.official --max-posts 20

# Or fetch 5 of each type:
uv run python social/instagram/cli.py posts olga_sinenko.official --max-per-type 5
```

---

## Output Structure

Outputs default to `users/olga/data/instagram/`. For another person, pass `--data-dir users/<slug>/data/instagram` to every command:

```text
users/olga/data/instagram/
├── olga.yaml                    # Master manifest (profile metadata + post index)
└── posts/                       # Individual Markdown files
    ├── 2026-09-20-its-not-a-join-this.md
    ├── 2026-09-17-yes-on-my-youtube-detailed.md
    ├── 2026-09-15-tired-of-i-need-to.md
    └── ...
```

### Master Manifest Schema (`olga.yaml`)

```yaml
profile:
  id: '6444200548'
  username: olga_sinenko.official
  fullName: Olga Sinenko | Real Estate Sales Mentor
  biography: |
    11+ yrs selling Dubai real estate
    I teach to turn “Just send me some OPTIONS” into closed deals🔥
    Start with FREE Sales Training on Telegram ↓
  followersCount: 1598
  followsCount: 874
  postsCount: 362
  externalUrl: https://youtube.com/@olgasinenkorealestate
  verified: false

posts:
  - id: '3987994461602135310'
    type: reel
    date: '2026-09-17'
    url: https://www.instagram.com/p/DdYM9ViBT0O/
    likes: 18
    comments: 0
    views: 134
    file: ./posts/2026-09-17-yes-on-my-youtube-detailed.md
  - id: '3985329903603160430'
    type: carousel
    date: '2026-09-13'
    url: https://www.instagram.com/p/DdOvG6hAhVu/
    likes: 23
    comments: 5
    file: ./posts/2026-09-13-1-week-post-tony-robbins.md
```

### Post Schema (`posts/*.md`)

```markdown
---
id: '3987994461602135310'
type: reel # reel | carousel | image
date: '2026-09-17T06:20:07.000Z'
url: https://www.instagram.com/p/DdYM9ViBT0O/
likes: 18
comments: 0
views: 134
location: Dubai, United Arab Emirates
videoUrl: https://...mp4
---

## Caption
Yes - on my YouTube detailed Time management for agents!

#realestatecoachingdubai #realestateagenttraining
```

---

## CLI Options Reference

| Argument | Description | Default |
| :--- | :--- | :--- |
| `command` | Subcommand: `all`, `profile`, `posts` | *required* |
| `username` | Instagram username or profile URL | *required* |
| `--slug` | Manifest filename slug | Username |
| `--data-dir` | Output base directory | `users/olga/data/instagram` |
| `--max-per-type` | Max posts per category (`reel`, `carousel`, `image`) | `None` |
| `--max-posts` | Max total posts to scrape | `30` (or `60` with `--max-per-type`) |
| `--api-key` | Apify API token override | `APIFY_API_KEY` from `.env` |
| `-o`, `--output` | Explicit custom output path | Auto-generated in `--data-dir` |
