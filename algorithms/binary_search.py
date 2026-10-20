"""Practice binary search on an ascending sequence.

Binary search repeatedly halves the search interval.
Time complexity: O(log n); auxiliary space: O(1).

Run: python algorithms/binary_search.py
"""


def binary_search(values: list[int], target: int) -> int | None:
    """Return an index of target in sorted values, or None if it is absent.

    The input list must be sorted in ascending order. If duplicate values
    exist, the returned index may point to any one of those occurrences.
    """
    left = 0
    right = len(values) - 1

    while left <= right:
        middle = left + (right - left) // 2
        current = values[middle]

        if current == target:
            return middle
        if current < target:
            left = middle + 1
        else:
            right = middle - 1

    return None


def main() -> None:
    """Show a few examples and their results."""
    numbers = [3, 8, 12, 17, 25, 31, 42]

    for target in (17, 3, 42, 19):
        result = binary_search(numbers, target)
        if result is None:
            print(f"{target} was not found.")
        else:
            print(f"{target} found at index {result}.")


if __name__ == "__main__":
    main()
