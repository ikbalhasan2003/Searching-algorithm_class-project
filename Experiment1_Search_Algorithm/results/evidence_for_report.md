# Experiment 1 — Report Evidence Organizer

This file only organizes factual evidence and implementation information.
It is NOT the report. Use it as a source of facts while writing the report yourself.
All results below were obtained by actually executing the project on 2026-09-28.

---

## 1. Experiment Title

- "Design and implementation of search algorithm" (Experiment 1, Introduction to Artificial Intelligence).
- **ADDITIONAL INFORMATION**: full title, purpose, and requirements are in `../Docs/Experiment 1 Searching algorithm.docx`.

## 2. Purpose and Requirements

**COURSE CONCEPT** (from the experiment requirements document):
1. Master the configuration of the Python programming environment and the basic syntax of Python.
2. Implement classical search algorithms through programming, including depth-first and breadth-first search algorithms, and deepen the understanding of artificial intelligence algorithms.

Requirements:
- Clearly state the configuration process of the Python programming environment (Anaconda/PyCharm/VS Code and library installation).
- Specify the NumPy syntax learning process, including experimental code and results display.
- Explain the principles of breadth-first and depth-first search algorithms.
- Realize the construction of a graph-theory data set and the code of BFS and DFS.
- Write the code steps and show the results.
- Compare the results of different search algorithms.

## 3. Experimental Environment

**ACTUAL RESULT** (measured on this machine):
- OS: Windows
- Python: 3.13.15 (`C:\Users\user\AppData\Local\Programs\Python\Python313\python.exe`)
- NumPy: 2.5.3
- Editor: VS Code (workspace `Searching algorithm`)

**MY PERSONAL INFORMATION NEEDED**:
- Whether you personally installed Anaconda or used plain Python, and your installation steps/screenshots.
- Whether you use PyCharm or VS Code, and your editor setup screenshots.

## 4. Procedure / Flow Chart Information

**ADDITIONAL INFORMATION**: the intended experiment flow is:

```
Environment -> NumPy Learning -> Graph Dataset -> DFS -> BFS -> Execution -> Results -> Comparison
```

For the report you should draw a flow chart yourself. The actual executed flow was:
1. `numpy_experiment.py` (NumPy syntax learning)
2. `graph.py` (graph dataset construction)
3. `dfs.py` (DFS traversal)
4. `bfs.py` (BFS traversal)
5. `main.py` (integrated run + comparison)

## 5. NumPy Learning and Experimental Code

- **File**: `numpy_experiment.py` (single file, 12 demo functions, one per course topic).
- **Topics covered**: overview, array creation, ndarray attributes, slicing, multidimensional arrays, ufunc/arithmetic, comparison, broadcasting, random numbers, statistics, sorting, vstack/hstack/column_stack/split.
- **ACTUAL RESULT**: executed successfully, exit code 0, no errors. Full console output is saved in `results/numpy_output.txt`. Key actual outputs:
  - `np.arange(1, 20, 5)` = `[1 6 11 16]`
  - attributes of a (3,4) array: `shape=(3,4)`, `size=12`, `dtype=int64`, `ndim=2`
  - slicing view behavior demonstrated (`b[0] = -10` also changed `a`)
  - random array with `np.random.seed(42)`: `np.sum(a)=92`, `np.mean(a)=4.6`, `np.var(a)=7.94`, `np.std(a)≈2.8178`
  - `np.median(a)=4.5`, `np.ptp(a)=9`
- **Screenshot to capture**: run `python numpy_experiment.py` in the VS Code terminal and screenshot the output (e.g., one screenshot for sections 1–6 and one for sections 7–12).

## 6. Graph Dataset Construction

- **File**: `graph.py` (function `build_graph()` returns an adjacency list — a dictionary of lists).
- **Structure**: tree rooted at A:

```
        A
      /   \
     B     C
    / \   / \
   D   E F   G
```

- Adjacency list (as actually printed):

```
A -> ['B', 'C']
B -> ['D', 'E']
C -> ['F', 'G']
D -> []
E -> []
F -> []
G -> []
```

- **ACTUAL RESULT**: executed successfully; output saved in `results/graph_output.txt`.
- **Screenshot to capture**: console output of `python graph.py`, or the graph section at the top of `main.py` output.
- **COURSE CONCEPT**: the course slides build the graph with a `Graph` class and `add_node`; this project uses the simpler equivalent — a plain dictionary of neighbor lists, which both algorithms read directly.

## 7. DFS Principle

