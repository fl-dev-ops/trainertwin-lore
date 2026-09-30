"""Small file-store primitives: budgets, validated caches and artifact receipts."""

from __future__ import annotations

import fcntl
import hashlib
import json
import os
import tempfile
import time
from collections.abc import Callable
from contextlib import contextmanager
from copy import deepcopy
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
    if path.is_file() and path.read_text(encoding="utf-8") == text:
        return
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


class InvalidItems(ValueError):
    """Item-local failures can be repaired without regenerating valid siblings."""

    def __init__(self, errors):
        self.errors = errors  # (section, index, message)
        super().__init__("; ".join(f"{s}[{i}]: {e}" for s, i, e in errors))


def call_key(model, operation, schema, prompt, payload):
    return digest([SCHEMA_VERSION, model, operation, schema, prompt, payload])


def source_progress(workspace, stage, source, status, error=None):
    atomic(
        workspace / "work" / f"{stage}_sources" / f"{source.id}.json",
        js(
            {
                "source_id": source.id,
                "source_path": source.relative_path,
                "source_hash": source.sha256,
                "metadata_hash": source.metadata_hash,
                "status": status,
                "error": error,
            }
        ),
    )


def work_state(workspace, operation, key):
    path = workspace / "work" / operation / f"{key}.json"
    return load_json(path) if path.exists() else {"status": "pending"}


def cached_call(
    workspace: Path,
    model: Model,
    operation: str,
    schema: dict,
    prompt: str,
    payload: dict,
    budget: list[int],
    validate: Callable[[dict], Any],
    *,
    retry_failed=False,
) -> Any:
    """Persist checkpoints, quarantine rejected responses, and repair only bad items."""
    if len(budget) != 1 or type(budget[0]) is not int or budget[0] < 0:
        raise ValueError("Budget must contain one nonnegative integer")
    key = call_key(model.model, operation, schema, prompt, payload)
    cache = workspace / "cache" / operation / f"{key}.json"
    state_path = workspace / "work" / operation / f"{key}.json"
    state = work_state(workspace, operation, key)

    def mark(status, error=None):
        state.update(
            status=status,
            key=key,
            operation=operation,
            source_id=payload.get("source_id"),
            updated_at=stamp(),
            error=error,
        )
        atomic(state_path, js(state))

    if cache.exists():
        try:
            value = validate(load_json(cache))
        except ValueError as exc:
            mark("failed", str(exc))
            if not retry_failed:
                raise ValueError(
                    f"Cached {operation} fails current validation; audit or use --retry-failed: {exc}"
                ) from exc
        else:
            if state.get("status") != "completed":
                mark("completed")
            return value
    if state.get("status") == "failed" and not retry_failed:
        raise ValueError(
            f"Previous {operation} failed; use --retry-failed: {state.get('error')}"
        )
    request_schema, message, request_name = schema, js(payload), operation
    original, bad = None, None
    for attempt in range(2):
        if budget[0] <= 0:
            mark("blocked", "call_budget")
            raise RuntimeError(
                f"Call budget exhausted ({operation}); completed calls remain cached"
            )
        budget[0] -= 1
        state["attempts"] = state.get("attempts", 0) + 1
        mark("pending")  # An interrupted request remains resumable, never completed.
        started = time.monotonic()
        try:
            response = model.complete(request_name, request_schema, prompt, message)
        except Exception as exc:
            mark("blocked", str(exc))
            raise
        finally:
            usage = getattr(model, "last_usage", None)
            append(
                workspace / "usage.jsonl",
                {
                    "at": stamp(),
                    "model": model.model,
                    "operation": operation,
                    "repair": bool(attempt),
                    "key": key,
                    "source_id": payload.get("source_id"),
                    "duration_seconds": time.monotonic() - started,
                    "usage": usage if isinstance(usage, dict) else {},
                },
            )
        result = response
        try:
            if bad is not None:
                if not isinstance(response, dict) or set(response) != set(bad):
                    raise ValueError("Repair must return exactly the failed sections")
                result = deepcopy(original)
                for section, indices in bad.items():
                    if not isinstance(response[section], list) or len(
                        response[section]
                    ) != len(indices):
                        raise ValueError(
                            "Repair must return every failed item in order"
                        )
                    for index, item in zip(indices, response[section], strict=True):
                        result[section][index] = item
            value = validate(result)
        except ValueError as exc:
            atomic(
                workspace / "rejected" / operation / f"{key}-{state['attempts']}.json",
                js(
                    {
                        "key": key,
                        "request": message,
                        "response": response,
                        "error": str(exc),
                        "at": stamp(),
                    }
                ),
            )
            log(workspace, f"validation-failed | {operation} | {exc}")
            mark("failed", str(exc))
            if attempt:
                raise ValueError(
                    f"Invalid {operation} after repair; nothing published: {exc}"
                ) from exc
            repair_payload = {**payload, "validation_error": str(exc)}
            if isinstance(exc, InvalidItems):
                original, bad = result, {}
                for section, index, _ in exc.errors:
                    bad.setdefault(section, []).append(index)
                repair_payload["failed_items"] = {
                    s: [result[s][i] for i in indices] for s, indices in bad.items()
                }
                # Keep only referenced units and adjacent context. Unknown references
                # fall back to the supplied window, never to another source.
                units = payload.get("units", [])
                selected = js(repair_payload["failed_items"])
                positions = [i for i, u in enumerate(units) if u["id"] in selected]
                if positions:
                    wanted = {
                        j
                        for i in positions
                        for j in range(max(0, i - 1), min(len(units), i + 2))
                    }
                    repair_payload["units"] = [
                        u for i, u in enumerate(units) if i in wanted
                    ]
                properties = {
                    s: {
                        **schema["properties"][s],
                        "minItems": len(indices),
                        "maxItems": len(indices),
                    }
                    for s, indices in bad.items()
                }
                request_schema = {
                    "type": "object",
                    "properties": properties,
                    "required": list(properties),
                    "additionalProperties": False,
                }
                request_name = operation + "_repair"
            else:
                repair_payload["previous_response"] = response
            message = js(repair_payload)
        else:
            atomic(cache, js(result))
            mark("completed")
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
