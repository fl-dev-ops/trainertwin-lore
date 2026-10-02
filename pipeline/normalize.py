"""Normalize extracted tags into canonical clusters and aliases using TypeSafe Jev."""

from __future__ import annotations

import os
import re
import sys
import time
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import Any

import httpx

from .storage import atomic, js, load_json

BASE_STOPWORDS = {
    # Functional English words
    "and", "or", "the", "in", "of", "for", "to", "a", "an", "by", "on", "with", "at", "is", "from",
    "how", "what", "why", "vs", "versus", "about", "into", "over", "after", "before",
    # Generic format / meta words that don't distinguish concepts
    "guide", "tutorial", "tips", "basics", "fundamentals", "overview", "introduction",
    "question", "questions", "concept", "concepts",
}


def slugify(text: str) -> str:
    cleaned = re.sub(r"[^a-z0-9]+", "-", text.lower().strip()).strip("-")
    return cleaned[:60] or "unnamed"


STOPWORD_SCHEMA = {
    "type": "object",
    "additionalProperties": False,
    "properties": {
        "domain_words": {
            "type": "array",
            "items": {"type": "string"},
        }
    },
    "required": ["domain_words"],
}

STOPWORD_PROMPT = """You are analyzing metadata tags extracted from an educational content creator.
Identify 3 to 8 ubiquitous domain background words.
A domain background word represents the overarching profession, industry, or format (e.g. "sales", "real-estate", "javascript", "frontend", "interview", "supply-chain").
These words appear everywhere across this creator's catalog and do NOT help distinguish one specific lesson/topic from another.

Do NOT include specific technical topics, skills, or methodologies (e.g. "closures", "debouncing", "cold-calling", "negotiation", "resumes" are NOT background words).

Return JSON: {"domain_words": ["word1", "word2", ...]}"""


def detect_domain_stopwords_llm(
    items: list[dict], api_key: str, model: str = "google/gemini-3.8-flash"
) -> set[str]:
    """Ask an LLM to identify ubiquitous macro-domain words from top tags."""
    from .client import OpenRouter

    tag_counts: Counter[str] = Counter()
    for it in items:
        for t in it.get("tags", []):
            label = t.get("label", "").strip()
            if label:
                tag_counts[label] += 1

    if not tag_counts:
        return set()

    top_tags = [f"- {l} ({c}x)" for l, c in tag_counts.most_common(40)]
    user_prompt = "Top tags in creator catalog:\n" + "\n".join(top_tags)

    client = OpenRouter(api_key, model)
    client.max_output_tokens = 2048
    try:
        raw = client.complete("detect_domain_stopwords", STOPWORD_SCHEMA, STOPWORD_PROMPT, user_prompt)
        words = raw.get("domain_words") or []
        tokens = set()
        for w in words:
            for sub in re.findall(r"[a-z0-9]+", w.lower()):
                if len(sub) > 2 and sub not in BASE_STOPWORDS:
                    tokens.add(sub)
        return tokens
    except Exception as exc:
        print(f"Warning: LLM domain stopword detection failed ({exc}); falling back to heuristic", file=sys.stderr, flush=True)
        return detect_domain_stopwords(items)
    finally:
        client.close()


def detect_domain_stopwords(items: list[dict], threshold: float = 0.08) -> set[str]:
    """Find words that appear across >8% of all tags in this persona's corpus."""
    total_tags = 0
    counts: Counter[str] = Counter()
    for it in items:
        for t in it.get("tags", []):
            label = t.get("label", "")
            if not label:
                continue
            total_tags += 1
            words = set(re.findall(r"[a-z0-9]+", label.lower()))
            for w in words:
                if len(w) > 2 and w not in BASE_STOPWORDS:
                    counts[w] += 1
    if total_tags == 0:
        return set()
    return {w for w, c in counts.items() if c / total_tags >= threshold}


def tokenize(s: str, stopwords: set[str] | None = None) -> set[str]:
    cleaned = re.sub(r"[\-_/]+", " ", s.lower())
    words = re.findall(r"[a-z0-9]+", cleaned)
    sw = stopwords if stopwords is not None else BASE_STOPWORDS
    return {w for w in words if w not in sw and len(w) > 2}


