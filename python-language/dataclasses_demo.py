"""
Python dataclasses: @dataclass decorator, defaults, immutability, field().

Run this file to see examples and output.
"""

from dataclasses import dataclass, field
from typing import List


@dataclass
class Point:
    """Simple dataclass with x and y coordinates."""
    x: float
    y: float

    def distance_from_origin(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5


@dataclass
class Person:
    """Dataclass with default values."""
    name: str
    age: int = 0
    email: str = "unknown@example.com"

    def __post_init__(self):
        if self.age < 0:
            raise ValueError("Age cannot be negative")


@dataclass
class Team:
    """Dataclass with mutable default using field()."""
    name: str
    members: List[str] = field(default_factory=list)

    def add_member(self, member: str) -> None:
        self.members.append(member)


@dataclass(frozen=True)
class ImmutableConfig:
    """Frozen dataclass (immutable)."""
    host: str
    port: int
    debug: bool = False

    def connection_string(self) -> str:
        return f"{self.host}:{self.port}"


@dataclass
class Config:
    """Dataclass with field() to exclude from comparison."""
    name: str
    value: str
    internal_id: int = field(repr=False, compare=False)


def run_demo() -> None:
    # Simple dataclass
    p = Point(3.0, 4.0)
    print('Point:', p)
    print('Distance from origin:', p.distance_from_origin())

    # Defaults
    person1 = Person("Alice", 30)
    person2 = Person("Bob")  # uses defaults
    print('Person 1:', person1)
    print('Person 2:', person2)

    # Mutable default with field()
    team1 = Team("A-Team")
    team1.add_member("John")
    team1.add_member("Jane")
    team2 = Team("B-Team")
    print('Team 1:', team1)
    print('Team 2:', team2)  # empty, not shared with team1

    # Frozen dataclass
    cfg = ImmutableConfig("localhost", 8080)
    print('Config:', cfg)
    print('Connection string:', cfg.connection_string())
    try:
        cfg.port = 9000  # type: ignore
    except Exception as e:
        print('Cannot modify frozen dataclass:', type(e).__name__)

    # Field exclusions
    config = Config("db_config", "production", 12345)
    print('Config:', config)


if __name__ == '__main__':
    run_demo()
