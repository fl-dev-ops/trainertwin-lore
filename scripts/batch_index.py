"""Submit indexing as an OpenRouter batch — ~50% cheaper, 24h completion window."""

import hashlib
import json
import os
import sys
import time
from pathlib import Path

import httpx
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parents[1]
load_dotenv(ROOT / ".env")

from pipeline.index import (
    PROMPT, SCHEMA, _is_channel_manifest, accept, plan, source_id,
)
from pipeline.storage import atomic, js, load_json


EXTENSIONS = {".md", ".markdown", ".txt", ".yaml", ".yml"}


def eligible_files(data_dir: Path) -> list[Path]:
    return sorted(
        p for p in data_dir.rglob("*")
        if p.is_file() and not p.is_symlink()
        and p.suffix.lower() in EXTENSIONS
        and not any(part.startswith(".") or part == "__pycache__" for part in p.relative_to(data_dir).parts)
    )


def build_requests(data_dir: Path, model: str, reasoning_effort: str = "low", max_output_tokens: int = 8192):
    """Build batch request items from source files."""
    requests = []
    file_map = {}  # custom_id → (path, source_id, sha256, mode)

    for path in eligible_files(data_dir):
        text = path.read_text()
        if _is_channel_manifest(path, text):
            continue
        lines = text.splitlines()
        if not any(line.strip() for line in lines):
            continue

        digest = hashlib.sha256(text.encode()).hexdigest()
        ident = source_id(path, data_dir)
        rel = path.relative_to(data_dir).as_posix()
        mode, extra = plan(text)
        numbered = "\n".join(f"{i}|{line}" for i, line in enumerate(lines, 1))

        custom_id = ident
        file_map[custom_id] = {
            "path": path,
            "rel": rel,
            "source_id": ident,
            "sha256": digest,
            "mode": mode,
            "lines": lines,
        }
        requests.append({
            "custom_id": custom_id,
            "body": {
                "model": model,
                "messages": [
                    {"role": "system", "content": PROMPT},
                    {"role": "user", "content": numbered + extra},
                ],
                "response_format": {
                    "type": "json_schema",
                    "json_schema": {"name": "index_items", "strict": True, "schema": SCHEMA},
                },
                "max_tokens": max_output_tokens,
                **({"reasoning": {"effort": reasoning_effort}} if reasoning_effort else {}),
            },
        })

    return requests, file_map


def submit_batch(api_key: str, model: str, requests: list[dict]) -> str:
    """Submit batch and return batch ID."""
    http = httpx.Client(
        base_url="https://openrouter.ai/api/v1",
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
        timeout=httpx.Timeout(120.0, connect=20.0),
    )
    try:
        resp = http.post("/batches", json={
            "endpoint": "/v1/chat/completions",
            "model": model,
            "completion_window": "24h",
            "requests": requests,
        })
        if resp.status_code != 202:
            raise RuntimeError(f"Batch submit failed: HTTP {resp.status_code} {resp.text[:500]}")
        data = resp.json()
        return data["id"]
    finally:
        http.close()


def poll_batch(api_key: str, batch_id: str, interval: int = 30) -> dict:
    """Poll until terminal status. Returns the batch object with results."""
    http = httpx.Client(
        base_url="https://openrouter.ai/api/v1",
        headers={"Authorization": f"Bearer {api_key}"},
        timeout=httpx.Timeout(60.0, connect=20.0),
    )
    terminal = {"completed", "failed", "expired", "cancelled"}
    consecutive_404s = 0
    try:
        while True:
            try:
                resp = http.get(f"/batches/{batch_id}")
                if resp.status_code == 404:
                    consecutive_404s += 1
                    if consecutive_404s > 10:
                        resp.raise_for_status()
                    print(f"  [{batch_id[:12]}] 404 while propagating ({consecutive_404s}/10), waiting...", flush=True)
                    time.sleep(min(interval, 10))
                    continue
                resp.raise_for_status()
                consecutive_404s = 0
                batch = resp.json()
                status = batch["status"]
                counts = batch.get("request_counts", {})
                print(f"  [{batch_id[:12]}] status={status} total={counts.get('total', '?')} "
                      f"completed={counts.get('completed', '?')} failed={counts.get('failed', '?')}",
                      flush=True)
                if status in terminal:
                    return batch
            except (httpx.TimeoutException, httpx.NetworkError, httpx.RemoteProtocolError) as exc:
                print(f"  [{batch_id[:12]}] network error ({exc}), retrying...", flush=True)
            time.sleep(interval)
    finally:
        http.close()


