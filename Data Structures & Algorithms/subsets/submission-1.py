class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(index, subset):
            if index == len(nums):
                ans.append(subset.copy())
                return

            subset.append(nums[index])
            backtrack(index + 1, subset)
            subset.pop()
            backtrack(index + 1, subset)

        ans = []
        backtrack(0, [])
        return ans