class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        heap = [(0, 0)]   # (cost_to_connect, node)
        visited = set()
        ans = 0

        while heap:
            cost, node = heapq.heappop(heap)

            if node in visited:
                continue

            visited.add(node)
            ans += cost

            for i, point in enumerate(points):
                if i not in visited:
                    cost = abs(points[node][0] - point[0]) + abs(points[node][1] - point[1])
                    heapq.heappush(heap, (cost, i))

        return ans