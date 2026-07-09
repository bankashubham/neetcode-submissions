class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(index, subset):
            ans.append(subset.copy())

            for j in range(index, len(nums)):
                if j > index and nums[j] == nums[j - 1]:
                    continue
                subset.append(nums[j])
                backtrack(j + 1, subset)
                subset.pop()

        ans = []
        nums.sort()
        backtrack(0, [])
        return ans