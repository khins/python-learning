"""
Tuples & Sets — concise guide, examples and small exercises.

Run this file to see demonstrations and solution outputs.
"""

from collections import namedtuple
from typing import List, Tuple


def tuple_examples() -> Tuple[tuple, tuple]:
    # creation and immutability
    t = (1, 2, 3)
    # packing / unpacking
    a, b, c = t

    # single-element tuple needs a trailing comma
    single = (42,)

    # namedtuple for lightweight records
    Point = namedtuple('Point', ['x', 'y'])
    p = Point(3, 4)

    return t, (a, b, c, single, p)


def set_examples():
    s = {1, 2, 3}
    s.add(4)
    s.discard(10)  # no error if missing

    a = {1, 2, 3}
    b = {3, 4, 5}
    intersection = a & b
    union = a | b
    difference = a - b
    symmetric = a ^ b

    # frozenset is immutable and hashable
    fs = frozenset(a)

    return s, (intersection, union, difference, symmetric, fs)


# Use-cases quick guide
# - tuple: fixed-size, heterogeneous record; use for return values you won't modify
# - set: membership tests, unique elements, set algebra (union/intersection)


def exercises():
    # Exercise 1: convert list to unique sorted list using set
    data = [3, 1, 2, 3, 2, 4]
    unique_sorted = sorted(set(data))

    # Exercise 2: check if one list is subset of another
    a = [1, 2, 3]
    b = [0, 1, 2, 3, 4]
    is_subset = set(a).issubset(b)

    return unique_sorted, is_subset


if __name__ == '__main__':
    print('Tuple examples:', tuple_examples())
    print('Set examples:', set_examples())
    print('Exercises:', exercises())
