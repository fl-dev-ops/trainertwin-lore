import pytest

from pipeline.transcript_norm import TranscriptValidationError, normalize_transcript
from social.content import read, read_turns

FM = "---\nid: x\ntitle: Test Title\nspeakers:\n  speaker_1: null\n  speaker_2: Olga\n---\n\n"


def turns(out):
    meta, body = read(out)
    return read_turns(body, meta["speakers"])


def test_front_matter_kept_and_no_markdown_added():
    out = normalize_transcript(FM + "speaker_1: Hello\n")
    assert out.startswith(FM) and "#" not in out.split("---\n", 2)[2]


def test_merges_same_speaker():
    out = normalize_transcript(FM + "speaker_1: Hello there\n\nspeaker_1: Okay so\n\nspeaker_2: Hi\n")
    assert turns(out) == [("speaker_1", "Hello there\n\nOkay so"), ("speaker_2", "Hi")]


def test_punctuation_and_symbols():
    out = normalize_transcript(FM + "speaker_1: Don't use 0.5, it's 2 + 1 = 3 and 50%.\n")
    assert "Dont" in out and "0 point 5" in out
    assert "2 plus 1 equals 3" in out and "50 percent" in out


def test_devanagari_preserved_danda_removed():
    out = normalize_transcript(FM + "speaker_1: श्री गुरुभ्यो नमः।\n")
    assert "श्री गुरुभ्यो नमः" in out and "।" not in out


def test_noise_tags_removed_but_words_kept():
    out = normalize_transcript(FM + "speaker_1: [music] The event F [snorts] is measurable\n")
    assert "snorts" not in out and "music" not in out
    assert "The event F is measurable" in out


def test_no_speech_file_is_unchanged_and_stray_text_refused():
    assert normalize_transcript(FM) == FM
    with pytest.raises(TranscriptValidationError):
        normalize_transcript(FM + "text without a speaker\n")


def test_leftover_punctuation_removed():
    assert "," not in normalize_transcript(FM + "speaker_1: Hello, world\n")
