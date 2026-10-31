"""Unit tests for quick sort."""

import unittest

from algorithms.quick_sort import quick_sort


class TestQuickSort(unittest.TestCase):
    def test_sorts_unsorted_values(self) -> None:
        self.assertEqual(quick_sort([10, 7, 8, 9, 1, 5]), [1, 5, 7, 8, 9, 10])

    def test_handles_empty_and_single_item_lists(self) -> None:
        self.assertEqual(quick_sort([]), [])
        self.assertEqual(quick_sort([42]), [42])

    def test_handles_negative_numbers_and_duplicates(self) -> None:
        self.assertEqual(quick_sort([0, -7, 4, -2, 4]), [-7, -2, 0, 4, 4])

    def test_handles_all_equal_values(self) -> None:
        self.assertEqual(quick_sort([4] * 100), [4] * 100)

    def test_handles_sorted_and_reverse_sorted_values(self) -> None:
        self.assertEqual(quick_sort([1, 2, 3, 4]), [1, 2, 3, 4])
        self.assertEqual(quick_sort([4, 3, 2, 1]), [1, 2, 3, 4])

    def test_does_not_modify_original_list(self) -> None:
        values = [8, 3, 6, 1]
        result = quick_sort(values)
        self.assertEqual(values, [8, 3, 6, 1])
        self.assertIsNot(result, values)

    def test_handles_a_larger_input(self) -> None:
        values = list(range(2000, -1, -1))
        self.assertEqual(quick_sort(values), list(range(2001)))


if __name__ == "__main__":
    unittest.main()
