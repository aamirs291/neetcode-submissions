# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        good_nodes_count = [0]
        # max_val = [1]

        def good_node(root, max_val):

            if not root:
                return 0
            
            if root.val >= max_val:
                max_val = root.val
                good_nodes_count[0] += 1
            
            good_node(root.left, max_val)
            good_node(root.right, max_val)
        
        good_node(root, root.val)

        return good_nodes_count[0]

        