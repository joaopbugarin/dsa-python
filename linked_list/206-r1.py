# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        save_head = head
        save_prev = None
        curr = save_head
        while curr:
            save_next = curr.next
            curr.next = save_prev
            save_prev = curr
            curr = save_next
        return save_prev

