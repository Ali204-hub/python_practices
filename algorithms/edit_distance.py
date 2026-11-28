"""Levenshtein edit distance using dynamic programming."""


def edit_distance(first: str, second: str) -> int:
    """Return the minimum insertions, deletions, or substitutions needed."""
    if not first:
        return len(second)
    if not second:
        return len(first)

    previous = list(range(len(second) + 1))

    for row, first_char in enumerate(first, start=1):
        current = [row]

        for col, second_char in enumerate(second, start=1):
            insertion = current[col - 1] + 1
            deletion = previous[col] + 1
            substitution = previous[col - 1] + (first_char != second_char)
            current.append(min(insertion, deletion, substitution))

        previous = current

    return previous[-1]


if __name__ == "__main__":
    import unittest

    class TestEditDistance(unittest.TestCase):
        def test_kitten_sitting(self) -> None:
            self.assertEqual(edit_distance("kitten", "sitting"), 3)

        def test_identical_strings(self) -> None:
            self.assertEqual(edit_distance("python", "python"), 0)

        def test_empty_first_string(self) -> None:
            self.assertEqual(edit_distance("", "abc"), 3)

        def test_empty_second_string(self) -> None:
            self.assertEqual(edit_distance("abc", ""), 3)

        def test_single_substitution(self) -> None:
            self.assertEqual(edit_distance("cat", "cut"), 1)

    unittest.main()
