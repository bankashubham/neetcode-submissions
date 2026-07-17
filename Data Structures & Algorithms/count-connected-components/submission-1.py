class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        def dfs(node):
            visited.add(node)

            for neighbor in adj[node]:
                if neighbor not in visited:
                    dfs(neighbor)

        visited = set()
        components = 0
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        for node in range(n):
            if node not in visited:
                dfs(node)
                components += 1

        return components