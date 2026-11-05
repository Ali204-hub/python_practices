"""Disjoint Set Union (Union-Find) with path compression and union by size.

The structure tracks groups of connected hashable items. find, union,
connected, and component_size are nearly O(1) amortized operations.

Run: python data_structures/union_find.py
"""

from collections.abc import Hashable, Iterable
from typing import Generic, TypeVar


T = TypeVar("T", bound=Hashable)


class UnionFind(Generic[T]):
    """Maintain disjoint groups and merge them efficiently."""

    def __init__(self, items: Iterable[T] = ()) -> None:
        self._parent: dict[T, T] = {}
        self._size: dict[T, int] = {}
        self._components = 0
        for item in items:
            self.add(item)

    def add(self, item: T) -> bool:
        """Add an item as its own group; return False if it already exists."""
        if item in self._parent:
            return False
        self._parent[item] = item
        self._size[item] = 1
        self._components += 1
        return True

    def _require_item(self, item: T) -> None:
        if item not in self._parent:
            raise KeyError(
                f"Unknown item: {item!r}. Add it before using UnionFind operations."
            )

    def find(self, item: T) -> T:
        """Return the representative of item, compressing its path."""
        self._require_item(item)

        root = item
        while self._parent[root] != root:
            root = self._parent[root]

        # Iterative path compression avoids recursion-depth limits.
        current = item
        while self._parent[current] != current:
            parent = self._parent[current]
            self._parent[current] = root
            current = parent

        return root

    def union(self, first: T, second: T) -> bool:
        """Merge two groups; return True only when a merge takes place."""
        root_first = self.find(first)
        root_second = self.find(second)

        if root_first == root_second:
            return False

        # Attach the smaller tree beneath the larger tree.
        if self._size[root_first] < self._size[root_second]:
            root_first, root_second = root_second, root_first

        self._parent[root_second] = root_first
        self._size[root_first] += self._size[root_second]
        del self._size[root_second]
        self._components -= 1
        return True

    def connected(self, first: T, second: T) -> bool:
        """Return whether both known items belong to the same group."""
        return self.find(first) == self.find(second)

    def component_size(self, item: T) -> int:
        """Return the number of items in item's connected group."""
        return self._size[self.find(item)]

    def groups(self) -> list[list[T]]:
        """Return all groups, preserving item insertion order within groups."""
        grouped: dict[T, list[T]] = {}
        for item in self._parent:
            representative = self.find(item)
            grouped.setdefault(representative, []).append(item)
        return list(grouped.values())

    @property
    def component_count(self) -> int:
        """Return the current number of disjoint groups."""
        return self._components

    def __len__(self) -> int:
        """Return the number of items stored in the structure."""
        return len(self._parent)


def main() -> None:
    """Group cities connected by roads."""
    cities = UnionFind(["Jhang", "Faisalabad", "Lahore", "Multan"])
    cities.union("Jhang", "Faisalabad")
    cities.union("Faisalabad", "Lahore")

    print("Connected cities:", cities.connected("Jhang", "Lahore"))
    print("Groups:", cities.groups())
    print("Separate components:", cities.component_count)


if __name__ == "__main__":
    main()
