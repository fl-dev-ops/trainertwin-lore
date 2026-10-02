"""Retrieve grounded source clips for a target scenario using Jev and taxonomy expansion."""

from __future__ import annotations

import os
import re
from pathlib import Path
from typing import Any

import httpx

from .normalize import JevClient, slugify
from .storage import load_json


def extract_keywords(text: str) -> set[str]:
    stopwords = {
        "and", "or", "the", "in", "of", "for", "to", "a", "an", "by", "on", "with", "at", "is", "from",
        "how", "what", "why", "does", "she", "he", "they", "who", "when", "where", "can", "should", "would",
        "about", "into", "over", "after", "before", "i", "you", "my", "your"
    }
    words = re.findall(r"[a-z0-9]+", text.lower())
    return {w for w in words if w not in stopwords and len(w) > 2}


def route_query_with_jev(
    query: str,
    taxonomy: dict[str, Any],
    jev: JevClient,
    *,
    max_criteria: int = 60,
) -> tuple[str | None, list[str], float]:
    """Use Jev to match a query to the best canonical concept in taxonomy.json."""
    query_tokens = extract_keywords(query)
    candidates: dict[str, str] = {}

    # Score taxonomy concepts by token overlap with query
    scored_concepts: list[tuple[int, str, dict[str, Any]]] = []
    for facet in ("situation", "topic", "activity"):
        for cid, c in taxonomy.get(facet, {}).items():
            c_text = (c.get("preferred", "") + " " + " ".join(c.get("aliases", []))).lower()
            c_tokens = extract_keywords(c_text)
            overlap = len(query_tokens & c_tokens)
            scored_concepts.append((overlap, cid, c))

    scored_concepts.sort(key=lambda x: x[0], reverse=True)

    # Take top candidate concepts
    for _, cid, c in scored_concepts[:max_criteria]:
        desc = c["preferred"]
        aliases = c.get("aliases", [])
        if aliases:
            desc += f" (e.g. {', '.join(aliases[:2])})"
        candidates[cid] = desc[:120]

    candidates["other"] = "None of the above"

    try:
        resp = jev.decide(
            f"Target Scenario Query: \"{query}\"",
            {
                "matched_concept": {
                    "type": "choice",
                    "instructions": "Which canonical concept best matches the situation or question in this scenario?",
                    "criteria": candidates,
                }
            },
        )
        ans = resp.get("matched_concept", {})
        choice = ans.get("choice")
        confidence = ans.get("confidence", 0.0)

        if choice and choice != "other" and confidence >= 0.40:
            # Find the concept object across facets
            for facet in ("situation", "topic", "activity"):
                if choice in taxonomy.get(facet, {}):
                    c = taxonomy[facet][choice]
                    aliases = list({c["preferred"].lower()} | {a.lower() for a in c.get("aliases", [])})
                    return choice, aliases, confidence
    except Exception as exc:
        print(f"Warning: Jev query routing failed ({exc}); falling back to keyword search", flush=True)

    return None, [], 0.0


def score_and_select_items(
    items: list[dict[str, Any]],
    query: str,
    target_aliases: list[str],
    *,
    max_clips: int = 5,
    max_per_file: int = 2,
) -> list[dict[str, Any]]:
    """Score items by concept match + lexical match, and enforce set-diversity."""
    query_tokens = extract_keywords(query)
    target_alias_set = set(target_aliases)

    scored: list[tuple[float, dict[str, Any]]] = []

    for it in items:
        score = 0.0
        # 1. Concept match via tag labels
        item_tag_labels = [t.get("label", "").lower() for t in it.get("tags", [])]
        matched_tags = target_alias_set & set(item_tag_labels)
        if matched_tags:
            score += 10.0 * len(matched_tags)

        # 2. Lexical keyword match on title & quote
        it_tokens = extract_keywords(it.get("title", "") + " " + it.get("quote", ""))
        overlap = query_tokens & it_tokens
        score += 1.0 * len(overlap)

        if score > 0.0:
            scored.append((score, it))

    # Sort by score descending
    scored.sort(key=lambda x: x[0], reverse=True)

    # 3. Set-Utility diversification: max_per_file limit
    selected: list[dict[str, Any]] = []
    file_counts: dict[str, int] = {}

    for score, it in scored:
        path = it.get("path", "")
        if file_counts.get(path, 0) < max_per_file:
            file_counts[path] = file_counts.get(path, 0) + 1
            selected.append({**it, "retrieval_score": round(score, 2)})

        if len(selected) >= max_clips:
            break

    return selected


def slice_verbatim_text(data_dir: Path, item: dict[str, Any]) -> str:
    """Read verbatim lines directly from the raw source file on disk."""
    path = data_dir / item["path"]
    if not path.is_file():
        return item.get("quote", "")

    lines = path.read_text(encoding="utf-8").splitlines()
    start = item["span"]["start_line"]
    end = item["span"]["end_line"]

    selected_lines = lines[start - 1 : end]
    # Clean speaker headers and empty lines
    cleaned = [
        l.strip() for l in selected_lines
        if l.strip() and not l.strip().startswith("###") and not l.strip().startswith("---")
    ]
    return " ".join(cleaned)


def retrieve(
    workspace: Path,
    data_dir: Path,
    query: str,
    api_key: str,
    *,
    max_clips: int = 5,
) -> dict[str, Any]:
    """Retrieve grounded clips for a query using Jev + Taxonomy + Source files."""
    index_path = workspace / "index.json"
    taxonomy_path = workspace / "taxonomy.json"

    if not index_path.exists():
        raise FileNotFoundError(f"Missing {index_path}. Run index first.")
    if not taxonomy_path.exists():
        raise FileNotFoundError(f"Missing {taxonomy_path}. Run normalize first.")

    index_data = load_json(index_path)
    taxonomy = load_json(taxonomy_path)
    items = index_data.get("items", [])

    jev = JevClient(api_key)
    try:
        concept_id, aliases, confidence = route_query_with_jev(query, taxonomy, jev)
    finally:
        jev.close()

    selected_items = score_and_select_items(items, query, aliases, max_clips=max_clips)

    clips = []
    for it in selected_items:
        verbatim = slice_verbatim_text(data_dir, it)
        clips.append({
            "item_id": it.get("item_id"),
            "path": it.get("path"),
            "span": it.get("span"),
            "title": it.get("title"),
            "tags": it.get("tags"),
            "prev": it.get("prev"),
            "next": it.get("next"),
            "retrieval_score": it.get("retrieval_score"),
            "verbatim_text": verbatim,
        })

    return {
        "query": query,
        "matched_concept": concept_id,
        "concept_confidence": round(confidence, 2),
        "aliases_used": aliases,
        "clips": clips,
    }
