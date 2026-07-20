class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [(-v, k) for k, v in count.items()]
        heapq.heapify(maxHeap)

        time = 0
        queue = deque()
        while maxHeap or queue:
            if maxHeap:
                freq, task = heapq.heappop(maxHeap)
                remainingFreq = -freq - 1
                if remainingFreq:
                    queue.append((task, remainingFreq, time + n + 1))
            time += 1

            if queue:
                obj = queue[0]
                if obj[2] == time:
                    task, remainingFreq, nextTime = queue.popleft()
                    heapq.heappush(maxHeap, (-remainingFreq, task))

        return time
        