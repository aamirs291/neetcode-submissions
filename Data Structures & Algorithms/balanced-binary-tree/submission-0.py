# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        is_balanced = [True]

        def dfs(root):
            if not root:
                return 0

            lst = dfs(root.left)
            rst = dfs(root.right)

            if abs(lst-rst)>1:
                is_balanced[0] = False
            
            return 1 + max(lst, rst)
        
        dfs(root)

        return is_balanced[0]
        
        
