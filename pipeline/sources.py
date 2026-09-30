"""Immutable source text, original passages and bounded citation units."""

from __future__ import annotations

import hashlib
import json
import re
from dataclasses import dataclass, field
from datetime import UTC, date, datetime
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

import yaml

from .evidence import frontmatter

EXTENSIONS = {".md", ".markdown", ".txt", ".json", ".jsonl", ".yaml", ".yml", ".csv"}
UNIT_CHARS = 800
SOURCE_FORMAT_VERSION = "source-products-v4"
FORMATS = {"post", "document", "transcript", "interview", "qa", "role_play", "lesson"}
METADATA_KEYS = {
    "id",
    "url",
    "file",
    "date",
    "published_at",
    "upload_date",
    "author",
    "speakers",
    "format",
    "model",
    "audio_file",
    "job_id",
    "channel_url",
    "profilePicUrl",
    "profileImageUrl",
}


@dataclass
class Source:
    id: str
    title: str
    path: Path
    sha256: str
    category: str
    units: list[dict]
    date: str = ""
    url: str = ""
    author: str = ""
    date_basis: str = "unknown"
    metadata_hash: str = ""
    external_id: str = ""
    format: str = "document"
    speakers: dict[str, str] = field(default_factory=dict)
    passages: list[dict] = field(default_factory=list)
    original_text: str = ""
    content_hash: str = ""
    relative_path: str = ""
    audience: str = ""
    purpose: str = ""


def paths(root: Path) -> list[Path]:
    return sorted(
        p
        for p in root.rglob("*")
        if p.is_file()
        and not p.is_symlink()
        and p.suffix.lower() in EXTENSIONS
        and not any(
            part.startswith(".") or part == "__pycache__"
            for part in p.relative_to(root).parts
        )
        and p.resolve().is_relative_to(root.resolve())
    )


def source_id(path: Path, root: Path) -> str:
    relative = path.relative_to(root).as_posix()
    base = re.sub(r"[^a-z0-9]+", "-", relative.lower()).strip("-")[:85].rstrip("-")
    return f"{base}-{hashlib.sha256(relative.encode()).hexdigest()[:10]}"


def spans(text: str):
    """Bound original spans without losing words, short answers or punctuation."""
    start = end = None
    for match in re.finditer(r"\S+", text):
        if start is not None and match.end() - start > UNIT_CHARS:
            yield start, end
            start = end = None
        left = match.start()
        while match.end() - left > UNIT_CHARS:
            yield left, left + UNIT_CHARS
            left += UNIT_CHARS
        if start is None:
            start = left
        end = match.end()
    if start is not None:
        yield start, end


def split_text(text: str):
    for start, end in spans(text):
        yield " ".join(text[start:end].split())


def flatten(obj: Any, pointer: str = ""):
    if isinstance(obj, dict):
        for key, value in obj.items():
            if str(key) not in METADATA_KEYS:
                part = str(key).replace("~", "~0").replace("/", "~1")
                yield from flatten(value, f"{pointer}/{part}")
    elif isinstance(obj, list):
        for n, value in enumerate(obj):
            yield from flatten(value, f"{pointer}/{n}")
    elif (
        isinstance(obj, str)
        and len(obj.strip()) >= 12
        and not obj.startswith(("http://", "https://"))
    ):
        yield pointer or "/", obj


def normalize_date(value: Any) -> str:
    if not value:
        return ""
    text = str(value).strip()
    try:
        if re.fullmatch(r"\d{4}-\d{2}-\d{2}", text):
            return date.fromisoformat(text).isoformat()
        parsed = datetime.fromisoformat(text)
    except ValueError:
        try:
            parsed = datetime.strptime(text, "%a %b %d %H:%M:%S %z %Y")
        except ValueError as exc:
            raise ValueError(f"Invalid publication date: {text!r}") from exc
    if parsed.tzinfo is None:
        raise ValueError(f"Publication datetime requires a timezone: {text!r}")
    return parsed.astimezone(UTC).isoformat().replace("+00:00", "Z")


