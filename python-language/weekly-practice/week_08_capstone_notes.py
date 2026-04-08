"""
Week 8 practice: capstone checklist helper.
"""


def capstone_checklist() -> list[str]:
    return [
        "Add tasks from the command line",
        "List tasks from JSON storage",
        "Complete tasks by id",
        "Delete tasks by id",
        "Handle validation errors",
        "Run tests after each change",
    ]


def run_demo() -> None:
    for item in capstone_checklist():
        print("-", item)


if __name__ == "__main__":
    run_demo()
