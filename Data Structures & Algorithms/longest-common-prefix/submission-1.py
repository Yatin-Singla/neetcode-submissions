class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie = {}
        def insert(word):
            path = trie
            for ch in word:
                if ch not in path:
                    path[ch] = {}
                path = path[ch]

            path["*"] = None
            return

        for word in strs:
            insert(word)

        LCP = []
        path = trie
        while path:
            keys = list(path.keys())
            if len(keys) > 1:
                break
            if keys[0] == "*":
                break
            LCP.append(keys[0])
            path = path[keys[0]]
            
        return ''.join(LCP) if LCP else ""