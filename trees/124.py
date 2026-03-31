# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')
        def dfs(node): #lets use postorder dfs (we need both children values before moving up)
            if not node:
                return 0

            sum_left = max(dfs(node.left), 0)
            sum_right = max(dfs(node.right), 0)

            curr_sum = sum_left + node.val + sum_right
            self.max_sum = max(curr_sum, self.max_sum)

            return max(node.val + sum_left, node.val + sum_right)

        dfs(root)
        return self.max_sum
