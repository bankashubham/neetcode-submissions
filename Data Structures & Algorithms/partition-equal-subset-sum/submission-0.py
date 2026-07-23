class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        def dp(i, remainingSum):
            if remainingSum == 0:
                return True

            if remainingSum < 0:
                return False

            if i == len(nums):
                return False

            if (i, remainingSum) in memo:
                return memo[(i, remainingSum)]

            memo[(i, remainingSum)] = dp(i + 1, remainingSum - nums[i]) or dp(i + 1, remainingSum)

            return memo[(i, remainingSum)]

        if sum(nums) % 2 == 1:
            return False

        memo = {}
        target = sum(nums) // 2

        return dp(0, target)