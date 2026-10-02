"""Index a captured file. The file's own list is the count; otherwise long files use sections."""

from __future__ import annotations

import hashlib
import re
from pathlib import Path

from .storage import atomic, js, load_json, run_bounded

def source_id(path: Path, root: Path) -> str:
    relative = path.relative_to(root).as_posix()
    base = re.sub(r"[^a-z0-9]+", "-", relative.lower()).strip("-")[:85].rstrip("-")
    return f"{base}-{hashlib.sha256(relative.encode()).hexdigest()[:10]}"


FACETS = ("topic", "situation", "activity")


def _to_seconds(ts: str) -> int:
    """Parse M:SS, MM:SS, H:MM:SS, or HH:MM:SS to integer seconds."""
    parts = ts.strip().split(":")
    if len(parts) == 3:
        return int(parts[0]) * 3600 + int(parts[1]) * 60 + int(parts[2])
    if len(parts) == 2:
        return int(parts[0]) * 60 + int(parts[1])
    return 0


def _is_channel_manifest(path: Path, text: str) -> bool:
    """Channel-level YAML manifests duplicate individual video files — skip."""
    if path.suffix.lower() not in (".yaml", ".yml"):
        return False
    head = text[:500]
    return "total_videos:" in head or ("videos:" in head and "channel_url:" in head)


def list_ranges(lines: list[str]) -> list[tuple[int, int]]:
    """Extract deterministic list-item boundaries from timecodes or numbered markers."""
    tc_pat = re.compile(r"^\s*(\d{1,2}:\d{2}(?::\d{2})?)\s+[-\u2013\u2014]?\s*\S")
    timecodes = [(i, m.group(1)) for i, line in enumerate(lines, 1) if (m := tc_pat.match(line))]

    num_pat = re.compile(r"^\s*(\d{1,2})[.)]\s+\S")
    numbered = [i for i, line in enumerate(lines, 1) if num_pat.match(line)]

    if len(timecodes) >= 2:
        ranges = _tc_to_ranges(lines, timecodes)
    elif len(numbered) >= 2:
        ranges = _num_to_ranges(lines, numbered)
    else:
        return []

    if any(end - start > 100 for start, end in ranges):
        return []
    return ranges


