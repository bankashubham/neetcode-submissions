class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(current, used):
            if len(current) == len(nums):
                ans.append(current.copy())
                return

            for j in range(len(nums)):
                if used[j]:
                    continue
                current.append(nums[j])
                used[j] = True
                backtrack(current, used)
                current.pop()
                used[j] = False

        current = []
        used = [False] * len(nums)
        ans = []
        backtrack(current, used)
        return ans