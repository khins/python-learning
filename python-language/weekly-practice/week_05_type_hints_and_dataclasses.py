"""
Week 5 practice: type hints and dataclasses.
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class Lesson:
    title: str
    duration_minutes: int
    completed: bool = False


def find_lesson(title: str, lessons: list[Lesson]) -> Optional[Lesson]:
    for lesson in lessons:
        if lesson.title == title:
            return lesson
    return None


def run_demo() -> None:
    lessons = [
        Lesson("Functions", 35, True),
        Lesson("JSON Files", 40),
    ]
    print("Lesson list:", lessons)
    print("Find lesson:", find_lesson("JSON Files", lessons))


if __name__ == "__main__":
    run_demo()
