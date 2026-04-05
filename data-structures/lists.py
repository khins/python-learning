"""
Lists: usage & common methods with examples and small exercises.

Run this file to see demo output and solutions to the tiny exercises.
"""

from typing import List


def create_examples() -> List[int]:
    # creation
    a = [1, 2, 3]
    b = list(range(4, 7))
    c = [0] * 5  # repeated values
    return a, b, c


def indexing_and_slicing():
    lst = ['a', 'b', 'c', 'd', 'e']
    first = lst[0]
    last = lst[-1]
    middle = lst[1:4]  # slice [start:stop]
    step = lst[::2]
    return first, last, middle, step


def mutating_methods_demo():
    lst = [3, 1, 4]
    lst.append(2)       # [3,1,4,2]
    lst.extend([9, 8])  # [3,1,4,2,9,8]
    lst.insert(0, 7)    # [7,3,1,4,2,9,8]
    popped = lst.pop()  # removes and returns last element (8)
    lst.remove(1)       # remove first occurrence of 1
    idx = lst.index(4)  # find position of 4
    cnt = lst.count(3)  # count occurrences
    lst.sort()          # sorts in-place
    lst.reverse()       # reverse order in-place
    copy = lst.copy()   # shallow copy
    return lst, popped, idx, cnt, copy


def comprehension_examples():
    nums = [1, 2, 3, 4, 5]
    squares = [n * n for n in nums]
    evens = [n for n in nums if n % 2 == 0]
    pairs = [(x, y) for x in nums for y in nums if x < y]
    return squares, evens, pairs


# Complexity notes (average-case):
# - index access: O(1)
# - append: O(1) amortized
# - insert/remove at arbitrary index: O(n)
# - slice: O(k) where k = length of slice


def exercises():
    # Exercise 1: remove duplicates while preserving order
    data = [3, 1, 2, 3, 2, 4]

    def remove_duplicates_preserve_order(lst):
        seen = set()
        out = []
        for x in lst:
            if x not in seen:
                seen.add(x)
                out.append(x)
        return out

    # Exercise 2: flatten a nested list of depth 1
    nested = [[1, 2], [3], [4, 5]]

    def flatten_once(nested_list):
        return [x for sub in nested_list for x in sub]

    return remove_duplicates_preserve_order(data), flatten_once(nested)


if __name__ == '__main__':
    print('Create examples:', create_examples())
    print('Index/slice:', indexing_and_slicing())
    print('Mutating methods demo:', mutating_methods_demo())
    print('Comprehensions:', comprehension_examples())
    print('Exercises solutions:', exercises())
