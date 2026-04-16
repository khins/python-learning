"""
Lesson 13: Error Handling and Logging
🧠 Big picture

This file teaches how to handle errors safely and log what’s 
happening instead of crashing or blindly printing.
Production-ready alternative to print
Supports levels: DEBUG, INFO, WARNING, ERROR  
“Fail fast” when input is invalid  
"""

import logging
from pathlib import Path


# ---------------------------
# Setup logging
# Sets global logging behavior
# ---------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# ---------------------------
# Example 1: Basic try/except
# Divide two numbers safely without crashing
# ---------------------------
def safe_divide(a: float, b: float) -> float:
    try:
        return a / b
    # Instead of crashing → logs error
    # Returns fallback value (0)
    except ZeroDivisionError:
        logging.error("Attempted division by zero")
        return 0


# ---------------------------
# Example 2: File handling
# Safely read a file without crashing if it’s missing
# ---------------------------
def read_file(path: Path) -> str:
    try:
        return path.read_text()
# File exists → returns contents
# File missing → logs warning + returns empty string
    except FileNotFoundError:
        logging.warning(f"File not found: {path}")
        return ""


# ---------------------------
# Example 3: Custom exception
# Your own error type for specific cases
# Makes errors meaningful
# Easier to catch specific problems
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

# 🏁 8. Entry point
if __name__ == "__main__":
    run_demo()