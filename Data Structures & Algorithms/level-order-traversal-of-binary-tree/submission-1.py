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
            val = []
            size = len(q)

            for i in range(size):
                curr = q.popleft()
                val.append(curr.val)

                if curr.left:
                    q.append(curr.left)
                
                if curr.right:
                    q.append(curr.right)
            
            res.append(val)
        
        return res
            

        