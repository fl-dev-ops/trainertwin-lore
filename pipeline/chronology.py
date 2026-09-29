"""Offline publication chronology preview: python -m pipeline.chronology."""

import os
import re
from collections import Counter
from datetime import UTC, datetime
from html import escape
from pathlib import Path

from .core import read_records, source_root
from .records import record_summary
from .sources import read_source

ROOT = Path(__file__).resolve().parents[1]
SELECTION = Path(__file__).with_name("pilot-sources.txt")
OUT = ROOT / "users" / "olga" / "workspace"
CHANNELS = {
    "youtube": ("YouTube", "#326bb0", 150),
    "linkedin": ("LinkedIn", "#22846e", 275),
    "twitter": ("X", "#b66a28", 400),
}
KINDS = {
    "fact_claim": "Fact claim · unverified",
    "self_report": "Self-report",
    "observed_behavior": "Public behavior",
    "case_study": "Case-study claim",
    "teaching_move": "Teaching method",
    "advice": "Advice",
    "belief": "Stated belief",
    "style": "Communication style",
    "offering": "Offer",
}


def selected_sources():
    root = ROOT / "users" / "olga" / "data"
    names = [
        line.strip()
        for line in SELECTION.read_text().splitlines()
        if line.strip() and not line.startswith("#")
    ]
    if len(names) != len(set(names)):
        raise ValueError("Duplicate path in pilot-sources.txt")
    sources, omitted = [], []
    for name in names:
        path = root / name
        source = read_source(path, root)
        if not source or source.category not in CHANNELS:
            raise ValueError(f"Invalid selected source: {name}")
        if not source.date or not source.url:
            if source.category != "youtube":
                raise ValueError(f"Missing dated source or URL: {name}")
            omitted.append(
                name
            )  # Never pair an actively relabelled transcript with an old video URL.
            continue
        sources.append(source)
    return sorted(sources, key=lambda source: (source.date, source.id)), omitted


def evidence_for(sources, workspace=OUT):
    """Project current records; publication metadata may await re-ingestion."""
    root = source_root(sources[0]) if sources else None
    records, snapshots = read_records(workspace, root, require_fresh=False)
    result = {source.id: [] for source in sources}
    for source in sources:
        if source.id in snapshots and snapshots[source.id].sha256 != source.sha256:
            raise ValueError(f"Source text changed since extraction: {source.id}")
    units = {u["id"]: u for source in snapshots.values() for u in source.units}
    for record in records:
        if record["source_id"] not in result:
            continue
        field = next(
            record["content"][key]
            for key in ("summary", "situation", "observation")
            if key in record["content"]
        )
        citation = field["citations"][0]
        unit = units[citation["unit_id"]]
        result[record["source_id"]].append(
            {
                "id": record["id"],
                "source_id": record["source_id"],
                "kind": "case_study"
                if record["product"] == "cases"
                else "style"
                if record["product"] == "expression"
                else {"claim": "fact_claim", "method": "teaching_move"}.get(
                    record["content"]["kind"], record["content"]["kind"]
                ),
                "context": record["content"].get("kind", "source_local"),
                "statement": record_summary(record),
                "quote": citation["quote"],
                "locator": unit["locator"],
                "speaker_id": unit["speaker_id"],
            }
        )
    return result


def published_datetime(value):
    parsed = datetime.fromisoformat(value)
    return (
        parsed if parsed.tzinfo else parsed.replace(tzinfo=UTC)
    )  # date-only sources plot at UTC midnight


