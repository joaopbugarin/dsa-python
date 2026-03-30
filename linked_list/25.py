class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def make_list(arr):
    dummy = ListNode(0)
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

def print_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print(result)


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Check if we have k nodes left
        count = 0
        curr = head
        #check if we have over k nodes left first
        while curr and count < k:
            curr = curr.next
            count += 1

        if count < k:
            return head #return head if not

        curr = head
        prev = None

        for _ in range(k): #reverse the nodes
            save_next = curr.next
            curr.next = prev
            prev = curr
            curr = save_next

        head.next = self.reverseKGroup(curr, k) #connect last one bit to the following reversed

        return prev

# Test
head = make_list([1, 2, 3, 4, 5])
sol = Solution()
result = sol.reverseKGroup(head, 2)
print_list(result)  # expected: [2, 1, 4, 3, 5]