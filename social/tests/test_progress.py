import io
import json
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from threading import Barrier

import pytest

from social import cli, progress, transcribe


def test_background_progress_is_line_based_and_stderr_only(monkeypatch, capsys):
    monkeypatch.setattr(progress.sys.stderr, "isatty", lambda: False)
    assert list(progress.track(["a", "b", "c"], "Export", unit="post")) == [
        "a",
        "b",
        "c",
    ]
    output = capsys.readouterr()
    assert output.out == ""
    assert "Export: 0/3 post processed" in output.err
    assert "Export: 3/3 post processed — finished" in output.err
    assert "\r" not in output.err and "\x1b" not in output.err


@pytest.mark.parametrize("items,total", [([], "0/0"), (iter([1, 2]), "2/?")])
def test_empty_and_unknown_totals(items, total, monkeypatch, capsys):
    monkeypatch.setattr(progress.sys.stderr, "isatty", lambda: False)
    list(progress.track(items, "Items"))
    assert f"Items: {total} item processed — finished" in capsys.readouterr().err


def test_terminal_uses_tqdm_bar(monkeypatch, capsys):
    class Terminal(io.StringIO):
        def isatty(self):
            return True

    terminal = Terminal()
    monkeypatch.setattr(progress.sys, "stderr", terminal)
    for _ in progress.track([1, 2], "Export", unit="post"):
        progress.status("Exporting")
    output = terminal.getvalue()
    assert "100%" in output and "2/2" in output and "Exporting" in output
    assert capsys.readouterr().out == ""


def test_progress_does_not_report_success_after_iterator_failure(monkeypatch, capsys):
    monkeypatch.setattr(progress.sys.stderr, "isatty", lambda: False)

    def broken():
        yield "one"
        raise ValueError("provider failed")

    with pytest.raises(ValueError, match="provider failed"):
        list(progress.track(broken(), "Export", total=2))
    output = capsys.readouterr().err
    assert "1/2 item processed — stopped" in output
    assert "finished" not in output


def test_progress_closes_without_counting_unprocessed_item(monkeypatch, capsys):
    monkeypatch.setattr(progress.sys.stderr, "isatty", lambda: False)
    iterator = progress.track([1, 2], "Export")
    assert next(iterator) == 1
    iterator.close()
    assert "0/2 item processed — stopped" in capsys.readouterr().err


def test_cli_keeps_failure_status_with_platform_progress(tmp_path, monkeypatch, capsys):
    monkeypatch.setattr(cli, "ROOT", tmp_path)
    monkeypatch.setattr(progress.sys.stderr, "isatty", lambda: False)
    calls = []

    def fail(*args):
        raise RuntimeError("provider unavailable")

    def succeed(*args):
        calls.append("twitter")
        for label in ("profile", "tweets", "saved"):
            progress.stage(label)

    monkeypatch.setattr(cli, "collect_linkedin", fail)
    monkeypatch.setattr(cli, "collect_twitter", succeed)
    with pytest.raises(SystemExit) as error:
        cli.main(
            [
                "--user",
                "test-user",
                "--since",
                "2020-01-01",
                "--linkedin",
                "https://linkedin.com/in/test",
                "--twitter",
                "https://x.com/test",
            ]
        )
    assert error.value.code == 1
    output = capsys.readouterr()
    assert calls == ["twitter"]
    assert "provider unavailable" in output.err
    assert "twitter: collection finished" in output.err
    assert "linkedin: collection finished" not in output.err
    assert "linkedin: 0/3 stages — stopped" in output.err
    assert "twitter: 3/3 stages — finished" in output.err
    assert output.out == ""


def test_platforms_overlap_and_write_separately(tmp_path, monkeypatch, capsys):
    monkeypatch.setattr(cli, "ROOT", tmp_path)
    monkeypatch.setattr(progress.sys.stderr, "isatty", lambda: False)
    rendezvous = Barrier(4, timeout=5)

    def collector(platform):
        def run(url, data, *args):
            rendezvous.wait()  # Sequential execution would time out here.
            data.mkdir(parents=True)
            (data / "result.txt").write_text(platform)
            for label in ("profile", "posts", "saved"):
                progress.stage(label)
            if platform == "youtube":
                progress.stage("transcripts")

        return run

    for platform in ("linkedin", "twitter", "instagram", "youtube"):
        monkeypatch.setattr(cli, f"collect_{platform}", collector(platform))
    cli.main(
        [
            "--user",
            "test-user",
            "--since",
            "2020-01-01",
            "--linkedin",
            "https://linkedin.com/in/test",
            "--twitter",
            "https://x.com/test",
            "--instagram",
            "https://instagram.com/test",
            "--youtube",
            "https://youtube.com/@test",
        ]
    )
    root = tmp_path / "users" / "test-user" / "data"
    for platform in ("linkedin", "twitter", "instagram", "youtube"):
        assert (root / platform / "result.txt").read_text() == platform
    output = capsys.readouterr()
    for platform in ("linkedin", "twitter", "instagram"):
        assert f"{platform}: 3/3 stages — finished" in output.err
    assert "youtube: 4/4 stages — finished" in output.err
    assert output.out == ""


