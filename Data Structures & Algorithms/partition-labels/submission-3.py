class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        for i, c in enumerate(s):
            last[c] = i

        start = 0
        end = 0
        ans = []

        for i, c in enumerate(s):
            end = max(end, last[c])

            if i == end:
                ans.append(end - start + 1)
                start = i + 1

        return ans
