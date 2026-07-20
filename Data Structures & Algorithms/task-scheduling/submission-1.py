class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [(-v, k) for k, v in count.items()]
        heapq.heapify(maxHeap)

        time = 0
        queue = deque()
        while maxHeap or queue:
            while queue:
                if queue[0][2] == time:
                    task, remainingCount, nextTime = queue.popleft()
                    heapq.heappush(maxHeap, (-remainingCount, task))
                else:
                    break
            if maxHeap:
                freq, task = heapq.heappop(maxHeap)
                remainingCount = -freq - 1
                if remainingCount:
                    queue.append((task, remainingCount, time + n + 1))
            time += 1

        return time
