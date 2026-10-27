"""Unit tests for merge sort."""

import unittest

from algorithms.merge_sort import merge_sort


class TestMergeSort(unittest.TestCase):
    def test_sorts_unsorted_values(self) -> None:
        self.assertEqual(merge_sort([38, 27, 43, 3, 9, 82, 10]), [3, 9, 10, 27, 38, 43, 82])

    def test_handles_empty_list(self) -> None:
        self.assertEqual(merge_sort([]), [])

    def test_handles_single_value(self) -> None:
        self.assertEqual(merge_sort([42]), [42])

    def test_handles_negative_values(self) -> None:
        self.assertEqual(merge_sort([0, -5, 12, -1]), [-5, -1, 0, 12])

    def test_handles_duplicate_values(self) -> None:
        self.assertEqual(merge_sort([4, 2, 4, 1, 2]), [1, 2, 2, 4, 4])

    def test_handles_already_sorted_values(self) -> None:
        self.assertEqual(merge_sort([1, 2, 3, 4]), [1, 2, 3, 4])

    def test_handles_reverse_sorted_values(self) -> None:
        self.assertEqual(merge_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_does_not_modify_original_list(self) -> None:
        values = [9, 3, 7, 1]
        merge_sort(values)
        self.assertEqual(values, [9, 3, 7, 1])


if __name__ == "__main__":
    unittest.main()
