from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "task-tracker"))

from task_tracker.errors import TaskNotFoundError, TaskStorageError, TaskValidationError
from task_tracker.storage import TaskStorage
from task_tracker.tracker import TaskTracker


class TaskTrackerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp_dir.cleanup)
        self.data_path = Path(self.temp_dir.name) / "tasks.json"
        self.tracker = TaskTracker(TaskStorage(self.data_path))

    def test_add_task_saves_to_json(self) -> None:
        task = self.tracker.add_task("Study Python", priority="high")

        self.assertEqual(task.id, 1)
        self.assertTrue(self.data_path.exists())
        saved_text = self.data_path.read_text(encoding="utf-8")
        self.assertIn("Study Python", saved_text)
        self.assertIn('"priority": "high"', saved_text)

    def test_blank_task_title_raises_validation_error(self) -> None:
        with self.assertRaises(TaskValidationError):
            self.tracker.add_task("   ")

    def test_complete_task_marks_task_done(self) -> None:
        self.tracker.add_task("Write tests")
        completed = self.tracker.complete_task(1)

        self.assertTrue(completed.completed)
        listed = self.tracker.list_tasks(completed_only=True)
        self.assertEqual(len(listed), 1)
        self.assertEqual(listed[0].id, 1)

    def test_delete_task_removes_it_from_storage(self) -> None:
        self.tracker.add_task("One")
        self.tracker.add_task("Two")

        deleted = self.tracker.delete_task(1)

        self.assertEqual(deleted.title, "One")
        remaining = self.tracker.list_tasks()
        self.assertEqual(len(remaining), 1)
        self.assertEqual(remaining[0].title, "Two")

    def test_missing_task_raises_not_found_error(self) -> None:
        with self.assertRaises(TaskNotFoundError):
            self.tracker.complete_task(99)

    def test_invalid_json_raises_storage_error(self) -> None:
        self.data_path.write_text("{not valid json", encoding="utf-8")

        with self.assertRaises(TaskStorageError):
            self.tracker.list_tasks()


if __name__ == "__main__":
    unittest.main()
