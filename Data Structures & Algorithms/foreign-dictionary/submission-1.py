class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = defaultdict(set)
        indegree = {}
        for word in words:
            for c in word:
                indegree[c] = 0

        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]

            if len(w1) > len(w2) and w1.startswith(w2):
                return ""

            for j in range(min(len(w1), len(w2))):
                if w1[j] != w2[j]:
                    if w2[j] not in graph[w1[j]]:
                        graph[w1[j]].add(w2[j])
                        indegree[w2[j]] += 1
                    break

        queue = deque()
        for ch in indegree:
            if indegree[ch] == 0:
                queue.append(ch)
        ans = []

        while queue:
            ch = queue.popleft()
            ans.append(ch)
            for neighbor in graph[ch]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        if len(ans) != len(indegree):
            return ""

        return "".join(ans)
