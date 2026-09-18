class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = []
        i, m, n = 0, len(word1), len(word2)
        while i < m and i < n:
            output.append(word1[i])
            output.append(word2[i])
            i += 1

        if i < m:
            output.append(word1[i:])
        if i < n:
            output.append(word2[i:])

        return ''.join(output)
