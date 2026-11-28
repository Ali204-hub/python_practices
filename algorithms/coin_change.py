"""Minimum coin change solution using dynamic programming."""


def min_coins(coins: list[int], amount: int) -> int:
    """Return the minimum number of coins needed to make amount, or -1."""
    if amount < 0:
        raise ValueError("amount cannot be negative")
    if any(coin <= 0 for coin in coins):
        raise ValueError("coins must be positive")

    unreachable = amount + 1
    dp = [unreachable] * (amount + 1)
    dp[0] = 0

    for current_amount in range(1, amount + 1):
        for coin in coins:
            if coin <= current_amount:
                dp[current_amount] = min(
                    dp[current_amount],
                    dp[current_amount - coin] + 1,
                )

    return -1 if dp[amount] == unreachable else dp[amount]


if __name__ == "__main__":
    import unittest

    class TestMinCoins(unittest.TestCase):
        def test_basic_case(self) -> None:
            self.assertEqual(min_coins([1, 2, 5], 11), 3)

        def test_exact_coin(self) -> None:
            self.assertEqual(min_coins([2, 5, 10], 10), 1)

        def test_unreachable_amount(self) -> None:
            self.assertEqual(min_coins([2], 3), -1)

        def test_zero_amount(self) -> None:
            self.assertEqual(min_coins([1, 2, 5], 0), 0)

        def test_invalid_coin(self) -> None:
            with self.assertRaises(ValueError):
                min_coins([1, 0, 2], 5)

    unittest.main()
