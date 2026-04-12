"""
Python context managers: with statement, resource cleanup, custom classes, and
contextlib.contextmanager.

Run this file to see examples and output.
one central idea: a context manager is a safe, structured way to
set something up, use it for a block of code, and then clean it up
automatically. In Python, that usually happens with the with statement.
Big Picture
This file shows two ways to make context managers:

A class-based context manager with __enter__ and __exit__
A function-based context manager using @contextlib.contextmanager
It also shows why they matter:

opening and closing files safely temporarily changing state
handling cleanup even if something goes wrong (suppressing exceptions)
"""

import contextlib
import os
from typing import Iterator, Any

"""
Key ideas:
1. FileOpener: class-based context manager
In context_managers.py (line 13), FileOpener is a custom class that 
works with with.

The key methods are:

__enter__() runs at the start of the with block
__exit__() runs when leaving the block, even if there was an error
Flow:

with FileOpener(path, 'w') as f:
Python calls __enter__()
The file is opened and returned as f
The block runs
Python calls __exit__()
The file is closed.
important detail:
return False in __exit__ means “do not suppress exceptions.” 
If an error happens inside the with block, Python will still raise
it after __exit__ finishes cleanup.
"""
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

    """
    2. Why __exit__ gets exception info
    In context_managers.py (line 26), __exit__ receives:

    exc_type
    exc_value
    traceback
    These are None if no exception happened.

    This lets a context manager decide:

    just clean up and let the error continue
    or clean up and suppress the error
    This file prints the exception type if one occurred, but still 
    returns False, so it only observes the exception rather than 
    swallowing it.
    """
    def __exit__(self, exc_type: Any, exc_value: Any, traceback: Any) -> bool:
        print(f'Closing file {self.path}')
        if self.file:
            self.file.close()
        if exc_type:
            print(f'Handled exception: {exc_type.__name__}')
        return False

"""
3. change_directory: function-based context manager
In context_managers.py (line 35), the file uses
 @contextlib.contextmanager.

This is a simpler way to write a context manager as a 
generator-style function:

code before yield is setup
the yield value becomes the as ... variable
code after yield is cleanup
Here’s the logic:

save the current directory
switch to a new one
yield the current directory
always switch back in finally
That finally block is the safety feature. Even if the code 
inside the with block crashes, the original directory is restored.

This is a really important real-world lesson: context managers
are often used to temporarily change state and then reliably undo
that change.
"""
@contextlib.contextmanager
def change_directory(path: str) -> Iterator[str]:
    """Context manager that temporarily changes the working directory."""
    previous_dir = os.getcwd()
    try:
        os.chdir(path)
        yield os.getcwd()
    finally:
        os.chdir(previous_dir)

"""
4. suppress_errors: selective exception suppression
In suppress_errors catches only
specific exceptions passed into it.

This is a common pattern when you want to ignore certain 
expected errors but still let unexpected ones raise.
"""
@contextlib.contextmanager
def suppress_errors(*exceptions: type[BaseException]) -> Iterator[None]:
    """Context manager that suppresses specific exceptions."""
    try:
        yield
    except exceptions:
        print(f'Suppressed {exceptions}')

"""
5. nested_contexts_example(): stacking context managers
the file nests two with blocks.

What happens:

It prints the directory before entering
It temporarily changes directory
Inside that block, it also suppresses FileNotFoundError
Trying to open a missing file triggers that suppression
After the block ends, the directory is restored
This teaches that context managers can be layered together, and
each one handles its own responsibility.

That is a very Pythonic pattern:

one context manager manages location
another manages error behavior
"""
def nested_contexts_example() -> None:
    print('Outside directory:', os.getcwd())
    with change_directory('.') as current:
        print('Inside directory:', current)
        with suppress_errors(FileNotFoundError):
            open('nonexistent-file.txt')

"""
6. run_demo(): what the file demonstrates
the demo does three things:

writes to a file using FileOpener
reads that file using FileOpener
runs the nested example
"""
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
