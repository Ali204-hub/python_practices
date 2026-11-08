"""Build a minimum spanning tree with Kruskal's algorithm.

The graph is an undirected weighted edge list. Each edge is a
(source, target, weight) tuple. The algorithm uses the repository's
Union-Find implementation to detect cycles.

Time complexity: O(E log E) due to sorting the edges.
Run: python algorithms/kruskal_mst.py
"""

from data_structures.union_find import UnionFind


def kruskal_mst(
    nodes: list[str],
    edges: list[tuple[str, str, int | float]],
) -> tuple[int | float, list[tuple[str, str, int | float]]]:
    """Return (total weight, selected edges) for a minimum spanning forest.

    A disconnected graph returns a minimum spanning forest rather than
    raising an error. Self-loops are ignored.
    """
    node_set = set(nodes)
    for source, target, weight in edges:
        node_set.update((source, target))
        if isinstance(weight, bool) or not isinstance(weight, (int, float)):
            raise ValueError("Edge weights must be numbers.")

    uf = UnionFind(node_set)
    selected: list[tuple[str, str, int | float]] = []
    total_weight: int | float = 0

    for source, target, weight in sorted(edges, key=lambda edge: edge[2]):
        if source == target:
            continue
        if uf.union(source, target):
            selected.append((source, target, weight))
            total_weight += weight

    return total_weight, selected


def main() -> None:
    """Show the minimum spanning tree for a small network."""
    nodes = ["A", "B", "C", "D"]
    edges = [
        ("A", "B", 4),
        ("A", "C", 1),
        ("B", "C", 2),
        ("B", "D", 5),
        ("C", "D", 3),
    ]
    weight, tree = kruskal_mst(nodes, edges)
    print("Minimum spanning tree:", tree)
    print("Total weight:", weight)


if __name__ == "__main__":
    main()
