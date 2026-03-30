# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #idea: use the same BFS to loop through both the trees at same time
        #if any difference is noted return False, otherwise return True
        k1 = deque()
        k2 = deque()
        k1.append(p)
        k2.append(q)

        while k1 or k2:
            n1 = k1.popleft() if k1 else None
            n2 = k2.popleft() if k2 else None
            print('n1: ', n1)
            print('n2: ', n2)
            l1, l2 = n1.left if n1 and n1.left else None, n2.left if n2 and n2.left else None
            r1, r2 = n1.right if n1 and n1.right else None, n2.right if n2 and n2.right else None
            if n1 and n2 and n1.val != n2.val:
                return False
            if n1 and not n2:
                return False
            if n2 and not n1:
                return False
            if l1 and not l2:
                return False
            if r1 and not r2:
                return False
            if l1: k1.append(l1)
            if l2: k2.append(l2)
            if r1: k1.append(r1)
            if r2: k2.append(r2)
        
        return True

# Test case: p = [1,2,3], q = [1,2,3]
p = TreeNode(1, TreeNode(2), TreeNode(3))
q = TreeNode(1, TreeNode(2), TreeNode(3))

solution = Solution()
result = solution.isSameTree(p, q)
print(f"Test case - p = [1,2,3], q = [1,2,3]: {result}")