def chart(sources, evidence):
    left, right = 190, 1360
    dates = [published_datetime(s.date) for s in sources]
    earliest, latest = min(dates), max(dates)
    start = datetime(earliest.year, 1 if earliest.month < 5 else 7, 1, tzinfo=UTC)
    end = datetime(latest.year + 1, 1, 1, tzinfo=UTC)

    def x(date):
        return left + (date - start).total_seconds() / (end - start).total_seconds() * (
            right - left
        )

    counts = Counter(s.category for s in sources)
    parts = [
        '<svg class="plot" viewBox="0 0 1440 500" role="img" aria-labelledby="plot-title plot-desc" xmlns="http://www.w3.org/2000/svg">',
        '<title id="plot-title">Publication dates of selected Olga Sinenko sources</title>',
        '<desc id="plot-desc">Selected YouTube, LinkedIn, and X publication dates. This is a curated sample, not a complete activity record.</desc>',
        '<rect width="1440" height="500" fill="#fcfbf7"/>',
    ]
    for year in range(start.year, end.year + 1):
        for month, label in [(1, "JAN"), (7, "JUL")]:
            tick = datetime(year, month, 1, tzinfo=UTC)
            if start <= tick < end:
                px = x(tick)
                parts.append(
                    f'<path d="M {px:.1f} 78 V 438" stroke="#d9e2e0" stroke-width="1"/>'
                )
                parts.append(
                    f'<text x="{px + 8:.1f}" y="59" fill="#647580" font-size="16" font-family="Avenir Next, sans-serif">{year} {label}</text>'
                )
    for channel, (label, color, lane) in CHANNELS.items():
        parts.append(
            f'<path d="M {left} {lane} H {right}" stroke="#cbd8d7" stroke-width="2"/>'
        )
        parts.append(
            f'<text x="35" y="{lane - 8}" fill="#19374a" font-size="21" font-weight="700" font-family="Avenir Next, sans-serif">{label}</text>'
        )
        parts.append(
            f'<text x="35" y="{lane + 21}" fill="#647580" font-size="16" font-family="Avenir Next, sans-serif">{counts[channel]} selected</text>'
        )
        previous = None
        collision = 0
        for source in (s for s in sources if s.category == channel):
            px = x(published_datetime(source.date))
            collision = (
                collision + 1 if previous is not None and px - previous < 19 else 0
            )
            offset = (0, -17, 17)[collision % 3]
            previous = px
            n = len(evidence[source.id])
            tooltip = escape(
                f"{source.date[:10]} · {source.title} · {n} saved evidence excerpts"
                if n
                else f"{source.date[:10]} · {source.title} · not extracted yet"
            )
            fill, outline = (color, "#fcfbf7") if n else ("#fcfbf7", color)
            parts.append(
                f'<a href="#source-{source.id}"><circle cx="{px:.1f}" cy="{lane + offset}" r="10" fill="{fill}" stroke="{outline}" stroke-width="3"><title>{tooltip}</title></circle></a>'
            )
    parts.append(
        '<text x="190" y="483" fill="#647580" font-size="15" font-family="Avenir Next, sans-serif">Publication date →   ·   positions within each channel lane are spread slightly where posts overlap</text></svg>'
    )
    return "\n".join(parts)


def evidence_item(card):
    kind = escape(KINDS.get(card["kind"], card["kind"].replace("_", " ")))
    context = escape(card["context"].replace("_", " "))
    speaker = (
        f" · diarization {escape(card['speaker_id'])} (identity unknown)"
        if card.get("speaker_id")
        else ""
    )
    return (
        '<li class="evidence-item">'
        f'<span class="evidence-kind">{kind}</span> <span class="context">{context}</span>'
        f"<p>{escape(card['statement'])}</p>"
        f"<details><summary>Exact passage · {escape(card['locator'])}{speaker}</summary>"
        f"<blockquote>{escape(card['quote'])}</blockquote><small>Evidence ID: {escape(card['id'])}</small></details></li>"
    )


def chronology_rows(sources, evidence):
    parts = []
    year = None
    for source in sources:
        current = source.date[:4]
        if current != year:
            if year is not None:
                parts.append("</div>")
            year = current
            parts.append(f'<h2 id="year-{year}">{year}</h2><div class="year-entries">')
        label, _, _ = CHANNELS[source.category]
        cards = sorted(
            evidence[source.id],
            key=lambda c: list(KINDS).index(c["kind"]) if c["kind"] in KINDS else 99,
        )
        date = escape(source.date[:10])
        time = f" · {escape(source.date[11:16])} UTC" if "T" in source.date else ""
        local = escape(
            os.path.relpath(source.path, OUT).replace(os.sep, "/"), quote=True
        )
        original = escape(source.url, quote=True)
        location = escape(
            source.path.relative_to(ROOT / "users" / "olga" / "data").as_posix()
        )
        external_label = (
            "Open original on X (may require sign-in)"
            if source.category == "twitter"
            else f"Open original on {label}"
        )
        parts.append(
            f'<article class="entry" id="source-{source.id}"><time datetime="{escape(source.date, quote=True)}">{date[5:]}{time}</time><span class="channel {source.category}">{label}</span><div class="record">'
            f'<h3>{escape(source.title)}</h3><p class="source-links"><a href="{local}">Captured source</a> · <a href="{original}" target="_blank" rel="noopener noreferrer">{external_label} ↗</a> · {location} · {escape(source.date_basis)} publication date</p>'
        )
        if cards:
            parts.append(
                f'<p class="record-count">{len(cards)} draft evidence excerpts · source-grounded, not fact-checked</p><ol class="evidence-list">'
            )
            parts.extend(evidence_item(card) for card in cards[:3])
            parts.append("</ol>")
            if len(cards) > 3:
                parts.append(
                    f'<details class="more"><summary>Show {len(cards) - 3} more extracted excerpts</summary><ol class="evidence-list">'
                )
                parts.extend(evidence_item(card) for card in cards[3:])
                parts.append("</ol></details>")
        else:
            parts.append(
                '<p class="record-count">Not extracted yet · source preview below, not an evidence claim</p>'
            )
            if source.category == "twitter":
                parts.append(
                    f'<blockquote class="source-preview">{escape(" ".join(unit["text"] for unit in source.units))}</blockquote>'
                )
        parts.append("</div></article>")
    if year is not None:
        parts.append("</div>")
    return "\n".join(parts)


