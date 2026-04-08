from __future__ import annotations

import json
from pathlib import Path

from task_tracker.errors import TaskStorageError
from task_tracker.models import Task


class TaskStorage:
    def __init__(self, path: Path):
        self.path = path

    def load_tasks(self) -> list[Task]:
        if not self.path.exists():
            return []

        try:
            raw_data = json.loads(self.path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            raise TaskStorageError(f"Invalid JSON in {self.path}") from exc
        except OSError as exc:
            raise TaskStorageError(f"Could not read {self.path}") from exc

        if not isinstance(raw_data, list):
            raise TaskStorageError("Task data must be stored as a list")

        try:
            return [Task.from_dict(item) for item in raw_data]
        except (KeyError, TypeError, ValueError) as exc:
            raise TaskStorageError("Task data has an invalid shape") from exc

    def save_tasks(self, tasks: list[Task]) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        payload = [task.to_dict() for task in tasks]

        try:
            self.path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
        except OSError as exc:
            raise TaskStorageError(f"Could not write {self.path}") from exc
