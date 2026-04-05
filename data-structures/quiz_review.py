"""
Quiz and review for Python data structures.

Run this file to see questions and answers. Covers all topics from the learning plan.
"""

from typing import List, Tuple


def quiz_questions() -> List[Tuple[str, str]]:
    return [
        ("What are the main built-in data structures in Python?", "Lists, tuples, sets, dictionaries."),
        ("Which data structures are mutable?", "Lists, sets, dictionaries."),
        ("Which data structures are immutable?", "Tuples, frozensets."),
        ("What's the time complexity of list append?", "O(1) amortized."),
        ("What's the time complexity of list insert at index 0?", "O(n)."),
        ("How do you create a set from a list?", "set(my_list)."),
        ("What's the difference between tuple and list?", "Tuple is immutable, list is mutable."),
        ("How do you access dictionary values safely?", "Use .get(key, default) or check 'key in dict'."),
        ("What does Counter do?", "Counts frequency of elements in an iterable."),
        ("What does defaultdict do?", "Provides default values for missing keys."),
        ("What's the advantage of deque over list?", "Efficient append/pop from both ends."),
        ("What's Big-O for dict lookup?", "O(1) average case."),
        ("What's Big-O for set membership test?", "O(1) average case."),
        ("How to remove duplicates from a list while preserving order?", "Use a set to track seen items."),
        ("What's the purpose of namedtuple?", "Lightweight class for storing data with named fields."),
        ("How to merge two dictionaries?", "Use {**d1, **d2} or dict.update()."),
        ("What's the time complexity of sorting a list?", "O(n log n)."),
        ("How to group items by a key?", "Use defaultdict(list)."),
        ("What's ChainMap used for?", "Combining multiple dicts with fallback lookup."),
        ("How to get top-k most common elements?", "Use Counter.most_common(k)."),
    ]


def run_quiz() -> None:
    questions = quiz_questions()
    print("Python Data Structures Quiz")
    print("=" * 40)
    for i, (q, a) in enumerate(questions, 1):
        print(f"{i}. {q}")
        print(f"   Answer: {a}")
        print()


if __name__ == '__main__':
    run_quiz()