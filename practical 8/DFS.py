def dfs(graph, start):
    """
    graph: adjacency list -> {node: [neighbor, ...]}
    start: node to begin traversal from
    Returns the list of nodes in DFS order.
    """
    visited = set()
    stack = [start]
    order = []

    while stack:
        node = stack.pop()          # O(1) removal from the back (LIFO)

        if node in visited:
            continue

        visited.add(node)
        order.append(node)

        # push in reverse so neighbors are visited in their listed order
        for neighbor in reversed(graph[node]):
            if neighbor not in visited:
                stack.append(neighbor)

    return order


def dfs_recursive(graph, node, visited=None, order=None):
    """Recursive version of DFS (uses the call stack instead of pop())."""
    if visited is None:
        visited, order = set(), []

    visited.add(node)
    order.append(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited, order)

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

    print("DFS traversal (iterative) from node 0:")
    print(dfs(graph, 0))

    print("DFS traversal (recursive) from node 0:")
    print(dfs_recursive(graph, 0))