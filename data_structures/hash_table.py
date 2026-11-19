"""Hash table implementation using separate chaining."""

class HashTable:
    """Store key-value pairs with average O(1) lookup and updates."""

    def __init__(self, capacity: int = 8) -> None:
        if capacity < 1:
            raise ValueError("capacity must be at least 1")
        self._buckets: list[list[tuple[str, int]]] = [[] for _ in range(capacity)]
        self._size = 0

    def _index(self, key: str) -> int:
        return hash(key) % len(self._buckets)

    def set(self, key: str, value: int) -> None:
        """Insert a key or update its existing value."""
        bucket = self._buckets[self._index(key)]

        for position, (stored_key, _) in enumerate(bucket):
            if stored_key == key:
                bucket[position] = (key, value)
                return

        bucket.append((key, value))
        self._size += 1

    def get(self, key: str) -> int:
        """Return the value for key or raise KeyError."""
        bucket = self._buckets[self._index(key)]

        for stored_key, value in bucket:
            if stored_key == key:
                return value

        raise KeyError(key)

    def contains(self, key: str) -> bool:
        """Return True when key exists in the table."""
        try:
            self.get(key)
            return True
        except KeyError:
            return False

    def delete(self, key: str) -> bool:
        """Remove key and return True when it existed."""
        bucket = self._buckets[self._index(key)]

        for position, (stored_key, _) in enumerate(bucket):
            if stored_key == key:
                del bucket[position]
                self._size -= 1
                return True

        return False

    def __len__(self) -> int:
        return self._size


if __name__ == "__main__":
    import unittest

    class TestHashTable(unittest.TestCase):
        def test_set_and_get(self) -> None:
            table = HashTable()
            table.set("name", 42)
            self.assertEqual(table.get("name"), 42)

        def test_update_existing_key(self) -> None:
            table = HashTable()
            table.set("score", 10)
            table.set("score", 25)
            self.assertEqual(table.get("score"), 25)
            self.assertEqual(len(table), 1)

        def test_contains_and_delete(self) -> None:
            table = HashTable()
            table.set("python", 3)
            self.assertTrue(table.contains("python"))
            self.assertTrue(table.delete("python"))
            self.assertFalse(table.contains("python"))
            self.assertEqual(len(table), 0)

        def test_missing_key(self) -> None:
            table = HashTable()
            self.assertFalse(table.contains("missing"))
            self.assertFalse(table.delete("missing"))
            with self.assertRaises(KeyError):
                table.get("missing")

    unittest.main()
