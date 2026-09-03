class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        state = {}
        maxLength = maxFreq = start = 0
        for end in range(len(s)):
            state[s[end]] = state.get(s[end], 0) + 1
            maxFreq = max(maxFreq, state[s[end]])
            if k + maxFreq < end - start + 1:
                state[s[start]] -= 1
                start += 1
            
            maxLength = max(maxLength, end - start + 1)
        
        return maxLength