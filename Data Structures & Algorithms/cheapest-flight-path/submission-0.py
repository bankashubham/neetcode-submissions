class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))

        dist = [[float("inf")] * (k + 2) for _ in range(n)]
        dist[src][0] = 0

        heap = [(0, src, 0)]

        while heap:

            cost, node, stops = heapq.heappop(heap)

            if cost > dist[node][stops] or stops > k + 1:
                continue

            if node == dst:
                return cost

            for nei, price in graph[node]:

                newCost = cost + price
                newStops = stops + 1

                if newStops <= k + 1 and newCost < dist[nei][newStops]:
                    dist[nei][newStops] = newCost
                    heapq.heappush(heap, (newCost, nei, newStops))

        return -1