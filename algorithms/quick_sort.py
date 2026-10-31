"""Practice quick sort using a three-way partition.

Average time complexity: O(n log n); worst case: O(n^2).
Auxiliary space: O(log n) for the pending partitions.
The input list is not modified.

Run: python algorithms/quick_sort.py
"""


def quick_sort(values: list[int]) -> list[int]:
    """Return a sorted copy of values using quick sort."""
    result = values.copy()
    pending = [(0, len(result) - 1)]

    while pending:
        low, high = pending.pop()

        while low < high:
            middle = low + (high - low) // 2
            pivot = sorted((result[low], result[middle], result[high]))[1]

            # Three-way partition keeps duplicate values together.
            smaller = low
            current = low
            larger = high

            while current <= larger:
                if result[current] < pivot:
                    result[smaller], result[current] = (
                        result[current],
                        result[smaller],
                    )
                    smaller += 1
                    current += 1
                elif result[current] > pivot:
                    result[current], result[larger] = (
                        result[larger],
                        result[current],
                    )
                    larger -= 1
                else:
                    current += 1

            # Process the smaller side immediately and save the larger side.
            left_size = smaller - low
            right_size = high - larger

            if left_size < right_size:
                if larger + 1 < high:
                    pending.append((larger + 1, high))
                high = smaller - 1
            else:
                if low < smaller - 1:
                    pending.append((low, smaller - 1))
                low = larger + 1

    return result


def main() -> None:
    """Demonstrate quick sort on a sample list."""
    numbers = [10, 7, 8, 9, 1, 5, 5]
    print("Original:", numbers)
    print("Sorted:  ", quick_sort(numbers))
    print("Original remains unchanged:", numbers)


if __name__ == "__main__":
    main()
