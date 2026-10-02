class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def oneAway(word1, word2) -> bool:
            return len(transformDict[word1] & transformDict[word2]) >= 1

        wordList.append(beginWord)
        wordLookup = defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                wildcard = word[:i] + "*" + word[i+1:]
                wordLookup[wildcard].append(word)
                
        visited = set()
        queue = deque([beginWord])
        transformations = 1

        while queue:
            size = len(queue)
            for _ in range(size):
                word = queue.popleft()
                if word == endWord:
                    return transformations
                for i in range(len(word)):
                    wildcard = word[:i] + "*" + word[i+1:]
                    for neighbor in wordLookup[wildcard]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)

            transformations += 1

        return 0
