# https://leetcode.com/explore/interview/card/google/59/array-and-strings/449/

class Solution:
	def intersection(self, nums1, nums2):
		m = set()
		for num in nums1:
			m.add(num)
		res = []
		for num in nums2:
			if num in m:
				res.append(num)
				m.remove(num) # NOTE: remove rather than pop
		return res
	
