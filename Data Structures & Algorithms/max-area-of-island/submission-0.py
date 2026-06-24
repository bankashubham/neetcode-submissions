class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(row, col):
            area = 1
            grid[row][col] = 0
            for dx, dy in directions:
                nr = row + dx
                nc = col + dy
                if ( 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1):
                    area += dfs(nr, nc)
            return area

        m = len(grid)
        n = len(grid[0])

        directions = [ (0, 1), (0, -1), (1, 0), (-1, 0)]
        ans = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    ans = max(ans, dfs(r, c))

        return ans