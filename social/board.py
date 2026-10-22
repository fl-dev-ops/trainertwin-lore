"""uv-style live board for parallel jobs.

The live area holds only one overall row per board plus the jobs running right now, so it
stays shorter than the terminal (taller frames can't be redrawn in place and duplicate).
Finished jobs scroll up as permanent ✓/✗ lines. All boards in the process share one Live
display, because concurrent Live displays (YouTube + Loom threads) overwrite each other.
"""

from __future__ import annotations

import re
import sys
import threading
from collections.abc import Callable
from contextlib import contextmanager
from time import monotonic
from typing import Any

from rich.console import Console
from rich.markup import escape
from rich.progress import (
    BarColumn,
    Progress,
    ProgressColumn,
    TaskID,
    TaskProgressColumn,
    TextColumn,
    TimeElapsedColumn,
)
from rich.spinner import Spinner
from rich.table import Column
from rich.text import Text


class StatusIconColumn(ProgressColumn):
    """Spinner while running, ⏸ before any progress."""

    def __init__(self) -> None:
        super().__init__()
        self.spinner = Spinner("dots")

    def render(self, task: Any) -> Text:
        if task.completed == 0:
            return Text("⏸", style="dim")
        return self.spinner.render(task.get_time())


_thread_job = threading.local()
_shared_lock = threading.RLock()
_shared: Progress | None = None
_users = 0


def board_live() -> bool:
    """True while a board owns the terminal; other writers (tqdm) must stay quiet."""
    return _shared is not None


def _acquire(make_console: Callable[[], Console]) -> Progress:
    global _shared, _users
    with _shared_lock:
        if _shared is None:
            _shared = Progress(
                StatusIconColumn(),
                TextColumn("{task.fields[name]}", table_column=Column(width=32, no_wrap=True, overflow="ellipsis")),
                BarColumn(bar_width=16),
                TaskProgressColumn(),
                TextColumn("{task.description}", table_column=Column(width=34, no_wrap=True, overflow="ellipsis")),
                TimeElapsedColumn(),
                console=make_console(),
                transient=True,
                refresh_per_second=2,  # SSH over a saturated link: full redraws every 10Hz are pricey
                redirect_stdout=False,  # stdout is data for standalone collectors; never reroute it
            )
            _shared.start()
        _users += 1
        return _shared


def _release() -> None:
    global _shared, _users
    with _shared_lock:
        _users -= 1
        if _users == 0 and _shared is not None:
            _shared.stop()
            _shared = None


def _elapsed(seconds: float) -> str:
    minutes, secs = divmod(int(seconds), 60)
    return f"{minutes}:{secs:02d}"


class ParallelJobBoard:
    """Per-platform view onto the shared live display."""

    def __init__(self, title: str, total_jobs: int, total_steps: int = 5, console: Console | None = None) -> None:
        self.title = title
        self.total_jobs = total_jobs
        self.total_steps = total_steps
        self.terminal = console.is_terminal if console is not None else sys.stderr.isatty()
        self._console = console
        self._lock = threading.Lock()
        self._names: dict[str, str] = {}
        self._tasks: dict[str, TaskID] = {}
        self._started: dict[str, float] = {}
        self._finished = 0
        self._failed = 0
        self.progress: Progress | None = None
        self._overall: TaskID | None = None

    def add_job(self, job_id: str, name: str) -> None:
        """Register a queued job; it gets a row only once it starts."""
        self._names[job_id] = " ".join(str(name).split()) or job_id

    def _refresh_overall(self) -> None:
        if self.progress is None or self._overall is None:
            return
        running = len(self._tasks)
        queued = self.total_jobs - self._finished - running
        desc = f"{self._finished}/{self.total_jobs} done · {running} running · {max(queued, 0)} queued"
        if self._failed:
            desc += f" · [red]{self._failed} failed[/red]"
        self.progress.update(self._overall, completed=self._finished, description=desc)

    def update(
        self,
        job_id: str,
        stage: str,
        step: float | None = None,
        style: str = "yellow",
        done: bool = False,
        error: str | None = None,
    ) -> None:
        if self.progress is None:
            return
        with self._lock:
            name = escape(self._names.get(job_id, job_id))
            task = self._tasks.get(job_id)
            if done or error:
                if task is not None:
                    self.progress.remove_task(task)
                    del self._tasks[job_id]
                took = _elapsed(monotonic() - self._started.pop(job_id, monotonic()))
                if error:
                    self._failed += 1
                    reason = escape(error.strip().splitlines()[0] if error.strip() else "error")
                    self.progress.console.print(f"[bold red]✗[/bold red] {name} [red]— {reason}[/red]")
                else:
                    self.progress.console.print(f"[bold green]✓[/bold green] {name} [dim]({took})[/dim]")
                self._refresh_overall()
                return
            if task is None:
                task = self.progress.add_task("", name=name, total=self.total_steps, completed=0)
                self._tasks[job_id] = task
                self._started[job_id] = monotonic()
                self._refresh_overall()
            changes: dict[str, Any] = {"description": f"[{style}]{escape(stage)}[/{style}]"}
            if step is not None:
                changes["completed"] = step
            self.progress.update(task, **changes)

    def advance_overall(self) -> None:
        if self.progress is None:
            return
        with self._lock:
            self._finished += 1
            self._refresh_overall()

    @contextmanager
    def run(self):
        if not self.terminal or self.total_jobs == 0:
            yield self
            return
        self.progress = _acquire(lambda: self._console or Console(file=sys.stderr))
        self._overall = self.progress.add_task(
            "", name=f"[bold yellow]{escape(self.title)}[/bold yellow]", total=self.total_jobs, completed=0
        )
        self._refresh_overall()
        try:
            yield self
        finally:
            with self._lock:
                for task in [self._overall, *self._tasks.values()]:
                    self.progress.remove_task(task)
                self._tasks.clear()
                ok = self._finished - self._failed
                summary = f"[bold]{escape(self.title)}[/bold]: {ok} done"
                if self._failed:
                    summary += f", [red]{self._failed} failed[/red]"
                self.progress.console.print(summary)
            self.progress = None
            self._overall = None
            _release()


@contextmanager
def active_job(board: ParallelJobBoard, job_id: str):
    """Bind the worker thread to a job so status() messages update its row."""
    _thread_job.board = board
    _thread_job.job_id = job_id
    try:
        yield
    finally:
        _thread_job.board = None
        _thread_job.job_id = None


_STAGES = (
    ("downloading", "downloading audio", 1, "yellow"),
    ("uploading temporary audio", "uploading to AssemblyAI", 2, "cyan"),
    ("resuming transcription job", "resuming AssemblyAI job", 3, "magenta"),
    ("transcribing audio", "transcribing audio", 4, "blue"),
    ("transcript ready", "transcript ready", 4.5, "green"),
)


def notify_status(message: str) -> bool:
    """Route a known stage message from a bound worker thread into its row."""
    board: ParallelJobBoard | None = getattr(_thread_job, "board", None)
    job_id: str | None = getattr(_thread_job, "job_id", None)
    if board is None or job_id is None or board.progress is None:
        return False
    for needle, stage, step, style in _STAGES:
        if needle in message:
            client = re.search(r"\(([a-z_]+)\)$", message.strip())  # yt-dlp fallback client
            board.update(job_id, stage=f"{stage} ({client[1]})" if client and step == 1 else stage,
                         step=step, style=style)
            return True
    return False


def print_board_status(message: str) -> bool:
    """While a board is live, print other messages above it instead of through it."""
    with _shared_lock:
        progress = _shared
    if progress is None:
        return False
    progress.console.print(escape(message))
    return True
