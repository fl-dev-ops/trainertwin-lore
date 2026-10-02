"""Small file helpers used by the index."""

from __future__ import annotations

import json
import os
import queue
import tempfile
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Any


def js(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, indent=2) + "\n"


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


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


def run_bounded(items, workers, clients, fn):
    """Run fn(item, client, lock). One client stays on one thread."""
    if workers < 1 or len(clients) != workers:
        raise ValueError("--workers must be positive and match the client count")
    lock = threading.Lock()
    if workers == 1:
        for item in items:
            fn(item, clients[0], lock)
        return
    available, local, stop, fatal = queue.Queue(), threading.local(), threading.Event(), []
    for client in clients:
        available.put(client)

    def wrapped(item):
        if stop.is_set():
            return
        if not hasattr(local, "client"):
            local.client = available.get()
        try:
            fn(item, local.client, lock)
        except Exception as exc:
            if type(exc).__name__ == "ProviderBlocked" or "Call budget exhausted" in str(exc):
                stop.set()
                fatal.append(exc)
            raise

    with ThreadPoolExecutor(max_workers=workers) as pool:
        futures = [pool.submit(wrapped, item) for item in items]
        for future in as_completed(futures):
            future.result()
    if fatal:
        raise fatal[0]
