"""
Python decorators: function decorators, class decorators,
parameterized decorators, and metadata preservation.

Run this file to see practical examples and output.
🧠 Big picture

This file demonstrates:

Function decorators
Metadata preservation (functools.wraps)
Timing & logging
Memoization (caching)
Parameterized decorators
Class decorators
"""

# functools is used for metadata preservation in decorators
# callable types and time for timing decorator
import functools
import time
from typing import Any, Callable

# What it does

# Wraps a function to print before and after execution.
def simple_decorator(func: Callable[..., Any]) -> Callable[..., Any]:
    """Basic decorator that prints before and after function calls."""
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f'Calling {func.__name__}')
        result = func(*args, **kwargs)
        print(f'{func.__name__} returned {result}')
        return result
    return wrapper

# What it does
# Measures execution time
# Prints duration
def timing_decorator(func: Callable[..., Any]) -> Callable[..., Any]:
    """Decorator that measures and prints execution time."""
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'{func.__name__} took {end - start:.4f} seconds')
        return result
    return wrapper

# Key idea:

# Store results of previous calls in a cache (dict)
def cache_decorator(func: Callable[..., Any]) -> Callable[..., Any]:
    """Simple memoization decorator using a dict cache."""
    cache: dict[tuple, Any] = {}

    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (args, tuple(sorted(kwargs.items())))
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return wrapper

# Key idea:
# Decorator with arguments to repeat function calls
def parameterized_decorator(repeat: int) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """Parameterized decorator that repeats function calls."""
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> list[Any]:
            results = []
            for _ in range(repeat):
                results.append(func(*args, **kwargs))
            return results
        return wrapper
    return decorator

# What it does
# Modifies a class after it's defined to add a new method.
def class_decorator(cls: type) -> type:
    """Class decorator that adds a method to the class."""
    cls.new_method = lambda self: f'Hello from {cls.__name__}!'
    return cls


@class_decorator
class ExampleClass:
    def __init__(self, value: int):
        self.value = value

    def get_value(self) -> int:
        return self.value


@simple_decorator
def greet(name: str) -> str:
    return f'Hello, {name}!'


@timing_decorator
def slow_function(n: int) -> int:
    time.sleep(0.1)
    return n * 2


@cache_decorator
def fibonacci(n: int) -> int:
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


@parameterized_decorator(3)
def random_number() -> float:
    import random
    return random.random()


def run_demo() -> None:
    print('Simple decorator:')
    print(greet('World'))

    print('\nTiming decorator:')
    print('Result:', slow_function(5))

    print('\nCache decorator (Fibonacci):')
    print('fib(10):', fibonacci(10))
    print('fib(10) again (cached):', fibonacci(10))

    print('\nParameterized decorator (repeat 3 times):')
    print('Random numbers:', random_number())

    print('\nClass decorator:')
    obj = ExampleClass(42)
    print('Value:', obj.get_value())
    print('New method:', obj.new_method())


if __name__ == '__main__':
    run_demo()
