import json
import subprocess
from datetime import date
from pathlib import Path

import httpx
import pytest
import yaml

from pipeline.sources import read_source
from social import cli, gemini, progress, transcribe
from social import fs as social_fs
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


def test_oversized_audio_splits_and_resumes_without_reupload(tmp_path, monkeypatch):
    audio = tmp_path / "long.mp3"
    audio.write_bytes(b"temporary audio")
    raw = tmp_path / "results"
    monkeypatch.setattr(youtube, "audio_seconds", lambda _: 7201)
    uploads = []

    def split(command, **kwargs):
        Path(command[-1]).write_bytes(b"one audio segment")
        return subprocess.CompletedProcess(command, 0, "", "")

    monkeypatch.setattr(youtube.subprocess, "run", split)

    class Job:
        def upload_files(self, files, **kwargs):
            self.path = Path(files[0])
            assert self.path.exists()
            uploads.append(self.path.name)

        def start(self):
            assert not self.path.exists()

        def wait_until_complete(self, **kwargs):
            self.job_state = "Completed"
            return self

        def is_successful(self):
            return True

        def download_outputs(self, directory):
            (Path(directory) / f"{self.path.name}.json").write_text(
                json.dumps({"diarized_transcript": {"entries": [{
                    "speaker_id": "1", "transcript": "A spoken sentence from this part.",
                    "start_time_seconds": 2, "end_time_seconds": 5,
                }]}})
            )

    class Client:
        def __init__(self, **kwargs):
            self.speech_to_text_job = self

        def create_job(self, **kwargs):
            return Job()

    monkeypatch.setattr("sarvamai.SarvamAI", Client)
    youtube.transcribe_long_audio(audio, raw, 10, "fake")
    entries = youtube.load_entries(raw / "010.mp3.json")
    assert uploads == ["010-part00.mp3", "010-part01.mp3", "010-part02.mp3"]
    assert [entry.start for entry in entries] == [2, 3602, 7202]
    assert audio.exists()  # The collector removes it only after all videos complete.
    youtube.transcribe_long_audio(audio, raw, 10, "fake")
    assert len(uploads) == 3  # Cached text results, no duplicate paid requests.
    assert not list(tmp_path.rglob("010-part*.mp3"))


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


def test_atomic_write_survives_mid_write_interruption(tmp_path, monkeypatch):
    """An interrupted write leaves the old file intact and no permanent partial content."""
    target = tmp_path / "video.md"
    social_fs.atomic_write(target, "old content")

    real_temp = social_fs.tempfile.NamedTemporaryFile

    class InterruptingHandle:
        def __init__(self, real):
            self._real = real

        def __enter__(self):
            return self

        def __exit__(self, *args):
            self._real.__exit__(*args)

        def __getattr__(self, name):
            return getattr(self._real, name)

        def write(self, text):
            self._real.write(text[:3])  # Partial write, then crash.
            raise OSError("simulated crash mid-write")

    def interrupting_temp(*args, **kwargs):
        return InterruptingHandle(real_temp(*args, **kwargs))

    monkeypatch.setattr(social_fs.tempfile, "NamedTemporaryFile", interrupting_temp)
    with pytest.raises(OSError, match="simulated crash"):
        social_fs.atomic_write(target, "new content")
    assert target.read_text() == "old content"  # Original file intact.
    assert not [p for p in tmp_path.iterdir() if p.name != "video.md"]  # Failed temp cleaned up.

    monkeypatch.undo()  # Restore the real temp-file writer for the recovery check.
    social_fs.atomic_write(target, "new content")
    assert target.read_text() == "new content"
    assert not [p for p in tmp_path.iterdir() if p.name != "video.md"]  # Temps cleaned.


