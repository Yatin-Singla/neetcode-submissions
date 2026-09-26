from collections import deque
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda item: (item[1], item[2]))
        heap = []
        for nPass, pickup, drop in trips:
            # prev stop < new trip start 
            while heap and heap[0][0] <= pickup:
                _ ,nDropped = heapq.heappop(heap)
                capacity += nDropped
                
            capacity -= nPass
            if capacity < 0:
                return False

            heapq.heappush(heap, [drop, nPass])

        return True

