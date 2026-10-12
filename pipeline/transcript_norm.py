"""Normalize video transcript markdown into turn-merged, punctuation-free text.

One entry point: `normalize_transcript(md_text)` takes a transcript .md file's
content and returns the normalized content, or raises TranscriptValidationError
if any spoken word would be lost.

Pipeline:
  1. merge (deterministic)  drop `### HH:MM:SS ·` timestamps, merge consecutive
                            same-speaker turns into one `### Speaker N` block
  2. clean (rule-based)     noise tags removed; spoken symbols -> words
                            (= equals, + plus, * times, % percent, 0.5 point,
                            1/3 by, 1:1 to, word-joining hyphen -> space,
                            don't -> dont, remaining P*/S* -> space)
  3. validate (per turn)    every letter/digit/Devanagari char of the original
                            must survive in order; only sanctioned insertions
                            allowed. Refuses to write on any failure.

CLI:
    python -m pipeline transcripts file1.md file2.md... [--write]
    Default is a dry run (prints per-file stats, writes nothing).
"""
from __future__ import annotations

import argparse
import itertools
import re
import unicodedata
from pathlib import Path

KEEP_CATS = ("L", "M", "N")  # letters, combining marks, digits
TURN_HEADER = re.compile(r"^### (?:\d\d:\d\d:\d\d · )?(.+)$")
NOISE_TAGS = re.compile(
    r"\[(music|applause|laughter|clears? throat|snorts?|coughs?|noise|sighs?|laughs?|silence)\]",
    re.I,
)

PUNCT_NAME = None  # set lazily in _is_punct


def _is_punct(ch: str) -> bool:
    return unicodedata.category(ch)[0] in ("P", "S")


def _skeleton(s: str) -> str:
    return unicodedata.normalize(
        "NFC", "".join(c for c in s if unicodedata.category(c)[0] in KEEP_CATS))


def _merge_text(text: str) -> str:
    lines = text.splitlines()
    while lines and not lines[0].strip():
        lines.pop(0)
    while lines and not lines[-1].strip():
        lines.pop()
    return "\n".join(lines)


def _parse(md_text: str):
    """-> (frontmatter, other_lines, turns=[(label, text)]); turns empty for
    caption-style files without headers."""
    m = re.match(r"(---\n.*?\n---\n)", md_text, re.S)
    fm = m.group(1) if m else ""
    rest = md_text[len(fm):]
    parts = rest.split("## Transcript", 1)
    if len(parts) != 2:
        raise ValueError("no '## Transcript' section")
    turns, other = [], []
    cur_label, cur = None, []
    for line in parts[1].splitlines():
        tm = TURN_HEADER.match(line)
        if tm:
            if cur_label is not None:
                turns.append((cur_label, "\n".join(cur)))
            cur_label, cur = tm.group(1).strip(), []
        elif line.startswith("# ") or line.strip() == "## Transcript":
            other.append(line)
        elif cur_label is not None:
            cur.append(line)
    if cur_label is not None:
        turns.append((cur_label, "\n".join(cur)))
    return fm, other, turns


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


class TranscriptValidationError(Exception):
    pass


def normalize_transcript(md_text: str, source: str = "") -> str:
    """Transcript md in -> normalized md out. Raises on any validation failure."""
    fm, other, turns = _parse(md_text)
    if not turns:  # caption-style: single implicit segment
        body = md_text.split("## Transcript", 1)[1]
        groups = [(None, _merge_text(body))]
    else:
        groups = [(k, _merge_text("\n".join(t[1] for t in g)))
                  for k, g in itertools.groupby(turns, key=lambda t: t[0])]

    cleaned, errs = [], []
    for k, (label, otext) in enumerate(groups):
        ntext = _merge_text("\n".join(_clean_line(l) for l in otext.splitlines()))
        if not _skeleton(ntext):
            errs.append(f"segment {k}: empty after cleanup")
            continue
        lost = _insertions_only(_skeleton(NOISE_TAGS.sub(" ", otext)), _skeleton(ntext))
        if lost:
            errs.append(f"segment {k} ({label or 'body'}): {lost}")
        bad = sorted({c for c in ntext if _is_punct(c)})
        if bad:
            errs.append(f"segment {k}: leftover punctuation/symbols: {bad}")
        if re.search(r"\d\d:\d\d:\d\d", ntext):
            errs.append(f"segment {k}: leftover timestamp")
        cleaned.append((label, ntext))
    if errs:
        raise TranscriptValidationError(
            f"{source}: refused\n" + "\n".join("   " + e for e in errs[:10]))

    out = [fm] + other + ["## Transcript", ""]
    for label, text in cleaned:
        if label:
            out += [f"### {label}", ""]
        out += [text, ""]
    return "\n".join(out)


def cli_files(files, write=False):
    """CLI entry used by pipeline/__main__.py `transcripts` subcommand."""
    failed = 0
    for path in files:
        try:
            out = normalize_transcript(path.read_text(), source=str(path))
        except (TranscriptValidationError, ValueError) as e:
            failed += 1
            print(f"REFUSED {path.name}\n{e}")
            continue
        turns = out.count("\n### ")
        if write:
            path.write_text(out)
            print(f"OK {path.name} ({turns} speaker turns) [written]")
        else:
            print(f"OK {path.name} ({turns} speaker turns) [dry run]")
    if failed:
        raise SystemExit(1)


def cli():
    parser = argparse.ArgumentParser(description="Normalize transcript md files")
    parser.add_argument("files", nargs="+", type=Path)
    parser.add_argument("--write", action="store_true", help="overwrite in place (default: dry run)")
    args = parser.parse_args()
    failed = 0
    for path in args.files:
        try:
            out = normalize_transcript(path.read_text(), source=str(path))
        except (TranscriptValidationError, ValueError) as e:
            failed += 1
            print(f"REFUSED {path.name}\n{e}")
            continue
        turns = out.count("\n### ")
        if args.write:
            path.write_text(out)
            print(f"OK {path.name} ({turns} speaker turns) [written]")
        else:
            print(f"OK {path.name} ({turns} speaker turns) [dry run]")
    raise SystemExit(1 if failed else 0)


if __name__ == "__main__":
    cli()
