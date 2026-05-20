"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        seen = {}


        def dfs(root):
            if not root:
                return

            if root in seen:
                return seen[root]

            curr = Node(root.val, None) # start the deep copy of the current node w/ the value
            seen[root] = curr

            if root.neighbors:
                for n in root.neighbors:
                    curr.neighbors.append(dfs(n))
            else:
                curr.neighbors = []

            return curr #return root deep copy ref


        return dfs(node)