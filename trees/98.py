# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #idea: dfs, ofc
        return self.is_valid_node(root, float('-inf'), float('inf'))
    
    
    def is_valid_node(self, node, min_seen, max_seen):
        if not node:
            return True
        
        if not min_seen < node.val < max_seen:
            return False
        
        return self.is_valid_node(node.left, min_seen, node.val) and self.is_valid_node(node.right, node.val, max_seen)