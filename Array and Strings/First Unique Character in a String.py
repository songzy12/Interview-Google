# https://leetcode.com/explore/interview/card/google/59/array-and-strings/459/
class Solution:
	def firstUniqChar(self, s):
		appeared = set()
		repeated = set()
		for c in s:
			if c in appeared:
				repeated.add(c)
			else:
				appeared.add(c)
		for i, c in enumerate(s):
			if c not in repeated:
				return i
		return -1
		
