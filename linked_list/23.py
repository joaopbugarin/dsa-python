# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#idea: use the merge 2 lists several times
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1: #we will reduce until it becomes just one

            curr = []

            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i+1] if i+1 < len(lists) else None
                curr.append(self.mergeTwoLists(list1,list2))
            lists = curr

        return lists[0]

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new_list = ListNode()
        curr = new_list
        while list1 or list2:
            val1 = list1.val if list1 else float('inf')
            val2 = list2.val if list2 else float('inf')
            if val1 <= val2:
                curr.next = ListNode(val1)
                list1 = list1.next if list1 else None
            else:
                curr.next = ListNode(val2)
                list2 = list2.next if list2 else None

            curr = curr.next

        return new_list.next