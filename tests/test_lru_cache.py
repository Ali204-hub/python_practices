"""Tests for the LRU cache data structure."""

import unittest

from data_structures.lru_cache import LRUCache


class TestLRUCache(unittest.TestCase):
    def test_put_and_get(self) -> None:
        cache = LRUCache[str, int](2)
        cache.put("a", 1)
        cache.put("b", 2)
        self.assertEqual(cache.get("a"), 1)

    def test_get_marks_item_as_recent(self) -> None:
        cache = LRUCache[str, int](2)
        cache.put("a", 1)
        cache.put("b", 2)
        cache.get("a")
        cache.put("c", 3)
        self.assertNotIn("b", cache)
        self.assertEqual(cache.keys(), ["a", "c"])

    def test_put_evicts_least_recently_used(self) -> None:
        cache = LRUCache[str, int](2)
        cache.put("a", 1)
        cache.put("b", 2)
        cache.put("c", 3)
        self.assertNotIn("a", cache)
        self.assertEqual(cache.get("b"), 2)

    def test_updating_key_does_not_increase_size(self) -> None:
        cache = LRUCache[str, int](2)
        cache.put("a", 1)
        cache.put("a", 10)
        self.assertEqual(len(cache), 1)
        self.assertEqual(cache.get("a"), 10)

    def test_missing_key_returns_default(self) -> None:
        cache = LRUCache[str, int](2)
        self.assertIsNone(cache.get("missing"))
        self.assertEqual(cache.get("missing", 99), 99)

    def test_rejects_non_positive_capacity(self) -> None:
        with self.assertRaises(ValueError):
            LRUCache(0)


if __name__ == "__main__":
    unittest.main()
