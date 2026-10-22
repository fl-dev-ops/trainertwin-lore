import copy
import json
import threading
from types import SimpleNamespace

import httpx
import pytest

from social import cli, transcribe
from social.youtube import cli as youtube

RAW = {
    "speakers": [{"id": "1", "label": "Speaker 1"}, {"id": "2", "label": "Speaker 2"}],
    "turns": [{"speaker_id": "1", "text": "Hello Ahmed."}, {"speaker_id": "2", "text": "Hi."}],
}
VIDEO = {"id": "abcdefghijk", "title": "Call", "url": "https://youtube.com/watch?v=abcdefghijk",
         "upload_date": "20260901", "author": "Uploader"}
PROVIDER = {
    "status": "completed", "speech_model_used": "universal-3-5-pro", "text": "Hello Ahmed. Hi.",
    "words": [{"text": "Hello"}, {"text": "Ahmed."}, {"text": "Hi."}],
    "utterances": [{"speaker": "A", "text": "Hello Ahmed.", "start": 0, "end": 900},
                   {"speaker": "B", "text": "Hi.", "start": 1000, "end": 1200}],
}


@pytest.fixture
def assembly(monkeypatch):
    monkeypatch.setenv("ASSEMBLYAI_API_KEY", "test-key")
    monkeypatch.setattr(transcribe, "load_dotenv", lambda *a: None)
    monkeypatch.setattr(transcribe.time, "sleep", lambda _: None)
    calls = SimpleNamespace(uploaded=[], submitted=[], polled=0, deleted=[],
                            response=copy.deepcopy(PROVIDER), statuses=["completed"], fail=None)

    def handler(request):
        assert request.headers["authorization"] == "test-key"
        if calls.fail == (request.method, request.url.path):
            return httpx.Response(402, text="secret provider body must never be printed")
        if request.method == "POST" and request.url.path == "/v2/upload":
            calls.uploaded.append(request.read())
            return httpx.Response(200, json={"upload_url": "https://cdn.assemblyai.test/audio"})
        if request.method == "POST" and request.url.path == "/v2/transcript":
            calls.submitted.append(json.loads(request.read()))
            return httpx.Response(200, json={"id": "job-123"})
        if request.method == "GET":
            calls.polled += 1
            status = calls.statuses.pop(0) if len(calls.statuses) > 1 else calls.statuses[0]
            return httpx.Response(200, json={**calls.response, "status": status})
        if request.method == "DELETE":
            calls.deleted.append(request.url.path)
            return httpx.Response(200, json={"id": "job-123"})
        pytest.fail(f"Unexpected request: {request.method} {request.url.path}")

    real_client = httpx.Client
    monkeypatch.setattr(transcribe.httpx, "Client", lambda **kw: real_client(**kw, transport=httpx.MockTransport(handler)))
    return calls


def audio_file(directory):
    audio = directory / "test.mp3"
    audio.write_bytes(b"fake audio")
    return audio


def test_assembly_context_only_diarization_and_cleanup(tmp_path, assembly):
    audio = audio_file(tmp_path)
    result = transcribe.transcribe_audio(audio, "A JavaScript lesson about hoisting.")
    assert result == dict(RAW, model=transcribe.MODEL, speaker_count=2)
    assert assembly.submitted == [{"audio_url": "https://cdn.assemblyai.test/audio",
        "speech_models": [transcribe.MODEL], "speaker_labels": True, "language_detection": True,
        "prompt": "A JavaScript lesson about hoisting."}]
    assert assembly.deleted == ["/v2/transcript/job-123"]
    assert audio.exists(), "Caller-owned local originals must never be deleted"
    assert all(set(t) == {"speaker_id", "text"} for t in result["turns"])


