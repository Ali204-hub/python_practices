"""Unit tests for the A* grid pathfinding algorithm."""

import unittest

from algorithms.a_star import a_star_shortest_path


class TestAStarShortestPath(unittest.TestCase):
    def test_finds_shortest_path_around_obstacles(self) -> None:
        grid = [
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0],
        ]
        path = a_star_shortest_path(grid, (0, 0), (2, 2))
        self.assertEqual(path, [
            (0, 0),
            (0, 1),
            (0, 2),
            (1, 2),
            (2, 2),
        ])

    def test_returns_none_when_goal_is_blocked(self) -> None:
        grid = [[0, 0], [0, 1]]
        self.assertIsNone(a_star_shortest_path(grid, (0, 0), (1, 1)))

    def test_returns_none_when_route_is_unreachable(self) -> None:
        grid = [
            [0, 1, 0],
            [1, 1, 1],
            [0, 1, 0],
        ]
        self.assertIsNone(a_star_shortest_path(grid, (0, 0), (2, 2)))

    def test_start_equal_to_goal(self) -> None:
        self.assertEqual(a_star_shortest_path([[0]], (0, 0), (0, 0)), [(0, 0)])

    def test_rejects_empty_grid(self) -> None:
        with self.assertRaises(ValueError):
            a_star_shortest_path([], (0, 0), (0, 0))

    def test_rejects_ragged_grid(self) -> None:
        with self.assertRaises(ValueError):
            a_star_shortest_path([[0, 0], [0]], (0, 0), (1, 0))

    def test_rejects_out_of_bounds_points(self) -> None:
        with self.assertRaises(ValueError):
            a_star_shortest_path([[0, 0]], (0, 0), (1, 0))

    def test_does_not_modify_grid(self) -> None:
        grid = [[0, 0], [0, 0]]
        original = [row.copy() for row in grid]
        a_star_shortest_path(grid, (0, 0), (1, 1))
        self.assertEqual(grid, original)


if __name__ == "__main__":
    unittest.main()
