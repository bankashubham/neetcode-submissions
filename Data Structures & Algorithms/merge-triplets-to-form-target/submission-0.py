class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        matched = [False, False, False]

        for triplet in triplets:
            if triplet[0] <= target[0] and triplet[1] <= target[1] and triplet[2] <= target[2]:
                if triplet[0] == target[0]:
                    matched[0] = True
                if triplet[1] == target[1]:
                    matched[1] = True
                if triplet[2] == target[2]:
                    matched[2] = True

        return all(matched)