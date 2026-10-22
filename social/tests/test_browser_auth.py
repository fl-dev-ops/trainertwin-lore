from social.youtube.cli import ytdlp_auth_args


def test_browser_cookies_require_explicit_opt_in(monkeypatch):
    monkeypatch.delenv('YT_DLP_COOKIES', raising=False)
    monkeypatch.delenv('YT_DLP_COOKIES_FROM_BROWSER', raising=False)
    assert ytdlp_auth_args() == []
    monkeypatch.setenv('YT_DLP_COOKIES_FROM_BROWSER', 'safari')
    assert ytdlp_auth_args() == ['--cookies-from-browser', 'safari']
    monkeypatch.setenv('YT_DLP_COOKIES', '/private/cookies.txt')
    assert ytdlp_auth_args() == ['--cookies', '/private/cookies.txt']


def test_authenticated_download_uses_default_cookie_compatible_client(tmp_path, monkeypatch):
    from types import SimpleNamespace

    from social import transcribe
    monkeypatch.delenv('YT_DLP_COOKIES', raising=False)
    monkeypatch.setenv('YT_DLP_COOKIES_FROM_BROWSER', 'safari')
    def download(command, **kwargs):
        assert '--extractor-args' not in command
        assert '--cookies-from-browser' in command and 'safari' in command
        assert '--cookies' not in command
        (tmp_path / 'Video [abcdefghijk].mp3').write_bytes(b'audio')
        return SimpleNamespace(returncode=0)
    monkeypatch.setattr(transcribe.subprocess, 'run', download)
    assert transcribe.download_video_audio('https://youtube.com/watch?v=abcdefghijk', tmp_path).is_file()
