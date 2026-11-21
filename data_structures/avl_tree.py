"""AVL tree implementation with automatic height balancing."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class _Node:
    key: int
    height: int = 1
    left: _Node | None = None
    right: _Node | None = None


class AVLTree:
    """Self-balancing binary search tree with O(log n) operations."""

    def __init__(self) -> None:
        self.root: _Node | None = None

    @staticmethod
    def _height(node: _Node | None) -> int:
        return node.height if node else 0

    @classmethod
    def _update_height(cls, node: _Node) -> None:
        node.height = 1 + max(cls._height(node.left), cls._height(node.right))

    @classmethod
    def _balance_factor(cls, node: _Node) -> int:
        return cls._height(node.left) - cls._height(node.right)

    @classmethod
    def _rotate_right(cls, node: _Node) -> _Node:
        new_root = node.left
        assert new_root is not None
        node.left = new_root.right
        new_root.right = node
        cls._update_height(node)
        cls._update_height(new_root)
        return new_root

    @classmethod
    def _rotate_left(cls, node: _Node) -> _Node:
        new_root = node.right
        assert new_root is not None
        node.right = new_root.left
        new_root.left = node
        cls._update_height(node)
        cls._update_height(new_root)
        return new_root

    @classmethod
    def _rebalance(cls, node: _Node) -> _Node:
        cls._update_height(node)
        balance = cls._balance_factor(node)

        if balance > 1:
            if cls._balance_factor(node.left) < 0:
                assert node.left is not None
                node.left = cls._rotate_left(node.left)
            return cls._rotate_right(node)

        if balance < -1:
            if cls._balance_factor(node.right) > 0:
                assert node.right is not None
                node.right = cls._rotate_right(node.right)
            return cls._rotate_left(node)

        return node

    @classmethod
    def _insert(cls, node: _Node | None, key: int) -> _Node:
        if node is None:
            return _Node(key)

        if key < node.key:
            node.left = cls._insert(node.left, key)
        elif key > node.key:
            node.right = cls._insert(node.right, key)
        else:
            return node

        return cls._rebalance(node)

    def insert(self, key: int) -> None:
        """Insert key; duplicate keys are ignored."""
        self.root = self._insert(self.root, key)

    def contains(self, key: int) -> bool:
        """Return True when key exists in the tree."""
        node = self.root
        while node:
            if key == node.key:
                return True
            node = node.left if key < node.key else node.right
        return False

    def inorder(self) -> list[int]:
        """Return keys in sorted order."""

        def walk(node: _Node | None) -> list[int]:
            if node is None:
                return []
            return walk(node.left) + [node.key] + walk(node.right)

        return walk(self.root)


if __name__ == "__main__":
    import unittest

    class TestAVLTree(unittest.TestCase):
        def test_insert_keeps_sorted_order(self) -> None:
            tree = AVLTree()
            for value in [30, 10, 20, 40, 50]:
                tree.insert(value)
            self.assertEqual(tree.inorder(), [10, 20, 30, 40, 50])

        def test_balances_left_heavy_case(self) -> None:
            tree = AVLTree()
            for value in [30, 20, 10]:
                tree.insert(value)
            self.assertEqual(tree.root.key, 20)
            self.assertEqual(tree.inorder(), [10, 20, 30])

        def test_balances_right_heavy_case(self) -> None:
            tree = AVLTree()
            for value in [10, 20, 30]:
                tree.insert(value)
            self.assertEqual(tree.root.key, 20)

        def test_duplicates_and_search(self) -> None:
            tree = AVLTree()
            tree.insert(15)
            tree.insert(15)
            self.assertTrue(tree.contains(15))
            self.assertFalse(tree.contains(99))
            self.assertEqual(tree.inorder(), [15])

    unittest.main()
