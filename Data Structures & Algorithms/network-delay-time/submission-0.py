class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = defaultdict(list)
        for u, v, w in times:
            adj_list[u].append((v, w))

        dist = [float("inf")] * (n + 1)
        dist[k] = 0

        heap = []
        heapq.heappush(heap, (0, k))

        while heap:
            currDist, node = heapq.heappop(heap)
            if currDist > dist[node]:
                continue
            else:
                for nei, weight in adj_list[node]:
                    newDist = currDist + weight
                    if newDist < dist[nei]:
                        dist[nei] = newDist
                        heapq.heappush(heap, (newDist, nei))
        ans = max(dist[1:])
        return -1 if ans == float("inf") else ans
                