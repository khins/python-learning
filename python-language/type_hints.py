"""
Python type hints: typing module, generics, protocols, and static checking.

Run this file to see examples and output.

Basic function: def add_numbers(a: int, b: int) -> int:
Optional value: age: Optional[int] means int | None
Union of types: value: Union[int, str, float]
Generic type variable: T = TypeVar('T')
Generic list function: def first_item(items: List[T]) -> Optional[T]:
Generic class: class Stack(Generic[T]):
Protocol: define required behavior, not inheritance
Callable: Callable[[int], int] means takes int, returns int

Quick memorize-this rules

Optional[X] means maybe None.
Union[A, B] means either type is allowed.
TypeVar keeps input/output types connected.
Generic[T] makes reusable typed classes.
Protocol means “anything with this method shape is valid.”
Callable[[A], B] describes a function signature.
"""

from typing import List, Dict, Optional, Union, Callable, Protocol, TypeVar, Generic
import math


# Basic type hints
def add_numbers(a: int, b: int) -> int:
    """Add two integers."""
    return a + b


def greet(name: str, age: Optional[int] = None) -> str:
    """Greet a person, optionally with age."""
    if age is not None:
        return f"Hello {name}, you are {age} years old!"
    return f"Hello {name}!"


# Union types
def process_value(value: Union[int, str, float]) -> str:
    """Process different types of values."""
    if isinstance(value, int):
        return f"Integer: {value}"
    elif isinstance(value, str):
        return f"String: {value}"
    elif isinstance(value, float):
        return f"Float: {value}"
    return "Unknown type"


# Generics
T = TypeVar('T')


def first_item(items: List[T]) -> Optional[T]:
    """Get the first item from a list, or None if empty."""
    return items[0] if items else None


class Stack(Generic[T]):
    """Generic stack implementation."""

    def __init__(self):
        self.items: List[T] = []

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> Optional[T]:
        return self.items.pop() if self.items else None

    def peek(self) -> Optional[T]:
        return self.items[-1] if self.items else None


# Protocol for duck typing
class Drawable(Protocol):
    def draw(self) -> str:
        ...


class Circle:
    def __init__(self, radius: float):
        self.radius = radius

    def draw(self) -> str:
        return f"Drawing circle with radius {self.radius}"


class Square:
    def __init__(self, side: float):
        self.side = side

    def draw(self) -> str:
        return f"Drawing square with side {self.side}"


def render_shape(shape: Drawable) -> None:
    """Render any drawable shape."""
    print(shape.draw())


# Callable types
def apply_function(func: Callable[[int], int], value: int) -> int:
    """Apply a function to a value."""
    return func(value)


def run_demo() -> None:
    # Basic types
    result = add_numbers(5, 3)
    print('Add numbers:', result)

    greeting1 = greet("Alice")
    greeting2 = greet("Bob", 25)
    print('Greetings:', greeting1, greeting2)

    # Union
    print('Process value (int):', process_value(42))
    print('Process value (str):', process_value("hello"))
    print('Process value (float):', process_value(3.14))

    # Generics
    numbers = [1, 2, 3, 4, 5]
    first = first_item(numbers)
    print('First item:', first)

    stack = Stack[str]()
    stack.push("hello")
    stack.push("world")
    print('Stack peek:', stack.peek())
    print('Stack pop:', stack.pop())
    print('Stack pop:', stack.pop())

    # Protocol
    circle = Circle(5.0)
    square = Square(4.0)
    render_shape(circle)
    render_shape(square)

    # Callable
    doubled = apply_function(lambda x: x * 2, 10)
    squared = apply_function(lambda x: x ** 2, 5)
    print('Doubled:', doubled)
    print('Squared:', squared)


if __name__ == '__main__':
    run_demo()
