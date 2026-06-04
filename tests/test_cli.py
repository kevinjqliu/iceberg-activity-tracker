from __future__ import annotations

from datetime import date

import pytest

from iceberg_activity import cli


def test_resolve_date_range_defaults_to_45_day_lookback(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(cli, "default_until", lambda: date(2026, 6, 3))

    since, until = cli.resolve_date_range(None, None)

    assert since == date(2026, 4, 19)
    assert until == date(2026, 6, 3)


def test_resolve_date_range_uses_explicit_dates() -> None:
    since, until = cli.resolve_date_range(date(2026, 5, 1), date(2026, 5, 31))

    assert since == date(2026, 5, 1)
    assert until == date(2026, 5, 31)


def test_resolve_date_range_rejects_inverted_dates() -> None:
    with pytest.raises(ValueError, match="--since"):
        cli.resolve_date_range(date(2026, 6, 1), date(2026, 5, 1))


def test_resolve_summary_range_defaults_to_21_day_meeting_window(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(cli, "default_until", lambda: date(2026, 6, 3))

    since, until = cli.resolve_summary_range(since=None, until=None, meeting_date=None)

    assert since == date(2026, 5, 14)
    assert until == date(2026, 6, 3)


def test_resolve_summary_range_uses_meeting_date() -> None:
    since, until = cli.resolve_summary_range(
        since=None,
        until=None,
        meeting_date=date(2026, 6, 3),
    )

    assert since == date(2026, 5, 14)
    assert until == date(2026, 6, 3)


def test_resolve_summary_range_uses_explicit_range() -> None:
    since, until = cli.resolve_summary_range(
        since=date(2026, 5, 15),
        until=date(2026, 6, 3),
        meeting_date=None,
    )

    assert since == date(2026, 5, 15)
    assert until == date(2026, 6, 3)


def test_resolve_summary_range_rejects_conflicting_meeting_date_and_until() -> None:
    with pytest.raises(ValueError, match="must match"):
        cli.resolve_summary_range(
            since=None,
            until=date(2026, 6, 4),
            meeting_date=date(2026, 6, 3),
        )


def test_parse_iso_date_rejects_invalid_date() -> None:
    with pytest.raises(Exception, match="expected YYYY-MM-DD"):
        cli.parse_iso_date("06/03/2026")
