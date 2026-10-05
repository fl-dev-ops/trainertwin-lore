"""Pre-submit pending long-audio hour-parts to Sarvam while the main collect loop works serially.

Mirrors social.youtube.cli.transcribe_long_audio numbering ({n:03d}-part{p:02d}.mp3.json
checkpoints under sarvam-json/) so the main loop skips pre-seeded parts and only assembles.
Skips lectures already partially processed by the main loop (in-flight ownership).
Resumable via preseed-jobs.json state.
"""

import json
import subprocess
import sys
import tempfile
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from social.youtube.cli import get_sarvam_key, match_sarvam_json  # noqa: E402

AUDIOS = ROOT / "users/prathosh/audios/2024-01-01/02a95f893f"
RAW = ROOT / "users/prathosh/audios/runs/2024-01-01/02a95f893f/sarvam-json"
STATE = RAW.parent / "preseed-jobs.json"
TAKEOVER = "--takeover" in sys.argv


def ffprobe_seconds(path: Path) -> int:
    out = subprocess.run(
        ["ffprobe", "-v", "quiet", "-show_entries", "format=duration", "-of", "csv=p=0", str(path)],
        capture_output=True, text=True, check=False,
    ).stdout.strip()
    return int(float(out)) if out else 0


def atomic_write_bytes(path: Path, data: bytes) -> None:
    pending = path.with_suffix(".tmp")
    pending.write_bytes(data)
    pending.replace(path)


def main() -> None:
    from sarvamai import SarvamAI

    key = get_sarvam_key(None)
    state = json.loads(STATE.read_text()) if STATE.exists() else {"jobs": []}
    known = {j["name"] for j in state["jobs"]}

    tasks = []
    for n, mp3 in enumerate(sorted(AUDIOS.glob("*.mp3")), 1):
        secs = ffprobe_seconds(mp3)
        if secs < 7200:
            continue
        parts = (secs + 3599) // 3600
        have = len(list(RAW.glob(f"{n:03d}-part*.json")))
        label = mp3.name.split(" [")[0]
        if have >= parts:
            continue
        if 0 < have < parts and not TAKEOVER:
            print(f"SKIP in-flight (main loop owns it): {label} {have}/{parts}")
            continue
        for part in range(parts):
            tasks.append((n, part, secs, mp3, label))

    print(f"{len(tasks)} pending parts to submit")

    def submit(task) -> None:
        n, part, secs, mp3, label = task
        name = f"{n:03d}-part{part:02d}.mp3"
        if name in known:
            return
        try:
            with tempfile.TemporaryDirectory() as tmp:
                chunk = Path(tmp) / name
                result = subprocess.run(
                    ["ffmpeg", "-v", "error", "-ss", str(part * 3600), "-t", "3600",
                     "-i", str(mp3), "-vn", "-c:a", "copy", str(chunk)],
                    capture_output=True, text=True, check=False,
                )
                if result.returncode != 0 or not chunk.is_file():
                    print(f"SPLIT FAILED {name}: {result.stderr[:200]}")
                    return
                client = SarvamAI(api_subscription_key=key)
                job = client.speech_to_text_job.create_job(
                    model="saaras:v3", mode="verbatim", language_code="unknown",
                    with_timestamps=True, with_diarization=True,
                )
                job.upload_files([str(chunk)], timeout=600)
                job.start()
            state["jobs"].append({"name": name, "job_id": job.job_id, "label": label})
            STATE.write_text(json.dumps(state, indent=2) + "\n")
            print(f"SUBMITTED {name} ({label}) -> {job.job_id}")
        except Exception as exc:  # noqa: BLE001
            print(f"SUBMIT FAILED {name}: {exc}")

    with ThreadPoolExecutor(max_workers=3) as pool:
        list(pool.map(submit, tasks))

    # Server runs every job concurrently; sequential polling does not serialize work.
    for entry in list(state["jobs"]):
        name, job_id, label = entry["name"], entry["job_id"], entry.get("label", "")
        checkpoint = RAW / f"{name}.json"
        if checkpoint.exists():
            continue
        try:
            client = SarvamAI(api_subscription_key=key)
            job = client.speech_to_text_job.get_job(job_id)
            print(f"WAITING {name} ({label})")
            result = job.wait_until_complete(poll_interval=15, timeout=7200)
            print(f"{name}: {result.job_state}")
            if not job.is_successful():
                print(f"JOB FAILED {name}: {json.dumps(job.get_file_results(), default=str)[:400]}")
                continue
            with tempfile.TemporaryDirectory() as tmp:
                job.download_outputs(tmp)
                output = match_sarvam_json(name, Path(tmp))
                if output is None:
                    print(f"NO OUTPUT MATCH {name}")
                    continue
                atomic_write_bytes(checkpoint, output.read_bytes())
            print(f"CHECKPOINTED {name}")
        except Exception as exc:  # noqa: BLE001
            print(f"WAIT/SAVE FAILED {name}: {exc}")

    total = len(state["jobs"])
    done = sum(1 for j in state["jobs"] if (RAW / f"{j['name']}.json").exists())
    print(f"PRESEED DONE: {done}/{total} checkpoints present")


if __name__ == "__main__":
    main()
