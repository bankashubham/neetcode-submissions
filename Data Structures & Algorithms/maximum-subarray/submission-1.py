class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currMax = globalMax = nums[0]

        for num in nums[1:]:
            currMax = max(num, currMax + num)
            globalMax = max(globalMax, currMax)

        return globalMax