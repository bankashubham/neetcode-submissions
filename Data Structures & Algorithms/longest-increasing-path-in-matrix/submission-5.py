import sys
sys.setrecursionlimit(100000)

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        memo = {}
        def dfs(i, j):

            if (i, j) in memo:
                return memo[(i, j)]

            memo[(i, j)] = 1
            directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
            for dx, dy in directions:
                ni, nj = i + dx, j + dy
                if 0 <= ni < rows and 0 <= nj < cols and matrix[ni][nj] > matrix[i][j]:
                    memo[(i, j)] = max(memo[(i, j)], 1 + dfs(ni, nj))

            return memo[(i, j)]

        ans = 0
        for i in range(rows):
            for j in range(cols):
                ans = max(ans, dfs(i, j))

        return ans