def _tc_to_ranges(lines: list[str], timecodes: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """Map description timecodes to transcript turn positions when available."""
    turn_pat = re.compile(r"^### (\d{2}:\d{2}:\d{2})")
    turns = [(i, _to_seconds(m.group(1))) for i, line in enumerate(lines, 1) if (m := turn_pat.match(line))]

    if not turns:
        # No transcript — use timecode lines directly as boundaries
        positions = [tc[0] for tc in timecodes]
        return [(positions[i], positions[i + 1] - 1 if i + 1 < len(positions) else len(lines))
                for i in range(len(positions))]

    # Map each chapter timecode to the nearest transcript turn (within 60s)
    mapped = []
    used: set[int] = set()
    for _, ts_str in timecodes:
        target = _to_seconds(ts_str)
        candidates = [(ln, abs(s - target)) for ln, s in turns if ln not in used]
        if not candidates:
            continue
        best_line, distance = min(candidates, key=lambda x: x[1])
        if distance <= 60:
            used.add(best_line)
            mapped.append(best_line)

    if len(mapped) < 2:
        return []
    mapped.sort()
    return [(mapped[i], mapped[i + 1] - 1 if i + 1 < len(mapped) else len(lines))
            for i in range(len(mapped))]


def _num_to_ranges(lines: list[str], positions: list[int]) -> list[tuple[int, int]]:
    """Create ranges from numbered list items."""
    # Find where comments start (cap the last item there)
    comment_start = len(lines)
    for i, line in enumerate(lines, 1):
        if line.strip().startswith("## Comments"):
            comment_start = i - 1
            break
    ranges = []
    for i, pos in enumerate(positions):
        end = positions[i + 1] - 1 if i + 1 < len(positions) else comment_start
        ranges.append((pos, end))
    return ranges

PROMPT = """Index this file. Do not summarize it and do not copy it.

A list the file already wrote is the count. A list is only one of these:
- chapters, timecodes, or a "what you'll learn" section
- a line that starts a point with "1." or "2." or "1)"
- a timestamp followed by a title, with or without a dash, such as "0:00 Introduction"
- words that enumerate cases, such as "two ways" followed by separate cases

These are not lists: 12th, 1st, 2nd, 3rd, a year, a price, a count such as 100k, or a number in the middle of a sentence. "after 12th" is not item 1 and item 2.

If a list exists, return one item per listed point. Use the listed name as the title. Do not add the unnumbered sentences around it. Do not include comments.
If a listed point never appears in the body, omit it.

If no list exists and section ranges are given, return exactly one item per range. Do not merge those ranges into one item. Do not add items outside them.
If no list exists and no sections are given, return one item for the whole text. The only exception is an enumerated case list, as above.

Ignore hashtags, greetings, subscribe lines, and comments.
A span uses the line numbers at the left, contains the point, and is no wider than 100 lines.
The title names the point taught or claimed in that span. Never use "section", "part", "lines", a timestamp alone, or a range label as the title.
Set basis to "list", "sections", or "whole".

Each item must have at least one tag. Each tag has a facet and a label.
Facets:
- "topic": the specific subject discussed (e.g. "cold calling", "off-plan vs secondary", "closures"). Not the broad domain everyone shares.
- "situation": the trigger, objection, or circumstance being addressed (e.g. "client wants to wait for crash", "candidate gives up on problem", "lead stops responding"). Only when present in the text.
- "activity": the format or task (e.g. "mock interview", "sales coaching", "listing presentation"). Only when clearly identifiable.

Do not use the person's entire profession as a topic. "Dubai Real Estate" or "JavaScript" alone is too broad. Name the specific subject within that domain.

Done means that count is returned, nothing more."""

SCHEMA = {
    "type": "object",
    "additionalProperties": False,
    "properties": {
        "basis": {"type": "string"},
        "items": {
            "type": "array",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "properties": {
                    "title": {"type": "string"},
                    "tags": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "additionalProperties": False,
                            "properties": {
                                "facet": {"type": "string"},
                                "label": {"type": "string"},
                            },
                            "required": ["facet", "label"],
                        },
                    },
                    "span": {
                        "type": "object",
                        "additionalProperties": False,
                        "properties": {
                            "start_line": {"type": "integer"},
                            "end_line": {"type": "integer"},
                        },
                        "required": ["start_line", "end_line"],
                    },
                },
                "required": ["title", "tags", "span"],
            },
        },
    },
    "required": ["basis", "items"],
}


def has_list(text: str) -> bool:
    if re.search(r"(?im)^(what you.?ll learn|chapters|timecodes)\b", text):
        return True
    if re.search(r"(?m)^\s*\d{1,2}:\d{2}(?::\d{2})?\s+-\s+\S", text):
        return True
    if re.search(r"(?m)^\s*\d{1,2}:\d{2}(?::\d{2})?\s+[A-Za-z]", text):
        return True
    return bool(re.search(r"(?m)^\s*\d{1,2}[.)]\s+\S", text))


def sections(lines: list[str]) -> list[tuple[int, int]]:
    turns = [i for i, line in enumerate(lines, 1) if re.match(r"### \d{2}:\d{2}:\d{2}", line)]
    if len(turns) < 8:
        return []
    groups = [turns[i : i + 6] for i in range(0, len(turns), 6)]
    ranges = []
    for n, group in enumerate(groups):
        end = groups[n + 1][0] - 1 if n + 1 < len(groups) else len(lines)
        ranges.append((group[0], end))
    return ranges


