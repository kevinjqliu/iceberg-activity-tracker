from __future__ import annotations

from pathlib import Path

from iceberg_activity.vector_ranker import (
    build_java_highlight_index,
    clean_highlight_text,
    extract_java_highlights,
    rank_with_lancedb,
    text_to_vector,
)


def test_clean_highlight_text_removes_thanks_and_pr_number() -> None:
    text = "Core: Add V4 utilities (#16174) <Thanks Anoop Johnson!>"

    assert clean_highlight_text(text) == "Core: Add V4 utilities"


def test_extract_java_highlights_from_notes(tmp_path: Path) -> None:
    notes = tmp_path / "notes.md"
    notes.write_text(
        """2026-06-03
● Highlights
○ Java
■ Core: Add V4 utilities (#1) <Thanks A!>
■ Spark: Support row lineage (#2) <Thanks B!>
○ Python
■ Should not appear
""",
        encoding="utf-8",
    )

    assert extract_java_highlights(notes) == [
        "Core: Add V4 utilities",
        "Spark: Support row lineage",
    ]


def test_text_to_vector_is_normalized() -> None:
    vector = text_to_vector("Core: Add V4 utilities")

    assert len(vector) == 256
    assert 0.99 < sum(value * value for value in vector) < 1.01


def test_rank_with_lancedb_matches_similar_highlight(tmp_path: Path) -> None:
    notes = tmp_path / "notes.md"
    db_dir = tmp_path / "lancedb"
    notes.write_text(
        """2026-06-03
● Highlights
○ Java
■ Core: Add V4 location relativization utilities (#16174) <Thanks A!>
■ Docs: Fix typo (#2) <Thanks B!>
""",
        encoding="utf-8",
    )

    indexed = build_java_highlight_index(notes, db_dir)
    match = rank_with_lancedb(
        {
            "subject": "Core: Add V4 location utilities (#3)",
            "body": "",
            "top_level_paths": "core",
        },
        db_dir,
    )

    assert indexed == 2
    assert match.score > 0
    assert match.matched_example == "Core: Add V4 location relativization utilities"
