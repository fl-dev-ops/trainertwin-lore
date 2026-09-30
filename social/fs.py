"""Durable file writes: an interrupted process must never leave a half-written source file."""

import os
import tempfile


def atomic_write(path, text: str) -> None:
    """Write text via a same-directory temp file and an atomic rename."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        "w", encoding="utf-8", dir=path.parent, delete=False, prefix=f".{path.name}."
    ) as handle:
        temp = handle.name
        try:
            handle.write(text)
            handle.flush()
            os.fsync(handle.fileno())
            os.replace(temp, path)
        finally:
            if os.path.exists(temp):
                os.unlink(temp)
