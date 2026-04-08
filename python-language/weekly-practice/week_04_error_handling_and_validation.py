"""
Week 4 practice: validation and custom exceptions.
"""


class InputValidationError(Exception):
    """Raised when provided input is invalid."""


def parse_menu_choice(value: str) -> int:
    cleaned = value.strip()
    if not cleaned:
        raise InputValidationError("Menu choice cannot be blank")

    try:
        number = int(cleaned)
    except ValueError as exc:
        raise InputValidationError("Menu choice must be a number") from exc

    if number not in {1, 2, 3}:
        raise InputValidationError("Menu choice must be 1, 2, or 3")

    return number


def run_demo() -> None:
    for value in ["1", "  ", "abc", "9"]:
        try:
            print(value, "->", parse_menu_choice(value))
        except InputValidationError as exc:
            print(value, "->", exc)


if __name__ == "__main__":
    run_demo()
