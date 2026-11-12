import heapq
import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heapq.heapify_max(gifts)
        for _ in range(k):
            nGifts = heapq.heappop_max(gifts)
            heapq.heappush_max(gifts, math.isqrt(nGifts))

        return sum(gifts)