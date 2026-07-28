from functools import cache
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        @cache
        def dfs(left, right):
            if right - left == 1:
                return 0

            best = 0
            for k in range(left + 1, right):
                best = max(
                    best,
                    dfs(left, k)
                    + nums[left] * nums[k] * nums[right]
                    + dfs(k, right)
                )
            return best

        nums = [1] + nums + [1]
        return dfs(0, len(nums) - 1)