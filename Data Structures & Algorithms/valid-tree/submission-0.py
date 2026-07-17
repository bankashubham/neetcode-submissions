class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(node, parent):
            visited.add(node)

            for neighbor in adj[node]:

                if neighbor == parent:
                    continue

                if neighbor in visited:
                    return False

                if not dfs(neighbor, node):
                    return False

            return True

        visited = set()
        if not dfs(0, -1):
            return False
   
        return len(visited) == n