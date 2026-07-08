class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        queue = deque()
        fresh = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        time = 0

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
                    
        while queue and fresh:
            size = len(queue)
            for _ in range(size):
                r, c = queue.popleft()
                for dx, dy in directions:
                    nr, nc = r + dx, c + dy

                    if (0 <= nr < ROW) and (0 <= nc < COL) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        queue.append((nr, nc))
            time += 1

        return time if not fresh else -1