TEMPLATE = """<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Olga Sinenko · Publication chronology</title>
<style>
:root{color-scheme:light;--ink:#19374a;--quiet:#566c77;--line:#d9e2e0;--paper:#fcfbf7}
*{box-sizing:border-box}body{margin:0;background:var(--paper);color:var(--ink);font:16px/1.55 "Avenir Next",Avenir,sans-serif}
main{max-width:1300px;padding:0 36px 100px;margin:auto}header{padding:70px 0 44px;display:grid;grid-template-columns:1.2fr .8fr;gap:8vw;align-items:end;border-bottom:1px solid var(--line)}
h1{font:normal clamp(3rem,6vw,6rem)/.99 Baskerville,Georgia,serif;letter-spacing:-.035em;margin:0;max-width:12ch}h1 em{font-style:italic;color:#a55b2a}
.intro{max-width:50ch;margin:0 0 5px;color:var(--quiet);font-size:1.05rem}.intro strong{color:var(--ink)}.meta{margin:0 0 14px;color:var(--quiet);font-size:.9rem}
.chart-wrap{padding:30px 0 10px;border-bottom:1px solid var(--line)}.plot{display:block;width:100%;height:auto}.plot a circle{cursor:pointer}.plot a:hover circle,.plot a:focus-visible circle{r:14;stroke-width:4}
.legend{display:flex;gap:22px;flex-wrap:wrap;align-items:center;padding:17px 0 0;color:var(--quiet);font-size:.92rem}.legend b{display:inline-block;width:10px;height:10px;border-radius:50%;margin-right:7px}.legend .yt{background:#326bb0}.legend .li{background:#22846e}.legend .x{background:#b66a28}
.kind-summary{display:flex;gap:9px;flex-wrap:wrap;padding:20px 0 6px}.kind-summary span{font-size:.9rem;border:1px solid var(--line);padding:5px 10px}.kind-summary b{color:var(--ink);font-variant-numeric:tabular-nums}.section-head{display:flex;justify-content:space-between;align-items:baseline;gap:20px;margin:55px 0 12px}.section-head h2{font:normal 2.3rem/1 Baskerville,Georgia,serif;margin:0}.section-head p{color:var(--quiet);margin:0}
h2[id^=year-]{font:normal 2rem/1.2 Baskerville,Georgia,serif;margin:44px 0 12px;border-bottom:1px solid var(--line);padding-bottom:10px}.entry{display:grid;grid-template-columns:150px 120px 1fr;gap:22px;align-items:start;border-bottom:1px solid var(--line);padding:16px 0}.entry time{font-variant-numeric:tabular-nums;color:var(--quiet);font-size:.9rem;padding-top:3px}
.channel{font-size:.875rem;font-weight:700;letter-spacing:.06em;text-transform:uppercase;padding:4px 9px;border-radius:3px;width:max-content}.channel.youtube{background:#e7f0fc;color:#245e9f}.channel.linkedin{background:#dbf2eb;color:#176f5c}.channel.twitter{background:#fbead8;color:#8a4d19}
a{color:var(--ink);text-decoration-thickness:1px;text-underline-offset:4px}a:hover{color:#a55b2a}.entry h3{font:normal 1.5rem/1.25 Baskerville,Georgia,serif;margin:0 0 7px}.source-links,.record-count{font-size:.9rem;color:var(--quiet);margin:5px 0 14px}.source-links a{font-weight:600}.evidence-list{list-style:none;padding:0;margin:0}.evidence-item{border-top:1px solid var(--line);padding:12px 0}.evidence-kind{font-size:.875rem;font-weight:700;text-transform:uppercase;letter-spacing:.045em;color:#245e9f}.context{font-size:.875rem;color:var(--quiet)}.evidence-item p{margin:5px 0;font-size:1rem;max-width:75ch}.evidence-item summary,.more summary{cursor:pointer;color:#335c70;font-size:.875rem}.evidence-item blockquote,.source-preview{margin:9px 0;padding:7px 14px;border-left:1px solid #a55b2a;color:#465d69;font-size:.95rem;max-width:80ch}.evidence-item small{font-size:.875rem;color:var(--quiet)}.more{padding:9px 0}.more>summary{font-weight:700}html{scroll-behavior:smooth}article[id]{scroll-margin-top:30px}
footer{color:var(--quiet);font-size:.9rem;border-top:1px solid var(--line);margin-top:55px;padding-top:22px;max-width:85ch}
:focus-visible{outline:3px solid #a55b2a;outline-offset:4px}@media(max-width:720px){main{padding:0 18px 70px}header{display:block;padding:43px 0 28px}h1{margin-bottom:23px}.chart-wrap{overflow-x:auto}.plot{min-width:720px}.entry{grid-template-columns:92px 1fr;gap:9px 15px}.entry>div{grid-column:2}.entry time{font-size:.875rem}.channel{font-size:.875rem}.section-head{display:block}.section-head p{margin-top:9px}}
@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}}
</style></head><body><main>
<header><h1>Evidence through <em>time.</em></h1><div><p class="intro"><strong>Olga Sinenko’s public sources</strong>, organized by publication date. Follow each mark to extracted claims, teaching methods, observed behavior and the exact source passage. A publication date does not date an event described in a post.</p><p class="meta">__EVIDENCE__ draft excerpts from __COVERED__ of __COUNT__ selected sources · __RANGE__ · __GENERATED__ UTC</p></div></header>
<section class="chart-wrap" aria-label="Publication chart">__CHART__<div class="legend"><span><b class="yt"></b>YouTube (__YT__)</span><span><b class="li"></b>LinkedIn (__LI__)</span><span><b class="x"></b>X (__X__)</span><span>Filled = extracted · hollow = awaiting extraction</span></div><div class="kind-summary" aria-label="Saved evidence by type">__KINDS__</div></section>
<section aria-label="Dated extracted evidence"><div class="section-head"><h2>Read the evidence</h2><p>Oldest → newest · chart dots jump to their passages</p></div>__ROWS__</section>
<footer>This is a <strong>curated pilot sample</strong>, not a complete posting history or a measure of posting frequency. __OMITTED____PENDING__ displayed sources have not yet been extracted. Evidence shown here is a machine-extracted research draft from an earlier pilot, joined to publication metadata; its claims are not externally verified and some speakers in videos are unidentified. YouTube dates came from individual video metadata; LinkedIn and X dates came from exported posts. Event dates are not inferred. X can require sign-in, so its captured text remains visible here.</footer>
</main></body></html>"""


