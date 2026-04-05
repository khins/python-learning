"""
Dictionaries: common patterns, idioms and examples.

Run this file to see demos and small exercise solutions.
"""

from collections import defaultdict, Counter, OrderedDict
from typing import Dict, List, Any


def creation_examples():
    a = {'x': 1, 'y': 2}
    b = dict(a=3, b=4)
    pairs = [('k1', 10), ('k2', 20)]
    c = dict(pairs)
    return a, b, c


def access_and_methods():
    d = {'a': 1, 'b': 2}
    # safe access
    val = d.get('c', 0)
    # set default if missing
    d.setdefault('c', 3)
    # iterate
    keys = list(d.keys())
    items = list(d.items())
    values = list(d.values())
    # pop
    popped = d.pop('b', None)
    return val, d, keys, items, values, popped


def common_patterns():
    data = ['apple', 'banana', 'apple', 'orange', 'banana']

    # frequency counts: Counter
    freq = Counter(data)

    # grouping by a key: defaultdict(list)
    items = [('fruit', 'apple'), ('fruit', 'banana'), ('veg', 'carrot')]
    groups: Dict[str, List[str]] = defaultdict(list)
    for k, v in items:
        groups[k].append(v)

    # invert mapping while collecting duplicates
    mapping = {'a': 1, 'b': 2, 'c': 1}
    inv = defaultdict(list)
    for k, v in mapping.items():
        inv[v].append(k)

    # merge dictionaries (py3.9+: | operator)
    d1 = {'x': 1}
    d2 = {'y': 2}
    merged = {**d1, **d2}

    # ordered behavior: insertion order guaranteed in CPython3.7+
    od = OrderedDict()
    od['first'] = 1
    od['second'] = 2

    return freq, groups, inv, merged, od


def memoization_example():
    cache: Dict[int, int] = {}

    def fib(n: int) -> int:
        if n < 2:
            return n
        if n in cache:
            return cache[n]
        cache[n] = fib(n - 1) + fib(n - 2)
        return cache[n]

    return fib(10), cache


def exercises():
    # Exercise 1: count words in text
    text = 'one two two three three three'
    word_counts = Counter(text.split())

    # Exercise 2: group people by age
    people = [('Alice', 30), ('Bob', 25), ('Carol', 30)]
    by_age: Dict[int, List[str]] = defaultdict(list)
    for name, age in people:
        by_age[age].append(name)

    # Exercise 3: flatten nested dict of lists
    nested = {'a': [1, 2], 'b': [3]}
    flat = [x for lst in nested.values() for x in lst]

    return word_counts, by_age, flat


if __name__ == '__main__':
    print('Creation examples:', creation_examples())
    print('Access/methods demo:', access_and_methods())
    print('Common patterns:', common_patterns())
    print('Memoization (fib(10)) and cache:', memoization_example())
    print('Exercises solutions:', exercises())
