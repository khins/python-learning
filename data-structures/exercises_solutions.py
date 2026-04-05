"""
Exercises and solutions for Python data structures.

Includes small practice problems covering lists, tuples, sets, dicts,
collections, and complexity awareness.
"""

from collections import Counter, defaultdict, deque, ChainMap
from typing import List, Tuple, Dict


def exercise_remove_duplicates(xs: List[int]) -> List[int]:
    seen = set()
    result = []
    for x in xs:
        if x not in seen:
            seen.add(x)
            result.append(x)
    return result


def exercise_flatten_once(nested: List[List[int]]) -> List[int]:
    return [item for sublist in nested for item in sublist]


def exercise_rotate_list(nums: List[int], shift: int) -> List[int]:
    n = len(nums)
    shift = shift % n if n else 0
    return nums[-shift:] + nums[:-shift] if shift else nums[:]


def exercise_tuple_swap(values: Tuple[int, int]) -> Tuple[int, int]:
    a, b = values
    return b, a


def exercise_unique_sorted(xs: List[int]) -> List[int]:
    return sorted(set(xs))


def exercise_count_words(text: str) -> Dict[str, int]:
    return dict(Counter(text.split()))


def exercise_group_by_age(people: List[Tuple[str, int]]) -> Dict[int, List[str]]:
    grouped: Dict[int, List[str]] = defaultdict(list)
    for name, age in people:
        grouped[age].append(name)
    return dict(grouped)


def exercise_rolling_average(values: List[float], window_size: int) -> List[float]:
    window = deque(maxlen=window_size)
    averages = []
    for value in values:
        window.append(value)
        averages.append(sum(window) / len(window))
    return averages


def exercise_top_k(items: List[str], k: int) -> List[Tuple[str, int]]:
    return Counter(items).most_common(k)


def exercise_config_override(user: Dict[str, int], defaults: Dict[str, int]) -> ChainMap:
    return ChainMap(user, defaults)


def complexity_check(xs: List[int], target: int) -> Tuple[bool, bool]:
    found_in_list = target in xs
    found_in_set = target in set(xs)
    return found_in_list, found_in_set


def run_all() -> None:
    print('Remove duplicates:', exercise_remove_duplicates([3, 1, 2, 3, 2, 4]))
    print('Flatten once:', exercise_flatten_once([[1, 2], [3], [4, 5]]))
    print('Rotate list by 2:', exercise_rotate_list([1, 2, 3, 4, 5], 2))
    print('Tuple swap:', exercise_tuple_swap((7, 11)))
    print('Unique sorted:', exercise_unique_sorted([3, 1, 2, 3, 2, 4]))
    print('Count words:', exercise_count_words('one two two three three three'))
    print('Group by age:', exercise_group_by_age([('Alice', 30), ('Bob', 25), ('Carol', 30)]))
    print('Rolling average:', exercise_rolling_average([10.0, 20.0, 30.0, 40.0], 3))
    print('Top k:', exercise_top_k(['x', 'y', 'x', 'z', 'x', 'y'], 2))
    print('Config override:', dict(exercise_config_override({'retries': 5}, {'timeout': 30, 'retries': 3})))
    print('Complexity check:', complexity_check(list(range(10)), 7))


if __name__ == '__main__':
    run_all()
