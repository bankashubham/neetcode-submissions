class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        n = len(nums)

        if total % 2 == 1:
            return False

        target = total // 2
        dp = [[False] * (target + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = True

        for i in range(len(nums) - 1, -1, -1):
            for r in range(1, target + 1):
                if nums[i] > r:
                    dp[i][r] = dp[i + 1][r]
                else:
                    dp[i][r] = dp[i + 1][r] or dp[i + 1][r - nums[i]]
        
        return dp[0][target]