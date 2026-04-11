from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "python-language" / "weekly-practice"))

from week_06_testing_basics import divide, is_even


class Week06TestingBasicsTests(unittest.TestCase):
    def test_is_even_returns_true_for_even_number(self) -> None:
        self.assertTrue(is_even(4))

    def test_is_even_returns_false_for_odd_number(self) -> None:
        self.assertFalse(is_even(5))

    def test_divide_returns_quotient(self) -> None:
        self.assertEqual(divide(10, 2), 5.0)

    def test_divide_raises_error_for_zero_divisor(self) -> None:
        with self.assertRaises(ValueError):
            divide(10, 0)


if __name__ == "__main__":
    unittest.main()
