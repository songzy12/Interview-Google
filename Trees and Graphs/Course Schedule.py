class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        degree = [0 for i in range(numCourses)]
        from collections import defaultdict
        sons = defaultdict(set)
        for u, v in prerequisites:
            degree[v] += 1
            sons[u].add(v)
        queue = []
        for i in range(numCourses):
            if degree[i] == 0:
                queue.append(i)
        visited = set([])

        while queue:
            cur = queue.pop()
            visited.add(cur)
            for t in sons[cur]:
                degree[t] -= 1
                if degree[t] == 0:
                    queue.append(t)
        return len(visited) == numCourses

