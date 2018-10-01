class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.grid = [[0 for i in range(n+1)] for j in range(n+1)]
        self.left = [[[0 for i in range(n+1)]
                      for j in range(n+1)] for t in range(3)]
        self.right = [[[0 for i in range(n+1)]
                       for j in range(n+1)] for t in range(3)]
        self.up = [[[0 for i in range(n+1)]
                    for j in range(n+1)] for t in range(3)]
        self.down = [[[0 for i in range(n+1)]
                      for j in range(n+1)] for t in range(3)]

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        self.grid[row][col] = player

        def check_diag(player, dir):
            if dir == 1:
                for i in range(len(self.grid) - 1):
                    if self.grid[i][i] != player:
                        return False
                return True
            for i in range(len(self.grid) - 1):
                if self.grid[i][len(self.grid)-2-i] != player:
                    return False
            return True
        if row == col and check_diag(player, 1):
            return player
        if row + col == len(self.grid) - 2 and check_diag(player, -1):
            return player
        i, j = row, col
        
        if self.left[player][i][j-1] + self.right[player][i][j+1] + 1 == len(self.grid) - 1:
            return player
        if self.up[player][i-1][j] + self.down[player][i+1][j] + 1 == len(self.grid) - 1:
            return player
       
        left_ = right_ = j
        if self.grid[i][j-1] == player:
            left_ = j - self.left[player][i][j-1]
        if self.grid[i][j+1] == player:
            right_ = j + self.right[player][i][j+1]

        self.right[player][i][left_] = right_ - left_ + 1
        self.left[player][i][right_] = right_ - left_ + 1

        up_ = down_ = i
        if self.grid[i-1][j] == player:
            up_ = i - self.up[player][i-1][j]
        if self.grid[i+1][j] == player:
            down_ = i + self.down[player][i+1][j]
        self.up[player][down_][j] = down_ - up_ + 1
        self.down[player][up_][j] = down_ - up_ + 1
        return 0

# Your TicTacToe object will be instantiated and called as such:


moves = [[1,2,2],[3,0,1],[2,2,2],[1,0,1],[2,1,2],[4,4,1],[0,3,2],[0,0,1],[0,1,2],[2,3,1],[1,1,2],[2,4,1],[4,0,2],[3,4,1],[0,2,2],[1,3,1],[3,1,2],[4,1,1],[2,0,2],[3,3,1],[4,2,2],[4,3,1],[3,2,2]]
obj = TicTacToe(5)
for row, col, player in moves:
    temp = obj.move(row,col,player)

    # for row in obj.grid:
    #     print(row)    

    print(temp)
