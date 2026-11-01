"""Order the vertices of a directed acyclic graph with Kahn's algorithm.

The adjacency list maps each vertex to the vertices it points to.
Time complexity: O(V + E); auxiliary space: O(V).

Run: python algorithms/topological_sort.py
"""

from collections import deque


def topological_sort(graph: dict[str, list[str]]) -> list[str]:
    """Return a valid topological order, or raise ValueError for a cycle.

    Vertices that appear only as neighbors are included automatically.
    The graph is not modified. Multiple valid orders may exist.
    """
    indegree: dict[str, int] = {node: 0 for node in graph}

    # Include destination-only vertices and count each incoming edge.
    for neighbors in graph.values():
        for neighbor in neighbors:
            indegree.setdefault(neighbor, 0)
            indegree[neighbor] += 1

    ready = deque(node for node, degree in indegree.items() if degree == 0)
    order: list[str] = []

    while ready:
        current = ready.popleft()
        order.append(current)

        for neighbor in graph.get(current, []):
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                ready.append(neighbor)

    if len(order) != len(indegree):
        raise ValueError("Topological ordering is not possible: graph contains a cycle.")

    return order


def main() -> None:
    """Demonstrate a possible order for a small course prerequisite graph."""
    prerequisites = {
        "Programming": ["Data Structures"],
        "Data Structures": ["Algorithms"],
        "Mathematics": ["Algorithms"],
        "Algorithms": [],
    }
    print("Suggested study order:", " -> ".join(topological_sort(prerequisites)))


if __name__ == "__main__":
    main()
