"""Unit tests for the Trie prefix tree."""

import unittest

from data_structures.trie import Trie


class TestTrie(unittest.TestCase):
    def setUp(self) -> None:
        self.trie = Trie()

    def test_inserts_and_searches_complete_words(self) -> None:
        self.assertTrue(self.trie.insert("python"))
        self.assertTrue(self.trie.search("python"))
        self.assertFalse(self.trie.search("py"))

    def test_duplicate_insert_does_not_increase_size(self) -> None:
        self.assertTrue(self.trie.insert("tree"))
        self.assertFalse(self.trie.insert("tree"))
        self.assertEqual(len(self.trie), 1)

    def test_checks_prefixes(self) -> None:
        self.trie.insert("developer")
        self.assertTrue(self.trie.starts_with("devel"))
        self.assertFalse(self.trie.starts_with("design"))
        self.assertTrue(self.trie.starts_with(""))

    def test_returns_words_with_prefix_in_sorted_order(self) -> None:
        for word in ("app", "apple", "apt", "bat"):
            self.trie.insert(word)
        self.assertEqual(self.trie.words_with_prefix("ap"), ["app", "apple", "apt"])
        self.assertEqual(self.trie.words_with_prefix(), ["app", "apple", "apt", "bat"])

    def test_delete_removes_only_the_complete_word(self) -> None:
        self.trie.insert("car")
        self.trie.insert("cart")
        self.assertTrue(self.trie.delete("car"))
        self.assertFalse(self.trie.search("car"))
        self.assertTrue(self.trie.search("cart"))
        self.assertEqual(len(self.trie), 1)

    def test_delete_returns_false_for_missing_word(self) -> None:
        self.trie.insert("hello")
        self.assertFalse(self.trie.delete("help"))
        self.assertEqual(len(self.trie), 1)

    def test_delete_prunes_nodes_without_affecting_other_words(self) -> None:
        for word in ("cat", "car", "dog"):
            self.trie.insert(word)
        self.assertTrue(self.trie.delete("cat"))
        self.assertEqual(self.trie.words_with_prefix("ca"), ["car"])
        self.assertTrue(self.trie.search("dog"))

    def test_is_case_sensitive(self) -> None:
        self.trie.insert("Python")
        self.assertTrue(self.trie.search("Python"))
        self.assertFalse(self.trie.search("python"))

    def test_rejects_non_string_and_empty_words(self) -> None:
        with self.assertRaises(TypeError):
            self.trie.insert(123)  # type: ignore[arg-type]
        with self.assertRaises(ValueError):
            self.trie.insert("")

    def test_empty_prefix_and_missing_prefix(self) -> None:
        self.assertFalse(self.trie.starts_with(""))
        self.trie.insert("code")
        self.assertEqual(self.trie.words_with_prefix("xyz"), [])


if __name__ == "__main__":
    unittest.main()
