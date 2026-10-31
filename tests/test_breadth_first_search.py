"""Unit tests for breadth-first search."""

import unittest

from algorithms.breadth_first_search import breadth_first_search


class TestBreadthFirstSearch(unittest.TestCase):
    def test_finds_a_shortest_path(self) -> None:
        graph = {
            "A": ["B", "C"],
            "B": ["D"],
            "C": ["D", "E"],
            "D": ["F"],
            "E": ["F"],
            "F": [],
        }
        path = breadth_first_search(graph, "A", "F")
        self.assertIsNotNone(path)
        self.assertEqual(len(path), 4)
        self.assertEqual(path[0], "A")
        self.assertEqual(path[-1], "F")

    def test_returns_none_when_goal_is_unreachable(self) -> None:
        graph = {"A": ["B"], "B": [], "C": []}
        self.assertIsNone(breadth_first_search(graph, "A", "C"))

    def test_returns_single_node_when_start_is_goal(self) -> None:
        self.assertEqual(breadth_first_search({}, "A", "A"), ["A"])

    def test_handles_missing_start_node(self) -> None:
        self.assertIsNone(breadth_first_search({}, "A", "B"))

    def test_can_reach_node_without_its_own_adjacency_entry(self) -> None:
        graph = {"A": ["B"]}
        self.assertEqual(breadth_first_search(graph, "A", "B"), ["A", "B"])

    def test_does_not_repeat_nodes_in_a_cycle(self) -> None:
        graph = {"A": ["B"], "B": ["A", "C"], "C": []}
        self.assertEqual(breadth_first_search(graph, "A", "C"), ["A", "B", "C"])


if __name__ == "__main__":
    unittest.main()
