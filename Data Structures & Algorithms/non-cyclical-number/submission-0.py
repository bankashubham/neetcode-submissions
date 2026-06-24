class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()

        while n not in visited:
            visited.add(n)
            n = self.sumSquare(n)
            if n == 1:
                return True
        return False

    def sumSquare(self, n: int) -> int:
        sum = 0
        while n:
            sum += (n%10) ** 2
            n = n // 10
        return sum