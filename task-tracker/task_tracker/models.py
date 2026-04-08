from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from task_tracker.errors import TaskValidationError

VALID_PRIORITIES = {"low", "medium", "high"}


@dataclass
class Task:
    id: int
    title: str
    completed: bool = False
    priority: str = "medium"
    due_date: str | None = None

    def __post_init__(self) -> None:
        cleaned_title = self.title.strip()
        if not cleaned_title:
            raise TaskValidationError("Task title cannot be blank")
        if self.priority not in VALID_PRIORITIES:
            raise TaskValidationError(
                f"Priority must be one of: {', '.join(sorted(VALID_PRIORITIES))}"
            )
        self.title = cleaned_title

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "title": self.title,
            "completed": self.completed,
            "priority": self.priority,
            "due_date": self.due_date,
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Task":
        return cls(
            id=int(data["id"]),
            title=str(data["title"]),
            completed=bool(data.get("completed", False)),
            priority=str(data.get("priority", "medium")),
            due_date=data.get("due_date"),
        )
