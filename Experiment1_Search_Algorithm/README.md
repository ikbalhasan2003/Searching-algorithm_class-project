# Experiment 1: Design and Implementation of Search Algorithm

University project for the "Introduction to Artificial Intelligence" course:
implementation of **Depth-First Search (DFS)** and **Breadth-First Search (BFS)**
on a graph-theory dataset, plus a NumPy syntax learning experiment.

## Project Structure

```
Experiment1_Search_Algorithm/
├── README.md            This file
├── requirements.txt     Python dependencies (numpy only)
├── numpy_experiment.py  NumPy syntax learning experiment
├── graph.py             Graph-theory dataset construction
├── dfs.py               Depth-First Search implementation
├── bfs.py               Breadth-First Search implementation
├── main.py              Runs the experiment and shows results
├── results/             Saved output of test runs
└── screenshots/         Screenshots for the experiment report
```

## Requirements

- Python 3.x
- NumPy

Install dependencies:

```
pip install -r requirements.txt
```

## How to Run

1. NumPy learning experiment:

   ```
   python numpy_experiment.py
   ```

2. Search algorithms (builds the graph, runs BFS and DFS, compares results):

   ```
   python main.py
   ```

## Course Materials

The primary references are located in `../Docs/`:

- `Experiment 1 Searching algorithm.docx`
- `Numpy.pptx`
- `Search Algortihm.pptx`
