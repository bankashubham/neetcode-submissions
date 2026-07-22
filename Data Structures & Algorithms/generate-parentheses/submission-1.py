class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(curr, openCount, closeCount):
            if len(curr) == 2 * n:
                result.append("".join(curr))
                return

            if openCount < n:
                curr.append("(")
                backtrack(curr, openCount + 1, closeCount)
                curr.pop()

            if closeCount < openCount:
                curr.append(")")
                backtrack(curr, openCount, closeCount + 1)
                curr.pop()

        curr = []
        result = []
        backtrack(curr, 0, 0)
        return result