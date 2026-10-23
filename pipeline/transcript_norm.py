"""Normalize a transcript file: merge same-speaker turns, strip punctuation, refuse any lost word.

The file layout (front matter + `speaker_N: text` turns, no Markdown) lives in social/content.py.

  1. merge (deterministic)  consecutive same-speaker turns become one turn
  2. clean (rule-based)     noise tags removed; spoken symbols -> words
                            (= equals, + plus, * times, % percent, 0.5 point,
                            1/3 by, 1:1 to, word-joining hyphen -> space,
                            don't -> dont, remaining P*/S* -> space)
  3. validate (per turn)    every letter/digit/Devanagari char of the original
                            must survive in order; only sanctioned insertions
                            allowed. Refuses to write on any failure.

CLI:
    python -m pipeline transcripts FILE... [--write]   normalize (dry run by default)
    python -m social.content users [--write]           convert old Markdown layouts (one-off migration)
"""
from __future__ import annotations

import argparse
import itertools
import re
import unicodedata
from pathlib import Path

from social.content import read_turns, render_turns, split

KEEP_CATS = ("L", "M", "N")  # letters, combining marks, digits
NOISE_TAGS = re.compile(
    r"\[(music|applause|laughter|clears? throat|snorts?|coughs?|noise|sighs?|laughs?|silence)\]",
    re.I,
)


class TranscriptValidationError(Exception):
    pass


def _is_punct(ch: str) -> bool:
    return unicodedata.category(ch)[0] in ("P", "S")


def _skeleton(s: str) -> str:
    return unicodedata.normalize(
        "NFC", "".join(c for c in s if unicodedata.category(c)[0] in KEEP_CATS))


def _trim(text: str) -> str:
    lines = text.splitlines()
    while lines and not lines[0].strip():
        lines.pop(0)
    while lines and not lines[-1].strip():
        lines.pop()
    return "\n".join(lines)


def _clean_line(line: str) -> str:
    s = NOISE_TAGS.sub(" ", line)
    # spoken symbols -> words
    s = re.sub(r"(?<=\d)\.(?=\d)", " point ", s)
    s = re.sub(r"(?<=\d):(?=\d)", " to ", s)
    s = s.replace("=", " equals ").replace("+", " plus ")
    s = s.replace("*", " times ").replace("%", " percent ")
    s = re.sub(r"(\w) ?/ ?(\w)", r"\1 by \2", s)
    # hyphen: word-join between letters -> space; term separator -> minus
    s = re.sub(r"(?<=[A-Za-z])-(?=[A-Za-z])", " ", s)
    s = re.sub(r"(?<=\w) - (?=\w)", " minus ", s)
    s = re.sub(r"(?<![\w])- ", " minus ", s)
    # apostrophe/period between letters -> delete (dont, VAEs, ie)
    s = re.sub(r"(?<=[A-Za-z])['\u2019](?=[A-Za-z])", "", s)
    s = re.sub(r"(?<=[A-Za-z])\.(?=[A-Za-z])", "", s)
    s = re.sub(r"(?<=\d),(?=\d)", "", s)
    # ASR latex-ish artifacts keep inner words
    s = s.replace("\\", " ").replace("{", " ").replace("}", " ")
    # remaining punctuation/symbols -> space
    s = "".join(" " if _is_punct(c) else c for c in s)
    return re.sub(r" {2,}", " ", s).rstrip()


def _insertions_only(o_sk: str, n_sk: str):
    """Greedy subsequence: every original char must appear in order in the new
    text; only new chars (sanctioned expansions) may be inserted. None = OK."""
    i, m = 0, len(n_sk)
    for j, ch in enumerate(o_sk):
        while i < m and n_sk[i] != ch:
            i += 1
        if i == m:
            return f"lost/changed at orig char {j}: ...{o_sk[max(0, j - 40):j + 40]!r}"
        i += 1
    return None


def _labels(fm: str) -> list[str]:
    m = re.search(r"^speakers:\n((?:[ \t]+.*\n?)*)", fm, re.M)
    return re.findall(r"^[ \t]+(speaker_[1-9]\d*):", m.group(1), re.M) if m else []


def normalize_transcript(md_text: str, source: str = "") -> str:
    """Transcript file in -> normalized file out (front matter unchanged). Raises on any failure."""
    fm, body = split(md_text)
    try:
        turns = read_turns(body, _labels(fm))
    except ValueError as exc:
        raise TranscriptValidationError(f"{source}: refused\n   {exc}") from None
    if not turns:
        if body.strip():
            raise TranscriptValidationError(f"{source}: refused\n   text without speaker turns")
        return md_text  # no speech
    groups = [(k, "\n\n".join(t for _, t in g)) for k, g in itertools.groupby(turns, key=lambda t: t[0])]
    cleaned, errs = [], []
    for k, (label, otext) in enumerate(groups):
        ntext = _trim("\n".join(_clean_line(l) for l in otext.splitlines()))
        if not _skeleton(ntext):
            errs.append(f"segment {k}: empty after cleanup")
            continue
        lost = _insertions_only(_skeleton(NOISE_TAGS.sub(" ", otext)), _skeleton(ntext))
        if lost:
            errs.append(f"segment {k} ({label}): {lost}")
        bad = sorted({c for c in ntext if _is_punct(c)})
        if bad:
            errs.append(f"segment {k}: leftover punctuation/symbols: {bad}")
        if re.search(r"\d\d:\d\d:\d\d", ntext):
            errs.append(f"segment {k}: leftover timestamp")
        cleaned.append((label, ntext))
    if errs:
        raise TranscriptValidationError(
            f"{source}: refused\n" + "\n".join("   " + e for e in errs[:10]))
    return "---\n" + fm + "---\n\n" + render_turns(cleaned) + "\n"


def cli_files(files, write=False):
    """CLI entry used by pipeline/__main__.py `transcripts` subcommand."""
    failed = 0
    for path in files:
        try:
            out = normalize_transcript(path.read_text(), source=str(path))
        except TranscriptValidationError as e:
            failed += 1
            print(f"REFUSED {path.name}\n{e}")
            continue
        if write:
            path.write_text(out)
        print(f"OK {path.name} [{'written' if write else 'dry run'}]")
    if failed:
        raise SystemExit(1)


def cli():
    parser = argparse.ArgumentParser(description="Normalize transcript md files")
    parser.add_argument("files", nargs="+", type=Path)
    parser.add_argument("--write", action="store_true", help="overwrite in place (default: dry run)")
    args = parser.parse_args()
    cli_files(args.files, write=args.write)


if __name__ == "__main__":
    cli()
