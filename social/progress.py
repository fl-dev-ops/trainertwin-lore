"""Terminal progress bars with newline-only progress for redirected/background logs."""

import sys
from collections.abc import Iterable, Iterator, Sized
from time import monotonic

from tqdm import tqdm


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
