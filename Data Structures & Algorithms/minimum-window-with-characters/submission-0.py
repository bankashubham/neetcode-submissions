from collections import Counter, defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        window = defaultdict(int)
        formed = 0
        left = 0
        required = len(need)
        min_len = float("inf")
        start = 0

        for right in range(len(s)):
            ch = s[right]
            window[ch] += 1

            if ch in need and window[ch] == need[ch]:
                formed += 1

            while formed == required:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    start = left

                left_char = s[left]
                window[left_char] -= 1

                if left_char in need and window[left_char] < need[left_char]:
                    formed -= 1

                left += 1

        if min_len == float("inf"):
            return ""

        return s[start: start + min_len]