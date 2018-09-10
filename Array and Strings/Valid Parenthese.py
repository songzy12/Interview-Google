# https://leetcode.com/explore/interview/card/google/59/array-and-strings/467/

class Solution:
	def isValid(self, s):
		stack = []
		m = {'[': ']', '{': '}', '(': ')'}
		for c in s:
			if c in '([{':
				stack.append(c)
			else:
				if not stack:
					return False
				if m[stack[-1]] != c:
					return False
				stack.pop(-1)
		return not stack 
