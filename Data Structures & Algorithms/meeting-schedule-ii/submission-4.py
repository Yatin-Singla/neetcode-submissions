"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        roomsReq = 0
        rooms, heap = 0, []
        intervals.sort(key=lambda x: x.start)
        for interval in intervals:
            start, end = interval.start, interval.end
            if heap:
                if start < heap[0]:
                    rooms += 1
                else: # start >= heap[0]
                    heapq.heappop(heap)
            else:
                rooms += 1
            roomsReq = max(roomsReq, rooms)
            heapq.heappush(heap, end)

        return roomsReq
            