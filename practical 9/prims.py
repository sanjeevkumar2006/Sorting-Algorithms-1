import heapq

def prims_algorithm(graph, start=0):
    """
    graph: adjacency list -> {node: [(neighbor, weight), ...]}
    Returns the MST edges and total weight.
    """
    visited = set()
    mst_edges = []
    total_weight = 0

    # (weight, current_node, parent_node)
    min_heap = [(0, start, None)]

    while min_heap and len(visited) < len(graph):
        weight, node, parent = heapq.heappop(min_heap)

        if node in visited:
            continue

        visited.add(node)
        total_weight += weight

        if parent is not None:
            mst_edges.append((parent, node, weight))

        for neighbor, w in graph[node]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (w, neighbor, node))

    return mst_edges, total_weight


# Example usage
if __name__ == "__main__":
    graph = {
        0: [(1, 2), (3, 6)],
        1: [(0, 2), (2, 3), (3, 8), (4, 5)],
        2: [(1, 3), (4, 7)],
        3: [(0, 6), (1, 8), (4, 9)],
        4: [(1, 5), (2, 7), (3, 9)],
    }

    edges, total = prims_algorithm(graph)

    print("Edges in the MST:")
    for u, v, w in edges:
        print(f"{u} -- {v}  (weight {w})")
    print("Total weight:", total)