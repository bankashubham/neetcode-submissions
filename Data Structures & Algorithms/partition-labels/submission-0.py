class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        for i, c in enumerate(s):
            last[c] = i

        i = 0
        end = last[s[0]]
        ans = []
        while end < len(s):
            partition = []
            while i < end + 1:
                partition.append(s[i])
                end = max(end, last[s[i]])
                i += 1
            ans.append(len(partition))
            end = last[s[i]] if i < len(s) else len(s)

        return ans
