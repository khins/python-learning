from __future__ import annotations

from task_tracker.errors import TaskNotFoundError
from task_tracker.models import Task
from task_tracker.storage import TaskStorage


class TaskTracker:
    def __init__(self, storage: TaskStorage):
        self.storage = storage

    def list_tasks(
        self,
        *,
        completed_only: bool = False,
        active_only: bool = False,
    ) -> list[Task]:
        tasks = self.storage.load_tasks()
        if completed_only:
            return [task for task in tasks if task.completed]
        if active_only:
            return [task for task in tasks if not task.completed]
        return tasks

    def add_task(
        self,
        title: str,
        *,
        priority: str = "medium",
        due_date: str | None = None,
    ) -> Task:
        tasks = self.storage.load_tasks()
        task = Task(
            id=self._next_id(tasks),
            title=title,
            priority=priority,
            due_date=due_date,
        )
        tasks.append(task)
        self.storage.save_tasks(tasks)
        return task

    def complete_task(self, task_id: int) -> Task:
        tasks = self.storage.load_tasks()
        task = self._find_task(task_id, tasks)
        task.completed = True
        self.storage.save_tasks(tasks)
        return task

    def delete_task(self, task_id: int) -> Task:
        tasks = self.storage.load_tasks()
        task = self._find_task(task_id, tasks)
        remaining_tasks = [item for item in tasks if item.id != task_id]
        self.storage.save_tasks(remaining_tasks)
        return task

    @staticmethod
    def _next_id(tasks: list[Task]) -> int:
        return max((task.id for task in tasks), default=0) + 1

    @staticmethod
    def _find_task(task_id: int, tasks: list[Task]) -> Task:
        for task in tasks:
            if task.id == task_id:
                return task
        raise TaskNotFoundError(f"Task with id {task_id} was not found")
