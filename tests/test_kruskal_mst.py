"""Unit tests for Kruskal's minimum spanning tree algorithm."""

import unittest

from algorithms.kruskal_mst import kruskal_mst


class TestKruskalMst(unittest.TestCase):
    def test_builds_a_minimum_spanning_tree(self) -> None:
        nodes = ["A", "B", "C", "D"]
        edges = [
            ("A", "B", 4),
            ("A", "C", 1),
            ("B", "C", 2),
            ("B", "D", 5),
            ("C", "D", 3),
        ]
        weight, tree = kruskal_mst(nodes, edges)
        self.assertEqual(weight, 6)
        self.assertEqual(len(tree), 3)

    def test_avoids_cycles(self) -> None:
        edges = [("A", "B", 1), ("B", "C", 2), ("A", "C", 3)]
        weight, tree = kruskal_mst(["A", "B", "C"], edges)
        self.assertEqual(weight, 3)
        self.assertEqual(len(tree), 2)

    def test_handles_a_disconnected_graph_as_a_forest(self) -> None:
        edges = [("A", "B", 2), ("C", "D", 1)]
        weight, tree = kruskal_mst(["A", "B", "C", "D"], edges)
        self.assertEqual(weight, 3)
        self.assertEqual(len(tree), 2)

    def test_ignores_self_loops(self) -> None:
        weight, tree = kruskal_mst(["A", "B"], [("A", "A", 1), ("A", "B", 4)])
        self.assertEqual(weight, 4)
        self.assertEqual(tree, [("A", "B", 4)])

    def test_supports_negative_weights(self) -> None:
        edges = [("A", "B", -2), ("B", "C", 3), ("A", "C", 1)]
        weight, _ = kruskal_mst(["A", "B", "C"], edges)
        self.assertEqual(weight, 1)

    def test_supports_decimal_weights(self) -> None:
        edges = [("A", "B", 1.5), ("B", "C", 2.25), ("A", "C", 4.0)]
        weight, _ = kruskal_mst(["A", "B", "C"], edges)
        self.assertEqual(weight, 3.75)

    def test_rejects_boolean_weights(self) -> None:
        with self.assertRaises(ValueError):
            kruskal_mst(["A", "B"], [("A", "B", True)])

    def test_does_not_modify_the_edges(self) -> None:
        edges = [("A", "B", 3), ("B", "C", 1)]
        original = edges.copy()
        kruskal_mst(["A", "B", "C"], edges)
        self.assertEqual(edges, original)


if __name__ == "__main__":
    unittest.main()
