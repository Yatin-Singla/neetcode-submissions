# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        def reverseLL(head, idx):
            initialHead = head
            prev, curr = head, head.next
            while idx != right:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
                idx += 1
                
            initialHead.next = curr
            return prev

        dummy = ListNode(next=head)
        prev, curr = dummy, head
        idx = 1
        while idx != left:
            prev = curr
            curr = curr.next
            idx += 1

        newHead = reverseLL(curr, idx)
        prev.next = newHead

        return dummy.next
