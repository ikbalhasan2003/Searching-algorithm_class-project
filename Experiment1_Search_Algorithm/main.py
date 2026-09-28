"""
Experiment 1 - Main entry point.

Builds the graph, runs BFS and DFS, shows the results of both
search algorithms and compares them.

Run this file with:
    python main.py
"""

from graph import build_graph, print_graph
from dfs import dfs
from bfs import bfs

# The graph is a tree, so every node is reachable from the root "A".
START_NODE = "A"

# Text file where a copy of the console output is saved,
# so the results can be looked at again while writing the report.
RESULTS_FILE = "results/comparison.txt"


def compare_results(dfs_order, bfs_order):
    """Print a short comparison of the two traversal orders."""
    print("=" * 60)
    print("Comparison of DFS and BFS")
    print("=" * 60)

    print("DFS visits:", dfs_order)
    print("BFS visits:", bfs_order)
    print()

    # Both algorithms visit every node of the graph exactly once,
    # but in a different order (unless the graph is very small).
    print("Both algorithms visited all", len(dfs_order), "nodes, but in a different order:")
    print("  - DFS goes DEEP first  (follows one branch, then backtracks).")
    print("  - BFS goes WIDE first  (visits all nodes of one level, then the next).")

    if dfs_order == bfs_order:
        print("  Here both orders happen to be identical.")
    else:
        first_difference = next(
            i for i in range(len(dfs_order)) if dfs_order[i] != bfs_order[i]
        )
        print("  The first difference is at position", first_difference, ":")
        print("    DFS visits", dfs_order[first_difference], "- BFS visits", bfs_order[first_difference])


if __name__ == "__main__":
    # --- 1. Build and show the graph dataset -----------------------------
    graph = build_graph()
    print_graph(graph)

    # --- 2. Run DFS -------------------------------------------------------
    print()
    print("Depth-First Search (DFS)")
    dfs_order = dfs(graph, START_NODE)
    print("Visit order:", dfs_order)

    # --- 3. Run BFS -------------------------------------------------------
    print()
    print("Breadth-First Search (BFS)")
    bfs_order = bfs(graph, START_NODE)
    print("Visit order:", bfs_order)

    # --- 4. Compare the two results ---------------------------------------
    print()
    compare_results(dfs_order, bfs_order)

    # --- 5. Save a copy of the results to a text file ---------------------
    lines = []   # the summary written to the results file
    lines.append("Experiment 1 - search algorithm results")
    lines.append("")
    lines.append("Graph (adjacency list):")
    for node, neighbors in graph.items():
        lines.append(f"  {node} -> {neighbors}")
    lines.append("")
    lines.append("DFS visit order: " + " -> ".join(dfs_order))
    lines.append("BFS visit order: " + " -> ".join(bfs_order))

    with open(RESULTS_FILE, "w", encoding="utf-8") as file:
        file.write("\n".join(lines) + "\n")

    print()
    print("Results saved to", RESULTS_FILE)
