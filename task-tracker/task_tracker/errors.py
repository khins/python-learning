class TaskTrackerError(Exception):
    """Base exception for the task tracker."""


class TaskValidationError(TaskTrackerError):
    """Raised when task data is invalid."""


class TaskNotFoundError(TaskTrackerError):
    """Raised when a task id cannot be found."""


class TaskStorageError(TaskTrackerError):
    """Raised when task data cannot be loaded or saved."""
