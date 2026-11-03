"""Unit tests for depth-first search."""

import unittest

from algorithms.depth_first_search import depth_first_search


class TestDepthFirstSearch(unittest.TestCase):
    def test_visits_neighbors_in_adjacency_order(self) -> None:
        graph = {
            "A": ["B", "C"],
            "B": ["D", "E"],
            "C": ["E"],
            "D": [],
            "E": [],
        }
        self.assertEqual(
            depth_first_search(graph, "A"),
            ["A", "B", "D", "E", "C"],
        )

    def test_handles_cycles_without_repeating_vertices(self) -> None:
        graph = {"A": ["B"], "B": ["A", "C"], "C": ["B"]}
        self.assertEqual(depth_first_search(graph, "A"), ["A", "B", "C"])

    def test_includes_a_start_vertex_missing_from_graph(self) -> None:
        self.assertEqual(depth_first_search({}, "X"), ["X"])

    def test_does_not_include_unreachable_vertices(self) -> None:
        graph = {"A": ["B"], "B": [], "Z": []}
        self.assertEqual(depth_first_search(graph, "A"), ["A", "B"])

    def test_handles_repeated_edges(self) -> None:
        self.assertEqual(depth_first_search({"A": ["B", "B"], "B": []}, "A"), ["A", "B"])

    def test_does_not_modify_the_graph(self) -> None:
        graph = {"A": ["B"], "B": []}
        original = {node: neighbors.copy() for node, neighbors in graph.items()}
        depth_first_search(graph, "A")
        self.assertEqual(graph, original)


if __name__ == "__main__":
    unittest.main()