def test_youtube_description_with_hr_rule_is_kept_not_regenerated(tmp_path, monkeypatch):
    """A valid transcript whose description contains an indented '---' rule is recognized."""
    video_dir = tmp_path / "video"
    video_dir.mkdir(parents=True)
    existing = video_dir / "2026-05-31-should-Z-Zj0bYQqnU.md"
    body = (
        "---\n"
        "id: Z-Zj0bYQqnU\n"
        "title: Should Frontend Developers Learn AI\n"
        "description: '🚀 Cohort announcement\n\n"
        "  What is the last innovation?\n\n"
        "  ---\n\n"
        "  About CareerWithVasanth\n\n"
        "  #careerwithvasanth'\n"
        "duration: 00:10:22\n"
        "transcript: true\n"
        "---\n\n# t\n\n## Transcript\n\n### 00:00:00 · Speaker 1\n\nSpoken text.\n"
    )
    existing.write_text(body)
    audios = tmp_path / "audios"
    raw = tmp_path / "raw"
    audios.mkdir()
    raw.mkdir()
    (audios / "Should [Z-Zj0bYQqnU].mp3").write_bytes(b"fake audio")
    (raw / "001.mp3.json").write_text(
        '{"diarized_transcript":{"entries":['
        '{"speaker_id":"1","transcript":"Spoken text.","start_time_seconds":0,"end_time_seconds":2}'
        ']}}'
    )
    monkeypatch.setattr(youtube, "ffprobe_duration", lambda _: "00:10:22")
    messages = []
    monkeypatch.setattr(youtube, "status", lambda message: messages.append(message))
    count = youtube.build_markdowns_from_json(
        audios, raw, video_dir,
        [{"id": "Z-Zj0bYQqnU", "title": "Should Frontend Developers Learn AI", "upload_date": "2026-05-31"}],
    )
    assert count == 1
    assert not any("regenerating" in m for m in messages)  # HR rule inside description is valid YAML.
    lines = existing.read_text().splitlines()
    end = lines.index("---", 1)
    assert str(yaml.safe_load("\n".join(lines[1:end]))["id"]) == "Z-Zj0bYQqnU"


def test_youtube_replaces_corrupt_existing_transcript(tmp_path, monkeypatch):
    """A half-written transcript (interrupted write) is regenerated instead of crashing."""
    audios = tmp_path / "audios"
    raw = tmp_path / "raw"
    video_dir = tmp_path / "data/youtube/video"
    audios.mkdir()
    raw.mkdir()
    (audios / "A helpful title [pQCLpcXSx2s].mp3").write_bytes(b"fake audio")
    (raw / "001.mp3.json").write_text(
        '{"diarized_transcript":{"entries":['
        '{"speaker_id":"1","transcript":"Ask the buyer what matters to them before you pitch the property.","start_time_seconds":10,"end_time_seconds":15}'
        ']}}'
    )
    monkeypatch.setattr(youtube, "ffprobe_duration", lambda _: "00:00:30")
    corrupt = video_dir / "2026-08-13-helpful-pQCLpcXSx2s.md"
    corrupt.parent.mkdir(parents=True)
    corrupt.write_text(
        "---\nid: pQCLpcXSx2s\ndescription: '🚀 unterminated quoted scalar\n---\n"
    )
    videos = [{"id": "pQCLpcXSx2s", "title": "A helpful title", "upload_date": "2026-08-13"}]
    assert youtube.build_markdowns_from_json(audios, raw, video_dir, videos) == 1
    assert read_source(corrupt, tmp_path / "data").title == "A helpful title"
    assert "🚀" not in corrupt.read_text()


