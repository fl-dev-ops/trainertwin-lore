"""One layout for every collected file: YAML front matter, then the content and nothing else.

    ---
    id: ...
    title: ...                 # every label/metadata lives here
    speakers: {speaker_1: null}
    author_comments: [...]     # only the author's own comments
    ---

    speaker_1: spoken turn ...  # transcripts: `speaker_N: ` starts a turn; other lines continue it

No Markdown in the body: no `# Title`, `## Transcript`, `## Caption`, `### @user` sections.

`migrate(path, text)` converts the older Markdown layouts. It refuses (ValueError) unless every
kept word is unchanged; only listed noise is dropped (headings, alt text, OCR refusals, other
people's comments, commenter headlines, duplicated article/document links, expired CDN URLs).
"""
from __future__ import annotations

import json
import re
import unicodedata

import yaml

FRONT = re.compile(r"\A\ufeff?---\n(.*?\n)?---\n", re.DOTALL)
SPEAKER_LINE = re.compile(r"^(speaker_[1-9]\d*): ?(.*)$")
NO_SPEECH = "> [No spoken dialogue detected]"
# Vision-model answers that say there is no text are not content.
OCR_REFUSAL = re.compile(
    r"\A\s*(?:I'?m sorry|I am sorry|I cannot|I can't|There is no (?:readable |discernible |visible )?text"
    r"|There is no discernible|The image is very blurry|No (?:readable |visible )?text)", re.IGNORECASE)


def skeleton(s: str) -> str:
    return unicodedata.normalize("NFC", "".join(c for c in s if unicodedata.category(c)[0] in "LMN"))


def is_ocr_refusal(text: str) -> bool:
    return bool(OCR_REFUSAL.match(text or "")) and "text" in text.lower()


# ---------- read / write ----------

def split(text: str) -> tuple[str, str]:
    """-> (front-matter YAML text, body). A file without front matter is all body."""
    m = FRONT.match(text)
    return (m.group(1) or "", text[m.end():]) if m else ("", text)


def load_meta(fm: str) -> dict:
    try:
        meta = yaml.safe_load(fm) or {}
    except yaml.YAMLError:
        raise ValueError("front matter is not valid YAML") from None
    if not isinstance(meta, dict):
        raise TypeError("front matter must be a mapping")
    return meta


def read(text: str) -> tuple[dict, str]:
    fm, body = split(text)
    return load_meta(fm), body.strip("\n")


class _Dumper(yaml.SafeDumper):
    pass


def _str(dumper, value):
    # Multi-line text reads as a block (`|`); PyYAML falls back to quoting when a block cannot round-trip.
    style = "|" if "\n" in value else None
    return dumper.represent_scalar("tag:yaml.org,2002:str", value, style=style)


_Dumper.add_representer(str, _str)


def dump_yaml(meta: dict) -> str:
    return yaml.dump(meta, Dumper=_Dumper, sort_keys=False, allow_unicode=True, width=10**6)


def render(meta: dict, body: str = "") -> str:
    body = body.strip("\n")
    return "---\n" + dump_yaml(meta) + "---\n" + (f"\n{body}\n" if body else "")


def read_turns(body: str, labels) -> list[tuple[str, str]]:
    """Transcript turns. Text before the first declared speaker line is an error, never dropped."""
    labels, turns, current = set(labels), [], None
    for line in body.splitlines():
        m = SPEAKER_LINE.match(line)
        if m and m.group(1) in labels:
            current = [m.group(1), [m.group(2)]]
            turns.append(current)
        elif current is not None:
            current[1].append(line)
        elif line.strip():
            raise ValueError("text before the first speaker line")
    return [(label, "\n".join(lines).strip("\n")) for label, lines in turns]


def render_turns(turns) -> str:
    return "\n\n".join(f"{label}: {text}" for label, text in turns)


# ---------- front matter edits that keep existing lines byte-for-byte ----------

def _repair(fm: str) -> str:
    """Some exporters left a colon-bearing title unquoted; quote it (the value is unchanged)."""
    try:
        load_meta(fm)
        return fm
    except ValueError:
        fixed = re.sub(r"^(title|description): ([^'\"\n].*)$",
                       lambda m: f"{m[1]}: " + json.dumps(m[2], ensure_ascii=False), fm, flags=re.MULTILINE)
        load_meta(fm := fixed)
        return fm


def _drop_key(fm: str, key: str) -> str:
    return re.sub(rf"^{key}:.*\n(?:[ \t]+.*\n|-.*\n)*", "", fm, flags=re.MULTILINE)


