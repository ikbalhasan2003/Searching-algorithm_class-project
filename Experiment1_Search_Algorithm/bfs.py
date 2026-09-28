"""
Experiment 1 - Breadth-First Search (BFS).

BFS explores the graph level by level: it first visits all
neighbors of the start node (level 1), then all nodes two
steps away (level 2), and so on.

The algorithm uses a queue (FIFO):
- nodes discovered earlier are expanded earlier,
- so every level is fully processed before the next level begins.
"""

from graph import build_graph


def bfs(graph, start):
    """Traverse the graph with breadth-first search.

    Args:
        graph: adjacency list (dictionary of lists), from build_graph().
        start: the node where the traversal begins (e.g. "A").

    Returns:
        The list of nodes in the order they were visited.
    """
    queue = [start]   # queue (FIFO): nodes waiting to be expanded
    visited = []      # nodes already visited, in visit order

    while queue:
        node = queue.pop(0)       # take the OLDEST node (front of the queue)

        if node not in visited:   # skip nodes that were already visited
            visited.append(node)  # record the visit

            # Enqueue children left to right,
            # so the whole current level is expanded before the next level.
            for child in graph[node]:
                queue.append(child)

    return visited


if __name__ == "__main__":
    graph = build_graph()
    print("Breadth-First Search (BFS)")
    print("Visit order:", bfs(graph, "A"))
