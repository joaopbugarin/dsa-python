# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque([root])
        lvl = []
        out = []
        while q:
            lvl_len = len(q)
            for _ in range(lvl_len):
                curr = q.popleft()
                if curr:
                    lvl.append(curr.val)
                    if curr.left:
                        q.append(curr.left)
                    if curr.right:
                        q.append(curr.right)
            if lvl:
                out.append(lvl[-1])

        return out