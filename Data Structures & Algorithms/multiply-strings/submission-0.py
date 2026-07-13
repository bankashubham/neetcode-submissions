class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        m, n = len(num1), len(num2)
        res = [0] * (m + n)

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):

                product = int(num1[i]) * int(num2[j])

                p1 = i + j
                p2 = i + j + 1

                total = product + res[p2]

                res[p2] = total % 10
                res[p1] += total // 10

        i = 0
        while i < len(res) - 1 and res[i] == 0:
            i += 1

        return "".join(map(str, res[i:]))