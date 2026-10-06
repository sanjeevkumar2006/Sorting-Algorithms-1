class DisjointSet:
    def __init__(self, vertices):
        self.parent = list(range(vertices))
        self.rank = [0] * vertices

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a == root_b:
            return False

        if self.rank[root_a] < self.rank[root_b]:
            self.parent[root_a] = root_b
        elif self.rank[root_a] > self.rank[root_b]:
            self.parent[root_b] = root_a
        else:
            self.parent[root_b] = root_a
            self.rank[root_a] += 1

        return True


def kruskal_mst(vertices, edges):
    ds = DisjointSet(vertices)
    mst = []
    total_weight = 0

    for u, v, w in sorted(edges, key=lambda edge: edge[2]):
        if ds.union(u, v):
            mst.append((u, v, w))
            total_weight += w

            if len(mst) == vertices - 1:
                break

    return mst, total_weight


if __name__ == "__main__":
    vertices = 5
    edges = [
        (0, 1, 2), (0, 3, 6),
        (1, 2, 3), (1, 3, 8), (1, 4, 5),
        (2, 4, 7), (3, 4, 9)
    ]

    mst, total_weight = kruskal_mst(vertices, edges)

    print("Edges in the MST:")
    for u, v, w in mst:
        print(f"{u} -- {v}  (weight {w})")
    print("Total weight:", total_weight)