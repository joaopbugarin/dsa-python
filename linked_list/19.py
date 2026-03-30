# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        remove_index = -n
        stk = []
        saveHead = head
        curr = head
        while curr:
            stk.append(curr)
            curr = curr.next
        if len(stk) == n:
            return stk[0].next
        if stk and len(stk) > 1 and len(stk)!= n:
            to_remove = stk.pop(remove_index)
            save_next = to_remove.next
            curr = stk.pop(remove_index)
            curr.next = save_next
        elif len(stk) <= 1:
            return None
        return saveHead