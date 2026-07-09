class Solution:
    def rob(self, nums: List[int]) -> int:
        def robRange(left, right):
            robPrev = 0
            skipPrev = 0
            for num in nums[left:right+1]:
                tmp = max((num + robPrev), skipPrev)
                robPrev = skipPrev
                skipPrev = tmp

            return skipPrev

        if len(nums) == 1:
            return nums[0]

        return max(
            robRange(0, len(nums) - 2),
            robRange(1, len(nums) - 1)
        )