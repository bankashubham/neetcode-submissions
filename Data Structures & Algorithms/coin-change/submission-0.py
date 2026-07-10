class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dp(remainingAmount):
            if remainingAmount == 0:
                return 0

            if remainingAmount < 0:
                return float("inf")

            if remainingAmount in memo:
                return memo[remainingAmount]

            ans = float("inf")

            for coin in coins:
                ans = min(ans, 1 + dp(remainingAmount - coin))

            memo[remainingAmount] = ans
            return memo[remainingAmount]

        result = dp(amount)
        return -1 if result == float("inf") else result