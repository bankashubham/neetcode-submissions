class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        visited = set()
        heap = [(grid[0][0], 0, 0)]

        while heap:
            currTime, r, c = heapq.heappop(heap)

            if (r, c) in visited:
                continue

            visited.add((r, c))

            if r == (len(grid) - 1) and c == (len(grid[0]) - 1):
                return currTime
            
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

            for dx, dy in directions:
                nr, nc = r + dx, c + dy
                if (nr, nc) not in visited and 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                    newTime = max(currTime, grid[nr][nc])
                    heapq.heappush(heap, (newTime, nr, nc))