class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        nBoats = 0
        left, right = 0, len(people) - 1

        while left <= right:
            nBoats += 1
            if people[left] + people[right] <= limit:
                left += 1
                right -= 1
            else:
                right -= 1

        return nBoats