def test_platform_progress_is_thread_local_and_cleans_up(monkeypatch, capsys):
    monkeypatch.setattr(progress.sys.stderr, "isatty", lambda: False)
    with progress.platform_progress("Instagram", 0, 3, 2):
        progress.stage("profile")
        progress.stage("posts")
        progress.stage("saved")
    progress.stage("outside context")
    output = capsys.readouterr()
    assert "Instagram: 3/3 stages — finished" in output.err
    assert "outside context" not in output.err
    assert output.out == ""


def test_terminal_renders_concurrent_platform_rows(monkeypatch):
    class Terminal(io.StringIO):
        def isatty(self):
            return True

    terminal = Terminal()
    monkeypatch.setattr(progress.sys, "stderr", terminal)
    rendezvous = Barrier(2, timeout=5)

    def run(name, position):
        with progress.platform_progress(name, position, 1, 2):
            for _ in progress.track([1], f"{name} items"):
                rendezvous.wait()
                progress.stage("saved")

    with ThreadPoolExecutor(max_workers=2) as pool:
        jobs = [
            pool.submit(run, name, pos)
            for pos, name in enumerate(("LinkedIn", "Instagram"))
        ]
        for job in jobs:
            job.result()

    output = terminal.getvalue()
    assert "LinkedIn" in output and "Instagram" in output
    assert "LinkedIn items" in output and "Instagram items" in output
    assert output.count("100%") >= 2


def test_youtube_metadata_progress_reports_skipped_dates(tmp_path, monkeypatch, capsys):
    monkeypatch.setattr(progress.sys.stderr, "isatty", lambda: False)
    monkeypatch.setattr(
        cli.youtube,
        "fetch_channel_videos",
        lambda _: [
            {"id": "missingdate", "url": "https://youtube.com/watch?v=missingdate"},
        ],
    )
    monkeypatch.setattr(cli, "video_date", lambda _: None)
    with progress.platform_progress("youtube", 0, 4, 1):
        cli.collect_youtube(
            "https://youtube.com/@test",
            tmp_path / "test/data/youtube",
            tmp_path / "audios",
            cli.date(2020, 1, 1),
            False,
        )
    output = capsys.readouterr()
    assert "youtube: 4/4 stages — finished" in output.err
    assert "publication date unavailable" in output.err
    assert "1/1 video processed — finished" in output.err
    assert "selected 0/1 videos" in output.err
    assert output.out == ""


def test_reel_shows_provider_stages_without_fake_percentage(monkeypatch, capsys):
    monkeypatch.setattr(transcribe, "get_sarvam_key", lambda _: "test-key")

    def download(_, directory):
        audio = directory / "audio.mp3"
        audio.write_bytes(b"test audio" * 200)
        return audio

    class Job:
        def upload_files(self, files, **kwargs):
            self.audio = Path(files[0])
            assert self.audio.exists()

        def start(self):
            assert not self.audio.exists()

        def wait_until_complete(self, **kwargs):
            assert not self.audio.exists()
            return self

        def is_successful(self):
            return True

        def download_outputs(self, directory):
            (Path(directory) / "audio.json").write_text(
                json.dumps(
                    {
                        "diarized_transcript": {
                            "entries": [
                                {
                                    "speaker_id": "1",
                                    "transcript": "A spoken example.",
                                    "start_time_seconds": 0,
                                    "end_time_seconds": 2,
                                }
                            ]
                        },
                    }
                )
            )

    class Client:
        speech_to_text_job = None

        def __init__(self, **kwargs):
            self.speech_to_text_job = self

        def create_job(self, **kwargs):
            return Job()

    monkeypatch.setattr(transcribe, "download_audio_ephemeral", download)
    monkeypatch.setattr("sarvamai.SarvamAI", Client)
    assert (
        transcribe.transcribe_media_url("https://example.org/reel")[0]["text"]
        == "A spoken example."
    )
    output = capsys.readouterr()
    assert "Reel: uploading audio" in output.err
    assert "percentage unavailable" in output.err
    assert "Reel: downloading transcript results" in output.err
    assert "transcript ready (1 turns)" in output.err
    assert output.out == ""
