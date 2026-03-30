# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        return self.node_height(root) > -1



    def node_height(self, node):
        if not node:
            return 0

        left = self.node_height(node.left)
        right = self.node_height(node.right)

        if abs(left - right) > 1 or left == -1 or right == -1:
            return -1

        return max(left, right) + 1
