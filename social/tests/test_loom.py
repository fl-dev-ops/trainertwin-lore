from datetime import date
from types import SimpleNamespace

import pytest
import yaml

from social import cli, transcribe
from social.loom import cli as loom
from social.youtube import cli as youtube

ID = "5912cd3e872a4a1f890a56983f4c9583"
URL = f"https://www.loom.com/share/{ID}"


@pytest.fixture(autouse=True)
def no_paid_calls(monkeypatch):
    monkeypatch.setenv("ASSEMBLYAI_API_KEY", "test-key")
    monkeypatch.setattr(transcribe, "_request", lambda *a, **kw: pytest.fail("Unexpected paid call"))


def test_share_links_and_manifest(tmp_path):
    assert loom.share_url(f"https://loom.com/share/Ahmed-{ID.upper()}?sid=abc") == URL
    source = tmp_path / "loom.yaml"
    source.write_text(f"videos:\n- url: {URL}\n- url: https://loom.com/share/{ID}\n")
    assert loom.source_urls(str(source)) == [URL]
    assert cli.profile_url(str(source), "loom") == str(source)
    assert cli.profile_url(URL, "loom") == URL
    for invalid in [f"http://loom.com/share/{ID}", f"https://evil.test/share/{ID}",
                    "https://loom.com/folders/abc", f"https://user@loom.com/share/{ID}"]:
        with pytest.raises(ValueError):
            loom.share_url(invalid)
    source.write_text("no links")
    with pytest.raises(ValueError, match="No Loom share links"):
        loom.source_urls(str(source))


def test_metadata_does_not_use_loom_transcript(monkeypatch):
    monkeypatch.setattr(youtube, "fetch_video_details", lambda url: {
        "id": ID, "title": "Role play", "upload_date": "20260901", "uploader": "Liveit Up",
        "duration": 3320, "subtitles": {"en": [{"url": "https://example.org/loom-whisper"}]},
    })
    assert loom.fetch_video(URL) == {"id": ID, "url": URL, "title": "Role play", "upload_date": "20260901",
                                    "description": "", "author": "Liveit Up"}


def test_loom_audio_download_uses_no_subtitles(tmp_path, monkeypatch):
    def download(command, **kwargs):
        assert command[0] == "yt-dlp"
        assert command[command.index("-f") + 1] == "hls-raw-audio-audio/bestaudio/best"
        assert "--write-subs" not in command and "--write-auto-subs" not in command
        (tmp_path / f"Role play [{ID}].mp3").write_bytes(b"audio")
        return SimpleNamespace(returncode=0)
    monkeypatch.setattr(transcribe.subprocess, "run", download)
    assert loom.download_audio(URL, tmp_path).name.endswith(f"[{ID}].mp3")


def test_loom_registered_and_metadata_only(tmp_path, monkeypatch):
    monkeypatch.setattr(cli, "ROOT", tmp_path)
    monkeypatch.setattr(loom, "fetch_video", lambda url: {
        "id": ID, "url": url, "title": "Call", "upload_date": "20260901",
    })
    monkeypatch.setattr(cli, "transcribe_videos", lambda *a: pytest.fail("Must not transcribe metadata-only"))
    cli.main(["--user", "test", "--since", "2020-01-01", "--loom", URL, "--no-transcribe"])
    folder = tmp_path / "users/test/data/loom"
    assert yaml.safe_load((folder / "collected.yaml").read_text())["videos"][0]["id"] == ID
    assert not (folder / "videos").exists()


def test_loom_filters_dates_and_keeps_input_manifest(tmp_path, monkeypatch):
    second = "1ddaa7cff1d34df7a09594e4de58e517"
    data = tmp_path / "test/data/loom"
    data.mkdir(parents=True)
    source = data / "loom.yaml"
    source.write_text(f"videos:\n- url: {URL}\n- url: https://www.loom.com/share/{second}\n")
    original = source.read_bytes()
    def metadata(url):
        vid = url.rsplit("/", 1)[-1]
        return {"id": vid, "url": url, "upload_date": "20260901" if vid == ID else "20100101"}
    monkeypatch.setattr(loom, "fetch_video", metadata)
    cli.collect_loom(str(source), data, date(2026, 1, 1), False)
    assert source.read_bytes() == original
    assert [v["id"] for v in yaml.safe_load((data / "collected.yaml").read_text())["videos"]] == [ID]


def test_loom_uses_shared_assemblyai_flow_and_count(tmp_path, monkeypatch):
    data = tmp_path / "test/data/loom"
    monkeypatch.setattr(loom, "fetch_video", lambda url: {
        "id": ID, "url": url, "title": "Olga & Ahmed", "upload_date": "20260901", "author": "Uploader",
    })
    directories, calls = [], []
    def download(url, directory):
        directories.append(directory)
        audio = directory / f"Olga & Ahmed [{ID}].mp3"
        audio.write_bytes(b"audio")
        return audio
    def convert(audio, context, key, **kwargs):
        calls.append(audio)
        assert audio.is_file() and "Title: Olga & Ahmed" in context and "Channel: Uploader" in context
        return transcribe.validate_transcript({"speakers": [{"id": "1", "label": "Olga"}],
                                              "turns": [{"speaker_id": "1", "text": "Hello Ahmed."}]})
    monkeypatch.setattr(loom, "download_audio", download)
    monkeypatch.setattr(transcribe, "transcribe_audio", convert)
    cli.collect_loom(URL, data, date(2020, 1, 1), True)
    path = next((data / "videos").glob("*.md"))
    meta = transcribe.transcript_metadata(path)
    assert meta["url"] == URL and meta["model"] == transcribe.MODEL and meta["speaker_count"] == 1
    assert "duration" not in meta and "### Speaker 1 · Olga" in path.read_text()
    assert yaml.safe_load((data / "collected.yaml").read_text())["videos"][0]["speaker_count"] == 1
    assert not list(data.rglob("*.mp3")) and (data / "assemblyai-json" / f"{ID}.json").exists()
    assert all(not d.exists() for d in directories)
    cli.collect_loom(URL, data, date(2020, 1, 1), True)
    assert len(calls) == 1


def test_failed_download_cleans_partial_audio_and_preserves_source(tmp_path, monkeypatch):
    videos = tmp_path / "videos"
    videos.mkdir()
    old = videos / f"old-{ID}.md"
    old.write_text("Legacy transcript")
    directories = []
    def fail(url, directory):
        directories.append(directory)
        (directory / "partial.mp4.part").write_bytes(b"partial audio")
        raise ValueError("download interrupted")
    with pytest.raises(ValueError, match="download interrupted"):
        cli.transcribe_videos("Loom", [{"id": ID, "url": URL}], videos, fail)
    assert old.read_text() == "Legacy transcript"
    assert all(not d.exists() for d in directories)
    assert not list(tmp_path.rglob("*.part"))


@pytest.mark.parametrize("vid,url", [(ID, URL), ("abcdefghijk", "https://www.youtube.com/watch?v=abcdefghijk")])
def test_shared_writer_keeps_platform_urls(tmp_path, vid, url):
    path = transcribe.save_transcript({"id": vid, "title": "Call", "upload_date": "20260101"}, {
        "speakers": [{"id": "1", "label": "Speaker 1"}],
        "turns": [{"speaker_id": "1", "text": "Hello."}],
    }, tmp_path)
    assert transcribe.transcript_metadata(path)["url"] == url
