"""Fenwick tree (Binary Indexed Tree) for prefix sums."""

from __future__ import annotations


class FenwickTree:
    """Support point additions and prefix/range sum queries in O(log n)."""

    def __init__(self, values: list[int]) -> None:
        self._n = len(values)
        self._tree = [0] * (self._n + 1)

        for index, value in enumerate(values, start=1):
            self.add(index, value)

    def add(self, index: int, delta: int) -> None:
        """Add delta to the one-based position index."""
        self._check_index(index)

        while index <= self._n:
            self._tree[index] += delta
            index += index & -index

    def prefix_sum(self, index: int) -> int:
        """Return the sum of positions 1 through index."""
        if index < 0 or index > self._n:
            raise IndexError("index out of range")

        total = 0
        while index > 0:
            total += self._tree[index]
            index -= index & -index

        return total

    def range_sum(self, left: int, right: int) -> int:
        """Return the inclusive sum for one-based positions left through right."""
        if left < 1 or right > self._n or left > right:
            raise IndexError("invalid query range")

        return self.prefix_sum(right) - self.prefix_sum(left - 1)

    def _check_index(self, index: int) -> None:
        if not 1 <= index <= self._n:
            raise IndexError("index out of range")


if __name__ == "__main__":
    import unittest

    class TestFenwickTree(unittest.TestCase):
        def setUp(self) -> None:
            self.tree = FenwickTree([3, 1, 4, 2, 5])

        def test_prefix_sum(self) -> None:
            self.assertEqual(self.tree.prefix_sum(3), 8)

        def test_range_sum(self) -> None:
            self.assertEqual(self.tree.range_sum(2, 4), 7)

        def test_add_updates_totals(self) -> None:
            self.tree.add(3, 6)
            self.assertEqual(self.tree.prefix_sum(3), 14)
            self.assertEqual(self.tree.range_sum(3, 5), 17)

        def test_invalid_index(self) -> None:
            with self.assertRaises(IndexError):
                self.tree.add(0, 5)

    unittest.main()
