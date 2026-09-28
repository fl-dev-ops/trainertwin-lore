from datetime import date

import pytest
import yaml

from social import cli as social
from social.dates import in_window, published_day
from social.instagram import cli as instagram
from social.linkedin import cli as linkedin
from social.twitter import cli as twitter


def test_absolute_utc_dates_and_cli_validation(tmp_path, monkeypatch):
    assert published_day("2026-08-01T00:30:00+02:00") == date(2026, 7, 31)
    assert published_day("Fri Aug 01 02:00:00 +0000 2025") == date(2025, 8, 1)
    assert published_day("20260801") == date(2026, 8, 1)
    assert in_window("2026-08-01T00:00:00Z", date(2026, 8, 1), date(2026, 8, 2))
    with pytest.raises(ValueError, match="no publication date"):
        published_day(None)
    with pytest.raises(ValueError, match="lacks timezone"):
        published_day("2026-08-01T12:00:00")
    with pytest.raises(SystemExit):
        social.main(
            [
                "--user",
                "../other",
                "--since",
                "2026-08-01",
                "--twitter",
                "https://x.com/me",
            ]
        )
    with pytest.raises(SystemExit):
        social.main(
            ["--user", "jane", "--since", "2026-02-30", "--twitter", "https://x.com/me"]
        )
    with pytest.raises(SystemExit):
        social.main(
            [
                "--user",
                "jane",
                "--since",
                "2026-08-01",
                "--twitter",
                "https://x.com/me/status/123",
            ]
        )

    monkeypatch.setattr(social, "ROOT", tmp_path)
    calls = []
    monkeypatch.setattr(
        social,
        "collect_twitter",
        lambda url, data, since: calls.append((url, data, since)),
    )
    social.main(
        ["--user", "jane", "--since", "2026-08-01", "--twitter", "https://x.com/me"]
    )
    assert calls == [
        ("https://x.com/me", tmp_path / "users/jane/data/twitter", date(2026, 8, 1))
    ]


def test_linkedin_and_twitter_stop_at_old_page(monkeypatch):
    since = date(2026, 8, 1)

    class Response:
        status_code = 200

        def __init__(self, data):
            self.data = data

        def json(self):
            return self.data

    class Client:
        calls = 0

        def __init__(self, **kwargs):
            pass

        def __enter__(self):
            return self

        def __exit__(self, *args):
            pass

        def get(self, *args, **kwargs):
            self.calls += 1
            return Response(
                {
                    "elements": [{"postedAt": {"date": "2026-08-01T00:00:00Z"}}],
                    "pagination": {"paginationToken": "next"},
                }
                if self.calls == 1
                else {
                    "elements": [{"postedAt": {"date": "2026-07-31T00:00:00Z"}}],
                    "pagination": {"paginationToken": "more"},
                }
            )

    client = Client()
    monkeypatch.setattr(linkedin.httpx, "Client", lambda **kwargs: client)
    assert (
        len(linkedin.fetch_all_posts("https://linkedin.com/in/me", "key", since=since))
        == 1
    )
    assert client.calls == 2
    monkeypatch.setattr(
        linkedin.httpx,
        "Client",
        lambda **kwargs: type(
            "FailClient",
            (Client,),
            {
                "get": lambda self, *args, **kwargs: type(
                    "Failure", (), {"status_code": 503}
                )()
            },
        )(),
    )
    with pytest.raises(ValueError, match="refusing partial date window"):
        linkedin.fetch_all_posts("https://linkedin.com/in/me", "key", since=since)

    pages = iter(
        [
            {
                "data": {"tweets": [{"createdAt": "2026-08-01T00:00:00Z"}]},
                "has_next_page": True,
                "next_cursor": "next",
            },
            {
                "data": {"tweets": [{"createdAt": "2026-07-31T00:00:00Z"}]},
                "has_next_page": True,
                "next_cursor": "more",
            },
        ]
    )
    monkeypatch.setattr(twitter, "fetch_api", lambda *args: next(pages))
    monkeypatch.setattr(twitter.time, "sleep", lambda *_: None)
    assert len(twitter.fetch_user_tweets("me", "key", since=since)) == 1


def test_instagram_applies_actor_and_local_bounds(monkeypatch):
    captured = {}

    def actor(actor_id, payload, api_key):
        captured.update(payload)
        return [
            {"timestamp": "2026-07-31T12:00:00Z"},
            {"timestamp": "2026-08-01T12:00:00Z"},
        ]

    monkeypatch.setattr(instagram, "run_apify_actor", actor)
    posts = instagram.fetch_posts("me", "key", since=date(2026, 8, 1))
    assert len(posts) == 1
    assert captured["onlyPostsNewerThan"] == "2026-08-01"
    assert captured["resultsLimit"] == 10000
    monkeypatch.setattr(
        instagram, "run_apify_actor", lambda *args: [{"timestamp": None}]
    )
    with pytest.raises(ValueError, match="no publication date"):
        instagram.fetch_posts("me", "key", since=date(2026, 8, 1))


def test_youtube_skips_old_and_guards_existing_selection(tmp_path, monkeypatch):
    since = date(2026, 8, 1)
    videos = [
        {"id": "old", "title": "Old", "url": "old", "upload_date": "20260731"},
        {"id": "new", "title": "New", "url": "new", "upload_date": "20260801"},
    ]
    monkeypatch.setattr(social.youtube, "fetch_channel_videos", lambda url: videos)
    data, audios = tmp_path / "data", tmp_path / "audios"
    social.collect_youtube("https://youtube.com/@me", data, audios, since, False)
    manifest = yaml.safe_load((data / "channel.yaml").read_text())
    assert [v["id"] for v in manifest["videos"]] == ["new"]
    assert manifest["videos"][0]["url"] == "https://www.youtube.com/watch?v=new"
    assert not audios.exists()
    selection = data / "runs" / since.isoformat() / "selection.json"
    selection.parent.mkdir(parents=True)
    selection.write_text('["different"]')
    with pytest.raises(ValueError, match="selection changed"):
        social.collect_youtube("https://youtube.com/@me", data, audios, since, True)
