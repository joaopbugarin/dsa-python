# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list3_head = ListNode() #this will be a dummy node
        list3_tail = list3_head  #saving last node of list3 address
        while list1 and list2:
            if list1.val > list2.val:
                list3_tail.next = list2
                list2 = list2.next
            else:
                list3_tail.next = list1
                list1 = list1.next
            list3_tail = list3_tail.next  #move on to the next node

        list3_tail.next = list1 if list1 else list2 #attach remaining of the longest list

        return list3_head.next #return w/o the dummy node at the beginning