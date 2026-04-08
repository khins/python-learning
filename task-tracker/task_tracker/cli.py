from __future__ import annotations

import argparse
import os
from pathlib import Path

from task_tracker.errors import TaskNotFoundError, TaskStorageError, TaskValidationError
from task_tracker.models import Task
from task_tracker.storage import TaskStorage
from task_tracker.tracker import TaskTracker

try:
    from rich.console import Console
except ImportError:
    Console = None


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Simple command-line task tracker")
    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("title", help="Task title")
    add_parser.add_argument(
        "--priority",
        default="medium",
        choices=["low", "medium", "high"],
        help="Task priority",
    )
    add_parser.add_argument("--due-date", help="Optional due date string")

    list_parser = subparsers.add_parser("list", help="List tasks")
    list_parser.add_argument("--completed-only", action="store_true")
    list_parser.add_argument("--active-only", action="store_true")

    complete_parser = subparsers.add_parser("complete", help="Mark a task complete")
    complete_parser.add_argument("task_id", type=int)

    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("task_id", type=int)

    return parser


def get_data_path() -> Path:
    env_path = os.getenv("TASK_TRACKER_DATA")
    if env_path:
        return Path(env_path)
    return Path(__file__).resolve().parent.parent / "tasks.json"


def make_tracker() -> TaskTracker:
    return TaskTracker(TaskStorage(get_data_path()))


def print_message(message: str) -> None:
    if Console is not None:
        Console().print(message)
    else:
        print(message)


def render_tasks(tasks: list[Task]) -> None:
    if not tasks:
        print_message("No tasks found.")
        return

    for task in tasks:
        status = "done" if task.completed else "open"
        due_date = f" | due: {task.due_date}" if task.due_date else ""
        print_message(
            f"[{task.id}] {task.title} | status: {status} | priority: {task.priority}{due_date}"
        )


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    tracker = make_tracker()

    try:
        if args.command == "add":
            task = tracker.add_task(args.title, priority=args.priority, due_date=args.due_date)
            print_message(f"Added task {task.id}: {task.title}")
            return 0

        if args.command == "list":
            tasks = tracker.list_tasks(
                completed_only=args.completed_only,
                active_only=args.active_only,
            )
            render_tasks(tasks)
            return 0

        if args.command == "complete":
            task = tracker.complete_task(args.task_id)
            print_message(f"Completed task {task.id}: {task.title}")
            return 0

        if args.command == "delete":
            task = tracker.delete_task(args.task_id)
            print_message(f"Deleted task {task.id}: {task.title}")
            return 0
    except (TaskValidationError, TaskNotFoundError, TaskStorageError) as exc:
        print_message(f"Error: {exc}")
        return 1

    parser.print_help()
    return 1