@pytest.mark.parametrize("path", ["/v2/upload", "/v2/transcript"])
def test_paid_posts_not_retried_and_errors_do_not_leak(tmp_path, assembly, path):
    assembly.fail = ("POST", path)
    audio = audio_file(tmp_path)
    with pytest.raises(RuntimeError, match="HTTP 402") as exc:
        transcribe.transcribe_audio(audio)
    assert "secret" not in str(exc.value) and audio.exists()
    assert len(assembly.uploaded) <= 1 and not assembly.deleted


def test_queued_processing_are_polled(tmp_path, assembly):
    assembly.statuses = ["queued", "processing", "completed"]
    assert transcribe.transcribe_audio(audio_file(tmp_path))["speaker_count"] == 2
    assert assembly.polled == 3 and len(assembly.submitted) == 1


def test_provider_failure_preserves_job_checkpoint(tmp_path, assembly):
    assembly.statuses = ["error"]
    cache = tmp_path / "cache.json"
    with pytest.raises(RuntimeError, match="transcription failed"):
        transcribe.transcribe_audio(audio_file(tmp_path), cache_path=cache)
    assert not cache.exists() and cache.with_suffix(".job.json").exists()
    assert not assembly.deleted


def test_polling_timeout_resumes_without_second_paid_post(tmp_path, assembly, monkeypatch):
    assembly.statuses = ["processing"]
    monkeypatch.setattr(transcribe, "POLL_TIMEOUT", 0)
    audio = audio_file(tmp_path)
    cache = tmp_path / "cache.json"
    with pytest.raises(TimeoutError):
        transcribe.transcribe_audio(audio, "Coaching call", cache_path=cache)
    assert cache.with_suffix(".job.json").exists() and not cache.exists()
    assembly.statuses = ["completed"]
    result = transcribe.transcribe_audio(audio, "Coaching call", cache_path=cache)
    assert result["speaker_count"] == 2 and cache.exists()
    assert len(assembly.submitted) == len(assembly.uploaded) == 1
    assert not cache.with_suffix(".job.json").exists()
    # Once exported, cached JSON rebuilds with neither media nor credentials.
    audio.unlink()
    monkeypatch.delenv("ASSEMBLYAI_API_KEY")
    assert transcribe.transcribe_audio(audio, cache_path=cache) == result


@pytest.mark.parametrize("change", ["context", "audio", "id"])
def test_checkpoint_mismatch_stops_before_paid_call(tmp_path, assembly, change):
    audio = audio_file(tmp_path)
    cache = tmp_path / "cache.json"
    assembly.statuses = ["processing"]
    original_timeout = transcribe.POLL_TIMEOUT
    transcribe.POLL_TIMEOUT = 0
    try:
        with pytest.raises(TimeoutError):
            transcribe.transcribe_audio(audio, "old context", cache_path=cache)
    finally:
        transcribe.POLL_TIMEOUT = original_timeout
    context = "old context"
    if change == "context":
        context = "new context"
    elif change == "audio":
        audio.write_bytes(b"different audio")
    else:
        job = json.loads(cache.with_suffix(".job.json").read_text())
        job["id"] = "../../another-job"
        cache.with_suffix(".job.json").write_text(json.dumps(job))
    with pytest.raises(ValueError, match="Saved AssemblyAI job"):
        transcribe.transcribe_audio(audio, context, cache_path=cache)
    assert len(assembly.submitted) == 1


def test_delete_failure_warns_without_losing_transcript(tmp_path, assembly, capsys):
    assembly.fail = ("DELETE", "/v2/transcript/job-123")
    cache = tmp_path / "cache.json"
    assert transcribe.transcribe_audio(audio_file(tmp_path), cache_path=cache)["speaker_count"] == 2
    assert cache.exists() and "could not delete AssemblyAI" in capsys.readouterr().err


