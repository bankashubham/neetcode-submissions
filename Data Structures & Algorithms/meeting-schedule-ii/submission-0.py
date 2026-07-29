"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x.start)
        heap = []
        heapq.heappush(heap, intervals[0].end)

        for interval in intervals[1:]:
            if heap[0] <= interval.start:
                heapq.heappop(heap)
            heapq.heappush(heap, interval.end)

        return len(heap)