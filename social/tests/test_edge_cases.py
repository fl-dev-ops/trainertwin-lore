import httpx
import pytest

from pipeline.sources import read_source
from social import gemini, transcribe
from social.instagram import cli as instagram
from social.linkedin import cli as linkedin
from social.twitter import cli as twitter
from social.youtube import cli as youtube


def test_silent_video_handled_cleanly(tmp_path):
    """Sarvam returns 0 entries (silent video or music only). Must NOT crash or call SystemExit."""
    sarvam_json = tmp_path / "silent.json"
    sarvam_json.write_text('{"diarized_transcript": {"entries": []}}')
    entries = youtube.load_entries(sarvam_json)
    assert entries == []

    audios = tmp_path / "audios"
    raw = tmp_path / "raw"
    video_dir = tmp_path / "video"
    audios.mkdir()
    raw.mkdir()
    (audios / "Silent Clip [abc12345678].mp3").write_bytes(b"dummy")
    (raw / "001.mp3.json").write_text('{"diarized_transcript": {"entries": []}}')

    videos = [{"id": "abc12345678", "title": "Silent Clip", "description": "Visual video only."}]
    count = youtube.build_markdowns_from_json(audios, raw, video_dir, videos)
    assert count == 1
    md_file = next(video_dir.glob("*.md"))
    content = md_file.read_text()
    assert "No spoken dialogue detected" in content
    assert "Visual video only" in content


def test_corrupt_or_zero_byte_audio_skipped(tmp_path, monkeypatch):
    """Audio file under 1000 bytes (corrupt or 0 bytes) is skipped without upload to Sarvam."""
    empty_file = tmp_path / "audio.mp3"
    empty_file.write_bytes(b"")  # 0 bytes

    monkeypatch.setattr(transcribe, "download_audio_ephemeral", lambda url, target: empty_file)
    monkeypatch.setenv("SARVAM_API_KEY", "fake-key")

    turns = transcribe.transcribe_media_url("https://example.com/empty.mp4")
    assert turns == []


def test_openrouter_ocr_refusal_or_null_content(monkeypatch):
    """OpenRouter returns safety block or null message content without raising exceptions."""
    monkeypatch.setenv("OPENROUTER_API_KEY", "fake-key")

    def mock_handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(
            200,
            json={
                "choices": [
                    {
                        "finish_reason": "content_filter",
                        "message": {"content": None},
                    }
                ]
            },
        )

    mock_client = httpx.Client(transport=httpx.MockTransport(mock_handler))
    res = gemini.ocr_image_bytes(b"image_bytes", client=mock_client)
    assert res == ""


def test_reel_transcript_with_no_turns_does_not_crash_pipeline(tmp_path):
    """Reel with transcript: true in frontmatter but no spoken turns parses caption cleanly."""
    post = tmp_path / "reel.md"
    post.write_text(
        "---\n"
        "id: '123'\n"
        "transcript: true\n"
        "---\n\n"
        "## Caption\n"
        "A purely visual reel with text overlay only.\n\n"
        "## Transcript\n\n"
        "> [No spoken dialogue detected]\n"
    )
    source = read_source(post, tmp_path)
    assert source is not None
    assert len(source.units) == 1
    assert "A purely visual reel with text overlay only" in source.units[0]["text"]
    assert source.units[0]["t"] == ""
    assert source.units[0]["speaker_id"] == ""


def test_twitter_retweeted_status_and_article_preview(tmp_path):
    """Twitter retweets preserve original author and text under ### Quoting @author."""
    tweets_dir = tmp_path / "tweets"
    tweet = {
        "id": "2000000000000000001",
        "createdAt": "Mon Sep 28 12:00:00 +0000 2026",
        "text": "RT @expert_analyst: Dubai Land Department reports record transaction volume.",
        "isRetweet": True,
        "retweeted_status": {
            "id": "1999999999999999999",
            "author": {"userName": "expert_analyst"},
            "text": "Dubai Land Department reports record transaction volume across off-plan sectors.",
            "url": "https://x.com/expert_analyst/status/1999999999999999999",
        },
    }
    index = twitter.save_tweets_to_markdown([tweet], tweets_dir)
    assert len(index) == 1

    md_text = next(tweets_dir.glob("*.md")).read_text()
    assert "is_retweet: true" in md_text
    assert "### Quoting @expert_analyst:" in md_text
    assert "> Dubai Land Department reports record transaction volume" in md_text
    assert "> Original: https://x.com/expert_analyst/status/1999999999999999999" in md_text


