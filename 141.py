# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from collections import defaultdict
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = defaultdict(int)
        curr = head
        while curr:
            if seen[curr] > 0:
                return True
            seen[curr] += 1
            curr = curr.next
        return False