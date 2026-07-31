class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        for source, destination in tickets:
            graph[source].append(destination)

        for k, v in graph.items():
            v.sort(reverse = True)

        ans = []

        def dfs(node):
            while graph[node]:
                dfs(graph[node].pop())
            ans.append(node)

        dfs("JFK")
        return ans[::-1]
