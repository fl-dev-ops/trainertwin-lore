"""Terminal progress bars with newline-only progress for redirected/background logs."""

import sys
from collections.abc import Iterable, Iterator, Sized
from contextlib import contextmanager
from threading import local
from time import monotonic

from tqdm import tqdm

_platform = local()


@contextmanager
def platform_progress(name: str, position: int, stages: int, child_base: int):
    """Reserve one terminal row per platform and one for its current item-level task."""
    terminal = sys.stderr.isatty()
    with tqdm(
        total=stages,
        desc=name,
        unit="stage",
        position=position,
        file=sys.stderr,
        disable=not terminal,
        dynamic_ncols=True,
        leave=True,
    ) as bar:
        _platform.bar = bar
        _platform.name = name
        _platform.done = 0
        _platform.child_position = child_base + position
        if not terminal:
            status(f"{name}: 0/{stages} stages — starting")
        try:
            yield
        finally:
            if not terminal:
                state = "finished" if _platform.done == stages else "stopped"
                status(f"{name}: {_platform.done}/{stages} stages — {state}")
            del _platform.bar, _platform.name, _platform.done, _platform.child_position


def stage(message: str) -> None:
    """Advance the current platform's known stage count; no-op in standalone CLIs."""
    bar = getattr(_platform, "bar", None)
    if bar is not None:
        _platform.done += 1
        if bar.disable:
            status(f"{_platform.name}: {_platform.done}/{bar.total} stages — {message}")
        else:
            bar.set_postfix_str(message)
            bar.update(1)


def status(message: str) -> None:
    """Keep progress off stdout, which standalone collectors use for data output."""
    tqdm.write(message, file=sys.stderr)


def track[T](
    items: Iterable[T], label: str, *, unit: str = "item", total: int | None = None
) -> Iterator[T]:
    """Count processed items, not successful results; do not invent provider progress."""
    if total is None and isinstance(items, Sized):
        total = len(items)
    terminal = sys.stderr.isatty()
    started = last_report = monotonic()
    count = 0
    finished = False
    target = "?" if total is None else str(total)
    if not terminal:
        status(f"{label}: 0/{target} {unit} processed — starting")
    try:
        with tqdm(
            total=total,
            desc=label,
            unit=unit,
            file=sys.stderr,
            disable=not terminal,
            dynamic_ncols=True,
            mininterval=0.5,
            position=getattr(_platform, "child_position", None),
            leave=not hasattr(_platform, "child_position"),
        ) as bar:
            for item in items:
                yield item
                count += 1
                bar.update(1)
                now = monotonic()
                if not terminal and (
                    count == 1 or count % 10 == 0 or now - last_report >= 15
                ):
                    status(
                        f"{label}: {count}/{target} {unit} processed ({now - started:.0f}s)"
                    )
                    last_report = now
        finished = True
    finally:
        if not terminal:
            state = "finished" if finished else "stopped"
            status(
                f"{label}: {count}/{target} {unit} processed — {state} ({monotonic() - started:.0f}s)"
            )
