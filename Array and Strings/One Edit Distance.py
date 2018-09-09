# https://leetcode.com/explore/interview/card/google/59/array-and-strings/398/
class Solution:
	def isOneEditDistance(self, s, t):
		for i in range(min(len(s), len(t))): # NOTE: find the shorter string
			if s[i] == t[i]:
				continue
			else:
				if s[i+1:] == t[i:] or s[i:] == t[i+1:] or s[i+1:] == t[i+1:]:
					return True
				else:
					return False
		return abs(len(t) - len(s)) == 1 # NOTE: rather than <=
		
