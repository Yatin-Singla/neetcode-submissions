from collections import deque
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda item: (item[1], item[2]))
        heap = []
        for i in range(len(trips)):
            # prev stop < new trip start 
            while heap and heap[0][0] <= trips[i][1]:
                capacity += heap[0][1]
                heapq.heappop(heap)
            capacity -= trips[i][0]
            if capacity < 0:
                return False

            heapq.heappush(heap, [trips[i][2], trips[i][0]])

        return True

