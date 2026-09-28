"""Publication dates for bounded social collection, compared as UTC calendar days."""

from datetime import UTC, date, datetime


def published_day(value: str | None) -> date:
    if not value:
        raise ValueError(
            "A post has no publication date; cannot guarantee a bounded collection"
        )
    text = str(value).strip()
    if len(text) == 8 and text.isdigit():  # yt-dlp upload_date
        return date.fromisoformat(f"{text[:4]}-{text[4:6]}-{text[6:]}")
    try:
        if len(text) == 10:
            return date.fromisoformat(text)
        parsed = datetime.fromisoformat(text)
    except ValueError:
        try:
            parsed = datetime.strptime(text, "%a %b %d %H:%M:%S %z %Y")
        except ValueError as exc:
            raise ValueError(f"Unparseable publication date: {text!r}") from exc
    if parsed.tzinfo is None:
        raise ValueError(f"Publication date lacks timezone: {text!r}")
    return parsed.astimezone(UTC).date()


def in_window(value: str | None, since: date, today: date) -> bool:
    return since <= published_day(value) <= today
