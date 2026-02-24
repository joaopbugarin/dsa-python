# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque()
        q.append(root)

        while q:
            node = q.popleft()
            invertNode(node)
            if node and node.left: q.append(node.left)
            if node and node.right: q.append(node.right)

        return root



def invertNode(node):
    if not node:
        return
    save_left = node.left if node.left else None
    save_right = node.right if node.right else None
    node.left = save_right
    node.right = save_left