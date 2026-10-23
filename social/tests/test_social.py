import json
import subprocess
from datetime import date
from pathlib import Path

import httpx
import pytest

from social.content import read as read_content
import yaml

from social import cli as social
from social import gemini, transcribe
from social.dates import in_window, published_day
from social.instagram import cli as instagram
from social.linkedin import cli as linkedin
from social.twitter import cli as twitter
from social.youtube import cli as youtube


@pytest.fixture
def read_source():
    return pytest.importorskip("pipeline.sources", reason="Legacy source parser is absent in this workspace").read_source


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


def test_youtube_skips_old_metadata_only(tmp_path, monkeypatch):
    since = date(2026, 8, 1)
    videos = [
        {"id": "old", "title": "Old", "url": "old", "upload_date": "20260731"},
        {"id": "new", "title": "New", "url": "new", "upload_date": "20260801"},
    ]
    monkeypatch.setattr(social.youtube, "fetch_channel_videos", lambda url: videos)
    data, audios = tmp_path / "users/me/data/youtube", tmp_path / "users/me/audios"
    monkeypatch.setattr(
        social.youtube,
        "fetch_video_details",
        lambda url: {"description": "Video description"},
    )
    social.collect_youtube("https://youtube.com/@me", data, since, False)
    manifest = yaml.safe_load((data / "me.yaml").read_text())
    assert [v["id"] for v in manifest["videos"]] == ["new"]
    assert manifest["videos"][0]["url"] == "https://www.youtube.com/watch?v=new"
    assert manifest["videos"][0]["description"] == "Video description"
    assert sorted(p.name for p in data.iterdir()) == ["me.yaml"]
    assert not audios.exists()


def test_youtube_reuses_manifest_metadata_when_live_details_are_blocked(tmp_path, monkeypatch):
    data = tmp_path / "users/me/data/youtube"
    data.mkdir(parents=True)
    (data / "me.yaml").write_text(
        yaml.safe_dump(
            {
                "videos": [
                    {
                        "id": "blocked1234",
                        "title": "Saved title",
                        "url": "https://youtube.com/watch?v=blocked1234",
                        "upload_date": "2026-08-01",
                        "description": "Saved description",
                        "author": "me",
                    }
                ]
            }
        )
    )
    monkeypatch.setattr(
        social.youtube,
        "fetch_channel_videos",
        lambda _: [
            {
                "id": "blocked1234",
                "title": "Saved title",
                "url": "https://youtube.com/watch?v=blocked1234",
            }
        ],
    )
    monkeypatch.setattr(
        social.youtube,
        "fetch_video_details",
        lambda _: pytest.fail("saved metadata should avoid a blocked live lookup"),
    )

    social.collect_youtube(
        "https://youtube.com/@me", data, date(2005, 4, 23), False
    )

    manifest = yaml.safe_load((data / "me.yaml").read_text())
    assert manifest["videos"][0]["upload_date"] == "2026-08-01"


def test_youtube_audio_download_retries_alternate_client(tmp_path, monkeypatch):
    calls = []

    def run(command, **kwargs):
        calls.append(command)
        if len(calls) > 1:
            (tmp_path / "Video [blocked1234].mp3").write_bytes(b"audio")
        return subprocess.CompletedProcess(
            command, 1 if len(calls) == 1 else 0, "", "HTTP Error 403"
        )

    monkeypatch.setattr(youtube.subprocess, "run", run)
    assert youtube.download_video_audio("https://youtube.com/watch?v=blocked1234", tmp_path)
    assert "youtube:player_client=web_embedded" in calls[0]
    assert "youtube:player_client=android_vr" in calls[1]


def test_youtube_discovery_preserves_channel_author(monkeypatch):
    payload = {
        "entries": [
            {
                "id": "pQCLpcXSx2s",
                "title": "A helpful title",
                "uploader_id": "@careerwithvasanth",
            }
        ]
    }
    monkeypatch.setattr(
        youtube.subprocess,
        "run",
        lambda *args, **kwargs: subprocess.CompletedProcess(
            args[0], 0, json.dumps(payload), ""
        ),
    )
    videos = youtube.fetch_channel_videos("https://youtube.com/@careerwithvasanth")
    assert videos[0]["author"] == "careerwithvasanth"


