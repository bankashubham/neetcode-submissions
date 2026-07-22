class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def backtrack(row):
            if row == n:
                ans.append(["".join(r) for r in board])
                return

            for col in range(n):
                diag = row - col
                anti = row + col

                if col in cols or diag in diag1 or anti in diag2:
                    continue

                board[row][col] = "Q"
                cols.add(col)
                diag1.add(diag)
                diag2.add(anti)

                backtrack(row + 1)

                board[row][col] = "."
                cols.remove(col)
                diag1.remove(diag)
                diag2.remove(anti)

        ans = []
        cols = set()
        diag1 = set()
        diag2 = set()
        board = [["."] * n for _ in range(n)]
        backtrack(0)

        return ans
