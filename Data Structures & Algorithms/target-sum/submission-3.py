from collections import defaultdict
from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        current = {0: 1}

        for num in nums:
            nxt = defaultdict(int)

            for total, ways in current.items():
                nxt[total + num] += ways
                nxt[total - num] += ways

            current = nxt

        return current.get(target, 0)