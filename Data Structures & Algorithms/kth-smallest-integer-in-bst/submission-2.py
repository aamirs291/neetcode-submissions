# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        incr = [0]
        res = [root.val]

        def smallest_k(root):

            if not root:
                incr[0] += 1
                return
            
            smallest_k(root.left)

            if incr[0]==k:
                res[0] = root.val
                
            smallest_k(root.right)
        
        smallest_k(root)

        return res[0]
