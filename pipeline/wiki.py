"""Readable, linked wiki views. Source records remain the authority beneath every view."""

from collections import Counter

from .organization import key, load_organization, source_units
from .records import PRODUCTS
from .storage import digest, js, jsonl, load_json, publish


def unit_anchor(ident):
    return "unit-" + digest(ident)[:16]


def entry_name(record):
    return key(record["title"])[:80] + "-" + digest(record["id"])[:10]


def build_wiki(workspace, source_dir, records, sources, inputs):
    from .core import escaped, link, record_link, render_record

    wiki = workspace / "wiki"
    documents, definitions, stale = load_organization(workspace, sources)
    topics = {t["id"]: {**t, "record_ids": [], "episode_ids": []} for t in definitions}
    aliases = {a: t["id"] for t in definitions for a in t["aliases"]}

    def topic_id(label):
        ident = aliases.get(label, key(label))
        if ident == "index":
            ident = "index-topic"
        if ident not in topics:
            topics[ident] = {
                "id": ident,
                "name": label,
                "aliases": [label],
                "parent_id": None,
                "record_ids": [],
                "episode_ids": [],
            }
        elif label not in topics[ident]["aliases"]:
            topics[ident]["aliases"].append(label)
        return ident

    for record in records:
        topics[topic_id(record["topic"])]["record_ids"].append(record["id"])
    by_record = {r["id"]: r for r in records}
    units = {s.id: source_units(s) for s in sources.values()}
    unit_lookup = {u["id"]: u for us in units.values() for u in us}
    episodes, entities = [], {}
    for sid, document in documents.items():
        for episode in document["episodes"]:
            episode = {
                **episode,
                "source_id": sid,
                "platform": sources[sid].category,
                "part": unit_lookup[episode["unit_ids"][0]]["part"],
                "topics": [topic_id(t) for t in episode["topics"]],
                "status": "unreviewed",
                "path": f"episodes/{episode['id']}.md",
            }
            episode["record_ids"] = [
                r["id"]
                for r in records
                if r["source_id"] == sid
                and set(r["content"]["context_unit_ids"]) & set(episode["unit_ids"])
            ]
            episode["roles"] = sorted({m["role"] for m in episode["moves"]})
            episodes.append(episode)
            for t in episode["topics"]:
                topics[t]["episode_ids"].append(episode["id"])
        for entity in document["entities"]:
            # People/projects stay source-scoped. Other equal names are grouped as
            # mention labels only; this does not assert employment or endorsement.
            ident = (
                entity["id"]
                if entity["kind"] in {"person", "project"}
                else f"{entity['kind']}-{key(entity['name'])[:60]}-{digest([entity['kind'], entity['name'].casefold()])[:8]}"
            )
            target = entities.setdefault(
                ident,
                {
                    "id": ident,
                    "name": entity["name"],
                    "kind": entity["kind"],
                    "mentions": [],
                    "path": f"entities/{ident}.md",
                },
            )
            target["mentions"].extend(
                {"source_id": sid, **c} for c in entity["mentions"]
            )
    by_episode = {e["id"]: e for e in episodes}
    files = {}

    def header(title, note=None):
        return [f"# {escaped(title)}", "", "[Wiki home](../index.md)", ""] + (
            [f"> {note}", ""] if note else []
        )

    def cite(c, sid, page):
        unit = unit_lookup[c["unit_id"]]
        target = (
            link(wiki / "sources" / f"{sid}.md", page) + "#" + unit_anchor(unit["id"])
        )
        line = f"- “{escaped(c['quote'])}” — [{escaped(unit['locator'])}]({target})"
        if c.get("end_unit_id"):
            end = unit_lookup[c["end_unit_id"]]
            end_target = (
                link(wiki / "sources" / f"{sid}.md", page)
                + "#"
                + unit_anchor(end["id"])
            )
            line += f" through [{escaped(end['locator'])}]({end_target})"
        return line

    def rec_list(items, page):
        return [
            f"- [{escaped(r['title'])}]({record_link(r, workspace, page)}) · {r['product']} · {r['category']}"
            for r in items
        ]

    def episode_list(items, page):
        return [
            f"- [{escaped(e['title'])}]({link(wiki / e['path'], page)}) · {', '.join(e['activities'])} · {e['part']}"
            for e in items
        ]

    def related(record, page):
        t = topic_id(record["topic"])
        lines = [
            "## Connections",
            "",
            f"- Topic: [{escaped(topics[t]['name'])}]({link(wiki / 'topics' / f'{t}.md', page)})",
        ]
        lines += episode_list(
            [e for e in episodes if record["id"] in e["record_ids"]], page
        )
        return lines

    for product in PRODUCTS:
        subset = [r for r in records if r["product"] == product]
        files[f"{product}.jsonl"] = jsonl(subset)
        page = wiki / f"{product}.md"
        files[f"{product}.md"] = (
            f"# {product.title()}\n\n" + "\n".join(rec_list(subset, page)) + "\n"
        )
    methods = []
    expressions = []
    for record in records:
        directory = (
            "methods"
            if record["product"] == "knowledge"
            and record["content"]["kind"] == "method"
            else "expression"
            if record["product"] == "expression"
            else None
        )
        if directory:
            path = f"{directory}/{entry_name(record)}.md"
            page = wiki / path
            files[path] = (
                "\n".join(
                    header(
                        record["title"],
                        "Source-local evidence, not a recurring habit or verified effectiveness.",
                    )
                    + related(record, page)
                )
                + "\n\n"
                + render_record(record, sources[record["source_id"]], page)
            )
            item = {
                "id": record["id"],
                "title": record["title"],
                "path": path,
                "source_id": record["source_id"],
                "topics": [topic_id(record["topic"])],
                "platform": record["category"],
            }
            item["parts"] = sorted(
                {unit_lookup[u]["part"] for u in record["content"]["context_unit_ids"]}
            )
            (methods if directory == "methods" else expressions).append(item)

    for episode in episodes:
        page = wiki / episode["path"]
        sid = episode["source_id"]
        lines = header(
            episode["title"],
            "Model-organized source episode; labels and summary are unreviewed. No hidden intention or outcome is established.",
        )
        lines += [
            f"**Platform:** {episode['platform']} · **Part:** {episode['part']} · **Scope:** {episode['scope']}",
            f"**Activities:** {', '.join(episode['activities'])}",
            "",
            escaped(episode["summary"]["text"]),
            "",
        ]
        lines += [cite(c, sid, page) for c in episode["summary"]["citations"]]
        lines += ["", "## Topics", ""] + [
            f"- [{escaped(topics[t]['name'])}](../topics/{t}.md)"
            for t in episode["topics"]
        ]
        lines += ["", "## Observed sequence", ""]
        for move in episode["moves"]:
            unit = unit_lookup[move["unit_id"]]
            who = unit["speaker_name"] or (
                "Speaker " + unit["speaker_id"]
                if unit["speaker_id"]
                else unit["author"] or "unknown author"
            )
            lines += [
                f"### {escaped(move['action'])}",
                f"{escaped(who)} · tentative role: {move['role']}",
                cite(move, sid, page),
                "",
            ]
        lines += ["## Related extracted records", ""] + rec_list(
            [by_record[i] for i in episode["record_ids"]], page
        )
        lines += ["", "## Complete selected passage sequence", ""]
        for uid in episode["unit_ids"]:
            u = unit_lookup[uid]
            lines += [
                f"**{escaped(u['speaker_name'] or u['speaker_id'] or u['author'] or 'unknown')}** · {escaped(u['time'] or u['locator'])}",
                "",
                "\n".join("> " + escaped(line) for line in u["text"].splitlines()),
                "",
            ]
        files[episode["path"]] = "\n".join(lines) + "\n"

    for entity in entities.values():
        page = wiki / entity["path"]
        lines = header(
            entity["name"],
            "A named mention is not evidence of a relationship, employment, or endorsement. People/projects are source-scoped.",
        )
        lines += [f"**Type:** {entity['kind']}", "", "## Source mentions", ""]
        for mention in entity["mentions"]:
            lines.append(cite(mention, mention["source_id"], page))
        mention_ids = {m["unit_id"] for m in entity["mentions"]}
        linked = [e for e in episodes if mention_ids & set(e["unit_ids"])]
        lines += ["", "## Episodes", ""] + episode_list(linked, page)
        entity["episode_ids"] = [e["id"] for e in linked]
        entity["topics"] = sorted({t for e in linked for t in e["topics"]})
        files[entity["path"]] = "\n".join(lines) + "\n"

    for ident, topic in sorted(topics.items()):
        page = wiki / "topics" / f"{ident}.md"
        lines = header(
            topic["name"],
            "Navigation groups source evidence; it does not establish a universal position or independent corroboration.",
        )
        lines += ["**Aliases:** " + ", ".join(escaped(a) for a in topic["aliases"]), ""]
        if topic["parent_id"]:
            parent = topics[topic["parent_id"]]
            lines += [
                f"**Broader topic:** [{escaped(parent['name'])}]({parent['id']}.md)",
                "",
            ]
        children = [t for t in topics.values() if t["parent_id"] == ident]
        if children:
            lines += (
                ["## Subtopics", ""]
                + [f"- [{escaped(t['name'])}]({t['id']}.md)" for t in children]
                + [""]
            )
        connected = [m for m in methods + expressions if ident in m["topics"]]
        lines += ["## Methods and expression", ""] + [
            f"- [{escaped(m['title'])}]({link(wiki / m['path'], page)})"
            for m in connected
        ]
        lines += ["", "## Episodes", ""] + episode_list(
            [by_episode[i] for i in topic["episode_ids"]], page
        )
        named = [e for e in entities.values() if ident in e["topics"]]
        lines += ["", "## Named entities", ""] + [
            f"- [{escaped(e['name'])}]({link(wiki / e['path'], page)})" for e in named
        ]
        lines += ["", "## Source-local knowledge, cases and expression", ""]
        # Keep all accepted fields available on topic pages as well as canonical
        # source anchors; these are projections of records, not independent copies.
        lines += [
            render_record(by_record[i], sources[by_record[i]["source_id"]], page)
            for i in topic["record_ids"]
        ]
        files[f"topics/{ident}.md"] = "\n".join(lines) + "\n"

    source_entries = []
    for source in sources.values():
        sid = source.id
        page = wiki / "sources" / f"{sid}.md"
        source_episodes = [e for e in episodes if e["source_id"] == sid]
        source_entities = [
            e
            for e in entities.values()
            if any(m["source_id"] == sid for m in e["mentions"])
        ]
        source_records = [r for r in records if r["source_id"] == sid]
        lines = header(source.title)
        lines += [
            f"[Original captured file]({link(source.path, page)}) · {source.date or 'undated'} · {source.category}",
            f"**Publisher/author:** {escaped(source.author or 'unknown')} · **Supplied speakers:** {escaped(js(source.speakers).strip())}",
            "",
            "## Episodes",
            "",
        ] + episode_list(source_episodes, page)
        if sid not in documents:
            lines += [
                "Episode/entity organization has not been run for this source (or is stale).",
                "",
            ]
        lines += ["", "## Named mentions", ""] + [
            f"- [{escaped(e['name'])}]({link(wiki / e['path'], page)})"
            for e in source_entities
        ]
        lines += ["", "## Extracted records", ""] + rec_list(source_records, page)
        lines += [
            "",
            "## Captured source parts",
            "",
            "Speaker names are supplied metadata, not independently authenticated. Comment authors remain distinct from the publisher.",
            "",
        ]
        for u in units[sid]:
            who = u["speaker_name"] or (
                "Speaker " + u["speaker_id"]
                if u["speaker_id"]
                else u["author"] or "unknown author"
            )
            lines += [
                f'<a id="{unit_anchor(u["id"])}"></a>',
                f"### {u['part']} · {escaped(u['time'] or u['locator'])}",
                f"**{escaped(who)}**",
                "",
                "\n".join("> " + escaped(line) for line in u["text"].splitlines()),
                "",
            ]
        lines += ["## Record details", ""] + [
            render_record(r, source, page, include_context=False)
            for r in source_records
        ]
        files[f"sources/{sid}.md"] = "\n".join(lines) + "\n"
        source_entries.append(
            {
                "id": sid,
                "title": source.title,
                "path": f"sources/{sid}.md",
                "platform": source.category,
                "published_at": source.date or None,
                "author": source.author or None,
                "speakers": source.speakers,
                "parts": sorted({u["part"] for u in units[sid]}),
                "content_family": source.content_hash,
                "organized": sid in documents,
            }
        )

    for directory, entries in (
        ("methods", methods),
        ("expression", expressions),
        ("episodes", episodes),
        ("entities", list(entities.values())),
        ("sources", source_entries),
    ):
        page = wiki / directory / "index.md"
        lines = header(directory.title())
        lines += [
            f"- [{escaped(e.get('title', e.get('name', e['id'])))}]({link(wiki / e['path'], page)})"
            for e in entries
        ]
        if not entries:
            lines += [
                "No entries yet. Run `organize` on ingested sources for source-backed episodes and entities; missing entries are not evidence of absence."
            ]
        files[f"{directory}/index.md"] = "\n".join(lines) + "\n"
    files["topics/index.md"] = (
        "# Topics\n\n[Wiki home](../index.md)\n\n"
        + "\n".join(
            f"- [{escaped(t['name'])}]({i}.md)" for i, t in sorted(topics.items())
        )
        + "\n"
    )
    for platform in sorted({s.category for s in sources.values()}):
        files[f"channels/{key(platform)}.md"] = (
            f"# {escaped(platform)}\n\n"
            + "\n".join(
                f"- [{escaped(s.title)}](../sources/{s.id}.md)"
                for s in sources.values()
                if s.category == platform
            )
            + "\n"
        )
    for activity in sorted({a for e in episodes for a in e["activities"]}):
        page = wiki / "activities" / f"{activity}.md"
        files[f"activities/{activity}.md"] = (
            "\n".join(
                header(
                    activity.title(),
                    "Activities are unreviewed episode-level labels, not inferred from platform ownership.",
                )
                + episode_list(
                    [e for e in episodes if activity in e["activities"]], page
                )
            )
            + "\n"
        )
    timeline = sorted(sources.values(), key=lambda s: (s.date or "9999", s.id))
    files["timeline.md"] = (
        "# Publication timeline\n\n> Publication dates, not event dates.\n\n"
        + "\n".join(
            f"- {s.date or 'undated'} · [{escaped(s.title)}](sources/{s.id}.md)"
            for s in timeline
        )
        + "\n"
    )
    summary = {
        "sources": len(sources),
        "records": len(records),
        "products": dict(Counter(r["product"] for r in records)),
        "topics": len(topics),
        "methods": len(methods),
        "episodes": len(episodes),
        "entities": len(entities),
        "organized_sources": len(documents),
        "unorganized_sources": len(sources) - len(documents),
        "stale_organization": stale,
        "omitted_entity_candidates": sum(
            d.get("omitted_entities", 0) for d in documents.values()
        ),
        "topic_aliases_organized": bool(definitions)
        and (
            {r["topic"] for r in records}
            | {
                t
                for d in documents.values()
                for e in d["episodes"]
                for t in e["topics"]
            }
        ).issubset(aliases),
        "content_families": len({s.content_hash for s in sources.values()}),
        "channels": dict(Counter(s.category for s in sources.values())),
        "processing": [
            load_json(p)["quality"] for p in (workspace / "manifest").glob("*.json")
        ],
        "unknown_case_fields": dict(
            Counter(
                k
                for r in records
                if r["product"] == "cases"
                for k in ("diagnosis", "rationale", "outcome")
                if r["content"][k] is None
            )
        ),
    }
    files["overview.json"] = js(summary)
    files["overview.md"] = (
        f"# Corpus overview\n\n{len(sources)} source publications; {len(records)} accepted source-local records.\n\n"
        + "\n".join(
            f"- {k}: {summary[k]}"
            for k in (
                "topics",
                "methods",
                "episodes",
                "entities",
                "organized_sources",
                "unorganized_sources",
                "omitted_entity_candidates",
                "topic_aliases_organized",
            )
        )
        + "\n\nCounts are not recall or confidence. Organization labels are unreviewed; methods retain source-local variants.\n"
    )
    files["catalog.json"] = js(
        {
            "topics": list(topics.values()),
            "entities": list(entities.values()),
            "methods": methods,
            "episodes": episodes,
            "expression": expressions,
            "sources": source_entries,
            "coverage": {
                k: summary[k]
                for k in (
                    "organized_sources",
                    "unorganized_sources",
                    "stale_organization",
                    "omitted_entity_candidates",
                    "topic_aliases_organized",
                )
            },
        }
    )
    lines = [
        "# Knowledge wiki",
        "",
        "A reusable map of source evidence—not a persona report.",
        "",
        f"{len(sources)} sources · {len(records)} records · {len(topics)} topics · {len(episodes)} organized episodes",
        "",
        "## Explore",
        "",
    ]
    lines += [
        f"- [{name.title()}]({name}/index.md)"
        for name in (
            "topics",
            "entities",
            "methods",
            "episodes",
            "expression",
            "sources",
        )
    ]
    lines += [
        "",
        "[Coverage](overview.md) · [Publication timeline](timeline.md)",
        "",
        "## Platforms",
        "",
    ]
    lines += [f"- [{escaped(p)}](channels/{key(p)}.md)" for p in summary["channels"]]
    lines += ["", "## Activities", ""] + [
        f"- [{a}](activities/{a}.md)"
        for a in sorted({a for e in episodes for a in e["activities"]})
    ]
    lines += [
        "",
        "## Coverage limits",
        "",
        f"Episode/entity organization covers {len(documents)} of {len(sources)} sources. Unprocessed sources remain fully accessible; no persona-level patterns are inferred.",
        f"Unsupported entity candidates omitted: {summary['omitted_entity_candidates']}. Topic aliases organized: {summary['topic_aliases_organized']}.",
        "",
        "## Topics",
        "",
    ]
    lines += [
        f"- [{escaped(t['name'])}](topics/{i}.md)" for i, t in sorted(topics.items())
    ]
    files["index.md"] = "\n".join(lines) + "\n"
    files = {
        name: value.rstrip() + "\n" if name.endswith(".md") else value
        for name, value in files.items()
    }
    publish(wiki, files, inputs)
    return wiki / "index.md"


