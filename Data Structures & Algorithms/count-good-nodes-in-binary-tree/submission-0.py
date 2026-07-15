# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.counts = 0

        def dfs(node, maxSoFar):
            if not node:
                return

            if node.val >= maxSoFar:
                self.counts += 1

            newMax = max(maxSoFar, node.val)

            dfs(node.left, newMax)
            dfs(node.right, newMax)

            return self.counts

        return dfs(root, float("-inf"))