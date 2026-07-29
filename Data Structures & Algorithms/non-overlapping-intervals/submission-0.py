class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key = lambda x : x[0])
        ans = 0
        prev_end = intervals[0][1]

        for curr in intervals[1:]:
            if prev_end > curr[0] :
                ans += 1
                prev_end = min(prev_end, curr[1])
            else:
                prev_end = curr[1]
        return ans