@pytest.mark.parametrize("change", ["fallback", "missing_turns", "partial", "bad_speaker", "bad_time", "missing_words"])
def test_incomplete_provider_output_is_rejected(tmp_path, assembly, change):
    if change == "fallback": assembly.response["speech_model_used"] = "universal-2"
    if change == "missing_turns": assembly.response["utterances"] = None
    if change == "partial": assembly.response["utterances"].pop()
    if change == "bad_speaker": assembly.response["utterances"][0]["speaker"] = None
    if change == "bad_time": assembly.response["utterances"][0]["end"] = -1
    if change == "missing_words": assembly.response["words"] = []
    cache = tmp_path / "cache.json"
    with pytest.raises((ValueError, TypeError)):
        transcribe.transcribe_audio(audio_file(tmp_path), cache_path=cache)
    assert not cache.exists() and not assembly.deleted


def test_overlapping_speakers_are_valid(tmp_path, assembly):
    assembly.response['utterances'][0].update(start=0, end=1500)
    assembly.response['utterances'][1].update(start=1000, end=1200)
    result = transcribe.transcribe_audio(audio_file(tmp_path))
    assert result['speaker_count'] == 2
    assert result['turns'] == RAW['turns']


def test_non_ascii_local_video_filename(tmp_path, assembly):
    video = tmp_path / "Dubai vs Saudi： Холодные [x1].mp4"
    video.write_bytes(b"fake local video")
    assert transcribe.transcribe_audio(video)["speaker_count"] == 2
    assert video.exists()


def test_silent_audio_and_temporary_url_download(tmp_path, monkeypatch, assembly):
    assembly.response.update(text=None, words=[], utterances=[])
    directories = []
    def download(url, directory):
        directories.append(directory)
        return audio_file(directory)
    monkeypatch.setattr(transcribe, "download_audio_ephemeral", download)
    assert transcribe.transcribe_media_url("https://example.test/audio")["speaker_count"] == 0
    assert not directories[0].exists()
    assembly.fail = ("POST", "/v2/upload")
    assert transcribe.transcribe_media_url("https://example.test/audio") is None
    assert all(not p.exists() for p in directories)


def test_missing_key_empty_or_missing_audio_never_uploads(tmp_path, assembly, monkeypatch):
    monkeypatch.delenv("ASSEMBLYAI_API_KEY")
    with pytest.raises(ValueError, match="ASSEMBLYAI_API_KEY"):
        transcribe.transcribe_audio(audio_file(tmp_path))
    empty = tmp_path / "empty.mp3"
    empty.touch()
    with pytest.raises(ValueError, match="empty audio"):
        transcribe.transcribe_audio(empty)
    assert not assembly.uploaded


@pytest.mark.parametrize("raw", [
    {}, {"speakers": {}, "turns": []},
    {"speakers": [{"id": "1", "label": "One"}] * 2, "turns": []},
    {"speakers": [], "turns": [{"speaker_id": "1", "text": "Hello"}]},
    {"speakers": [{"id": "1", "label": "One"}], "turns": []},
    dict(RAW, speaker_count=3), dict(RAW, model="another-model"), dict(RAW, duration=10),
    {"speakers": RAW["speakers"], "turns": [dict(RAW["turns"][0], timestamp="00:00:00")]},
])
def test_invalid_schema_rejected(raw):
    with pytest.raises((ValueError, TypeError)):
        transcribe.validate_transcript(raw)


def test_count_uses_ids_not_names_and_drops_silent_speakers():
    raw = {"speakers": [{"id": "1", "label": "Guest"}, {"id": "2", "label": "Guest"},
                        {"id": "3", "label": "Silent"}], "turns": RAW["turns"]}
    assert transcribe.validate_transcript(raw)["speaker_count"] == 2
    assert transcribe.validate_transcript({"speakers": [], "turns": []})["speaker_count"] == 0


