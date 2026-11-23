"""Segment tree for range-sum queries and point updates."""

from __future__ import annotations


class SegmentTree:
    """Maintain an integer array with O(log n) sum queries and updates."""

    def __init__(self, values: list[int]) -> None:
        if not values:
            raise ValueError("values must not be empty")

        self._n = len(values)
        self._tree = [0] * (4 * self._n)
        self._build(values, 1, 0, self._n - 1)

    def _build(self, values: list[int], node: int, left: int, right: int) -> None:
        if left == right:
            self._tree[node] = values[left]
            return

        mid = (left + right) // 2
        self._build(values, node * 2, left, mid)
        self._build(values, node * 2 + 1, mid + 1, right)
        self._tree[node] = self._tree[node * 2] + self._tree[node * 2 + 1]

    def update(self, index: int, value: int) -> None:
        """Replace one value at index."""
        self._check_index(index)
        self._update(1, 0, self._n - 1, index, value)

    def _update(self, node: int, left: int, right: int, index: int, value: int) -> None:
        if left == right:
            self._tree[node] = value
            return

        mid = (left + right) // 2
        if index <= mid:
            self._update(node * 2, left, mid, index, value)
        else:
            self._update(node * 2 + 1, mid + 1, right, index, value)

        self._tree[node] = self._tree[node * 2] + self._tree[node * 2 + 1]

    def query(self, left: int, right: int) -> int:
        """Return the inclusive sum of values from left to right."""
        if left < 0 or right >= self._n or left > right:
            raise IndexError("invalid query range")
        return self._query(1, 0, self._n - 1, left, right)

    def _query(
        self, node: int, start: int, end: int, left: int, right: int
    ) -> int:
        if left <= start and end <= right:
            return self._tree[node]

        mid = (start + end) // 2
        total = 0

        if left <= mid:
            total += self._query(node * 2, start, mid, left, right)
        if right > mid:
            total += self._query(node * 2 + 1, mid + 1, end, left, right)

        return total

    def _check_index(self, index: int) -> None:
        if not 0 <= index < self._n:
            raise IndexError("index out of range")


if __name__ == "__main__":
    import unittest

    class TestSegmentTree(unittest.TestCase):
        def setUp(self) -> None:
            self.tree = SegmentTree([2, 4, 1, 7, 3])

        def test_full_range(self) -> None:
            self.assertEqual(self.tree.query(0, 4), 17)

        def test_partial_range(self) -> None:
            self.assertEqual(self.tree.query(1, 3), 12)

        def test_update_changes_queries(self) -> None:
            self.tree.update(2, 10)
            self.assertEqual(self.tree.query(1, 3), 21)

        def test_invalid_range(self) -> None:
            with self.assertRaises(IndexError):
                self.tree.query(-1, 2)

    unittest.main()
