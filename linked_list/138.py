"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
import copy #much needed

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_copy = { None : None }
        curr = head

        while curr:
            old_copy[curr] = Node(curr.val)
            curr = curr.next

        curr = head

        while curr:
            this_node = old_copy[curr]
            this_node.next = old_copy[curr.next]
            this_node.random = old_copy[curr.random]
            curr = curr.next

        return old_copy[head]
