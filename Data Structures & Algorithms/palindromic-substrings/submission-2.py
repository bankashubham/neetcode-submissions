class Solution:
    def countSubstrings(self, s: str) -> int:
        def expand(l, r):
            cnt = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                cnt += 1
                l -= 1
                r += 1
            return cnt

        count = 0
        for i in range(len(s)):
            for left, right in [(i, i), (i, i + 1)]:
                count += expand(left, right)   
        return count