class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        dp = [[0] * 2 for _ in range(n + 2)]

        for i in range(n - 1, -1, -1):
            # Not holding
            buy = -prices[i] + dp[i + 1][1]
            skip = dp[i + 1][0]
            dp[i][0] = max(buy, skip)

            # Holding
            sell = prices[i] + dp[i + 2][0]
            hold = dp[i + 1][1]
            dp[i][1] = max(sell, hold)

        return dp[0][0]