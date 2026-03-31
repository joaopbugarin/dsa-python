# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #idea: traverse the tree using DFS-inorder -> gives us the tree in sorted order already
        self.kth = 0
        self.smallest = root.val
        def check_in_order(node):
            if not node:
                return
            check_in_order(node.left)
            self.kth += 1
            if self.kth == k:
                self.smallest = node.val
            check_in_order(node.right)

        check_in_order(root)
        return self.smallest
