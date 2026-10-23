# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        max_dia = [0]

        def diam(root):

            if not root:
                return 0
            
            left_dia = diam(root.left)
            right_dia = diam(root.right)

            max_dia[0] = max(max_dia[0], left_dia + right_dia)

            height = 1 + max(left_dia, right_dia)

            return height
        
        diam(root)

        return max_dia[0]


        