# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #idea: BFS returning only the rightmost element of each level
        q = deque([root])
        out = []
        while q:
            lvl_size = len(q)
            lvl = []
            for _ in range(lvl_size):
                curr = q.popleft()
                if curr and curr.val is not None:
                    lvl.append(curr.val)
                if curr and curr.left:
                    q.append(curr.left)
                if curr and curr.right:
                    q.append(curr.right)
            if lvl:
                out.append(lvl[-1])
        return out
