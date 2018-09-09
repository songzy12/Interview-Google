# https://leetcode.com/explore/interview/card/google/59/array-and-strings/346/

class Solution:
	def gameOfLife(self, board):
		def get_count(i, j):
			cnt = 0
			for dx in [-1, 0, 1]:
				for dy in [-1, 0, 1]:
					if not dx and not dy:
						continue
					x = dx + i
					y = dy + j
					if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]):
						continue
					if board[x][y] & 1:
						cnt += 1
			return cnt
			
		def update(i, j):
			cnt = get_count(i, j)				
		
			next_state = 0
			if board[i][j] & 1: # live
				if cnt in [2, 3]:
					next_state = 1
			else: # dead
				if cnt == 3:
					next_state = 1
			board[i][j] = board[i][j] | (next_state << 1)
		for i in range(len(board)):
			for j in range(len(board[i])):
				update(i, j)
		for i in range(len(board)):
			for j in range(len(board[i])):
				board[i][j] = board[i][j] >> 1
		


