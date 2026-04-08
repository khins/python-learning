"""
Week 6 practice: small functions that are easy to test.
"""


def is_even(number: int) -> bool:
    return number % 2 == 0


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def run_demo() -> None:
    print("is_even(4):", is_even(4))
    print("divide(10, 2):", divide(10, 2))


if __name__ == "__main__":
    run_demo()
