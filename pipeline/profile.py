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
from pathlib import Path

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

    /* Action / Next Step Banner */
    .action-box {
      background: linear-gradient(135deg, rgba(56, 189, 248, 0.08), rgba(249, 115, 22, 0.06));
      border: 1px solid rgba(56, 189, 248, 0.2);
      border-radius: 16px;
      padding: 16px 20px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      margin-bottom: 32px;
    }

    .action-text {
      display: flex;
      flex-direction: column;
      gap: 4px;
    }

    .action-title {
      font-size: 13px;
      font-weight: 700;
      color: #38bdf8;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .action-desc {
      font-size: 13.5px;
      color: #e4e4e7;
      font-weight: 500;
    }

    .action-btn {
      background: #38bdf8;
      color: #09090b;
      font-size: 13px;
      font-weight: 700;
      padding: 9px 18px;
      border-radius: 10px;
      text-decoration: none;
      white-space: nowrap;
      transition: transform 0.15s, opacity 0.15s;
    }

    .action-btn:hover {
      opacity: 0.92;
      transform: translateY(-1px);
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
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 18px;
      padding: 16px;
      width: 250px;
      min-width: 250px;
      text-decoration: none;
      color: inherit;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      transition: transform 0.2s ease, border-color 0.2s ease;
      cursor: pointer;
    }

    .post-card:hover {
      transform: translateY(-3px);
      border-color: rgba(255, 255, 255, 0.22);
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.4);
    }

    /* YouTube Card */
    .yt-card {
      width: 270px;
      min-width: 270px;
      padding: 0;
      overflow: hidden;
    }

    .yt-thumb-box {
      width: 100%;
      height: 145px;
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
      line-height: 1.45;
      color: #d4d4d8;
      display: -webkit-box;
      -webkit-line-clamp: 4;
      -webkit-box-orient: vertical;
      overflow: hidden;
      margin-bottom: 14px;
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
      padding: 8px 14px;
      border-radius: 12px;
      font-size: 12.5px;
      color: #d4d4d8;
      cursor: pointer;
      transition: all 0.2s;
    }

    .prompt-pill:hover {
      background: rgba(56, 189, 248, 0.12);
      border-color: #38bdf8;
      color: #fff;
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
      <a href="https://www.linkedin.com/in/olgasi" target="_blank" class="btn-create">LinkedIn Profile</a>
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
        <svg class="verified-badge" viewBox="0 0 24 24" fill="currentColor">
          <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/>
        </svg>
      </div>
      <div class="profile-sub">
        <span>{{SUBTITLE_1}}</span>
        <span class="sub-divider">•</span>
        <span>{{SUBTITLE_2}}</span>
        <span class="sub-divider">•</span>
        <span>{{SUBTITLE_3}}</span>
      </div>
    </div>

    <!-- 1-Paragraph Action-Oriented Summary -->
    <p class="profile-bio">
      {{BIO_SUMMARY}}
    </p>

    <!-- Action & Next Step Hub -->
    <div class="action-box">
      <div class="action-text">
        <div class="action-title">
          <span>⚡</span>
          <span>Core Action Principle</span>
        </div>
        <div class="action-desc">{{ACTION_PRINCIPLE}}</div>
      </div>
      <a href="{{ACTION_URL}}" target="_blank" class="action-btn">Take Action</a>
    </div>

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

    <!-- Action Prompt Section -->
    <div class="ask-footer-bar">
      <div class="ask-header">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>
        <span>Explore Key Sales Situations</span>
      </div>
      <div class="prompt-pills">
        <div class="prompt-pill" onclick="alert('Olga\\'s Rule: Never email listings immediately. A buyer asking for options without discovery is not ready to buy. Ask: What specific criteria will make or break this decision?')">
          "What to say when a buyer asks to 'Just send options'?"
        </div>
        <div class="prompt-pill" onclick="alert('Olga\\'s Rule: Stop sending random follow-ups. Acknowledge their priority shift directly: \"I noticed we haven\\'t connected—has the timeline changed, or is this property no longer a fit?\"')">
          "How to overcome client ghosting without being pushy?"
        </div>
        <div class="prompt-pill" onclick="alert('Olga\\'s Rule: Isolate whether they seek capital appreciation or rental yield before quoting numbers. Never pitch off-plan ROI without knowing their exit horizon.')">
          "How to qualify an off-plan investor in Dubai?"
        </div>
      </div>
    </div>
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


def build_profile(user: str = "olga") -> Path:
    """Build action-oriented Delphi-style trainer profile HTML."""
    user_root = ROOT / "users" / user
    data_dir = user_root / "data"
    workspace = user_root / "workspace"
    workspace.mkdir(parents=True, exist_ok=True)

    # 1. Profile metadata
    name = "Olga Sinenko"
    avatar_url = "https://media.licdn.com/dms/image/v2/D4D03AQHXCUjkOxhpUA/profile-displayphoto-crop_800_800/B4DZ0_fwi1I0AI-/0/1774886784218?e=1792022400&v=beta&t=-eHo66a62btnwS4PERkehZW6Zhro9kalrszUPutemC8"
    sub1 = "Dubai Real Estate Sales Mentor"
    sub2 = "Live It Up Academy"
    sub3 = "Neuro-Emotional Persuasion"
    bio = (
        "For the past 6+ years, I’ve been training Dubai real estate agents to turn conversations, "
        "calls, presentations, and follow-ups into closed deals. Over 2,000 agents have gone through my trainings, "
        "earning up to 1M+ AED in annual commissions. I teach how to influence through my Neuro-Emotional "
        "Persuasion System: understanding human behavior, reading hesitation, asking the right questions, and "
        "guiding clients to a clear next step without pushy tactics."
    )
    action_principle = "Never pitch listings before qualifying client criteria. Turn 'I’ll think about it' into a clear agreed next step."
    action_url = "https://www.linkedin.com/in/olgasi"

    # 2. YouTube Cards
    yt_cards_html = []
    yt_file = data_dir / "youtube" / "olga.yaml"
    if yt_file.exists():
        yt_data = yaml.safe_load(yt_file.read_text(encoding="utf-8"))
        for v in yt_data.get("videos", [])[:8]:
            vid_id = v.get("id", "")
            title = v.get("title", "Video")
            url = v.get("url", f"https://www.youtube.com/watch?v={vid_id}")
            duration = v.get("duration", "10:00")
            thumb = f"https://img.youtube.com/vi/{vid_id}/hqdefault.jpg"
            yt_cards_html.append(f"""
              <a href="{url}" target="_blank" class="post-card yt-card">
                <div class="yt-thumb-box">
                  <img src="{thumb}" alt="{title}" class="yt-thumb-img" onerror="this.src='https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=300&h=180&fit=crop'">
                  <div class="yt-duration">{duration}</div>
                </div>
                <div class="yt-content">
                  <div class="yt-title">{title}</div>
                  <div class="yt-footer">
                    <span>YouTube Video</span>
                    <span>Watch ↗</span>
                  </div>
                </div>
              </a>
            """)

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
            date_str = date_m.group(1)[:10] if date_m else ""
            url = url_m.group(1) if url_m else "https://www.linkedin.com/in/olgasi"
            lines = [l.strip() for l in body.splitlines() if l.strip()]
            snippet = " ".join(lines[:3])[:150] + "..." if lines else "LinkedIn post"
            li_cards_html.append(f"""
              <a href="{url}" target="_blank" class="post-card">
                <div class="card-platform-row">
                  <svg class="platform-icon" viewBox="0 0 24 24" fill="#0284c7"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/></svg>
                  <span>@olgasi</span>
                </div>
                <div class="post-text">{snippet}</div>
                <div class="post-footer">
                  <span>{date_str}</span>
                  <span>View Post ↗</span>
                </div>
              </a>
            """)

    # 4. Instagram Cards
    ig_cards_html = []
    ig_dir = data_dir / "instagram" / "posts"
    if ig_dir.exists():
        for p in sorted(ig_dir.glob("*.md"), reverse=True)[:8]:
            txt = p.read_text(encoding="utf-8")
            m = re.search(r"---\s*\n(.*?)\n---\s*\n(.*)", txt, re.DOTALL)
            meta, body = m.groups() if m else ("", txt)
            date_m = re.search(r"date:\s*[\'\"]?([^\n\'\"]+)", meta)
            url_m = re.search(r"url:\s*[\'\"]?([^\n\'\"]+)", meta)
            type_m = re.search(r"type:\s*[\'\"]?([^\n\'\"]+)", meta)
            date_str = date_m.group(1)[:10] if date_m else ""
            url = url_m.group(1) if url_m else "https://www.instagram.com/olga_sinenko.official/"
            post_type = type_m.group(1).upper() if type_m else "POST"
            lines = [l.strip().removeprefix("## Caption").strip() for l in body.splitlines() if l.strip() and not l.startswith("## ")]
            snippet = " ".join(lines)[:140] + "..." if lines else "Instagram update"
            ig_cards_html.append(f"""
              <a href="{url}" target="_blank" class="post-card">
                <div class="card-platform-row">
                  <svg class="platform-icon" viewBox="0 0 24 24" fill="#e1306c"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg>
                  <span>{post_type}</span>
                </div>
                <div class="post-text">{snippet}</div>
                <div class="post-footer">
                  <span>{date_str}</span>
                  <span>View Reel ↗</span>
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
            date_str = date_m.group(1)[:10] if date_m else ""
            url = url_m.group(1) if url_m else "https://x.com/Olga_Si_Sales"
            lines = [l.strip() for l in body.splitlines() if l.strip() and not l.startswith("## ")]
            snippet = " ".join(lines)[:140] if lines else "Tweet update"
            tw_cards_html.append(f"""
              <a href="{url}" target="_blank" class="post-card">
                <div class="card-platform-row">
                  <svg class="platform-icon" viewBox="0 0 24 24" fill="#fafafa"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>
                  <span>@Olga_Si_Sales</span>
                </div>
                <div class="post-text">{snippet}</div>
                <div class="post-footer">
                  <span>{date_str}</span>
                  <span>View Post ↗</span>
                </div>
              </a>
            """)

    html = (
        HTML_TEMPLATE.replace("{{NAME}}", name)
        .replace("{{AVATAR_URL}}", avatar_url)
        .replace("{{SUBTITLE_1}}", sub1)
        .replace("{{SUBTITLE_2}}", sub2)
        .replace("{{SUBTITLE_3}}", sub3)
        .replace("{{BIO_SUMMARY}}", bio)
        .replace("{{ACTION_PRINCIPLE}}", action_principle)
        .replace("{{ACTION_URL}}", action_url)
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
