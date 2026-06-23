class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        braces = {
            '[': ']',
            '{': '}',
            '(': ')'
        }
        for ch in s:
            if ch in braces:
                stack.append(ch)
            else:
                if stack and (braces[stack[-1]] == ch):
                    stack.pop()
                else:
                    return False
        return len(stack) == 0