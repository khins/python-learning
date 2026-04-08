"""
Week 2 practice: files, pathlib, and JSON.
"""

from __future__ import annotations

import json
from pathlib import Path


def save_scores(path: Path, scores: dict[str, int]) -> None:
    path.write_text(json.dumps(scores, indent=2), encoding="utf-8")


def load_scores(path: Path) -> dict[str, int]:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def run_demo() -> None:
    demo_path = Path(__file__).with_name("scores_demo.json")
    scores = {"Alice": 95, "Bob": 87}

    save_scores(demo_path, scores)
    print("Saved scores to:", demo_path.name)
    print("Loaded scores:", load_scores(demo_path))


if __name__ == "__main__":
    run_demo()
