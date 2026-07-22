class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []

        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(curr, index):
            if index == len(digits):
                result.append("".join(curr))
                return

            for ch in phone[digits[index]]:
                curr.append(ch)
                backtrack(curr, index + 1)
                curr.pop()

        result = []
        backtrack([], 0)
        return result