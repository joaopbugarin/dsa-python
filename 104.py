# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #idea: implement DFS and update max value found

        self.max_depth = 0
        self.pre_order(root, 1)

        return self.max_depth


    def pre_order(self, node, depth):
        if not node:
            return

        self.max_depth = max(self.max_depth, depth)
        print(self.max_depth)
        self.pre_order(node.left, depth + 1)
        self.pre_order(node.right, depth + 1)