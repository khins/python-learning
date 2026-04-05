"""
Core concepts for Python data structures — concise overview and examples.

Topics:
- Built-in types: lists, tuples, sets, dicts
- Mutability vs immutability
- Sequences vs mappings vs unordered collections
- When to use which structure
- Time complexity (big-O) highlights
"""

from collections import deque, Counter, defaultdict


def mutability_examples():

    # mutable: list, dict, set
    lst = [1, 2, 3]
    lst.append(4)  # modifies in-place

    d = {'a': 1}
    d['b'] = 2

    s = {1, 2}
    s.add(3)

    # immutable: tuple, frozenset
    tpl = (1, 2, 3)
    fs = frozenset({1, 2, 3})

    return lst, d, s, tpl, fs


def choosing_structure(use_case: str):

    """Return recommended data structure for a short use-case string."""
    if use_case == 'ordered collection with mutations':
        return 'list or deque (deque for efficient pops from both ends)'
    if use_case == 'fixed sequence':
        return 'tuple'
    if use_case == 'unique items, fast membership':
        return 'set'
    if use_case == 'key -> value lookup':
        return 'dict (or defaultdict/Counter for common patterns)'
    return 'list (default)'


# Quick complexity notes (average-case):
# - list: index O(1), append O(1) amortized, insert/remove O(n)
# - tuple: like list but immutable
# - dict: lookup/insert/delete O(1)
# - set: membership/insert/delete O(1)
# - deque: append/pop both ends O(1)


if __name__ == '__main__':
	print('Mutability examples:', mutability_examples())
	print('Choose for queue:', choosing_structure('ordered collection with mutations'))
	print('Choose for fixed sequence:', choosing_structure('fixed sequence'))
