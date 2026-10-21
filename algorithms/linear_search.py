"""Linear search over any sequence of integers.

Unlike binary search, linear search does not require sorted input.
Time complexity: O(n); auxiliary space: O(1).

Run: python algorithms/linear_search.py
"""


def linear_search(values: list[int], target: int) -> int | None:
    """Return the first index of target, or None if it is absent."""
    for index, value in enumerate(values):
        if value == target:
            return index
    return None


def main() -> None:
    """Demonstrate successful and unsuccessful searches."""
    numbers = [17, 4, 29, 8, 13]

    for target in (29, 17, 99):
        index = linear_search(numbers, target)
        if index is None:
            print(f"{target} was not found.")
        else:
            print(f"{target} found at index {index}.")


if __name__ == "__main__":
    main()
