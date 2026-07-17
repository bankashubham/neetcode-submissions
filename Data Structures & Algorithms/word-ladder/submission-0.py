class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        patternMap = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                patternMap[pattern].append(word)

        queue = deque([(beginWord, 1)])
        visited = {beginWord}

        while queue:
            word, length = queue.popleft()
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                for neighbor in patternMap[pattern]:
                    if neighbor == endWord:
                        return length + 1 
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, length + 1))
                patternMap[pattern] = []

        return 0
                    
