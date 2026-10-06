Graph Traversal — BFS and DFS

Python implementations of the two fundamental graph traversal algorithms: Breadth-First Search (BFS) and Depth-First Search (DFS).

Files
File	Description
bfs.py	BFS using a queue (collections.deque and popleft())
dfs.py	DFS using a stack (list and pop()), plus a recursive version
Breadth-First Search (BFS)

BFS explores a graph level by level: it visits the start node, then all its neighbors, then their neighbors, and so on.

How it works
Put the start node in a queue and mark it visited.
Remove the node at the front of the queue with popleft().
Add every unvisited neighbor to the back of the queue and mark it visited.
Repeat until the queue is empty.
Why popleft()?

BFS needs first-in, first-out (FIFO) order. deque.popleft() removes from the front in O(1). Using list.pop(0) also works but costs O(n), because every remaining element shifts.

Depth-First Search (DFS)

DFS goes as deep as possible along a path before backtracking.

How it works
Push the start node onto a stack.
Remove the node at the top of the stack with pop().
If it has not been visited, mark it visited and push its unvisited neighbors.
Repeat until the stack is empty.

A recursive version is also included; it uses the call stack instead of an explicit stack.

Why pop()?

DFS needs last-in, first-out (LIFO) order. list.pop() removes from the back in O(1), so a plain list works as the stack.

Complexity
Algorithm	Time	Space
BFS	O(V + E)	O(V)
DFS	O(V + E)	O(V)
