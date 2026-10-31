"""Find shortest paths in an unweighted graph with breadth-first search.

Time complexity: O(V + E), where V is the number of vertices and E is
the number of edges explored. Auxiliary space: O(V).

The graph is represented as an adjacency list. Edges are directed:
add the reverse connection when an undirected edge is needed.

Run: python algorithms/breadth_first_search.py
"""

from collections import deque


def breadth_first_search(
    graph: dict[str, list[str]], start: str, goal: str
) -> list[str] | None:
    """Return a shortest path from start to goal, or None if unreachable.

    Breadth-first search explores vertices level by level, so the first
    discovered route to the goal uses the fewest edges.
    """
    if start == goal:
        return [start]

    queue = deque([start])
    parents: dict[str, str | None] = {start: None}

    while queue:
        current = queue.popleft()

        for neighbor in graph.get(current, []):
            if neighbor in parents:
                continue

            parents[neighbor] = current

            if neighbor == goal:
                path = [goal]
                node: str | None = current
                while node is not None:
                    path.append(node)
                    node = parents[node]
                return list(reversed(path))

            queue.append(neighbor)

    return None


def main() -> None:
    """Demonstrate a shortest route in a small graph."""
    graph = {
        "A": ["B", "C"],
        "B": ["D"],
        "C": ["D", "E"],
        "D": ["F"],
        "E": ["F"],
        "F": [],
    }

    path = breadth_first_search(graph, "A", "F")
    print("Shortest path:", " -> ".join(path) if path else "No path found")


if __name__ == "__main__":
    main()
