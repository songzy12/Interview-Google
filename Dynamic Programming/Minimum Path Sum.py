class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dp = {}
        def get_dp(i, j):
            if i == len(grid) - 1 and j == len(grid[0]) - 1:
                return grid[i][j]
            if i == len(grid) or j == len(grid[0]):
                return 1<<32
            if (i, j) in dp:
                return dp[i, j]
            dp[i, j] = grid[i][j] + min(get_dp(i+1,j), get_dp(i, j+1))
            return dp[i, j]
        return get_dp(0, 0)