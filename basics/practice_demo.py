"""
Practice Demo: Core Python Concepts

Covers:
- Functions and arguments
- Lists, dicts, sets
- File I/O with pathlib + JSON
- Generators
- Decorators
- Simple class usage
"""

from __future__ import annotations

import json
from pathlib import Path
from collections import Counter
from typing import List, Dict, Callable


# ---------------------------
# 1. Basic Functions
# ---------------------------
def add_numbers(a: int, b: int = 10) -> int:
    return a + b


def variable_args(*args: int) -> int:
    return sum(args)


# ---------------------------
# 2. Collections
# ---------------------------
def collections_demo() -> Dict[str, int]:
    data = ["apple", "banana", "apple", "orange", "banana", "apple"]
    counts = Counter(data)
    return counts


def set_demo(nums: List[int]) -> List[int]:
    seen = set(nums)
    return list(seen)


# ---------------------------
# 3. File + JSON Handling
# ---------------------------
def save_data(path: Path, data: dict) -> None:
    path.write_text(json.dumps(data, indent=2), encoding="utf-8")


def load_data(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


# ---------------------------
# 4. Generators
# ---------------------------
def square_generator(n: int):
    for i in range(n):
        yield i * i


# ---------------------------
# 5. Higher-Order Function
# ---------------------------
def apply_function(values: List[int], func: Callable[[int], int]) -> List[int]:
    return [func(v) for v in values]


# ---------------------------
# 6. Decorator Example
# ---------------------------
def debug_decorator(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        print(f"[DEBUG] Calling {func.__name__} with {args}")
        result = func(*args, **kwargs)
        print(f"[DEBUG] Result: {result}")
        return result
    return wrapper


@debug_decorator
def multiply(x: int, y: int) -> int:
    return x * y


# ---------------------------
# 7. Simple Class
# ---------------------------
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def greet(self) -> str:
        return f"Hi, I'm {self.name} and I'm {self.age} years old."


# ---------------------------
# 8. Main Runner
# ---------------------------
def run_demo():
    print("=== Functions ===")
    print(add_numbers(5))
    print(variable_args(1, 2, 3, 4))

    print("\n=== Collections ===")
    print(collections_demo())
    print(set_demo([1, 2, 2, 3, 3, 3]))

    print("\n=== File I/O ===")
    path = Path("demo_data.json")
    save_data(path, {"x": 1, "y": 2})
    print(load_data(path))

    print("\n=== Generators ===")
    print(list(square_generator(5)))

    print("\n=== Higher-Order Function ===")
    print(apply_function([1, 2, 3], lambda x: x * 10))

    print("\n=== Decorators ===")
    print(multiply(3, 4))

    print("\n=== Class ===")
    p = Person("Kevin", 30)
    print(p.greet())


if __name__ == "__main__":
    run_demo()