def process_results(batch: dict, file_map: dict, workspace: Path):
    """Convert batch results into index.json."""
    results = batch.get("results") or []
    successes, failures = 0, 0

    # Load or init index
    index_path = workspace / "index.json"
    data = {"sources": {}, "items": []}
    if index_path.exists():
        data = load_json(index_path)
        data.setdefault("sources", {})
        data.setdefault("items", [])

    for result in results:
        cid = result["custom_id"]
        info = file_map.get(cid)
        if not info:
            print(f"  Unknown custom_id: {cid}", flush=True)
            failures += 1
            continue

        if result.get("error"):
            print(f"  {info['rel']}: batch error ({result['error']})", flush=True)
            failures += 1
            continue

        body = result.get("response", {}).get("body", {})
        choice = (body.get("choices") or [{}])[0]
        if choice.get("finish_reason") != "stop":
            print(f"  {info['rel']}: incomplete ({choice.get('finish_reason')})", flush=True)
            failures += 1
            continue

        content = choice.get("message", {}).get("content", "")
        try:
            raw = json.loads(content)
        except (json.JSONDecodeError, TypeError):
            print(f"  {info['rel']}: bad JSON", flush=True)
            failures += 1
            continue

        items = accept(info["lines"], raw)
        if not items:
            print(f"  {info['rel']}: no valid items", flush=True)
            failures += 1
            continue

        ident = info["source_id"]
        for n, item in enumerate(items):
            item["item_id"] = f"{ident}:{item['span']['start_line']:04d}-{item['span']['end_line']:04d}"
            item["source_id"] = ident
            item["path"] = info["rel"]
        for n, item in enumerate(items):
            item["prev"] = items[n - 1]["item_id"] if n > 0 else None
            item["next"] = items[n + 1]["item_id"] if n + 1 < len(items) else None

        data["sources"][ident] = {
            "path": info["rel"],
            "sha256": info["sha256"],
            "basis": raw.get("basis") or info["mode"],
        }
        data["items"] = [i for i in data["items"] if i.get("source_id") != ident]
        data["items"].extend(items)
        successes += 1
        print(f"  {info['rel']}: {info['mode']}:{len(items)}", flush=True)

    workspace.mkdir(parents=True, exist_ok=True)
    atomic(index_path, js(data))
    return successes, failures


def get_batch(http: httpx.Client, batch_id: str) -> dict:
    """Fetch batch status once."""
    resp = http.get(f"/batches/{batch_id}")
    resp.raise_for_status()
    return resp.json()


