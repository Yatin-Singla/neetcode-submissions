from collections import defaultdict
class PrefixTree:
    def __init__(self):
        self.map = {}

    def insert(self, word: str) -> None:
        ptr = self.map
        for ch in word:
            if ch not in ptr: 
                ptr[ch] = {}
            ptr = ptr[ch]
        ptr["*"] = None
        return

    def search(self, word: str) -> bool:
        ptr = self.map
        for ch in word:
            if ch not in ptr:
                return False
            ptr = ptr[ch]
        
        if "*" in ptr:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        ptr = self.map
        for ch in prefix:
            if ch not in ptr:
                return False
            ptr = ptr[ch]

        return True
        
        