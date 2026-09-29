"""Turn text files beneath a curated data root into cited, bounded source units."""

from __future__ import annotations

import hashlib
import json
import re
from dataclasses import dataclass
from datetime import UTC, date, datetime
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

import yaml

EXTENSIONS = {".md", ".markdown", ".txt", ".json", ".jsonl", ".yaml", ".yml", ".csv"}
UNIT_CHARS = 800  # Fits even the minimum --chunk-chars (1000), including labels.
SOURCE_FORMAT_VERSION = "markdown-passages-v2"


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
    )


def source_id(path: Path, root: Path) -> str:
    relative = path.relative_to(root).as_posix()
    base = re.sub(r"[^a-z0-9]+", "-", relative.lower()).strip("-")[:85].rstrip("-")
    return f"{base}-{hashlib.sha256(relative.encode()).hexdigest()[:10]}"


def split_text(text: str):
    """Split long values without dropping characters; no source unit exceeds 800 chars."""
    text = " ".join(text.split())
    while len(text) > UNIT_CHARS:
        end = text.rfind(" ", 0, UNIT_CHARS + 1)
        if end < UNIT_CHARS // 2:
            end = UNIT_CHARS
        yield text[:end]
        text = text[end:].lstrip()
    if text:
        yield text


def flatten(obj: Any, pointer: str = ""):
    if isinstance(obj, dict):
        for key, value in obj.items():
            part = str(key).replace("~", "~0").replace("/", "~1")
            yield from flatten(value, f"{pointer}/{part}")
    elif isinstance(obj, list):
        for n, value in enumerate(obj):
            yield from flatten(value, f"{pointer}/{n}")
    elif isinstance(obj, str) and len(obj.strip()) >= 12:
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
    root = root or path.parent
    raw = path.read_bytes()
    text = raw.decode("utf-8-sig")
    relative = path.relative_to(root)
    ident = source_id(path, root)
    metadata: dict = {}
    units: list[dict] = []
    heading = ""

    def add(value: str, locator: str, time: str = "", speaker: str = "") -> None:
        for part, excerpt in enumerate(split_text(value), 1):
            if len(excerpt) < 12:
                continue
            units.append(
                {
                    "id": f"{ident}:u{len(units) + 1:06d}",
                    "locator": locator + (f" part {part}" if part > 1 else ""),
                    "t": time,
                    "speaker_id": speaker,
                    "text": excerpt,
                }
            )

    if path.suffix.lower() in {".md", ".markdown", ".txt", ".csv"}:
        start = 0
        lines = text.splitlines()
        if (
            path.suffix.lower() in {".md", ".markdown"}
            and lines
            and lines[0].strip() == "---"
        ):
            try:
                end = lines.index("---", 1)
            except ValueError as exc:
                raise ValueError(f"Unclosed Markdown frontmatter: {path}") from exc
            metadata = yaml.safe_load("\n".join(lines[1:end])) or {}
            if not isinstance(metadata, dict):
                raise ValueError(f"Invalid Markdown frontmatter: {path}")
            start = end + 1
        passage: list[str] = []
        first = start + 1
        last = start + 1
        if metadata.get("transcript") is True:
            time = speaker = ""
            for n in range(start, len(lines)):
                value = lines[n].strip()
                turn = re.fullmatch(
                    r"### (\d{2,}:\d{2}:\d{2}) · Speaker (\S.*)", value
                )
                if turn:
                    if time:
                        if not passage:
                            raise ValueError(f"Empty transcript turn in {path}")
                        add(" ".join(passage), f"lines {first}-{last}", time, speaker)
                    time, speaker = turn.groups()
                    if any(int(v) >= 60 for v in time.split(":")[1:]):
                        raise ValueError(
                            f"Invalid transcript timestamp in {path}: {time}"
                        )
                    passage = []
                elif time and value:
                    if not passage:
                        first = n + 1
                    passage.append(value)
                    last = n + 1
            if not time or not passage:
                raise ValueError(f"Missing transcript turns or text in {path}")
            add(" ".join(passage), f"lines {first}-{last}", time, speaker)
        else:
            for n in range(start, len(lines)):
                value = lines[n].strip()
                if value.startswith(("### Quoting @", "## Comments")):
                    break  # Stop parsing at comments or quoted tweets; they belong to third parties.
                if (
                    not value
                    or value == "*"
                    or (
                        value.startswith("#")
                        and all(word.startswith("#") for word in value.split())
                    )
                ):
                    continue
                if not heading:
                    heading = value.lstrip("# ")[:110]
                if passage and len(" ".join(passage)) + len(value) + 1 > UNIT_CHARS:
                    add(" ".join(passage), f"lines {first}-{last}")
                    passage = []
                if not passage:
                    first = n + 1
                passage.append(value)
                last = n + 1
            if passage:
                add(" ".join(passage), f"lines {first}-{last}")
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
            if (
                ("channel_url" in obj and isinstance(obj.get("videos"), list))
                or (
                    isinstance(obj.get("tweets"), list)
                    and obj["tweets"]
                    and all(
                        isinstance(item, dict) and "file" in item
                        for item in obj["tweets"]
                    )
                )
                or (
                    isinstance(obj.get("posts"), list)
                    and obj["posts"]
                    and all(
                        isinstance(item, dict) and "file" in item
                        for item in obj["posts"]
                    )
                    and "profile"
                    not in obj  # pure post index; profile files stay (bio text)
                )
            ):
                return None  # Collection indexes point to source files; not independent testimony.
            metadata = obj
        if isinstance(obj, dict) and isinstance(obj.get("turns"), list):
            for n, turn in enumerate(obj["turns"]):
                if not isinstance(turn, dict) or not isinstance(turn.get("text"), str):
                    raise ValueError(f"Invalid transcript turn {n} in {path}")  # noqa: TRY004 - invalid source document
                time = str(turn.get("t", ""))
                if time and (
                    not re.fullmatch(r"\d{2,}:\d{2}:\d{2}", time)
                    or any(int(v) >= 60 for v in time.split(":")[1:])
                ):
                    raise ValueError(f"Invalid timestamp in {path}: {time}")
                add(
                    turn["text"], f"/turns/{n}/text", time, str(turn.get("speaker", ""))
                )
        elif (
            isinstance(obj, dict)
            and isinstance(obj.get("diarized_transcript"), dict)
            and isinstance(obj["diarized_transcript"].get("entries"), list)
        ):
            for n, entry in enumerate(obj["diarized_transcript"]["entries"]):
                if isinstance(entry, dict) and isinstance(entry.get("transcript"), str):
                    add(
                        entry["transcript"],
                        f"/diarized_transcript/entries/{n}/transcript",
                        str(entry.get("start_time_seconds", "")),
                        str(entry.get("speaker_id", "")),
                    )
        else:
            for pointer, value in flatten(obj):
                add(value, pointer)
    if not units:
        return None  # Metadata-only files (e.g. job IDs) contain no research text.
    sidecar = root / ".source-metadata.yaml"
    overrides = (
        (yaml.safe_load(sidecar.read_text(encoding="utf-8")) or {})
        if sidecar.exists()
        else {}
    )
    if not isinstance(overrides, dict):
        raise ValueError(f"Invalid source metadata map: {sidecar}")  # noqa: TRY004 - malformed document
    supplement = overrides.get(relative.as_posix(), {})
    if not isinstance(supplement, dict):
        raise ValueError(f"Invalid source metadata for {relative}")  # noqa: TRY004 - malformed document
    date_value = (
        supplement.get("date")
        or metadata.get("date")
        or metadata.get("published_at")
        or metadata.get("upload_date")
    )
    published_at = normalize_date(date_value)
    url = str(supplement.get("url") or metadata.get("url") or "")
    if url and urlparse(url).scheme not in ("http", "https"):
        raise ValueError(f"Invalid source URL in {relative}")
    author = str(supplement.get("author") or metadata.get("author") or "")
    if not author and url:
        if "linkedin.com/posts/" in url:
            author = url.split("/posts/", 1)[1].split("_", 1)[0]
        elif "x.com/" in url or "twitter.com/" in url:
            author = urlparse(url).path.strip("/").split("/", 1)[0]
    basis = (
        "sidecar"
        if supplement.get("date")
        else ("source" if published_at else "unknown")
    )
    external_id = str(supplement.get("id") or metadata.get("id") or "")
    title = str(
        supplement.get("title") or metadata.get("title") or heading or path.stem
    )
    metadata_hash = hashlib.sha256(
        json.dumps(
            {
                "date": published_at,
                "url": url,
                "author": author,
                "date_basis": basis,
                "external_id": external_id,
                "title": title,
            },
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
        published_at,
        url,
        author,
        basis,
        metadata_hash,
        external_id,
    )


def chunks(source: Source, max_chars: int) -> list[list[dict]]:
    if max_chars < 1000:
        raise ValueError("--chunk-chars must be at least 1000")
    result: list[list[dict]] = []
    current: list[dict] = []
    size = 0
    for unit in source.units:
        length = len(unit["text"]) + 150
        if length > max_chars:
            raise ValueError(f"Unit {unit['id']} is too long; increase --chunk-chars")
        if current and size + length > max_chars:
            result.append(current)
            current, size = [], 0
        current.append(unit)
        size += length
    if current:
        result.append(current)
    return result
