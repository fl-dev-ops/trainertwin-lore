"""Offline checks for the standalone profile export."""

from html.parser import HTMLParser

import yaml

from pipeline import profile


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags = []

    def handle_starttag(self, tag, attrs):
        self.tags.append((tag, dict(attrs)))


def test_profile_dates_images_and_accessible_cards(tmp_path, monkeypatch):
    monkeypatch.setattr(profile, "ROOT", tmp_path)
    data = tmp_path / "users" / "jane" / "data"
    posts = data / "linkedin" / "posts"
    posts.mkdir(parents=True)
    (data / "linkedin" / "jane.yaml").write_text(
        yaml.safe_dump(
            {
                "profile": {
                    "name": "Jane Doe",
                    "summary": "A source-backed introduction.",
                    "profilePicture": {"url": "https://example.com/jane.jpg"},
                    "publicIdentifier": "jane-doe",
                    "url": "https://linkedin.com/in/jane-doe",
                }
            }
        )
    )
    # The alphabetic order deliberately disagrees with the publication order.
    (posts / "z-old.md").write_text(
        "---\ndate: 2026-01-01\nurl: https://linkedin.com/posts/old\n---\nOlder post\n## Comments\nUnrelated follower comment\n"
    )
    (posts / "a-new.md").write_text(
        "---\ndate: 2026-09-21\nurl: https://linkedin.com/posts/new\n---\nNewer <post>\n### Quoting @other\nQuoted third party\n"
    )
    html = profile.build_profile("jane").read_text()
    assert html.index('href="https://linkedin.com/posts/new"') < html.index(
        'href="https://linkedin.com/posts/old"'
    )
    assert "Newer &lt;post&gt;" in html
    assert "Unrelated follower comment" not in html and "Quoted third party" not in html
    assert 'src="https://example.com/jane.jpg"' in html
    assert "@jane-doe" in html
    assert "No YouTube posts collected yet." in html
    assert "Core Action Principle" not in html and "alert(" not in html
    assert "unsplash" not in html and "{{" not in html
    page = Page()
    page.feed(html)
    for tag, attrs in page.tags:
        if tag == "button" and "arrow-button" in attrs.get("class", ""):
            assert attrs.get("aria-label") and attrs.get("aria-controls")
        if tag == "a" and attrs.get("target") == "_blank":
            assert attrs.get("rel") == "noopener noreferrer"

    # Missing/unsafe photos never substitute a stranger's portrait.
    (data / "linkedin" / "jane.yaml").write_text(
        yaml.safe_dump(
            {"profile": {"name": "Jane Doe", "profilePicture": "javascript:alert(1)"}}
        )
    )
    fallback = profile.build_profile("jane").read_text()
    assert '<span class="initials" aria-hidden="true">JD</span>' in fallback
    assert 'src="javascript:' not in fallback


def test_profile_optional_metadata_formats():
    assert profile.publication("20260921") == "2026-09-21"
    assert profile.publication("unknown") == ""
    assert profile.display_date("") == "Date unavailable"
    assert profile.duration("00:11:29") == "11:29"
    assert profile.duration("01:02:30") == "1:02:30"
    assert profile.duration(None) == ""
    assert profile.metric(None, "views") == ""
    assert profile.metric(0, "views") == "0 views"
    assert profile.metric(1, "views") == "1 view"
    assert profile.metric(9900, "views") == "9.9K views"
