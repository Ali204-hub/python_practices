"""Unit tests for topological sort."""

import unittest

from algorithms.topological_sort import topological_sort


class TestTopologicalSort(unittest.TestCase):
    def assert_edges_follow_order(self, graph: dict[str, list[str]], order: list[str]) -> None:
        positions = {node: index for index, node in enumerate(order)}
        for node, neighbors in graph.items():
            for neighbor in neighbors:
                self.assertLess(positions[node], positions[neighbor])

    def test_returns_a_valid_prerequisite_order(self) -> None:
        graph = {"A": ["C"], "B": ["C"], "C": ["D"], "D": []}
        order = topological_sort(graph)
        self.assertEqual(set(order), set(graph))
        self.assert_edges_follow_order(graph, order)

    def test_includes_vertices_that_only_appear_as_neighbors(self) -> None:
        graph = {"A": ["B"]}
        self.assertEqual(topological_sort(graph), ["A", "B"])

    def test_handles_disconnected_vertices(self) -> None:
        graph = {"A": [], "B": [], "C": ["D"], "D": []}
        order = topological_sort(graph)
        self.assertEqual(set(order), set(graph))
        self.assert_edges_follow_order(graph, order)

    def test_handles_an_empty_graph(self) -> None:
        self.assertEqual(topological_sort({}), [])

    def test_rejects_a_cycle(self) -> None:
        graph = {"A": ["B"], "B": ["C"], "C": ["A"]}
        with self.assertRaises(ValueError):
            topological_sort(graph)

    def test_rejects_a_self_loop(self) -> None:
        with self.assertRaises(ValueError):
            topological_sort({"A": ["A"]})

    def test_handles_repeated_edges(self) -> None:
        graph = {"A": ["B", "B"], "B": []}
        self.assertEqual(topological_sort(graph), ["A", "B"])

    def test_does_not_modify_the_graph(self) -> None:
        graph = {"A": ["B"], "B": []}
        original = {node: neighbors.copy() for node, neighbors in graph.items()}
        topological_sort(graph)
        self.assertEqual(graph, original)


if __name__ == "__main__":
    unittest.main()
