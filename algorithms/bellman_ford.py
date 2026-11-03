"""Find shortest paths when a graph can contain negative edge weights.

The graph is a directed adjacency list where each edge is
(neighbor, weight). Negative weights are supported, but a reachable
negative-weight cycle makes a shortest path undefined.

Time complexity: O(V * E); auxiliary space: O(V + E).

Run: python algorithms/bellman_ford.py
"""

import math


def bellman_ford_shortest_path(
    graph: dict[str, list[tuple[str, int | float]]],
    start: str,
    goal: str,
) -> tuple[int | float, list[str]] | None:
    """Return (minimum distance, path), or None if goal is unreachable.

    Raises ValueError for malformed edges, non-numeric/non-finite weights,
    or a negative-weight cycle reachable from start. The original graph
    is not modified.
    """
    edges: list[tuple[str, str, int | float]] = []
    vertices = set(graph)

    # Flatten and validate the edge list before running the algorithm.
    for source, neighbors in graph.items():
        for edge in neighbors:
            if not isinstance(edge, (tuple, list)) or len(edge) != 2:
                raise ValueError("Each edge must contain a neighbor and a weight.")

            neighbor, weight = edge

            if isinstance(weight, bool) or not isinstance(weight, (int, float)):
                raise ValueError("Edge weights must be numbers.")

            if isinstance(weight, float) and not math.isfinite(weight):
                raise ValueError("Edge weights must be finite.")

            vertices.add(neighbor)
            edges.append((source, neighbor, weight))

    distances: dict[str, int | float] = {start: 0}
    parents: dict[str, str] = {}

    # Relax every edge at most |V| - 1 times.
    for _ in range(max(len(vertices) - 1, 0)):
        updated = False

        for source, target, weight in edges:
            if source not in distances:
                continue

            candidate = distances[source] + weight
            if target not in distances or candidate < distances[target]:
                distances[target] = candidate
                parents[target] = source
                updated = True

        # Stop early when a complete pass makes no improvement.
        if not updated:
            break

    # One more relaxation pass reveals a negative cycle reachable from start.
    for source, target, weight in edges:
        if source in distances:
            candidate = distances[source] + weight
            if target not in distances or candidate < distances[target]:
                raise ValueError("A reachable negative-weight cycle was detected.")

    if goal not in distances:
        return None

    path = [goal]
    while path[-1] != start:
        path.append(parents[path[-1]])

    path.reverse()
    return distances[goal], path


def main() -> None:
    """Compare routes where one road has a negative adjustment."""
    graph = {
        "A": [("B", 4), ("C", 5)],
        "B": [("C", -2), ("D", 4)],
        "C": [("D", 3)],
        "D": [],
    }

    result = bellman_ford_shortest_path(graph, "A", "D")
    if result is None:
        print("No route found.")
    else:
        distance, path = result
        print("Shortest path:", " -> ".join(path))
        print("Total cost:", distance)


if __name__ == "__main__":
    main()
