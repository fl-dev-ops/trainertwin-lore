"""Export a responsive trainer profile with source-linked social carousels.

Run: uv run python -m pipeline.profile --user olga --open
"""

import argparse
import re
import webbrowser
from datetime import date
from html import escape
from pathlib import Path
from urllib.parse import urlparse

import yaml

from .sources import normalize_date

ROOT = Path(__file__).resolve().parents[1]
PLATFORMS = {
    "youtube": "YouTube",
    "linkedin": "LinkedIn",
    "instagram": "Instagram",
    "twitter": "X",
}
ICONS = {
    "youtube": '<rect x="2" y="5" width="20" height="14" rx="4"/><path d="m10 9 5 3-5 3Z"/>',
    "linkedin": '<rect x="3" y="3" width="18" height="18" rx="3"/><path d="M7 10v7m0-10v.1M11 17v-7m0 3a3 3 0 0 1 6 0v4"/>',
    "instagram": '<rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><path d="M17.5 6.5h.01"/>',
    "twitter": '<path d="M4 4h4l12 16h-4ZM20 4l-7 8M4 20l7-8"/>',
    "arrow": '<path d="M6 18 18 6M6 6h12v12"/>',
    "next": '<path d="m9 5 7 7-7 7"/>',
    "previous": '<path d="m15 5-7 7 7 7"/>',
    "copy": '<rect x="8" y="8" width="12" height="12" rx="2"/><path d="M16 8V4H4v12h4"/>',
    "play": '<path d="m9 5 11 7-11 7Z"/>',
    "check": '<path d="m5 12 4 4L19 6"/>',
}


def icon(name: str) -> str:
    return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[name]}</svg>'


HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="color-scheme" content="dark">
  <title>{{NAME}} — TrainerTwin</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <style>
    :root {
      --bg: #141516; --surface: #1d1e20; --hover: #252628;
      --text: #f3f0ea; --muted: #b2b0ab; --line: #38393b;
      --accent: #efb38d; --radius: 14px; --gap: 24px;
    }
    * { box-sizing: border-box; }
    html { scroll-behavior: smooth; scroll-padding-top: 104px; }
    body { margin: 0; background: var(--bg); color: var(--text); font-family: 'Plus Jakarta Sans', sans-serif; -webkit-font-smoothing: antialiased; }
    a { color: inherit; text-decoration: none; }
    button { color: inherit; font: inherit; cursor: pointer; }
    button:disabled { opacity: .35; cursor: default; }
    a, button, summary { -webkit-tap-highlight-color: transparent; }
    :focus-visible { outline: 2px solid var(--accent); outline-offset: 5px; }
    svg { width: 20px; height: 20px; flex: none; }
    h1, h2, h3, p { margin: 0; }
    [hidden] { display: none !important; }
    .wrap { width: min(1120px, calc(100% - 80px)); margin-inline: auto; }
    .skip-link { position: absolute; top: -60px; padding: 12px; z-index: 10; background: var(--text); color: var(--bg); }
    .skip-link:focus { top: 12px; }
    .topbar { display: flex; align-items: center; justify-content: space-between; min-height: 88px; border-bottom: 1px solid var(--line); gap: 20px; }
    .brand { display: inline-flex; align-items: center; gap: 12px; font-size: 19px; font-weight: 700; letter-spacing: -.04em; }
    .brand-mark { width: 32px; height: 32px; color: var(--accent); }
    .top-note { font-size: 13px; color: var(--muted); }
    .hero { display: grid; grid-template-columns: 184px minmax(0, 1fr); column-gap: 48px; padding: 64px 0 48px; align-items: start; }
    .portrait { position: relative; width: 184px; aspect-ratio: 1; overflow: hidden; border-radius: 24px; background: var(--surface); }
    .initials { position: absolute; inset: 0; display: grid; place-items: center; font-size: 48px; font-weight: 600; color: var(--accent); }
    .portrait img { position: relative; display: block; width: 100%; height: 100%; object-fit: cover; }
    .name-row { display: flex; align-items: center; gap: 14px; }
    h1 { font-size: clamp(34px, 4.5vw, 60px); line-height: 1.1; letter-spacing: -.04em; font-weight: 600; overflow-wrap: anywhere; }
    .verification { color: var(--accent); display: inline-flex; align-items: center; flex: none; }
    .verification svg { width: 24px; height: 24px; }
    .headline { margin-top: 14px; font-size: 16px; line-height: 1.6; color: var(--accent); }
    .bio { max-width: 70ch; margin-top: 20px; font-size: 16px; line-height: 1.85; color: var(--muted); }
    .hero-actions { display: flex; flex-wrap: wrap; align-items: center; gap: 12px 24px; margin-top: 28px; }
    .button { display: inline-flex; align-items: center; justify-content: center; gap: 10px; min-height: 46px; padding: 10px 18px; border: 1px solid var(--line); border-radius: 8px; font-size: 13px; font-weight: 600; background: transparent; }
    .button.primary { background: var(--text); border-color: var(--text); color: var(--bg); }
    .button:hover { background: var(--hover); }
    .button.primary:hover { background: #dcd7cf; }
    .text-link { display: inline-flex; gap: 8px; align-items: center; min-height: 44px; font-size: 13px; color: var(--muted); }
    .text-link:hover { color: var(--text); }
    .text-link svg { width: 16px; height: 16px; }
    .feed-nav { position: sticky; top: 0; z-index: 3; background: var(--bg); border-block: 1px solid var(--line); }
    .feed-nav-inner { display: flex; gap: 32px; overflow-x: auto; scrollbar-width: thin; }
    .feed-nav a { display: flex; align-items: center; gap: 8px; min-height: 62px; border-bottom: 2px solid transparent; color: var(--muted); font-size: 14px; white-space: nowrap; }
    .feed-nav a:hover, .feed-nav a[aria-current] { color: var(--text); border-bottom-color: var(--accent); }
    .feed-nav svg { width: 17px; height: 17px; }
    .channel { padding-top: 48px; scroll-margin-top: 12px; }
    .section-header { display: flex; align-items: center; justify-content: space-between; gap: 20px; margin-bottom: 24px; }
    .section-heading { display: flex; gap: 14px; align-items: center; }
    .platform-mark { display: grid; place-items: center; width: 42px; height: 42px; border-radius: 12px; background: var(--surface); }
    .youtube .platform-mark { color: #ff8b83; }
    .linkedin .platform-mark { color: #88c9f8; }
    .instagram .platform-mark { color: #f7a6bf; }
    .twitter .platform-mark { color: var(--text); }
    h2 { font-size: 24px; font-weight: 600; letter-spacing: -.025em; }
    .section-caption { margin-top: 5px; color: var(--muted); font-size: 12px; line-height: 1.6; }
    .row-controls { display: flex; align-items: center; gap: 8px; }
    .row-count { color: var(--muted); font-size: 12px; margin-right: 12px; font-variant-numeric: tabular-nums; }
    .arrow-button { display: grid; place-items: center; width: 44px; height: 44px; border-radius: 50%; background: transparent; border: 1px solid var(--line); }
    .arrow-button:not(:disabled):hover { background: var(--surface); border-color: var(--muted); }
    .arrow-button svg { width: 16px; height: 16px; }
    .cards { display: grid; grid-auto-flow: column; grid-auto-columns: calc((100% - var(--gap) * 2) / 3); gap: var(--gap); overflow-x: auto; scroll-snap-type: x mandatory; scrollbar-width: thin; scrollbar-color: var(--line) transparent; padding: 4px 2px 18px; }
    .post-card { min-width: 0; display: flex; flex-direction: column; scroll-snap-align: start; border-radius: var(--radius); background: var(--surface); border: 1px solid var(--line); overflow: hidden; transition: border-color .18s; }
    .post-card:hover { border-color: var(--muted); }
    .post-card:focus-visible { outline-offset: -3px; }
    .thumb { position: relative; aspect-ratio: 16 / 9; background: #26272a; overflow: hidden; }
    .thumb img { width: 100%; height: 100%; object-fit: cover; display: block; position: relative; }
    .thumb-fallback { position: absolute; inset: 0; display: grid; place-content: center; gap: 10px; color: var(--muted); text-align: center; font-size: 12px; }
    .thumb-fallback svg { margin-inline: auto; width: 28px; height: 28px; }
    .play { position: absolute; left: 14px; bottom: 12px; display: grid; place-items: center; width: 34px; height: 34px; border-radius: 50%; background: #141516e6; color: white; }
    .play svg { width: 16px; height: 16px; }
    .duration { position: absolute; bottom: 15px; right: 12px; padding: 4px 7px; border-radius: 4px; font-size: 11px; font-variant-numeric: tabular-nums; color: white; background: #141516e6; }
    .card-body { padding: 22px; display: flex; flex-direction: column; flex: 1; min-width: 0; }
    .card-meta { display: flex; justify-content: space-between; align-items: baseline; flex-wrap: wrap; gap: 6px; color: var(--muted); font-size: 11px; line-height: 1.6; margin-bottom: 18px; }
    .card-meta .handle { max-width: 60%; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
    h3 { font-size: 17px; line-height: 1.55; font-weight: 600; letter-spacing: -.02em; overflow-wrap: anywhere; }
    .excerpt { font-size: 14px; line-height: 1.8; color: var(--muted); margin-top: 10px; overflow-wrap: anywhere; }
    .clamp { display: -webkit-box; -webkit-box-orient: vertical; -webkit-line-clamp: 3; overflow: hidden; }
    .excerpt.clamp { -webkit-line-clamp: 4; }
    .card-footer { margin-top: auto; padding-top: 24px; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 10px; font-size: 12px; }
    .card-action { display: flex; align-items: center; gap: 6px; color: var(--text); font-weight: 500; }
    .card-action svg { width: 15px; height: 15px; }
    .engagement { color: var(--muted); font-size: 11px; }
    .text-card .card-body { min-height: 300px; }
    .empty { padding: 32px 0; color: var(--muted); border-block: 1px dashed var(--line); font-size: 14px; }
    .situations { display: grid; grid-template-columns: 1fr 2fr; gap: 48px; margin-top: 64px; padding-top: 40px; border-top: 1px solid var(--line); }
    .situations p { margin-top: 12px; color: var(--muted); font-size: 14px; line-height: 1.7; }
    details { border-bottom: 1px solid var(--line); }
    summary { display: flex; align-items: center; justify-content: space-between; gap: 20px; cursor: pointer; padding: 20px 0; list-style: none; font-size: 14px; line-height: 1.6; }
    summary::-webkit-details-marker { display: none; }
    summary svg { width: 16px; height: 16px; transition: transform .18s; }
    details[open] summary svg { transform: rotate(90deg); }
    .answer { color: var(--muted); font-size: 14px; line-height: 1.8; padding-bottom: 20px; }
    .page-footer { margin-top: 64px; padding: 28px 0 36px; border-top: 1px solid var(--line); display: flex; justify-content: space-between; gap: 20px; color: var(--muted); font-size: 12px; line-height: 1.6; }
    .page-footer a { text-decoration: underline; text-underline-offset: 4px; }
    .toast { position: fixed; bottom: 24px; left: 50%; transform: translateX(-50%); max-width: calc(100% - 32px); background: var(--text); color: var(--bg); border-radius: 10px; padding: 14px 20px; box-shadow: 0 8px 24px #0006; font-size: 13px; z-index: 10; }
    .toast:empty { display: none; }
    @media (max-width: 900px) {
      .wrap { width: calc(100% - 48px); }
      .hero { grid-template-columns: 144px minmax(0, 1fr); gap: 28px; padding-top: 48px; }
      .portrait { width: 144px; }
      .cards { grid-auto-columns: calc((100% - var(--gap)) / 2); }
      .situations { grid-template-columns: 1fr; gap: 16px; }
    }
    @media (max-width: 600px) {
      :root { --gap: 16px; }
      .wrap { width: calc(100% - 40px); }
      .topbar { min-height: 72px; }
      .top-note { font-size: 11px; }
      .hero { display: block; padding: 32px 0; }
      .portrait { width: 96px; border-radius: 18px; margin-bottom: 24px; }
      .initials { font-size: 30px; }
      h1 { font-size: 38px; }
      .headline { font-size: 14px; }
      .bio { font-size: 15px; line-height: 1.8; margin-top: 16px; }
      .hero-actions { gap: 12px 20px; margin-top: 24px; }
      .feed-nav-inner { gap: 24px; }
      .feed-nav a { font-size: 13px; min-height: 56px; }
      .channel { padding-top: 32px; }
      .section-header { gap: 12px; margin-bottom: 16px; }
      .section-heading { gap: 10px; }
      h2 { font-size: 21px; }
      .section-caption { max-width: 25ch; font-size: 11px; }
      .row-count { display: none; }
      .platform-mark { width: 36px; height: 36px; border-radius: 10px; }
      .cards { grid-auto-columns: 88%; }
      .card-body { padding: 20px; }
      .text-card .card-body { min-height: 280px; }
      .situations { margin-top: 40px; padding-top: 28px; }
      .page-footer { margin-top: 40px; flex-direction: column; gap: 8px; }
    }
    @media (prefers-reduced-motion: reduce) {
      html { scroll-behavior: auto; }
      *, *::before, *::after { transition: none !important; }
    }
  </style>
</head>
<body id="top">
  <a class="skip-link" href="#latest">Skip to posts</a>
  <header class="topbar wrap">
    <a href="#top" class="brand" aria-label="TrainerTwin, back to top">
      <svg class="brand-mark" viewBox="0 0 32 32" fill="none" aria-hidden="true"><path d="M3 8h18M12 8v20M11 3h18M20 3v20" stroke="currentColor" stroke-width="3" stroke-linecap="round"/></svg>
      TrainerTwin
    </a>
    <span class="top-note">The person behind the ideas.</span>
  </header>
  <main class="wrap">
    <section class="hero" aria-labelledby="profile-name">
      <div class="portrait">
        <span class="initials" aria-hidden="true">{{INITIALS}}</span>
        {{AVATAR}}
      </div>
      <div class="hero-copy">
        <div class="name-row"><h1 id="profile-name">{{NAME}}</h1>{{VERIFIED_BADGE}}</div>
        <p class="headline">{{HEADLINE}}</p>
        <p class="bio">{{BIO_SUMMARY}}</p>
        <div class="hero-actions">
          <a class="button primary" href="#latest">Explore posts {{NEXT_ICON}}</a>
          {{PROFILE_LINK}}
          {{COPY_BUTTON}}
        </div>
      </div>
    </section>
    <nav class="feed-nav" aria-label="Jump to platform"><div class="feed-nav-inner">{{PLATFORM_NAV}}</div></nav>
    <div id="latest">{{SECTIONS}}</div>
    {{PROMPT_SECTION}}
    <footer class="page-footer"><span>Collected with TrainerTwin. Each card opens its original source.</span><a href="#top">Back to top</a></footer>
  </main>
  <div class="toast" role="status" aria-live="polite"></div>
  <script>
    const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
    document.querySelectorAll('.channel').forEach(section => {
      const row = section.querySelector('.cards');
      const prev = section.querySelector('[data-direction="-1"]');
      const next = section.querySelector('[data-direction="1"]');
      if (!row) return;
      const update = () => {
        prev.disabled = row.scrollLeft <= 2;
        next.disabled = row.scrollLeft >= row.scrollWidth - row.clientWidth - 2;
      };
      section.querySelectorAll('[data-direction]').forEach(button => {
        button.addEventListener('click', () => row.scrollBy({
          left: Number(button.dataset.direction) * (row.firstElementChild.getBoundingClientRect().width + parseFloat(getComputedStyle(row).gap)),
          behavior: reducedMotion.matches ? 'instant' : 'smooth'
        }));
      });
      row.addEventListener('scroll', update, {passive: true});
      new ResizeObserver(update).observe(row);
      update();
    });
    const navLinks = [...document.querySelectorAll('.feed-nav a')];
    function markCurrent(id) {
      navLinks.forEach(link => {
        if (link.hash === '#' + id) link.setAttribute('aria-current', 'location');
        else link.removeAttribute('aria-current');
      });
    }
    if (navLinks.length) markCurrent(navLinks[0].hash.slice(1));
    const observer = new IntersectionObserver(entries => {
      entries.forEach(entry => { if (entry.isIntersecting) markCurrent(entry.target.id); });
    }, {rootMargin: '-15% 0px -65% 0px'});
    document.querySelectorAll('.channel').forEach(section => observer.observe(section));
    navLinks.forEach(link => link.addEventListener('click', () => markCurrent(link.hash.slice(1))));
    const copy = document.querySelector('[data-copy-url]');
    let toastTimer;
    copy?.addEventListener('click', async () => {
      const toast = document.querySelector('.toast');
      try {
        await navigator.clipboard.writeText(copy.dataset.copyUrl);
        toast.textContent = 'LinkedIn profile link copied.';
      } catch {
        toast.textContent = 'Copy unavailable here. Open the LinkedIn profile and copy its address.';
      }
      clearTimeout(toastTimer);
      toastTimer = setTimeout(() => { toast.textContent = ''; }, 5000);
    });
  </script>
</body>
</html>
"""

# Existing preview content; native disclosures keep it keyboard-accessible.
OLGA_PROMPTS = """<section class="situations" aria-labelledby="situations-title">
  <div><h2 id="situations-title">Explore sales situations</h2><p>Start with a question you encounter in your day-to-day work.</p></div>
  <div>
    <details><summary>What to say when a buyer asks to “just send options”? {{NEXT_ICON}}</summary><div class="answer"><b>Olga’s Rule:</b> Never email listings immediately. A buyer asking for options without discovery is not ready to buy. Ask: <em>“What specific criteria will make or break this decision for you?”</em></div></details>
    <details><summary>How to overcome client ghosting without being pushy? {{NEXT_ICON}}</summary><div class="answer"><b>Olga’s Rule:</b> Stop sending random follow-ups. Acknowledge their priority shift directly: <em>“I noticed we haven’t connected—has the timeline changed, or is this property no longer a fit?”</em></div></details>
    <details><summary>How to qualify an off-plan investor in Dubai? {{NEXT_ICON}}</summary><div class="answer"><b>Olga’s Rule:</b> Isolate whether they seek capital appreciation or rental yield before quoting numbers. Never pitch off-plan ROI without knowing their exit horizon.</div></details>
  </div>
</section>"""


def safe_url(value: object) -> str:
    value = str(value or "")
    parsed = urlparse(value)
    return (
        escape(value, quote=True)
        if parsed.scheme in {"http", "https"} and parsed.hostname
        else ""
    )


def publication(value: object) -> str:
    text = str(value or "")
    if re.fullmatch(r"\d{8}", text):
        text = f"{text[:4]}-{text[4:6]}-{text[6:]}"
    try:
        return normalize_date(text)
    except ValueError:
        return ""


def display_date(value: str) -> str:
    if not value:
        return "Date unavailable"
    return date.fromisoformat(value[:10]).strftime("%b %d, %Y").replace(" 0", " ")


def duration(value: object) -> str:
    text = str(value or "")
    parts = text.split(":")
    if len(parts) == 3 and all(p.isdigit() for p in parts):
        return (
            f"{int(parts[1])}:{parts[2]}"
            if int(parts[0]) == 0
            else f"{int(parts[0])}:{parts[1]}:{parts[2]}"
        )
    return text


def metric(value: object, label: str) -> str:
    if not isinstance(value, (int, float)) or isinstance(value, bool) or value < 0:
        return ""
    number = (
        f"{value / 1_000_000:.1f}M"
        if value >= 1_000_000
        else f"{value / 1000:.1f}K"
        if value >= 1000
        else f"{value:,.0f}"
    )
    return f"{number} {label.removesuffix('s') if value == 1 else label}"


def post_cards(data_dir: Path, platform: str, handle: str) -> list[str]:
    """Read frontmatter dates rather than filename order; never preview comments/quotes."""
    posts = []
    folder = "tweets" if platform == "twitter" else "posts"
    for path in sorted((data_dir / platform / folder).glob("*.md")):
        text = path.read_text(encoding="utf-8")
        match = re.match(r"\A---\s*\n(.*?)\n---\s*\n(.*)", text, re.DOTALL)
        meta, body = (yaml.safe_load(match[1]) or {}, match[2]) if match else ({}, text)
        if not isinstance(meta, dict):
            raise ValueError(f"Invalid Markdown frontmatter: {path}")  # noqa: TRY004 - invalid source document
        body = re.split(r"(?m)^\s*(?:## Comments|### Quoting @)", body, maxsplit=1)[0]
        lines = [
            line.strip()
            for line in body.splitlines()
            if line.strip() and not line.lstrip().startswith("## ")
        ]
        url = safe_url(meta.get("url"))
        if lines and url:
            posts.append((publication(meta.get("date")), meta, lines, url))
    cards = []
    for published, meta, lines, url in sorted(posts, key=lambda p: p[0], reverse=True)[
        :8
    ]:
        title = lines[0]
        rest = " ".join(lines[1:])
        if len(title) > 160:
            cut = title.rfind(" ", 0, 160)
            cut = cut if cut > 0 else 160
            rest = title[cut:].strip() + " " + rest
            title = title[:cut] + "…"
        excerpt = rest[:320].rsplit(" ", 1)[0] + "…" if len(rest) > 320 else rest
        kind = (
            str(meta.get("type") or "Post").title()
            if platform == "instagram"
            else handle
        )
        action = (
            "Watch reel"
            if platform == "instagram" and meta.get("type") == "reel"
            else "Read post"
        )
        engagement = (
            metric(meta.get("views"), "views")
            if platform == "twitter"
            else metric(meta.get("likes"), "likes")
        )
        date_html = (
            f'<time datetime="{published}">{display_date(published)}</time>'
            if published
            else "Date unavailable"
        )
        cards.append(f'''<a class="post-card text-card" href="{url}" target="_blank" rel="noopener noreferrer">
          <div class="card-body">
            <div class="card-meta"><span class="handle">{escape(kind)}</span>{date_html}</div>
            <h3 class="clamp">{escape(title)}</h3><p class="excerpt clamp">{escape(excerpt)}</p>
            <div class="card-footer"><span class="card-action">{action} {icon("arrow")}</span><span class="engagement">{engagement}</span></div>
          </div></a>''')
    return cards


def build_profile(user: str = "olga") -> Path:
    """Build a self-contained HTML page from this user's collected public metadata."""
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", user):
        raise ValueError("User must be a lowercase slug (e.g. jane-doe)")
    user_root = ROOT / "users" / user
    data_dir = user_root / "data"
    if not data_dir.is_dir():
        raise ValueError(f"User data directory not found: {data_dir}")

    def metadata(platform: str) -> tuple[dict, str]:
        for path in sorted((data_dir / platform).glob("*.yaml")):
            doc = yaml.safe_load(path.read_text(encoding="utf-8"))
            if isinstance(doc, dict) and isinstance(doc.get("profile"), dict):
                p = doc["profile"]
                handle = (
                    p.get("publicIdentifier")
                    or p.get("userName")
                    or p.get("username")
                    or path.stem
                )
                return p, str(handle)
        return {}, ""

    profiles = {
        platform: metadata(platform)
        for platform in ("linkedin", "instagram", "twitter")
    }
    profile = next((p for p, _ in profiles.values() if p), {})
    name = str(
        profile.get("fullName")
        or profile.get("name")
        or " ".join(filter(None, (profile.get("firstName"), profile.get("lastName"))))
        or user.replace("-", " ").title()
    )
    image = (
        profile.get("profilePicUrl")
        or profile.get("profilePicture")
        or profile.get("profileImageUrl")
        or profile.get("photo")
    )
    if isinstance(image, dict):
        image = image.get("url")
    avatar = safe_url(image)
    bio = str(
        profile.get("biography")
        or profile.get("description")
        or profile.get("summary")
        or profile.get("about")
        or "Public profile assembled from collected social posts."
    )
    # Keep the collected introduction, rather than inventing a biography or performance claims.
    bio = " ".join(bio.split("\n\n", 1)[0].split())
    if len(bio) > 650:
        bio = bio[:650].rsplit(" ", 1)[0] + "…"
    headline = str(profile.get("headline") or profile.get("position") or "")
    # The remaining LinkedIn headline is marketing copy, not a second biography.
    headline = headline.split("|", 1)[0].strip()
    linkedin, linkedin_handle = profiles["linkedin"]
    linkedin_url = safe_url(
        linkedin.get("linkedinUrl")
        or linkedin.get("url")
        or (
            f"https://www.linkedin.com/in/{linkedin_handle}/" if linkedin_handle else ""
        )
    )

    videos = []
    yt_files = sorted((data_dir / "youtube").glob("*.yaml"))
    yt_files.sort(key=lambda p: p.name != "channel.yaml")
    for path in yt_files:
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        if isinstance(doc, dict) and isinstance(doc.get("videos"), list):
            videos = [v for v in doc["videos"] if isinstance(v, dict)]
            break
    videos.sort(key=lambda v: publication(v.get("upload_date")), reverse=True)
    youtube_cards = []
    for video in videos[:8]:
        ident = str(video.get("id") or "")
        url = safe_url(video.get("url") or f"https://www.youtube.com/watch?v={ident}")
        if not url:
            continue
        title = escape(str(video.get("title") or "Untitled video"))
        thumb = (
            safe_url(f"https://img.youtube.com/vi/{ident}/hqdefault.jpg")
            if re.fullmatch(r"[\w-]+", ident)
            else ""
        )
        thumb_image = (
            f'<img src="{thumb}" alt="" loading="lazy" onerror="this.hidden=true">'
            if thumb
            else ""
        )
        length = escape(duration(video.get("duration")))
        published = publication(video.get("upload_date"))
        youtube_cards.append(f'''<a class="post-card video-card" href="{url}" target="_blank" rel="noopener noreferrer">
          <div class="thumb"><span class="thumb-fallback">{icon("youtube")}Video preview</span>{thumb_image}
            <span class="play">{icon("play")}</span>{f'<span class="duration">{length}</span>' if length else ""}</div>
          <div class="card-body"><h3 class="clamp">{title}</h3>
            <div class="card-footer"><span class="card-action">Watch video {icon("arrow")}</span><span class="engagement">{metric(video.get("view_count"), "views")}</span></div>
            {f'<p class="section-caption">{display_date(published)}</p>' if published else ""}
          </div></a>''')
    cards_by_platform = {"youtube": youtube_cards}
    for platform in ("linkedin", "instagram", "twitter"):
        handle = profiles[platform][1]
        cards_by_platform[platform] = post_cards(
            data_dir, platform, f"@{handle}" if handle else PLATFORMS[platform]
        )

    sections = []
    nav = []
    for platform, label in PLATFORMS.items():
        cards = cards_by_platform[platform]
        nav.append(f'<a href="#{platform}">{icon(platform)}{label}</a>')
        caption = (
            "Collected videos · channel order where dates are unavailable"
            if platform == "youtube"
            else "Latest posts in this collection"
        )
        controls = (
            f'''<div class="row-controls"><span class="row-count">{len(cards)} {"videos" if platform == "youtube" else "posts"}</span>
          <button class="arrow-button" data-direction="-1" aria-label="Previous {label} posts" aria-controls="{platform}-cards">{icon("previous")}</button>
          <button class="arrow-button" data-direction="1" aria-label="Next {label} posts" aria-controls="{platform}-cards">{icon("next")}</button></div>'''
            if cards
            else ""
        )
        row = (
            f'<div class="cards" id="{platform}-cards" role="region" aria-label="{label} posts" tabindex="0">{"".join(cards)}</div>'
            if cards
            else f'<p class="empty">No {label} posts collected yet.</p>'
        )
        sections.append(f'''<section class="channel {platform}" id="{platform}" aria-labelledby="{platform}-title">
          <div class="section-header"><div class="section-heading"><span class="platform-mark">{icon(platform)}</span>
            <div><h2 id="{platform}-title">{label}</h2><p class="section-caption">{caption}</p></div></div>{controls}</div>{row}</section>''')

    replacements = {
        "NAME": escape(name),
        "INITIALS": escape("".join(word[0] for word in name.split()[:2])),
        "AVATAR": f'<img src="{avatar}" alt="{escape(name)}" width="184" height="184" onerror="this.hidden=true">'
        if avatar
        else "",
        "HEADLINE": escape(headline),
        "BIO_SUMMARY": escape(bio),
        "VERIFIED_BADGE": f'<span class="verification" role="img" aria-label="Verified on the source profile" title="Verified on the source profile">{icon("check")}</span>'
        if profile.get("verified") is True
        else "",
        "PROFILE_LINK": f'<a class="text-link" href="{linkedin_url}" target="_blank" rel="noopener noreferrer">LinkedIn profile {icon("arrow")}</a>'
        if linkedin_url
        else "",
        "COPY_BUTTON": f'<button class="text-link" style="border:0;background:none;padding:0" data-copy-url="{linkedin_url}">{icon("copy")}Copy LinkedIn link</button>'
        if linkedin_url
        else "",
        "PLATFORM_NAV": "".join(nav),
        "SECTIONS": "\n".join(sections),
        "PROMPT_SECTION": OLGA_PROMPTS.replace("{{NEXT_ICON}}", icon("next"))
        if user == "olga"
        else "",
        "NEXT_ICON": icon("next"),
    }
    html = re.sub(
        r"\{\{([A-Z_]+)\}\}", lambda match: replacements[match[1]], HTML_TEMPLATE
    )
    workspace = user_root / "workspace"
    workspace.mkdir(parents=True, exist_ok=True)
    output = workspace / "profile.html"
    output.write_text(html, encoding="utf-8")
    return output


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate a source-linked trainer profile"
    )
    parser.add_argument(
        "--user", default="olga", help="User slug under users/ (default: olga)"
    )
    parser.add_argument("--open", action="store_true", help="Open in default browser")
    args = parser.parse_args()
    output = build_profile(user=args.user)
    print(f"Generated trainer profile page: {output}")
    if args.open:
        webbrowser.open(output.resolve().as_uri())


if __name__ == "__main__":
    main()
