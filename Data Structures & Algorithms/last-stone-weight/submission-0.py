class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-stone for stone in stones]
        heapq.heapify(maxHeap)

        while maxHeap:
            if len(maxHeap) == 1:
                return -(maxHeap[0])
            stoneA = -(heapq.heappop(maxHeap))
            stoneB = -(heapq.heappop(maxHeap))

            if stoneA > stoneB:
                heapq.heappush(maxHeap, -(stoneA - stoneB))
            elif stoneB > stoneA:
                heapq.heappush(maxHeap, -(stoneB - stoneA))

        return 0