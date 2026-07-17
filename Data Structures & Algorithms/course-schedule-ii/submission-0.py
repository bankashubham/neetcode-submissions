class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        indegree = [0] * numCourses
        order = []
        queue = deque()

        for course, prereq in prerequisites:
            adj[prereq].append(course)
            indegree[course] += 1

        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)

        while queue:
            node = queue.popleft()
            order.append(node)

            for nei in adj[node]:
                indegree[nei] -= 1

                if indegree[nei] == 0:
                    queue.append(nei)

        if len(order) == numCourses:
            return order

        return []