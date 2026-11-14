"""Binary search tree implementation for integer values."""


class BinarySearchTree:
    """Store unique integers while supporting search and sorted traversal."""

    class _Node:
        def __init__(self, value: int) -> None:
            self.value = value
            self.left: "BinarySearchTree._Node | None" = None
            self.right: "BinarySearchTree._Node | None" = None

    def __init__(self) -> None:
        self._root: BinarySearchTree._Node | None = None

    def insert(self, value: int) -> None:
        """Insert a value; duplicate values are ignored."""
        if self._root is None:
            self._root = self._Node(value)
            return

        current = self._root
        while True:
            if value == current.value:
                return
            if value < current.value:
                if current.left is None:
                    current.left = self._Node(value)
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = self._Node(value)
                    return
                current = current.right

    def contains(self, value: int) -> bool:
        """Return True when value exists in the tree."""
        current = self._root
        while current is not None:
            if value == current.value:
                return True
            current = current.left if value < current.value else current.right
        return False

    def inorder(self) -> list[int]:
        """Return values in ascending order."""
        result: list[int] = []

        def visit(node: BinarySearchTree._Node | None) -> None:
            if node is None:
                return
            visit(node.left)
            result.append(node.value)
            visit(node.right)

        visit(self._root)
        return result


if __name__ == "__main__":
    import unittest

    class TestBinarySearchTree(unittest.TestCase):
        def test_insert_and_search(self) -> None:
            tree = BinarySearchTree()
            for value in [8, 3, 10, 1, 6]:
                tree.insert(value)
            self.assertTrue(tree.contains(6))
            self.assertFalse(tree.contains(7))

        def test_inorder_returns_sorted_values(self) -> None:
            tree = BinarySearchTree()
            for value in [7, 2, 9, 1, 5, 8]:
                tree.insert(value)
            self.assertEqual(tree.inorder(), [1, 2, 5, 7, 8, 9])

        def test_duplicates_are_ignored(self) -> None:
            tree = BinarySearchTree()
            tree.insert(4)
            tree.insert(4)
            self.assertEqual(tree.inorder(), [4])

        def test_empty_tree(self) -> None:
            tree = BinarySearchTree()
            self.assertEqual(tree.inorder(), [])
            self.assertFalse(tree.contains(10))

    unittest.main()
