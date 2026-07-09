class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def backtrack(start):
            if start == len(s):
                ans.append(partition.copy())
                return

            for end in range(start, len(s)):
                if not isPalindrome(start, end):
                    continue

                partition.append(s[start:end+1])
                backtrack(end + 1)
                partition.pop()

        def isPalindrome(left, right):
            st = s[left : right + 1]
            return st == st[::-1]

        ans = []
        partition = []
        backtrack(0)
        return ans