**COURSE CONCEPT** (from slides, section 4.2.5):
- DFS tries to get as deep into the tree as quickly as possible; it always chooses the leftmost branch, and backtracks when a dead end is reached.
- Search and backtracking alternate: expand a node, follow its child deeper; when a node cannot be expanded, fall back to a sibling; if no sibling, go back to the parent's siblings.
- Implemented with a stack (LIFO).

## 8. DFS Implementation

- **File**: `dfs.py` (function `dfs(graph, start)`).
- **Key steps** (read from the actual code):
  1. Initialize `stack = [start]`, `visited = []`.
  2. Pop the most recently added node (`stack.pop()`).
  3. If not visited: record it, push its children in REVERSE order (so the leftmost child is on top of the stack and is expanded first).
  4. Repeat until the stack is empty.
- Comments in the file explain every step.

## 9. DFS Experimental Result

**ACTUAL RESULT** (from real execution):

```
Depth-First Search (DFS)
Visit order: ['A', 'B', 'D', 'E', 'C', 'F', 'G']
```

- Saved in `results/dfs_output.txt`.
- **Screenshot to capture**: console output of `python dfs.py`.
- **Observation**: this matches the DFS order given in the course slides (A, B, D, E, C, F, G): A -> B (leftmost) -> D (leftmost, deepest) -> E (sibling, backtrack to B) -> C (backtrack to A) -> F -> G.

## 10. BFS Principle

**COURSE CONCEPT** (from slides, section 4.2.6):
- BFS accesses nodes layer by layer, from the top of the tree to the bottom, left to right.
- All nodes of level i must be visited before any node of level i+1.
- Implemented with a queue (FIFO): nodes discovered earlier are expanded earlier.

## 11. BFS Implementation

- **File**: `bfs.py` (function `bfs(graph, start)`).
- **Key steps** (read from the actual code):
  1. Initialize `queue = [start]`, `visited = []`.
  2. Take the OLDEST node from the queue (`queue.pop(0)`).
  3. If not visited: record it, enqueue its children left to right.
  4. Repeat until the queue is empty.

## 12. BFS Experimental Result

**ACTUAL RESULT** (from real execution):

```
Breadth-First Search (BFS)
Visit order: ['A', 'B', 'C', 'D', 'E', 'F', 'G']
```

- Saved in `results/bfs_output.txt`.
- **Screenshot to capture**: console output of `python bfs.py`.
- **Observation**: this matches the BFS order given in the course slides (A, B, C, D, E, F, G): level 0 = A, level 1 = B, C, level 2 = D, E, F, G.

## 13. Comparison and Analysis of BFS and DFS

**ACTUAL RESULT** (from the real `main.py` execution, saved in `results/main_output.txt` and `results/comparison.txt`):

```
DFS visits: ['A', 'B', 'D', 'E', 'C', 'F', 'G']
BFS visits: ['A', 'B', 'C', 'D', 'E', 'F', 'G']

Both algorithms visited all 7 nodes, but in a different order:
  - DFS goes DEEP first  (follows one branch, then backtracks).
  - BFS goes WIDE first  (visits all nodes of one level, then the next).
  The first difference is at position 2:
    DFS visits D - BFS visits C
```

Factual points you can analyze in the report:
- Both algorithms visit all 7 nodes exactly once (complete traversal of a connected graph/tree).
- First difference is at index 2: DFS visits D (level 2, deep branch) while BFS visits C (level 1, same level as B).
- DFS order reflects depth + backtracking; BFS order reflects level-by-layer expansion.
- Data structure difference: DFS = stack (LIFO), BFS = queue (FIFO) — only this changes the order.

**Screenshot to capture**: the full console output of `python main.py` (graph + DFS + BFS + comparison in one image).

## 14. Source Code

- `numpy_experiment.py` — NumPy learning experiment (12 topics).
- `graph.py` — graph dataset construction (adjacency list).
- `dfs.py` — depth-first search (stack-based).
- `bfs.py` — breadth-first search (queue-based).
- `main.py` — integration: builds graph, runs DFS and BFS, compares, saves results.
- `requirements.txt` — dependencies (`numpy`).
- All code contains docstrings and comments.

## 15. Experimental Summary / Points to Reflect On

**MY PERSONAL INFORMATION NEEDED** (the report must be written independently; write these in your own words):
- What you learned about the Python environment setup.
- What you learned from the NumPy syntax experiment.
- Your understanding of DFS vs BFS after seeing the real outputs.
- Difficulties you met (installation, code, understanding) and how you solved them.

**ADDITIONAL INFORMATION** (facts you may reflect on):
- The whole experiment ran without errors (all exit codes 0).
- The results matched the theory given in the course slides, which is a good verification point.
