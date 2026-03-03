# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #idea: DFS, we go bottom -> checking if it's ever increasing
        if not root:
            return 0

        return self.dfs_with_max(root, root.val)

    def dfs_with_max(self, node, max_seen):
        if not node:
            return 0

        count = 1 if node.val >= max_seen else 0
        max_seen = max(max_seen, node.val)
        left = self.dfs_with_max(node.left, max_seen)
        right = self.dfs_with_max(node.right, max_seen)
        count = count + left + right

        return count