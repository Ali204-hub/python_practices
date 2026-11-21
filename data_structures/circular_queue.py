"""Fixed-capacity circular queue implementation."""

from __future__ import annotations


class CircularQueue:
    """FIFO queue that reuses freed slots in a fixed-size buffer."""

    def __init__(self, capacity: int) -> None:
        if capacity < 1:
            raise ValueError("capacity must be at least 1")
        self._items: list[object | None] = [None] * capacity
        self._front = 0
        self._size = 0

    @property
    def capacity(self) -> int:
        return len(self._items)

    def enqueue(self, item: object) -> None:
        """Add an item to the rear or raise OverflowError when full."""
        if self.is_full():
            raise OverflowError("queue is full")

        rear = (self._front + self._size) % self.capacity
        self._items[rear] = item
        self._size += 1

    def dequeue(self) -> object:
        """Remove and return the oldest item or raise IndexError when empty."""
        if self.is_empty():
            raise IndexError("dequeue from empty queue")

        item = self._items[self._front]
        self._items[self._front] = None
        self._front = (self._front + 1) % self.capacity
        self._size -= 1
        return item

    def peek(self) -> object:
        """Return the oldest item without removing it."""
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self._items[self._front]

    def is_empty(self) -> bool:
        return self._size == 0

    def is_full(self) -> bool:
        return self._size == self.capacity

    def __len__(self) -> int:
        return self._size


if __name__ == "__main__":
    import unittest

    class TestCircularQueue(unittest.TestCase):
        def test_fifo_order(self) -> None:
            queue = CircularQueue(3)
            queue.enqueue("A")
            queue.enqueue("B")
            queue.enqueue("C")
            self.assertEqual(queue.dequeue(), "A")
            self.assertEqual(queue.dequeue(), "B")

        def test_reuses_slots_after_dequeue(self) -> None:
            queue = CircularQueue(3)
            queue.enqueue(1)
            queue.enqueue(2)
            queue.enqueue(3)
            self.assertEqual(queue.dequeue(), 1)
            queue.enqueue(4)
            self.assertEqual([queue.dequeue(), queue.dequeue(), queue.dequeue()], [2, 3, 4])

        def test_full_queue_rejects_new_items(self) -> None:
            queue = CircularQueue(2)
            queue.enqueue(1)
            queue.enqueue(2)
            self.assertTrue(queue.is_full())
            with self.assertRaises(OverflowError):
                queue.enqueue(3)

        def test_empty_queue_operations(self) -> None:
            queue = CircularQueue(2)
            self.assertTrue(queue.is_empty())
            with self.assertRaises(IndexError):
                queue.peek()
            with self.assertRaises(IndexError):
                queue.dequeue()

    unittest.main()
