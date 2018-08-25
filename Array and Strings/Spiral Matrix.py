class Solution:

    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []

        res = []
        cnt = 0
        n_row = len(matrix)
        n_col = len(matrix[0])

        cur = [0, 0]
        d = [0, 1]

        cur_right = n_col
        cur_bottom = n_row
        cur_left = -1
        cur_up = 0

        while cnt < n_row * n_col:
            cnt += 1
            res.append(matrix[cur[0]][cur[1]])

            def next_cur(cur, d, cur_right, cur_left, cur_up, cur_bottom):
                temp = [cur[i] + d[i] for i in [0, 1]]
                if d == [0, 1] and temp[1] == cur_right:
                    cur_right -= 1
                    temp[0] += 1
                    temp[1] -= 1
                    d = [1, 0]
                elif d == [1, 0] and temp[0] == cur_bottom:
                    cur_bottom -= 1
                    temp[0] -= 1
                    temp[1] -= 1
                    d = [0, -1]
                elif d == [0, -1] and temp[1] == cur_left:
                    cur_left += 1
                    temp[0] -= 1
                    temp[1] += 1
                    d = [-1, 0]
                elif d == [-1, 0] and temp[0] == cur_up:
                    cur_up += 1
                    temp[0] += 1
                    temp[1] += 1
                    d = [0, 1]

                return d, temp, cur_right, cur_left, cur_up, cur_bottom

            d, cur, cur_right, cur_left, cur_up, cur_bottom = next_cur(cur, d, cur_right, cur_left, cur_up, cur_bottom)

        return res

matrix = [[1, 2, 3, 4], 
          [5, 6, 7, 8], 
          [9, 10, 11, 12], 
          [13, 14, 15, 16]]
print(Solution().spiralOrder(matrix))

# 一方面是函数传参
# 另一方面是把改变后的参数传回来

# 就是局部变量的作用域
# 和按值传参对原值的影响
