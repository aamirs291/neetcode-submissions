# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def valid_bst_check(root, minVal, maxVal):
            if not root:
                return True
            
            if not (root.val<maxVal and root.val>minVal):
                return False
            
            return valid_bst_check(root.left, minVal, root.val) and valid_bst_check(root.right, root.val, maxVal)
        
        return valid_bst_check(root, float("-inf"), float("inf"))
        