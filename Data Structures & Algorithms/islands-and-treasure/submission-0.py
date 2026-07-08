from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROW = len(grid)
        COL = len(grid[0])
        queue = deque()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        INF = 2147483647

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 0:
                    queue.append((r, c))
                    
        while queue:
            r, c = queue.popleft()
            for dx, dy in directions:
                nr, nc = r + dx, c + dy

                if (0 <= nr < ROW) and (0 <= nc < COL) and grid[nr][nc] == INF:
                    grid[nr][nc] = grid[r][c] + 1

                    queue.append((nr, nc))