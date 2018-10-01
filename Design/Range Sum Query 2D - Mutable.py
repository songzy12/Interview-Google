# https://leetcode.com/explore/interview/card/google/65/design-4/477/
class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """

        if not matrix or not matrix[0]:
            self.BIT = matrix
            return

        self.BIT = [[0 for i in range(len(matrix[0]) + 1)]
                    for j in range(len(matrix) + 1)]

        self.matrix = [[0 for i in range(len(matrix[0]) + 1)]
                       for j in range(len(matrix)+1)] # NOTE: before init, set this to 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self.update(i, j, matrix[i][j])

        self.matrix = matrix

    def update(self, row, col, val):
        """
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        delta = val - self.matrix[row][col]
        # print('delta', delta)
        x = row + 1
        while x < len(self.BIT):
            y = col + 1
            while y < len(self.BIT[0]):
                self.BIT[x][y] += delta
                y += y & -y
            x += x & -x

        self.matrix[row][col] = val  # NOTE: compute the delta

    def _sumRegion(self, row, col):
        res = 0

        x = row
        while x:
            y = col
            while y:
                res += self.BIT[x][y]
                y -= y & -y
            x -= x & -x
        return res

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self._sumRegion(row2 + 1, col2 + 1) - self._sumRegion(row1, col2 + 1) - self._sumRegion(row2 + 1, col1) + self._sumRegion(row1, col1)


# Your NumMatrix object will be instantiated and called as such:
matrix = [[1]]
obj = NumMatrix(matrix)
row1, col1, row2, col2 = [0, 0, 0, 0]
print(obj.sumRegion(row1, col1, row2, col2))
row, col, val = 0, 0, -1
obj.update(row, col, val)
row1, col1, row2, col2 = [0, 0, 0, 0]
print(obj.sumRegion(row1, col1, row2, col2))

# really, I do not konw how to do this.
# Segment Tree and Binary Index Tree

# Reference：
# https://www.topcoder.com/community/competitive-programming/tutorials/binary-indexed-trees/#2d
