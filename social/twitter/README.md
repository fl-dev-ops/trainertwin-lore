# Twitter/X Ingestion CLI (`social/twitter/cli.py`)

A lightweight CLI tool to extract Twitter/X user profiles, following networks, followers, mentions, tweet timelines, conversation threads, and long-form articles via TwitterAPI.io for TrainerTwin persona development.

---

## Prerequisites

1. Set your `TWITTER_API_KEY` in `olga/.env`:
   ```bash
   TWITTER_API_KEY=your_api_key_here
   ```
2. Dependencies (`httpx`, `pyyaml`, `python-dotenv`) run via `uv`.
3. Note on Free-Tier Rate Limits: TwitterAPI.io free tier allows 1 request every 5 seconds. The CLI automatically enforces a 5-second backoff between pagination requests.

---

## Quick Start

Run commands from the `olga` project root:

```bash
cd ~/Developers/Github/foreverlearning/olga
```

### 1. Extract Everything (`all`)

Fetches profile metadata, following accounts, sample followers, recent mentions, and historical tweets:

```bash
uv run python social/twitter/cli.py all Olga_Si_Sales --max-tweets 20
```

---

### 2. Extract Persona Context & Network (`profile`)

Fetches profile bio, following list, followers, and mentions:

```bash
uv run python social/twitter/cli.py profile Olga_Si_Sales --with-following 20 --with-followers 20 --with-mentions 10
```

To fetch only profile without network/mentions:
```bash
uv run python social/twitter/cli.py profile Olga_Si_Sales --with-following 0 --with-followers 0 --with-mentions 0
```

---

### 3. Extract Timeline Tweets (`tweets`)

Paginates tweets and saves each tweet as an individual Markdown file with YAML frontmatter:

```bash
uv run python social/twitter/cli.py tweets Olga_Si_Sales --max-tweets 30
```

---

### 4. Fetch Full Conversation Thread (`thread`)

Reconstructs an entire multi-tweet thread and displays or exports it:

```bash
# Pass tweet ID or full URL:
uv run python social/twitter/cli.py thread "https://x.com/Olga_Si_Sales/status/TWEET_ID"
```

Export to YAML:
```bash
uv run python social/twitter/cli.py thread 2039805659525644595 -o users/olga/data/twitter/threads/thread-sample.yaml
```

---

### 5. Fetch Long-Form Article (`article`)

Fetches long-form articles / notes published on X:

```bash
uv run python social/twitter/cli.py article <tweet_id_or_url>
```

---

## Output Structure

Outputs default to `users/olga/data/twitter/`. For another person, pass `--data-dir users/<slug>/data/twitter` to every command:

```text
users/olga/data/twitter/
├── {username}.yaml              # Master manifest (profile, following, followers, mentions, tweet index)
└── tweets/                      # Individual Markdown files
    ├── 2026-04-02-llm-knowledge-bases-something-im-finding.md
    ├── 2026-03-31-new-supply-chain-attack-this-time.md
    └── ...
```

### Manifest Format (`{username}.yaml`)

```yaml
profile:
  id: '33836629'
  name: Olga Sinenko
  userName: Olga_Si_Sales
  description: sales coaching
  followers: 4213285
  following: 1137
  createdAt: '2009-04-21T06:49:15.000000Z'

following:
  - id: '2434761475'
    name: theseriousadult
    userName: gallabytes
    description: father, ML enjoyer @anthropicai

followers:
  - ...

mentions:
  - id: '2103188486677500155'
    text: "Example mention of @Olga_Si_Sales..."

tweets:
  - id: '2039805659525644595'
    date: 'Thu Apr 02 20:42:21 +0000 2026'
    url: https://x.com/Olga_Si_Sales/status/EXAMPLE_ID
    likes: 60990
    retweets: 7391
    replies: 2937
    file: ./tweets/2026-04-02-llm-knowledge-bases-something.md
```

### Tweet Format (`tweets/*.md`)

```markdown
---
id: '2039805659525644595'
date: 'Thu Apr 02 20:42:21 +0000 2026'
url: https://x.com/Olga_Si_Sales/status/EXAMPLE_ID
likes: 60990
retweets: 7391
replies: 2937
quotes: 2207
views: 21920901
isReply: false
---

LLM Knowledge Bases

Something I'm finding very useful recently: using LLMs to build personal knowledge bases...
```

---

## CLI Options Reference

| Argument | Description | Default |
| :--- | :--- | :--- |
| `command` | Subcommand: `all`, `profile`, `tweets`, `thread`, `article` | *required* |
| `username` / `target` | Twitter handle / URL or Tweet ID / URL | *required* |
| `--slug` | Slug for filenames | Extracted handle |
| `--data-dir` | Output base directory | `users/olga/data/twitter` |
| `--max-tweets` | Max tweets to paginate | `None` (all) |
| `--with-following` | Number of followed accounts to include | `30` |
| `--with-followers` | Number of followers to include | `30` |
| `--with-mentions` | Number of mentions to include | `20` |
| `--api-key` | TwitterAPI.io key override | `TWITTER_API_KEY` from `.env` |
| `-o`, `--output` | Explicit custom output path | Auto-generated in `--data-dir` |
