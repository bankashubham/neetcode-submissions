class Solution:
    def countSubstrings(self, s: str) -> int:
        def expand(l, r):
            cnt = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                cnt += 1
                l -= 1
                r += 1
            return cnt

        n = len(s)
        if len(s) <= 1:
            return len(s)
        count = 0
        for i in range(n):
            for left, right in [(i, i), (i, i + 1)]:
                count += expand(left, right)   
        return count