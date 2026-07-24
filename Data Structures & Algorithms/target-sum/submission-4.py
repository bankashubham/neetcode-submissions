class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        S = sum(nums)

        if abs(target) > S or (S + target) % 2 != 0:
            return 0

        target = (S + target) // 2

        dp = [0] * (target + 1)
        dp[0] = 1

        for num in nums:
            for s in range(target, num - 1, -1):
                dp[s] += dp[s - num]

        return dp[target]