# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(root, maxVal, minVal):
            if not root:
                return True
            
            if not (root.val<maxVal and root.val>minVal):
                return False
            
            left = dfs(root.left, root.val, minVal)
            right = dfs(root.right, maxVal, root.val)

            return left and right
        
        return dfs(root,float("inf"), float("-inf"))


        