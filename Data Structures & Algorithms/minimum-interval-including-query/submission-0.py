class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key=lambda x: x[0])

        sorted_queries = sorted(enumerate(queries), key=lambda x: x[1])

        i = 0
        ans = [-1] * len(queries)
        heap = []

        for index, value in sorted_queries:

            while i < len(intervals) and intervals[i][0] <= value:
                heapq.heappush(heap, (intervals[i][1] - intervals[i][0] + 1, intervals[i][1]))
                i += 1


            while heap and heap[0][1] < value:
                heapq.heappop(heap)

            if heap:
                ans[index] = heap[0][0]

        return ans


