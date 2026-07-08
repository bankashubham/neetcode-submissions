class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROW = len(board)
        COL = len(board[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(r, c):
            if (r < 0 or c < 0 or r == ROW or c == COL or board[r][c] == "T" or board[r][c] == "X"):
                return

            board[r][c] = "T"
            for dx, dy in directions:
                nr, nc = r + dx, c + dy
                dfs(nr, nc)


        for r in range(ROW):
            if board[r][0] == "O":
                dfs(r, 0)
            if board[r][COL -1] == "O":
                dfs(r, COL -1)

        for c in range(COL):
            if board[0][c] == "O":
                dfs(0, c)
            if board[ROW - 1][c] == "O":
                dfs(ROW - 1, c)

        for r in range(ROW):
            for c in range(COL):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "T":
                    board[r][c] = "O"