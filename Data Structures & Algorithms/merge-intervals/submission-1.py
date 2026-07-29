class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals.sort(key=lambda x: x[0])

        result = [intervals[0]]

        for curr in intervals[1:]:
            if result[-1][1] >= curr[0]:
                result[-1][1] = max(result[-1][1], curr[1])
            else:
                result.append(curr)

        return result