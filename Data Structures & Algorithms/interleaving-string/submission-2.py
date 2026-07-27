class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)

        if m + n != len(s3):
            return False

        dp = [[False] * (n + 1) for _ in range(m + 1)]

        # Base case
        dp[m][n] = True

        # Initialize last row
        for j in range(n - 1, -1, -1):
            if s2[j] == s3[m + j]:
                dp[m][j] = dp[m][j + 1]
            else:
                dp[m][j] = False

        # Initialize last column
        for i in range(m - 1, -1, -1):
            if s1[i] == s3[i + n]:
                dp[i][n] = dp[i + 1][n]
            else:
                dp[i][n] = False

        # Fill remaining table
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                takeFromS1 = False
                takeFromS2 = False

                if i < m and s1[i] == s3[i + j]:
                    takeFromS1 = dp[i + 1][j]

                if j < n and s2[j] == s3[i + j]:
                    takeFromS2 = dp[i][j + 1]

                dp[i][j] = takeFromS1 or takeFromS2

        return dp[0][0]