"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        cloneMap = {}

        def dfs(node):
            if not node:
                return node

            if node in cloneMap:
                return cloneMap[node]
            
            cloned_node = Node(node.val)
            cloneMap[node] = cloned_node

            for neighbor in node.neighbors:
                cloned_node.neighbors.append(dfs(neighbor))# the dfs call is being done to create clones and update the mappings. 

            return cloned_node
        
        return dfs(node) if node else None


