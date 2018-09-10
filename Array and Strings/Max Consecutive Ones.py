# https://leetcode.com/explore/interview/card/google/59/array-and-strings/454/

class Solution:
	def findMaxConsecutiveOnes(self, nums):
		res = 0
		cur = 0
		for num in nums:
			if not num:
				res = max(res, cur)
				cur = 0
			else:
				cur += 1
		res = max(res, cur)
		return res
