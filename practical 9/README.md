Prim's Algorithm — Minimum Spanning Tree

A Python implementation of Prim's algorithm, which finds the Minimum Spanning Tree (MST) of a connected, weighted, undirected graph using a min-heap (priority queue).

What is a Minimum Spanning Tree?

Given a connected, weighted, undirected graph, a spanning tree is a subset of edges that connects all vertices without forming any cycle. The minimum spanning tree is the spanning tree with the smallest possible total edge weight.

How Prim's Algorithm Works

Prim's is a greedy algorithm that grows the MST one edge at a time:

Start from any vertex and mark it as visited.
Push all edges from the visited vertices into a min-heap.
Pop the edge with the smallest weight.
If it leads to an unvisited vertex, add the edge to the MST and mark that vertex visited.
Repeat steps 2-4 until all vertices are visited.
Complexity
Implementation	Time	Space
Min-heap + adj. list	O(n log n)	O(n+n)
Adjacency matrix	O(n²)	O(n²)
