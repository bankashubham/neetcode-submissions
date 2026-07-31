class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        minDist = [float("inf")] * n
        minDist[0] = 0

        visited = set()
        heap = [(0, 0)]          # (cost, node)

        ans = 0

        while len(visited) < n:
            cost, node = heapq.heappop(heap)

            if node in visited:
                continue

            visited.add(node)
            ans += cost

            x1, y1 = points[node]

            for nei in range(n):
                if nei in visited:
                    continue

                x2, y2 = points[nei]
                newCost = abs(x1 - x2) + abs(y1 - y2)

                if newCost < minDist[nei]:
                    minDist[nei] = newCost
                    heapq.heappush(heap, (newCost, nei))

        return ans