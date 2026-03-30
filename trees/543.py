# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
from typing import Optional
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #idea: find the max_depth from left/right in a given node and sum
        #the node with the highest sum value wins
        #we traverse the tree and calculate for every node, updating the max_value
        q = deque()
        q.append(root)
        sum_left = 0
        sum_right = 0
        max_sum = 0
        while q:
            node = q.popleft()
            if node.left:
                q.append(node.left)
                sum_left = self.max_depth(node.left)
            else:
                sum_left = 0
            if node.right:
                q.append(node.right)
                sum_right = self.max_depth(node.right)
            else:
                sum_right = 0
            max_sum = max(max_sum, sum_left + sum_right)
        return max_sum
    
    def max_depth(self, node):
        if not node:
            return 0
        
        left = self.max_depth(node.left)
        right = self.max_depth(node.right)
        return 1 + max(left,right)

test = Solution()

print(test.diameterOfBinaryTree(TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))))

# Test case 1: root = [1,2,3,4,5]
root1 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
print(f"Test case 1 (root = [1,2,3,4,5]): {test.diameterOfBinaryTree(root1)}")

# Test case 2: root = [1,2]
root2 = TreeNode(1, TreeNode(2))
print(f"Test case 2 (root = [1,2]): {test.diameterOfBinaryTree(root2)}")

# Test case 3: root = [3,1,null,null,2]
root3 = TreeNode(3, TreeNode(1, None, TreeNode(2)))
print(f"Test case 3 (root = [3,1,null,null,2]): {test.diameterOfBinaryTree(root3)}")
