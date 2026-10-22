"""Insertion sort for learning in-place sorting logic.

Time complexity: O(n) in the best case and O(n^2) in the average/worst case.
Auxiliary space: O(1) beyond the copied output list.

Run: python algorithms/insertion_sort.py
"""


def insertion_sort(values: list[int]) -> list[int]:
    """Return a sorted copy of values without changing the original list."""
    result = values.copy()

    for index in range(1, len(result)):
        current = result[index]
        position = index - 1

        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1

        result[position + 1] = current

    return result


def main() -> None:
    """Demonstrate sorting an unsorted list."""
    numbers = [9, 3, 7, 1, 5]
    print("Original:", numbers)
    print("Sorted:  ", insertion_sort(numbers))
    print("Original remains unchanged:", numbers)


if __name__ == "__main__":
    main()
