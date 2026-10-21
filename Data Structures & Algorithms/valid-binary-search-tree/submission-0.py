# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(node, maxVal, minVal):
            if not node:
                return True
            
            if node.val >=maxVal or node.val<=minVal:
                return False
            
            left = dfs(node.left, node.val, minVal)
            right = dfs(node.right, maxVal, node.val)

            return left and right
        
        return dfs(root, float("inf"), float("-inf"))
        