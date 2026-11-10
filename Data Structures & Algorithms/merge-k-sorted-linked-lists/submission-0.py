# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = curr = ListNode()
        heap = []
        for i, node in enumerate(lists):
            if node:
                heap.append((node.val, i, node))
        heapq.heapify(heap)
        while heap:
            _, i, node = heapq.heappop(heap)
            curr.next = node
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

            curr = curr.next

        return dummy.next