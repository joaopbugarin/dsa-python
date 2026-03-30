# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self. max_diameter = 0

        def node_diameter(node):
            if not node:
                return 0
            size_left = node_diameter(node.left) #left height
            size_right = node_diameter(node.right) #right height
            self.max_diameter = max(self.max_diameter, size_left +size_right) #update max_diameter for the current node
            return max(size_left, size_right) + 1 #return biggest height of current node + 1

        node_diameter(root)

        return self.max_diameter


