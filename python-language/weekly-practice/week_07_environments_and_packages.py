"""
Week 7 practice: understanding environments and third-party imports.
"""

from importlib.util import find_spec


def package_available(package_name: str) -> bool:
    return find_spec(package_name) is not None


def run_demo() -> None:
    for package_name in ["json", "pathlib", "rich"]:
        print(f"{package_name}: installed = {package_available(package_name)}")


if __name__ == "__main__":
    run_demo()
