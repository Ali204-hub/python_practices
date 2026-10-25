"""Selection sort for practicing comparison-based sorting.

Time complexity: O(n^2) in best, average, and worst cases.
Auxiliary space: O(n) for the returned copy; sorting the copy uses O(1)
additional space.

Run: python algorithms/selection_sort.py
"""


def selection_sort(values: list[int]) -> list[int]:
    """Return values in ascending order without modifying the input list."""
    result = values.copy()
    size = len(result)

    for start in range(size - 1):
        minimum_index = start

        for current in range(start + 1, size):
            if result[current] < result[minimum_index]:
                minimum_index = current

        if minimum_index != start:
            result[start], result[minimum_index] = (
                result[minimum_index],
                result[start],
            )

    return result


def main() -> None:
    """Show selection sort on a sample list."""
    numbers = [29, 10, 14, 37, 13]
    print("Original:", numbers)
    print("Sorted:  ", selection_sort(numbers))
    print("Original remains unchanged:", numbers)


if __name__ == "__main__":
    main()
