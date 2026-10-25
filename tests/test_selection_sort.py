"""Unit tests for selection sort."""

import unittest

from algorithms.selection_sort import selection_sort


class TestSelectionSort(unittest.TestCase):
    def test_sorts_unsorted_values(self) -> None:
        self.assertEqual(selection_sort([29, 10, 14, 37, 13]), [10, 13, 14, 29, 37])

    def test_handles_empty_list(self) -> None:
        self.assertEqual(selection_sort([]), [])

    def test_handles_single_item(self) -> None:
        self.assertEqual(selection_sort([7]), [7])

    def test_handles_negative_numbers(self) -> None:
        self.assertEqual(selection_sort([0, -4, 8, -1]), [-4, -1, 0, 8])

    def test_handles_duplicate_values(self) -> None:
        self.assertEqual(selection_sort([3, 1, 3, 2, 1]), [1, 1, 2, 3, 3])

    def test_handles_already_sorted_values(self) -> None:
        self.assertEqual(selection_sort([1, 2, 3, 4]), [1, 2, 3, 4])

    def test_handles_reverse_sorted_values(self) -> None:
        self.assertEqual(selection_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_does_not_modify_original_list(self) -> None:
        values = [4, 2, 3, 1]
        selection_sort(values)
        self.assertEqual(values, [4, 2, 3, 1])


if __name__ == "__main__":
    unittest.main()