def _with(fm: str, extra: dict, drop=()) -> str:
    fm = _repair(fm)
    for key in list(drop) + list(extra):
        fm = _drop_key(fm, key)
    fm += dump_yaml(extra) if extra else ""
    meta = load_meta(fm)
    if any(meta.get(k) != v for k, v in extra.items()) or any(k in meta for k in drop if k not in extra):
        raise ValueError("front matter edit did not round-trip")
    return fm


def _out(fm: str, body: str) -> str:
    body = body.strip("\n")
    return "---\n" + fm + "---\n" + (f"\n{body}\n" if body else "")


def _same(before: str, after: str, what: str):
    if skeleton(before) != skeleton(after):
        raise ValueError(f"{what} changed")


# ---------- old layouts -> new ----------

INSTAGRAM_SECTION = re.compile(r"^## (Caption|Transcript|Carousel Slides \(\d+\)|Image Text|Comments \(\d+\))$")


def _sections(body: str, heading_line=re.compile(r"^## ")) -> list[tuple[str | None, str]]:
    """Split on section headings: [(heading or None, text)]."""
    parts, heading, lines = [], None, []
    for line in body.splitlines():
        if heading_line.match(line):
            parts.append((heading, "\n".join(lines)))
            heading, lines = line[3:].strip(), []
        else:
            lines.append(line)
    parts.append((heading, "\n".join(lines)))
    return [(h, t) for h, t in parts if h is not None or t.strip()]


def _quoted(block: str) -> str:
    """'> ' quoted lines back to text."""
    return "\n".join(re.sub(r"^> ?", "", l) for l in block.strip("\n").splitlines()).strip()


def _transcript_body(text: str) -> str:
    text = text.strip("\n")
    return "" if text == NO_SPEECH else text


def migrate_transcript(text: str) -> str:
    fm, body = split(text)
    meta = load_meta(_repair(fm))
    parts = _sections(body)
    heads = [h for h, _ in parts]
    if "Transcript" not in heads or heads.count("Transcript") != 1:
        raise ValueError("expected one Transcript section")
    for h, t in parts:
        if h is None:  # only the '# Title' line may precede the transcript
            for line in t.splitlines():
                if line.strip() and not (line.startswith("# ") and skeleton(line[2:]) in skeleton(str(meta.get("title", "")))):
                    raise ValueError("unexpected text before the transcript")
        elif h != "Transcript":
            raise ValueError(f"unexpected section {h}")
    new = _transcript_body(dict(parts)["Transcript"])
    labels = [k for k in (meta.get("speakers") or {}) if SPEAKER_LINE.match(f"{k}: ")]
    if new and not read_turns(new, labels):
        raise ValueError("transcript has no speaker turns")
    _same(dict(parts)["Transcript"].replace(NO_SPEECH, ""), new, "transcript")
    return _out(_repair(fm), new)


def migrate_instagram(text: str, owner: str) -> str:
    fm, body = split(text)
    meta = load_meta(_repair(fm))
    # Only the exporter's own headings split sections: OCR text may contain '## ' lines of its own.
    parts = _sections(body, INSTAGRAM_SECTION)
    if any(h is None and t.strip() for h, t in parts):
        raise ValueError("text outside a section")
    found = {}
    for h, t in parts:
        key = re.sub(r" \(\d+\)$", "", h)
        if key in found:
            raise ValueError(f"repeated section {h}")
        found[key] = t
    caption = found.get("Caption", "").strip("\n").strip()
    extra, drop = {}, ["videoUrl"]  # signed CDN links expire: no lasting value
    if "Image Text" in found:
        image = "\n".join(l for l in found["Image Text"].splitlines() if not l.startswith("> Alt text:")).strip()
        if image and not is_ocr_refusal(image):
            extra["image_text"] = _plain_checked(image, "image text")
    if "Carousel Slides" in found:
        slides = []
        for chunk in re.split(r"^### Slide \d+\n", found["Carousel Slides"], flags=re.MULTILINE)[1:]:
            lines = [l for l in chunk.splitlines() if not l.startswith("> Alt text:")]
            slide = "\n".join(lines).strip()
            if slide and not is_ocr_refusal(slide):
                slides.append(_plain_checked(slide, "slide text"))
        if slides:
            extra["slides"] = slides
    if "Comments" in found:
        mine = []
        for chunk in re.split(r"^### @", found["Comments"], flags=re.MULTILINE)[1:]:
            author, _, rest = chunk.partition("\n")
            if author.strip() == owner:
                mine.append(_quoted(rest))
        if mine:
            extra["author_comments"] = mine
    if meta.get("transcript") is True and "Transcript" in found:
        new_body = _transcript_body(found["Transcript"])
        _same(found["Transcript"].replace(NO_SPEECH, ""), new_body, "transcript")
        if caption:
            extra["caption"] = caption
    elif "Transcript" in found:
        raise ValueError("transcript section without transcript: true")
    else:
        new_body = caption
    out = _out(_with(fm, extra, drop), new_body)
    meta2, body2 = read(out)
    kept = (meta2.get("caption", "") + body2 + meta2.get("image_text", "") + "".join(meta2.get("slides", []))
            + "".join(meta2.get("author_comments", [])))
    if skeleton(caption) not in skeleton(kept):
        raise ValueError("caption changed")
    return out