def test_linkedin_post_empty_text_with_document_only(tmp_path):
    """LinkedIn post with no typed text but a shared document and article is preserved."""
    posts_dir = tmp_path / "posts"
    post = {
        "id": "7500000000000000001",
        "postedAt": {"date": "2026-09-28T14:00:00Z"},
        "linkedinUrl": "https://www.linkedin.com/posts/olgasi_presentation",
        "content": "",  # Empty author text
        "document": {
            "title": "Mastering Cold Calling Slides.pdf",
            "documentUrl": "https://media.licdn.com/slides.pdf",
            "pageCount": 25,
        },
        "stats": {"likesCount": 40, "commentsCount": 2},
    }
    index = linkedin.save_posts_to_markdown([post], posts_dir)
    assert len(index) == 1
    assert index[0]["hasDocument"] is True

    md_text = next(posts_dir.glob("*.md")).read_text()
    assert "### Shared Document: [Mastering Cold Calling Slides.pdf](https://media.licdn.com/slides.pdf) (25 pages)" in md_text


def test_instagram_carousel_missing_childposts(tmp_path):
    """Instagram carousel with empty or missing childPosts does not raise KeyError."""
    posts_dir = tmp_path / "posts"
    post = {
        "id": "333444555",
        "type": "carousel",
        "timestamp": "2026-09-28T15:00:00Z",
        "url": "https://www.instagram.com/p/carousel_empty/",
        "caption": "A carousel post where child posts are not returned by the scraper.",
        "childPosts": [],  # Empty
    }
    index = instagram.save_posts_to_markdown([post], posts_dir)
    assert len(index) == 1
    md_text = next(posts_dir.glob("*.md")).read_text()
    assert "## Carousel Slides" not in md_text
    assert "A carousel post where child posts are not returned" in md_text


def test_instagram_single_image_ocr_keeps_caption_and_alt(tmp_path, monkeypatch):
    urls = []

    def ocr(url):
        urls.append(url)
        return "Offer ends Friday. Call for details."

    monkeypatch.setattr(instagram, "ocr_image_url", ocr)
    post = {
        "id": "12345",
        "type": "Image",
        "timestamp": "2026-09-20T10:00:00Z",
        "url": "https://www.instagram.com/p/example/",
        "caption": "New training announcement.",
        "displayUrl": "https://example.org/photo.jpg",
        "alt": "Flyer with an announcement",
    }
    posts_dir = tmp_path / "posts"
    index = instagram.save_posts_to_markdown([post], posts_dir)
    text = (posts_dir / index[0]["file"].split("/")[-1]).read_text()
    assert urls == ["https://example.org/photo.jpg"]
    assert "type: image" in text
    assert "## Caption\nNew training announcement." in text
    assert "## Image Text\n\n> Alt text: Flyer with an announcement" in text
    assert "Offer ends Friday. Call for details." in text
    assert not list(tmp_path.rglob("*.jpg"))


def test_instagram_single_image_without_media_preserves_caption(tmp_path, monkeypatch):
    monkeypatch.setattr(
        instagram, "ocr_image_url", lambda _: pytest.fail("No image URL to OCR")
    )
    post = {"id": "67890", "type": "image", "caption": "Text only post."}
    posts_dir = tmp_path / "posts"
    index = instagram.save_posts_to_markdown([post], posts_dir)
    text = (posts_dir / index[0]["file"].split("/")[-1]).read_text()
    assert "## Caption\nText only post." in text
    assert "## Image Text" not in text
