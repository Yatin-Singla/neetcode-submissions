class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)
        heap = [(-val, key) for key, val in counter.items()]
        heapq.heapify(heap)
        _, key = heapq.heappop(heap)
        return key