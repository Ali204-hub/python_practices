"""Unit tests for heap sort."""

import unittest

from algorithms.heap_sort import heap_sort


class TestHeapSort(unittest.TestCase):
    def test_sorts_unsorted_values(self) -> None:
        self.assertEqual(heap_sort([12, 11, 13, 5, 6, 7]), [5, 6, 7, 11, 12, 13])

    def test_handles_empty_list(self) -> None:
        self.assertEqual(heap_sort([]), [])

    def test_handles_single_item(self) -> None:
        self.assertEqual(heap_sort([42]), [42])

    def test_handles_negative_numbers(self) -> None:
        self.assertEqual(heap_sort([0, -7, 4, -2]), [-7, -2, 0, 4])

    def test_handles_duplicate_values(self) -> None:
        self.assertEqual(heap_sort([3, 1, 3, 2, 1]), [1, 1, 2, 3, 3])

    def test_handles_already_sorted_values(self) -> None:
        self.assertEqual(heap_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_handles_reverse_sorted_values(self) -> None:
        self.assertEqual(heap_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_does_not_modify_original_list(self) -> None:
        values = [8, 3, 6, 1]
        heap_sort(values)
        self.assertEqual(values, [8, 3, 6, 1])


if __name__ == "__main__":
    unittest.main()
