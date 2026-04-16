"""
Lesson 13: Error Handling and Logging
"""

import logging
from pathlib import Path


# ---------------------------
# Setup logging
# ---------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# ---------------------------
# Example 1: Basic try/except
# ---------------------------
def safe_divide(a: float, b: float) -> float:
    try:
        return a / b
    except ZeroDivisionError:
        logging.error("Attempted division by zero")
        return 0


# ---------------------------
# Example 2: File handling
# ---------------------------
def read_file(path: Path) -> str:
    try:
        return path.read_text()
    except FileNotFoundError:
        logging.warning(f"File not found: {path}")
        return ""


# ---------------------------
# Example 3: Custom exception
# ---------------------------
class InvalidDataError(Exception):
    pass


def process_data(value: int) -> int:
    if value < 0:
        raise InvalidDataError("Value must be positive")
    return value * 2


# ---------------------------
# Demo runner
# ---------------------------
def run_demo():
    print("Safe divide:", safe_divide(10, 0))

    print("\nFile read:")
    print(read_file(Path("missing.txt")))

    print("\nCustom exception:")
    try:
        process_data(-5)
    except InvalidDataError as e:
        logging.error(f"Custom error: {e}")


if __name__ == "__main__":
    run_demo()