# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def checkLength(self, head, k):
        if not head or k <= 0:
            return None, False

        while head and k > 0:
            head = head.next
            k -= 1
        
        return head, k == 0

    def reverse(self, head, k):
        prev, curr = head, head.next

        while k > 1:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
            k -= 1

        return prev, head

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = curr = ListNode(next = head)
        while True:
            newHead, hasK = self.checkLength(curr.next, k)
            if hasK:
                revHead, revTail = self.reverse(curr.next, k)
                curr.next = revHead
                revTail.next = newHead
                curr = revTail
            else:
                break

        return dummy.next
            