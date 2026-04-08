"""
Week 1 practice: functions and core data structures.
"""


def calculate_average(scores: list[int]) -> float:
    return sum(scores) / len(scores) if scores else 0.0


def build_contact_lookup(names: list[str], numbers: list[str]) -> dict[str, str]:
    return {name: number for name, number in zip(names, numbers)}


def unique_words(words: list[str]) -> set[str]:
    return {word.lower() for word in words}


def total_cart(items: list[tuple[str, float]]) -> float:
    return sum(price for _, price in items)


def run_demo() -> None:
    scores = [90, 82, 100, 88]
    names = ["Alice", "Bob", "Chris"]
    numbers = ["555-1000", "555-2000", "555-3000"]
    items = [("Notebook", 4.5), ("Pen", 1.25), ("Bag", 15.0)]

    print("Average:", calculate_average(scores))
    print("Contacts:", build_contact_lookup(names, numbers))
    print("Unique words:", unique_words(["Python", "python", "Loops"]))
    print("Cart total:", total_cart(items))


if __name__ == "__main__":
    run_demo()
