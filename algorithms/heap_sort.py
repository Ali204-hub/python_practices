"""Heap sort for practicing the binary heap data structure.

Time complexity: O(n log n) in best, average, and worst cases.
Auxiliary space: O(n) for the returned copy; heap operations use O(1)
additional space apart from recursive call stack frames.

Run: python algorithms/heap_sort.py
"""


def heap_sort(values: list[int]) -> list[int]:
    """Return values sorted in ascending order without modifying the input."""
    result = values.copy()
    size = len(result)

    def sift_down(heap_size: int, root: int) -> None:
        """Move the larger child upward until the max-heap property holds."""
        largest = root
        left_child = 2 * root + 1
        right_child = 2 * root + 2

        if left_child < heap_size and result[left_child] > result[largest]:
            largest = left_child

        if right_child < heap_size and result[right_child] > result[largest]:
            largest = right_child

        if largest != root:
            result[root], result[largest] = result[largest], result[root]
            sift_down(heap_size, largest)

    # Build a max heap from the unsorted data.
    for root in range(size // 2 - 1, -1, -1):
        sift_down(size, root)

    # Move each maximum to the end, then restore the heap.
    for end in range(size - 1, 0, -1):
        result[0], result[end] = result[end], result[0]
        sift_down(end, 0)

    return result


def main() -> None:
    """Demonstrate heap sort on a sample list."""
    numbers = [12, 11, 13, 5, 6, 7]
    print("Original:", numbers)
    print("Sorted:  ", heap_sort(numbers))
    print("Original remains unchanged:", numbers)


if __name__ == "__main__":
    main()
