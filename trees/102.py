# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = deque([root])
        print('q: ', q)
        while q:
            level_size = len(q)
            level = []
            for _ in range(level_size):
                curr = q.popleft()
                if curr:
                    level.append(curr.val)
                if curr and curr.left: q.append(curr.left)
                if curr and curr.right: q.append(curr.right)
            if level:
                res.append(level)
        return res