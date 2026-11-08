"""Unit tests for Floyd-Warshall all-pairs shortest paths."""

import math
import unittest

from algorithms.floyd_warshall import floyd_warshall


class TestFloydWarshall(unittest.TestCase):
    def test_finds_shortest_paths_through_intermediate_vertices(self) -> None:
        graph = {"A": [("B", 3), ("C", 10)], "B": [("C", 2)], "C": []}
        distances = floyd_warshall(graph)
        self.assertEqual(distances["A"]["C"], 5)

    def test_returns_zero_for_same_vertex(self) -> None:
        distances = floyd_warshall({"A": [], "B": []})
        self.assertEqual(distances["A"]["A"], 0)

    def test_marks_unreachable_vertices_as_infinity(self) -> None:
        distances = floyd_warshall({"A": [("B", 1)], "C": []})
        self.assertEqual(distances["A"]["C"], math.inf)

    def test_includes_destination_only_vertices(self) -> None:
        distances = floyd_warshall({"A": [("B", 4)]})
        self.assertEqual(set(distances), {"A", "B"})
        self.assertEqual(distances["A"]["B"], 4)

    def test_supports_negative_edges_without_negative_cycle(self) -> None:
        graph = {"A": [("B", 4), ("C", 5)], "B": [("C", -2)], "C": []}
        self.assertEqual(floyd_warshall(graph)["A"]["C"], 2)

    def test_detects_negative_cycles(self) -> None:
        graph = {"A": [("B", 1)], "B": [("A", -2)]}
        with self.assertRaises(ValueError):
            floyd_warshall(graph)

    def test_rejects_non_finite_weights(self) -> None:
        with self.assertRaises(ValueError):
            floyd_warshall({"A": [("B", math.inf)]})

    def test_does_not_modify_the_graph(self) -> None:
        graph = {"A": [("B", 2)], "B": []}
        original = {node: edges.copy() for node, edges in graph.items()}
        floyd_warshall(graph)
        self.assertEqual(graph, original)


if __name__ == "__main__":
    unittest.main()
