class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr_l1 = l1
        curr_l2 = l2
        curr_sum = ListNode(0)
        has_carry_over = 0
        save_head = curr_sum

        while curr_l1 or curr_l2 or has_carry_over > 0:
            val_l1 = curr_l1.val if curr_l1 else 0
            val_l2 = curr_l2.val if curr_l2 else 0

            curr_sum.val = (val_l1 + val_l2 + has_carry_over) % 10
            has_carry_over = (val_l1 + val_l2 + has_carry_over) // 10

            if curr_l1:
                curr_l1 = curr_l1.next
            if curr_l2:
                curr_l2 = curr_l2.next

            if curr_l1 or curr_l2 or has_carry_over:
                curr_sum.next = ListNode(0)
                curr_sum = curr_sum.next

        return save_head