def monitor_batches(api_key: str, active: dict[str, str]):
    """active is {user: batch_id}. Poll all and process each as it finishes."""
    model = "google/gemini-3.8-flash:batch"
    pending = dict(active)
    file_maps = {}
    for user in pending:
        data_dir = (ROOT / "users" / user / "data").resolve()
        _, fmap = build_requests(data_dir, model)
        file_maps[user] = fmap

    http = httpx.Client(
        base_url="https://openrouter.ai/api/v1",
        headers={"Authorization": f"Bearer {api_key}"},
        timeout=httpx.Timeout(60.0, connect=20.0),
    )
    try:
        while pending:
            for user, batch_id in list(pending.items()):
                try:
                    batch = get_batch(http, batch_id)
                except Exception as exc:
                    print(f"Error checking {user} ({batch_id[:12]}): {exc}", flush=True)
                    continue

                status = batch.get("status")
                counts = batch.get("request_counts", {})
                print(f"[{user:7s}] status={status:11s} total={counts.get('total', '?')} "
                      f"completed={counts.get('completed', '?')} failed={counts.get('failed', '?')}",
                      flush=True)

                if status == "completed":
                    print(f"\n{'='*60}\n{user.upper()} BATCH COMPLETED! Processing results...", flush=True)
                    workspace = (ROOT / "users" / user / "workspace").resolve()
                    ok, fail = process_results(batch, file_maps[user], workspace)
                    cost = batch.get("usage", {}).get("cost", "?")
                    print(f"{user}: DONE — {ok} sources indexed, {fail} failures, cost=${cost}\n{'='*60}\n", flush=True)
                    del pending[user]
                elif status in ("failed", "expired", "cancelled"):
                    print(f"\n{user.upper()} BATCH {status}: {batch.get('error')}", flush=True)
                    del pending[user]

            if pending:
                time.sleep(30)
    finally:
        http.close()
    print("All monitored batches finished.")


def main():
    api_key = os.getenv("OPENROUTER_API_KEY", "")
    if not api_key:
        raise SystemExit("Set OPENROUTER_API_KEY")

    model = "google/gemini-3.8-flash:batch"
    args = sys.argv[1:]

    if len(args) >= 1 and args[0] == "--monitor":
        # python scripts/batch_index.py --monitor user1:batch1 user2:batch2 ...
        pairs = {}
        for item in args[1:]:
            u, b = item.split(":")
            pairs[u] = b
        monitor_batches(api_key, pairs)
        return

    # Check for --attach <batch_id> <user>
    if len(args) >= 3 and args[0] == "--attach":
        batch_id, user = args[1], args[2]
        data_dir = (ROOT / "users" / user / "data").resolve()
        workspace = (ROOT / "users" / user / "workspace").resolve()
        _, file_map = build_requests(data_dir, model)
        print(f"Attaching to batch {batch_id} for user {user} ({len(file_map)} files in map)...")
        batch = poll_batch(api_key, batch_id)
        if batch["status"] != "completed":
            raise SystemExit(f"Batch {batch['status']}: {batch.get('error', {}).get('message', 'unknown')}")
        ok, fail = process_results(batch, file_map, workspace)
        cost = batch.get("usage", {}).get("cost", "?")
        print(f"{user}: done — {ok} sources indexed, {fail} failures, cost=${cost}")
        return

    users = args or ["olga", "vasanth", "jameel"]

    for user in users:
        data_dir = (ROOT / "users" / user / "data").resolve()
        workspace = (ROOT / "users" / user / "workspace").resolve()
        if not data_dir.is_dir():
            print(f"{user}: data dir not found, skipping")
            continue

        # Backup existing index
        index_path = workspace / "index.json"
        if index_path.exists():
            import shutil
            from datetime import datetime, timezone
            backup = index_path.with_name(f"index.backup-{datetime.now(timezone.utc):%Y%m%dT%H%M%SZ}.json")
            shutil.copy2(index_path, backup)
            index_path.unlink()
            print(f"{user}: backed up to {backup.name}")

        print(f"\n{'='*60}")
        print(f"{user}: building requests...")
        requests, file_map = build_requests(data_dir, model)
        print(f"{user}: {len(requests)} requests built, submitting batch...")

        batch_id = submit_batch(api_key, model, requests)
        print(f"{user}: batch submitted → {batch_id}")
        print(f"{user}: polling (24h window, ~50% cheaper)...")

        batch = poll_batch(api_key, batch_id)

        if batch["status"] != "completed":
            print(f"{user}: batch {batch['status']}: {batch.get('error', {}).get('message', 'unknown')}")
            continue

        print(f"{user}: processing results...")
        ok, fail = process_results(batch, file_map, workspace)
        cost = batch.get("usage", {}).get("cost", "?")
        print(f"{user}: done — {ok} sources indexed, {fail} failures, cost=${cost}")


if __name__ == "__main__":
    main()
