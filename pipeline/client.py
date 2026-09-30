"""Small OpenRouter client with bounded retries and strict JSON responses."""

import json
import math
import random
import time
from typing import Any

import httpx

from .storage import atomic, js, load_json


class ProviderBlocked(RuntimeError):
    """Account/configuration failure: no subsequent paid work should be scheduled."""


class SpendBudget:
    """Conservative reservations, persisted before dispatch. Prices are operator inputs.

    UTF-8 bytes bound text-token counts conservatively; output is explicitly capped.
    Lost/unknown responses keep their reservation. This is not a billing guarantee
    if the provider charges above the configured rates or outside token usage.
    """

    def __init__(self, maximum, input_price, output_price, path):
        if not all(
            math.isfinite(x) and x >= 0 for x in (maximum, input_price, output_price)
        ):
            raise ValueError(
                "Dollar cap and token prices must be finite and nonnegative"
            )
        self.maximum, self.input_price, self.output_price, self.path = (
            maximum,
            input_price,
            output_price,
            path,
        )
        self.spent = load_json(path)["spent_or_reserved_usd"] if path.exists() else 0.0
        if (
            type(self.spent) not in {int, float}
            or not math.isfinite(self.spent)
            or self.spent < 0
        ):
            raise ValueError("Invalid persisted spend budget")

    def reserve(self, payload, max_output_tokens):
        amount = (
            (len(js(payload).encode("utf-8")) + 512) * self.input_price
            + max_output_tokens * self.output_price
        ) / 1_000_000
        if self.spent + amount > self.maximum:
            raise ProviderBlocked(
                f"Dollar budget exhausted: ${self.spent:.4f} spent/reserved; next reservation ${amount:.4f}, cap ${self.maximum:.2f}"
            )
        self.spent += amount
        self.save()
        return amount

    def settle(self, reservation, usage):
        actual = usage.get("cost")
        if type(actual) in {int, float} and math.isfinite(actual) and actual >= 0:
            self.spent += actual - reservation
            self.save()

    def save(self):
        atomic(
            self.path,
            js(
                {
                    "max_usd": self.maximum,
                    "spent_or_reserved_usd": self.spent,
                    "input_usd_per_million": self.input_price,
                    "output_usd_per_million": self.output_price,
                }
            ),
        )


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
        self.spend_budget = None
        self.max_output_tokens = 8192
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
            "max_tokens": self.max_output_tokens,
        }
        for attempt in range(4):
            reservation = (
                self.spend_budget.reserve(payload, self.max_output_tokens)
                if self.spend_budget
                else None
            )
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
                    raise ProviderBlocked(
                        f"OpenRouter HTTP {response.status_code}; stop paid stages and check model/schema/credits"
                    )
                data = response.json()
                self.last_usage = data.get("usage") or {}
                if not isinstance(self.last_usage, dict):
                    self.last_usage = {}
                    raise ModelError("Malformed OpenRouter usage")
                if self.spend_budget:
                    self.spend_budget.settle(reservation, self.last_usage)
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