def test_youtube_date_fetches_description_with_missing_flat_metadata(monkeypatch):
    video = {"id": "pQCLpcXSx2s", "url": "https://youtube.com/watch?v=pQCLpcXSx2s"}
    monkeypatch.setattr(
        youtube,
        "fetch_video_details",
        lambda _: {
            "upload_date": "20260813",
            "description": "Full video description",
            "uploader_id": "@careerwithvasanth",
        },
    )
    assert social.video_date(video) == date(2026, 8, 13)
    assert video["description"] == "Full video description"
    assert video["author"] == "careerwithvasanth"


def test_youtube_manifest_keeps_earlier_videos(tmp_path, monkeypatch):
    data = tmp_path / "users/me/data/youtube"
    data.mkdir(parents=True)
    (data / "me.yaml").write_text(
        yaml.safe_dump(
            {
                "channel_url": "https://youtube.com/@me/videos",
                "videos": [{"id": "previous123", "description": "Earlier video"}],
            }
        )
    )
    monkeypatch.setattr(
        social.youtube,
        "fetch_channel_videos",
        lambda _: [
            {
                "id": "newvideo123",
                "title": "New",
                "url": "https://youtube.com/watch?v=newvideo123",
                "upload_date": "20260801",
                "description": "New description",
            }
        ],
    )
    social.collect_youtube(
        "https://youtube.com/@me/shorts",
        data,
        date(2026, 8, 1),
        False,
    )
    index = yaml.safe_load((data / "me.yaml").read_text())
    assert index["total_videos"] == 2
    assert {v["id"] for v in index["videos"]} == {"previous123", "newvideo123"}


def test_youtube_markdown_preserves_metadata_without_time_fields(tmp_path):
    video_dir = tmp_path / "data/youtube/video"
    video = {"id": "pQCLpcXSx2s", "title": "A helpful title",
             "url": "https://www.youtube.com/watch?v=pQCLpcXSx2s", "upload_date": "2026-08-13",
             "description": "Description is metadata, not quoted speech.", "author": "careerwithvasanth"}
    result = {"speakers": [{"id": "1", "label": "Speaker 1"}],
              "turns": [{"speaker_id": "1", "text": "Ask the buyer what matters."}]}
    path = transcribe.save_transcript(video, result, video_dir)
    assert path.name == "2026-08-13-a-helpful-title-pQCLpcXSx2s.md"
    meta = transcribe.transcript_metadata(path)
    assert meta["date"] == "2026-08-13" and meta["url"] == video["url"]
    assert meta["author"] == "careerwithvasanth" and meta["speaker_count"] == 1
    assert read_content(path.read_text())[1] == "speaker_1: Ask the buyer what matters"
    assert "#" not in path.read_text().split("---\n", 2)[2]
    assert "duration" not in meta
    assert transcribe.save_transcript(dict(video, title="Another title"), result, video_dir) == path
    assert transcribe.transcript_metadata(path)["title"] == "Another title"
    path.write_text(path.read_text().replace("id: pQCLpcXSx2s", "id: wrong-id"))
    transcribe.save_transcript(video, result, video_dir)
    assert transcribe.transcript_metadata(path)["id"] == video["id"]


def test_gemini_ocr_in_memory_and_ephemeral_files(monkeypatch):
    monkeypatch.setenv("OPENROUTER_API_KEY", "fake-openrouter-key")
    calls = []

    def mock_handler(request: httpx.Request) -> httpx.Response:
        calls.append((request.method, str(request.url)))
        if "chat/completions" in str(request.url):
            return httpx.Response(
                200,
                json={
                    "choices": [
                        {
                            "message": {
                                "content": "**Extracted Slide Text**: 5 Rules for Closing Deals"
                            }
                        }
                    ]
                },
            )
        return httpx.Response(
            200, content=b"fake-image-bytes", headers={"content-type": "image/jpeg"}
        )

    mock_client = httpx.Client(transport=httpx.MockTransport(mock_handler))
    res = gemini.ocr_image_url("https://example.com/slide1.jpg", client=mock_client)
    assert "5 Rules for Closing Deals" in res
    assert any("chat/completions" in url for _, url in calls)


