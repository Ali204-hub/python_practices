"""Unit tests for Bellman-Ford shortest path."""

import math
import unittest

from algorithms.bellman_ford import bellman_ford_shortest_path


class TestBellmanFordShortestPath(unittest.TestCase):
    def test_finds_shortest_path_with_a_negative_edge(self) -> None:
        graph = {
            "A": [("B", 4), ("C", 5)],
            "B": [("C", -2), ("D", 4)],
            "C": [("D", 3)],
            "D": [],
        }
        self.assertEqual(
            bellman_ford_shortest_path(graph, "A", "D"),
            (5, ["A", "B", "C", "D"]),
        )

    def test_returns_none_for_an_unreachable_goal(self) -> None:
        graph = {"A": [("B", 1)], "B": [], "C": []}
        self.assertIsNone(bellman_ford_shortest_path(graph, "A", "C"))

    def test_start_equal_to_goal_has_zero_cost(self) -> None:
        self.assertEqual(bellman_ford_shortest_path({}, "A", "A"), (0, ["A"]))

    def test_detects_a_reachable_negative_cycle(self) -> None:
        graph = {"A": [("B", 1)], "B": [("C", -2)], "C": [("A", 0)]}
        with self.assertRaises(ValueError):
            bellman_ford_shortest_path(graph, "A", "C")

    def test_ignores_a_negative_cycle_unreachable_from_start(self) -> None:
        graph = {
            "A": [("B", 3)],
            "B": [],
            "X": [("Y", -2)],
            "Y": [("X", 1)],
        }
        self.assertEqual(
            bellman_ford_shortest_path(graph, "A", "B"),
            (3, ["A", "B"]),
        )

    def test_rejects_non_finite_boolean_and_non_numeric_weights(self) -> None:
        for weight in (math.inf, math.nan, -math.inf, True, "3"):
            with self.subTest(weight=weight):
                with self.assertRaises(ValueError):
                    bellman_ford_shortest_path({"A": [("B", weight)]}, "A", "B")

    def test_rejects_malformed_edges(self) -> None:
        with self.assertRaises(ValueError):
            bellman_ford_shortest_path({"A": [("B", 1, "extra")]}, "A", "B")

    def test_includes_vertices_that_only_appear_as_neighbors(self) -> None:
        self.assertEqual(
            bellman_ford_shortest_path({"A": [("B", -2)]}, "A", "B"),
            (-2, ["A", "B"]),
        )

    def test_does_not_modify_the_graph(self) -> None:
        graph = {"A": [("B", -1)], "B": []}
        original = {node: neighbors.copy() for node, neighbors in graph.items()}
        bellman_ford_shortest_path(graph, "A", "B")
        self.assertEqual(graph, original)


if __name__ == "__main__":
    unittest.main()
