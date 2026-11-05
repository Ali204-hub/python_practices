"""Unit tests for Disjoint Set Union (Union-Find)."""

import unittest

from data_structures.union_find import UnionFind


class TestUnionFind(unittest.TestCase):
    def test_initializes_items_as_separate_components(self) -> None:
        groups = UnionFind([1, 2, 3])
        self.assertEqual(len(groups), 3)
        self.assertEqual(groups.component_count, 3)

    def test_adds_new_items_and_ignores_duplicates(self) -> None:
        groups = UnionFind(["A"])
        self.assertTrue(groups.add("B"))
        self.assertFalse(groups.add("B"))
        self.assertEqual(len(groups), 2)
        self.assertEqual(groups.component_count, 2)

    def test_unions_two_components(self) -> None:
        groups = UnionFind([1, 2, 3])
        self.assertTrue(groups.union(1, 2))
        self.assertTrue(groups.connected(1, 2))
        self.assertEqual(groups.component_count, 2)

    def test_repeated_union_does_not_change_component_count(self) -> None:
        groups = UnionFind([1, 2])
        self.assertTrue(groups.union(1, 2))
        self.assertFalse(groups.union(2, 1))
        self.assertEqual(groups.component_count, 1)

    def test_component_size_tracks_merged_groups(self) -> None:
        groups = UnionFind(["a", "b", "c", "d"])
        groups.union("a", "b")
        groups.union("c", "d")
        groups.union("a", "c")
        self.assertEqual(groups.component_size("d"), 4)
        self.assertEqual(groups.component_size("a"), 4)

    def test_groups_returns_each_item_once(self) -> None:
        groups = UnionFind([1, 2, 3, 4])
        groups.union(1, 2)
        groups.union(3, 4)
        actual = {frozenset(group) for group in groups.groups()}
        self.assertEqual(actual, {frozenset({1, 2}), frozenset({3, 4})})

    def test_supports_strings_and_tuple_items(self) -> None:
        groups = UnionFind([("row", 1), ("row", 2), ("col", 1)])
        groups.union(("row", 1), ("row", 2))
        self.assertTrue(groups.connected(("row", 1), ("row", 2)))
        self.assertFalse(groups.connected(("row", 1), ("col", 1)))

    def test_raises_for_unknown_items(self) -> None:
        groups = UnionFind([1, 2])
        with self.assertRaises(KeyError):
            groups.find(3)
        with self.assertRaises(KeyError):
            groups.union(1, 3)

    def test_empty_structure(self) -> None:
        groups = UnionFind()
        self.assertEqual(groups.groups(), [])
        self.assertEqual(groups.component_count, 0)
        self.assertEqual(len(groups), 0)

    def test_large_chain_of_unions(self) -> None:
        groups = UnionFind(range(1000))
        for item in range(999):
            groups.union(item, item + 1)
        self.assertEqual(groups.component_count, 1)
        self.assertEqual(groups.component_size(500), 1000)


if __name__ == "__main__":
    unittest.main()
