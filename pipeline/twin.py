"""Attributed cases/expression -> observations and separately proposed adaptations."""

from collections import Counter, defaultdict, deque
from pathlib import Path

from . import prompts
from .core import active_records, artifact_inputs, escaped, link
from .records import (
    array,
    attributed_to,
    enum,
    nullable,
    obj,
    original_context,
    plain,
    quote_in_text,
    text,
    validate_schema,
)
from .storage import (
    Model,
    cached_call,
    check_artifacts,
    digest,
    js,
    json_lines,
    jsonl,
    load_json,
    partition,
    publish,
)

PATTERN_SCHEMA = obj(
    {
        "patterns": array(
            obj(
                {
                    "dimension": enum(
                        ("expression", "teaching_strategy", "interaction")
                    ),
                    "scope": text(
                        "Exact supporting platform, or general with cross-platform support",
                        60,
                    ),
                    "situation": text(
                        "Observed context, not an invented use case", 500
                    ),
                    "observation": text(
                        "Concrete source-supported form/sequence, not a topic summary or effectiveness claim",
                        1500,
                    ),
                    "support_ids": array(text("Exact example ID", 80), 16, 1),
                    "counter_ids": array(text("Exact contrary example ID", 80), 16),
                    "citations": array(
                        obj(
                            {
                                "example_id": text("Supporting example ID", 80),
                                "unit_id": text("Exact original unit ID", 200),
                                "quote": text("Exact original excerpt", 800),
                            }
                        ),
                        24,
                        1,
                    ),
                    "qualification": text(
                        "Actual evidential limits, not invented explanations", 1200
                    ),
                    "proposed_adaptation": nullable(
                        obj(
                            {
                                "when": text("Proposed application context", 500),
                                "action": text(
                                    "Conditional reuse of the observed form or documented teaching strategy",
                                    1000,
                                ),
                                "limits": text(
                                    "Where NOT to generalize; no claimed effectiveness",
                                    800,
                                ),
                            }
                        )
                    ),
                }
            ),
            12,
        )
    }
)


def alias(value: str) -> str:
    return plain(value).casefold().removeprefix("@")


def prepare_examples(records, sources, authors, max_sources=12, *, reviewed_only=False):
    if not authors or any(not isinstance(a, str) or not alias(a) for a in authors):
        raise ValueError(
            "Supply explicit --author aliases; identities are never guessed"
        )
    if max_sources < 1:
        raise ValueError("--max-sources must be positive")
    aliases = {alias(a) for a in authors}
    groups, excluded = defaultdict(list), Counter()
    for record in records:
        if record["product"] not in {"cases", "expression"}:
            continue
        if record["semantic_status"] == "human_unsupported":
            excluded["human_rejected"] += 1
            continue
        if reviewed_only and record["semantic_status"] != "human_supported":
            excluded["not_human_reviewed"] += 1
            continue
        source = sources[record["source_id"]]
        if source.format == "role_play":
            excluded["role_play"] += 1
            continue
        if not attributed_to(record, source, aliases):
            excluded["attribution_unknown_or_other"] += 1
            continue
        context = original_context(record, source)
        example = {
            "id": "ex-" + digest(record["id"])[:16],
            "record_id": record["id"],
            "source_id": source.id,
            "channel": source.category,
            "published_at": source.date or None,
            "format": source.format,
            "author": source.author or None,
            "content_hash": source.content_hash,
            "product": record["product"],
            "record": record["content"],
            "semantic_status": record["semantic_status"],
            "original_context": context,
        }
        groups[source.id].append(example)
    # Preserve every eligible case/expression from selected publications, not one
    # arbitrarily chosen card. Repeated publications do not multiply support.
    unique = {}
    for ident in sorted(groups, key=lambda i: (sources[i].date, i), reverse=True):
        unique.setdefault(sources[ident].content_hash, ident)
    queues = defaultdict(deque)
    for ident in sorted(unique.values(), key=lambda i: (sources[i].date, i)):
        queues[sources[ident].category].append(ident)
    selected, newest = [], False
    while len(selected) < max_sources and any(queues.values()):
        for channel in sorted(queues):
            if queues[channel] and len(selected) < max_sources:
                selected.append(
                    queues[channel].pop() if newest else queues[channel].popleft()
                )
        newest = not newest
    examples = [e for ident in selected for e in groups[ident]]
    coverage = {
        "active_sources": len(sources),
        "active_records": len(records),
        "eligible_sources": len(groups),
        "selected_sources": len(selected),
        "selected_examples": len(examples),
        "selected_by_channel": dict(Counter(sources[i].category for i in selected)),
        "selected_dates": sorted(
            {sources[i].date for i in selected if sources[i].date}
        ),
        "duplicate_publications_omitted": len(groups) - len(unique),
        "source_limit_omitted": len(unique) - len(selected),
        "excluded_records": dict(excluded),
        "policy": "All eligible case/expression records from date/channel-balanced, content-deduplicated publications",
        "warning": "Counts describe selected evidence, not persona confidence or extraction recall",
    }
    return examples, coverage


