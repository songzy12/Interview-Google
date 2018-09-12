# https://leetcode.com/explore/interview/card/google/59/array-and-strings/465/
class Solution:
	def shortestPalindrome(self, s):
		if not s: # NOTE: remeber to check this
			return ""
		def check(s, i):
			head = 0
			tail = i
			while head < tail:
				if s[head] != s[tail]:
					return False
				head += 1 # NOTE: do not forget this
				tail -= 1
			return True
		for i in range(len(s) - 1, -1, -1):
			if check(s, i):
				return s[i+1:][::-1] + s

# TLE		
