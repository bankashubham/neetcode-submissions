# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorderMap = {}
        
        for i, val in enumerate(inorder):
            inorderMap[val] = i

        def build(preL, preR, inL, inR):
            if preL > preR:
                return None

            rootVal = preorder[preL]
            root = TreeNode(rootVal)

            mid = inorderMap[rootVal]
            leftSize = mid - inL

            root.left = build(
                preL + 1, preL + leftSize,
                inL, mid - 1
                )

            root.right = build(
                preL + leftSize + 1, preR,
                mid + 1, inR
                )

            return root

        return build(0, len(preorder)-1, 0, len(inorder)-1)