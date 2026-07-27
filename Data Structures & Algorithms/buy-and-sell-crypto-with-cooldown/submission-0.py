class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}

        def dfs(i, holding):
            if i >= len(prices):
                return 0

            if (i, holding) in memo:
                return memo[(i, holding)]

            if holding:
                sell = prices[i] + dfs(i + 2, False)
                hold = dfs(i + 1, True)

                memo[(i, holding)] = max(sell, hold)
            else:
                buy = -prices[i] + dfs(i + 1, True)
                skip = dfs(i + 1, False)

                memo[(i, holding)] = max(buy, skip)

            return memo[(i, holding)]

        return dfs(0, False)