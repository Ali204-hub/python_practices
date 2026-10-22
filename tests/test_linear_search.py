"""Unit tests for the linear search practice implementation."""

import unittest

from algorithms.linear_search import linear_search


class TestLinearSearch(unittest.TestCase):
    def test_finds_first_item(self) -> None:
        self.assertEqual(linear_search([5, 9, 2], 5), 0)

    def test_finds_middle_item(self) -> None:
        self.assertEqual(linear_search([5, 9, 2, 7], 2), 2)

    def test_finds_last_item(self) -> None:
        self.assertEqual(linear_search([5, 9, 2], 2), 2)

    def test_returns_none_when_value_is_missing(self) -> None:
        self.assertIsNone(linear_search([1, 4, 8], 6))

    def test_returns_none_for_empty_list(self) -> None:
        self.assertIsNone(linear_search([], 1))

    def test_supports_negative_numbers(self) -> None:
        self.assertEqual(linear_search([-8, -3, 0, 6], -3), 1)

    def test_returns_first_match_for_duplicates(self) -> None:
        self.assertEqual(linear_search([4, 7, 4, 9], 4), 0)


if __name__ == "__main__":
    unittest.main()