def test_instagram_reels_transcription_and_carousel_ocr(tmp_path, monkeypatch):
    posts_dir = tmp_path / "posts"
    # Mock Reel transcription
    monkeypatch.setattr(
        instagram,
        "transcribe_media_url",
        lambda url, **kwargs: transcribe.validate_transcript({
            "speakers": [{"id": "1", "label": "Speaker 1"}],
            "turns": [{"speaker_id": "1", "text": "Stop pitching and start asking better questions."}],
        }),
    )
    # Mock Carousel OCR
    monkeypatch.setattr(
        instagram,
        "ocr_image_url",
        lambda url: (
            "**Slide Text:** Never send property brochures before finding out budget and timeline."
        ),
    )

    reel_post = {
        "id": "111222333",
        "type": "reel",
        "timestamp": "2026-09-15T12:00:00Z",
        "url": "https://www.instagram.com/reel/abc123xyz/",
        "caption": "A quick tip for cold calling in Dubai.",
        "videoUrl": "https://cdn.instagram.com/reel.mp4",
        "videoDuration": 30.5,
        "musicInfo": {"artistName": "Audio Artist", "songName": "Sales Motivation"},
    }
    carousel_post = {
        "id": "444555666",
        "type": "carousel",
        "timestamp": "2026-09-16T12:00:00Z",
        "url": "https://www.instagram.com/p/carousel123/",
        "caption": "Slide breakdown of objection handling.",
        "childPosts": [
            {
                "id": "c1",
                "displayUrl": "https://cdn.instagram.com/slide1.jpg",
                "alt": "May be text about brochures",
            },
            {
                "id": "c2",
                "displayUrl": "https://cdn.instagram.com/slide2.jpg",
                "alt": "May be infographic",
            },
        ],
    }

    index = instagram.save_posts_to_markdown([reel_post, carousel_post], posts_dir)
    assert len(index) == 2
    assert index[0]["hasTranscript"] is True
    assert index[1]["slide_count"] == 2

    reel_md = (posts_dir / Path(index[0]["file"]).name).read_text()
    reel_meta, speak = read_content(reel_md)
    assert speak.startswith("speaker_1: Stop pitching") and reel_meta["speakers"] == {"speaker_1": None}
    assert reel_meta["caption"] and "videoUrl" not in reel_meta
    assert index[0]["speaker_count"] == 1
    assert "duration:" not in speak and "00:00" not in speak
    assert "Stop pitching and start asking better questions." in reel_md
    assert "transcript: true" in reel_md

    carousel_md = (posts_dir / Path(index[1]["file"]).name).read_text()
    carousel_meta, _ = read_content(carousel_md)
    assert any("Never send property brochures before finding out budget" in s for s in carousel_meta["slides"])
    assert "Alt text" not in carousel_md and "###" not in carousel_md


