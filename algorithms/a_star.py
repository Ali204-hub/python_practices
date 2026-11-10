"""Find a shortest path on a rectangular grid with A* search.

The grid uses 0 for open cells and 1 for blocked cells. Movement is limited
to the four cardinal directions, and every move has cost 1.

Time complexity: O(V log V) in the worst case.
Run: python algorithms/a_star.py
"""

import heapq


Grid = list[list[int]]
Point = tuple[int, int]


def a_star_shortest_path(grid: Grid, start: Point, goal: Point) -> list[Point] | None:
    """Return the shortest grid path from start to goal, or None if unreachable."""
    if not grid or not grid[0]:
        raise ValueError("Grid must not be empty.")

    rows = len(grid)
    cols = len(grid[0])

    if any(len(row) != cols for row in grid):
        raise ValueError("Grid rows must have the same length.")

    for point in (start, goal):
        row, col = point
        if not (0 <= row < rows and 0 <= col < cols):
            raise ValueError("Start and goal must be inside the grid.")

    if grid[start[0]][start[1]] or grid[goal[0]][goal[1]]:
        return None

    def heuristic(point: Point) -> int:
        return abs(point[0] - goal[0]) + abs(point[1] - goal[1])

    neighbors = ((-1, 0), (1, 0), (0, -1), (0, 1))
    costs: dict[Point, int] = {start: 0}
    parents: dict[Point, Point] = {}
    queue: list[tuple[int, int, Point]] = [(heuristic(start), 0, start)]

    while queue:
        _, current_cost, current = heapq.heappop(queue)

        if current_cost != costs[current]:
            continue

        if current == goal:
            path = [goal]
            while path[-1] != start:
                path.append(parents[path[-1]])
            return list(reversed(path))

        row, col = current
        for row_step, col_step in neighbors:
            next_point = (row + row_step, col + col_step)
            next_row, next_col = next_point

            if not (0 <= next_row < rows and 0 <= next_col < cols):
                continue
            if grid[next_row][next_col]:
                continue

            new_cost = current_cost + 1
            if new_cost < costs.get(next_point, float("inf")):
                costs[next_point] = new_cost
                parents[next_point] = current
                priority = new_cost + heuristic(next_point)
                heapq.heappush(queue, (priority, new_cost, next_point))

    return None


def main() -> None:
    """Show a shortest route through a sample grid."""
    grid = [
        [0, 0, 0, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 0],
    ]
    path = a_star_shortest_path(grid, (0, 0), (2, 3))
    print("Path:", path)


if __name__ == "__main__":
    main()
