# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        balance_check = [True]

        def balanceTree(root):
            if not root:
                return 0
            
            left_h = balanceTree(root.left)
            right_h = balanceTree(root.right)

            if abs(left_h - right_h)>1:
                balance_check[0] = False
            
            height = 1 + max(left_h, right_h)

            return height
        
        balanceTree(root)

        return balance_check[0]
        