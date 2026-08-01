# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        quotient = 0
        l1Head = ListNode(next = l1)
        tail = l1Head
        while l1 and l2:
            add = l1.val + l2.val + quotient
            l1.val = add % 10
            quotient = add // 10

            l1 = l1.next
            l2 = l2.next
            tail = tail.next

        remaining = l1 or l2 

        while remaining:
            add = remaining.val + quotient
            remaining.val = add % 10
            quotient = add // 10

            tail.next = remaining
            remaining = remaining.next
            tail = tail.next


        if quotient:
            tail.next = ListNode(val=quotient)

        return l1Head.next