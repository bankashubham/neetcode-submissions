class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1/x
            n = -n

        def power(x, n):

            if n == 0:
                return 1

            half = power(x, n // 2)

            result = half * half
            if n % 2:
                result *= x
            return result

        return power(x, n)