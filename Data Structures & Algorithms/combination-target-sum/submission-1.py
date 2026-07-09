class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def backtrack(index, remainingTarget):
            if remainingTarget == 0:
                ans.append(subset.copy())
                return

            if remainingTarget < 0:
                return

            for j in range(index, len(nums)):
                subset.append(nums[j])
                backtrack(j, remainingTarget - nums[j])
                subset.pop()

        ans = []
        subset = []
        backtrack(0, target)
        return ans