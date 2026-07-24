class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0] * (amount + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = 1

        for i in range(n - 1, -1, -1):
            for r in range(1, amount + 1):
                if coins[i] <= r:
                    dp[i][r] = dp[i][r - coins[i]] + dp[i + 1][r]
                else:
                    dp[i][r] = dp[i + 1][r]

        return dp[0][amount]

