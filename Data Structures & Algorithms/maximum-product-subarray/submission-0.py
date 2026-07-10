class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        previousMax = nums[0]
        previousMin = nums[0]
        result = nums[0]

        for num in nums[1:]:
            newMax = max(num, num * previousMax, num * previousMin)
            newMin = min(num, num * previousMax, num * previousMin)
            previousMax = newMax
            previousMin = newMin
            result = max(result, previousMax)

        return result