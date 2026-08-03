from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def timeTaken(k):
            time = 0
            for nanaCount in piles:
                time += ceil(nanaCount / k)
            return time

        piles.sort()
        eatSpeed, low, high = 1, 1, max(piles)
        while low <= high:
            rate = (low + high) >> 1
            time = timeTaken(rate)
            if time <= h:
                eatSpeed = rate
                high = rate - 1
            else: # time > h
                low = rate + 1

        return eatSpeed