"""0/1 Knapsack dynamic programming solution."""


def knapsack_01(weights: list[int], values: list[int], capacity: int) -> int:
    """Return the maximum value achievable without exceeding capacity."""
    if len(weights) != len(values):
        raise ValueError("weights and values must have the same length")
    if capacity < 0:
        raise ValueError("capacity cannot be negative")
    if any(weight < 0 for weight in weights):
        raise ValueError("weights cannot be negative")

    dp = [0] * (capacity + 1)

    for weight, value in zip(weights, values):
        for current_capacity in range(capacity, weight - 1, -1):
            dp[current_capacity] = max(
                dp[current_capacity],
                dp[current_capacity - weight] + value,
            )

    return dp[capacity]


if __name__ == "__main__":
    import unittest

    class TestKnapsack01(unittest.TestCase):
        def test_basic_case(self) -> None:
            self.assertEqual(
                knapsack_01([2, 3, 4, 5], [3, 4, 5, 6], 5),
                7,
            )

        def test_exact_capacity(self) -> None:
            self.assertEqual(knapsack_01([1, 2, 3], [6, 10, 12], 3), 16)

        def test_empty_items(self) -> None:
            self.assertEqual(knapsack_01([], [], 10), 0)

        def test_invalid_lengths(self) -> None:
            with self.assertRaises(ValueError):
                knapsack_01([1], [2, 3], 3)

        def test_negative_capacity(self) -> None:
            with self.assertRaises(ValueError):
                knapsack_01([1], [2], -1)

    unittest.main()
