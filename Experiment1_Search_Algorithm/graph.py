r"""
Experiment 1 - Graph-theory dataset construction.

Builds the example graph used by both search algorithms (BFS and DFS).

Graph structure (tree rooted at A):

            A
          /   \
         B     C
        / \   / \
       D   E F   G

The graph is stored as an adjacency list:
a dictionary where each key is a node name,
and each value is the list of its neighbors (children).

BFS and DFS both work by "expanding" a node,
which means reading its neighbor list from this dictionary.
"""


def build_graph():
    """Return the example graph as an adjacency list (dictionary of lists).

    The neighbor lists are ordered (left to right as drawn above),
    so the traversal order of BFS and DFS is always the same
    and can be checked manually.
    """
    graph = {
        "A": ["B", "C"],  # A connects to B and C
        "B": ["D", "E"],  # B connects to D and E
        "C": ["F", "G"],  # C connects to F and G
        "D": [],          # leaf node (no neighbors)
        "E": [],          # leaf node (no neighbors)
        "F": [],          # leaf node (no neighbors)
        "G": [],          # leaf node (no neighbors)
    }
    return graph


def print_graph(graph):
    """Print the adjacency list in a human-readable way."""
    print("Graph (adjacency list):")
    for node, neighbors in graph.items():
        print(f"  {node} -> {neighbors}")


if __name__ == "__main__":
    graph = build_graph()
    print_graph(graph)
