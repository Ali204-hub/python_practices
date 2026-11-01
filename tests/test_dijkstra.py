"""Unit tests for Dijkstra's shortest-path algorithm."""

import math
import unittest

from algorithms.dijkstra import dijkstra_shortest_path


class TestDijkstraShortestPath(unittest.TestCase):
    def test_finds_the_lowest_cost_path(self) -> None:
        graph = {
            "A": [("B", 4), ("C", 1)],
            "B": [("D", 1)],
            "C": [("B", 2), ("D", 8)],
            "D": [],
        }
        self.assertEqual(dijkstra_shortest_path(graph, "A", "D"), (4, ["A", "C", "B", "D"]))

    def test_returns_none_when_goal_is_unreachable(self) -> None:
        self.assertIsNone(dijkstra_shortest_path({"A": [("B", 2)], "C": []}, "A", "C"))

    def test_start_equal_to_goal_has_zero_cost(self) -> None:
        self.assertEqual(dijkstra_shortest_path({}, "A", "A"), (0, ["A"]))

    def test_supports_zero_weight_edges(self) -> None:
        graph = {"A": [("B", 0)], "B": [("C", 2)], "C": []}
        self.assertEqual(dijkstra_shortest_path(graph, "A", "C"), (2, ["A", "B", "C"]))

    def test_supports_decimal_weights(self) -> None:
        graph = {"A": [("B", 1.5), ("C", 3.0)], "B": [("C", 0.5)], "C": []}
        self.assertEqual(dijkstra_shortest_path(graph, "A", "C"), (2.0, ["A", "B", "C"]))

    def test_rejects_negative_weights(self) -> None:
        with self.assertRaises(ValueError):
            dijkstra_shortest_path({"A": [("B", -1)]}, "A", "B")

    def test_rejects_non_finite_weights(self) -> None:
        for weight in (math.inf, math.nan, -math.inf):
            with self.subTest(weight=weight):
                with self.assertRaises(ValueError):
                    dijkstra_shortest_path({"A": [("B", weight)]}, "A", "B")

    def test_rejects_boolean_weight(self) -> None:
        with self.assertRaises(ValueError):
            dijkstra_shortest_path({"A": [("B", True)]}, "A", "B")

    def test_does_not_modify_the_graph(self) -> None:
        graph = {"A": [("B", 3)], "B": []}
        original = {node: edges.copy() for node, edges in graph.items()}
        dijkstra_shortest_path(graph, "A", "B")
        self.assertEqual(graph, original)


if __name__ == "__main__":
    unittest.main()
