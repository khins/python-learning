"""
Complexity & best practices for Python data structures and algorithms.

Includes a short Big-O reference, concrete examples, and concise best-practice rules.
"""

from typing import List


# Quick Big-O reference (average / typical):
# - O(1): dict/set lookup, append (amortized), index access
# - O(log n): binary search (bisect) on sorted arrays
# - O(n): scanning a list, building a dict from n items
# - O(n log n): efficient sorts (Timsort)
# - O(n^2): nested loops that touch pairs of items


def linear_sum(xs: List[int]) -> int:
    # O(n) — single pass
    total = 0
    for x in xs:
        total += x
    return total


def quadratic_pairs(xs: List[int]) -> List[tuple]:
    # O(n^2) — all pairs
    out = []
    for i in range(len(xs)):
        for j in range(i + 1, len(xs)):
            out.append((xs[i], xs[j]))
    return out


def dict_lookup_vs_list_search(xs: List[int], target: int):
    # list search: O(n)
    found_in_list = target in xs

    # dict/set lookup: O(1) average
    s = set(xs)
    found_in_set = target in s
    return found_in_list, found_in_set


# Best practice rules (short):
# 1) Choose the right abstraction: use dict for key-value, list for ordered sequence, set for membership/unique.
# 2) Prefer built-ins and library functions (they are fast and well-tested).
# 3) Avoid growing lists in tight loops when possible; preallocate or use comprehensions.
# 4) For large data, favor generators/iterators to reduce peak memory.
# 5) Measure with a profiler when in doubt; optimize the hot path.
# 6) Keep complexity visible in code reviews: annotate or document expected complexity.


def tips_examples():
    # Example: using Counter for frequency counts (fast C-optimized)
    from collections import Counter

    data = ['a'] * 1000 + ['b'] * 500
    counts = Counter(data)  # efficient

    # Example: sorting once instead of sorting repeatedly
    xs = list(range(1000, 0, -1))
    xs.sort()  # O(n log n) once

    # Example: use set for membership tests inside loop
    haystack = set(range(10000))
    needles = [5, 9999, -1]
    membership = [n in haystack for n in needles]  # O(1) per check

    return counts, membership


if __name__ == '__main__':
    xs = list(range(10))
    print('linear_sum:', linear_sum(xs))
    print('quadratic_pairs (len):', len(quadratic_pairs(xs)))
    print('lookup (list,set):', dict_lookup_vs_list_search(xs, 7))
    print('tips examples:', tips_examples())
