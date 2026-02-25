# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #working from bottom up, using post order to count the depth
        if not root:
            return True
   
        left = self.max_depth(root.left)
        right = self.max_depth(root.right)
        
        return (abs(left - right) <= 1 
            and self.isBalanced(root.left) 
            and self.isBalanced(root.right))
    
    def max_depth(self, node):
        if not node:
            return 0

        left = self.max_depth(node.left)
        right = self.max_depth(node.right)
        return 1 + max(left,right)
        