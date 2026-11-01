"""Find shortest paths in a weighted graph with Dijkstra's algorithm.

All edge weights must be finite and non-negative. The graph uses an
adjacency list: each node maps to (neighbor, weight) pairs.

Time complexity: O((V + E) log V) with a binary heap.
Run: python algorithms/dijkstra.py
"""

import heapq
import math


def dijkstra_shortest_path(
    graph: dict[str, list[tuple[str, int | float]]],
    start: str,
    goal: str,
) -> tuple[int | float, list[str]] | None:
    """Return (minimum distance, path) or None when goal is unreachable."""
    # Dijkstra's algorithm is not correct when an edge has a negative weight.
    for edges in graph.values():
        for neighbor, weight in edges:
            if isinstance(weight, bool) or not isinstance(weight, (int, float)):
                raise ValueError("Edge weights must be numbers.")
            if weight < 0 or (isinstance(weight, float) and not math.isfinite(weight)):
                raise ValueError("Edge weights must be finite and non-negative.")

    distances: dict[str, int | float] = {start: 0}
    parents: dict[str, str] = {}
    priority_queue: list[tuple[int | float, str]] = [(0, start)]

    while priority_queue:
        distance, current = heapq.heappop(priority_queue)

        # Ignore an outdated queue entry after a shorter route was found.
        if distance != distances[current]:
            continue

        if current == goal:
            path = [goal]
            while path[-1] != start:
                path.append(parents[path[-1]])
            return distance, list(reversed(path))

        for neighbor, weight in graph.get(current, []):
            new_distance = distance + weight
            if new_distance < distances.get(neighbor, math.inf):
                distances[neighbor] = new_distance
                parents[neighbor] = current
                heapq.heappush(priority_queue, (new_distance, neighbor))

    return None


def main() -> None:
    """Show the cheapest route between two sample locations."""
    graph = {
        "Home": [("Market", 4), ("College", 2)],
        "College": [("Market", 1), ("Library", 5)],
        "Market": [("Library", 1)],
        "Library": [],
    }
    result = dijkstra_shortest_path(graph, "Home", "Library")
    if result is None:
        print("No route found.")
    else:
        distance, path = result
        print("Cheapest route:", " -> ".join(path))
        print("Total distance:", distance)


if __name__ == "__main__":
    main()
