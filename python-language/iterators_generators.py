"""
Python iterators and generators: yield, generator expressions,
custom iterators, and lazy evaluation.

Run this file to see practical examples and output.
teaches how Python produces values one at a time instead of building everything up front. 
That’s the core idea behind both iterators and generators: lazy evaluation.
Iterators and Generators
The file starts with generator functions like fibonacci_generator() in iterators_generators.py (line 11) and countdown() in iterators_generators.py (line 19). The key keyword is yield. Unlike return, which ends the function, yield pauses it and remembers its state so the next value can be produced later. That’s why list(fibonacci_generator(10)) gives the first 10 Fibonacci numbers without storing them all inside the function first.

RangeIterator in iterators_generators.py (line 26) 
shows the lower-level iterator protocol. An iterator class needs
 __iter__() and __next__(). __iter__() returns the iterator object,
and __next__() returns the next value or raises StopIteration when
it is done. This is what Python uses under the hood for for loops.
One important learning note: this implementation works well for 
positive steps, but it would not handle negative steps correctly
because it always stops when current >= end. That is a common edge 
case to watch for when writing custom iterators.
Generator expressions in iterators_generators.py (line 49) are a 
concise way to create

Most important ideas to remember

An iterable is something you can loop over.
An iterator is the object that gives the next item.
A generator is a simple way to create an iterator using yield.
yield pauses the function and saves its state.
StopIteration tells Python the iteration is finished.
Generator expressions are lazy; list comprehensions are eager.
Generators are especially useful for large data, pipelines, and streams.

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
    """
    compares list comprehensions and generator expressions. A list
    comprehension like [x * x for x in numbers] builds the whole 
    list immediately. A generator expression like
    (x * x for x in numbers) produces items only as needed.
    That’s why generator expressions are often better for large 
    datasets or one-pass calculations like 
    sum(x * x for x in numbers).
    """
    squares_list = [x * x for x in numbers]
    print('List comprehension result:', squares_list)

    # Generator expression: lazy evaluation
    squares_gen = (x * x for x in numbers)
    print('Generator expression result:', list(squares_gen))

    # Memory-efficient: sum without creating intermediate list
    total = sum(x * x for x in numbers)
    print('Sum using generator expression:', total)

"""
example of laziness. It can produce values forever because it only
 gives you one at a time when you ask for one with next(). The 
 demo wisely limits it to five items instead of trying to turn it 
 into a full list.
"""
def infinite_generator() -> Generator[int, None, None]:
    """Infinite generator example (use with caution)."""
    n = 0
    while True:
        yield n
        n += 1

"""
shows one of the best real uses for generators: chaining steps together.
Each function in the pipeline is a generator that takes an iterable and yields transformed items. This allows you to build complex data processing 
pipelines without ever creating large intermediate
"""
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