def plan(text: str) -> tuple[str, str]:
    lines = text.splitlines()
    if has_list(text):
        ranges = list_ranges(lines)
        if ranges:
            listed = "\n".join(f"- lines {a}-{b}" for a, b in ranges)
            return "list", "\n\nA list was found and these ranges contain its points. Return exactly one item per range. Use the listed name as the title if present.\n" + listed
        return "list", "\n\nA list is present. Use only that list."
    ranges = [] if has_list(text) else sections(lines)
    if ranges:
        listed = "\n".join(f"- lines {a}-{b}" for a, b in ranges)
        return "sections", "\n\nNo list was found. These ranges are locations, not titles. Return exactly one item per range. Name what that range teaches.\n" + listed
    return "whole", "\n\nNo list and no sections were found. Return one item, unless the text itself enumerates cases such as two ways."


def _bad_title(title: str) -> bool:
    return bool(re.fullmatch(r"(?i)(section|part|lines?)( \d+)?", title.strip()))


def accept(lines: list[str], raw: dict) -> list[dict]:
    kept = []
    for item in raw.get("items") or []:
        title = " ".join(str(item.get("title") or "").split())
        span = item.get("span") or {}
        try:
            start, end = int(span["start_line"]), int(span["end_line"])
        except (KeyError, TypeError, ValueError):
            continue
        if not title or _bad_title(title) or not (1 <= start <= end <= len(lines)) or end - start > 100:
            continue
        quote = " ".join(line.strip() for line in lines[start - 1 : end] if line.strip() and not line.strip().startswith("###"))
        quote = " ".join(quote.split())
        if len(quote) < 12:
            continue
        tags = []
        for tag in item.get("tags") or []:
            facet = str(tag.get("facet") or "").strip()
            label = " ".join(str(tag.get("label") or "").split())
            if facet in FACETS and label:
                tags.append({"facet": facet, "label": label})
        kept.append({"title": title, "tags": tags, "span": {"start_line": start, "end_line": end}, "quote": quote[:500]})
    return kept


def index_list(workspace: Path) -> dict:
    path = workspace / "index.json"
    if not path.exists():
        return {"sources": {}, "items": []}
    data = load_json(path)
    data.setdefault("sources", {})
    data.setdefault("items", [])
    return data


def index_file(path: Path, root: Path, workspace: Path, model, lock) -> str:
    text = path.read_text()
    if _is_channel_manifest(path, text):
        return "skipped:manifest"
    lines = text.splitlines()
    if not any(line.strip() for line in lines):
        return "empty"
    digest = hashlib.sha256(text.encode()).hexdigest()
    ident = source_id(path, root)
    rel = path.relative_to(root).as_posix()
    with lock:
        if index_list(workspace)["sources"].get(ident, {}).get("sha256") == digest:
            return "unchanged"
    mode, extra = plan(text)
    numbered = "\n".join(f"{i}|{line}" for i, line in enumerate(lines, 1))
    raw = model.complete("index_items", SCHEMA, PROMPT, numbered + extra)
    items = accept(lines, raw)
    if not items:
        raise ValueError("No valid index items")
    for n, item in enumerate(items):
        item["item_id"] = f"{ident}:{item['span']['start_line']:04d}-{item['span']['end_line']:04d}"
        item["source_id"] = ident
        item["path"] = rel
    # adjacency pointers within this source
    for n, item in enumerate(items):
        item["prev"] = items[n - 1]["item_id"] if n > 0 else None
        item["next"] = items[n + 1]["item_id"] if n + 1 < len(items) else None
    with lock:
        data = index_list(workspace)
        data["sources"][ident] = {"path": rel, "sha256": digest, "basis": raw.get("basis") or mode}
        data["items"] = [item for item in data["items"] if item.get("source_id") != ident]
        data["items"].extend(items)
        atomic(workspace / "index.json", js(data))
    return f"{mode}:{len(items)}"


