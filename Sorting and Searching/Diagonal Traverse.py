class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        def get_next(i, j, dir, n, m):
            if dir == 1:
                next_i = i - 1
                next_j = j + 1
                if next_i < 0:
                    next_i = i
                    next_j = j + 1
                    dir = -1
                if next_j == m:
                    next_i = i + 1
                    next_j = j
                    dir = -1
            else:
                next_i = i + 1
                next_j = j - 1
                if next_i == n:
                    next_i = i
                    next_j = j + 1
                    dir = 1
                if next_j < 0:
                    next_i = i + 1
                    next_j = j
                    dir = 1
            return next_i, next_j, dir
        if not matrix:
            return matrix
        res = []
        i, j, dir, n, m = 0, 0, 1, len(matrix), len(matrix[0])
        while (i, j) != (n-1, m-1):
            res.append(matrix[i][j])
            i, j, dir = get_next(i, j, dir, n, m)
        res.append(matrix[i][j])
        return res
        

