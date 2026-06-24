class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs(row, col):

            grid[row][col] = "0"

            for dx, dy in directions:

                nr = row + dx
                nc = col + dy

                if (0 <= nr < m and 0 <= nc < n and grid[nr][nc] == "1"):
                    dfs(nr, nc)

        m = len(grid)
        n = len(grid[0])

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        islands = 0

        for r in range(m):
            for c in range(n):

                if grid[r][c] == "1":
                    dfs(r, c)
                    islands += 1

        return islands