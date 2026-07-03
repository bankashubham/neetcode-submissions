class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        for i in range(len(nums) - 2):
            if  nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i -1]:
                continue

            l = i + 1
            r = len(nums) - 1
            while l < r:
                currSum = nums[i] + nums[l] + nums[r]
                if currSum > 0:
                    r -= 1
                elif currSum < 0:
                    l += 1
                else:
                    ans.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return ans