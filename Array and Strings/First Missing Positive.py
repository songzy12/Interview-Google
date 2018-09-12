# https://leetcode.com/explore/interview/card/google/59/array-and-strings/457/
class Solution:
	def firstMissingPositive(self, nums):
		visited = set()
		for num in nums:
			visited.add(num)
		i = 1
		while True:
			if i not in visited:
				return i
			i += 1
