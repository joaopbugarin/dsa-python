# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        curr = head
        stk = []
        while curr:
            stk.append(curr)
            curr = curr.next

        curr = head

        while curr != stk[-1] and curr.next != stk[-1]:
            last = stk.pop()

            save_curr_next = curr.next
            curr.next = last
            last.next = save_curr_next

            curr = save_curr_next
        stk[-1].next = None