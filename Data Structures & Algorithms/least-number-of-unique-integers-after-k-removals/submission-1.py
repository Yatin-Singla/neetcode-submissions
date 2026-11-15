from collections import Counter

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter = Counter(arr)
        frequencies = sorted([freq for freq in counter.values()])
        unique = len(frequencies)

        for freq in frequencies:
            if freq > k:
                break
            k -= freq
            unique -= 1

        return unique
