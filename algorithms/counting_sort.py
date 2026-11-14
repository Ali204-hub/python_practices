"""Counting sort for integer lists with a small non-negative range."""


def counting_sort(values: list[int]) -> list[int]:
    """Return values sorted in ascending order using frequency counts."""
    if not values:
        return []

    if any(value < 0 for value in values):
        raise ValueError("counting_sort accepts non-negative integers")

    counts = [0] * (max(values) + 1)
    for value in values:
        counts[value] += 1

    result: list[int] = []
    for value, frequency in enumerate(counts):
        result.extend([value] * frequency)
    return result


if __name__ == "__main__":
    import unittest

    class TestCountingSort(unittest.TestCase):
        def test_sorts_values(self) -> None:
            self.assertEqual(counting_sort([4, 2, 7, 1, 2]), [1, 2, 2, 4, 7])

        def test_handles_empty_input(self) -> None:
            self.assertEqual(counting_sort([]), [])

        def test_handles_duplicates_and_zero(self) -> None:
            self.assertEqual(counting_sort([0, 3, 0, 1, 3]), [0, 0, 1, 3, 3])

        def test_rejects_negative_values(self) -> None:
            with self.assertRaises(ValueError):
                counting_sort([2, -1, 3])

    unittest.main()
