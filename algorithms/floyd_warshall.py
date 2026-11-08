"""Compute all-pairs shortest paths with Floyd-Warshall.

The graph is represented as a mapping of nodes to weighted outgoing edges.
Missing edges are treated as unreachable. Negative edge weights are allowed,
but a negative cycle raises ValueError.

Time complexity: O(V^3); space complexity: O(V^2).
Run: python algorithms/floyd_warshall.py
"""

import math


def floyd_warshall(
    graph: dict[str, list[tuple[str, int | float]]],
) -> dict[str, dict[str, int | float]]:
    """Return the shortest distance between every pair of vertices."""
    nodes = set(graph)
    for edges in graph.values():
        for neighbor, weight in edges:
            nodes.add(neighbor)
            if isinstance(weight, bool) or not isinstance(weight, (int, float)):
                raise ValueError("Edge weights must be numbers.")
            if isinstance(weight, float) and not math.isfinite(weight):
                raise ValueError("Edge weights must be finite.")

    distances: dict[str, dict[str, int | float]] = {
        source: {target: (0 if source == target else math.inf) for target in nodes}
        for source in nodes
    }

    for source, edges in graph.items():
        for target, weight in edges:
            distances[source][target] = min(distances[source][target], weight)

    for via in nodes:
        for source in nodes:
            if distances[source][via] == math.inf:
                continue
            for target in nodes:
                through_via = distances[source][via] + distances[via][target]
                if through_via < distances[source][target]:
                    distances[source][target] = through_via

    if any(distances[node][node] < 0 for node in nodes):
        raise ValueError("Graph contains a negative-weight cycle.")

    return distances


def main() -> None:
    """Show the cheapest distance between every pair in a sample graph."""
    graph = {
        "A": [("B", 3), ("C", 10)],
        "B": [("C", 2)],
        "C": [],
    }
    distances = floyd_warshall(graph)
    print("Shortest A -> C:", distances["A"]["C"])


if __name__ == "__main__":
    main()
