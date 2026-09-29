"""Offline, bounded, task-conditioned selection from the three information products."""

import re
from collections import deque
from datetime import date
from pathlib import Path

from .core import active_records
from .records import PRODUCTS, attributed_to, grounded_fields, original_context, plain
from .storage import js

STOPWORDS = {
    "a",
    "an",
    "the",
    "is",
    "are",
    "was",
    "were",
    "do",
    "does",
    "how",
    "what",
    "why",
    "when",
    "where",
    "who",
    "which",
    "to",
    "of",
    "for",
    "in",
    "on",
    "and",
    "or",
    "with",
    "about",
    "me",
    "my",
    "your",
    "their",
    "this",
    "that",
    "please",
}


def words(value):
    return set(re.findall(r"\w+", value.casefold())) - STOPWORDS


def select_context(
    workspace: Path,
    source_dir: Path,
    query: str,
    *,
    authors=None,
    platform=None,
    max_records=8,
    max_chars=24000,
    as_of=None,
    reviewed_only=False,
) -> dict:
    if (
        not isinstance(query, str)
        or not query.strip()
        or max_records < 1
        or max_chars < 1000
    ):
        raise ValueError(
            "Supply a question, positive record limit and >=1000-character context budget"
        )
    if as_of:
        as_of = date.fromisoformat(as_of).isoformat()
    aliases = {plain(a).casefold().removeprefix("@") for a in authors or []}
    records, sources = active_records(workspace, source_dir)
    tokens = words(query)
    queues = {}
    for product in PRODUCTS:
        ranked = []
        for record in records:
            if record["product"] != product:
                continue
            if platform and record["category"] != platform:
                continue
            if reviewed_only and record["semantic_status"] != "human_supported":
                continue
            if as_of and (
                not record["published_at"] or record["published_at"][:10] > as_of
            ):
                continue  # Unknown publication dates cannot establish availability before a date.
            if (
                aliases
                and product != "knowledge"
                and not attributed_to(record, sources[record["source_id"]], aliases)
            ):
                continue
            content = " ".join(
                f["text"] for f in grounded_fields(record["content"]).values()
            )
            score = len(tokens & words(content)) + 2 * len(
                tokens & words(record["title"] + " " + record["topic"])
            )
            if score:
                ranked.append(
                    (score, record["published_at"] or "", record["id"], record)
                )
        queues[product] = deque(
            r[-1] for r in sorted(ranked, key=lambda r: r[:3], reverse=True)
        )
    result = {
        "query": query,
        "platform": platform,
        "as_of_publication": as_of,
        "knowledge": [],
        "cases": [],
        "expression": [],
        "budget_omitted": 0,
        "selection": "Lexical relevance, recency tie-break and product diversity; not semantic retrieval",
        "instructions": [
            "Use cited knowledge and complete method steps, not generic persona assumptions.",
            "Reported/illustrative cases are not recorded behavior; unknown rationale/outcome stays unknown.",
            "Authorship is not the speaker identity of embedded quotations.",
            "No match means insufficient retrieved evidence, not proof that the corpus contains no answer.",
        ],
        "abstain": True,
    }
    count, seen = 0, set()
    while count < max_records and any(queues.values()):
        for product in PRODUCTS:
            if not queues[product] or count >= max_records:
                continue
            record = queues[product].popleft()
            family = (product, record["content_hash"])
            if family in seen:
                continue
            source = sources[record["source_id"]]
            entry = {
                "record": record,
                "original_context": original_context(record, source),
                "target_attribution": attributed_to(record, source, aliases)
                if aliases
                else None,
            }
            result[product].append(entry)
            if len(js(result)) > max_chars:
                result[product].pop()
                result["budget_omitted"] += 1
                continue
            seen.add(family)
            count += 1
    result["abstain"] = count == 0
    while len(js(result)) > max_chars and count:
        product = next(p for p in reversed(PRODUCTS) if result[p])
        result[product].pop()
        result["budget_omitted"] += 1
        count -= 1
        result["abstain"] = count == 0
    if len(js(result)) > max_chars:
        raise ValueError("Question and context metadata exceed --max-chars")
    return result
