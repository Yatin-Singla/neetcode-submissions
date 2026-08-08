import copy
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter, freqMap = [0]*26, [0]*26
        for ch in s1:
            counter[ord(ch) - ord('a')] += 1

        start = 0
        for end in range(len(s2)):
            freqMap[ord(s2[end]) - ord('a')] += 1
            if end - start + 1 == len(s1):
                if counter == freqMap:
                    return True

                freqMap[ord(s2[start]) - ord('a')] -= 1
                start += 1

        return False