def test_youtube_skips_paid_retranscription_for_saved_videos(tmp_path, monkeypatch):
    """Videos whose Markdown transcripts exist are not downloaded or sent to Sarvam again."""
    data = tmp_path / "users/me/data/youtube"
    video_dir = data / "video"
    video_dir.mkdir(parents=True)
    calls = {"downloads": 0, "submits": 0}

    monkeypatch.setattr(youtube, "fetch_channel_videos", lambda _: [
        {"id": "olddddd11", "title": "Old", "url": "https://youtube.com/watch?v=olddddd11", "upload_date": "20260731"},
        {"id": "newdddddd", "title": "New", "url": "https://youtube.com/watch?v=newddddddd", "upload_date": "20260801"},
    ])

    def fake_download(url, directory):
        calls["downloads"] += 1
        return directory

    monkeypatch.setattr(youtube, "download_video_audio", fake_download)
    monkeypatch.setattr(youtube, "get_sarvam_key", lambda _: "key")
    monkeypatch.setattr(youtube, "submit_sarvam_jobs", lambda *a: calls.__setitem__("submits", calls["submits"] + 1))
    monkeypatch.setattr(youtube, "wait_and_download_sarvam", lambda *a: None)
    monkeypatch.setattr(youtube, "ffprobe_duration", lambda _: "00:00:30")
    monkeypatch.setattr(youtube, "load_date_cache", lambda _: {})
    monkeypatch.setattr(youtube, "save_date_cache", lambda *_: None)

    def fake_build(audios_dir, json_dir, directory, videos, **kwargs):
        calls["built"] = len(videos)
        return len(videos)

    monkeypatch.setattr(youtube, "build_markdowns_from_json", fake_build)
    (video_dir / "2026-07-31-old-olddddd11.md").write_text(
        "---\nid: oldddddd11\n---\n\n# Old\n\n## Transcript\n\n### 00:00:00 · Speaker 1\n\nOld spoken text.\n"
    )
    cli.collect_youtube("https://youtube.com/@me", data, tmp_path / "audios", date(2026, 7, 1), True)
    assert calls["downloads"] == 1  # Only the new video was downloaded.
    assert calls["submits"] == 1
    assert calls["built"] == 2  # Export still covers every indexed video.
    assert not list((tmp_path / "audios").rglob("*.mp3"))  # Audio deleted after build.


def test_worker_crash_is_recorded_not_fatal(tmp_path, monkeypatch, capsys):
    """An unexpected per-platform exception is reported and the command still exits 1."""
    import yaml as yaml_module

    monkeypatch.setattr(cli, "ROOT", tmp_path)
    monkeypatch.setattr(progress.sys.stderr, "isatty", lambda: False)

    def crash(*args):
        raise yaml_module.YAMLError("malformed frontmatter")

    monkeypatch.setattr(cli, "collect_twitter", crash)
    with pytest.raises(SystemExit) as error:
        cli.main(
            ["--user", "test-user", "--since", "2020-01-01", "--twitter", "https://x.com/test"]
        )
    assert error.value.code == 1
    output = capsys.readouterr()
    assert "malformed frontmatter" in output.err
    assert "Traceback" not in output.err
    assert output.out == ""


def test_harvest_comments_402_preserves_remaining_posts(tmp_path, monkeypatch):
    """When HarvestAPI credits run out (HTTP 402) on comments, save remaining posts without crashing."""
    posts_dir = tmp_path / "posts"
    posts = [
        {"id": "post1", "content": "Post 1 text", "engagement": {"comments": 5}, "linkedinUrl": "https://linkedin.com/p1"},
        {"id": "post2", "content": "Post 2 text", "engagement": {"comments": 3}, "linkedinUrl": "https://linkedin.com/p2"},
        {"id": "post3", "content": "Post 3 text", "engagement": {"comments": 2}, "linkedinUrl": "https://linkedin.com/p3"},
    ]
    comment_calls = []

    def mock_fetch_comments(url, key):
        comment_calls.append(url)
        raise RuntimeError("HarvestAPI HTTP 402: Used all credits available - please top up your balance")

    monkeypatch.setattr(linkedin, "fetch_comments_for_post", mock_fetch_comments)

    index = linkedin.save_posts_to_markdown(posts, posts_dir, api_key="test-key", comments_min=1)
    # All 3 posts must be successfully saved!
    assert len(index) == 3
    # Comment call attempted once, recognized 402, and stopped hammering the API
    assert len(comment_calls) == 1
    files = list(posts_dir.glob("*.md"))
    assert len(files) == 3
    contents = [f.read_text() for f in files]
    assert any("Post 1 text" in c for c in contents)
    assert any("Post 2 text" in c for c in contents)
    assert any("Post 3 text" in c for c in contents)



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
