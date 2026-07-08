class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROW = len(heights)
        COL = len(heights[0])
        pacific = set()
        atlantic = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]


        def dfs(r, c, visited, prevHeight):
            if ((r, c) in visited or r < 0 or c < 0 or
            r == ROW or c == COL or heights[r][c] < prevHeight):
                return

            visited.add((r, c))
            for dx, dy in directions:
                nr, nc = r + dx, c + dy
                dfs(nr, nc, visited, heights[r][c])

        for r in range(ROW):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, COL - 1, atlantic, heights[r][COL - 1])
        
        for c in range(COL):
            dfs(0, c, pacific, heights[0][c])
            dfs(ROW - 1, c, atlantic, heights[ROW - 1][c])

        answer = []

        for r in range(ROW):
            for c in range(COL):
                if (r, c) in pacific and (r, c) in atlantic:
                    answer.append([r, c])

        return answer