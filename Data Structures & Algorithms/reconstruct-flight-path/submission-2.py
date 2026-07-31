class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        tickets.sort(reverse = True)

        for source, destination in tickets:
            graph[source].append(destination)

        ans = []

        def dfs(node):
            while graph[node]:
                dfs(graph[node].pop())
            ans.append(node)

        dfs("JFK")
        return ans[::-1]
