"""Least Recently Used (LRU) cache implementation."""

from collections import OrderedDict
from typing import Generic, TypeVar


K = TypeVar("K")
V = TypeVar("V")


class LRUCache(Generic[K, V]):
    """A fixed-capacity cache that evicts the least recently used item."""

    def __init__(self, capacity: int) -> None:
        if capacity <= 0:
            raise ValueError("capacity must be greater than zero")
        self._capacity = capacity
        self._items: OrderedDict[K, V] = OrderedDict()

    def get(self, key: K, default: V | None = None) -> V | None:
        """Return a value and mark the key as recently used."""
        if key not in self._items:
            return default
        self._items.move_to_end(key)
        return self._items[key]

    def put(self, key: K, value: V) -> None:
        """Insert or replace a value and evict the oldest item if needed."""
        if key in self._items:
            self._items.move_to_end(key)
        self._items[key] = value

        if len(self._items) > self._capacity:
            self._items.popitem(last=False)

    def keys(self) -> list[K]:
        """Return keys from least recently used to most recently used."""
        return list(self._items.keys())

    def __len__(self) -> int:
        return len(self._items)

    def __contains__(self, key: K) -> bool:
        return key in self._items
