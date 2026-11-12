"""Tests for the Knuth-Morris-Pratt string search algorithm."""

import unittest

from algorithms.kmp import find_all_occurrences


class TestFindAllOccurrences(unittest.TestCase):
    def test_finds_single_match(self) -> None:
        self.assertEqual(find_all_occurrences("hello world", "world"), [6])

    def test_finds_overlapping_matches(self) -> None:
        self.assertEqual(find_all_occurrences("aaaaa", "aaa"), [0, 1, 2])

    def test_returns_empty_for_no_match(self) -> None:
        self.assertEqual(find_all_occurrences("python", "java"), [])

    def test_returns_empty_when_pattern_is_longer(self) -> None:
        self.assertEqual(find_all_occurrences("cat", "catch"), [])

    def test_handles_match_at_start(self) -> None:
        self.assertEqual(find_all_occurrences("abcabc", "abc"), [0, 3])

    def test_rejects_empty_pattern(self) -> None:
        with self.assertRaises(ValueError):
            find_all_occurrences("abc", "")


if __name__ == "__main__":
    unittest.main()
