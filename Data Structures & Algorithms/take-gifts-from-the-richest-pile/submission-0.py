import heapq
import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heapq.heapify_max(gifts)
        while k != 0:
            nGifts = heapq.heappop_max(gifts)
            heapq.heappush_max(gifts, math.isqrt(nGifts))
            k -= 1

        return sum(gifts)