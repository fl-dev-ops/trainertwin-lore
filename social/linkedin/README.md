# LinkedIn Ingestion CLI (`social/linkedin/cli.py`)

A lightweight CLI tool to extract LinkedIn profiles, posts, and comments via HarvestAPI and export them directly into structured YAML and Markdown for TrainerTwin knowledge ingestion.

---

## Prerequisites

1. Set your `HARVEST_API_KEY` in `olga/.env`:
   ```bash
   HARVEST_API_KEY=your_harvest_api_key_here
   ```
2. Dependencies (`httpx`, `pyyaml`, `python-dotenv`) are installed via `uv`.

---

## Quick Start

Run all commands from the `olga` project root using `uv run`:

```bash
cd ~/Developers/Github/foreverlearning/olga
```

### 1. Extract Everything (Profile + All Posts)

Fetches the complete profile, paginates through all posts, writes individual Markdown files, and generates the master manifest:

```bash
uv run python social/linkedin/cli.py all https://www.linkedin.com/in/olgasi/ --slug olga
```

With work email lookup:
```bash
uv run python social/linkedin/cli.py all olgasi --slug olga --find-email
```

Fetch only the latest N posts:
```bash
uv run python social/linkedin/cli.py all olgasi --slug olga --max-posts 50
```

---

### 2. Extract Only Profile

Fetches the trainer's identity, bio, experience timeline, education, and skills:

```bash
uv run python social/linkedin/cli.py profile olgasi --slug olga
```

---

### 3. Extract Only Posts

Paginates through post history and generates `.md` files without re-fetching profile:

```bash
uv run python social/linkedin/cli.py posts olgasi --slug olga
```

---

### 4. Fetch Comments for a Post

Fetches comments from LinkedIn and **appends them directly to the bottom** of the post's Markdown file under `## Comments`:

```bash
# Pass the local markdown file:
uv run python social/linkedin/cli.py comments users/olga/data/linkedin/posts/2026-09-21-which-problem-do-you-solve.md

# Or pass the LinkedIn post URL directly:
uv run python social/linkedin/cli.py comments "https://www.linkedin.com/posts/olgasi_realestatetraining-activity-7507718658257735681-motX"
```

---

### 5. Automated High-Signal Comments During Ingestion

Fetch comments automatically for any post exceeding an engagement threshold (e.g. at least 10 comments):

```bash
uv run python social/linkedin/cli.py all olgasi --slug olga --comments-min 10
```

---

## Output Structure

Outputs default to `users/olga/data/linkedin/`. For another person, pass `--data-dir users/<slug>/data/linkedin` to every command:

```text
users/olga/data/linkedin/
├── olga.yaml                    # Master manifest (profile, experience, education, skills, posts index)
└── posts/                       # Individual Markdown files per post
    ├── 2026-09-21-more-valuable-than-money-your.md
    ├── 2026-09-21-which-problem-do-you-solve.md
    ├── 2026-09-17-getting-ghosted-by-your-clients.md
    └── ...
```

### Manifest Format (`olga.yaml`)

```yaml
profile:
  id: 'ACoAABbS-R8B...'
  firstName: Olga
  lastName: Sinenko
  headline: Dubai Real Estate Sales Mentor...
  about: 1 Billion AED + between me and my Team...

experience:
  - position: Founder and Leading Sales Trainer
    companyName: Live It Up - Real Estate Training Academy
    duration: 6 yrs 1 mo
    description: "At Real Estate Growth Academy..."

education:
  - schoolName: University of Wollongong in Dubai
    degree: Master of Business Administration - MBA

skills:
  - name: Cold Calling
    endorsements: 7 endorsements

posts:
  - id: '7507742242774601728'
    date: '2026-09-21T10:07:17.783Z'
    url: https://www.linkedin.com/posts/...
    likes: 16
    comments: 1
    file: ./posts/2026-09-21-more-valuable-than-money-your.md
```

### Post Format (`posts/*.md`)

```markdown
---
id: '7507718658257735681'
date: '2026-09-21T08:33:34.796Z'
url: https://www.linkedin.com/posts/...
likes: 22
comments: 13
---

Which problem Do You solve?…. This is my first question to anyone who writes me...

## Comments (9)

### Kavi Chandru (Executive Director at Top Rock Group)
> The strongest shift is from describing your service to articulating the problem you solve...

### Lisa Marie Agius (Real Estate Agent at betterhomes)
> We’ve all heard introductions where the job title lasts longer than the actual conversation
```

---

## CLI Options Reference

| Argument | Description | Default |
| :--- | :--- | :--- |
| `command` | Subcommand: `all`, `profile`, `posts`, `comments` | *required* |
| `url` / `target` | Profile URL/handle or post URL / `.md` file path | *required* |
| `--slug` | File slug prefix | Auto-extracted from handle |
| `--data-dir` | Output base directory | `users/olga/data/linkedin` |
| `--comments-min` | Minimum comments to trigger comment fetching during extraction | `0` (off) |
| `--max-posts` | Limit maximum posts to paginate | `None` (all) |
| `--find-email` | Perform SMTP email verification lookup | `false` |
| `--api-key` | HarvestAPI key override | `HARVEST_API_KEY` from `.env` |
| `-o`, `--output` | Explicit custom output path | Auto-generated in `--data-dir` |