def canonical_stem(s: str) -> str:
    """Deterministic basic normalization: case, whitespace, hyphens, and simple plurals."""
    cleaned = re.sub(r"[\-_/]+", " ", s.lower()).strip()
    words = cleaned.split()
    norm = []
    for w in words:
        if w.endswith("ies") and len(w) > 4:
            norm.append(w[:-3] + "y")
        elif w.endswith("es") and len(w) > 4 and not w.endswith("ss"):
            norm.append(w[:-2])
        elif w.endswith("s") and len(w) > 3 and not w.endswith("ss"):
            norm.append(w[:-1])
        else:
            norm.append(w)
    return " ".join(norm)


class JevClient:
    def __init__(self, api_key: str):
        if not api_key:
            raise ValueError("OPENROUTER_API_KEY is required for Jev normalization")
        self.http = httpx.Client(
            headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
            timeout=httpx.Timeout(40.0, connect=10.0),
        )

    def close(self):
        self.http.close()

    def decide(self, state: str, questions: dict[str, dict[str, Any]]) -> dict[str, Any]:
        """Send questions to Jev and return dict of question_id -> answer object."""
        if not questions:
            return {}
        for attempt in range(3):
            try:
                resp = self.http.post(
                    "https://openrouter.ai/api/alpha/decisions",
                    json={"model": "typesafe/jev-1.13", "state": state, "questions": questions},
                )
                if resp.status_code in (429, 500, 502, 503, 504):
                    time.sleep(2**attempt)
                    continue
                resp.raise_for_status()
                return resp.json().get("answers", {})
            except (httpx.TimeoutException, httpx.NetworkError):
                if attempt == 2:
                    raise
                time.sleep(2**attempt)
        return {}


def cluster_facet(
    facet: str,
    label_counts: Counter,
    jev: JevClient,
    *,
    threshold: float = 0.70,
    batch_size: int = 25,
    workers: int = 8,
    max_candidates_per_label: int = 3,
    stopwords: set[str] | None = None,
) -> list[dict[str, Any]]:
    """Cluster raw labels for one facet into canonical concepts with aliases."""
    # 1. Deterministic stem grouping first (0 API calls)
    stemmed_map: dict[str, list[tuple[str, int]]] = {}
    for label, count in label_counts.items():
        key = canonical_stem(label)
        stemmed_map.setdefault(key, []).append((label, count))

    # Pick the most frequent original casing as the display label for each stem group
    deduped: list[tuple[str, int, list[str]]] = []
    for key, variants in stemmed_map.items():
        variants.sort(key=lambda x: x[1], reverse=True)
        canonical_label = variants[0][0]
        total_count = sum(c for _, c in variants)
        all_aliases = list({v[0] for v in variants})
        deduped.append((canonical_label, total_count, all_aliases))

    # Sort candidates by frequency descending
    deduped.sort(key=lambda x: x[1], reverse=True)

    clusters: list[dict[str, Any]] = []
    pairs_to_evaluate: list[dict[str, Any]] = []

    # 2. Build candidate pairs
    for label_idx, (label, count, aliases) in enumerate(deduped):
        label_tokens = tokenize(label, stopwords=stopwords)
        candidates = []

        if label_tokens or facet == "situation":
            for c_idx, c in enumerate(clusters):
                shared = label_tokens & c["tokens"]
                is_candidate = (
                    len(shared) >= 2
                    or (len(shared) == 1 and (len(label_tokens) <= 2 or len(c["tokens"]) <= 2))
                    or (facet == "situation" and c_idx < 5 and label_idx < 50)
                )
                if is_candidate:
                    candidates.append(c_idx)
                    if len(candidates) >= max_candidates_per_label:
                        break

        for c_idx in candidates:
            pairs_to_evaluate.append({
                "label_idx": label_idx,
                "label": label,
                "count": count,
                "aliases": aliases,
                "tokens": label_tokens,
                "target_idx": c_idx,
                "target_preferred": clusters[c_idx]["preferred"],
            })

        # Pre-seed as initial cluster placeholder
        clusters.append({
            "id": slugify(label),
            "preferred": label,
            "aliases": sorted(aliases),
            "tokens": label_tokens,
            "count": count,
            "merged": False,
        })

    # If no pairs to evaluate with Jev, return clusters directly
    if not pairs_to_evaluate:
        for c in clusters:
            c.pop("tokens", None)
            c.pop("merged", None)
            c["aliases"].sort()
        return clusters

    # 3. Pack candidate pairs into batches of 25
    batches: list[tuple[list[dict[str, Any]], dict[str, dict[str, Any]]]] = []
    for i in range(0, len(pairs_to_evaluate), batch_size):
        chunk = pairs_to_evaluate[i : i + batch_size]
        questions = {
            f"p_{j}": {
                "type": "noul",
                "instructions": (
                    f"In the context of {facet}s, are \"{item['label']}\" and \"{item['target_preferred']}\" "
                    f"close synonyms describing the exact same {facet}?"
                ),
            }
            for j, item in enumerate(chunk)
        }
        batches.append((chunk, questions))

    # 4. Run batches in parallel using ThreadPoolExecutor
    def process_batch(batch_item):
        chunk, questions = batch_item
        scores = jev.decide(f"Matching {facet} synonyms", questions)
        results = []
        for j, item in enumerate(chunk):
            score = scores.get(f"p_{j}", {}).get("noul", 0.0)
            results.append((item, score))
        return results

    evaluations: list[tuple[dict[str, Any], float]] = []
    with ThreadPoolExecutor(max_workers=workers) as pool:
        for batch_res in pool.map(process_batch, batches):
            evaluations.extend(batch_res)

    # 5. Group best match per label
    best_matches: dict[int, tuple[int, float, dict[str, Any]]] = {}
    for item, score in evaluations:
        l_idx = item["label_idx"]
        t_idx = item["target_idx"]
        if score >= threshold:
            if l_idx not in best_matches or score > best_matches[l_idx][1]:
                best_matches[l_idx] = (t_idx, score, item)

    # 6. Apply merges
    final_clusters: list[dict[str, Any]] = []
    merged_indices = set()

    for l_idx, (t_idx, score, item) in best_matches.items():
        # Find root target cluster
        root_idx = t_idx
        target = clusters[root_idx]
        while target.get("merged_into") is not None:
            root_idx = target["merged_into"]
            target = clusters[root_idx]

        if root_idx != l_idx:
            for a in item["aliases"]:
                if a not in target["aliases"]:
                    target["aliases"].append(a)
            target["count"] += item["count"]
            target["tokens"] |= item["tokens"]
            clusters[l_idx]["merged"] = True
            clusters[l_idx]["merged_into"] = root_idx
            merged_indices.add(l_idx)

    for idx, c in enumerate(clusters):
        if idx not in merged_indices:
            c.pop("tokens", None)
            c.pop("merged", None)
            c.pop("merged_into", None)
            c["aliases"].sort()
            final_clusters.append(c)

    final_clusters.sort(key=lambda c: c["count"], reverse=True)
    return final_clusters