def test_collection_cache_metadata_and_preserve_legacy(tmp_path, assembly):
    directories = []
    def download(url, directory):
        directories.append(directory)
        path = directory / f"Call [{VIDEO['id']}].mp3"
        path.write_bytes(b"audio")
        return path
    selected = [dict(VIDEO)]
    directory = tmp_path / "data/youtube/video"
    cli.transcribe_videos("YouTube", selected, directory, download)
    source = next(directory.glob("*.md"))
    meta = transcribe.transcript_metadata(source)
    assert meta["model"] == transcribe.MODEL and meta["speaker_count"] == 2
    assert meta["speakers"] == {"1": "Speaker 1", "2": "Speaker 2"}
    assert "duration" not in meta and "00:00" not in source.read_text()
    assert selected[0]["speaker_count"] == 2
    youtube.save_video_index("https://youtube.com/@person", selected, directory.parent / "person.yaml")
    assert all(not d.exists() for d in directories) and not list(tmp_path.rglob("*.mp3"))
    cli.transcribe_videos("YouTube", selected, directory, download)
    assert len(assembly.submitted) == len(directories) == 1
    source.unlink()
    cli.transcribe_videos("YouTube", selected, directory, download)
    assert source.exists() and len(assembly.submitted) == len(directories) == 1
    # Neither bracketed legacy filenames nor old model metadata cause a paid rerun.
    body = source.read_text().replace(transcribe.MODEL, "nvidia/canary-qwen-2.5b + sortformer")
    source.unlink()
    legacy = directory / f"2020-01-01-Call [{VIDEO['id']}].md"
    legacy.write_text(body)
    cli.transcribe_videos("YouTube", selected, directory, download)
    assert legacy.read_text() == body and len(assembly.submitted) == 1


def test_parallel_jobs_overlap_and_failure_keeps_others(tmp_path, monkeypatch, capsys):
    barrier = threading.Barrier(2)
    converted = []
    def download(url, temporary):
        barrier.wait(timeout=10)
        path = temporary / f"Call [{url.split('=')[1]}].mp3"
        path.write_bytes(b"audio")
        return path
    def succeed(audio, context, key, **kwargs):
        converted.append(context)
        return transcribe.validate_transcript(RAW)
    monkeypatch.setattr(transcribe, "get_api_key", lambda _: "test-key")
    monkeypatch.setattr(transcribe, "transcribe_audio", succeed)
    videos = [dict(VIDEO, id=f"video{n}", title=f"Call {n}", url=f"https://youtube.com/watch?v=video{n}") for n in range(2)]
    cli.transcribe_videos("YouTube", videos, tmp_path / "video", download, workers=2)
    assert len(converted) == 2 and [v["speaker_count"] for v in videos] == [2, 2]
    def fail_one(url, temporary):
        if "video9" in url: raise ValueError("download interrupted")
        path = temporary / "Call [video1].mp3"
        path.write_bytes(b"audio")
        return path
    kept = dict(VIDEO, id="video1", title="Keep", url="https://youtube.com/watch?v=video1")
    with pytest.raises(ValueError, match="download interrupted"):
        cli.transcribe_videos("YouTube", [dict(VIDEO, id="video9", url="https://youtube.com/watch?v=video9"), kept], tmp_path / "video2", fail_one, workers=2)
    assert (tmp_path / "assemblyai-json/video1.json").exists()
    assert list((tmp_path / "video2").glob("*keep-video1.md"))
    assert "download interrupted" in capsys.readouterr().err


def test_workers_positive_and_invalid_ids(tmp_path):
    with pytest.raises(ValueError, match="workers"):
        cli.transcribe_videos("YouTube", [], tmp_path, lambda u,d: None, workers=0)
    with pytest.raises(ValueError, match="Invalid video ID"):
        transcribe.transcript_path(tmp_path, "../../secret")
    for prefix in ("a", "b"):
        (tmp_path / f"{prefix}-{VIDEO['id']}.md").touch()
    with pytest.raises(ValueError, match="Multiple transcripts"):
        transcribe.needs_transcript(tmp_path, VIDEO["id"])


