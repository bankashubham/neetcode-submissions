class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1:r]

        n = len(s)
        if len(s) <= 1:
            return s
        res = ""
        curr = ""
        for i in range(n):
            for left, right in [(i, i), (i, i + 1)]:
                curr = expand(left, right)
                if len(curr) > len(res):
                    res = curr
            
        return res

        