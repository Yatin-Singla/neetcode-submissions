class WordDictionary:
    def __init__(self):
        self.tree = {}

    def addWord(self, word: str) -> None:
        path = self.tree
        for ch in word:
            if ch not in path:
                path[ch] = {}
            path = path[ch]
        path["*"] = {}

    def search(self, word: str) -> bool:
        n = len(word)
        def dfs(path, idx):
            if idx == n:
                return "*" in path
            
            if word[idx] == ".":
                for ch in path.keys():
                    if dfs(path[ch], idx + 1):
                        return True
            elif word[idx] in path:
                return dfs(path[word[idx]], idx + 1)

            return False
        return dfs(self.tree, 0)
        
