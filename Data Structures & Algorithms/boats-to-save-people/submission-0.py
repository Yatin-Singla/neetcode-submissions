class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        nBoats = 0
        people.sort()
        left, right = 0, len(people) - 1

        while left < right:
            if people[right] < 0:
                right -= 1
                continue
            if people[left] < 0:
                left += 1
                continue
            if people[left] + people[right] <= limit:
                nBoats += 1
                people[left], people[right] = -people[left], -people[right] 
            else:
                right -= 1


        for i in range(len(people)):
            if people[i] > 0:
                nBoats += 1
        return nBoats