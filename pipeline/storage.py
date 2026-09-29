"""Small file-store primitives: budgets, validated caches and artifact receipts."""

from __future__ import annotations

import fcntl
import hashlib
import json
import os
import tempfile
from collections.abc import Callable
from contextlib import contextmanager
from datetime import UTC, datetime
from pathlib import Path
from typing import Any, Protocol

# Stored-data compatibility marker, not a selectable pipeline implementation.
SCHEMA_VERSION = "4"


class Model(Protocol):
    model: str

    def complete(self, name: str, schema: dict, system: str, user: str) -> dict: ...


def stamp() -> str:
    return datetime.now(UTC).isoformat(timespec="seconds").replace("+00:00", "Z")


def js(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n"


def digest(value: Any) -> str:
    return hashlib.sha256(
        value if isinstance(value, bytes) else js(value).encode()
    ).hexdigest()


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def json_lines(path: Path) -> list[dict]:
    if not path.exists():
        return []
    values = [
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    if any(not isinstance(item, dict) for item in values):
        raise ValueError(f"Expected object records in {path}")
    return values


def jsonl(values: list[dict]) -> str:
    return "".join(
        json.dumps(v, ensure_ascii=False, sort_keys=True) + "\n" for v in values
    )


def atomic(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        "w", encoding="utf-8", dir=path.parent, delete=False
    ) as stream:
        temporary = Path(stream.name)
        try:
            stream.write(text)
            stream.flush()
            os.fsync(stream.fileno())
            temporary.replace(path)
        finally:
            temporary.unlink(missing_ok=True)


def append(path: Path, record: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as stream:
        stream.write(json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n")


def log(workspace: Path, event: str) -> None:
    append(workspace / "events.jsonl", {"at": stamp(), "event": event})


@contextmanager
def one_writer(workspace: Path):
    workspace.mkdir(parents=True, exist_ok=True)
    with (workspace / ".lock").open("a") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        try:
            yield
        finally:
            fcntl.flock(lock, fcntl.LOCK_UN)


def inside(root: Path, relative: str) -> Path:
    if (
        not isinstance(relative, str)
        or not relative
        or Path(relative).is_absolute()
        or ".." in Path(relative).parts
    ):
        raise ValueError("Expected a safe relative artifact/source path")
    path = root / relative
    if not path.resolve().is_relative_to(root.resolve()) or path.is_symlink():
        raise ValueError(f"Path escapes its root or is a symlink: {relative}")
    return path


def file_hash(path: Path) -> str:
    return digest(path.read_bytes())


def publish(directory: Path, files: dict[str, str], inputs: dict) -> dict:
    """Write generated files, then publish their completion receipt last.

    Only files owned by a previous receipt can be pruned. Human/unmanaged files
    are never read as evidence or silently removed. Call under one_writer.
    """
    receipt_path = directory / "build.json"
    old = load_json(receipt_path).get("files", {}) if receipt_path.exists() else {}
    for name, text in files.items():
        if name == "build.json":
            raise ValueError("build.json is reserved for the artifact receipt")
        atomic(inside(directory, name), text)
    for name in set(old) - set(files):
        inside(directory, name).unlink(missing_ok=True)
    receipt = {
        "version": SCHEMA_VERSION,
        "inputs": inputs,
        "files": {name: file_hash(inside(directory, name)) for name in sorted(files)},
    }
    atomic(receipt_path, js(receipt))
    return receipt


def check_artifacts(directory: Path, inputs: dict | None = None) -> dict:
    path = directory / "build.json"
    if not path.exists():
        raise ValueError(f"Incomplete {directory.name}; regenerate it")
    receipt = load_json(path)
    if receipt.get("version") != SCHEMA_VERSION or (
        inputs is not None and receipt.get("inputs") != inputs
    ):
        raise ValueError(f"Stale {directory.name}; regenerate it from current records")
    files = receipt.get("files")
    if not isinstance(files, dict) or not files:
        raise ValueError(f"Invalid artifact receipt: {path}")
    for name, expected in files.items():
        artifact = inside(directory, name)
        if not artifact.is_file() or file_hash(artifact) != expected:
            raise ValueError(f"Modified or missing artifact: {artifact}")
    return receipt


def cached_call(
    workspace: Path,
    model: Model,
    operation: str,
    schema: dict,
    prompt: str,
    payload: dict,
    budget: list[int],
    validate: Callable[[dict], Any],
) -> Any:
    """One logical budget for every request/repair; never cache invalid output."""
    if len(budget) != 1 or type(budget[0]) is not int or budget[0] < 0:
        raise ValueError("Budget must contain one nonnegative integer")
    key = digest([SCHEMA_VERSION, model.model, operation, schema, prompt, payload])
    cache = workspace / "cache" / operation / f"{key}.json"
    if cache.exists():
        return validate(load_json(cache))
    message = js(payload)
    for attempt in range(2):
        if budget[0] <= 0:
            raise RuntimeError(
                f"Call budget exhausted ({operation}); completed calls remain cached"
            )
        budget[0] -= 1
        try:
            result = model.complete(operation, schema, prompt, message)
        finally:
            usage = getattr(model, "last_usage", None)
            if isinstance(usage, dict) and usage:
                append(
                    workspace / "usage.jsonl",
                    {
                        "at": stamp(),
                        "model": model.model,
                        "operation": operation,
                        "repair": bool(attempt),
                        "usage": usage,
                    },
                )
        try:
            value = validate(result)
        except ValueError as exc:
            log(workspace, f"validation-failed | {operation} | {exc}")
            if attempt:
                raise ValueError(
                    f"Invalid {operation} after repair; nothing published: {exc}"
                ) from exc
            message = (
                js(payload)
                + f"\nValidation error: {exc}. Return a complete corrected response; do not invent missing evidence."
            )
        else:
            atomic(cache, js(result))
            return value
    raise AssertionError("unreachable")


def partition(items: list[dict], max_chars: int) -> list[list[dict]]:
    if max_chars < 1000:
        raise ValueError("Chunk size must be at least 1000 characters")
    groups, current, size = [], [], 0
    for item in items:
        length = len(js(item))
        if length > max_chars:
            raise ValueError(
                "One complete item exceeds the context budget; increase --chunk-chars"
            )
        if current and size + length > max_chars:
            groups.append(current)
            current, size = [], 0
        current.append(item)
        size += length
    if current:
        groups.append(current)
    return groups
