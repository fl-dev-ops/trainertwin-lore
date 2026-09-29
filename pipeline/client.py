"""Small OpenRouter client with bounded retries and strict JSON responses."""

import json
import random
import time
from typing import Any

import httpx


class ModelError(RuntimeError):
    pass


class OpenRouter:
    def __init__(
        self, api_key: str, model: str, *, transport: httpx.BaseTransport | None = None
    ):
        if not api_key or not model:
            raise ValueError("OPENROUTER_API_KEY and --model are required")
        self.model = model
        self.last_usage: dict[str, Any] = {}
        self.http = httpx.Client(
            base_url="https://openrouter.ai/api/v1",
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
            },
            timeout=httpx.Timeout(120.0, connect=20.0),
            transport=transport,
        )

    def close(self) -> None:
        self.http.close()

    def complete(
        self, name: str, schema: dict[str, Any], system: str, user: str
    ) -> dict[str, Any]:
        self.last_usage = {}
        payload = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
            "response_format": {
                "type": "json_schema",
                "json_schema": {"name": name, "strict": True, "schema": schema},
            },
            "provider": {"require_parameters": True},
        }
        for attempt in range(4):
            try:
                response = self.http.post("/chat/completions", json=payload)
                if response.status_code in (408, 429, 500, 502, 503, 504):
                    if attempt == 3:
                        raise ModelError(
                            f"OpenRouter HTTP {response.status_code} after retries"
                        )
                    retry_after = response.headers.get("Retry-After", "")
                    delay = (
                        float(retry_after)
                        if retry_after.replace(".", "", 1).isdigit()
                        else min(2**attempt, 16)
                    )
                    time.sleep(min(delay, 30) + random.random() / 4)
                    continue
                if response.is_error:
                    # Never print the response body: upstream errors can echo request content.
                    raise ModelError(
                        f"OpenRouter HTTP {response.status_code}; check model/schema/credits"
                    )
                data = response.json()
                self.last_usage = data.get("usage") or {}
                choice = data["choices"][0]
                if choice.get("finish_reason") != "stop":
                    raise ModelError(
                        f"Incomplete model output: {choice.get('finish_reason')}"
                    )
                content = choice["message"]["content"]
                if not isinstance(content, str):
                    raise ModelError("Model returned no JSON content")
                result = json.loads(content)
                if not isinstance(result, dict):
                    raise ModelError("Expected a JSON object")
                return result
            except (httpx.TimeoutException, httpx.NetworkError, httpx.HTTPError) as exc:
                if attempt == 3:
                    raise ModelError(
                        "OpenRouter request timed out or network failed"
                    ) from exc
                time.sleep(min(2**attempt, 16) + random.random() / 4)
            except (
                KeyError,
                IndexError,
                TypeError,
                ValueError,
                json.JSONDecodeError,
            ) as exc:
                raise ModelError("Malformed OpenRouter response") from exc
        raise AssertionError("unreachable")
