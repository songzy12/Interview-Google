# https://leetcode.com/explore/interview/card/google/59/array-and-strings/442/

class Solution:
    def imageSmoother(self, M):
        if not M:
            return []
        res = [[0 for i in range(len(M[0]))] for j in range(len(M))]
        def update(i, j):
            cnt = 0
            sum = 0
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    x = i + dx
                    y = j + dy
                    if x < 0 or x >= len(M) or y < 0 or y >= len(M[0]):
                        continue

                    cnt += 1
                    sum += M[x][y]
            # NOTE: take care of variable names
            # NOTE: take care of / and //
            return sum / cnt 
        for i in range(len(M)):
            for j in range(len(M[0])):
                res[i][j] = update(i, j)
        return res
