"""Gemini Flash OCR client supporting OpenRouter and Google Gemini Files API.

Features:
- Primary: OpenRouter with `google/gemini-2.5-flash` (reuses existing OPENROUTER_API_KEY).
- In-memory Base64 data URIs for all images (zero permanent disk storage, no bot-block on image fetch).
- Immediate cleanup of uploaded remote files if OpenRouter/Google Files API is used.
- Fallback: Direct Google Gemini Files API if GEMINI_API_KEY is supplied.
"""

from __future__ import annotations

import base64
import os
import sys

import httpx

OPENROUTER_BASE = "https://openrouter.ai/api/v1"
OPENROUTER_FILES_BASE = "https://openrouter.ai/api/v1/files"
DEFAULT_OPENROUTER_MODEL = "google/gemini-2.5-flash"

GOOGLE_UPLOAD_BASE = "https://generativelanguage.googleapis.com/upload/v1beta/files"
GOOGLE_GENERATE_BASE = "https://generativelanguage.googleapis.com/v1beta/models"
GOOGLE_FILES_BASE = "https://generativelanguage.googleapis.com/v1beta"
DEFAULT_GOOGLE_MODEL = "gemini-2.0-flash"

DEFAULT_PROMPT = (
    "Extract all readable text, headlines, numbers, and bullet points from this slide or image "
    "verbatim. Output clean Markdown only."
)


def get_ocr_credentials() -> tuple[str, str]:
    """Return ('openrouter', key) or ('google', key) or ('', '')."""
    or_key = os.getenv("OPENROUTER_API_KEY", "").strip()
    if or_key:
        return "openrouter", or_key
    gemini_key = (os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY") or "").strip()
    if gemini_key:
        return "google", gemini_key
    return "", ""


def ocr_image_bytes(
    content: bytes,
    mime_type: str = "image/jpeg",
    prompt: str = DEFAULT_PROMPT,
    model: str = "",
    client: httpx.Client | None = None,
) -> str:
    """Run OCR on in-memory image bytes via OpenRouter (or Google Files API fallback)."""
    provider, key = get_ocr_credentials()
    if not key or not content:
        return ""

    if provider == "openrouter":
        target_model = model or DEFAULT_OPENROUTER_MODEL
        # Base64 data URI directly in chat completions
        b64_str = base64.b64encode(content).decode("ascii")
        data_uri = f"data:{mime_type};base64,{b64_str}"
        payload = {
            "model": target_model,
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt},
                        {"type": "image_url", "image_url": {"url": data_uri}},
                    ],
                }
            ],
        }
        headers = {
            "Authorization": f"Bearer {key}",
            "Content-Type": "application/json",
        }
        http = client or httpx.Client(timeout=60.0)
        try:
            resp = http.post(f"{OPENROUTER_BASE}/chat/completions", headers=headers, json=payload)
            if resp.status_code == 200:
                data = resp.json()
                try:
                    choice = data.get("choices", [{}])[0]
                    content_val = choice.get("message", {}).get("content")
                    if isinstance(content_val, str):
                        return content_val.strip()
                except (KeyError, IndexError, TypeError):
                    return ""
                return ""
            print(f"Warning: OpenRouter bytes OCR HTTP {resp.status_code}: {resp.text[:120]}", file=sys.stderr)
            return ""
        except Exception as exc:  # noqa: BLE001
            print(f"Warning: OpenRouter bytes OCR exception: {exc}", file=sys.stderr)
            return ""
        finally:
            if not client:
                http.close()

    # Direct Google Files API fallback
    target_model = model or DEFAULT_GOOGLE_MODEL
    if len(content) < 4 * 1024 * 1024:
        encoded = base64.b64encode(content).decode("ascii")
        payload = {
            "contents": [
                {
                    "role": "user",
                    "parts": [
                        {"inlineData": {"mimeType": mime_type, "data": encoded}},
                        {"text": prompt},
                    ],
                }
            ]
        }
        http = client or httpx.Client(timeout=60.0)
        try:
            resp = http.post(
                f"{GOOGLE_GENERATE_BASE}/{target_model}:generateContent",
                headers={"x-goog-api-key": key, "Content-Type": "application/json"},
                json=payload,
            )
            if resp.status_code == 200:
                data = resp.json()
                return data["candidates"][0]["content"]["parts"][0]["text"].strip()
            return ""
        finally:
            if not client:
                http.close()

    # Large files on Google Files API
    file_name = None
    http = client or httpx.Client(timeout=90.0)
    try:
        upload_resp = http.post(
            GOOGLE_UPLOAD_BASE,
            headers={"x-goog-api-key": key, "Content-Type": mime_type},
            params={"uploadType": "media"},
            content=content,
        )
        if upload_resp.status_code != 200:
            return ""
        file_info = upload_resp.json().get("file", {})
        file_uri = file_info.get("uri")
        file_name = file_info.get("name")
        if not file_uri:
            return ""

        payload = {
            "contents": [
                {
                    "role": "user",
                    "parts": [
                        {"fileData": {"mimeType": mime_type, "fileUri": file_uri}},
                        {"text": prompt},
                    ],
                }
            ]
        }
        gen_resp = http.post(
            f"{GOOGLE_GENERATE_BASE}/{target_model}:generateContent",
            headers={"x-goog-api-key": key, "Content-Type": "application/json"},
            json=payload,
        )
        if gen_resp.status_code != 200:
            return ""
        return gen_resp.json()["candidates"][0]["content"]["parts"][0]["text"].strip()
    finally:
        if file_name:
            try:
                http.delete(f"{GOOGLE_FILES_BASE}/{file_name}", headers={"x-goog-api-key": key})
            except Exception:  # noqa: BLE001, S110
                pass
        if not client:
            http.close()


def ocr_image_url(
    url: str,
    prompt: str = DEFAULT_PROMPT,
    model: str = "",
    client: httpx.Client | None = None,
) -> str:
    """Run OCR on an image URL via in-memory stream into OpenRouter (or Google fallback). Zero disk footprint."""
    if not url:
        return ""
    _, key = get_ocr_credentials()
    if not key:
        return ""

    http = client or httpx.Client(timeout=30.0, follow_redirects=True)
    try:
        resp = http.get(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
        if resp.status_code != 200:
            print(f"Warning: Failed to fetch image {url[:60]} (HTTP {resp.status_code})", file=sys.stderr)
            return ""
        content_type = resp.headers.get("content-type", "image/jpeg").split(";")[0].strip()
        if not content_type.startswith("image/"):
            content_type = "image/jpeg"
        return ocr_image_bytes(
            resp.content, mime_type=content_type, prompt=prompt, model=model, client=http
        )
    except Exception as exc:  # noqa: BLE001
        print(f"Warning: Failed to fetch image for OCR {url[:60]}: {exc}", file=sys.stderr)
        return ""
    finally:
        if not client:
            http.close()
