# https://leetcode.com/explore/interview/card/google/59/array-and-strings/464/
class Solution:
	def removeDuplicates(self, nums):
		head = 0
		cur = 0
		while cur < len(nums):
			nums[head] = nums[cur]
            # NOTE: while cur + 1 < len(nums)
			while cur + 1 < len(nums) and nums[cur + 1] == nums[cur]:
				cur += 1
			cur += 1
			head += 1
		return head
