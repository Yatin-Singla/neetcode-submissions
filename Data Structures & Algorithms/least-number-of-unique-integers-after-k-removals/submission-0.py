from collections import Counter
import heapq
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter = Counter(arr)
        heap = [(freq, key) for key, freq in counter.items()]
        heapq.heapify(heap)

        while k > 0 and heap:
            freq, key = heapq.heappop(heap)
            if freq - 1 > 0:
                heapq.heappush(heap, (freq - 1, key))
            k -= 1

        return len(heap)