def read_source(path: Path, root: Path | None = None) -> Source | None:
    root = (root or path.parent).resolve()
    if path.is_symlink() or not path.resolve().is_relative_to(root):
        raise ValueError(f"Source escapes data root or is a symlink: {path}")
    path = path.resolve()
    raw = path.read_bytes()
    text = raw.decode("utf-8-sig")
    relative = path.relative_to(root)
    ident = source_id(path, root)
    metadata, units, passages = {}, [], []
    heading = ""
    transcript = False

    def add(value, locator, time="", speaker="", representation="authored_text"):
        if not value.strip():
            return
        pid = f"{ident}:p{len(passages) + 1:06d}"
        passages.append(
            {
                "id": pid,
                "text": value,
                "locator": locator,
                "t": time,
                "speaker_id": speaker,
                "representation": representation,
            }
        )
        for n, (start, end) in enumerate(spans(value), 1):
            units.append(
                {
                    "id": f"{ident}:u{len(units) + 1:06d}",
                    "passage_id": pid,
                    "locator": locator + (f" part {n}" if n > 1 else ""),
                    "t": time,
                    "speaker_id": speaker,
                    "representation": representation,
                    "text": " ".join(value[start:end].split()),
                    "raw_text": value[start:end],
                    "start": start,
                    "end": end,
                }
            )

    if path.suffix.lower() in {".md", ".markdown", ".txt", ".csv"}:
        lines = text.splitlines()
        start = 0
        if (
            path.suffix.lower() in {".md", ".markdown"}
            and lines
            and lines[0].strip() == "---"
        ):
            metadata, start = frontmatter(text)
        transcript = metadata.get("transcript") is True
        representation = "spoken_turn" if transcript else "authored_text"
        time = speaker = ""
        first = last = None

        def flush():
            if first is not None:
                add(
                    "\n".join(lines[first : last + 1]),
                    f"lines {first + 1}-{last + 1}",
                    time,
                    speaker,
                    representation,
                )

        for n in range(start, len(lines)):
            value = lines[n].strip()
            if value.startswith(("### Quoting @", "## Comments")):
                break  # Original text is retained; third-party sections are not extraction units.
            turn = (
                re.fullmatch(r"### (\d{2,}:\d{2}:\d{2}) · Speaker (\S.*)", value)
                if transcript
                else None
            )
            if turn or (transcript and value in {"## Caption", "## Transcript"}):
                flush()
                first = last = None
                if turn:
                    time, speaker = turn.groups()
                    if any(int(v) >= 60 for v in time.split(":")[1:]):
                        raise ValueError(f"Invalid transcript timestamp: {time}")
                    representation = "spoken_turn"
                else:
                    time = speaker = ""
                    representation = (
                        "authored_text" if value == "## Caption" else "spoken_turn"
                    )
                continue
            if not value or value == "*" or value == "> [No spoken dialogue detected]":
                continue
            if value.startswith("#") and all(
                word.startswith("#") for word in value.split()
            ):
                continue
            if not heading:
                heading = value.lstrip("# ")[:110]
            if transcript and not time and value.startswith("#"):
                continue
            if first is None:
                first = n
            last = n
        flush()
    elif path.suffix.lower() == ".jsonl":
        for n, line in enumerate(text.splitlines(), 1):
            if line.strip():
                for pointer, value in flatten(json.loads(line)):
                    add(value, f"line {n}{pointer}")
    else:
        obj = (
            json.loads(text) if path.suffix.lower() == ".json" else yaml.safe_load(text)
        )
        if isinstance(obj, dict):
            metadata = obj
            if "channel_url" in obj and isinstance(obj.get("videos"), list):
                return None
            for name in ("posts", "tweets"):
                if (
                    name in obj
                    and isinstance(obj[name], list)
                    and all(isinstance(v, dict) and "file" in v for v in obj[name])
                    and "profile" not in obj
                ):
                    return None
            profile = obj.get("profile")
            if isinstance(profile, dict):
                metadata = {
                    **obj,
                    "author": obj.get("author")
                    or profile.get("publicIdentifier")
                    or profile.get("userName")
                    or profile.get("username")
                    or "",
                }
        if isinstance(obj, dict) and isinstance(obj.get("turns"), list):
            transcript = True
            for n, turn in enumerate(obj["turns"]):
                if not isinstance(turn, dict) or not isinstance(turn.get("text"), str):
                    raise ValueError(f"Invalid transcript turn {n} in {path}")  # noqa: TRY004 - invalid document
                time = str(turn.get("t", ""))
                if time and (
                    not re.fullmatch(r"\d{2,}:\d{2}:\d{2}", time)
                    or any(int(v) >= 60 for v in time.split(":")[1:])
                ):
                    raise ValueError(f"Invalid timestamp in {path}: {time}")
                add(
                    turn["text"],
                    f"/turns/{n}/text",
                    time,
                    str(turn.get("speaker", "")),
                    "spoken_turn",
                )
        elif isinstance(obj, dict) and isinstance(obj.get("diarized_transcript"), dict):
            transcript = True
            for n, entry in enumerate(obj["diarized_transcript"].get("entries", [])):
                if not isinstance(entry, dict) or not isinstance(
                    entry.get("transcript"), str
                ):
                    raise ValueError(f"Invalid diarized entry {n} in {path}")  # noqa: TRY004 - invalid document
                add(
                    entry["transcript"],
                    f"/diarized_transcript/entries/{n}/transcript",
                    str(entry.get("start_time_seconds", "")),
                    str(entry.get("speaker_id", "")),
                    "spoken_turn",
                )
        else:
            content = (
                obj.get("profile")
                if isinstance(obj, dict) and isinstance(obj.get("profile"), dict)
                else obj
            )
            for pointer, value in flatten(content):
                add(value, ("/profile" if content is not obj else "") + pointer)
    if not units:
        return None
    sidecar = root / ".source-metadata.yaml"
    overrides = (
        yaml.safe_load(sidecar.read_text(encoding="utf-8")) or {}
        if sidecar.exists()
        else {}
    )
    if not isinstance(overrides, dict):
        raise ValueError(f"Invalid source metadata map: {sidecar}")  # noqa: TRY004 - invalid document
    supplement = overrides.get(relative.as_posix(), {})
    if not isinstance(supplement, dict):
        raise ValueError(f"Invalid source metadata for {relative}")  # noqa: TRY004 - invalid document
    merged = {**metadata, **supplement}
    date_value = (
        merged.get("date") or merged.get("published_at") or merged.get("upload_date")
    )
    published = normalize_date(date_value)
    url = str(merged.get("url") or "")
    parsed = urlparse(url)
    if url and (parsed.scheme not in {"https", "http"} or not parsed.hostname):
        raise ValueError(f"Invalid source URL in {relative}")
    author = str(merged.get("author") or "")
    if not author:
        host = (parsed.hostname or "").lower().removeprefix("www.")
        if host == "linkedin.com" and parsed.path.startswith("/posts/"):
            author = parsed.path.split("/posts/", 1)[1].split("_", 1)[0]
        elif host in {"x.com", "twitter.com"}:
            author = parsed.path.strip("/").split("/", 1)[0]
    speakers = merged.get("speakers", {})
    if not isinstance(speakers, dict) or not all(
        isinstance(k, str) and isinstance(v, str) and k and v.strip()
        for k, v in speakers.items()
    ):
        raise ValueError(f"Invalid explicit speaker mapping in {relative}")
    default_format = (
        "transcript"
        if transcript
        else "post"
        if relative.parts[0] in {"linkedin", "twitter", "instagram"}
        else "document"
    )
    source_format = merged.get("format", default_format)
    if not isinstance(source_format, str) or source_format not in FORMATS:
        raise ValueError(f"Invalid source format: {source_format!r}")
    title = str(merged.get("title") or heading or path.stem)
    basis = (
        "sidecar"
        if any(supplement.get(k) for k in ("date", "published_at", "upload_date"))
        else "source"
        if published
        else "unknown"
    )
    external_id = str(merged.get("id") or "")
    audience, purpose = (
        str(merged.get("audience") or ""),
        str(merged.get("purpose") or ""),
    )
    metadata_hash = hashlib.sha256(
        json.dumps(
            [
                published,
                url,
                author,
                basis,
                external_id,
                title,
                source_format,
                speakers,
                audience,
                purpose,
            ],
            sort_keys=True,
        ).encode()
    ).hexdigest()
    return Source(
        ident,
        title,
        path,
        hashlib.sha256(raw).hexdigest(),
        relative.parts[0] if len(relative.parts) > 1 else "uncategorized",
        units,
        published,
        url,
        author,
        basis,
        metadata_hash,
        external_id,
        source_format,
        speakers,
        passages,
        text,
        hashlib.sha256(" ".join(u["text"] for u in units).encode()).hexdigest(),
        relative.as_posix(),
        audience,
        purpose,
    )


def chunks(source: Source, max_chars: int) -> list[list[dict]]:
    """Bound citation-unit windows; original passages remain stored independently."""
    if max_chars < 1000:
        raise ValueError("--chunk-chars must be at least 1000")
    result, current, size = [], [], 0
    for unit in source.units:
        length = len(unit["raw_text"]) + 150
        if current and size + length > max_chars:
            result.append(current)
            current, size = [], 0
        current.append(unit)
        size += length
    if current:
        result.append(current)
    return result
