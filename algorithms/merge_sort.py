"""Merge sort for learning divide-and-conquer algorithms.

Time complexity: O(n log n) in best, average, and worst cases.
Auxiliary space: O(n) for the temporary lists used during merging.

Run: python algorithms/merge_sort.py
"""


def merge_sort(values: list[int]) -> list[int]:
    """Return a sorted copy of values without changing the input list."""
    if len(values) <= 1:
        return values.copy()

    middle = len(values) // 2
    left = merge_sort(values[:middle])
    right = merge_sort(values[middle:])

    return _merge(left, right)


def _merge(left: list[int], right: list[int]) -> list[int]:
    """Merge two already-sorted lists into one sorted list."""
    merged: list[int] = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    return merged


def main() -> None:
    """Demonstrate merge sort on an unsorted list."""
    numbers = [38, 27, 43, 3, 9, 82, 10]
    print("Original:", numbers)
    print("Sorted:  ", merge_sort(numbers))
    print("Original remains unchanged:", numbers)


if __name__ == "__main__":
    main()
