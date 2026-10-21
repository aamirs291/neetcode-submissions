# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        diameter = [0]

        def diameterBT(root):
            if not root:
                return 0

            left = diameterBT(root.left)
            right = diameterBT(root.right)

            diameter[0] = max(diameter[0], left + right)

            return 1 + max(left, right)
        
        diameterBT(root)

        return diameter[0]

        