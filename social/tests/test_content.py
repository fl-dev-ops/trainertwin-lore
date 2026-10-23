"""The one file layout: front matter + content only. Migration keeps every kept word."""
import pytest

from social import content
from social.content import migrate, plain, read, read_turns


def test_transcript_drops_headings_and_keeps_turns():
    old = ("---\nid: v\ntitle: Lesson one\ntranscript: true\nspeakers:\n  speaker_1: null\n---\n\n"
           "# Lesson one\n\n## Transcript\n\nspeaker_1: first part\n\nsecond part\n")
    new = migrate("users/u/data/youtube/video/a.md", old)
    meta, body = read(new)
    assert "#" not in body and meta["title"] == "Lesson one"
    assert read_turns(body, meta["speakers"]) == [("speaker_1", "first part\n\nsecond part")]
    assert migrate("users/u/data/youtube/video/a.md", new) == new


def test_no_speech_transcript_has_empty_body():
    old = "---\nid: v\ntitle: t\ntranscript: true\nspeakers: {}\n---\n\n# t\n\n## Transcript\n\n> [No spoken dialogue detected]\n"
    assert read(migrate("users/u/data/loom/videos/a.md", old))[1] == ""


def test_instagram_keeps_caption_ocr_and_only_author_comments():
    old = ("---\nid: '1'\ntype: carousel\nvideoUrl: https://cdn/x?oe=1\n---\n\n## Caption\nMy caption\n\n"
           "## Carousel Slides (2)\n\n### Slide 1\n\n> Alt text: Photo by me.\n\n\n## BIG TITLE\n**Tip** one\n\n"
           "### Slide 2\n\n> Alt text: Photo.\n\nI'm sorry, but I cannot extract any readable text from this image.\n\n"
           "## Comments (2)\n\n### @fan\n> nice\n\n### @me\n> thank you\n> both lines\n")
    meta, body = read(migrate("users/u/data/instagram/posts/a.md", old, {"u": "me"}))
    assert body == "My caption"
    assert meta["slides"] == ["BIG TITLE\nTip one"]
    assert meta["author_comments"] == ["thank you\nboth lines"]
    assert "videoUrl" not in meta and "fan" not in str(meta)


def test_instagram_reel_body_is_transcript_and_caption_moves_to_front_matter():
    old = ("---\nid: '1'\ntype: reel\ntranscript: true\nspeakers:\n  speaker_1: null\n---\n\n## Caption\nWatch this\n\n"
           "## Transcript\n\nspeaker_1: Hello\n")
    meta, body = read(migrate("users/u/data/instagram/posts/a.md", old, {"u": "me"}))
    assert body == "speaker_1: Hello" and meta["caption"] == "Watch this"


def test_linkedin_quote_article_and_author_comments():
    old = ("---\nid: '1'\narticle:\n  title: My book\n  link: https://b\n---\n\nPost text\n#tag\n\n"
           "### Quoting @Jane Smith:\n> Original words\n> Original Post: https://li/x\n\n"
           "### Shared Article: [My book](https://b)\n> b\n\n\n## Comments (2)\n\n"
           "### Bob (Long headline)\n> Congrats\n\n### Me (Coach) (Author)\n> Thanks Bob\n")
    meta, body = read(migrate("users/u/data/linkedin/posts/a.md", old))
    assert body == "Post text\n#tag"
    assert meta["quoted"] == {"author": "Jane Smith", "text": "Original words", "url": "https://li/x"}
    assert meta["author_comments"] == ["Thanks Bob"] and "Bob (Long" not in str(meta)


def test_article_markdown_becomes_plain_text_but_code_is_verbatim():
    md = ("# Title\n\n## **Why?**\n\n**First Law**Everything counts, see [the docs](https://d).\n\n"
          "| A | B |\n|---|---|\n| 1 | 2 |\n\n```js\nconst a = b * c_d_e;\n```\n- item\n* other\n")
    out = plain(md)
    assert out == ("Title\n\nWhy?\n\nFirst Law\nEverything counts, see the docs.\n\nA | B\n1 | 2\n\n"
                   "const a = b * c_d_e;\n\n- item\n- other")


def test_changed_words_are_refused():
    with pytest.raises(ValueError):
        content._same("one two", "one", "text")


def test_invalid_yaml_title_is_quoted_without_changing_its_value():
    old = "---\ntitle: Part 2 : Transfer\nurl: x\n---\n\n# Part 2 : Transfer\n\nBody **bold**\n"
    meta, body = read(migrate("users/u/data/website/a.md", old))
    assert meta["title"] == "Part 2 : Transfer" and body == "Body bold"
