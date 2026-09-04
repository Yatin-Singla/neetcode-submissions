class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        def compare(word1, word2):
            n, m, idx = len(word1), len(word2), 0
            while idx < n and idx < m:
                if seq[word1[idx]] < seq[word2[idx]]:
                    return True
                elif seq[word1[idx]] > seq[word2[idx]]:
                    return False
                idx += 1
            
            return n <= m
            

        seq = {}
        for i, ch in enumerate(order):
            seq[ch] = i

        for i in range(1, len(words)):
            if not compare(words[i-1], words[i]):
                return False

        return True

        