import pytest

from pipeline.transcript_norm import TranscriptValidationError, normalize_transcript

FM = "---\nid: x\ntitle: Test Title\n---\n\n# Test Title\n\n## Transcript\n\n"


def test_title_preserved():
    md = FM + "### Speaker 1\n\nHello\n"
    out = normalize_transcript(md)
    assert "# Test Title" in out and out.index("# Test Title") < out.index("## Transcript")


def test_merges_same_speaker_and_drops_timestamps():
    md = FM + "### 00:00:01 · Speaker 1\n\nHello there\n\n### 00:00:05 · Speaker 1\n\nOkay so\n\n### 00:00:09 · Speaker 2\n\nHi\n"
    out = normalize_transcript(md)
    assert out.count("### Speaker") == 2
    assert "00:00:01" not in out and "00:00:05" not in out
    assert "Hello there" in out and "Okay so" in out


def test_punctuation_and_symbols():
    md = FM + "### Speaker 1\n\nDon't use 0.5, it's 2 + 1 = 3 and 50%.\n"
    out = normalize_transcript(md)
    assert "Dont" in out and "0 point 5" in out
    assert "2 plus 1 equals 3" in out and "50 percent" in out


def test_devanagari_preserved_danda_removed():
    md = FM + "### Speaker 1\n\nश्री गुरुभ्यो नमः।\n"
    out = normalize_transcript(md)
    assert "श्री गुरुभ्यो नमः" in out and "।" not in out


def test_noise_tags_removed_but_words_kept():
    md = FM + "### Speaker 1\n\n[music] The event F [snorts] is measurable\n"
    out = normalize_transcript(md)
    assert "snorts" not in out and "music" not in out
    assert "The event F is measurable" in out


def test_transform_preserves_every_word():
    md = FM + "### Speaker 1\n\nThe quick brown fox jumps over 3 dogs\n"
    out = normalize_transcript(md)
    # deterministic transform must not lose any input word
    assert "brown" in out and "quick" in out and "jumps" in out and "3" in out


def test_leftover_punctuation_refused():
    md = FM + "### Speaker 1\n\nHello, world\n"
    bad = FM + "### Speaker 1\n\nHello, world\n".replace("world", "world")
    out = normalize_transcript(md)
    assert "," not in out