def main():
    sources, omitted = selected_sources()
    if not sources:
        raise ValueError("No sources with verified publication metadata")
    counts = Counter(s.category for s in sources)
    evidence = evidence_for(sources)
    kinds = Counter(card["kind"] for cards in evidence.values() for card in cards)
    covered = sum(bool(cards) for cards in evidence.values())
    assert len(sources) == sum(counts.values()) and all(
        s.url.startswith("https://") for s in sources
    )
    visual = chart(sources, evidence)
    html = TEMPLATE
    for key, value in {
        "__COUNT__": str(len(sources)),
        "__EVIDENCE__": str(sum(kinds.values())),
        "__COVERED__": str(covered),
        "__PENDING__": str(len(sources) - covered),
        "__OMITTED__": f"{len(omitted)} selected YouTube transcripts are temporarily omitted because their current video identity/date is unverified after a concurrent relabel. "
        if omitted
        else "",
        "__KINDS__": "".join(
            f"<span><b>{kinds[kind]}</b> {escape(KINDS[kind])}</span>"
            for kind in KINDS
            if kinds[kind]
        ),
        "__RANGE__": f"{sources[0].date[:7]}–{sources[-1].date[:7]}",
        "__GENERATED__": datetime.now(UTC).strftime("%Y-%m-%d"),
        "__YT__": str(counts["youtube"]),
        "__LI__": str(counts["linkedin"]),
        "__X__": str(counts["twitter"]),
        "__CHART__": visual,
        "__ROWS__": chronology_rows(sources, evidence),
    }.items():
        html = html.replace(key, value)
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "chronology.html").write_text(html, encoding="utf-8")
    (OUT / "chronology.svg").write_text(
        re.sub(r"</?a\b[^>]*>", "", visual), encoding="utf-8"
    )
    print(f"Wrote {OUT / 'chronology.html'} and chronology.svg ({dict(counts)})")


if __name__ == "__main__":
    main()