def migrate_linkedin(text: str) -> str:
    fm, body = split(text)
    meta = load_meta(_repair(fm))
    comments = ""
    m = re.search(r"\n\n## Comments \(\d+\)\n", body)
    if m:
        body, comments = body[:m.start()], body[m.end():]
    blocks = re.split(r"\n\n(?=### (?:Quoting @.+:|Shared Article: |Shared Document: ))", body)
    content, extra = blocks[0].strip("\n"), {}
    for block in blocks[1:]:
        head, _, rest = block.partition("\n")
        if head.startswith("### Quoting @"):
            lines, quoted = _quoted(rest).splitlines(), {"author": head[len("### Quoting @"):-1]}
            while lines and re.match(r"^(\[(Article|Document): .*\]\(.*\)|Original Post: \S+)$", lines[-1]):
                line = lines.pop()
                if line.startswith("Original Post: "):
                    quoted["url"] = line[len("Original Post: "):]
                else:
                    kind, title, link = re.match(r"^\[(Article|Document): (.*)\]\((.*)\)$", line).groups()
                    quoted[kind.lower()] = {"title": title, "link": link} if link else {"title": title}
            quoted["text"] = "\n".join(lines).strip()
            if quoted["text"] == "[No text content]":
                quoted["text"] = ""
            extra["quoted"] = {k: quoted[k] for k in ("author", "text", "url", "article", "document") if quoted.get(k)}
        elif head.startswith("### Shared Article: "):
            if not meta.get("article", {}).get("title") or skeleton(meta["article"]["title"]) not in skeleton(block):
                raise ValueError("shared article not in front matter")
        elif head.startswith("### Shared Document: "):
            if not meta.get("document", {}).get("title") or skeleton(meta["document"]["title"]) not in skeleton(block):
                raise ValueError("shared document not in front matter")
    mine = []
    for chunk in re.split(r"^### ", comments, flags=re.MULTILINE)[1:]:
        head, _, rest = chunk.partition("\n")
        if head.rstrip().endswith("(Author)"):
            text_ = _quoted(rest)
            if text_ and text_ != "[Empty comment]":
                mine.append(text_)
    if mine:
        extra["author_comments"] = mine
    return _out(_with(fm, extra), content)


TAGS = re.compile(r"</?(?:sup|sub|br)\b[^>]*>")  # inline typography; other HTML in articles is code
LINK = re.compile(r"(!?)\[([^\]]*)\]\(([^)\s]*)\)")  # link text may span lines (Medium link cards)
MARKDOWN = re.compile(r"^#{1,6} |^```|^\s*\|.*\||\]\(|^> ", re.MULTILINE)


def _segments(md: str):
    """[(is_code, text)]: fenced code blocks (fence lines dropped) and the prose between them."""
    out, code, lines = [], False, []
    for line in md.splitlines():
        if line.strip().startswith("```"):
            out.append((code, "\n".join(lines)))
            code, lines = not code, []
        else:
            lines.append(line)
    out.append((code, "\n".join(lines)))
    return out


def _prose(text: str) -> str:
    text = LINK.sub(lambda m: m.group(2), text)
    text = re.sub(r"\\+(?=\n|$)", "", text, flags=re.MULTILINE)  # trailing backslashes = hard line break
    out = []
    for line in text.splitlines():
        if (re.fullmatch(r"\s*\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)*\|?\s*", line)
                or re.fullmatch(r"\s*(-{3,}|\*{3,}|_{3,})\s*", line)):
            continue  # table separator or horizontal rule
        s = re.sub(r"^#{1,6}\s+", "", line)
        s = re.sub(r"^>\s?", "", s)
        s = re.sub(r"^(\s*)[*+] (?=\S)", r"\1- ", s)  # one bullet style
        s = re.sub(r"^(\*\*|__)([^*_\n]+?)\1(?=\w)", r"\2\n", s)  # '**First Law**Everything' -> two lines
        s = re.sub(r"(\*\*|__)(?=\S)(.+?)(?<=\S)\1", r"\2", s)
        s = re.sub(r"(?<![\w*\\])\*(?=[^\s*])(.+?)(?<=[^\s*])\*(?![\w*])", r"\1", s)
        s = re.sub(r"(?<![\w\\])_(?=\S)(.+?)(?<=\S)_(?!\w)", r"\1", s)
        s = re.sub(r"`([^`\n]+)`", r"\1", s)
        s = TAGS.sub("", s)
        s = re.sub(r"\\([\\`*_{}\[\]()#+\-.!|>])", r"\1", s)
        if s.lstrip().startswith("|"):
            s = " | ".join(c.strip() for c in s.strip().strip("|").split("|"))
        out.append(s.rstrip())
    return "\n".join(out)


