from collections import deque


def bfs(graph, start):
    """
    graph: adjacency list -> {node: [neighbor, ...]}
    start: node to begin traversal from
    Returns the list of nodes in BFS order.
    """
    visited = set([start])
    queue = deque([start])
    order = []

    while queue:
        node = queue.popleft()      # O(1) removal from the front (FIFO)
        order.append(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return order


# Example usage
if __name__ == "__main__":
    graph = {
        0: [1, 2],
        1: [0, 3, 4],
        2: [0, 5],
        3: [1],
        4: [1],
        5: [2],
    }

    print("BFS traversal starting from node 0:")
    print(bfs(graph, 0))