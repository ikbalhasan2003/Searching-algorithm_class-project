"""
Experiment 1 - Depth-First Search (DFS).

DFS tries to go as deep into the graph as possible.
It expands a node, continues deeper when possible,
and backtracks when it cannot continue along the
current path.

The algorithm uses a stack (LIFO):
- the newest discovered node is always expanded first,
- when a dead end is reached (no unvisited children),
  backtracking happens automatically, because the
  previous path nodes are still waiting on the stack.
"""

from graph import build_graph


def dfs(graph, start):
    """Traverse the graph with depth-first search.

    Args:
        graph: adjacency list (dictionary of lists), from build_graph().
        start: the node where the traversal begins (e.g. "A").

    Returns:
        The list of nodes in the order they were visited.
    """
    stack = [start]   # stack (LIFO): nodes waiting to be expanded
    visited = []      # nodes already visited, in visit order

    while stack:
        node = stack.pop()          # take the most recently added node (go deeper)

        if node not in visited:     # skip nodes that were already visited
            visited.append(node)    # record the visit

            # Push the children in REVERSE order,
            # so the leftmost child ends up on top of the stack
            # and is expanded first.
            for child in reversed(graph[node]):
                stack.append(child)

    return visited


if __name__ == "__main__":
    graph = build_graph()
    print("Depth-First Search (DFS)")
    print("Visit order:", dfs(graph, "A"))
