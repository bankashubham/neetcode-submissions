class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def find(x):
            if parent[x] == x:
                return x
            parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)

            if rootX == rootY:
                return False

            if size[rootX] < size[rootY]:
                parent[rootX] = rootY
                size[rootY] += size[rootX]
            else:
                parent[rootY] = rootX
                size[rootX] += size[rootY]
            return True

        n = len(edges)
        parent = [i for i in range(n + 1)]
        size = [1] * (n + 1)
        for u, v in edges:
            if not union(u, v):
                return [u, v]