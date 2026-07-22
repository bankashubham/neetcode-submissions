class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(r, c, index):
            if index == len(word):
                return True

            if r < 0 or r >= ROWS or c < 0 or c >= COLS:
                return False

            if (r, c) in visited:
                return False

            if board[r][c] != word[index]:
                return False

            visited.add((r, c))
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if backtrack(r + dx, c + dy, index + 1):
                    visited.remove((r, c))
                    return True

            visited.remove((r, c))
            return False

        ROWS = len(board)
        COLS = len(board[0])

        visited = set()
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    if backtrack(r, c, 0):
                        return True

        return False