def plain(md: str) -> str:
    """Markdown -> plain text. Code keeps its lines verbatim (fences dropped); links keep their text."""
    parts = [part.strip("\n") if code else re.sub(r"\n{3,}", "\n\n", _prose(part)).strip("\n")
             for code, part in _segments(md)]
    return "\n\n".join(part for part in parts if part.strip())  # a blank line around each code block


def _words_without_markup(md: str) -> str:
    """What plain() must keep: every word except fence tags, link/image URLs and inline tags."""
    return "\n".join(part if code else TAGS.sub("", LINK.sub(lambda m: m.group(2), part))
                     for code, part in _segments(md))


def _plain_checked(md: str, what: str) -> str:
    new = plain(md)
    _same(_words_without_markup(md), new, what)
    return new


def migrate_article(text: str) -> str:
    fm, body = split(text)
    meta = load_meta(_repair(fm))
    title = str(meta.get("title", ""))
    lines = body.strip("\n").splitlines()
    if lines and lines[0].startswith("# ") and skeleton(lines[0][2:]) and skeleton(lines[0][2:]) in skeleton(title):
        lines = lines[1:]  # the title is already in the front matter
    source = "\n".join(lines)
    new = plain(source)
    _same(_words_without_markup(source), new, "article text")
    if MARKDOWN.search(new):  # would be converted again on a rerun
        raise ValueError("Markdown left after conversion")
    return _out(_repair(fm), new)


def migrate(path: str, text: str, owners: dict[str, str] | None = None) -> str:
    """Dispatch by location; files that are not collected content stay unchanged."""
    p = "/" + path.replace("\\", "/")
    if not FRONT.match(text):
        return text  # e.g. docs and notes without front matter
    if "/youtube/video/" in p or "/loom/videos/" in p:
        out = migrate_transcript(text) if "## Transcript" in text else text
    elif "/instagram/posts/" in p:
        if not re.search(r"^## (Caption|Transcript|Comments|Image Text|Carousel)", text, re.MULTILINE):
            return text
        user = p.split("/users/", 1)[-1].split("/")[0] if "/users/" in p else ""
        owner = (owners or {}).get(user)
        if not owner:
            raise ValueError("unknown Instagram account owner")
        out = migrate_instagram(text, owner)
    elif "/linkedin/posts/" in p:
        out = migrate_linkedin(text)
    elif "/medium/posts/" in p or "/website/" in p:
        out = migrate_article(text) if MARKDOWN.search(split(text)[1]) else text
    else:
        return text
    if out != text:
        read(out)  # front matter must load
        if migrate(path, out, owners) != out:
            raise ValueError("migration is not idempotent")
    return out


def owners(users_dir) -> dict[str, str]:
    """Instagram account handle per user, from the collected profile YAML."""
    from pathlib import Path
    found = {}
    for path in Path(users_dir).glob("*/data/instagram/*.yaml"):
        profile = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        handle = (profile.get("profile") or profile).get("username")
        if handle:
            found[path.parts[-4]] = handle
    return found


def main(argv=None):
    """python -m social.content users [--write]: dry run by default; refusals block nothing else."""
    import argparse
    from pathlib import Path
    parser = argparse.ArgumentParser(description=main.__doc__)
    parser.add_argument("users", type=Path)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args(argv)
    accounts, counts, refused = owners(args.users), {}, []
    for path in sorted(args.users.rglob("*.md")):
        if "/data/" not in path.as_posix():
            continue
        text = path.read_text(encoding="utf-8")
        kind = path.relative_to(args.users).parts[2]
        try:
            new = migrate(path.as_posix(), text, accounts)
        except ValueError as exc:
            refused.append(f"{path}: {exc}")
            continue
        state = "changed" if new != text else "unchanged"
        counts[(kind, state)] = counts.get((kind, state), 0) + 1
        if args.write and new != text:
            path.write_text(new, encoding="utf-8")
    for line in refused:
        print("REFUSED", line)
    for (kind, state), n in sorted(counts.items()):
        print(f"{kind:10} {state:9} {n}")
    print(f"{'written' if args.write else 'dry run'}; {len(refused)} refused")
    if refused:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
