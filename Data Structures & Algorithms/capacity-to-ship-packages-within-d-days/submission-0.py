class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canShip(capacity):
            ships, currCap = 1, capacity
            for weight in weights:
                if currCap - weight < 0:
                    currCap = capacity
                    ships += 1
                    if ships > days:
                        return False
                currCap -= weight

            return True
        
        left, right = max(weights), sum(weights)
        while left < right:
            mid = (left + right) >> 1
            if canShip(mid):
                right = mid
            else:
                left = mid + 1

        return left