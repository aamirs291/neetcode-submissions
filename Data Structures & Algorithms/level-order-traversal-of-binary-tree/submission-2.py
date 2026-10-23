# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        q = deque()

        if root:
            q.append(root)
        
        res = []
        while q:
            curr = []
            size = len(q)

            for i in range(size):
                curr_root = q.popleft()
                curr.append(curr_root.val)

                if curr_root.left:
                    q.append(curr_root.left)

                if curr_root.right:
                    q.append(curr_root.right)
            
            res.append(curr)
        
        return res
                