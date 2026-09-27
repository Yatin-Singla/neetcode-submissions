class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        output = []
        for key, val in counter.items():
            if val > len(nums) // 3:
                output.append(key)

        return output