def normalize_workspace(
    workspace: Path,
    api_key: str,
    *,
    model: str = "google/gemini-3.8-flash",
    threshold: float = 0.70,
    workers: int = 8,
) -> dict[str, Any]:
    """Build taxonomy.json for all facets in a workspace."""
    index_path = workspace / "index.json"
    if not index_path.exists():
        raise FileNotFoundError(f"Missing {index_path}. Run index first.")

    data = load_json(index_path)
    items = data.get("items", [])

    by_facet: dict[str, Counter] = {}
    for item in items:
        for tag in item.get("tags", []):
            facet = tag.get("facet", "topic")
            label = tag.get("label", "").strip()
            if facet and label:
                by_facet.setdefault(facet, Counter())[label] += 1

    # 1. Dynamically identify domain background stopwords using LLM
    domain_sw = detect_domain_stopwords_llm(items, api_key, model=model)
    effective_stopwords = BASE_STOPWORDS | domain_sw
    if domain_sw:
        print(f"LLM-identified creator domain background words: {sorted(domain_sw)}", file=sys.stderr, flush=True)

    jev = JevClient(api_key)
    taxonomy: dict[str, Any] = {}

    try:
        for facet, counts in sorted(by_facet.items()):
            t0 = time.time()
            print(f"Normalizing '{facet}' ({len(counts)} raw labels)...", file=sys.stderr, flush=True)
            clusters = cluster_facet(
                facet, counts, jev, threshold=threshold, workers=workers, stopwords=effective_stopwords
            )
            taxonomy[facet] = {c["id"]: c for c in clusters}
            merged_count = len(counts) - len(clusters)
            dt = time.time() - t0
            print(f"  → {len(clusters)} canonical concepts ({merged_count} synonyms merged) in {dt:.2f}s", file=sys.stderr, flush=True)
    finally:
        jev.close()

    out_path = workspace / "taxonomy.json"
    atomic(out_path, js(taxonomy))
    print(f"Taxonomy saved to {out_path}", file=sys.stderr, flush=True)
    return taxonomy
