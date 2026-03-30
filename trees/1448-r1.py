# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        return self.dfs(root, root.val) #we can pass the root val as max seen here

    
    def dfs(self, node, max_seen):
        if not node:
            return 0
        
        count = 1 if node.val >= max_seen else 0
        max_seen = max(node.val, max_seen)
        left_count, right_count = self.dfs(node.left, max_seen), self.dfs(node.right, max_seen)

        return count + left_count + right_count
