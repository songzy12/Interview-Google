class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        from collections import defaultdict
        cnt = defaultdict(int)
        if not matrix:
            return []

        def bfs(queue):
            print(queue)
            visited = set(queue)
            while queue:
                x, y = queue.pop(0)
                cnt[x, y] += 1
                for dx, dy in [[0, 1], [0, -1], [-1, 0], [1, 0]]:
                    x_, y_ = x + dx, y + dy
                    if 0 <= x_ < len(matrix) and 0 <= y_ < len(matrix[0]) and \
                            matrix[x_][y_] >= matrix[x][y] and (x_, y_) not in visited:
                        visited.add((x_, y_))
                        queue.append((x_, y_))

        queue = [(0, i) for i in range(len(matrix[0]))] + \
                [(i, 0) for i in range(1, len(matrix))]

        bfs(queue)

        queue = [(len(matrix) - 1, i) for i in range(len(matrix[0]))] + \
                [(i, len(matrix[0]) - 1) for i in range(len(matrix) - 1)]
        bfs(queue)

        res = []
        for k in cnt:
            if  cnt[k] == 2:
                res.append(k)
        return res