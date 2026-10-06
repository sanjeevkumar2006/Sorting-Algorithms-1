Kruskal's Algorithm — Minimum Spanning Tree

A Python implementation of Kruskal's algorithm, which finds the Minimum Spanning Tree (MST) of a connected, weighted, undirected graph using sorted edges and a Disjoint Set Union (Union-Find) structure.

What is a Minimum Spanning Tree?

Given a connected, weighted, undirected graph, a spanning tree is a subset of edges that connects all vertices without forming any cycle. The minimum spanning tree is the spanning tree with the smallest possible total edge weight.

How Kruskal's Algorithm Works

Kruskal's is a greedy algorithm that builds the MST by picking the cheapest edges first:

Sort all edges in increasing order of weight.
Initialize a Disjoint Set so every vertex starts in its own component.
Take the next smallest edge (u, v).
If find(u) != find(v), the endpoints are in different components, so adding the edge creates no cycle. Add it to the MST and union(u, v).
Otherwise, skip the edge.
Stop when the MST has V - 1 edges.
Disjoint Set Union (Union-Find)

The cycle check relies on two operations:

find(x) returns the representative (root) of the set containing x, using path compression.
union(a, b) merges the two sets, using union by rank.

Together these make each operation nearly constant time.

Complexity
Step	Time
Sorting edges	O(E log E)
Union-Find operations	O(E · α(V))
Overall	O(E log E)