def test_linkedin_rich_reposts_articles_and_documents(tmp_path, read_source):
    posts_dir = tmp_path / "posts"
    post = {
        "id": "7000000000000000001",
        "postedAt": {"date": "2026-09-20T10:00:00Z"},
        "linkedinUrl": "https://www.linkedin.com/posts/olgasi_update-7000000000000000001",
        "content": "Check out this great analysis by my colleague!",
        "isRepost": True,
        "isQuotePost": True,
        "resharedPost": {
            "author": {"name": "Jane Smith", "publicIdentifier": "janesmith"},
            "linkedinUrl": "https://www.linkedin.com/posts/janesmith_original-8000000",
            "content": "Dubai real estate yields remain the highest among global financial capitals.",
        },
        "article": {
            "title": "UAE Market Trends 2026",
            "subtitle": "Analysis of off-plan vs secondary",
            "link": "https://www.linkedin.com/pulse/uae-market-trends",
        },
        "document": {
            "title": "Quarterly Sales Guide.pdf",
            "documentUrl": "https://media.licdn.com/doc.pdf",
            "pageCount": 12,
        },
        "stats": {"likesCount": 55, "commentsCount": 8, "repostsCount": 14},
    }

    index = linkedin.save_posts_to_markdown([post], posts_dir)
    assert len(index) == 1
    assert index[0]["hasResharedPost"] is True
    assert index[0]["hasArticle"] is True
    assert index[0]["hasDocument"] is True

    md_text = next(posts_dir.glob("*.md")).read_text()
    assert "is_repost: true" in md_text
    assert "is_quote_post: true" in md_text
    assert "reposts: 14" in md_text
    assert "### Quoting @Jane Smith:" in md_text
    assert "> Dubai real estate yields remain the highest" in md_text
    assert (
        "### Shared Article: [UAE Market Trends 2026](https://www.linkedin.com/pulse/uae-market-trends)"
        in md_text
    )
    assert (
        "### Shared Document: [Quarterly Sales Guide.pdf](https://media.licdn.com/doc.pdf) (12 pages)"
        in md_text
    )

    # Verify pipeline ignores quoted third-party speech
    source = read_source(next(posts_dir.glob("*.md")), tmp_path)
    assert len(source.units) == 1
    assert "Check out this great analysis" in source.units[0]["text"]
    assert "highest among global financial capitals" not in source.units[0]["text"]


def test_twitter_note_tweet_and_quoted_expansion(tmp_path):
    tweets_dir = tmp_path / "tweets"
    long_text = (
        "This is a full long-form note tweet that exceeds standard Twitter length. " * 5
    )
    tweet = {
        "id": "1800000000000000001",
        "createdAt": "Sun Sep 27 10:15:30 +0000 2026",
        "text": "Short truncated preview...",
        "note_tweet": {"text": long_text},
        "conversationId": "1800000000000000000",
        "inReplyToScreenName": "client",
        "quoted_tweet": {
            "id": "1799999999999999999",
            "author": {"userName": "dubai_analyst"},
            "text": "Original analyst tweet on transaction volumes.",
            "url": "https://x.com/dubai_analyst/status/1799999999999999999",
        },
    }

    index = twitter.save_tweets_to_markdown([tweet], tweets_dir)
    assert len(index) == 1

    md_text = next(tweets_dir.glob("*.md")).read_text()
    assert long_text in md_text
    assert "Short truncated preview" not in md_text
    assert "conversationId: '1800000000000000000'" in md_text
    assert "inReplyTo: '@client'" in md_text
    quoted = read_content(md_text)[0]["quoted"]
    assert quoted["author"] == "dubai_analyst" and quoted["text"] == "Original analyst tweet on transaction volumes."
    assert quoted["url"] == "https://x.com/dubai_analyst/status/1799999999999999999"


def test_reel_always_uses_audio_and_preserves_saved_transcript(tmp_path, monkeypatch):
    calls = []
    def convert(url, **kwargs):
        calls.append(url)
        return transcribe.validate_transcript({"speakers": [{"id": "1", "label": "Speaker 1"}],
                                              "turns": [{"speaker_id": "1", "text": "Spoken audio text"}]})
    monkeypatch.setattr(instagram, "transcribe_media_url", convert)
    post = {"id": "reel1", "type": "reel", "url": "https://instagram.com/reel/one/",
            "caption": "Caption", "transcript": "Ignore this supplied scraper transcript"}
    entry = instagram.save_posts_to_markdown([post], tmp_path)[0]
    original = next(tmp_path.glob("*.md")).read_text()
    assert entry["speaker_count"] == 1 and entry['hasTranscript'] is True and len(calls) == 1
    assert "Ignore this supplied scraper transcript" not in original
    entry = instagram.save_posts_to_markdown([post], tmp_path)[0]
    assert entry["speaker_count"] == 1 and entry["hasTranscript"] is True and len(calls) == 1
    assert next(tmp_path.glob("*.md")).read_text() == original
