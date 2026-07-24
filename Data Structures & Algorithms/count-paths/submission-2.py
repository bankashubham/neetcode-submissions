class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        nextRow = [0] * (n + 1)
        nextRow[n - 1] = 1

        for row in range(m - 1, -1, -1):
            currRow = [0] * (n + 1)
            for col in range(n - 1, -1, -1):
                currRow[col] = nextRow[col] + currRow[col + 1]
            nextRow = currRow

        return nextRow[0]