def validate_patterns(result, examples):
    validate_schema(result, PATTERN_SCHEMA)
    for pattern in result["patterns"]:
        for key in ("support_ids", "counter_ids"):
            ids = pattern[key]
            if len(ids) != len(set(ids)) or any(i not in examples for i in ids):
                raise ValueError("Unknown or duplicate twin example ID")
        support = [examples[i] for i in pattern["support_ids"]]
        channels = {e["channel"] for e in support}
        if pattern["scope"] == "general":
            if len(channels) == 1:
                # The exact narrower scope is derivable; never spend a repair call
                # or publish an overbroad claim for this model classification slip.
                pattern["scope"] = next(iter(channels))
            elif len({e["content_hash"] for e in support}) < 2:
                raise ValueError(
                    "General observations need distinct content from multiple platforms"
                )
        elif channels != {pattern["scope"]}:
            raise ValueError(
                "Observation scope does not match its supporting platforms"
            )
        if pattern["dimension"] == "interaction" and not all(
            e["product"] == "cases" and e["record"]["kind"] == "recorded_exchange"
            for e in support
        ):
            if all(e["product"] == "expression" for e in support):
                pattern["dimension"] = "expression"
            elif all(
                e["product"] == "cases" and e["record"]["strategy"] for e in support
            ):
                pattern["dimension"] = "teaching_strategy"
            else:
                raise ValueError(
                    "Interaction observations require recorded exchanges, not narrated or illustrative cases"
                )
        if pattern["dimension"] == "teaching_strategy" and not all(
            e["product"] == "cases" and e["record"]["strategy"] for e in support
        ):
            if all(e["product"] == "expression" for e in support):
                pattern["dimension"] = "expression"
            else:
                raise ValueError(
                    "Teaching-strategy observations need source-cited case strategies"
                )
        covered = set()
        for citation in pattern["citations"]:
            ident = citation["example_id"]
            if ident not in pattern["support_ids"] + pattern["counter_ids"]:
                raise ValueError(
                    "Citation is not attached to a declared support/counterexample"
                )
            example = examples[ident]
            units = {
                u["id"]: u for p in example["original_context"] for u in p["units"]
            }
            unit = units.get(citation["unit_id"])
            quote = plain(citation["quote"])
            if not unit or not quote_in_text(quote, unit["text"]):
                matches = [u for u in units.values() if quote_in_text(quote, u["text"])]
                if len(matches) == 1:
                    unit = matches[0]
                    citation["unit_id"] = unit["id"]
                else:
                    raise ValueError(
                        "Twin observation contains an unsupported quotation"
                    )
            if len(quote) < min(12, len(unit["text"])):
                raise ValueError("Twin observation contains an unsupported quotation")
            covered.add(ident)
        if not set(pattern["support_ids"] + pattern["counter_ids"]).issubset(covered):
            raise ValueError("Every support/counterexample needs an original quotation")
    return result["patterns"]


