"""
Python context managers: with statement, resource cleanup, custom classes, and
contextlib.contextmanager.

Run this file to see examples and output.
"""

import contextlib
import os
from typing import Iterator, Any


class FileOpener:
    """Custom context manager using __enter__ and __exit__."""

    def __init__(self, path: str, mode: str = 'r'):
        self.path = path
        self.mode = mode
        self.file = None

    def __enter__(self):
        print(f'Opening file {self.path}')
        self.file = open(self.path, self.mode)
        return self.file

    def __exit__(self, exc_type: Any, exc_value: Any, traceback: Any) -> bool:
        print(f'Closing file {self.path}')
        if self.file:
            self.file.close()
        if exc_type:
            print(f'Handled exception: {exc_type.__name__}')
        return False


@contextlib.contextmanager
def change_directory(path: str) -> Iterator[str]:
    """Context manager that temporarily changes the working directory."""
    previous_dir = os.getcwd()
    try:
        os.chdir(path)
        yield os.getcwd()
    finally:
        os.chdir(previous_dir)


@contextlib.contextmanager
def suppress_errors(*exceptions: type[BaseException]) -> Iterator[None]:
    """Context manager that suppresses specific exceptions."""
    try:
        yield
    except exceptions:
        print(f'Suppressed {exceptions}')


def nested_contexts_example() -> None:
    print('Outside directory:', os.getcwd())
    with change_directory('.') as current:
        print('Inside directory:', current)
        with suppress_errors(FileNotFoundError):
            open('nonexistent-file.txt')


def run_demo() -> None:
    path = 'context_demo.txt'
    with FileOpener(path, 'w') as f:
        f.write('Hello from context managers!\n')

    with FileOpener(path, 'r') as f:
        print('Read content:', f.read().strip())

    nested_contexts_example()

    print('Done with context manager examples.')


if __name__ == '__main__':
    run_demo()
