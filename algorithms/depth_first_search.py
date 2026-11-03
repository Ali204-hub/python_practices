"""Traverse a graph depth-first without using recursive calls.

The graph is represented as an adjacency list. Neighbors are visited in
the same order in which they appear in each adjacency list.

Time complexity: O(V + E); auxiliary space: O(V).

Run: python algorithms/depth_first_search.py
"""


def depth_first_search(graph: dict[str, list[str]], start: str) -> list[str]:
    """Return the depth-first traversal order starting from start.

    Vertices that cannot be reached from start are not included. A vertex
    is returned only once, even when the graph contains cycles or repeated
    edges. The original graph is not modified.
    """
    stack = [start]
    visited: set[str] = set()
    order: list[str] = []

    while stack:
        current = stack.pop()

        if current in visited:
            continue

        visited.add(current)
        order.append(current)

        # Reverse before pushing so the first listed neighbor is visited first.
        for neighbor in reversed(graph.get(current, [])):
            if neighbor not in visited:
                stack.append(neighbor)

    return order


def main() -> None:
    """Demonstrate depth-first traversal on a small friendship network."""
    graph = {
        "Ali": ["Hassan", "Sara"],
        "Hassan": ["Usman", "Sara"],
        "Sara": ["Ayesha"],
        "Usman": [],
        "Ayesha": [],
    }

    print("DFS visit order:", " -> ".join(depth_first_search(graph, "Ali")))


if __name__ == "__main__":
    main()
