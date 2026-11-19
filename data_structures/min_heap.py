"""Min-heap data structure implementation."""

class MinHeap:
    """Maintain integers so the smallest value is always at the root."""

    def __init__(self) -> None:
        self._items: list[int] = []

    def push(self, value: int) -> None:
        """Add a value and restore the heap property."""
        self._items.append(value)
        self._sift_up(len(self._items) - 1)

    def pop(self) -> int:
        """Remove and return the smallest value."""
        if not self._items:
            raise IndexError("pop from empty heap")

        smallest = self._items[0]
        last = self._items.pop()

        if self._items:
            self._items[0] = last
            self._sift_down(0)

        return smallest

    def peek(self) -> int:
        """Return the smallest value without removing it."""
        if not self._items:
            raise IndexError("peek from empty heap")
        return self._items[0]

    def __len__(self) -> int:
        return len(self._items)

    def _sift_up(self, index: int) -> None:
        while index > 0:
            parent = (index - 1) // 2
            if self._items[parent] <= self._items[index]:
                break
            self._items[parent], self._items[index] = (
                self._items[index],
                self._items[parent],
            )
            index = parent

    def _sift_down(self, index: int) -> None:
        size = len(self._items)

        while True:
            left = 2 * index + 1
            right = left + 1
            smallest = index

            if left < size and self._items[left] < self._items[smallest]:
                smallest = left
            if right < size and self._items[right] < self._items[smallest]:
                smallest = right

            if smallest == index:
                break

            self._items[index], self._items[smallest] = (
                self._items[smallest],
                self._items[index],
            )
            index = smallest


if __name__ == "__main__":
    import unittest

    class TestMinHeap(unittest.TestCase):
        def test_push_and_peek(self) -> None:
            heap = MinHeap()
            for value in [9, 3, 7, 1, 5]:
                heap.push(value)
            self.assertEqual(heap.peek(), 1)
            self.assertEqual(len(heap), 5)

        def test_pop_returns_sorted_values(self) -> None:
            heap = MinHeap()
            for value in [4, 1, 8, 2, 6]:
                heap.push(value)
            self.assertEqual([heap.pop() for _ in range(len(heap))], [1, 2, 4, 6, 8])

        def test_duplicate_values(self) -> None:
            heap = MinHeap()
            for value in [3, 3, 1, 2, 1]:
                heap.push(value)
            self.assertEqual([heap.pop() for _ in range(len(heap))], [1, 1, 2, 3, 3])

        def test_empty_heap_errors(self) -> None:
            heap = MinHeap()
            with self.assertRaises(IndexError):
                heap.peek()
            with self.assertRaises(IndexError):
                heap.pop()

    unittest.main()
