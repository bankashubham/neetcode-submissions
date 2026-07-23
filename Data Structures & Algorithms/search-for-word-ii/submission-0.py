class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def __init__(self):
        self.root = TrieNode()

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        for word in words:
            curr = self.root
            for c in word:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
            curr.word = word

        ROWS = len(board)
        COLS = len(board[0])
        result = []

        def dfs(r, c, node):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS:
                return

            if board[r][c] == "#":
                return

            char = board[r][c]
            if char not in node.children:
                return

            node = node.children[char]

            if node.word:
                result.append(node.word)
                node.word = None

            temp = board[r][c]
            board[r][c] = "#"

            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            for dx, dy in directions:
                dfs(r + dx, c + dy, node)
            
            board[r][c] = temp

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, self.root)
            
        return result