def index_paths(selected, root, workspace, model, budget, *, workers=1, clients=None):
    failures = []

    def run(path, client, lock):
        try:
            with lock:
                if budget[0] <= 0:
                    raise RuntimeError("Call budget exhausted")
                budget[0] -= 1
            print(f"{path.relative_to(root)}: {index_file(path, root, workspace, client, lock)}", flush=True)
        except Exception as exc:
            if type(exc).__name__ == "ProviderBlocked" or "Call budget exhausted" in str(exc):
                raise
            failures.append(path)
            print(f"{path.relative_to(root)}: incomplete ({exc})", flush=True)

    run_bounded(selected, workers, clients or [model], run)
    if failures:
        raise RuntimeError(f"Index incomplete for {len(failures)} source(s)")


def demo():
    assert not has_list("what is after 12th ?\nSeptember 2026 - approx 80k")
    assert has_list("1. Stop sending listings\n2. Ask if they are still looking")
    assert has_list("  0:00 Introduction\n  0:59 Warning 1 - The Coordination Trap")
    assert not has_list("### 00:00:00 · Speaker 1\nhello")
    lines = ["# t", "", "1. Stop sending listings now", "", "2. Ask if they are still looking now"]
    kept = accept(lines, {"items": [
        {"title": "section 1", "tags": [], "span": {"start_line": 3, "end_line": 3}},
        {"title": "Stop sending listings", "tags": [{"facet": "topic", "label": "sales"}], "span": {"start_line": 3, "end_line": 3}},
    ]})
    assert len(kept) == 1 and kept[0]["quote"].startswith("1. Stop")
    assert kept[0]["tags"] == [{"facet": "topic", "label": "sales"}]
    # bad facet rejected
    kept2 = accept(lines, {"items": [
        {"title": "Stop sending listings", "tags": [{"facet": "nope", "label": "x"}], "span": {"start_line": 3, "end_line": 3}},
    ]})
    assert kept2[0]["tags"] == []
    # channel manifest detection
    assert _is_channel_manifest(Path("x.yaml"), "channel_url: https://...\ntotal_videos: 5\nvideos:\n")
    assert not _is_channel_manifest(Path("x.yaml"), "profile:\n  name: Test\n")
    assert not _is_channel_manifest(Path("x.md"), "total_videos: 5\n")
    # timecode parsing
    assert _to_seconds("1:43") == 103
    assert _to_seconds("01:12:10") == 4330
    # numbered list ranges
    assert _num_to_ranges(["a", "1. X", "y", "2. Y", "z"], [2, 4]) == [(2, 3), (4, 5)]
    # numbered list with comments section
    assert _num_to_ranges(["a", "1. X", "y", "2. Y", "## Comments", "c"], [2, 4]) == [(2, 3), (4, 4)]
    # timecode ranges with transcript turns
    tc_lines = [
        "0:00 Intro", "1:30 Topic A", "---", "",
        "### 00:00:00 · S1", "hello", "### 00:00:30 · S1", "world",
        "### 00:01:30 · S1", "topic a", "### 00:02:00 · S1", "more",
    ]
    ranges = list_ranges(tc_lines)
    assert len(ranges) == 2
    assert ranges[0][0] == 5  # maps to ### 00:00:00
    assert ranges[1][0] == 9  # maps to ### 00:01:30
    # list_ranges for numbered items
    num_lines = ["header", "1. First point", "detail", "2. Second point", "detail"]
    assert list_ranges(num_lines) == [(2, 3), (4, 5)]
    # plan uses deterministic ranges for list mode
    tc_text = "0:00 Intro\n1:30 Topic\n---\n\n### 00:00:00 · S1\nhello\n### 00:01:30 · S1\ntopic"
    mode, extra = plan(tc_text)
    assert mode == "list" and "lines 5-" in extra
    print("index demo ok")


if __name__ == "__main__":
    demo()
