"""Unit tests for the binary search practice implementation."""

import unittest

from algorithms.binary_search import binary_search


class TestBinarySearch(unittest.TestCase):
    def test_finds_middle_value(self) -> None:
        self.assertEqual(binary_search([1, 3, 5, 7, 9], 5), 2)

    def test_finds_first_value(self) -> None:
        self.assertEqual(binary_search([1, 3, 5, 7, 9], 1), 0)

    def test_finds_last_value(self) -> None:
        self.assertEqual(binary_search([1, 3, 5, 7, 9], 9), 4)

    def test_handles_single_item_list(self) -> None:
        self.assertEqual(binary_search([42], 42), 0)

    def test_returns_none_for_empty_list(self) -> None:
        self.assertIsNone(binary_search([], 3))

    def test_returns_none_for_missing_value_between_items(self) -> None:
        self.assertIsNone(binary_search([2, 4, 6, 8], 5))

    def test_returns_none_for_value_outside_range(self) -> None:
        values = [10, 20, 30]
        self.assertIsNone(binary_search(values, 1))
        self.assertIsNone(binary_search(values, 40))

    def test_supports_negative_numbers(self) -> None:
        self.assertEqual(binary_search([-9, -5, -1, 4], -5), 1)

    def test_duplicate_values(self) -> None:
        values = [1, 2, 2, 2, 4]
        index = binary_search(values, 2)
        self.assertIsNotNone(index)
        self.assertEqual(values[index], 2)  # type: ignore[index]


if __name__ == "__main__":
    unittest.main()