def browse(
    workspace,
    query="",
    *,
    platform=None,
    activity=None,
    part=None,
    role=None,
    kind=None,
    limit=20,
):
    """Offline catalog navigation; return references, not a generated answer."""
    from .core import wiki_inputs
    from .storage import check_artifacts

    if limit < 1:
        raise ValueError("--limit must be positive")
    check_artifacts(workspace / "wiki", wiki_inputs(workspace))
    catalog = load_json(workspace / "wiki/catalog.json")
    tokens = set(key(query).split("-")) if query.strip() else set()
    result = []
    for category in (
        "sources",
        "topics",
        "entities",
        "methods",
        "episodes",
        "expression",
    ):
        if kind and category != kind:
            continue
        for entry in catalog[category]:
            if platform and entry.get("platform") != platform:
                continue
            if activity and activity not in entry.get("activities", []):
                continue
            if part and part not in entry.get("parts", [entry.get("part")]):
                continue
            if role and role not in entry.get("roles", []):
                continue
            searchable = " ".join(
                str(entry.get(k, ""))
                for k in ("title", "name", "aliases", "topics", "summary")
            )
            score = len(tokens & set(key(searchable).split("-")))
            if tokens and not score:
                continue
            result.append(
                {
                    "kind": category,
                    "id": entry["id"],
                    "title": entry.get("title", entry.get("name")),
                    "path": entry.get("path", f"topics/{entry['id']}.md"),
                    "score": score,
                }
            )
    result.sort(key=lambda e: (-e["score"], e["kind"], e["id"]))
    return {
        "entries": result[:limit],
        "omitted": max(0, len(result) - limit),
        "coverage": catalog["coverage"],
        "note": "Navigation only; no matches do not prove absence. Activities/roles require organized episodes.",
    }
