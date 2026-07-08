class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROW = len(board)
        COL = len(board[0])
        safe = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(r, c, visited):
            if (r < 0 or c < 0 or r == ROW or c == COL or (r, c) in visited or board[r][c] == "X"):
                return

            visited.add((r, c))
            for dx, dy in directions:
                nr, nc = r + dx, c + dy
                dfs(nr, nc, visited)


        for r in range(ROW):
            if board[r][0] == "O":
                dfs(r, 0, safe)
            if board[r][COL -1] == "O":
                dfs(r, COL -1, safe)

        for c in range(COL):
            if board[0][c] == "O":
                dfs(0, c, safe)
            if board[ROW - 1][c] == "O":
                dfs(ROW - 1, c, safe)

        for r in range(ROW):
            for c in range(COL):
                if (r, c) not in safe and board[r][c] == "O":
                    board[r][c] = "X"