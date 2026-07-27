class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}

        def dfs(i, holding):
            if i >= len(prices):
                return 0

            if (i, holding) in memo:
                return memo[(i, holding)]

            if holding:
                ans = max(
                    prices[i] + dfs(i + 2, False),
                    dfs(i + 1, True)
                )
            else:
                ans = max(
                    -prices[i] + dfs(i + 1, True),
                    dfs(i + 1, False)
                )

            memo[(i, holding)] = ans
            return ans

        return dfs(0, False)