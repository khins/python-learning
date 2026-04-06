"""
Python iterators and generators: yield, generator expressions,
custom iterators, and lazy evaluation.

Run this file to see practical examples and output.
"""

from typing import Iterator, Generator, Iterable

# Generator function that yields Fibonacci numbers up to n terms.
def fibonacci_generator(n: int) -> Generator[int, None, None]:
    """Generator function that yields Fibonacci numbers up to n terms."""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Another example: a countdown generator
def countdown(start: int) -> Iterator[int]:
    """Generator that counts down from start to 0."""
    while start >= 0:
        yield start
        start -= 1


class RangeIterator:
    """Custom iterator class that mimics range() but with step."""
    def __init__(self, start: int, end: int, step: int = 1):
        self.current = start
        self.end = end
        self.step = step

    def __iter__(self) -> Iterator[int]:
        return self

    def __next__(self) -> int:
        if self.current >= self.end:
            raise StopIteration
        value = self.current
        self.current += self.step
        return value


def generator_expressions() -> None:
    """Demonstrate generator expressions vs list comprehensions."""
    numbers = range(10)

    # List comprehension: creates full list in memory
    squares_list = [x * x for x in numbers]
    print('List comprehension result:', squares_list)

    # Generator expression: lazy evaluation
    squares_gen = (x * x for x in numbers)
    print('Generator expression result:', list(squares_gen))

    # Memory-efficient: sum without creating intermediate list
    total = sum(x * x for x in numbers)
    print('Sum using generator expression:', total)


def infinite_generator() -> Generator[int, None, None]:
    """Infinite generator example (use with caution)."""
    n = 0
    while True:
        yield n
        n += 1


def pipeline_example() -> None:
    """Demonstrate chaining generators in a pipeline."""
    def numbers(n: int) -> Generator[int, None, None]:
        for i in range(n):
            yield i

    def even_only(nums: Iterable[int]) -> Generator[int, None, None]:
        for num in nums:
            if num % 2 == 0:
                yield num

    def multiply_by_10(nums: Iterable[int]) -> Generator[int, None, None]:
        for num in nums:
            yield num * 10

    # Pipeline: numbers -> even_only -> multiply_by_10
    result = list(multiply_by_10(even_only(numbers(10))))
    print('Pipeline result:', result)


def run_demo() -> None:
    print('Fibonacci generator (first 10):', list(fibonacci_generator(10)))
    print('Countdown from 5:', list(countdown(5)))

    print('Custom RangeIterator (0 to 10 step 2):', list(RangeIterator(0, 10, 2)))

    generator_expressions()

    pipeline_example()

    # Infinite generator demo (limited)
    gen = infinite_generator()
    print('Infinite generator (first 5):', [next(gen) for _ in range(5)])


if __name__ == '__main__':
    run_demo()
