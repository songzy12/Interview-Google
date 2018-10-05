class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return -1

        dist = [[[] for i in range(len(grid[0]))] for j in range(len(grid))]
        not_valid = set()

        def bfs(i, j, dist):
            temp = [[-1 for _i in range(len(grid[0]))]
                    for _j in range(len(grid))]
            queue = [(i, j, 0)]  # NOTE: do not mess up the variables
            visited = set((i, j))
            while queue:
                x, y, s = queue.pop(0)
                temp[x][y] = s

                for dx, dy in [[0, -1], [0, 1], [1, 0], [-1, 0]]:
                    x_, y_ = x + dx, y + dy
                    if (x_, y_) not in visited and \
                            0 <= x_ < len(grid) and \
                            0 <= y_ < len(grid[0]) and\
                            grid[x_][y_] == 0:
                        visited.add((x_, y_))
                        queue.append((x_, y_, s + 1))
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if temp[i][j] == -1:
                        not_valid.add((i, j))
                    else:
                        dist[i][j].append(temp[i][j])

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    bfs(i, j, dist)

        # print(dist)
        res = -1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0 and (i, j) not in not_valid:
                    temp = sum(dist[i][j])
                    if res == -1 or temp < res:
                        res = temp

        return res


grid = [[1, 0, 2, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]]
print(Solution().shortestDistance(grid))
# for each building, compute for each cell the distance
# then for each cell, add up the distances for all the buildings