def test_writer_preserves_existing_path_and_category(tmp_path):
    old = tmp_path / f"old-{VIDEO['id']}.md"
    old.write_text(f"---\nid: {VIDEO['id']}\ncategory: training\n---\nLegacy speech")
    with pytest.raises(ValueError, match="refusing to overwrite"):
        transcribe.save_transcript(dict(VIDEO), {"speakers": [], "turns": []}, tmp_path)
    assert transcribe.save_transcript(dict(VIDEO), RAW, tmp_path) == old
    assert transcribe.transcript_metadata(old)["category"] == "training"


def test_rebuild_does_not_relabel_old_provider_cache(tmp_path):
    old = tmp_path / "gemini-json"
    old.mkdir()
    (old / f"{VIDEO['id']}.json").write_text(json.dumps(dict(RAW, model="gemini-2.5-flash")))
    assert transcribe.rebuild_transcripts([dict(VIDEO)], tmp_path / "video") == 0


def test_single_transcription_implementation():
    from pathlib import Path
    root = Path(__file__).resolve().parents[2]
    assert cli.transcribe_videos is transcribe.transcribe_videos
    assert youtube.download_video_audio is transcribe.download_video_audio
    for p in (root / 'social').rglob('*.py'):
        if 'tests' in p.parts or p.name == 'transcribe.py': continue
        code = p.read_text()
        assert '/v2/transcript' not in code
        assert 'def transcribe_audio(' not in code
        assert 'from google import genai' not in code


def test_migration_backs_up_original_and_resumes(tmp_path, assembly):
    directory = tmp_path / 'videos'
    video = dict(VIDEO)
    original = transcribe.save_transcript(video, RAW, directory)
    original.write_text(original.read_text().replace(transcribe.MODEL, 'nvidia/canary-qwen-2.5b + sortformer'))
    before = original.read_bytes()
    backup = tmp_path / 'backups'
    def download(url, temporary):
        path = temporary / f"Call [{VIDEO['id']}].mp3"
        path.write_bytes(b'audio')
        return path
    transcribe.transcribe_videos('Loom', [dict(VIDEO)], directory, download,
                                retranscribe=True, backup_dir=backup)
    assert (backup / original.name).read_bytes() == before
    assert transcribe.transcript_metadata(original)['model'] == transcribe.MODEL
    transcribe.transcribe_videos('Loom', [dict(VIDEO)], directory, download,
                                retranscribe=True, backup_dir=backup)
    assert len(assembly.submitted) == 1
    assert (backup / original.name).read_bytes() == before


def test_migration_requires_backup_and_failure_preserves_original(tmp_path, assembly):
    directory = tmp_path / 'videos'
    original = transcribe.save_transcript(dict(VIDEO), RAW, directory)
    original.write_text(original.read_text().replace(transcribe.MODEL, 'gemini-2.5-flash'))
    before = original.read_bytes()
    with pytest.raises(ValueError, match='backup directory'):
        transcribe.transcribe_videos('YouTube', [dict(VIDEO)], directory, None, retranscribe=True)
    assembly.statuses = ['error']
    def download(url, temporary):
        path = temporary / f"Call [{VIDEO['id']}].mp3"
        path.write_bytes(b'audio')
        return path
    with pytest.raises(RuntimeError, match='transcription failed'):
        transcribe.transcribe_videos('YouTube', [dict(VIDEO)], directory, download,
                                    retranscribe=True, backup_dir=tmp_path / 'backups')
    assert original.read_bytes() == before


def test_credit_failure_stops_queued_paid_work(tmp_path, assembly):
    assembly.fail = ('POST', '/v2/transcript')
    downloads = []
    def download(url, temporary):
        downloads.append(url)
        ident = url.rsplit('=', 1)[1]
        path = temporary / f'Call [{ident}].mp3'
        path.write_bytes(b'audio')
        return path
    videos = [dict(VIDEO, id=f'video{n}', url=f'https://youtube.com/watch?v=video{n}') for n in range(20)]
    with pytest.raises(transcribe.AssemblyAIAccountError):
        transcribe.transcribe_videos('YouTube', videos, tmp_path / 'videos', download, workers=1)
    assert len(assembly.uploaded) == len(downloads) == 1
