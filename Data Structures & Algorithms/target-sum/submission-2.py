class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        S = sum(nums)

        # Optional optimization
        if abs(target) > S:
            return 0

        dp = [[0] * (2 * S + 1) for _ in range(n + 1)]

        # Base case
        dp[n][target + S] = 1

        for i in range(n - 1, -1, -1):
            for total in range(-S, S + 1):

                plus = 0
                minus = 0

                if total + nums[i] <= S:
                    plus = dp[i + 1][total + S + nums[i]]

                if total - nums[i] >= -S:
                    minus = dp[i + 1][total + S - nums[i]]

                dp[i][total + S] = plus + minus

        return dp[0][S]