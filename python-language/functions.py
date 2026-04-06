"""
Python language functions demo: args, kwargs, defaults, closures,
higher-order functions, and lambdas.

Run this file to see practical examples and output.
"""

from typing import Any, Callable, Dict, Iterable, Tuple

# Function definitions with various argument types and a simple decorator.
def positional_and_keyword(a: int, b: int = 10, *, c: int = 20) -> int:
    """Demonstrate positional args, default values, and keyword-only args."""
    return a + b + c

# Variadic arguments: *args for positional, **kwargs for keyword
def varargs_example(*args: int, **kwargs: int) -> Tuple[int, Dict[str, int]]:
    """Collect arbitrary positional and keyword arguments."""
    total = sum(args)
    return total, kwargs

# Higher-order function: takes a callable and applies it to values
def apply_operation(values: Iterable[int], operation: Callable[[int], int]) -> list[int]:
    """Higher-order function: applies a callable to each item."""
    return [operation(value) for value in values]

# Closure example: make_multiplier returns a function that multiplies by a factor
def make_multiplier(factor: int) -> Callable[[int], int]:
    """Closure example: returns a function that multiplies by factor."""
    def multiplier(n: int) -> int:
        return n * factor
    return multiplier

# Decorator example: a simple wrapper that prints before and after calling a function
def decorator_example(func: Callable[..., Any]) -> Callable[..., Any]:
    """Simple decorator that prints before and after calling func."""
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f'Calling {func.__name__} with {args} and {kwargs}')
        result = func(*args, **kwargs)
        print(f'{func.__name__} returned {result}')
        return result
    return wrapper

# Example of a decorated function
@decorator_example
def decorated_add(a: int, b: int) -> int:
    return a + b

# Lambda examples: anonymous functions for simple operations
def lambda_examples() -> list[int]:
    values = [1, 2, 3, 4, 5]
    squared = list(map(lambda x: x * x, values))
    evens = [x for x in values if (lambda y: y % 2 == 0)(x)]
    return squared + evens


def run_demo() -> None:
    print('positional_and_keyword(5):', positional_and_keyword(5))
    print('positional_and_keyword(5, 7, c=3):', positional_and_keyword(5, 7, c=3))

    total, kwargs = varargs_example(1, 2, 3, alpha=100, beta=200)
    print('varargs_example total:', total)
    print('varargs_example kwargs:', kwargs)

    double = make_multiplier(2)
    triple = make_multiplier(3)
    print('double(10):', double(10))
    print('triple(10):', triple(10))

    print('apply_operation squares:', apply_operation([1, 2, 3], lambda x: x * x))

    print('decorated_add(4, 5):', decorated_add(4, 5))

    print('lambda_examples:', lambda_examples())


if __name__ == '__main__':
    run_demo()
