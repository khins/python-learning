"""
Python error handling: try/except, else/finally, custom exceptions, and cleanup.

Run this file to see practical examples and output.
"""

from typing import List


class ValidationError(Exception):
    """Custom exception for validation failures."""
    pass


class NotFoundError(Exception):
    """Custom exception when an item is not found."""
    pass


def divide_numbers(a: float, b: float) -> float:
    """Divide two numbers, handling division by zero."""
    try:
        return a / b
    except ZeroDivisionError as exc:
        print('Caught ZeroDivisionError')
        raise ValueError('Cannot divide by zero') from exc


def parse_int(value: str) -> int:
    """Parse an integer, handling invalid input."""
    try:
        return int(value)
    except ValueError as exc:
        raise ValidationError(f'Invalid integer: {value}') from exc


def find_item(items: List[str], target: str) -> str:
    """Find an item and raise NotFoundError when missing."""
    for item in items:
        if item == target:
            return item
    raise NotFoundError(f'Item {target!r} not found')


def safe_open(path: str):
    """Demonstrate else and finally in exception handling."""
    file = None
    try:
        file = open(path, 'r')
    except FileNotFoundError:
        print('File not found:', path)
        return None
    else:
        print('File opened successfully')
        content = file.read().strip()
        return content
    finally:
        if file:
            print('Closing file in finally')
            file.close()


def nested_exception_example(value: int) -> None:
    """Demonstrate exception chaining and cleanup."""
    try:
        if value < 0:
            raise ValidationError('Value must be non-negative')
        result = 10 / value
        print('Result:', result)
    except ValidationError as exc:
        print('Validation error:', exc)
    except ZeroDivisionError as exc:
        print('Zero division error, chaining to ValueError')
        raise ValueError('Cannot compute with zero') from exc
    finally:
        print('Nested exception cleanup complete')


def run_demo() -> None:
    # Division
    try:
        print('Divide 10 by 2:', divide_numbers(10, 2))
        print('Divide 10 by 0:')
        divide_numbers(10, 0)
    except ValueError as exc:
        print('Handled error:', exc)

    # Parsing
    for text in ['5', 'abc', '42']:
        try:
            value = parse_int(text)
            print(f'Parsed {text}:', value)
        except ValidationError as exc:
            print('Validation error:', exc)

    # Not found
    try:
        print('Find item:', find_item(['apple', 'banana'], 'banana'))
        find_item(['apple', 'banana'], 'orange')
    except NotFoundError as exc:
        print('Not found error:', exc)

    # Safe open
    print('Safe open:', safe_open('context_demo.txt'))
    print('Safe open missing:', safe_open('missing-file.txt'))

    # Nested exception example
    try:
        nested_exception_example(0)
    except ValueError as exc:
        print('Chained error:', exc)


if __name__ == '__main__':
    run_demo()
