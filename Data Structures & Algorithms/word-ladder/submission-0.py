class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def oneAway(word1, word2) -> bool:
            transformed = False
            idx, n = 0, len(word1)
            while idx < n:
                if word1[idx] != word2[idx]:
                    if transformed:
                        return False
                    else:
                        transformed = True
                idx += 1
            return True

        wordList.append(beginWord)
        graph = defaultdict(list)
        for i in range(len(wordList)):
            for j in range(i+1, len(wordList)):
                if oneAway(wordList[i], wordList[j]):
                    graph[wordList[i]].append(wordList[j])
                    graph[wordList[j]].append(wordList[i])

        visited = set()
        queue = deque([beginWord])
        transformations = 1

        while queue:
            size = len(queue)
            for _ in range(size):
                word = queue.popleft()
                if word == endWord:
                    return transformations
                for neighbor in graph[word]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)

            transformations += 1

        return 0
