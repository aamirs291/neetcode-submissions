# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        res = [0]
        n = [0]

        def dfs(root):
            if not root:
                return 0
            
            dfs(root.left)

            n[0]+=1
            if n[0]==k:
                res[0]= root.val
            
            dfs(root.right)

            return res[0]
        
        return dfs(root)
        