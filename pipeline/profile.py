"""Generate an action-oriented Delphi.ai-style trainer profile page.

Features:
- Profile card with squircle avatar, verified badge, and action-oriented bio.
- Latest posts from each social platform (YouTube, LinkedIn, Instagram, X) as interactive cards.
- Cards link directly to primary sources with zero extra clutter (no ask button).
- Action and next-step oriented core with instant prompt suggestions.

Run:
    uv run python -m pipeline.profile --user olga
"""

import argparse
import re
from html import escape
from pathlib import Path
from urllib.parse import urlparse

import yaml

ROOT = Path(__file__).resolve().parents[1]

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>{{NAME}} — TrainerTwin</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
  <style>
    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      background-color: #0c0d0e;
      color: #ededed;
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      align-items: center;
      padding: 24px 16px 80px 16px;
      -webkit-font-smoothing: antialiased;
    }

    /* Top Nav */
    .top-nav {
      width: 100%;
      max-width: 860px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 24px;
      padding: 0 4px;
    }

    .brand-logo {
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 15px;
      font-weight: 700;
      letter-spacing: -0.02em;
      color: #fafafa;
      text-decoration: none;
    }

    .brand-icon {
      width: 22px;
      height: 22px;
      background: linear-gradient(135deg, #ff5e3a, #ff2a6d);
      border-radius: 6px;
      display: flex;
      align-items: center;
      justify-content: center;
      color: #fff;
      font-size: 12px;
      font-weight: 900;
    }

    .nav-actions {
      display: flex;
      align-items: center;
      gap: 12px;
    }

    .btn-create {
      background: #f97316;
      color: #fff;
      font-size: 13px;
      font-weight: 600;
      padding: 8px 16px;
      border-radius: 20px;
      text-decoration: none;
      transition: opacity 0.2s;
    }

    .btn-create:hover {
      opacity: 0.9;
    }

    /* Main Profile Card */
    .profile-card {
      width: 100%;
      max-width: 860px;
      background: #17181c;
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 28px;
      padding: 36px 36px 32px 36px;
      position: relative;
      box-shadow: 0 20px 40px -10px rgba(0, 0, 0, 0.5);
    }

    .card-top {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      margin-bottom: 20px;
    }

    .avatar-wrapper {
      width: 104px;
      height: 104px;
      border-radius: 26px;
      overflow: hidden;
      background: #27272a;
      border: 1px solid rgba(255, 255, 255, 0.12);
      box-shadow: 0 8px 16px rgba(0, 0, 0, 0.35);
      flex-shrink: 0;
    }

    .avatar-img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
    }

    .btn-share {
      background: rgba(255, 255, 255, 0.07);
      border: 1px solid rgba(255, 255, 255, 0.08);
      color: #d4d4d8;
      font-size: 13px;
      font-weight: 600;
      padding: 8px 16px;
      border-radius: 20px;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s;
    }

    .btn-share:hover {
      background: rgba(255, 255, 255, 0.12);
      color: #fff;
    }

    /* Name & Badges */
    .profile-header {
      margin-bottom: 16px;
    }

    .name-row {
      display: flex;
      align-items: center;
      gap: 8px;
      margin-bottom: 6px;
    }

    .profile-name {
      font-size: 28px;
      font-weight: 800;
      letter-spacing: -0.03em;
      color: #fafafa;
    }

    .verified-badge {
      width: 20px;
      height: 20px;
      color: #38bdf8;
      display: inline-flex;
    }

    .profile-sub {
      font-size: 13px;
      color: #a1a1aa;
      font-weight: 500;
      display: flex;
      align-items: center;
      flex-wrap: wrap;
      gap: 8px;
    }

    .sub-divider {
      color: #52525b;
    }

    /* Bio Summary */
    .profile-bio {
      font-size: 14.5px;
      line-height: 1.65;
      color: #d4d4d8;
      margin-bottom: 24px;
      font-weight: 400;
    }

    /* Section Headers */
    .section-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 14px;
      margin-top: 28px;
    }

    .section-title {
      font-size: 16px;
      font-weight: 700;
      color: #fafafa;
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .carousel-arrows {
      display: flex;
      gap: 6px;
    }

    .btn-arrow {
      width: 28px;
      height: 28px;
      border-radius: 50%;
      background: rgba(255, 255, 255, 0.06);
      border: 1px solid rgba(255, 255, 255, 0.08);
      color: #a1a1aa;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      font-size: 12px;
      transition: all 0.2s;
    }

    .btn-arrow:hover {
      background: rgba(255, 255, 255, 0.12);
      color: #fff;
    }

    /* Horizontal Carousels */
    .cards-carousel {
      display: flex;
      gap: 14px;
      overflow-x: auto;
      padding-bottom: 6px;
      scroll-behavior: smooth;
      scrollbar-width: none;
    }

    .cards-carousel::-webkit-scrollbar {
      display: none;
    }

    /* Card Base */
    .post-card {
      background: #1e1f24;
      border: 1px solid rgba(255, 255, 255, 0.06);
      border-radius: 18px;
      padding: 16px;
      width: 260px;
      min-width: 260px;
      text-decoration: none;
      color: inherit;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      transition: transform 0.2s ease, border-color 0.2s ease, box-shadow 0.2s ease;
      cursor: pointer;
    }

    .post-card:hover {
      transform: translateY(-4px);
      border-color: rgba(255, 255, 255, 0.18);
      box-shadow: 0 12px 28px rgba(0, 0, 0, 0.5);
    }

    /* YouTube Card */
    .yt-card {
      width: 280px;
      min-width: 280px;
      padding: 0;
      overflow: hidden;
    }

    .yt-thumb-box {
      width: 100%;
      height: 155px;
      background: #09090b;
      position: relative;
      overflow: hidden;
    }

    .yt-thumb-img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
      transition: transform 0.3s;
    }

    .yt-card:hover .yt-thumb-img {
      transform: scale(1.04);
    }

    .yt-duration {
      position: absolute;
      bottom: 8px;
      right: 8px;
      background: rgba(0, 0, 0, 0.8);
      color: #fff;
      font-size: 11px;
      font-weight: 600;
      font-family: 'JetBrains Mono', monospace;
      padding: 2px 6px;
      border-radius: 4px;
    }

    .yt-content {
      padding: 14px 16px;
    }

    .yt-title {
      font-size: 13.5px;
      font-weight: 700;
      line-height: 1.4;
      color: #f4f4f5;
      margin-bottom: 8px;
      display: -webkit-box;
      -webkit-line-clamp: 2;
      -webkit-box-orient: vertical;
      overflow: hidden;
    }

    .yt-footer {
      font-size: 11px;
      color: #71717a;
      display: flex;
      justify-content: space-between;
    }

    /* Post Content Common */
    .card-platform-row {
      display: flex;
      align-items: center;
      gap: 6px;
      font-size: 12px;
      color: #a1a1aa;
      margin-bottom: 10px;
      font-weight: 500;
    }

    .platform-icon {
      width: 14px;
      height: 14px;
      display: inline-flex;
    }

    .post-text {
      font-size: 13px;
      line-height: 1.5;
      color: #a1a1aa;
      display: -webkit-box;
      -webkit-line-clamp: 3;
      -webkit-box-orient: vertical;
      overflow: hidden;
      margin-bottom: 14px;
      flex-grow: 1;
    }

    .post-headline {
      font-size: 14px;
      font-weight: 700;
      color: #f4f4f5;
      line-height: 1.35;
      margin-bottom: 6px;
      display: -webkit-box;
      -webkit-line-clamp: 2;
      -webkit-box-orient: vertical;
      overflow: hidden;
    }

    .engagement-badge {
      color: #a1a1aa;
      font-family: 'JetBrains Mono', monospace;
      font-size: 11px;
    }

    .ig-type-badge {
      font-weight: 600;
      font-size: 11px;
      letter-spacing: 0.04em;
    }

    .post-footer {
      font-size: 11px;
      color: #71717a;
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-top: auto;
      border-top: 1px solid rgba(255, 255, 255, 0.05);
      padding-top: 10px;
    }

    /* Floating Ask Bar */
    .ask-footer-bar {
      margin-top: 36px;
      background: #111215;
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 20px;
      padding: 16px 20px;
    }

    .ask-header {
      font-size: 12px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: #71717a;
      margin-bottom: 12px;
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .prompt-pills {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
    }

    .prompt-pill {
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid rgba(255, 255, 255, 0.08);
      padding: 10px 16px;
      border-radius: 12px;
      font-size: 13px;
      color: #d4d4d8;
      cursor: pointer;
      transition: all 0.2s;
      position: relative;
    }

    .prompt-pill:hover {
      background: rgba(56, 189, 248, 0.12);
      border-color: #38bdf8;
      color: #fff;
    }

    .prompt-pill.expanded {
      background: rgba(56, 189, 248, 0.08);
      border-color: rgba(56, 189, 248, 0.3);
      color: #fff;
    }

    .prompt-answer {
      display: none;
      margin-top: 8px;
      padding-top: 8px;
      border-top: 1px solid rgba(56, 189, 248, 0.15);
      font-size: 12.5px;
      line-height: 1.55;
      color: #94a3b8;
    }

    .prompt-pill.expanded .prompt-answer {
      display: block;
    }
  </style>
</head>
<body>

  <!-- Top Navigation -->
  <nav class="top-nav">
    <a href="#" class="brand-logo">
      <div class="brand-icon">T</div>
      <span>TrainerTwin</span>
    </a>
    <div class="nav-actions">
      {{LINKEDIN_NAV}}
    </div>
  </nav>

  <!-- Main Profile Card -->
  <main class="profile-card">
    <div class="card-top">
      <div class="avatar-wrapper">
        <img src="{{AVATAR_URL}}" alt="{{NAME}}" class="avatar-img" onerror="this.src='https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=300&h=300&fit=crop'">
      </div>
      <button class="btn-share" onclick="navigator.clipboard.writeText(window.location.href); alert('Profile link copied to clipboard!');">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 12v8a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-8"/><polyline points="16 6 12 2 8 6"/><line x1="12" y1="2" x2="12" y2="15"/></svg>
        <span>Share</span>
      </button>
    </div>

    <div class="profile-header">
      <div class="name-row">
        <h1 class="profile-name">{{NAME}}</h1>
        {{VERIFIED_BADGE}}
      </div>
      <div class="profile-sub">{{SUBTITLES}}</div>
    </div>

    <!-- 1-Paragraph Action-Oriented Summary -->
    <p class="profile-bio">
      {{BIO_SUMMARY}}
    </p>

    <!-- Latest on YouTube -->
    <div class="section-header">
      <div class="section-title">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="#ef4444"><path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg>
        <span>Latest on YouTube</span>
      </div>
      <div class="carousel-arrows">
        <button class="btn-arrow" onclick="scrollCarousel('ytCarousel', -300)">‹</button>
        <button class="btn-arrow" onclick="scrollCarousel('ytCarousel', 300)">›</button>
      </div>
    </div>
    <div class="cards-carousel" id="ytCarousel">
      {{YOUTUBE_CARDS}}
    </div>

    <!-- Latest on LinkedIn -->
    <div class="section-header">
      <div class="section-title">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="#0284c7"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/></svg>
        <span>Latest on LinkedIn</span>
      </div>
      <div class="carousel-arrows">
        <button class="btn-arrow" onclick="scrollCarousel('liCarousel', -300)">‹</button>
        <button class="btn-arrow" onclick="scrollCarousel('liCarousel', 300)">›</button>
      </div>
    </div>
    <div class="cards-carousel" id="liCarousel">
      {{LINKEDIN_CARDS}}
    </div>

    <!-- Latest on Instagram -->
    <div class="section-header">
      <div class="section-title">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="#e1306c"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg>
        <span>Latest on Instagram</span>
      </div>
      <div class="carousel-arrows">
        <button class="btn-arrow" onclick="scrollCarousel('igCarousel', -300)">‹</button>
        <button class="btn-arrow" onclick="scrollCarousel('igCarousel', 300)">›</button>
      </div>
    </div>
    <div class="cards-carousel" id="igCarousel">
      {{INSTAGRAM_CARDS}}
    </div>

    <!-- Latest on X (Twitter) -->
    <div class="section-header">
      <div class="section-title">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="#fafafa"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>
        <span>Latest on X</span>
      </div>
      <div class="carousel-arrows">
        <button class="btn-arrow" onclick="scrollCarousel('twCarousel', -300)">‹</button>
        <button class="btn-arrow" onclick="scrollCarousel('twCarousel', 300)">›</button>
      </div>
    </div>
    <div class="cards-carousel" id="twCarousel">
      {{TWITTER_CARDS}}
    </div>

    {{PROMPT_SECTION}}
  </main>

  <script>
    function scrollCarousel(id, amount) {
      const el = document.getElementById(id);
      if (el) {
        el.scrollBy({ left: amount, behavior: 'smooth' });
      }
    }
  </script>
</body>
</html>
"""

OLGA_PROMPTS = """<!-- Action Prompt Section -->
    <div class="ask-footer-bar">
      <div class="ask-header">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>
        <span>Explore Key Sales Situations</span>
      </div>
      <div class="prompt-pills">
        <div class="prompt-pill" onclick="this.classList.toggle('expanded')">
          “What to say when a buyer asks to 'Just send options'?”
          <div class="prompt-answer">⚡ <b>Olga’s Rule:</b> Never email listings immediately. A buyer asking for options without discovery is not ready to buy. Ask: <em>"What specific criteria will make or break this decision for you?"</em></div>
        </div>
        <div class="prompt-pill" onclick="this.classList.toggle('expanded')">
          “How to overcome client ghosting without being pushy?”
          <div class="prompt-answer">⚡ <b>Olga’s Rule:</b> Stop sending random follow-ups. Acknowledge their priority shift directly: <em>"I noticed we haven’t connected—has the timeline changed, or is this property no longer a fit?"</em></div>
        </div>
        <div class="prompt-pill" onclick="this.classList.toggle('expanded')">
          “How to qualify an off-plan investor in Dubai?”
          <div class="prompt-answer">⚡ <b>Olga’s Rule:</b> Isolate whether they seek capital appreciation or rental yield before quoting numbers. Never pitch off-plan ROI without knowing their exit horizon.</div>
        </div>
      </div>
    </div>"""


def build_profile(user: str = "olga") -> Path:
    """Build action-oriented Delphi-style trainer profile HTML."""
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", user):
        raise ValueError("User must be a lowercase slug (e.g. jane-doe)")
    user_root = ROOT / "users" / user
    data_dir = user_root / "data"
    if not data_dir.is_dir():
        raise ValueError(f"User data directory not found: {data_dir}")
    workspace = user_root / "workspace"
    workspace.mkdir(parents=True, exist_ok=True)

    def safe_url(value: str) -> str:
        value = str(value or "")
        parsed = urlparse(value)
        return escape(value, quote=True) if parsed.scheme in {"http", "https"} and parsed.hostname else "#"

    def metadata(platform: str) -> tuple[dict, str]:
        for path in sorted((data_dir / platform).glob("*.yaml")):
            doc = yaml.safe_load(path.read_text(encoding="utf-8"))
            if isinstance(doc, dict) and isinstance(doc.get("profile"), dict):
                return doc["profile"], path.stem
        return {}, ""

    linkedin, linkedin_handle = metadata("linkedin")
    instagram, instagram_handle = metadata("instagram")
    twitter, twitter_handle = metadata("twitter")
    profile = linkedin or instagram or twitter
    name = str(profile.get("fullName") or profile.get("name") or
               " ".join(filter(None, (profile.get("firstName"), profile.get("lastName")))) or
               user.replace("-", " ").title())
    avatar_url = (profile.get("profilePicUrl") or profile.get("profilePicture") or
                  profile.get("profileImageUrl") or "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=300&h=300&fit=crop")
    bio = profile.get("biography") or profile.get("description") or profile.get("summary") or "Public profile assembled from collected social posts."
    subtitles = [profile.get("headline") or profile.get("position"), profile.get("company")]
    linkedin_url = linkedin.get("linkedinUrl") or linkedin.get("url") or (
        f"https://www.linkedin.com/in/{linkedin_handle}/" if linkedin_handle else ""
    )
    def _fmt_duration(d: str) -> str:
        """Convert 00:11:29 -> 11:29, keep 1:02:30 as-is."""
        parts = d.split(":")
        if len(parts) == 3 and parts[0] == "00":
            return f"{int(parts[1])}:{parts[2]}"
        if len(parts) == 3:
            return f"{int(parts[0])}:{parts[1]}:{parts[2]}"
        return d

    def _fmt_views(v: int | None) -> str:
        if not v:
            return ""
        if v >= 1_000_000:
            return f"{v / 1_000_000:.1f}M views"
        if v >= 1_000:
            return f"{v / 1_000:.1f}K views"
        return f"{v:,} views"

    def _fmt_engagement(likes: str, comments: str) -> str:
        parts = []
        if likes and likes != "0":
            parts.append(f"♥ {likes}")
        if comments and comments != "0":
            parts.append(f"💬 {comments}")
        return "  ".join(parts) if parts else ""

    def _relative_date(iso: str) -> str:
        """Turn 2026-09-21 into 'Sep 21' for compact display."""
        if not iso or len(iso) < 10:
            return iso
        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                  "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        try:
            m = int(iso[5:7])
            d = int(iso[8:10])
            return f"{months[m - 1]} {d}"
        except (ValueError, IndexError):
            return iso[:10]

    # 2. YouTube Cards
    yt_cards_html = []
    yt_files = sorted((data_dir / "youtube").glob("*.yaml"))
    yt_files.sort(key=lambda p: p.name != "channel.yaml")
    for yt_file in yt_files:
        yt_data = yaml.safe_load(yt_file.read_text(encoding="utf-8"))
        if not isinstance(yt_data, dict) or not isinstance(yt_data.get("videos"), list):
            continue
        for v in yt_data["videos"][:8]:
            vid_id = v.get("id", "")
            title = escape(str(v.get("title") or "Video"))
            url = safe_url(v.get("url") or f"https://www.youtube.com/watch?v={vid_id}")
            duration = escape(_fmt_duration(str(v.get("duration") or "")))
            views = _fmt_views(v.get("view_count"))
            thumb = safe_url(f"https://img.youtube.com/vi/{vid_id}/hqdefault.jpg") if re.fullmatch(r"[\w-]+", str(vid_id)) else "#"
            yt_cards_html.append(f"""
              <a href="{url}" target="_blank" class="post-card yt-card">
                <div class="yt-thumb-box">
                  <img src="{thumb}" alt="{title}" class="yt-thumb-img" onerror="this.src='https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=300&h=180&fit=crop'">
                  <div class="yt-duration">{duration}</div>
                </div>
                <div class="yt-content">
                  <div class="yt-title">{title}</div>
                  <div class="yt-footer">
                    <span>{views}</span>
                    <span>Watch ↗</span>
                  </div>
                </div>
              </a>
            """)
        break

    # 3. LinkedIn Cards
    li_cards_html = []
    li_dir = data_dir / "linkedin" / "posts"
    if li_dir.exists():
        for p in sorted(li_dir.glob("*.md"), reverse=True)[:8]:
            txt = p.read_text(encoding="utf-8")
            m = re.search(r"---\s*\n(.*?)\n---\s*\n(.*)", txt, re.DOTALL)
            meta, body = m.groups() if m else ("", txt)
            date_m = re.search(r"date:\s*[\'\"]?([^\n\'\"]+)", meta)
            url_m = re.search(r"url:\s*[\'\"]?([^\n\'\"]+)", meta)
            likes_m = re.search(r"likes:\s*(\d+)", meta)
            comments_m = re.search(r"comments:\s*(\d+)", meta)
            date_str = _relative_date(date_m.group(1)[:10]) if date_m else ""
            url = safe_url(url_m.group(1) if url_m else linkedin_url)
            engagement = _fmt_engagement(
                likes_m.group(1) if likes_m else "",
                comments_m.group(1) if comments_m else "",
            )
            lines = [l.strip() for l in body.splitlines() if l.strip() and not l.startswith("## ")]
            # Split into a bold headline + body snippet
            headline = escape(lines[0][:80] if lines else "LinkedIn post")
            body_snippet = escape(" ".join(lines[1:3])[:120] + "..." if len(lines) > 1 else "")
            li_cards_html.append(f"""
              <a href="{url}" target="_blank" class="post-card">
                <div class="card-platform-row">
                  <svg class="platform-icon" viewBox="0 0 24 24" fill="#0284c7"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/></svg>
                  <span>{escape('@' + linkedin_handle) if linkedin_handle else 'LinkedIn'}</span>
                </div>
                <div class="post-headline">{headline}</div>
                <div class="post-text">{body_snippet}</div>
                <div class="post-footer">
                  <span>{date_str}</span>
                  <span class="engagement-badge">{engagement}</span>
                </div>
              </a>
            """)

    # 4. Instagram Cards
    ig_cards_html = []
    ig_dir = data_dir / "instagram" / "posts"
    ig_type_icons = {"REEL": "▶", "CAROUSEL": "⊞", "IMAGE": "◻", "POST": "◻"}
    if ig_dir.exists():
        for p in sorted(ig_dir.glob("*.md"), reverse=True)[:8]:
            txt = p.read_text(encoding="utf-8")
            m = re.search(r"---\s*\n(.*?)\n---\s*\n(.*)", txt, re.DOTALL)
            meta, body = m.groups() if m else ("", txt)
            date_m = re.search(r"date:\s*[\'\"]?([^\n\'\"]+)", meta)
            url_m = re.search(r"url:\s*[\'\"]?([^\n\'\"]+)", meta)
            type_m = re.search(r"type:\s*[\'\"]?([^\n\'\"]+)", meta)
            likes_m = re.search(r"likes:\s*(\d+)", meta)
            date_str = _relative_date(date_m.group(1)[:10]) if date_m else ""
            url = safe_url(url_m.group(1) if url_m else f"https://www.instagram.com/{instagram_handle}/")
            post_type = type_m.group(1).upper() if type_m else "POST"
            type_icon = ig_type_icons.get(post_type, "◻")
            likes_str = f"♥ {likes_m.group(1)}" if likes_m and likes_m.group(1) != "0" else ""
            lines = [l.strip().removeprefix("## Caption").strip() for l in body.splitlines() if l.strip() and not l.startswith("## ")]
            snippet = escape(" ".join(lines)[:140] + "..." if lines else "Instagram update")
            ig_cards_html.append(f"""
              <a href="{url}" target="_blank" class="post-card">
                <div class="card-platform-row">
                  <svg class="platform-icon" viewBox="0 0 24 24" fill="#e1306c"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg>
                  <span class="ig-type-badge">{type_icon} {post_type}</span>
                </div>
                <div class="post-text">{snippet}</div>
                <div class="post-footer">
                  <span>{date_str}</span>
                  <span class="engagement-badge">{likes_str}</span>
                </div>
              </a>
            """)

    # 5. Twitter Cards
    tw_cards_html = []
    tw_dir = data_dir / "twitter" / "tweets"
    if tw_dir.exists():
        for p in sorted(tw_dir.glob("*.md"), reverse=True)[:8]:
            txt = p.read_text(encoding="utf-8")
            m = re.search(r"---\s*\n(.*?)\n---\s*\n(.*)", txt, re.DOTALL)
            meta, body = m.groups() if m else ("", txt)
            date_m = re.search(r"date:\s*[\'\"]?([^\n\'\"]+)", meta)
            url_m = re.search(r"url:\s*[\'\"]?([^\n\'\"]+)", meta)
            likes_m = re.search(r"likes:\s*(\d+)", meta)
            views_m = re.search(r"views:\s*(\d+)", meta)
            date_str = _relative_date(date_m.group(1)[:10]) if date_m else ""
            url = safe_url(url_m.group(1) if url_m else f"https://x.com/{twitter_handle}")
            engagement = _fmt_engagement(
                likes_m.group(1) if likes_m else "",
                "",
            )
            views_str = _fmt_views(int(views_m.group(1))) if views_m else ""
            lines = [l.strip() for l in body.splitlines() if l.strip() and not l.startswith("## ")]
            snippet = escape(" ".join(lines)[:140] if lines else "Tweet update")
            tw_cards_html.append(f"""
              <a href="{url}" target="_blank" class="post-card">
                <div class="card-platform-row">
                  <svg class="platform-icon" viewBox="0 0 24 24" fill="#fafafa"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>
                  <span>{escape('@' + twitter_handle) if twitter_handle else 'X'}</span>
                </div>
                <div class="post-text">{snippet}</div>
                <div class="post-footer">
                  <span>{date_str}  {views_str}</span>
                  <span class="engagement-badge">{engagement}</span>
                </div>
              </a>
            """)

    html = (
        HTML_TEMPLATE.replace("{{NAME}}", escape(name))
        .replace("{{VERIFIED_BADGE}}", '<svg class="verified-badge" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/></svg>' if profile.get("verified") is True else "")
        .replace("{{AVATAR_URL}}", safe_url(avatar_url))
        .replace("{{SUBTITLES}}", ' <span class="sub-divider">•</span> '.join(f"<span>{escape(str(s))}</span>" for s in subtitles if s))
        .replace("{{BIO_SUMMARY}}", escape(str(bio)))
        .replace("{{LINKEDIN_NAV}}", f'<a href="{safe_url(linkedin_url)}" target="_blank" class="btn-create">LinkedIn Profile</a>' if linkedin_url else "")
        .replace("{{PROMPT_SECTION}}", OLGA_PROMPTS if user == "olga" else "")
        .replace("{{YOUTUBE_CARDS}}", "\n".join(yt_cards_html))
        .replace("{{LINKEDIN_CARDS}}", "\n".join(li_cards_html))
        .replace("{{INSTAGRAM_CARDS}}", "\n".join(ig_cards_html))
        .replace("{{TWITTER_CARDS}}", "\n".join(tw_cards_html))
    )

    out = workspace / "profile.html"
    out.write_text(html, encoding="utf-8")
    return out


def main():
    parser = argparse.ArgumentParser(description="Generate Delphi.ai-style trainer profile")
    parser.add_argument("--user", default="olga", help="User slug under users/ (default: olga)")
    parser.add_argument("--open", action="store_true", help="Open in default browser")
    args = parser.parse_args()

    out = build_profile(user=args.user)
    print(f"Generated Delphi-style profile page: {out}")
    if args.open:
        import subprocess
        subprocess.run(["open", str(out)], check=False)


if __name__ == "__main__":
    main()
