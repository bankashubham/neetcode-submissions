class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(index, remainingTarget):
            if remainingTarget == 0:
                ans.append(subset.copy())
                return

            if remainingTarget < 0:
                return

            for j in range(index, len(candidates)):
                if j > index and candidates[j] == candidates[j - 1]:
                    continue

                if candidates[j] > remainingTarget:
                    break
                    
                subset.append(candidates[j])
                backtrack(j + 1, remainingTarget - candidates[j])
                subset.pop()

        ans = []
        subset = []
        candidates.sort()
        backtrack(0, target)
        return ans