def render_profile(patterns, examples, coverage, workspace):
    page = workspace / "twin/profile.md"
    by_id = {e["id"]: e for e in examples}
    lines = [
        "# TrainerTwin specification",
        "",
        "> Source-supported candidates for human review, not a verified personality or proof of effectiveness.",
        "",
        "## Evidence coverage",
        "",
        "```json",
        js(coverage).strip(),
        "```",
        "",
        "## Boundaries",
        "",
        "- Knowledge/methods belong in the wiki; use original cases to understand their application.",
        "- Authored narration and recorded interaction are different evidence. Unknown motives/outcomes stay unknown.",
        "- Observations describe sources. Adaptations below are proposals, not facts about what the trainer always does.",
        "- Select for the current learner situation; do not force platform marketing or catchphrases into every reply.",
        "",
    ]
    if not patterns:
        lines += [
            "No supported patterns produced. Check source coverage and attribution; do not invent a persona.",
            "",
        ]
    for n, pattern in enumerate(patterns, 1):
        lines += [
            f"## {n}. Source observation",
            "",
            escaped(pattern["observation"]),
            "",
            f"**Dimension:** {pattern['dimension']} · **Scope:** {escaped(pattern['scope'])} · **Review:** unreviewed",
            f"**Situation:** {escaped(pattern['situation'])}",
            f"**Qualification:** {escaped(pattern['qualification'])}",
            "",
        ]
        for citation in pattern["citations"]:
            example = by_id[citation["example_id"]]
            lines.append(
                f"- “{escaped(citation['quote'])}” — [{citation['example_id']}]({link(workspace / 'wiki/sources' / (example['source_id'] + '.md'), page)}) (`{citation['unit_id']}`)"
            )
        adaptation = pattern["proposed_adaptation"]
        lines += ["", "### Proposed adaptation — not observed behavior", ""]
        if adaptation:
            lines += [
                f"**When:** {escaped(adaptation['when'])}",
                f"**Consider:** {escaped(adaptation['action'])}",
                f"**Limits:** {escaped(adaptation['limits'])}",
                "",
            ]
        else:
            lines += ["No adaptation proposed from this evidence.", ""]
    lines += ["## Original context examples", ""]
    for example in examples:
        lines += [
            f"### {example['id']}",
            "",
            f"Product: {example['product']} · Format: {example['format']} · Source support: {example['semantic_status']}",
            "",
        ]
        for passage in example["original_context"]:
            who = (
                passage["speaker_name"] or "unknown speaker"
                if passage["representation"] == "spoken_turn"
                else "author: " + (passage["author"] or "unknown")
            )
            lines += [
                f"**{escaped(who)}** · {escaped(passage['locator'])}",
                escaped(passage["attribution_note"]),
                "",
                "\n".join(
                    "> " + escaped(line) for line in passage["text"].splitlines()
                ),
                "",
            ]
    return "\n".join(lines).rstrip() + "\n"


def twin_inputs(workspace, source_dir, config):
    return {
        **artifact_inputs(workspace, source_dir),
        "config": config,
        "specification": digest([prompts.TWIN, PATTERN_SCHEMA]),
    }


def build_twin(
    workspace: Path,
    source_dir: Path,
    model: Model,
    *,
    authors: list[str],
    budget: list[int],
    max_sources=12,
    max_chars=24000,
    reviewed_only=False,
) -> Path:
    check_artifacts(workspace / "wiki", artifact_inputs(workspace, source_dir))
    records, sources = active_records(workspace, source_dir)
    examples, coverage = prepare_examples(
        records, sources, authors, max_sources, reviewed_only=reviewed_only
    )
    config = {
        "authors": sorted({alias(a) for a in authors}),
        "max_sources": max_sources,
        "max_chars": max_chars,
        "model": model.model,
        "reviewed_only": reviewed_only,
    }
    patterns = []
    for batch in partition(examples, max_chars):
        allowed = {e["id"]: e for e in batch}
        result = cached_call(
            workspace,
            model,
            "twin_observations",
            PATTERN_SCHEMA,
            prompts.TWIN,
            {
                "examples": batch,
                "selected_sources_in_batch": len({e["source_id"] for e in batch}),
            },
            budget,
            lambda value, allowed=allowed: validate_patterns(value, allowed),
        )
        patterns.extend(result)
    profile = {
        "config": config,
        "coverage": coverage,
        "patterns": patterns,
        "observation_review": "unreviewed",
        "adaptations_status": "proposed_not_observed",
    }
    publish(
        workspace / "twin",
        {
            "profile.json": js(profile),
            "examples.jsonl": jsonl(examples),
            "profile.md": render_profile(patterns, examples, coverage, workspace),
        },
        twin_inputs(workspace, source_dir, config),
    )
    return workspace / "twin/profile.md"


def validate_twin(workspace, records, sources):
    profile = load_json(workspace / "twin/profile.json")
    root = Path(load_json(workspace / "wiki/build.json")["inputs"]["source_root"])
    check_artifacts(workspace / "twin", twin_inputs(workspace, root, profile["config"]))
    accepted = [r for r in records if r["semantic_status"] != "human_unsupported"]
    expected, coverage = prepare_examples(
        accepted,
        sources,
        profile["config"]["authors"],
        profile["config"]["max_sources"],
        reviewed_only=profile["config"]["reviewed_only"],
    )
    examples = json_lines(workspace / "twin/examples.jsonl")
    if expected != examples or coverage != profile["coverage"]:
        raise ValueError("Twin context or coverage no longer matches active evidence")
    for pattern in profile["patterns"]:
        validate_patterns({"patterns": [pattern]}, {e["id"]: e for e in examples})
    if render_profile(profile["patterns"], examples, coverage, workspace) != (
        workspace / "twin/profile.md"
    ).read_text(encoding="utf-8"):
        raise ValueError("Twin Markdown does not match the structured observations")
