from __future__ import annotations

import hashlib
import math
import re
from dataclasses import dataclass
from pathlib import Path

import lancedb

VECTOR_DIMENSIONS = 256
JAVA_BULLET_RE = re.compile(
    r"○\s*Java[^\n]*\n(?P<body>.*?)(?=\n○\s|\n●\s|\n\d{4}-\d{2}-\d{2} |\Z)",
    re.S,
)
HIGHLIGHT_RE = re.compile(r"^\s*■\s*(?P<text>.+?)\s*$", re.M)
THANKS_RE = re.compile(r"\s*[<(]\s*Thanks\b.*?[!）)]\s*>?\s*$", re.I)
PR_RE = re.compile(r"\s*(?:\(#\d+\)|\[#\d+\]|#\d+)\s*")
TOKEN_RE = re.compile(r"[a-z0-9][a-z0-9_.-]*", re.I)


@dataclass(frozen=True)
class VectorMatch:
    score: int
    reason: str
    matched_example: str


def clean_highlight_text(text: str) -> str:
    text = THANKS_RE.sub("", text).strip()
    text = PR_RE.sub(" ", text)
    return re.sub(r"\s+", " ", text).strip()


def extract_java_highlights(notes_path: Path) -> list[str]:
    if not notes_path.exists():
        return []
    notes = notes_path.read_text(encoding="utf-8")
    highlights: list[str] = []
    seen: set[str] = set()
    for section in JAVA_BULLET_RE.finditer(notes):
        for match in HIGHLIGHT_RE.finditer(section.group("body")):
            text = clean_highlight_text(match.group("text"))
            if text and text not in seen:
                seen.add(text)
                highlights.append(text)
    return highlights


def tokenize(text: str) -> list[str]:
    return [token.lower() for token in TOKEN_RE.findall(text)]


def text_to_vector(text: str, dimensions: int = VECTOR_DIMENSIONS) -> list[float]:
    vector = [0.0] * dimensions
    tokens = tokenize(text)
    features = tokens + [f"{left} {right}" for left, right in zip(tokens, tokens[1:])]
    for feature in features:
        digest = hashlib.blake2b(feature.encode("utf-8"), digest_size=8).digest()
        bucket = int.from_bytes(digest[:4], "big") % dimensions
        sign = 1.0 if digest[4] & 1 else -1.0
        vector[bucket] += sign
    length = math.sqrt(sum(value * value for value in vector))
    if not length:
        return vector
    return [value / length for value in vector]


def commit_text(row: dict[str, str]) -> str:
    parts = [
        row.get("subject", ""),
        row.get("body", "").split("\n\n", 1)[0],
        row.get("top_level_paths", ""),
    ]
    return "\n".join(part for part in parts if part)


def build_java_highlight_index(notes_path: Path, db_dir: Path) -> int:
    highlights = extract_java_highlights(notes_path)
    db_dir.mkdir(parents=True, exist_ok=True)
    db = lancedb.connect(db_dir)
    data = [
        {
            "id": index,
            "text": highlight,
            "vector": text_to_vector(highlight),
        }
        for index, highlight in enumerate(highlights)
    ]
    if data:
        db.create_table("java_highlights", data=data, mode="overwrite")
    elif "java_highlights" in list_table_names(db):
        db.drop_table("java_highlights")
    return len(data)


def list_table_names(db: object) -> list[str]:
    tables = db.list_tables()
    if isinstance(tables, list):
        return tables
    return list(getattr(tables, "tables", []))


def l2_similarity(distance: float) -> float:
    return max(0.0, min(1.0, 1.0 - (distance / 2.0)))


def rank_with_lancedb(row: dict[str, str], db_dir: Path) -> VectorMatch:
    db = lancedb.connect(db_dir)
    if "java_highlights" not in list_table_names(db):
        return VectorMatch(0, "no LanceDB highlight index", "")
    table = db.open_table("java_highlights")
    results = table.search(text_to_vector(commit_text(row))).limit(1).to_list()
    if not results:
        return VectorMatch(0, "no LanceDB highlight matches", "")
    best = results[0]
    distance = float(best.get("_distance", 2.0))
    similarity = l2_similarity(distance)
    score = round(similarity * 30)
    example = str(best.get("text", ""))
    return VectorMatch(score, f"LanceDB similarity {similarity:.2f}", example)
