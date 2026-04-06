"""
Examples of useful types from the `collections` module.

Includes: `deque`, `defaultdict`, `Counter`, `namedtuple`, `OrderedDict`, `ChainMap`.
"""

from collections import deque, defaultdict, Counter, namedtuple, OrderedDict, ChainMap
from typing import List, Dict, Any


def deque_demo():
    dq = deque(maxlen=5)
    for i in range(7):
        dq.append(i)
    # dq now holds last 5 items: 2..6
    dq.appendleft(100)
    dq.rotate(2)
    popped = dq.pop()
    popleft = dq.popleft()
    return dq, popped, popleft


def defaultdict_demo():
    items = [('fruit', 'apple'), ('veg', 'carrot'), ('fruit', 'banana')]
    groups: Dict[str, List[str]] = defaultdict(list)
    for k, v in items:
        groups[k].append(v)
    return groups


def counter_demo():
    data = ['a', 'b', 'a', 'c', 'b', 'a']
    cnt = Counter(data)
    top2 = cnt.most_common(2)
    cnt.update(['b', 'b', 'd'])
    return cnt, top2


def namedtuple_demo():
    Point = namedtuple('Point', ['x', 'y'])
    p = Point(10, 20)
    # access by name or index
    return p, p.x, p[1]


def ordered_dict_demo():
    od = OrderedDict()
    od['one'] = 1
    od['two'] = 2
    od['three'] = 3
    od.move_to_end('one')
    popped_first = od.popitem(last=False)
    return od, popped_first


def chainmap_demo():
    defaults = {'timeout': 30, 'retries': 3}
    cfg = {'retries': 5}
    cm = ChainMap(cfg, defaults)
    # lookup falls back to defaults
    return cm['timeout'], cm['retries']


def exercises():
    # Exercise: fixed-size rolling average using deque
    values = [10, 20, 30, 40, 50]
    window = deque(maxlen=3)
    averages = []
    for v in values:
        window.append(v)
        averages.append(sum(window) / len(window))

    # Exercise: top-k frequent using Counter (wrapper)
    items = ['x', 'y', 'x', 'z', 'x', 'y']
    top = Counter(items).most_common(2)

    return averages, top

from collections import namedtuple

def namedtuple_example():
    Point = namedtuple('Point', ['x', 'y'])
    
    p = Point(10, 20)
    
    return {
        "object": p,
        "by_attr": p.x,
        "by_index": p[1]
    }

from dataclasses import dataclass

def dataclass_example():
    
    @dataclass
    class Point:
        x: int
        y: int

    p = Point(10, 20)
    
    # mutate value
    p.x = 30

    return {
        "object": p,
        "x": p.x,
        "y": p.y
    }

from typing import TypedDict

def typeddict_example():
    
    class Point(TypedDict):
        x: int
        y: int

    p: Point = {"x": 10, "y": 20}
    
    # mutate like normal dict
    p["x"] = 30

    return {
        "object": p,
        "x": p["x"],
        "y": p["y"]
    }


if __name__ == '__main__':
    print('Deque demo:', deque_demo())
    print('Defaultdict groups:', defaultdict_demo())
    print('Counter demo:', counter_demo())
    print('Namedtuple demo:', namedtuple_demo())
    print('OrderedDict demo:', ordered_dict_demo())
    print('ChainMap demo:', chainmap_demo())
    print('Exercises solutions:', exercises())
    print("=== namedtuple ===")
    print(namedtuple_example())
    
    print("\n=== dataclass ===")
    print(dataclass_example())
    
    print("\n=== TypedDict ===")
    print(typeddict_example())
