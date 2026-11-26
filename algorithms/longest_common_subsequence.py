"""Longest Common Subsequence dynamic programming solution."""


def longest_common_subsequence(first: str, second: str) -> str:
    """Return one longest common subsequence shared by two strings."""
    rows, cols = len(first), len(second)
    dp = [[0] * (cols + 1) for _ in range(rows + 1)]

    for row in range(rows - 1, -1, -1):
        for col in range(cols - 1, -1, -1):
            if first[row] == second[col]:
                dp[row][col] = 1 + dp[row + 1][col + 1]
            else:
                dp[row][col] = max(dp[row + 1][col], dp[row][col + 1])

    result: list[str] = []
    row = col = 0

    while row < rows and col < cols:
        if first[row] == second[col]:
            result.append(first[row])
            row += 1
            col += 1
        elif dp[row + 1][col] >= dp[row][col + 1]:
            row += 1
        else:
            col += 1

    return "".join(result)


if __name__ == "__main__":
    import unittest

    class TestLongestCommonSubsequence(unittest.TestCase):
        def test_classic_case(self) -> None:
            self.assertEqual(longest_common_subsequence("ABCBDAB", "BDCABA"), "BDAB")

        def test_no_common_characters(self) -> None:
            self.assertEqual(longest_common_subsequence("abc", "xyz"), "")

        def test_repeated_characters(self) -> None:
            result = longest_common_subsequence("aaaa", "aa")
            self.assertEqual(result, "aa")

        def test_empty_string(self) -> None:
            self.assertEqual(longest_common_subsequence("", "hello"), "")

        def test_identical_strings(self) -> None:
            self.assertEqual(longest_common_subsequence("python", "python"), "python")

    unittest.main()
