class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        m = len(nums)

        dp = [[0] * m for _ in range(m)]

        for length in range(2, m):
            for left in range(m - length):
                right = left + length

                for k in range(left + 1, right):
                    dp[left][right] = max(
                        dp[left][right],
                        dp[left][k]
                        + nums[left] * nums[k] * nums[right]
                        + dp[k][right]
                    )

        return dp[0][m - 1]